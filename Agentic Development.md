# Agentic development

This collection develops subject-matter knowledge about building software with agents and engineering agentic systems. It covers agent architecture, context and memory, harnesses, verification, workflows, reliability and economics. It separates source claims, our interpretation, proposed practices and observed results.

[FDE](FDE.md) and [Staff Engineer](Staff%20Engineer.md) remain separate role syntheses. A technical method can be relevant to either without establishing a claim about that role. Qualified applications belong beside their assumptions and evidence; domain sources do not automatically enter the role catalogues.

## Initial working position

Separate feedback used while an agent builds from the independent checks used to accept its output. [Jain's experiment](Articles/2026-10-13%20-%20Naresh%20Jain%20-%20Are%20Harnesses%20Worth%20the%20Cost.md) motivates investigating feedback cadence against task outcomes and total cost; it does not establish a universal model-selection rule.

Before adopting a workflow, ask which requirements the checks cover, which failure modes remain unobserved, who defined the expected results, and what human effort the cost accounting leaves out. These are questions for investigation, not a locally validated procedure.

[Kimani](Articles/2026-10-12%20-%20Robert%20Kimani%20-%20Your%20engineering%20strategy%20has%20a%20new%20failure%20mode.md) adds a system-level question: does faster implementation increase accepted delivery, or move the constraint downstream? His assumption register is practitioner guidance, not a validated intervention.

For agent-assisted optimisation, [Goedecke](Articles/2026-10-23%20-%20Sean%20Goedecke%20-%20Performance%20design%20before%20language%20rewrites.md) suggests measuring the workload before choosing a language rewrite. Treat this as a candidate workflow; benefits and correctness remain untested here.

[EGM](Approaches/Elephant-Goldfish%20design%20and%20review.md) adds a proposed boundary between context-rich design and fresh-context review. Conversation isolation can expose unstated assumptions, but it does not establish independent correctness or replace acceptance evidence. Its essay and plugin share provenance.

## Reading and evidence

Start with [Agent harnesses and verification](Themes/Agent%20harnesses%20and%20verification.md) and [Agent-assisted performance engineering](Themes/Agent-assisted%20performance%20engineering.md). Browse the independent source inventory below; additional themes should follow the material rather than a predetermined taxonomy.

[Agentic sources](Bases/Agentic%20sources.md)

## Methods and tools

The first extracted method is [Elephant-Goldfish design and review](Approaches/Elephant-Goldfish%20design%20and%20review.md), with a reviewed implementation in [Elephant-Goldfish Model](Resources/Elephant-Goldfish%20Model.md). These inventories remain separate from FDE/Staff methods and resources.

[Agentic approaches](Bases/Agentic%20approaches.md)

[Agentic resources](Bases/Agentic%20resources.md)

## Questions to investigate

- When does feedback during development improve accepted outcomes enough to justify its cost?
- How should independent acceptance checks be maintained when agents generate both implementations and tests?
- Which findings transfer to existing codebases, incomplete requirements and different failure consequences?
- How do context, memory and tool boundaries affect recoverability and human review effort?
- Which observable changes should trigger reassessment of an AI workflow investment, and who can act on them?

No local experiments have been recorded for this collection yet. [Catalogue](Catalogue.md) provides navigation across the knowledge base.

## Record metadata

| Property | Value |
| --- | --- |
| type | synthesis |
| collection | agentic-development |
| status | evolving |
| created | 2026-10-21 |
| updated | 2026-10-25 |
| tags | agentic-development |
