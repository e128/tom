# Strategy Execution Report: Inversion Technique (S-013)

## Execution Context
- **Strategy:** S-013 (Inversion Technique)
- **Template:** `/Users/adam.nowak/workspace/GitHub/geekatron/jerry/.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `skills/user-experience/SKILL.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 4 (C4 tournament)
- **Finding Prefix:** IN-NNN-004

---

# Inversion Report: User-Experience SKILL.md

**Strategy:** S-013 Inversion Technique
**Deliverable:** `skills/user-experience/SKILL.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-013)
**H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (confirmed by prior strategy outputs in tournament sequence)
**Goals Analyzed:** 7 | **Assumptions Mapped:** 12 | **Vulnerable Assumptions:** 7

---

## Summary

The SKILL.md presents a well-structured orchestration design with 10 UX framework specialists, 5-wave deployment gating, and synthesis confidence gates. Inversion analysis against the skill's 7 primary goals surfaces 7 vulnerable assumptions: 2 Critical and 5 Major. The two Critical findings concern (1) the complete stub state of every subordinate implementation artifact — the skill assumes its operational promise is anchored to prose documentation alone, and (2) the absence of any enforcement mechanism preventing the orchestrator from routing to Wave N+1 sub-skills that do not yet exist. These vulnerabilities mean the skill could route users into dead ends at runtime before any sub-skill implementation work begins. The recommendation is **REVISE** — address the two Critical findings before proceeding to Wave 1 implementation.

---

## Findings Summary

| ID | Assumption / Anti-Goal | Type | Confidence | Severity | Affected Dimension |
|----|------------------------|------|------------|----------|--------------------|
| IN-001-004 | Runtime routing assumes sub-skill agents exist and are deployable | Assumption | Low | Critical | Completeness |
| IN-002-004 | Wave gate enforcement assumes orchestrator can detect signoff file before routing | Assumption | Low | Critical | Methodological Rigor |
| IN-003-004 | Synthesis confidence gate assumes ux-orchestrator knows each sub-skill's synthesis category | Assumption | Medium | Major | Internal Consistency |
| IN-004-004 | Tiny-team capacity check assumes one structured question produces reliable capacity signal | Assumption | Medium | Major | Evidence Quality |
| IN-005-004 | Wave bypass mechanism assumes 3-field documentation prevents systemic drift | Assumption | Medium | Major | Methodological Rigor |
| IN-006-004 | CRISIS mode assumes a fixed 3-skill sequence matches all urgent UX failure patterns | Assumption | Low | Major | Completeness |
| IN-007-004 | Cross-framework synthesis assumes signal extraction correctly identifies convergent findings | Assumption | Low | Major | Internal Consistency |

---

## Step 1: Goal Inventory

| Goal | Description | Source |
|------|-------------|--------|
| G-1: Lifecycle Routing | Route tiny teams to the correct UX framework specialist based on product stage, reducing time-to-first-UX-insight | SKILL.md §Lifecycle-Stage Routing |
| G-2: Wave-Gated Quality | Prevent premature use of advanced sub-skills before foundational work is complete via 5-wave criteria gates | SKILL.md §Wave Architecture |
| G-3: AI-Bias Mitigation | Prevent teams from acting on hallucinated synthesis outputs; LOW confidence outputs must never produce design recommendations | SKILL.md §Synthesis Hypothesis Validation |
| G-4: Incremental Adoption | Enable teams to start with Wave 1 and progress without re-architecting the skill build-out | SKILL.md §Wave Architecture |
| G-5: Framework Integrity | Preserve methodological fidelity to 10 proven UX frameworks | SKILL.md §Purpose, §Available Agents |
| G-6: Orchestration Reliability | Ensure ux-orchestrator correctly sequences multi-skill workflows without P-003 violations | SKILL.md §P-003 Compliance |
| G-7: Tiny-Team Calibration | Remain usable at 20-50% of one person's time; not overwhelm teams | SKILL.md §Purpose ("calibrated for 20-50%") |

---

## Step 2: Anti-Goals (Goal Inversions)

| Goal | Anti-Goal (Guaranteed Failure Conditions) | Addressed by SKILL.md? |
|------|------------------------------------------|------------------------|
| G-1: Lifecycle Routing | Route users to agents that do not exist; present 10 routing options when only 1 sub-skill is deployed; fail silently when no sub-skill matches user intent | PARTIALLY — SKILL.md defines routing prose but ux-routing-rules.md is a stub with no operational logic |
| G-2: Wave-Gated Quality | Allow orchestrator to invoke Wave 3 sub-skills when Wave 1 is not deployed; accept a non-existent signoff file as "passed"; skip gate entirely when user is frustrated | PARTIALLY — signoff enforcement stated but no enforcement mechanism described for missing agents |
| G-3: AI-Bias Mitigation | Present LOW confidence synthesis to user without labeling; let user override LOW confidence by pressing ahead; fail to classify synthesis when sub-skill confidence category is not known to orchestrator | PARTIALLY — classification table exists but orchestrator's mechanism for accessing per-sub-skill confidence is not documented |
| G-4: Incremental Adoption | Make Wave 1 deployment require Wave 2-5 artifacts to function; create a broken initial experience before any sub-skill is implemented; require all 11 agents to exist for the orchestrator to work | NOT ADDRESSED — SKILL.md does not describe orchestrator behavior when sub-skills are absent |
| G-5: Framework Integrity | Override Nielsen's heuristics with AI-generated alternatives; omit Fogg's B=MAP trigger taxonomy; allow ux-heart-analyst to skip metric threshold derivation | NOT DIRECTLY ADDRESSED — frameworks are named but each sub-skill is only planned; no validation that implementation will be faithful |
| G-6: Orchestration Reliability | Orchestrator spawns Task for a sub-skill that is not defined in Claude Code; Task invocation fails silently; orchestrator retries indefinitely | NOT ADDRESSED — no error handling for Task failure documented in SKILL.md or stub agent |
| G-7: Tiny-Team Calibration | Present all 5 waves as immediately mandatory; require Figma + Miro + Storybook + Zeroheight before first insight; default the capacity question to "full UX team" | PARTIALLY — capacity check and cost tiers are described; wave sequencing protects against overload in theory but orchestrator must enforce it |

---

## Step 3: Assumption Map

| ID | Assumption | Type | Confidence | Validation Status | Failure Consequence |
|----|-----------|------|------------|-------------------|---------------------|
| A-01 | Sub-skill agents (ux-heuristic-evaluator through ux-ai-design-guide) exist as Claude Code agents when the orchestrator attempts Task invocation | Technical (deployment) | Low | Not validated — all 10 sub-skills marked [PLANNED: Wave N] | Orchestrator Task call fails; user receives opaque error; routing promise broken |
| A-02 | WAVE-N-SIGNOFF.md existence can be checked by the orchestrator before routing to gated sub-skills | Process (file state) | Low | Not validated — wave-progression.md is a stub; no file-path query logic described | Wave gate is bypassed because orchestrator has no mechanism to verify gate state |
| A-03 | The orchestrator possesses per-sub-skill synthesis confidence category knowledge at invocation time | Technical (data access) | Medium | Partially validated — SKILL.md provides the Sub-Skill Synthesis Output Map table, but orchestrator implementation does not confirm how it reads this table at runtime | Orchestrator assigns wrong confidence tier; LOW output presented as MEDIUM; P-022 violated |
| A-04 | A single capacity question ("what is your UX time allocation?") reliably classifies teams into < 20% vs 20-50% vs > 50% | Resource (measurement) | Medium | Not empirically validated — no pilot data cited | Orchestrator misclassifies team capacity; recommends Wave 3-5 sub-skills to a < 20%-time team; methodology overhead overwhelms tiny team |
| A-05 | The 3-field wave bypass documentation (unmet criterion, impact, remediation) prevents teams from systematically bypassing all waves to reach advanced sub-skills | Process (governance) | Medium | Not validated — no enforcement mechanism described | Teams document bypass fields perfunctorily and leap from Wave 0 directly to Wave 5; framework calibration absent; sub-skill outputs unreliable |
| A-06 | The fixed CRISIS sequence (Heuristic Eval → Behavior Design → HEART) is sufficient for all urgent UX failure patterns | Domain (methodology) | Low | Not validated — no research cited showing this sequence covers > X% of crisis scenarios | CRISIS user with "users cannot complete checkout" gets Design Sprint-level investment when a single JTBD study or Kano re-prioritization would resolve it faster |
| A-07 | The cross-framework synthesis signal extraction step correctly identifies convergent signals across heterogeneous sub-skill output formats | Technical (parsing) | Low | Not validated — sub-skill output formats are not yet specified; synthesis relies on "reading findings/recommendations sections" but section names vary per sub-skill | Synthesis produces false convergence (finding A from heuristic eval and finding B from HEART appear convergent by keyword proximity but address different issues); user acts on misleading HIGH confidence synthesis |
| A-08 | 10 UX frameworks are appropriate for a single tiny team (1-5 people) in a single product | Domain (scope) | Medium | Partially validated — tiny teams research cited but not linked to 10-framework selection | Teams experience framework paralysis; no sub-skill is fully adopted; Wave 1 never reaches Wave 2 completion threshold |
| A-09 | The 0.85 wave transition threshold reliably discriminates "deployment ready" from "not ready" | Process (measurement) | Medium | Not validated — ADR-PROJ022-002 explicitly marked "pending"; threshold called "provisional" | Gate permits low-quality sub-skill deployment at 0.85 when output is misleading; gate blocks high-quality deployment when calibration artifact is unusual |
| A-10 | Existing handoff schema (handoff-v2.schema.json) is sufficient for UX-specific cross-sub-skill handoffs (job statements, switch forces, validated hypotheses, severity-rated findings) | Technical (schema) | Medium | Not validated — handoff-v2 is a general schema; UX-specific artifact types listed in SKILL.md are not mapped to handoff-v2 fields | Handoff data lost in translation; ux-jtbd-analyst passes job statement to ux-design-sprint but job statement structure is not preserved in generic handoff format |
| A-11 | Session state flag mechanism (ONBOARD fires "once per session") is implemented and reliable | Technical (state) | Low | Not validated — no state mechanism described in ux-orchestrator stub | ONBOARD fires on every invocation; user receives HIGH RISK warning on every UX request in a session; repeated warnings trigger warning fatigue |
| A-12 | The ux-ai-design-guide CONDITIONAL gate ("Enabler DONE + WSM >= 7.80") will be enforced by the orchestrator at Wave 5 | Process (gate logic) | Medium | Not validated — WSM metric and its collection mechanism are not defined | ux-ai-design-guide invoked without the Enabler prerequisite; AI interaction design without prior framework calibration produces low-quality AI-first recommendations on insufficient product UX foundation |

---

## Detailed Findings

### IN-001-004: Sub-Skill Deployment Assumption Unvalidated [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Type** | Assumption (Technical) |
| **Assumption** | A-01: Sub-skill agents exist as functional Claude Code agents when the orchestrator calls Task |
| **Inversion** | All 10 sub-skills are marked `[PLANNED: Wave N]`; not a single sub-skill agent .md file exists outside the orchestrator stub |
| **Plausibility** | Certain — SKILL.md References table explicitly lists 10 out of 11 agents as `[PLANNED: Wave N]` |
| **Confidence** | Low |

**Evidence:**
From `skills/user-experience/SKILL.md` References section (lines 559-569):
```
| ux-heuristic-evaluator | ... | [PLANNED: Wave 1] |
| ux-jtbd-analyst        | ... | [PLANNED: Wave 1] |
| ux-lean-ux-facilitator | ... | [PLANNED: Wave 2] |
...
| ux-ai-design-guide     | ... | [PLANNED: Wave 5] |
```

The ux-orchestrator stub (line 23 of `skills/user-experience/agents/ux-orchestrator.md`): `<!-- STUB: Full agent definition to be implemented in PROJ-022 EPIC-001. -->`

The SKILL.md presents a complete routing capability including specific Task invocation syntax (lines 223-240) with concrete agent names, but none of the named subagent_type values correspond to existing agent files.

**Consequence:**
Any user invoking `/user-experience` with a real UX request will trigger the orchestrator; the orchestrator will attempt to invoke a sub-skill via Task; Claude Code will fail to find the agent. The entire routing promise of the SKILL.md is non-operational until Wave 1 completes. The SKILL.md does not disclose this operational status to readers or describe behavior when a sub-skill is absent.

**Affected Dimension:** Completeness — the deliverable omits the operational state gap; readers cannot distinguish the documented design from the deployable state.

**Mitigation:** Add a prominent operational status section to SKILL.md stating: "Current deployment status: Wave 0 — Orchestrator stub only. Sub-skills are not yet deployable. Wave 1 sub-skills (ux-heuristic-evaluator, ux-jtbd-analyst) target completion in PROJ-022 EPIC-001. Until Wave 1 signoff, invoking `/user-experience` will produce a routing response without sub-skill execution."

**Acceptance Criteria:** SKILL.md includes a "Current Deployment Status" section or banner listing which waves are signed off, which are pending, and what user-visible behavior to expect at each state. The section is updated on every wave signoff. Alternatively, this information is surfaced in ux-orchestrator's system prompt as a runtime guard.

---

### IN-002-004: Wave Gate Enforcement Mechanism Absent [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Type** | Assumption (Process) |
| **Assumption** | A-02: WAVE-N-SIGNOFF.md existence can be checked by the orchestrator before routing to gated sub-skills |
| **Inversion** | wave-progression.md is a full stub with `<!-- TODO (EPIC-001): -->` placeholders; no file path, schema, or query mechanism is described |
| **Plausibility** | Certain — confirmed by reading `skills/user-experience/rules/wave-progression.md` (all 4 sections are "Pending implementation") |
| **Confidence** | Low |

**Evidence:**
From `skills/user-experience/rules/wave-progression.md` (lines 20-23):
```
<!-- TODO (EPIC-001): Define per-wave quality gate criteria. -->
...
Pending implementation. Wave transition threshold: >= 0.85 deployment readiness score.
```

SKILL.md states (line 265): "The orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills."

But neither the ux-orchestrator `<methodology>` section (absent from stub) nor wave-progression.md provides: the file path where WAVE-N-SIGNOFF.md is expected, the schema for a valid signoff file, the orchestrator logic for checking file existence before a Task call, or what happens when the file is absent.

**Consequence:**
Without an enforcement mechanism, the wave gate is purely documentary. The SKILL.md asserts the gate exists ("The orchestrator checks...") but the assertion is unimplemented. An orchestrator following only the stub system prompt has no instructions to perform the check. A developer implementing EPIC-001 receives no specification for how the enforcement works — they must reconstruct the design intent from SKILL.md prose alone, with high risk of divergent implementation.

**Affected Dimension:** Methodological Rigor — the wave gate is the primary quality mechanism of the deployment model; an unenforced gate is not a gate.

**Mitigation:** wave-progression.md must define: (1) canonical file path for WAVE-N-SIGNOFF.md (`skills/user-experience/output/WAVE-N-SIGNOFF.md` or engagement-scoped), (2) minimum fields for a valid signoff (sub-skill quality scores, S-014 composite value, user approval timestamp), (3) orchestrator guard: before invoking any Wave N sub-skill, Read(file_path=WAVE-(N-1)-SIGNOFF.md); if file is absent or incomplete, surface error per gate rules. Acceptance criteria: wave-progression.md has all 4 sections populated with non-stub content, and the orchestrator `<methodology>` section in EPIC-001 includes the WAVE check as a named step.

---

### IN-003-004: Synthesis Confidence Category Not Accessible at Orchestrator Runtime [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Assumption (Technical) |
| **Assumption** | A-03: The orchestrator reads per-sub-skill synthesis confidence from the Sub-Skill Synthesis Output Map at invocation time |
| **Inversion** | The map is in SKILL.md (a human-readable document), not in a machine-queryable location; the orchestrator stub has no reference to this table |
| **Plausibility** | High — the orchestrator's system prompt (currently a stub) would need to embed or load this table |
| **Confidence** | Medium |

**Evidence:**
SKILL.md §Sub-Skill Synthesis Output Map (lines 344-356) contains the confidence classification per sub-skill synthesis step. However, the ux-orchestrator.md stub (lines 29-67) contains only a 4-bullet `<identity>` and 3-item `<guardrails>` section — no `<methodology>` that would include the synthesis confidence lookup logic.

synthesis-validation.md (all 4 sections): `Pending implementation.`

**Consequence:**
When the orchestrator produces cross-framework synthesis after Wave 2 completion, it must classify each signal's confidence tier. Without the synthesis output map accessible in its methodology, it will either (a) apply a generic MEDIUM to all synthesis outputs, undermining LOW-confidence enforcement per P-022, or (b) hallucinate per-sub-skill confidence classifications that deviate from the SKILL.md design.

**Affected Dimension:** Internal Consistency — P-022 is cited as the enforcement rationale for synthesis confidence gates, but the mechanism connecting the confidence table to orchestrator behavior is missing.

**Mitigation:** The ux-orchestrator system prompt `<methodology>` section in EPIC-001 must include the per-sub-skill confidence classification table as an embedded reference or include a Read step for `skills/user-experience/SKILL.md` §Sub-Skill Synthesis Output Map. synthesis-validation.md must specify how the orchestrator accesses confidence classifications and what error occurs when a sub-skill's synthesis step is not in the table.

---

### IN-004-004: Capacity Check Single-Question Reliability Assumption [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Assumption (Resource/Measurement) |
| **Assumption** | A-04: One structured question reliably classifies a team as < 20%, 20-50%, or > 50% UX time |
| **Inversion** | Teams overestimate available UX time at the start of an engagement; < 20% teams report "about 30%" and receive Wave 3 routing |
| **Plausibility** | High — overestimation of available capacity is a documented failure mode in time-allocation estimation literature |
| **Confidence** | Medium |

**Evidence:**
SKILL.md §Lifecycle-Stage Routing (lines 292-293):
```
2. CAPACITY CHECK: Ask team UX time allocation
   -> If < 20% of one person's time: recommend Wave 1 sub-skills only (P-020: user decides)
```

The SKILL.md offers no follow-up question, no calibration example, and no anchoring mechanism ("e.g., how many hours per sprint?"). ux-routing-rules.md: "Pending implementation. See SKILL.md..."

**Consequence:**
Teams with < 20% capacity select Wave 2+ sub-skills based on optimistic capacity self-report. ux-lean-ux-facilitator runs a multi-sprint experiment cycle for a team that has 2 hours per week available. Team abandons the methodology mid-cycle. Wave signoff is never achieved. Wave progression stalls. Tiny-team calibration goal (G-7) is violated without any behavioral trigger to detect the failure.

**Affected Dimension:** Evidence Quality — a single unanchored self-report question is insufficient evidence for routing decisions that determine weeks of methodology commitment.

**Mitigation:** Replace the binary < 20% / 20-50% question with a calibrated capacity prompt: "Approximately how many hours per sprint (or per week) does your team spend on UX? For reference: 2h/sprint is < 20%; 8h/sprint is ~20-50%." Add a secondary check: "Have you previously completed a UX methodology cycle to conclusion?" — teams with no prior completion are treated as < 20% regardless of stated allocation. These anchors do not override user decision (P-020); they inform it.

---

### IN-005-004: 3-Field Bypass Documentation Does Not Prevent Systemic Wave Skipping [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Assumption (Process/Governance) |
| **Assumption** | A-05: 3-field documentation (unmet criterion, impact, remediation) prevents teams from bypassing all waves |
| **Inversion** | A team fills in perfunctory bypass docs for Waves 1-4 in one session and jumps directly to Wave 5 (Design Sprint) |
| **Plausibility** | High — no constraint limits the number of simultaneous or consecutive bypasses; SKILL.md describes bypass as self-service |
| **Confidence** | Medium |

**Evidence:**
SKILL.md §Wave Architecture (lines 260-261): The bypass mechanism requires 3-field documentation and user confirmation. No limit on bypass count, no escalation required for multiple consecutive bypasses, no audit trail that surfaces cumulative bypass state.

Design Sprint early-access note (lines 260-261) explicitly describes skipping Waves 1-4 for teams "at product inception." The orchestrator is instructed to "present the bypass prompt" but no guard prevents the user from approving all five bypass prompts sequentially.

**Consequence:**
A team uses the Design Sprint sub-skill (Wave 5) without any JTBD job statement, heuristic calibration, Lean UX hypothesis history, or Atomic Design foundation. The Design Sprint challenge statement lacks user-research grounding. The orchestrator produces a sprint output that violates the very framework integrity (G-5) the wave gates are meant to protect. The cumulative bypass state is invisible in the output without an audit trail.

**Affected Dimension:** Methodological Rigor — the wave gate exists to enforce framework sequencing; a bypass mechanism that can be applied five consecutive times is equivalent to no gate.

**Mitigation:** Add a cumulative bypass ceiling: maximum 2 consecutive wave bypasses before a "methodology gap notice" is generated and persisted as a mandatory warning on all subsequent sub-skill outputs. Alternatively, require that any bypass of Waves 1-2 (foundational) triggers a governance-level user confirmation that explicitly names the methodology risk. Bypass audit trail stored in WAVE-BYPASS-LOG.md per engagement ID.

---

### IN-006-004: Fixed CRISIS Sequence May Misroute Non-Matching Failure Patterns [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Assumption (Domain) |
| **Assumption** | A-06: The fixed CRISIS sequence (Heuristic Eval → Behavior Design → HEART) is appropriate for all urgent UX failure patterns |
| **Inversion** | A team with "users can't find the checkout button" (layout/IA problem) is routed through the full CRISIS sequence including Behavior Design (Fogg B=MAP) and HEART metrics, adding overhead that delays the obvious fix |
| **Plausibility** | High — CRISIS problems have diverse root causes; a layout error does not require behavioral modeling |
| **Confidence** | Low |

**Evidence:**
SKILL.md §Lifecycle-Stage Routing (lines 309-311):
```
+-- "CRISIS: Urgent UX problems"  -> Emergency 3-skill sequence:
                                      Heuristic Eval -> Behavior Design -> HEART
```
SKILL.md §Common Intent-to-Route Resolution (line 324): `"CRISIS: urgent UX problems" | Emergency 3-skill sequence | No qualification needed`

The CRISIS path explicitly has "No qualification needed" — meaning the sequence fires without diagnosing whether the crisis type matches all three sub-skills.

Note: ux-routing-rules.md (line 31) shows the CRISIS sequence as `Heuristic Evaluation → HEART Metrics → JTBD Analysis` — different from SKILL.md's `Heuristic Eval → Behavior Design → HEART`. This is an internal inconsistency as well.

**Consequence:**
CRISIS users receive a 3-skill sequence that may mismatch their crisis type. A layout-only problem inflated into a B=MAP behavioral analysis wastes the team's most scarce resource (time). Additionally, the sequence discrepancy between SKILL.md and ux-routing-rules.md will produce divergent implementations when EPIC-001 builds out the routing.

**Affected Dimension:** Completeness — CRISIS mode covers a critical failure path with a blunt instrument and an internal discrepancy.

**Mitigation:** Add a minimal triage question before entering CRISIS mode: "Is the urgent problem about (a) users not finding/understanding interface elements, (b) users starting but not completing an action, or (c) not knowing whether UX is healthy?" Route (a) → Heuristic Eval only; (b) → Behavior Design then optionally HEART; (c) → HEART first. Resolve the sequence discrepancy between SKILL.md and ux-routing-rules.md in both files. Acceptance criteria: both files state identical CRISIS sequences.

---

### IN-007-004: Cross-Framework Synthesis Signal Extraction Lacks Format Contract [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Assumption (Technical) |
| **Assumption** | A-07: Signal extraction correctly identifies convergent signals across heterogeneous sub-skill output formats |
| **Inversion** | Sub-skills produce outputs with different section names, finding numbering schemes, and severity vocabularies; the orchestrator cannot reliably detect convergence without a shared format contract |
| **Plausibility** | High — sub-skill output formats are not yet specified (all sub-skills are [PLANNED]); without a format contract, implementation will diverge |
| **Confidence** | Low |

**Evidence:**
SKILL.md §Cross-Framework Synthesis Protocol (lines 373-376):
```
1. Signal Extraction: The orchestrator reads each sub-skill output's findings/recommendations
   sections and extracts actionable signals (findings rated severity >= 2 for heuristic eval;
   metrics below target for HEART; unvalidated assumptions for Lean UX; etc.).
```

The extraction logic is sub-skill-specific (severity >= 2 for heuristic eval, metrics below target for HEART) but defined only in SKILL.md prose — not in a machine-queryable extraction schema. No shared output format contract is referenced. synthesis-validation.md Section "Synthesis Protocol Validation": `Pending implementation.`

**Consequence:**
Each sub-skill EPIC team independently implements output format. ux-heuristic-evaluator uses `Severity: 3` notation. ux-heart-analyst uses `Status: Below Target`. ux-lean-ux-facilitator uses `Validated: false`. The orchestrator's signal extraction logic (written for one format) fails silently against the others. Convergence detection is unreliable. The synthesis hypothesis confidence classification (HIGH/MEDIUM/LOW) is applied to false or missed convergences, violating P-022.

**Affected Dimension:** Internal Consistency — cross-framework synthesis is architecturally promised but technically unconstrained.

**Mitigation:** Define a minimal "signal extraction contract" in synthesis-validation.md: a standardized `## Synthesis Signals` section that every sub-skill output MUST produce, listing extractable signals in a consistent format (e.g., `- Signal: {description} | Severity: {1-4} | Framework: {framework-name}`). The orchestrator reads only this section for cross-framework synthesis. Acceptance criteria: synthesis-validation.md defines the signal section format and at least one sub-skill (ux-heuristic-evaluator or ux-heart-analyst) implements it before Wave 2 synthesis is first attempted.

---

## Step 5: Recommendations

### Critical Findings — MUST Mitigate

**IN-001-004: Sub-Skill Deployment Status Undisclosed**
- Action: Add "Current Deployment Status" banner to SKILL.md with per-wave deployment state; add orchestrator runtime guard for absent sub-skills
- Acceptance Criteria: SKILL.md states which waves are signed off; orchestrator returns graceful error (not Task failure) when sub-skill is absent; banner is updated on each wave signoff commit

**IN-002-004: Wave Gate Enforcement Mechanism Absent**
- Action: wave-progression.md must be populated with: canonical WAVE-N-SIGNOFF.md path, minimum signoff schema, orchestrator pre-routing check logic
- Acceptance Criteria: wave-progression.md has all 4 sections non-stub; ux-orchestrator methodology section includes wave check step; wave check is covered by CI gate in ci-checks.md

### Major Findings — SHOULD Mitigate

**IN-003-004: Synthesis Confidence Category Inaccessible**
- Action: Embed per-sub-skill confidence table in ux-orchestrator system prompt OR define synthesis-validation.md lookup mechanism
- Acceptance Criteria: synthesis-validation.md Section "Confidence Classification" is non-stub; orchestrator methodology includes confidence lookup step

**IN-004-004: Capacity Check Reliability**
- Action: Replace single capacity question with anchored prompt (hours/sprint) and prior-completion secondary check
- Acceptance Criteria: ux-routing-rules.md Section "Lifecycle Stage Router" documents the anchored capacity question; routing logic is testable against known team profiles

**IN-005-004: Bypass Accumulation Risk**
- Action: Add cumulative bypass ceiling (max 2 consecutive) and bypass audit log per engagement ID
- Acceptance Criteria: wave-progression.md Bypass Mechanism section specifies ceiling and WAVE-BYPASS-LOG.md format

**IN-006-004: CRISIS Sequence Mismatch + Discrepancy**
- Action: Add minimal CRISIS triage question; resolve sequence discrepancy between SKILL.md (Heuristic → Behavior → HEART) and ux-routing-rules.md (Heuristic → HEART → JTBD)
- Acceptance Criteria: SKILL.md and ux-routing-rules.md list identical CRISIS sequences; CRISIS triage is documented in ux-routing-rules.md

**IN-007-004: Signal Extraction Format Contract Absent**
- Action: Define standardized `## Synthesis Signals` section format in synthesis-validation.md
- Acceptance Criteria: synthesis-validation.md defines the signal format; at least the first two sub-skills (Wave 1) implement it before Wave 2 synthesis is attempted

---

## Scoring Impact

| Dimension | Weight | Impact | Findings Driving Impact |
|-----------|--------|--------|------------------------|
| Completeness | 0.20 | Negative | IN-001-004 (absent deployment status), IN-006-004 (incomplete CRISIS coverage) — the skill omits operational state and handles CRISIS with a blunt fixed sequence |
| Internal Consistency | 0.20 | Negative | IN-003-004 (confidence table not wired to orchestrator), IN-007-004 (no signal format contract), IN-006-004 (CRISIS sequence discrepancy between SKILL.md and ux-routing-rules.md) — architectural promises are made without consistent implementation scaffolding |
| Methodological Rigor | 0.20 | Negative | IN-002-004 (wave gate unenforced), IN-005-004 (bypass accumulation unconstrained) — the wave progression model's two quality controls (gate and bypass) are stated but mechanically unimplemented |
| Evidence Quality | 0.15 | Negative | IN-004-004 (capacity check unanchored single question), IN-001-004 (deployment status is a gap that should be evidenced in the document) — routing decisions relying on uncalibrated self-report and absent sub-skills reduce evidence credibility |
| Actionability | 0.15 | Mixed | Positive: all mitigations above are specific and actionable; each has an acceptance criterion. Negative: the current SKILL.md delivers routing descriptions and framework catalogs but no actionable operational steps for a team encountering the skill before Wave 1 completes |
| Traceability | 0.10 | Neutral | Framework references and standards citations are thorough and accurate; all findings trace to specific SKILL.md line ranges and stub rule files |

**Overall Assessment: REVISE**

The SKILL.md is architecturally coherent and thoroughly documented for a design-phase deliverable. The two Critical findings are characteristic of a SKILL.md that is ahead of its implementation — the design is sound, but the document presents full operational capability while being pre-Wave 1. Addressing IN-001-004 and IN-002-004 requires documentation of current state and enforcement mechanism specification, not architectural revision. All Major findings require additions to currently-stub rule files. No finding requires rethinking the core wave architecture or agent hierarchy.

---

## Execution Statistics
- **Total Findings:** 7
- **Critical:** 2
- **Major:** 5
- **Minor:** 0
- **Protocol Steps Completed:** 6 of 6
- **Goals Analyzed:** 7
- **Assumptions Mapped:** 12
- **Anti-Goal Conditions Identified:** 7 per goal (49 total conditions assessed)
- **Vulnerable Assumptions:** 7 (stress-tested with IN-NNN identifiers)
