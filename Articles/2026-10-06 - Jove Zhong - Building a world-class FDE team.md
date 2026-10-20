---
type: article
title: How Cresta Built a World-Class Forward Deployed Engineering Team in a Year
author:
- Jove Zhong
author_role: Head of Forward Deployed Engineering
site: Cresta
url: https://cresta.com/blog/building-a-world-class-fde-team
canonical_url: https://cresta.com/blog/building-a-world-class-fde-team
publication_date: 2026-10-06
publication_date_basis: Visible article date on the supplied page
accessed: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
status: reviewed
source_kind: practitioner-case-study
tags:
- fde
- fde/role
- fde/discovery
- fde/execution
- fde/product-feedback
- fde/evaluation
- fde/development
- fde/agentic-ai
themes:
- '[[Themes/Role and product feedback]]'
- '[[Themes/Field discovery and execution]]'
- '[[Themes/Technical and professional development]]'
collection: fde
evidence_family: cresta-fde-operating-account
evidence_basis:
- reported-experience
- practitioner-argument
contribution: Adds an engineering-owned FDE model linking field delivery, evaluations, and shared product reuse
models:
- '[[Operating models/Product-oriented FDE]]'
playbooks:
- '[[Playbooks/Scope an engagement]]'
- '[[Playbooks/Evaluate outcomes and reuse]]'
people:
- '[[People/Jove Zhong]]'
---

# Building a world-class FDE team

[Read the article](https://cresta.com/blog/building-a-world-class-fde-team).

## Summary

Zhong describes Cresta's FDE function as an engineering-owned team responsible for closing the gap between an AI prototype and a production system. The gap includes domain language, edge cases, labelled data, representative tests, permissions, compliance, integrations, and failure handling. Cresta expects each FDE to combine business judgment with the technical ability to build the most complete option, then present customers with alternatives that expose effort and payoff, including a smaller change or no change.

The reported delivery sequence combines onsite kickoff and discovery, remote building and evaluation, onsite acceptance, and live operation. FDEs meet process owners, observe work, map systems and controls, test against historical conversations, conduct user acceptance work, and then monitor and optimise in production. Zhong reports that customer trips usually last two to three days and no more than about five, while deployments generally reach production in one to three months.

Projects reportedly use two or three FDEs: one owns technical design and key implementation, another reviews and handles adjacent use cases, and an occasional third advises. An FDE commonly works on two to four projects. Cresta says it will not ship without vertical-specific evaluations because a model, prompt, or toolset that works in one domain may fail in another.

## Product compounding mechanism

Cresta places FDE inside Product Engineering and allows FDEs to contribute directly to the product. Recurring task patterns become reusable skills; missing connectors, workflow friction, and hard-to-judge model behaviour can become platform changes or evaluation sets. Because deployments share a platform rather than customer-specific forks, the company argues that later engagements should start with more reusable capability than earlier ones.

This strengthens [[Operating models/Product-oriented FDE]] with a concrete organisational mechanism: field engineers need an accepted contribution path into maintained product code, not only a mandate to report customer learning.

## Selection and development signals

Cresta interviews experienced candidates with production scenarios rather than testing coding proficiency alone. Questions about agent failures and unsuitable feature requests are intended to reveal vertical knowledge and customer-facing maturity, including how someone communicates bad news or says no while preserving trust. Using similar scenarios for peer learning is a vault adaptation; the article describes selection, not evidence that the method develops those capabilities.

## Perspective and limits

This is a company-authored account and recruiting article. Team growth from one to more than fifty people, typical deployment time, a twelve-to-eight-to-six-week acceleration example, awards, customer value, and the claim of a "world-class" team are not supported by methods, baselines, comparative data, or detailed engagement results in the article. Availability on a shared platform does not by itself establish reuse, improvement for another customer, or freedom from regressions.

The article names evaluation activities but provides no evaluation criteria, results, or launch thresholds. It also does not describe customer ownership, handover, maintenance boundaries, or engagement exit. It therefore supports product-oriented delivery and field-to-product learning, not a claim of customer independence.

## Connections

Compare [[Articles/2026-09-12 - Vinoo Ganesh - The rise of the forward deployed engineer|Ganesh's product-oriented definition]], [[Articles/2026-03-24 - Doug McClure - How FDE was born at PagerDuty|PagerDuty's product-team contribution path]], and [[Articles/2026-03-18 - Carlos Becker - FDE evolution at HappyRobot|HappyRobot's outcome-scoped missions]]. [[Playbooks/Scope an engagement]] adapts the option menu, while [[Playbooks/Evaluate outcomes and reuse]] retains separate evidence tests for behaviour, workflow value, and cross-customer reuse.
