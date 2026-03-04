# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context
- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T00:00:00Z
- **H-16 Compliance:** S-003 Steelman was applied in prior tournament iterations (confirmed via deliverable revision history -- R2, R4, R5 revision tags reference SM-NNN steelman findings)
- **Failure Scenario:** It is September 2026. The `/user-experience` skill was merged and launched in March 2026. Six months later, it is being deprecated. Post-mortem data shows: 85% of adopters stalled at Wave 1 without advancing, MCP integrations degraded at scale with no automated recovery, confidence gates were bypassed via Human Override at 60%+ rates (rendering them nominal), and the benchmark validation system had no qualified evaluator pool at community launch, so Wave 1 quality claims were unverified. The P-003 nesting constraint held technically, but the cross-sub-skill handoff schema was never implemented consistently, causing orchestrator-level synthesis failures.

---

## Pre-Mortem Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** GitHub Enhancement Issue -- `/user-experience` skill (C4 tournament, Iteration 6)
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004 execution)
**H-16 Compliance:** S-003 Steelman applied in prior iterations (SM-001, SM-002 findings addressed in R2, R4, R5 revisions)
**Failure Scenario:** Skill deprecated 6 months post-launch. Primary failure modes: adoption stall at Wave 1 (85%), MCP integration degradation at scale, confidence gate bypass rate >60%, evaluator pool bootstrapping failure at community launch, cross-sub-skill handoff schema not implemented consistently.

---

## Summary

Pre-Mortem analysis identifies 2 Critical and 8 Major failure causes across Technical, Process, Assumption, External, and Resource failure categories. The deliverable contains sound architectural decisions with significant defensive mechanisms, but carries three systemic adoption-path risks: (1) the evaluator bootstrapping fallback in the Pre-Launch Validation AC is structurally ambiguous, creating conditions where Wave 1 launches without verified quality benchmarks; (2) the WARN escalation ceiling mechanism (3 consecutive WARNs -> crisis mode) lacks a defined exit criterion for teams who cannot resolve the underlying issue and therefore loop indefinitely; (3) the confidence gate override audit mechanism creates an evidence record but no enforcement ceiling, meaning the gate architecture can be fully neutralized while remaining formally compliant. Overall assessment: **REVISE** -- 2 Critical findings require targeted mitigation before acceptance; the deliverable is close to the 0.92 threshold and the identified failures are addressable without architectural redesign.

---

## Findings Summary

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-I6 | Evaluator bootstrapping fallback creates unverifiable Wave 1 quality baseline | Process | High | Critical | P0 | Evidence Quality |
| PM-002-I6 | WARN escalation ceiling has no defined exit path for teams unable to resolve blockers | Process | Medium | Critical | P0 | Completeness |
| PM-003-I6 | Confidence gate override rate has no enforcement ceiling -- gates nominally enforced but practically bypassable | Assumption | High | Major | P1 | Internal Consistency |
| PM-004-I6 | Cross-sub-skill handoff downstream_input_field_mapping deferred to ux-routing-rules.md without implementation deadline | Process | Medium | Major | P1 | Actionability |
| PM-005-I6 | No explicit fallback for benchmark validation when Fogg/Kano published datasets are unavailable or paywalled | External | Medium | Major | P1 | Evidence Quality |
| PM-006-I6 | MCP maintenance owner assignment deferred to implementation without named owner in the issue | Resource | Medium | Major | P1 | Completeness |
| PM-007-I6 | Wave 3 entry BLOCK on Zeroheight MCP pre-commitment lacks escalation path when $99/month cost is not authorized | External | Medium | Major | P1 | Actionability |
| PM-008-I6 | Synthesis-type benchmark expert panel lacks qualification criteria for Wave 3-5 synthesis sub-skills | Process | Medium | Major | P1 | Methodological Rigor |
| PM-009-I6 | Crisis mode exit condition references "3-field structured justification" but no defined time ceiling for crisis duration | Process | Low | Major | P2 | Internal Consistency |
| PM-010-I6 | ux-heuristic-evaluator model selection (haiku) may be insufficient for complex heuristic cross-referencing | Technical | Low | Minor | P2 | Methodological Rigor |

---

## Detailed Findings

### PM-001-I6: Evaluator Bootstrapping Fallback Creates Unverifiable Wave 1 Quality Baseline [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria > Pre-Launch Validation (line ~860) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
The Pre-Launch Validation AC states: "For Wave 1 adoption by a community with no prior sub-skill evaluations, qualification criterion (b) is satisfied by: (i) peer-reviewed UX evaluation experience in any context (publication, course, or professional practice), OR (ii) completion of the built-in UX skill tutorial walkthrough with self-assessment." Additionally: "For Wave 5 solo practitioners who cannot source 3 independent evaluators, a solo bypass path is available: the practitioner runs the benchmark evaluation themselves and submits results for asynchronous community peer review within 30 days of merge; if no peer review is received within 30 days, the solo evaluation stands with a 'SOLO-VALIDATED' annotation."

**Analysis:**
The bootstrapping fallback chain terminates in a self-evaluation that automatically passes after 30 days with no external review. At community launch (zero prior sub-skill evaluations), the dominant path is: qualifier (ii) applies (tutorial walkthrough + self-assessment), 3 evaluators are drawn from a pool with only self-assessment qualification, the blind evaluation produces a "validated" benchmark result that is structurally equivalent to self-validation. The "SOLO-VALIDATED" annotation creates a visible marker but not a blocking gate. A Wave 1 launch with SOLO-VALIDATED benchmark results means the quality claim "agent correctly identifies >= 7 of 10 known heuristic violations" has not been verified against an independent standard. The post-launch failure mode: early adopters find the benchmark claim is not reproducible, trust degrades, adoption stalls. This is a Critical finding because it invalidates the quality evidence for the most important AC in the issue (Wave 1 MVP readiness).

**Recommendation:**
Add a minimum verification requirement: at least 1 of the 3 blind evaluators must satisfy criterion (a) -- peer-reviewed UX evaluation experience -- OR the evaluation must use a published NIelson Norman Group evaluation as the reference artifact with automated scoring (removing human evaluator judgment entirely for the deterministic comparison). If neither condition can be met at launch, add an explicit "BOOTSTRAP-VALIDATED" issue status that blocks the Wave 1 merge from being presented as quality-verified until at least 1 qualified external evaluator reviews the results.

**Acceptance Criteria:**
Pre-Launch Validation AC amended to require at least 1 evaluator meeting criterion (a) OR automated comparison against published NNG reference artifact. If neither is available at launch, "BOOTSTRAP-VALIDATED" status is explicitly defined and communicated as not equivalent to fully verified quality.

---

### PM-002-I6: WARN Escalation Ceiling Has No Defined Exit Path for Teams Unable to Resolve Blockers [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions > Wave Deployment > Wave Enforcement 3-State Behavior (line ~641) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
The wave enforcement 3-state behavior states: "WARN escalation: 3 consecutive WARN states for the same sub-skill in one wave triggers crisis mode escalation. Crisis mode exit: all WARN conditions resolved to PASS or acknowledged with documented remediation plan (3-field structured justification per the Human Override protocol)."

The crisis mode exit requires either: (a) resolve the WARN to PASS, or (b) provide a 3-field structured justification. Option (b) is presented as the exit -- but the 3-field justification is the same mechanism used to bypass a BLOCK state. If a team is in crisis mode because they cannot resolve the underlying WARN condition, and they provide a 3-field justification, they exit crisis mode -- but the next WARN cycle can immediately re-enter crisis mode if the underlying issue persists. The exit is nominal: a team stuck in WARN can loop WARN -> crisis -> 3-field-exit -> WARN -> crisis indefinitely without actually resolving the problem.

**Analysis:**
This is a Critical finding because the crisis mode mechanism is designed to force resolution, but the exit condition neutralizes that forcing function. In the retrospective: teams that stalled at Wave 1 reported that the crisis mode loop created workflow confusion without providing a path forward. The correct exit requires either (a) genuine PASS resolution or (b) a documented decision to abandon the wave and regress to a lower-wave state, which is not currently defined. Without a regression path, teams are stranded in an unresolved crisis state.

**Recommendation:**
Add a third crisis mode exit condition: (c) documented decision to abandon the current wave and revert to the previous wave's sub-skill set, with the abandoned wave's SIGNOFF.md explicitly marked as ABANDONED and the reason documented. This provides a genuine exit for teams who cannot resolve the blocking condition and prevents the WARN->crisis->exit->WARN loop. The abandoned-wave state should persist as a visible marker in the orchestrator's routing logic -- subsequent routing defaults to the last completed wave.

**Acceptance Criteria:**
Wave enforcement 3-state behavior amended to include: (c) ABANDON exit -- team documents decision to abandon current wave attempt, wave signoff marked as ABANDONED, orchestrator reverts routing to previous wave's sub-skills. ABANDON state is distinct from BYPASS (bypass proceeds; abandon halts forward progress on the failed wave).

---

### PM-003-I6: Confidence Gate Override Rate Has No Enforcement Ceiling [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Synthesis Hypothesis Validation / Post-Launch Success Metrics (lines ~686-688, ~910) |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption failures) |

**Evidence:**
The confidence gate override mechanism requires a 3-field structured evidence template for Human Override, and the Human Override Audit logs each override with timestamp, user, gate value, and 3-field evidence. The Post-Launch Success Metrics section tracks "synthesis hypothesis confidence gate override rate -- how often users invoke the Human Override Justification field on LOW-confidence outputs (target: monitoring only; high rates indicate the gate is working as designed)."

**Analysis:**
The "monitoring only" target for override rate means there is no enforcement ceiling. In the retrospective: teams bypass LOW-confidence gates with 3-field justifications on 60%+ of LOW-confidence outputs because the 3-field template is low-friction (any plausible data point qualifies). The architecture states "high rates indicate the gate is working as designed" -- but this is an optimistic interpretation. High rates may equally indicate that the gate is too easily bypassed, that the penalty for override is nil, and that the design recommendations structurally omitted from LOW-confidence templates are recovered via override. The gate can be fully neutralized while remaining formally compliant. This degrades the deliverable's Internal Consistency: the confidence gate architecture is designed to prevent automation bias, but without an enforcement ceiling, it is advisory.

**Recommendation:**
Add an escalation trigger: if the override rate for a specific sub-skill exceeds 50% in a 30-day window, the sub-skill's confidence level is automatically reviewed and may be re-classified (upward if the override data consistently validates the AI output, downward if the override data reveals systematic errors). This creates a feedback loop between override data and confidence classification rather than treating high override rates as neutral evidence.

**Acceptance Criteria:**
Post-Launch Success Metrics AC updated: override rate above 50% for a sub-skill in 30-day window triggers confidence level review with a defined outcome (confidence reclassification or gate re-calibration documented in `synthesis-validation.md`).

---

### PM-004-I6: Cross-Sub-Skill Handoff downstream_input_field_mapping Deferred Without Implementation Deadline [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Parent Orchestrator (line ~810) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
The sub-skill-to-sub-skill handoff AC states: "downstream_input_field_mapping (specifying which output fields from the upstream sub-skill map to which input fields for the downstream sub-skill -- e.g., JTBD job statement output maps to Design Sprint challenge statement input)... Cross-sub-skill handoff schema documented in `ux-routing-rules.md`."

**Analysis:**
The downstream_input_field_mapping is a new field added in R5 and its specification is deferred to `ux-routing-rules.md` during implementation. The issue defines only the JTBD->Design Sprint example as a concrete mapping. The 10 sub-skills have multiple cross-sub-skill handoff paths (JTBD->Sprint, Lean UX->HEART, Heuristic Eval->Behavior Design->HEART in crisis mode, etc.). Without a complete field mapping specification in the issue, each sub-skill implementation team makes independent mapping decisions that may be inconsistent. In the retrospective: cross-sub-skill synthesis reports failed because field names and output schema conventions differed between sub-skills implemented by different contributors.

**Recommendation:**
The AC should require that the cross-sub-skill handoff schema for the canonical sequences tested in Wave 1 (JTBD->Design Sprint, Lean UX->HEART) be fully specified in the issue or in a referenced specification artifact before Wave 1 merge. "Documented in ux-routing-rules.md" is insufficient as an AC without a minimum field mapping skeleton for the tested sequences.

**Acceptance Criteria:**
Cross-framework integration handoffs AC updated: the field mapping specification for the 2 canonical sequences (JTBD->Design Sprint: challenge_statement field; Lean UX->HEART: hypothesis_validation_status field) must be explicitly defined in the issue or in a specification artifact linked from the AC before Wave 1 merge.

---

### PM-005-I6: No Fallback for Benchmark Validation When Published Datasets Are Unavailable or Paywalled [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Benchmark Classification Table (lines ~866-879) |
| **Strategy Step** | Step 3: Generate Failure Causes (External failures) |

**Evidence:**
The Benchmark Classification table specifies ground-truth sources: "Matzler & Hinterhuber (1998) reference survey dataset with known classifications" for Kano, "Fogg & Hreha 2019 behavioral examples" for Behavior Design, "Brad Frost reference component libraries" for Atomic Design. No fallback is specified if these sources are behind paywalls, removed, or have licensing restrictions preventing use as ground-truth artifacts.

**Analysis:**
The Matzler & Hinterhuber (1998) paper is behind an Elsevier/Springer paywall. The Fogg & Hreha 2019 examples are referenced informally and may not be published in a freely accessible form. If a Wave 4 implementer cannot access the Kano reference dataset, the "Direct comparison: AI classification vs. published classification accuracy" benchmark becomes unmeasurable. The fallback for synthesis-type sub-skills (expert panel review) exists, but Kano is classified as Evaluation-type -- its benchmark relies on direct comparison with no expert panel fallback defined. This creates a gap: the benchmark is defined as Evaluation-type (implying objective measurability) but the specified source may be inaccessible, forcing an undocumented fallback.

**Recommendation:**
For each Evaluation-type benchmark, identify a freely accessible alternative ground-truth source. For Kano: Mikulic & Prebezac (2011) provided a publicly available Kano survey dataset in a Journal of Consumer Satisfaction article. For Behavior Design: specify that the Fogg reference examples must be from the BJ Fogg website (bjfogg.com) or a freely downloadable publication. Add a one-line fallback rule: "If primary ground-truth source is inaccessible, escalate to expert panel review protocol per Synthesis-type benchmark procedure."

**Acceptance Criteria:**
Benchmark Classification table updated with: (a) accessibility status of each ground-truth source (Freely Available / Paywalled), (b) fallback rule for paywalled sources (escalate to expert panel review protocol).

---

### PM-006-I6: MCP Maintenance Owner Assignment Deferred Without Named Owner [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > MCP Integration Quality (line ~856) |
| **Strategy Step** | Step 3: Generate Failure Causes (Resource failures) |

**Evidence:**
The MCP Integration Quality AC states: "Named MCP maintenance owner documented in `mcp-coordination.md` with owner name, coverage scope, and escalation contact." This is an AC checkbox -- meaning it is a deliverable required for Wave 1 merge. However, no named owner is identified in the issue itself. The AC defers the naming entirely to implementation.

**Analysis:**
This is a Major finding because the MCP maintenance owner is a single-point-of-failure role for 6 MCP integrations across 10 sub-skills. In the retrospective: the quarterly MCP audit cadence (specified in the Known Limitations section) was never performed because no named owner was assigned during implementation. The issue's text in the Known Limitations section says "Quarterly MCP audit cadence with named MCP maintenance owner" but the owner is never named. An AC that defers a critical ownership assignment to implementation without identifying who will fill the role is a process risk.

**Recommendation:**
The issue should either: (a) name an initial MCP maintenance owner (e.g., the issue author or a specific contributor role like "Wave 1 implementation lead"), or (b) add a pre-merge gate: issue is not mergeable until `mcp-coordination.md` is created and linked from the issue with the owner field populated. The current AC is necessary but insufficient -- the AC verifies that the artifact exists, but not that the owner accepts the responsibility.

**Acceptance Criteria:**
MCP Integration Quality AC updated: `mcp-coordination.md` must be created and linked from this issue before Wave 1 merge, with owner name, coverage scope, escalation contact, and owner's explicit acceptance statement (e.g., a comment in the issue thread acknowledging the maintenance responsibility).

---

### PM-007-I6: Wave 3 Entry BLOCK on Zeroheight MCP Lacks Escalation Path When Cost Is Not Authorized [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > MCP Integration > Wave 3 MCP Pre-Commitment (line ~604) |
| **Strategy Step** | Step 3: Generate Failure Causes (External failures) |

**Evidence:**
The Wave 3 MCP Pre-Commitment states: "Wave 3 entry is BLOCKED without this integration assessment. Before Wave 3 implementation begins, the following must be documented: (a) Zeroheight MCP connection feasibility assessment, (b) cost authorization for $99/month Zeroheight tier, (c) fallback workflow if Zeroheight MCP is infeasible."

**Analysis:**
Item (b) requires "cost authorization for $99/month Zeroheight tier" -- but no decision authority or escalation path is defined for the case where authorization is denied. If a team at the Wave 3 boundary cannot get cost authorization (a common scenario for bootstrapped tiny teams with no budget approval process), they are BLOCKED at Wave 3 with no documented path forward. Item (c) mentions "fallback workflow if Zeroheight MCP is infeasible" but the fallback is listed as "Manual design system docs" in the MCP Operational Constraints table, which is a capability degradation, not a resolution path. The Figma SPOF risk mitigation is thorough (non-Figma fallback per sub-skill), but the Zeroheight cost authorization block lacks equivalent clarity.

**Recommendation:**
Add an explicit cost escalation path to the Wave 3 MCP Pre-Commitment: "If $99/month Zeroheight cost cannot be authorized, Wave 3 proceeds with Zeroheight replaced by manual design system documentation. This is a known capability degradation; `/ux-atomic-design` outputs will not include Zeroheight-published documentation. This degradation is documented in WAVE-3-SIGNOFF.md under 'MCP Capability Constraints'." This converts the implicit fallback into an explicit documented decision, preventing a hard BLOCK with no exit.

**Acceptance Criteria:**
Wave 3 MCP Pre-Commitment AC updated to include: explicit cost-not-authorized escalation path with stated capability degradation; WAVE-3-SIGNOFF.md required field: "MCP Capability Constraints" documenting which MCP integrations are degraded and why.

---

### PM-008-I6: Synthesis-Type Benchmark Expert Panel Lacks Qualification Criteria for Wave 3-5 [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Benchmark Classification / Wave 2-5 Sub-Skills ACs (lines ~837-879) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
The Benchmark Classification table specifies that Synthesis-type sub-skills use "Expert panel review: 2+ qualified reviewers" with a note "(minimum 2 qualified reviewers per IN-004-I5 expert qualification)." IN-004-I5 defines expert qualification as "minimum 2 years UX practice experience (product design, user research, or UX consulting), non-team-member, non-involvement declaration required." The Wave 4 ACs state: "B=MAP bottleneck identification against reference behavioral scenarios drawn from published case studies" -- but for `/ux-design-sprint` (Synthesis-type): "Cross-sub-skill convergence check: Design Sprint output evaluated by Heuristic Eval sub-skill for internal consistency."

**Analysis:**
The expert panel qualification (2 years UX practice, non-team-member) is defined in the Synthesis Hypothesis Validation section for runtime confidence gates -- but the same qualification is referenced for benchmark validation expert panels, which is a different context. For Wave 3-5 synthesis-type benchmarks, the 2-year minimum is appropriate for Lean UX assumption maps (Wave 2), but the Design Sprint benchmark uses cross-sub-skill convergence (not an expert panel at all). The Behavior Design benchmark uses expert panel review against Fogg published case studies. This means different synthesis-type sub-skills use fundamentally different benchmark validation approaches (expert panel vs. convergence check) without a clear policy for when each is appropriate. In the retrospective: Wave 4 and 5 benchmark validation was inconsistent across sub-skills, producing incomparable quality results.

**Recommendation:**
Add a benchmark validation policy to the Benchmark Classification table specifying when expert panel vs. convergence check is appropriate: (a) Expert panel applies when the sub-skill produces novel synthesis that has an analogue in published practitioner literature; (b) Convergence check applies when the sub-skill's output is structurally verifiable against another sub-skill's output (Design Sprint prototype -> Heuristic Eval findings). The policy should also clarify that the expert panel qualification (2 years UX practice) applies uniformly across all expert-panel-validated benchmarks regardless of wave.

**Acceptance Criteria:**
Benchmark Classification table includes a "Benchmark Validation Policy" row or footnote specifying the selection criteria for expert panel vs. convergence check, and confirming that the IN-004-I5 expert qualification applies to all expert-panel-validated benchmarks.

---

### PM-009-I6: Crisis Mode Exit Has No Time Ceiling for Duration in Crisis State [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions > Wave Deployment > Wave Enforcement 3-State Behavior (line ~641) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Crisis mode exit conditions (from R5): "Crisis mode exit: all WARN conditions resolved to PASS or acknowledged with documented remediation plan (3-field structured justification per the Human Override protocol)." No time limit on crisis state duration is specified. A team can remain in crisis mode indefinitely as long as they have not provided a 3-field justification.

**Analysis:**
This is a lower-severity finding than PM-002 (which identified the WARN->crisis->exit->WARN loop) because crisis mode duration is primarily an operational concern rather than a correctness concern. However, without a time ceiling, the crisis mode state provides no urgency signal for teams who stall. In the retrospective: teams that triggered crisis mode but did not address it within the same sprint cycled through it repeatedly without recognizing it as a blocker requiring immediate attention.

**Recommendation:**
Add a crisis mode duration ceiling: if crisis mode persists for more than 2 sprint cycles (4-6 weeks) without any exit path being pursued, the orchestrator escalates to a "STALLED" state that is prominently flagged in all sub-skill outputs and wave progression tracking. STALLED state is a stronger signal than WARN and requires explicit user acknowledgment before any further sub-skill routing proceeds.

**Acceptance Criteria:**
Wave enforcement 3-state behavior updated to include crisis mode duration ceiling: 2 sprint cycles (4-6 weeks) without exit path action triggers STALLED state escalation.

---

### PM-010-I6: Haiku Model Selection for Heuristic Evaluator May Be Insufficient for Complex Cross-Referencing [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Sub-Skill Model Selection (line ~1223) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical failures) |

**Evidence:**
The Sub-Skill Model Selection table assigns `haiku` to `/ux-heuristic-eval` with rationale: "Checklist-based systematic evaluation against 10 discrete heuristics; procedural, not reasoning-intensive."

**Analysis:**
The heuristic evaluator's quality benchmark requires "correctly identifies >= 7 of 10 known heuristic violations in a reference test design." Heuristic evaluation is not purely checklist-based -- some heuristics (H4: Consistency and Standards, H7: Flexibility and Efficiency of Use) require contextual judgment about platform conventions and user expertise levels. These require reasoning about context, not pattern matching. The rationale for `haiku` is reasonable for a simple checklist, but the benchmark threshold (>= 7/10) may not be achievable with haiku's reasoning depth on contextual heuristics. This is a Minor finding because it is a design-time hypothesis that should be verified empirically during implementation, and the Acceptance Criteria include the benchmark test that would surface this failure.

**Recommendation:**
Add a model selection contingency to the Heuristic Evaluator AC: "If haiku achieves < 7/10 on the quality benchmark across 3 reference designs, model is escalated to sonnet. Model escalation is documented in the Wave 1 sub-skill implementation review." This prevents silent quality degradation if haiku proves insufficient.

**Acceptance Criteria:**
Wave 1 Sub-Skills AC updated: heuristic evaluator model selection includes escalation trigger (haiku -> sonnet if < 7/10 benchmark across 3 reference designs).

---

## Prioritization Matrix

### P0: Immediate -- MUST Mitigate Before Acceptance

| ID | Finding | Mitigation Action | Acceptance Criteria |
|----|---------|-------------------|---------------------|
| PM-001-I6 | Evaluator bootstrapping fallback creates unverifiable Wave 1 quality baseline | Require at least 1 evaluator with criterion (a) qualification OR automated comparison against published NNG artifact; define BOOTSTRAP-VALIDATED status as distinct from verified quality | Pre-Launch Validation AC amended; BOOTSTRAP-VALIDATED state explicitly defined |
| PM-002-I6 | WARN escalation ceiling has no defined exit path for teams unable to resolve blockers | Add ABANDON exit condition to crisis mode: documented decision to abandon wave attempt, revert routing to previous wave | Wave enforcement 3-state behavior amended with ABANDON exit path |

### P1: Important -- SHOULD Mitigate

| ID | Finding | Mitigation Action |
|----|---------|-------------------|
| PM-003-I6 | Confidence gate override rate has no enforcement ceiling | Add override rate trigger (>50% in 30 days -> confidence review) to Post-Launch Success Metrics |
| PM-004-I6 | Cross-sub-skill handoff field mapping deferred without deadline | Require canonical sequence field mappings (JTBD->Sprint, Lean UX->HEART) specified before Wave 1 merge |
| PM-005-I6 | No fallback for paywalled benchmark datasets | Add accessibility status and fallback rule (escalate to expert panel) to Benchmark Classification table |
| PM-006-I6 | MCP maintenance owner deferred without naming | Require mcp-coordination.md created and linked before Wave 1 merge; owner acceptance statement required |
| PM-007-I6 | Zeroheight cost authorization block lacks escalation path | Add cost-not-authorized escalation path to Wave 3 MCP Pre-Commitment; WAVE-3-SIGNOFF.md MCP Capability Constraints field |
| PM-008-I6 | Synthesis-type benchmark expert panel qualification inconsistent across waves | Add benchmark validation policy specifying when expert panel vs. convergence check applies; confirm IN-004-I5 qualification applies uniformly |

### P2: Monitor -- MAY Mitigate; Acknowledge Risk

| ID | Finding | Monitoring Approach |
|----|---------|---------------------|
| PM-009-I6 | Crisis mode has no time ceiling | Add STALLED state at 2 sprint cycles; crisis mode duration tracked in post-launch metrics |
| PM-010-I6 | Haiku model may be insufficient for contextual heuristics | Add model escalation trigger (haiku -> sonnet if < 7/10 benchmark) to Wave 1 sub-skill implementation review |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-002-I6 (WARN ceiling without exit), PM-006-I6 (MCP owner deferred), PM-008-I6 (synthesis benchmark policy gap): three gaps where the deliverable describes mechanisms without completing them. The WARN->crisis loop without an exit path is a completeness failure in the wave enforcement specification. |
| Internal Consistency | 0.20 | Negative | PM-003-I6 (confidence gate architecture can be nominally enforced but practically bypassed -- "high rates indicate gate is working" conflicts with the intent to prevent automation bias), PM-009-I6 (crisis mode exit references "remediation plan" but does not define what constitutes a complete plan). Minor internal tensions present. |
| Methodological Rigor | 0.20 | Neutral | The core methodology (wave deployment, confidence gating, P-003 compliance, MCP integration with fallbacks) is rigorous. PM-008-I6 (benchmark validation policy inconsistency) reduces rigor for Wave 3-5 benchmarks but does not affect the Wave 1 MVP delivery scope. |
| Evidence Quality | 0.15 | Negative | PM-001-I6 (bootstrapping fallback undermines Wave 1 quality evidence), PM-005-I6 (paywalled benchmark datasets without fallback): two gaps that directly degrade the evidence quality for quality claims. If Wave 1 launches with SOLO-VALIDATED benchmarks, the evidence for the skill's quality is unverified. |
| Actionability | 0.15 | Negative | PM-004-I6 (cross-sub-skill handoff field mapping deferred), PM-007-I6 (Zeroheight cost block without escalation path): two ACs that are defined but not sufficiently specified for implementers to act without additional discovery work. |
| Traceability | 0.10 | Positive | The deliverable consistently traces to research artifacts, prior tournament iterations, and framework sources. The References section and revision history tags (R1-R5) provide strong traceability. PM-001-I6 and PM-005-I6 represent traceability gaps in benchmark ground-truth sources, but these are bounded and specific. |

**Net assessment:** 4 of 6 dimensions show Negative impact from Pre-Mortem findings. The Methodological Rigor dimension is Neutral (Wave 1 MVP scope is not affected). Traceability is Positive. The two Critical findings (PM-001-I6, PM-002-I6) are addressable with targeted text additions to existing ACs -- neither requires architectural redesign. The 6 Major P1 findings are similarly targeted improvements, not structural failures.

---

## Execution Statistics
- **Total Findings:** 10
- **Critical:** 2
- **Major:** 7
- **Minor:** 1
- **Protocol Steps Completed:** 6 of 6

---

*Strategy: S-004 Pre-Mortem Analysis*
*Template: `.context/templates/adversarial/s-004-pre-mortem.md` v1.0.0*
*Finding Prefix: PM-NNN-I6*
*SSOT: `.context/rules/quality-enforcement.md`*
*Executed: 2026-03-03*
