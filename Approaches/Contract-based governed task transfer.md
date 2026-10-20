---
type: approach
collection: fde
status: evolving
created: 2026-10-07
updated: 2026-10-07
tags:
- fde
- fde/research
- fde/agentic-ai
- fde/governance
purpose: Define and test a bounded transfer of accepted work from people to software without losing evidence, authority, or residual labor
mechanism: Specify an executable task contract, engineer its information and authority interfaces, and evaluate accepted output, route reliability, and complete human work separately
application_scope: Recurring review or decision workflows with explicit evidence, policies, mandates, and outputs
evidence_status: source-reported
application_status: proposed
sources:
- '[[Articles/2026-09-24 - Jeremy Canale - The Last Human Gate]]'
playbooks:
- '[[Playbooks/Stage agent autonomy]]'
- '[[Playbooks/Evaluate outcomes and reuse]]'
resources:
- '[[Resources/DGF-Bench repository]]'
local_observations: []
---

# Contract-based governed task transfer

## Research basis

[[Articles/2026-09-24 - Jeremy Canale - The Last Human Gate|Canale]] defines a review contract through permitted evidence and tools, versioned policy, authorization mandate, acceptance conditions, and a required output record. The paper's synthetic benchmark measures specified governance reviews; it does not demonstrate this approach in a live enterprise.

## Proposed use in FDE work

Before building an agent for a recurring review or decision task:

1. Name the transferred task and population. Specify where it begins and ends, the input cases, output record, service criteria, and work that remains outside scope.
2. Define the information interface. Identify authoritative sources, accessible representations, versions, conflicts, and the allowed response when a necessary fact is missing.
3. Separate interpretation from enforcement. Decide what an agent investigates, what deterministic policy evaluates, what evidence service preserves provenance, and what authority mechanism makes or rejects commitments.
4. Fix representative acceptance cases. Include valid, deficient, incomplete, conflicting, unauthorized, and out-of-scope inputs. Test complete routes and repeated trajectories when handoffs or stochastic execution matter.
5. Design the residual path. Give people enough context to resolve exceptions without reconstructing the whole case. Record accepted, escalated, corrected, and failed work separately.
6. Define containment and stopping conditions. Unsupported material findings, unauthorized commitments, lost obligations, inaccessible required sources, or persistent quality deterioration should trigger an agreed response.
7. Evaluate separate claims. Report task acceptance, end-to-end reliability, and total human work without substituting one measure for another.

This sequence adapts the paper's governance implementation to a broader class of bounded tasks. It is not evidence that all professional judgment can or should become an executable contract.

## Fit and failure modes

The approach is a candidate when inputs and outputs recur, policies and decision rights can be named, evidence is accessible, and acceptance can be observed. It is weaker when material knowledge remains tacit, policy conflicts are unresolved, commitments require non-delegable judgment, or the case population changes faster than its interfaces can be maintained.

A narrow automated path can still be useful, but excluded work must remain visible. Escalating every difficult case may preserve safety while transferring little work. High task success may coexist with poor route reliability, and broad case coverage may leave most human labor in costly exceptions.

## Evidence to collect

Retain the contract and versions used, representative-case results, evidence and authorization traces, route and repeated-run outcomes, exception effort, ordinary review, rework, recurring maintenance, supplier effort, and transition cost. Count shared work once across the common process boundary.

No local application is recorded. Use [[Playbooks/Stage agent autonomy]] for action boundaries and [[Playbooks/Evaluate outcomes and reuse]] for operational evaluation. Return to [[Approaches]] and [[FDE#Executing more effectively]].
