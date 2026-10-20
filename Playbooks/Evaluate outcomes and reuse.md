# Evaluate outcomes and reuse

## When to use it

When deciding whether an AI capability works, improves a workflow, or merits shared product investment. This is a proposed review procedure, not a benchmark supplied by any one source.

## Preconditions

Define representative cases, an operational baseline, people who can judge business correctness, and an owner who can act on findings. If another deployment is unavailable, keep reuse as a hypothesis.

## Procedure

1. Evaluate behaviour against explicit criteria, including incomplete evidence, uncertainty, and relevant failure cases. Investigate failures and retain useful regression cases.
2. Observe the workflow. Compare total effort, mistakes, review burden, sustained adoption, operating costs, and agreed outcomes with the baseline. Count exception handling, ordinary review, correction, recurring engineering, and supplier effort across the common process boundary.
3. Decide whether the underlying cause needs an agent change, an integration change, or an authorised process change.
4. Separate a candidate shared capability from customer-specific assumptions and configuration. Record what would falsify the reuse hypothesis.
5. Test the candidate under another customer's conditions when possible. Document adaptations and failures rather than counting deployment alone as proof of generality.
6. Re-evaluate behaviour and workflow outcomes after a change, and report the remaining uncertainty.

The [Atlassian PDF, pages 14–17](../Articles/undated%20-%20Atlassian%20-%20Forward%20deployed%20engineering%20playbook.md), motivates separating launch curiosity from continued use and examining context and compute costs alongside displaced effort.

[Canale](../Articles/2026-09-24%20-%20Jeremy%20Canale%20-%20The%20Last%20Human%20Gate.md) further separates accepted task execution, complete-route reliability, and net human-work substitution. A high success or coverage rate does not estimate labor removed when difficult exceptions, verification, rework, or maintenance retain a disproportionate share of effort.

[Cresta](../Articles/2026-10-06%20-%20Jove%20Zhong%20-%20Building%20a%20world-class%20FDE%20team.md) reports creating evaluation sets from real conversations and moving recurring patterns, connectors, and workflow improvements into a shared platform. This supports linking evaluation findings to reuse decisions while keeping their evidence separate: the article does not show evaluation results or demonstrate that a shared capability succeeds under another customer's conditions.

## Artifact to leave

A review with separate behaviour results, operational results, reuse evidence, proposed changes, and decision owners. Include the measurement period and conditions.

## Checks and failure modes

Passing agent checks does not establish business benefit. Faster execution can increase human review cost. A second customer asking for a feature does not prove a shared implementation fits. This review does not grant authority to change a customer's policies.

Return to [FDE](../FDE.md#what-good-looks-like) and [Product-oriented FDE](../Operating%20models/Product-oriented%20FDE.md).

## Record metadata

| Property | Value |
| --- | --- |
| type | playbook |
| collection | fde |
| created | 2026-10-05 |
| updated | 2026-10-09T10:42 |
| tags | fde |
| status | draft |
| practice_status | proposed |
| purpose | Review a deployed capability or proposed product improvement |
| sources | [2026-09-21 - Pablo Bermejo - Turning intelligence into lasting value](../Articles/2026-09-21%20-%20Pablo%20Bermejo%20-%20Turning%20intelligence%20into%20lasting%20value.md); [2026-09-12 - Vinoo Ganesh - The rise of the forward deployed engineer](../Articles/2026-09-12%20-%20Vinoo%20Ganesh%20-%20The%20rise%20of%20the%20forward%20deployed%20engineer.md); [2026-10-01 - Karthik Sonti et al - FDE pathways for AWS partners](../Articles/2026-10-01%20-%20Karthik%20Sonti%20et%20al%20-%20FDE%20pathways%20for%20AWS%20partners.md); [2026-03-18 - Carlos Becker - FDE evolution at HappyRobot](../Articles/2026-03-18%20-%20Carlos%20Becker%20-%20FDE%20evolution%20at%20HappyRobot.md); [undated - Atlassian - Forward deployed engineering playbook](../Articles/undated%20-%20Atlassian%20-%20Forward%20deployed%20engineering%20playbook.md); [2026-09-24 - Jeremy Canale - The Last Human Gate](../Articles/2026-09-24%20-%20Jeremy%20Canale%20-%20The%20Last%20Human%20Gate.md); [2026-10-06 - Jove Zhong - Building a world-class FDE team](../Articles/2026-10-06%20-%20Jove%20Zhong%20-%20Building%20a%20world-class%20FDE%20team.md) |
| local_observations |  |
