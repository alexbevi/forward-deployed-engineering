---
type: article
collection: agentic-development
title: Software is slow because of bad design, not slow languages
author:
  - Sean Goedecke
site: seangoedecke.com
url: https://www.seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages/
canonical_url: null
publication_date: 2026-10-23
publication_date_basis: Visible date in the article header
source_updated: null
source_updated_basis: No modification date declared in the inspected HTML
accessed: 2026-10-25
created: 2026-10-25
updated: 2026-10-25
status: reviewed
source_kind: practitioner-article
evidence_family: sean-goedecke-performance-design-2026
evidence_basis:
  - practitioner-argument
  - reported-experience
  - hypothetical-example
contribution: Directs agent-assisted optimisation toward measured workload constraints
tags:
  - agentic-development
  - agentic-development/performance
themes:
  - "[[Themes/Agent-assisted performance engineering]]"
models: []
approaches: []
playbooks: []
people: []
resources: []
role_applications: []
---

# Performance design before language rewrites

[Read Sean Goedecke's article](https://www.seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages/), published October 23, 2026.

## Contribution and limits

Goedecke recommends profiling an agent's optimisation target before choosing a rewrite. His examples favour reducing repeated work and changing data access or data structures; CPU-bound hotspots can still justify a faster language.

The argument draws on practitioner experience, illustrative calculations and secondary anecdotes, not a controlled agent evaluation. In an addendum he acknowledges contested assumptions about I/O-bound CRUD workloads and the limited company sample behind his flamegraph experience. Measure the workload; the title is not a universal rule.

## Placement and verification

Filed in [[Agentic Development]] through [[Themes/Agent-assisted performance engineering]] for its explicit coding-agent application. It establishes no role-specific FDE or Staff conclusion. No separate procedure or local result is recorded.

Full article and addendum reviewed on October 25, 2026. Direct HTML confirms the title, author header and publication date; no canonical link was declared. Linked benchmark repositories and discussion threads were not independently reviewed or reproduced.
