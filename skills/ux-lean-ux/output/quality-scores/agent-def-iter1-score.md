# Quality Score Report: ux-lean-ux-facilitator Agent Definition

## L0 Executive Summary
**Score:** 0.884/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.78)
**One-line assessment:** A well-structured, nearly complete agent definition that passes all structural gates but has a meaningful gap in methodological specification (ICE scoring scale undefined) and traceability evidence for its reasoning_effort justification; targeted fixes to these areas are sufficient to reach the 0.95 C4 threshold.

---

## Scoring Context
- **Deliverable:** `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` + `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.governance.yaml`
- **Deliverable Type:** Agent definition (H-34 dual-file architecture)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (C4 quality gate)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.884 |
| **Threshold** | 0.95 (C4 H-13) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 7 .md body sections present; all required governance fields populated; H-34 dual-file compliance met; one minor gap: `reasoning_effort` placement outside schema-defined path |
| Internal Consistency | 0.20 | 0.91 | 0.182 | .md and governance agree on tool tier (T3), cognitive mode (systematic), tools list; description matches methodology outputs; Wave and SKILL.md references consistent |
| Methodological Rigor | 0.20 | 0.86 | 0.172 | 5-step workflow well-specified with tables and diagrams; ICE scoring formula referenced but scale/rating criteria not defined; assumption map quadrant diagram included; experiment type selection criteria clear |
| Evidence Quality | 0.15 | 0.78 | 0.117 | Gothelf & Seiden (2021, 3rd ed.) cited correctly; reasoning_effort justification asserts "C4 applies to overall deliverable quality gate, not per-agent reasoning" without citation; ICE scoring attribution ("ICE scoring") lacks source; AI-supplement heuristic citations absent (contrast: ux-heuristic-evaluator cites Amershi et al. 2019 and Google PAIR) |
| Actionability | 0.15 | 0.93 | 0.140 | Input format fully specified with field names, formats, and optional fields; output location template clear with examples; on-send YAML payload fully enumerated; degraded mode disclosure protocol defined; fallback behaviors for each failure mode documented |
| Traceability | 0.10 | 0.89 | 0.089 | Footer traceability comment covers 13 standard IDs (H-34, AD-M-001 through ET-M-001, SR-002/003/009, AR-012); links to SKILL.md, Jerry Constitution, and parent skill all resolvable; Wave 2 reference points to wave-progression.md (not verified to exist but follows established pattern); governance.yaml references `docs/governance/JERRY_CONSTITUTION.md` correctly |
| **TOTAL** | **1.00** | | **0.884** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**

*Markdown file (.md):*
- Frontmatter contains ONLY official Claude Code fields: `name`, `description`, `model`, `tools`, `disallowedTools`, `mcpServers`. No non-official fields present. PASS.
- All 7 required markdown body sections present with XML tags: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`. PASS.
- `<identity>` includes role, expertise (6 bullet domains), cognitive mode, and key distinction table. PASS.
- `<input>` includes required/optional fields, input validation checklist (5 items), and degraded mode protocol. PASS.
- `<guardrails>` includes constitutional compliance table, forbidden actions (6 entries), input validation, output filtering, fallback behavior, and P-003 runtime self-check. PASS.
- `<output>` includes output location template, full 9-section required report structure, all section formats, on-send YAML payload, and handoff threshold rule. PASS.

*Governance file (.governance.yaml):*
- Required fields: `version` (1.0.0 -- valid semver PASS), `tool_tier` (T3 -- valid enum PASS), `identity.role`, `identity.expertise` (5 items >= minItems:2 PASS), `identity.cognitive_mode` (systematic -- valid enum PASS). All PASS.
- Recommended fields present: `persona` (tone, communication_style, audience_level), `capabilities.forbidden_actions` (3 entries >= minItems:3 PASS), `forbidden_action_format` (NPT-009-complete), `allowed_tools` (9 tools), `output_formats`, `guardrails.input_validation`, `guardrails.output_filtering` (5 items >= minItems:3 PASS), `guardrails.fallback_behavior` (warn_and_retry -- valid pattern PASS), `output.required`, `output.location`, `output.levels` (L0, L1, L2), `constitution.principles_applied` (5 items >= minItems:3 PASS), `validation.post_completion_checks` (6 items), `session_context.on_receive` (4 items), `session_context.on_send` (5 items), `enforcement` (quality_gate, quality_threshold, tier, escalation_path). All present. PASS.

**Gaps:**

1. `reasoning_effort` is declared as `reasoning_effort: medium` with an inline comment inside `capabilities` block. The schema uses `additionalProperties: true` for capabilities, so this is structurally valid. However, per ET-M-001, `reasoning_effort` is an agent-level field, not a capabilities sub-field. The reference agent (ux-heuristic-evaluator.governance.yaml line 38) places it as a top-level YAML field outside any object. In the scored file, it is nested inside `capabilities` -- this is a structural placement deviation from the reference pattern.

2. Minor: The governance.yaml does not declare `session_context.schema` (optional per schema), consistent with the reference agent.

**Improvement Path:**
Move `reasoning_effort: medium` to top-level in the YAML (outside `capabilities` block), matching the structural pattern of the reference agent. This raises completeness to 0.95+.

---

### Internal Consistency (0.91/1.00)

**Evidence:**

- **Tool tier vs tools declared:** `.md` `tools` field = [Read, Write, Edit, Glob, Grep, WebSearch, WebFetch]. Governance `tool_tier` = T3. T3 per agent-development-standards.md includes "T2 + WebSearch, WebFetch, Context7." WebSearch and WebFetch present. Context7 declared via `mcpServers` (architecturally correct per H-34). Consistent.
- **Cognitive mode:** `.md` body says "Systematic" (Step 1 sentence: "you apply the Build-Measure-Learn cycle methodology step-by-step"). Governance `cognitive_mode: systematic`. Consistent.
- **Agent name:** `.md` frontmatter `name: jerry:ux-lean-ux-facilitator`. Governance comment `Runtime config: ux-lean-ux-facilitator.md`. SKILL.md `agents: [ux-lean-ux-facilitator]`. All consistent.
- **Description vs methodology outputs:** Description lists "hypothesis backlogs, assumption maps, MVP experiment designs, and validated learning logs." Methodology Step 1 produces the hypothesis backlog, Step 2 the assumption map, Step 3 the experiment designs, Step 4 the validated learning log. Consistent.
- **Wave designation:** `<purpose>` says "Wave 2 (Data-Ready)". Footer metadata says "Wave: 2 (Data-Ready)". Consistent.
- **Forbidden actions mirror:** `.md` `<guardrails>` lists 6 forbidden actions. Governance `forbidden_actions` lists 3 (the constitutional triplet). The `.md` has 3 additional domain-specific entries (assumption quadrant rationale, BML cycle step skipping, Miro fidelity claim). This is not a contradiction -- governance captures the minimum constitutional triplet while `.md` elaborates with domain-specific entries. Consistent by design.
- **Constitutional triplet (P-003, P-020, P-022):** Present in both `.md` guardrails table AND governance `constitution.principles_applied`. PASS.

**Gaps:**

1. The `<identity>` section references "AD-M-005, ET-M-001" in parentheses within the Cognitive Mode paragraph. AD-M-005 is about expertise entries (which this file also has). ET-M-001 is about reasoning_effort. This cross-reference is to the governance field, but the governance `reasoning_effort` value is `medium`. The `.md` does not state the reasoning effort anywhere in the body -- no slight inconsistency, but the standard referenced (ET-M-001) is only documented in governance, not in the `.md` body itself, which could cause confusion for a reader of only the `.md`.

2. Minor: The `<purpose>` section says "Its validated/invalidated hypothesis outputs feed directly into HEART Metrics." The on-send protocol does not explicitly list the HEART Metrics sub-skill as a named downstream target; it refers generically to "downstream sub-skills." The Handoff Data section does name "HEART Metrics" explicitly. No contradiction, just slight inconsistency in specificity.

**Improvement Path:**
Add a brief note in `<identity>` or `<capabilities>` that references `reasoning_effort: medium` to make the ET-M-001 self-reference internally complete.

---

### Methodological Rigor (0.86/1.00)

**Evidence:**

- **5-step workflow:** All 5 steps present with clear names and sequential dependency declarations ("Every step must complete before proceeding to the next"). Systematic cognitive mode correctly applied.
- **Hypothesis format:** Canonical Lean UX format documented with 4 components (Outcome, Users, Change, Evidence) in a table with descriptions and examples. Component table is high quality.
- **Hypothesis lifecycle:** Status states (DRAFT, ACTIVE, VALIDATED, INVALIDATED, DEFERRED) defined with format (`HYP-{NNN}`). Lifecycle transitions implied by the workflow steps.
- **Assumption mapping:** 4-quadrant ASCII diagram present with correct axis labels (Known/Unknown x High Risk/Low Risk). Quadrant action table (Q1-Q4) with action and priority. 3 assumption categories defined. Rating discipline rule ("when uncertain, choose HIGHER-risk quadrant") present and well-reasoned.
- **Experiment types:** 7 experiment types tabulated with Best For, Confidence, Duration, Cost columns. Experiment selection criteria (5 rules) provided. Each experiment design output format specified.
- **Learning documentation:** Per-cycle format template with 8 required fields. Decision framework (PERSEVERE/PIVOT/KILL) defined.
- **Self-review (Step 5):** 7-point S-010 checklist present before persisting.
- **Synthesis judgments:** Confidence classification table (HIGH/MEDIUM/LOW) with criteria and action.
- **Single-facilitator reliability note:** Limitation disclosed with compensation strategy per P-022. Recommendation for human supplement provided.

**Gaps:**

1. **ICE scoring scale not defined (SIGNIFICANT GAP):** The hypothesis backlog table header shows "ICE Score" as `{I+C+E}/3`. The methodology Step 1 mentions "ICE scoring (Impact, Confidence, Ease) for hypothesis prioritization." The identity section lists ICE scoring in expertise. However, nowhere in the methodology is the ICE rating scale defined: what does a 1-10 Impact score look like? What makes Confidence a 1 vs a 7? Without rating scale definitions, two practitioners would score the same hypothesis differently, undermining the claimed systematic rigor. This is not present even in condensed form.

2. **BML cycle handoff trigger to Step 5 unclear:** Step 4 (Validated Learning) says "After each cycle, re-score remaining hypotheses in the backlog." The transition from Step 4 back into Step 1 (iteration) is described at a high level but the trigger for when to start a new cycle vs. proceed to Step 5 is not defined. A practitioner with only this document would be uncertain whether Step 5 runs after each hypothesis or at the end of all hypotheses in scope.

3. **Upstream data integration is MEDIUM not LOW detail:** Step 1 describes "When upstream data is available" integration from JTBD, Heuristic Evaluation, and Design Sprint. This integration pattern is described at a useful level, though the exact mapping (e.g., "which JTBD artifact field maps to which hypothesis component") is left implicit.

**Improvement Path:**
Add an ICE Scoring Scale subsection to Step 1 that defines Impact (1-10: user reach and business value), Confidence (1-10: evidence strength), and Ease (1-10: inverse of implementation effort) with anchor examples for each dimension. This single addition would raise this dimension to 0.92+.

---

### Evidence Quality (0.78/1.00)

**Evidence:**

- **Primary methodology citation:** Gothelf & Seiden (2021, 3rd ed.) cited in identity section, description, and governance expertise. Specific edition cited. PASS.
- **Assumption mapping source:** "4-quadrant risk/knowledge framework per Gothelf & Seiden (2021)" -- attributed. PASS.
- **Output location is canonical:** References `skills/ux-lean-ux/output/{engagement-id}/...` which follows the established pattern from the reference agent.
- **Wave progression reference:** `skills/user-experience/rules/wave-progression.md` cited in `<purpose>`. This is a specific, verifiable path.

**Gaps:**

1. **ICE scoring attribution missing:** The methodology section uses ICE scoring extensively but does not cite the source. ICE scoring is generally attributed to Sean Ellis and the Growth Hacking literature. A practitioner reading this cannot trace where the ICE formula originated or verify the `{I+C+E}/3` formula against the canonical source.

2. **reasoning_effort justification uncited:** The comment "C4 applies to overall deliverable quality gate, not per-agent reasoning" is an interpretive claim about how ET-M-001 applies. ET-M-001 states "Orchestrator agents SHOULD use `high` or `max`" and "Mapping: C1=default, C2=medium, C3=high, C4=max." A facilitator agent (worker, not orchestrator) using `medium` at C4 is a deliberate deviation from the mapping. The justification is reasonable but states it as fact without citing the ET-M-001 exception case or documenting it as a formal MEDIUM override with documented justification per the standards.

3. **Contrast with reference agent:** `ux-heuristic-evaluator.md` cites Amershi et al. (2019) "Guidelines for Human-AI Interaction" and Google PAIR "People + AI Guidebook" (2019) for its AI supplement heuristics. `ux-lean-ux-facilitator.md` does not have equivalent secondary-source citations for experiment design patterns or any of the 7 experiment types. While Gothelf & Seiden is the primary source, the 7 experiment types table draws on broader lean startup / MVP literature (Ries, 2011; SVPG) that goes uncited.

4. **Synthesis judgment cross-reference:** The synthesis judgments table in Step 5 mentions a "synthesis gate" but does not reference `skills/user-experience/rules/synthesis-validation.md` (which the heuristic evaluator references in its Step 5). If this file exists, the lean UX facilitator should reference it. If it does not exist for this sub-skill, that gap should be noted.

**Improvement Path:**
(1) Add ICE scoring citation (Sean Ellis / Growth Hacking literature, or any authoritative source). (2) Add a citation or standards reference for the ET-M-001 deviation (or promote the reasoning_effort justification to a formal MEDIUM override note in governance). (3) Add secondary citations for at least the experiment type taxonomy. (4) Add reference to synthesis-validation.md in Step 5 if the file exists, or note its absence.

---

### Actionability (0.93/1.00)

**Evidence:**

- **Input format:** The `## UX CONTEXT (REQUIRED)` block is complete with 5 named fields, typed expectations, and clear optionality boundaries. An invoking orchestrator has a precise template to fill.
- **Output location:** `skills/ux-lean-ux/output/{engagement-id}/ux-lean-ux-facilitator-{topic-slug}.md` with variable definitions and kebab-case example. Unambiguous.
- **Output structure:** 9-section required structure with section names, level labels, and purpose descriptions. The backlog table has column headers with format examples (`HYP-001`, `{I+C+E}/3`). Experiment and learning formats use code blocks with all required fields.
- **On-send payload:** Complete YAML payload with field names, types (int, bool), and inline comments explaining semantics. An orchestrator can parse this immediately.
- **Degraded mode:** Disclosed in `<input>` with specific feature reductions listed. A user knows exactly what capability is missing.
- **Fallback behaviors:** 4 distinct fallback scenarios documented with specific orchestrator response instructions.
- **P-003 runtime self-check:** 4-point checklist with a specific error message string for violation. Fully executable.

**Gaps:**

1. **ICE formula in backlog table header** shows `{I+C+E}/3` but the actual score is not shown as a number (e.g., 7.0 out of 10) or a classification. Without knowing the scale (see Methodological Rigor gap), a practitioner cannot compute the score. The actionability of the backlog format is partially undermined by the undefined scale.

2. **Cycle scope field guidance:** The optional `Cycle Scope` field lists 5 valid values (`hypothesis-generation | assumption-mapping | experiment-design | learning-documentation | full-cycle`). However, the methodology does not define what happens when a partial scope is requested -- does the agent produce only Step 1 artifacts when scope is `hypothesis-generation`? Does it skip Steps 2-5? This partial-scope behavior is unspecified.

**Improvement Path:**
Add a one-paragraph "Partial Scope Behavior" note in `<input>` or `<methodology>` clarifying which steps execute for each `Cycle Scope` value.

---

### Traceability (0.89/1.00)

**Evidence:**

- **Footer traceability comment:** 13 standard IDs listed: H-34, H-34b, AD-M-001, AD-M-004, AD-M-005, AD-M-006, AD-M-007, AD-M-008, ET-M-001, SR-002, SR-003, SR-009, AR-012. Each maps to a verifiable standard in agent-development-standards.md.
- **SSOT declaration:** Footer states `SSOT: skills/ux-lean-ux/SKILL.md`. Verified: SKILL.md exists at that path, lists `ux-lean-ux-facilitator` in its agents array.
- **Parent skill reference:** `Parent Skill: /user-experience v1.0.0` -- references the parent user-experience skill. Traceable.
- **Governance constitution reference:** `docs/governance/JERRY_CONSTITUTION.md` -- standard path verified against quality-enforcement.md.
- **Wave progression reference:** `skills/user-experience/rules/wave-progression.md` -- referenced in `<purpose>`. File was not verified to exist during this scoring, but follows the established reference pattern.
- **Inline standard references in guardrails:** `(H-34b, AR-012)` after forbidden actions, `(SR-002)` after input validation, `(SR-009)` after fallback -- all present and traceable.
- **Identity section references:** `(AD-M-005, ET-M-001)` inline in the Cognitive Mode paragraph. Traceable to agent-development-standards.md.

**Gaps:**

1. **synthesis-validation.md not referenced:** The heuristic evaluator cites `skills/user-experience/rules/synthesis-validation.md` in its Step 5. The lean UX facilitator's Step 5 has an equivalent synthesis judgments section but does not reference this rule file. If the file governs synthesis validation across all sub-skills, the traceability chain is broken for this agent.

2. **ICE scoring source untraced:** The ICE scoring methodology has no citation or standards reference anywhere in the file, making it an untraceable methodology claim.

3. **Handoff schema reference absent:** The on-send protocol produces YAML-structured data but does not reference `docs/schemas/handoff-v2.schema.json` or any handoff schema. The reference agent (ux-heuristic-evaluator) does not reference it either, so this is a consistent pattern, but it is still a traceability gap.

**Improvement Path:**
(1) Add `skills/user-experience/rules/synthesis-validation.md` reference in Step 5 (or explicitly note it does not apply to this sub-skill). (2) Add ICE scoring source citation. Both improvements are low-effort.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Methodological Rigor | 0.86 | 0.93 | Add ICE Scoring Scale subsection in Step 1: define Impact (1-10), Confidence (1-10), Ease (1-10) with one anchor example per scale (low/mid/high). This is the single largest gap in the methodology. |
| 2 | Evidence Quality | 0.78 | 0.90 | (a) Add ICE scoring source citation (Sean Ellis or equivalent). (b) Add citation for the experiment type taxonomy (Gothelf & Seiden covers some, but Fake Door/Smoke Test origins are from lean startup literature). (c) Add formal ET-M-001 deviation note or cite standards exception for reasoning_effort: medium at C4 for a worker agent. |
| 3 | Completeness | 0.92 | 0.96 | Move `reasoning_effort: medium` to top-level in governance.yaml (outside `capabilities` block) to match the structural pattern of the reference agent (ux-heuristic-evaluator.governance.yaml line 38). |
| 4 | Actionability | 0.93 | 0.96 | Add "Partial Scope Behavior" note clarifying which methodology steps execute for each `Cycle Scope` value. |
| 5 | Traceability | 0.89 | 0.93 | (a) Add reference to `skills/user-experience/rules/synthesis-validation.md` in Step 5 (or explicitly note non-applicability). (b) Add ICE scoring citation to traceability comment. |
| 6 | Internal Consistency | 0.91 | 0.94 | Add a note in `<capabilities>` or `<identity>` that ET-M-001 reasoning_effort is declared in governance at `medium`, making the cross-reference to ET-M-001 in the cognitive mode paragraph self-contained within the .md file. |

---

## Leniency Bias Check
- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score (specific line numbers / field names cited)
- [x] Uncertain scores resolved downward (Methodological Rigor: 0.86 not 0.88; Evidence Quality: 0.78 not 0.82)
- [x] First-draft calibration considered (this is Iteration 1; Evidence Quality gap reflects a genuine first-draft omission)
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Composite (0.884) is below the C4 threshold (0.95) -- consistent with a strong first draft that has identifiable, fixable gaps

---

## Computation Verification

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| Completeness | 0.20 | 0.92 | 0.1840 |
| Internal Consistency | 0.20 | 0.91 | 0.1820 |
| Methodological Rigor | 0.20 | 0.86 | 0.1720 |
| Evidence Quality | 0.15 | 0.78 | 0.1170 |
| Actionability | 0.15 | 0.93 | 0.1395 |
| Traceability | 0.10 | 0.89 | 0.0890 |
| **TOTAL** | **1.00** | | **0.8835 ≈ 0.884** |

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.884
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.78
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add ICE Scoring Scale subsection (Impact/Confidence/Ease 1-10 with anchor examples) to Step 1 of methodology"
  - "Add ICE scoring source citation and experiment type taxonomy citations"
  - "Add formal ET-M-001 deviation note for reasoning_effort: medium at C4 worker level"
  - "Move reasoning_effort to top-level in governance.yaml (structural placement fix)"
  - "Add Partial Scope Behavior note for Cycle Scope field in <input>"
  - "Add synthesis-validation.md reference in Step 5 or note non-applicability"
```

---

*Scored by: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*SSOT: `.context/rules/quality-enforcement.md`*
*Reference agent: `skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md`*
*Governance schema: `docs/schemas/agent-governance-v1.schema.json`*
*Scoring date: 2026-03-04*
