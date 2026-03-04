# Strategy Execution Report: Inversion Technique (S-013)

## Execution Context
- **Strategy:** S-013 (Inversion Technique)
- **Template:** `.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `skills/user-experience/SKILL.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 6 (C4 tournament)
- **Finding Prefix:** IN-NNN-006

---

# Inversion Report: User-Experience SKILL.md

**Strategy:** S-013 Inversion Technique
**Deliverable:** `skills/user-experience/SKILL.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-013)
**H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (confirmed by prior strategy outputs in tournament sequence)
**Goals Analyzed:** 7 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 6

---

## Summary

Between iteration 4 and iteration 6, the SKILL.md incorporated significant fixes: the deployment status disclosure is now present (IN-001-004 partially addressed), the CRISIS sequence is consistent between SKILL.md and ux-routing-rules.md (IN-006-004 resolved), and Wave 1 agent stubs now exist as physical files. However, inversion analysis on the current state surfaces 6 remaining vulnerable assumptions — 2 Critical and 4 Major. The two new Critical findings concern (1) the complete absence of orchestrator `<methodology>` content in the ux-orchestrator stub despite that stub now being declared the active Wave 0 deliverable, and (2) the `handoff-v2.schema.json` reference marked "pending file creation" in SKILL.md while the cross-sub-skill handoff protocol claims to rely on it. These remain structural failure conditions that would prevent runtime operation. The recommendation is **REVISE** — three legacy Major findings from iteration 4 are unresolved and two new Critical gaps have emerged from the stub-to-implementation transition.

---

## Prior Findings Resolution Status

| Prior ID | Finding | Status in Iteration 6 |
|----------|---------|----------------------|
| IN-001-004 (Critical) | Sub-skill deployment status undisclosed | RESOLVED — SKILL.md Purpose section now discloses "not yet deployed" status explicitly |
| IN-002-004 (Critical) | Wave gate enforcement mechanism absent | PARTIALLY RESOLVED — wave-progression.md has canonical SIGNOFF path; signoff schema, bypass ceiling, and orchestrator pre-routing check remain stub |
| IN-003-004 (Major) | Synthesis confidence category inaccessible to orchestrator | UNRESOLVED — synthesis-validation.md still entirely stub |
| IN-004-004 (Major) | Capacity check single-question reliability | UNRESOLVED — ux-routing-rules.md Section "Lifecycle Stage Router" still "Pending implementation" for anchored capacity prompt |
| IN-005-004 (Major) | Bypass accumulation risk — no ceiling or audit log | UNRESOLVED — wave-progression.md Bypass Mechanism still stub; no ceiling or WAVE-BYPASS-LOG defined |
| IN-006-004 (Major) | CRISIS sequence discrepancy + blunt routing | RESOLVED — ux-routing-rules.md now shows `Heuristic Eval → Behavior Design → HEART` matching SKILL.md |
| IN-007-004 (Major) | Signal extraction format contract absent | UNRESOLVED — synthesis-validation.md Synthesis Protocol Validation still stub |

**Carry-forward unresolved (3 Major):** IN-003-004, IN-004-004, IN-005-004, IN-007-004 (renumbered as IN-003-006, IN-004-006, IN-005-006, IN-007-006 in this report).

---

## Findings Summary

| ID | Assumption / Anti-Goal | Type | Confidence | Severity | Evidence | Affected Dimension |
|----|------------------------|------|------------|----------|----------|--------------------|
| IN-001-006 | ux-orchestrator stub has no `<methodology>` — the only Wave 0 agent cannot route or synthesize | Assumption (Technical) | Low | Critical | `skills/user-experience/agents/ux-orchestrator.md` lines 29-67 | Completeness |
| IN-002-006 | `handoff-v2.schema.json` is referenced as foundational but marked "pending file creation" | Assumption (Process) | Low | Critical | `skills/user-experience/SKILL.md` line 617 | Methodological Rigor |
| IN-003-006 | Synthesis confidence gate assumes orchestrator knows per-sub-skill confidence categories | Assumption (Technical) | Medium | Major | `skills/user-experience/rules/synthesis-validation.md` lines 20-50 | Internal Consistency |
| IN-004-006 | Capacity check single question reliably classifies < 20% vs 20-50% capacity | Assumption (Resource) | Medium | Major | `skills/user-experience/rules/ux-routing-rules.md` CAPACITY CHECK unimplemented | Evidence Quality |
| IN-005-006 | Wave bypass documentation (3 fields) prevents systemic wave skipping | Assumption (Process) | Medium | Major | `skills/user-experience/rules/wave-progression.md` lines 43-52 | Methodological Rigor |
| IN-006-006 | Signal extraction correctly identifies convergent signals across heterogeneous sub-skill output formats | Assumption (Technical) | Low | Major | `skills/user-experience/rules/synthesis-validation.md` lines 30-34 | Internal Consistency |

---

## Step 1: Goal Inventory (Unchanged from Iteration 4)

| Goal | Description | Source |
|------|-------------|--------|
| G-1: Lifecycle Routing | Route tiny teams to the correct UX framework specialist based on product stage | SKILL.md §Lifecycle-Stage Routing |
| G-2: Wave-Gated Quality | Prevent premature use of advanced sub-skills before foundational work is complete | SKILL.md §Wave Architecture |
| G-3: AI-Bias Mitigation | Prevent teams from acting on hallucinated synthesis outputs | SKILL.md §Synthesis Hypothesis Validation |
| G-4: Incremental Adoption | Enable teams to start with Wave 1 and progress without re-architecting | SKILL.md §Wave Architecture |
| G-5: Framework Integrity | Preserve methodological fidelity to 10 proven UX frameworks | SKILL.md §Purpose, §Available Agents |
| G-6: Orchestration Reliability | Ensure ux-orchestrator correctly sequences multi-skill workflows without P-003 violations | SKILL.md §P-003 Compliance |
| G-7: Tiny-Team Calibration | Remain usable at 20-50% of one person's time | SKILL.md §Purpose |

---

## Step 2: Anti-Goals (Updated for Iteration 6 State)

| Goal | Anti-Goal (Guaranteed Failure Conditions) | Addressed by Current State? |
|------|------------------------------------------|-----------------------------|
| G-1: Lifecycle Routing | Orchestrator receives a routing request but has no `<methodology>` to execute triage; returns a generic LLM response that bypasses the 4-step routing logic | NOT ADDRESSED — ux-orchestrator.md stub contains only `<identity>`, `<purpose>`, and `<guardrails>`; the `<methodology>` section (where the 4-step triage lives) is absent |
| G-2: Wave-Gated Quality | Wave gate check references WAVE-N-SIGNOFF.md but no cross-sub-skill handoff schema exists to populate the signoff artifact | PARTIALLY ADDRESSED — canonical path defined (wave-progression.md line 60) but signoff schema contents and orchestrator pre-routing check logic remain stub |
| G-3: AI-Bias Mitigation | Orchestrator runs cross-framework synthesis after Wave 2 without knowing per-sub-skill confidence categories; assigns MEDIUM to all outputs | NOT ADDRESSED — synthesis-validation.md confidence classification section stub; orchestrator has no embedded confidence lookup |
| G-4: Incremental Adoption | Wave 1 agent stubs exist as files but contain no methodology; user invokes Wave 1 and receives a stub identity section with no operational behavior | PARTIALLY ADDRESSED — agent stubs created; stub state explicitly disclosed; but stub agents cannot execute their described frameworks |
| G-5: Framework Integrity | Cross-sub-skill handoffs use a schema that does not exist (handoff-v2.schema.json pending); data is lost at every sub-skill boundary | NOT ADDRESSED — SKILL.md line 617 explicitly notes schema is "pending file creation" |
| G-6: Orchestration Reliability | ux-orchestrator invokes sub-skills via Task but sub-skill `subagent_type` values point to agent names not yet resolvable as Claude Code agents (stubs only) | PARTIALLY ADDRESSED — SKILL.md now discloses stub status; stubs exist at correct paths; but no methodology to handle Task failures gracefully |
| G-7: Tiny-Team Calibration | Team uses wave bypass 3 consecutive times to reach Wave 5 without any methodology foundation; orchestrator does not detect cumulative bypass state | NOT ADDRESSED — bypass ceiling (max 2) mentioned in SKILL.md §Wave Architecture but not implemented in wave-progression.md bypass mechanism section |

---

## Step 3: Assumption Map (Iteration 6 — New and Carry-Forward)

| ID | Assumption | Type | Confidence | Validation Status | Failure Consequence |
|----|-----------|------|------------|-------------------|---------------------|
| A-01 | ux-orchestrator will have a `<methodology>` section implementing 4-step triage when EPIC-001 delivers | Technical (stub state) | Low | Not validated — stub exists without methodology placeholder or section stub | Orchestrator responds to UX requests as a generic LLM without the 4-step routing protocol; lifecycle routing goal (G-1) fails completely |
| A-02 | handoff-v2.schema.json will be created before cross-sub-skill handoffs are needed at Wave 2 | Process (schema dependency) | Low | Not validated — SKILL.md notes "pending file creation"; no worktracker tracking of this dependency | UX-specific handoff data (job statements, severity-rated findings, validated prototypes) is transmitted as unstructured text; data fidelity lost at every sub-skill boundary |
| A-03 | The orchestrator possesses per-sub-skill synthesis confidence category knowledge at invocation time | Technical (data access) | Medium | Partially validated — SKILL.md provides the Sub-Skill Synthesis Output Map table; orchestrator stub has no reference to this table | Orchestrator assigns wrong confidence tier; LOW output presented as MEDIUM; P-022 violated |
| A-04 | A single capacity question reliably classifies teams into < 20%, 20-50%, or > 50% UX time allocation | Resource (measurement) | Medium | Not validated — no anchoring example, no prior-completion secondary check defined | Teams overestimate capacity; receive Wave 3-5 routing; abandon methodology mid-cycle |
| A-05 | The 3-field wave bypass prevents teams from bypassing all 5 waves consecutively | Process (governance) | Medium | Not validated — bypass ceiling "max 2 concurrent bypasses" stated in SKILL.md but not implemented in wave-progression.md | Teams bypass Waves 1-4 in one session; Design Sprint executes without any framework calibration |
| A-06 | Signal extraction correctly identifies convergent signals across heterogeneous sub-skill output formats | Technical (parsing) | Low | Not validated — sub-skill output formats not yet specified; synthesis relies on section name matching across non-uniform formats | False convergence detected; HIGH confidence applied to mismatched findings; P-022 violated |
| A-07 | Session state flag ("ONBOARD fires once per session") is implemented and reliable across LLM context resets | Technical (state) | Low | Not validated — no state mechanism described; ux-orchestrator stub has no state management | ONBOARD fires on every invocation within session causing HIGH RISK warning fatigue; or ONBOARD never fires after context compaction |
| A-08 | The WSM >= 7.80 conditional gate for ux-ai-design-guide is measurable and the WSM metric has been defined | Process (gate logic) | Low | Not validated — WSM (Weighted Skill Maturity?) metric not defined anywhere in SKILL.md or referenced files | ux-ai-design-guide invoked without the Enabler prerequisite; AI-first design on insufficient foundation |
| A-09 | The 0.85 wave transition threshold reliably discriminates deployment-ready from not-ready | Process (measurement) | Medium | Not validated — ADR-PROJ022-002 explicitly marked DRAFT; threshold provisional | Gate permits low-quality sub-skill deployment at 0.85; OR blocks high-quality deployment when calibration artifact is atypical |
| A-10 | The ux-routing-rules.md routing table operates correctly without the Dispatch logic step (which remains a stub) | Process (implementation) | Low | Not validated — ux-routing-rules.md "PARTIAL IMPLEMENTATION: Routing table populated. Full dispatch logic in EPIC-001" | Routing table exists as documentation but dispatch logic (step 4 of 4-step triage) does not yet map table entries to actual Task invocations |
| A-11 | The "< 20% capacity: recommend Wave 1 only" check works when user declines to provide capacity information | Process (P-020 compliance) | Medium | Not validated — P-020 says user decides; if user refuses to answer capacity question, triage stalls or defaults arbitrarily | Orchestrator blocks routing until capacity answer received (P-020 violation) OR skips check silently and routes to Wave 5 |
| A-12 | Wave 1 agent stubs can be extended to full implementations without changing their file paths or frontmatter agent names | Technical (migration) | Medium | Partially validated — stub files at correct paths per SKILL.md References table | If stub-to-implementation requires file restructuring, all SKILL.md References paths become stale |
| A-13 | The `<input>` section of sub-skill agents (absent in all stubs) will receive the correct UX context fields from the orchestrator when EPIC-002 implements them | Technical (handoff interface) | Low | Not validated — ux-orchestrator stub shows Task invocation template (SKILL.md lines 222-241) but sub-skill stubs have no `<input>` section defining expected fields | Orchestrator passes fields (Engagement ID, Topic, Product, Target Users) but sub-skill agents expect different or additional fields; handoff data mismatch at Wave 1 |
| A-14 | The SKILL.md navigation table and all 15 section anchors remain correct as EPIC-001 updates stub files and adds new content | Process (documentation integrity) | Medium | Partially validated — navigation table exists; all anchors verified in current SKILL.md | As stub files are implemented in EPIC-001, SKILL.md cross-references to specific line numbers and section names may drift; NAV-001/H-23 violations accumulate silently |

---

## Detailed Findings

### IN-001-006: ux-orchestrator Stub Has No `<methodology>` — Wave 0 Agent Is Non-Operational [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | `skills/user-experience/agents/ux-orchestrator.md` |
| **Strategy Step** | Step 2 (Anti-Goals) + Step 4 (Stress-Test) |

**Evidence:**

The ux-orchestrator.md stub contains exactly three XML sections (lines 39-77):
```
<identity>    (9 lines: role, expertise, cognitive mode)
<purpose>     (8 lines: existence justification)
<guardrails>  (12 lines: P-003/P-020/P-022 + 3 forbidden actions)
```

Missing sections per `agent-development-standards.md` [Markdown Body Sections]: `<input>`, `<capabilities>`, `<methodology>`, `<output>`.

The `<methodology>` section is where the 4-step lifecycle triage lives — ONBOARD, CAPACITY CHECK, MCP CHECK, STAGE TRIAGE. SKILL.md lines 292-315 describe this triage in detail but the orchestrator's system prompt contains none of it. Without `<methodology>`, the ux-orchestrator receives UX requests and responds as a generic Opus LLM rather than executing the documented routing protocol.

**Analysis:**

The iteration 4 Critical finding IN-001-004 was addressed by adding deployment status disclosure to SKILL.md. That was the documentation gap. The implementation gap persists: the ux-orchestrator is now the declared Wave 0 deliverable (the only fully described "deployed" component), but its agent definition omits the most critical section. A stub with only `<identity>`, `<purpose>`, and `<guardrails>` cannot route, gate, or synthesize. Any user invoking `/user-experience` after Wave 0 signoff will interact with an agent that knows what it is but not what to do.

The inversion is direct: to guarantee lifecycle routing fails, ensure the routing methodology is documented in SKILL.md but absent from the agent that executes it.

**Recommendation:**

Add a `<methodology>` section to ux-orchestrator.md that includes at minimum a stub placeholder for each of the 4 triage steps with explicit EPIC-001 TODO markers, and an `<input>` section defining the expected UX context fields. This does not need to be fully implemented — it needs to exist so EPIC-001 has a structural scaffold to fill in rather than creating the section from scratch.

**Acceptance Criteria:**
- ux-orchestrator.md contains all 7 XML sections from the agent-development-standards.md [Markdown Body Sections] schema
- The `<methodology>` section names each of the 4 triage steps (ONBOARD, CAPACITY CHECK, MCP CHECK, STAGE TRIAGE) as explicit subsections or TODO stubs
- The `<input>` section defines the UX context fields expected from user or orchestration handoff

---

### IN-002-006: handoff-v2.schema.json Referenced as Foundational but Marked "Pending File Creation" [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | `skills/user-experience/SKILL.md` line 617 |
| **Strategy Step** | Step 2 (Anti-Goals) + Step 4 (Stress-Test) |

**Evidence:**

SKILL.md §References → Standards References (line 617):
```
| Handoff Schema | `docs/schemas/handoff-v2.schema.json` (canonical path per
  `agent-development-standards.md`; file pending creation) |
```

SKILL.md §Cross-Skill Integration (line 470):
```
Handoffs use the Jerry handoff protocol (schema specified in
`agent-development-standards.md` [Handoff Protocol]; canonical path
`docs/schemas/handoff-v2.schema.json`, pending file creation)
```

SKILL.md §Cross-Sub-Skill Handoff Data (lines 472-480) lists 6 specific handoff types with UX-specific artifact types (job statement + switch forces; validated prototype + Day 4 findings; severity-rated findings; etc.).

The handoff-v2.schema.json is described as the structural contract for all cross-sub-skill data exchange. It does not exist.

**Analysis:**

Inverting Goal G-5 (Framework Integrity): to guarantee framework data is lost at every sub-skill boundary, ensure the handoff schema that would constrain data format does not exist. This is the current state. Each EPIC team implementing a Wave N sub-skill will define their own output structure. When the orchestrator performs cross-framework synthesis in Wave 2+, the signal extraction step (SKILL.md lines 373-376) relies on consistent finding formats across sub-skills — but without a schema contract, each sub-skill will independently define its "findings/recommendations sections." The synthesis step will fail silently (no error, just incorrect convergence detection) because heterogeneous formats look similar enough to parse but yield different semantics.

This is distinct from IN-007-006 (the signal extraction format contract): IN-002-006 is about the structural handoff schema that governs how sub-skills exchange intermediate artifacts (job statements, prototype references, severity findings) between themselves; IN-007-006 is about the synthesis signal extraction format within individual sub-skill outputs.

**Recommendation:**

`docs/schemas/handoff-v2.schema.json` should be created before Wave 1 implementation begins in EPIC-002 (not EPIC-001). The UX-specific fields needed beyond the generic handoff-v2 fields should be documented in a UX handoff extensions spec in `skills/user-experience/rules/ux-routing-rules.md` [Handoff Schema] section (currently stub). Minimum: the 6 handoff types from SKILL.md §Cross-Sub-Skill Handoff Data must map to specific JSON Schema fields before the first cross-sub-skill handoff is implemented.

**Acceptance Criteria:**
- `docs/schemas/handoff-v2.schema.json` exists as a valid JSON Schema file before Wave 1 handoff paths are implemented (ux-jtbd → ux-design-sprint; ux-jtbd → ux-kano-model)
- `skills/user-experience/rules/ux-routing-rules.md` [Handoff Schema] section is non-stub and defines the UX-specific artifact types mapped to handoff-v2 fields
- SKILL.md §References line 617 drops the "pending file creation" annotation

---

### IN-003-006: Synthesis Confidence Gate Inaccessible to Orchestrator Runtime [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/synthesis-validation.md` lines 20-34 |
| **Strategy Step** | Step 4 (Stress-Test) — carry-forward from IN-003-004 |

**Evidence:**

`synthesis-validation.md` Confidence Classification section (lines 19-26):
```
<!-- TODO (EPIC-001): Define confidence gates with thresholds per P-022. -->
Pending implementation. All synthesis hypotheses MUST include confidence classification:
- HIGH: 3+ frameworks converge on the same finding
- MEDIUM: 2 frameworks converge OR 1 framework with strong evidence
- LOW: Single framework finding, weak evidence, or contradiction present
```

The Synthesis Protocol Validation, Convergence Thresholds, and Contradiction Handling sections are all "Pending implementation."

The ux-orchestrator stub system prompt contains no reference to synthesis-validation.md, no embedded confidence lookup table, and no methodology section where lookup logic could be placed.

**Analysis:**

The inversion: to guarantee AI-bias mitigation fails, ensure the confidence classification rules exist in a prose document (SKILL.md §Sub-Skill Synthesis Output Map) but are not accessible to the agent that enforces them. The orchestrator must classify each synthesis signal's confidence tier at invocation time. Without the table embedded in its system prompt or a defined mechanism to read synthesis-validation.md at runtime, the orchestrator will apply heuristic confidence rather than the specified classification. P-022 is cited as the enforcement rationale for synthesis confidence gates — if the mechanism is absent, the P-022 commitment is unfulfilled.

**Recommendation:**

synthesis-validation.md must have all 4 sections populated (non-stub) before Wave 2 synthesis is first attempted. The ux-orchestrator `<methodology>` section (created via IN-001-006 mitigation) must explicitly name synthesis-validation.md as the lookup source and define the lookup step: "Before classifying synthesis output confidence, Read synthesis-validation.md [Confidence Classification] and apply the per-sub-skill table."

**Acceptance Criteria:**
- synthesis-validation.md has all 4 sections non-stub with specific gate thresholds (not just "Pending implementation")
- ux-orchestrator `<methodology>` includes an explicit "Confidence Lookup" step that names synthesis-validation.md as the source
- At least one sub-skill's synthesis output is tested against the confidence gate before Wave 2 synthesis is declared complete

---

### IN-004-006: Capacity Check Single-Question Reliability — Unanchored Self-Report [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/ux-routing-rules.md` — CAPACITY CHECK section |
| **Strategy Step** | Step 4 (Stress-Test) — carry-forward from IN-004-004 |

**Evidence:**

ux-routing-rules.md §Lifecycle Stage Router (lines 26-28):
```
2. CAPACITY CHECK: Ask team UX time allocation. If < 20% of one person's
   time: recommend Wave 1 sub-skills only (P-020: user decides)
```

No anchoring example (e.g., "2h/sprint = < 20%"), no secondary confirmation check, no defined fallback when user declines to answer. The routing-rules.md comment notes: "PARTIAL IMPLEMENTATION: Routing table populated. Full dispatch logic in EPIC-001."

**Analysis:**

The inversion: to guarantee tiny-team calibration fails, let teams self-report capacity using an unanchored question at the start of an engagement when enthusiasm and optimism are highest. "About 30% of my time" is the most common initial estimate from teams who actually have 2-3 hours per week — which is 5-7% of one person's time. Routing a 5%-capacity team to Lean UX (Wave 2) or Atomic Design (Wave 3) produces a multi-sprint commitment the team cannot sustain. Wave signoffs are never achieved. The wave progression stalls. No finding will ever surface this failure because the capacity mismatch produces abandonment, not error output.

**Recommendation:**

When ux-routing-rules.md receives its EPIC-001 full implementation, the CAPACITY CHECK must include:
1. An anchoring example: "Approximately how many hours per sprint do you spend on UX-related work? (For reference: 2h/sprint ≈ less than 20%; 8h/sprint ≈ 25-40%)"
2. A prior-completion secondary: "Have you previously completed a UX methodology cycle — e.g., a full heuristic evaluation from start to findings report?" Teams with no prior completion are treated as Wave 1-only regardless of stated hours (a P-020-compliant recommendation, not a restriction)

**Acceptance Criteria:**
- ux-routing-rules.md CAPACITY CHECK documents the anchoring example with sprint-hours reference points
- ux-routing-rules.md CAPACITY CHECK documents behavior when user refuses to answer (default: recommend Wave 1)
- The anchored capacity question is included in the ux-orchestrator `<methodology>` stub as a named step

---

### IN-005-006: Wave Bypass Accumulation — Ceiling Stated in SKILL.md but Not Implemented in Rules [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/wave-progression.md` lines 43-52 |
| **Strategy Step** | Step 4 (Stress-Test) — carry-forward from IN-005-004 |

**Evidence:**

SKILL.md §Wave Architecture (line 279): "**Cumulative ceiling:** Maximum 2 concurrent bypasses per team. If a team has 2 active bypasses, the orchestrator requires remediation of at least one before granting additional bypasses."

wave-progression.md §Bypass Mechanism (lines 43-52):
```
<!-- TODO (EPIC-001): Define 3-field bypass documentation requirements. -->
Pending implementation. Bypass fields:
1. Unmet criterion
2. Impact assessment
3. Remediation plan
User approval required per P-020.
```

No ceiling, no enforcement mechanism, no WAVE-BYPASS-LOG.md format.

**Analysis:**

The inversion: to guarantee wave-gated quality fails, implement a bypass mechanism that can be invoked 5 consecutive times without any cumulative state enforcement. The SKILL.md states the ceiling (max 2 concurrent) as a governance constraint; wave-progression.md is where the orchestrator looks for bypass rules. The ceiling is documented in one file and absent from the enforcement file. An EPIC-001 developer building the bypass mechanism from wave-progression.md will implement 3-field documentation without a ceiling because wave-progression.md specifies no ceiling. The SKILL.md ceiling will become a documentation artifact with no behavioral backing.

**Recommendation:**

wave-progression.md §Bypass Mechanism must be updated (before EPIC-001 implements bypass) to include:
1. The max-2-concurrent-bypasses ceiling, with explicit statement that bypass count 3+ requires remediation of at least one prior bypass
2. WAVE-BYPASS-LOG.md format: `{engagement-id}/{bypass-id}/{wave-bypassed}/{fields}/{timestamp}`
3. Bypass state query: orchestrator checks WAVE-BYPASS-LOG.md count before presenting bypass prompt; if count >= 2, refuses bypass and presents remediation prompt

**Acceptance Criteria:**
- wave-progression.md §Bypass Mechanism specifies the 2-concurrent ceiling with enforcement steps
- wave-progression.md §Bypass Mechanism specifies WAVE-BYPASS-LOG.md path and format
- ux-orchestrator `<methodology>` stub names bypass ceiling check as a pre-bypass step

---

### IN-006-006: Cross-Framework Synthesis Signal Extraction Has No Format Contract [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/synthesis-validation.md` lines 30-34 |
| **Strategy Step** | Step 4 (Stress-Test) — carry-forward from IN-007-004 |

**Evidence:**

SKILL.md §Cross-Framework Synthesis Protocol (lines 373-376):
```
1. Signal Extraction: The orchestrator reads each sub-skill output's
   findings/recommendations sections and extracts actionable signals
   (findings rated severity >= 2 for heuristic eval; metrics below target
   for HEART; unvalidated assumptions for Lean UX; etc.).
```

synthesis-validation.md §Synthesis Protocol Validation (lines 30-34):
```
<!-- TODO (EPIC-001): Define validation checks for each of the 4 synthesis steps. -->
Pending implementation. Validates: Signal Extraction, Convergence Detection,
Contradiction Identification, Unified Output.
```

No standardized `## Synthesis Signals` section is defined for sub-skill outputs. No cross-sub-skill output format contract exists.

**Analysis:**

The inversion: to guarantee cross-framework synthesis produces unreliable convergence detection, allow each sub-skill EPIC team to independently implement their output format. ux-heuristic-evaluator uses "Severity: 3"; ux-heart-analyst uses "Status: Below Target"; ux-lean-ux-facilitator uses "Validated: false". The orchestrator's signal extraction reads for "severity >= 2" in one format and "below target" in another — producing false convergence when "Severity: 1" and "Slightly Below Target" appear in adjacent sections, or missing real convergence because severity notation differs.

Unlike IN-003-006 (the confidence classification lookup problem), this finding is about the sub-skill output structure rather than the orchestrator lookup mechanism. Both must be solved: sub-skills must produce standardized signal sections (this finding), and the orchestrator must know which confidence tier to assign (IN-003-006).

**Recommendation:**

synthesis-validation.md §Synthesis Protocol Validation must define a minimal standardized `## Synthesis Signals` section that every sub-skill output MUST produce. Minimum format:
```
## Synthesis Signals
- Signal: {1-line finding description} | Severity: {1-4} | Framework: {framework-name} | Status: {confirmed|unvalidated}
```
This section is read-only by the orchestrator during signal extraction. Wave 1 sub-skills (ux-heuristic-evaluator, ux-jtbd-analyst) must implement this section before Wave 2 synthesis is first attempted.

**Acceptance Criteria:**
- synthesis-validation.md §Synthesis Protocol Validation defines the `## Synthesis Signals` section format
- ux-heuristic-evaluator and ux-jtbd-analyst output templates include the `## Synthesis Signals` section before Wave 2 signoff
- The orchestrator's signal extraction step in `<methodology>` reads only the `## Synthesis Signals` section, not free-text findings prose

---

## Step 5: Recommendations

### Critical Findings — MUST Mitigate

**IN-001-006: ux-orchestrator Missing `<methodology>` Section**
- Action: Add all 7 XML sections to ux-orchestrator.md; `<methodology>` must name the 4 triage steps as stubs with EPIC-001 TODO markers; `<input>` must define UX context fields
- Acceptance Criteria: ux-orchestrator.md has 7 XML sections; `<methodology>` names ONBOARD, CAPACITY CHECK, MCP CHECK, STAGE TRIAGE as explicit stubs; agent-development-standards.md [Markdown Body Sections] compliance verified

**IN-002-006: handoff-v2.schema.json Not Created**
- Action: Create `docs/schemas/handoff-v2.schema.json` before Wave 1 implementation begins; populate ux-routing-rules.md [Handoff Schema] with UX-specific artifact field mappings; remove "pending file creation" annotation from SKILL.md
- Acceptance Criteria: Schema file exists; 6 UX handoff types from SKILL.md mapped to schema fields; SKILL.md line 617 updated; tracked as EPIC-001 dependency

### Major Findings — SHOULD Mitigate

**IN-003-006: Synthesis Confidence Gate Inaccessible**
- Action: Populate synthesis-validation.md all 4 sections before Wave 2; add confidence lookup step to ux-orchestrator `<methodology>` stub
- Acceptance Criteria: synthesis-validation.md non-stub; ux-orchestrator methodology names synthesis-validation.md as lookup source

**IN-004-006: Capacity Check Unanchored**
- Action: Add anchoring example (hours/sprint reference) and prior-completion secondary check to ux-routing-rules.md CAPACITY CHECK when EPIC-001 implements dispatch logic
- Acceptance Criteria: Anchored capacity question documented in ux-routing-rules.md; behavior on refusal defined

**IN-005-006: Bypass Ceiling Not Implemented in Rules**
- Action: Add 2-concurrent-bypass ceiling, WAVE-BYPASS-LOG.md format, and pre-bypass orchestrator check to wave-progression.md §Bypass Mechanism
- Acceptance Criteria: wave-progression.md Bypass Mechanism non-stub with ceiling and audit log format

**IN-006-006: Signal Extraction Format Contract Absent**
- Action: Define `## Synthesis Signals` standardized section format in synthesis-validation.md; require Wave 1 sub-skills to implement before Wave 2
- Acceptance Criteria: synthesis-validation.md defines signal section format; Wave 1 implementation includes the section

---

## Scoring Impact

| Dimension | Weight | Impact | Findings Driving Impact |
|-----------|--------|--------|------------------------|
| Completeness | 0.20 | Negative | IN-001-006 — the only deployed agent lacks 4 of 7 required sections including the methodology that implements the skill's core routing capability; the skill's operational promise cannot be delivered by the current orchestrator stub |
| Internal Consistency | 0.20 | Negative | IN-003-006, IN-006-006 — synthesis confidence classification is documented in SKILL.md but inaccessible to the orchestrator; signal extraction assumes uniform output format across stubs that have no format contract |
| Methodological Rigor | 0.20 | Negative | IN-002-006, IN-005-006 — handoff schema is foundational to all cross-sub-skill data exchange and does not exist; bypass ceiling is stated in SKILL.md but absent from the rule file that implements it |
| Evidence Quality | 0.15 | Negative | IN-004-006 — capacity routing decision relies on a single unanchored self-report question; routing to multi-sprint methodology frameworks for a < 20% capacity team is a high-consequence mismatch with no calibration anchor |
| Actionability | 0.15 | Positive | All 6 findings have specific mitigations with concrete acceptance criteria; findings identify the specific file and section requiring action; no finding requires architectural revision — all require spec additions to existing stub files |
| Traceability | 0.10 | Neutral | Framework citations, standards references, and iteration 4 finding carry-forward are well traced; all findings reference specific line numbers and file paths; prior finding resolution table is explicit about what was and was not addressed |

**Overall Assessment: REVISE**

The SKILL.md has addressed 2 of 7 prior Critical/Major findings (IN-001-004 deployment disclosure, IN-006-004 CRISIS sequence) and partially addressed 1 more (IN-002-004 wave path definition). Two new Critical gaps have emerged as the skill transitions from pure design documentation to a hybrid design-plus-stub state: the orchestrator stub is incomplete (missing methodology), and the handoff schema foundational to cross-sub-skill data exchange does not yet exist. Four Major findings carry forward unresolved. None require architectural revision — all require specific additions to stub files already created during the Foundation phase. The deliverable's design remains sound; the implementation scaffolding (stub completeness, schema creation, enforcement rules) requires targeted additions before Wave 1 implementation can produce an operationally reliable skill.

---

## Execution Statistics
- **Total Findings:** 6
- **Critical:** 2
- **Major:** 4
- **Minor:** 0
- **Protocol Steps Completed:** 6 of 6
- **Goals Analyzed:** 7
- **Assumptions Mapped:** 14
- **Anti-Goal Conditions Identified:** 7 per goal (49 conditions assessed)
- **Vulnerable Assumptions:** 6 (stress-tested with IN-NNN-006 identifiers)
- **Prior Findings Resolved:** 2 of 7 (IN-001-004 fully, IN-006-004 fully)
- **Prior Findings Partially Addressed:** 1 of 7 (IN-002-004)
- **Prior Findings Carry-Forward:** 4 of 7 (IN-003-004, IN-004-004, IN-005-004, IN-007-004)
- **New Findings Introduced:** 2 (IN-001-006, IN-002-006)
