# Records and views

All content records use `collection: fde`, `type`, `status`, ISO `created` and `updated` dates, and a list of plain `tags`. Keep the source's dates separate from note dates. Use YAML null for unknown scalars, empty lists for unknown list values, and quoted wikilinks for relationships. Preserve existing properties and user annotations when migrating records.

## Source records

Keep the established article fields: title, author list, site, url, canonical_url, publication_date, publication_date_basis, accessed, source_kind, and themes. Filename convention is `Articles/YYYY-MM-DD - Author - Short title.md`; use `undated` when needed and preserve existing filenames after corrections.

Additional fields support extraction and browsing:

| Property | Shape and purpose |
| --- | --- |
| evidence_family | A string identifying related provenance, such as APEG's overlapping engagement series. Use a stable slug without spaces. |
| evidence_basis | List of applicable evidence types, such as reported-experience, practitioner-argument, measured-results, hypothetical-example, vendor-announcement, analyst-advice, forecast, future-expectation. |
| contribution | A short statement of the source's useful addition; not a second abstract. |
| people | Links to documented person notes. Preserve author names separately. |
| models | Links to relevant operating-model notes. |
| playbooks | Links to procedures informed by the source. |
| resources | Links to useful resource records. |

`reviewed` means the source text was read, not that its claims were independently verified. `partial` records disclose access gaps. Separate author, quoted analyst, publisher, and source-modification metadata when useful. Do not label an example measured-results simply because it contains numbers; say whether underlying measurements were inspected.

## Extracted records

| type | Required content and properties |
| --- | --- |
| operating-model | mandate, engagement_type, ownership, success_measure, evidence_status, sources. Describe lifecycle, decision rights, fit, and failure modes in prose. Use unknown/null for missing evidence. Initial evidence_status is source-reported. |
| approach | purpose, mechanism, application_scope, evidence_status, application_status, sources, local_observations. Explain fit, transfer assumptions and failure modes in prose. |
| playbook | purpose, practice_status, sources, local_observations. Procedure, artifact, checks, and limitations belong in the body. |
| person | person_name, relevance, public_url, sources. Keep unknown public_url null. Record dated evidence for roles, affiliations, and influence when adding them. |
| resource | resource_kind, purpose, url, status, sources. Use null for inaccessible or unknown URLs. Add availability and last_verified when supported. |
| theme | Reading question, curated source catalogue, questions, and practical connections. |
| index | Directory purpose, relevant Base embed, and useful navigation. |
| synthesis | Main argument and adjacent evidence links. |

`sources` contains article-note links supporting an extracted record. External documentation can instead be supported by its inspected URL and verification date. Do not count an index as evidence.

Playbook `practice_status` is `proposed`, `source-reported`, or `locally-tried`. A combined or adapted procedure is proposed even if some constituent practices were reported elsewhere. Local observations describe context, date, result, limitations, and any revision. Locally-tried does not mean generally validated.

Resource `status` is `mentioned`, `reviewed`, or `used`. Mentioned records identify their source and what remains unverified. Reviewed records require direct inspection of the resource's material. Used records require an actual recorded local use. `last_verified` dates a particular inspection, not the ingestion of an article that merely links to the resource.

For a resource supplied directly, `sources: []` is valid when `url` and `last_verified` identify inspected primary material. Explain that evidence in the body and link the resource from a relevant theme; a duplicate article record is unnecessary. A resource mentioned by another source retains that article relationship. Reuse an existing resource when repository URL casing, a homepage, or a documentation URL identifies the same tool.

For tools and repositories, add these optional properties when useful:

| Property | Meaning |
| --- | --- |
| reviewed_revision | Quoted commit SHA or immutable release identifier inspected. |
| reviewed_version | Quoted version read from the inspected manifest or release, with its basis in the body. It does not establish a published or installed version. |
| license | Verified license identifier, or null when unknown. |
| review_scope | What was inspected and which execution checks, if any, ran. |
| themes | Quoted theme wikilinks for discovery and practical relevance. |
| local_observations | Actual use context, date, outcome and limits; use `[]` when none. Required evidence for `used`. |

Record practical prerequisites, host compatibility claims, installation documentation and a concrete trial idea in the body. Keep publisher tests separate from local results. `availability` describes access observed on `last_verified`, not a promise of support or stability.

## Bases

The `.base` files live in `Bases/`. Scope each to Markdown files with `note.collection == "fde"` and its intended `note.type`. This avoids depending on the FDE folder's position inside the containing vault.

Current views are Sources, Operating models, Approaches, Playbooks, People, and Resources. Sources includes provenance grouping and verification gaps; Resources includes unreviewed leads. Tables use file.name plus relevant frontmatter properties. Avoid dynamic filters involving `this` unless needed, because embedding changes what it refers to.

Use the [official syntax reference](https://obsidian.md/help/bases/syntax) before introducing new formulas or view options. Do not change global Obsidian property settings or plugin configuration as part of catalogue maintenance. When available, use [the optional CLI checks](obsidian-cli.md) to verify affected Base queries in Obsidian; YAML validation and record counts alone do not establish runtime query results.

## Relationship example

```yaml
collection: fde
evidence_family: publisher-engagement-account
evidence_basis:
  - reported-experience
contribution: "Explains a concrete handover practice"
people:
  - "[[People/Verified name]]"
models:
  - "[[Operating models/Customer-owned delivery]]"
playbooks:
  - "[[Playbooks/Prove a handover]]"
```

The example's destinations are schematic; actual record links must resolve. Reuse existing relationships instead of creating notes to satisfy this example.

## PDF attachments and searchable text

For a PDF source, set `source_format: pdf`, `primary_source_url` to the artifact URL, and keep `url`/`canonical_url` for the landing page when one exists. Use `attachments` (PDF wikilink list) and `text_indexes` (attachment-text note wikilink list). A month-only publication uses null `publication_date` and a quoted `publication_month: "YYYY-MM"`; record landing dates separately.

An `attachment-text` record lives beside its PDF in `Attachments/`. It requires `sources`, scalar `attachment` wikilink, `source_url`, `sha256`, `byte_size`, `page_count`, `downloaded`, `indexed`, `extraction_method`, `extraction_status`, and `pages_with_text`, plus standard content fields. Use `status: derived`. Extraction status is `text-extracted` or `partial-needs-review`; neither proves visual fidelity. Sections use `## Page N` and `[[Attachments/name.pdf#page=N|Open PDF page N]]`. Full SHA-256 identifies the bytes; filenames include a hash prefix. Preserve prior versions and user annotations.

The source and resource Bases expose local attachments and search indices. The derived index remains outside the article inventory. Obsidian's native [Search](https://obsidian.md/help/plugins/search) searches note contents, so the Markdown sidecar supplies searchable text while the PDF supplies the original layout.

## Research papers and approaches

Research papers remain `type: article` under `Articles/`, with `source_kind: research-paper` and, for arXiv, `source_format: html`, `arxiv_id` as a quoted string, `arxiv_version` such as v1, and `primary_source_url` as the versioned HTML URL. Preserve the supplied `url`; use a versioned abstract URL for `canonical_url`. Verify `publication_date` against that version's submission history and explain its basis. Keep `research_status` as preprint unless peer-reviewed publication is verified; `venue` is null when unknown. Use a stable evidence family based on the arXiv identifier across manuscript versions. Keep benchmark/code versions separate. `reported-experiment` identifies inspected experimental reporting, not a reproduced result.

Source, playbook and resource notes may link `approaches` as a list of quoted approach-note wikilinks. Approaches link source evidence through `sources`, and actionable procedures through `playbooks`. `evidence_status` is source-reported or independently-reproduced; `application_status` is proposed or locally-tried. Independently-reproduced and locally-tried require actual `local_observations`. A successful reproduction still does not prove transfer to a customer engagement. Track local context, date, checks, outcome and limitations when evidence exists.
