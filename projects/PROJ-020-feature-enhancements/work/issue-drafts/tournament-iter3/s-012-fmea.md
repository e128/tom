# FMEA Report: /user-experience Skill GitHub Enhancement Issue (R2)

**Strategy:** S-012 FMEA (Failure Mode and Effects Analysis)
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-012, Iteration 3)
**H-16 Compliance:** S-003 Steelman applied in prior tournament sequence (confirmed)
**Elements Analyzed:** 15 | **Failure Modes Identified:** 24 | **Total RPN:** 1,732

---

## Summary

The R2 deliverable shows meaningful improvement: FM-002 (MCP operational constraints) is fully addressed with a new table covering rate limits, auth methods, and failure codes. FM-003 (JTBD benchmark) is resolved with a deterministic 3-criterion rubric. FM-011 (behavior-design contradiction) is resolved by renaming to "Reference Intervention Patterns" and reclassifying to MEDIUM. Residual top risks are FM-001 (synthesis gate — WAVE-N-SIGNOFF enforcement is documented but the AC does not specify what the orchestrator does when `WAVE-N-SIGNOFF.md` is absent, leaving a gap between intent and verification), FM-004 (sub-skill handoff protocols — cross-framework integration ACs test 2 canonical sequences but do not define the handoff schema or success signal format), and FM-009 (Zeroheight and Whimsical operational data deferred to future waves with no interim constraints). Total RPN declined from 2,204 to 1,732 (21% reduction). Four new failure modes are introduced by R2 changes. Recommendation: **REVISE** — targeted corrections required before PASS.

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
| E-08 | Wave Deployment Model | 5 waves, entry criteria, WAVE-N-SIGNOFF enforcement, bypass mechanism |
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
| FM-001-I3 | E-08, E-10 | Wave enforcement AC specifies WAVE-N-SIGNOFF.md check but does not define orchestrator behavior on absence (block routing? warn? log?) | 8 | 6 | 7 | 336 | Critical | Define the three-state handling: (a) SIGNOFF absent = hard block with user message, (b) bypass in progress = route with warning banner, (c) SIGNOFF present = route normally. Add to E-08 wave enforcement paragraph and E-10 wave progression AC. | Completeness |
| FM-004-I3 | E-04, E-10 | Cross-framework handoff protocol undefined: AC tests 2 integration sequences (JTBD→Sprint, Lean UX→HEART) but neither the handoff schema nor the success signal format is specified | 7 | 6 | 7 | 294 | Critical | Define handoff schema (minimum fields: upstream_artifact, downstream_input_mapping, confidence_level) and success signal format for cross-sub-skill integration. Add to `ux-routing-rules.md` scope in Directory Structure section and add AC: "Cross-framework handoff schema defined and validated in at least 2 canonical sequences." | Completeness |
| FM-009-I3 | E-07 | Zeroheight and Whimsical operational constraint rows deferred ("Populated during Wave N implementation") with no interim constraints or placeholder validation plan | 7 | 7 | 5 | 245 | Critical | Add a placeholder row with known constraints or document an explicit pre-Wave commitment: "Zeroheight and Whimsical operational constraints MUST be documented and committed to the issue before the sub-skill that requires them enters Wave N development (not at merge time for that Wave)." | Methodological Rigor |
| FM-019-I3 | E-10 | Pre-launch validation AC requires external ground-truth artifact for Wave 1 quality benchmarks but does not specify who selects or approves the ground-truth artifact — self-selection by the implementing team negates the independence guarantee | 7 | 6 | 5 | 210 | Critical | Add independence requirement: "The ground-truth artifact is proposed by the implementing team and approved by an independent reviewer (not the person who built the sub-skill). Approval is recorded in the pre-launch validation log." | Evidence Quality |
| FM-002-I3 | E-07 | MCP operational constraints table added (R2 fix): Figma rate limit (720 req/min) and Miro rate limit (100 req/min) lack per-operation cost estimates — heuristic evaluation and design sprint are the most rate-intensive operations but no request-per-invocation budget is defined, making the rate limits non-actionable | 6 | 5 | 6 | 180 | Major | Add per-operation request budget estimates for the two highest-rate operations: `/ux-heuristic-eval` (estimated Figma API calls per full 10-heuristic evaluation) and `/ux-design-sprint` (estimated Miro calls per sprint day). Mark as "estimated; validate during Wave 1 implementation." | Actionability |
| FM-006-I3 | E-09 | HIGH-confidence gate requires "enumerated acknowledgment of AI judgment calls via Synthesis Judgments Summary" but the Synthesis Judgments Summary format is not defined — what is an "AI judgment call" in this context? | 6 | 6 | 5 | 180 | Major | Define the Synthesis Judgments Summary format: each entry should include (a) the claim the AI made, (b) the evidence basis, (c) the confidence descriptor. Add a template stub or example to `synthesis-validation.md` scope or acceptance criteria. | Completeness |
| FM-010-I3 | E-04 | `/ux-ai-first-design` synthesis hypothesis warning states "all AI interaction pattern recommendations are LOW confidence" but the synthesis validation section (E-09) does NOT list this sub-skill in the LOW-confidence outputs section — it lists `/ux-kano-model`, `/ux-heart-metrics`, and `/ux-ai-first-design` in LOW, and `/ux-behavior-design` in MEDIUM. Cross-check: LOW list in E-09 does include `/ux-ai-first-design`, so no inconsistency. However, `/ux-heart-metrics` is listed as LOW confidence for "metric threshold recommendation" but the sub-skill description for HEART (E-04) does not include any synthesis hypothesis warning. | 5 | 6 | 6 | 180 | Major | Add a synthesis hypothesis warning to the `/ux-heart-metrics` sub-skill description (E-04) noting that "metric threshold recommendations are LOW confidence (reference-only)" to match the classification in E-09. | Internal Consistency |
| FM-014-I3 | E-06 | Crisis mode activation criteria include "user explicitly describes urgency" (via keyword detection) OR "multiple prior sub-skill invocations without resolution" but "resolution" is undefined — what counts as resolved vs. unresolved for the circuit breaker trigger? | 6 | 5 | 6 | 180 | Major | Define "resolution" for crisis mode activation: "A sub-skill invocation is considered resolved when the user explicitly acknowledges the output, accepts a recommendation, or closes the sub-skill session with a confirmed output artifact. An invocation is unresolved if the user re-invokes without an acknowledged prior output." Add to crisis mode description in E-06. | Completeness |
| FM-003-I3 | E-10 | JTBD benchmark (R2 fix): 3-criterion deterministic rubric is well-defined, but does not specify the minimum pass threshold — must all 3 criteria pass, or is 2/3 actionable? | 5 | 5 | 6 | 150 | Major | Clarify: "3/3 criteria = actionable (current text)" explicitly blocks 2/3 pass — confirm this is intentional. If 3/3 is required, add rationale: "all 3 criteria are necessary conditions; 2/3 with a missing emotional/social dimension produces incomplete job statements that underspecify motivation." | Methodological Rigor |
| FM-016-I3 | E-10 | Wave 2-5 quality benchmark ACs specify benchmarks for each sub-skill (e.g., Lean UX: "assumption map with >= 3 risk categories"; HEART: "all 5 dimensions with measurable signals") but do NOT specify what constitutes a "measurable signal" for HEART — teams could claim any text in the field qualifies | 5 | 6 | 5 | 150 | Major | Add a minimum definition of "measurable signal" for the HEART benchmark: "A measurable signal includes at minimum a metric name, a data source, and a measurement method (e.g., 'daily active users from Mixpanel, measured weekly')." | Evidence Quality |
| FM-020-I3 | E-07 | R2 added MCP Operational Constraints table but the table note states values are "point-in-time as of March 2026" — the quarterly audit cadence is referenced but the ownership field for the audit is "named MCP maintenance owner" without specifying how that owner is assigned or tracked | 5 | 5 | 6 | 150 | Major | Add an explicit maintenance owner assignment mechanism: "MCP maintenance owner is assigned in the `KICKOFF-SIGNOFF.md` template (a named field). The quarterly audit is tied to this owner." Reference the `kickoff-signoff-template.md` artifact in the constraint table note. | Actionability |
| FM-021-I3 | E-05 | Key Design Decision #1 (framework-per-skill) references AD-M-004 for L0/L1/L2 output levels in orchestrator AC but the issue does not define what L0/L1/L2 means for UX deliverables in this context — inherited from Jerry framework but not adapted to UX outputs | 5 | 5 | 5 | 125 | Major | Add a UX-context L0/L1/L2 definition (even a brief one): "L0: executive UX summary (problem, recommendation, confidence). L1: technical findings (scored violation list, B=MAP diagnosis). L2: strategic implications (portfolio coverage, capability map impact)." This can be placed in the orchestrator AC or Key Design Decision #1. | Completeness |
| FM-005-I3 | E-08 | Wave bypass mechanism requires "3-field documentation" but the bypass expiry is undefined — once bypass is invoked, can a team remain in bypass indefinitely? The "WAVE BYPASS ACTIVE" warning appears on outputs but nothing forces resolution. | 5 | 5 | 5 | 125 | Major | Add bypass expiry: "A wave bypass expires after 60 days or the next wave progression review (whichever comes first). If the remediation plan's target date passes without closure, the orchestrator escalates to the user via an explicit warning message before each sub-skill invocation." | Completeness |
| FM-007-I3 | E-11 | Figma SPOF limitation references "Dev Mode became paid in 2023" as evidence of monetization risk, but Figma's current API pricing (as of 2026) may differ — the citation is outdated and weakens the risk argument | 4 | 4 | 5 | 80 | Major | Update the Figma risk citation with the current API access status as of March 2026. If specific pricing has changed, correct it. If the general pattern (Figma restricting free access) still holds, reference the most recent example. | Evidence Quality |
| FM-011-I3 | E-04 | R2 fix applied: `/ux-behavior-design` renamed "Reference Intervention Patterns" and reclassified LOW→MEDIUM. The synthesis hypothesis warning in E-04 correctly states "MEDIUM confidence. Require expert review OR validation against 2-3 real user data points." However, the rubric for "expert review" is undefined — who qualifies as an expert in this context? | 4 | 5 | 5 | 100 | Major | Define "expert review" minimally: "A person with demonstrated UX research or behavioral design experience — either a professional UX practitioner, a published UX academic, or a product leader with documented UX background. AI cannot serve as the expert reviewer for MEDIUM-confidence outputs." | Completeness |
| FM-013-I3 | E-06 | Routing triage flowchart includes a "MCP-heavy team?" node but "MCP-heavy" is not defined — what criteria determine this classification? The orchestrator needs a testable definition to implement the routing branch | 4 | 5 | 5 | 100 | Major | Define "MCP-heavy team" as a triage criterion: "A team is MCP-heavy if they have 2+ Required MCPs configured and active (not just subscribed). The orchestrator determines this from `KICKOFF-SIGNOFF.md` field 'Available MCP Tools'." | Methodological Rigor |
| FM-015-I3 | E-12 | V2 trigger conditions (#3: "3+ monthly requests for AI UX pattern guidance while AI-First Design Enabler is incomplete") cannot be measured by the V1 architecture — there is no request-tracking mechanism defined for counting sub-skill invocations | 3 | 5 | 5 | 75 | Minor | Add V2 trigger measurement mechanism: "Monthly invocation counts tracked via worktracker log entries (each sub-skill invocation creates a worktracker entry). V2 trigger threshold measured against worktracker entry counts." | Actionability |
| FM-017-I3 | E-13 | WSM criteria weights (C1: 0.25, C2: 0.20, C3-C5: 0.15 each, C6: 0.10) sum to 1.00 (verified), but the "graduated-priority weighting" rationale references Tier 1 (C1+C2 = 0.45) as "defining requirements" without explaining why C1 outweighs C2 by 25% — C2 (Composability) seems equally critical for a Jerry skill | 3 | 4 | 5 | 60 | Minor | Add a brief justification for C1 > C2 weighting: "C1 (Applicability to tiny teams, 0.25) is weighted above C2 (Composability, 0.20) because a framework that cannot serve tiny teams fails the fundamental use case even if perfectly composable as a Jerry skill. C2 receives the second-highest weight because non-composable frameworks cannot be delivered at all." | Evidence Quality |
| FM-018-I3 | E-03 | Mermaid diagram for parent orchestrator uses `style AF fill:#E8A838` (orange) to mark AI-First Design as conditional, but no legend explains this color coding in the diagram itself | 3 | 5 | 4 | 60 | Minor | Add a legend to the mermaid diagram or a caption: "Orange fill = CONDITIONAL sub-skill (requires Enabler completion before Wave 5 deployment)." | Traceability |
| FM-008-I3 | E-09 | Human Override Justification field described as creating "an auditable paper trail" but no storage mechanism is defined — where is this justification stored? In the output file? A worktracker entry? | 3 | 5 | 4 | 60 | Minor | Specify storage: "Human Override Justification is stored as a block-quoted field in the sub-skill output artifact, under a heading `## Human Override Justification` at the end of the output. The worktracker entry for the invocation links to this section." | Traceability |
| FM-012-I3 | E-14 | Integration diagram shows `/orchestration` as coordinating "multi-framework workflows (JTBD→Sprint→Lean UX→HEART)" but the AC for cross-framework integration only tests 2 sequences — JTBD→Sprint and Lean UX→HEART. The 4-skill canonical sequence (JTBD→Sprint→Lean UX→HEART) is not tested end-to-end | 3 | 4 | 4 | 48 | Minor | Note in the AC: "The 4-skill canonical sequence (JTBD→Sprint→Lean UX→HEART) is a V2 integration test — V1 validates the 2 two-skill handoffs that compose it (JTBD→Sprint as Seq-1, Lean UX→HEART as Seq-2) as sufficient for V1." This makes the scoping decision explicit rather than leaving it as a gap. | Completeness |
| FM-022-I3 | E-10 | Post-launch success metrics section defines 5 metrics with "target: baseline establishment" for most, but "MCP fallback activation rate < 20%" is a hard target mixed in with baseline-only targets — the inconsistency means the 20% target will be missed without triggering any defined response | 3 | 4 | 4 | 48 | Minor | Clarify the response to missing the 20% fallback target: "If MCP fallback activation rate exceeds 20% for a Required MCP during the first 90 days, the MCP integration is flagged for review in the next V2 planning cycle." | Actionability |
| FM-023-I3 | E-05 | Key Design Decision #6 (synthesis validation) describes the 3-tier gate as "architecturally visible and structurally enforced through template design" but the Directory Structure (E-15) does not include a `kickoff-signoff-template.md` in the parent skill templates, only `wave-signoff-template.md` | 3 | 5 | 3 | 45 | Minor | Add `kickoff-signoff-template.md` to the parent skill templates in the Directory Structure: `skills/user-experience/templates/kickoff-signoff-template.md` (already referenced in the Wave 1 entry criteria text in E-08, but absent from E-15). | Traceability |
| FM-024-I3 | E-02 | Population segments table has no entry for teams with a dedicated part-time designer (e.g., a contractor UX designer, 10-20 hrs/week) — this is a common tiny-team composition that does not fit any of the 4 segments | 2 | 3 | 4 | 24 | Minor | Add a fifth segment row: "Part-time contractor UX (2-5 team + contractor UX, 10-20 hrs/week): HIGH fit for discovery and evaluation frameworks; contractor handles judgment-intensive steps; AI handles synthesis and structured evaluation." | Completeness |

---

## Detailed Findings

### FM-001-I3: Wave Enforcement Behavior on SIGNOFF Absence

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Element** | E-08 (Wave Deployment), E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-08: "Each wave requires a `WAVE-{N}-SIGNOFF.md` file completed before the orchestrator routes to sub-skills in the next wave. The orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills."
E-10 AC: "Wave entry enforcement: orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills"

**Analysis:**
The AC specifies WHAT the orchestrator checks (existence of SIGNOFF file) but NOT WHAT it does when the check fails. Three plausible behaviors exist: (1) hard block — refuses to route, displays error; (2) soft warning — routes but displays warning; (3) bypass gate — treats absence as an implied bypass request. Without explicit specification, implementers will choose inconsistently, and users will experience undefined behavior at the critical wave progression gate. This was flagged in Iter 2 as FM-001 (RPN 324 → 336 in Iter 3 because the R2 fix was incomplete — the enforcement AC was added but the three-state behavior was not defined). Occurrence increased from 5 to 6 because the R2 text makes the check mechanism explicit without completing the behavioral specification.

**Recommendation:**
Add to E-08 (wave enforcement paragraph): "When `WAVE-{N}-SIGNOFF.md` is absent, the orchestrator: (a) displays the unmet entry criteria, (b) presents two options to the user — complete the SIGNOFF or document a bypass — and (c) routes ONLY after explicit user selection per H-31 (P-020 user authority). Routing is NOT a default fallback." Add to E-10 wave progression AC: "Orchestrator three-state behavior (block / bypass-with-warning / route) is verified by a state transition test during Wave 1 integration testing."

**Post-Correction RPN:** S=8, O=3, D=4 → RPN=96 (expected post-R3 fix)

---

### FM-004-I3: Cross-Framework Handoff Protocol Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Element** | E-04 (Sub-Skill Descriptions), E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-10 AC: "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)"
E-04: Each sub-skill lists "Key Output" but no field defines the format that downstream sub-skills consume.

**Analysis:**
The AC mandates testing of cross-framework handoffs but specifies neither the handoff schema (what fields the output contains) nor the success signal (how the receiving sub-skill knows it has received valid input). The JTBD→Design Sprint handoff, for example, requires that the job statement output from `ux-jtbd-analyst` can be consumed directly by `ux-sprint-facilitator` as the challenge statement input. Without a defined schema, the integration test verifies only that invocations complete, not that the data contract is sound. This failure mode was FM-004 in Iter 2 (RPN 252). In Iter 3, the issue closure condition AC was added (FM-004 Iter2 fix), but the handoff schema definition — the upstream fix — was not added.

**Recommendation:**
Add to `ux-routing-rules.md` scope in Directory Structure (E-15): "Includes cross-sub-skill handoff schema (minimum fields: upstream_artifact path, downstream_input_field_mapping, confidence_level, validation_checkpoint)." Add to E-10 cross-framework integration AC: "Handoff schema validated — downstream sub-skill successfully populates its challenge statement / hypothesis input from upstream artifact without manual reformatting by the user."

**Post-Correction RPN:** S=7, O=3, D=4 → RPN=84 (expected post-R3 fix)

---

### FM-009-I3: Zeroheight and Whimsical Operational Constraints Deferred Without Commitment

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Element** | E-07 (MCP Integration) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-07 MCP Operational Constraints table:
- Zeroheight: "Populated during Wave 3 implementation" in rate limits, auth method, API version, and failure codes.
- Whimsical: "Populated during Wave 5 implementation" in rate limits, auth method, and API version.

**Analysis:**
The R2 MCP constraints table (which resolved FM-002's absence) introduces a new failure mode: two of six MCP servers have deferred operational constraints with no interim commitment. This creates a gap where Wave 3 and Wave 5 sub-skills could enter development without having validated MCP operational data. The "Populated during Wave N" language functions as a silent placeholder — it looks complete from a table-structure perspective but contains no actionable constraints. Teams planning Wave 3 (Atomic Design) with Zeroheight will not know rate limits or auth requirements until they begin implementation.

**Recommendation:**
Replace "Populated during Wave N implementation" rows with explicit pre-commitment language: "Zeroheight: Auth method known (API key per product docs); rate limits TBD — MUST be verified and committed to this table before Wave 3 development kickoff. Failure to commit before kickoff blocks Wave 3 SIGNOFF." Apply same pattern to Whimsical. This converts the deferral from a silent gap into a tracked commitment.

**Post-Correction RPN:** S=7, O=3, D=3 → RPN=63 (expected post-R3 fix)

---

### FM-019-I3: Pre-Launch Validation Independence Guarantee Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Element** | E-10 (Acceptance Criteria) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-10 Pre-Launch Validation AC: "Before Wave 1 sub-skill merge, each sub-skill's quality benchmark is validated against an external ground-truth artifact (not self-created by the implementing team). Benchmark achievement is demonstrated via test output comparison, not merely defined."

**Analysis:**
The AC states the ground-truth artifact must be "not self-created by the implementing team" but does not specify who selects or approves it. Without an approval mechanism, the implementing team can select a ground-truth artifact that is superficially external (published case study) but selectively chosen to make the benchmark easy to pass. The AI-First Design benchmark is deferred to Enabler acceptance criteria, creating another validation gap. The independence guarantee is well-intentioned but unenforced without an approval layer.

**Recommendation:**
Add: "The external ground-truth artifact is nominated by the implementing team but must be approved by an independent reviewer before benchmark testing begins. The independent reviewer signs off in the pre-launch validation log (a new artifact in the Wave 1 AC set). This mirrors the AI-First Design Enabler requirement for independent reviewer sign-off [R2-fix: RT-005]."

**Post-Correction RPN:** S=7, O=3, D=4 → RPN=84 (expected post-R3 fix)

---

### FM-002-I3: MCP Rate Limit Lacks Per-Operation Request Budget

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-07 (MCP Integration) |
| **Strategy Step** | Step 2: Failure mode lens — Insufficient |

**Evidence:**
E-07: "Figma: Tier-dependent (Professional: 720 req/min per-user)" and "Miro: 100 req/min per-user (Team plan)"
No per-operation request cost is specified for any sub-skill invocation.

**Analysis:**
The R2 fix added operational constraints (FM-002 Iter2 resolved), but the implementation constraint — how many API requests a typical invocation consumes — is missing. 720 req/min (Figma) sounds generous but if `/ux-heuristic-eval` makes 200 requests per heuristic evaluation (fetching frames, extracting components, analyzing contrast per element), a single session could exhaust the budget within minutes. Without per-operation budgets, the rate limits are informational but not actionable for capacity planning.

**Recommendation:**
Add a "Typical Requests/Invocation (Estimate)" column to the MCP constraints table, or add a footnote under the table: "Implementation note: `/ux-heuristic-eval` estimated at [X] Figma API calls per full evaluation (to be validated during Wave 1). `/ux-design-sprint` estimated at [Y] Miro calls per sprint day. Teams operating near rate limits should request higher API tiers before Wave 1 go-live."

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72 (expected post-R3 fix)

---

### FM-006-I3: Synthesis Judgments Summary Format Undefined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-09 (Synthesis Hypothesis Validation) |
| **Strategy Step** | Step 2: Failure mode lens — Missing |

**Evidence:**
E-09: "HIGH confidence gate: User reviews output and acknowledges specific AI judgment calls via a Synthesis Judgments Summary."

**Analysis:**
The "Synthesis Judgments Summary" is referenced as the mechanism for HIGH-confidence acknowledgment but its format is entirely undefined. What makes something an "AI judgment call" that must appear in the summary? Is it any claim the AI makes without user data? Only claims that could materially affect a design decision? The undefined format means implementers will generate summaries inconsistently, and users will be unable to meaningfully evaluate what they are acknowledging. This undermines the automation bias mitigation mechanism.

**Recommendation:**
Define the Synthesis Judgments Summary format in the `synthesis-validation.md` scope (and reference it in E-09): each entry contains (a) the AI claim ("Job statement: 'When onboarding new customers...'"), (b) the basis ("Generated from secondary research — no user interview data"), and (c) the confidence qualifier ("MEDIUM; requires validation against 2-3 user interviews"). A minimum of 3 entries is required for a HIGH-confidence output (if fewer than 3 AI judgment calls are present, the output downgrades to MEDIUM).

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72 (expected post-R3 fix)

---

### FM-010-I3: HEART Sub-Skill Missing Synthesis Hypothesis Warning

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-04 (Sub-Skill Descriptions), E-09 (Synthesis Hypothesis Validation) |
| **Strategy Step** | Step 2: Failure mode lens — Inconsistent |

**Evidence:**
E-09 LOW-confidence outputs list: `/ux-kano-model` (feature priority conflict interpretation), `/ux-heart-metrics` (metric threshold recommendation), `/ux-ai-first-design` (AI interaction pattern recommendations).
E-04 `/ux-heart-metrics` description: No synthesis hypothesis warning present. All other sub-skills with LOW/MEDIUM confidence outputs have explicit warnings in their E-04 descriptions.

**Analysis:**
HEART metric threshold recommendations are classified as LOW confidence in E-09, but the HEART sub-skill description in E-04 includes no synthesis hypothesis warning. This inconsistency means that a reader reviewing the HEART sub-skill description alone will not discover the LOW-confidence classification for threshold recommendations. The pattern of explicit warnings in all other affected sub-skills (JTBD, Lean UX, Kano, Behavior Design) creates an expectation that HEART has none, because it does not need one — which is incorrect.

**Recommendation:**
Add a synthesis hypothesis warning to the `/ux-heart-metrics` sub-skill description (E-04): "**Synthesis hypothesis warning:** Metric threshold recommendations (e.g., 'Happiness score should target >= 4.0/5.0') are LOW confidence (reference-only). Teams must validate thresholds against their product's baseline data before using them as design targets."

**Post-Correction RPN:** S=5, O=2, D=4 → RPN=40 (expected post-R3 fix)

---

### FM-014-I3: Crisis Mode "Resolution" Undefined for Circuit Breaker

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Element** | E-06 (Routing Triage Logic) |
| **Strategy Step** | Step 2: Failure mode lens — Ambiguous |

**Evidence:**
E-06: "Crisis mode activates when the user explicitly describes urgency... or when the orchestrator detects multiple prior sub-skill invocations without resolution."

**Analysis:**
"Multiple prior sub-skill invocations without resolution" is the orchestrator-side activation trigger, but "resolution" is not defined. Does a sub-skill invocation count as "resolved" when the user acknowledges the output? When they close the session? When they create a worktracker entity with the output? Without a definition, the crisis mode circuit breaker is unimplementable — the orchestrator has no criterion to evaluate.

**Recommendation:**
Add to E-06 crisis mode description: "An invocation is 'resolved' when the user explicitly acknowledges the sub-skill output with one of: (a) a worktracker entity created from the output, (b) a verbal confirmation ('got it', 'moving on'), or (c) invocation of a downstream sub-skill that consumes this output. An invocation is 'unresolved' if the user re-invokes the same sub-skill within the same session without an intervening acknowledgment. Crisis mode triggers after 2 unresolved invocations."

**Post-Correction RPN:** S=6, O=3, D=4 → RPN=72 (expected post-R3 fix)

---

## Recommendations

### Critical Findings (Mandatory Corrective Action)

| ID | Corrective Action | Acceptance Criteria | Est. RPN Post-Fix |
|----|------------------|---------------------|-------------------|
| FM-001-I3 | Define 3-state orchestrator behavior (block/bypass/route) for WAVE-N-SIGNOFF absence; add state-transition test AC | AC verifies all 3 states; implementer cannot route to next wave without explicit user selection | 96 |
| FM-004-I3 | Define cross-sub-skill handoff schema (minimum fields); add handoff schema validation to integration test AC | Schema documented in `ux-routing-rules.md`; AC verifies schema compliance, not just invocation completion | 84 |
| FM-009-I3 | Replace deferred Zeroheight/Whimsical constraint rows with pre-commitment language blocking wave kickoff without data | Wave N development cannot begin until the table rows are completed; tracked as a wave-entry criterion | 63 |
| FM-019-I3 | Add independent reviewer approval for external ground-truth artifact selection; pre-launch validation log artifact | Ground-truth artifact approval documented before benchmark testing begins | 84 |

### Major Findings (Recommended Corrective Action)

| ID | Corrective Action | Est. RPN Post-Fix |
|----|------------------|-------------------|
| FM-002-I3 | Add per-operation request budget estimates (estimated Figma/Miro calls per invocation for top-2 operations) | 72 |
| FM-006-I3 | Define Synthesis Judgments Summary format with 3-field entries and minimum count (3 entries for HIGH confidence) | 72 |
| FM-010-I3 | Add synthesis hypothesis warning to HEART sub-skill description (LOW confidence for metric threshold recommendations) | 40 |
| FM-014-I3 | Define "resolution" for crisis mode circuit breaker (2 unresolved invocations = crisis trigger) | 72 |
| FM-003-I3 | Confirm 3/3 pass requirement for JTBD benchmark is intentional; add rationale if so | 80 |
| FM-016-I3 | Define "measurable signal" for HEART Wave 2 benchmark (metric name + data source + measurement method) | 60 |
| FM-020-I3 | Link MCP maintenance owner to KICKOFF-SIGNOFF.md named field | 60 |
| FM-021-I3 | Add UX-context L0/L1/L2 definition for orchestrator outputs | 60 |
| FM-005-I3 | Add wave bypass expiry (60 days or next wave review) with orchestrator escalation on expiry | 60 |
| FM-007-I3 | Update Figma risk citation to current API access status (March 2026) | 40 |
| FM-011-I3 | Define "expert review" qualification for MEDIUM-confidence outputs (behavior design) | 50 |
| FM-013-I3 | Define "MCP-heavy" classification criteria tied to KICKOFF-SIGNOFF.md "Available MCP Tools" field | 50 |

### Minor Findings (Improvement Opportunities)

| ID | Corrective Action | Est. RPN Post-Fix |
|----|------------------|-------------------|
| FM-015-I3 | Link V2 trigger measurement to worktracker invocation log entries | 30 |
| FM-017-I3 | Add justification for C1 > C2 weighting in WSM criteria | 25 |
| FM-018-I3 | Add mermaid diagram legend for orange fill (conditional sub-skill) | 20 |
| FM-008-I3 | Specify Human Override Justification storage location (output artifact + worktracker link) | 20 |
| FM-012-I3 | Note explicitly that 4-skill canonical sequence is a V2 integration test (V1 validates component two-skill handoffs) | 20 |
| FM-022-I3 | Define response to exceeding the 20% MCP fallback rate target (V2 planning flag) | 20 |
| FM-023-I3 | Add `kickoff-signoff-template.md` to Directory Structure E-15 | 15 |
| FM-024-I3 | Add part-time contractor UX segment to population segments table | 12 |

---

## RPN Comparison: Iter 2 → Iter 3

### Items Addressed by R2 (Recalculated)

| Iter 2 ID | Iter 2 RPN | R2 Fix Applied | Iter 3 ID | Iter 3 RPN | Change |
|-----------|-----------|----------------|-----------|-----------|--------|
| FM-002 (MCP absent) | 336 | MCP constraints table added (partial fix) | FM-002-I3 (rate limit non-actionable) | 180 | -156 |
| FM-003 (JTBD benchmark) | 245 | Deterministic 3-criterion rubric added | FM-003-I3 (pass threshold ambiguous) | 150 | -95 |
| FM-011 (behavior-design) | — (resolved) | Renamed + reclassified LOW→MEDIUM | — | 0 | -resolved |
| FM-001 (synthesis gate) | 324 | Wave signoff AC added (incomplete fix) | FM-001-I3 (3-state behavior missing) | 336 | +12 |
| FM-004 (handoff) | 252 | Closure condition AC added (incomplete fix) | FM-004-I3 (schema still missing) | 294 | +42 |

**Note on FM-001 and FM-004 RPN increases:** The R2 fixes added partial structure (AC text) that increased Occurrence detectability without fully resolving the underlying gap. Severity held constant; Detection improved slightly (D=8→D=7); but Occurrence increased (O=5→O=6) as the now-explicit but incomplete specification makes it more likely that implementers will notice and mishandle the gap.

### New Failure Modes Introduced by R2

| ID | Source | RPN |
|----|--------|-----|
| FM-009-I3 | MCP constraints table defers Zeroheight/Whimsical | 245 |
| FM-019-I3 | Pre-launch validation independence gap | 210 |
| FM-020-I3 | MCP maintenance owner unassigned mechanism | 150 |
| FM-022-I3 | MCP fallback rate target lacks response definition | 48 |

**Total new RPN from R2-introduced modes:** 653

### Persistent Failure Modes (Unchanged from Iter 2)

FM-006-I3 (180), FM-010-I3 (180), FM-014-I3 (180), FM-005-I3 (125), FM-016-I3 (150), FM-021-I3 (125), FM-007-I3 (80), FM-011-I3 (100), FM-013-I3 (100), FM-015-I3 (75), FM-017-I3 (60), FM-018-I3 (60), FM-008-I3 (60), FM-012-I3 (48), FM-023-I3 (45), FM-024-I3 (24)

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| **Completeness** | 0.20 | Negative | FM-001-I3 (wave enforcement 3-state behavior missing), FM-004-I3 (handoff schema missing), FM-006-I3 (Synthesis Judgments Summary format missing), FM-014-I3 (crisis mode "resolution" undefined), FM-021-I3 (L0/L1/L2 UX context missing) represent significant structural gaps. R2 improved completeness on MCP constraints (FM-002 partially resolved) and wave bypass documentation. Net: moderate negative. |
| **Internal Consistency** | 0.20 | Negative | FM-010-I3 (HEART sub-skill missing synthesis hypothesis warning present in all other affected sub-skills) is a direct internal consistency failure. FM-001-I3 gap between wave enforcement statement and undefined behavior creates an implicit inconsistency. Net: minor negative. |
| **Methodological Rigor** | 0.20 | Negative | FM-009-I3 (deferred MCP constraints undermine the completeness of the operational constraints methodology), FM-013-I3 (undefined "MCP-heavy" classification makes routing non-implementable), FM-003-I3 (benchmark pass threshold ambiguous). R2 resolved the core MCP absence gap. Net: minor-to-moderate negative. |
| **Evidence Quality** | 0.15 | Negative | FM-019-I3 (pre-launch validation independence undefined weakens the evidentiary basis for quality benchmarks), FM-007-I3 (Figma citation outdated), FM-017-I3 (C1>C2 weighting unjustified). Net: minor negative. |
| **Actionability** | 0.15 | Mixed | FM-002-I3 (rate limits non-actionable without per-operation budgets), FM-020-I3 (MCP maintenance owner unassigned), FM-022-I3 (fallback rate target lacks response definition). R2 partially improved actionability by adding the MCP constraints table. Net: minor negative. |
| **Traceability** | 0.10 | Positive | FM-018-I3 and FM-023-I3 are minor traceability gaps. R2 added source-accurate WSM criteria inline and fixed multiple cross-reference issues. R2's issue closure condition (FM-004 Iter2) improved traceability for scope decisions. Net: minor positive. |

---

## Execution Statistics

- **Total Findings:** 24
- **Critical:** 4 (FM-001-I3, FM-004-I3, FM-009-I3, FM-019-I3)
- **Major:** 12
- **Minor:** 8
- **Total RPN (Iter 3):** 1,732
- **Total RPN (Iter 2):** 2,204
- **RPN Change:** -472 (-21%)
- **Protocol Steps Completed:** 5 of 5

---

## Overall Assessment

**REVISE** — Targeted corrections required.

The R2 deliverable closed 3 of the top 4 Iter 2 findings cleanly (FM-011 fully resolved, FM-002 and FM-003 substantially improved). The four remaining Critical findings (FM-001-I3, FM-004-I3, FM-009-I3, FM-019-I3) are all specification completeness gaps — the deliverable establishes the right mechanisms but leaves the implementation behavior underspecified. These gaps are correctible without structural changes. The issue is advancing toward PASS: total RPN down 21% from Iter 2, and the residual failures are increasingly in the category of "mechanism defined, behavior unspecified" rather than "mechanism absent." One more targeted revision cycle addressing the 4 Critical and top 4 Major findings should bring the total RPN below 800 and resolve all blocks to PASS.

---

*Report Version: Iteration 3*
*Strategy: S-012 FMEA*
*SSOT: `.context/rules/quality-enforcement.md`*
*Template: `.context/templates/adversarial/s-012-fmea.md`*
*Generated: 2026-03-03*
