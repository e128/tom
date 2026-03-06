# Strategy Execution Report: Inversion Technique (S-013)

## Execution Context
- **Strategy:** S-013 (Inversion Technique)
- **Template:** `.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `skills/user-experience/SKILL.md`
- **Executed:** 2026-03-04T00:00:00Z
- **Iteration:** 7 (C4 tournament)
- **Finding Prefix:** IN-NNN-007

---

# Inversion Report: User-Experience SKILL.md

**Strategy:** S-013 Inversion Technique
**Deliverable:** `skills/user-experience/SKILL.md`
**Criticality:** C4
**Date:** 2026-03-04
**Reviewer:** adv-executor (S-013)
**H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (confirmed by prior strategy outputs in tournament sequence)
**Goals Analyzed:** 7 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 5

---

## Summary

Iteration 7 applied 8 editorial fixes targeting Internal Consistency, Evidence Quality, and Traceability dimensions. These fixes addressed documentation-layer issues: the Design Sprint stage label mismatch, Wave 1 agent status annotation, ADR status labels, research provenance table completeness, activation-keywords asymmetry footnote, and ux-routing-rules.md status disclosure. None of the iteration 6 structural findings (IN-001-006 through IN-006-006) were addressed by these editorial changes, as all 6 findings target implementation gaps in stub files and absent schemas — not documentation accuracy.

Inversion analysis on the current iteration 7 state confirms: both Critical findings (IN-001-006, IN-002-006) remain OPEN — ux-orchestrator.md still contains only `<identity>`, `<purpose>`, and `<guardrails>` with no `<methodology>`, `<input>`, `<capabilities>`, or `<output>` sections; and `docs/schemas/handoff-v2.schema.json` does not exist (confirmed by filesystem check). All four Major findings (IN-003-006 through IN-006-006) also remain OPEN. One new finding (IN-001-007) is identified this iteration: the WSM (Weighted Skill Maturity) conditional gate value `>= 7.80` that governs ux-ai-design-guide access is referenced in Wave 5 entry criteria but WSM is undefined across all skill files, creating an unmeasurable prerequisite that would silently block or silently permit ux-ai-design-guide invocation.

The recommendation remains **REVISE** — the 8 editorial fixes do not address the foundational implementation-layer gaps identified by inversion analysis.

---

## Prior Findings Resolution Status

| Prior ID | Finding | Status in Iteration 7 |
|----------|---------|----------------------|
| IN-001-006 (Critical) | ux-orchestrator stub missing `<methodology>`, `<input>`, `<capabilities>`, `<output>` sections | OPEN — ux-orchestrator.md still contains only 3 XML sections (`<identity>`, `<purpose>`, `<guardrails>`); no change in iteration 7 |
| IN-002-006 (Critical) | `handoff-v2.schema.json` referenced as foundational but does not exist | OPEN — filesystem confirms the file does not exist; SKILL.md still annotates "pending file creation" at lines 476 and 623 |
| IN-003-006 (Major) | Synthesis confidence gate inaccessible to orchestrator runtime | OPEN — `synthesis-validation.md` is entirely stub; all 4 sections pending implementation; no change in iteration 7 |
| IN-004-006 (Major) | Capacity check single-question reliability — unanchored self-report | OPEN — `ux-routing-rules.md` CAPACITY CHECK section still reads "Pending implementation" in full dispatch logic; no anchoring example added |
| IN-005-006 (Major) | Wave bypass accumulation — ceiling stated in SKILL.md but absent from rules | OPEN — `wave-progression.md` Bypass Mechanism still stub; no 2-concurrent ceiling, no WAVE-BYPASS-LOG format |
| IN-006-006 (Major) | Cross-framework synthesis signal extraction has no format contract | OPEN — `synthesis-validation.md` Synthesis Protocol Validation still stub |

**Carry-forward (all 6):** IN-001-006, IN-002-006, IN-003-006, IN-004-006, IN-005-006, IN-006-006 — renumbered as IN-001-007 through IN-005-007 and IN-007-007 in this report to preserve the 006-series identifiers for historical reference.

**Editorial fix impact on prior findings:** None. All 8 iteration 7 fixes were documentation-layer corrections (label accuracy, status disclosure, asymmetry documentation). The underlying structural gaps they address are different from the implementation gaps tracked by the IN-NNN-006 findings.

---

## Findings Summary

| ID | Assumption / Anti-Goal | Type | Confidence | Severity | Evidence | Affected Dimension |
|----|------------------------|------|------------|----------|----------|--------------------|
| IN-001-007 | ux-orchestrator stub lacks `<methodology>`, `<input>`, `<capabilities>`, `<output>` — Wave 0 agent is non-operational | Assumption (Technical) | Low | Critical | `skills/user-experience/agents/ux-orchestrator.md` lines 39-77 (3 sections present of 7 required) | Completeness |
| IN-002-007 | `handoff-v2.schema.json` referenced as the structural contract for all cross-sub-skill data exchange but does not exist on the filesystem | Assumption (Process) | Low | Critical | SKILL.md lines 476, 623; filesystem confirmation: file absent | Methodological Rigor |
| IN-003-007 | Synthesis confidence gate assumes orchestrator knows per-sub-skill confidence categories at invocation time | Assumption (Technical) | Medium | Major | `synthesis-validation.md` lines 20-50 (all stub) | Internal Consistency |
| IN-004-007 | Capacity check single question reliably classifies < 20% vs 20-50% team UX time allocation | Assumption (Resource) | Medium | Major | `ux-routing-rules.md` CAPACITY CHECK — "Pending implementation" in dispatch logic section | Evidence Quality |
| IN-005-007 | Wave bypass documentation (3 fields) prevents systemic wave skipping without cumulative ceiling enforcement | Assumption (Process) | Medium | Major | `wave-progression.md` Bypass Mechanism lines 43-52 (stub — no ceiling, no audit log) | Methodological Rigor |
| IN-006-007 | WSM >= 7.80 conditional gate for ux-ai-design-guide is measurable because WSM is defined | Assumption (Process) | Low | Major | SKILL.md line 267 (Wave 5 entry criteria); WSM undefined in all skill files | Evidence Quality |
| IN-007-007 | Signal extraction correctly identifies convergent signals across heterogeneous sub-skill output formats | Assumption (Technical) | Low | Major | `synthesis-validation.md` Synthesis Protocol Validation lines 30-34 (stub) | Internal Consistency |

---

## Step 1: Goal Inventory (Unchanged from Iterations 4 and 6)

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

## Step 2: Anti-Goals (Iteration 7 State Assessment)

| Goal | Anti-Goal (Guaranteed Failure Conditions) | Addressed by Iteration 7 State? |
|------|------------------------------------------|---------------------------------|
| G-1: Lifecycle Routing | Orchestrator receives routing request but has no `<methodology>` to execute the 4-step triage; returns generic LLM response bypassing documented logic | NOT ADDRESSED — ux-orchestrator.md stub unchanged; still contains only `<identity>`, `<purpose>`, `<guardrails>` |
| G-2: Wave-Gated Quality | Wave gate check references WAVE-N-SIGNOFF.md but wave-progression.md has no schema for signoff contents; and bypass ceiling is undocumented in the enforcement file | NOT ADDRESSED — wave-progression.md stub unchanged; no ceiling enforcement, no signoff schema |
| G-3: AI-Bias Mitigation | Orchestrator assigns wrong confidence tier because per-sub-skill confidence table is not embedded in its system prompt and synthesis-validation.md is unimplemented | NOT ADDRESSED — synthesis-validation.md stub unchanged |
| G-4: Incremental Adoption | WSM gate for Wave 5 AI-First sub-skill is undefined, so the gate either always blocks (if orchestrator checks) or never triggers (if orchestrator skips undefined gate) | NOT ADDRESSED — WSM not defined anywhere in skill files; this is a new finding in iteration 7 |
| G-5: Framework Integrity | Cross-sub-skill handoffs use an undefined schema; each EPIC team defines their own data format; synthesis fails silently on format mismatch | NOT ADDRESSED — handoff-v2.schema.json does not exist; SKILL.md annotation unchanged |
| G-6: Orchestration Reliability | ux-orchestrator.md has no `<input>` section defining expected handoff fields; when the orchestrator receives a handoff from another skill, it does not know what fields to expect | NOT ADDRESSED — no `<input>` section in ux-orchestrator stub |
| G-7: Tiny-Team Calibration | Team with < 20% capacity answers capacity question with enthusiasm-inflated estimate; routed to Wave 3-5; abandons mid-cycle; no capacity calibration anchors defined | NOT ADDRESSED — ux-routing-rules.md CAPACITY CHECK dispatch logic still stub |

---

## Step 3: Assumption Map (Iteration 7 — New Finding Added)

| ID | Assumption | Type | Confidence | Validation Status | Failure Consequence |
|----|-----------|------|------------|-------------------|---------------------|
| A-01 | ux-orchestrator will have a `<methodology>` section implementing 4-step triage when EPIC-001 delivers | Technical (stub state) | Low | Not validated — stub has no methodology placeholder or section stub | Orchestrator responds to UX requests as generic Opus LLM without routing protocol; lifecycle routing fails completely (G-1) |
| A-02 | handoff-v2.schema.json will be created before cross-sub-skill handoffs are needed at Wave 2 | Process (schema dependency) | Low | Not validated — file absent from filesystem; SKILL.md notes "pending file creation" | UX-specific handoff data transmitted as unstructured text; data fidelity lost at every sub-skill boundary (G-5) |
| A-03 | Orchestrator possesses per-sub-skill synthesis confidence category knowledge at invocation time | Technical (data access) | Medium | Partially validated — SKILL.md Sub-Skill Synthesis Output Map table exists; orchestrator stub has no reference to it | Orchestrator assigns wrong confidence tier; LOW output presented as MEDIUM; P-022 violated (G-3) |
| A-04 | Single capacity question reliably classifies teams into < 20%, 20-50%, or > 50% UX time allocation | Resource (measurement) | Medium | Not validated — no anchoring example, no prior-completion check, no fallback if user declines | Teams overestimate capacity; receive Wave 3-5 routing; abandon methodology mid-cycle (G-7) |
| A-05 | 3-field wave bypass prevents teams from bypassing all 5 waves consecutively | Process (governance) | Medium | Not validated — bypass ceiling "max 2 concurrent bypasses" stated in SKILL.md but not in wave-progression.md Bypass Mechanism section | Teams bypass Waves 1-4 in one session; Design Sprint executes without any framework calibration (G-2) |
| A-06 | WSM >= 7.80 conditional gate for ux-ai-design-guide is measurable at runtime | Process (gate logic) | Low | Not validated — WSM (Weighted Skill Maturity) metric not defined anywhere in SKILL.md, ux-routing-rules.md, ADR-PROJ022-001, ADR-PROJ022-002, or any skill file | ux-ai-design-guide gate cannot be enforced; gate either always passes (metric unknown = threshold unknowable) or always blocks (conservative default); incremental adoption damaged (G-4) |
| A-07 | Signal extraction correctly identifies convergent signals across heterogeneous sub-skill output formats | Technical (parsing) | Low | Not validated — sub-skill output formats not yet specified; synthesis relies on section name matching across non-uniform stubs | False convergence detected; HIGH confidence applied to mismatched findings; P-022 violated (G-3) |
| A-08 | Session state flag for ONBOARD fires once per session and is reliable across LLM context resets | Technical (state) | Low | Not validated — no state mechanism described; ux-orchestrator stub has no state management | ONBOARD fires on every invocation causing HIGH RISK warning fatigue; or ONBOARD never fires after context compaction |
| A-09 | 0.85 wave transition threshold reliably discriminates deployment-ready from not-ready | Process (measurement) | Medium | Not validated — ADR-PROJ022-002 PROVISIONAL; formal derivation pending | Gate permits low-quality sub-skill deployment at 0.85; OR blocks useful deployment when output calibration data is atypical |
| A-10 | ux-routing-rules.md routing table operates correctly without the Dispatch logic step (still stub) | Process (implementation) | Low | Not validated — PARTIAL IMPLEMENTATION comment in ux-routing-rules.md: "Full dispatch logic in EPIC-001" | Routing table is documentation; dispatch logic does not map table entries to actual Task invocations |
| A-11 | < 20% capacity check works when user declines to provide capacity information | Process (P-020 compliance) | Medium | Not validated — no defined fallback; P-020 says user decides | Orchestrator blocks routing (P-020 violation) OR skips check and routes to Wave 5 arbitrarily |
| A-12 | Wave 1 agent stubs can be extended to full implementations without changing file paths or frontmatter names | Technical (migration) | Medium | Partially validated — stub files at correct paths per SKILL.md References table | If stub-to-implementation requires restructuring, all SKILL.md References paths become stale |
| A-13 | Sub-skill agents (all stubs) will receive correct UX context fields from orchestrator when EPIC-002 implements them | Technical (handoff interface) | Low | Not validated — ux-orchestrator stub shows Task template (SKILL.md lines 222-241) but sub-skill stubs have no `<input>` section | Orchestrator passes (Engagement ID, Topic, Product, Target Users) but sub-skill agents expect different fields; data mismatch at Wave 1 |
| A-14 | SKILL.md navigation table and all 15 section anchors remain correct as EPIC-001 updates stub files | Process (documentation integrity) | Medium | Partially validated — navigation table and anchors verified current | As EPIC-001 implements stubs, SKILL.md cross-references to specific line numbers may drift; NAV-001/H-23 violations accumulate |

---

## Step 4: Stress-Test Results (Iteration 7)

### New Assumption Stress-Test: A-06 (WSM Gate)

**Assumption:** WSM >= 7.80 conditional gate for ux-ai-design-guide is measurable at runtime because WSM is defined somewhere.

**Inversion:** WSM is NOT defined in any accessible file. The ux-orchestrator cannot compute WSM at routing time.

**Plausibility:** High. A filesystem search across all skill files (ux-routing-rules.md, wave-progression.md, synthesis-validation.md, SKILL.md, ADR-PROJ022-001, ADR-PROJ022-002) returns no definition of WSM or Weighted Skill Maturity. The only occurrence of "WSM >= 7.80" is in SKILL.md line 267 within the Wave 5 entry criteria table.

**Consequences if assumption fails:**

1. **Silent-block path:** The orchestrator checks for WSM value, finds no definition or stored value, defaults to 0 (below threshold), and silently blocks ux-ai-design-guide even when the Enabler is DONE and the team is ready. The team experiences unexplained access denial for an AI-First design capability they expected after completing Wave 4.

2. **Silent-pass path:** The orchestrator checks for WSM gate, cannot resolve the metric, treats undefined = gate skipped, and routes to ux-ai-design-guide before the AI-First Enabler is complete. The AI-first design methodology runs without the quality prerequisite — the scenario the gate was designed to prevent.

3. **EPIC-001 developer path:** A developer implementing the orchestrator `<methodology>` reads Wave 5 entry criteria, sees "WSM >= 7.80", cannot find WSM defined anywhere, and either (a) invents a WSM calculation, creating an undocumented metric, or (b) removes the gate as unmeasurable, silently degrading the quality gate.

**Severity Classification: Major** — The gate failure does not block Wave 1-4 operations. It specifically affects Wave 5 (Process Intensives), which are CONDITIONAL dependencies. However, the gate is listed as an explicit prerequisite for ux-ai-design-guide in SKILL.md line 267 and the Enabler condition is cited there without WSM being defined. An undefined metric in a quality gate is a methodological rigor failure.

**Affected Dimension:** Evidence Quality — a gate value without a defined measurement source lacks evidentiary basis.

### Prior Critical Findings Re-Verification

**IN-001-006 (now IN-001-007): ux-orchestrator Missing `<methodology>` Section**

Filesystem verification of `skills/user-experience/agents/ux-orchestrator.md`:
- Lines 39-51: `<identity>` section (9 lines)
- Lines 53-63: `<purpose>` section (10 lines)
- Lines 65-77: `<guardrails>` section (12 lines)
- File ends at line 77

Grep for "methodology|input|capabilities|output" in ux-orchestrator.md returns only:
- "methodology" appears as a noun in prose within `<identity>` and `<guardrails>` (e.g., "methodology selection") — not as an XML section heading
- No `<methodology>`, `<input>`, `<capabilities>`, or `<output>` XML sections exist

**Status: OPEN — Critical finding persists unchanged.**

**IN-002-006 (now IN-002-007): handoff-v2.schema.json Does Not Exist**

Filesystem glob for `handoff-v2.schema.json` across the entire repository returns no results. SKILL.md lines 476 and 623 both retain the "pending file creation" annotation.

**Status: OPEN — Critical finding persists unchanged.**

### Prior Major Findings Re-Verification

**IN-003-006 (now IN-003-007):** `synthesis-validation.md` all 4 sections remain "Pending implementation" — no change. **OPEN.**

**IN-004-006 (now IN-004-007):** `ux-routing-rules.md` CAPACITY CHECK section — dispatch logic section comment still reads "PARTIAL IMPLEMENTATION: Routing table populated. Full dispatch logic in EPIC-001" — no anchoring example added. **OPEN.**

**IN-005-006 (now IN-005-007):** `wave-progression.md` Bypass Mechanism — still stub with 3-field list and no ceiling, no WAVE-BYPASS-LOG format. **OPEN.**

**IN-007-006 (now IN-007-007):** `synthesis-validation.md` Synthesis Protocol Validation — still stub. No `## Synthesis Signals` format defined. **OPEN.**

---

## Detailed Findings

### IN-001-007: ux-orchestrator Stub Has No `<methodology>` — Wave 0 Agent Is Non-Operational [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | `skills/user-experience/agents/ux-orchestrator.md` |
| **Strategy Step** | Step 2 (Anti-Goals) + Step 4 (Stress-Test) |
| **Prior ID** | IN-001-006 (OPEN — carry-forward, no change) |

**Evidence:**

ux-orchestrator.md (78 lines) contains exactly three XML sections:
```
<identity>    lines 39-51 — role, expertise bullets, cognitive mode
<purpose>     lines 53-63 — existence justification paragraph
<guardrails>  lines 65-77 — P-003/P-020/P-022 + 3 forbidden actions
```

Missing per `agent-development-standards.md` [Markdown Body Sections] (7 required sections):
- `<input>` — defines expected UX context fields from user or handoff
- `<capabilities>` — tool usage patterns and constraints
- `<methodology>` — 4-step lifecycle triage (ONBOARD, CAPACITY CHECK, MCP CHECK, STAGE TRIAGE)
- `<output>` — artifact location, L0/L1/L2 structure requirements

Iteration 7 editorial fixes did not touch ux-orchestrator.md.

**Analysis:**

SKILL.md lines 292-315 and 321 document the orchestrator's 4-step routing triage in detail. That documentation exists nowhere in the orchestrator's system prompt. Per agent-development-standards.md, `<methodology>` is "How the agent works — Step-by-step process, decision criteria, quality standards." Without it, when the orchestrator processes a user's UX request, it applies generic Opus reasoning rather than the specified 4-step protocol. The Wave 0 deliverable cannot deliver Wave 0 behavior.

Inversion: to guarantee G-1 (Lifecycle Routing) fails, document the routing methodology in SKILL.md but omit it from the agent file that executes it. This is the current state after 7 iterations.

**Recommendation:**

Add all 7 required XML sections to ux-orchestrator.md. The `<methodology>` section must name the 4 triage steps as explicit stub subsections with EPIC-001 TODO markers. The `<input>` section must define the UX context fields. The `<output>` section must reference the L0/L1/L2 output structure from SKILL.md §Available Agents.

**Acceptance Criteria:**
- ux-orchestrator.md contains all 7 XML sections per agent-development-standards.md [Markdown Body Sections]
- `<methodology>` section names ONBOARD, CAPACITY CHECK, MCP CHECK, STAGE TRIAGE as explicit subsections
- `<input>` section defines: Engagement ID, Product, Target Users, Lifecycle Stage (at minimum)
- Compliance verifiable by section-heading grep

---

### IN-002-007: handoff-v2.schema.json Referenced as Foundational but Does Not Exist [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | `skills/user-experience/SKILL.md` lines 476, 623 |
| **Strategy Step** | Step 2 (Anti-Goals) + Step 4 (Stress-Test) |
| **Prior ID** | IN-002-006 (OPEN — carry-forward, no change) |

**Evidence:**

SKILL.md line 476 (§Cross-Skill Integration):
```
Handoffs use the Jerry handoff protocol (schema specified in
`agent-development-standards.md` [Handoff Protocol]; canonical path
`docs/schemas/handoff-v2.schema.json`, pending file creation)
```

SKILL.md line 623 (§Standards References):
```
| Handoff Schema | `docs/schemas/handoff-v2.schema.json` (canonical path per
  `agent-development-standards.md`; file pending creation) |
```

Filesystem confirmation: `glob("handoff-v2.schema.json")` across the entire repository returns no results. The file does not exist.

SKILL.md §Cross-Sub-Skill Handoff Data (lines 472-487) lists 6 specific UX handoff types — job statement + switch forces, validated prototype + Day 4 findings, severity-rated findings, component inventory with Storybook references, validated/invalidated hypothesis backlog — all described as using this schema. None of these handoff types can be schema-validated without the file.

**Analysis:**

The schema is listed in SKILL.md §Standards References alongside Jerry Constitution and quality-enforcement.md — the authoritative governance files. Listing a non-existent file in the same reference table as foundational standards signals that it is considered foundational. The inversion of G-5 (Framework Integrity) is: to guarantee UX sub-skill data is lost at every framework boundary, ensure the schema that would constrain cross-sub-skill data format never gets created. The "pending file creation" annotation has appeared in each of the last 3 iterations without movement.

**Recommendation:**

The handoff-v2.schema.json file must be created as a tracked dependency before Wave 1 sub-skill implementation begins (EPIC-002). The `skills/user-experience/rules/ux-routing-rules.md` [Handoff Schema] section (currently stub) must document the UX-specific extensions needed beyond the generic handoff-v2 fields. The 6 UX handoff types from SKILL.md §Cross-Sub-Skill Handoff Data must each map to specific schema fields.

**Acceptance Criteria:**
- `docs/schemas/handoff-v2.schema.json` exists as a valid JSON Schema Draft 2020-12 file before EPIC-002 begins
- `ux-routing-rules.md` [Handoff Schema] section is non-stub with UX artifact type mappings
- SKILL.md lines 476 and 623 drop "pending file creation" annotation
- Worktracker tracking: dependency tracked as a prerequisite to EPIC-002 start

---

### IN-003-007: Synthesis Confidence Gate Inaccessible to Orchestrator Runtime [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/synthesis-validation.md` lines 20-50 |
| **Strategy Step** | Step 4 (Stress-Test) |
| **Prior ID** | IN-003-006 (OPEN — carry-forward, no change) |

**Evidence:**

`synthesis-validation.md` Confidence Classification (lines 19-26):
```
<!-- TODO (EPIC-001): Define confidence gates with thresholds per P-022. -->
Pending implementation. All synthesis hypotheses MUST include confidence classification:
- HIGH: 3+ frameworks converge on the same finding
- MEDIUM: 2 frameworks converge OR 1 framework with strong evidence
- LOW: Single framework finding, weak evidence, or contradiction present
```

All 4 sections of synthesis-validation.md (Confidence Classification, Synthesis Protocol Validation, Convergence Thresholds, Contradiction Handling) remain "Pending implementation." Iteration 7 editorial fixes did not touch synthesis-validation.md.

The ux-orchestrator stub system prompt contains no reference to synthesis-validation.md and no embedded confidence lookup table. The Sub-Skill Synthesis Output Map in SKILL.md (lines 344-365) provides per-sub-skill confidence assignments but is in SKILL.md, not in the agent file.

**Analysis:**

The P-022 compliance rationale for synthesis confidence gates requires the orchestrator to know, at runtime, which confidence tier to assign to each synthesis signal. This knowledge must be either embedded in the `<methodology>` section or accessible via a Read call to a non-stub rule file. Both paths are currently blocked: the methodology section does not exist (IN-001-007), and synthesis-validation.md is entirely stub.

**Recommendation:**

Populate all 4 synthesis-validation.md sections before Wave 2 synthesis is first attempted. Add a "Confidence Lookup" step to ux-orchestrator `<methodology>` naming synthesis-validation.md as the lookup source.

**Acceptance Criteria:**
- `synthesis-validation.md` has all 4 sections non-stub with specific thresholds
- ux-orchestrator `<methodology>` includes explicit "Confidence Lookup" step referencing synthesis-validation.md
- At least one sub-skill output tested against the confidence gate before Wave 2 synthesis signoff

---

### IN-004-007: Capacity Check Single-Question Reliability — Unanchored Self-Report [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/ux-routing-rules.md` — CAPACITY CHECK (lines 26-28) |
| **Strategy Step** | Step 4 (Stress-Test) |
| **Prior ID** | IN-004-006 (OPEN — carry-forward, no change) |

**Evidence:**

ux-routing-rules.md §Lifecycle Stage Router (lines 26-28):
```
2. CAPACITY CHECK: Ask team UX time allocation. If < 20% of one person's
   time: recommend Wave 1 sub-skills only (P-020: user decides)
```

No anchoring example, no prior-completion check, no fallback if user declines. Section comment: "PARTIAL IMPLEMENTATION: Routing table populated. Full dispatch logic in EPIC-001." Iteration 7 did not modify ux-routing-rules.md dispatch logic.

**Analysis:**

The inversion: to guarantee G-7 (Tiny-Team Calibration) fails, ask teams to self-report time capacity at the moment of highest motivation (first invocation) using an unanchored percentage. "About 30% of my time" from a team that has 2-3 sprint hours is a systematic overestimate. Routing a 5%-capacity team to Lean UX (Wave 2) or Atomic Design (Wave 3) sets up multi-sprint commitments they cannot sustain. Wave signoffs are never achieved. The wave model stalls invisibly — no error output, just user abandonment. Capacity mismatch is the highest-probability failure mode for a methodology targeting tiny teams, and the capacity check is the only protective mechanism.

**Recommendation:**

When ux-routing-rules.md receives EPIC-001 full dispatch implementation, the CAPACITY CHECK must include (1) sprint-hours anchoring example (2h/sprint ≈ < 20%; 8h/sprint ≈ 25-40%), and (2) prior-completion secondary check. Teams with no prior UX methodology cycle completion are treated as Wave 1-only regardless of stated hours (P-020-compliant recommendation).

**Acceptance Criteria:**
- ux-routing-rules.md CAPACITY CHECK documents anchoring example with sprint-hours reference points
- ux-routing-rules.md CAPACITY CHECK documents behavior when user refuses to answer (default: recommend Wave 1)
- Anchored capacity question included in ux-orchestrator `<methodology>` stub as a named step

---

### IN-005-007: Wave Bypass Accumulation — Ceiling Stated in SKILL.md but Absent from Enforcement Rules [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/wave-progression.md` Bypass Mechanism (lines 43-52) |
| **Strategy Step** | Step 4 (Stress-Test) |
| **Prior ID** | IN-005-006 (OPEN — carry-forward, no change) |

**Evidence:**

SKILL.md line 279: "**Cumulative ceiling:** Maximum 2 concurrent bypasses per team. If a team has 2 active bypasses, the orchestrator requires remediation of at least one before granting additional bypasses."

wave-progression.md §Bypass Mechanism (lines 43-52):
```
<!-- TODO (EPIC-001): Define 3-field bypass documentation requirements. -->
Pending implementation. Bypass fields:
1. Unmet criterion
2. Impact assessment
3. Remediation plan
User approval required per P-020.
```

No ceiling. No enforcement mechanism. No WAVE-BYPASS-LOG format. Iteration 7 did not modify wave-progression.md.

**Analysis:**

SKILL.md declares the ceiling; wave-progression.md is where EPIC-001 developers will look for bypass implementation guidance. The ceiling does not appear there. An EPIC-001 developer building bypass from wave-progression.md will implement 3-field documentation correctly but without a ceiling — the ceiling will become a documentation artifact with no behavioral backing. The inversion of G-2 (Wave-Gated Quality): to guarantee quality gates are circumventable, implement bypass documentation without the accumulation cap.

**Recommendation:**

wave-progression.md §Bypass Mechanism must be updated before EPIC-001 implements bypass to include: (1) max-2-concurrent-bypasses ceiling with explicit enforcement steps, (2) WAVE-BYPASS-LOG.md format definition, (3) orchestrator pre-bypass ceiling check description.

**Acceptance Criteria:**
- wave-progression.md §Bypass Mechanism specifies 2-concurrent ceiling with enforcement steps
- wave-progression.md §Bypass Mechanism specifies WAVE-BYPASS-LOG.md path and format
- ux-orchestrator `<methodology>` stub names bypass ceiling check as a pre-bypass step

---

### IN-006-007: WSM >= 7.80 Conditional Gate for ux-ai-design-guide Is Unmeasurable [MAJOR — NEW]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/SKILL.md` line 267 (Wave 5 entry criteria) |
| **Strategy Step** | Step 3 (Assumption Mapping) + Step 4 (Stress-Test) |
| **Prior ID** | A-08 (assumption mapped in iteration 6, not promoted to finding; promoted this iteration due to persistence across 7 iterations) |

**Evidence:**

SKILL.md line 267 (Wave Architecture table, Wave 5 entry criteria):
```
AI-First: Enabler DONE + WSM >= 7.80
```

Filesystem search for WSM or "Weighted Skill Maturity" across all skill files (SKILL.md, ux-routing-rules.md, wave-progression.md, synthesis-validation.md, ADR-PROJ022-001, ADR-PROJ022-002) returns results only from SKILL.md line 267 itself. No definition, no calculation formula, no scale, no measurement mechanism exists for WSM.

The ux-routing-rules.md Stage Routing Table lists Wave 5 entry as "Wave 4: 30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed; AI-First: Enabler DONE" without mentioning WSM — suggesting partial omission in the routing rules file.

**Analysis:**

The inversion of G-4 (Incremental Adoption): to guarantee that the highest-capability sub-skill (ux-ai-design-guide) is either always blocked or always accessible, define an unmeasurable prerequisite. WSM >= 7.80 is referenced in SKILL.md as a quality gate but WSM is not defined anywhere in the skill specification. An EPIC-001 developer implementing the orchestrator routing logic faces three choices: (1) invent a WSM calculation, (2) treat the gate as unimplementable and omit it, (3) block ux-ai-design-guide access permanently as a conservative default. All three paths deviate from the intended design without the creator's knowledge, because the omission is silent.

The plausibility of this inversion is High — seven tournament iterations have passed without WSM being defined. This means the gap has persisted through the entire C4 review cycle.

**Recommendation:**

WSM must be defined in wave-progression.md or a new `skills/user-experience/rules/metrics-plan.md` section before EPIC-001 implements Wave 5 routing. The definition must include: (1) what WSM measures (candidate: aggregate deployment readiness score across completed waves), (2) how it is calculated (formula or scoring rubric), (3) what 7.80 represents on the scale, and (4) where the value is stored for orchestrator access.

**Acceptance Criteria:**
- WSM is defined in a non-stub rule file with a calculation formula and scale reference
- SKILL.md line 267 references the defining rule file (not leaves WSM undefined)
- ux-routing-rules.md Stage Routing Table includes WSM >= 7.80 condition for Wave 5 AI-First routing
- Worktracker: WSM definition tracked as a prerequisite to EPIC-001 Wave 5 routing implementation

---

### IN-007-007: Cross-Framework Synthesis Signal Extraction Has No Format Contract [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `skills/user-experience/rules/synthesis-validation.md` lines 30-34 |
| **Strategy Step** | Step 4 (Stress-Test) |
| **Prior ID** | IN-006-006 (OPEN — carry-forward, no change) |

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

No standardized `## Synthesis Signals` section is defined for sub-skill outputs. No cross-sub-skill output format contract exists. Iteration 7 did not modify synthesis-validation.md.

**Analysis:**

To guarantee G-3 (AI-Bias Mitigation) fails via synthesis, allow each sub-skill EPIC team to define their own output structure independently. ux-heuristic-evaluator may use "Severity: 3"; ux-heart-analyst may use "Status: Below Target"; ux-lean-ux-facilitator may use "Validated: false". The orchestrator's signal extraction uses format-specific rules ("severity >= 2", "below target", "unvalidated assumptions") that will fail silently when applied to outputs using different notation. False convergence — or missing real convergence — follows without any error surfacing. This is distinct from IN-003-007 (which concerns the confidence tier lookup) — both the signal format (this finding) and the confidence tier assignment (IN-003-007) must be standardized.

**Recommendation:**

synthesis-validation.md §Synthesis Protocol Validation must define a `## Synthesis Signals` section as a mandatory output section for all sub-skills. Minimum format: `Signal: {description} | Severity: {1-4} | Framework: {name} | Status: {confirmed|unvalidated}`. Wave 1 sub-skills must implement this before Wave 2 synthesis is attempted.

**Acceptance Criteria:**
- synthesis-validation.md §Synthesis Protocol Validation defines `## Synthesis Signals` format
- Wave 1 sub-skill (ux-heuristic-evaluator, ux-jtbd-analyst) output templates include the section before Wave 2 signoff
- Orchestrator signal extraction step in `<methodology>` reads only `## Synthesis Signals` section, not free-text prose

---

## Step 5: Recommendations

### Critical Findings — MUST Mitigate

**IN-001-007: ux-orchestrator Missing 4 of 7 Required XML Sections**
- Action: Add `<input>`, `<capabilities>`, `<methodology>`, `<output>` sections to `skills/user-experience/agents/ux-orchestrator.md`; `<methodology>` must name ONBOARD, CAPACITY CHECK, MCP CHECK, STAGE TRIAGE as explicit subsections with EPIC-001 TODO markers; `<input>` must define at minimum: Engagement ID, Product, Target Users, Lifecycle Stage
- Acceptance Criteria: ux-orchestrator.md has all 7 XML sections; `<methodology>` names 4 triage steps as explicit stubs; section-heading grep confirms compliance

**IN-002-007: handoff-v2.schema.json Does Not Exist**
- Action: Create `docs/schemas/handoff-v2.schema.json` as a valid JSON Schema file before EPIC-002 begins; populate `ux-routing-rules.md` [Handoff Schema] with UX-specific artifact type mappings; remove "pending file creation" annotation from SKILL.md lines 476 and 623; track as EPIC-001/EPIC-002 dependency in worktracker
- Acceptance Criteria: Schema file exists; 6 UX handoff types mapped to schema fields; SKILL.md annotation removed; worktracker dependency tracked

### Major Findings — SHOULD Mitigate

**IN-003-007: Synthesis Confidence Gate Inaccessible**
- Action: Populate all 4 synthesis-validation.md sections before Wave 2; add confidence lookup step to ux-orchestrator `<methodology>` stub naming synthesis-validation.md as source
- Acceptance Criteria: synthesis-validation.md non-stub; ux-orchestrator methodology names synthesis-validation.md as lookup source; gate tested before Wave 2 signoff

**IN-004-007: Capacity Check Unanchored**
- Action: Add sprint-hours anchoring example and prior-completion secondary check to ux-routing-rules.md CAPACITY CHECK when EPIC-001 implements dispatch logic
- Acceptance Criteria: Anchored capacity question documented; behavior on user refusal defined; step named in ux-orchestrator `<methodology>` stub

**IN-005-007: Bypass Ceiling Not Implemented in Rules**
- Action: Add 2-concurrent-bypass ceiling, WAVE-BYPASS-LOG.md format definition, and pre-bypass orchestrator ceiling check to wave-progression.md §Bypass Mechanism before EPIC-001 builds bypass implementation
- Acceptance Criteria: wave-progression.md Bypass Mechanism non-stub with ceiling and audit log format; orchestrator `<methodology>` stub names ceiling check

**IN-006-007: WSM Gate Undefined — Unmeasurable Prerequisite (NEW)**
- Action: Define WSM (calculation, scale, storage location) in wave-progression.md or metrics-plan.md; update SKILL.md line 267 to reference the defining rule file; update ux-routing-rules.md Stage Routing Table Wave 5 row to include WSM condition; track as EPIC-001 dependency
- Acceptance Criteria: WSM defined with formula and scale; SKILL.md cross-references definition; routing table includes WSM condition; tracked in worktracker

**IN-007-007: Signal Extraction Format Contract Absent**
- Action: Define `## Synthesis Signals` section format in synthesis-validation.md §Synthesis Protocol Validation; require Wave 1 sub-skills to implement before Wave 2; add extraction step to ux-orchestrator `<methodology>` that reads only this section
- Acceptance Criteria: synthesis-validation.md defines signal section format; Wave 1 stubs include the section before Wave 2 signoff

---

## Scoring Impact

| Dimension | Weight | Impact | Findings Driving Impact |
|-----------|--------|--------|------------------------|
| Completeness | 0.20 | Negative | IN-001-007 — the only deployed agent (ux-orchestrator) lacks 4 of 7 required XML sections including `<methodology>`, the section that implements the skill's core routing capability; without it, the Wave 0 deliverable cannot deliver its documented behavior |
| Internal Consistency | 0.20 | Negative | IN-003-007, IN-007-007 — synthesis confidence classification is documented in SKILL.md Sub-Skill Synthesis Output Map but inaccessible to the orchestrator; signal extraction assumes uniform sub-skill output format but no format contract exists; the synthesis system is internally described in SKILL.md but lacks the rule file backing that would make it internally consistent at runtime |
| Methodological Rigor | 0.20 | Negative | IN-002-007, IN-005-007 — handoff schema is the structural contract for all cross-sub-skill data exchange and does not exist; bypass ceiling is stated in SKILL.md but absent from wave-progression.md where EPIC-001 developers will implement bypass; both create methodology statements without enforceable mechanisms |
| Evidence Quality | 0.15 | Negative | IN-004-007, IN-006-007 — capacity routing relies on an unanchored self-report question with no calibration mechanism; WSM >= 7.80 gate has no defined measurement source, making the gate value unverifiable and the quality gate unenforced |
| Actionability | 0.15 | Positive | All 7 findings have specific mitigations with concrete acceptance criteria; no finding requires architectural revision — all require additions to existing stub files or creation of one new schema file; the corrective path is clear and bounded |
| Traceability | 0.10 | Neutral | All findings trace to specific file paths and line numbers; prior finding resolution table explicitly documents carry-forward rationale; editorial fix impact on prior findings is explicitly assessed; new finding (IN-006-007) traced to SKILL.md line 267 and confirmed absence via filesystem search |

**Overall Assessment: REVISE**

The 8 editorial fixes in iteration 7 improved documentation accuracy (Design Sprint stage label, ADR status, research provenance, asymmetry transparency) but did not address any of the 6 structural findings carried forward from iteration 6. Both Critical findings (ux-orchestrator missing methodology; handoff schema absent) remain open. All 4 Major findings from iteration 6 remain open. One new Major finding (IN-006-007: WSM undefined) was promoted from the assumption map — it has been present as assumption A-08 since iteration 6 but is now surfaced as a finding because seven tournament iterations have elapsed without WSM being defined, demonstrating it will not self-resolve through editorial revision cycles.

The deliverable's architectural design remains sound. The implementation scaffolding (stub file completeness, schema creation, enforcement rule population) requires targeted additions that are bounded and feasible. The skill cannot be declared Wave 0 complete while the Wave 0 agent lacks operational methodology.

---

## Execution Statistics
- **Total Findings:** 7
- **Critical:** 2 (both carry-forward from iteration 6)
- **Major:** 5 (4 carry-forward; 1 new)
- **Minor:** 0
- **Protocol Steps Completed:** 6 of 6
- **Goals Analyzed:** 7
- **Assumptions Mapped:** 14
- **Anti-Goal Conditions Identified:** 7 per goal (49 conditions assessed)
- **Vulnerable Assumptions:** 7 (5 carry-forward with IN-NNN-007 identifiers; 1 newly promoted to finding; 1 new)
- **Prior Findings Resolved (this iteration):** 0 — editorial fixes addressed documentation accuracy only
- **Prior Findings Carry-Forward:** 6 of 6 (IN-001-006 through IN-006-006, all OPEN)
- **New Findings Introduced:** 1 (IN-006-007: WSM undefined — promoted from assumption A-08)
- **Editorial Fix Impact on Prior Findings:** None — all 8 iteration 7 fixes were documentation-layer corrections targeting different concerns than the structural implementation gaps
