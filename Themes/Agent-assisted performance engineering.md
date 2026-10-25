---
type: theme
collection: agentic-development
status: evolving
created: 2026-10-25
updated: 2026-10-25
tags:
  - agentic-development
  - agentic-development/performance
---

# Agent-assisted performance engineering

How should agents investigate and improve performance while preserving required behaviour?

## Catalogue

- [[Articles/2026-10-23 - Sean Goedecke - Performance design before language rewrites|Goedecke, 2026]]. Practitioner argument for profiling before language rewrites, with workload-dependent exceptions.

## Connections

[[Themes/Agent harnesses and verification]] asks how agent output should be checked. This theme adds a candidate investigation: establish representative performance and correctness checks before accepting an optimisation. No local comparison has tested that workflow.

## Questions to investigate

- Which workloads and correctness checks represent the intended use?
- Can an agent distinguish a measured bottleneck from an attractive rewrite target?
- Does the accepted improvement survive realistic load and operating costs?

Return to [[Agentic Development]].
