# Stage agent autonomy

## When to use it

When defining an agent's initial action scope or considering more autonomy. This is our proposed adaptation of the source, not a validated procedure or a universal requirement to progress toward automation.

## Source idea

[PDF page 12](../Attachments/atlassian-fde-playbook-c9cd5956a217.pdf#page=12) distinguishes Read, Draft, and Act. Consult the PDF for the original description.

[Canale](../Articles/2026-09-24%20-%20Jeremy%20Canale%20-%20The%20Last%20Human%20Gate.md) adds a governed-transfer contract: define the task population, information, output, policy version, mandate, acceptance conditions, residual human path, and stopping criteria before treating software as the task executor. The paper tests synthetic review contracts, not this playbook in production.

## Procedure

1. Identify the task population, authoritative evidence, output record, affected people, permission owners, and possible consequences of error. Name work that remains outside the transfer.
2. Decide whether the agent may only retrieve information, propose actions for approval, or execute a bounded action. Staying at the first two levels may be the right outcome.
3. Record the applicable policy version and mandate. Separate what the agent proposes from the mechanism that makes, constrains, or rejects a commitment.
4. Make audit evidence, exception context, escalation, containment, and recovery explicit for the chosen action scope.
5. Test representative authorised, unauthorised, incomplete, conflicting, and out-of-scope cases. Report accepted and escalated volumes; escalation of every case is not task transfer.
6. Agree stopping conditions for unsupported material findings, lost obligations, inaccessible required sources, unauthorized commitments, and persistent quality or service deterioration.
7. Review operational outcomes and residual human effort with the accountable owner before changing permissions or action scope. Revisit the decision when policies, sources, tools, or models change.

## Artifact and checks

Leave a decision record naming the task and action boundaries, evidence and policy versions, mandate, owner, checks, residual path, stopping conditions, and uncertainty. A successful demonstration or increased user trust alone does not establish that broader autonomy is appropriate.

No local use is recorded. Return to [Playbooks](../Playbooks.md) and [FDE](../FDE.md#executing-more-effectively).

## Record metadata

| Property | Value |
| --- | --- |
| collection | fde |
| created | 2026-10-06 |
| updated | 2026-10-07T08:35 |
| tags | fde |
| type | playbook |
| status | draft |
| practice_status | proposed |
| purpose | Choose and review the actions an agent may take |
| sources | [undated - Atlassian - Forward deployed engineering playbook](../Articles/undated%20-%20Atlassian%20-%20Forward%20deployed%20engineering%20playbook.md); [2026-09-24 - Jeremy Canale - The Last Human Gate](../Articles/2026-09-24%20-%20Jeremy%20Canale%20-%20The%20Last%20Human%20Gate.md) |
| local_observations |  |
