# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context
- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
- **Executed:** 2026-03-02T00:00:00Z
- **H-16 Compliance:** S-003 Steelman applied on 2026-03-02 (`adversary-iteration-2-steelman.md`) — confirmed

---

# Pre-Mortem Report: UX Framework Selection

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** UX Framework Selection: Weighted Multi-Criteria Analysis (Revision 2, post-Steelman)
**Criticality:** C3 (Significant — governs a production Jerry skill implementation)
**Date:** 2026-03-02
**Reviewer:** adv-executor (S-004)
**H-16 Compliance:** S-003 Steelman applied on 2026-03-02 (confirmed — `adversary-iteration-2-steelman.md`)
**Failure Scenario:** It is September 2026. The `/user-experience` skill has been shipped with all 10 sub-skills. Adoption is near zero. When users do invoke it, 3 of the 10 sub-skills produce unusable outputs or fail silently. The AI-First Design prerequisite was never resolved. Two MCP integrations required for core workflows turned out to be non-functional in the Tiny Teams context. The skill was quietly removed from CLAUDE.md recommendations after 6 months. Post-mortem question: why did the most carefully analyzed framework selection in PROJ-020 produce a skill that nobody uses?

---

## Summary

The Pre-Mortem identifies 17 failure causes across 5 categories: 4 Critical, 8 Major, and 5 Minor. The selection analysis is methodologically sound, but the analysis-to-execution gap is where the failure originates. Three compounding failure chains are independently capable of sinking the skill: (1) the AI-First Design synthesis prerequisite is a blocking dependency that has no assigned owner, no timeline, and no fallback, making it the single most likely reason the skill stalls before launch; (2) the Hotjar Bridge MCP dependency is documented as a warning but never mitigated — two sub-skills (HEART, Fogg Behavior) depend on it for their core measurement functions, and without it those sub-skills are UX theory without UX data; (3) ten independently-invokable sub-skills with no routing guidance, no entry-point skill, and no disambiguation between overlapping use cases creates a skill that users cannot learn to use. The recommendation is ACCEPT with mandatory mitigations: address all P0 findings before the implementation phase begins, and treat the AI-First Design prerequisite as a blocking dependency that must be resolved before any other sub-skill implementation starts.

---

## Temporal Perspective Statement

*It is September 2026. We are six months past the launch of the `/user-experience` skill. We are in a post-mortem meeting explaining why it failed. We are not asking "might it fail?" — it has already failed. We are explaining why.*

---

## Findings Summary

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-20260302 | AI-First Design synthesis never completed — skill blocks indefinitely | Process | High | Critical | P0 | Completeness |
| PM-002-20260302 | No `/ux` entry-point skill — users can't discover or learn which sub-skill to invoke | Process | High | Critical | P0 | Actionability |
| PM-003-20260302 | Hotjar Bridge MCP fails in practice — HEART and Fogg become data-free theory tools | Technical | High | Critical | P0 | Evidence Quality |
| PM-004-20260302 | 10 sub-skills with overlapping use cases creates routing paralysis — users stop invoking | Assumption | High | Critical | P0 | Actionability |
| PM-005-20260302 | Design Sprint Friday user testing has no fallback that actually works at scale | Assumption | High | Major | P1 | Completeness |
| PM-006-20260302 | Kano Model's 30-user prerequisite fails pre-launch teams — the primary target audience | Assumption | High | Major | P1 | Evidence Quality |
| PM-007-20260302 | JTBD job synthesis without grounded input artifacts produces plausible-but-wrong jobs | Technical | Medium | Major | P1 | Evidence Quality |
| PM-008-20260302 | Lean UX and Design Sprint compete for the same workflow slot — teams pick one and ignore the other | Assumption | Medium | Major | P1 | Internal Consistency |
| PM-009-20260302 | Atomic Design assumes an existing component library — fails for teams building from scratch | Assumption | Medium | Major | P1 | Completeness |
| PM-010-20260302 | MCP dependency updates break sub-skills silently — no version monitoring, no maintenance owner | Process | Medium | Major | P1 | Methodological Rigor |
| PM-011-20260302 | Microsoft Inclusive Design Persona Spectrum tool produces generic AI output without team context | Technical | Medium | Major | P1 | Evidence Quality |
| PM-012-20260302 | Nielsen Heuristic evaluation on Figma requires human judgment AI cannot reliably substitute | Technical | Medium | Major | P1 | Methodological Rigor |
| PM-013-20260302 | HEART Happiness dimension requires real users — teams without live products cannot use the framework | Assumption | Low | Minor | P2 | Completeness |
| PM-014-20260302 | AI-generated Kano questionnaires elicit socially desirable answers rather than true preference | Technical | Medium | Minor | P2 | Evidence Quality |
| PM-015-20260302 | Portfolio integration paths (JTBD → Design Sprint → Lean UX → HEART) require orchestration skill not built | Process | Low | Minor | P2 | Actionability |
| PM-016-20260302 | Complementarity Matrix becomes a liability — users spend time studying which framework to use | Assumption | Medium | Minor | P2 | Actionability |
| PM-017-20260302 | Fogg Behavior Model's ethical use constraint produces outputs users find too cautious to act on | Assumption | Low | Minor | P2 | Actionability |

---

## Detailed Findings

### PM-001: AI-First Design Synthesis Never Completed — Skill Blocks Indefinitely [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.7 (AI-First Design) |
| **Category** | Process |
| **Likelihood** | High |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** Section 3.7 explicitly states: "Building `/ux-ai-first` requires a **prerequisite framework synthesis deliverable** before skill implementation can begin." This prerequisite has no assigned owner, no scope estimate, no timeline, and no explicit "block other work" status. In a Tiny Team context where implementation resources are minimal, this creates a common failure mode: the prerequisite is deprioritized in favor of "easier" sub-skills, the AI-First Design sub-skill is marked "pending", and 6 months later the portfolio has a 9-sub-skill skill instead of 10 — with its highest-uniqueness sub-skill permanently absent.

**Evidence:** Section 3.7: "A framework synthesis document MUST be produced as a separate deliverable before `/ux-ai-first` can be implemented." Section 3.7: "RT-003 TRANSPARENCY NOTICE: Unlike the other 9 selected frameworks, AI-First Design does NOT have an authoritative, codified framework document." The analysis acknowledges the prerequisite exists but does not make it a blocking dependency on the overall project plan — it is documented in one section of one framework description, with no worktracker entity, no acceptance criteria, and no sequencing constraint in the broader implementation plan.

**Analysis:** The AI-First Design prerequisite fails because it has the characteristics of work that gets dropped: it is complex (synthesizing across multiple practitioner sources into a codified framework), it produces an intermediate artifact rather than a user-visible skill, and it has no external deadline or user-visible consequence if deferred. The analysis correctly identifies the risk ("higher implementation risk than the other 9") but does not convert this risk into an implementation constraint. Without explicit blocking status, teams under time pressure will rationalize deferral: "we can launch 9 sub-skills now and add AI-First Design later." This is the precise path to permanent deferral.

**Recommendation:** Elevate the AI-First Design synthesis deliverable to a blocking dependency on all `/ux-ai-first` implementation work and create a worktracker entity for it immediately. Define the synthesis deliverable's acceptance criteria: (a) synthesizes Nudelman (2025), Fard (2025-2026), and NN Group (2026) sources into a single codified framework document with phases, inputs, outputs, and completion criteria; (b) review by at least one practitioner with AI UX experience; (c) framework document stored at a canonical path in the repository. Alternatively, if the synthesis cannot be completed before the skill launch timeline, consider replacing AI-First Design in the selected 10 with Service Blueprinting (rank 11, score 7.35) which has an authoritative, immediately adoptable framework body.

**Acceptance Criteria:** Either (a) AI-First Design synthesis deliverable exists as a completed worktracker entity with reviewer sign-off before any `/ux-ai-first` implementation begins, OR (b) the analysis explicitly demotes AI-First Design to a V2 item and replaces it with Service Blueprinting or another framework with an authoritative body, with a documented rationale for the substitution.

---

### PM-002: No Entry-Point Skill — Users Cannot Discover Which Sub-Skill to Invoke [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3 (All sub-skill descriptions) / Section 4 (Complementarity Matrix) |
| **Category** | Process |
| **Likelihood** | High |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The analysis defines 10 sub-skills with distinct use cases (`/ux-design-sprint`, `/ux-heuristic-eval`, `/ux-atomic-design`, `/ux-heart-metrics`, `/ux-lean-ux`, `/ux-jtbd`, `/ux-inclusive-design`, `/ux-ai-first`, `/ux-kano-model`, `/ux-behavior-design`). It does not define a `/ux` or `/user-experience` entry-point skill that answers the question "I want to improve my product's UX — where do I start?" The analysis correctly builds a complementarity matrix showing how the 10 frameworks work together across the product lifecycle, but this matrix lives in a framework selection analysis document that users never read. No mechanism routes users from "I have a UX problem" to "invoke sub-skill X."

**Evidence:** Section 4 Complementarity Matrix maps frameworks to BEFORE/DURING/AFTER lifecycle phases, but this is static analysis documentation, not a routing mechanism. Every sub-skill entry in Section 3 leads with "Proposed Jerry sub-skill: `/ux-{name}`" but no Section 3 entry describes when NOT to use that sub-skill relative to the other 9. The skill name space (`/ux-*`) creates 10 equally-weighted entry points with no disambiguation layer. The analysis's own RT-007 finding acknowledges a "TRIAGE EXISTING PRODUCT" scenario but does not specify which sub-skill a user would invoke to access that scenario.

**Analysis:** The mandatory-skill-usage.md trigger map can only hold one entry for the `/user-experience` skill. If all 10 sub-skills register separately, each sub-skill needs its own trigger keywords — creating a 10-row trigger map collision problem and making routing stochastic for common vocabulary ("improve UX," "make this more usable," "user testing"). If only the parent `/user-experience` skill registers with a set of trigger keywords, it must route internally to the correct sub-skill — but no internal routing mechanism is described. This is an adoption-blocker: a user who invokes `/user-experience` with no further context receives no actionable guidance unless a parent skill exists to triage their intent.

**Recommendation:** Define a `/user-experience` parent skill that is the sole entry point for all UX work. The parent skill's first action is a brief triage: "What lifecycle phase are you in? (a) Before design — problem framing and prioritization; (b) During design — process, evaluation, and components; (c) After design — metrics and behavioral analysis; (d) Existing product with UX problems." Based on the answer, the parent skill invokes the appropriate sub-skill(s). This mirrors how `/orchestration` coordinates multi-step workflows. Without this entry point, the 10 sub-skills are a library without a librarian.

**Acceptance Criteria:** A `/user-experience` parent skill is defined in `skills/user-experience/SKILL.md` with: (a) a triage mechanism routing users to the correct sub-skill based on their context, (b) a single set of trigger keywords registered in `mandatory-skill-usage.md`, and (c) explicit "when to invoke which sub-skill" decision guidance.

---

### PM-003: Hotjar Bridge MCP Fails in Practice — HEART and Fogg Become Theory Tools [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Sections 3.4 (HEART), 3.9 (Fogg Behavior Model) |
| **Category** | Technical |
| **Likelihood** | High |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** Both HEART (Section 3.4) and Fogg Behavior Model (Section 3.9) depend on Hotjar as their primary source of behavioral data. Both sections carry explicit warnings that Hotjar's MCP integration is a "Bridge MCP via Zapier/Pipedream — NOT a plug-and-play MCP server." The analysis acknowledges this risk but does not mitigate it: no alternative data source is specified for HEART's Happiness and Task Success dimensions or for Fogg's B=MAP diagnosis. Without behavioral data, HEART becomes a template-filling exercise producing GSM tables with no actual metric values, and Fogg becomes a framework discussion that cannot diagnose real behavior bottlenecks.

**Evidence:** Section 3.4: "**WARNING: Requires paid Zapier/Pipedream subscription, custom workflow configuration, and ongoing maintenance. NOT a plug-and-play MCP integration. Expect 2-4 hours of setup time and ongoing maintenance overhead.**" Section 3.9: "**WARNING: Bridge MCP only — requires paid Zapier/Pipedream subscription and custom configuration. This is Fogg's only MCP integration path; teams without Hotjar should use manual analytics export for the Measure step.**" The analysis states "teams without Hotjar should use manual analytics export" but does not specify what manual analytics export looks like, how an AI agent accesses it, or what the skill behavior should be when Hotjar is unavailable.

**Analysis:** The Tiny Teams target audience (2-3 people, no UX specialist) is the audience least likely to configure a Zapier/Pipedream MCP bridge. The appeal of Jerry sub-skills to Tiny Teams is zero-configuration, AI-augmented execution. A sub-skill that requires 2-4 hours of pre-configuration and an ongoing paid subscription before it can do anything useful will not be invoked by Tiny Teams. The failure mode is silent: users invoke `/ux-heart-metrics`, the Hotjar Bridge MCP is not configured, the skill produces a HEART template with blank Happiness and Task Success cells, the user receives no behavioral insight, and they stop using the skill. HEART's 8.30 selection score assumed 4/10 MCP integration (Bridge MCP) — but Bridge MCP in practice for Tiny Teams performs at 1-2/10 because configuration friction eliminates adoption.

**Recommendation:** Define explicit fallback data sources for HEART and Fogg that do not require Hotjar. For HEART: (a) Happiness — user survey templates the AI generates and formats for distribution via email/Typeform (no MCP required); (b) Task Success — structured user testing session reports from Design Sprint Friday tests; (c) Engagement and Retention — product analytics APIs (Posthog, Mixpanel, or even GA4) that have community MCP servers or direct API access. For Fogg: (a) behavioral data from product analytics exports (CSV/JSON input to the skill); (b) structured interview protocol for teams with no analytics. The sub-skills MUST be defined to work without Hotjar, with Hotjar as an enhancement, not a dependency.

**Acceptance Criteria:** Both `/ux-heart-metrics` and `/ux-behavior-design` skill definitions include: (a) explicit primary fallback data sources that do not require Hotjar, (b) defined skill behavior when no analytics tool is configured (explicit degraded-mode output, not silent failure), and (c) updated MCP integration section distinguishing "required for core function" from "optional enhancement."

---

### PM-004: 10 Sub-Skills with Overlapping Use Cases Creates Routing Paralysis [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3 (all sub-skills), Section 4 (Complementarity Matrix) |
| **Category** | Assumption |
| **Likelihood** | High |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** The analysis correctly argues that the 10 frameworks are non-redundant at the portfolio level, and the complementarity matrix shows how they compose across the product lifecycle. However, non-redundancy at the portfolio level does not prevent user routing confusion at the invocation level. A developer facing a usability problem has at least 4 plausible first-call sub-skills: `/ux-heuristic-eval` (expert inspection), `/ux-lean-ux` (hypothesis-driven improvement), `/ux-behavior-design` (behavioral diagnosis), or `/ux-heart-metrics` (measurement). The selection analysis never answers the question "given the user's current problem, what is the right first sub-skill to invoke?"

**Evidence:** Section 4 Complementarity Matrix defines distinct lifecycle positions (BEFORE DESIGN / DURING DESIGN / AFTER DESIGN), but this is a conceptual framing for a selection analysis, not an operational routing guide. Multiple sub-skills share "DURING DESIGN" positioning: Design Sprint, Lean UX, Nielsen's Heuristics, Atomic Design, Microsoft Inclusive Design, and AI-First Design. The cognitive load for a Tiny Team developer (non-UX-specialist) trying to select among 6 "during design" options will exceed their willingness to engage. Section 1's RT-007 finding (Triage Existing Product) demonstrates that even the analysis authors needed to explicitly map sub-skills to a specific scenario — this mapping work is required but is embedded in a framework selection document, not in the skill itself.

**Analysis:** The failure mechanism is cognitive overload leading to disengagement. When users face more than 3-4 equally-valid options and the cost of the wrong choice is unclear, they experience decision paralysis and default to not deciding. The 10 sub-skills are individually excellent but collectively overwhelming without a routing mechanism. This is particularly acute for Tiny Teams — the target audience — who have no UX specialist to make framework selection decisions. The analysis's own value proposition ("AI replaces the need for UX specialists") creates the failure condition: without a UX specialist to choose the right framework, users need the skill itself to choose the right sub-skill.

**Recommendation:** See PM-002 (entry-point skill) for the primary mitigation. Additionally: each sub-skill definition must include a "when to use THIS vs. THAT" disambiguation block — a 3-5 row table answering "use `/ux-X` when: [condition]. Use `/ux-Y` instead when: [competing condition]." This table must be actionable by a non-UX-specialist developer, not abstract ("use HEART for metrics, Kano for prioritization"). Example from Fogg: "Use `/ux-behavior-design` when users are not completing a specific action you have behavioral data for. Use `/ux-lean-ux` when you want to test whether a proposed change will improve behavior before building it."

**Acceptance Criteria:** Each of the 10 sub-skill definitions includes a "disambiguation block" with at least 2 entries specifying "use this sub-skill when X; use `/ux-Y` instead when Y." The parent `/user-experience` skill triage mechanism addresses the most common routing decision: "which sub-skill do I start with?"

---

### PM-005: Design Sprint Friday Testing Has No Viable Fallback [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.1 (Design Sprint) |
| **Category** | Assumption |
| **Likelihood** | High |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** Section 3.1 acknowledges that "AI cannot substitute for real users — the Friday test is the empirical validation step that AI cannot automate." The proposed fallback is "conduct a cognitive walkthrough with a team member playing the user role while AI evaluates against Nielsen's Heuristics." This fallback is inadequate for the use case: the Design Sprint's entire value proposition is rapid empirical validation before committing to implementation. A cognitive walkthrough conducted by the same team that built the solution suffers from familiarity bias — the team knows how the prototype works and will not encounter the confusion a real user would.

**Evidence:** Section 3.1 AI Augmentation Prerequisites: "Without real users for Friday, the Sprint produces an untested prototype, not a validated solution. Fallback for Friday: at minimum, conduct a cognitive walkthrough with a team member playing the user role while AI evaluates against Nielsen's Heuristics." The fallback does not address the core validity problem: a team cognitive walkthrough validates whether the prototype is logically consistent, not whether users find it intuitive. This is analogous to validating a joke by asking the joke's author whether it is funny.

**Analysis:** The Design Sprint sub-skill has the highest selection score (9.15) and the largest promise ("replace 5-7 people with 2 people + AI"). This promise creates the highest expectations and therefore the highest disappointment potential. When a Tiny Team runs the 4-day Design Sprint and arrives at Friday with no real users and a team-conducted cognitive walkthrough, they have invested 4 days of effort for a result they could have achieved with a 1-hour design review. The sub-skill loses credibility on first use, which predicts non-reinvocation.

**Recommendation:** Define a realistic "minimum viable Friday testing" protocol for teams without user access: (a) unmoderated remote test sessions using tools like Maze, Useberry, or Lookback that require no live user availability; (b) a structured recruitment-from-personal-network protocol (5 users from the team's extended network, screened by persona match); (c) explicit guidance on when the fallback produces sufficient signal ("proceed if you complete 3+ sessions") vs. insufficient signal ("do not proceed with implementation if you complete fewer than 3 sessions"). The fallback must be honest about its limitations and specify an acceptable minimum, not an "at minimum" that implies any level of compliance is sufficient.

**Acceptance Criteria:** The `/ux-design-sprint` skill definition includes a tested fallback protocol for Friday with: (a) specific tools requiring no live user coordination, (b) minimum session count (3+) for signal sufficiency, and (c) explicit guidance that team-only cognitive walkthrough is NOT sufficient validation for proceeding to implementation.

---

### PM-006: Kano Model Fails Pre-Launch Teams — The Primary Target Audience [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.10 (Kano Model) |
| **Category** | Assumption |
| **Likelihood** | High |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** Section 3.10 explicitly documents the 30-user prerequisite: "Kano Model requires at minimum 30 accessible, willing survey respondents to produce statistically meaningful feature classifications. For pre-launch teams (no user base): Kano Model is NOT executable as intended." The Gartner Tiny Teams context (the explicitly stated target audience) includes a significant proportion of pre-launch teams or teams in early growth phases with user bases well below 30. For these teams, the Kano sub-skill exists but cannot be used for its primary purpose, with a fallback to "qualitative Kano approximation" from 5-8 interviews — a substantially different methodology.

**Evidence:** Section 1 Criterion 1 (Tiny Teams Applicability): scored Kano at 8/10, justifying with "standardized questionnaire is highly automatable." The 8/10 score does not account for the user-base prerequisite that blocks the most common Tiny Teams scenario (pre-launch or early-stage with < 30 users). The Tiny Teams research (E-013 through E-016) describes AI augmentation for teams at any stage, not specifically post-launch teams with established user bases. The Kano prerequisites block in Section 3.10 was added as a Red Team finding (RT-006) but the selection score was not revisited after the prerequisite was identified.

**Analysis:** A sub-skill that is "NOT executable as intended" for a significant portion of the target audience should not score 8/10 on "Applicability to AI-Augmented Tiny Teams." The Kano score of 8/10 appears to evaluate the framework's theoretical capabilities for post-launch teams with 30+ users, not for the median Tiny Team user who may be pre-launch. The failure mode: a pre-launch Tiny Team developer invokes `/ux-kano-model`, receives an explanation that they need 30 users, has 0 users, and encounters an unusable sub-skill at the exact moment they need prioritization guidance most.

**Recommendation:** Revise the Kano sub-skill to lead with the prerequisite check: the first action of `/ux-kano-model` must be to ask "how many users do you have direct access to?" and route accordingly — (a) 30+: full Kano methodology; (b) 5-29: qualitative approximation path with explicit labeling; (c) 0-4: explicit "use JTBD instead — Kano requires real user feedback to be meaningful" redirect. Additionally, reconsider Kano's C1 score (currently 8/10) — the prerequisite may warrant a score reduction to 6/10, which could affect its selection ranking relative to Service Blueprinting (7.35) or other near-threshold candidates.

**Acceptance Criteria:** `/ux-kano-model` skill definition includes explicit prerequisite check at invocation. Users with 0-4 accessible users are explicitly redirected to JTBD. The analysis either revises Kano's C1 score to reflect the prerequisite constraint or explicitly documents why 8/10 remains justified despite the user-base requirement.

---

### PM-007: JTBD Job Synthesis Without Grounded Inputs Produces Plausible-but-Wrong Jobs [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.6 (Jobs to Be Done) |
| **Category** | Technical |
| **Likelihood** | Medium |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** Section 3.6 AI augmentation prerequisites state: "Without these input sources, AI cannot generate grounded job statements — it will hallucinate plausible-sounding but unvalidated jobs." The specified input sources are user interview transcripts, support ticket archives, or App Store/product review corpora. The failure mode: most Tiny Teams building new products have none of these. They have a product idea, maybe 1-2 early adopter conversations, and a hypothesis. An AI synthesizing JTBD job statements from insufficient input will produce job statements that sound correct and feel insightful but are actually reflecting the team's own assumptions back at them, dressed in the JTBD vocabulary.

**Evidence:** Section 3.6: "Without these input sources, AI cannot generate grounded job statements — it will hallucinate plausible-sounding but unvalidated jobs." The "fallback: conduct 3-5 manual Switch interviews" is appropriate but requires the team to understand and execute the Jobs-to-Be-Done interview methodology — a specialized qualitative research skill that the analysis's own C6 criterion scores JTBD at 8/10 (non-specialists can produce meaningful results with some orientation). However, "meaningful results" may be too optimistic for the Switch interview methodology, which requires active listening, non-leading questioning, and skilled probing for "the moment of switch." A developer applying this methodology without training will likely conduct a needs-assessment interview, not a Switch interview.

**Analysis:** The failure consequence is silent and severe: the Tiny Team builds a product around a job-to-be-done that was synthesized from insufficient data and validated by nothing more than "it felt right." The framework's credibility is intact (the team did their due diligence, ran the skill, produced job statements), but the job statements are wrong. The product fails for the actual users' actual jobs. This failure is worse than having no JTBD framework, because it provides false confidence.

**Recommendation:** The `/ux-jtbd` skill must implement a data sufficiency check before job synthesis: if the team cannot provide at minimum 3 distinct data sources (interview transcripts, reviews, support tickets, competitor reviews), the skill must surface an explicit warning: "Job synthesis from insufficient data produces unvalidated jobs. Before proceeding, complete at least 3 Switch interviews using the following protocol: [specific interview guide]. Provide the transcripts as input." The skill should also label AI-generated job statements with a confidence level (HIGH: synthesized from 10+ user data points / MEDIUM: synthesized from 3-9 data points / LOW: synthesized from < 3 data points — treat as hypothesis requiring validation).

**Acceptance Criteria:** `/ux-jtbd` skill includes data sufficiency check. Job statements generated from < 3 data sources are explicitly labeled as LOW confidence hypotheses requiring empirical validation. A Switch interview guide is included as a skill artifact.

---

### PM-008: Lean UX and Design Sprint Compete for the Same Workflow Slot [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Sections 3.1 (Design Sprint), 3.5 (Lean UX), 4 (Coverage Analysis) |
| **Category** | Assumption |
| **Likelihood** | Medium |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** The analysis describes Design Sprint and Lean UX as complementary — "episodic intensive (Sprint) + continuous iteration (Lean UX)" — but this framing requires a team to maintain two parallel UX process frameworks simultaneously. In practice, Tiny Teams under time pressure will adopt one and ignore the other. The selection analysis does not specify how a team transitions from Design Sprint to Lean UX (when does a team stop running Sprints and start running Lean UX cycles? after 1 Sprint? after product launch?), nor does it address the scenario where a team starts with Lean UX and then needs the Design Sprint for a major pivot.

**Evidence:** Section 4: "Design Sprint is the only framework in the selected set providing a complete, time-boxed, end-to-end design process." Section 4: "Lean UX provides the day-to-day hypothesis-driven operating model between Design Sprints. Where Design Sprint is the intensive 5-day process for big decisions, Lean UX is the ongoing cycle for continuous product improvement." This is a clean conceptual distinction that works in a framework analysis document. It becomes ambiguous in practice: what makes a decision "big enough" for a Sprint vs. addressable with a Lean UX hypothesis? A Tiny Team without UX experience will not know, and without guidance they will default to whichever framework they understand better and abandon the other.

**Analysis:** The analysis correctly avoids the Double Diamond/Design Thinking redundancy by excluding those frameworks. But the Sprint/Lean UX combination has a softer version of the same problem: both are process frameworks, both require team commitment to a workflow, and both cannot be simultaneously active for the same problem. The cognitive switching cost for a Tiny Team to maintain two active process frameworks is non-trivial and is not addressed.

**Recommendation:** Add an explicit "Process Framework Decision Guide" to the `/user-experience` skill (or to both sub-skills): "Use Design Sprint when: (a) the team is stuck on a major product direction decision, (b) you have 4-5 consecutive days available, (c) the decision is reversible but costly to get wrong. Use Lean UX when: (a) you are iterating on a known product direction, (b) you run continuous sprints and need a hypothesis-testing cadence, (c) the decision is low-cost to test." Additionally, specify the default sequencing: "New teams should start with Lean UX for its lower time commitment. Reserve Design Sprint for major product pivots or initial product direction validation."

**Acceptance Criteria:** The `/user-experience` parent skill or both sub-skill definitions include explicit "use Sprint vs. Lean UX" decision guidance covering the primary decision scenarios.

---

### PM-009: Atomic Design Assumes an Existing Component Library [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.3 (Atomic Design) |
| **Category** | Assumption |
| **Likelihood** | Medium |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** Section 3.3 describes Atomic Design enabling AI agents to query the Storybook MCP to discover "existing Atoms (input fields, buttons, labels) and Molecules (form groups, error states)." The key word is "existing." For a Tiny Team building a new product, there is no existing component library, no Storybook, and no atoms to compose. The Atomic Design skill assumes a mature design system that the Tiny Team is supposed to maintain — but for many Tiny Teams, the first use of the skill would be to BUILD the design system, not to operate within one. The skill description does not address this zero-state scenario.

**Evidence:** Section 3.3 Tiny Teams enablement pattern: "A tiny team building a product uses Atomic Design to structure their component library in Storybook. When a developer asks 'how should I build the checkout form?', an AI agent queries the Storybook MCP to discover existing Atoms..." This scenario assumes Storybook is installed, configured, and populated. Section 3.3 Required MCP Integrations lists Storybook as "Primary: exposes component hierarchy (Atoms/Molecules/Organisms) as AI-queryable API" — but this API only works after significant upfront investment in Storybook configuration and component documentation.

**Analysis:** The Storybook MCP integration scores 10/10 on the MCP integration criterion — but the score reflects the value of the integration when it exists, not the effort required to create it. For a Tiny Team starting from scratch, setting up Storybook with meaningful Atomic Design documentation is weeks of work, not a skill invocation. The sub-skill risks being useful only to teams who are already sophisticated enough to have built the infrastructure it requires.

**Recommendation:** The `/ux-atomic-design` skill must include an explicit "green field" path for teams without an existing design system: (a) a "bootstrap" mode that generates a minimal Storybook configuration with a starter set of Atoms (button, input, text, container, icon), (b) a "growth" mode that incrementally adds Molecules and Organisms as they are built, (c) explicit prerequisites ("Storybook version X.Y+ required; initial setup time: 2-4 hours"). The skill should default to green field mode and only enter "query existing" mode if Storybook MCP reports a populated component catalog.

**Acceptance Criteria:** `/ux-atomic-design` skill definition includes a green field bootstrap path with specific starting deliverables and a time estimate for initial setup.

---

### PM-010: MCP Dependency Updates Break Sub-Skills Silently [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 (MCP Tool Inventory), Sections 3.1-3.10 (all sub-skill MCP integrations) |
| **Category** | Process |
| **Likelihood** | Medium |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** All 10 sub-skills depend on MCP integrations across 7 tools (Figma, Miro, Storybook, Zeroheight, Hotjar, Figma, Framer, Whimsical). MCP servers are community-maintained, versioned independently, and subject to breaking API changes from the underlying tool (e.g., Figma changing its REST API). The analysis documents MCP dependencies at a point in time (2026-03-02) but does not address what happens when Figma releases a breaking API update, or when the Storybook community MCP is deprecated, or when a community-maintained MCP server is abandoned. With 10 sub-skills and 7 MCP dependencies, the probability of at least one broken dependency within 6 months is high.

**Evidence:** The MCP Tool Inventory (Section 1, Criterion 3) identifies 4 categories: Native MCP (Official), Community MCP, Bridge MCP, none. The analysis notes "(experimental)" and "(early access)" for Penpot and Rive respectively, and explicitly warns about Bridge MCP maintenance overhead. However, the analysis provides no mechanism for detecting broken MCP dependencies, no monitoring approach, and no maintenance owner for the `/user-experience` skill's MCP integrations.

**Analysis:** The `/user-experience` skill is the most MCP-dependent skill in the Jerry framework, with significantly more external tool dependencies than any other skill (by comparison, `/adversary` is tool-tier T1, read-only with no MCP dependencies). This creates a maintenance burden that scales with the number of external tools. When a MCP server breaks, the failure is silent: the sub-skill invocation succeeds at the Jerry level, the AI agent attempts the MCP call, receives an error, and either produces degraded output or fails in a way that is opaque to the user.

**Recommendation:** Define an explicit maintenance contract for the `/user-experience` skill before launch: (a) a quarterly MCP dependency audit checking that each integration remains functional; (b) a monitoring approach for MCP server status (watching the MCP servers' GitHub repositories for breaking change announcements); (c) each sub-skill's MCP integrations must be classified as "required for core function" (failure = degraded mode) vs. "enhancement only" (failure = cosmetic limitation). When a required MCP breaks, the sub-skill must surface an explicit error rather than producing silently-wrong output.

**Acceptance Criteria:** The `/user-experience` skill includes a maintenance document listing MCP dependencies with monitoring approach. Each sub-skill classification of "required" vs. "enhancement" MCP integrations is documented. A quarterly audit cadence is established.

---

### PM-011: Microsoft Inclusive Design Persona Spectrum Produces Generic Output Without Team Context [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.8 (Microsoft Inclusive Design) |
| **Category** | Technical |
| **Likelihood** | Medium |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** Section 3.8 describes AI agents evaluating Figma screens against the Microsoft Persona Spectrum (permanent/temporary/situational barriers). The failure mode is that without specific knowledge of the team's user population, target market, and primary use scenarios, AI-generated Persona Spectrum evaluations produce generic accessibility findings identical to a standard WCAG 2.2 audit. The "Solve for One, Extend to Many" principle requires knowing who "One" is — without a specific constrained user persona defined by the team, the AI defaults to generic permanent disability categories.

**Evidence:** Section 3.8 Tiny Teams enablement pattern: "AI agents use the Figma MCP to evaluate each screen against the Microsoft Persona Spectrum: permanent, temporary, situational." The pattern does not specify how the AI determines which disabilities and scenarios are most relevant to this team's specific users. A developer building a field data collection tool for outdoor workers has very different situational barriers (bright sunlight, gloved hands, interrupted workflows) than a developer building a financial dashboard for office users (cognitive load, screen reader compatibility, color blindness). Generic Persona Spectrum evaluation misses the context-specific barriers.

**Recommendation:** The `/ux-inclusive-design` skill must accept a user context brief as a required input: who are the primary users? what are their primary use contexts? what are 2-3 known or suspected user constraints? Without this context brief, the skill should prompt for it before proceeding rather than producing context-free generic findings.

**Acceptance Criteria:** `/ux-inclusive-design` skill requires user context brief as input. Persona Spectrum findings reference the specific team-provided context. Generic WCAG findings are labeled as "baseline" findings, distinguished from context-specific Inclusive Design findings.

---

### PM-012: Nielsen Heuristic Evaluation on Figma Requires Human Judgment AI Cannot Reliably Substitute [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.2 (Nielsen's Heuristics) |
| **Category** | Technical |
| **Likelihood** | Medium |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** Section 3.2 proposes that AI agents evaluate Figma designs against each of the 10 heuristics to produce "a structured heuristic evaluation report with severity ratings." This is plausible for heuristics with objective, measurable criteria (H1: Visibility of system status — presence or absence of loading indicators; H9: Help users recognize errors — presence or absence of error message text). It is not reliable for heuristics requiring contextual judgment: H6 (Recognition over recall — what is the mental model of the intended user?), H4 (Consistency and standards — consistent with what ecosystem conventions?), H2 (Match between system and real world — what is "the real world" for this user?). An AI evaluating these heuristics without user context produces confident-sounding findings that may be systematically wrong.

**Evidence:** Section 3.2: "AI evaluates each of the 10 heuristics against the design and generates findings with severity ratings (catastrophic/major/minor/cosmetic)." The sub-skill description does not differentiate between mechanically-evaluable heuristics (presence/absence of UI elements) and contextually-evaluable heuristics (requires knowing user mental models). This undifferentiated treatment creates false equivalence between AI-reliable findings and AI-unreliable findings.

**Recommendation:** The `/ux-heuristic-eval` skill must explicitly separate heuristics by AI reliability: (a) "High AI confidence" heuristics (H1, H3, H5, H9) — findings can be presented as conclusions; (b) "Requires team input" heuristics (H2, H4, H6, H7, H8, H10) — findings presented as hypotheses requiring human validation with specific questions the team must answer ("Does this match the conventions of the [specified platform/ecosystem]?"). The skill output should clearly mark which findings require human verification before acting on them.

**Acceptance Criteria:** `/ux-heuristic-eval` skill output distinguishes high-AI-confidence findings from human-verification-required findings. Each heuristic is pre-classified by reliability tier.

---

## Detailed Findings — Minor

### PM-013: HEART Happiness Dimension Requires Real Users — Pre-Launch Teams Cannot Use It [MINOR]

**Category:** Assumption | **Likelihood:** Low | **Severity:** Minor | **Priority:** P2

The HEART framework's Happiness dimension measures subjective user satisfaction through surveys and session recordings. Pre-launch teams have no users to survey. The analysis documents HEART as suitable for post-launch measurement but does not address how pre-launch teams should use the framework. Teams that invoke HEART pre-launch will encounter a structural gap in the first and most psychologically important dimension.

**Recommendation:** `/ux-heart-metrics` should include a pre-launch mode: "No users yet? Use HEART as a goal-setting framework — define your target signal and metric for each dimension BEFORE launch, then measure actuals at launch." This converts HEART from a measurement tool to a goal-specification tool for pre-launch teams, maintaining its relevance across team lifecycle stages.

---

### PM-014: AI-Generated Kano Questionnaires Elicit Socially Desirable Answers [MINOR]

**Category:** Technical | **Likelihood:** Medium | **Severity:** Minor | **Priority:** P2

Kano questionnaires use functional/dysfunctional question pairs to classify features. AI-generated questionnaire items may be phrased in ways that elicit acquiescence bias (respondents agree with positively-framed items regardless of true preference) or social desirability bias (respondents say they want "inclusive features" even when they are neutral in practice). The analysis treats Kano as "highly automatable" (Section 3.10) without addressing questionnaire design quality as a variable.

**Recommendation:** Include questionnaire design quality guidelines in the `/ux-kano-model` skill, with specific guidance on neutral phrasing and a validation pass where a sample question set is reviewed before distribution.

---

### PM-015: Portfolio Integration Paths Require Orchestration Skill Not Built [MINOR]

**Category:** Process | **Likelihood:** Low | **Severity:** Minor | **Priority:** P2

Section 4 defines integration paths between frameworks (JTBD → Design Sprint → Lean UX → HEART) that represent an optimal product development workflow. Executing these integration paths requires an orchestration layer that routes outputs from one sub-skill as inputs to the next. No orchestration agent for the `/user-experience` skill is defined. Teams following the integration paths manually will encounter friction at each handoff.

**Recommendation:** The `/user-experience` parent skill (see PM-002) should include a "full lifecycle workflow" mode that orchestrates the primary integration path automatically, as an alternative to individual sub-skill invocations.

---

### PM-016: Complementarity Matrix Becomes Cognitive Overhead for Users [MINOR]

**Category:** Assumption | **Likelihood:** Medium | **Severity:** Minor | **Priority:** P2

The Complementarity Matrix is excellent analytical work that demonstrates non-redundancy. However, when surfaced to users as part of the skill onboarding experience, it becomes 10 frameworks × N dimensions of information they must process before making a decision. The documentation value of the matrix for this framework selection analysis is high; its operational value for a developer trying to invoke a UX skill is low.

**Recommendation:** Keep the Complementarity Matrix in the analysis document (where it belongs) and DO NOT surface it as part of the skill's user-facing onboarding. Instead, provide a simpler "start here" decision tree in the `/user-experience` parent skill.

---

### PM-017: Fogg Behavior Model Ethical Guardrails Produce Cautious Outputs [MINOR]

**Category:** Assumption | **Likelihood:** Low | **Severity:** Minor | **Priority:** P2

Section 3.9 notes that Fogg's model is "explicitly ethical in its design guidance, distinguishing between facilitating natural behaviors (ethical) and coercing behaviors against user interest (unethical)." When implemented as a skill with guardrails, this ethical constraint may cause the AI agent to add excessive caveats to behavior design recommendations, reducing actionability. A team trying to increase notification opt-ins should not receive a dissertation on the ethics of persuasive technology with every recommendation.

**Recommendation:** Ethical guardrails in the Fogg skill should operate at the input screening level (flag obviously manipulative use cases at invocation time) rather than at the output level (adding caveats to every recommendation). Outputs should be actionable first; ethical context should be a one-time framing at skill initialization, not a per-recommendation disclaimer.

---

## Recommendations

### P0 — Critical: MUST mitigate before implementation begins

| Finding | Mitigation Action | Acceptance Criteria |
|---------|-------------------|---------------------|
| PM-001 | Create worktracker entity for AI-First Design synthesis deliverable with blocking status on `/ux-ai-first` implementation; OR substitute Service Blueprinting (rank 11, 7.35) as the 10th selection | Synthesis entity exists with owner, timeline, and acceptance criteria OR substitution decision documented in analysis |
| PM-002 | Define `/user-experience` parent skill with triage mechanism and single trigger map entry | `/user-experience` SKILL.md exists with triage mechanism routing to correct sub-skill; registered in mandatory-skill-usage.md |
| PM-003 | Define Hotjar-free fallback data sources for HEART and Fogg; both sub-skills must work without Hotjar | Sub-skill definitions include primary non-Hotjar data paths and explicit degraded-mode behavior |
| PM-004 | Add disambiguation blocks to each sub-skill; parent skill provides routing decision guidance | Each sub-skill has "use this vs. that" table; parent skill has routing decision tree |

### P1 — Important: SHOULD mitigate before sub-skill implementation

| Finding | Mitigation Action |
|---------|-------------------|
| PM-005 | Define minimum viable Friday testing protocol (3+ unmoderated remote sessions); remove "team cognitive walkthrough is sufficient" framing |
| PM-006 | Kano skill opens with user-base prerequisite check; routes < 5 users to JTBD; revise C1 score if warranted |
| PM-007 | JTBD skill adds data sufficiency check; labels AI job statements with confidence level (LOW/MEDIUM/HIGH) |
| PM-008 | Add Sprint vs. Lean UX decision guide to parent skill or both sub-skills |
| PM-009 | Atomic Design skill includes green-field bootstrap path for teams without existing component library |
| PM-010 | Define maintenance contract: MCP dependency classification (required vs. enhancement), quarterly audit cadence |
| PM-011 | Inclusive Design skill requires user context brief as input; differentiates context-specific from generic findings |
| PM-012 | Heuristic eval skill pre-classifies heuristics by AI reliability tier; labels findings requiring human validation |

### P2 — Monitor: MAY mitigate; acknowledge risk

| Finding | Monitoring Approach |
|---------|---------------------|
| PM-013 | HEART skill includes pre-launch goal-setting mode; document limitation in skill description |
| PM-014 | Kano questionnaire design guidelines included in skill; version and review before distribution |
| PM-015 | Note lifecycle integration paths in parent skill; full orchestration deferred to V2 |
| PM-016 | Complementarity matrix stays in analysis document; not surfaced in skill onboarding |
| PM-017 | Fogg ethical guardrails operate at input screening level only |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-001 (AI-First Design prerequisite unmanaged), PM-009 (Atomic Design zero-state gap), PM-013 (HEART pre-launch gap). The analysis is complete as an analytical document but incomplete as an implementation specification — key operational prerequisites are acknowledged but not resolved. |
| Internal Consistency | 0.20 | Negative | PM-004 (10 sub-skills with no routing mechanism contradicts the "Tiny Teams don't need specialists" premise), PM-008 (Sprint and Lean UX positioned as complementary but with no switching guidance). The analysis's core promise — AI replaces the need for a UX specialist — is partially undermined by requiring the team to make specialist-level framework selection decisions. |
| Methodological Rigor | 0.20 | Neutral | The selection methodology is sound. Failure risks are at the implementation specification level, not the analysis methodology level. The weighting rationale, sensitivity analysis, and failure mode coverage validation are methodologically strong. PM-010 (MCP maintenance) and PM-012 (Nielsen reliability tiers) are execution specification gaps, not methodological flaws. |
| Evidence Quality | 0.15 | Negative | PM-003 (Hotjar Bridge MCP value overstated given Tiny Teams context), PM-006 (Kano C1 score does not reflect prerequisite constraint), PM-007 (JTBD effectiveness understated for teams without existing data). Several evidence claims assume best-case conditions that Tiny Teams will not reliably have. |
| Actionability | 0.15 | Negative | PM-002 (no entry-point skill defined), PM-004 (routing paralysis with 10 equally-invocable sub-skills), PM-015 (integration paths documented but not orchestrated). The analysis is highly actionable as an analytical deliverable for an implementer who reads the full document. It is not actionable for an end user who needs to invoke a skill without reading a 6-section framework selection analysis. |
| Traceability | 0.10 | Positive | Strong throughout. Each selection traces to evidence (E-001 through E-023), scores are verified with calculations, revisions are tracked (RT-001 through RT-010), and steelman improvements are annotated (SM-001 through SM-004). PM findings trace to specific sections with direct quotes. |

---

## Execution Statistics
- **Total Findings:** 17
- **Critical:** 4
- **Major:** 8
- **Minor:** 5
- **Protocol Steps Completed:** 6 of 6

---

*Pre-Mortem executed per S-004 template v1.0.0 | Klein (1998, 2007) prospective hindsight methodology | Academic basis: Mitchell et al. (1989) — "it has happened" framing generates 30% more failure causes*
*Finding prefix: PM-NNN-20260302*
*H-16 compliance: S-003 Steelman confirmed at adversary-iteration-2-steelman.md*
