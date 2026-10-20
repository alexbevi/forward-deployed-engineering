---
type: article
collection: fde
status: reviewed
created: 2026-10-07
updated: 2026-10-07
tags:
- fde
- fde/research
- fde/agentic-ai
- fde/governance
- fde/evaluation
title: 'The Last Human Gate: Forward Deployed Engineering for Governance Automation'
author:
- Jeremy Canale
site: arXiv
url: https://arxiv.org/html/2609.29345v1
canonical_url: https://arxiv.org/abs/2609.29345v1
primary_source_url: https://arxiv.org/html/2609.29345v1
pdf_url: https://arxiv.org/pdf/2609.29345v1
source_format: html
publication_date: 2026-09-24
publication_date_basis: 'arXiv submission history: v1 submitted 24 September 2026; this is a submission date, not a journal publication date'
accessed: 2026-10-07
source_kind: research-paper
arxiv_id: '2609.29345'
arxiv_version: v1
research_status: preprint
venue: null
review_status_basis: arXiv record inspected; peer-reviewed venue not established
benchmark_release: dgf-bench-300-20260923
evidence_family: arxiv-2609-29345
evidence_basis:
- synthetic-benchmark
- formal-accounting-framework
- author-hypothesis
contribution: Separates accepted task execution, whole-route reliability, and net human-work substitution while specifying a governed task-transfer contract
themes:
- '[[Themes/Field discovery and execution]]'
- '[[Themes/Technical and professional development]]'
approaches:
- '[[Approaches/Contract-based governed task transfer]]'
playbooks:
- '[[Playbooks/Stage agent autonomy]]'
- '[[Playbooks/Evaluate outcomes and reuse]]'
resources:
- '[[Resources/DGF-Bench repository]]'
models: []
people:
- '[[People/Jeremy Canale]]'
attachments: []
text_indexes: []
---

# The Last Human Gate

[Reviewed HTML version](https://arxiv.org/html/2609.29345v1) · [Submission record](https://arxiv.org/abs/2609.29345v1) · [PDF](https://arxiv.org/pdf/2609.29345v1).

## Contribution

Canale treats a governance gate as a review contract: permitted evidence and tools, a versioned policy, an authorization mandate, acceptance conditions, and an output containing the disposition, findings, actions, supporting evidence, and authorization record. Transferring its execution to software requires adequate information, valid output across the declared population, and authority for any effective commitment. A correct refusal can therefore be a successful review, while an approval without required evidence or authority is not.

The proposed FDE implementation separates agent investigation from deterministic policy execution, evidence services, authority enforcement, and exception handling. It begins with a bounded task and representative acceptance cases, preserves open obligations across handoffs, and defines stopping conditions before expanding automation. [[Approaches/Contract-based governed task transfer]] extracts this method without adopting the paper's governance-first adoption hypothesis.

The paper also distinguishes three claims that need different evidence:

| Claim | Required observation |
| --- | --- |
| Contract execution | An accepted decision, findings, actions, evidence, and mandate for one review occurrence. |
| Workflow reliability | Every required gate succeeds and repeated trajectories remain dependable. |
| Net task substitution | Comparable accepted output and quality require fewer total human hours after exceptions, verification, correction, and recurring support are counted. |

## Reported experiment

DGF-Bench generates 300 synthetic Buy, Integrate, and Build projects. The experiment reports 899 evaluable model-project runs, with 1,700 scheduled gate occurrences per complete model condition. Strict gate success is 94.98% for Gemini 3.8 Flash, 83.29% for GPT-5.6 Luna, and 74.18% for DeepSeek v4.1 Flash; complete-route success falls to 76.92%, 42.33%, and 24.67%. A deterministic control passes all 1,700 gates and 300 routes using the supplied policies and structured facts.

The control is important: under this prepared information condition, the represented decision kernel is executable without model calls. The experiment therefore does not establish an incremental LLM advantage for structured rule execution. Evidence conformity accounts for many model failures, while some errors change decisions or miss critical findings. A follow-up runs three additional trajectories for each of 15 existing dossiers; it tests repeatability but does not add independent projects.

## Perspective and limits

The policy, generator, and evaluator share one declared rule system, and the cases are synthetic and sampled for decision coverage rather than enterprise frequency. Human-review performance, deployment effort, operating labor, customer outcomes, and staffing changes are not measured. The strongest supported claim is bounded technical feasibility for executing specified review contracts in the engineered environment.

The paper's prediction of at least 80% fewer workload-equivalent Digital Governance Framework FTE by 20 September 2033 is an author-selected, falsifiable hypothesis, not an extrapolation from benchmark scores. No enterprise cohort is enrolled and the historical baseline would require auditable records. The two manuscripts in [[Resources/DGF-Bench repository]] share one experimental record and must not be counted as independent studies.

## Proposed application

Use [[Approaches/Contract-based governed task transfer]] to define a bounded automation candidate before choosing an agent architecture. [[Playbooks/Stage agent autonomy]] applies its evidence, policy, mandate, and stopping checks; [[Playbooks/Evaluate outcomes and reuse]] keeps behaviour, whole-workflow reliability, and complete human effort separate. No local trial is recorded.
