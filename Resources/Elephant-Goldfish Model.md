# Elephant-Goldfish Model

[Project site](https://egm.dev/) and [repository at reviewed commit 3d0b348](https://github.com/google/elephant-goldfish-model/tree/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669). The inspected `plugin.json` declares 0.1.0; this is not verification of a published release. The [license](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/LICENSE) is Apache-2.0. Google publishes the project without official product support.

## Capabilities and prerequisites

The plugin packages brainstorming, specification drafting, staged review, finding resolution, codebase documentation and drift-reporting instructions. See [Elephant-Goldfish design and review](../Approaches/Elephant-Goldfish%20design%20and%20review.md) for the mechanism.

The [harness guide](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/docs/harnesses.md) requires the complete plugin, including personas and standards. Review requires native fresh-context subagent support; an in-thread review does not meet that condition. Host setup and permissions remain prerequisites, and compatibility here is untested.

## Evidence limits and proposed trial

The [project's testing record](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/TESTING.md) reports packaging checks and selected native workflow fixtures. It records incomplete cloud traces for Cowork and ChatGPT Work. These project-reported checks concern installation and execution, not comparative engineering outcomes. The site's engineer-adoption claim was not independently verified.

Proposed trial: use a small existing design with independently known omissions. Compare ordinary review with fresh-context review, recording valid findings, false positives, repair effort and total cost. No plugin installation, tests or agent workflow ran for this review. Status remains `reviewed`.

Return to [Agentic Development](../Agentic%20Development.md).

## Record metadata

| Property | Value |
| --- | --- |
| type | resource |
| collection | agentic-development |
| status | reviewed |
| created | 2026-10-25 |
| updated | 2026-10-25 |
| tags | agentic-development; agentic-development/context; agentic-development/verification |
| resource_kind | agent-plugin |
| purpose | Candidate tooling for specification drafting, isolated review and documentation maintenance |
| url | https://github.com/google/elephant-goldfish-model |
| homepage | https://egm.dev/ |
| maintainer | Google LLC |
| evidence_family | elephant-goldfish-model |
| sources | [2026-04-27 - Dave Rensin - Elephants Goldfish and software engineering](../Articles/2026-04-27%20-%20Dave%20Rensin%20-%20Elephants%20Goldfish%20and%20software%20engineering.md) |
| themes | [Agent harnesses and verification](../Themes/Agent%20harnesses%20and%20verification.md) |
| approaches | [Elephant-Goldfish design and review](../Approaches/Elephant-Goldfish%20design%20and%20review.md) |
| availability | Public project site and repository accessible on the verification date |
| last_verified | 2026-10-25 |
| reviewed_revision | 3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669 |
| reviewed_version | 0.1.0 |
| license | Apache-2.0 |
| review_scope | Project site, README, license, plugin manifest, architecture, harness and Codex documentation, review skill and dispatch excerpts, comprehension persona and testing record; no installation or execution |
| local_observations |  |
