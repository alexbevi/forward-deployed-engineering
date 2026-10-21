"""Check skill files and Obsidian Sync once per Codex session on this device."""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
import getpass
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import sqlite3
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent
HOOK_LABEL = "FDE vault: check skills and Obsidian Sync"
REQUIRED = (
    "SKILL.md",
    "references/schema.md",
    "references/obsidian-cli.md",
    "scripts/validate_vault.py",
    "scripts/index_pdf.py",
)
AGENTIC_REQUIRED = ("SKILL.md", "references/schema.md")


def install_local(root: Path) -> None:
    root = root.resolve()
    discovery = root / ".agents" / "skills"
    discovery.mkdir(parents=True, exist_ok=True)
    for skill in sorted((root / "Skills").glob("*/SKILL.md")):
        link = discovery / skill.parent.name
        if (link.is_symlink() or getattr(link, "is_junction", lambda: False)()) and link.resolve() == skill.parent.resolve():
            continue
        if link.exists() or link.is_symlink():
            raise FileExistsError(f"Preserved existing discovery entry: {link}")
        try:
            link.symlink_to(Path("../..") / "Skills" / skill.parent.name, target_is_directory=True)
        except OSError as exc:
            if os.name != "nt" or exc.winerror != 1314:
                raise
            # Directory junctions do not require Windows symlink privileges.
            subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(skill.parent.resolve())],
                           check=True, capture_output=True, text=True)

    config_dir = root / ".codex"
    config_dir.mkdir(exist_ok=True)
    hooks_path = config_dir / "hooks.json"
    original = hooks_path.read_text() if hooks_path.exists() else ""
    hooks = json.loads(original) if original else {}
    hooks.setdefault("description", "FDE vault session prerequisites: verify catalogue skills and Obsidian Sync once per session.")
    groups = hooks.setdefault("hooks", {}).setdefault("SessionStart", [])
    command_args = [sys.executable if os.name == "nt" else "python3", str(root / "Skills" / "check_session.py"), "--hook"]
    command = subprocess.list2cmdline(command_args) if os.name == "nt" else shlex.join(command_args)
    legacy_command = shlex.join(["python3", str(root / "Skills" / "check_session.py"), "--hook"])
    matching = [h for g in groups for h in g.get("hooks", []) if h.get("command") in {command, legacy_command}]
    if matching:
        for handler in matching:
            handler["command"] = command
            handler["statusMessage"] = HOOK_LABEL
    else:
        groups.append({
            "matcher": "^(startup|resume|clear|compact|fork)$",
            "hooks": [{"type": "command", "command": command, "timeout": 20,
                       "additionalContextLimit": 1000, "statusMessage": HOOK_LABEL}],
        })
    rendered = json.dumps(hooks, indent=2) + "\n"
    if rendered != original:
        hooks_path.write_text(rendered)
    config_path = config_dir / "config.toml"
    if not config_path.exists():
        config_path.write_text("# Local session hooks are registered in hooks.json.\n")


def cli_output(executable: str, *arguments: str) -> str:
    result = subprocess.run([executable, *arguments], capture_output=True, text=True, timeout=6)
    if result.returncode:
        raise RuntimeError(f"Obsidian CLI exited with status {result.returncode}")
    return result.stdout.strip()


def sync_probe(root: Path) -> dict:
    root = root.resolve()
    vault = next((p for p in (root, *root.parents) if (p / ".obsidian").is_dir()), None)
    if vault is None:
        raise RuntimeError("Containing Obsidian vault was not found")
    executable = shutil.which("obsidian")
    bundled = Path("/Applications/Obsidian.app/Contents/MacOS/obsidian-cli")
    if executable is None and bundled.is_file():
        executable = str(bundled)
    if executable is None:
        raise RuntimeError("Obsidian CLI is unavailable")
    names = []
    for line in cli_output(executable, "vaults", "verbose").splitlines():
        name, separator, path = line.rpartition("\t")
        if separator and Path(path).resolve() == vault:
            names.append(name)
    if len(names) != 1:
        raise RuntimeError("Could not uniquely match the containing vault in Obsidian")
    skills_path = (root.relative_to(vault) / "Skills").as_posix()
    # The filter is an internal Obsidian interface; unknown shapes stay unverified.
    code = """JSON.stringify((() => {
      const p = app.internalPlugins.plugins.sync;
      const f = p?.instance?.filter;
      const path = SKILLS_PATH;
      return {
        vaultPath: app.vault.adapter.getBasePath(),
        enabled: p?.enabled === true,
        allOtherTypes: f?.allowTypes instanceof Set ? f.allowTypes.has("unsupported") : null,
        excluded: Array.isArray(f?.ignoreFolders) ? f.ignoreFolders.some(raw => {
          const folder = raw.replace(/\\/$/, "");
          return path === folder || path.startsWith(folder + "/") || folder.startsWith(path + "/");
        }) : null
      };
    })())""".replace("SKILLS_PATH", json.dumps(skills_path))
    output = cli_output(executable, f"vault={names[0]}", "eval", f"code={code}")
    data = json.loads(output.removeprefix("=> "))
    if Path(data["vaultPath"]).resolve() != vault:
        raise RuntimeError("Obsidian returned a different vault")
    return data


def check_sync(root: Path) -> dict:
    try:
        data = sync_probe(root)
    except (OSError, RuntimeError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        return {"status": "unverified", "detail": str(exc)}
    if not data["enabled"]:
        return {"status": "disabled", "detail": "Obsidian Sync is disabled for this vault"}
    if data["allOtherTypes"] is False:
        return {"status": "disabled", "detail": "Enable Settings > Sync > Sync all other types on this device"}
    if data["excluded"] is True:
        return {"status": "disabled", "detail": "Skills or part of its folder tree is excluded from Sync"}
    if data["allOtherTypes"] is not True or data["excluded"] is not False:
        return {"status": "unverified", "detail": "Obsidian's Sync filter interface was not recognized"}
    return {"status": "enabled", "detail": "All other types enabled; Skills has no folder exclusions"}


def check_workspace(root: Path) -> dict:
    missing = [f"Skills/fde-catalogue/{name}" for name in REQUIRED
               if not (root / "Skills" / "fde-catalogue" / name).is_file()]
    missing.extend(f"Skills/agentic-development-catalogue/{name}" for name in AGENTIC_REQUIRED
                   if not (root / "Skills" / "agentic-development-catalogue" / name).is_file())
    warnings = [f"Required skill file is missing: {name}" for name in missing]
    if not (root / "Skills" / "staff-engineer-catalogue" / "SKILL.md").is_file():
        warnings.append("Staff catalogue skill is missing; restore it before Staff-specific ingestion")
    sync = check_sync(root)
    if sync["status"] != "enabled":
        warnings.append(f"Sync {sync['status']}: {sync['detail']}")
    return {"checked_at": datetime.now(timezone.utc).isoformat(), "missing_files": missing,
            "sync": sync, "warnings": warnings}


def session_report(root: Path, session_id: str, cache_dir: Path) -> tuple[dict, bool]:
    root = root.resolve()
    cache_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    key = hashlib.sha256(f"{root}\0{session_id}".encode()).hexdigest()
    with closing(sqlite3.connect(cache_dir / "checks.sqlite3", timeout=15)) as connection, connection:
        connection.execute("CREATE TABLE IF NOT EXISTS checks (key TEXT PRIMARY KEY, report TEXT NOT NULL)")
        connection.execute("BEGIN IMMEDIATE")
        row = connection.execute("SELECT report FROM checks WHERE key = ?", (key,)).fetchone()
        if row:
            return json.loads(row[0]), True
        report = check_workspace(root)
        connection.execute("INSERT INTO checks VALUES (?, ?)", (key, json.dumps(report)))
    return report, False


def emit_report(report: dict, cached: bool, hook: bool) -> None:
    if not hook:
        print(json.dumps({"cached": cached, **report}, indent=2))
        return
    context = ("FDE session prerequisites already checked. " if cached else "FDE session prerequisites checked. ")
    context += json.dumps(report)
    context += " Reuse this result after resume or compaction. Do not repeat startup warnings. Read the relevant skill when needed."
    output = {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}
    if report["warnings"] and not cached:
        output["systemMessage"] = "FDE session check: " + "; ".join(report["warnings"])
    print(json.dumps(output))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install", action="store_true", help="Install local discovery links and SessionStart hook")
    parser.add_argument("--hook", action="store_true", help="Read the Codex hook event from stdin")
    parser.add_argument("--session-id", help="Actual conversation ID when Codex does not export one")
    parser.add_argument("--cache-dir", type=Path, default=Path(tempfile.gettempdir()) / f"fde-session-check-{getpass.getuser()}")
    args = parser.parse_args()
    if args.install:
        install_local(ROOT)
        print(f"Local discovery links and SessionStart hook installed: {HOOK_LABEL}. "
              "Restart Codex, trust this workspace if needed, and review /hooks.")
        return
    event = json.load(sys.stdin) if args.hook else {}
    session_id = args.session_id or event.get("session_id") or os.environ.get("CODEX_THREAD_ID") or os.environ.get("CODEX_SESSION_ID")
    if not session_id:
        parser.error("No session ID available; supply the actual conversation ID with --session-id")
    report, cached = session_report(ROOT, session_id, args.cache_dir)
    emit_report(report, cached, args.hook)


if __name__ == "__main__":
    main()
