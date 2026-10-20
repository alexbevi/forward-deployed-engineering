"""Render vault links, properties and Base views as GitHub-flavored Markdown."""

from __future__ import annotations

import json
import posixpath
import re
from urllib.parse import quote, unquote, urlsplit

WIKILINK = re.compile(r"(!?)\[\[([^\]\n]+)\]\]")
MARKDOWN_LINK = re.compile(r"(?<!!)\[([^\]\n]*)\]\(([^\s)]+)\)")


def map_prose(text: str, transform, protect_inline: bool = True) -> str:
    lines = []
    fence = ""
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            if (
                marker
                and marker[1][0] == fence[0]
                and len(marker[1]) >= len(fence)
                and not line[marker.end() :].strip()
            ):
                fence = ""
            lines.append(line)
        elif marker:
            fence = marker[1]
            lines.append(line)
        else:
            parts = re.split(r"(`+.*?`+)", line) if protect_inline else [line]
            lines.append(
                "".join(
                    part if i % 2 else transform(part) for i, part in enumerate(parts)
                )
            )
    return "".join(lines)


def slug(text: str) -> str:
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]*>|[*`~]", "", text).strip().lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def headings(body: str) -> dict[str, str]:
    result = {}
    used = set()

    def collect(text):
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", text)
        if match:
            title = match[1]
            anchor = slug(title)
            unique = anchor
            index = 0
            while unique in used:
                index += 1
                unique = f"{anchor}-{index}"
            used.add(unique)
            result.setdefault(title, unique)
        return text

    map_prose(body, collect, protect_inline=False)
    return result


def output_path(path: str) -> str:
    return path.removesuffix(".base") + ".md" if path.endswith(".base") else path


class Renderer:
    def __init__(
        self,
        records: dict,
        bases: dict,
        assets: set[str],
        excluded: set[str],
        repository: str,
    ):
        self.records = records
        self.bases = bases
        self.paths = set(records) | set(bases) | assets
        self.excluded = excluded
        self.repository = repository
        self.names = {}
        for path in self.paths:
            name = posixpath.basename(path).removesuffix(".md")
            self.names.setdefault(name, []).append(path)

    def resolve(self, target: str, caller: str) -> tuple[str, str]:
        name, _, anchor = target.partition("#")
        name = name or caller
        choices = [name, name + ".md"]
        path = next((choice for choice in choices if choice in self.paths), None)
        if path is None:
            matches = self.names.get(name.removesuffix(".md"), [])
            if len(matches) != 1:
                raise ValueError(f"{caller}: missing or ambiguous link {target}")
            path = matches[0]
        if anchor and path in self.records:
            resolved = self.records[path]["headings"].get(anchor)
            if resolved is None:
                raise ValueError(f"{caller}: missing heading {target}")
            anchor = resolved
        elif anchor and path.endswith(".pdf"):
            if not re.fullmatch(r"page=[1-9]\d*", anchor):
                raise ValueError(f"{caller}: unsupported PDF fragment {target}")
        elif anchor:
            raise ValueError(f"{caller}: unsupported link fragment {target}")
        return output_path(path), anchor

    def dependency(self, key: str, caller: str):
        if key.startswith("base:"):
            return self.bases[key[5:]]["signature"]
        if key.startswith("markdown:"):
            return self.markdown_url(key[9:], caller)
        return list(self.resolve(key, caller))

    def markdown_url(self, href: str, caller: str) -> str:
        url = urlsplit(href)
        if url.scheme or url.netloc:
            return href
        path = (
            posixpath.normpath(
                posixpath.join(posixpath.dirname(caller), unquote(url.path))
            )
            if url.path
            else caller
        )
        if path in self.excluded:
            return (
                self.repository
                + "/blob/main/"
                + quote(path, safe="/")
                + ("#" + url.fragment if url.fragment else "")
            )
        if path not in self.paths:
            raise ValueError(f"{caller}: missing Markdown link {href}")
        if (
            url.fragment
            and path in self.records
            and unquote(url.fragment) not in self.records[path]["headings"].values()
        ):
            raise ValueError(f"{caller}: missing Markdown heading {href}")
        relative = posixpath.relpath(
            output_path(path), posixpath.dirname(output_path(caller)) or "."
        )
        return (
            quote(relative, safe="/")
            + ("?" + url.query if url.query else "")
            + ("#" + url.fragment if url.fragment else "")
        )

    def link(
        self, target: str, caller: str, deps: dict, label: str | None = None
    ) -> str:
        path, anchor = self.resolve(target, caller)
        deps[target] = [path, anchor]
        relative = posixpath.relpath(
            path, posixpath.dirname(output_path(caller)) or "."
        )
        url = quote(relative, safe="/") + (
            "#" + quote(anchor, safe="=-_") if anchor else ""
        )
        label = (
            label
            or posixpath.basename(target.split("#")[0])
            .removesuffix(".md")
            .removesuffix(".base")
            or target.lstrip("#")
        )
        label = label.replace("[", "\\[").replace("]", "\\]")
        return f"[{label}]({url})"

    def prose(self, text: str, caller: str, deps: dict) -> str:
        def markdown_link(match):
            label, href = match.groups()
            url = self.markdown_url(href, caller)
            if not urlsplit(href).scheme and not urlsplit(href).netloc:
                deps["markdown:" + href] = url
            return f"[{label}]({url})"

        def replace(match):
            embed, content = match.groups()
            target, _, label = content.partition("|")
            if embed and not target.split("#")[0].endswith((".pdf", ".base")):
                raise ValueError(f"{caller}: unsupported embed {target}")
            return self.link(target, caller, deps, label)

        return map_prose(
            text,
            lambda part: WIKILINK.sub(replace, MARKDOWN_LINK.sub(markdown_link, part)),
        )

    def value(self, value, caller: str, deps: dict) -> str:
        if value is None:
            return ""
        if isinstance(value, list):
            return "; ".join(self.value(item, caller, deps) for item in value)
        if isinstance(value, dict):
            value = json.dumps(value, ensure_ascii=False)
        return (
            self.prose(str(value), caller, deps)
            .replace("|", "\\|")
            .replace("\n", "<br>")
        )

    def base(self, path: str, caller: str, deps: dict) -> str:
        parts = []
        for view in self.bases[path]["views"]:
            parts.append("## " + view["name"])
            groups = sorted(
                {row["group"] for row in view["rows"]},
                reverse=view["group"].get("direction") == "DESC",
            )
            for group in groups:
                if view["group"]:
                    parts.append("### " + (group or "Unspecified"))
                columns = view["columns"]
                table = [
                    "| " + " | ".join(c.removeprefix("note.") for c in columns) + " |",
                    "| " + " | ".join("---" for _ in columns) + " |",
                ]
                for row in view["rows"]:
                    if row["group"] == group:
                        cells = [
                            self.link(row["path"], caller, deps)
                            if column == "file.name"
                            else self.value(value, caller, deps)
                            for column, value in zip(columns, row["values"])
                        ]
                        table.append("| " + " | ".join(cells) + " |")
                parts.append("\n".join(table))
            if not groups:
                parts.append("No matching records.")
        return "\n\n".join(parts)

    def page(self, path: str, body: str) -> tuple[str, dict]:
        deps = {}
        if path in self.bases:
            deps["base:" + path] = self.bases[path]["signature"]
            text = (
                "# "
                + posixpath.basename(path).removesuffix(".base")
                + "\n\n"
                + self.base(path, path, deps)
            )
        else:
            text = self.prose(body, path, deps).rstrip()
            meta = self.records[path]["meta"]
            if meta:
                rows = ["| Property | Value |", "| --- | --- |"]
                rows.extend(
                    f"| {key} | {self.value(value, path, deps)} |"
                    for key, value in meta.items()
                )
                text += "\n\n## Record metadata\n\n" + "\n".join(rows)
        return text.rstrip() + "\n", deps
