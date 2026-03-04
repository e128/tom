# FMEA Report: /user-experience Skill GitHub Enhancement Issue (R6)

**Strategy:** S-012 FMEA (Failure Mode and Effects Analysis)
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-012, Iteration 7)
**H-16 Compliance:** S-003 Steelman applied in prior tournament sequence (confirmed)
**Elements Analyzed:** 15 | **Failure Modes Identified:** 14 | **Total RPN:** 1,356

---

## Summary

The R6 deliverable shows targeted improvement on two of I6's two highest-RPN findings (FM-006, FM-014), but both resolutions are partial. FM-006-I6 (Synthesis Judgments Summary format) is partially resolved — R6 defined the 3-field format inline and referenced `synthesis-validation.md`, but the minimum entry count and auto-downgrade rule recommended in I6 were not added; RPN reduced from 180 to 100. FM-014-I6 (crisis mode "resolution" criterion) is partially resolved — R6 added crisis mode exit conditions to the WARN escalation path, but the separate automatic-detection trigger ("multiple prior sub-skill invocations without resolution") still lacks a computable definition of "resolved"; RPN reduced from 180 to 150. Additionally, one new Major finding (FM-028-I7, RPN 150) was introduced by R6's RT-001 fix: the R6 addition stating "The Pre-Launch Validation 15% pass threshold applies per-dimension (completeness, actionability, time-to-insight individually)" creates an operationally incoherent evaluation — time-to-insight is defined as wall-clock execution time, which blind evaluators cannot measure without running timed evaluations, which is incompatible with the blind evaluation methodology. The 11 remaining I6 findings are unchanged (no R6 fixes applied). Total RPN is 1,356 (14 findings: 8 Major, 6 Minor). Recommendation: **REVISE** — the two partial resolutions represent genuine progress; addressing the 3 highest-RPN Major findings (FM-014-I7, FM-028-I7, FM-002-I6) with single-paragraph additions would reduce RPN by approximately 378 points and close the most persistent implementation gaps.

---

## Element Inventory

| ID | Element | Description |
|----|---------|-------------|
| E-01 | Vision Statement | Mission, design philosophy, Saucer Boy narrative framing |
| E-02 | Problem Definition | Tiny Teams UX gap, population segments table |
| E-03 | Solution Architecture | Parent orchestrator + 10 pluggable sub-skills, mermaid diagram |
| E-04 | Sub-Skill Descriptions | 10 framework specifications (agent, mode, tier, MCP, AI/human split) |
| E-05 | Key Design Decisions | 6 decisions: framework-per-skill, routing, P-003, MCP, waves, synthesis validation |
| E-06 | Routing Triage Logic | Flowchart, intent resolution table, crisis mode, capacity check |
| E-07 | MCP Integration | 6 servers, dependency classification, operational constraints table, cost tiers, fallbacks |
| E-08 | Wave Deployment Model | 5 waves, entry criteria, WAVE-N-SIGNOFF enforcement, 4-state behavior (PASS/WARN/ABANDON/BLOCK), bypass mechanism |
| E-09 | Synthesis Hypothesis Validation | 3-tier confidence gates (HIGH/MEDIUM/LOW), automation bias risk, Human Override Justification |
| E-10 | Acceptance Criteria | Parent, Wave 1, Wave 2-5, synthesis, MCP, pre-launch, benchmark classification, quality, wave progression, post-launch |
| E-11 | Known Limitations | User research gap, AI-First conditional, ethics gaps, Figma SPOF, context window, scope creep |
| E-12 | V2 Roadmap | V2 candidates, V2 trigger conditions, architecture evolution path |
| E-13 | Research Backing | Phase 1-3 artifacts, adversarial validation, WSM criteria inline |
| E-14 | Jerry Ecosystem Integration | Relationship diagram, integration table with 6 skills |
| E-15 | Directory Structure | 11 skill directories, ~67 artifacts |

---

## Findings Table

| ID | Element | Failure Mode | S | O | D | RPN | Severity | Corrective Action | Affected Dimension |
|----|---------|-------------|---|---|---|-----|----------|-------------------|--------------------|
| FM-014-I7 | E-06 | Crisis mode auto-detection "resolution" criterion still unimplementable: orchestrator trigger "multiple prior sub-skill invocations without resolution" has no computable definition of a "resolved" invocation despite R6 partially addressing crisis mode exit conditions | 6 | 5 | 5 | 150 | Major | Add to E-06 crisis mode paragraph: "An invocation is resolved when: (a) user creates a worktracker entity from the output, (b) user provides verbal confirmation (e.g., 'got it', 'moving on'), or (c) user invokes a downstream sub-skill consuming this output. An invocation is unresolved if user re-invokes the same sub-skill within the same session without intervening acknowledgment. Crisis mode auto-detection triggers after 2 consecutive unresolved invocations." | Completeness |
| FM-028-I7 | E-10 | R6 time-to-insight fix introduces Pre-Launch Validation incoherence: line 912 states "Pre-Launch Validation 15% pass threshold applies per-dimension (completeness, actionability, time-to-insight individually)" — but time-to-insight is wall-clock execution time, which blind evaluators cannot measure without running timed executions, contradicting the blind evaluation methodology | 5 | 6 | 5 | 150 | Major | Remove "time-to-insight" from the Pre-Launch Validation blind evaluation rubric dimensions. Time-to-insight is a Post-Launch metric (line 912) measured by instrumented session timestamps, not by blind evaluators comparing content outputs. Revise line 912 to: "The Pre-Launch Validation 15% pass threshold applies per-dimension (completeness and actionability individually), not as a composite. Time-to-insight thresholds are enforced as post-launch operational metrics, not pre-launch evaluation criteria." | Internal Consistency |
| FM-002-I7 | E-07 | MCP rate limits non-actionable: Figma (720 req/min) and Miro (100 req/min) documented but no per-invocation request estimate exists for the two highest-rate operations (persistent from Iter 3 — six iterations unchanged) | 6 | 5 | 5 | 150 | Major | Add "Estimated Requests/Invocation" note below the MCP constraints table: "`/ux-heuristic-eval` Figma — estimated 30-50 API calls per 10-heuristic evaluation (10 frame fetches + per-heuristic analysis calls); well within 720/min ceiling. `/ux-design-sprint` Miro — estimated 20-40 calls per sprint day; 4-day sprint cumulative estimated 120-200 calls across 4 sessions; monitor against 100/min peak rate. Mark as 'estimated; validate during Wave N implementation.'" | Actionability |
| FM-016-I7 | E-10 | "Measurable signal" for HEART Wave 2 benchmark undefined: AC requires "all 5 HEART dimensions with measurable signals" but any text string qualifies (persistent from Iter 3 — six iterations unchanged) | 5 | 6 | 5 | 150 | Major | Add: "A measurable signal requires at minimum: (a) metric name, (b) data source, (c) measurement method. Text descriptions without a named data source do not qualify. Example: 'Daily Active Users (Engagement), measured via analytics platform, tracked weekly' qualifies; 'Users should be engaged' does not." | Evidence Quality |
| FM-006-I7 | E-09 | Synthesis Judgments Summary partially resolved: R6 defined the 3-field format inline (AI claim, evidence basis, confidence qualifier) but did not add minimum entry count or auto-downgrade rule; an output with 1 entry claiming "HIGH confidence" still passes the gate nominally | 5 | 4 | 5 | 100 | Major | Add to the HIGH-confidence gate cell in E-09: "Minimum 3 judgment call entries required for HIGH-confidence output designation. Outputs with fewer than 3 identifiable AI judgment calls auto-downgrade to MEDIUM confidence. The Synthesis Judgments Summary minimum entry count is documented in `synthesis-validation.md`." | Completeness |
| FM-026-I7 | E-10 | Cross-framework synthesis AC defines "unified insight report" but specifies no minimum structure for convergent/divergent findings sections (persistent from Iter 4 — five iterations unchanged) | 4 | 5 | 5 | 100 | Major | Define minimum structure: "(a) Convergent findings: 1+ recommendations where 2+ sub-skills agree. (b) Divergent findings: conflicting recommendations with explicit resolution guidance. (c) Portfolio gap: UX lifecycle stages not covered by activated sub-skills. Each section requires at least 1 entry or 'none identified' statement." | Completeness |
| FM-003-I7 | E-10 | JTBD benchmark pass threshold ambiguous: 3-criterion rubric is well-defined but the AC does not state whether 3/3 criteria are required or 2/3 is actionable (persistent from Iter 3 — six iterations unchanged) | 5 | 5 | 5 | 125 | Major | Add explicit pass threshold: "3/3 criteria required for an actionable job statement. A job statement missing the functional+emotional/social dimension underspecifies user motivation; a feature- or technology-framed outcome cannot be validated against user behavior." | Methodological Rigor |
| FM-013-I7 | E-06 | "MCP-heavy team" routing classification undefined: flowchart has "MCP-heavy team?" decision node with no testable definition (persistent from Iter 3 — six iterations unchanged) | 4 | 5 | 4 | 80 | Major | Define as: "A team is MCP-heavy if they have 2+ Required MCPs configured and active. The orchestrator determines this from `KICKOFF-SIGNOFF.md` field 'Available MCP Tools'. A Required MCP counts as configured if the corresponding MCP server is listed in `.claude/settings.local.json` and the team confirms activation during KICKOFF." | Methodological Rigor |
| FM-015-I7 | E-12 | V2 trigger #3 (monthly AI UX pattern requests) cannot be measured — no request-tracking mechanism defined (persistent from Iter 3 — six iterations unchanged) | 3 | 5 | 5 | 75 | Minor | Add: "Monthly invocation counts tracked via worktracker log entries. V2 trigger threshold measured against worktracker entry counts for `/ux-ai-first-design` routing attempts while Enabler incomplete." | Actionability |
| FM-017-I7 | E-13 | WSM C1 > C2 weighting justification absent: graduated-priority rationale does not explain why C1 (0.25) outweighs C2 (0.20) by 25% (persistent from Iter 3 — six iterations unchanged) | 3 | 4 | 5 | 60 | Minor | Add: "C1 (0.25) is weighted above C2 (0.20) because a framework that cannot serve tiny teams fails the fundamental use case even if perfectly composable as a Jerry skill. The defining requirement (C1) outweighs the implementation requirement (C2)." | Evidence Quality |
| FM-018-I7 | E-03 | Mermaid diagram orange fill for AI-First Design conditional has no legend entry in the diagram itself (persistent from Iter 3 — six iterations unchanged) | 3 | 5 | 4 | 60 | Minor | Add diagram caption below the mermaid block: "Orange fill = CONDITIONAL sub-skill (requires Enabler DONE status with verified WSM score >= 8.00 before Wave 5 deployment)." | Traceability |
| FM-008-I7 | E-09 | Human Override Justification storage mechanism undefined: described as creating "an auditable evidence chain" but no storage location specified for the 3-field structured template entries (persistent from Iter 3 — six iterations unchanged) | 3 | 5 | 4 | 60 | Minor | Specify: "Human Override Justification is stored as a block-quoted field in the sub-skill output artifact under a `## Human Override Justification` heading. The 3-field structured evidence template is appended to the artifact at the point of override." | Traceability |
| FM-022-I7 | E-10 | MCP fallback rate target (< 20%) lacks a defined response when the target is exceeded (persistent from Iter 4 — five iterations unchanged) | 3 | 4 | 4 | 48 | Minor | Add: "If MCP fallback rate exceeds 20% for a Required MCP during the first 90 days, the named MCP maintenance owner (from `mcp-coordination.md`) investigates root cause within 2 weeks and reports findings to the V2 planning cycle." | Actionability |
| FM-027-I7 | E-10 | Wave bypass expiry described in E-08 ("bypass state persists as a warning banner") but no expiry deadline enforced in the Wave Progression AC section (persistent from Iter 4 — five iterations unchanged) | 3 | 4 | 4 | 48 | Minor | Add to Wave Progression AC: "Wave bypass expires after 60 days or the next wave progression review (whichever is sooner). The orchestrator displays an escalation warning before each subsequent sub-skill invocation after expiry, prompting the team to either close the gap or formally ABANDON the wave." | Completeness |

*Note: 14 active findings total (8 Major, 6 Minor, 0 Critical). Two I6 findings partially resolved by R6 (FM-006, FM-014) with reduced RPNs. One new finding (FM-028-I7) introduced by the R6 RT-001 fix. Eleven I6 findings continued unchanged.*

---

## Detailed Findings

### FM-014-I7: Crisis Mode Auto-Detection Resolution Criterion Unimplementable

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-06 (Routing Triage Logic) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-06 (line 431): "Crisis mode activates when the user explicitly describes urgency ('urgent', 'critical UX issue', 'users are leaving') or when the orchestrator detects multiple prior sub-skill invocations without resolution."

R6 added exit conditions (line 641): "Crisis mode exit: (a) all WARN conditions resolved to PASS (automated check against WAVE-N-SIGNOFF.md criteria), OR (b) blocker acknowledged with documented remediation plan (worktracker entity creation + named owner + target date), OR (c) ABANDON."

No definition of "resolved" vs. "unresolved" invocation exists anywhere in E-05, E-06, or E-10.

**Analysis:**
R6 partially addressed this finding by adding crisis mode exit conditions to the WARN escalation path. This is a genuine improvement — knowing how to exit crisis mode is important. However, the R6 fix addresses the exit path from crisis mode, not the entry criterion via automatic detection. The trigger "orchestrator detects multiple prior sub-skill invocations without resolution" still has no computable definition of resolution. An implementer cannot write the detection logic without knowing what signal constitutes a "resolved" invocation. The exit conditions (WARN resolved to PASS, documented remediation, ABANDON) are orthogonal to this — those address the WARN escalation pathway to crisis mode, whereas the automatic-detection pathway has no defined resolution signal. S unchanged at 6 (automatic-detection path is unimplementable). O reduced from 5 to 5 (partial fix doesn't change detection ambiguity). D reduced from 6 to 5 (R6 fix makes the document appear more specified, reducing casual detection of the gap). RPN: 6×5×5 = 150.

**Recommendation:**
Add to E-06 crisis mode paragraph immediately after "without resolution": "For automatic-detection purposes, an invocation is resolved when: (a) user creates a worktracker entity from the sub-skill output, (b) user provides verbal confirmation (e.g., 'got it', 'acknowledged', 'moving on'), or (c) user invokes a downstream sub-skill that references this sub-skill's output as an input. An invocation is unresolved if the user re-invokes the same sub-skill within the same session without an intervening acknowledgment signal. Crisis mode automatic-detection triggers after 2 consecutive unresolved invocations of the same sub-skill."

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72

---

### FM-028-I7: Time-to-Insight Creates Pre-Launch Validation Incoherence

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria — Pre-Launch Validation and Post-Launch Success Metrics) |
| **Strategy Step** | Step 2: Failure mode lens — Inconsistent |

**Evidence:**
E-10, Pre-Launch Validation (line 861): "Comparison uses a blind evaluation rubric: 3 independent evaluators score both the AI-augmented output and a manually-produced reference output on completeness, actionability, and time-to-insight without knowing which is AI-augmented... Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions."

E-10, Post-Launch Success Metrics (line 912) — R6 fix: "Time-to-insight defined as: elapsed wall-clock time from sub-skill invocation to first actionable finding presented to user. Measurement: instrumented via session timestamp delta (invocation start to first L0 output). Threshold: <= 15 minutes for Wave 1-2 sub-skills... The Pre-Launch Validation 15% pass threshold applies per-dimension (completeness, actionability, time-to-insight individually), not as a composite."

**Analysis:**
The Pre-Launch Validation blind evaluation methodology (line 861) was established in prior iterations to have 3 evaluators score AI-augmented vs. reference outputs on completeness, actionability, and time-to-insight. The R6 fix defined time-to-insight as wall-clock execution time measured by session timestamp instrumentation. These two definitions are operationally incompatible: a blind evaluator comparing two static outputs (the AI-augmented output and the manually-produced reference output) cannot measure wall-clock execution time — the evaluators see the finished artifacts, not the generation process. The 15% pass threshold applies to a metric that the evaluators cannot observe. The R6 addition resolves the "time-to-insight undefined" issue (RT-001) but introduces an internal inconsistency in the Pre-Launch Validation section. S=5 (creates operationally incoherent evaluation criterion but does not invalidate the overall Pre-Launch Validation approach). O=6 (the inconsistency is inherent in the current text and will affect any implementer who tries to set up the blind evaluation). D=5 (the connection between the two sections requires cross-referencing line 912 back to line 861). RPN: 5×6×5 = 150.

**Recommendation:**
Remove "time-to-insight" from the Pre-Launch Validation blind evaluation rubric dimensions in line 861 — change "completeness, actionability, and time-to-insight" to "completeness and actionability". Time-to-insight is an instrumented operational metric (post-launch, measured by session timestamp delta) and cannot be evaluated in a blind content comparison. Revise the R6 addition in line 912 to: "The Pre-Launch Validation 15% pass threshold applies per-dimension (completeness and actionability individually), not as a composite. Time-to-insight thresholds (≤ 15 minutes for Wave 1-2, ≤ 30 minutes for Wave 3-5) are enforced as post-launch operational metrics measured by instrumented session timestamps, not as pre-launch evaluation criteria."

**Post-Correction RPN:** S=5, O=3, D=3 → RPN=45

---

### FM-002-I7: MCP Rate Limits Non-Actionable Without Per-Operation Estimates

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-07 (MCP Integration) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-07 MCP constraints table (lines 593-599): Figma rate limit documented as "720 req/min per-user (Professional)" and Miro as "100 req/min per-user (Team plan)." No per-invocation request estimate exists for any operation.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. The absolute rate limit is documented but not actionable. An implementer needs to know whether a single `/ux-heuristic-eval` evaluation comes anywhere near the 720 req/min Figma ceiling, or whether the 100 req/min Miro limit creates practical constraints during a 4-day Design Sprint. Without per-operation estimates, the rate limit rows are awareness-only, not implementable guardrails. An MCP runbook AC was added in Iter 4 requiring backoff strategy documentation, but a backoff strategy requires knowing when backoff triggers — i.e., approximately how many requests a typical invocation makes. R6 did not add per-operation estimates. S=6. O=5. D=5. RPN: 6×5×5 = 150.

**Recommendation:**
Add a note below the MCP constraints table: "Per-Operation Request Estimates (for rate limit planning, provisional — validate during Wave N implementation): `/ux-heuristic-eval` Figma evaluation — estimated 30-50 API calls per 10-heuristic assessment (10 frame fetches + per-heuristic analysis calls); well within 720/min ceiling. `/ux-design-sprint` Miro — estimated 20-40 calls per sprint day (board create, lane create, sticky create per exercise); cumulative 4-day sprint estimated 120-200 calls across 4 sessions; monitor against 100/min peak call rate during Day 2-3 intensive exercises."

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72

---

### FM-016-I7: HEART Benchmark "Measurable Signal" Criterion Unverifiable

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-10 Wave 2 benchmark (line 835): "benchmark: populates all 5 HEART dimensions with measurable signals from a product description."

No definition of "measurable signal" appears in E-10, E-04, or E-09. Any text generated for each HEART dimension technically constitutes "signals."

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. The HEART benchmark requires "measurable signals" but the term has no operational definition in the document. Without this, a benchmark evaluator cannot distinguish a passing signal ("Daily Active Users, measured via analytics platform, tracked weekly") from a non-qualifying description ("Users should be happy with the product"). The ambiguity means the benchmark can be satisfied by any generated text that mentions the five dimensions. S=5. O=6. D=5. RPN: 5×6×5 = 150.

**Recommendation:**
Add after "measurable signals" in the Wave 2 HEART benchmark: "(A measurable signal must contain at minimum: (a) a metric name, (b) a named data source, and (c) a measurement method. Example: 'Task completion rate [metric] via session recording analytics [source], calculated as completed flows / initiated flows per session [method]'. A description without a named data source does not qualify as a measurable signal.)"

**Post-Correction RPN:** S=5, O=3, D=4 → RPN=60

---

### FM-006-I7: Synthesis Judgments Summary Minimum Entry Count Missing

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-09 (Synthesis Hypothesis Validation) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-09 (line 680) — R6 fix: "Synthesis Judgments Summary format: 3 fields per judgment -- (a) AI-generated claim (verbatim from sub-skill output), (b) Evidence basis (source sub-skill, confidence level, data points cited), (c) Confidence qualifier (HIGH/MEDIUM/LOW with rationale). Documented in `skills/user-experience/rules/synthesis-validation.md`."

E-10 Synthesis Hypothesis Validation AC (line 843): "HIGH-confidence outputs require enumerated acknowledgment of AI judgment calls"

No minimum entry count is defined. No auto-downgrade rule is defined.

**Analysis:**
R6 addressed the I6 finding by defining the 3-field format for individual entries — this is a genuine improvement. However, the I6 recommendation also included: (a) a minimum entry count ("Minimum 3 entries required for HIGH-confidence output"), and (b) an auto-downgrade rule ("fewer than 3 identifiable AI judgment calls auto-downgrades to MEDIUM confidence"). Neither was added by R6. Without a minimum entry count, the HIGH-confidence gate is satisfied by a single entry with the correct 3-field format, providing nominal rather than substantive oversight. The E-10 AC still says only "enumerated acknowledgment" with no minimum count. S reduced from 6 to 5 (format is now defined, reducing systemic ambiguity). O reduced from 6 to 4 (the fix narrows the failure mode to a specific gap rather than complete absence). D unchanged at 5 (the missing count is not obvious from the defined format). RPN: 5×4×5 = 100.

**Recommendation:**
Add to E-09 HIGH-confidence gate cell immediately after the R6 format definition: "Minimum 3 judgment call entries required for HIGH-confidence output designation. Outputs with fewer than 3 identifiable AI judgment calls auto-downgrade to MEDIUM confidence and are processed according to the MEDIUM gate behavior. The minimum entry count is enforced by the sub-skill template structure." Also add to E-10 Synthesis Hypothesis Validation AC: "HIGH-confidence outputs require enumerated acknowledgment via Synthesis Judgments Summary with minimum 3 entries (3-field format: AI claim, evidence basis, confidence qualifier) per `synthesis-validation.md`."

**Post-Correction RPN:** S=5, O=3, D=4 → RPN=60

---

### FM-003-I7: JTBD Benchmark Pass Threshold Not Stated

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-10 Wave 1 JTBD benchmark (line 829): "agent produces job statements that pass a 3-criterion deterministic rubric: (a) follows canonical 'When [situation], I want to [motivation], so I can [outcome]' format; (b) contains at least 1 functional AND 1 emotional or social dimension; (c) references an outcome, not a product feature or technology. 3/3 criteria = actionable."

The rubric description says "3/3 criteria = actionable" but the AC text itself does not say whether 2/3 passes or fails.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. The phrase "3/3 criteria = actionable" appears in parentheses in a descriptive context, which is ambiguous — it could be read as "if all 3 are met the output is actionable" rather than "all 3 are required." An evaluator comparing AI output to the benchmark could argue that 2/3 criteria satisfied constitutes partial credit. The corrective action is a single clarifying sentence. S=5. O=5. D=5. RPN: 5×5×5 = 125.

**Recommendation:**
Replace "3/3 criteria = actionable. No UX practitioner consultation required." with "Pass threshold: 3/3 criteria required. A job statement that satisfies only 2/3 criteria is not actionable and does not pass the benchmark. Rationale: (b) a missing emotional/social dimension underspecifies user motivation; (c) a feature- or technology-framed outcome cannot be validated against user behavior independent of implementation."

**Post-Correction RPN:** S=5, O=3, D=4 → RPN=60

---

### FM-026-I7: Cross-Framework Synthesis Unified Report Minimum Structure Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-10 Parent Orchestrator AC (line 809): "Cross-framework synthesis AC: The `/user-experience` parent skill produces a unified insight report combining findings from 2+ sub-skill analyses on the same product, identifying convergent and divergent recommendations across frameworks."

No minimum structure is defined for the unified insight report. "Convergent and divergent recommendations" is undefined in terms of minimum content.

**Analysis:**
Persistent from Iter 4 — five iterations unchanged. The AC defines the outcome ("identifies convergent and divergent recommendations") but does not define what constitutes a minimal compliant report. An implementer or reviewer cannot determine whether a report that mentions convergence in one sentence passes this AC. S=4. O=5. D=5. RPN: 4×5×5 = 100.

**Recommendation:**
Extend the cross-framework synthesis AC: "The unified insight report MUST contain minimum three sections: (a) Convergent findings — at least 1 recommendation supported by 2+ sub-skills; (b) Divergent findings — at least 1 case where sub-skills produce conflicting guidance, with explicit resolution recommendation; (c) Portfolio gap — UX lifecycle stages not covered by currently activated sub-skills. Each section requires at least 1 entry or an explicit 'none identified' statement with rationale."

**Post-Correction RPN:** S=4, O=3, D=4 → RPN=48

---

### FM-013-I7: MCP-Heavy Team Routing Classification Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-06 (Routing Triage Logic) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-06 routing flowchart (lines 440-477): flowchart includes decision node "MCP-heavy team?" with branches to "Apply MCP-heavy variant recommendations" or to Stage routing. No definition of "MCP-heavy" appears in E-05, E-06, or E-10.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. The flowchart has a decision node for MCP-heavy teams, but the orchestrator cannot evaluate this condition without a testable definition. An implementer writing the routing rules cannot determine which teams qualify. S=4. O=5. D=4. RPN: 4×5×4 = 80.

**Recommendation:**
Add a definition in the E-05 Key Design Decision #2 (Parent Orchestrator Routes) section, adjacent to the flowchart explanation: "MCP-heavy team definition: a team that has 2+ Required MCPs (not Enhancement MCPs) configured and active at KICKOFF-SIGNOFF. The orchestrator reads the 'Available MCP Tools' field from `KICKOFF-SIGNOFF.md` to evaluate this condition. Required MCPs are those listed as 'Required' in the sub-skill attribute tables. Enhancement MCPs do not count toward the threshold."

**Post-Correction RPN:** S=4, O=3, D=3 → RPN=36

---

### FM-015-I7: V2 Trigger #3 Has No Measurement Mechanism

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Element** | E-12 (V2 Roadmap) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-12 (lines 920-925): "V2 planning begins when any 2 of these conditions are met in a single month:... 3+ monthly requests for AI UX pattern guidance while the AI-First Design Enabler is incomplete."

No request-tracking mechanism defined for condition 3.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. Unlike conditions 1, 2, and 4 (which have observable signals), condition 3 requires counting "monthly requests for AI UX pattern guidance" with no specification of what tool tracks these or what constitutes a qualifying "request." S=3. O=5. D=5. RPN: 3×5×5 = 75.

**Recommendation:**
Add: "Condition 3 measurement: monthly worktracker entry counts for `/ux-ai-first-design` routing attempts (requests that triggered the conditional status warning) while Enabler status is incomplete. Tracked by the named MCP maintenance owner in `mcp-coordination.md`."

**Post-Correction RPN:** S=3, O=3, D=4 → RPN=36

---

### FM-017-I7: WSM C1 > C2 Weighting Rationale Missing

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Element** | E-13 (Research Backing) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-13 (lines 972-981): WSM Criteria table lists C1 (Applicability to AI-Augmented Tiny Teams, 0.25) and C2 (Composability as Independent Jerry Sub-Skill, 0.20). Graduated-priority rationale (line 981): "Tier 1 (C1: 25%, C2: 20%) represents the defining requirements for tiny-teams AI-augmented context." The statement identifies both as "defining requirements" without explaining why C1 outweighs C2.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. Reviewers challenging the framework selection may question why the primary differentiator (Tiny Teams fit) outweighs the operational requirement (Jerry composability) by 25%. One clarifying sentence resolves this. S=3. O=4. D=5. RPN: 3×4×5 = 60.

**Recommendation:**
Add to the graduated-priority rationale: "C1 (0.25) is weighted above C2 (0.20) because a framework that cannot serve tiny teams fails the core use case regardless of how well it composes as a Jerry skill. C2 is a constraint that limits the candidate universe; C1 is the criterion that differentiates candidates that pass the constraint."

**Post-Correction RPN:** S=3, O=3, D=4 → RPN=36

---

### FM-018-I7: Mermaid Diagram Missing Legend for Conditional Sub-Skill

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Element** | E-03 (Solution Architecture) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-03 mermaid diagram (lines 101-143): `style AF fill:#E8A838,color:#000` sets AI-First Design to orange fill. No caption or legend entry explains what the orange fill means.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. Orange fill indicates conditional status, but this is not self-evident to a first-time reader. The solution description mentions "CONDITIONAL" in the sub-skill label, but a legend makes the visual encoding explicit. S=3. O=5. D=4. RPN: 3×5×4 = 60.

**Recommendation:**
Add a caption line immediately after the mermaid code block closing: "**Diagram key:** Blue fill (UE node) = parent orchestrator. Orange fill (AF node) = CONDITIONAL sub-skill — deployment requires Enabler DONE status with verified WSM score >= 8.00 before Wave 5."

**Post-Correction RPN:** S=3, O=3, D=3 → RPN=27

---

### FM-008-I7: Human Override Justification Storage Location Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Element** | E-09 (Synthesis Hypothesis Validation) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-09 (line 687): "Each synthesis output therefore includes a `Human Override Justification` field -- if a user chooses to act on a LOW-confidence output, they must provide a 3-field structured evidence template: (a) Named data source...; (b) Specific supporting data point...; (c) Validation date..."

E-09 (line 689): "Every P-020 override of wave gates or confidence thresholds is logged with: (a) override timestamp, (b) overriding user, (c) original gate/threshold value, (d) 3-field structured evidence justification... Audit log persisted to `work/audit/override-log.md`."

The audit log storage is defined (`work/audit/override-log.md`) but the inline storage of the Human Override Justification field in the sub-skill output artifact has no defined location. These are two separate storage concerns: the audit log (aggregate) and the per-output field (inline).

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. The audit log location is defined; the per-output field storage is not. An implementer designing the sub-skill output template does not know where to place the Human Override Justification field. S=3. O=5. D=4. RPN: 3×5×4 = 60.

**Recommendation:**
Add to E-09 Human Override Justification paragraph: "The 3-field Human Override Justification is stored inline in the sub-skill output artifact as a `## Human Override Justification` section appended at the end of the output document, immediately before the References section if present."

**Post-Correction RPN:** S=3, O=3, D=3 → RPN=27

---

### FM-022-I7: MCP Fallback Rate 20% Target Has No Defined Response

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-10 Post-Launch Success Metrics (line 910): "Track: MCP fallback activation rate per sub-skill (target: < 20% of invocations requiring fallback for Required MCPs)."

No defined response when the 20% target is exceeded.

**Analysis:**
Persistent from Iter 4 — five iterations unchanged. The tracking target is defined but it is monitoring-only without a response trigger. A target without a defined response is advisory rather than actionable. S=3. O=4. D=4. RPN: 3×4×4 = 48.

**Recommendation:**
Extend the MCP fallback rate metric: "Target: < 20% of invocations requiring fallback for Required MCPs. If this target is exceeded during the first 90-day post-launch period, the named MCP maintenance owner (from `mcp-coordination.md`) investigates root cause within 2 weeks and presents findings at the next V2 planning review."

**Post-Correction RPN:** S=3, O=3, D=3 → RPN=27

---

### FM-027-I7: Wave Bypass Expiry Not Enforced in Acceptance Criteria

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Inconsistent |

**Evidence:**
E-08 (line 645): "Wave stall bypass: If a wave stalls for 2+ sprint cycles... Bypass state persists as a warning banner on all sub-skill outputs produced under bypass."

E-10 Wave Progression AC (lines 892-899): Wave bypass is listed as requiring 3-field documentation, but no expiry deadline or escalation for persistent bypass appears in the AC section.

**Analysis:**
Persistent from Iter 4 — five iterations unchanged. The bypass mechanism is described in E-08 as producing a warning banner. However, the Wave Progression AC does not require the orchestrator to enforce expiry or escalate persistent bypasses. Without an expiry AC, teams can remain indefinitely in bypass state without accountability. S=3. O=4. D=4. RPN: 3×4×4 = 48.

**Recommendation:**
Add to Wave Progression AC: "Wave bypass expires after 60 days or the next wave progression review (whichever is sooner). The orchestrator MUST display an escalation warning before each subsequent sub-skill invocation after bypass expiry, prompting the team to either close the unmet criterion or formally ABANDON the wave per the ABANDON procedure. Indefinite bypass without resolution or ABANDON is not a valid state."

**Post-Correction RPN:** S=3, O=3, D=3 → RPN=27

---

## Recommendations (Priority-Ordered)

### Critical Findings
*None.*

### Major Findings (Priority Order by RPN)

| Priority | ID | Current RPN | Corrective Action | Est. Post-Correction RPN |
|----------|----|-----------|--------------------|--------------------------|
| 1 | FM-014-I7 | 150 | Add computable "resolved" invocation definition to crisis mode auto-detection trigger | 72 |
| 2 | FM-028-I7 | 150 | Remove time-to-insight from Pre-Launch Validation blind evaluation dimensions; clarify it is post-launch operational metric only | 45 |
| 3 | FM-002-I7 | 150 | Add per-operation request estimates (provisional) for Figma and Miro below MCP constraints table | 72 |
| 4 | FM-016-I7 | 150 | Define "measurable signal" with 3-part minimum (metric name + data source + measurement method) in HEART benchmark | 60 |
| 5 | FM-003-I7 | 125 | Explicitly state "3/3 criteria required" as pass threshold in JTBD benchmark | 60 |
| 6 | FM-006-I7 | 100 | Add minimum 3-entry count and auto-downgrade rule to Synthesis Judgments Summary gate | 60 |
| 7 | FM-026-I7 | 100 | Define minimum 3-section structure for unified insight report in cross-framework synthesis AC | 48 |
| 8 | FM-013-I7 | 80 | Define "MCP-heavy team" as 2+ Required MCPs configured and active at KICKOFF | 36 |

### Minor Findings (Priority Order by RPN)

| Priority | ID | Current RPN | Corrective Action | Est. Post-Correction RPN |
|----------|----|-----------|--------------------|--------------------------|
| 9 | FM-015-I7 | 75 | Add worktracker log as V2 trigger #3 measurement mechanism | 36 |
| 10 | FM-017-I7 | 60 | Add C1 > C2 weighting rationale (1 sentence) | 36 |
| 11 | FM-018-I7 | 60 | Add diagram caption with visual encoding legend | 27 |
| 12 | FM-008-I7 | 60 | Specify Human Override Justification stored as `## Human Override Justification` section in output artifact | 27 |
| 13 | FM-022-I7 | 48 | Add response trigger when MCP fallback rate exceeds 20% | 27 |
| 14 | FM-027-I7 | 48 | Add wave bypass expiry enforcement to Wave Progression AC | 27 |

**Estimated total post-correction RPN (all 14 findings addressed):** ~617 (from 1,356)
**Estimated RPN reduction if top-4 Major findings addressed:** 1,356 - (150-72) - (150-45) - (150-72) - (150-60) = 1,356 - 78 - 105 - 78 - 90 = 1,005

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | FM-014-I7 (crisis mode auto-detection unimplementable), FM-006-I7 (Synthesis Judgments minimum count missing), FM-026-I7 (unified report structure undefined), FM-027-I7 (bypass expiry not in AC) collectively leave 4 operational mechanisms underspecified |
| Internal Consistency | 0.20 | Negative | FM-028-I7 (R6-introduced inconsistency between Pre-Launch Validation and Post-Launch time-to-insight definitions) is a new dimension debit; the R6 fix that improved Actionability introduced this Consistency gap |
| Methodological Rigor | 0.20 | Negative | FM-003-I7 (JTBD pass threshold unstated), FM-013-I7 (MCP-heavy classification undefined) — two benchmark/routing mechanisms are defined by process but not evaluable without the missing thresholds |
| Evidence Quality | 0.15 | Negative | FM-016-I7 (HEART measurable signal undefined), FM-017-I7 (WSM C1>C2 rationale absent) — benchmark evaluation criteria and selection rationale lack the specificity needed for independent reproducibility |
| Actionability | 0.15 | Mixed | FM-002-I7 (MCP rate limits non-actionable) and FM-015-I7 (V2 trigger unmeasurable) remain; FM-006-I7 partial resolution on Synthesis Judgments is a positive step; FM-028-I7 resolution would improve actionability of Pre-Launch Validation |
| Traceability | 0.10 | Negative | FM-018-I7 (mermaid diagram legend missing), FM-008-I7 (Human Override storage location undefined) — two traceability gaps persist; both are single-sentence fixes |

---

## RPN Comparison Table

| Finding ID | I6 RPN | I7 RPN | Change | Reason |
|------------|--------|--------|--------|--------|
| FM-014 | 180 | 150 | -30 | Partial resolution: R6 added exit conditions but not auto-detection definition |
| FM-006 | 180 | 100 | -80 | Partial resolution: R6 added format but not minimum count or auto-downgrade |
| FM-028 | N/A | 150 | NEW | R6 RT-001 fix introduced Pre-Launch Validation / time-to-insight inconsistency |
| FM-002 | 150 | 150 | 0 | Unchanged — no R6 fix |
| FM-016 | 150 | 150 | 0 | Unchanged — no R6 fix |
| FM-003 | 125 | 125 | 0 | Unchanged — no R6 fix |
| FM-026 | 100 | 100 | 0 | Unchanged — no R6 fix |
| FM-013 | 80 | 80 | 0 | Unchanged — no R6 fix |
| FM-015 | 75 | 75 | 0 | Unchanged — no R6 fix |
| FM-017 | 60 | 60 | 0 | Unchanged — no R6 fix |
| FM-018 | 60 | 60 | 0 | Unchanged — no R6 fix |
| FM-008 | 60 | 60 | 0 | Unchanged — no R6 fix |
| FM-022 | 48 | 48 | 0 | Unchanged — no R6 fix |
| FM-027 | 48 | 48 | 0 | Unchanged — no R6 fix |

**I6 Total RPN (arithmetic):** 1,316 (13 findings)
**I7 Total RPN (arithmetic):** 1,356 (14 findings)
**Net change:** +40 points (+3.0%) — two partial resolutions (-110 points combined) offset by one new finding (+150 points)

---

## Execution Statistics
- **Total Findings:** 14
- **Critical:** 0
- **Major:** 8
- **Minor:** 6
- **Protocol Steps Completed:** 5 of 5
- **Elements Analyzed:** 15
- **Failure Mode Lenses Applied Per Element:** All 5 (Missing, Incorrect, Ambiguous, Inconsistent, Insufficient)

---

*Report Version: I7*
*Strategy: S-012 FMEA*
*Template: `.context/templates/adversarial/s-012-fmea.md` v1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Iteration: 7 (post-R6 revision)*
*Prior FMEA: `tournament-iter6/s-012-fmea.md`*
