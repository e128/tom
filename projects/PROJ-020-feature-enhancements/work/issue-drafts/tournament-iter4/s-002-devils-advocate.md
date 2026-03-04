# Devil's Advocate Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4 (Critical -- architecture addition, irreversible once merged, tournament mode)
**Date:** 2026-03-03T00:00:00Z
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied 2026-03-03 (confirmed -- `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter4/s-003-steelman.md`)

---

## Summary

12 counter-arguments identified (3 Critical, 5 Major, 4 Minor). R3 addressed 5 of the 8 prior-iteration Major findings through structural additions: the WAVE-N-SIGNOFF.md 3-state enforcement, handoff data contract, MCP runbook AC, cross-framework synthesis AC, and blind evaluation rubric are all genuine improvements. However, the three Iter 3 Critical findings -- DA-001-I3 (Design Sprint AI capability claims), DA-002-I3 (Wave 5 unreachable for median user), and DA-003-I3 (ux-orchestrator undocumented failure modes) -- remain **unresolved in R3**. These are carried forward at Critical severity. Additionally, two new Major findings surface from R3's own additions: the blind evaluation rubric's 3-independent-evaluators requirement is operationally infeasible for the target population; and the crisis mode vs. BLOCK state conflict is a new contradiction introduced by R3's BLOCK state definition. Three prior Major findings (DA-005-I3, DA-007-I3, DA-011-I3) remain persistent. Recommend REVISE to address Critical findings before merge.

---

## Role Assumption Statement

**Deliverable challenged:** `ux-skill-issue-body-saucer-boy.md` (post-R3 revision)
**Scope:** Full issue body as GitHub enhancement specification and design document
**Criticality level:** C4 -- architecture addition with governance implications; all 10 strategies required; tournament mode
**H-16 compliance:** Confirmed. S-003 Steelman executed 2026-03-03 (`tournament-iter4/s-003-steelman.md`). Deliverable strengthened before this critique.
**Advocate role:** Argue against the strongest version of the deliverable. Find the reasons it is wrong, incomplete, or will fail.

---

## Prior Finding Status Assessment

Before constructing new counter-arguments, this section establishes what R3 resolved and what persists.

### RESOLVED Findings (addressed in R3)

| Prior ID | Finding | R3 Resolution | Notes |
|----------|---------|---------------|-------|
| DA-004-I3 | Calibration artifact unspecified | PARTIALLY resolved -- pre-launch validation AC added with NNGroup reference. Counting methodology still implicit ("7 of 10 violations") but external reference grounds it. | Accept as resolved; counting methodology gap addressed via external reference |
| DA-006-I3 | Routing conflict analysis incomplete | Resolved -- AC now specifies positive keywords and names skills to avoid collision with; negative keywords list included in AC text | Accepted |
| DA-008-I3 | Crisis mode bypasses wave prerequisites silently | PARTIALLY resolved -- WARN state behavior now defined; crisis mode activation criteria added. BLOCK state intersection with crisis mode remains undefined. | Downgraded to new DA-008-I4 at Major |
| DA-009-I3 | Zeroheight operational constraints deferred | Resolved -- MCP runbook AC now requires each sub-skill's MCP runbook before merge. This defers the detail appropriately to the implementation-time runbook. | Accepted |
| DA-010-I3 | AI-First Design expiry field unnamed | Resolved -- "The expiry deadline is tracked as a worktracker entity field" is insufficient but R3 adds the MCP runbook AC which adds a verification layer. However, field name remains unnamed. | DOWNGRADED but not fully resolved; carried forward as Minor DA-012-I4 |

### PERSISTENT Findings (not addressed in R3, carried forward)

| Prior ID | Current Status | Severity | Notes |
|----------|---------------|----------|-------|
| DA-001-I3 | **PERSISTENT** | Critical | Design Sprint "generates 20+ sketch variants; builds interactive Figma prototypes" -- no revision in R3. The Vision section added confidence-gated output depth qualification [R3-fix: DA-005-iter3] but this does not apply to the Design Sprint-specific capability claims in Sub-Skill #9. |
| DA-002-I3 | **PERSISTENT** | Critical | Wave 5 unreachable for Part-time UX median case -- no wave restructuring in R3. The wave table, entry criteria, and Part-time UX row framing are unchanged from Iter 3. |
| DA-003-I3 | **PERSISTENT** | Critical | ux-orchestrator failure modes undocumented. R3 added the handoff data contract AC (FM-004-I3) specifying what the parent passes to sub-skills, but recovery behavior for MCP failure mid-routing, WAVE-N-SIGNOFF.md not found, and cross-framework sequence partial failure remain undocumented. |
| DA-005-I3 | **PERSISTENT** | Major | MEDIUM confidence gate validation paths undefined. R3 made no change to synthesis-validation definitions. "Expert review OR 2-3 real user data points" remains operationally undefined. |
| DA-007-I3 | **PERSISTENT** | Major | Capacity check lacks mechanism and derivation. R3 did not remove or specify the capacity check. The WAVE-N-SIGNOFF.md remains the deterministic gate; the < 20% UX time self-report check still appears in the routing logic and routing triage flowchart. |
| DA-011-I3 | **PERSISTENT** | Major | Design Sprint 2-person adaptation unvalidated for multi-day sessions. No citation or limitation statement added in R3. |
| DA-013-I3 | **PARTIALLY RESOLVED** | Minor | Post-launch success metrics have "tracking" targets in ACs. R3 changed nothing; the 5 tracking ACs still have no named collection mechanism. Carried forward at Minor. |
| DA-014-I3 | **PERSISTENT** | Minor | Tonal inconsistency -- no McConkey voice transitions added before Acceptance Criteria section in R3. |
| DA-015-I3 | **PERSISTENT** | Minor | Wave 5 diagrams don't reflect conditional 1-vs-2 sub-skill structure. The gantt chart and mermaid diagram are unchanged from Iter 3. |
| DA-012-I3 | **PERSISTENT** | Minor | Wave 3 entry criterion leads with "Launched product" framing. The ordering is unchanged from Iter 3. |

---

## Step 2: Assumption Inventory (Iteration 4 Update)

Persistent assumptions from Iter 3 are retained. New assumptions introduced by R3 additions are marked [NEW-R3].

### Explicit Assumptions (stated in deliverable)

| # | Assumption | Location | Status |
|---|-----------|---------|--------|
| A1 | LLMs can evaluate designs against Nielsen's 10 heuristics with >= 7/10 violation detection accuracy | AC > Wave 1 > `/ux-heuristic-eval` | Persistent |
| A2 | Design Sprint 2.0 collapses to 1-2 days for 2-person teams with AI filling missing participant roles | Sub-Skill #9 | Persistent (DA-001-I3, DA-011-I3 unresolved) |
| A3 | B=MAP diagnosis is MEDIUM confidence requiring expert review OR 2-3 user data points | Synthesis Hypothesis Validation | Persistent (DA-005-I3 unresolved) |
| A4 | Figma MCP is stable and production-ready for 4 sub-skills | MCP Integration | Persistent |
| A5 | Wave progression criteria are sequential gates ensuring teams have foundation before advancing | Wave Deployment | Persistent |
| A6 | AI generates 20+ sketch variants and builds interactive Figma prototypes in Design Sprint | Sub-Skill #9 | Persistent (DA-001-I3 unresolved) |
| A7 | 3-tier confidence gate (HIGH/MEDIUM/LOW) architecturally prevents over-reliance on unvalidated AI outputs | Synthesis Hypothesis Validation | Persistent |
| A8 | ux-orchestrator T5 can coordinate 10 sub-skills within P-003 single-level nesting | P-003 Compliance | Persistent |
| A9-NEW | 3 independent evaluators are accessible for blind evaluation rubric validation before Wave 1 merge | Pre-Launch Validation AC | [NEW-R3] |
| A10-NEW | The blind evaluation 15% threshold can be assessed by evaluators without knowing which output is AI-augmented | Pre-Launch Validation AC | [NEW-R3] |

### Implicit Assumptions (relied upon but not stated)

| # | Assumption | Where it matters |
|---|-----------|-----------------|
| A11 | Wave entry criteria are calibrated for the Part-time UX median population | Wave 5 is inaccessible for Part-time UX segment |
| A12 | "Expert" in MEDIUM confidence validation is accessible to tiny teams without UX specialists | DA-005-I3 persistent |
| A13 | The capacity check (< 20% UX time) adds routing value on top of WAVE-N-SIGNOFF.md deterministic gates | DA-007-I3 persistent |
| A14-NEW | The 3-independent-evaluators for blind rubric are available from the implementing team or community at no cost | Pre-Launch Validation AC |
| A15-NEW | "Any Jerry Framework user who did NOT author the sub-skill" can serve as a qualified independent reviewer for WSM scoring AND as a blind rubric evaluator | AI-First Design and Pre-Launch Validation |

---

## Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-I4 | Design Sprint AI capability claims remain unverified (PERSISTENT from DA-001-I3) | Critical | "generates 20+ sketch variants during Day 2 ideation; builds interactive Figma prototypes during Day 3" (Sub-Skill #9) -- unchanged in R3 | Evidence Quality |
| DA-002-I4 | Wave 5 unreachable for median target population (PERSISTENT from DA-002-I3) | Critical | Part-time UX is "median" per SM-001 framing; explicit restriction "treat wave progression beyond Wave 2 as aspirational" -- unchanged in R3; Design Sprint still Wave 5 | Methodological Rigor / Internal Consistency |
| DA-003-I4 | ux-orchestrator failure modes undocumented (PERSISTENT from DA-003-I3) | Critical | R3 added handoff data contract AC but no recovery behavior for MCP failure mid-routing, WAVE-N-SIGNOFF.md not found, or cross-framework sequence partial failure | Completeness |
| DA-004-I4 | Blind evaluation rubric's "3 independent evaluators" requirement is operationally infeasible for the target population | Major | "3 independent evaluators score both the AI-augmented output and a manually-produced reference output" (Pre-Launch Validation AC) -- target population is solo practitioners and tiny teams | Actionability |
| DA-005-I4 | MEDIUM confidence gate validation paths remain undefined (PERSISTENT from DA-005-I3) | Major | "Requires expert review OR validation against 2-3 real user data points" (Synthesis Hypothesis Validation) -- no operational definition in R3 | Actionability |
| DA-006-I4 | Capacity check (< 20% UX time) persists without derivation or relationship to WAVE-N-SIGNOFF.md (PERSISTENT from DA-007-I3) | Major | Routing triage flowchart Step 2 still shows hard capacity gate before stage routing; no derivation added in R3; WAVE-N-SIGNOFF.md is the deterministic gate | Methodological Rigor |
| DA-007-I4 | Design Sprint 2-person adaptation lacks citation or quality-difference characterization (PERSISTENT from DA-011-I3) | Major | "the sprint collapses to 1-2 days with the AI filling the 'missing participant' roles" -- no citation or limitation statement added in R3 | Evidence Quality |
| DA-008-I4 | Crisis mode BLOCK state intersection creates undocumented mandatory bypass | Major | WARN state now defined (WAVE-N-SIGNOFF.md exists but incomplete). BLOCK state (file does not exist) + crisis mode invocation: orchestrator refuses Wave N+1 routing but crisis mode activates Wave 4 (Behavior Design). The two behaviors conflict without resolution | Internal Consistency |
| DA-009-I4 | AI-First Design Enabler expiry tracking field remains unnamed (partially PERSISTENT from DA-010-I3) | Minor | "tracked as a worktracker entity field" -- no field name specified. R3 added MCP runbook AC but did not address expiry tracking. | Actionability |
| DA-010-I4 | Post-launch success metrics have no collection mechanism (PERSISTENT from DA-013-I3) | Minor | 5 "Track:" ACs with no named collection mechanism, no session identity mechanism, no instrumentation scope | Actionability |
| DA-011-I4 | Wave 5 diagrams do not reflect conditional 1-vs-2 sub-skill structure (PERSISTENT from DA-015-I3) | Minor | Gantt chart marks `/ux-ai-first-design` as `crit` without showing expiry/substitution branch; sub-skill summary table shows 2 Wave 5 entries as peers | Completeness |
| DA-012-I4 | Wave 3 entry criterion leads with "Launched product" framing that traps pre-launch teams (PERSISTENT from DA-012-I3) | Minor | "Launched product with an analytics data source (for HEART) OR completed 1 Lean UX build-measure-learn hypothesis cycle" -- pre-launch path listed second | Completeness |

---

## Detailed Findings

### DA-001-I4: Design Sprint AI Capability Claims Remain Unverified [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | The Solution > Sub-Skill #9 (/ux-design-sprint) |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Contradicting evidence, Unstated assumptions) |
| **Prior ID** | DA-001-I3 (PERSISTENT -- not addressed in R3) |

**Claim Challenged:**
> "What AI does: Generates 20+ sketch variants during Day 2 ideation; builds interactive Figma prototypes during Day 3"

**Counter-Argument:**
These specific claims -- 20+ sketch variants and interactive Figma prototype construction -- have not been qualified, cited, or scoped to current capability in any revision across R1, R2, or R3. R3 added a Vision-level qualification [R3-fix: DA-005-iter3]: "HIGH-confidence sub-skills produce full recommendations; MEDIUM produce guided analysis requiring validation; LOW produce reference summaries requiring specialist interpretation." This is a valuable architecture-level fix, but it does not resolve the Design Sprint sub-skill's specific capability claims. The Design Sprint sub-skill has no confidence classification in the Synthesis Hypothesis Validation section -- it does not appear in the LOW, MEDIUM, or HIGH confidence output lists. The "What AI does" section for Design Sprint continues to make claims at the same specificity as Iter 1.

The internal inconsistency identified in Iter 3 (DA-001-I3 Evidence point 4) also persists: the Wave 5 pre-launch validation benchmark requires "a testable prototype spec from a reference challenge statement" -- a spec, not an interactive prototype. The sub-skill's primary description claims "builds interactive Figma prototypes" but the quality benchmark validates only "prototype spec" production. These are not equivalent deliverables.

**Evidence:**
1. Sub-Skill #9 "What AI does": "Generates 20+ sketch variants during Day 2 ideation; builds interactive Figma prototypes during Day 3" -- text unchanged across R1, R2, R3.
2. Wave 5 benchmark AC: "produces a testable prototype spec from a reference challenge statement" -- "spec" is not the same as "interactive prototype." The benchmark describes a lower-capability output than the sub-skill's description.
3. Non-MCP fallback for Design Sprint: "Miro-only mode (sprint exercises in Miro; manual prototype reference)" -- the fallback explicitly replaces prototype building with "manual reference," confirming that AI-built interactive prototypes are a primary-path aspiration, not a demonstrated capability.
4. No sub-skill confidence classification for Design Sprint appears in the synthesis validation section (HIGH/MEDIUM/LOW output lists do not include Design Sprint sketch generation or prototype building).

**Impact:**
Design Sprint is the #2 ranked framework (score 8.65). If the AI's actual Day 2 and Day 3 contributions are constrained to facilitation support and prototype specifications rather than divergent sketch generation and interactive prototype building, the sub-skill's described primary-path capability substantially overstates what teams will experience. Developers implementing the sub-skill will discover this during implementation, potentially after significant Wave 5 infrastructure investment.

**Dimension:** Evidence Quality

**Response Required:** Provide either (a) a citation to verified LLM + Figma MCP capability demonstrating 20+ distinct sketch variant generation and interactive Figma prototype construction, OR (b) revise the Design Sprint "What AI does" section to scope claims to verifiable current capability (facilitation, template management, ideation prompting, prototype spec generation), label aspirational capabilities separately, and align the Wave 5 pre-launch benchmark with the revised capability description. Add Design Sprint sketch generation/prototype building to the synthesis hypothesis confidence classification with appropriate confidence tier (MEDIUM or LOW as applicable).

**Acceptance Criteria:** Evidence citation provided, OR "What AI does" section accurately represents current LLM + Figma MCP capability with aspirational items clearly labeled. Wave 5 pre-launch benchmark is consistent with the sub-skill's primary description. Design Sprint output type is classified in the synthesis confidence gate table.

---

### DA-002-I4: Wave 5 Is Unreachable for the Median Target Population [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions > Wave Deployment; The Problem > Who This Is For |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Internal contradictions, Alternative interpretations) |
| **Prior ID** | DA-002-I3 (PERSISTENT -- not addressed in R3) |

**Claim Challenged:**
> Population segments table with "Part-time UX" segment (Portfolio Fit: MEDIUM). "Teams in the 'part-time UX' segment should treat wave progression beyond Wave 2 as aspirational."
>
> Combined with S-003 SM-001-I4 steelman argument (carried since Iter 3): the Part-time UX case describes the majority of 2-5 person startups.
>
> Combined with Design Sprint (rank #2, score 8.65) at Wave 5.

**Counter-Argument:**
The contradiction introduced by SM-001 reframing (Part-time UX as the median case) and preserved through R3 creates a more severe structural problem than a simple framing mismatch. The steelman report for Iter 4 (SM-001-I4) doubles down on this: "The median tiny team is the 'Part-time UX' case... Wave 1-2 are not 'what you settle for' without a UX specialist -- they are a meaningful UX capability gain for a team that previously had none." This is correct as steelman argumentation. But as DA logic it exposes the contradiction more sharply: if the primary audience is Part-time UX teams (Wave 1-2 ceiling), and Design Sprint is the portfolio's second-highest-value framework, then the portfolio's value architecture is inverted for its primary audience.

The wave path from Part-time UX access to Design Sprint requires:
- Wave 2 completion: At least 1 heuristic evaluation report + 1 JTBD job statement used in a product decision. (Achievable for Part-time UX.)
- Wave 3 entry: "Launched product with analytics OR completed 1 Lean UX cycle." Wave 3 sub-skills: Atomic Design (Storybook required), Inclusive Design (Figma required). For a Part-time UX team without MCP tools, Wave 3 may be blocked on tool access.
- Wave 4 entry: "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review." Both require Wave 3 completion (Atomic Design output + Inclusive Design output). For a Part-time UX team, Storybook setup with 5+ classified components is a significant infrastructure investment.
- Wave 5 entry: "Kano classification matrix OR B=MAP analysis." Wave 4 requires Wave 3. The complete chain: KICKOFF → Wave 1 (Heuristic + JTBD) → Wave 2 (Lean UX + HEART) → Wave 3 (Atomic + Inclusive with Storybook/Figma MCPs) → Wave 4 (Behavior + Kano, both requiring user data) → Wave 5 (Design Sprint).

This is a 5-wave sequential path requiring design system infrastructure (Storybook), analytics infrastructure (Wave 3 HEART path), and user survey data (Kano). For a team described as the "median" case, this path is theoretically achievable but practically inaccessible within a reasonable horizon without full MCP tool investment.

The more damaging observation: **Design Sprint is the framework most valuable at the earliest product stage** (before you know what to build, before you have users, before you need analytics). Placing it at Wave 5 (post-analytics, post-design-system) means it is most accessible when teams need it least. The wave ordering optimizes for pedagogical dependency, not for value delivery timing.

**Evidence:**
1. Part-time UX segment explicitly restricted to Wave 1-2 in the segment table.
2. Wave 5 entry requires Wave 4 completion; Wave 4 requires Storybook + Persona Spectrum; Wave 3 requires Storybook OR analytics.
3. Design Sprint's highest-value scenario: "Before design: Need validated prototype" routes to `/ux-design-sprint` (routing flowchart). This scenario is most relevant to pre-launch teams with no design yet -- teams who are at Wave 0-1, not Wave 5.
4. R3 made no change to wave assignments, entry criteria, or the Part-time UX segment restriction.

**Impact:**
The portfolio's highest-ceremony, second-highest-scoring framework is optimally useful at the earliest product stage but gated behind the most infrastructure-intensive wave sequence. Teams who reach Wave 5 have already launched, iterated, and built a design system -- they no longer have the "we don't know what to build" problem that Design Sprint solves. The wave deployment architecture creates a capability mismatch between when a tool is needed and when it is accessible.

**Dimension:** Methodological Rigor / Internal Consistency

**Response Required:** One of three options: (a) Define a "pre-launch bypass path" to Design Sprint that allows access regardless of prior wave completion for teams that have not yet built a product (the scenario where Design Sprint is most valuable), OR (b) restructure wave assignments to move Design Sprint to Wave 2 or Wave 3 as an option for pre-launch teams, treating it as parallel to (not dependent on) the post-launch analytics waves, OR (c) explicitly acknowledge the contradiction in the Wave Deployment section: "Design Sprint is most valuable pre-launch; Part-time UX teams should access it directly via bypass rather than through the sequential wave path. The wave prerequisites are designed for post-launch teams iterating on existing products."

**Acceptance Criteria:** The relationship between Design Sprint's optimal use case (pre-launch, discovery) and its Wave 5 gate is explicitly addressed. A Part-time UX team reading the wave documentation can determine when they are eligible to use Design Sprint without contradiction with the segment's Wave 1-2 restriction.

---

### DA-003-I4: ux-orchestrator Failure Modes Remain Undocumented [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions > P-003 Compliant Single-Level Nesting; Acceptance Criteria > Parent Orchestrator |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unaddressed risks, Logical flaws) |
| **Prior ID** | DA-003-I3 (PERSISTENT -- R3 partial improvement insufficient) |

**Claim Challenged:**
> "Parent-to-sub-skill handoff includes: product context (name, domain, target users), selected sub-skill, prior sub-skill outputs (if any), and quality gate threshold" [R3-fix: FM-004-I3]
>
> "Parent orchestrator performs MCP connectivity pre-check before routing to MCP-dependent sub-skills; on failure, routes to non-MCP fallback path with user notification" (Acceptance Criteria)

**Counter-Argument:**
R3's FM-004-I3 fix adds the handoff data contract (what the parent passes to sub-skills). This improves the happy-path specification. However, the three failure modes identified in DA-003-I3 remain without documented recovery behavior:

**Failure Mode 1 -- MCP pre-check failure mid-routing:** The AC says the orchestrator "routes to non-MCP fallback path with user notification." What is the fallback path for Figma failure on a Design Sprint Day 3 request? The Design Sprint fallback is "Miro-only mode (sprint exercises in Miro; manual prototype reference)." But who initiates this fallback routing? The AC says "routes to non-MCP fallback path" but the routing triage flowchart does not include an MCP failure branch. The flowchart ends at the sub-skill invocation node with no failure exit.

**Failure Mode 2 -- WAVE-N-SIGNOFF.md not found (BLOCK state):** The WAVE-N-SIGNOFF.md BLOCK state is now defined [R3-fix: FM-001-I3]: "Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process." SM-005-I4 (Steelman Iter 4) also notes the BLOCK state user experience is under-specified. The "directs user" behavior: what specific information does the orchestrator provide? What routing alternative is offered? Can the user still invoke Wave 1-N sub-skills directly? The BLOCK state is a hard stop with no documented path forward.

**Failure Mode 3 -- Cross-framework sequence partial failure:** The AC requires "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)." The handoff data contract (FM-004-I3) defines what is passed. It does not define what the orchestrator does when the JTBD analysis completes but the Design Sprint invocation fails partway through (e.g., Figma MCP timeout on Day 3). The partial completion state (JTBD output exists, Design Sprint output does not) is unaddressed. The H-36 circuit breaker governs routing loops across skills; it does not govern intra-session partial completion of cross-framework sequences.

The orchestrator's compound responsibilities (6 distinct stateful operations identified in DA-003-I3) make failure mode documentation non-trivial. The ux-orchestrator is architecturally more complex than any existing Jerry orchestrator and the implementation risk scales with undocumented failure behavior.

**Evidence:**
1. The routing triage flowchart has no MCP failure branch -- the flowchart ends at sub-skill invocation nodes with no failure exits.
2. BLOCK state documented as "refuses to route and directs user" -- no specific content for the "directs" action.
3. Cross-framework handoff AC requires testing 2 sequences but defines no recovery behavior for partial completion.
4. No failure recovery documentation was added to the Acceptance Criteria > Parent Orchestrator section in R3.

**Impact:**
An implementing developer receives a specification with happy-path detail and no failure recovery guidance for the most complex orchestrator in the Jerry skill inventory. Failure behavior will be inferred during implementation, producing inconsistent recovery behavior across the 6 compound operations. Post-launch, users experiencing BLOCK states, MCP failures, or partial-completion sequences receive implementation-specific behavior rather than design-specified behavior.

**Dimension:** Completeness

**Response Required:** Add an "Orchestrator Failure Behavior" subsection to the Acceptance Criteria > Parent Orchestrator section (or to the Key Design Decisions > routing section) specifying recovery behavior for: (a) MCP pre-check failure -- what the orchestrator routes to and what message it displays; (b) WAVE-N-SIGNOFF.md BLOCK state -- the specific information the orchestrator provides and whether direct sub-skill invocation is available; (c) cross-framework sequence partial failure -- whether the orchestrator preserves partial state, retries the failed step, or resets and informs the user. Minimum: one documented behavior per failure mode, even if brief.

**Acceptance Criteria:** At least 3 orchestrator failure modes are documented with explicit recovery behavior descriptions. The routing triage flowchart OR an accompanying failure behavior table covers the MCP failure path. BLOCK state behavior specifies what the orchestrator tells the user and confirms direct sub-skill invocation availability.

---

### DA-004-I4: Blind Evaluation Rubric "3 Independent Evaluators" Is Operationally Infeasible for the Target Population [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Pre-Launch Validation |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unstated assumptions, Actionability) |
| **Prior ID** | NEW finding (created by R3's Pre-Launch Validation AC addition) |

**Claim Challenged:**
> "Comparison uses a blind evaluation rubric: 3 independent evaluators score both the AI-augmented output and a manually-produced reference output on completeness, actionability, and time-to-insight without knowing which is AI-augmented."

**Counter-Argument:**
The pre-launch validation AC's blind evaluation requirement assumes that 3 independent evaluators are available to the implementing team before Wave 1 merge. This assumption fails for the target population: solo practitioners, 2-person startups, and tiny teams without UX specialists. A solo implementer building Wave 1 cannot independently recruit 3 evaluators from within their team. The "independent" requirement (evaluators cannot know which output is AI-augmented) further constrains the evaluator pool: team members who watched the implementation cannot credibly evaluate blind. The requirement to produce both an AI-augmented output AND a "manually-produced reference output" additionally requires the implementer to produce high-quality manual UX analyses (e.g., a Nielsen heuristic evaluation against a reference design) to serve as the comparison baseline. Manual production of reference UX analyses is itself a skilled UX task -- the target population is defined as teams without UX specialists.

The S-003 SM-004-I4 steelman correctly identifies this section as needing calibration rationale (why 15%, why those dimensions) and recommends the strengthened derivation. But SM-004-I4 does not question the feasibility of the 3-independent-evaluators requirement itself -- that is the devil's advocate gap. The steelman strengthens the rubric's justification; this finding challenges whether the evaluation protocol can be executed at all.

**Evidence:**
1. Target population: "Solo practitioner (1)," "Dev+Designer pair (2)," "Small cross-functional team (3-5)" -- teams of 1-5 where UX is explicitly not a specialist responsibility.
2. "Independent reviewer = any Jerry Framework user who did NOT author the sub-skill under review" -- the AI-First Design independent reviewer definition uses "any Jerry Framework user," suggesting the broader Jerry community as the evaluator pool. The pre-launch validation AC does not make this community-evaluator option explicit. 3 evaluators from the Jerry community for a Wave 1 pre-launch validation implies a community engagement mechanism that does not currently exist in the framework.
3. "manually-produced reference output" -- producing a manual Nielsen heuristic evaluation for a reference design requires UX expertise. A team that cannot apply Nielsen heuristics manually is exactly the target audience for `/ux-heuristic-eval`; asking them to produce a ground-truth manual evaluation before using the tool creates a bootstrap paradox.

**Impact:**
The pre-launch validation AC as written is a gatekeeping requirement that the target population cannot meet without: (a) recruiting UX-specialist evaluators from outside the team (cost and access barriers), (b) engaging the Jerry community in a structured evaluation process (community infrastructure not yet defined), or (c) producing manual reference analyses that require the expertise the skill is designed to provide. If the gate cannot be met, Wave 1 either never launches or the AC is treated as aspirational rather than enforced -- neither of which is the design intent.

**Dimension:** Actionability

**Response Required:** Revise the blind evaluation rubric protocol to specify an evaluator pool accessible to the target population. Options: (a) define the evaluator pool as "3 participants from the Jerry community" with a community engagement mechanism described (e.g., "post to the Jerry project for community evaluation volunteers prior to Wave 1 PR merge"), (b) reduce to 1 independent evaluator with a rubric-based structured review (trading blind evaluation rigor for feasibility), OR (c) define "manually-produced reference output" with a qualification threshold accessible to non-specialists (e.g., "a reference output produced using only the published NNGroup 10 heuristics summary without AI assistance" -- removes the expert knowledge requirement). The bootstrap paradox (target users producing manual analyses to evaluate the tool that automates those analyses) must be acknowledged and resolved.

**Acceptance Criteria:** The blind evaluation protocol specifies an evaluator pool that a solo practitioner or 2-person team can access without UX expert recruitment. The "manually-produced reference output" requirement either names a non-specialist production method or uses a published reference (NNGroup, Intercom JTBD Playbook) as the comparison artifact rather than a team-produced manual analysis.

---

### DA-005-I4: MEDIUM Confidence Gate Validation Paths Remain Undefined [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Synthesis Hypothesis Validation |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unstated assumptions, Actionability) |
| **Prior ID** | DA-005-I3 (PERSISTENT -- unchanged in R3) |

**Claim Challenged:**
> "MEDIUM: Requires expert review OR validation against 2-3 real user data points. The output includes a 'Validation Required' section. The agent does not generate design recommendations until a named validation source is provided."

**Counter-Argument:**
This is the third consecutive iteration in which "expert review OR 2-3 real user data points" appears without operational definition. The validation requirement is the most frequently triggered gate in the portfolio (B=MAP diagnosis, JTBD from secondary research). Without defining "expert" (minimum qualification accessible to tiny teams) and "real user data points" (minimum fidelity), teams either: (a) interpret the gate strictly and cannot use MEDIUM-confidence outputs because they lack expert access, or (b) interpret it loosely and trivially satisfy it with nominal "validation" that does not reduce confidence risk.

The `synthesis-validation.md` rules file is specified in the directory structure and is described as the location for this protocol. Its contents are not specified in the issue body. If the definitions will be deferred to implementation-time, the AC that requires "`synthesis-validation.md` implements the 3-tier confidence gate protocol" provides no quality guarantee on the definitions' substance.

**Evidence:**
Synthesis Hypothesis Validation section: "Requires expert review OR validation against 2-3 real user data points" -- text unchanged across R1, R2, R3. No AC or directory structure addition specifies minimum qualification definitions. `synthesis-validation.md` is in the directory structure but its content is not specified in any AC.

**Impact:**
The MEDIUM confidence gate -- designed to prevent over-reliance on AI-generated behavioral diagnoses and job statements -- is architecturally correct but operationally empty. The gate behavior ("agent does not generate design recommendations until named validation source is provided") is structural. The gate quality ("what counts as a valid validation source") is undefined. For the most frequently triggered gate in the portfolio, this is the functional equivalent of a security checkpoint that requires showing ID but does not specify what documents count as ID.

**Dimension:** Actionability

**Response Required:** Add an AC specifying that `synthesis-validation.md` MUST include minimum qualification definitions for both MEDIUM gate validation paths: (a) "expert review" minimum qualification (e.g., "a person with 2+ years of product management, UX, or closely related domain experience who has not participated in building the product under review"); (b) "real user data points" minimum fidelity (e.g., "at least 1 completed session of > 5 minutes with a person who is or closely resembles a member of the target user population, producing at minimum a recorded behavioral observation"). Definitions must be accessible to non-UX-specialist evaluators.

**Acceptance Criteria:** An AC explicitly commits that `synthesis-validation.md` contains operational definitions for both MEDIUM gate validation paths. The definitions are accessible to a developer without UX specialist training (examples provided; jargon-free).

---

### DA-006-I4: Capacity Check Persists Without Derivation or Mechanism [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Parent Orchestrator Routes via Lifecycle-Stage Triage |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Logical flaws, Unstated assumptions) |
| **Prior ID** | DA-007-I3 (PERSISTENT -- unchanged in R3) |

**Claim Challenged:**
> "Checks team UX capacity -- if < 20% of one person's time, restricts recommendations to Wave 1 sub-skills"

**Counter-Argument:**
The routing triage flowchart shows the capacity check as a hard gate (Step 2, directly after the onboarding warning) that restricts to Wave 1 before any product stage routing. This gate is operationally a user self-report with no verification. The WAVE-N-SIGNOFF.md enforcement system is the deterministic wave gate (file exists / passes criteria / is blocked). The capacity check adds a second wave gate that:

1. Is not correlated with the actual WAVE-N-SIGNOFF.md criteria (completing entry criteria does not require 20%+ UX time).
2. Overrides the deterministic WAVE-N-SIGNOFF.md gate in the wrong direction: a team reporting 15% UX time but with a completed WAVE-2-SIGNOFF.md is blocked from Wave 3+ routing by the capacity check, even though their objective wave gate says they are qualified.
3. The 20% threshold has no documented derivation for three iterations. What is the minimum UX time allocation required to benefit from Wave 2-5 sub-skills? The wave entry criteria (WAVE-N-SIGNOFF.md) operationalize this question objectively; the 20% threshold is a parallel and inconsistent answer.

R3 added no change to the capacity check. The flowchart is unchanged. The threshold remains underived. The redundancy with WAVE-N-SIGNOFF.md remains unresolved.

**Evidence:**
Routing triage flowchart Step 2: "UX capacity < 20% of 1 person?" → Yes → "Recommend Wave 1 only" → continues to MCP check. The "Recommend Wave 1 only" node in the flowchart routes to `WaveLimit["Recommend Wave 1 only"]` which then feeds into `MCP`. This creates the routing sequence: capacity check → Wave 1 limit → MCP check → Stage routing. A team below 20% UX capacity is Wave-1-limited before the WAVE-N-SIGNOFF.md check occurs.

**Impact:**
A team with 15% UX time that has completed Wave 1 and Wave 2 objectives (has WAVE-2-SIGNOFF.md) is incorrectly restricted to Wave 1 recommendations by the capacity check, despite the deterministic gate indicating Wave 3 readiness. The capacity check creates false negatives (teams that are Wave-3-qualified but told Wave 1 only) and provides no false positive prevention that WAVE-N-SIGNOFF.md doesn't already handle.

**Dimension:** Methodological Rigor

**Response Required:** Either (a) remove the capacity check and rely exclusively on WAVE-N-SIGNOFF.md for wave gating (recommended -- removes redundancy and inconsistency), OR (b) reclassify the capacity check as advisory only (update the flowchart to show "Recommend Wave 1 focus" as a recommendation, not a routing gate), and specify how the capacity check interacts with WAVE-N-SIGNOFF.md when they conflict (WAVE-N-SIGNOFF.md takes precedence). Document the 20% threshold derivation if retained.

**Acceptance Criteria:** Capacity check is either removed from the routing flowchart OR reclassified as advisory with explicit acknowledgment that WAVE-N-SIGNOFF.md is the authoritative wave gate. Routing flowchart reflects the updated behavior.

---

### DA-007-I4: Design Sprint 2-Person Adaptation Remains Unvalidated [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | The Solution > Sub-Skill #9 (/ux-design-sprint) > Team size adaptation |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Contradicting evidence, Historical precedents) |
| **Prior ID** | DA-011-I3 (PERSISTENT -- unchanged in R3) |

**Claim Challenged:**
> "For 2-person teams, the sprint collapses to 1-2 days with the AI filling the 'missing participant' roles (note-taker, sketch generator, prototype builder)"

**Counter-Argument:**
This claim now intersects with DA-001-I4 (sketch generation and prototype building unverified) to create a compound problem: the 2-person sprint adaptation's primary AI contributions ("sketch generator, prototype builder") are themselves unverified capabilities. Even if the general claim were qualified to "facilitation roles only," the team size adaptation section does not address: multi-day session state persistence, decision legitimacy, or the quality difference in sprint outputs between 4-5 participants and 2-person + AI.

AJ&Smart's Design Sprint 2.0 methodology (the cited source) explicitly requires a "Decider" role with organizational authority over the product. For a 2-person team where both participants are co-founders or co-developers with equal authority, the sprint's decision-making dynamics differ fundamentally from the methodology's design. AI cannot fill the Decider role (P-020: user authority). The 2-person adaptation as written positions AI in the note-taker, sketch generator, and prototype builder roles -- but the "missing participant" whose absence most affects sprint quality is the Decider, not the note-taker or sketch generator.

Three iterations without a citation or quality-difference characterization indicates this is not an oversight -- it is a claim the deliverable does not have evidence to support. The honest characterization (sprint produces directional outputs requiring stakeholder alignment, not final product decisions) would improve the sub-skill's credibility without reducing its value.

**Evidence:**
1. Team size adaptation text unchanged across R1, R2, R3.
2. AJ&Smart Design Sprint 2.0 published methodology requires Decider role with organizational authority (not an AI-fillable role per P-020).
3. DA-001-I4: "sketch generator" and "prototype builder" roles are themselves unverified LLM+Figma capabilities.
4. Design Sprint non-MCP fallback: "Miro-only mode; manual prototype reference" -- the fallback drops prototype building to manual, confirming it is a primary-path aspiration.

**Impact:**
Teams investing in a 2-person + AI Design Sprint may produce artifacts they treat as sprint decision outputs without recognizing the quality and legitimacy differences from a full-team sprint. This is a misalignment between expectation (equivalent sprint with AI filling roles) and reality (facilitation-assisted sprint with reduced decision diversity and unverified AI capability in key roles).

**Dimension:** Evidence Quality

**Response Required:** Revise the team size adaptation section to characterize what the 2-person + AI sprint preserves (structured process, templates, AI facilitation, ideation prompting) and what it reduces (decision diversity, collaborative buy-in, Decider legitimacy, AI-capability-dependent Day 2-3 contributions). Add a quality caveat: "2-person sprints produce directional inputs for further validation, not final product decisions from an authoritative Decider. Treat outputs as hypotheses requiring broader stakeholder alignment." OR provide a citation to validated 2-person + AI sprint methodology.

**Acceptance Criteria:** Team size adaptation section accurately characterizes the quality difference from 4-5 person sprint format, with a quality caveat for decision legitimacy, OR a citation to a validated source for 2-person + AI Design Sprint effectiveness.

---

### DA-008-I4: Crisis Mode BLOCK State Creates Undocumented Mandatory Bypass [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Parent Orchestrator Routes > Crisis mode; Wave enforcement 3-state behavior |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Internal contradictions, Logical flaws) |
| **Prior ID** | DA-008-I3 (PARTIALLY resolved in R3 for WARN state; BLOCK state conflict new) |

**Claim Challenged:**
> Crisis mode 3-skill sequence: "Heuristic Eval -> Behavior Design -> HEART" activates "when the user explicitly describes urgency ('urgent', 'critical UX issue', 'users are leaving') or when the orchestrator detects multiple prior sub-skill invocations without resolution."
>
> BLOCK state behavior (R3 addition): "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process."

**Counter-Argument:**
R3 added the WAVE-N-SIGNOFF.md 3-state enforcement, which introduced a hard BLOCK state for missing signoff files. Crisis mode bypasses wave prerequisites -- this was DA-008-I3's finding, which R3 partially addressed by adding the WARN state documentation. However, the BLOCK state (file does not exist) creates a new unresolved conflict:

Scenario: A team at Wave 0 (no completed waves, no signoff files) encounters a critical UX problem. They invoke `/user-experience` with "users are leaving -- urgent." Crisis mode activation criteria are met. The crisis sequence requires Behavior Design (Wave 4) and HEART (Wave 2). Both require WAVE-N-SIGNOFF.md files that do not exist. The BLOCK state behavior: "Orchestrator refuses to route to Wave N+1 sub-skills."

Which behavior wins -- crisis mode or BLOCK state? The specification defines both behaviors without defining their precedence. If BLOCK wins: crisis mode is non-functional for Wave 0-1 teams, which is exactly the team that most urgently needs diagnostic help. If crisis mode wins: BLOCK state is silently overridden in the most urgent user scenario, creating an undocumented bypass of the wave gate system.

The WARN state does not have this problem (the orchestrator asks for user confirmation); WARN preserves user authority (P-020). The BLOCK state is a hard refusal. The interaction between a hard refusal and an urgency-triggered bypass is architecturally undefined.

**Evidence:**
1. Crisis mode invokes Behavior Design (Wave 4) and HEART (Wave 2).
2. BLOCK state: "WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1."
3. A team at Wave 0 with no signoff files + crisis activation: both behaviors are triggered simultaneously. No precedence rule is defined.
4. Crisis mode was intended as an emergency bypass -- the wave bypass documentation (3-field documentation for stall recovery) applies to Wave stall scenarios, not to crisis mode activation.

**Impact:**
Crisis mode for Wave 0-1 teams (most urgently in need of diagnostic help) either silently bypasses the BLOCK gate (undocumented) or is non-functional (defeats the purpose of crisis mode). Neither outcome is documented. Implementing developers must infer the precedence rule, producing inconsistent behavior.

**Dimension:** Internal Consistency

**Response Required:** Define the precedence rule between crisis mode and BLOCK state. Recommended: "Crisis mode overrides BLOCK state for sub-skills in the crisis sequence, with a mandatory quality warning: 'Operating in crisis mode without Wave N prerequisites. [Sub-Skill X] output quality is degraded -- behavioral data and metric baselines required for reliable diagnosis. Use crisis output as directional input, not confirmed diagnosis.'" Document this as the explicit resolution in the crisis mode or wave enforcement section.

**Acceptance Criteria:** The relationship between crisis mode activation and BLOCK state is explicitly documented with a defined precedence rule. If crisis mode can override BLOCK, the output quality degradation warning is defined. If BLOCK overrides crisis mode, the crisis sequence degrades gracefully to Wave-0-accessible sub-skills only (Heuristic Eval).

---

### DA-009-I4: AI-First Design Enabler Expiry Field Remains Unnamed [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Known Limitations > AI-First Design: Conditional Status |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Actionability) |
| **Prior ID** | DA-010-I3 (PARTIALLY PERSISTENT -- downgraded from Major to Minor due to MCP runbook AC addition, but field naming gap remains) |

**Claim Challenged:**
> "The expiry deadline is tracked as a worktracker entity field."

**Counter-Argument:**
The worktracker entity schema does not include a standard expiry_date field. The orchestrator's AI-First Design expiry check requires: (a) a named frontmatter field in the Enabler entity, (b) a parsing mechanism (`jerry ast frontmatter` per H-33), (c) a date comparison against current date, (d) routing behavior change on expiry detection. None of these are specified. "Tracked as a worktracker entity field" is a process statement that does not enable automated enforcement. Three iterations without naming the field suggests this is an implementation detail being deferred -- but it is a specification gap that blocks implementing the 90-day expiry enforcement.

**Dimension:** Actionability

**Response Required:** Name the Enabler frontmatter field (e.g., `Expiry-Date: YYYY-MM-DD`). Specify the orchestrator check: "At Wave 5 invocation, the orchestrator reads the AI-First Design Enabler via `jerry ast frontmatter {enabler-path}`, compares the `Expiry-Date` field against current date, and on expiry routes to Design Sprint only with a substitution notice." One sentence per step is sufficient.

**Acceptance Criteria:** Enabler frontmatter field name specified in the Known Limitations section or Wave 5 AC. Orchestrator check mechanism defined (tool invocation pattern or file read pattern). Wave 5 routing behavior on expiry explicitly described.

---

### DA-010-I4: Post-Launch Success Metrics Have No Collection Mechanism [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Acceptance Criteria > Post-Launch Success Metrics |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Logical flaws) |
| **Prior ID** | DA-013-I3 (PERSISTENT -- unchanged in R3) |

**Claim Challenged:**
> "Track: number of unique teams that complete Wave 1 within 30 days of first invocation (target: baseline establishment, no threshold for V1)"

**Counter-Argument:**
The 5 "Track:" ACs have no collection mechanism, no session identity mechanism, and no instrumentation scope in the directory structure. "Track: average S-014 quality score of sub-skill outputs across all invocations" requires automated score aggregation across invocations that is not part of the current Jerry architecture. These are aspirational metrics listed as ACs, implying they will be implemented at launch. If they cannot be collected at launch, they should be moved to the V2 Roadmap or reclassified as "aspirational monitoring targets requiring instrumentation enabler."

**Dimension:** Actionability

**Response Required:** Reclassify the 5 "Track:" items as V2 aspirational targets requiring a separate instrumentation enabler, OR specify the collection mechanism for each metric. Moving them to V2 Roadmap with a parenthetical "(Requires instrumentation enabler)" is a one-line change that resolves the AC completeness issue without expanding scope.

**Acceptance Criteria:** The 5 post-launch success metrics are either (a) moved to V2 Roadmap with instrumentation enabler noted, OR (b) each metric's AC specifies its collection mechanism with implementation in scope for this issue.

---

### DA-011-I4: Wave 5 Diagrams Do Not Reflect Conditional Structure [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions > Wave Deployment (gantt chart, mermaid diagram) |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Unaddressed risks) |
| **Prior ID** | DA-015-I3 (PERSISTENT -- unchanged in R3) |

**Claim Challenged:**
The gantt chart marks `/ux-ai-first-design` as `crit` (critical path). The mermaid architecture diagram shows it with "(CONDITIONAL)" label.

**Counter-Argument:**
The substitution path means Wave 5 is a permanent 1-sub-skill wave if the Enabler expires. The gantt chart shows both Wave 5 sub-skills as critical path items without showing the conditional branch. Developers reading the gantt at Wave 5 implementation time after Enabler expiry would see a 2-sub-skill Wave 5 but only 1 deliverable. The 1-sub-skill scenario is implied but not diagrammed.

**Dimension:** Completeness

**Response Required:** Update the gantt chart to show the conditional structure: mark Design Sprint as the guaranteed Wave 5 component and AI-First Design as conditional with note "90-day expiry; reverts to Design Sprint-only."

**Acceptance Criteria:** Wave 5 diagrams reflect both scenarios (1-sub-skill on Enabler expiry, 2-sub-skill on Enabler completion). The permanent 1-sub-skill scenario is visually distinguishable.

---

### DA-012-I4: Wave 3 Entry Criterion Leads With "Launched Product" Framing [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions > Wave Deployment |
| **Strategy Step** | Step 3: Construct Counter-Arguments (Lens: Alternative interpretations) |
| **Prior ID** | DA-012-I3 (PERSISTENT -- unchanged in R3) |

**Claim Challenged:**
> Wave 3 entry: "Launched product with an analytics data source (for HEART) OR completed 1 Lean UX build-measure-learn hypothesis cycle"

**Counter-Argument:**
Leading with "Launched product" creates a mental model that Wave 3 is post-launch only. The Lean UX alternative path (achievable pre-launch) is listed second. Pre-launch teams may self-exclude from Wave 3 without reading the OR condition. The reorder is a one-line change; the OR path is the more achievable and pre-launch-compatible option for the median Part-time UX user.

**Dimension:** Completeness

**Response Required:** Reorder to lead with the pre-launch path: "Completed 1 Lean UX build-measure-learn hypothesis cycle OR launched product with an analytics data source."

**Acceptance Criteria:** Wave 3 entry criterion lists the pre-launch Lean UX path first.

---

## Step 4: Response Requirements

### P0 (Critical -- MUST resolve before merge)

| ID | Finding | Required Action | Acceptance Criteria |
|----|---------|----------------|---------------------|
| DA-001-I4 | Design Sprint AI capability claims unverified | Evidence citation for 20+ sketch generation and interactive Figma prototype building, OR scope "What AI does" to verified current capability; add Design Sprint output type to synthesis confidence classification | Evidence cited OR "What AI does" revised; Wave 5 benchmark consistent with description; confidence classification includes Design Sprint |
| DA-002-I4 | Wave 5 unreachable for median target population (Part-time UX) | Pre-launch bypass path to Design Sprint, OR wave restructuring for pre-launch teams, OR explicit contradiction acknowledgment with resolution guidance | Wave documentation addresses Part-time UX / pre-launch Design Sprint access path without contradiction |
| DA-003-I4 | ux-orchestrator failure modes undocumented | Document 3 failure modes (MCP failure, BLOCK state, cross-framework partial failure) with recovery behavior | 3 failure modes documented; routing flowchart or failure table covers MCP failure path; BLOCK state specifies user communication and direct invocation availability |

### P1 (Major -- SHOULD resolve; require justification if not)

| ID | Finding | Required Action | Acceptance Criteria |
|----|---------|----------------|---------------------|
| DA-004-I4 | Blind evaluation 3-evaluators infeasible for target population | Define accessible evaluator pool (community mechanism, reduced evaluator count, or non-specialist reference production method); resolve bootstrap paradox for manually-produced reference output | Evaluator pool accessible to solo practitioner or 2-person team; manual reference output method defined without UX expertise requirement |
| DA-005-I4 | MEDIUM confidence gate validation paths undefined | Add AC committing synthesis-validation.md to include operational definitions for "expert review" and "real user data points" | AC explicitly commits to operational definitions; examples accessible to non-specialists |
| DA-006-I4 | Capacity check lacks derivation and conflicts with WAVE-N-SIGNOFF.md | Remove capacity check (recommended) OR reclassify as advisory with WAVE-N-SIGNOFF.md precedence | Flowchart updated; capacity check removed OR reclassified as advisory; WAVE-N-SIGNOFF.md is authoritative wave gate |
| DA-007-I4 | Design Sprint 2-person adaptation unvalidated | Citation OR limitation statement characterizing quality difference; quality caveat for decision legitimacy | Team size adaptation section accurately describes quality difference from 4-5 person format |
| DA-008-I4 | Crisis mode BLOCK state conflict undocumented | Define precedence rule between crisis mode and BLOCK state; document crisis quality warning for missing prerequisites | Precedence rule documented; quality degradation warning defined for crisis + BLOCK interaction |

### P2 (Minor -- MAY resolve; acknowledgment sufficient)

| ID | Finding | Required Action |
|----|---------|----------------|
| DA-009-I4 | Expiry field unnamed | Name Enabler frontmatter field; specify orchestrator check mechanism |
| DA-010-I4 | Success metrics no collection mechanism | Move to V2 Roadmap with instrumentation enabler note OR specify collection mechanism per metric |
| DA-011-I4 | Wave 5 diagrams missing conditional structure | Update gantt chart to show expiry branch and 1-vs-2 sub-skill conditional |
| DA-012-I4 | Wave 3 entry framing | Reorder Wave 3 entry criterion to lead with pre-launch Lean UX path |

---

## Step 5: Scoring Impact

| Dimension | Weight | Impact | DA Findings | Rationale |
|-----------|--------|--------|-------------|-----------|
| Completeness | 0.20 | Negative | DA-003-I4, DA-008-I4, DA-011-I4, DA-012-I4 | ux-orchestrator failure modes (DA-003-I4 Critical) is the highest weight gap; crisis mode BLOCK state conflict (DA-008-I4 Major) is a design contradiction uncovered by R3's own BLOCK state addition; Wave 5 diagram (DA-011-I4) and Wave 3 framing (DA-012-I4) are documentation completeness gaps at Minor |
| Internal Consistency | 0.20 | Negative | DA-002-I4, DA-006-I4, DA-008-I4 | Part-time UX median vs. Wave 5 restriction (DA-002-I4 Critical) is a persistent logical contradiction; capacity check vs. WAVE-N-SIGNOFF.md (DA-006-I4 Major) creates a second inconsistency between two wave gates; crisis mode vs. BLOCK state (DA-008-I4 Major) is a new contradiction from R3 additions |
| Methodological Rigor | 0.20 | Negative | DA-001-I4, DA-002-I4, DA-006-I4 | Unverified Design Sprint AI claims (DA-001-I4 Critical) undermine the methodology's most complex sub-skill; wave accessibility contradiction (DA-002-I4) undermines the deployment methodology for the median user; capacity check without derivation (DA-006-I4) is a methodology-layer redundancy |
| Evidence Quality | 0.15 | Negative | DA-001-I4, DA-007-I4 | Design Sprint capability claims (DA-001-I4) and 2-person adaptation (DA-007-I4) both lack evidence across 3 iterations; these are the portfolio's most specification-confident claims with the weakest evidentiary basis |
| Actionability | 0.15 | Negative | DA-004-I4, DA-005-I4, DA-006-I4, DA-009-I4, DA-010-I4 | Blind evaluation 3-evaluators infeasible (DA-004-I4), MEDIUM gate undefined (DA-005-I4), and expiry field unnamed (DA-009-I4) are direct blockers to implementing the quality enforcement mechanisms; success metrics without collection mechanism (DA-010-I4) makes the post-launch monitoring AC unexecutable |
| Traceability | 0.10 | Neutral | DA-009-I4 | Expiry field naming (DA-009-I4 Minor) is a traceability gap; other findings do not affect the document's existing traceability strengths (tournament provenance, wave signoff file naming, references section, WSM methodology). Net traceability is neutral given R3's provenance improvements (handoff schema, synthesis AC). |

**Overall Assessment:** Targeted revision required. Three Critical findings persist from Iter 3 (DA-001-I4, DA-002-I4, DA-003-I4) -- these are not new observations; they have been identified across multiple iterations without resolution. The additional 5 Major findings (DA-004-I4 through DA-008-I4) are a mix of R3-introduced gaps (DA-004-I4 from blind evaluation rubric addition, DA-008-I4 from BLOCK state addition) and persistent under-specification (DA-005-I4, DA-006-I4, DA-007-I4). R3 produced genuine structural improvements in the enforcement layer (WAVE-N-SIGNOFF.md 3-state, handoff contract, MCP runbook AC). The remaining work is primarily: resolving 3 persistent Critical findings that require either evidence provision or honest scope qualification, and closing 5 Major gaps that are specification completeness issues rather than architectural redesigns.

---

## Execution Statistics

- **Total Findings:** 12 (3 Critical, 5 Major, 4 Minor)
- **Critical:** 3 (DA-001-I4, DA-002-I4, DA-003-I4 -- all persistent from Iter 3)
- **Major:** 5 (DA-004-I4 new from R3; DA-005-I4, DA-006-I4, DA-007-I4 persistent; DA-008-I4 new from R3)
- **Minor:** 4 (DA-009-I4, DA-010-I4, DA-011-I4, DA-012-I4 -- all persistent from Iter 3)
- **Protocol Steps Completed:** 5 of 5
- **Prior findings RESOLVED in R3:** DA-004-I3 (partially), DA-006-I3, DA-008-I3 (partially), DA-009-I3, DA-010-I3 (partially)
- **Prior findings PERSISTENT:** DA-001-I3, DA-002-I3, DA-003-I3, DA-005-I3, DA-007-I3, DA-011-I3, DA-012-I3, DA-013-I3, DA-014-I3, DA-015-I3
- **New findings this iteration:** DA-004-I4 (blind evaluation evaluator feasibility -- created by R3 blind rubric AC), DA-008-I4 (crisis mode BLOCK state conflict -- created by R3 BLOCK state definition)

---

*Strategy Execution Report*
*Strategy: S-002 (Devil's Advocate)*
*Template: `.context/templates/adversarial/s-002-devils-advocate.md`*
*Deliverable: `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`*
*Executed: 2026-03-03T00:00:00Z*
*Iteration: 4*
