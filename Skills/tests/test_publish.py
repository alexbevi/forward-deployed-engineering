"""Exercise committed snapshots, dependency invalidation and Markdown conversion."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PUBLISH = Path(__file__).resolve().parents[1] / "publish"
sys.path.insert(0, str(PUBLISH))
SPEC = importlib.util.spec_from_file_location("publish_export", PUBLISH / "export.py")
EXPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPORT)


class PublishTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "source"
        self.root.mkdir()
        self.output = self.base / "published"
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        self.write(
            "README.md",
            "# Index\n\n[[Articles/One#Details|Read one]]\n\n![[Bases/Sources.base]]\n",
        )
        self.write(
            "Articles/One.md",
            "---\ncollection: fde\ntype: article\nstatus: reviewed\nfamily: alpha\n---\n# One\n\n## Details\n\nOriginal text.\n",
        )
        self.write(
            "Resources/Tool.md", "---\ncollection: fde\ntype: resource\n---\n# Tool\n"
        )
        self.write(
            "Bases/Sources.base",
            """filters:
  and:
    - file.ext == "md"
    - note.collection == "fde"
    - note.type == "article"
views:
  - type: table
    name: All sources
    order: [file.name, note.status]
  - type: table
    name: By family
    groupBy: {property: family, direction: ASC}
    order: [file.name, status]
  - type: table
    name: Missing status
    filters: status == null
    order: [file.name]
""",
        )
        self.write(
            "Bases/Resources.base",
            """filters: note.type == "resource"
views:
  - type: table
    name: All resources
    order: [file.name]
""",
        )
        self.write("Attachments/test.pdf", b"%PDF-fixture")
        self.commit()

    def git(self, *args):
        return (
            subprocess.check_output(
                ["git", "-C", str(self.root), *args], stderr=subprocess.PIPE
            )
            .decode()
            .strip()
        )

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text if isinstance(text, bytes) else text.encode())

    def commit(self):
        self.git("add", "--all")
        return self.git(
            "-c", "commit.gpgsign=false", "commit", "-m", "docs: update fixture"
        )

    def export(self, output=None, commit="HEAD"):
        return EXPORT.export(
            self.root, output or self.output, commit, "https://github.com/example/vault"
        )

    def assert_matches_fresh(self):
        fresh = self.base / "fresh"
        self.export(fresh)
        cached = {
            p.relative_to(self.output): p.read_bytes()
            for p in self.output.rglob("*")
            if p.is_file()
        }
        rebuilt = {
            p.relative_to(fresh): p.read_bytes()
            for p in fresh.rglob("*")
            if p.is_file()
        }
        self.assertEqual(cached, rebuilt)

    def test_noop_does_not_load_or_render_notes_and_preserves_mtime(self):
        self.export()
        path = self.output / "Articles/One.md"
        timestamp = path.stat().st_mtime_ns
        with patch.object(
            EXPORT, "parse_note", side_effect=AssertionError("Unchanged note parsed")
        ):
            result = self.export()
        self.assertEqual(result["rendered"], [])
        self.assertEqual(result["copied"], [])
        self.assertEqual(path.stat().st_mtime_ns, timestamp)

    def test_body_edit_rebuilds_only_changed_page(self):
        self.export()
        path = self.root / "Articles/One.md"
        self.write(
            "Articles/One.md", path.read_text().replace("Original text.", "New text.")
        )
        self.commit()
        result = self.export()
        self.assertEqual(result["rendered"], ["Articles/One.md"])
        self.assert_matches_fresh()

    def test_agentic_sources_publish_in_their_own_inventory(self):
        self.write("Articles/Agentic.md", "---\ncollection: agentic-development\ntype: article\n---\n# Agentic\n")
        self.write("Bases/Agentic sources.base", '''filters:
  and:
    - file.ext == "md"
    - note.collection == "agentic-development"
    - note.type == "article"
views:
  - type: table
    name: Agentic sources
    order: [file.name]
''')
        self.commit()
        self.export()
        agentic = (self.output / "Bases/Agentic sources.md").read_text()
        role = (self.output / "Bases/Sources.md").read_text()
        self.assertIn("[Agentic](../Articles/Agentic.md)", agentic)
        self.assertNotIn("Articles/One.md", agentic)
        self.assertIn("[One](../Articles/One.md)", role)
        self.assertNotIn("Articles/Agentic.md", role)

    def test_metadata_edit_rebuilds_base_and_reuses_linking_page(self):
        self.export()
        path = self.root / "Articles/One.md"
        self.write(
            "Articles/One.md",
            path.read_text().replace("status: reviewed", "status: partial"),
        )
        self.commit()
        result = self.export()
        self.assertEqual(
            set(result["rendered"]),
            {"Articles/One.md", "Bases/Sources.md"},
        )
        self.assert_matches_fresh()

    def test_rename_addition_and_deletion_remove_stale_output(self):
        self.export()
        self.git("mv", "Articles/One.md", "Articles/Renamed.md")
        self.write(
            "README.md",
            "# Index\n\n[[Articles/Renamed#Details]]\n\n![[Bases/Sources.base]]\n",
        )
        self.write(
            "Articles/Two.md", "---\ncollection: fde\ntype: article\n---\n# Two\n"
        )
        (self.root / "Resources/Tool.md").unlink()
        (self.root / "Attachments/test.pdf").unlink()
        self.commit()
        result = self.export()
        self.assertEqual(
            set(result["removed"]),
            {"Articles/One.md", "Resources/Tool.md", "Attachments/test.pdf"},
        )
        self.assert_matches_fresh()

    def test_workflow_links_point_to_source_and_missing_markdown_links_fail(self):
        self.write("Skills/example.md", "# Workflow source\n")
        self.write("README.md", "# Index\n\n[Workflow](Skills/example.md)\n")
        self.commit()
        self.export()
        self.assertIn(
            "https://github.com/example/vault/blob/main/Skills/example.md",
            (self.output / "README.md").read_text(),
        )
        self.assertFalse((self.output / "Skills/example.md").exists())
        (self.root / "Skills/example.md").unlink()
        self.commit()
        with self.assertRaisesRegex(ValueError, "missing Markdown link"):
            self.export()

    def test_snapshot_ignores_uncommitted_edits(self):
        commit = self.git("rev-parse", "HEAD")
        self.write("Articles/One.md", "UNCOMMITTED")
        self.export(commit=commit)
        self.assertIn("Original text.", (self.output / "Articles/One.md").read_text())

    def test_links_pdf_fragments_grouping_and_code_examples(self):
        self.write(
            "README.md",
            """# Index

[[Articles/One#Details|Label]] and [[Attachments/test.pdf#page=2|PDF page]].

`[[literal]]`

~~~text
[[also literal]]
~~~

![[Bases/Sources.base]]
""",
        )
        self.commit()
        self.export()
        text = (self.output / "README.md").read_text()
        self.assertIn("[Label](Articles/One.md#details)", text)
        self.assertIn("[PDF page](Attachments/test.pdf#page=2)", text)
        self.assertIn("`[[literal]]`", text)
        self.assertIn("~~~text\n[[also literal]]\n~~~", text)
        self.assertIn("[Sources](Bases/Sources.md)", text)
        self.assertNotIn("| file.name |", text)
        base = (self.output / "Bases/Sources.md").read_text()
        self.assertIn("### alpha", base)
        self.assertIn("[One](../Articles/One.md)", base)
        self.assertIn("## Missing status\n\nNo matching records.", base)

    def test_missing_heading_fails_even_when_linking_page_is_unchanged(self):
        self.export()
        before = {p: p.read_bytes() for p in self.output.rglob("*") if p.is_file()}
        path = self.root / "Articles/One.md"
        self.write(
            "Articles/One.md", path.read_text().replace("## Details", "## Renamed")
        )
        self.commit()
        with self.assertRaisesRegex(ValueError, "missing heading"):
            self.export()
        self.assertEqual({p: p.read_bytes() for p in before}, before)

    def test_unsupported_base_expression_fails(self):
        self.write(
            "Bases/Resources.base",
            'filters: file.hasTag("secret")\nviews:\n  - type: table\n    name: Bad\n    order: [file.name]\n',
        )
        self.commit()
        with self.assertRaisesRegex(ValueError, "Unsupported Base expression"):
            self.export()

    def test_unsupported_view_filter_fails_with_no_matching_records(self):
        self.write(
            "Bases/Resources.base",
            """filters: note.type == "absent"
views:
  - type: table
    name: Unsupported
    filters: file.hasTag("secret")
    order: [file.name]
""",
        )
        self.commit()
        with self.assertRaisesRegex(ValueError, "Unsupported Base expression"):
            self.export()

    def test_missing_output_is_restored_from_committed_source(self):
        self.export()
        (self.output / "Articles/One.md").unlink()
        result = self.export()
        self.assertEqual(result["rendered"], ["Articles/One.md"])
        self.assert_matches_fresh()

    def test_changed_cached_output_is_restored(self):
        self.export()
        (self.output / "Articles/One.md").write_text("Unexpected edit")
        (self.output / "Attachments/test.pdf").write_bytes(b"Unexpected edit")
        result = self.export()
        self.assertEqual(result["rendered"], ["Articles/One.md"])
        self.assertEqual(result["copied"], ["Attachments/test.pdf"])
        self.assert_matches_fresh()

    def test_exporter_change_rebuilds_cache_and_retains_deletions(self):
        self.export()
        path = self.output / EXPORT.CACHE
        cache = json.loads(path.read_text())
        cache["fingerprint"] = "old-exporter"
        path.write_text(json.dumps(cache))
        (self.root / "Resources/Tool.md").unlink()
        self.commit()
        result = self.export()
        self.assertGreater(len(result["rendered"]), 1)
        self.assertEqual(result["removed"], ["Resources/Tool.md"])
        self.assert_matches_fresh()


if __name__ == "__main__":
    unittest.main()
