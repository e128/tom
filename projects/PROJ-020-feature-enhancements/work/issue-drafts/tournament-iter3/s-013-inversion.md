# Strategy Execution Report: Inversion Technique (S-013)

## Execution Context

- **Strategy:** S-013 (Inversion Technique)
- **Template:** `.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Deliverable Type:** GitHub Enhancement Issue -- `/user-experience` skill proposal (~1146 lines, R2-revised)
- **Criticality:** C4
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 3 (post-R2; R2 applied fixes from Iter 2 tournament findings)
- **Prior Scores:** Iter 1: 0.704, Iter 2: 0.724
- **H-16 Compliance:** S-003 Steelman applied in prior tournament chain (confirmed)

---

## Inversion Report: `/user-experience` Skill -- GitHub Enhancement Issue (R2-Revised)

**Strategy:** S-013 Inversion Technique
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-013), Iteration 3
**H-16 Compliance:** S-003 Steelman applied in prior tournament iteration (confirmed)
**Goals Analyzed:** 11 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 8

---

## Summary

R2 applied targeted fixes to the Iter 2 S-013 findings. Three of the five Major findings are partially addressed: IN-003 (wave bypass) received the strongest fix via WAVE-N-SIGNOFF.md enforcement and 3-field bypass documentation, materially reducing the bypass-as-default risk; IN-004 (LOW-confidence bypass via follow-up) is partially addressed because behavior design was promoted from LOW to MEDIUM confidence, removing the clearest bypass pathway; IN-001 (benchmark self-validation) received a new Pre-Launch Validation AC requiring external ground-truth artifacts. However, two Major findings from Iter 2 remain unaddressed in R2 (IN-002: Human Override Justification rationalization ritual; IN-005: recall metric invalid for synthesis frameworks), and the Pre-Launch Validation AC for IN-001 creates its own assumption vulnerability. Fresh inversion of the R2 deliverable surfaces three new or deepened vulnerabilities not raised in prior iterations: (1) the Pre-Launch Validation AC requires external ground-truth but does not specify who defines "external" or how the comparison is conducted, leaving the validation method undefined; (2) the WAVE-N-SIGNOFF.md check prevents routing to the next wave but does not prevent teams from directly invoking sub-skills by name, creating a direct-invocation bypass that circumvents the entire gating architecture; (3) the independent reviewer requirement for the AI-First Design Enabler WSM (RT-005) raises the gate quality but the same deliverable does not define how an "independent reviewer" is qualified or sourced for a synthesized framework in an emerging domain. Overall recommendation: **REVISE** -- two persistent Major findings from Iter 2 (IN-002, IN-005), one new Major finding (IN-008: direct-invocation bypasses WAVE-N-SIGNOFF.md gating), and two Minor findings require mitigation before the deliverable can approach the quality threshold.

---

## Step 1: Goals Inventory

The goals inventory is carried forward from Iter 2 with one addition to reflect the R2-added issue closure condition:

| # | Goal | Type | Stated / Inferred |
|---|------|------|-------------------|
| G-01 | Enable tiny teams (1-5 people) to execute professional UX methodology without a UX specialist | Primary | Stated |
| G-02 | Cover the full UX lifecycle via 10 sub-skills implementing proven frameworks | Scope | Stated |
| G-03 | Comply with Jerry framework architectural constraints (P-003, H-34, progressive disclosure, wave deployment) | Compliance | Stated |
| G-04 | Deploy in 5 criteria-gated waves to reduce adoption risk and manage progressive complexity | Risk Management | Stated |
| G-05 | Prevent over-reliance on AI synthesis outputs via 3-tier confidence gates | Safety | Stated |
| G-06 | Achieve S-014 scoring >= 0.92 at wave transitions for C2+ UX deliverables | Quality | Stated |
| G-07 | Each sub-skill independently maintainable and evolvable without breaking sibling skills | Maintainability | Implicit |
| G-08 | MCP integration remains stable enough to provide documented functionality | Infrastructure | Implicit |
| G-09 | Non-specialist developers successfully execute UX frameworks using AI guidance alone | Adoptability | Implicit (core value proposition) |
| G-10 | Per-sub-skill quality benchmarks validate that AI framework application quality meets minimum recall thresholds before production launch | Quality Validation | Stated (R1-added) |
| G-11 | The issue specification provides sufficient detail for implementation without major clarifying questions | Implementability | Implicit |

**R2 goal change note:** G-04 (criteria-gated wave deployment) is now supported by WAVE-N-SIGNOFF.md enforcement (R2-fix: IN-003, PM-004). The goal itself is unchanged but the mechanism has materially strengthened. New vulnerability in R2 emerges from the gap between the SIGNOFF check and the direct-invocation path (see IN-008 below).

---

## Step 2: Anti-Goals (Goal Inversions)

**G-04 Anti-Goal (revised for R2):** To guarantee wave criteria are bypassed despite WAVE-N-SIGNOFF.md enforcement:
- Teams invoke sub-skills directly by slash command (e.g., `/ux-design-sprint`) rather than routing through `/user-experience`, bypassing the orchestrator's SIGNOFF check entirely
- The WAVE-N-SIGNOFF.md check is referenced in the Acceptance Criteria but not stated as a constraint in the sub-skill definitions themselves, meaning the gating logic exists only at the orchestrator level and is not enforced when sub-skills are invoked directly
- Direct invocation still triggers the wave prerequisite check mentioned in the routing design ("Direct invocation still checks wave prerequisites: if the sub-skill belongs to a wave whose entry criteria have not been met, the agent displays a warning...") -- but "displays a warning" and "asks the user to confirm" (P-020) means the check is advisory, not gating

**G-05 Anti-Goal (R2 update -- behavior design reclassified):** To guarantee systematic over-reliance on AI synthesis outputs despite confidence gate architecture:
- The `Human Override Justification` field (R1-added, unaddressed in R2) continues to accept rationalizations as evidence
- Promoting `/ux-behavior-design` from LOW to MEDIUM confidence (R2-fix: FM-011) means its outputs now require "expert review OR validation against 2-3 real user data points" -- but "OR" allows either condition, and the MEDIUM gate does not specify how "expert review" is qualified. Any colleague with UX interest can serve as the "expert"
- The remaining LOW-confidence outputs (Kano feature priority conflict interpretation, HEART metric threshold, AI-First Design) retain the structural omission gate, which the follow-up prompt bypass (IN-004, unresolved at architecture level) continues to circumvent

**G-09 Anti-Goal (R2 context):** To guarantee non-specialists cannot successfully execute UX frameworks:
- The Pre-Launch Validation AC (R2-fix: DA-001) requires benchmark comparison against "external ground-truth artifact (not self-created by the implementing team)" but does not define the comparison method. A non-specialist implementation team procures a published Nielsen Norman Group evaluation and attempts to compare the AI's output to the published evaluation -- but "comparison" is itself an expert judgment that requires UX evaluation experience to conduct meaningfully
- Quality benchmarks validated against external artifacts by non-specialists may confirm surface similarity (same heuristics cited, similar severity categories) while missing substantive quality differences

**G-10 Anti-Goal (R2 update):** To guarantee quality benchmarks do not validate AI framework execution despite Pre-Launch Validation AC:
- Pre-Launch Validation AC requires the sub-skill's quality benchmark to be "validated against an external ground-truth artifact (not self-created by the implementing team). Benchmark achievement is demonstrated via test output comparison" -- but "test output comparison" is undefined. The implementing team generates AI output, compares it to the external artifact, and judges whether it meets the benchmark threshold. This is still a self-assessment of comparison, just with external input
- The two named example sources (Nielsen Norman Group published evaluations, Intercom JTBD Playbook examples) are named for Wave 1 only. Wave 2-5 sub-skills retain the gap: no named external sources are specified for Lean UX, HEART, Atomic Design, Inclusive Design, Behavior Design, Kano, Design Sprint benchmarks

---

## Step 3: Assumption Map

| ID | Assumption | Type | Category | Confidence | Validation Status |
|----|------------|------|----------|------------|-------------------|
| A-01 | Pre-Launch Validation AC (R2-fix: DA-001) adequately closes the benchmark self-validation loop | Quality | Process | Medium | AC adds external ground-truth requirement for Wave 1 but leaves Wave 2-5 without named sources; comparison method undefined |
| A-02 | The `Human Override Justification` field creates genuine validation behavior, not rationalization rituals | Behavioral | Process | Low | Not addressed in R2; rationalization risk remains; no structured evidence template required |
| A-03 | WAVE-N-SIGNOFF.md existence check prevents teams from accessing un-gated wave sub-skills | Gating | Technical | Medium | Enforced at orchestrator routing level only; direct sub-skill invocation path acknowledged ("still checks wave prerequisites") but check is advisory (warning + P-020 user confirm) |
| A-04 | The MEDIUM-confidence gate for `/ux-behavior-design` (R2-fix: FM-011) prevents over-reliance on Reference Intervention Patterns | Safety | Process | Low | "Expert review OR validation against 2-3 real user data points" -- MEDIUM gate's "expert review" condition does not define expert qualification; any self-described expert satisfies it |
| A-05 | Recall metric is an adequate quality benchmark for synthesis-framework sub-skills | Quality | Technical | Low | Not addressed in R2; recall metric remains invalid for JTBD, Lean UX, HEART, Behavior Design, Kano (5-6 of 10 sub-skills) |
| A-06 | Independent reviewer sign-off requirement for AI-First Design Enabler WSM (R2-fix: RT-005) ensures objective evaluation | Quality | Process | Low | "Independent reviewer" not defined; no qualification criteria, sourcing guidance, or conflict-of-interest standard specified; in a tiny team context the "independent reviewer" may be a friend or colleague equally unfamiliar with the emerging AI UX domain |
| A-07 | 90-day AI-First Design Enabler timeline is sufficient for novel framework synthesis | Resource | Temporal | Low | Not substantively addressed in R2 (gate raised from 7.80 to 8.00, independent reviewer added, but timeline unchanged); 90 days remains optimistic for a novel methodology synthesis |
| A-08 | Onboarding user research warning maintains behavioral effectiveness across multi-sub-skill sessions | Behavioral | UX | Low | Not addressed in R2; single-session first-invocation warning decay persists |
| A-09 | The "test output comparison" in the Pre-Launch Validation AC is a meaningful evaluation method when performed by a non-specialist implementation team | Quality | Process | Low | No guidance on comparison method; a non-specialist comparing AI output to a published NNG evaluation may confirm surface formatting similarity while missing substantive quality gaps |
| A-10 | 8-category routing triage handles all real UX request types | Technical | Technical | Medium | Persists from Iter 1 and Iter 2; cross-lifecycle requests remain unhandled |
| A-11 | Hotjar bridge via Zapier warrants "Enhancement MCP" classification given its operational barrier | Infrastructure | Process | Low | Persists from Iter 2; bridge requires paid Zapier + custom workflow setup; classification as "Enhancement" understates barrier |
| A-12 | "WAVE BYPASS ACTIVE" warning banner is visible and cognitively salient to users who encounter it on sub-skill outputs | Behavioral | UX | Low | Newly introduced by R2-fix: IN-003; warning banner existence is specified but format, placement, and dismissibility are undefined; warning banners in AI output contexts are frequently ignored |
| A-13 | Wave bypass state "persists as a warning banner on all sub-skill outputs produced under bypass" is technically achievable with current Jerry architecture | Technical | Technical | Low | Persistent state tracking across sub-skill invocations requires orchestrator state management capability not currently specified in Jerry's architecture for sub-skill outputs; the mechanism is aspirational without a stated implementation path |
| A-14 | The 3-field bypass documentation requirement prevents rationalized bypasses | Behavioral | Process | Medium | Better than Iter 2 (no structure); but field population can still be completed with low-effort content ("Wave 2 stalled because we lack analytics. We'll set up analytics by Q2.") |

---

## Step 4: Stress-Test Results

| ID | Assumption | Inversion | Plausibility | Severity | Affected Dimension |
|----|------------|-----------|--------------|----------|--------------------|
| IN-001-20260303c | A-01: Pre-Launch Validation AC closes benchmark self-validation loop | Wave 1 gets external ground-truth (NNG study) but Wave 2-5 benchmarks remain self-created; comparison method is undefined and self-assessed by the implementation team | HIGH -- Wave 1 partial fix leaves 8 of 10 sub-skills with the original problem; comparison method gap persists for all waves | Major | Methodological Rigor |
| IN-002-20260303c | A-02: Human Override Justification creates genuine validation | Teams populate the field with "our user population matches mainstream SaaS users" and proceed; no structured evidence template, no validation source required, no review step | HIGH -- rationalization is the path of least resistance; R2 did not address this finding | Major | Evidence Quality |
| IN-003-20260303c | A-03: WAVE-N-SIGNOFF.md check prevents unauthorized wave access | User invokes `/ux-design-sprint` directly by slash command; sub-skill's direct-invocation wave check "displays a warning with the unmet criteria and asks the user to confirm" (P-020 user decides); user confirms and proceeds; the gating architecture is advisory at the sub-skill level | HIGH -- P-020 compliance makes the sub-skill-level check necessarily advisory; teams under delivery pressure confirm bypass; the SIGNOFF.md check governs orchestrator routing but not direct invocation | Major | Methodological Rigor |
| IN-004-20260303c | A-04: MEDIUM gate for behavior design prevents over-reliance on Reference Intervention Patterns | "Expert review OR validation against 2-3 real user data points" -- user provides self as expert ("I have 2 years of product experience") or asks a colleague; MEDIUM gate satisfied; Reference Intervention Patterns advance to design decisions without genuine external validation | HIGH -- "expert review" is undefined; in tiny team context, expert qualification cannot be verified; OR-condition means neither arm of the gate is rigorously checked | Major | Evidence Quality |
| IN-005-20260303c | A-05: Recall metric is adequate for synthesis-framework sub-skills | 6 of 10 sub-skills (JTBD, Lean UX, HEART, Behavior Design, Kano, AI-First Design) are synthesis frameworks where recall against a static ground-truth is not a valid quality metric; quality validation for majority of portfolio is structurally broken | HIGH -- not addressed in R2; structural problem persists | Major | Completeness |
| IN-006-20260303c | A-06: Independent reviewer for AI-First Design WSM is objective | "Independent reviewer" could be the implementing team's colleague, manager, or a community contributor equally unfamiliar with the nascent AI UX domain; gate passes but provides no assurance of rigor | MEDIUM -- the Enabler is conditional and far on the implementation timeline; independent reviewer lack-of-definition is a Medium-plausibility failure given the AI UX domain's current state | Minor | Methodological Rigor |
| IN-007-20260303c | A-08: Onboarding warning persists across multi-sub-skill sessions | User invokes JTBD at session start (warning fires), then Design Sprint 3 hours later in same session; sprint challenge is committed without warning re-trigger; highest-stakes synthesis-to-decision handoff occurs without the cognitive context of the risk warning | HIGH -- single-fire warning decay is unchanged from Iter 2; not addressed in R2 | Minor | Evidence Quality |
| IN-008-20260303c | A-12/A-13: WAVE BYPASS ACTIVE warning banner is visible, persistent, and architecturally achievable | Warning banner specified in text but format undefined; users presented with AI-generated content that contains a warning header learn to scroll past it; Jerry architecture does not currently implement persistent cross-invocation state for sub-skill output headers | MEDIUM -- warning banner format and persistence mechanism are implementation details that could be specified; but the assumption that a warning banner changes behavior is the same assumption the deliverable critiques in automation bias contexts | Minor | Internal Consistency |

---

## Step 5: Detailed Findings

### IN-001-20260303c: Pre-Launch Validation Partial Fix -- Wave 2-5 Ground-Truth Gap and Undefined Comparison Method [MAJOR]

**Type:** Assumption
**Original Assumption (from Iter 2 IN-001):** Per-sub-skill quality benchmark ground-truth artifacts will exist and be verifiable before production launch.
**R2 Fix Applied:** Pre-Launch Validation AC (R2-fix: DA-001): "Before Wave 1 sub-skill merge, each sub-skill's quality benchmark is validated against an external ground-truth artifact (not self-created by the implementing team). Benchmark achievement is demonstrated via test output comparison, not merely defined."
**Inversion:** The R2 fix addresses Wave 1 explicitly (names NNG published evaluations and Intercom JTBD Playbook as examples). Wave 2-5 sub-skills are covered by the wave-level ACs that use the same benchmark patterns without naming external ground-truth sources. The Pre-Launch Validation AC applies to "each sub-skill" but is placed in a section under "Wave 1 Sub-Skills (Minimum Viable Launch)" -- the scope is ambiguous. More critically: "demonstrated via test output comparison" is undefined. Who conducts the comparison? By what criteria? What constitutes a passing comparison?
**Plausibility:** HIGH. Wave 2-5 sub-skills will be implemented after Wave 1. By the time of Wave 2-5 implementation, the Pre-Launch Validation AC pattern (external ground-truth) may not be consistently applied unless explicitly required in the wave-level ACs. The "test output comparison" gap applies to all waves: comparing AI-generated JTBD job statements to Intercom case study examples is an expert judgment task that non-specialist implementing teams cannot reliably perform.
**Consequence:** Wave 1 gets a partial fix (external source named, but comparison method undefined). Wave 2-5 retain the original vulnerability. The benchmark self-validation loop is partially closed for evaluation frameworks (Heuristic Eval, Inclusive Design) where recall comparison is tractable, but remains fully open for synthesis frameworks (JTBD, Lean UX, HEART, Behavior Design, Kano) where quality comparison requires expert judgment.
**Evidence:** Pre-Launch Validation AC: "Before Wave 1 sub-skill merge, each sub-skill's quality benchmark is validated against an external ground-truth artifact (not self-created by the implementing team)." Wave 2-5 ACs cite benchmarks (e.g., "benchmark: generates assumption map with >= 3 risk categories from a product brief" for Lean UX) without naming external ground-truth sources or specifying the comparison method.
**Dimension:** Methodological Rigor
**Mitigation:** (1) Extend Pre-Launch Validation AC explicitly to Wave 2-5: each wave-level AC should include a Pre-Launch Validation requirement with a named ground-truth source appropriate to the framework type. For synthesis frameworks, the named source must be an expert-authored case study output (not a count threshold). (2) Define "test output comparison" as a structured evaluation: specify who conducts the comparison (e.g., "A UX practitioner who did not author the sub-skill"), what dimensions are compared, and what score constitutes a passing result.
**Acceptance Criteria:** (1) Wave 2-5 ACs each include a Pre-Launch Validation requirement with a named external ground-truth source. (2) The comparison method for each framework type is defined (evaluation: recall/precision; synthesis: expert-structured rubric). (3) Comparison is conducted by someone who did not author the sub-skill under test.

---

### IN-002-20260303c: Human Override Justification Remains an Unstructured Rationalization Field [MAJOR] (Persistent from Iter 2)

**Type:** Assumption
**Original Assumption:** The `Human Override Justification` field creates genuine validation behavior when users choose to act on LOW-confidence synthesis outputs.
**R2 Fix Applied:** None. R2 did not address IN-002-20260303b.
**Inversion:** A tiny team facing schedule pressure and a LOW-confidence JTBD job statement output will write "our user population matches mainstream SaaS users" or "we conducted informal user observation" in the justification field and proceed. The field has no structure requiring named data sources, specific data points, or validation dates. It accepts any free-text input. The audit trail shows the field was populated but provides no evidence of genuine validation.
**Plausibility:** HIGH. Rationalization is the behavior of least resistance when a required field has no validation constraints. The deliverable's Automation Bias section (lines 641-642) explicitly acknowledges: "no template-level mechanism fully prevents a determined user from treating LOW-confidence outputs as actionable." The Override Justification field is supposed to be that mechanism, but without structure, it fails this role. The deliverable correctly diagnoses the problem in its own text and then provides an inadequate solution.
**Consequence:** Users systematically bypass LOW-confidence gates via the justification field on consequential design decisions. The architecture appears to address over-reliance on AI synthesis outputs (audit trail exists) while the behavior (teams making decisions on unvalidated AI outputs) continues unchanged. This is the most dangerous pattern in the deliverable: a safety mechanism that creates the appearance of governance while the underlying risk persists.
**Evidence:** Line 641: "Each synthesis output therefore includes a `Human Override Justification` field -- if a user chooses to act on a LOW-confidence output, they must document their rationale and the evidence supporting their decision. This creates an auditable paper trail rather than a hard block." The phrase "the evidence supporting their decision" presupposes the user has evidence; teams without UX expertise will have rationalizations, not evidence.
**Dimension:** Evidence Quality
**Mitigation:** Replace the free-text `Human Override Justification` field with a structured evidence template containing three required named fields: (a) **Named data source** (e.g., "3 user interviews conducted 2026-01-15 with [population]" -- not "informal observation"); (b) **Specific supporting data point** (e.g., "Interview participant 2 confirmed friction at Step 3 of the onboarding flow" -- not "our users are typical"); (c) **Validation date** (ISO 8601). Generic content in any of the three fields triggers a warning before the output proceeds. The structured template logic is documented in `synthesis-validation.md`.
**Acceptance Criteria:** (1) `Human Override Justification` field is replaced by a 3-field structured evidence template. (2) Sub-skill output logic validates that at minimum Fields (a) and (b) contain non-generic content (defined negatively: does not contain "typical", "similar", "probably", "informal", or other non-specific qualifiers). (3) Validation logic documented in `synthesis-validation.md`. (4) Generic-content warning behavior defined in `synthesis-validation.md`.

---

### IN-003-20260303c: WAVE-N-SIGNOFF.md Gating Bypassed by Direct Sub-Skill Invocation [MAJOR] (New in Iter 3)

**Type:** Anti-Goal
**Context:** R2-fix IN-003 and PM-004 added WAVE-N-SIGNOFF.md existence check at the orchestrator routing level. This is a meaningful fix for the "bypass through parent orchestrator" path. The inversion identifies the "bypass through direct sub-skill invocation" path that the SIGNOFF.md check does not cover.
**Inversion:** User invokes `/ux-design-sprint` directly without going through `/user-experience`. The sub-skill's direct-invocation logic "displays a warning with the unmet criteria and asks the user to confirm they want to proceed despite incomplete prerequisites (P-020: user decides)." P-020 (user authority) means the check cannot be a hard gate -- it must respect user decision-making authority. A user who directly invokes `/ux-design-sprint` and confirms "yes, proceed" bypasses the WAVE-N-SIGNOFF.md check entirely because the SIGNOFF.md check lives in the orchestrator routing logic, not in the sub-skill definition.
**Plausibility:** HIGH. Direct sub-skill invocation is explicitly documented as a supported path: "Users who know the specific sub-skill they need can invoke it directly (e.g., `/ux-heuristic-eval`) to bypass the triage." The design correctly serves users who know what they need, but it means the gating architecture has a documented bypass path that is not governed by the SIGNOFF.md check. Under schedule pressure, "just invoke `/ux-design-sprint` directly" becomes the obvious path.
**Consequence:** The WAVE-N-SIGNOFF.md enforcement mechanism governs the orchestrator routing path only. Teams who learn (or discover by accident) that direct invocation shows a warning rather than a hard block will use direct invocation when they want to skip a wave. The wave gating architecture's effectiveness is contingent on teams always routing through `/user-experience`, which the deliverable itself describes as optional.
**Evidence:** Line 419: "Users who know the specific sub-skill they need can invoke it directly (e.g., `/ux-heuristic-eval`) to bypass the triage. Direct invocation still checks wave prerequisites: if the sub-skill belongs to a wave whose entry criteria have not been met, the agent displays a warning with the unmet criteria and asks the user to confirm they want to proceed despite incomplete prerequisites (P-020: user decides)."

The R2-added Wave Progression AC: "Wave entry enforcement: orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills." This governs orchestrator routing only; it does not modify the sub-skill-level direct-invocation behavior.
**Dimension:** Methodological Rigor
**Mitigation:** Align direct invocation behavior with the WAVE-N-SIGNOFF.md check: when a user invokes a Wave N sub-skill directly, the sub-skill checks for `WAVE-{N-1}-SIGNOFF.md` existence (not just wave entry criteria assessment) before proceeding. If SIGNOFF.md does not exist, the sub-skill behavior matches the orchestrator behavior: deny routing with a "WAVE-{N-1}-SIGNOFF.md not found -- complete Wave N-1 entry criteria before proceeding" message. P-020 is respected by documenting the bypass path (3-field bypass documentation) rather than by permitting advisory-only warning.
**Acceptance Criteria:** (1) Sub-skill agent definitions (in methodology or rules) include a SIGNOFF.md existence check equivalent to the orchestrator check. (2) Missing SIGNOFF.md produces a denial (not an advisory warning) with a bypass path requiring 3-field documentation consistent with the orchestrator bypass mechanism. (3) `ux-routing-rules.md` documents both the orchestrator-routing check and the direct-invocation check as co-equal enforcement mechanisms.

---

### IN-004-20260303c: MEDIUM Confidence Gate for Behavior Design "Expert Review OR" Condition Is Exploitable [MAJOR] (R2 partial-fix deepening)

**Type:** Assumption
**Original Finding:** IN-004-20260303b (follow-up prompt bypass of LOW-confidence structural omission).
**R2 Fix Applied:** R2-fix: FM-011 reclassified `/ux-behavior-design` outputs from LOW to MEDIUM confidence. This removes the most frequently invoked LOW-confidence pathway for a synthesis framework. The architectural LOW-confidence structural omission bypass (asking for recommendations in follow-up) still applies to remaining LOW-confidence outputs (Kano priority conflict, HEART threshold, AI-First Design pattern recommendations).
**New Inversion (R2 deepening):** The MEDIUM confidence gate requires "expert review OR validation against 2-3 real user data points." The OR condition means either arm satisfies the gate. "Expert review" is undefined: no qualification criteria, no conflict-of-interest standard, no required reviewer independence. A tiny team member with "some UX reading" can self-designate as the expert. A team with a part-time designer can have the designer "review" their own behavioral diagnosis. The OR condition creates a gate that can be satisfied with minimal friction by any team member claiming relevant expertise.
**Plausibility:** HIGH. In tiny team contexts, "expert review" is an informal concept. The MEDIUM gate is more demanding than the LOW gate (which only required the Human Override Justification rationalization field) but less demanding than genuine external validation. The OR condition allows any team to satisfy the gate without engaging an actual UX practitioner.
**Consequence:** Reclassifying behavior design from LOW to MEDIUM moves Reference Intervention Patterns from "reference-only" to "requires validation before design decisions." But if the MEDIUM gate's "expert review" arm is satisfied by any colleague, the practical barrier is only slightly higher than the LOW gate's rationalization field. The reclassification adds ceremony without adding rigor.
**Evidence:** Line 655-656: "MEDIUM: Requires expert review OR validation against 2-3 real user data points. The output includes a 'Validation Required' section. The agent does not generate design recommendations until a named validation source is provided." Line 310: Reference Intervention Patterns "require expert review OR validation against 2-3 real user data points before use in design decisions."

The MEDIUM gate specifies "a named validation source" but does not define what qualifies as a valid expert. "Named validation source" for expert review could be satisfied by naming any colleague.
**Dimension:** Evidence Quality
**Mitigation:** Define "expert review" for the MEDIUM confidence gate: minimum qualification criteria (e.g., "2+ years of UX practice, does not work on the product being reviewed") and specify that self-review and review by direct team members are excluded. Alternatively, replace the OR condition with AND: both expert review AND at minimum 1 real user data point are required for MEDIUM-confidence synthesis outputs to advance to design decisions. The AND condition is more appropriate for a framework like B=MAP where behavioral diagnosis is highly context-dependent.
**Acceptance Criteria:** (1) MEDIUM confidence gate definition in `synthesis-validation.md` specifies minimum expert qualifications and excludes self-review and direct team member review. (2) OR condition is either retained with defined expert qualifications OR replaced with AND condition for synthesis frameworks where AI diagnosis is context-dependent. (3) "Named validation source" field for expert review includes reviewer name, qualification, and a declaration of non-involvement with the product under review.

---

### IN-005-20260303c: Recall Metric Remains Invalid for Synthesis-Framework Sub-Skills [MAJOR] (Persistent from Iter 2)

**Type:** Assumption
**Original Assumption:** Recall against a ground-truth artifact is a valid quality metric applicable across all 10 sub-skills.
**R2 Fix Applied:** None. R2 did not address IN-005-20260303b.
**Inversion:** 5-6 of 10 sub-skills are synthesis frameworks (JTBD, Lean UX, HEART, Behavior Design, Kano) where there is no fixed "correct answer" to recall against. The Wave 2-5 quality benchmark ACs use count thresholds (e.g., "generates assumption map with >= 3 risk categories") or recall thresholds for scenarios where ground-truth is defined by expert judgment (e.g., "correctly identifies the bottleneck component for >= 3 of 4 reference behavioral scenarios" -- but the "correct" bottleneck identification is itself context-dependent). Quality validation for the majority of the portfolio is structurally broken.
**Plausibility:** HIGH. The distinction between evaluation frameworks (fixed set of findings) and synthesis frameworks (context-dependent expert judgment) is structural. This was raised in Iter 2 and not addressed. The Pre-Launch Validation AC (R2-fix: DA-001) partially helps by requiring external ground-truth for Wave 1, but does not address the metric type mismatch for synthesis frameworks. A Wave 1 JTBD benchmark can compare AI job statements to Intercom examples, but "do the AI's job statements look like the Intercom examples" is not the same as "are the AI's job statements valid for the team's specific user population."
**Consequence:** Quality validation for synthesis-framework sub-skills either (a) uses count thresholds that test output quantity but not quality, or (b) uses recall against an external artifact that tests surface similarity but not appropriateness for the specific product context. Neither validates that the AI's synthesis is expert-quality. The skill can launch with passing benchmarks on evaluation frameworks while the synthesis frameworks (which constitute the majority of use cases for tiny teams) remain unvalidated.
**Evidence:** Wave 2 AC: "benchmark: generates assumption map with >= 3 risk categories from a product brief." A count threshold. Wave 4 AC: "benchmark: correctly identifies the bottleneck component for >= 3 of 4 reference behavioral scenarios." A recall threshold -- but the "correct" B=MAP bottleneck for a reference scenario is itself expert-defined, and the reference scenarios are not specified.
**Dimension:** Completeness
**Mitigation:** Differentiate benchmark types by framework category, explicitly in the Acceptance Criteria section: (a) **Evaluation frameworks** (Heuristic Eval, Inclusive Design): Recall/precision against a named external expert-authored artifact. Specify the artifact. (b) **Synthesis frameworks** (JTBD, Lean UX, HEART, Behavior Design, Kano): Expert-review rubric with named reviewer qualification criteria. The rubric should evaluate: dimensional completeness (does the output address the framework's required components?), framework fidelity (does the output follow the framework's prescribed method?), and actionability (can the output drive a product decision without further expert intervention?). Each dimension scored 1-5; passing threshold defined. (c) **Conditional frameworks** (AI-First Design): Deferred to Enabler acceptance criteria.
**Acceptance Criteria:** (1) Acceptance Criteria section includes a Quality Benchmark Type Classification table that classifies each sub-skill as Evaluation-type or Synthesis-type. (2) Synthesis-type benchmarks specify a named expert reviewer qualification and a structured quality rubric (not a count or recall threshold). (3) Evaluation-type benchmarks name the specific external ground-truth artifact.

---

### IN-006-20260303c: Independent Reviewer for AI-First Design WSM Not Defined [MINOR]

**Type:** Assumption
**Original Assumption (from Iter 2 IN-006):** 90 days and raised WSM gate (>= 8.00, R2-fix: RT-005) are sufficient and verifiable for novel AI-First Design framework synthesis.
**R2 Fix Applied:** R2-fix: RT-005 raised the gate from >= 7.80 to >= 8.00 and added "Independent reviewer sign-off required on WSM scoring for Enabler validation -- the person scoring the Enabler cannot be the person who built it."
**Inversion:** "Independent reviewer" is undefined: no qualification criteria, no domain expertise requirement, no sourcing guidance. For a synthesized framework in an emerging domain (AI UX, where established practitioners are rare), the implementing team's definition of "independent" may be any team member not directly involved in authoring the framework. A colleague reviewing a novel AI UX framework against the same 6 WSM criteria (which were calibrated for the original 40-framework selection) may not have the domain expertise to assess whether the synthesized framework meets the criteria's intent for AI interaction patterns.
**Plausibility:** MEDIUM. The independent reviewer requirement is a meaningful improvement over self-assessment. The failure mode requires the reviewer to be unqualified AND willing to sign off on a framework they do not deeply understand -- plausible but not the dominant outcome. The risk is highest in the early implementation period when AI UX expertise is scarce and team networks are small.
**Consequence:** The WSM gate passes with a higher numerical threshold (>= 8.00 vs. 7.80) but the evaluation quality is unchanged if the reviewer lacks domain expertise. The Enabler either passes an insufficiently rigorous review and enters Wave 5 with an under-validated framework, or the independent reviewer requirement cannot be satisfied within the 90-day timeline and the substitution path activates.
**Evidence:** Line 381: "Independent reviewer sign-off required on WSM scoring for Enabler validation -- the person scoring the Enabler cannot be the person who built it." No qualification criteria defined beyond "not the person who built it."
**Dimension:** Methodological Rigor
**Mitigation:** Define independent reviewer minimum qualifications for the AI-First Design Enabler WSM: (1) Minimum 2 years UX practice experience (to evaluate general UX framework criteria), AND (2) Demonstrated familiarity with AI interaction patterns (publication, project, or course reference acceptable). Alternatively, specify that in the absence of a qualified independent reviewer within the team's network, the Enabler WSM review is conducted using the same adversarial tournament process as the original 40-framework selection (i.e., S-014 scoring by /adversary).
**Acceptance Criteria:** (1) AI-First Design Enabler acceptance criteria specify independent reviewer minimum qualifications (2 years UX practice + AI UX familiarity). (2) Alternative review path via /adversary S-014 scoring is documented if a qualified reviewer is unavailable. (3) Reviewer qualifications are documented in the Enabler's DONE criteria.

---

### IN-007-20260303c: Onboarding Warning Decay Persists -- Single-Session Cognitive Decay Unaddressed [MINOR] (Persistent from Iter 2)

**Type:** Assumption
**Original Assumption:** The onboarding warning about the user research gap maintains behavioral effectiveness across multi-sub-skill sessions.
**R2 Fix Applied:** None. R2 did not address IN-007-20260303b.
**Inversion:** The user research gap warning fires once at first `/user-experience` invocation per session. A session that spans JTBD at session start, Lean UX hypothesis generation mid-session, and Design Sprint challenge commitment at session end sees the warning only at JTBD invocation time. By sprint challenge commitment -- the highest-stakes decision point in the portfolio -- the cognitive context of the warning has fully decayed. The sprint challenge statement (which commits the team to a 4-day sprint direction) is often built directly from AI-generated JTBD job statements, making this the highest-stakes synthesis-to-decision handoff in the system.
**Plausibility:** HIGH. Warning fatigue and cognitive decay in sequential decision workflows are well-documented. The architecture applies the behavioral reasoning it uses elsewhere (automation bias, confidence gate design) inconsistently: it correctly specifies that confidence gates must be structurally embedded in outputs, but leaves the onboarding warning as a single-trigger session-start event. The same logic that justifies embedded confidence gates justifies embedded risk warnings at synthesis-to-decision handoffs.
**Consequence:** The user research gap risk is least communicated at the most consequential moments. Teams who encounter the warning at session start and then make a 4-day sprint commitment based on AI-generated job statements 3 hours later have not been reminded that the input to their commitment is a hypothesis.
**Evidence:** Routing flowchart: "Start -> Onboard -> Display HIGH RISK user research warning" (single trigger). The Lean UX sub-skill description notes "synthesis hypothesis warning: Job statements generated from secondary research are MEDIUM confidence. They require named validation sources before feeding into Design Sprint challenge statements." This is the correct intervention point -- but it is only described in the sub-skill documentation, not specified as a behavioral requirement that the sub-skill actively enforces when JTBD outputs are passed to Design Sprint.
**Dimension:** Evidence Quality
**Mitigation:** Specify re-trigger conditions for the user research warning in `ux-routing-rules.md`: (1) When the parent orchestrator routes a synthesis output (JTBD job statement, Lean UX assumption map) as input to a Design Sprint challenge statement, the orchestrator re-triggers the warning before proceeding. (2) Define at minimum 3 "handoff risk" synthesis-to-decision scenarios where the warning re-triggers: (a) JTBD output -> Design Sprint challenge statement, (b) Lean UX assumption map -> hypothesis selection commitment, (c) HEART metric selection -> dashboard build commitment.
**Acceptance Criteria:** (1) `ux-routing-rules.md` defines 3+ handoff risk scenarios where user research warning re-triggers. (2) Parent orchestrator identifies JTBD -> Design Sprint as a mandatory re-trigger point. (3) The warning text at re-trigger points is decision-proximate (identifies the specific synthesis output being used and the specific decision being committed, not a generic gap notice).

---

## Step 6: Recommendations

### Major Findings (MUST Mitigate)

| ID | Finding | Action | Acceptance Criteria |
|----|---------|--------|---------------------|
| IN-001-20260303c | Pre-Launch Validation partial -- Wave 2-5 ground-truth gap and undefined comparison method | Extend Pre-Launch Validation AC to Wave 2-5; define comparison method and comparison conductor | Wave 2-5 ACs name external ground-truth; comparison method defined; conducted by non-author |
| IN-002-20260303c | Human Override Justification unstructured rationalization field (persistent from Iter 2) | Replace with 3-field structured evidence template; define generic-content warning logic | 3-field template; generic-content warning; documented in `synthesis-validation.md` |
| IN-003-20260303c | WAVE-N-SIGNOFF.md gating bypassed by direct sub-skill invocation (new) | Sub-skill definitions include SIGNOFF.md existence check equivalent to orchestrator; missing SIGNOFF.md produces denial with bypass path | Sub-skill SIGNOFF check documented in methodology; denial behavior defined; bypass path documented |
| IN-004-20260303c | MEDIUM confidence gate "expert review OR" condition exploitable (R2 deepening) | Define expert qualification criteria for MEDIUM gate; consider replacing OR with AND for context-dependent synthesis | `synthesis-validation.md` defines expert qualifications; OR/AND condition updated with qualifications |
| IN-005-20260303c | Recall metric invalid for synthesis-framework sub-skills (persistent from Iter 2) | Classify benchmarks as Evaluation-type or Synthesis-type; Synthesis-type uses expert-review rubric | Benchmark Type Classification table in ACs; Synthesis-type ACs specify reviewer qualification + rubric |

### Minor Findings (SHOULD Mitigate)

| ID | Finding | Action | Acceptance Criteria |
|----|---------|--------|---------------------|
| IN-006-20260303c | Independent reviewer for AI-First Design WSM not defined | Define minimum reviewer qualifications; add /adversary alternative review path | Enabler AC specifies reviewer qualifications; alternative path documented |
| IN-007-20260303c | Onboarding warning decay persists (persistent from Iter 2) | Define 3+ re-trigger handoff risk scenarios in `ux-routing-rules.md` | `ux-routing-rules.md` defines JTBD->Sprint and 2+ other re-trigger points |

---

## Step 7: Scoring Impact

| Dimension | Weight | Impact | Finding References | Rationale |
|-----------|--------|--------|-------------------|-----------|
| Completeness | 0.20 | Negative | IN-005-20260303c | Synthesis-framework benchmark metric remains structurally broken for 5-6 of 10 sub-skills; quality validation is incomplete for the majority of the portfolio. R2 did not address this finding. |
| Internal Consistency | 0.20 | Mixed | IN-003-20260303c, IN-004-20260303c | R2's WAVE-N-SIGNOFF.md enforcement is internally inconsistent with the direct-invocation path that explicitly allows wave bypass with only a warning and P-020 user confirm. The MEDIUM gate expert-review criterion is internally inconsistent with the MEDIUM gate's stated intent of preventing over-reliance on unvalidated synthesis. Positive: R2's reclassification of behavior design to MEDIUM is internally consistent with the synthesis hypothesis validation framework. |
| Methodological Rigor | 0.20 | Negative | IN-001-20260303c, IN-003-20260303c, IN-005-20260303c | Pre-Launch Validation AC partially closes Wave 1 benchmark gap but leaves Wave 2-5 open and comparison method undefined. Direct-invocation bypass defeats the primary wave-gating mechanism. Synthesis benchmark metric remains invalid for most sub-skills. |
| Evidence Quality | 0.15 | Negative | IN-002-20260303c, IN-004-20260303c, IN-007-20260303c | Human Override Justification remains a free-text rationalization field. MEDIUM gate "expert review" arm is exploitable by informal peer review. Onboarding warning decays before highest-stakes synthesis-to-decision handoffs. |
| Actionability | 0.15 | Mixed | IN-001-20260303c, IN-006-20260303c | Pre-Launch Validation AC is an actionable addition for Wave 1 evaluation frameworks. AI-First Design independent reviewer requirement is more actionable than self-assessment but remains under-specified. Synthesis-framework quality metric gap (IN-005) leaves implementation teams without actionable benchmarks for 5-6 sub-skills. |
| Traceability | 0.10 | Positive | (no new traceability findings) | R2 fix annotations (R2-fix: identifiers) are traceable to specific Iter 2 findings. WSM table replacement (R2-fix: CV-001, CV-002) cites source artifact. WAVE-N-SIGNOFF.md enforcement traces to IN-003 and PM-004. |

**Net assessment:** R2 made material improvements to wave gating (WAVE-N-SIGNOFF.md) and behavior design confidence classification (MEDIUM reclassification), but these fixes surface adjacent vulnerabilities (direct-invocation bypass, MEDIUM gate "expert review" exploit) and left two of the five Iter 2 Major findings (IN-002, IN-005) unaddressed. The score trajectory (Iter 1: 0.704, Iter 2: 0.724) reflects real but incremental improvement. Five Major findings require mitigation for substantive score advancement. With targeted mitigation of the five Major findings, the deliverable should approach the 0.85+ range in Iter 4. **REVISE** before Iter 4 tournament cycle.

---

## Execution Statistics

- **Total Findings:** 7
- **Critical:** 0
- **Major:** 5 (2 persistent from Iter 2, 1 new in Iter 3, 2 R2-deepened)
- **Minor:** 2 (1 persistent from Iter 2, 1 new in Iter 3)
- **Protocol Steps Completed:** 6 of 6

---

## R2 Fix Adequacy Assessment

| Iter 2 Finding | R2 Fix Applied | Adequacy |
|----------------|---------------|----------|
| IN-001-20260303b (benchmark self-validation) | Pre-Launch Validation AC (DA-001): external ground-truth for Wave 1 | PARTIAL -- Wave 1 named; Wave 2-5 gap persists; comparison method undefined. Downgraded from Major persistence to new Major with adjacent vulnerability (IN-001-20260303c). |
| IN-002-20260303b (Human Override Justification) | None | NOT ADDRESSED -- persistent as IN-002-20260303c (Major) |
| IN-003-20260303b (wave bypass defeats gating) | WAVE-N-SIGNOFF.md enforcement + 3-field bypass docs (IN-003, PM-004) | PARTIAL -- orchestrator-routing path meaningfully strengthened; direct-invocation bypass not addressed (new IN-003-20260303c Major). Net: genuine improvement at orchestrator level, but adjacent vulnerability discovered. |
| IN-004-20260303b (LOW-confidence follow-up bypass) | Behavior design reclassified to MEDIUM (FM-011) | PARTIAL -- removes the primary LOW-confidence synthesis bypass path for behavior design; remaining LOW-confidence outputs unchanged; MEDIUM gate "expert review" condition introduces new exploitability (IN-004-20260303c Major). Net: genuine improvement with new vulnerability. |
| IN-005-20260303b (recall metric invalid) | None | NOT ADDRESSED -- persistent as IN-005-20260303c (Major) |
| IN-006-20260303b (90-day Enabler timeline) | Gate raised to >= 8.00, independent reviewer required (RT-005) | PARTIAL -- higher gate and independent reviewer are improvements; reviewer not defined; timeline unchanged. Downgraded to Minor (IN-006-20260303c). Net: genuine improvement. |
| IN-007-20260303b (onboarding warning decay) | None | NOT ADDRESSED -- persistent as IN-007-20260303c (Minor) |

---

## H-15 Self-Review

Pre-persistence verification:

1. **All findings have specific evidence from the deliverable.** Citations to line numbers and section text provided for every finding. IN-003-20260303c cites line 419 (direct invocation description) and the R2 Wave Progression AC. IN-004-20260303c cites lines 655-656 and line 310. PASS.
2. **Severity classifications justified.** Five Majors: IN-001 (incomplete Pre-Launch Validation fix leaves Wave 2-5 without external ground-truth and comparison method undefined); IN-002 (unaddressed rationalization ritual is a persistent significant gap); IN-003 (direct-invocation bypass circumvents primary wave-gating architecture -- not a corner case, it is an explicitly documented user path); IN-004 (MEDIUM gate "expert review OR" exploitable in tiny team context where "expert" is undefined -- the gate's stated purpose is not achieved); IN-005 (recall metric invalid for 5-6 of 10 sub-skills -- quality validation broken for majority of portfolio). Two Minors: IN-006 (independent reviewer undefined -- improvement over self-assessment but residual gap); IN-007 (onboarding warning decay -- documented UX safety concern but does not invalidate the overall architecture). PASS.
3. **Finding identifiers follow IN-NNN-20260303c format** (c suffix differentiates Iter 3 from Iter 1 and Iter 2 same-date identifiers). PASS.
4. **Summary table matches detailed findings** (7 findings: 0 Critical, 5 Major, 2 Minor). PASS.
5. **No findings omitted or minimized.** IN-003 (direct invocation bypass) evaluated for potential Minor status -- rejected because the direct invocation path is explicitly documented as a supported user path ("Users who know the specific sub-skill they need can invoke it directly to bypass the triage") making this a high-plausibility bypass, not an edge case. Major classification justified. PASS.
