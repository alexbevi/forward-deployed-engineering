---
type: playbook
collection: fde
created: 2026-10-05
updated: 2026-10-20
tags:
  - fde
status: draft
practice_status: proposed
purpose: Start or reset an engagement
sources:
  - "[[Articles/2026-10-13 - OrNsoft team - How a forward-deployed engagement works]]"
  - "[[Articles/2026-10-16 - McKinsey - What is a forward-deployed engineer]]"
  - "[[Articles/undated - Kusum Motiani - What 133 companies reveal about FDE]]"
  - "[[Articles/2026-09-14 - Arun Prasath E G - FDE engagements for owners]]"
  - "[[Articles/2026-09-29 - Gartner - Vendor FDE abandonment forecast]]"
  - "[[Articles/2026-09-14 - Arun Prasath E G - What is an FDE]]"
  - "[[Articles/2026-03-18 - Carlos Becker - FDE evolution at HappyRobot]]"
  - "[[Articles/undated - Atlassian - Forward deployed engineering playbook]]"
  - "[[Articles/2026-10-06 - Jove Zhong - Building a world-class FDE team]]"
local_observations: []
---

# Scope an engagement

## When to use it

Before committing to delivery, or when scope, access, or responsibility changes. This procedure is our synthesis of the linked sources. It has not been tried locally.

## Preconditions

Have a business decision-maker and someone who understands the actual workflow. Identify the intended receiving team. If these are missing, record the gap before agreeing to a delivery plan.

## Procedure

1. Observe a representative task with its user, noting decisions and data. Describe the current problem, how often it occurs, and observable success condition. Ask the domain reviewer to correct that description.
2. List business decisions, engineering decisions, spending approvals, and authority over production changes. Name an owner for each.
3. Verify practical access to representative data and the systems involved. Record limitations and approval dependencies.
4. Define an initial usable increment, acceptance checks, a baseline, and a date to review progress. Where the choice is material, present alternatives with their effort, payoff, and limitations, including a smaller change or no change.
5. Agree what is excluded, who operates the result, and how support and transition will work. Record IP ownership, rights needed for maintenance and reuse, and how scope changes affect pricing and acceptance.
6. Review whether an existing product or a smaller advisory task would meet the need before building.

The [[Articles/undated - Atlassian - Forward deployed engineering playbook|Atlassian PDF, pages 10 and 12]], adds a problem-selection lens and early permission design. Record the intended agent action boundary before implementation.

## Artifact to leave

A short engagement brief with the problem, users, baseline, success checks, scope, owners, dependencies, exclusions, first increment, review date, and transition expectation.

For AI production work, propose a signed acceptance record with versioned evaluation examples and cut-over conditions. Allow diagnosis to end in a documented no-go. This adapts [[Articles/2026-10-13 - OrNsoft team - How a forward-deployed engagement works|OrNsoft's production definition]].

## Checks and failure modes

Can the customer explain the intended outcome and the decisions still theirs? Can an engineer access what delivery needs? An approval promise is not working access. A customer opportunity is not an approved scope change. Revisit decisions when facts change instead of treating the brief as permanent truth.

## Evidence and adaptation

The workflow-observation step adapts [[Articles/2026-10-16 - McKinsey - What is a forward-deployed engineer|Harrysson's account]].

[[Articles/undated - Kusum Motiani - What 133 companies reveal about FDE|GoodFirms' vendor checklist]] motivates the IP and scope-change checks. The proposed brief should name decisions the engineer can make, dependencies controlled by others, and an escalation owner when those dependencies block the agreed outcome.

The owner guide supplies a commercial practice; the overview offers reported cases; the mission account supplies a company-specific approach; Gartner supplies advice and forecasts; and Cresta supplies the option-menu pattern. They do not validate this combined procedure. Record local outcomes before changing practice_status to locally-tried.

Return to [[FDE#Executing more effectively]] and [[Operating models]].
