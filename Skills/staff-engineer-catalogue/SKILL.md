---
name: staff-engineer-catalogue
description: Catalogue supplied Staff+ engineering sources in this Obsidian vault, maintain the Staff Engineer synthesis, and reconcile only explicit overlap into the FDE synthesis. Use for URLs or content about Staff, Principal, or senior individual-contributor engineering practice; use the FDE catalogue workflow for FDE-only material.
---

# Staff Engineer Catalogue

Create an evidence-backed Staff engineering collection alongside, but not inside, the FDE argument.

## Ingest a source

Work in the folder containing `Staff Engineer.md` and `AGENTS.md`. Read `AGENTS.md`, the Staff synthesis and relevant catalogues, then retrieve enough of the supplied source to verify its title, author, publication date, canonical URL, central claims, examples, and limitations. If access is incomplete, set `status: partial` and state what could not be verified.

Use the shared metadata schema in [../fde-catalogue/references/schema.md](../fde-catalogue/references/schema.md). For primary PDFs and research sources, follow the attachment and research procedures in [../fde-catalogue/SKILL.md](../fde-catalogue/SKILL.md); those shared mechanics do not change the Staff evidence scope. For FDE-only material use that FDE workflow. For general agentic development use [../agentic-development-catalogue/SKILL.md](../agentic-development-catalogue/SKILL.md), preserving its separate collection and synthesis.

Search existing URLs, canonical URLs and title/author matches across collections before creating a record. Create one note in `Articles/` per distinct source; reuse an existing source rather than duplicating it across roles or collections. Follow the existing article frontmatter conventions, including `type`, title and author fields, URL provenance, dates, status, source kind, tags, themes, collection, evidence family and basis, contribution, and people. Use `collection: fde` for new Staff records so the existing source and people Bases cover the shared vault. Do not count a search result, summary, or another article's citation as independent support.

Separate:

- the source's claims and reported experience;
- vault synthesis or transfer assumptions;
- proposed practices that have not been locally evaluated.

Create or update contributor notes only from verified source information. Catalogue relevant material even when it does not change either synthesis.

## Maintain the Staff synthesis

Update `Staff Engineer.md` only when the source adds, qualifies, contradicts, or supports a useful point about senior individual-contributor scope, technical judgment, influence, collaboration, or capability-building. Maintain relevant theme catalogues and `Catalogue.md` as reading paths rather than duplicating the synthesis.

Treat career-level labels as organisation-specific unless a source establishes otherwise. Do not turn a practitioner's recommended method into a universal progression framework or an evidenced outcome.

## Reconcile the FDE intersection

Staff level and FDE are different dimensions: Staff describes scope and influence; FDE describes a field-facing engineering context. Neither implies the other.

Edit `FDE.md` only when the source supports an obvious connection to field discovery, system design, customer or product alignment, production delivery, handover, peer development, or cross-team learning. Label the transfer when the source was not about FDE, preserve contrary evidence, and link to `Staff Engineer.md` rather than importing Staff-only material.

For a source relevant to both, use one article note with both sets of tags and theme links. Shared provenance must not appear as two independent sources.

## Verify and report

Run the shared validator with `uv run --with pyyaml python Skills/fde-catalogue/scripts/validate_vault.py`, or an existing PyYAML-enabled Python. Check YAML, wikilinks, source relationships, duplicate notes, and coverage by `Bases/Sources.base` and `Bases/People.base`. When the Obsidian CLI is available, follow [../fde-catalogue/references/obsidian-cli.md](../fde-catalogue/references/obsidian-cli.md) for targeted runtime checks; otherwise report that runtime verification was skipped.

Follow the repository's Conventional Commit and push workflow in `AGENTS.md`. Report what was added, how each synthesis changed or why it did not, and any material verification or synchronization gaps. Recommend a next step only when the evidence exposes a concrete question, contradiction, or practice worth testing.
