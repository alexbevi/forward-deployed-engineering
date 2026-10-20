---
type: playbook
collection: fde
status: draft
created: '2026-10-06'
updated: '2026-10-06'
tags:
- fde
- fde/research
- fde/deployment
purpose: Test whether another engineer can deploy the delivered package
practice_status: proposed
sources:
- '[[Articles/2026-09-23 - Weihang Ding et al - FDE-Bench]]'
approaches:
- '[[Approaches/Deployment verification through fresh replay]]'
local_observations: []
---

# Rehearse a deployment from delivered artifacts

This is our proposed application of [[Approaches/Deployment verification through fresh replay]].

## Preconditions

Agree a disposable environment, authorised test data, dependency access, cost limit and cleanup owner. Identify exclusions such as a production-only migration.

## Procedure

1. Freeze the delivery package and acceptance criteria. Name external dependencies and their owners.
2. Ask a receiving engineer to deploy it in the agreed environment using the package and documented instructions. Record each extra action or missing input.
3. Run the acceptance checks. Include a customer-relevant transaction and a deliberate failure when appropriate; record what each check actually establishes.
4. Separate package defects, environment differences and faulty checks. Repair the affected part and repeat it.
5. Record acceptance, remaining gaps and cleanup. Link the result to [[Playbooks/Prove a handover]].

## Artifact and limits

Leave a versioned rehearsal record with checks, logs, interventions, exclusions and owners. Passing establishes only the conditions exercised. Record customer value separately in [[Playbooks/Evaluate outcomes and reuse]].

No local trial has been recorded. This exercise does not require running the research benchmark.
