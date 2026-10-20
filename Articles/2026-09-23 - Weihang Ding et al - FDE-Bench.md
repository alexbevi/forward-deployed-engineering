---
type: article
collection: fde
status: reviewed
created: '2026-10-06'
updated: '2026-10-06'
tags:
- fde
- fde/research
- fde/deployment
title: 'FDE-Bench: Evaluating LLM Agents for Deployment Environment Configuration'
author:
- Weihang Ding
- Junfei Zhan
- Yueting Li
- Qirong Guo
site: arXiv
url: https://arxiv.org/html/2609.27571v1
canonical_url: https://arxiv.org/abs/2609.27571v1
primary_source_url: https://arxiv.org/html/2609.27571v1
source_format: html
publication_date: '2026-09-23'
publication_date_basis: 'arXiv submission history: v1 submitted 23 September 2026; this is a submission date, not
  a journal publication date'
accessed: '2026-10-06'
source_kind: research-paper
arxiv_id: '2609.27571'
arxiv_version: v1
research_status: preprint
venue: null
review_status_basis: arXiv record inspected; peer-reviewed venue not established
benchmark_version: v1.1
evidence_family: arxiv-2609-27571
evidence_basis:
- reported-experiment
contribution: Provides a candidate method for evaluating deployment reproducibility
themes:
- '[[Themes/Field discovery and execution]]'
- '[[Themes/Technical and professional development]]'
approaches:
- '[[Approaches/Deployment verification through fresh replay]]'
playbooks:
- '[[Playbooks/Rehearse a deployment from delivered artifacts]]'
resources:
- '[[Resources/FDE-Bench development repository]]'
models: []
people: []
attachments: []
text_indexes: []
---

# FDE-Bench

[Reviewed HTML version](https://arxiv.org/html/2609.27571v1) · [Submission record](https://arxiv.org/abs/2609.27571v1).

## Contribution and limits

The paper evaluates 136 deployment-configuration tasks through fresh replay of submitted artifacts. Checks distinguish build, readiness, behaviour and specification conformance. Seven models resolve 52.9–75.0% of tasks. Readiness is the largest failure stage. See [protocol](https://arxiv.org/html/2609.27571v1#S3) and [experiments](https://arxiv.org/html/2609.27571v1#S4).

These are author-reported sandbox results, not a measure of the whole FDE role. Single episodes do not estimate run-to-run variation; the human comparison has one participant and a richer interface. Repository code and results were not reproduced. See [limitations](https://arxiv.org/html/2609.27571v1#S6).

The reviewed arXiv version is v1; its benchmark revision is v1.1. These are separate version identifiers.

## Proposed application

[[Approaches/Deployment verification through fresh replay]] informs [[Playbooks/Rehearse a deployment from delivered artifacts]]. This is a candidate delivery practice, with no local observations. It does not define an engagement operating model.

## Resource lead

[[Resources/FDE-Bench development repository]] tracks the repository named in the paper. Its contents have not been inspected.
