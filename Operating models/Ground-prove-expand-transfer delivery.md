---
type: operating-model
collection: fde
created: 2026-10-07
updated: 2026-10-07
tags:
- fde
- fde/execution
- fde/ownership
status: evolving
evidence_status: source-reported
mandate: Move one evidence-grounded use case into production, then enable customer-owned expansion
engagement_type: Ground, prove, expand, and transfer
ownership: Customer engineers co-build from discovery; completion requires independent delivery of the next use case
success_measure: A production use case and demonstrated ability for the receiving team to add another
sources:
- '[[Articles/2026-10-06 - CTERA - Forward deployed engineering for enterprise AI]]'
---

# Ground-prove-expand-transfer delivery

This name is a vault abstraction of CTERA's reported phases, not the vendor's label and not a validated general model.

## Reported model

[[Articles/2026-10-06 - CTERA - Forward deployed engineering for enterprise AI|CTERA's press release]] describes an embedded FDE and Deployment Strategist working with customer subject-matter experts and engineers:

| Phase | Reported purpose | Evidence to retain when transferring the model |
| --- | --- | --- |
| Ground | Discover the workflow and inspect the real data, systems, access patterns, and constraints. | A verified task, baseline, permissions, source systems, and named domain reviewers. |
| Prove | Put one bounded use case into production and validate it against real data. | Acceptance evidence, failure modes, an accountable operator, and observed workflow results. |
| Expand | Apply what was learned to additional workflows. | Evidence that the approach repeats without hiding new bespoke work or unsafe assumptions. |
| Transfer | Co-build and document throughout so the receiving team can continue independently. | The receiving team adds or changes the next use case without reliance on private vendor context. |

The evidence column is our proposed interpretation using the wider vault; CTERA does not specify all of these artifacts.

## Reusable insight

The first production use case is a learning wedge, not proof of generality. Expansion tests whether the approach is repeatable, while transfer tests whether that repeatability belongs to the receiving team. This makes "add the next use case" a stronger candidate handover demonstration than delivery plus documentation alone.

For work outside CTERA's data platform, generalise "start from the data" to "start from direct operating evidence." The relevant evidence may include user work, system behaviour, permissions, integrations, and organisational constraints as well as data.

## Fit and failure modes

A candidate when a bounded first use case can reach production, later use cases are plausibly related, and a receiving team can work alongside the FDE from discovery. It is weaker when the first case is cherry-picked, expansion means repeating bespoke implementation, the customer lacks authority or capacity to take over, or "independence" is tested only through configuration rather than operation and change.

Do not force expansion when one use case is sufficient. Do not defer ownership work to the final phase; the reported model starts co-building and documentation at the beginning.

## Comparison and unknowns

[[Operating models/Atlassian co-engineering]] uses Discover, Build, Adopt, and Value and explicitly includes sustained adoption and product improvement. This model instead foregrounds a first-to-next-use-case progression and an independence test. It is a concrete variant of [[Operating models/Customer-owned delivery]] and can coexist with [[Operating models/Outcome-scoped missions]].

No source yet establishes CTERA's decision rights, engagement duration, continuing support, customer outcomes, or whether field learning changes its core product. Treat those as unknowns rather than importing them from other operating models.

See [[Playbooks/Scope an engagement]], [[Playbooks/Evaluate outcomes and reuse]], and [[Playbooks/Prove a handover]]. Return to [[Operating models]].
