# Devil's Advocate Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4 (Critical -- architecture addition, irreversible once merged, tournament mode)
**Date:** 2026-03-03T00:00:00Z
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied 2026-03-03 (confirmed -- `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter3/s-003-steelman.md`)

---

## Summary

15 counter-arguments identified (3 Critical, 8 Major, 4 Minor). The deliverable is architecturally coherent and benefits from two prior revision cycles. However, three core structural issues survive the post-R2 document: (1) the Design Sprint sub-skill makes specific AI capability claims ("generates 20+ sketch variants," "builds interactive Figma prototypes") that are unverified against current LLM + Figma MCP integration capability; (2) the wave progression system places the highest-value framework (Design Sprint, score 8.65) in Wave 5, which is unreachable for the "Part-time UX" segment the document now identifies as the median target case -- a contradiction introduced by the Iteration 3 steelman's SM-001 reframing; (3) the T5 ux-orchestrator's failure modes under partial-completion states, MCP pre-check failures, and multi-session wave state management are undocumented for what would be the most complex orchestrator in the Jerry skill inventory. Recommend REVISE to address Critical findings before merge.

---

## Role Assumption Statement

**Deliverable challenged:** `ux-skill-issue-body-saucer-boy.md` (post-R2 revision)
**Scope:** Full issue body as GitHub enhancement specification and design document
**Criticality level:** C4 -- architecture addition with governance implications; all 10 strategies required; tournament mode
**H-16 compliance:** Confirmed. S-003 Steelman executed and loaded (`tournament-iter3/s-003-steelman.md`). Deliverable strengthened before this critique.
**Advocate role:** Argue against the strongest version of the deliverable. Find the reasons it is wrong, incomplete, or will fail.

---

## Step 2: Assumption Inventory

### Explicit Assumptions (stated in deliverable)

| # | Assumption | Location |
|---|-----------|---------|
| A1 | LLMs can evaluate designs against Nielsen's 10 heuristics with sufficient accuracy to produce actionable findings (>= 7/10 violations detected) | Acceptance Criteria > Wave 1 > `/ux-heuristic-eval` quality benchmark |
| A2 | The Design Sprint 2.0 framework can be collapsed from 4-5 participants to 2-person teams by having AI fill "missing participant" roles | The Solution > Sub-Skill #9 |
| A3 | B=MAP diagnosis from AI is MEDIUM confidence and requires "expert review OR validation against 2-3 real user data points" | Key Design Decisions > Synthesis Hypothesis Validation |
| A4 | The Figma MCP integration is stable and production-ready for 4 sub-skills | Key Design Decisions > MCP Integration |
| A5 | Wave progression criteria are sequential gates that ensure teams have the right foundation before advancing | Key Design Decisions > Wave Deployment |
| A6 | AI can "generate 20+ sketch variants" and "build interactive Figma prototypes" during Design Sprint Day 2-3 | The Solution > Sub-Skill #9 |
| A7 | The 3-tier confidence gate protocol (HIGH/MEDIUM/LOW) architecturally prevents over-reliance on unvalidated AI outputs | Key Design Decisions > Synthesis Hypothesis Validation |
| A8 | The `ux-orchestrator` T5 agent can coordinate 10 sub-skill agents within P-003's single-level nesting constraint | Key Design Decisions > P-003 Compliance |

### Implicit Assumptions (relied upon but not stated)

| # | Assumption | Where it matters |
|---|-----------|-----------------|
| A9 | The wave entry criteria are calibrated such that the target population (tiny teams) can actually meet them within a reasonable timeframe | Wave 5 entry requires Wave 4 outputs; Wave 4 requires Wave 3 outputs; Wave 3 requires "launched product with analytics" |
| A10 | Teams that cannot run a Design Sprint "sprint" of 4 days can meaningfully collapse it to 1-2 days with AI assistance | Design Sprint is Wave 5; reaching Wave 5 requires prior waves' completion |
| A11 | The Figma MCP server's capabilities (frame extraction, prototype building) match the functionality assumed by the sub-skill architecture | Multiple sub-skills depend on Figma doing specific things like "interactive Figma prototypes" |
| A12 | Adding 10+ new skills to Jerry does not meaningfully degrade the routing precision of existing skills | mandatory-skill-usage.md trigger map currently has 12 skills; `/user-experience` adds at priority 12 with broad UX keyword set |
| A13 | The sub-skill agents (T2-T3) can complete UX analysis tasks in reasonable time given the context budgets available | Agent definitions not yet specified; no time-to-completion estimate for individual agent invocations |
| A14 | "Expert review" and "2-3 real user data points" are accessible to the target user population (tiny teams without UX specialists) | MEDIUM confidence gate validation paths for B=MAP diagnosis and JTBD synthesis |

---

## Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-I3 | Design Sprint AI capability claims are unverified and may be false | Critical | "generates 20+ sketch variants during Day 2 ideation; builds interactive Figma prototypes during Day 3" (Sub-Skill #9) | Evidence Quality |
| DA-002-I3 | Wave 5 is unreachable for the median target population (Part-time UX case) | Critical | Wave 5 requires Wave 4 outputs; Wave 4 requires Wave 3; Wave 3 requires "Launched product with analytics OR 1 Lean UX cycle." The Part-time UX segment, now identified as the median case (SM-001), is explicitly restricted to Wave 1-2. | Methodological Rigor |
| DA-003-I3 | T5 ux-orchestrator creates a de facto multi-framework session coordinator with undocumented failure modes under partial-completion states | Critical | "Workers return results to the orchestrator, which coordinates cross-framework integration" -- compound responsibilities (MCP pre-check, wave signoff file check, crisis detection, capacity check) with no documented failure recovery | Completeness |
| DA-004-I3 | `/ux-heuristic-eval` quality benchmark has no calibration artifact or counting methodology defined | Major | "calibration artifact provided with sub-skill" -- no artifact is in the directory structure; no counting methodology (per-heuristic-category vs. per-instance) specified | Completeness |
| DA-005-I3 | 3-tier confidence gates' MEDIUM validation paths are undefined for the target population | Major | "Requires expert review OR validation against 2-3 real user data points" -- neither "expert" nor "real user data point" is defined; target population cannot hire UX experts | Actionability |
| DA-006-I3 | Routing conflict with `/nasa-se` and `/eng-team` on broad UX keywords is insufficiently analyzed | Major | AC lists "user interface, accessibility audit, design system" as positive keywords overlapping with `/nasa-se` and `/eng-team`; named negative keyword set not specified | Completeness |
| DA-007-I3 | Capacity check (< 20% of one person's time) has no measurement mechanism and no derivation | Major | Capacity check is a user self-report with undefined threshold derivation; WAVE-N-SIGNOFF.md already enforces wave prerequisites deterministically | Methodological Rigor |
| DA-008-I3 | Crisis mode 3-skill sequence contradicts wave prerequisite system | Major | Crisis mode invokes Behavior Design (Wave 4) and HEART (Wave 2) regardless of whether entry criteria are met -- undocumented bypass of wave gate system | Internal Consistency |
| DA-009-I3 | Zeroheight MCP operational constraints entirely deferred to Wave 3 implementation | Major | Rate limits, auth method, API version, failure codes all "Populated during Wave 3 implementation" -- blocks Wave 3 launch readiness assessment; $99/month cost assumption unverified | Evidence Quality |
| DA-010-I3 | AI-First Design Enabler 90-day expiry tracking field is unnamed and the orchestrator check mechanism is undefined | Major | "tracked as a worktracker entity field" -- which field? Worktracker schema has no standard expiry_date field; without named field, jerry ast frontmatter cannot detect expiry | Actionability |
| DA-011-I3 | Design Sprint "AI fills missing participant roles" is an unvalidated behavioral claim for multi-day sessions | Major | "the sprint collapses to 1-2 days with the AI filling the 'missing participant' roles" -- multi-day persistent state, decision diversity, and collaborative legitimacy are not addressed | Evidence Quality |
| DA-012-I3 | Wave 3 entry criterion leads with "Launched product" framing that traps pre-launch teams | Minor | "Launched product with an analytics data source (for HEART) OR completed 1 Lean UX hypothesis cycle" -- the OR path exists but is deprioritized by framing | Completeness |
| DA-013-I3 | Post-launch success metrics have no collection mechanism | Minor | "Track: number of unique teams..." -- no session identity mechanism, no aggregation infrastructure, no tracking implementation in directory structure | Actionability |
| DA-014-I3 | Tonal inconsistency between McConkey voice sections and technical specification sections | Minor | Vision/Problem sections use high-energy McConkey voice; ACs, MCP Constraints, Directory Structure use neutral technical language with no voice connectors | Internal Consistency |
| DA-015-I3 | Wave 5 diagrams do not reflect the 1-sub-skill vs 2-sub-skill conditional structure | Minor | Gantt chart and mermaid diagram show `/ux-ai-first-design` as a Wave 5 component without any visual indication of its conditional/expired state | Completeness |

---

## Detailed Findings

### DA-001-I3: Design Sprint AI Capability Claims Are Unverified and May Be False [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | The Solution > Sub-Skill #9 (/ux-design-sprint) |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Contradicting evidence, Unstated assumptions) |

**Claim Challenged:**
> "What AI does: Generates 20+ sketch variants during Day 2 ideation; builds interactive Figma prototypes during Day 3"

**Counter-Argument:**
These are specific capability claims about what the `ux-sprint-facilitator` agent will do. As of March 2026, generating "20+ sketch variants" from a Design Sprint challenge statement requires LLM capability to produce genuinely divergent conceptual designs, not variations on a theme. "Building interactive Figma prototypes" requires multi-step API operations (creating frames, linking interactions, populating content) that Figma MCP supports at limited fidelity for complex prototypes. Current LLM behavior with design tools tends toward variation generation rather than divergent concept generation. If these claims are false or require capabilities significantly beyond current tool integrations, the highest-ceremony framework in the portfolio (Wave 5, Design Sprint, score 8.65) becomes non-functional as described -- the primary AI-value-add does not materialize.

**Evidence:**
1. The deliverable provides no citation or verification for LLM capability to generate 20+ distinct sketch variants. The pre-launch validation AC for Wave 5 requires only that the agent "produces a testable prototype spec from a reference challenge statement" -- this does not validate the 20+ variants claim.
2. The non-MCP fallback for Design Sprint is "Miro-only mode (sprint exercises in Miro; manual prototype reference)" -- the fallback explicitly drops prototype building to "manual reference," suggesting that AI-built interactive prototypes are a primary-path-only aspiration, not a validated capability.
3. Design Sprint 2.0 Day 3 normally requires 6-8 hours of skilled prototyping work by human designers. The claim that AI can replace this within a session is extraordinary and requires extraordinary evidence.
4. The pre-launch validation AC for Wave 5 is: "benchmark: produces a testable prototype spec from a reference challenge statement" -- a "spec" is not an interactive prototype. The AC downgrades the claim from "builds interactive Figma prototypes" to "produces a prototype spec," creating an internal inconsistency within the ACs.

**Impact:**
If AI cannot reliably generate 20+ distinct sketch variants and build interactive Figma prototypes, the Design Sprint sub-skill delivers facilitation assistance only (templates, note-taking, exercise management) -- a significantly reduced capability compared to the described "Day 2 ideation" and "Day 3 prototype building" contributions. This would not invalidate the portfolio but would invalidate the Design Sprint sub-skill's described primary-path capability.

**Dimension:** Evidence Quality

**Response Required:** Provide either (a) a citation to verified LLM + Figma MCP capability demonstrating 20+ sketch variant generation and interactive prototype building, or (b) revise the Design Sprint "What AI does" section to scope claims to what AI can currently reliably do (facilitation, template management, ideation prompting, prototype spec generation), clearly labeling aspirational future capabilities. Align the Wave 5 pre-launch validation benchmark with the claimed capabilities.

**Acceptance Criteria:** Evidence citation for 20+ sketch generation and interactive prototype building, OR revised capability claims scoped to verified current capability with aspirational claims labeled. The Wave 5 pre-launch validation benchmark is consistent with the "What AI does" description.

---

### DA-002-I3: Wave 5 Is Unreachable for the Median Target Population [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions > Wave Deployment; The Problem > Who This Is For |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Alternative interpretations, Unaddressed risks, Internal contradictions) |

**Claim Challenged:**
> S-003 SM-001 addition (incorporated into deliverable): "The median tiny team is the 'Part-time UX' case. Across 2-5 person startups, having a dedicated UX person at any percentage of time is the exception, not the rule."
>
> Combined with Wave 5 entry: "Kano classification matrix completed for at least 1 product (Wave 4 output) OR B=MAP behavioral analysis completed for at least 1 user flow (Wave 4 output)"
>
> And the deliverable's explicit restriction: "Teams in the 'part-time UX' segment should treat wave progression beyond Wave 2 as aspirational"

**Counter-Argument:**
The deliverable simultaneously frames "Part-time UX" as the median case AND places the two highest-scoring sub-skills behind wave gates unreachable from that segment's starting position. Design Sprint (rank #2, score 8.65) is Wave 5. Atomic Design (rank #3, score 8.55) is Wave 3. For the median team (Part-time UX, < 20% UX time), the document explicitly restricts them to Wave 1-2. This means the median user of the skill portfolio never reaches the 2nd and 3rd highest-value sub-skills. Wave 5 requires completing Wave 4 (Behavior Design + Kano, requiring user survey data and Wave 3 design system infrastructure); Wave 4 requires completing Wave 3 (Atomic Design + Inclusive Design, requiring Storybook with 5+ classified components AND an accessibility review); Wave 3 requires completing Wave 2 (Lean UX + HEART, requiring analytics data from a launched product OR a completed Lean UX cycle). For a team with < 20% UX time, setting up Storybook, classifying 5+ components, running a Persona Spectrum review, processing Kano surveys, AND running B=MAP analysis before accessing Design Sprint is architecturally incompatible with the "part-time UX as median case" framing.

The contradiction was created by the Iteration 3 steelman (SM-001), which correctly identified the rhetorical opportunity to reframe Part-time UX as the median case. However, the wave architecture was not updated to match that framing -- the architecture was designed for teams that would systematically progress through all 5 waves, not for the median team that will stay in Waves 1-2.

**Evidence:**
1. Wave 3 entry requires "Launched product with an analytics data source (for HEART)" -- a pre-launch team cannot meet this without first launching.
2. The "Part-time UX" segment row explicitly states "Kano and HEART may exceed part-time capacity; prioritize Wave 1-2 only." But Design Sprint is Wave 5, above Wave 2.
3. Design Sprint's most compelling use case is for pre-launch teams that don't yet know what to build -- precisely the profile of a tiny team at the start. Placing it at Wave 5 (post-launch, post-design-system, post-analytics) means by the time a team reaches it, they may no longer need it.

**Impact:**
The portfolio's most compelling selling proposition for the median user (Design Sprint as the structured "figure out what to build before you build it" tool) is gated behind requirements the median user cannot meet. The portfolio as delivered for Part-time UX teams provides: Wave 1 (Heuristic Eval 9.05, JTBD 8.05) and Wave 2 (HEART 8.30, Lean UX 8.25). Wave 3-5 are "aspirational." This is still a valuable portfolio, but the gap between the "median case" framing and the accessible capabilities is not acknowledged in the deliverable.

**Dimension:** Methodological Rigor

**Response Required:** Reconcile the "Part-time UX as median case" framing with the wave architecture. Three options: (a) restructure wave assignments to make Design Sprint accessible earlier (e.g., as a standalone Wave 2 or Wave 3 option for teams that haven't yet launched, bypassing the design system waves), or (b) explicitly acknowledge in the wave documentation that Design Sprint is designed for teams beyond the Part-time UX median case and update the framing accordingly (Part-time UX is the Wave 1-2 use case, Design Sprint is the Wave 3+ use case), or (c) define a "pre-launch bypass path" that allows teams to access Design Sprint early if they have not yet built anything (when Design Sprint is most valuable) regardless of prior wave completion.

**Acceptance Criteria:** The wave documentation explicitly addresses how the median target population (Part-time UX, < 20% time) relates to the Design Sprint sub-skill access path, with no contradiction between the median-case framing and the wave restriction that caps this segment at Wave 2.

---

### DA-003-I3: T5 ux-orchestrator Has Undocumented Failure Modes Under Partial-Completion States [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions > P-003 Compliant Single-Level Nesting; Acceptance Criteria > Parent Orchestrator |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unaddressed risks, Historical precedents of failure) |

**Claim Challenged:**
> "The parent orchestrator (`ux-orchestrator`) is the only T5 agent with Task tool access. All sub-skill agents are T2-T3 and cannot spawn further sub-agents. Workers return results to the orchestrator, which coordinates cross-framework integration."

**Counter-Argument:**
The P-003 compliance claim is formally correct (one level of nesting). However, the `ux-orchestrator` is asked to perform compound responsibilities that no current Jerry orchestrator handles: (1) MCP connectivity pre-check before routing to MCP-dependent sub-skills, (2) WAVE-N-SIGNOFF.md existence check before routing to Wave N+1 sub-skills, (3) UX capacity assessment (< 20% time), (4) crisis mode detection from user language patterns, (5) AI-First Design Enabler expiry check, and (6) cross-framework integration handoff coordination (JTBD job statement -> Design Sprint challenge statement). These are 6 distinct stateful operations per invocation. The failure mode for each is undocumented: What does the orchestrator do when MCP pre-check fails mid-routing (after the user has already stated their task)? What happens when WAVE-N-SIGNOFF.md is not found for a wave the user is trying to access? What is the recovery path when a sub-skill invocation fails partway through a cross-framework sequence (e.g., JTBD completes but Design Sprint fails)? No cross-framework integration handoff schema is defined.

The existing Jerry H-36 circuit breaker (max 3 hops) addresses routing loops, not intra-session long-running coordination. The ux-orchestrator's design is substantively more complex than `/orchestration` (which coordinates a pre-defined pipeline) or `/adversary` (which runs strategies against a single artifact) -- it manages user-adaptive, state-dependent, multi-session workflows across 10 sub-skills.

**Evidence:**
1. The acceptance criteria include: "Parent orchestrator performs MCP connectivity pre-check before routing to MCP-dependent sub-skills; on failure, routes to non-MCP fallback path with user notification" -- but the AC for the ux-orchestrator agent definition does not include a failure behavior specification or recovery handoff schema.
2. "Cross-framework integration handoffs tested for at least 2 canonical sequences" -- but no handoff schema is specified in this issue. The handoff schema standard (HD-M-001 through HD-M-005 per agent-development-standards.md) requires fields including `from_agent`, `to_agent`, `artifacts`, `key_findings`, `blockers`, `confidence`, `criticality`. None of these are defined for the ux-jtbd -> ux-design-sprint handoff.
3. The orchestrator's behavior when WAVE-N-SIGNOFF.md does not exist is: "orchestrator checks WAVE-N-SIGNOFF.md existence before routing to Wave N+1 sub-skills" -- but what is the recovery path? Display an error? Suggest completing current wave? Route to a different sub-skill?

**Impact:**
An orchestrator without documented failure behavior is a runtime mystery. For a C4 architecture addition, undefined failure modes create implementation risk: the implementing developer must infer failure behavior from the design intent, potentially creating inconsistent behavior across failure scenarios.

**Dimension:** Completeness

**Response Required:** Document the ux-orchestrator's failure behavior for at minimum: (a) MCP pre-check failure (specific recovery path, not just "routes to fallback"), (b) WAVE-N-SIGNOFF.md not found (what the orchestrator tells the user and what routing alternative it offers), (c) sub-skill invocation failure mid-cross-framework sequence, (d) multi-session state loss between invocations. Define the cross-framework integration handoff schema for at least the JTBD -> Design Sprint canonical sequence (minimum required fields per HD-M-001).

**Acceptance Criteria:** At least 3 orchestrator failure modes documented with explicit recovery behavior. Cross-framework handoff schema specified for the JTBD -> Design Sprint canonical sequence, validating against the HD-M-001 required fields.

---

### DA-004-I3: Heuristic Eval Calibration Artifact Is Unspecified and Not in Directory Structure [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Wave 1 > `/ux-heuristic-eval` |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unstated assumptions) |

**Claim Challenged:**
> "Quality benchmark: agent correctly identifies >= 7 of 10 known heuristic violations in a reference test design (calibration artifact provided with sub-skill)"

**Counter-Argument:**
The benchmark states "calibration artifact provided with sub-skill" but the Directory Structure does not include a calibration test design file. The Pre-Launch Validation AC adds: "For `/ux-heuristic-eval`: published heuristic evaluation case study with known findings (e.g., Nielsen Norman Group published evaluations)." However, NNGroup published evaluations are narrative case studies, not structured violation datasets with machine-readable ground truth. A developer implementing the benchmark must determine: (a) which specific NNGroup evaluation to use, (b) how to count violations (per heuristic category -- 10 possible -- or per individual violation instance, which could yield 3 or 30 from the same design), and (c) whether the ">= 7 of 10 violations" criterion means "7 of 10 heuristic categories with at least one violation identified" or "7 of a defined set of 10 specific violations." Without this specification, the benchmark cannot be reproduced or validated consistently.

**Evidence:**
The directory structure for `/ux-heuristic-eval` includes: `SKILL.md`, `ux-heuristic-evaluator.md`, `ux-heuristic-evaluator.governance.yaml`, `heuristic-evaluation-rules.md`, `heuristic-report-template.md`. No calibration test design is listed. The benchmark "calibration artifact provided with sub-skill" is undelivered.

**Impact:**
The pre-launch validation AC (added in R2 as DA-001-I2 resolution) cannot be executed without a defined calibration artifact. The benchmark improvement from Iter 1 (no benchmark -> Iter 2 subjective benchmark -> Iter 3 defined benchmark) is incomplete until the artifact is specified and scoped.

**Dimension:** Completeness

**Response Required:** Specify: (a) the calibration artifact source (which NNGroup evaluation, or commitment to create a purpose-built reference design), (b) the violation counting methodology (per-heuristic-category or per-instance, with defined total count), (c) add the calibration artifact to the `/ux-heuristic-eval` directory structure. Add a task for calibration artifact creation to the Wave 1 ACs.

**Acceptance Criteria:** Calibration artifact source named with counting methodology. Directory structure for `/ux-heuristic-eval` includes calibration artifact path (e.g., `calibration/reference-design-with-violations.md` and `calibration/ground-truth-findings.md`).

---

### DA-005-I3: MEDIUM Confidence Gate Validation Paths Undefined for Target Population [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Synthesis Hypothesis Validation |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unstated assumptions, Actionability) |

**Claim Challenged:**
> "MEDIUM: Requires expert review OR validation against 2-3 real user data points. The agent does not generate design recommendations until a named validation source is provided."

**Counter-Argument:**
The target population is defined as tiny teams who "cannot afford UX" and specifically "without structured user research methodology." If these teams could readily access "expert review" or conduct structured "user data collection," they would not be the target population. Neither "expert review" nor "real user data points" is defined with minimum qualification standards. "Expert" in UX could mean a PhD in HCI, a seasoned UX practitioner, or a product manager who has done a Coursera UX course. "2-3 real user data points" could mean 2-3 formal interviews, 2-3 hallway tests, or 2-3 user sessions of any kind. Without operational definitions, the gate is either trivially satisfied ("I asked my co-founder, that's 1 data point") or infinitely demanding ("I need to hire a UX consultant"). The MEDIUM gate is the most common confidence level in the portfolio (B=MAP diagnosis from behavior data, JTBD from secondary research), making this the most-triggered validation requirement.

**Evidence:**
The synthesis validation section defines gate behavior but provides no operational guidance. The `synthesis-validation.md` rules file is listed in the directory structure but its content is not specified in this issue. The B=MAP sub-skill says MEDIUM confidence requires "expert review OR validation against 2-3 real user data points" but the `fogg-behavior-rules.md` file that would presumably define these standards does not yet exist.

**Impact:**
Teams either (a) cannot use MEDIUM-confidence outputs because they interpret the gate strictly (no expert access), defeating the behavioral diagnosis value, or (b) trivially satisfy the gate with nominal "validation" that does not reduce confidence risk, defeating the gate's safety function. Neither serves the design intent.

**Dimension:** Actionability

**Response Required:** Define "expert review" with a minimum qualification accessible to tiny teams (e.g., "a person with 2+ years of product management, UX, or relevant domain experience who has not participated in building the product, reviewing the output for the first time"). Define "real user data points" with minimum fidelity (e.g., "at least 1 completed session of > 5 minutes with a person who is or closely resembles a member of the target user population"). Document these definitions in `synthesis-validation.md`.

**Acceptance Criteria:** `synthesis-validation.md` includes minimum qualification definitions for both validation paths at MEDIUM confidence, with examples accessible to non-UX-specialists.

---

### DA-006-I3: Routing Conflict With Existing Skills Not Fully Analyzed [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Parent Orchestrator > trigger map entry |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unaddressed risks) |

**Claim Challenged:**
> "positive keywords (`UX, user experience, usability, heuristic evaluation, design sprint, lean ux, heart metrics, atomic design, inclusive design, behavior design, kano model, jobs to be done, jtbd, user interface, accessibility audit, design system`), priority 12... negative keywords preventing collision with `/adversary`, `/red-team`, `/nasa-se`, `/transcript`, `/problem-solving`"

**Counter-Argument:**
The AC names the skills to avoid collision with but does not name the negative keywords that prevent those collisions. "User interface" is a standard term in requirements discussions (`/nasa-se` domain: interface, design, architecture). "Accessibility audit" and "design system" overlap with `/eng-team` (security architecture, OWASP, ASVS). The trigger map specification requires negative keywords for skills with > 5 positive keywords (RT-M-001, agent-routing-standards.md). `/user-experience` has 16+ positive keywords, making negative keyword specification mandatory, not optional. Additionally, at priority 12 (next after the current maximum of 11 shared by `/prompt-engineering` and `/diataxis`), the routing algorithm's Step 3 (numeric priority ordering) requires a 2-level gap for auto-routing without escalation to Layer 2 (ambiguous). `/user-experience` at 12 is 1 level above both `/prompt-engineering` and `/diataxis` at 11 -- any keyword overlap with those skills would trigger Layer 2 escalation rather than clean routing.

**Evidence:**
The `/diataxis` trigger map entry includes "documentation" keywords that could overlap with UX documentation workflows. The `/problem-solving` trigger includes "analyze" and "evaluate" -- terms that could co-occur with "user experience" and "design" in a request like "analyze whether my user interface design works." Without named negative keywords, the router cannot determine which skill to invoke.

**Impact:**
Keyword routing collisions produce either (a) unintended routing to `/user-experience` for non-UX requests that happen to mention "user interface" or "design," (b) routing ambiguity requiring Layer 2 resolution for common UX+analysis requests, or (c) masking of `/user-experience` routing when UX keywords co-occur with problem-solving or requirements terms.

**Dimension:** Completeness

**Response Required:** Specify the complete negative keyword set for the `/user-experience` trigger map entry, with at least 8 terms addressing the specific collision zones identified: security/requirements vocabulary (blocking `/nasa-se` and `/eng-team` co-occurrence), documentation vocabulary (blocking `/diataxis` co-occurrence), and analysis vocabulary (blocking `/problem-solving` co-occurrence). Add a routing conflict test case to the Acceptance Criteria that demonstrates at least 3 collision scenarios handled correctly.

**Acceptance Criteria:** Trigger map entry in the AC specifies a named negative keyword set. A routing conflict test case is added to the ACs covering at least 3 ambiguous requests (e.g., "design the user interface for the authentication API" -- should not route to `/user-experience`; "analyze the usability of this registration form" -- should route to `/user-experience`).

---

### DA-007-I3: Capacity Check Mechanism Is Undefined and Its Threshold Lacks Derivation [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Parent Orchestrator Routes via Lifecycle-Stage Triage |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Logical flaws, Unstated assumptions) |

**Claim Challenged:**
> "Checks team UX capacity -- if < 20% of one person's time, restricts recommendations to Wave 1 sub-skills"

**Counter-Argument:**
The orchestrator cannot measure UX time allocation. The capacity check is operationally a question the orchestrator asks the user and then restricts routing based on the answer -- a self-report mechanism with no verification. The 20% threshold has no documented derivation: why 20%? Wave 2 requires Miro MCP and at least 1 completed heuristic evaluation report. Wave 3 requires a launched product with analytics (or 1 Lean UX cycle). These are output-based gates, not time-allocation gates. A team that spends 5% of their time on UX but has completed a heuristic evaluation and JTBD analysis has met Wave 2 criteria regardless of their time allocation. The capacity check adds a routing filter that is (a) not correlated with the actual wave entry criteria (WAVE-N-SIGNOFF.md), (b) duplicative (WAVE-N-SIGNOFF.md already gates wave progression deterministically), (c) based on subjective self-report, and (d) potentially overriding the objective wave gate in the wrong direction (a 15%-time team that meets Wave 2 criteria is blocked; a 25%-time team that hasn't completed Wave 1 is allowed).

**Evidence:**
The routing triage flowchart shows capacity check as a hard gate that restricts to Wave 1 before the product stage routing. This ordering means a team reporting < 20% UX capacity is never routed to Wave 2+ sub-skills regardless of their actual WAVE-N-SIGNOFF.md completion status. The KICKOFF-SIGNOFF.md template includes "team UX time allocation" as a field, but the relationship between KICKOFF-SIGNOFF values and the orchestrator's capacity check behavior is not defined.

**Impact:**
Teams with partial UX capacity but real Wave 2 achievements are incorrectly restricted. The capacity check creates a second gate that contradicts the WAVE-N-SIGNOFF.md primary gate, adding complexity without adding reliability.

**Dimension:** Methodological Rigor

**Response Required:** Either (a) remove the capacity check entirely and rely on WAVE-N-SIGNOFF.md as the sole wave gate mechanism (recommended -- simplification with no capability loss), or (b) document the 20% threshold derivation, define how the capacity check relates to WAVE-N-SIGNOFF.md (does it override or complement?), and define what happens when the user's reported capacity changes between sessions. If retained, the capacity check should be advisory (recommend Wave 1 focus) rather than restrictive (block routing to Wave 2+).

**Acceptance Criteria:** Capacity check is either removed (with rationale noting WAVE-N-SIGNOFF.md handles the same function) OR its threshold, measurement mechanism, and relationship to WAVE-N-SIGNOFF.md are explicitly documented, with the check reclassified as advisory rather than blocking.

---

### DA-008-I3: Crisis Mode Invokes Wave 4 Sub-Skills Without Wave Prerequisites [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Parent Orchestrator Routes via Lifecycle-Stage Triage |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Logical flaws, Internal contradictions) |

**Claim Challenged:**
> "crisis mode activates when the user explicitly describes urgency... emergency 3-skill sequence (Heuristic Eval -> Behavior Design -> HEART)"

**Counter-Argument:**
Crisis mode invokes Behavior Design (Wave 4) and HEART (Wave 2) regardless of whether the team has completed Wave 2, 3, or 4 entry criteria. This is an undocumented bypass of the wave gate system that the wave deployment section explicitly defines as "criteria-gated, not time-gated." Behavior Design requires understanding of B=MAP bottlenecks from actual user behavioral data -- without behavioral data from prior wave activities, the B=MAP analysis produces a diagnosis without evidence. HEART requires a populated GSM template with existing metric baselines -- without analytics data from a launched product, HEART produces an empty template. Crisis mode for a team that has never completed any wave invocations would produce: (a) Heuristic Eval findings (valid -- Wave 1, no prerequisites), (b) B=MAP "diagnosis" without behavioral data (low-quality -- Wave 4 prerequisite not met), (c) HEART GSM without metric baselines (empty -- Wave 2 prerequisite not met). The crisis sequence as designed produces false assurance that a diagnosis and measurement have been completed when the underlying data infrastructure is missing.

**Evidence:**
The wave prerequisite system is designed precisely to prevent this: "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review" (Wave 4 entry) exists because Behavior Design needs design system context. Crisis mode bypasses this without documentation or quality impact acknowledgment.

**Impact:**
Crisis mode may produce low-quality B=MAP and HEART outputs for teams without prior wave completion. The "emergency 3-skill sequence" framing suggests high confidence in the crisis diagnosis, but the quality of outputs 2 and 3 in the sequence depends entirely on having the prerequisite infrastructure.

**Dimension:** Internal Consistency

**Response Required:** Document crisis mode's wave prerequisite behavior explicitly. Options: (a) require minimum Wave 1 completion before crisis mode activates Behavior Design (it already invokes Heuristic Eval, which is Wave 1); reduce crisis mode to Heuristic Eval only for Wave 0-1 teams with explicit note about what's not available; (b) define "degraded mode" outputs for crisis B=MAP and HEART when prerequisites are not met, with explicit quality warnings; (c) document crisis mode as a Wave 1+ capability with the capacity check defining whether the full sequence or reduced sequence runs.

**Acceptance Criteria:** Crisis mode documentation specifies minimum wave prerequisites for each sub-skill in the sequence, or explicitly defines degraded-mode output quality when prerequisites are missing. "Emergency 3-skill sequence" framing is accompanied by a quality caveat.

---

### DA-009-I3: Zeroheight MCP Operational Constraints Are Fully Deferred [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > MCP Integration > MCP Operational Constraints table |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unaddressed risks) |

**Claim Challenged:**
> Zeroheight row in MCP Operational Constraints: Rate Limits = "Populated during Wave 3 implementation"; Auth Method = "Populated during Wave 3 implementation"; API Version = "Populated during Wave 3 implementation"; Known Failure Codes = "Populated during Wave 3 implementation"

**Counter-Argument:**
Zeroheight is an Enhancement MCP for Wave 3 Atomic Design (the #3 ranked framework at 8.55). The MCP Operational Constraints table was added in R2 specifically to address missing operational detail. However, deferring all Zeroheight operational constraints creates a known-unknown that blocks Wave 3 launch readiness assessment. Critically, Zeroheight carries the highest per-seat cost in the portfolio: $99/month Team plan. Unlike Figma ($15/editor) and Miro ($8/member), Zeroheight is a design system documentation platform with a much narrower use case. A team with 5 Atomic Design components in their design system may find $99/month difficult to justify. The cost assumption ("$99/month Team plan") is listed in the MCP classification table but not verified against current Zeroheight pricing as of 2026 (Zeroheight has historically changed pricing tiers). Additionally, Zeroheight is Enhancement (not Required) MCP -- meaning its absence is described as producing only "cosmetic limitation," but Wave 3 Atomic Design's primary output (design system documentation) depends heavily on Zeroheight for its published documentation path.

**Evidence:**
Figma MCP (highest dependency risk) has fully populated operational constraints: 720 req/min rate limit (Professional), OAuth 2.0 auth, REST API v1, known failure codes 429/403/404. Zeroheight has equivalent unknown risk at Wave 3 but all fields deferred. The Whimsical entry (also deferred) is Wave 5 Community MCP with MEDIUM-LOW stability -- lower risk profile than Zeroheight Wave 3 Enhancement with Official status and $99/month cost commitment.

**Impact:**
Wave 3 Atomic Design implementation team discovers Zeroheight constraints at implementation time. If Zeroheight has changed pricing, restricted API access, or has auth model requirements incompatible with the planned integration, Wave 3 Atomic Design launch is delayed.

**Dimension:** Evidence Quality

**Response Required:** Research and populate Zeroheight MCP operational constraints before this issue is merged, OR add an explicit Wave 3 pre-entry research task: "Verify Zeroheight MCP API rate limits, auth method, API version, and failure codes" as a required task before Wave 3 WAVE-3-SIGNOFF.md can be completed.

**Acceptance Criteria:** Zeroheight operational constraints are populated in the MCP table, OR a Wave 3 pre-entry Zeroheight verification task is scoped in the Wave 3 entry criteria. The $99/month cost is verified against current Zeroheight pricing.

---

### DA-010-I3: AI-First Design Expiry Field Unnamed; Orchestrator Check Mechanism Undefined [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Known Limitations > AI-First Design: Conditional Status |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unstated assumptions, Actionability) |

**Claim Challenged:**
> "The expiry deadline is tracked as a worktracker entity field."

**Counter-Argument:**
The worktracker entity schema does not include a standard `expiry_date` or `deadline` field. The AC states the orchestrator checks WAVE-N-SIGNOFF.md existence (a file existence check -- mechanical and deterministic). The AI-First Design expiry check is described as a "worktracker entity field" check -- which requires: (a) a named field in the Enabler frontmatter, (b) a parsing mechanism (presumably `jerry ast frontmatter` per H-33), (c) a date comparison against current date, and (d) an explicit routing behavior change when expired (substitute to Design Sprint only). None of these are specified. Without the field name, implementing the expiry check requires either custom tooling or manual monitoring. The 90-day time-box is the primary enforcement mechanism ensuring the AI-First Design Enabler does not remain conditionally "in progress" indefinitely. Without machine-readable enforcement, it relies on human memory to check at Wave 5 activation time.

**Evidence:**
The WAVE-N-SIGNOFF.md mechanism is deterministic (file exists or doesn't). The expiry mechanism is described as a "field" but without specification, implementation is blocked. The current worktracker entity frontmatter standard fields (per `skills/worktracker/rules/`) do not include an expiry field.

**Impact:**
Without a named field and orchestrator check mechanism, the 90-day time-box is unenforced. The AI-First Design Enabler could remain in an expired state at Wave 5 activation without triggering the substitution path, leading to Wave 5 routing to an unimplemented conditional sub-skill.

**Dimension:** Actionability

**Response Required:** Specify: (a) the Enabler frontmatter field name (e.g., `Expiry-Date: YYYY-MM-DD`), (b) the orchestrator's expiry check mechanism (e.g., `jerry ast frontmatter {enabler-path} | check Expiry-Date against current date`), (c) the routing behavior on expiry (route to Design Sprint only, display substitution notice). Add the field specification to the AI-First Design conditional Enabler creation story.

**Acceptance Criteria:** Enabler frontmatter field name specified. Orchestrator expiry check mechanism defined (tool invocation or file read pattern). Wave 5 routing AC includes expiry check step with defined behavior on expiry detection.

---

### DA-011-I3: Design Sprint Two-Person Adaptation Is Unvalidated for Multi-Day Sessions [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | The Solution > Sub-Skill #9 (/ux-design-sprint) > Team size adaptation |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Contradicting evidence, Historical precedents) |

**Claim Challenged:**
> "the sprint collapses to 1-2 days with the AI filling the 'missing participant' roles (note-taker, sketch generator, prototype builder)"

**Counter-Argument:**
The "AI fills missing participant roles" claim raises three distinct objections:

1. **Multi-day session state**: The note-taker role requires tracking decisions across the full sprint duration. Jerry's architecture (and LLM sessions generally) does not maintain state across multi-day sessions without explicit file-based handoffs. The deliverable does not describe how sprint session state is persisted between Day 1 and Day 2 of a 2-day compressed sprint.

2. **Decision diversity**: Design Sprint 2.0's decision-making power comes from the social dynamics of group disagreement and buy-in. A "decision-maker" role requires someone with organizational authority over the product direction. A 2-person team where both people hold opinions on the same design decision produces different sprint dynamics than a 4-5 person team with a designated decision-maker. AI cannot substitute for decision legitimacy.

3. **Empirical validation**: "Sketch generator" and "prototype builder" are the roles challenged in DA-001-I3. The claim that these roles can be filled by AI is unverified as a complete package in a Design Sprint context.

**Evidence:**
AJ&Smart's Design Sprint 2.0 methodology (the cited source) explicitly designs around 4-5 participants including a designated Decider with organizational authority. The published methodology provides no case studies or adaptations for 2-person teams with AI participation. The "1-2 day collapse" is presented as a design decision without citation.

**Impact:**
Teams running a 2-person + AI sprint may produce sprint artifacts (sketches, prototype spec, Day 4 test plan) that are technically complete but lack the decision legitimacy and behavioral diversity that make sprint decisions durable in practice. The sub-skill may consistently produce sprint outputs that teams revisit or abandon because the decisions weren't validated by the right people.

**Dimension:** Evidence Quality

**Response Required:** Either (a) cite an AJ&Smart or equivalent source validating 2-person + AI Design Sprint effectiveness, or (b) revise the team size adaptation section to explicitly characterize what is preserved (structure, templates, AI facilitation) and what is reduced (decision diversity, collaborative buy-in) in the 2-person format, positioning it as a "reduced ceremony approximation" rather than an equivalent sprint, or (c) add a caveat: "2-person sprints produce directional outputs suitable for rapid validation, not final product decisions. Treat as input to further stakeholder alignment."

**Acceptance Criteria:** Team size adaptation section accurately characterizes the quality difference between 4-5 person and 2-person sprint outcomes, with at least one citation or explicit limitation statement about decision diversity.

---

### DA-012-I3: Wave 3 Entry Criterion Framing Traps Pre-Launch Teams [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions > Wave Deployment |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Alternative interpretations) |

**Claim Challenged:**
> Wave 3 entry: "Launched product with an analytics data source (for HEART) OR completed 1 Lean UX build-measure-learn hypothesis cycle"

**Counter-Argument:**
The "OR" condition provides a valid pre-launch path (completed 1 Lean UX cycle does not require launch). However, leading with "Launched product with analytics data source" creates a mental model that Wave 3 is a post-launch wave. Pre-launch teams reading this criterion may incorrectly self-exclude. The Lean UX alternative path is the more achievable option for the median Part-time UX team, yet it is listed second. Additionally, a Wave 2 completion that includes a Lean UX build-measure-learn cycle satisfies Wave 3 entry directly -- meaning Wave 2 and Wave 3 entry can be achieved simultaneously by a Lean UX-active team. This collapsibility is not communicated and would benefit from explicit acknowledgment.

**Dimension:** Completeness

**Response Required:** Reorder the Wave 3 entry criterion to lead with the more achievable and pre-launch-compatible path: "Completed 1 Lean UX build-measure-learn hypothesis cycle OR launched product with an analytics data source."

**Acceptance Criteria:** Wave 3 entry criterion presents both paths as equally valid with the pre-launch path listed first.

---

### DA-013-I3: Post-Launch Success Metrics Have No Collection Mechanism [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Acceptance Criteria > Post-Launch Success Metrics |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Logical flaws) |

**Claim Challenged:**
> "Track: number of unique teams that complete Wave 1 within 30 days of first invocation (target: baseline establishment, no threshold for V1)"

**Counter-Argument:**
Five tracking targets are listed as ACs but none specifies a collection mechanism. "Number of unique teams" requires identity tracking across sessions -- Jerry has no built-in team identity mechanism. "Average S-014 quality score of sub-skill outputs" requires automated score aggregation across invocations that is not part of the current Jerry architecture. "Wave progression rate" requires cross-session wave state tracking, which WAVE-N-SIGNOFF.md provides at the individual project level but not at the aggregate "all teams" level. The directory structure includes no analytics or telemetry components. Listing these as ACs ("Track: ...") implies they are implemented at launch, but implementation is not scoped.

**Dimension:** Actionability

**Response Required:** Reclassify the post-launch success metrics as aspirational V2 targets requiring a separate instrumentation enabler, OR scope the specific collection mechanism for each metric (e.g., "aggregate count of WAVE-1-SIGNOFF.md files across all projects" for wave progression rate). If the metrics are aspirational V2 targets, move them to the V2 Roadmap section with a note: "Requires instrumentation enabler."

**Acceptance Criteria:** Post-launch success metrics are either (a) moved to V2 Roadmap with instrumentation enabler noted, or (b) each metric specifies its collection mechanism with implementation in scope for this issue.

---

### DA-014-I3: Tonal Inconsistency Between McConkey Voice and Technical Sections [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Document-wide (Acceptance Criteria, MCP Operational Constraints, Directory Structure) |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Alternative interpretations) |

**Claim Challenged:**
The document uses McConkey / Saucer Boy voice consistently in Vision, Problem, and conceptual sections, then switches to neutral technical language for Acceptance Criteria, MCP Operational Constraints, and Directory Structure without voice connectors.

**Counter-Argument:**
The tonal shift is jarring for sequential readers. After "Two people, one product, zero UX specialists -- and the product is going to feel like a team of eight built it," the Acceptance Criteria section begins with a checkboxes list in standard GitHub issue format. The S-003 steelman (SM-007) identified this for the Estimated Scope section specifically; the pattern is broader. The Known Limitations section begins with "We scoped this mountain from every angle. Here is what we found." -- a McConkey transition that works well. The Acceptance Criteria and Directory Structure sections have no equivalent transition. As a GitHub issue targeting developers who will implement this skill, the tonal consistency signals that the proposal's author has sustained engagement with the document as a whole, not just the opening sections.

**Dimension:** Internal Consistency

**Response Required:** Add a brief McConkey-voice transitional line before the Acceptance Criteria section (e.g., "Here is the gear checklist for the route we just described. Check every box before calling the line clean.") and optionally before the Directory Structure section. One sentence each, consistent with the established voice.

**Acceptance Criteria:** At least one McConkey-voice transitional sentence before the Acceptance Criteria section. The transition connects the conceptual framing to the technical specification rather than leaving them as separate documents.

---

### DA-015-I3: Wave 5 Diagrams Do Not Reflect the Conditional Sub-Skill Structure [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions > Wave Deployment (gantt chart, mermaid diagram) |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unaddressed risks) |

**Claim Challenged:**
> The gantt chart shows `/ux-ai-first-design` as a standard Wave 5 component (marked `crit` for critical path). The mermaid architecture diagram shows `/ux-ai-first-design` as a Wave 5 sub-skill labeled "(CONDITIONAL)."

**Counter-Argument:**
The substitution path states: "If the AI-First Design Enabler has not achieved its validation gate by Wave 5, Wave 5 delivers Design Sprint only." This creates a permanent 1-sub-skill Wave 5 scenario if the Enabler expires. Wave 5 would have only Design Sprint (1 sub-skill) while Waves 1-4 each have 2 sub-skills. The gantt chart marks `/ux-ai-first-design` as `crit` (critical path) without showing the expiry-to-substitution path. The sub-skill summary table shows Wave 5 with 2 entries. A developer reading the diagrams at Wave 5 implementation time, after the Enabler has expired, would see a Wave 5 designed for 2 sub-skills but only 1 deliverable. The 1-sub-skill permanent scenario is implied by the Known Limitations section but not reflected in the diagrams that implementers use as structural reference.

**Dimension:** Completeness

**Response Required:** Update the gantt chart to show the conditional/expiry branch: show Design Sprint as the guaranteed Wave 5 component and AI-First Design as conditional with a note "90-day expiry; reverts to Design Sprint-only on expiry." Update the mermaid diagram legend or sub-skill table to show that Wave 5 may have 1 or 2 sub-skills depending on Enabler status.

**Acceptance Criteria:** Wave 5 diagrams reflect both scenarios (2-sub-skill if Enabler complete, 1-sub-skill if expired). The permanent 1-sub-skill scenario is visually distinguishable from the conditional 2-sub-skill scenario.

---

## Step 4: Response Requirements

### P0 (Critical -- MUST resolve before merge)

| ID | Finding | Required Action | Acceptance Criteria |
|----|---------|----------------|---------------------|
| DA-001-I3 | Design Sprint AI capability claims unverified | Evidence citation for 20+ sketch generation and interactive Figma prototype building, OR scope revised to current verified capability with aspirational claims labeled | Evidence citation OR revised "What AI does" section; Wave 5 benchmark consistent with capability description |
| DA-002-I3 | Wave 5 unreachable for median target population | Reconcile Part-time UX median framing with wave restriction; define Design Sprint access path | Wave docs address Part-time UX / pre-launch teams and Design Sprint access without contradiction |
| DA-003-I3 | ux-orchestrator failure modes undocumented | Document 3+ failure modes with recovery behavior; specify cross-framework handoff schema | 3 failure scenarios documented; JTBD -> Design Sprint handoff schema specified per HD-M-001 |

### P1 (Major -- SHOULD resolve; require justification if not)

| ID | Finding | Required Action | Acceptance Criteria |
|----|---------|----------------|---------------------|
| DA-004-I3 | Heuristic eval calibration artifact unspecified | Name artifact source, counting methodology; add to directory structure | Artifact source named; counting methodology defined; directory structure includes artifact path |
| DA-005-I3 | MEDIUM confidence gate validation paths undefined | Define "expert" and "user data point" minimum standards | `synthesis-validation.md` includes operational definitions accessible to non-specialists |
| DA-006-I3 | Routing conflict analysis incomplete | Specify negative keyword set (>= 8 terms); add routing conflict test case | Named negative keywords in AC; 3-scenario routing conflict test in ACs |
| DA-007-I3 | Capacity check lacks mechanism and derivation | Remove (simplification) OR document threshold, measurement, and relationship to WAVE-N-SIGNOFF.md | Capacity check removed OR fully specified with threshold derivation and advisory classification |
| DA-008-I3 | Crisis mode bypasses wave prerequisites silently | Document crisis wave bypass; define minimum prerequisites per sub-skill | Crisis mode prerequisites documented with quality caveat for missing data |
| DA-009-I3 | Zeroheight operational constraints deferred | Research and populate constraints OR add Wave 3 pre-entry task | Zeroheight row populated OR Wave 3 pre-entry verification task scoped |
| DA-010-I3 | AI-First Design expiry field unnamed | Specify field name, check mechanism, routing behavior on expiry | Field name specified; orchestrator check mechanism defined; Wave 5 AC includes expiry step |
| DA-011-I3 | Design Sprint 2-person adaptation unvalidated | Citation OR explicit limitation statement about decision diversity | Evidence citation OR limitation statement acknowledging quality difference from 4-5 person format |

### P2 (Minor -- MAY resolve; acknowledgment sufficient)

| ID | Finding | Required Action |
|----|---------|----------------|
| DA-012-I3 | Wave 3 entry framing | Reorder to lead with pre-launch Lean UX path |
| DA-013-I3 | Success metrics no collection mechanism | Reclassify as V2 aspirational OR specify collection mechanism |
| DA-014-I3 | Tonal inconsistency | Add McConkey transition before Acceptance Criteria section |
| DA-015-I3 | Wave 5 diagrams missing conditional structure | Update gantt/mermaid to show 1-sub-skill vs 2-sub-skill conditional |

---

## Step 5: Scoring Impact

| Dimension | Weight | Impact | DA Findings | Rationale |
|-----------|--------|--------|-------------|-----------|
| Completeness | 0.20 | Negative | DA-003, DA-004, DA-006, DA-012, DA-015 | Orchestrator failure modes (DA-003) is the most significant; calibration artifact (DA-004), negative keywords (DA-006), Wave 3 framing (DA-012), and Wave 5 diagram (DA-015) are documentation completeness gaps ranging from Major to Minor |
| Internal Consistency | 0.20 | Negative | DA-002, DA-008, DA-014 | The Part-time UX median framing vs. Wave 5 restriction creates a logical contradiction (DA-002 -- Critical); crisis mode bypasses the wave gate system it depends on (DA-008 -- Major); tonal inconsistency (DA-014 -- Minor) is lower severity |
| Methodological Rigor | 0.20 | Negative | DA-001, DA-007, DA-011 | Unverified AI Design Sprint capability claims (DA-001 -- Critical) are the primary rigor gap; undefined capacity check threshold (DA-007) and unvalidated 2-person sprint adaptation (DA-011) further weaken the methodology of the most complex sub-skill |
| Evidence Quality | 0.15 | Negative | DA-001, DA-009, DA-011 | Design Sprint capability claims (DA-001) and 2-person adaptation (DA-011) lack evidence; Zeroheight unknown constraints (DA-009) represent evidence gaps in MCP planning that could affect Wave 3 cost and feasibility |
| Actionability | 0.15 | Negative | DA-005, DA-007, DA-010, DA-013 | MEDIUM gate validation undefined (DA-005), capacity check mechanism unclear (DA-007), expiry field unnamed (DA-010), success metric collection undefined (DA-013) -- all reduce actionability for implementing teams |
| Traceability | 0.10 | Neutral | DA-006, DA-010 | Routing conflict analysis (DA-006) and expiry tracking (DA-010) have traceability implications; existing traceability strengths (tournament provenance, wave signoff file naming, references section) are not undermined by these findings |

**Overall Assessment:** Targeted revision required. The three Critical findings (DA-001, DA-002, DA-003) address material issues that warrant substantive response before merge: an unverified capability claim for the portfolio's second-highest-scoring framework, a structural contradiction between the target population framing and the wave accessibility design, and undocumented failure modes for the most complex orchestrator in the Jerry skill inventory. Eight Major findings are addressable through documentation additions and specification clarifications -- most require 1-5 sentences of additional specification rather than architectural redesign. Minor findings are cosmetic and framing improvements.

---

## Execution Statistics

- **Total Findings:** 15
- **Critical:** 3 (DA-001-I3, DA-002-I3, DA-003-I3)
- **Major:** 8 (DA-004-I3 through DA-011-I3)
- **Minor:** 4 (DA-012-I3 through DA-015-I3)
- **Protocol Steps Completed:** 5 of 5

### Iteration Comparison

| Category | Iter 1 | Iter 2 | Iter 3 (this) | Notes |
|----------|--------|--------|---------------|-------|
| Critical | 4 | 2 | 3 | DA-001-I3 (capability claims) persistent from I1/I2; DA-002-I3 (wave/median-case contradiction) is NEW -- created by I3 steelman's Part-time UX median reframing combined with unchanged wave architecture; DA-003-I3 (orchestrator failure modes) escalated from Major |
| Major | 7 | 8 | 8 | Stable; I2 resolutions: AI-First gate strengthened, wave bypass fixed; New I3 Majors: Zeroheight deferral (DA-009), expiry field (DA-010), 2-person sprint (DA-011) -- these address design gaps that were implicit in earlier iterations |
| Minor | 4 | 4 | 4 | Stable across iterations |
| **NEW this iteration** | -- | -- | DA-002 (wave/median contradiction from SM-001 reframe), DA-007 (capacity check), DA-009 (Zeroheight), DA-010 (expiry field), DA-011 (2-person sprint) | |
| **PERSISTENT** | -- | -- | DA-001 (capability claims -- unresolved across all iterations) | |

---

*Strategy Execution Report*
*Strategy: S-002 (Devil's Advocate)*
*Template: `.context/templates/adversarial/s-002-devils-advocate.md`*
*Deliverable: `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`*
*Executed: 2026-03-03T00:00:00Z*
*Iteration: 3*
*H-16 Compliance: S-003 Steelman confirmed (`tournament-iter3/s-003-steelman.md`)*
