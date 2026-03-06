# FMEA Report: /user-experience Skill GitHub Enhancement Issue (R3)

**Strategy:** S-012 FMEA (Failure Mode and Effects Analysis)
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-012, Iteration 4)
**H-16 Compliance:** S-003 Steelman applied in prior tournament sequence (confirmed)
**Elements Analyzed:** 15 | **Failure Modes Identified:** 20 | **Total RPN:** 1,058

---

## Summary

The R3 deliverable shows significant improvement over R2. FM-001-I3 (wave enforcement 3-state behavior) is fully resolved — PASS/WARN/BLOCK states are now explicitly defined with clear behavioral rules. FM-010-I3 (HEART synthesis hypothesis warning) is resolved. Multiple minor fixes are addressed (SR-008-I3 adds `kickoff-signoff-template.md` to directory structure, PM-001-I3 elevates MCP runbook to AC, RT-001-I3 defines blind evaluation rubric). The four Iter 3 Critical findings now reduce to two Criticals: FM-004-I4 (cross-sub-skill handoff schema) remains as R3 defined the parent-to-sub-skill handoff but left the sub-skill-to-sub-skill schema undefined, and FM-009-I4 (Zeroheight/Whimsical deferred constraints) persists unchanged. Seven Major findings remain from Iter 3 with varying degrees of progress. Three new failure modes emerge from R3 changes. Total RPN declined from 1,732 to 1,058 (39% reduction). Recommendation: **REVISE** — two Critical and seven Major findings require targeted correction before PASS.

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
| E-08 | Wave Deployment Model | 5 waves, entry criteria, WAVE-N-SIGNOFF enforcement, 3-state behavior, bypass mechanism |
| E-09 | Synthesis Hypothesis Validation | 3-tier confidence gates (HIGH/MEDIUM/LOW), automation bias risk, Human Override Justification |
| E-10 | Acceptance Criteria | Parent, Wave 1, Wave 2-5, synthesis, MCP, pre-launch, quality, wave progression, post-launch |
| E-11 | Known Limitations | User research gap, AI-First conditional, ethics gaps, Figma SPOF, context window, scope creep |
| E-12 | V2 Roadmap | V2 candidates, V2 trigger conditions, architecture evolution path |
| E-13 | Research Backing | Phase 1-3 artifacts, adversarial validation, WSM criteria inline |
| E-14 | Jerry Ecosystem Integration | Relationship diagram, integration table with 6 skills |
| E-15 | Directory Structure | 11 skill directories, ~67 artifacts |

---

## Findings Table

| ID | Element | Failure Mode | S | O | D | RPN | Severity | Corrective Action | Affected Dimension |
|----|---------|-------------|---|---|---|-----|----------|-------------------|--------------------|
| FM-004-I4 | E-04, E-10, E-14 | Cross-sub-skill handoff schema still undefined: R3 defined parent-to-sub-skill handoff (product context, sub-skill, prior outputs, quality threshold) but the sub-skill-to-sub-skill schema (JTBD→Sprint, Lean UX→HEART output format) remains unspecified | 7 | 6 | 6 | 252 | Critical | Define the sub-skill-to-sub-skill handoff schema separately from the parent-to-sub-skill schema: minimum fields for downstream consumption (upstream_artifact path, downstream_input_field_mapping, confidence_level, validation_checkpoint). Add to `ux-routing-rules.md` scope and add AC: "Cross-sub-skill handoff schema defined; downstream sub-skill populates its input from upstream artifact without manual reformatting." | Completeness |
| FM-009-I4 | E-07 | Zeroheight (Wave 3) and Whimsical (Wave 5) MCP operational constraints remain "Populated during Wave N implementation" with no interim commitment binding wave kickoff | 7 | 7 | 5 | 245 | Critical | Convert "Populated during Wave N" to a pre-commitment: "Auth method known (API key per docs); rate limits TBD — MUST be verified and committed before Wave N development kickoff. Failure to commit blocks Wave N KICKOFF-SIGNOFF." This makes the deferral a tracked obligation, not a silent placeholder. | Methodological Rigor |
| FM-006-I4 | E-09 | Synthesis Judgments Summary format still undefined: HIGH-confidence gate requires "enumerated acknowledgment of AI judgment calls via a Synthesis Judgments Summary" but no format is specified for what constitutes an entry | 6 | 6 | 5 | 180 | Major | Define the Synthesis Judgments Summary format in `synthesis-validation.md` scope: each entry contains (a) the AI claim, (b) the evidence basis (e.g., "secondary research — no user interview data"), (c) the confidence qualifier. Minimum 3 entries required for a HIGH-confidence output; fewer than 3 AI judgment calls downgrades output to MEDIUM. | Completeness |
| FM-014-I4 | E-06 | Crisis mode "resolution" definition (R3 fix not applied): The crisis mode circuit breaker trigger "multiple prior sub-skill invocations without resolution" still does not define what counts as resolved vs. unresolved | 6 | 5 | 6 | 180 | Major | Add to crisis mode description in E-06: "An invocation is resolved when: (a) user creates a worktracker entity from the output, (b) user provides verbal confirmation, or (c) user invokes a downstream sub-skill consuming this output. An invocation is unresolved if the user re-invokes the same sub-skill within the same session without intervening acknowledgment. Crisis mode triggers after 2 unresolved invocations." | Completeness |
| FM-002-I4 | E-07 | MCP rate limits non-actionable without per-operation request budgets: Figma (720 req/min) and Miro (100 req/min) documented but no per-invocation request estimate exists for the two highest-rate operations | 6 | 5 | 5 | 150 | Major | Add "Estimated Requests/Invocation" note to MCP constraints table for the two highest-rate operations: `/ux-heuristic-eval` (estimated Figma API calls per 10-heuristic evaluation) and `/ux-design-sprint` (estimated Miro calls per sprint day). Mark as "estimated; validate during Wave 1 implementation." | Actionability |
| FM-003-I4 | E-10 | JTBD benchmark pass threshold ambiguous: 3-criterion rubric is well-defined but does not state whether 3/3 is required or 2/3 is actionable — creates inconsistent acceptance testing | 5 | 5 | 5 | 125 | Major | Add explicit pass threshold statement: "3/3 criteria required. Rationale: all three are necessary conditions — a job statement missing the functional+emotional/social dimension underspecifies user motivation; a feature- or technology-framed outcome cannot be validated against user behavior." | Methodological Rigor |
| FM-016-I4 | E-10 | "Measurable signal" for HEART Wave 2 benchmark undefined: AC requires "all 5 HEART dimensions with measurable signals" but any text in the field could be claimed as a signal | 5 | 6 | 5 | 150 | Major | Add: "A measurable signal requires at minimum: (a) metric name, (b) data source, (c) measurement method (e.g., 'daily active users from Mixpanel, measured weekly'). Text descriptions without a named data source do not qualify." | Evidence Quality |
| FM-011-I4 | E-04 | "Expert review" qualification undefined for MEDIUM-confidence behavior-design outputs: synthesis hypothesis warning requires "expert review OR validation against 2-3 real user data points" but "expert" has no defined qualification | 4 | 5 | 5 | 100 | Major | Define "expert review": "A person with demonstrated UX research or behavioral design experience — professional UX practitioner, published UX academic, or product leader with documented UX background. AI cannot serve as the expert reviewer for MEDIUM-confidence outputs." | Completeness |
| FM-013-I4 | E-06 | "MCP-heavy team" routing classification undefined: The flowchart has an "MCP-heavy team?" decision node with no testable definition | 4 | 5 | 5 | 100 | Major | Define as: "A team is MCP-heavy if they have 2+ Required MCPs configured and active. The orchestrator determines this from `KICKOFF-SIGNOFF.md` field 'Available MCP Tools'." | Methodological Rigor |
| FM-025-I4 | E-10 | Pre-launch validation AC now specifies a 3-evaluator blind rubric (R3 fix) but does not define how the 3 independent evaluators are recruited, qualified, or tracked — self-selection by the implementing team could undermine the blind evaluation | 5 | 5 | 4 | 100 | Major | Add evaluator recruitment and qualification criteria: "Independent evaluators must not have contributed to the sub-skill design. Evaluation assignments are recorded in the pre-launch validation log (artifact name, evaluator ID or role, evaluation date). A single evaluator who is also the implementing team member does not satisfy the 3-evaluator requirement even if the team is small." | Evidence Quality |
| FM-015-I4 | E-12 | V2 trigger #3 (monthly AI UX pattern requests) cannot be measured by V1 architecture: no request-tracking mechanism is defined for counting invocations | 3 | 5 | 5 | 75 | Minor | Add: "Monthly invocation counts tracked via worktracker log entries (each sub-skill invocation creates a worktracker entry). V2 trigger threshold measured against worktracker entry counts." | Actionability |
| FM-017-I4 | E-13 | WSM C1 > C2 weighting justification absent: graduated-priority rationale does not explain why C1 (0.25) outweighs C2 (0.20) by 25% | 3 | 4 | 5 | 60 | Minor | Add: "C1 (0.25) is weighted above C2 (0.20) because a framework that cannot serve tiny teams fails the fundamental use case even if perfectly composable as a Jerry skill. C2 receives the second-highest weight because non-composable frameworks cannot be delivered." | Evidence Quality |
| FM-018-I4 | E-03 | Mermaid diagram orange fill for AI-First Design conditional has no legend in the diagram | 3 | 5 | 4 | 60 | Minor | Add caption below diagram: "Orange fill = CONDITIONAL sub-skill (requires Enabler DONE status before Wave 5 deployment)." | Traceability |
| FM-008-I4 | E-09 | Human Override Justification storage mechanism undefined: described as "auditable paper trail" but no storage location specified (output file? worktracker entry?) | 3 | 5 | 4 | 60 | Minor | Specify: "Human Override Justification is stored as a block-quoted field in the sub-skill output artifact under `## Human Override Justification` heading. The worktracker entry for the invocation links to this section." | Traceability |
| FM-012-I4 | E-14 | 4-skill canonical sequence (JTBD→Sprint→Lean UX→HEART) shown in integration diagram but only 2 two-skill handoffs tested in V1 ACs — the gap is implicit, not explicitly scoped to V2 | 3 | 4 | 4 | 48 | Minor | Add AC note: "The full 4-skill canonical sequence (JTBD→Sprint→Lean UX→HEART) is a V2 integration test. V1 validates the 2 two-skill handoffs that compose it (JTBD→Sprint, Lean UX→HEART) as the sufficient V1 scope." | Completeness |
| FM-022-I4 | E-10 | MCP fallback rate target (< 20%) lacks a defined response when the target is exceeded | 3 | 4 | 4 | 48 | Minor | Add: "If MCP fallback rate exceeds 20% for a Required MCP during the first 90 days, the integration is flagged for review in the next V2 planning cycle." | Actionability |
| FM-020-I4 | E-07 | MCP maintenance owner ownership mechanism undefined: quarterly audit cadence references a "named MCP maintenance owner" but no mechanism assigns this person or ties them to a tracking artifact | 3 | 4 | 4 | 48 | Minor | Add: "MCP maintenance owner is a named field in `kickoff-signoff-template.md`. The quarterly audit is tied to this owner." Reference `kickoff-signoff-template.md` (now present in E-15 per R3 fix). | Actionability |
| FM-026-I4 | E-10 | Cross-framework synthesis AC (R3-fix: SR-002-I3) defines a "unified insight report" requirement but does not specify the minimum structure of the report — what sections are required, what "convergent and divergent recommendations" means operationally | 4 | 5 | 5 | 100 | Major | Define the minimum structure for the unified insight report: "(a) Convergent findings: recommendations where 2+ sub-skills agree. (b) Divergent findings: recommendations where sub-skills conflict, with explicit resolution guidance. (c) Portfolio gap: UX lifecycle gaps not covered by the invoked sub-skills. Each section must have at least 1 entry or an explicit 'none identified' statement." | Completeness |
| FM-027-I4 | E-10 | Wave bypass expiry mechanism still absent from Wave Progression AC: E-08 describes bypass but the AC section does not enforce or test expiry behavior | 3 | 4 | 4 | 48 | Minor | Add to Wave Progression AC: "Wave bypass expires after 60 days or next wave progression review (whichever is sooner). If remediation target date passes without closure, orchestrator displays escalation warning before each subsequent sub-skill invocation." | Completeness |
| FM-024-I4 | E-02 | Population segments table still missing a part-time contractor UX segment | 2 | 3 | 4 | 24 | Minor | Add: "Part-time contractor UX (2-5 team + 10-20 hrs/week contractor UX): HIGH fit for discovery and evaluation frameworks; contractor handles judgment-intensive steps; AI handles synthesis and structured evaluation." | Completeness |

---

## Detailed Findings

### FM-004-I4: Cross-Sub-Skill Handoff Schema Still Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Element** | E-04 (Sub-Skill Descriptions), E-10 (Acceptance Criteria), E-14 (Jerry Ecosystem Integration) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
R3 added to E-10 AC (line 792): "Parent-to-sub-skill handoff includes: product context (name, domain, target users), selected sub-skill, prior sub-skill outputs (if any), and quality gate threshold."

E-04: Each sub-skill lists "Key Output" but no field defines the structured format that downstream sub-skills consume as input. No sub-skill-to-sub-skill schema exists.

E-10 AC: "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)" — present from R2, unchanged in R3.

**Analysis:**
R3 correctly defined the parent-to-sub-skill handoff (what the orchestrator passes when it invokes a sub-skill). However, the original finding was about the cross-sub-skill handoff: when `ux-jtbd-analyst` produces a job statement, what structured format does `ux-sprint-facilitator` expect as its challenge statement input? These are distinct schemas serving different handoff directions. The parent-to-sub-skill handoff tells the sub-skill what context to operate in; the sub-skill-to-sub-skill handoff tells the downstream sub-skill what to consume as primary input. The AC still tests only invocation completion ("cross-framework integration handoffs tested") without verifying data contract compliance. Iter 3 identified this as FM-004-I3 (RPN 294); R3 fixed the parent direction but left the sub-skill direction unaddressed.

**Recommendation:**
Add to `ux-routing-rules.md` scope in E-15: "Includes cross-sub-skill handoff schema (minimum fields: upstream_artifact path, downstream_input_field_mapping, confidence_level, validation_checkpoint)."

Add to E-10 cross-framework integration AC: "Handoff schema validated — downstream sub-skill successfully populates its challenge statement/hypothesis input from upstream artifact without manual reformatting by the user. Validation demonstrated by running the canonical sequence end-to-end with a reference product scenario."

**Post-Correction RPN:** S=7, O=3, D=4 → RPN=84

---

### FM-009-I4: Zeroheight and Whimsical Operational Constraints Deferred Without Commitment

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Element** | E-07 (MCP Integration) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-07 MCP Operational Constraints table (lines 588, 590):
- Zeroheight: "Populated during Wave 3 implementation" in rate limits, auth method, API version, and failure codes.
- Whimsical: "Populated during Wave 5 implementation" in rate limits, auth method, and API version.

E-07 table note (line 592): "Rows marked 'Populated during Wave N implementation' will be completed when the sub-skills requiring that MCP server enter active development."

**Analysis:**
This finding is identical to FM-009-I3 — R3 made no change to the Zeroheight or Whimsical rows. The table note now makes the deferral policy explicit ("will be completed when sub-skills enter active development"), but this actually reduces detection efficacy: the deferral is now documented as intentional policy rather than an oversight, making it less likely to be caught during review. Severity unchanged at 7; Occurrence remains 7 because deferred constraints are now normalized via the note; Detection improves slightly from 5 to 5 (no change — the note makes the deferral visible but does not prevent the gap).

**Recommendation:**
Convert deferred rows to commitment language: "Zeroheight: Auth method = API key (per product documentation). Rate limits, API version, failure codes: TBD — MUST be committed to this table before Wave 3 KICKOFF-SIGNOFF. Wave 3 kickoff is blocked until this row is complete." Apply same pattern for Whimsical with Wave 5 reference.

**Post-Correction RPN:** S=7, O=3, D=3 → RPN=63

---

### FM-006-I4: Synthesis Judgments Summary Format Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-09 (Synthesis Hypothesis Validation) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-09: "HIGH confidence gate: User reviews output and acknowledges specific AI judgment calls via a Synthesis Judgments Summary."

No format definition exists in E-09 or in the synthesis-validation.md scope entry in E-15.

**Analysis:**
Persistent from Iter 3 (FM-006-I3, RPN 180). R3 made no change to the Synthesis Judgments Summary. The HIGH-confidence gate's effectiveness depends entirely on users understanding what they are acknowledging. Without a defined format (what is an "AI judgment call"? what information must each entry contain?), implementers will generate inconsistent summaries and users will perform nominal acknowledgment rather than substantive review. The automation bias mitigation mechanism is theoretically defined but practically unenforceable.

**Recommendation:**
Define in `synthesis-validation.md` scope: Synthesis Judgments Summary format — each entry contains: (a) the specific AI claim ("Job statement: 'When onboarding new customers...'"), (b) the evidence basis ("Generated from secondary research — no user interview data"), (c) the confidence qualifier ("MEDIUM; requires validation against 2-3 user interviews"). Minimum 3 entries required for HIGH-confidence output; fewer than 3 AI judgment calls downgrades the output to MEDIUM automatically.

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72

---

### FM-014-I4: Crisis Mode "Resolution" Undefined for Circuit Breaker

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-06 (Routing Triage Logic) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-06 (line 421): "Crisis mode activates when the user explicitly describes urgency... or when the orchestrator detects multiple prior sub-skill invocations without resolution."

No definition of "resolution" exists in E-06 or E-10.

**Analysis:**
Persistent from Iter 3 (FM-014-I3, RPN 180). R3 made no change to the crisis mode resolution definition. The orchestrator circuit breaker trigger ("multiple prior sub-skill invocations without resolution") has no computable criterion. An orchestrator implementation cannot evaluate "resolved vs. unresolved" without a testable definition. This is not a quality nit — it is a blocking implementation gap for the crisis mode feature.

**Recommendation:**
Add to E-06: "An invocation is resolved when: (a) user creates a worktracker entity from the output, (b) user provides verbal confirmation ('got it', 'moving on'), or (c) user invokes a downstream sub-skill consuming this output. An invocation is unresolved if the user re-invokes the same sub-skill within the same session without an intervening acknowledgment. Crisis mode triggers after 2 unresolved invocations."

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72

---

### FM-025-I4: Pre-Launch Blind Evaluation Evaluator Qualification Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-10 Pre-Launch Validation AC (line 840): "3 independent evaluators score both the AI-augmented output and a manually-produced reference output on completeness, actionability, and time-to-insight without knowing which is AI-augmented. Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions."

No qualification criteria for the 3 independent evaluators is specified.

**Analysis:**
R3 added the blind evaluation rubric (addressing the FM-019-I3 ground-truth artifact independence concern), but introduced a new gap: who are these 3 evaluators? For a 1-2 person implementing team, "3 independent evaluators" is a significant recruitment requirement that is not addressed. Without qualification criteria, a team could use 3 LLM instances, 3 members of the implementing team, or 3 unqualified people. The evaluation protocol is well-specified (blind, 3-dimension rubric, 15% threshold) but the evaluator sourcing is not. This is a new failure mode introduced by R3.

**Recommendation:**
Add evaluator qualification: "Independent evaluators must: (a) not have contributed to the sub-skill design or implementation, (b) have sufficient UX familiarity to evaluate completeness and actionability (UX practitioner, product manager, or developer who regularly reviews UX artifacts), (c) be recorded in the pre-launch validation log with their role and evaluation date. For solo or 2-person implementing teams, evaluators from the broader Jerry community or external collaborators may serve."

**Post-Correction RPN:** S=5, O=3, D=4 → RPN=60

---

### FM-026-I4: Cross-Framework Synthesis AC Lacks Minimum Report Structure

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-10 (line 791): "Cross-framework synthesis AC: The `/user-experience` parent skill produces a unified insight report combining findings from 2+ sub-skill analyses on the same product, identifying convergent and divergent recommendations across frameworks."

No minimum structure for the unified insight report is defined.

**Analysis:**
This is a new failure mode introduced by R3 fix SR-002-I3. The AC correctly establishes the capability requirement (unified insight report across 2+ sub-skill analyses) but leaves "convergent and divergent recommendations" undefined. Without a minimum structure, the AC is satisfied by any document that mentions findings from two sub-skills — including a free-text summary with no structured comparison. The AC tests existence of the report but not its quality or completeness. This is a significant gap for the orchestrator's primary synthesis function.

**Recommendation:**
Define the minimum report structure as an AC addendum: "The unified insight report must include: (a) Convergent findings section — 1+ recommendations where 2+ sub-skills agree; (b) Divergent findings section — any conflicting recommendations with explicit resolution guidance; (c) Portfolio gap section — UX lifecycle stages not covered by the invoked sub-skills. Each section requires at least 1 entry or an explicit 'none identified' statement. The report must reference the specific sub-skill outputs by artifact path."

**Post-Correction RPN:** S=4, O=3, D=4 → RPN=48

---

## Recommendations

### Critical Findings (Mandatory Corrective Action)

| ID | Corrective Action | Acceptance Criteria | Est. RPN Post-Fix |
|----|------------------|---------------------|-------------------|
| FM-004-I4 | Define cross-sub-skill handoff schema (upstream_artifact, downstream_input_field_mapping, confidence_level, validation_checkpoint); add to `ux-routing-rules.md` scope; update cross-framework integration AC to verify data contract compliance | Schema documented; AC verifies downstream sub-skill populates input from upstream artifact without manual reformatting | 84 |
| FM-009-I4 | Replace "Populated during Wave N" with pre-commitment language; tie completion to Wave N KICKOFF-SIGNOFF as a blocking entry criterion | Wave N KICKOFF-SIGNOFF cannot be completed without the MCP constraint row being committed | 63 |

### Major Findings (Recommended Corrective Action)

| ID | Corrective Action | Est. RPN Post-Fix |
|----|------------------|-------------------|
| FM-006-I4 | Define Synthesis Judgments Summary format (3-field entries: claim, evidence basis, confidence qualifier); minimum 3 entries for HIGH confidence; fewer than 3 downgrades to MEDIUM | 72 |
| FM-014-I4 | Define "resolution" for crisis mode: worktracker entity created, verbal confirmation, or downstream invocation; crisis triggers after 2 unresolved invocations | 72 |
| FM-025-I4 | Add evaluator qualification criteria for blind evaluation (no contribution to sub-skill; sufficient UX familiarity); allow Jerry community evaluators for small teams | 60 |
| FM-026-I4 | Define minimum unified insight report structure (convergent findings, divergent findings with resolution guidance, portfolio gap) | 48 |
| FM-002-I4 | Add per-operation request budget estimates for `/ux-heuristic-eval` (Figma) and `/ux-design-sprint` (Miro); mark as estimated | 75 |
| FM-003-I4 | Confirm 3/3 pass requirement for JTBD benchmark; add rationale for why 2/3 is not actionable | 50 |
| FM-016-I4 | Define "measurable signal" (metric name + data source + measurement method) | 60 |
| FM-011-I4 | Define "expert review" qualification for MEDIUM-confidence behavior-design outputs | 40 |
| FM-013-I4 | Define "MCP-heavy team" via KICKOFF-SIGNOFF.md "Available MCP Tools" (2+ Required MCPs configured and active) | 40 |

### Minor Findings (Improvement Opportunities)

| ID | Corrective Action | Est. RPN Post-Fix |
|----|------------------|-------------------|
| FM-015-I4 | Link V2 trigger #3 measurement to worktracker invocation log entries | 25 |
| FM-017-I4 | Add justification for C1 > C2 weighting (failing tiny-teams applicability is disqualifying even if composable) | 20 |
| FM-018-I4 | Add caption to mermaid diagram: "Orange fill = CONDITIONAL sub-skill" | 20 |
| FM-008-I4 | Specify Human Override Justification storage: block-quoted field in output artifact under `## Human Override Justification` heading | 20 |
| FM-012-I4 | Add explicit AC note scoping 4-skill canonical sequence to V2 | 20 |
| FM-022-I4 | Define response when MCP fallback rate exceeds 20% (flag for V2 planning review) | 20 |
| FM-020-I4 | Tie MCP maintenance owner to named field in `kickoff-signoff-template.md` | 18 |
| FM-027-I4 | Add wave bypass expiry to Wave Progression AC (60 days or next wave review; escalation warning on expiry) | 18 |
| FM-024-I4 | Add part-time contractor UX segment (2-5 team + 10-20 hrs/week contractor) to population segments table | 12 |

---

## RPN Comparison: Iter 3 → Iter 4

### Items Resolved by R3

| Iter 3 ID | Iter 3 RPN | R3 Fix Applied | Iter 4 Status |
|-----------|-----------|----------------|---------------|
| FM-001-I3 | 336 | 3-state enforcement (PASS/WARN/BLOCK) fully defined | **RESOLVED** |
| FM-010-I3 | 180 | HEART synthesis hypothesis warning added | **RESOLVED** |
| FM-019-I3 | 210 | Blind evaluation rubric defined (partial fix — evaluator qualification gap remains as FM-025-I4) | **PARTIALLY RESOLVED** |
| FM-023-I3 | 45 | `kickoff-signoff-template.md` added to E-15 | **RESOLVED** |
| FM-005-I3 | 125 | Not directly addressed in R3 fixes (tracked in FM-027-I4) | **PARTIALLY RESOLVED** |

**Note on FM-019-I3 → FM-025-I4:** R3's blind evaluation rubric resolved the ground-truth artifact independence question but introduced an evaluator qualification gap. The finding changes character (independence of artifact selection → independence and qualification of evaluators) and receives a new identifier.

### Persistent Failure Modes (Iter 3 → Iter 4)

| Iter 3 ID | Iter 3 RPN | Iter 4 ID | Iter 4 RPN | Change | Notes |
|-----------|-----------|-----------|-----------|--------|-------|
| FM-004-I3 | 294 | FM-004-I4 | 252 | -42 | Parent handoff defined (R3); sub-skill handoff still missing. O reduced 6→6, D reduced 7→6. |
| FM-009-I3 | 245 | FM-009-I4 | 245 | 0 | No R3 change. Table note now normalizes deferral, keeping D=5. |
| FM-006-I3 | 180 | FM-006-I4 | 180 | 0 | No R3 change. |
| FM-014-I3 | 180 | FM-014-I4 | 180 | 0 | No R3 change. |
| FM-002-I3 | 180 | FM-002-I4 | 150 | -30 | O reduced 5→5, D reduced 6→5. MCP runbook now AC narrows detection gap marginally. |
| FM-003-I3 | 150 | FM-003-I4 | 125 | -25 | O reduced 5→5, D reduced 6→5. AC language slightly clearer. |
| FM-016-I3 | 150 | FM-016-I4 | 150 | 0 | No R3 change. |
| FM-011-I3 | 100 | FM-011-I4 | 100 | 0 | No R3 change. |
| FM-013-I3 | 100 | FM-013-I4 | 100 | 0 | No R3 change. |
| FM-015-I3 | 75 | FM-015-I4 | 75 | 0 | No R3 change. |
| FM-017-I3 | 60 | FM-017-I4 | 60 | 0 | No R3 change. |
| FM-018-I3 | 60 | FM-018-I4 | 60 | 0 | No R3 change. |
| FM-008-I3 | 60 | FM-008-I4 | 60 | 0 | No R3 change. |
| FM-012-I3 | 48 | FM-012-I4 | 48 | 0 | No R3 change. |
| FM-022-I3 | 48 | FM-022-I4 | 48 | 0 | No R3 change. |
| FM-020-I3 | 150 | FM-020-I4 | 48 | -102 | `kickoff-signoff-template.md` now exists in E-15 (R3 fix FM-023-I3); maintenance owner can be tied there. D reduced 6→4, O reduced 5→4. |
| FM-024-I3 | 24 | FM-024-I4 | 24 | 0 | No R3 change. |
| FM-021-I3 | 125 | — | — | RESOLVED | L0/L1/L2 UX context addressed in orchestrator AC (R3-fix: SR-003-I3 defined dual function). |
| FM-007-I3 | 80 | — | — | RESOLVED | Figma SPOF section retains the 2023 Dev Mode reference but this is a Known Limitations section citing a historical pattern — acceptable for risk documentation. |

### New Failure Modes Introduced by R3

| ID | Source | RPN |
|----|--------|-----|
| FM-025-I4 | Blind evaluation AC (R3-fix RT-001-I3) defines 3-evaluator protocol without evaluator qualification | 100 |
| FM-026-I4 | Cross-framework synthesis AC (R3-fix SR-002-I3) defines report requirement without minimum structure | 100 |
| FM-027-I4 | Wave bypass expiry behavior described in E-08 but not enforced in Wave Progression AC | 48 |

**Total new RPN from R3-introduced modes:** 248

### RPN Summary

| Metric | Iter 3 | Iter 4 | Change |
|--------|--------|--------|--------|
| Total RPN | 1,732 | 1,058 | -674 (-39%) |
| Critical count | 4 | 2 | -2 |
| Major count | 12 | 9 | -3 |
| Minor count | 8 | 9 | +1 |
| Total findings | 24 | 20 | -4 |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| **Completeness** | 0.20 | Negative (improving) | FM-004-I4 (sub-skill handoff schema missing), FM-006-I4 (Synthesis Judgments Summary format), FM-014-I4 (crisis mode resolution undefined), FM-026-I4 (unified insight report structure missing), FM-011-I4 (expert review undefined) are structural completeness gaps. R3 resolved FM-001-I3 (wave 3-state behavior) — the largest single completeness gain. Net: moderate negative, significantly improved from Iter 3. |
| **Internal Consistency** | 0.20 | Positive | FM-010-I3 fully resolved (HEART synthesis warning added; all affected sub-skills now consistently carry synthesis hypothesis warnings). R3 also addressed SR-002-I3 (Capability Map framing) and SR-003-I3 (cognitive mode dual function). No new internal consistency failures identified. Net: minor positive. |
| **Methodological Rigor** | 0.20 | Negative (improving) | FM-009-I4 (deferred MCP constraints) persists unchanged. FM-003-I4 (JTBD benchmark pass threshold) and FM-013-I4 (MCP-heavy definition) remain. FM-016-I4 (measurable signal definition) persists. R3 resolved the wave 3-state behavior methodological gap. Net: minor-to-moderate negative, improved from Iter 3. |
| **Evidence Quality** | 0.15 | Mixed | FM-025-I4 (evaluator qualification for blind evaluation) and FM-016-I4 (measurable signal definition) are new/persistent evidence quality gaps. R3 added blind evaluation rubric (FM-019-I3 partially resolved), WSM score scale disclosure (SR-005-I3). FM-017-I4 (C1>C2 weighting justification) persists. Net: neutral. |
| **Actionability** | 0.15 | Mixed | FM-002-I4 (rate limits non-actionable) persists but PM-001-I3 resolved by elevating MCP runbook to AC. FM-015-I4 and FM-022-I4 are minor. FM-026-I4 (report structure) affects actionability of the synthesis capability. Net: minor negative, marginally improved. |
| **Traceability** | 0.10 | Positive | FM-023-I3 resolved (kickoff-signoff-template.md in E-15). R3-fix SR-008-I3 added both template files to E-15. FM-018-I4 and FM-008-I4 are minor traceability gaps. Net: minor positive. |

---

## Overall Assessment

**REVISE** — Two Critical and nine Major findings require targeted correction.

The R3 deliverable demonstrates the fastest single-iteration RPN reduction in the tournament: 39% improvement (1,732 → 1,058). The resolution of FM-001-I3 (wave enforcement 3-state behavior) eliminates the highest-RPN finding in the entire Iter 3 set. Internal consistency is now at its best point in the tournament. The deliverable is approaching PASS territory: all remaining Critical findings are specification completeness gaps with well-defined corrective actions, and no findings challenge the architectural soundness of the design.

The residual pattern is consistent: mechanisms are defined, their internal behaviors are not fully specified. FM-004-I4 (sub-skill handoff schema), FM-006-I4 (Synthesis Judgments Summary format), FM-014-I4 (crisis mode resolution), and FM-026-I4 (unified insight report structure) all follow this pattern. One additional targeted revision addressing the 2 Critical findings and the 4 highest-RPN Major findings (FM-006-I4, FM-014-I4, FM-025-I4, FM-026-I4) should bring the total RPN below 400 and resolve all blocks to PASS.

---

## Execution Statistics

- **Total Findings:** 20
- **Critical:** 2 (FM-004-I4, FM-009-I4)
- **Major:** 9 (FM-006-I4, FM-014-I4, FM-025-I4, FM-026-I4, FM-002-I4, FM-003-I4, FM-016-I4, FM-011-I4, FM-013-I4)
- **Minor:** 9 (FM-015-I4, FM-017-I4, FM-018-I4, FM-008-I4, FM-012-I4, FM-022-I4, FM-020-I4, FM-027-I4, FM-024-I4)
- **Total RPN (Iter 4):** 1,058
- **Total RPN (Iter 3):** 1,732
- **RPN Change:** -674 (-39%)
- **Protocol Steps Completed:** 5 of 5

---

*Report Version: Iteration 4*
*Strategy: S-012 FMEA*
*SSOT: `.context/rules/quality-enforcement.md`*
*Template: `.context/templates/adversarial/s-012-fmea.md`*
*Generated: 2026-03-03*
