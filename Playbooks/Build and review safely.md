# Build and review safely

## When to use it

When entering an unfamiliar codebase or delivery process. These are proposed practices informed by reported engagements, not proof that automated review guarantees correctness.

## Procedure

1. Learn the maintainer's standards, contribution boundaries, acceptance criteria, and release process before changing code.
2. Take a small usable change through the actual build, review, and deployment path. Resolve process gaps before increasing scope.
3. Where useful, put third-party services behind explicit interfaces and deterministic test stand-ins. Keep stand-in behaviour distinct from live integration evidence.
4. Encode suitable quality checks in the build, and supplement them with human or automated review appropriate to the risk.
5. Record findings and their disposition. Examine the running behaviour when source inspection alone cannot answer the question.
6. Verify the real integration when access arrives. Make unavailable production dependencies visible; never let a test stand-in masquerade as successful live work.

## Artifact to leave

A small accepted contribution, known checks and limitations, integration evidence, and a short record of lessons another engineer can use.

## Checks and failure modes

Clean lint output does not establish runtime safety. A mock verifies only the assumptions encoded in it. Coding agents can introduce new errors while fixing old ones. Customer urgency does not override the maintainer's ownership or release rules.

## Evidence

The APEG account reports gates, stand-ins, and repeated review corrections. PagerDuty reports learning feature-team practices and contribution boundaries. We have not reproduced either team's tooling.

Return to [FDE](../FDE.md#developing-strong-fde-peers) and [PagerDuty AI Delivery Workbench](../Resources/PagerDuty%20AI%20Delivery%20Workbench.md).

## Record metadata

| Property | Value |
| --- | --- |
| type | playbook |
| collection | fde |
| created | 2026-10-05 |
| updated | 2026-10-05 |
| tags | fde |
| status | draft |
| practice_status | proposed |
| purpose | Develop an unfamiliar integration or contribute to shared product code |
| sources | [2026-09-14 - Arun Prasath E G - How an FDE engagement works](../Articles/2026-09-14%20-%20Arun%20Prasath%20E%20G%20-%20How%20an%20FDE%20engagement%20works.md); [2026-03-24 - Doug McClure - How FDE was born at PagerDuty](../Articles/2026-03-24%20-%20Doug%20McClure%20-%20How%20FDE%20was%20born%20at%20PagerDuty.md) |
| local_observations |  |
