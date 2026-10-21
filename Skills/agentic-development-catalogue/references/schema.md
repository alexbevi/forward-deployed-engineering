# Agentic development records

New records use `collection: agentic-development`, with `type`, `status`, ISO `created` and `updated` dates and plain-list `tags`. Use `agentic-development` and topic tags without adding `fde` merely to share the vault. Internal relationships are quoted wikilinks; external URLs are Markdown links. Reuse existing filenames after corrections.

## Articles and other sources

Store distinct sources in `Articles/YYYY-MM-DD - Author - Short title.md`, using `undated` when necessary. Require `title`, author list, `site`, supplied `url`, `canonical_url`, `publication_date`, `publication_date_basis`, `accessed`, `source_kind`, `evidence_family`, `evidence_basis`, `contribution` and `themes`. Unknown scalars are YAML null, unknown lists are `[]`. Keep modification dates in `source_updated` with a separate basis. A publisher's domain is not necessarily the author's name.

`status: reviewed` means the inspected material was read, not that its results were reproduced. `partial` records disclose access limits. Evidence bases can include `practitioner-argument`, `reported-experience`, `reported-experiment`, `hypothetical-example` and `vendor-announcement`. Preserve common provenance using a stable family slug. Article identity remains unique across collections.

At least one `themes` link must point to an agentic-development theme that catalogues the article. Optional `approaches`, `playbooks`, `people`, `resources` and `models` lists use existing typed records only when useful. `role_applications` may list exact FDE or Staff notes with a qualified application explained in the body; use `[]` when none is justified. Do not duplicate the source or turn a proposed transfer into an observed result.

For versioned research and PDF attachments, use the shared fields described in `Skills/fde-catalogue/references/schema.md`, retaining this collection value. Those format-specific fields do not assign an FDE mandate.

## Extracted notes

| Type | Required properties beyond common fields |
| --- | --- |
| approach | purpose, mechanism, application_scope, evidence_status, application_status, sources, local_observations |
| playbook | purpose, practice_status, sources, local_observations |
| resource | resource_kind, purpose, url, sources |
| person | person_name, relevance, public_url, sources |
| theme | Reading question, curated catalogue, connections and open questions in the body |
| synthesis or index | Maintained argument or directory purpose and useful navigation |

Use `sources` for article-note links. A directly inspected resource can use `sources: []` when `url` and `last_verified` identify its primary material. Resource status is `mentioned`, `reviewed` or `used`; only actual recorded use warrants `used`. Optional repository fields are `reviewed_revision`, `reviewed_version`, `license`, `review_scope` and `local_observations`.

Approach `evidence_status` is `source-reported` or `independently-reproduced`; `application_status` is `proposed` or `locally-tried`. Playbook `practice_status` is `proposed`, `source-reported` or `locally-tried`. Reproduced or locally tried claims require dated `local_observations` with context, outcome and limitations. Initial adaptations remain proposed.

## Views and boundaries

`Bases/Agentic sources.base` selects article records using `note.collection == "agentic-development"` and `note.type == "article"`. Keep `file.ext == "md"` in the top-level conjunction. Add another collection-scoped Base only when a populated record type warrants it. Existing FDE/Staff inventories continue selecting `collection: fde`; do not broaden them to include domain records automatically.

Publishing includes both collections and links to each generated Base page. Use the shared validator and publisher, not separate copies. Cross-domain navigation is allowed; a claim that evidence transfers requires an explicit explanation in the affected note.
