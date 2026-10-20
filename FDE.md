# Forward deployed engineering

This guide examines what good FDE work looks like, how to execute it, and how peers can improve their technical and professional practice. It develops a working position from the catalogue, with links to detailed models and proposed procedures.

## Current understanding of the role

Customer proximity connects engineering decisions to the conditions in which software must work. The contested question is what the engagement must leave behind. A [product-oriented function](Operating%20models/Product-oriented%20FDE.md) aims for shared product improvement; [customer-owned delivery](Operating%20models/Customer-owned%20delivery.md) aims for a system the receiving team can operate and change. Those outcomes can coexist, but the sources do not agree that both define every FDE role. [Atlassian co-engineering](Operating%20models/Atlassian%20co-engineering.md) explicitly combines them as stated engagement aims, without independently proving their attainment. [Cresta's account](Articles/2026-10-06%20-%20Jove%20Zhong%20-%20Building%20a%20world-class%20FDE%20team.md) supplies one concrete product-oriented mechanism: place FDE in engineering, let field engineers contribute through the product code path, and deploy on a shared platform. That is an organisational choice, not a universal reporting-line requirement, and the account does not establish customer handover.

Other accounts describe [outcome-scoped missions](Operating%20models/Outcome-scoped%20missions.md) or [partner delivery capabilities](Operating%20models/Partner%20production%20delivery.md). These describe different aspects of the work, so they are comparison lenses rather than mutually exclusive job categories. A capability credential does not define an engagement's ownership or business success.

The role can also be framed around an internal business function. [Forte's account](Articles/2026-10-16%20-%20Forte%20Group%20-%20FDEs%20in%20AI-shaped%20organizations.md) compares internal, partner and hybrid staffing. Our synthesis treats staffing source as separate from engagement mandate and ownership. The title alone does not establish shared-product contribution or receiving-team independence, and the account's reported workflow gain does not isolate an effect of the role.

Before relying on a title, establish the mandate, decision authority, operational ownership, success measures, and relationship to the product team. Definitions can differ even within one firm, as [McKinsey's interviewees](Articles/2026-10-16%20-%20McKinsey%20-%20What%20is%20a%20forward-deployed%20engineer.md) illustrate. Treat outcome responsibility, decision authority, IP ownership, and billing as separate agreements. [GoodFirms' survey](Articles/undated%20-%20Kusum%20Motiani%20-%20What%20133%20companies%20reveal%20about%20FDE.md) reports varied structures and pricing, qualifying its own simplified FDE comparison. Responsibility should be bounded by the decisions an engineer can make and the dependencies others control. [Operating models](Operating%20models.md) makes those differences explicit.

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

Keep agent correctness, workflow improvement, and reuse evidence separate. A system can pass evaluations without improving work, and a useful customer implementation can remain bespoke. [Evaluate outcomes and reuse](Playbooks/Evaluate%20outcomes%20and%20reuse.md) develops this distinction from [Bermejo's proposed feedback model](Articles/2026-09-21%20-%20Pablo%20Bermejo%20-%20Turning%20intelligence%20into%20lasting%20value.md).

[SAP's account](Articles/2026-10-13%20-%20Dominik%20Metzger%20-%20Industry%20AI%20and%20measurable%20value.md) illustrates why reported customer benefit, future capability, and claimed product reuse need separate evidence.

[Canale's synthetic governance study](Articles/2026-09-24%20-%20Jeremy%20Canale%20-%20The%20Last%20Human%20Gate.md) adds another separation: acceptance of a bounded task, dependable execution of its whole route, and reduction in total human work are different claims. High automated coverage does not establish labor reduction when exceptions, verification, correction, and recurring support retain substantial effort.

## Executing more effectively

Choose a procedure for the decision in front of you:

- [Scope an engagement](Playbooks/Scope%20an%20engagement.md) establishes the task, decision owners, access, acceptance, and transition expectations.
- [Build and review safely](Playbooks/Build%20and%20review%20safely.md) addresses unfamiliar codebases, contribution standards, validation, and integration evidence.
- [Evaluate outcomes and reuse](Playbooks/Evaluate%20outcomes%20and%20reuse.md) tests behaviour, business benefit, and potential shared capabilities separately.
- [Prove a handover](Playbooks/Prove%20a%20handover.md) checks whether the receiving team can recover and change the system.
- [Rehearse a deployment from delivered artifacts](Playbooks/Rehearse%20a%20deployment%20from%20delivered%20artifacts.md) tests the delivery package in an agreed disposable environment.
- [Stage agent autonomy](Playbooks/Stage%20agent%20autonomy.md) makes permissions, action boundaries, and review conditions explicit.

[Atlassian's PDF](Articles/undated%20-%20Atlassian%20-%20Forward%20deployed%20engineering%20playbook.md) adds sustained adoption and workflow economics to delivery review. Measure cost alongside the work displaced, and treat launch activity as distinct from enduring usefulness.

[CTERA's launch model](Articles/2026-10-06%20-%20CTERA%20-%20Forward%20deployed%20engineering%20for%20enterprise%20AI.md) adds a useful first-to-next-use-case sequence: ground the work in the actual environment, prove one bounded use case in production, test repeatability across another workflow, and transfer ownership. [Ground-prove-expand-transfer delivery](Operating%20models/Ground-prove-expand-transfer%20delivery.md) treats this as a candidate model rather than a universal lifecycle. Its strongest proposed exit test is whether the receiving team can add the next use case without relying on the vendor's private context; the announcement provides no completed-engagement evidence that this has occurred.

[Cresta](Articles/2026-10-06%20-%20Jove%20Zhong%20-%20Building%20a%20world-class%20FDE%20team.md) adds a different execution pattern: concentrate short customer visits around discovery and acceptance, use remote time for building and evaluation, and continue measurement in live operation. It also recommends presenting alternatives with explicit effort and payoff, including a smaller change or no change. [Scope an engagement](Playbooks/Scope%20an%20engagement.md) adapts that option menu. Cresta's one-to-three-month delivery range and claimed acceleration across deployments are company-reported, not comparative evidence for a general schedule.

For governed automation, define what is actually transferring before selecting an agent architecture. [Contract-based governed task transfer](Approaches/Contract-based%20governed%20task%20transfer.md) names the input population, evidence, output, policy, authority, exceptions, and stopping criteria, then tests task acceptance and route reliability separately from human-work reduction. The supporting experiment is synthetic; this is a candidate engineering method with no local outcome evidence.

For technical methods, browse [Approaches](Approaches.md). Research findings can suggest an exercise without establishing its effectiveness in a customer engagement.

These are proposed adaptations of the sources. No local results are recorded yet. Use the engagement's risks and constraints to choose the appropriate depth, and record what helped or failed.

A handover need not remove every external dependency. [Bermejo](Articles/2026-09-21%20-%20Pablo%20Bermejo%20-%20Turning%20intelligence%20into%20lasting%20value.md) distinguishes supportable arrangements from reliance on one engineer's memory. [Gartner's release](Articles/2026-09-29%20-%20Gartner%20-%20Vendor%20FDE%20abandonment%20forecast.md) motivates attention to independence, but its abandonment figures remain forecasts.

## Developing strong FDE peers

Develop engineering judgment, domain understanding, and the ability to work with customer decision-makers together. Review how a colleague framed the problem, selected evidence, communicated uncertainty, and left work another person can maintain. Cresta assesses candidates with production scenarios about agent mistakes and unsuitable feature requests. Using incident and decision scenarios in peer practice is a plausible adaptation for exercising trade-off reasoning and difficult communication, but the source reports a selection method rather than a demonstrated learning outcome.

[Larson's Staff-level work-selection guide](Articles/2020-09-04%20-%20Will%20Larson%20-%20Work%20on%20what%20matters.md) distinguishes consequential work from easy tasks, visible activity, and large changes based on an imported diagnosis. [Staff Engineer](Staff%20Engineer.md#choose-where-attention-can-matter) keeps the broader argument. Applied to FDE, the useful question is whether field context, technical judgment, or cross-team relationships make this a bottleneck the engineer can uniquely unblock; customer visibility and urgency are not evidence of value by themselves. This is a transfer from non-FDE practitioner guidance and remains bounded by engagement scope, decision rights, and sustainable ownership.

Larson's [broader Staff duties guide](Articles/2020-11-28%20-%20Will%20Larson%20-%20What%20do%20Staff%20engineers%20actually%20do.md) adds a cross-boundary responsibility: inject engineering context into unusual, consequential decisions while it can still change the outcome. For a Staff-level FDE, this can mean making production, integration, support, and product consequences visible during customer, roadmap, or commercial decisions. The engineer represents broader engineering interests rather than one account and does not acquire product or commercial authority by being in the room. [Staff Engineer](Staff%20Engineer.md#carry-engineering-context-across-boundaries) retains the non-FDE argument and its limits.

For a Staff-level FDE, delivery is only part of the expected leverage. [Selway's Staff engineering account](Articles/2026-08-26%20-%20Anna%20Selway%20-%20Staff%20engineers%20shift%20from%20solving%20problems%20to%20shaping%20systems.md) suggests looking beneath the presented problem, treating alignment as part of system design, and spreading a method rather than preserving dependence on its author. Applied to FDE, this means testing whether a field request is a symptom of a workflow or platform issue and making the reasoning usable by customer and product peers. This is a transfer from a non-FDE practitioner essay, not evidence that every engagement warrants a larger redesign.

[Socol](Articles/2026-08-18%20-%20James%20Socol%20-%20Staff%20engineers%20must%20rebuild%20team%20culture.md) adds a narrower warning: AI-enabled independent delivery may reduce the collaboration through which teams share context and reinforce norms. Staff-level FDE practice can deliberately preserve shared goals, review, and visible decision reasoning across customer and internal teams. The proposed cultural practices have not been evaluated in FDE settings, so use them as experiments rather than requirements. [Staff Engineer](Staff%20Engineer.md) keeps the broader Staff-level synthesis separate.

The [AWS announcement](Articles/2026-10-01%20-%20Karthik%20Sonti%20et%20al%20-%20FDE%20pathways%20for%20AWS%20partners.md) offers a technical assessment example; [PagerDuty](Articles/2026-03-24%20-%20Doug%20McClure%20-%20How%20FDE%20was%20born%20at%20PagerDuty.md) supplies product-team onboarding practices; [HappyRobot](Articles/2026-03-18%20-%20Carlos%20Becker%20-%20FDE%20evolution%20at%20HappyRobot.md) emphasises domain depth. These inputs do not yet establish a complete development pathway.

A proposed exercise is to use a real engagement artifact for peer review, select one gap, practise it with a colleague, and examine the next artifact for improvement. We need more evidence about progression, peer coaching, and whether these exercises improve delivery. See [Technical and professional development](Themes/Technical%20and%20professional%20development.md).

## How the function evolves

Two company accounts illuminate different changes. [PagerDuty](Articles/2026-03-24%20-%20Doug%20McClure%20-%20How%20FDE%20was%20born%20at%20PagerDuty.md) describes moving bespoke services toward product contributions and engineering alignment. [HappyRobot](Articles/2026-03-18%20-%20Carlos%20Becker%20-%20FDE%20evolution%20at%20HappyRobot.md) describes embedded missions and expects better tooling to enable deeper domain and product work. Neither establishes a universal sequence or proves that faster execution produces strategic value.

Compare changes in responsibilities and capabilities rather than publication dates alone. The catalogue contains practitioner arguments, overlapping engagement accounts, announcements, and forecasts. Four APEG pages share an author and examples; they are one related body of evidence, not four independent confirmations. [Catalogue](Catalogue.md) exposes provenance for further reading.

## Questions to investigate

- When should a field solution become a shared product capability, configuration, or deliberate temporary fix?
- Which outcomes can an individual FDE own, and which require a product or customer decision?
- What demonstrates that a receiving team can evolve the system?
- How does strong junior, senior, and staff-level FDE practice differ?
- Which learning exercises improve technical judgment and customer collaboration?

## Reading map

Browse [Catalogue](Catalogue.md), compare [Operating models](Operating%20models.md), or use [Playbooks](Playbooks.md). [Staff Engineer](Staff%20Engineer.md) develops the parallel Staff-level synthesis. [People](People.md) maps documented contributors and [Resources](Resources.md) records tools and learning leads without treating mentions as endorsements.

The reading themes are [Role and product feedback](Themes/Role%20and%20product%20feedback.md), [Field discovery and execution](Themes/Field%20discovery%20and%20execution.md), [Ownership and sustainable delivery](Themes/Ownership%20and%20sustainable%20delivery.md), [Technical and professional development](Themes/Technical%20and%20professional%20development.md), and [Staff engineering and influence](Themes/Staff%20engineering%20and%20influence.md).

## Sources

The view below is generated from article frontmatter. Theme notes retain curated relevance descriptions.

[Sources](Bases/Sources.md)

## Record metadata

| Property | Value |
| --- | --- |
| type | synthesis |
| collection | fde |
| status | evolving |
| created | 2026-10-05 |
| updated | 2026-10-19 |
| tags | fde |
