---
type: synthesis
collection: fde
status: evolving
created: 2026-10-05
updated: 2026-10-19
tags:
  - fde
---

# Forward deployed engineering

This guide examines what good FDE work looks like, how to execute it, and how peers can improve their technical and professional practice. It develops a working position from the catalogue, with links to detailed models and proposed procedures.

## Current understanding of the role

Customer proximity connects engineering decisions to the conditions in which software must work. The contested question is what the engagement must leave behind. A [[Operating models/Product-oriented FDE|product-oriented function]] aims for shared product improvement; [[Operating models/Customer-owned delivery|customer-owned delivery]] aims for a system the receiving team can operate and change. Those outcomes can coexist, but the sources do not agree that both define every FDE role. [[Operating models/Atlassian co-engineering]] explicitly combines them as stated engagement aims, without independently proving their attainment. [[Articles/2026-10-06 - Jove Zhong - Building a world-class FDE team|Cresta's account]] supplies one concrete product-oriented mechanism: place FDE in engineering, let field engineers contribute through the product code path, and deploy on a shared platform. That is an organisational choice, not a universal reporting-line requirement, and the account does not establish customer handover.

Other accounts describe [[Operating models/Outcome-scoped missions|outcome-scoped missions]] or [[Operating models/Partner production delivery|partner delivery capabilities]]. These describe different aspects of the work, so they are comparison lenses rather than mutually exclusive job categories. A capability credential does not define an engagement's ownership or business success.

The role can also be framed around an internal business function. [[Articles/2026-10-16 - Forte Group - FDEs in AI-shaped organizations|Forte's account]] compares internal, partner and hybrid staffing. Our synthesis treats staffing source as separate from engagement mandate and ownership. The title alone does not establish shared-product contribution or receiving-team independence, and the account's reported workflow gain does not isolate an effect of the role.

Before relying on a title, establish the mandate, decision authority, operational ownership, success measures, and relationship to the product team. Definitions can differ even within one firm, as [[Articles/2026-10-16 - McKinsey - What is a forward-deployed engineer|McKinsey's interviewees]] illustrate. Treat outcome responsibility, decision authority, IP ownership, and billing as separate agreements. [[Articles/undated - Kusum Motiani - What 133 companies reveal about FDE|GoodFirms' survey]] reports varied structures and pricing, qualifying its own simplified FDE comparison. Responsibility should be bounded by the decisions an engineer can make and the dependencies others control. [[Operating models]] makes those differences explicit.

## What good looks like

Our proposed rubric asks for observable evidence. It is not a validated scoring system.

| Area | Evidence to look for |
| --- | --- |
| Problem framing | A named user, concrete task, baseline, and agreed success condition. |
| Technical judgment | A design whose alternatives, limits, and failure modes are understood. |
| Delivery | A usable result with appropriate validation and an accountable owner. |
| Sustainable ownership | A receiving team able to operate and change the solution, with understood support dependencies. |
| Professional practice | Clear decision rights, accurate commitments, and explicit uncertainty. |
| Peer contribution | Reviewable artifacts and reasoning another engineer can apply. |

Keep agent correctness, workflow improvement, and reuse evidence separate. A system can pass evaluations without improving work, and a useful customer implementation can remain bespoke. [[Playbooks/Evaluate outcomes and reuse]] develops this distinction from [[Articles/2026-09-21 - Pablo Bermejo - Turning intelligence into lasting value|Bermejo's proposed feedback model]].

[[Articles/2026-10-13 - Dominik Metzger - Industry AI and measurable value|SAP's account]] illustrates why reported customer benefit, future capability, and claimed product reuse need separate evidence.

[[Articles/2026-09-24 - Jeremy Canale - The Last Human Gate|Canale's synthetic governance study]] adds another separation: acceptance of a bounded task, dependable execution of its whole route, and reduction in total human work are different claims. High automated coverage does not establish labor reduction when exceptions, verification, correction, and recurring support retain substantial effort.

## Executing more effectively

Choose a procedure for the decision in front of you:

- [[Playbooks/Scope an engagement]] establishes the task, decision owners, access, acceptance, and transition expectations.
- [[Playbooks/Build and review safely]] addresses unfamiliar codebases, contribution standards, validation, and integration evidence.
- [[Playbooks/Evaluate outcomes and reuse]] tests behaviour, business benefit, and potential shared capabilities separately.
- [[Playbooks/Prove a handover]] checks whether the receiving team can recover and change the system.
- [[Playbooks/Rehearse a deployment from delivered artifacts]] tests the delivery package in an agreed disposable environment.
- [[Playbooks/Stage agent autonomy]] makes permissions, action boundaries, and review conditions explicit.

[[Articles/undated - Atlassian - Forward deployed engineering playbook|Atlassian's PDF]] adds sustained adoption and workflow economics to delivery review. Measure cost alongside the work displaced, and treat launch activity as distinct from enduring usefulness.

[[Articles/2026-10-06 - CTERA - Forward deployed engineering for enterprise AI|CTERA's launch model]] adds a useful first-to-next-use-case sequence: ground the work in the actual environment, prove one bounded use case in production, test repeatability across another workflow, and transfer ownership. [[Operating models/Ground-prove-expand-transfer delivery]] treats this as a candidate model rather than a universal lifecycle. Its strongest proposed exit test is whether the receiving team can add the next use case without relying on the vendor's private context; the announcement provides no completed-engagement evidence that this has occurred.

[[Articles/2026-10-06 - Jove Zhong - Building a world-class FDE team|Cresta]] adds a different execution pattern: concentrate short customer visits around discovery and acceptance, use remote time for building and evaluation, and continue measurement in live operation. It also recommends presenting alternatives with explicit effort and payoff, including a smaller change or no change. [[Playbooks/Scope an engagement]] adapts that option menu. Cresta's one-to-three-month delivery range and claimed acceleration across deployments are company-reported, not comparative evidence for a general schedule.

For governed automation, define what is actually transferring before selecting an agent architecture. [[Approaches/Contract-based governed task transfer]] names the input population, evidence, output, policy, authority, exceptions, and stopping criteria, then tests task acceptance and route reliability separately from human-work reduction. The supporting experiment is synthetic; this is a candidate engineering method with no local outcome evidence.

For technical methods, browse [[Approaches]]. Research findings can suggest an exercise without establishing its effectiveness in a customer engagement.

These are proposed adaptations of the sources. No local results are recorded yet. Use the engagement's risks and constraints to choose the appropriate depth, and record what helped or failed.

A handover need not remove every external dependency. [[Articles/2026-09-21 - Pablo Bermejo - Turning intelligence into lasting value|Bermejo]] distinguishes supportable arrangements from reliance on one engineer's memory. [[Articles/2026-09-29 - Gartner - Vendor FDE abandonment forecast|Gartner's release]] motivates attention to independence, but its abandonment figures remain forecasts.

## Developing strong FDE peers

Develop engineering judgment, domain understanding, and the ability to work with customer decision-makers together. Review how a colleague framed the problem, selected evidence, communicated uncertainty, and left work another person can maintain. Cresta assesses candidates with production scenarios about agent mistakes and unsuitable feature requests. Using incident and decision scenarios in peer practice is a plausible adaptation for exercising trade-off reasoning and difficult communication, but the source reports a selection method rather than a demonstrated learning outcome.

[[Articles/2020-09-04 - Will Larson - Work on what matters|Larson's Staff-level work-selection guide]] distinguishes consequential work from easy tasks, visible activity, and large changes based on an imported diagnosis. [[Staff Engineer#Choose where attention can matter]] keeps the broader argument. Applied to FDE, the useful question is whether field context, technical judgment, or cross-team relationships make this a bottleneck the engineer can uniquely unblock; customer visibility and urgency are not evidence of value by themselves. This is a transfer from non-FDE practitioner guidance and remains bounded by engagement scope, decision rights, and sustainable ownership.

Larson's [[Articles/2020-11-28 - Will Larson - What do Staff engineers actually do|broader Staff duties guide]] adds a cross-boundary responsibility: inject engineering context into unusual, consequential decisions while it can still change the outcome. For a Staff-level FDE, this can mean making production, integration, support, and product consequences visible during customer, roadmap, or commercial decisions. The engineer represents broader engineering interests rather than one account and does not acquire product or commercial authority by being in the room. [[Staff Engineer#Carry engineering context across boundaries]] retains the non-FDE argument and its limits.

For a Staff-level FDE, delivery is only part of the expected leverage. [[Articles/2026-08-26 - Anna Selway - Staff engineers shift from solving problems to shaping systems|Selway's Staff engineering account]] suggests looking beneath the presented problem, treating alignment as part of system design, and spreading a method rather than preserving dependence on its author. Applied to FDE, this means testing whether a field request is a symptom of a workflow or platform issue and making the reasoning usable by customer and product peers. This is a transfer from a non-FDE practitioner essay, not evidence that every engagement warrants a larger redesign.

[[Articles/2026-08-18 - James Socol - Staff engineers must rebuild team culture|Socol]] adds a narrower warning: AI-enabled independent delivery may reduce the collaboration through which teams share context and reinforce norms. Staff-level FDE practice can deliberately preserve shared goals, review, and visible decision reasoning across customer and internal teams. The proposed cultural practices have not been evaluated in FDE settings, so use them as experiments rather than requirements. [[Staff Engineer]] keeps the broader Staff-level synthesis separate.

The [[Articles/2026-10-01 - Karthik Sonti et al - FDE pathways for AWS partners|AWS announcement]] offers a technical assessment example; [[Articles/2026-03-24 - Doug McClure - How FDE was born at PagerDuty|PagerDuty]] supplies product-team onboarding practices; [[Articles/2026-03-18 - Carlos Becker - FDE evolution at HappyRobot|HappyRobot]] emphasises domain depth. These inputs do not yet establish a complete development pathway.

A proposed exercise is to use a real engagement artifact for peer review, select one gap, practise it with a colleague, and examine the next artifact for improvement. We need more evidence about progression, peer coaching, and whether these exercises improve delivery. See [[Themes/Technical and professional development]].

## How the function evolves

Two company accounts illuminate different changes. [[Articles/2026-03-24 - Doug McClure - How FDE was born at PagerDuty|PagerDuty]] describes moving bespoke services toward product contributions and engineering alignment. [[Articles/2026-03-18 - Carlos Becker - FDE evolution at HappyRobot|HappyRobot]] describes embedded missions and expects better tooling to enable deeper domain and product work. Neither establishes a universal sequence or proves that faster execution produces strategic value.

Compare changes in responsibilities and capabilities rather than publication dates alone. The catalogue contains practitioner arguments, overlapping engagement accounts, announcements, and forecasts. Four APEG pages share an author and examples; they are one related body of evidence, not four independent confirmations. [[Catalogue]] exposes provenance for further reading.

## Questions to investigate

- When should a field solution become a shared product capability, configuration, or deliberate temporary fix?
- Which outcomes can an individual FDE own, and which require a product or customer decision?
- What demonstrates that a receiving team can evolve the system?
- How does strong junior, senior, and staff-level FDE practice differ?
- Which learning exercises improve technical judgment and customer collaboration?

## Reading map

Browse [[Catalogue]], compare [[Operating models]], or use [[Playbooks]]. [[Staff Engineer]] develops the parallel Staff-level synthesis. [[People]] maps documented contributors and [[Resources]] records tools and learning leads without treating mentions as endorsements.

The reading themes are [[Themes/Role and product feedback]], [[Themes/Field discovery and execution]], [[Themes/Ownership and sustainable delivery]], [[Themes/Technical and professional development]], and [[Themes/Staff engineering and influence]].

## Sources

The view below is generated from article frontmatter. Theme notes retain curated relevance descriptions.

![[Bases/Sources.base]]
