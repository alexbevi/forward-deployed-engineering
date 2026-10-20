---
type: synthesis
collection: fde
status: evolving
created: 2026-10-06
updated: 2026-10-09T11:58
tags:
  - fde
  - fde/staff-engineering
---

# Staff Engineer

This guide develops an evidence-backed view of Staff-level engineering practice alongside [[FDE]]. Staff level describes scope, judgment, and influence; FDE describes a field-facing engineering context. A role can be either, both, or neither, so the syntheses remain separate and share material only where the transfer is explicit.

## Current understanding

The current sources describe Staff impact as shaping the conditions under which engineering succeeds, not simply solving a harder assigned problem. [[Articles/2020-09-04 - Will Larson - Work on what matters|Larson's work-selection chapter]] starts one step earlier, with the allocation of scarce attention: avoid easy low-consequence tasks, visible work without substance, and large interventions imported from another context. His [[Articles/2020-11-28 - Will Larson - What do Staff engineers actually do|broader duties chapter]] proposes a shared foundation across Staff archetypes: technical direction, mentorship and sponsorship, engineering context in organisational decisions, exploration, and glue work. [[Articles/2026-08-26 - Anna Selway - Staff engineers shift from solving problems to shaping systems|Selway]] questions the proxy, assumption, or system boundary behind the visible request, then treats alignment and the spread of reasoning as part of the engineered outcome. [[Articles/2026-08-18 - James Socol - Staff engineers must rebuild team culture|Socol]] focuses on the social system: as AI makes individual delivery more independent, shared goals, review, stories, and visible decision-making may need deliberate reinforcement.

Together they suggest a working model, not a validated progression framework:

1. Select consequential work where intervention can change the outcome.
2. Find the problem beneath the presented one.
3. Choose an intervention at the appropriate system boundary.
4. Build shared understanding through review, prototypes, validation, and explainable decisions.
5. Help the work finish and leave technical or collaborative capability that does not depend on one engineer's presence.

The sources do not establish that larger redesigns are generally superior, that more interdependence is always healthier, or that these practices reliably cause organisational impact. Those are decisions to test against the local system. Larson's two chapters belong to the same authored book and are one evidence family, not independent confirmations.

## Practising Staff-level influence

### Choose where attention can matter

Larson distinguishes easy low-impact work, visible low-impact work, and high-effort work based on a diagnosis imported from another context. His alternative is conditional: address existential risks when they threaten the organisation; otherwise look for consequential work with room to contribute and enough attention to sustain the result. This is a judgment aid rather than an impact score. Organisational attention can be distorted, and Larson explicitly recognises an ethical case for advocating for important work the organisation undervalues.

Finite capacity makes opportunity cost visible. Before taking on work, ask what will not happen as a result, whether someone else could usefully own it, and whether senior context or relationships materially improve the outcome. Work that is energising can also support a sustainable career, but personal energy does not by itself establish organisational consequence.

### Carry engineering context across boundaries

Larson describes technical direction as pragmatic advocacy for the organisation's technology, grounded in real organisational needs rather than an engineer's preferred tools. Staff engineers may also enter infrequent, consequential decisions before the usual routines have assembled the right perspectives. Their contribution is to make engineering constraints, options, and long-term consequences legible while representing engineering broadly rather than promoting a personal position.

Exploration is a related but distinct responsibility when incremental improvement cannot reach an ambiguous, important opportunity or risk. It needs a bounded question, resources, decision points, and enough organisational trust to learn from failure. The source describes this work but does not supply an evaluation method.

### Shape the problem before scaling the solution

Ask what is directly observed, what is inferred through proxies, and which assumption has escaped review. A Staff contribution may be a better question or system boundary rather than the implementation itself. Conviction should follow evidence: Selway's example supports generating important information at source, but it does not justify redesign whenever an imperfect metric exists.

### Design alignment as part of the work

Architecture reviews, prototypes, and invitations to challenge a proposal can expose incompatible mental models before they become delivery risk. The goal is not universal agreement or personal persuasion. It is enough shared understanding that other people can evaluate, explain, and carry the direction without the originating engineer.

### Preserve useful collaboration under autonomy

Socol's warning is that faster independent delivery can reduce the interactions through which teams learn norms and context. Candidate responses include fewer shared goals, purposeful review, living working agreements, recognition of desired behaviours, and explaining the reasoning behind decisions. These should restore useful interdependence, not status meetings or friction for its own sake.

### Make influence observable after departure

Durable influence can appear in a product capability, decision heuristic, review habit, or team-owned artifact. "Becoming unnecessary" should mean reducing dependence on private context, not withdrawing support or erasing accountable ownership.

Larson adds two near-term forms of leverage: make a bounded intervention that helps another project succeed, and help nearly finished work cross the last technical or organisational barrier. These are valuable when they increase another person's capability or bring a useful result into operation. They become counterproductive when the Staff engineer takes over, claims visibility, or leaves the original owner dependent on privileged access.

His broader duties chapter distinguishes mentorship from sponsorship. Advice and contextual understanding help a colleague reason; sponsorship uses credibility and access to create or protect an opportunity. Both need the recipient's goals and context, and neither is evidence of impact merely because a career ladder asks for it.

### Stay technically grounded without using code volume as the measure

The chapter's interview excerpts describe coding, small experiments, data analysis, code reading, and review in different combinations. The common purpose is contact with the technical reality that informs direction and organisational decisions. A Staff engineer may write less production code without becoming technically detached; conversely, frequent coding is not proof of Staff-level leverage and can become comfortable work that crowds out a broader responsibility. The appropriate mix is contextual, not a universal percentage.

## Intersection with FDE

| Staff-level lens | FDE application | Transfer condition |
| --- | --- | --- |
| Select consequential work | Distinguish visible customer urgency from a field problem where senior judgment can change the outcome | Must respect engagement scope, customer authority, product priorities, and opportunity cost |
| Carry engineering context into decisions | Make production, integration, support, and product consequences visible in customer, roadmap, or commercial decisions | Represent engineering beyond one account; keep product and commercial authority explicit |
| Find the problem beneath the request | Test whether a customer-visible symptom reflects a workflow, data, or platform issue | Requires field evidence and authority to challenge the initial scope |
| Choose the system boundary | Decide among a local adaptation, reusable capability, or upstream product change | Must fit engagement ownership, risk, and product decision rights |
| Build shared belief | Connect customer, product, and engineering perspectives through review and validation | Alignment cannot substitute for customer acceptance or technical evidence |
| Make yourself unnecessary | Leave reasoning, artifacts, and operating capability others can use | Maps to sustainable ownership, not necessarily zero continuing support |
| Reinforce collaboration deliberately | Preserve shared goals, review, and learning across autonomous or distributed contributors | Socol's claims are not FDE-specific and need local evaluation |
| Edit and finish | Use cross-team context to unblock a peer or bring valuable work into operation | Support should build capability rather than seize ownership or create dependence |
| Stay technically grounded | Use implementation, experiments, data, code review, or operational evidence to inform direction | Do not equate code volume with technical judgment or Staff impact |

This overlap informs [[FDE#Developing strong FDE peers]] and [[Themes/Technical and professional development]]. FDE-specific mandate, customer ownership, and product-feedback questions remain in [[FDE]] and [[Operating models]].

## Questions to investigate

- What distinguishes Staff-level leverage from doing more delivery personally?
- How can influence be assessed without rewarding visibility over durable outcomes?
- When should a Staff engineer advocate for system redesign rather than an incremental correction?
- Which collaboration mechanisms retain shared context without recreating avoidable coordination?
- Which forms of hands-on work keep technical judgment grounded at different Staff scopes?
- What does Staff-level FDE practice require beyond the combination of generic Staff and FDE competencies?

## Reading map

Use [[Themes/Staff engineering and influence]] for the curated Staff catalogue. The broader source inventory is in [[Catalogue]], and [[People]] maps documented contributors. The FDE intersection is intentionally maintained in [[FDE]] rather than duplicated here.
