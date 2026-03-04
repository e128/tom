# Strategy Execution Report: FMEA (Failure Mode and Effects Analysis)

## Execution Context
- **Strategy:** S-012 (FMEA -- Failure Mode and Effects Analysis)
- **Template:** `.context/templates/adversarial/s-012-fmea.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 10)
- **Executed:** 2026-03-03T00:00:00Z
- **Criticality:** C4 | **Tournament Iteration:** 6 of 8
- **H-16 Compliance:** S-003 Steelman applied in prior iterations (confirmed via revision history)
- **Elements Analyzed:** 10 | **Failure Modes Identified:** 22 | **Total RPN:** 1,918

---

## Summary

R10 addressed all 5 Critical findings from Iteration 5 and introduced owner assignment rules, launch readiness gates, wave backward-pass protocol, uncertainty derivation, team segment variants, and LOW gate qualification. This FMEA analyzes all 10 elements of the deliverable systematically and finds 0 Critical findings (RPN >= 200), 8 Major findings (RPN 80-199), and 14 Minor findings (RPN < 80) for a total of 22 failure modes. The highest RPN in this iteration is 160 (FM-004-I6: wave backward-pass protocol circular dependency). The document has reached a maturity level where most remaining failure modes are residual-ambiguity and incomplete-operational-handoff issues rather than structural defects. ACCEPT with targeted corrections addressing the 8 Major findings.

---

## Findings Summary

| ID | Element | Failure Mode | S | O | D | RPN | Severity | Affected Dimension |
|----|---------|-------------|---|---|---|-----|----------|--------------------|
| FM-001-I6 | E7: Owner Assignment Rule | Owner role "project lead" undefined when no project lead exists at kickoff | 7 | 5 | 4 | 140 | Major | Actionability |
| FM-002-I6 | E8: LOW Gate Qualification | Implementation qualification is in a parenthetical mid-cell; easily missed | 6 | 6 | 4 | 144 | Major | Completeness |
| FM-003-I6 | E9: Tiny Teams Segments | Part-time UX segment's "C1 scores may overstate fit" claim is unquantified | 5 | 5 | 5 | 125 | Major | Evidence Quality |
| FM-004-I6 | E6: Wave Backward-Pass | Backward-pass protocol requires evaluator sign-off but evaluator role is wave-gated | 8 | 4 | 5 | 160 | Major | Internal Consistency |
| FM-005-I6 | E1: Uncertainty Derivation | ±0.25 band is called "heuristic bound" but the derivation anchor (adversarial correction magnitude) is only from 3 data points | 5 | 4 | 6 | 120 | Major | Methodological Rigor |
| FM-006-I6 | E7: Launch Readiness Gate | Gate uses "WORKTRACKER.md manifest" but format/location of owner field within WORKTRACKER.md is unspecified | 6 | 5 | 4 | 120 | Major | Actionability |
| FM-007-I6 | E6: Wave Transition Evaluator | Evaluator approval recorded as "completed Task" but Task entity schema for this approval is not specified | 5 | 5 | 5 | 125 | Major | Actionability |
| FM-008-I6 | E3: AI Reliability Tiers | H2/H4/H6/H7/H8/H10 "requires team input" tier lacks specific time estimate for context-gathering step | 5 | 4 | 6 | 120 | Major | Actionability |
| FM-009-I6 | E2: Scoring Matrix | Non-selected framework scores (ranks 13-40) remain single-rated with no adversarial review disclosure for that tier | 4 | 5 | 4 | 80 | Minor | Evidence Quality |
| FM-010-I6 | E5: Sub-Skill Routing | Section 7.1 routing table does not surface the user research gap warning at invocation time | 5 | 4 | 4 | 80 | Minor | Completeness |
| FM-011-I6 | E10: AI-First Design | SCORING METHODOLOGY DISCLAIMER (DA-002-I5) does not specify which sub-skills receive the "projected" caveat when reading the routing table | 4 | 4 | 5 | 80 | Minor | Completeness |
| FM-012-I6 | E4: V2 Roadmap | V2 scoping trigger criteria (SM-009) require "any two" triggers but do not specify which organizational role evaluates and acts on them | 4 | 5 | 4 | 80 | Minor | Actionability |
| FM-013-I6 | E9: Tiny Teams Segments | Segment table omits guidance for which of the 5 waves is appropriate for a solo practitioner running Design Sprint solo | 4 | 4 | 5 | 80 | Minor | Completeness |
| FM-014-I6 | E8: Gate Prompt Templates | MEDIUM gate prompt template says "option (a) or (b)" but the gate implementation spec says "user selects 'neither'" as the only other path -- no explicit "user selects option (a)" path is defined for recording | 4 | 4 | 5 | 80 | Minor | Internal Consistency |
| FM-015-I6 | E6: Wave Bypass Protocol | Wave bypass conditions define "2 sprint cycles" as the stall threshold but do not define sprint cycle length (1 week? 2 weeks?) | 3 | 5 | 5 | 75 | Minor | Actionability |
| FM-016-I6 | E1: Sensitivity Analysis | C2 perturbation table caption says "25%/15%/15%/15%/20%/10%" but C5 went from 15%→20%; the weights are listed in C1-C6 order so the reader must mentally re-order | 3 | 4 | 6 | 72 | Minor | Internal Consistency |
| FM-017-I6 | E3: Sub-Skill Profiles | HEART Section 3.4: degraded-mode behavior specifies "no analytics data source and no Hotjar bridge" but excludes the case where only a Hotjar bridge (no analytics) exists | 3 | 4 | 5 | 60 | Minor | Completeness |
| FM-018-I6 | E3: Sub-Skill Profiles | JTBD Section 3.6: data sufficiency check gate fires before synthesis, but the Switch interview guide referenced ("a Switch interview guide is included as a skill artifact") does not exist in this document | 5 | 3 | 4 | 60 | Minor | Completeness |
| FM-019-I6 | E8: Self-Attestation Limitation | DA-006 notes the MEDIUM gate requires "naming a specific validation source, creating an auditable claim" but there is no defined storage location or format for that audit trail | 3 | 5 | 4 | 60 | Minor | Traceability |
| FM-020-I6 | E7: Recurring Task Definition | Entity #3 (Ownership Verification, quarterly) and Entity #4 (MCP Ownership Verification, quarterly) both say "quarterly" but do not specify what happens if an owner is no longer available at the quarterly check | 3 | 4 | 5 | 60 | Minor | Completeness |
| FM-021-I6 | E6: Wave 5 Entry Criteria | Wave 5 /ux-ai-first entry criterion requires "Independent scoring artifact at specified path" but the "specified path" is not specified in Section 7.4 | 4 | 3 | 5 | 60 | Minor | Traceability |
| FM-022-I6 | E4: Ethics Gap | Ethics gap V2 prioritization table (from FM-003-20260303 R6) distinguishes P1/P2/P3 but has no defined owner for initiating V2 scoping | 3 | 4 | 4 | 48 | Minor | Actionability |

---

## Detailed Findings

### FM-001-I6: Owner Role Undefined When No Project Lead Exists

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=7, O=5, D=4, RPN=140) |
| **Section** | Section 7.5, Owner Assignment Rule (PM-001-I5 -- R10) |
| **Strategy Step** | Step 2 (Missing failure mode lens) |

**Evidence:**
> "The PROJ-020 project lead is responsible for populating owner fields for entities 1-4 at the kickoff meeting. Primary owner: the engineer assigned to the corresponding sub-skill Enabler in WORKTRACKER.md. Secondary owner: the `/user-experience` skill lead. If no skill lead is assigned at kickoff, the project lead assumes secondary ownership until delegation."

The rule handles the "no skill lead" case but has no fallback for the "no project lead" case. In Jerry projects, a project lead may not be formally designated at kickoff -- particularly for solo-initiated projects or when a project is started by a contributor without a lead role being formally assigned.

**Analysis:**
The launch readiness gate (Wave 1 BLOCKED) depends on owners being populated in WORKTRACKER.md. If there is no project lead to assign owners, the gate can never be satisfied as specified. This creates a circular dependency: the document says the project lead assigns owners, but does not define who assigns the project lead. The Missing lens identifies a gap: the rule chain bottoms out without a defined fallback authority.

**Recommendation:**
Add a fallback clause: "If no project lead is designated at kickoff, the initiating contributor assumes project lead responsibilities for entity ownership assignment purposes until a formal project lead is designated. In solo projects, the sole practitioner serves as project lead." Add this sentence to the Owner Assignment Rule paragraph in Section 7.5.

**Acceptance Criteria:** Owner Assignment Rule has a no-project-lead fallback clause. Wave 1 can be initiated by a solo practitioner without a formally designated project lead.

**Post-Correction RPN Estimate:** S=7, O=2, D=3 → RPN=42

---

### FM-002-I6: LOW Gate Qualification Buried in Mid-Cell Parenthetical

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=6, O=6, D=4, RPN=144) |
| **Section** | Section 7.6, Synthesis Hypothesis Validation Protocol, LOW confidence row |
| **Strategy Step** | Step 2 (Ambiguous/Insufficient failure mode lens) |

**Evidence:**
The LOW confidence gate row's "Enforcement Mechanism" cell contains the full gate language followed by a large parenthetical PM-007-I5 qualification block beginning with: "**Implementation qualification [PM-007-I5 -- R10]:** The 'cannot be overridden' language describes design intent for the LLM sub-skill agent's behavioral constraints, not a technical enforcement guarantee."

This qualification fundamentally changes the meaning of the "cannot be overridden" enforcement claim. It is embedded inside a table cell after the primary gate description, making it easy to miss when scanning the table.

**Analysis:**
A reader who processes only the table summary will see: "No user acknowledgment action can override this gate." A reader who reads the full cell will see that this is design intent, not a technical guarantee. The placement creates a two-tier information hazard: implementation teams reading quickly may implement the LOW gate as if it is a hard enforcement mechanism, while the qualification discloses it is not. This is an Ambiguous failure mode -- the same cell supports two incompatible interpretations depending on how thoroughly it is read.

**Recommendation:**
Elevate the PM-007-I5 qualification out of the table cell into a standalone paragraph immediately below the table, with a callout box or bold notice: "**IMPLEMENTATION CAVEAT (PM-007-I5):** The LOW confidence gate enforcement language above describes behavioral design intent for LLM agents, not a technical guarantee. See implementation qualification below." This ensures the caveat is visible at the table level, not buried in a cell.

**Acceptance Criteria:** PM-007-I5 qualification is visible at table scan level, not inside a table cell. Implementation teams cannot miss the caveat by reading only the table.

**Post-Correction RPN Estimate:** S=6, O=3, D=2 → RPN=36

---

### FM-003-I6: Part-Time UX Segment Fit Assessment Is Unquantified

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=5, O=5, D=5, RPN=125) |
| **Section** | Preamble, TINY TEAMS POPULATION SEGMENTS table (DA-003-I5 -- R10) |
| **Strategy Step** | Step 2 (Insufficient failure mode lens) |

**Evidence:**
> "| Team with part-time UX | 2-5, one part-time | UX is a part-time responsibility for one team member; depth is limited; frameworks must be low-ceremony | MEDIUM -- Kano (survey setup overhead) and HEART (metric infrastructure) may exceed part-time capacity; prioritize Wave 1-2 sub-skills | C1 scores may overstate fit for part-time segments; implementation should default to Wave 1 only until capacity assessment |"

The claim "C1 scores may overstate fit" is stated without quantification. By how much? Which frameworks are most overstated? The phrase "until capacity assessment" references a capacity assessment process that is not defined anywhere in the document.

**Analysis:**
The Insufficient lens applies: the segment entry is present (better than absence) but inadequate in specificity. A team in the part-time UX segment cannot act on "C1 scores may overstate fit" without knowing which specific framework scores are suspect and by how much. The undefined "capacity assessment" is a dangling reference -- it promises a process that does not exist in the document.

**Recommendation:**
(1) Add a specific sentence identifying which frameworks have the highest overstatement risk for part-time UX teams: "Specifically, Kano Model (C1=8) and HEART Framework (C1=9) may score 1-2 points lower for part-time teams due to survey distribution overhead and analytics infrastructure requirements respectively." (2) Either define what a capacity assessment entails in 2-3 bullets, or replace "until capacity assessment" with "until the team has confirmed at least 2 hours per week of dedicated UX practice time."

**Acceptance Criteria:** Part-time UX segment entry identifies specific frameworks with overstatement risk by name. "Capacity assessment" is either defined or replaced with a measurable threshold.

**Post-Correction RPN Estimate:** S=5, O=3, D=3 → RPN=45

---

### FM-004-I6: Wave Backward-Pass Protocol Has Circular Evaluator Dependency

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=8, O=4, D=5, RPN=160) |
| **Section** | Section 7.4, Wave backward-pass revision protocol (DA-004-I5 -- R10) |
| **Strategy Step** | Step 2 (Inconsistent failure mode lens) |

**Evidence:**
> "The wave transition evaluator reviews the contradiction resolution before the team resumes the later wave."

And from the Wave Transition Evaluator paragraph (PM-006-I5):
> "The PROJ-020 project lead (or delegated `/user-experience` skill lead) is responsible for evaluating wave transition readiness criteria and formally approving wave transitions."

The backward-pass protocol requires the wave transition evaluator to review contradiction resolution. However, the evaluator role is defined as evaluating forward wave transitions -- not backward-pass contradiction resolution. There is no specification for: (a) how quickly the evaluator must review backward-pass resolutions, (b) what happens if the evaluator disagrees with the team's contradiction resolution, or (c) whether the backward-pass review uses the same readiness criteria as the forward transition.

**Analysis:**
This is an Inconsistent failure mode: the backward-pass protocol assumes the evaluator role extends to backward-pass review, but the evaluator role is defined only for forward transitions. A team executing a backward-pass (e.g., Wave 5 Design Sprint output invalidates Wave 1 JTBD job statement) needs to know exactly what the evaluator reviews and approves in the backward-pass context. Without this specification, the backward-pass protocol's "evaluator reviews the contradiction resolution" clause is ambiguous: does the evaluator re-run the Wave 1 readiness criteria? Do they just confirm the contradiction is documented? The highest-RPN finding in this iteration because severity is high (S=8: a backward-pass executed incorrectly can invalidate multiple downstream wave outputs) and detection requires careful reading of two separate paragraphs to notice the gap (D=5).

**Recommendation:**
Add a backward-pass evaluator specification sub-section: "**Backward-pass evaluator review criteria:** The evaluator confirms: (1) the contradiction is documented in the worktracker as an impediment linking the two sub-skill stories; (2) the earlier-wave sub-skill step has been re-executed with the new information documented as the revised artifact; (3) the revision has been propagated forward through intermediate waves. The evaluator does NOT re-run the full wave transition readiness criteria -- they confirm the propagation chain is complete. Maximum review time: 5 business days from contradiction documentation. If the evaluator disagrees with the resolution, they document the disagreement as a worktracker blocker and the team re-executes the disputed step."

**Acceptance Criteria:** Backward-pass evaluator criteria are defined separately from forward-transition criteria. A team knows exactly what the evaluator reviews in a backward-pass scenario.

**Post-Correction RPN Estimate:** S=8, O=2, D=2 → RPN=32

---

### FM-005-I6: ±0.25 Uncertainty Derivation Has Thin Empirical Basis

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=5, O=4, D=6, RPN=120) |
| **Section** | Section 1, Methodology Limitations (DA-005-I5 -- R10) |
| **Strategy Step** | Step 2 (Insufficient failure mode lens) |

**Evidence:**
> "The three scoring errors detected by S-001 Red Team review (HEART C3: 6→4, Fogg C3: 4→3, AI-First Design C4: 3→2) each involved a 1-2 point per-criterion adjustment. For a 6-criterion WSM where weights range from 0.10-0.25, a 1-point error on a single criterion produces a weighted-total shift of 0.10-0.25 points. The ±0.25 band represents the maximum single-criterion error impact."

The derivation uses 3 data points (the 3 detected errors) to establish an uncertainty band that is then applied to all 40 frameworks. The document acknowledges this is "a heuristic bound, not a statistical confidence interval" but does not acknowledge that 3 detected errors from a set with an unknown total error count is a weak empirical foundation. The band could be understated (if undetected errors exceed 1 point) or overstated (if the adversarial review caught all errors).

**Analysis:**
Insufficient lens: the derivation is transparent about its limitations but does not quantify the risk of the band being systematically understated. Specifically: the 3 detected errors were all in the same direction (scores were corrected downward). If rater bias is systematic (tendency to overrate) rather than random, the ±0.25 symmetric band underestimates the downward shift risk and overestimates the upward shift risk. This asymmetric risk is not disclosed.

**Recommendation:**
Add one sentence to the uncertainty derivation: "The three detected errors were all downward corrections (score reduced after review), suggesting possible systematic overrating bias. Under systematic bias, the ±0.25 band may be more accurately interpreted as a -0.25 to -0.05 asymmetric band for frameworks that have not undergone adversarial review of all criteria. The symmetric ±0.25 band is retained as a conservative bound."

**Acceptance Criteria:** Uncertainty derivation acknowledges the directional asymmetry of detected errors and its implication for the band's symmetry assumption.

**Post-Correction RPN Estimate:** S=5, O=3, D=4 → RPN=60

---

### FM-006-I6: Launch Readiness Gate Does Not Specify Owner Field Location in WORKTRACKER.md

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=6, O=5, D=4, RPN=120) |
| **Section** | Section 7.5, Launch Readiness Gate (PM-001-I5 -- R10) |
| **Strategy Step** | Step 2 (Ambiguous failure mode lens) |

**Evidence:**
> "Wave 1 is BLOCKED until all four entity rows have owner fields populated with specific names in the PROJ-020 `WORKTRACKER.md` manifest. An implementer starting Wave 1 MUST confirm entities 1-4 exist with named owners before proceeding."

The gate references "owner fields" but the Jerry WORKTRACKER.md entity schema (worktracker entity frontmatter) uses `owner:` as a frontmatter field. However, the worktracker behavior rules (external to this document) define which entity types have an `owner:` field and what its valid values are. An implementer reading only this document cannot determine: (a) whether "owner fields" means frontmatter `owner:`, a table column, or free-text; (b) what format a "named individual" must take (email? full name? Jerry username?).

**Analysis:**
Ambiguous failure mode: "owner fields populated with specific names" is interpretable multiple ways. Without a reference to the worktracker entity schema, an implementer may populate the wrong field or use an incorrect format and still believe they have satisfied the gate. The gate is not self-contained.

**Recommendation:**
Add a format specification: "Owner fields are populated as the `owner:` frontmatter key in the WORKTRACKER.md entity entry for each required entity, following the jerry worktracker entity schema. Value format: full name or username matching the team's worktracker convention (e.g., `owner: jane.smith` or `owner: Jane Smith`). 'TBD', blank, or role titles (e.g., `owner: project lead`) do not satisfy this requirement."

**Acceptance Criteria:** Launch readiness gate specifies the exact field name (`owner:`) and acceptable value format. An implementer can verify gate compliance without consulting external worktracker documentation.

**Post-Correction RPN Estimate:** S=6, O=2, D=3 → RPN=36

---

### FM-007-I6: Wave Transition Approval Task Entity Schema Unspecified

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=5, O=5, D=5, RPN=125) |
| **Section** | Section 7.4, Wave Transition Evaluator (PM-006-I5 -- R10) |
| **Strategy Step** | Step 2 (Missing failure mode lens) |

**Evidence:**
> "The evaluator reviews the verification method column for the current transition, confirms all criteria are met, and records the transition approval in the worktracker as a completed Task."

The document specifies that approval is recorded "as a completed Task" but does not specify: (a) the Task title convention (e.g., "Wave 1 → 2 Transition Approval"?), (b) which worktracker entity the Task is a child of (the parent Enabler? the sub-skill Story?), (c) which worktracker fields confirm the approval (status: DONE? a comment? an acceptance criteria field?).

**Analysis:**
Missing lens: the approval mechanism is named (a Task) but its structure is missing. Without a schema, evaluators will create ad hoc Tasks with inconsistent titles and placements, making it impossible to audit wave transition history from the worktracker. This also means the launch readiness gate (Section 7.5) cannot be machine-verified -- a `wt-auditor` or similar agent cannot confirm all wave transitions were properly approved without a standardized Task structure.

**Recommendation:**
Add a wave transition Task template: "Wave transition approval Tasks follow the naming convention: `[Wave N → Wave N+1] Transition Approval`. The Task is created as a child of the `/user-experience` skill's parent Feature or Enabler in WORKTRACKER.md. The Task is marked DONE when the evaluator confirms all readiness criteria in the Acceptance Criteria field. Task Acceptance Criteria: list each readiness criterion from Section 7.4 with 'CONFIRMED' or 'EVIDENCE: [artifact path]' beside it."

**Acceptance Criteria:** Wave transition approval Task has a defined naming convention, parent entity, and acceptance criteria format. Tasks created using this template are auditable by `wt-auditor`.

**Post-Correction RPN Estimate:** S=5, O=3, D=3 → RPN=45

---

### FM-008-I6: AI Reliability Tiers Missing Time Estimate for Context-Gathering

| Attribute | Value |
|-----------|-------|
| **Severity** | Major (S=5, O=4, D=6, RPN=120) |
| **Section** | Section 3.1, Nielsen's Heuristics -- AI Reliability Tiers table |
| **Strategy Step** | Step 2 (Insufficient failure mode lens) |

**Evidence:**
> "**Requires team input** -- contextually evaluable | H2 (Match between system and real world), H4 (Consistency and standards), H6 (Recognition over recall), H7 (Flexibility and efficiency), H8 (Aesthetic and minimalist design), H10 (Help and documentation) | Present as hypotheses with specific questions for the team (e.g., 'Does this match the conventions of your target platform? What ecosystem standards apply?')"

The Time estimate qualification (DA-015 -- R7) provides a 30-35 minute total time estimate including "(b) team provides platform context for H2/H4/H6/H7/H8/H10 (~10-20 minutes of team time)." However, the AI Reliability Tiers table does not specify what constitutes sufficient "team input" for each of the 6 contextually-dependent heuristics, nor does it provide the specific questions the team must answer. The "e.g." notation suggests these are examples, not exhaustive question sets.

**Analysis:**
Insufficient lens: the tiers tell non-specialists *that* team input is needed but not *what* input. A non-specialist running heuristic evaluation does not know whether answering one question about H2 is sufficient or whether 5 platform-specific questions need answers before the heuristic can produce actionable findings. The 10-20 minute time estimate assumes teams know what to provide; without a concrete question set, the actual context-gathering time is undefined.

**Recommendation:**
For each "Requires team input" heuristic, add a one-line "Required context" entry: e.g., "H2 required context: name the target platform (iOS/Android/Web/Desktop) and 1-2 platform conventions the design should match." This converts the open-ended context request into a bounded input. Alternatively, create an appendix "Heuristic Context Collection Template" with one question per contextually-dependent heuristic that the team fills in before AI evaluation.

**Acceptance Criteria:** Each of the 6 contextually-dependent heuristics has a defined, bounded context requirement that a non-specialist can satisfy in the stated 10-20 minute window.

**Post-Correction RPN Estimate:** S=5, O=3, D=3 → RPN=45

---

### FM-009-I6 through FM-022-I6: Minor Findings

*(Full detail abbreviated; corrective actions are improvement opportunities)*

### FM-009-I6: Non-Selected Framework Score Disclosure Gap

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=4, O=5, D=4, RPN=80) |
| **Section** | Section 2, Full Scoring Matrix (rows 13-40) |
| **Strategy Step** | Step 2 (Insufficient) |

**Evidence:** The post-correction RPN verification table (R6) covers only the 6 Critical findings from the Revision 4 FMEA. Rows 13-40 in the scoring matrix are annotated as "single-rated with ±0.25 uncertainty" but this disclosure appears only in Section 1 Methodology Limitations, not adjacent to the matrix itself.

**Recommendation:** Add a row-level annotation to the scoring matrix header: "Rows 13-40: single-rater scores, no adversarial review, ±0.25 uncertainty applies."

**Post-Correction RPN Estimate:** S=4, O=3, D=3 → RPN=36

---

### FM-010-I6: User Research Gap Warning Not Surfaced at Routing Invocation

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=5, O=4, D=4, RPN=80) |
| **Section** | Section 7.1, Sub-Skill Routing / HIGH RISK gap (preamble) |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** The HIGH RISK -- USER RESEARCH GAP notice (preamble) states: "The sub-skill routing mechanism in Section 7.1 does NOT surface this limitation at invocation time; implementers MUST embed this warning in the parent `/user-experience` skill's onboarding text." This is a self-documented gap: the document acknowledges the gap exists but defers the fix to implementers.

**Recommendation:** Add a mandatory onboarding text template directly in Section 7.1 (not just the preamble) that implementers can copy verbatim into the parent skill definition.

**Post-Correction RPN Estimate:** S=5, O=2, D=3 → RPN=30

---

### FM-011-I6: SCORING METHODOLOGY DISCLAIMER Scope Unclear in Routing Context

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=4, O=4, D=5, RPN=80) |
| **Section** | Section 3.8, AI-First Design (DA-002-I5 notice) |
| **Strategy Step** | Step 2 (Ambiguous) |

**Evidence:** The SCORING METHODOLOGY DISCLAIMER notice for AI-First Design is in Section 3.8. Section 7.1 routing table references all 10 sub-skills without flagging which entries have projected (P) scores. A reader using only the routing table does not encounter the disclaimer.

**Recommendation:** Add a "(P) -- see Section 3.8 SCORING METHODOLOGY DISCLAIMER" footnote to the AI-First Design row in the Section 7.1 routing table.

**Post-Correction RPN Estimate:** S=4, O=2, D=3 → RPN=24

---

### FM-012-I6: V2 Scoping Trigger Criteria Have No Designated Evaluator

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=4, O=5, D=4, RPN=80) |
| **Section** | Section 4, V2 Scoping Trigger Criteria (SM-009 -- iter3) |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** "Any two triggers in a single month = initiate V2 scoping as a PROJ-020 follow-on project." No role is specified for monitoring triggers or deciding that the threshold has been met.

**Recommendation:** Add: "The `/user-experience` skill lead (or PROJ-020 project lead if no skill lead is assigned) monitors V2 triggers monthly and initiates V2 scoping when the two-trigger threshold is met."

**Post-Correction RPN Estimate:** S=4, O=3, D=3 → RPN=36

---

### FM-013-I6: Solo Practitioner Design Sprint Wave Guidance Missing

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=4, O=4, D=5, RPN=80) |
| **Section** | Preamble, TINY TEAMS POPULATION SEGMENTS (DA-003-I5) |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** Solo practitioner row says "Design Sprint requires adaptation (solo sprint = 1-2 days, not 4-5)" but the Wave adoption plan (Section 7.4) places Design Sprint in Wave 5 and does not reference the solo sprint adaptation. A solo practitioner reading Section 7.4 Wave 5 will find the full-team Design Sprint prerequisites with no solo guidance.

**Recommendation:** Add a solo-sprint parenthetical to Wave 5 entry: "(Solo practitioners: adapted solo sprint = 1-2 days per DA-003-I5; full 4-5 day protocol not required)."

**Post-Correction RPN Estimate:** S=4, O=2, D=3 → RPN=24

---

### FM-014-I6: MEDIUM Gate Recording Path for Confirmed Validation Is Implicit

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=4, O=4, D=5, RPN=80) |
| **Section** | Section 7.6, MEDIUM confidence gate prompt template |
| **Strategy Step** | Step 2 (Ambiguous) |

**Evidence:** The gate template says: "If user selects option (a) or (b), record the validation source and proceed." The term "record" is not defined -- record where? In the skill output? In a worktracker comment? In the synthesis output artifact?

**Recommendation:** Replace "record the validation source" with "include the validation source in the synthesis output artifact as a metadata field: `Validation source: [name / qualification / user count and source]`."

**Post-Correction RPN Estimate:** S=4, O=2, D=3 → RPN=24

---

### FM-015-I6: Wave Bypass Sprint Cycle Length Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=3, O=5, D=5, RPN=75) |
| **Section** | Section 7.4, Wave bypass/stall recovery protocol |
| **Strategy Step** | Step 2 (Ambiguous) |

**Evidence:** "When a wave stalls (team cannot meet readiness criteria within 2 sprint cycles)." Sprint cycle length is not defined. Jerry teams may use 1-week, 2-week, or 4-week sprints.

**Recommendation:** Add: "For this protocol, a sprint cycle is defined as the team's standard sprint length, minimum 1 week and maximum 4 weeks. Teams with no fixed sprint cadence use 2-week cycles as the default."

**Post-Correction RPN Estimate:** S=3, O=2, D=3 → RPN=18

---

### FM-016-I6: C2 Perturbation Table Weight Order Requires Mental Re-Ordering

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=3, O=4, D=6, RPN=72) |
| **Section** | Section 1, C2 Sensitivity Perturbation table header |
| **Strategy Step** | Step 2 (Ambiguous) |

**Evidence:** Table caption reads "25%/15%/15%/15%/20%/10% (C2↓, C5↑)" listing weights in C1-C6 order. A reader must mentally map: C1=25%, C2=15%, C3=15%, C4=15%, C5=20%, C6=10%. The non-standard C2 position (second number, now 15%) is not immediately obvious.

**Recommendation:** Change to "C1=25%, C2=15%, C3=15%, C4=15%, C5=20%, C6=10% (C2 reduced from 20%; C5 increased from 15%)" for clarity.

**Post-Correction RPN Estimate:** S=3, O=2, D=3 → RPN=18

---

### FM-017-I6: HEART Degraded-Mode Misses Hotjar-Only Input Case

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=3, O=4, D=5, RPN=60) |
| **Section** | Section 3.4, HEART Framework, degraded-mode behavior |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** "If the user invokes `/ux-heart-metrics` with no analytics data source and no Hotjar bridge configured, the skill will surface: 'No behavioral data source detected. Proceeding in goal-setting mode'." The case of "Hotjar bridge configured but no product analytics source" is not addressed.

**Recommendation:** Add: "If only Hotjar (Bridge MCP) is configured without a product analytics source, the skill proceeds in goal-setting mode for Engagement/Adoption/Retention/Task Success dimensions and uses Hotjar session recordings only for Happiness and qualitative Engagement insights."

**Post-Correction RPN Estimate:** S=3, O=2, D=3 → RPN=18

---

### FM-018-I6: JTBD Switch Interview Guide Is a Dangling Reference

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=5, O=3, D=4, RPN=60) |
| **Section** | Section 3.6, JTBD, data sufficiency check |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** "the skill surfaces: [...] 'complete at least 3 Switch interviews using the following protocol: [Switch interview guide]. Provide the transcripts as input.' A Switch interview guide is included as a skill artifact." No Switch interview guide exists in this document or at a specified path.

**Recommendation:** Either include a minimal Switch interview guide (4-6 questions, one paragraph) directly in Section 3.6, or specify the file path where the guide will be found in the `/ux-jtbd` sub-skill skill definition: "See `skills/user-experience/artifacts/switch-interview-guide.md`."

**Post-Correction RPN Estimate:** S=5, O=2, D=2 → RPN=20

---

### FM-019-I6: MEDIUM Gate Audit Trail Has No Defined Storage Location

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=3, O=5, D=4, RPN=60) |
| **Section** | Section 7.6, Self-Attestation Limitation (DA-006 -- R9) |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** "the MEDIUM gate requires naming a specific validation source, creating an auditable claim." No location or format for storing this audit trail is defined.

**Recommendation:** "The validation source is recorded in the synthesis output artifact header as `Validation: [source name / qualification / date]`. This constitutes the audit trail. Teams with higher rigor requirements attach the validation source artifact (interview transcript, expert review doc) as a linked file in the worktracker entry."

**Post-Correction RPN Estimate:** S=3, O=2, D=3 → RPN=18

---

### FM-020-I6: Quarterly Owner Verification Has No Succession Protocol

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=3, O=4, D=5, RPN=60) |
| **Section** | Section 7.5, Recurring Entity Tasks (#3 and #4) |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** Entities #3 and #4 require quarterly ownership verification but specify no protocol for when an owner is unavailable (left project, changed role, no longer accessible).

**Recommendation:** Add: "If the primary owner is unavailable at the quarterly verification, the secondary owner assumes verification responsibility. If both owners are unavailable, the PROJ-020 project lead re-executes the owner assignment rule to designate new owners before verification can be marked complete."

**Post-Correction RPN Estimate:** S=3, O=2, D=3 → RPN=18

---

### FM-021-I6: AI-First Design Wave 5 Entry "Specified Path" Is Unspecified

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=4, O=3, D=5, RPN=60) |
| **Section** | Section 7.4, Wave 5 entry criteria for /ux-ai-first |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** "Independent scoring artifact exists at specified path." No path is specified in Section 7.4 or Section 3.8.

**Recommendation:** Replace "at specified path" with the actual path: "at `projects/PROJ-020-feature-enhancements/work/analysis/ai-first-design-scoring.md` (or equivalent path defined in the AI-First Design Enabler's acceptance criteria)."

**Post-Correction RPN Estimate:** S=4, O=2, D=2 → RPN=16

---

### FM-022-I6: Ethics Gap V2 Table Has No Owner for Initiation

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor (S=3, O=4, D=4, RPN=48) |
| **Section** | Section 4, Consolidated V2 Roadmap |
| **Strategy Step** | Step 2 (Missing) |

**Evidence:** The V2 roadmap table and scoping trigger criteria (SM-009) define when to initiate V2 scoping but do not name who owns the ethics gap items (dark patterns, algorithmic bias) specifically.

**Recommendation:** Add note: "Ethics gap items (dark patterns, algorithmic bias) are owned by the same role as V2 scoping: the `/user-experience` skill lead or PROJ-020 project lead per FM-012-I6 correction."

**Post-Correction RPN Estimate:** S=3, O=2, D=3 → RPN=18

---

## Recommendations

### Major Findings (Priority 1 -- Corrective Action Required)

| ID | RPN | Finding | Corrective Action | Estimated Post-Correction RPN |
|----|-----|---------|-------------------|-------------------------------|
| FM-004-I6 | 160 | Wave backward-pass evaluator circular dependency | Define backward-pass evaluator review criteria as distinct from forward-transition criteria; specify timeline and disagreement procedure | 32 |
| FM-002-I6 | 144 | LOW gate qualification buried in cell | Elevate PM-007-I5 caveat to standalone paragraph with callout box above gate table | 36 |
| FM-001-I6 | 140 | No-project-lead fallback undefined | Add solo/no-lead fallback clause to Owner Assignment Rule | 42 |
| FM-007-I6 | 125 | Wave transition Task schema missing | Define Task naming convention, parent entity, and acceptance criteria format | 45 |
| FM-003-I6 | 125 | Part-time UX segment fit unquantified | Name specific frameworks with overstatement risk; define capacity threshold | 45 |
| FM-005-I6 | 120 | ±0.25 band asymmetry not disclosed | Add sentence noting all detected errors were downward corrections; acknowledge asymmetric risk | 60 |
| FM-006-I6 | 120 | Launch gate owner field format unspecified | Specify `owner:` frontmatter field and value format | 36 |
| FM-008-I6 | 120 | Heuristic context-gathering requirements open-ended | Define bounded context requirements per contextually-dependent heuristic | 45 |

### Minor Findings (Priority 2 -- Improvement Opportunities)

| ID | RPN | Finding | Corrective Action |
|----|-----|---------|-------------------|
| FM-009-I6 | 80 | Rows 13-40 no adjacent uncertainty disclosure | Add ±0.25 annotation to matrix header rows 13-40 |
| FM-010-I6 | 80 | User research gap not at routing invocation | Add onboarding text template to Section 7.1 |
| FM-011-I6 | 80 | AI-First Design disclaimer scope unclear in routing | Add (P) footnote to routing table row |
| FM-012-I6 | 80 | V2 trigger evaluator undefined | Assign V2 trigger monitoring to skill lead / project lead |
| FM-013-I6 | 80 | Solo practitioner Design Sprint wave guidance missing | Add solo-sprint parenthetical to Wave 5 entry |
| FM-014-I6 | 80 | MEDIUM gate recording path implicit | Specify validation source recorded in synthesis output artifact header |
| FM-015-I6 | 75 | Sprint cycle length undefined for bypass protocol | Define sprint cycle as team's standard length, default 2 weeks |
| FM-016-I6 | 72 | C2 perturbation weight order requires mental re-ordering | Spell out C1=25%, C2=15%, etc. explicitly |
| FM-017-I6 | 60 | HEART degraded-mode misses Hotjar-only case | Add Hotjar-only configuration handling |
| FM-018-I6 | 60 | JTBD Switch interview guide is a dangling reference | Include guide inline or specify file path |
| FM-019-I6 | 60 | MEDIUM gate audit trail has no storage location | Record validation source in synthesis output artifact header |
| FM-020-I6 | 60 | Quarterly owner verification has no succession protocol | Define secondary owner fallback and re-assignment trigger |
| FM-021-I6 | 60 | Wave 5 /ux-ai-first "specified path" unspecified | Replace with actual path or Enabler-defined path reference |
| FM-022-I6 | 48 | Ethics gap V2 table has no owner | Assign ethics gap ownership to skill lead / project lead |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Slightly Negative | FM-010, FM-013, FM-018, FM-020, FM-021 represent missing content. FM-018 (dangling Switch interview guide reference) is the most significant: the document promises an artifact that does not exist. Overall completeness is high; these are residual gaps in a mature document. |
| Internal Consistency | 0.20 | Slightly Negative | FM-004 (backward-pass/evaluator circular dependency) and FM-014 (MEDIUM gate recording path) represent internal inconsistencies. FM-004 is the most significant: the backward-pass protocol references the evaluator role in a context (backward-pass review) that the evaluator role definition does not cover. |
| Methodological Rigor | 0.20 | Slightly Negative | FM-005 (±0.25 asymmetry not disclosed) is the primary methodological rigor finding. The document's treatment of uncertainty is sophisticated and substantially adequate; the asymmetric directional bias disclosure is the remaining gap. |
| Evidence Quality | 0.15 | Slightly Negative | FM-003 (part-time UX segment unquantified) and FM-009 (no matrix-adjacent uncertainty disclosure for rows 13-40) are the primary evidence quality findings. Both are improvement opportunities rather than substantive defects. |
| Actionability | 0.15 | Slightly Negative | FM-001 (no-lead fallback), FM-006 (launch gate field format), FM-007 (Task schema), FM-008 (heuristic context requirements), FM-012 (V2 trigger evaluator), FM-015 (sprint cycle length) collectively represent the most actionability findings. The 8 Major findings are predominantly actionability gaps -- operations that are named but not fully specified for independent execution. |
| Traceability | 0.10 | Slightly Negative | FM-019 (MEDIUM gate audit trail storage), FM-021 (AI-First Design "specified path") are the primary traceability findings. Both are minor; the document's overall traceability (finding IDs, revision log, evidence table) is strong. |

---

## Execution Statistics

- **Total Findings:** 22
- **Critical (RPN >= 200):** 0
- **Major (RPN 80-199):** 8
- **Minor (RPN < 80):** 14
- **Highest RPN:** 160 (FM-004-I6: Wave backward-pass evaluator circular dependency)
- **Total RPN (pre-correction):** 1,918
- **Estimated Total RPN (post-correction):** ~631
- **RPN Reduction if All Findings Addressed:** ~67%
- **Protocol Steps Completed:** 5 of 5
- **Overall Assessment:** ACCEPT with targeted corrections. Zero Critical findings. The 8 Major findings are operational-specification gaps (missing fallback clauses, undefined schemas, ambiguous field references) introduced by R10's new sections. These are addressable without structural changes to the analysis. The document has matured significantly through 6 tournament iterations; the remaining failure modes are implementation-handoff gaps rather than analytical defects.
