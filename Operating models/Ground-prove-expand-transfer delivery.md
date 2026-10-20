# Ground-prove-expand-transfer delivery

This name is a vault abstraction of CTERA's reported phases, not the vendor's label and not a validated general model.

## Reported model

[CTERA's press release](../Articles/2026-10-06%20-%20CTERA%20-%20Forward%20deployed%20engineering%20for%20enterprise%20AI.md) describes an embedded FDE and Deployment Strategist working with customer subject-matter experts and engineers:

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

[Atlassian co-engineering](Atlassian%20co-engineering.md) uses Discover, Build, Adopt, and Value and explicitly includes sustained adoption and product improvement. This model instead foregrounds a first-to-next-use-case progression and an independence test. It is a concrete variant of [Customer-owned delivery](Customer-owned%20delivery.md) and can coexist with [Outcome-scoped missions](Outcome-scoped%20missions.md).

No source yet establishes CTERA's decision rights, engagement duration, continuing support, customer outcomes, or whether field learning changes its core product. Treat those as unknowns rather than importing them from other operating models.

See [Scope an engagement](../Playbooks/Scope%20an%20engagement.md), [Evaluate outcomes and reuse](../Playbooks/Evaluate%20outcomes%20and%20reuse.md), and [Prove a handover](../Playbooks/Prove%20a%20handover.md). Return to [Operating models](../Operating%20models.md).

## Record metadata

| Property | Value |
| --- | --- |
| type | operating-model |
| collection | fde |
| created | 2026-10-07 |
| updated | 2026-10-07 |
| tags | fde; fde/execution; fde/ownership |
| status | evolving |
| evidence_status | source-reported |
| mandate | Move one evidence-grounded use case into production, then enable customer-owned expansion |
| engagement_type | Ground, prove, expand, and transfer |
| ownership | Customer engineers co-build from discovery; completion requires independent delivery of the next use case |
| success_measure | A production use case and demonstrated ability for the receiving team to add another |
| sources | [2026-10-06 - CTERA - Forward deployed engineering for enterprise AI](../Articles/2026-10-06%20-%20CTERA%20-%20Forward%20deployed%20engineering%20for%20enterprise%20AI.md) |
