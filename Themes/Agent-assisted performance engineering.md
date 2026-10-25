# Agent-assisted performance engineering

How should agents investigate and improve performance while preserving required behaviour?

## Catalogue

- [Goedecke, 2026](../Articles/2026-10-23%20-%20Sean%20Goedecke%20-%20Performance%20design%20before%20language%20rewrites.md). Practitioner argument for profiling before language rewrites, with workload-dependent exceptions.

## Connections

[Agent harnesses and verification](Agent%20harnesses%20and%20verification.md) asks how agent output should be checked. This theme adds a candidate investigation: establish representative performance and correctness checks before accepting an optimisation. No local comparison has tested that workflow.

## Questions to investigate

- Which workloads and correctness checks represent the intended use?
- Can an agent distinguish a measured bottleneck from an attractive rewrite target?
- Does the accepted improvement survive realistic load and operating costs?

Return to [Agentic Development](../Agentic%20Development.md).

## Record metadata

| Property | Value |
| --- | --- |
| type | theme |
| collection | agentic-development |
| status | evolving |
| created | 2026-10-25 |
| updated | 2026-10-25 |
| tags | agentic-development; agentic-development/performance |
