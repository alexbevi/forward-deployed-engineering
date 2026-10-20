"""Incrementally export a committed vault snapshot as GitHub-flavored Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

import yaml
from markdown import Renderer, headings, output_path

from bases import table_views

CACHE = ".publish-cache.json"
CONTENT = {
    "Articles",
    "Themes",
    "Operating models",
    "Approaches",
    "Playbooks",
    "People",
    "Resources",
    "Attachments",
}


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(root), *args])


def digest(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, default=str).encode()
    ).hexdigest()


def content_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_files(root: Path, commit: str) -> tuple[dict[str, str], set[str]]:
    files = {}
    excluded = set()
    for entry in git(root, "ls-tree", "-rz", commit).split(b"\0"):
        if not entry:
            continue
        info, raw_path = entry.split(b"\t", 1)
        mode, _, oid = info.decode().split()
        name = raw_path.decode()
        path = PurePosixPath(name)
        selected = (
            path.suffix == ".md"
            and (len(path.parts) == 1 or path.parts[0] in CONTENT)
            or path.parts[0] == "Bases"
            and path.suffix == ".base"
            or path.parts[0] == "Attachments"
            and path.suffix == ".pdf"
        )
        if selected:
            if mode != "100644" and mode != "100755":
                raise ValueError(f"Cannot publish non-regular file: {name}")
            files[name] = oid
        else:
            excluded.add(name)
    return files, excluded


def parse_note(data: bytes) -> tuple[dict, str]:
    text = data.decode()
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        return {}, text
    meta = yaml.safe_load(match[1])
    if not isinstance(meta, dict):
        raise TypeError("Note frontmatter must be a mapping")
    return json.loads(json.dumps(meta, default=str)), text[match.end() :].lstrip("\n")


def destination(output: Path, name: str) -> Path:
    path = output / name
    if not path.resolve().is_relative_to(output) or any(
        p.is_symlink() for p in (path, *path.parents) if p != output
    ):
        raise ValueError(f"Unsafe publication path: {name}")
    return path


def write_changed(path: Path, data: bytes) -> bool:
    if path.is_file() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True


def load_cache(output: Path, fingerprint: str) -> dict:
    path = output / CACHE
    if not path.exists():
        return {}
    cache = json.loads(path.read_text())
    if cache.get("fingerprint") != fingerprint:
        print("Exporter changed; rebuilding the publication cache.")
        return {"outputs": {name: {} for name in cache.get("outputs", {})}}
    return cache


def load_records(
    root: Path, files: dict, changed: set, cache: dict
) -> tuple[dict, dict, dict]:
    records, specs, bodies = {}, {}, {}
    for path, oid in files.items():
        if path.endswith(".pdf"):
            continue
        if path not in changed:
            if path.endswith(".base"):
                specs[path] = cache["specs"][path]
            else:
                records[path] = cache["records"][path]
            continue
        data = git(root, "cat-file", "blob", oid)
        if path.endswith(".base"):
            specs[path] = yaml.safe_load(data)
        else:
            meta, body = parse_note(data)
            records[path] = {"path": path, "meta": meta, "headings": headings(body)}
            bodies[path] = body
    return records, specs, bodies


def plan_outputs(root, output, files, prior_outputs, renderer, bodies):
    outputs, rendered = {}, []
    pending = {}
    for path, oid in files.items():
        name = output_path(path)
        target = destination(output, name)
        prior = prior_outputs.get(name, {})
        source_changed = oid != prior.get("source_blob")
        existing = target.read_bytes() if target.is_file() else None
        intact = existing is not None and content_hash(existing) == prior.get("sha256")
        if path.endswith(".pdf"):
            data = (
                git(root, "cat-file", "blob", oid)
                if source_changed or not intact
                else existing
            )
            pending[name] = data
            outputs[name] = {
                "dependencies": {},
                "sha256": content_hash(data),
                "source_blob": oid,
            }
            continue
        dependencies = prior.get("dependencies", {})
        invalid = (
            source_changed
            or not intact
            or any(
                renderer.dependency(key, path) != value
                for key, value in dependencies.items()
            )
        )
        if invalid:
            if path in renderer.records and path not in bodies:
                _, bodies[path] = parse_note(git(root, "cat-file", "blob", oid))
            text, dependencies = renderer.page(path, bodies.get(path, ""))
            rendered.append(name)
            pending[name] = text.encode()
        outputs[name] = {
            "dependencies": dependencies,
            "source_blob": oid,
            "sha256": content_hash(pending[name]) if invalid else prior["sha256"],
        }
    return outputs, pending, rendered


def export(root: Path, output: Path, commit: str, repository: str) -> dict:
    root, output = root.resolve(), output.resolve()
    if output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError("Publication output must be outside the source checkout")
    commit = git(root, "rev-parse", "--verify", commit + "^{commit}").decode().strip()
    fingerprint = digest(
        {p.name: p.read_text() for p in sorted(Path(__file__).parent.glob("*.py"))}
    )
    cache = load_cache(output, fingerprint)
    files, excluded = source_files(root, commit)
    if "PUBLICATION.md" in files:
        raise ValueError("PUBLICATION.md is reserved for generated source provenance")
    previous = cache.get("source_commit")
    if previous:
        changed = set(
            git(root, "diff", "--name-only", "-z", previous, commit, "--")
            .decode()
            .split("\0")
        )
    else:
        changed = set(files)
    records, specs, bodies = load_records(root, files, changed, cache)
    bases = {}
    for path, spec in specs.items():
        views = table_views(spec, list(records.values()))
        bases[path] = {"views": views, "signature": digest(views)}
    renderer = Renderer(
        records, bases, {p for p in files if p.endswith(".pdf")}, excluded, repository
    )
    prior_outputs = cache.get("outputs", {})
    outputs, pending, rendered = plan_outputs(
        root, output, files, prior_outputs, renderer, bodies
    )
    written, copied = [], []
    removed = sorted(set(prior_outputs) - set(outputs))
    removed_paths = [destination(output, name) for name in removed]
    for name, data in pending.items():
        if write_changed(destination(output, name), data):
            (copied if name.endswith(".pdf") else written).append(name)
    for path in removed_paths:
        path.unlink(missing_ok=True)
    publication = (
        "# Publication\n\n"
        f"Generated from [source commit `{commit[:12]}`]({repository}/commit/{commit}).\n\n"
        f"Edit the [Obsidian source]({repository}/tree/main); this branch is generated.\n"
    )
    write_changed(output / "PUBLICATION.md", publication.encode())
    state = {
        "fingerprint": fingerprint,
        "source_commit": commit,
        "records": records,
        "specs": specs,
        "outputs": outputs,
    }
    write_changed(
        output / CACHE,
        (json.dumps(state, indent=2, ensure_ascii=False) + "\n").encode(),
    )
    return {
        "source_commit": commit,
        "previous_commit": previous,
        "rendered": rendered,
        "written": written,
        "copied": copied,
        "removed": removed,
        "reused": len(outputs) - len(rendered) - len(copied),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[2]
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--commit", default="HEAD")
    parser.add_argument(
        "--repository", required=True, help="HTTPS URL of the source repository"
    )
    args = parser.parse_args()
    print(
        json.dumps(
            export(args.root, args.output, args.commit, args.repository), indent=2
        )
    )


if __name__ == "__main__":
    main()
