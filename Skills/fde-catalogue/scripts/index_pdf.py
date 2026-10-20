"""Retain a PDF and create an immutable, page-numbered Markdown search copy."""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

import pymupdf
import yaml


class PlainDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def index_pdf(root: Path, source: str, url: str, prefix: str, downloaded: str,
              local_file: Path | None = None, max_bytes: int = 80 * 1024 * 1024) -> dict:
    root = root.resolve()
    date.fromisoformat(downloaded)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", prefix):
        raise ValueError("prefix must be a lowercase filename slug")
    source = source.removesuffix(".md")
    source_path = (root / (source + ".md")).resolve()
    if not source_path.is_relative_to(root) or not source_path.is_file():
        raise ValueError("source must identify an existing local source note")
    resolved_url = url
    if local_file:
        if local_file.stat().st_size > max_bytes:
            raise ValueError("PDF exceeds the download limit")
        data = local_file.read_bytes()
    else:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=40) as response:
            resolved_url = response.url
            data = response.read(max_bytes + 1)
        if len(data) > max_bytes:
            raise ValueError("PDF exceeds the download limit")
    if not data.startswith(b"%PDF-"):
        raise ValueError("Response is not a PDF; it may be a login page")
    sha = hashlib.sha256(data).hexdigest()
    folder = root / "Attachments"
    folder.mkdir(exist_ok=True)
    # Reuse identical bytes even if requested through a different URL or prefix.
    matches = [p for p in folder.glob("*.pdf")
               if p.stat().st_size == len(data) and hashlib.sha256(p.read_bytes()).hexdigest() == sha]
    pdf = matches[0] if matches else folder / f"{prefix}-{sha[:12]}.pdf"
    if pdf.exists() and hashlib.sha256(pdf.read_bytes()).hexdigest() != sha:
        raise ValueError("Content-addressed filename collision; existing PDF was preserved")
    with pymupdf.open(stream=data, filetype="pdf") as document:
        if document.needs_pass:
            raise ValueError("PDF needs a password; do not claim text extraction succeeded")
        pages = [page.get_text(sort=True) for page in document]
    if not pdf.exists():
        pdf.write_bytes(data)
    index = pdf.with_suffix(".md")
    nonempty = sum(bool(text.strip()) for text in pages)
    status = "text-extracted" if nonempty == len(pages) else "partial-needs-review"
    if index.exists():
        match = re.match(r"^---\n(.*?)\n---\n", index.read_text(), re.S)
        metadata = yaml.safe_load(match[1]) if match else {}
        if metadata.get("sha256") != sha or metadata.get("page_count") != len(pages):
            raise ValueError("Existing text index has inconsistent provenance; it was preserved")
        status = metadata.get("extraction_status")
    else:
        relpdf = pdf.relative_to(root).as_posix()
        metadata = {
            "type": "attachment-text", "collection": "fde", "status": "derived",
            "created": downloaded, "updated": downloaded, "tags": ["fde", "fde/attachment"],
            "sources": [f"[[{source}]]"], "attachment": f"[[{relpdf}]]",
            "source_url": url, "resolved_url": resolved_url, "sha256": sha,
            "byte_size": len(data), "page_count": len(pages),
            "downloaded": downloaded, "indexed": downloaded,
            "extraction_method": f"PyMuPDF {pymupdf.VersionBind}; sorted embedded text; no OCR",
            "extraction_status": status, "pages_with_text": nonempty,
        }
        body = [f"# PDF text index: {prefix}", "",
                f"Primary record: [[{source}]]. Original: [[{relpdf}]].", "",
                "Machine extraction for local search, not a second independent source. Layout, "
                "reading order, glyphs and diagrams may be inaccurate even on pages with text. "
                "Consult the PDF for authoritative wording. PDF page numbers are used below.", ""]
        for number, text in enumerate(pages, 1):
            # Literal fences keep extracted markup and instructions inert.
            runs = [len(s) for s in re.findall(r"`+", text)]
            fence = "`" * max(3, max(runs, default=0) + 1)
            body += [f"## Page {number}", "", f"[[{relpdf}#page={number}|Open PDF page {number}]]", "",
                     fence + "text", text.rstrip() or "[No embedded text extracted; page needs review.]", fence, ""]
        index.write_text("---\n" + yaml.dump(metadata, Dumper=PlainDumper, sort_keys=False,
                                           allow_unicode=True, width=120) + "---\n\n" + "\n".join(body))
    return {"attachment": pdf.relative_to(root).as_posix(),
            "text_index": index.relative_to(root).as_posix(), "sha256": sha,
            "byte_size": len(data), "page_count": len(pages),
            "pages_with_text": nonempty, "extraction_status": status}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--source", required=True, help="Source note path relative to FDE folder")
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--downloaded", default=date.today().isoformat())
    parser.add_argument("--local-file", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    print(json.dumps(index_pdf(args.root.resolve(), args.source, args.url, args.prefix,
                               args.downloaded, args.local_file), indent=2))
