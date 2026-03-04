# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context
- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T14:00:00Z
- **H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (SM-NNN findings addressed across R2, R4, R5, R6, R7 revision tags; confirmed via deliverable revision history)
- **Iteration:** I8 (post-R7 revision)
- **Prior I7 Critical Finding Status:** PM-001-I7 (BOOTSTRAP-VALIDATED passive trigger) addressed in R7 with 180-day calendar-anchored fallback + UNVERIFIED-BENCHMARK reclassification + named Wave Lead owner. PM-002-I7 (Synthesis Judgments Summary not AC-anchored) -- verify R7 address. PM-003-I7 (WARN counter scope) -- verify R7 address. PM-004-I7 (time-to-insight KICKOFF conflict) addressed in R7. PM-005-I7 (re-evaluation failure consequence) addressed in R7. PM-006-I7 (override rate no ceiling) -- verify address. PM-007-I7 (KICKOFF-SIGNOFF required fields) -- verify address. PM-008-I7 (haiku escalation) addressed in R7 with Haiku/Figma pre-launch benchmark AC.

---

## Pre-Mortem Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** GitHub Enhancement Issue -- `/user-experience` skill (C4 tournament, Iteration 8)
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004 execution, Iteration 8)
**H-16 Compliance:** S-003 Steelman applied in prior iterations (SM-001 through SM-006 findings addressed across R2-R7 revisions)
**Failure Scenario:** It is September 2026. Six months after Wave 1 launch. The quarterly skill review convenes. Usage is stagnant: fewer than 5 teams have reached Wave 2, the MCP-heavy variant activation rate is at 28% (above the 20% threshold that triggers V2 planning), and the 3-independent-evaluator requirement for pre-launch blind evaluation could not be staffed by the Jerry community contributor pool at Wave 1 launch. The R7 fixes addressed the passive BOOTSTRAP-VALIDATED trigger and introduced the 180-day calendar anchor and the haiku capability benchmark -- but the review board finds that several R7 additions have introduced implementation ambiguity: the solo bypass path's `SOLO-VALIDATED` peer review requirement has no escalation path when the 30-day window passes without peer review, the `wave-progression.md` ABANDON re-entry guard was added to the directory structure but has no corresponding AC checkpoint, and the dual evaluator qualification standard (pre-launch blind evaluators vs. synthesis-type expert panels) is defined in a footnote but cannot be distinguished at implementation time. The skill failed not because the design was wrong, but because implementation teams could not deterministically verify which qualification standard applied to which evaluation type.

---

## Summary

Pre-Mortem analysis of the post-R7 deliverable identifies **0 Critical** and **6 Major** failure causes across Technical, Process, Assumption, External, and Resource failure categories. The I7 Critical finding (PM-001-I7: BOOTSTRAP-VALIDATED passive trigger) was successfully resolved by R7 -- the 180-day calendar-anchored fallback, UNVERIFIED-BENCHMARK reclassification mechanism, and named Wave Lead owner requirement are all present and address the original finding. PM-008-I7 (haiku escalation) was resolved with the new Haiku/Figma pre-launch benchmark AC. However, R7 introduced three new areas of implementation ambiguity that the pre-mortem reveals as Major failure causes: the solo bypass peer review non-completion path lacks a defined consequence, the wave-progression.md ABANDON re-entry guard is in the directory structure but not in the AC, and the dual evaluator qualification standard creates selection ambiguity at implementation time. Three additional Major findings from prior iterations persist or have residual exposure: the V2 trigger conditions have no measurement owner or storage specification, the WARN counter per-sub-skill vs. per-wave ambiguity from PM-003-I7 needs verification, and the Post-Launch Metrics measurement plan ownership defers assignment entirely to Wave 1 implementation time without a fallback owner. Overall assessment: **REVISE** -- 0 Critical findings; 6 Major findings are addressable with focused AC additions. The deliverable is close to the 0.92 threshold; these are precision gaps, not structural failures.

---

## Step 1: Set the Stage

**Deliverable goals (success definition):**
1. The `/user-experience` skill ships with Wave 1 sub-skills operational, benchmarks validated, and wave enforcement enforced.
2. Teams progress through waves in criteria-gated sequence, with quality signals propagated via S-014 scoring.
3. Community adoption reaches the point where BOOTSTRAP-VALIDATED benchmarks are cross-validated within 180 days.
4. MCP integrations degrade gracefully; no sub-skill is entirely blocked by MCP unavailability.
5. The override and ABANDON mechanisms preserve user authority (P-020) while maintaining audit trails.

**Failure definition:** "It is September 2026. The skill has been live for 6 months. The quarterly review assesses whether to continue or deprecate. Wave 2 adoption is below targets. Implementation ambiguity caused by dual qualification standards prevented the pre-launch blind evaluation from being staffed correctly. The ABANDON re-entry guard was never implemented because no AC required it. The Wave Lead was assigned at KICKOFF but never given the 180-day calendar anchor responsibility in writing because the solo bypass `SOLO-VALIDATED` path did not define what happens when peer review does not arrive within 30 days."

## Step 2: Declare Failure and Shift Perspective

It is September 2026. The `/user-experience` skill launched in March 2026. We are now investigating why the implementation fell short of the quality baseline and wave adoption targets defined in the issue. The R7 fixes were technically correct but left unresolved seams that created friction at implementation time -- the kinds of friction that cause implementors to make defensible-but-wrong choices that compound over 6 months.

---

## Findings Summary

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-I8 | Solo bypass `SOLO-VALIDATED` peer review non-completion has no defined consequence -- the 30-day window passes silently | Process | High | Major | P1 | Actionability |
| PM-002-I8 | `wave-progression.md` ABANDON re-entry guard added to directory structure but has no corresponding AC checkbox -- implementation teams cannot verify it was built | Process | High | Major | P1 | Completeness |
| PM-003-I8 | Dual evaluator qualification standard (pre-launch blind evaluators vs. synthesis expert panels) defined in footnote but not at the point of use -- implementation time selection ambiguity | Technical | Medium | Major | P1 | Internal Consistency |
| PM-004-I8 | V2 trigger condition monitoring has no named owner or storage specification -- the 4 trigger conditions (e.g., "20%+ MCP-heavy variant activation") are defined but no metric owner is assigned to measure them | Resource | Medium | Major | P1 | Actionability |
| PM-005-I8 | WARN counter scope clarification (PM-003-I7) not verifiable in the R7 text -- per-sub-skill vs. per-wave WARN counting ambiguity may persist | Technical | Medium | Major | P1 | Internal Consistency |
| PM-006-I8 | Post-Launch Metrics measurement plan defers ALL ownership assignment to Wave 1 implementation time with no fallback owner defined -- if KICKOFF Wave Lead is unavailable, metrics are unowned | Resource | Low | Major | P2 | Actionability |

---

## Detailed Findings

### PM-001-I8: Solo Bypass `SOLO-VALIDATED` Peer Review Non-Completion Has No Defined Consequence [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Pre-Launch Validation (line ~862) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
The R7 fix for PM-001-I7 states: "The solo bypass 30-day auto-stand provision is replaced by a peer review submission requirement -- the solo evaluation must be submitted for peer review, and `SOLO-VALIDATED` status persists until peer review is completed (it does not auto-pass on timeout)."

Reading the full solo bypass path: "For Wave 5 solo practitioners who cannot source 3 independent evaluators, a solo bypass path is available: the practitioner runs the benchmark evaluation themselves and submits results for asynchronous community peer review within 30 days of merge; if no peer review is received within 30 days, the solo evaluation stands with a 'SOLO-VALIDATED' annotation on the benchmark result."

The R7 fix replaces the "auto-stand" behavior, but the replacement behavior is: `SOLO-VALIDATED` status persists until peer review is completed. If peer review never arrives, `SOLO-VALIDATED` persists indefinitely. No consequence is defined for the case where: (a) the submission was made within 30 days, (b) 30 days passed without peer review, and (c) the status remains `SOLO-VALIDATED` permanently. The R7 fix correctly removed the auto-pass, but left no escalation for the infinite-wait case.

**Analysis:**
In the failure scenario retrospective: a Wave 5 solo practitioner submitted their evaluation for peer review. The Jerry community's contributor pool did not include any available peer reviewers in the 60 days following submission. `SOLO-VALIDATED` status persisted. The benchmark was treated as equivalent to fully-validated by the implementation team, because no downgrade mechanism was defined for the prolonged-no-review case. The R7 fix improved the original 30-day auto-pass problem but left the infinite-persistence failure mode unresolved. This is a Major finding because it affects Wave 5 sub-skill quality baseline integrity -- the Design Sprint sub-skill's benchmark could remain permanently `SOLO-VALIDATED` without an escalation trigger.

**Recommendation:**
Add a calendar-based escalation for `SOLO-VALIDATED` persistence: "If no peer review is received within 90 days of the initial 30-day submission deadline (i.e., 120 days post-merge total), `SOLO-VALIDATED` status transitions to `UNVERIFIED-BENCHMARK` with the same L0 output flag defined for Wave 1 BOOTSTRAP-VALIDATED expiry. The Wave Lead is responsible for sourcing peer review before the 120-day threshold. This mirrors the 180-day BOOTSTRAP-VALIDATED calendar anchor pattern established for Wave 1."

**Acceptance Criteria:**
Pre-Launch Validation AC amended to: (a) define a 120-day maximum persistence window for `SOLO-VALIDATED` status (30 days submission + 90 days review window); (b) specify that `SOLO-VALIDATED` transitions to `UNVERIFIED-BENCHMARK` at 120 days without peer review; (c) assign responsibility for tracking the 120-day window to the Wave Lead.

---

### PM-002-I8: `wave-progression.md` ABANDON Re-Entry Guard in Directory Structure But Not in AC [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Directory Structure (line ~1082) and Acceptance Criteria > Wave Progression (line ~894) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
The R7 fix added `wave-progression.md` to the directory structure with the description: "Wave state tracking and ABANDON log [R7-fix: SR-001-I7]". The ABANDON mechanism text (Key Design Decisions > Wave Deployment, line ~642) states: "Re-entry guard: After ABANDON, the orchestrator MUST consult `wave-progression.md` and BLOCK Wave N+1 routing until a documented blocker-resolution entry is logged."

Searching the Wave Progression AC section (lines ~894-900): The checkboxes include wave entry criteria, wave bypass 3-field documentation, and `WAVE-N-SIGNOFF.md` closure deliverable requirements. There is no AC checkbox requiring that `wave-progression.md` is created with a schema, that the ABANDON re-entry guard is implemented and testable, or that the orchestrator's BLOCK behavior on ABANDON state is verified.

**Analysis:**
The ABANDON mechanism was described in the Key Design Decisions section (behavioral specification) and the directory structure (file listed), but was not elevated to an AC checkbox. In the retrospective: the Wave 1 implementation team created `wave-progression.md` as a blank file because no required fields were specified in the AC. When a team triggered ABANDON during Wave 2 testing, the orchestrator had no `wave-progression.md` schema to validate against, and the re-entry guard behavior was implemented inconsistently across teams. The ABANDON mechanism, described as having "no exceptions" for blocking re-entry without a documented blocker-resolution entry, became effectively advisory because its enforcement was not AC-verified.

**Recommendation:**
Add two AC checkboxes to the Wave Progression section: (1) "`wave-progression.md` created with required fields: wave number, ABANDON date, blocker description, re-entry criteria (what constitutes a documented blocker-resolution entry), and current ABANDON state (ACTIVE/RESOLVED)"; (2) "Orchestrator BLOCK behavior on active ABANDON state is verified: when `wave-progression.md` contains an ACTIVE ABANDON entry for Wave N, invoking any Wave N+1 sub-skill returns BLOCK with the blocker description and re-entry criteria displayed." This closes the gap between the behavioral specification and the deterministic verification checkpoint.

**Acceptance Criteria:**
Wave Progression AC section amended to add: (a) `wave-progression.md` schema AC with required fields enumerated; (b) ABANDON re-entry guard behavior verification AC (BLOCK returned when ACTIVE ABANDON exists, with specific content in the BLOCK message); (c) ABANDON state transitions tracked via `/worktracker` entities per the existing "Wave transitions tracked via `/worktracker` entities" AC.

---

### PM-003-I8: Dual Evaluator Qualification Standard Creates Selection Ambiguity at Implementation Time [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Benchmark Classification (line ~881) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical failures) |

**Evidence:**
The R7 fix (DA-003-I7) added to the Benchmark Classification section: "Reviewer qualification cross-reference: Expert panels for synthesis-type benchmark reviews follow the synthesis validation qualification standard (2 years UX practice, non-team-member). Pre-launch blind evaluators use the separate criterion a/b-i/b-ii standard. The two pools serve distinct functions; qualification standards are intentionally different. [R7-fix: DA-003-I7]"

The Benchmark Classification table lists sub-skills as either "Evaluation" or "Synthesis" type. Evaluation-type uses "Direct comparison" adjudication. Synthesis-type uses "Expert panel review." The Pre-Launch Validation AC (line ~862) defines the criterion a/b-i/b-ii evaluator qualification. The Synthesis Hypothesis Validation section (line ~681) defines the MEDIUM-confidence expert review qualification (2 years UX practice, non-team-member).

The cross-reference note correctly identifies that these are two different standards, but the cross-reference note is in a table footnote. At implementation time, an implementor faces: (1) a Benchmark Classification table listing each sub-skill's adjudication method, (2) a Pre-Launch Validation AC with criterion a/b-i/b-ii, (3) a Synthesis Hypothesis Validation section with a different qualification, and (4) a footnote clarifying these are different. Nothing at the point of each sub-skill's benchmark definition specifies WHICH standard applies to THAT sub-skill's evaluators.

**Analysis:**
In the failure scenario retrospective: the Wave 3 implementation team staffed the `/ux-atomic-design` expert panel review (Synthesis-type per the Benchmark Classification table) using the criterion a/b-i/b-ii standard (pre-launch blind evaluation standard) instead of the 2-years-UX-practice synthesis standard. The result: evaluators were qualified to assess output against a published reference (criterion b-ii: "peer-reviewed UX evaluation experience") but did not have the hands-on component classification experience required to judge whether the atomic design hierarchy recommendations were sound. The cross-reference footnote identified the distinction but did not prevent the wrong standard being applied to a specific sub-skill.

**Recommendation:**
In the Benchmark Classification table, add a column "Evaluator Standard" with values: "Pre-Launch (criterion a/b-i/b-ii)" for Evaluation-type sub-skills, and "Synthesis Expert Panel (2yr UX practice, non-team-member)" for Synthesis-type sub-skills. This puts the applicable qualification standard at the point of use for each sub-skill, eliminating the need for implementors to navigate between three sections.

**Acceptance Criteria:**
Benchmark Classification table amended to add "Evaluator Standard" column with per-sub-skill designation (Pre-Launch standard vs. Synthesis Expert Panel standard). Verification: the Wave 1 pre-launch validation AC references the Benchmark Classification table's Evaluator Standard column to confirm the correct evaluator pool is used for each sub-skill.

---

### PM-004-I8: V2 Trigger Condition Monitoring Has No Named Owner or Storage Specification [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | V2 Roadmap > V2 Candidates (line ~921) |
| **Strategy Step** | Step 3: Generate Failure Causes (Resource failures) |

**Evidence:**
The V2 Roadmap section defines: "V2 planning begins when any 2 of these conditions are met in a single month: (1) A team reports a major product decision made incorrectly due to missing user research; (2) The MCP-heavy variant is activated for 20%+ of invocations; (3) 3+ monthly requests for AI UX pattern guidance while the AI-First Design Enabler is incomplete; (4) A concrete dark pattern complaint or algorithmic bias issue occurs."

The Post-Launch Success Metrics section (lines ~907-913) defines measurement plans for skill adoption, S-014 scores, wave progression rate, MCP fallback activation rate, synthesis hypothesis override rate, and time-to-insight. The Post-Launch Metrics section specifies that "owner assignment, tooling selection, and storage specification are defined during Wave 1 implementation and documented in `skills/user-experience/rules/metrics-plan.md`."

However, the V2 trigger conditions are NOT included in the Post-Launch Metrics section. The MCP fallback rate metric (trigger condition 2: "MCP-heavy variant activated for 20%+ of invocations") has a post-launch metric counterpart, but trigger conditions 1, 3, and 4 have no defined measurement mechanism, owner, or storage location.

**Analysis:**
In the failure scenario retrospective: at the 6-month quarterly review, the MCP-heavy variant activation rate was available (it was tracked per the post-launch metric). But no data was available for trigger condition 1 (team self-reporting of incorrect major decisions due to missing user research) or condition 3 (monthly requests for AI UX pattern guidance). The V2 planning criteria could not be evaluated because 2 of the 4 trigger conditions were never measured. V2 planning was deferred indefinitely -- the skill remained on V1 with known gaps including the user research limitation, dark patterns gap, and algorithmic bias gap.

**Recommendation:**
Cross-reference the V2 trigger conditions with the Post-Launch Success Metrics section. For each trigger condition: (a) identify the corresponding post-launch metric (or add one if missing), (b) specify a measurement method and owner, (c) specify storage in `metrics-plan.md`. Specifically: Trigger 1 (incorrect decision reports) requires a structured user feedback mechanism (e.g., a "report-a-decision" template in the skill output with explicit submission path); Trigger 3 (monthly AI UX guidance requests) requires routing log analysis from the orchestrator; Trigger 4 (dark pattern/bias complaint) requires a feedback path in the `ux-routing-rules.md` issue reporting mechanism.

**Acceptance Criteria:**
V2 Roadmap amended to: (a) link each trigger condition to a corresponding post-launch metric or new tracking mechanism; (b) assign a measurement owner for each trigger condition (may be the same person as the Wave Lead or a named alternative); (c) specify that trigger condition measurements are included in `metrics-plan.md` per the Post-Launch Metrics measurement plan anchor.

---

### PM-005-I8: WARN Counter Per-Sub-Skill vs. Per-Wave Ambiguity May Persist Post-R7 [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Wave Deployment > Wave Enforcement 3-State Behavior (line ~641) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical failures) |

**Evidence:**
The PM-003-I7 finding identified that the WARN escalation counter scope "3 consecutive WARN states across ANY sub-skills within one wave" aggregates unrelated sub-skill WARNs. The I7 report recommended: "Add a per-sub-skill WARN counter: each sub-skill tracks its own consecutive WARN count independently. Crisis mode triggers when a SINGLE sub-skill reaches 3 consecutive WARNs, not when the aggregate across sub-skills reaches 3."

Examining the R7 text in the Wave Enforcement section (line ~641): "WARN escalation: 3 consecutive WARN states across ANY sub-skills within one wave (not per-sub-skill) triggers crisis mode escalation. Sub-skill switching does not reset the counter. [R6-fix: RT-002-I6]"

The R7 revision did NOT change this text. The "[R6-fix: RT-002-I6]" tag is unchanged and the text still reads "across ANY sub-skills within one wave (not per-sub-skill)." The PM-003-I7 recommendation to convert this to per-sub-skill counting was not implemented in R7. The I7 finding was logged as Major and the R7 fix tags do not include a PM-003-I7 resolution tag in this section.

**Analysis:**
This is a persistence of PM-003-I7 rather than a new finding. The aggregate-WARN-counter design means a team using two sub-skills in Wave 2 (Lean UX and HEART Metrics) that encounters 2 WARNs on Lean UX and 1 WARN on HEART Metrics will trigger crisis mode -- even if HEART Metrics is performing well and Lean UX has a specific unrelated issue. Crisis mode activates for the entire wave, routing all sub-skills to the emergency 3-skill sequence, which is disproportionate. This creates a Major failure risk in team adoption: teams will perceive the WARN escalation as erratic and work around it by avoiding the WARN reporting mechanism altogether.

The R7 focus for this section was PM-002-I7 (ABANDON mechanism) and RT-001-I7 (re-entry guard). PM-003-I7's WARN counter recommendation was not carried into R7.

**Recommendation:**
Revise the WARN escalation text to specify per-sub-skill counting: "WARN escalation: when a single sub-skill accumulates 3 consecutive WARN states, that sub-skill enters crisis mode escalation for that sub-skill only. Other sub-skills within the wave are not affected. The WARN counter is tracked per-sub-skill (not aggregated across sub-skills). Sub-skill switching does not affect other sub-skills' WARN counters."

**Acceptance Criteria:**
Wave enforcement 3-state behavior revised to: (a) specify per-sub-skill WARN counter tracking; (b) define crisis mode as affecting the triggering sub-skill only (not the full wave); (c) update the WARN state behavior in `ux-routing-rules.md` to implement per-sub-skill counter logic. Verification: a test scenario where Sub-skill A has 3 WARNs and Sub-skill B has 0 WARNs should result in Sub-skill A in crisis mode and Sub-skill B operating normally.

---

### PM-006-I8: Post-Launch Metrics Measurement Plan Defers All Ownership Assignment Without Fallback [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Post-Launch Success Metrics (line ~906) |
| **Strategy Step** | Step 3: Generate Failure Causes (Resource failures) |

**Evidence:**
The Post-Launch Success Metrics section states: "Post-launch metrics measurement plan: Each metric below requires: (a) named owner, (b) measurement frequency (monthly minimum), (c) tooling/storage specification, and (d) 90-day post-launch review trigger. Owner assignment, tooling selection, and storage specification are defined during Wave 1 implementation and documented in `skills/user-experience/rules/metrics-plan.md`."

The R5 fix added this measurement plan anchor (SR-001-I5). The AC checkboxes for each metric are defined but owner names are deferred: "defined during Wave 1 implementation." The 90-day post-launch review is defined as a trigger, but the reviewer is not named. The Wave Lead was added as the named owner for the BOOTSTRAP-VALIDATED 180-day calendar (R7 fix for PM-001-I7), but the Wave Lead assignment itself occurs at KICKOFF.

If KICKOFF-SIGNOFF.md is never completed (the prerequisite for Wave 1 routing), then no Wave Lead is assigned, and all metrics ownership defers to an unassigned role. The R7 fix for PM-001-I7 references the Wave Lead without verifying that the Wave Lead is assigned before the 180-day calendar starts counting.

**Analysis:**
In the failure scenario retrospective: the Wave Lead was assigned at KICKOFF-SIGNOFF.md completion. However, the Wave Lead changed roles 4 months after Wave 1 launch without a formal handoff of the metrics ownership. Because the metrics plan named only the Wave Lead (not a role title or backup owner), the metrics measurements stopped. The 90-day post-launch review was missed. The 180-day BOOTSTRAP-VALIDATED calendar was not tracked. The UNVERIFIED-BENCHMARK flag was never applied. The failure was not a design deficiency -- the ownership model was defined -- but the ownership model had no succession or fallback mechanism.

**Recommendation:**
The Post-Launch Metrics section and Wave Progression section should require: "The `metrics-plan.md` owner assignment includes a named primary owner AND a named backup owner. On primary owner departure, backup owner assumes all measurement responsibilities. Owner succession is documented in `metrics-plan.md` with a transition date. The 90-day post-launch review trigger is assigned to the backup owner if primary owner is unavailable." This addresses the single-point-of-failure in the metrics ownership model.

**Acceptance Criteria:**
Post-Launch Metrics AC amended to require: (a) `metrics-plan.md` includes both a named primary owner AND named backup owner; (b) backup owner succession protocol defined in `metrics-plan.md`; (c) the BOOTSTRAP-VALIDATED 180-day calendar tracking assignment in the Pre-Launch Validation AC references the `metrics-plan.md` primary/backup owner structure (not solely the Wave Lead title).

---

## Step 4: Priority Matrix

| Priority | Finding | Severity | Likelihood | Rationale |
|----------|---------|----------|------------|-----------|
| P1 | PM-001-I8: Solo bypass SOLO-VALIDATED infinite persistence | Major | High | Affects Wave 5 sub-skill quality baseline for any community without active peer reviewers; directly mirrors the PM-001-I7 pattern already confirmed as Critical in prior iterations |
| P1 | PM-002-I8: wave-progression.md ABANDON re-entry guard not in AC | Major | High | ABANDON mechanism described as having "no exceptions" but verification gap ensures it will be implemented inconsistently |
| P1 | PM-003-I8: Dual evaluator qualification selection ambiguity | Major | Medium | Affects every synthesis-type sub-skill benchmark (4 of 10 sub-skills); likely to cause systematic misqualification of expert panels |
| P1 | PM-004-I8: V2 trigger monitoring no owner | Major | Medium | V2 planning cannot trigger on unmeasured conditions; skills remain on V1 with known gaps indefinitely |
| P1 | PM-005-I8: WARN counter per-wave aggregation persists | Major | Medium | Adoption risk: teams experience disproportionate crisis mode escalation; adoption workaround undermines the WARN enforcement model |
| P2 | PM-006-I8: Post-launch metrics defers ownership without fallback | Major | Low | Low likelihood because Wave Lead assignment is required at KICKOFF; but if Wave Lead departs, all calendar-anchored enforcement collapses |

---

## Step 5: Mitigations

### P1 Mitigations (MUST address before acceptance)

**PM-001-I8 (Solo bypass `SOLO-VALIDATED` infinite persistence):**
Amend Pre-Launch Validation AC to add: "SOLO-VALIDATED status transitions to UNVERIFIED-BENCHMARK at 120 days post-merge if no peer review is received (30-day submission window + 90-day review window). The Wave Lead is responsible for tracking the 120-day window and escalating to the Jerry community contributor pool if peer review is not received by day 90."

**PM-002-I8 (ABANDON re-entry guard not in AC):**
Add two Wave Progression AC checkboxes: (1) "`wave-progression.md` created with required schema fields: wave number, ABANDON date, blocker description, re-entry criteria, current state (ACTIVE/RESOLVED)"; (2) "Orchestrator BLOCK behavior when active ABANDON state exists is verified: BLOCK message includes blocker description and re-entry criteria from `wave-progression.md`."

**PM-003-I8 (Dual evaluator standard selection ambiguity):**
Add "Evaluator Standard" column to Benchmark Classification table with per-sub-skill designation. Amendment is backward-compatible -- it adds a new column to an existing table without changing any existing rows.

**PM-004-I8 (V2 trigger monitoring no owner):**
Amend V2 Roadmap to cross-reference each trigger condition with a corresponding metric in `metrics-plan.md`. Add to Post-Launch Success Metrics section: one checkbox for each V2 trigger condition that lacks a current metric. Minimum additions: trigger condition 1 (incorrect decision reporting mechanism) and trigger condition 3 (AI UX guidance request routing log).

**PM-005-I8 (WARN counter per-wave aggregation persists):**
Revise WARN escalation text to specify per-sub-skill counting. This is a targeted one-paragraph revision in the Key Design Decisions > Wave Deployment section.

### P2 Mitigations (SHOULD address)

**PM-006-I8 (Post-launch metrics defers ownership without fallback):**
Amend Post-Launch Metrics section and Pre-Launch Validation AC to require both a named primary owner and a named backup owner in `metrics-plan.md`, with succession protocol. This is low-risk to implement and high-value for the calendar-anchored enforcement mechanisms added in R7.

---

## Step 6: Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative (PM-002-I8, PM-004-I8) | ABANDON re-entry guard not AC-anchored means a key behavioral specification (described as having "no exceptions") is incompletely specified. V2 trigger conditions 1 and 3 have no measurement mechanism, creating gaps in the deliverable's lifecycle management coverage. |
| Internal Consistency | 0.20 | Negative (PM-003-I8, PM-005-I8) | Dual evaluator qualification standard without per-row designation creates conflicting guidance between the Benchmark Classification table and the Pre-Launch Validation AC. WARN counter per-wave aggregation text unchanged from R6 despite I7 recommendation creates a persistent inconsistency between the stated design intent (wave-level enforcement) and the failure mode described in I7. |
| Methodological Rigor | 0.20 | Neutral | R7 fixes applied correctly address I7 Critical finding. The BOOTSTRAP-VALIDATED calendar anchor, UNVERIFIED-BENCHMARK mechanism, and haiku benchmark AC represent sound methodological additions. No methodological rigor findings in I8. |
| Evidence Quality | 0.15 | Neutral | Evidence quality improved by R7 (calendar-anchored 180-day benchmark, named Wave Lead owner). PM-001-I8 represents a residual evidence quality gap (solo bypass SOLO-VALIDATED can persist indefinitely), but it is a narrower scope than the I7 Critical finding. |
| Actionability | 0.15 | Negative (PM-001-I8, PM-005-I8, PM-006-I8) | Three Major findings affect actionability: solo bypass has no consequence for non-completion, WARN counter escalation is disproportionate to sub-skill-level issues making it difficult for teams to know what action to take, and metrics ownership has a succession gap. |
| Traceability | 0.10 | Neutral | Traceability improved by R7 additions (directory structure, wave-progression.md, ci-checks.md). PM-002-I8 creates a minor traceability gap (directory artifact defined but not AC-verifiable). |

**Net assessment:** Three of six dimensions show negative impact (Completeness, Internal Consistency, Actionability). Three are neutral or positive. The negative impacts are targeted and addressable with focused AC amendments -- none require structural redesign. The prior I7 Critical finding is confirmed resolved. Estimated composite score impact of P1 mitigations: +0.04 to +0.06 composite score improvement, consistent with bridging from 0.867 to the 0.92 threshold.

---

## Step 7: Verify Prior Critical Resolutions

**PM-001-I7 (BOOTSTRAP-VALIDATED passive trigger):**
Confirmed resolved by R7. The text now reads: "BOOTSTRAP-VALIDATED: Wave 1 evaluations using the fallback qualification path (criteria b-i or b-ii above) are tagged BOOTSTRAP-VALIDATED and are NOT equivalent to fully-verified quality benchmarks. Post-launch cross-validation REQUIRED: if no criterion-(a) evaluator completes cross-validation within 180 days of Wave 1 launch, BOOTSTRAP-VALIDATED benchmarks transition to UNVERIFIED-BENCHMARK status with a visible output flag prepended to the sub-skill's L0 output header." The calendar anchor is present. The named Wave Lead owner is present. The 180-day timer is calendar-anchored (not event-triggered). Original Critical finding is RESOLVED.

**PM-008-I7 (Haiku escalation path):**
Confirmed resolved by R7. The Sub-Skill Model Selection section now contains: "Pre-launch model capability benchmark REQUIRED: Haiku confirmed to achieve >= 90% reliability on Figma MCP OAuth + frame extraction across 3 reference design files. If benchmark fails, escalate to Sonnet with revised cost estimate and documented justification per AD-M-009. [R7-fix: DA-001-I7]" and the Wave 1 Sub-Skills AC contains a corresponding checkbox. Original Minor finding is RESOLVED.

**PM-004-I7 (Time-to-insight KICKOFF conflict):**
Confirmed resolved by R7. The text now reads: "Time-to-insight thresholds (<=15 min Wave 1-2, <=30 min Wave 3-5) are enforced as post-launch operational metrics measured by instrumented session timestamps, not as pre-launch evaluation criteria. [R7-fix: FM-028-I7]" The conflict between KICKOFF overhead and the measurement start point is resolved by clarifying that time-to-insight is a post-launch operational metric, not a pre-launch benchmark. Original Major finding is RESOLVED.

---

## Execution Statistics
- **Total Findings:** 6
- **Critical:** 0
- **Major:** 6
- **Minor:** 0
- **Protocol Steps Completed:** 6 of 6
- **Prior Critical (PM-001-I7) Status:** RESOLVED in R7 (confirmed)
- **Prior Critical (PM-002-I7) Status:** NOT RESOLVED -- PM-005-I8 documents continued persistence of WARN counter ambiguity (PM-003-I7 was the WARN finding; PM-002-I7 was Synthesis Judgments Summary; separate verification needed)
- **Overall Assessment:** REVISE -- 0 Critical findings; 6 Major findings requiring targeted AC additions before acceptance. Deliverable is at pre-threshold quality; R8 revisions should bridge to 0.92.
