"""Exercise session deduplication, Sync states and local registration preservation."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("check_session", Path(__file__).resolve().parents[1] / "check_session.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class SessionCheckTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.vault = self.base / "vault"
        (self.vault / ".obsidian").mkdir(parents=True)
        self.root = self.vault / "FDE"
        for name in CHECK.REQUIRED:
            path = self.root / "Skills" / "fde-catalogue" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        for name in CHECK.AGENTIC_REQUIRED:
            path = self.root / "Skills" / "agentic-development-catalogue" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        self.cache = self.base / "cache"

    def test_concurrent_calls_probe_once_and_new_session_probes_again(self):
        report = {"sync": {"status": "enabled"}, "warnings": []}
        with patch.object(CHECK, "check_workspace", return_value=report) as probe:
            with ThreadPoolExecutor(max_workers=4) as executor:
                results = list(executor.map(
                    lambda _: CHECK.session_report(self.root, "session-one", self.cache), range(4)))
            self.assertEqual(probe.call_count, 1)
            self.assertEqual(sum(not cached for _, cached in results), 1)
            CHECK.session_report(self.root, "session-two", self.cache)
            self.assertEqual(probe.call_count, 2)

    def test_same_session_checks_each_vault_and_device_cache(self):
        report = {"sync": {"status": "enabled"}, "warnings": []}
        with patch.object(CHECK, "check_workspace", return_value=report) as probe:
            CHECK.session_report(self.root, "session", self.cache)
            CHECK.session_report(self.root / "another", "session", self.cache)
            CHECK.session_report(self.root, "session", self.base / "other-device-cache")
            self.assertEqual(probe.call_count, 3)

    def test_warning_is_emitted_only_for_first_hook_result(self):
        report = {"sync": {"status": "disabled"}, "warnings": ["Enable all other types"]}
        for cached in [False, True]:
            output = io.StringIO()
            with redirect_stdout(output):
                CHECK.emit_report(report, cached, hook=True)
            data = json.loads(output.getvalue())
            self.assertEqual("systemMessage" in data, not cached)
            self.assertEqual(data["hookSpecificOutput"]["hookEventName"], "SessionStart")

    def test_sync_states(self):
        cases = [
            ({"enabled": True, "allOtherTypes": True, "excluded": False}, "enabled"),
            ({"enabled": False, "allOtherTypes": None, "excluded": None}, "disabled"),
            ({"enabled": True, "allOtherTypes": False, "excluded": False}, "disabled"),
            ({"enabled": True, "allOtherTypes": True, "excluded": True}, "disabled"),
            ({"enabled": True, "allOtherTypes": None, "excluded": False}, "unverified"),
            ({"enabled": True, "allOtherTypes": True, "excluded": None}, "unverified"),
        ]
        for data, expected in cases:
            with self.subTest(data=data), patch.object(CHECK, "sync_probe", return_value=data):
                self.assertEqual(CHECK.check_sync(self.root)["status"], expected)
        with patch.object(CHECK, "sync_probe", side_effect=FileNotFoundError("CLI unavailable")):
            self.assertEqual(CHECK.check_sync(self.root)["status"], "unverified")

    def test_probe_matches_vault_path_instead_of_active_vault(self):
        def output(executable, *arguments):
            if arguments == ("vaults", "verbose"):
                return f"Other vault\t/elsewhere\nNamed vault\t{self.vault}"
            self.assertEqual(arguments[0], "vault=Named vault")
            return "=> " + json.dumps({"vaultPath": str(self.vault), "enabled": True,
                                      "allOtherTypes": True, "excluded": False})
        with patch.object(CHECK.shutil, "which", return_value="obsidian"), patch.object(CHECK, "cli_output", side_effect=output):
            self.assertEqual(CHECK.check_sync(self.root)["status"], "enabled")

    def test_wrong_vault_response_is_unverified(self):
        outputs = [f"Named vault\t{self.vault}", json.dumps({"vaultPath": "/wrong-vault"})]
        with patch.object(CHECK.shutil, "which", return_value="obsidian"), patch.object(CHECK, "cli_output", side_effect=outputs):
            result = CHECK.check_sync(self.root)
            self.assertEqual(result["status"], "unverified")
            self.assertIn("different vault", result["detail"])

    def test_missing_skills_are_reported(self):
        (self.root / "Skills/fde-catalogue/SKILL.md").unlink()
        with patch.object(CHECK, "check_sync", return_value={"status": "enabled"}):
            report = CHECK.check_workspace(self.root)
        self.assertEqual(report["missing_files"], ["Skills/fde-catalogue/SKILL.md"])
        self.assertTrue(any("Staff catalogue" in warning for warning in report["warnings"]))

    def test_install_is_idempotent_and_preserves_existing_hooks_and_config(self):
        config = self.root / ".codex"
        config.mkdir()
        original = {"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "existing"}]}]}}
        (config / "hooks.json").write_text(json.dumps(original))
        (config / "config.toml").write_text("model = 'preserved'\n")
        CHECK.install_local(self.root)
        first = (config / "hooks.json").read_bytes()
        CHECK.install_local(self.root)
        self.assertEqual((config / "hooks.json").read_bytes(), first)
        self.assertEqual(json.loads(first)["hooks"]["Stop"], original["hooks"]["Stop"])
        self.assertEqual((config / "config.toml").read_text(), "model = 'preserved'\n")
        self.assertEqual((self.root / ".agents/skills/fde-catalogue").resolve(),
                         self.root / "Skills/fde-catalogue")

    def test_install_labels_existing_hook_without_replacing_settings(self):
        CHECK.install_local(self.root)
        path = self.root / ".codex/hooks.json"
        hooks = json.loads(path.read_text())
        hooks["description"] = "Existing workspace hooks"
        handler = hooks["hooks"]["SessionStart"][0]["hooks"][0]
        del handler["statusMessage"]
        handler["timeout"] = 30
        path.write_text(json.dumps(hooks))
        CHECK.install_local(self.root)
        handler["statusMessage"] = CHECK.HOOK_LABEL
        self.assertEqual(json.loads(path.read_text()), hooks)

    def test_install_preserves_conflicting_discovery_entry(self):
        link = self.root / ".agents/skills/fde-catalogue"
        link.mkdir(parents=True)
        marker = link / "existing"
        marker.write_text("preserved")
        with self.assertRaises(FileExistsError):
            CHECK.install_local(self.root)
        self.assertEqual(marker.read_text(), "preserved")

    def test_agentic_skill_is_discovered_and_missing_files_are_reported(self):
        CHECK.install_local(self.root)
        self.assertEqual((self.root / ".agents/skills/agentic-development-catalogue").resolve(),
                         self.root / "Skills/agentic-development-catalogue")
        (self.root / "Skills/agentic-development-catalogue/references/schema.md").unlink()
        with patch.object(CHECK, "check_sync", return_value={"status": "enabled"}):
            report = CHECK.check_workspace(self.root)
        self.assertEqual(report["missing_files"], ["Skills/agentic-development-catalogue/references/schema.md"])


if __name__ == "__main__":
    unittest.main()
