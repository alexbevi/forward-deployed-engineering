# Publish the Markdown edition

`main` holds the Obsidian source. The `Publish Markdown` GitHub Actions workflow exports it to the generated [`published` branch](https://github.com/alexbevi/forward-deployed-engineering/tree/published) after each push to `main`, or on manual dispatch. Publication commits use `docs(publish): export vault at <source commit>`.

The exporter converts wikilinks and heading references to relative Markdown links, turns PDF embeds into attachment links, and renders frontmatter as a metadata table. Base embeds become links to generated pages containing all their views. Links to tracked workflow files excluded from the edition point back to `main`. Code examples and fenced PDF search text remain literal.

## Incremental cache

The published branch retains `.publish-cache.json`, including the last exported source commit, parsed metadata, headings, output hashes and link/Base dependencies. Each run uses `git diff` from that source commit to the requested commit. It reads committed Git blobs, so uncommitted source edits cannot enter an export.

- Unchanged notes reuse cached metadata and rendered files.
- A body-only edit renders that note.
- Changed metadata can update a Base. Base signatures reflect the selected rows, columns and grouping, so unrelated tables and pages linking to them stay cached.
- Renames and deletions remove stale outputs; incoming links must still resolve.
- Missing or modified output files are restored. Exporter code changes rebuild the cache.

All new page content is rendered and links are resolved before output updates begin. A rendering error leaves the preceding publication intact. `PUBLICATION.md` records the source commit for the whole edition, avoiding a new commit stamp on every page.

The cache is stored with the generated output rather than in an expiring Actions cache. Source history must include the recorded commit. The workflow fetches full history and serializes publishing jobs; each job checks out the latest `main`, and publication uses a normal push.

## Local verification

Requires Python 3.12+ and PyYAML. Run from the repository root:

```sh
uv run --with pyyaml python -m unittest discover -s Skills/tests -v
uv run --with pyyaml python Skills/publish/export.py \
  --output /tmp/fde-published \
  --repository https://github.com/alexbevi/forward-deployed-engineering
```

Run the export again with the same output directory to verify cache reuse. `--commit <revision>` selects another committed snapshot. Keep the output outside the source checkout. The JSON report names rendered, written, copied and removed files; rendering a page does not rewrite identical output.

## Supported Base syntax

The evaluator supports this vault's table views, column order, scalar grouping in `ASC` or `DESC` order, and nested `and`, `or`, `not` filters. Comparisons support `==` and `!=` with JSON scalar literals, note properties, `file.name`, `file.ext` and string/list `.length`. Default row order is the source path. It does not execute expressions.

Unsupported expressions, view settings, embeds, ambiguous links and missing headings fail explicitly. Extend the evaluator and tests when introducing new Base features. Live Base editing and interactive filtering remain part of the Obsidian source, while the published edition is a static snapshot.
