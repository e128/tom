# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context

- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Criticality:** C4 (Tournament Iteration 4)
- **Revision under review:** R8 (score 0.848 REVISE, targeting >= 0.95)
- **H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (SM-001, SM-002, SM-003 findings incorporated into R8); confirmed in revision log.

---

## Pre-Mortem Header

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** UX Framework Selection: Weighted Multi-Criteria Analysis (R8)
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied on prior tournament iterations; SM-001/SM-002/SM-003 steelman improvements incorporated into R8 (confirmed via revision log, document preamble, and Section 1 WSM independence resolution).

**Failure Scenario:** "It is September 2026. The `/user-experience` skill was launched based on this analysis. Six months later, the skill is in partial use but failing its core mandate. Three of the ten sub-skills are effectively blocked or operating in degraded mode: `/ux-ai-first` never launched because the Enabler was never completed; `/ux-design-sprint` is rarely used because implementers did not understand Wave 5 was locked; the synthesis hypothesis validation protocol gates exist in the analysis but were never wired into sub-skill implementations because the analysis contains no implementation specification for how the gates mechanically operate. Teams that adopted the skill report that synthesis hypothesis outputs are routinely being used as findings without validation because there is no enforcement mechanism in the skill definitions themselves. The analysis correctly identified all the risks -- but described mitigations at the policy level without creating the implementation artifacts that would make those mitigations operational."

---

## Findings Summary

| ID | Severity | Finding | Section |
|----|----------|---------|---------|
| PM-001-I4 | Critical | Synthesis hypothesis validation gates have no implementation specification -- protocol exists as policy but cannot be enforced in skill definitions | Section 7.5 |
| PM-002-I4 | Critical | AI-First Design exclusion trigger has no automated monitoring mechanism; the 30-day expiry is stated but the operational check requires a human to look for it | Section 3.8 |
| PM-003-I4 | Major | Wave 5 conditional lock is documented in routing tables but the parent skill SKILL.md does not yet exist -- the routing mechanism itself is a future artifact | Section 7.1/7.4 |
| PM-004-I4 | Major | MCP owner succession protocol requires worktracker entities to be created "at Enabler creation time" but no worktracker Enabler has been created yet; the cascade of required artifacts is uninitialized | Section 3.8/7.3 |
| PM-005-I4 | Major | The analysis is conditioned on "analyst-derived" lifecycle categorization that has not been externally validated -- if a downstream implementer challenges the minimality claim, no external arbiter exists | Document preamble (MINIMALITY CLAIM QUALIFICATION) |
| PM-006-I4 | Major | Confidence level definitions for synthesis hypothesis outputs (HIGH/MEDIUM/LOW) in Section 7.5 do not match the confidence labeling conventions used in Sections 3.1-3.10 -- implementers face ambiguity about which definition governs | Sections 3.1-3.10 vs. Section 7.5 |
| PM-007-I4 | Major | V2 scoping trigger criteria require monitoring data (invocation counts, team reports) that no collection mechanism exists to gather -- triggers are defined but unobservable | Section 4 (V2 Scoping Triggers) |
| PM-008-I4 | Minor | The crisis triage sequence (option j) specifies time targets ("under 35 minutes," "same day," "within 1 week") that are not aligned with the qualified time estimates in Section 3.1 (30-35 minutes for a complete heuristic eval) -- creates inconsistent expectations | Sections 7.1, 7.2, 3.1 |
| PM-009-I4 | Minor | Free-tier team configuration note (Section 7.4) claims `/ux-heuristic-eval` works in "screenshot-input mode, no Figma required" but the Required MCP table in Section 7.3 classifies Figma as "Required for core function" for this sub-skill -- direct contradiction | Sections 7.3, 7.4 |
| PM-010-I4 | Minor | AI-First Design framework review cadence (Section 3.8) specifies "accurate as synthesized in Q1 2026; re-validate before Q4 2026" but the Enabler may not be completed until 30 days post-kickoff -- the cadence clock starts at a point that has not yet occurred | Section 3.8 |

---

## Detailed Findings

### PM-001-I4: Synthesis Hypothesis Validation Protocol Has No Implementation Specification [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.5 (Synthesis Hypothesis Validation Protocol) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical/Process category) |
| **Failure Category** | Process |
| **Likelihood** | High |
| **Priority** | P0 |
| **Affected Dimension** | Actionability (0.15) |

**Evidence:**
Section 7.5 states: "Gates fire at skill invocation time (when the sub-skill produces the synthesis output), not at document-generation time." The protocol specifies three confidence levels (HIGH/MEDIUM/LOW), user acknowledgment actions, and enforcement mechanisms. However, the enforcement mechanism descriptions are behavioral specifications, not implementation specifications:

- HIGH confidence: "Skill surfaces confirmation prompt before producing the design recommendation." -- This describes *what* the skill does but not *how* to implement it.
- MEDIUM confidence: "Skill surfaces validation prompt with the two options." -- Same gap.
- LOW confidence: "Skill labels the output and does NOT produce design recommendations from it." -- Same gap.

No artifact is defined that sub-skill implementers would use to wire these gates into their implementations. There is no prompt template, no gate interface specification, no output schema for the labeled outputs (what does "[UNCONFIRMED SYNTHESIS -- NOT FOR DESIGN DECISIONS]" look like in the sub-skill's actual response?), and no reference to where in the sub-skill lifecycle the invocation intercept occurs.

The scope table in Section 7.5 maps 10 sub-skills to synthesis steps and confidence levels. This is correctly specified. But the analysis provides no bridge from "here is the policy" to "here is the artifact implementers create to enforce it." The gap is between Section 7.5 (analysis deliverable) and the actual sub-skill SKILL.md files that do not yet exist.

**Analysis:**
This is the most operationally critical gap in the deliverable. The synthesis hypothesis validation protocol was added in R8 specifically to address a prior Critical finding (PM-001 from Iter3). But the R8 addition resolves the *analytical* gap (the protocol is now specified) without resolving the *implementation* gap (no implementer can wire this gate without an implementation specification). The analysis correctly identifies the risk that "synthesis hypothesis outputs are routinely being used as findings without validation" -- but the mitigation provided (Section 7.5) is a policy document, not an implementation artifact. When sub-skill implementers build `/ux-jtbd`, they need a concrete specification: "Include this gate at step X; present this prompt text; accept these inputs; label outputs in this schema." Without that, each implementer interprets Section 7.5 differently, leading to inconsistent enforcement or no enforcement.

The pre-mortem failure scenario (teams using synthesis hypothesis outputs as findings without validation) is directly traceable to this gap. The policy exists; the enforcement does not. Policy without enforcement is intention without effect.

**Recommendation:**
Add a sub-section to Section 7.5 titled "Implementation Specification for Sub-Skill Authors" that provides: (a) the exact prompt text for each confidence tier's confirmation prompt; (b) the exact output label strings (so they are consistent across all sub-skills); (c) the invocation intercept point in the sub-skill workflow (after synthesis output generation, before returning to user); (d) a reference implementation using a template that sub-skill authors can adapt. This does not require adding sub-skill SKILL.md files to this analysis -- it requires specifying the interface that those files will implement.

**Acceptance Criteria:** Section 7.5 includes an "Implementation Specification" sub-section with (a) prompt templates for all three confidence tiers, (b) canonical output label strings, and (c) the invocation intercept pattern. A sub-skill author reading only Section 7.5 can implement the gate without ambiguity.

---

### PM-002-I4: AI-First Design Expiry Trigger Has No Automated Monitoring Mechanism [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.8 (AI-First Design, prerequisite management) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process/Resource category) |
| **Failure Category** | Process |
| **Likelihood** | High |
| **Priority** | P0 |
| **Affected Dimension** | Actionability (0.15), Completeness (0.20) |

**Evidence:**
Section 3.8 states: "If the Enabler's DUE DATE passes without DONE status, the following action executes automatically: [Story: Implement `/ux-ai-first`] is marked BLOCKED and replaced with [Story: Implement `/ux-service-blueprinting`] in the backlog, with no further decision required."

The word "automatically" appears twice in this paragraph, and the blocking relationship states: "this Enabler is closed CANCELLED, and [Story: Implement `/ux-service-blueprinting`] is activated without requiring a human substitution decision."

However, the Jerry worktracker is a filesystem-based system. No automation engine exists that monitors worktracker entity DUE DATE fields and executes state transitions at expiry. The "automatic" trigger described here requires a human to: (a) notice the due date has passed, (b) check whether the Enabler is DONE, (c) execute the state transitions manually. The analysis says "no further decision required" -- but it does not eliminate the *action* required.

The "recurring worktracker task titled 'AI-First Design Enabler Ownership Verification' MUST be created at Enabler creation time with quarterly recurrence" is the only procedural mechanism described. But this task has not been created yet (no worktracker Enabler entity exists in the repository based on available context), and the quarterly recurrence is insufficient monitoring for a 30-day expiry trigger.

**Analysis:**
The automatic substitution mechanism is the deliverable's primary risk mitigation for FM-005 (AI-First Design blocking dependency, residual RPN=90 -- the second-highest residual risk in the analysis). If this mechanism does not execute reliably, the AI-First Design blocking risk is unmitigated despite the language of "automatic" execution. The gap is between the declarative specification ("this will happen automatically") and the operational reality (nothing in Jerry's architecture makes this happen without human action).

This creates a specific failure mode: the kickoff date passes, the Enabler is not completed on time, the 30-day mark arrives, but no one notices because the quarterly ownership verification task is the only trigger -- which fires at 90 days, not 30 days. The Service Blueprinting substitution never activates. The `/ux-ai-first` story remains in the backlog, blocked indefinitely.

**Recommendation:**
Replace the "automatic" language with an explicit human action protocol. Specify: (a) who is responsible for checking the Enabler status on Day 30 (the named primary owner); (b) what the check-in procedure is (a worktracker task due on kickoff+30); (c) the manual steps to execute the substitution (update Enabler status to CANCELLED, activate Service Blueprinting story). Also add a Day-30 check-in task (not just the quarterly ownership verification) to the list of required worktracker entities. The quarterly task is appropriate for ownership verification; a separate Day-30 milestone task is needed for the expiry trigger.

**Acceptance Criteria:** Section 3.8 removes the word "automatically" from the trigger description, replaces it with an explicit human action protocol, and specifies a Day-30 milestone worktracker task as a required creation alongside the quarterly ownership verification task.

---

### PM-003-I4: Parent Skill SKILL.md Does Not Exist -- Routing Mechanism Is a Future Artifact [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.1 (Parent Skill and Routing Framework), Section 7.4 (Implementation Sequencing) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical/Process category) |
| **Failure Category** | Process |
| **Likelihood** | High |
| **Priority** | P1 |
| **Affected Dimension** | Completeness (0.20), Actionability (0.15) |

**Evidence:**
Section 7.1 states: "The 10 sub-skills require a `/user-experience` parent skill as their single entry point... The parent skill: 1. Is the **only** entry registered in `mandatory-skill-usage.md` for UX work... 4. Must be created at `skills/user-experience/SKILL.md` before any sub-skill implementation."

The Wave 5 CONDITIONAL labels added in R8 correctly flag `/ux-design-sprint` as "NOT YET IMPLEMENTED until Wave 5 entry criteria are met." But Wave 1 (`/ux-heuristic-eval`, `/ux-jtbd`) and Wave 2 (`/ux-lean-ux`, `/ux-heart-metrics`) are presented without equivalent implementation-status labels -- as if they are available for use. However, none of the sub-skills have been implemented. The `/user-experience` parent SKILL.md does not exist. The routing mechanism described in the 45-line triage flow (options a-j) cannot function because the parent skill that implements it has not been created.

The analysis presents the routing framework as a completed design specification, but the deliverable's own Section 7.4 Wave table shows all 10 sub-skills as future implementation targets. The gap between "this routing will work" and "no implementation of this routing exists yet" is not consistently labeled across the document.

**Analysis:**
This is an internal consistency gap between the routing framework's forward-looking framing and the document's own status labels. Section CC-004 (line 444) states: "These patterns represent design targets for implementation, not descriptions of currently operational capabilities." This disclaimer applies to sub-skill capability claims but has not been extended to the routing mechanism itself. A reader encountering the Section 7.1 routing flows could reasonably interpret them as operational -- especially given that the document uses present-tense language ("Routes users to the correct sub-skill via a brief lifecycle-stage triage") and provides concrete dialogue examples.

The pre-mortem failure scenario surfaces this as: implementers treat the routing framework as a specification they are implementing against, not as a live capability -- but the analysis conflates design target and current state, leading to confusion about what must be built vs. what is already done.

**Recommendation:**
Add a consistent implementation-status header to Section 7 matching the CC-004 forward-looking framing: "All routing mechanisms described in this section are DESIGN SPECIFICATIONS for the `/user-experience` parent skill to be built, not descriptions of current capabilities." Apply the same status label format used for Wave 5 (`[WAVE 5 -- NOT YET IMPLEMENTED]`) uniformly across all wave entries in the routing tables (Waves 1-4 as `[DESIGN SPECIFICATION -- WAVE {N}]`). This provides consistent signaling without removing any content.

**Acceptance Criteria:** Section 7.1 includes a CC-004-style forward-looking framing disclaimer. Section 7.4 wave table entries for Waves 1-4 include status labels matching the Wave 5 CONDITIONAL pattern established in R8.

---

### PM-004-I4: Required Worktracker Entities Have Not Been Created -- The Mitigation Cascade Is Uninitialized [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.8 (AI-First Design Enabler), Section 7.3 (MCP Maintenance Contract) |
| **Strategy Step** | Step 3: Generate Failure Causes (Resource category) |
| **Failure Category** | Resource |
| **Likelihood** | High |
| **Priority** | P1 |
| **Affected Dimension** | Actionability (0.15), Traceability (0.10) |

**Evidence:**
Section 3.8 specifies: "An Enabler entity titled 'AI-First Design Framework Synthesis' MUST be created in the PROJ-020 worktracker before implementation begins." Section 7.3 specifies: "A recurring worktracker task titled 'MCP Ownership Verification' MUST be created at PROJ-020 kickoff." Section 3.8 also specifies: "A recurring worktracker task titled 'AI-First Design Enabler Ownership Verification' MUST be created at Enabler creation time with quarterly recurrence."

Neither the Enabler entity nor the two recurring tasks exist in the repository based on available project context. The analysis mandates creation of specific worktracker artifacts as part of its mitigation plan, but creates none of them. The deliverable describes the mitigation cascade in complete detail (entity type, title, owner requirements, due date computation, blocking relationships, succession protocol, recurrence cadence) but does not execute any step of it.

The mitigation cascade for FM-005 (AI-First Design blocking, RPN=90) and PM-002 (MCP owner succession) depends entirely on these entities existing. If the analysis is accepted without creating these entities, the risk mitigations described are specifications, not controls.

**Analysis:**
This is a structural gap between the analysis deliverable and the implementation artifacts it requires. The analysis describes a detailed control system (Enabler + recurring tasks + succession protocols + blocking relationships) but does not create any component of that system. The control system cannot self-activate from within a markdown document.

In practice, this means whoever reads this analysis and decides to implement the `/user-experience` skill must manually parse 3 separate sections (3.8, 7.3, and the PM-002 succession block) to reconstruct the full list of required worktracker entities. The synthesis risk is high: an implementer creating the Enabler but missing the recurring tasks, or creating both tasks but omitting the succession protocol from the entity, produces a partial control system that may fail exactly when needed.

**Recommendation:**
Add a "Required Implementation Artifacts Checklist" to Section 7 (before the waves table) that consolidates all required worktracker entities into a single actionable list:
- [ ] Enabler: "AI-First Design Framework Synthesis" (owner: TBD primary + secondary; due: kickoff+30; blocking: `/ux-ai-first` story)
- [ ] Task (quarterly): "AI-First Design Enabler Ownership Verification" (creates at Enabler creation; recurrence: quarterly)
- [ ] Task (Day 30): "AI-First Design Enabler Expiry Check" (creates at Enabler creation; due: kickoff+30)
- [ ] Task (quarterly): "MCP Ownership Verification" (creates at PROJ-020 kickoff; recurrence: quarterly)

This does not change any specification -- it synthesizes the scattered requirements into a single pre-launch checklist. The checklist format enables implementers to verify completeness without parsing the full document.

**Acceptance Criteria:** A consolidated "Required Pre-Launch Worktracker Entities" checklist exists in Section 7, listing all entities mandated across Sections 3.8 and 7.3 in a single location with creation owner and trigger.

---

### PM-005-I4: Minimality Proof Rests on Analyst-Derived Categorization With No External Validation Path [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Document preamble (MINIMALITY CLAIM QUALIFICATION block) |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption category) |
| **Failure Category** | Assumption |
| **Likelihood** | Medium |
| **Priority** | P1 |
| **Affected Dimension** | Evidence Quality (0.15), Internal Consistency (0.20) |

**Evidence:**
The MINIMALITY CLAIM QUALIFICATION block in the document preamble states: "The minimality proof relies on a lifecycle-stage-plus-primary-function categorization (Pre-Design, Design, Build, Post-Launch stages; intensive/continuous/evaluation function sub-types) that is analyst-derived, not externally validated. This categorization was constructed to describe the selected frameworks, not as a prior constraint that independently determined selection."

The R8 structured rebuttal (SM-001) provides a three-property defense of the minimality claim for the specific case of Design Sprint vs. Lean UX. However, the broader minimality claim covers all 10 frameworks across 4 stages and 3 function sub-types. The SM-001 rebuttal addresses one pairwise comparison (Design Sprint/Lean UX) but does not address all 45 possible pairwise comparisons among the 10 selected frameworks.

Specifically, the document does not provide a structured defense of these potentially contested pairs:
- JTBD (#6) vs. Lean UX (#5): both involve hypothesis generation about what users want; the document notes their integration path (Design Sprint findings become Lean UX hypotheses) but does not systematically address the redundancy question.
- Nielsen's Heuristics (#1) vs. Microsoft Inclusive Design (#7): both involve design evaluation; Section 7.2 directs users to Heuristic Eval as the "primary tool" and Inclusive Design for "specific knowledge of users with accessibility constraints" -- the boundary is usage-context, not lifecycle-stage.
- HEART (#4) vs. Kano (#9): both involve user satisfaction measurement; the "measurement vs. prioritization" distinction is functional but not lifecycle-stage distinct.

**Analysis:**
The minimality claim is the single most strategically important claim in the analysis -- it justifies why these 10 frameworks and not a different 10. The SM-001 rebuttal correctly strengthens the Design Sprint/Lean UX case. But a challenger could generate plausible minimality objections for other pairs, and the analysis would have no structured response. The qualification in the preamble acknowledges the categorization is "analyst-derived" -- but does not provide a general method for resolving future categorization challenges, only the specific SM-001 defense.

This matters for the pre-mortem scenario because: a decision-maker reviewing the analysis before implementing the skill may challenge the minimality claim for a different pair (e.g., "why Kano AND JTBD -- aren't both about what users want?"). Without a general method, the analyst must respond ad hoc, and the response may not be consistent with the SM-001 methodology.

**Recommendation:**
Extend the SM-001 structured rebuttal methodology into a general minimality test framework with two components: (1) a pairwise redundancy table covering all 10 choose 2 = 45 pairs (or at minimum the 15 pairs involving frameworks with score < 8.00, where redundancy is most plausible), using the three SM-001 properties (cadence orthogonality, output differentiability, C5 portfolio composition test); (2) a standard method for applying the three-property test to any future challenger pair. This transforms the minimality argument from a specific defense (Design Sprint vs. Lean UX) into a general methodology.

**Acceptance Criteria:** The MINIMALITY CLAIM QUALIFICATION block references a completeness table covering the highest-redundancy-risk pairs (minimum: the 6 pairs involving frameworks scoring 7.60-8.00 -- Fogg, Kano, AI-First Design, Microsoft, JTBD) with the three SM-001 properties applied to each.

---

### PM-006-I4: Section 7.5 Confidence Definitions Create Ambiguity With Per-Section AI Execution Taxonomy Labels [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.5 vs. Sections 3.1-3.10 (AI Execution Mode Taxonomy tables) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical/Assumption category) |
| **Failure Category** | Technical |
| **Likelihood** | High |
| **Priority** | P1 |
| **Affected Dimension** | Internal Consistency (0.20) |

**Evidence:**
The AI Execution Mode Taxonomy (Section 1) defines two modes: **Deterministic execution** and **Synthesis hypothesis**. Each framework section (3.1-3.10) uses these two modes in their per-step tables.

Section 7.5 introduces a three-level confidence system: **HIGH confidence synthesis**, **MEDIUM confidence synthesis**, **LOW confidence synthesis**. The Section 7.5 scope table maps sub-skill steps to these three confidence levels:

- `/ux-jtbd` job statement synthesis: "MEDIUM (no direct user data)"
- `/ux-design-sprint` Day 4 thematic analysis: "HIGH (grounded in interview data)"
- `/ux-kano-model` feature priority conflict: "LOW (strategic product judgment required)"

But the per-section AI Execution Mode Taxonomy tables in Sections 3.1-3.10 label the same steps as simply "Synthesis hypothesis" -- without a HIGH/MEDIUM/LOW qualifier. A sub-skill implementer reading Section 3.6 (JTBD) sees "Synthesis hypothesis" for job statement synthesis. A sub-skill implementer reading Section 7.5 sees "MEDIUM" for the same step. The connection between these two labeling systems is not made explicit.

Furthermore, the Fogg B=MAP diagnosis step (Section 3.10) is labeled "Synthesis hypothesis" in the execution taxonomy but mapped to "MEDIUM (data quality determines confidence)" in Section 7.5 -- the confidence level varies by data quality, which is context-dependent. This context-dependency is not reflected in the Section 3.10 taxonomy table.

**Analysis:**
The result is two parallel labeling systems for the same phenomenon. An implementer who reads Section 3.x before Section 7.5 encounters "Synthesis hypothesis" as a binary label. An implementer who reads Section 7.5 first encounters HIGH/MEDIUM/LOW as a three-level system. Neither section explains that the two systems must be read together, or which takes precedence when they conflict (e.g., if a step is "Synthesis hypothesis" in Section 3.x but "HIGH confidence" in Section 7.5 -- can it bypass the synthesis hypothesis gate because of high confidence?).

This ambiguity directly undermines the Section 7.5 enforcement mechanism. If a sub-skill author is implementing the gate for Fogg's B=MAP diagnosis, they need to know: which confidence level fires which gate? The answer is in Section 7.5's scope table, but the Section 3.10 taxonomy table does not reference Section 7.5, so an implementer focused on Section 3.10 may not encounter the gate specification.

**Recommendation:**
Unify the labeling systems by adding confidence level qualifiers to the Section 3.x taxonomy tables, or by cross-referencing Section 7.5 from each taxonomy table. The minimal intervention: add a column to each Section 3.x AI Execution Mode Taxonomy table with "Section 7.5 Confidence Level" as the column header, populated with the value from Section 7.5's scope table. For context-dependent levels (like Fogg's B=MAP diagnosis: "MEDIUM when data quality is sufficient"), note the dependency condition.

**Acceptance Criteria:** Each AI Execution Mode Taxonomy table in Sections 3.1-3.10 either: (a) includes a "Synthesis Confidence Level" column populated from Section 7.5's scope table, or (b) includes a cross-reference note linking to the Section 7.5 scope table entry for that sub-skill. The two labeling systems reference each other unambiguously.

---

### PM-007-I4: V2 Scoping Trigger Criteria Require Monitoring Data That No Collection Mechanism Exists to Gather [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 4 (V2 Scoping Trigger Criteria, SM-009 -- iter3) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process/Technical category) |
| **Failure Category** | Process |
| **Likelihood** | Medium |
| **Priority** | P1 |
| **Affected Dimension** | Actionability (0.15) |

**Evidence:**
Section 4 defines V2 scoping trigger criteria (SM-009): "V2 scoping should begin when any two of the following conditions are met within a single month." The four conditions are:

1. "At least one team reports a major product decision made incorrectly... OR `/ux-design-sprint` produces 3+ untested prototypes in sequence"
2. "The C3=25% MCP-heavy team variant portfolio is activated for >= 20% of `/user-experience` invocations in a month"
3. "Teams report 3+ distinct cases per month of needing AI UX pattern guidance while the Enabler is not DONE"
4. "A team reports a concrete dark pattern complaint or algorithmic bias issue..."

Triggers 2 and 3 require quantitative monitoring of invocation counts and team reports. No mechanism for collecting invocation counts exists in Jerry's current architecture -- the framework is file-based and does not instrument skill invocation frequency. Trigger 2 (20% of invocations use the C3=25% variant) cannot be computed without an invocation counter. Trigger 3 (3+ cases per month of AI UX guidance need) requires a reporting channel for teams to submit cases.

Triggers 1 and 4 are qualitative and self-reporting (a team reports...), which is observable but passive. The 20% threshold in Trigger 2 is not observational without instrumentation.

**Analysis:**
Trigger criteria that cannot be observed are effectively inert. The V2 scoping mechanism is designed as a feedback-driven escalation that surfaces when the V1 portfolio is insufficient. But if Trigger 2 (MCP-heavy team routing friction) cannot be measured, and if no team reporting channel exists for Triggers 1, 3, and 4, the V2 scoping decision defaults to ad hoc assessment. The carefully designed trigger criteria become a useful heuristic for thinking about V2 timing, not an operational escalation mechanism.

This matters for the pre-mortem scenario because: without V2 scoping triggers that can fire, the HIGH RISK user research gap and the ethics gaps (P1 priority) remain unaddressed until someone decides to address them -- which may never happen without a trigger.

**Recommendation:**
Qualify the V2 scoping trigger table with a "Collection Method" column that specifies how each trigger is observed in practice:

| Trigger | Feasibility | Collection Method |
|---------|------------|------------------|
| 1 (untested prototypes) | Observable | Count zero-user fallback activations in `/ux-design-sprint` output artifacts |
| 2 (MCP-heavy routing) | Not directly observable without instrumentation | Proxy: quarterly manual sample of active teams to identify MCP-heavy contexts |
| 3 (AI UX guidance need) | Observable via team communication | Define a reporting convention (e.g., tag in worktracker) |
| 4 (ethics complaints) | Observable via team communication | Same reporting convention as Trigger 3 |

This does not require building new infrastructure -- it requires making the observability limitations explicit and providing observable proxies.

**Acceptance Criteria:** The V2 scoping trigger table includes a "Current Observability" column noting each trigger's measurability under Jerry's current architecture, and a "Collection Method" column providing the most practical monitoring approach per trigger.

---

### PM-008-I4: Crisis Triage Time Targets Inconsistent With Section 3.1 Qualified Time Estimates [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.1 (option j), Section 7.2 (crisis row), Section 3.1 (time estimate qualification) |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption category) |
| **Failure Category** | Assumption |
| **Likelihood** | Medium |
| **Priority** | P2 |
| **Affected Dimension** | Internal Consistency (0.20) |

**Evidence:**
Section 7.1 crisis triage (PM-005 -- R8) states:
- "Step 1: /ux-heuristic-eval (immediate: identify the most severe usability violations **in under 35 minutes**)"

Section 3.1 (DA-015 -- R7) qualification states:
- "Total realistic time: 20-35 minutes for a complete evaluation, not 'under 10 minutes.'" -- This is for a complete 10-heuristic evaluation including team input time.
- "The 10-minute estimate is accurate only for the 4 Deterministic heuristics evaluated without team input -- it is NOT the time for a complete 10-heuristic evaluation."

Section 7.1 says "under 35 minutes" for crisis mode. Section 3.1 says "20-35 minutes" under normal operation for a complete evaluation. The crisis triage time target of "under 35 minutes" references Section 3.1's upper bound as if it is an accurate target, but Section 3.1 explicitly says this is a *total realistic time including team input time* -- meaning the crisis scenario estimate is at the upper bound of normal operation time, not a reliable crisis-mode target.

Additionally, Section 7.1's "same day: diagnose the specific B=MAP bottleneck" for Step 2 does not reference Section 3.10's "45-90 minutes per target behavior" estimate, creating an unanchored time expectation.

**Analysis:**
The inconsistency is minor but affects user expectations in the highest-stakes context (crisis mode). A team in crisis following the Section 7.1 protocol who finds that a heuristic evaluation takes 45 minutes instead of "under 35 minutes" has received misleading guidance at the worst possible time. The qualified estimates in Section 3.1 (DA-015) are more accurate; the crisis triage times should be consistent with them.

**Recommendation:**
Update the crisis triage option (j) time estimates to reference the Section 3.x qualified estimates: "Step 1: /ux-heuristic-eval (immediate: 20-35 minutes for complete evaluation per DA-015 -- begin with the 4 Deterministic heuristics for fastest initial triage, ~10 minutes)." Add a note for Step 2: "45-90 minutes per target behavior per Section 3.10."

**Acceptance Criteria:** Crisis triage time estimates in Section 7.1 are consistent with the qualified time estimates in Sections 3.1 and 3.10, and reference those sections for traceability.

---

### PM-009-I4: Free-Tier Configuration Claims `/ux-heuristic-eval` Works Without Figma -- Contradicts Required MCP Classification [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.4 (free-tier note, PM-004-20260303b -- R7) vs. Section 7.3 (Required vs. Enhancement MCP table) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical category) |
| **Failure Category** | Technical |
| **Likelihood** | High |
| **Priority** | P2 |
| **Affected Dimension** | Internal Consistency (0.20) |

**Evidence:**
Section 7.4 free-tier note (PM-004-20260303b -- R7) states:
> "Teams unable to meet the $46/month Figma+Miro baseline should prioritize Wave 1 and Wave 4 sub-skills (zero Required MCP cost): `/ux-heuristic-eval` (**screenshot-input mode, no Figma required**)..."

Section 7.3 Required vs. Enhancement classification table states:
> | `/ux-heuristic-eval` | **Figma (for design evaluation)** | Storybook (for component-level evaluation) |

Figma is explicitly classified as a **Required MCP** for `/ux-heuristic-eval` in Section 7.3. Section 7.4 explicitly classifies `/ux-heuristic-eval` as a zero Required MCP cost sub-skill for free-tier teams. These are directly contradictory.

The "screenshot-input mode" referenced in Section 7.4 is mentioned in passing in the Wave bypass/stall recovery protocol ("If `/ux-heuristic-eval` stalls (no Figma access), proceed if JTBD has a DONE story. Use screenshot-input mode for heuristic eval.") but screenshot-input mode is never defined in Section 3.1. No specification of what screenshot-input mode means operationally, how it differs from Figma-based evaluation, or what its limitations are appears anywhere in the document.

**Analysis:**
Free-tier teams following Section 7.4 will attempt to use `/ux-heuristic-eval` without Figma, expecting it to work in "screenshot-input mode." But Section 7.3 classifies Figma as Required, meaning the sub-skill's core function depends on it. Without a specification of screenshot-input mode in Section 3.1, the free-tier guidance creates a false expectation.

This is a direct internal consistency violation introduced by the Wave bypass protocol (R7 addition) without updating the Section 7.3 classification. The classification table should either be updated to reflect the screenshot-input degraded mode, or the Section 3.1 sub-skill definition should specify what screenshot-input mode provides.

**Recommendation:**
Resolve the contradiction in one of two ways: (a) downgrade Figma's Section 7.3 classification from "Required for core function" to "Required for full function; screenshot-input mode available as degraded fallback" and add a Section 3.1 specification of screenshot-input mode limitations; or (b) remove `/ux-heuristic-eval` from the Section 7.4 free-tier list and note it requires Figma.

**Acceptance Criteria:** Sections 7.3 and 7.4 are internally consistent: if `/ux-heuristic-eval` is listed as free-tier accessible, Section 7.3 must acknowledge screenshot-input mode; if Figma is Required for `/ux-heuristic-eval`, Section 7.4 must not list it as zero-cost.

---

### PM-010-I4: AI-First Design Framework Review Cadence Clock Has No Defined Start Point [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 3.8 (AI-First Design, framework review cadence, IN-009 -- R6) |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption category) |
| **Failure Category** | Assumption |
| **Likelihood** | Low |
| **Priority** | P2 |
| **Affected Dimension** | Actionability (0.15) |

**Evidence:**
Section 3.8 states: "The AI-First Design synthesis is optimized for Q1 2026 practitioner guidance... The explicit shelf life is: **accurate as synthesized in Q1 2026; re-validate before Q4 2026 implementation; full revision review at Q2 2027.**"

The synthesis has not been produced yet (the Enabler is uninitialized). The "synthesized in Q1 2026" reference point is already in the past from the current date (2026-03-03) -- the synthesis has not occurred in Q1 2026. If the synthesis is produced in Q2 2026 or later (which is plausible if the Enabler is not created until PROJ-020 kickoff and takes the full 30 days), the entire shelf-life timeline collapses: the synthesis would be "synthesized in Q2 2026" and the "re-validate before Q4 2026" target would be only 1-2 months after synthesis, making the review cadence unreasonably tight.

Additionally, the "accurate as synthesized in Q1 2026" claim for a synthesis that has not occurred is a prospective accuracy claim that cannot be evaluated until the synthesis exists.

**Analysis:**
The review cadence specification is anchored to a fixed calendar (Q1 2026 synthesis, Q4 2026 re-validate, Q2 2027 full revision) that assumes the synthesis occurs on schedule. If the synthesis is delayed -- which is the primary risk flagged throughout Section 3.8 -- the review cadence becomes misaligned. A synthesis produced in Q3 2026 would already need re-validation before it could be reviewed at Q4 2026.

This is a minor issue because the review cadence is a planning guidance item, not a blocking requirement. But it creates a false sense of precision: the cadence appears specific but is contingent on a delivery date that has not been achieved.

**Recommendation:**
Replace the fixed-calendar cadence with a relative cadence: "The synthesized framework should be re-validated 6 months after synthesis completion, and undergo full revision review at 12 months after synthesis completion. Given the pace of AI UX development, a synthesis completed after Q2 2026 should have an accelerated first re-validation at 3 months." This makes the cadence independent of a fixed synthesis date.

**Acceptance Criteria:** Section 3.8 review cadence uses relative timing (months after synthesis completion) rather than absolute calendar quarters, and includes guidance for the case where synthesis is completed after Q2 2026.

---

## Recommendations

### P0 -- Critical: MUST Mitigate Before Acceptance

**PM-001-I4: Add Implementation Specification to Section 7.5**

The synthesis hypothesis validation protocol must include concrete implementation artifacts: prompt templates for each confidence tier, canonical output label strings, and the invocation intercept pattern. A sub-skill author reading Section 7.5 must be able to implement the gate unambiguously without consulting any other document.

Acceptance criteria: Section 7.5 "Implementation Specification for Sub-Skill Authors" sub-section exists with prompt templates, label strings, and intercept pattern.

---

**PM-002-I4: Replace "Automatic" Expiry Language With Explicit Human Action Protocol**

The AI-First Design Enabler expiry trigger must specify a human actor, a check-in procedure, and a Day-30 milestone worktracker task. The word "automatically" must be replaced wherever it implies infrastructure-level execution in a file-based worktracker system.

Acceptance criteria: Section 3.8 removes "automatically" from the expiry trigger; a Day-30 milestone task is added to the required worktracker entity list alongside the quarterly ownership verification task.

---

### P1 -- Important: SHOULD Mitigate

**PM-003-I4: Add Consistent Implementation-Status Labels to Section 7**

Apply CC-004-style status labels to all routing mechanism content in Section 7 to distinguish design specification from operational capability.

Acceptance criteria: Section 7.1 includes a forward-looking framing disclaimer; Section 7.4 wave entries for Waves 1-4 include DESIGN SPECIFICATION status labels.

---

**PM-004-I4: Add Consolidated Pre-Launch Worktracker Entities Checklist**

Consolidate all required worktracker entities from Sections 3.8 and 7.3 into a single pre-launch checklist in Section 7.

Acceptance criteria: A "Required Pre-Launch Worktracker Entities" checklist covers all entities mandated in Sections 3.8 and 7.3 in a single location.

---

**PM-005-I4: Extend SM-001 Minimality Defense to High-Redundancy-Risk Pairs**

The three-property minimality test (SM-001) covers Design Sprint/Lean UX. Apply the same method to the 6 highest-redundancy-risk pairs among compression-zone frameworks.

Acceptance criteria: MINIMALITY CLAIM QUALIFICATION references a completeness table covering minimum 6 pairwise comparisons using the SM-001 three-property test.

---

**PM-006-I4: Unify Section 7.5 Confidence Labels With Section 3.x Taxonomy Tables**

Add a "Synthesis Confidence Level" column to each Section 3.x AI Execution Mode Taxonomy table, or add cross-reference notes linking to Section 7.5.

Acceptance criteria: Each Section 3.x AI Execution Mode Taxonomy table references Section 7.5 confidence levels unambiguously for synthesis hypothesis steps.

---

**PM-007-I4: Add Observability Qualification to V2 Trigger Table**

Add "Current Observability" and "Collection Method" columns to the V2 scoping trigger table.

Acceptance criteria: V2 trigger table includes per-trigger observability assessment and practical monitoring approach under Jerry's current architecture.

---

### P2 -- Monitor

**PM-008-I4:** Update crisis triage time estimates to reference Section 3.x qualified estimates. Acceptance criteria: Section 7.1 option (j) time estimates are consistent with DA-015 and Section 3.10 qualified values.

**PM-009-I4:** Resolve Figma Required MCP / free-tier screenshot-input mode contradiction between Sections 7.3 and 7.4. Acceptance criteria: Sections 7.3 and 7.4 are internally consistent on `/ux-heuristic-eval` MCP requirements.

**PM-010-I4:** Replace fixed-calendar AI-First Design review cadence with relative timing. Acceptance criteria: Section 3.8 cadence uses months-after-synthesis-completion framing.

---

## Scoring Impact

Pre-Mortem findings map to S-014 scoring dimensions as follows:

| Dimension | Weight | Pre-Mortem Impact | Rationale |
|-----------|--------|------------------|-----------|
| **Completeness** | 0.20 | Negative (PM-004-I4, PM-007-I4) | Required worktracker entities not created (PM-004-I4) and V2 trigger monitoring gaps (PM-007-I4) represent incompleteness in the mitigation system: the analysis describes controls but does not instantiate or make observable all of them. PM-001-I4 also represents a completeness gap -- the validation protocol exists as policy without implementation specification. |
| **Internal Consistency** | 0.20 | Negative (PM-006-I4, PM-008-I4, PM-009-I4) | Three internal consistency violations: dual labeling system conflict (PM-006-I4), crisis triage time inconsistency (PM-008-I4), and Figma Required MCP / free-tier contradiction (PM-009-I4). These are quantified, traceable, and resolvable. |
| **Methodological Rigor** | 0.20 | Neutral-Negative (PM-005-I4) | The minimality methodology (SM-001 three-property test) is sound and well-specified for the Design Sprint/Lean UX pair. The gap is that the method has not been applied to all high-redundancy-risk pairs -- a completeness gap in an otherwise rigorous method. The overall methodological rigor is high; this is a targeted extension need, not a fundamental rigor failure. |
| **Evidence Quality** | 0.15 | Neutral | No evidence quality gaps identified. Evidence citations are thorough (E-001 through E-029), sourcing is qualified, and the adversarial review process is documented. |
| **Actionability** | 0.15 | Negative (PM-001-I4, PM-002-I4, PM-003-I4, PM-004-I4, PM-007-I4, PM-010-I4) | The highest concentration of findings is in actionability: the analysis is analytically complete but operationally incomplete. The synthesis hypothesis validation protocol (PM-001-I4), the Enabler expiry mechanism (PM-002-I4), the routing implementation status (PM-003-I4), the worktracker entity creation (PM-004-I4), V2 observability (PM-007-I4), and the review cadence anchoring (PM-010-I4) all represent cases where the analysis provides correct guidance but insufficient operational specification for implementers to act without additional inference. |
| **Traceability** | 0.10 | Neutral | Traceability is strong throughout the document. Finding IDs with revision suffixes, evidence table with 29 entries, and cross-references between findings and revision log entries are well-maintained. PM-004-I4 is the only finding that affects traceability (scattered worktracker requirements across sections), but this is a synthesis gap, not a documentation gap. |

**Overall Assessment:** REVISE with targeted mitigation.

The deliverable is analytically excellent. The scoring matrix, sensitivity analysis, FMEA risk management, and complementarity structure are methodologically rigorous and well-evidenced. The pre-mortem analysis identified **no fundamental flaws** in the framework selection logic, the WSM scoring model, or the portfolio design.

The pre-mortem findings concentrate in two areas: (1) the gap between policy specification and implementation specification (PM-001-I4, PM-002-I4, PM-003-I4 -- the deliverable correctly identifies what should happen but provides insufficient specification for implementers to make it happen), and (2) internal consistency violations introduced by iterative R6-R8 additions that updated some sections without propagating changes to others (PM-006-I4, PM-008-I4, PM-009-I4).

The 2 Critical findings (PM-001-I4, PM-002-I4) are targeted and resolvable without restructuring the analysis. The 5 Major findings are also targeted. No finding requires selection changes or methodology revision. The pre-mortem projection is that addressing all P0 and P1 findings would improve the Actionability and Internal Consistency dimensions, which are the primary gaps holding the score below 0.95.

---

## Execution Statistics

- **Total Findings:** 10
- **Critical:** 2 (PM-001-I4, PM-002-I4)
- **Major:** 5 (PM-003-I4, PM-004-I4, PM-005-I4, PM-006-I4, PM-007-I4)
- **Minor:** 3 (PM-008-I4, PM-009-I4, PM-010-I4)
- **Protocol Steps Completed:** 6 of 6
- **H-16 Compliance:** Confirmed (S-003 Steelman applied in prior tournament iterations; SM-001/SM-002/SM-003 incorporated into R8)
- **Finding Categories Used:** Technical (PM-006-I4, PM-009-I4), Process (PM-001-I4, PM-002-I4, PM-003-I4, PM-007-I4), Assumption (PM-005-I4, PM-008-I4, PM-010-I4), Resource (PM-004-I4)
- **All 5 Category Lenses Applied:** Technical, Process, Assumption, External (no findings), Resource
