---
type: article
collection: fde
title: "Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL"
author:
  - Marianne Menglin Liu
  - Rongguang Wang
  - Zheng Wang
  - Yewen Wang
  - Leonid Boytsov
  - Tao Sheng
  - Sujith Ravi
  - Dan Roth
site: arXiv
affiliation_as_displayed: Oracle AI
url: https://arxiv.org/html/2611.03551v1
canonical_url: https://arxiv.org/abs/2611.03551v1
primary_source_url: https://arxiv.org/html/2611.03551v1
source_format: html
publication_date: 2026-11-02
publication_date_basis: arXiv submission history; v1 submitted November 2, 2026, not a journal publication date
accessed: 2026-11-04
created: 2026-11-04
updated: 2026-11-04
status: reviewed
source_kind: research-paper
arxiv_id: "2611.03551"
arxiv_version: v1
research_status: preprint
venue: null
review_status_basis: arXiv record inspected; peer-reviewed venue not established
evidence_family: arxiv-2611-03551
evidence_basis:
  - reported-experiment
contribution: Tests requirement discovery separately from delivery acceptance
tags:
  - fde
  - fde/research
  - fde/discovery
  - fde/execution
themes:
  - "[[Themes/Field discovery and execution]]"
playbooks:
  - "[[Playbooks/Scope an engagement]]"
approaches: []
models: []
people: []
resources: []
attachments: []
text_indexes: []
---

# FDE agent requirement discovery and delivery

[Version and authors](https://arxiv.org/abs/2611.03551v1). Reviewed the HTML methods, results, limitations and supporting appendices on November 4, 2026.

One engagement grounds a Gemini 2.5 Pro simulator with 17 known facts and six unknown decisions. Discovery tests 15 models, ten runs per opening profile. Pooled recovery is 60%; 21.2% of disclosed facts disappear from submissions. Gemini 2.5 Flash judges recovery; a 51-fact human audit agrees on 70.6% of labels. See [protocol](https://arxiv.org/html/2611.03551v1#A1) and [scoring](https://arxiv.org/html/2611.03551v1#A3).

Delivery compares four backbones in frozen-plan and autonomous OpenCode 1.18.4 workflows under a 12-hour A100 cap. Two of eight main runs pass: Spider accuracy ≥60%, production compilation failures ≤10%, CPU p90 <15s. GPT-6.1 Sol's six-run subset passes once. Human baseline reflects four months' work. See [delivery](https://arxiv.org/html/2611.03551v1#S4.SS3) and [repeats](https://arxiv.org/html/2611.03551v1#A6).

Compilation validity does not establish semantic correctness; the 100 production questions lack reference SQL. Unknown decisions do not count toward recovery. This single-case preprint cannot establish role replacement. Code and results were not reproduced. See [constraints](https://arxiv.org/html/2611.03551v1#A2).

[[Playbooks/Scope an engagement]] adapts the discovery check as a proposal. [[FDE#What good looks like]] connects it to the existing evidence rubric. No separate operating model or local experiment is warranted.
