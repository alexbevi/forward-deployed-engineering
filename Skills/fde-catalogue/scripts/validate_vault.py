"""Validate local FDE records and Base coverage; does not run Obsidian."""
from __future__ import annotations

import argparse
import hashlib
from collections import Counter
from datetime import date
from pathlib import Path
import re

import yaml


def validate(root: Path) -> int:
    root = root.resolve()
    errors: list[str] = []
    records: dict[str, tuple[dict, str]] = {}
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if rel.parts[0] == "Skills" or any(part.startswith(".") for part in rel.parts):
            continue
        text = path.read_text()
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not match:
            if rel.parts[0] in {"Articles", "Themes", "Operating models", "Playbooks", "People", "Resources", "Attachments", "Approaches"}:
                errors.append(f"{rel}: missing frontmatter")
            continue
        try:
            meta = yaml.safe_load(match[1])
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        if not isinstance(meta, dict) or meta.get("collection") != "fde":
            errors.append(f"{rel}: missing collection: fde")
            continue
        records[rel.with_suffix("").as_posix()] = (meta, text)

    required = {
        "article": {"title", "author", "site", "url", "canonical_url", "publication_date", "publication_date_basis", "accessed", "source_kind", "themes", "evidence_family", "evidence_basis", "contribution"},
        "operating-model": {"mandate", "engagement_type", "ownership", "success_measure", "evidence_status", "sources"},
        "approach": {"purpose", "mechanism", "application_scope", "evidence_status", "application_status", "sources", "local_observations"},
        "playbook": {"purpose", "practice_status", "sources", "local_observations"},
        "person": {"person_name", "relevance", "public_url", "sources"},
        "resource": {"resource_kind", "purpose", "url", "sources"},
        "attachment-text": {"sources", "attachment", "source_url", "sha256", "byte_size", "page_count", "downloaded", "indexed", "extraction_method", "extraction_status", "pages_with_text"},
        "theme": set(), "index": set(), "synthesis": set(),
    }
    identities: dict[str, str] = {}
    dates = {"created", "updated", "publication_date", "source_updated", "accessed", "last_verified", "downloaded", "indexed", "landing_publication_date", "landing_updated"}
    typed_links = {"sources": "article", "themes": "theme", "models": "operating-model", "playbooks": "playbook", "people": "person", "resources": "resource", "text_indexes": "attachment-text", "approaches": "approach"}

    def resolve(target: str, caller: str) -> str | None:
        destination = target.split("|", 1)[0]
        name, _, anchor = destination.partition("#")
        if not name:
            name = caller
        if name.endswith(".pdf"):
            path = (root / name).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                errors.append(f"{caller}: missing PDF {name}")
            elif anchor:
                index = records.get(name.removesuffix(".pdf"))
                match = re.fullmatch(r"page=([1-9][0-9]*)", anchor)
                if not match or not index or int(match[1]) > index[0].get("page_count", 0):
                    errors.append(f"{caller}: invalid PDF page reference {destination}")
            return None
        if name.endswith(".base"):
            if not (root / name).is_file():
                errors.append(f"{caller}: missing Base {name}")
            return None
        name = name.removesuffix(".md")
        if name not in records:
            errors.append(f"{caller}: unresolved local wikilink {destination}")
            return None
        if anchor and not anchor.startswith("^"):
            headings = re.findall(r"^#+\s+(.+)$", records[name][1], re.M)
            if anchor not in headings:
                errors.append(f"{caller}: missing heading {destination}")
        return name

    for name, (meta, text) in records.items():
        kind = meta.get("type")
        if kind not in required:
            errors.append(f"{name}: unsupported type {kind}")
            continue
        for key in required[kind] | {"type", "status", "created", "updated", "tags"}:
            if key not in meta:
                errors.append(f"{name}: missing {key}")
        for key in dates & meta.keys():
            value = meta[key]
            if value is not None and not isinstance(value, date):
                try:
                    date.fromisoformat(str(value))
                except ValueError:
                    errors.append(f"{name}: invalid ISO date in {key}")
        tags = meta.get("tags")
        if not isinstance(tags, list) or any(not isinstance(t, str) or t.startswith("#") for t in tags):
            errors.append(f"{name}: tags must be plain string list")
        # Extracted text and examples in literal fences are not Obsidian links.
        link_text = re.sub(r"(?ms)^(`{3,})[^\n]*\n.*?^\1[ \t]*$", "", text)
        for target in re.findall(r"\[\[([^\]]+)\]\]", link_text):
            resolve(target, name)
        for prop, expected in typed_links.items():
            if prop not in meta:
                continue
            links = meta[prop]
            if not isinstance(links, list):
                errors.append(f"{name}: {prop} must be a list")
                continue
            for target in links:
                if not isinstance(target, str) or not target.startswith("[[") or not target.endswith("]]"):
                    errors.append(f"{name}: {prop} needs quoted wikilinks")
                    continue
                linked = resolve(target[2:-2], name)
                if linked and records[linked][0].get("type") != expected:
                    errors.append(f"{name}: {prop} links to incorrect type: {linked}")
        if kind == "article":
            for prop in ["author", "evidence_basis"]:
                if not isinstance(meta.get(prop), list):
                    errors.append(f"{name}: {prop} must be a list")
            for url in set(filter(None, [meta.get("url"), meta.get("canonical_url"), meta.get("primary_source_url")])):
                if url in identities:
                    errors.append(f"Duplicate source identity: {name} and {identities[url]}")
                identities[url] = name
            if not meta.get("themes"):
                errors.append(f"{name}: missing theme membership")
            for target in meta.get("themes", []):
                linked = resolve(target[2:-2], name)
                if linked and name not in records[linked][1]:
                    errors.append(f"{name}: absent from theme catalogue {linked}")
        if kind in {"operating-model", "playbook", "person", "attachment-text", "approach"} and not meta.get("sources"):
            errors.append(f"{name}: needs source evidence")
        if "attachments" in meta:
            links = meta["attachments"]
            if not isinstance(links, list) or any(not isinstance(t, str) or not re.fullmatch(r"\[\[Attachments/[^\]#]+\.pdf\]\]", t) for t in links):
                errors.append(f"{name}: attachments must be PDF wikilink list")
        if kind == "article" and meta.get("source_format") == "pdf":
            if not all(meta.get(k) for k in ["primary_source_url", "attachments", "text_indexes"]):
                errors.append(f"{name}: PDF source needs artifact URL, attachment and text index")
        if kind == "attachment-text":
            target = meta.get("attachment", "")
            if not isinstance(target, str) or not re.fullmatch(r"\[\[Attachments/[^\]#]+\.pdf\]\]", target):
                errors.append(f"{name}: invalid attachment link")
            else:
                path = root / target[2:-2]
                if path.is_file():
                    data = path.read_bytes()
                    if not data.startswith(b"%PDF-") or len(data) != meta.get("byte_size") or hashlib.sha256(data).hexdigest() != meta.get("sha256"):
                        errors.append(f"{name}: PDF header, size or SHA-256 mismatch")
            pages = meta.get("page_count")
            count = meta.get("pages_with_text")
            if not isinstance(pages, int) or pages < 1 or not isinstance(count, int) or not 0 <= count <= pages:
                errors.append(f"{name}: invalid page counts")
            else:
                headings = re.findall(r"^## Page ([0-9]+)$", link_text, re.M)
                if headings != [str(n) for n in range(1, pages + 1)]:
                    errors.append(f"{name}: text index page sections do not match page count")
                expected = "text-extracted" if count == pages else "partial-needs-review"
                if meta.get("extraction_status") != expected:
                    errors.append(f"{name}: extraction status inconsistent with text coverage")
            for source in meta.get("sources", []):
                linked = resolve(source[2:-2], name)
                if linked and f"[[{name}]]" not in records[linked][0].get("text_indexes", []):
                    errors.append(f"{name}: source missing text-index backlink")
        if kind == "approach":
            if meta.get("evidence_status") not in {"source-reported", "independently-reproduced"}:
                errors.append(f"{name}: invalid approach evidence_status")
            if meta.get("application_status") not in {"proposed", "locally-tried"}:
                errors.append(f"{name}: invalid approach application_status")
            if (meta.get("application_status") == "locally-tried" or meta.get("evidence_status") == "independently-reproduced") and not meta.get("local_observations"):
                errors.append(f"{name}: observed approach status needs local observations")
        if kind == "article" and "arxiv_id" in meta:
            identifier = meta["arxiv_id"]
            version = meta.get("arxiv_version", "")
            if not isinstance(identifier, str) or not re.fullmatch(r"(?:[0-9]{4}\.[0-9]{4,5}|[a-z-]+(?:\.[A-Z]{2})?/[0-9]{7})", identifier):
                errors.append(f"{name}: invalid arxiv_id")
            if not isinstance(version, str) or not re.fullmatch(r"v[1-9][0-9]*", version):
                errors.append(f"{name}: invalid arxiv_version")
            identity = f"arxiv:{identifier}"
            if identity in identities:
                errors.append(f"Duplicate arXiv source: {name} and {identities[identity]}")
            identities[identity] = name
            expected_html = f"https://arxiv.org/html/{identifier}{version}"
            if meta.get("source_format") == "html" and meta.get("primary_source_url") != expected_html:
                errors.append(f"{name}: arXiv HTML URL must pin reviewed version")
            if meta.get("source_format") != "html" and not meta.get("html_access_gap"):
                errors.append(f"{name}: arXiv fallback needs html_access_gap")
            if meta.get("research_status") not in {"preprint", "peer-reviewed"} or "venue" not in meta:
                errors.append(f"{name}: missing research status or venue field")
            if meta.get("research_status") == "peer-reviewed" and not (meta.get("venue") and meta.get("review_status_basis")):
                errors.append(f"{name}: peer-reviewed needs verified venue and basis")
        if kind == "playbook":
            if meta.get("practice_status") not in {"proposed", "source-reported", "locally-tried"}:
                errors.append(f"{name}: invalid practice_status")
            if meta.get("practice_status") == "locally-tried" and not meta.get("local_observations"):
                errors.append(f"{name}: locally-tried needs actual observations")
        if kind == "resource":
            if meta.get("status") not in {"mentioned", "reviewed", "used"}:
                errors.append(f"{name}: invalid resource status")
            if not meta.get("sources") and not (meta.get("url") and meta.get("last_verified")):
                errors.append(f"{name}: needs source or inspected external documentation")
            if meta.get("status") == "used" and not meta.get("local_observations"):
                errors.append(f"{name}: used needs actual observations")

    counts = Counter(meta.get("type") for meta, _ in records.values())
    for name in ["Sources", "Operating models", "Approaches", "Playbooks", "People", "Resources"]:
        if not (root / "Bases" / f"{name}.base").is_file():
            errors.append(f"Missing Base: {name}")
    for path in sorted((root / "Bases").glob("*.base")):
        try:
            base = yaml.safe_load(path.read_text())
            filters = base["filters"]["and"]
            if 'file.ext == "md"' not in filters or 'note.collection == "fde"' not in filters:
                errors.append(f"{path.name}: unscoped Base")
            kinds = [re.fullmatch(r'note.type == "([a-z-]+)"', f) for f in filters if isinstance(f, str)]
            selected = [m[1] for m in kinds if m]
            if len(selected) != 1 or not counts[selected[0]]:
                errors.append(f"{path.name}: selector must cover a populated record type")
            if not base.get("views") or any(v.get("type") != "table" or not v.get("name") or not v.get("order") for v in base["views"]):
                errors.append(f"{path.name}: invalid table view structure")
            print(f"{path.name}: {counts[selected[0]] if len(selected) == 1 else 0} records selected")
        except (yaml.YAMLError, KeyError, TypeError) as exc:
            errors.append(f"{path.name}: invalid Base structure: {exc}")
    if errors:
        print("\n".join(sorted(set(errors))))
        return 1
    print(f"Validated {len(records)} content notes, relationships and Base record coverage. Obsidian rendering was not checked.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    raise SystemExit(validate(parser.parse_args().root.resolve()))
