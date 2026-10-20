# Optional Obsidian runtime verification

Use the [official CLI reference](https://obsidian.md/help/cli) and installed command help when syntax or capability is uncertain. The CLI needs a compatible installer, registration and the desktop app. Availability is an environment check, not a prerequisite for ingestion.

## Establish the target

Check `command -v obsidian`. On macOS, if it is absent but `/Applications/Obsidian.app/Contents/MacOS/obsidian-cli` exists, use that bundled executable directly without installing a symlink or changing PATH. If neither is available, skip runtime checks. Use the selected executable with `help` to inspect supported commands. If it reports that the CLI is disabled, report the Settings location it provides and skip runtime checks until enabled. Find the containing vault root through its `.obsidian` directory, then match its absolute path against `obsidian vaults verbose`. Do not assume this FDE subfolder is a standalone vault or that the active vault is correct. Use the matched vault name or ID explicitly, as the first argument before the command, and exact vault-relative file paths. Verify the target path before queries. Stop this optional check if targeting is ambiguous or the CLI fails; continue the local workflow.

The commands below use a placeholder `VAULT_ID`. In this workspace, record paths start with `Forward Deployed Engineering/` inside the containing vault. Recompute that prefix if the folder moves.

```sh
obsidian vault=VAULT_ID vault info=path
obsidian vault=VAULT_ID properties path="Forward Deployed Engineering/FDE.md" format=json
obsidian vault=VAULT_ID links path="Forward Deployed Engineering/FDE.md"
obsidian vault=VAULT_ID backlinks path="Forward Deployed Engineering/FDE.md" format=json
obsidian vault=VAULT_ID unresolved verbose format=json
obsidian vault=VAULT_ID base:query path="Forward Deployed Engineering/Bases/Sources.base" view="All sources" format=json
obsidian vault=VAULT_ID search query="governance" path="Forward Deployed Engineering/Attachments" limit=5 format=json
```

## Choose checks for the change

Inspect properties and links on changed records, not just FDE.md. Confirm intended source/theme/practice connections in Obsidian's interpretation. Scope unresolved-link findings to affected source files and compare against pre-edit findings when available. Unrelated vault issues are not ingestion failures; record relevant existing problems without claiming this batch introduced them. The local validator still checks heading anchors, typed relationships and PDF integrity.

For affected Bases, query the exact view and confirm expected new records appear, collection/type boundaries hold, and returned fields agree with the note metadata. This verifies runtime query results; it does not demonstrate visual layout.

For a new PDF text index, search for a distinctive phrase actually present in the extraction and confirm the expected sidecar appears. This checks native search visibility, not PDF binary indexing, extraction fidelity or diagram recognition. Search can also help find prior related material before deciding where a new contribution belongs.

Keep these checks read-only. Editing files remains part of the existing catalogue workflow; runtime verification does not require plugin changes, arbitrary eval, publishing or sync operations. If visual verification is needed, inspect the specific view and capture it using supported developer commands. Claim rendering verification only after viewing the relevant result.

## Report the boundary

Say which runtime checks ran and what they established. CLI absence or failure means runtime verification was skipped, not that the content failed validation. Base query success, native search visibility, link resolution and visual rendering are separate evidence. Never replace editorial review or source verification with an app check.
