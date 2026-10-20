---
created: 2026-10-05T19:38
updated: 2026-10-20
---

# Working in this FDE vault

This folder is part of an Obsidian vault. Build an evidence-backed understanding of the FDE role, effective execution, and technical and professional development of strong FDE peers. Focus on engineering practice and collaboration rather than people management.

## Once per session

Consume the result from the FDE `SessionStart` hook when present. Otherwise, before the first task in this folder, run `python3 Skills/check_session.py` from this folder. It uses the Codex session ID to cache the result outside the vault. Reuse that result for the rest of the session, including resumes and compaction. Do not rerun the Sync probe or repeat startup warnings on each prompt. If no session ID is available, supply the actual conversation ID with `--session-id`; do not invent one.

The check verifies required skill files, the containing vault, Sync's `Sync all other types` setting, and folder exclusions. Surface new warnings once. An unavailable CLI or changed Obsidian interface means unverified, not disabled. Never enable Sync or change its settings automatically.

On a new device, or when local registrations are missing, run `python3 Skills/check_session.py --install`. This creates local Codex discovery symlinks and a `SessionStart` hook labelled "FDE vault: check skills and Obsidian Sync" without copying the skills. The hook verifies catalogue skill files and Obsidian Sync once per session. Reinstalling adds the label to an existing registration. Restart Codex, mark this workspace trusted in Codex if necessary, and review the hook through `/hooks`. Codex skips project hooks in untrusted workspaces and skips hook definitions that have not been approved. Do not change trust settings automatically. Until the hook runs, use the check above. `.agents/` and `.codex/` are local registrations; `Skills/` holds the synced source files. The Sync setting must be enabled separately on each device.

## Ingesting sources

For supplied URLs or content intended for this knowledge base, verify that [Skills/fde-catalogue/SKILL.md](Skills/fde-catalogue/SKILL.md) exists, then read and apply it before ingestion, even if it is absent from the skill selector. Read it once when first needed and reuse its instructions within the session. A URL supplied for cataloguing authorises its source note, relevant theme and directory updates, justified extracted models or practices, and evidence-led edits to `FDE.md`. Complete those together without asking for routine confirmation.

For supplied material about Staff, Principal, or senior individual-contributor engineering practice, check `Skills/staff-engineer-catalogue/SKILL.md` and read it before ingestion when available. If it is missing, explain that the Staff ingestion workflow needs restoring; do not silently substitute the FDE skill or invent its instructions. Maintain `Staff Engineer.md` as a separate synthesis. When a source bears directly on field engineering, connect the source once and add a qualified adaptation to `FDE.md`; do not collapse the two roles.

The skill owns the ingestion workflow and metadata schema. Keep those instructions there rather than duplicating them here.

## Git synchronization

This folder is tracked at [alexbevi/forward-deployed-engineering](https://github.com/alexbevi/forward-deployed-engineering), with remote `origin` and branch `main`.

After each invocation of the FDE catalogue skill (`fde-catalogue`) or Staff Engineer catalogue skill (`staff-engineer-catalogue`), finish the relevant validation, review the changes, commit the changes made by that invocation when any, and run `git push origin main` before reporting completion. Routine commits and pushes are authorised; do not ask for confirmation again. Work on `main`, stage the invocation's content and related maintenance changes explicitly, and preserve unrelated work. Do not create empty commits or force-push. If a commit or push cannot complete, report the blocker and any changes still awaiting synchronization.

Use Conventional Commits with a brief description of the actual content changed, such as `docs(fde): catalogue OrNsoft engagement gates` or `docs(staff): add technical influence source`. Use an appropriate type and optional scope for skill or infrastructure changes. Keep device-local `.agents/` and `.codex/` registrations and generated caches out of Git; `Skills/` is the synced workflow source.

Pushes to `main` trigger `.github/workflows/publish.yml`, which incrementally exports standard Markdown to `published`. Edit the source on `main`; the workflow manages the generated branch and its `.publish-cache.json`. The cache records the last source commit and page dependencies so content edits update only affected pages and tables. `Skills/publish/README.md` documents local export, supported syntax and cache behavior. When changing the exporter, run its tests and inspect a generated export before pushing; report any failed publication workflow.

## Structure

- `FDE.md` is the evolving synthesis and entry point.
- `Staff Engineer.md` is the parallel synthesis for Staff-level engineering scope, influence, and craft.
- `Articles/` contains one note per distinct article or supplied source.
- `Themes/` contains curated reading catalogues and questions.
- `Operating models/` compares mandates, responsibility, and engagement mechanics.
- `Approaches/` captures reusable technical methods, including research-derived candidates, with explicit transfer assumptions and evidence status.
- `Playbooks/` holds practical procedures with explicit evidence and local-use status.
- `People/` and `Resources/` hold documented contributors and useful resource leads.
- `Catalogue.md`, `Operating models.md`, `Approaches.md`, `Playbooks.md`, `People.md`, and `Resources.md` are directory entry points.
- `Attachments/` retains primary PDFs and attributed, page-numbered Markdown search indices. Follow the skill for downloading, versioning and verification.
- `Bases/` generates scoped views from frontmatter; `collection: fde` identifies content in this collection.
- `Skills/fde-catalogue/` contains the reusable skill, metadata reference, and validator. `Skills/check_session.py` checks session prerequisites and installs local Codex registrations. Keep skill infrastructure outside content validation and Base inventories.

Use topic tags and theme notes before adding deeper folder hierarchies. Let the material justify new themes. Preserve existing filenames and links unless a reorganisation has a concrete benefit.

## Editorial rules

Preserve the user's writing and distinguish source claims, our synthesis, and proposed practices. Attribute disputed definitions and commercial claims. Keep disagreements visible; do not make the most recent article the vault's unquestioned position.

Catalogue useful material even when it does not change the root narrative. Edit `FDE.md` only when a source supports a useful addition, qualification, contradiction, or revision. A new source can also support an existing point without expanding the prose.

Use Obsidian wikilinks for internal connections, Markdown links for external sources, and valid YAML frontmatter. Prefer specific, readable prose and short paraphrases over long extracts.

After changes, check metadata, internal links, source relationships, and affected Base coverage. Report additions and explain how `FDE.md` changed, or why it stayed unchanged. State material verification gaps.

Recommend useful next steps when new content reveals a practical opportunity, evidence gap, contradiction, or structural improvement. Explain the reason without turning every article into a generic advice list. Keep model descriptions separate from proposed playbooks and locally observed results. Preserve shared provenance so overlapping sources do not masquerade as independent support.
