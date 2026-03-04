# FMEA Report: /user-experience Skill GitHub Enhancement Issue (R7)

**Strategy:** S-012 FMEA (Failure Mode and Effects Analysis)
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-012, Iteration 8)
**H-16 Compliance:** S-003 Steelman applied in prior tournament sequence (confirmed)
**Elements Analyzed:** 15 | **Failure Modes Identified:** 17 | **Total RPN:** 1,541

---

## Summary

The R7 deliverable resolved one I7 finding (FM-028-I7, Pre-Launch Validation time-to-insight incoherence, RPN reduced from 150 to 30) but introduced three new Major findings that offset the gain. The ABANDON re-entry guard added by RT-001-I7 contains a wave-numbering off-by-one error: the guard says "BLOCK Wave N+1 routing" when it should block Wave N (the abandoned wave's sub-skills) — the current text guards the wrong wave boundary (FM-029-I8, RPN 125). The SOLO-VALIDATED status created by PM-001-I7 lacks any defined relationship to the BOOTSTRAP-VALIDATED 180-day deadline, leaving the SOLO-VALIDATED state potentially indefinite (FM-030-I8, RPN 100). The Haiku/T3 benchmark added by DA-001-I7 specifies "90% reliability" without defining how reliability is measured or where the escalation cost estimate artifact should be stored (FM-031-I8, RPN 80). Net R7 RPN effect: +185 (from 1,356 to 1,541). The 13 remaining I7 findings are unchanged — the seven longest-running findings (FM-002, FM-016, FM-003, FM-006, FM-026, FM-013, FM-015) have now persisted for 4-6 iterations each without remediation. Recommendation: **REVISE** — R7 made genuine progress (ABANDON guard is a valuable structural addition despite the off-by-one; the Haiku benchmark is a needed quality gate despite the ambiguity), but the three new defects require targeted single-sentence corrections before the wave progression and benchmark validation machinery is implementable.

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
| E-13 | Research Backing | Phase 1-3 artifacts, adversarial validation, WSM criteria inline, C1 sensitivity analysis |
| E-14 | Jerry Ecosystem Integration | Relationship diagram, integration table with 6 skills |
| E-15 | Directory Structure | 11 skill directories, ~72 artifacts (updated from ~67 by R7) |

---

## Findings Table

| ID | Element | Failure Mode | S | O | D | RPN | Severity | Corrective Action | Affected Dimension |
|----|---------|-------------|---|---|---|-----|----------|-------------------|--------------------|
| FM-014-I7 | E-06 | Crisis mode auto-detection "resolution" criterion still unimplementable: "multiple prior sub-skill invocations without resolution" has no computable definition of a "resolved" invocation (persistent from I5, 4 iterations unchanged) | 6 | 5 | 5 | 150 | Major | Add definition: "For automatic-detection, an invocation is resolved when: (a) user creates a worktracker entity from the output, (b) user provides verbal confirmation, or (c) user invokes a downstream sub-skill consuming this output. An invocation is unresolved if user re-invokes the same sub-skill within the same session without intervening acknowledgment. Crisis mode triggers after 2 consecutive unresolved invocations." | Completeness |
| FM-002-I7 | E-07 | MCP rate limits non-actionable: Figma (720 req/min) and Miro (100 req/min) documented but no per-invocation request estimate exists for the two highest-rate operations (persistent from I3, 6 iterations unchanged) | 6 | 5 | 5 | 150 | Major | Add estimated request counts below the MCP constraints table: "/ux-heuristic-eval Figma -- estimated 30-50 API calls per 10-heuristic evaluation; well within 720/min ceiling. /ux-design-sprint Miro -- estimated 20-40 calls per sprint day; 4-day sprint cumulative 120-200 calls; monitor against 100/min peak." | Actionability |
| FM-016-I7 | E-10 | HEART Wave 2 benchmark "measurable signal" undefined: AC requires "all 5 HEART dimensions with measurable signals" but any text string qualifies (persistent from I3, 6 iterations unchanged) | 5 | 6 | 5 | 150 | Major | Add definition: "A measurable signal requires at minimum: (a) metric name, (b) data source, (c) measurement method. Example: 'Daily Active Users (Engagement), measured via analytics platform, tracked weekly' qualifies; 'Users should be engaged' does not." | Evidence Quality |
| FM-003-I7 | E-10 | JTBD benchmark pass threshold ambiguous: 3-criterion rubric is well-defined but the AC does not state whether 3/3 criteria are required or 2/3 is actionable (persistent from I3, 6 iterations unchanged) | 5 | 5 | 5 | 125 | Major | Add explicit pass threshold: "3/3 criteria required. A job statement failing any single criterion cannot be validated against user behavior or used in a Design Sprint challenge statement." | Methodological Rigor |
| FM-029-I8 | E-08 | ABANDON re-entry guard "N+1" off-by-one: guard says "BLOCK Wave N+1 routing" but the abandoned wave is Wave N -- the guard should block re-entry to Wave N (the abandoned wave), not Wave N+1 (the next wave beyond the abandoned one) | 5 | 5 | 5 | 125 | Major | Change "BLOCK Wave N+1 routing" to "BLOCK Wave N routing (the abandoned wave's sub-skills remain inaccessible) until a documented blocker-resolution entry is logged." The text already states the abandoned sub-skills are "removed from routing until the blocker is resolved" -- the re-entry guard should reinforce Wave N access, not Wave N+1. | Completeness |
| FM-006-I7 | E-09 | Synthesis Judgments Summary partially resolved: R6 defined the 3-field format but did not add minimum entry count or auto-downgrade rule; an output with 1 entry claiming HIGH confidence still nominally passes the gate (persistent from I6, 3 iterations unchanged) | 5 | 4 | 5 | 100 | Major | Add: "Minimum 3 judgment call entries required for HIGH-confidence designation. Outputs with fewer than 3 identifiable AI judgment calls auto-downgrade to MEDIUM. Documented in synthesis-validation.md." | Completeness |
| FM-026-I7 | E-10 | Cross-framework synthesis AC defines "unified insight report" but specifies no minimum structure for convergent/divergent findings sections (persistent from I4, 5 iterations unchanged) | 4 | 5 | 5 | 100 | Major | Define minimum structure: "(a) Convergent findings: 1+ recommendations where 2+ sub-skills agree. (b) Divergent findings: conflicting recommendations with resolution guidance. (c) Portfolio gap: UX lifecycle stages not covered. Each section requires at least 1 entry or 'none identified' statement." | Completeness |
| FM-030-I8 | E-10 | SOLO-VALIDATED status has no defined expiry relative to the BOOTSTRAP-VALIDATED 180-day deadline: PM-001-I7 states "SOLO-VALIDATED status persists until peer review is completed" but does not specify whether SOLO-VALIDATED benchmarks are subject to the 180-day BOOTSTRAP-VALIDATED cross-validation window | 4 | 5 | 5 | 100 | Major | Add one sentence after the SOLO-VALIDATED definition: "SOLO-VALIDATED benchmarks are a subset of BOOTSTRAP-VALIDATED benchmarks and are subject to the same 180-day cross-validation deadline; if peer review is not completed within 180 days of Wave 1 launch, SOLO-VALIDATED transitions to UNVERIFIED-BENCHMARK status per the same rules." | Internal Consistency |
| FM-013-I7 | E-06 | "MCP-heavy team" routing classification undefined: flowchart has "MCP-heavy team?" decision node with no testable definition (persistent from I3, 6 iterations unchanged) | 4 | 5 | 4 | 80 | Major | Define as: "A team is MCP-heavy if 2+ Required MCPs are configured and active. Determined from KICKOFF-SIGNOFF.md field 'Available MCP Tools'. A Required MCP counts as configured if listed in .claude/settings.local.json and confirmed active during KICKOFF." | Methodological Rigor |
| FM-031-I8 | E-10 | Haiku benchmark "reliability" measurement method undefined: DA-001-I7 adds AC ">=90% reliability on Figma MCP OAuth + frame extraction across 3 reference design files" but does not define what constitutes 90% reliability or where the "revised cost estimate" artifact should be stored on escalation | 4 | 4 | 5 | 80 | Major | Add measurement protocol: "'90% reliability' means: >= 27 of 30 total frame extraction calls across 3 reference design files (10 calls per file) return complete, parseable frame data within 5 seconds. On benchmark failure, the 'revised cost estimate' is documented in a new row added to the Sub-Skill Model Selection table: '| sonnet | Heuristic Evaluation (fallback) | [Haiku benchmark failure reason + cost delta vs. haiku] |'" | Methodological Rigor |
| FM-015-I7 | E-12 | V2 trigger #3 (monthly AI UX pattern requests) cannot be measured: no request-tracking mechanism defined (persistent from I3, 6 iterations unchanged) | 3 | 5 | 5 | 75 | Minor | Add: "Monthly invocation counts tracked via worktracker log entries for /ux-ai-first-design routing attempts while Enabler incomplete." | Actionability |
| FM-017-I7 | E-13 | WSM C1 > C2 weighting justification absent: C1 (0.25) outweighs C2 (0.20) by 25% but the graduated-priority rationale does not explain why (persistent from I3, 6 iterations unchanged) | 3 | 4 | 5 | 60 | Minor | Add: "C1 outweighs C2 because a framework that cannot serve tiny teams fails the core use case even if perfectly composable as a Jerry skill. The defining requirement (C1) outweighs the implementation requirement (C2)." | Evidence Quality |
| FM-018-I7 | E-03 | Mermaid diagram orange fill for AI-First Design conditional has no legend entry within the diagram itself (persistent from I3, 6 iterations unchanged) | 3 | 5 | 4 | 60 | Minor | Add diagram caption below the mermaid block: "Orange fill = CONDITIONAL sub-skill (requires Enabler DONE status with verified WSM score >= 8.00 before Wave 5 deployment)." | Traceability |
| FM-008-I7 | E-09 | Human Override Justification storage location undefined: described as creating "an auditable evidence chain" but no storage location specified for the 3-field structured template entries (persistent from I3, 6 iterations unchanged) | 3 | 5 | 4 | 60 | Minor | Specify: "Human Override Justification stored as a block-quoted field in the sub-skill output artifact under a ## Human Override Justification heading. The 3-field template is appended to the artifact at the point of override." | Traceability |
| FM-028-I7 | E-10 | Pre-Launch Validation time-to-insight incoherence: RESOLVED by R7 (line 862 now reads "completeness and actionability"; line 913 now reads "Time-to-insight thresholds are enforced as post-launch operational metrics, not pre-launch evaluation criteria") | 5 | 2 | 3 | 30 | Minor | Resolution confirmed. Post-correction RPN reflects residual risk that future edits may re-introduce the three-dimension framing; no further action needed. | Internal Consistency |
| FM-022-I7 | E-10 | MCP fallback rate target (< 20%) lacks defined response when the target is exceeded (persistent from I4, 5 iterations unchanged) | 3 | 4 | 4 | 48 | Minor | Add: "If MCP fallback rate exceeds 20% for a Required MCP during the first 90 days, the named MCP maintenance owner investigates root cause within 2 weeks and reports findings to the V2 planning cycle." | Actionability |
| FM-027-I7 | E-10 | Wave bypass expiry described in E-08 but no expiry deadline enforced in the Wave Progression AC section (persistent from I4, 5 iterations unchanged) | 3 | 4 | 4 | 48 | Minor | Add to Wave Progression AC: "Wave bypass expires after 60 days or the next wave progression review (whichever is sooner). After expiry, the orchestrator displays an escalation warning before each subsequent sub-skill invocation, prompting the team to close the gap or formally ABANDON." | Completeness |

*Note: 17 active findings total (0 Critical, 10 Major, 7 Minor). FM-028-I7 resolved by R7 (RPN 150 to 30, reclassified Minor). Three new findings introduced by R7 additions: FM-029-I8 (ABANDON guard off-by-one), FM-030-I8 (SOLO-VALIDATED deadline gap), FM-031-I8 (Haiku benchmark reliability undefined). Net R7 RPN effect: +185 (resolved 150, introduced 305). 14 findings persistent across 3+ iterations without remediation.*

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

R6 added exit conditions (line 641): "Crisis mode exit: (a) all WARN conditions resolved to PASS, OR (b) blocker acknowledged with documented remediation plan, OR (c) ABANDON."

No definition of "resolved" vs. "unresolved" invocation exists anywhere in E-05, E-06, or E-10. R7 did not address this finding.

**Analysis:**
Persistent from Iter 5 — four iterations unchanged. The automatic-detection trigger "orchestrator detects multiple prior sub-skill invocations without resolution" requires a computable definition of resolution. The R6 exit conditions address the WARN-escalation pathway to crisis mode, not the automatic-detection pathway via unresolved invocations. These are two different entry mechanisms for crisis mode. Without a resolution signal definition, an implementer cannot write the automatic-detection logic. S=6 (automatic-detection path is entirely unimplementable), O=5 (ambiguity is inherent in the current text), D=5 (no resolution signal appears anywhere in the document). RPN: 6×5×5=150.

**Recommendation:**
Add to E-06 crisis mode paragraph immediately after "without resolution": "For automatic-detection purposes, an invocation is resolved when: (a) user creates a worktracker entity from the sub-skill output, (b) user provides verbal confirmation (e.g., 'acknowledged', 'got it', 'moving on'), or (c) user invokes a downstream sub-skill that consumes this sub-skill's output. An invocation is unresolved if the user re-invokes the same sub-skill within the same session without an intervening acknowledgment signal. Crisis mode automatic-detection triggers after 2 consecutive unresolved invocations of the same sub-skill."

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72

---

### FM-002-I7: MCP Rate Limits Non-Actionable Without Per-Operation Estimates

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-07 (MCP Integration) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-07 MCP constraints table (lines 593-599): Figma rate limit documented as "720 req/min per-user (Professional)" and Miro as "100 req/min per-user (Team plan)." No per-invocation request estimate exists for any operation. R7 did not address this finding.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. Rate limit documentation without per-invocation estimates is awareness-only, not actionable. An MCP runbook AC requires backoff strategy documentation, but a backoff strategy requires knowing approximately how many requests a typical invocation makes. This gap has remained across six iterations. S=6. O=5. D=5. RPN: 6×5×5=150.

**Recommendation:**
Add a "Per-Operation Request Estimates" note below the MCP constraints table: "`/ux-heuristic-eval` Figma evaluation -- estimated 30-50 API calls per 10-heuristic assessment (10 frame fetches + per-heuristic analysis calls); well within 720/min ceiling. `/ux-design-sprint` Miro -- estimated 20-40 calls per sprint day (board create, lane create, sticky create per exercise); cumulative 4-day sprint estimated 120-200 calls across 4 sessions; monitor against 100/min peak call rate during Day 2-3 intensive exercises. Mark as 'estimated; validate during Wave N implementation.'"

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72

---

### FM-016-I7: HEART Benchmark "Measurable Signal" Criterion Unverifiable

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-10 Wave 2 benchmark (line 837): "benchmark: populates all 5 HEART dimensions with measurable signals from a product description."

No definition of "measurable signal" appears in E-10, E-04, or E-09. Any generated text technically constitutes "signals." R7 did not address this finding.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. Without an operational definition, any text string satisfies the benchmark. A benchmark evaluator cannot distinguish "Daily Active Users, measured via analytics platform" (measurable) from "Users should be engaged" (not measurable). S=5. O=6. D=5. RPN: 5×6×5=150.

**Recommendation:**
Add immediately after "measurable signals from a product description" in line 837: "A measurable signal requires at minimum: (a) metric name, (b) data source, (c) measurement method. Text descriptions without a named data source do not qualify. Example: 'Daily Active Users (Engagement), measured via analytics platform, tracked weekly' qualifies; 'Users should be engaged' does not."

**Post-Correction RPN:** S=5, O=3, D=4 → RPN=60

---

### FM-003-I7: JTBD Benchmark Pass Threshold Ambiguous

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-10 Wave 1 benchmark (line 830): "3/3 criteria = actionable. No UX practitioner consultation required." The rubric defines three criteria but does not explicitly state whether 2/3 constitutes a passing "actionable" result or whether 3/3 is strictly required. R7 did not address this finding.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. The phrase "3/3 criteria = actionable" in the current text is the closest statement, but it is ambiguous — it defines what 3/3 means without explicitly stating that 2/3 is not actionable. The absence of an explicit "all-or-nothing" statement means different evaluators could apply different thresholds. S=5. O=5. D=5. RPN: 5×5×5=125.

**Recommendation:**
Append to line 830 after "3/3 criteria = actionable": "2/3 is not actionable — a job statement missing the functional+emotional/social dimension underspecifies user motivation; a feature- or technology-framed outcome cannot be validated against user behavior and must be rewritten before use in design decisions."

**Post-Correction RPN:** S=5, O=3, D=4 → RPN=60

---

### FM-029-I8: ABANDON Re-Entry Guard "N+1" Off-by-One Error

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-08 (Wave Deployment Model) |
| **Strategy Step** | Step 2: Failure mode lens — Incorrect |

**Evidence:**
E-08, ABANDON state (line 642): "Re-entry guard: After ABANDON, the orchestrator MUST consult `wave-progression.md` and BLOCK Wave N+1 routing until a documented blocker-resolution entry is logged."

Context: When a team ABANDONS Wave N, they revert to Wave N-1 sub-skills. The abandoned wave is Wave N. The purpose of the re-entry guard is to prevent immediate re-entry to the abandoned Wave N without documented blocker resolution.

**Analysis:**
The R7 re-entry guard addresses the correct architectural concern (preventing immediate ABANDON-then-re-enter cycles) but references the wrong wave boundary. "BLOCK Wave N+1" blocks the wave AFTER the abandoned wave. This means: a team that abandons Wave 3 would have Wave 4 blocked by the re-entry guard (correct — can't skip ahead), but Wave 3 (the abandoned wave) would not be guarded — the team could immediately re-enter Wave 3 without logging a blocker resolution. The guard protects the wrong boundary. The preceding sentence already states the abandoned sub-skills are "removed from routing until the blocker is resolved" but the re-entry guard using "N+1" creates inconsistency with this statement. S=5 (the guard protects the wrong wave boundary, making ABANDON immediately reversible without blocker documentation), O=5 (the off-by-one is in the literal text), D=5 (the mismatch requires cross-reading two adjacent sentences to detect). RPN: 5×5×5=125.

**Recommendation:**
Change "BLOCK Wave N+1 routing" to "BLOCK Wave N routing (the abandoned wave's sub-skills remain inaccessible)" in line 642. Full corrected sentence: "Re-entry guard: After ABANDON, the orchestrator MUST consult `wave-progression.md` and BLOCK Wave N routing (the abandoned wave's sub-skills remain inaccessible) until a documented blocker-resolution entry is logged. The blocker-resolution entry must describe what changed and reference specific evidence."

**Post-Correction RPN:** S=5, O=2, D=3 → RPN=30

---

### FM-006-I7: Synthesis Judgments Summary Minimum Entry Count Absent

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-09 (Synthesis Hypothesis Validation) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-09 (line 680): HIGH confidence gate now specifies "Synthesis Judgments Summary format: 3 fields per judgment -- (a) AI-generated claim (verbatim from sub-skill output), (b) Evidence basis (source sub-skill, confidence level, data points cited), (c) Confidence qualifier (HIGH/MEDIUM/LOW with rationale)."

No minimum number of entries per summary is defined. An output with 1 AI judgment call can still be designated HIGH confidence. R7 did not address this finding.

**Analysis:**
Persistent from Iter 6 — three iterations unchanged. The 3-field format is well-specified. The missing element is the minimum entry count. A Synthesis Judgments Summary with a single entry provides less oversight than the architecture intends — a HIGH-confidence designation should require exhaustive enumeration of judgment calls, not a single acknowledgment. S=5. O=4. D=5. RPN: 5×4×5=100.

**Recommendation:**
Add to the HIGH-confidence gate cell: "Minimum 3 judgment call entries required for HIGH-confidence designation. Outputs with fewer than 3 identifiable AI judgment calls auto-downgrade to MEDIUM confidence. The minimum entry count and auto-downgrade rule are formally specified in `synthesis-validation.md`."

**Post-Correction RPN:** S=5, O=3, D=4 → RPN=60

---

### FM-026-I7: Cross-Framework Synthesis AC Lacks Minimum Report Structure

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-10, Parent Orchestrator AC (line 809): "The `/user-experience` parent skill produces a unified insight report combining findings from 2+ sub-skill analyses on the same product, identifying convergent and divergent recommendations across frameworks."

No minimum structure for the convergent/divergent sections is defined. R7 did not address this finding.

**Analysis:**
Persistent from Iter 4 — five iterations unchanged. "Identifying convergent and divergent recommendations" is not a verifiable criterion without minimum structure. An evaluator cannot determine whether a given report satisfies the AC without knowing what constitutes an adequate convergent or divergent findings section. S=4. O=5. D=5. RPN: 4×5×5=100.

**Recommendation:**
Append to line 809: "Minimum unified insight report structure: (a) Convergent findings section: 1+ recommendations where 2+ sub-skills agree on the same product area. (b) Divergent findings section: 1+ conflicting recommendations with explicit resolution guidance. (c) Portfolio gap section: UX lifecycle stages not covered by currently activated sub-skills. Each section requires at least 1 entry or an explicit 'none identified' statement to confirm the analysis was performed."

**Post-Correction RPN:** S=4, O=3, D=4 → RPN=48

---

### FM-030-I8: SOLO-VALIDATED Status Has No Defined Deadline

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria — Pre-Launch Validation) |
| **Strategy Step** | Step 2: Failure mode lens — Inconsistent |

**Evidence:**
E-10, Pre-Launch Validation (line 862): "BOOTSTRAP-VALIDATED: Wave 1 evaluations using the fallback qualification path are tagged BOOTSTRAP-VALIDATED and are NOT equivalent to fully-verified quality benchmarks. Post-launch cross-validation REQUIRED: if no criterion-(a) evaluator completes cross-validation within 180 days of Wave 1 launch, BOOTSTRAP-VALIDATED benchmarks transition to UNVERIFIED-BENCHMARK status."

Same paragraph, R7 addition: "SOLO-VALIDATED status persists until peer review is completed (it does not auto-pass on timeout)."

The relationship between SOLO-VALIDATED and BOOTSTRAP-VALIDATED is undefined. It is unclear whether SOLO-VALIDATED benchmarks are subject to the 180-day cross-validation deadline.

**Analysis:**
The R7 fix removes the 30-day auto-stand provision for SOLO-VALIDATED (a genuine improvement), but creates a new ambiguity: if SOLO-VALIDATED benchmarks do not have a deadline, they could persist indefinitely without transitioning to UNVERIFIED-BENCHMARK, potentially allowing sub-skills to operate under unverified quality baselines beyond the 180-day BOOTSTRAP-VALIDATED window. The text does not explicitly state whether SOLO-VALIDATED is a type of BOOTSTRAP-VALIDATED or an independent state. If independent, it has no deadline. If a subtype, it inherits the 180-day window — but this is not stated. S=4 (creates a state machine gap where solo-evaluated benchmarks have no defined transition to UNVERIFIED-BENCHMARK), O=5 (structural gap in the current text), D=5 (requires reading two adjacent paragraphs and inferring the relationship). RPN: 4×5×5=100.

**Recommendation:**
Add one sentence immediately after "SOLO-VALIDATED status persists until peer review is completed": "SOLO-VALIDATED benchmarks are a subset of BOOTSTRAP-VALIDATED benchmarks and are subject to the same 180-day cross-validation deadline; if peer review is not completed within 180 days of Wave 1 launch, SOLO-VALIDATED transitions to UNVERIFIED-BENCHMARK status with the same L0 output flag."

**Post-Correction RPN:** S=4, O=2, D=3 → RPN=24

---

### FM-013-I7: "MCP-Heavy Team" Routing Classification Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-06 (Routing Triage Logic) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-06, routing flowchart (lines 441-477): Flowchart has a "MCP-heavy team?" decision node that routes to "Apply MCP-heavy variant recommendations." No testable definition of "MCP-heavy" appears in E-05, E-06, or E-10. R7 did not address this finding.

**Analysis:**
Persistent from Iter 3 — six iterations unchanged. The flowchart is non-implementable at this node without a definition. Any routing logic must evaluate a boolean condition; "MCP-heavy team" is a qualitative judgment without a computable threshold. S=4. O=5. D=4. RPN: 4×5×4=80.

**Recommendation:**
Add definition after the "MCP-heavy team" mention in E-06: "A team is classified as MCP-heavy if they have 2+ Required MCPs configured and active at session start. The orchestrator determines MCP-heavy status from the 'Available MCP Tools' field in `KICKOFF-SIGNOFF.md`. A Required MCP counts as configured if the corresponding MCP server is listed in `.claude/settings.local.json` and the team confirmed activation during KICKOFF."

**Post-Correction RPN:** S=4, O=3, D=3 → RPN=36

---

### FM-031-I8: Haiku Benchmark "Reliability" Measurement Method Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria — Wave 1 Sub-Skills) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-10, Wave 1 sub-skills (line 822): "Heuristic Evaluation Haiku/Figma pre-launch benchmark: >= 90% reliability on Figma MCP OAuth + frame extraction across 3 reference design files (escalate to Sonnet with revised cost estimate if fail) [R7-fix: DA-001-I7]"

E-15, Sub-Skill Model Selection (line 1235): "Pre-launch model capability benchmark REQUIRED: Haiku confirmed to achieve >= 90% reliability on Figma MCP OAuth + frame extraction across 3 reference design files. If benchmark fails, escalate to Sonnet with revised cost estimate and documented justification per AD-M-009."

"Reliability" is not defined. "Revised cost estimate" has no artifact location.

**Analysis:**
The Haiku/T3 benchmark is a valuable quality gate (it prevents deploying an under-capable model for a critical integration path), but it cannot be executed without knowing how reliability is measured. Possible interpretations: (a) 90% of individual API calls succeed, (b) 9 of 10 complete frame extractions produce parseable output, (c) 9 of 10 evaluation runs produce a findable heuristic violation in a test design, (d) extraction completes within a time threshold 90% of the time. These interpretations yield different benchmark pass/fail outcomes. Additionally, "revised cost estimate" is a dangling reference — on escalation to Sonnet, the document requires a "revised cost estimate and documented justification" but does not specify where this artifact should be created. S=4 (benchmark is unverifiable without a measurement protocol), O=4 (two fields require specification, increasing probability of evaluator confusion), D=5 (the paragraph appears complete and specific on the surface). RPN: 4×4×5=80.

**Recommendation:**
Replace ">=90% reliability on Figma MCP OAuth + frame extraction across 3 reference design files" with: ">= 90% reliability defined as: >= 27 of 30 total frame extraction calls (10 calls per reference design file, 3 files) return complete, parseable frame data within 5 seconds. On benchmark failure, the revised cost estimate is documented in a new Sub-Skill Model Selection table row: '| sonnet | Heuristic Evaluation (fallback) | Haiku benchmark failed: [failure description]. Sonnet cost delta: [estimated cost increase per invocation vs. haiku]. Justification per AD-M-009. |'"

**Post-Correction RPN:** S=4, O=2, D=3 → RPN=24

---

## Recommendations

### Major Findings (Corrective Actions Required)

| ID | Corrective Action | Acceptance Criteria | Estimated RPN Reduction |
|----|------------------|--------------------|-----------------------|
| FM-029-I8 | Change "BLOCK Wave N+1 routing" to "BLOCK Wave N routing" in ABANDON re-entry guard (line 642) | Guard correctly references Wave N (abandoned wave), not Wave N+1. Re-entry to the abandoned wave requires blocker-resolution entry. | 125 → 30 (-95) |
| FM-014-I7 | Add resolution signal definition to crisis mode auto-detection (line 431) | Three computable resolution signals defined; 2-consecutive-unresolved trigger specified | 150 → 72 (-78) |
| FM-002-I7 | Add per-operation request estimates below MCP constraints table | /ux-heuristic-eval (~30-50 calls) and /ux-design-sprint (~20-40/day) estimates present with "estimated; validate during implementation" qualifier | 150 → 72 (-78) |
| FM-016-I7 | Add "measurable signal" definition after Wave 2 HEART benchmark (line 837) | Three-field definition (metric name, data source, measurement method) with passing/failing examples | 150 → 60 (-90) |
| FM-003-I7 | Add explicit "2/3 is not actionable" statement to JTBD benchmark (line 830) | Pass threshold unambiguous: 3/3 criteria required; consequences of 2/3 stated | 125 → 60 (-65) |
| FM-030-I8 | Add SOLO-VALIDATED deadline cross-reference to BOOTSTRAP-VALIDATED 180-day window (line 862) | SOLO-VALIDATED explicitly identified as BOOTSTRAP-VALIDATED subtype subject to 180-day deadline | 100 → 24 (-76) |
| FM-006-I7 | Add minimum entry count (3) and auto-downgrade rule to HIGH confidence gate (E-09) | Minimum 3 entries for HIGH confidence; outputs with < 3 AI judgment calls auto-downgrade to MEDIUM | 100 → 60 (-40) |
| FM-026-I7 | Define minimum structure for unified insight report (line 809) | Three required sections (convergent, divergent, portfolio gap) each with minimum 1 entry or "none identified" | 100 → 48 (-52) |
| FM-013-I7 | Add testable "MCP-heavy team" definition to E-06 routing flowchart | 2+ Required MCPs configured and active = MCP-heavy; KICKOFF-SIGNOFF.md field as source | 80 → 36 (-44) |
| FM-031-I8 | Define "reliability" measurement protocol for Haiku benchmark (lines 822, 1235) | 30 test calls / 3 files / >=27 pass within 5 seconds = 90% reliability; escalation artifact location specified | 80 → 24 (-56) |

**Estimated RPN reduction if all Major findings addressed:** 1,360 → 486 (estimated post-correction sum, excluding Minors)

### Minor Findings (Improvement Opportunities)

| ID | Corrective Action | Estimated RPN Reduction |
|----|------------------|------------------------|
| FM-028-I7 | RESOLVED (confirmed, no action needed) | Already at 30 |
| FM-015-I7 | Add worktracker-based tracking mechanism for V2 trigger #3 | 75 → 25 |
| FM-017-I7 | Add one-sentence C1 > C2 weighting rationale to WSM section | 60 → 20 |
| FM-018-I7 | Add mermaid diagram caption explaining orange fill = CONDITIONAL | 60 → 15 |
| FM-008-I7 | Specify Human Override Justification storage location in E-09 | 60 → 20 |
| FM-022-I7 | Define response procedure when MCP fallback rate exceeds 20% target | 48 → 16 |
| FM-027-I7 | Add 60-day bypass expiry with escalation behavior to Wave Progression AC | 48 → 16 |

---

## Scoring Impact

Map FMEA findings to S-014 scoring dimensions (weights from quality-enforcement.md SSOT):

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | FM-014-I7 (crisis mode resolution gap), FM-006-I7 (Synthesis Judgments minimum entry), FM-026-I7 (synthesis report structure), FM-029-I8 (ABANDON guard wrong boundary), FM-027-I7 (bypass expiry). Five findings represent omitted completeness in the wave enforcement, synthesis validation, and routing specifications. |
| Internal Consistency | 0.20 | Negative | FM-030-I8 (SOLO-VALIDATED vs. BOOTSTRAP-VALIDATED deadline inconsistency). FM-028-I7 resolved the prior time-to-insight inconsistency. One active Major + one resolved — net: partially resolved but active inconsistency remains. |
| Methodological Rigor | 0.20 | Negative | FM-003-I7 (JTBD pass threshold ambiguous), FM-013-I7 (MCP-heavy team undefined), FM-031-I8 (Haiku reliability unmeasured). Three unimplementable methodology elements. |
| Evidence Quality | 0.15 | Negative | FM-016-I7 (HEART "measurable signal" undefined), FM-017-I7 (WSM weighting justification absent), FM-002-I7 (MCP rate limits without per-operation context). Evidence claims are present but not operationally grounded. |
| Actionability | 0.15 | Negative | FM-002-I7 (rate limits non-actionable without estimates), FM-015-I7 (V2 trigger unmeasurable), FM-022-I7 (MCP fallback rate response undefined). Three findings make specified targets unactionable without additional specification. |
| Traceability | 0.10 | Negative | FM-018-I7 (diagram legend absent), FM-008-I7 (Human Override storage undefined). Two findings reduce traceability of key validation artifacts. |

**Overall Assessment:** The R7 deliverable requires targeted corrections before the wave enforcement and benchmark validation machinery are implementable. The ABANDON re-entry guard, Haiku benchmark, and SOLO-VALIDATED deadline gap are all introduced by R7's own additions, making them the most urgent corrections — they represent regressions from an otherwise valuable revision. The six longest-running findings (FM-002, FM-016, FM-003, FM-013, FM-015, FM-006) have now accumulated across 4-6 iterations each; their persistence suggests they are systematically overlooked during revision rather than considered and rejected. A targeted revision checklist for R8 should prioritize the three R7-introduced defects plus at least two of the oldest persistent Major findings.

---

## Execution Statistics

- **Total Findings:** 17
- **Critical:** 0
- **Major:** 10
- **Minor:** 7
- **Protocol Steps Completed:** 5 of 5
- **Total RPN:** 1,541
- **I7 Total RPN:** 1,356
- **Net R7 RPN Change:** +185 (1 finding resolved: -150 to +30; 3 new findings introduced: +305)
- **Findings Resolved by R7:** 1 (FM-028-I7, reclassified Minor at RPN 30)
- **New Findings Introduced by R7:** 3 (FM-029-I8, FM-030-I8, FM-031-I8)
- **Findings Unchanged from I7:** 13
