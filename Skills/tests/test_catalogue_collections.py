"""Check collection isolation in inventories, themes and source identities."""
from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

import yaml


SCRIPT = Path(__file__).resolve().parents[1] / "fde-catalogue/scripts/validate_vault.py"
SPEC = importlib.util.spec_from_file_location("validate_vault", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class CollectionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "Bases").mkdir()

    def base(self, name, collection):
        config = {
            "filters": {"and": ['file.ext == "md"', f'note.collection == "{collection}"', 'note.type == "article"']},
            "views": [{"type": "table", "name": "Sources", "order": ["file.name"]}],
        }
        (self.root / "Bases" / name).write_text(yaml.safe_dump(config))

    def test_base_counts_do_not_combine_collections(self):
        self.base("Sources.base", "fde")
        self.base("Agentic sources.base", "agentic-development")
        records = {
            "first": ({"collection": "fde", "type": "article"}, ""),
            "second": ({"collection": "fde", "type": "article"}, ""),
            "third": ({"collection": "agentic-development", "type": "article"}, ""),
            "tool": ({"collection": "agentic-development", "type": "resource"}, ""),
        }
        errors = []
        output = io.StringIO()
        with redirect_stdout(output):
            VALIDATOR.validate_bases(self.root, records, errors)
        self.assertEqual(errors, [])
        self.assertIn("Sources.base: 2 records selected", output.getvalue())
        self.assertIn("Agentic sources.base: 1 records selected", output.getvalue())

    def test_unknown_collection_is_rejected(self):
        self.base("Unknown.base", "agentic-typo")
        errors = []
        with redirect_stdout(io.StringIO()):
            VALIDATOR.validate_bases(self.root, {}, errors)
        self.assertIn("Unknown.base: unscoped Base", errors)

    def article(self, collection, theme, url):
        name = f"Articles/{collection}"
        meta = {
            "collection": collection, "type": "article", "title": name, "author": ["Author"],
            "site": "Example", "url": url, "canonical_url": None,
            "publication_date": None, "publication_date_basis": "Unknown", "accessed": "2026-10-21",
            "created": "2026-10-21", "updated": "2026-10-21", "status": "reviewed", "tags": [],
            "source_kind": "practitioner-argument", "evidence_family": collection,
            "evidence_basis": ["practitioner-argument"], "contribution": "Example", "themes": [f"[[Themes/{theme}]]"],
        }
        path = self.root / f"{name}.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text("---\n" + yaml.safe_dump(meta) + "---\n# Example\n")
        return name

    def theme(self, name, collection, articles):
        meta = {"type": "theme", "collection": collection, "created": "2026-10-21", "updated": "2026-10-21", "status": "evolving", "tags": []}
        path = self.root / "Themes" / f"{name}.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text("---\n" + yaml.safe_dump(meta) + "---\n" + "\n".join(f"[[{article}]]" for article in articles))

    def test_a_role_theme_alone_does_not_classify_an_agentic_source(self):
        article = self.article("agentic-development", "Role", "https://example.com/agentic")
        self.theme("Role", "fde", [article])
        output = io.StringIO()
        with redirect_stdout(output):
            VALIDATOR.validate(self.root)
        self.assertIn("Articles/agentic-development: needs a theme in its own collection", output.getvalue())

    def test_the_same_source_cannot_be_duplicated_across_collections(self):
        first = self.article("fde", "Role", "https://example.com/shared")
        second = self.article("agentic-development", "Domain", "https://example.com/shared")
        self.theme("Role", "fde", [first])
        self.theme("Domain", "agentic-development", [second])
        output = io.StringIO()
        with redirect_stdout(output):
            VALIDATOR.validate(self.root)
        self.assertIn("Duplicate source identity:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
