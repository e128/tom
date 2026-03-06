# Quality Score Report: Lean UX Sub-Skill SKILL.md

## L0 Executive Summary

**Score:** 0.949/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.92)
**One-line assessment:** All four iter2-specified fixes are verified as applied (ICE attribution corrected to Sean Ellis/GrowthHackers, H-26 reference normalized, on_receive/on_send inline tables enumerated, agent table stub marker fixed), raising the composite by 0.009 to 0.949 — one one-thousandth below the 0.950 threshold; the single blocking gap is two residual line-number citations in source footnotes that were not converted to section-anchor format despite iter2 committing to full conversion.

---

## Scoring Context

- **Deliverable:** `skills/ux-lean-ux/SKILL.md`
- **Deliverable Type:** Design (sub-skill specification)
- **Criticality Level:** C4 (critical — sub-skill specification)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (user-specified, above H-13 standard 0.92)
- **Scored:** 2026-03-04T00:00:00Z
- **Wave 1 structural reference:** `skills/ux-heuristic-eval/SKILL.md`
- **Prior Score:** 0.940 (iter2, 2026-03-04)
- **Iteration:** 3

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.949 |
| **Threshold** | 0.95 (user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Delta from iter2** | +0.009 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.95 | 0.190 | All 20 sections present; [PLANNED] markers intact; AI limitations disclosure intact; no new gaps introduced |
| Internal Consistency | 0.20 | 0.95 | 0.190 | `**` stub marker fix verified: agent table shows clean `ux-lean-ux-facilitator` with STUB note as separate paragraph; ICE tie-breaking aligns with quadrant priority table; all cross-references hold |
| Methodological Rigor | 0.20 | 0.96 | 0.192 | No regressions; experiment selection guide and ICE prioritization subsection intact from iter2; correct ICE source does not weaken methodology content |
| Evidence Quality | 0.15 | 0.92 | 0.138 | ICE attribution corrected (Sean Ellis/GrowthHackers circa 2015 — factually accurate); two line-number citations remain unconverted: `(lines 174-196)` and `(lines 200-250)` in source footnotes — iter2 claimed full section-anchor conversion but these two instances were missed |
| Actionability | 0.15 | 0.96 | 0.144 | on_receive/on_send fields enumerated as inline tables with 5 fields each (4-column format: field, type, required, description) — iter2 gap closed; all four invocation pathways intact |
| Traceability | 0.10 | 0.95 | 0.095 | H-26(c) reference normalized to "explicit exception to the H-26 registration requirement (parent-routed model)" — traceable to documented rule text; section-anchor citations throughout; minor residual: 2 line-number supplements in source footnotes |
| **TOTAL** | **1.00** | | **0.949** | |

**Composite (precise):** (0.95 × 0.20) + (0.95 × 0.20) + (0.96 × 0.20) + (0.92 × 0.15) + (0.96 × 0.15) + (0.95 × 0.10)
= 0.190 + 0.190 + 0.192 + 0.138 + 0.144 + 0.095
= **0.949**

---

## Detailed Dimension Analysis

### Completeness (0.95/1.00)

**Evidence:**

All four iter3 fixes are present and do not introduce new completeness gaps:

1. No new sections added or removed; the Document Sections nav table at line 44 correctly reflects all 20 sections with anchor links.
2. The `### AI-Augmented Analysis Limitations` subsection under Constitutional Compliance remains intact from iter2 with four specific disclosures (hypotheses are secondary-research-derived, experiment interpretation is data-dependent, assumption mapping reflects AI judgment, validate with real user data).
3. [PLANNED: Wave 2 Phase 2] markers on all four pending files remain present in the References and Templates sections.
4. The nav table entry for Constitutional Compliance still correctly reads "Governing principles and AI-augmented analysis limitations" matching the section content.

No new completeness gaps were introduced by the four iter3 fixes. The iteration 3 changes are all corrections to existing content (ICE source text, H-26 label text, inline tables added, stub marker formatting) — none remove required sections or add unclosed gaps.

**Gaps:**

No material completeness gaps. Minor: The Available Agents table footnote note on model escalation is not present for the Lean UX facilitator (Wave 1 heuristic evaluator has it; this Wave 2 sub-skill does not). This is a Wave 1 structural pattern that may not apply to Wave 2 given Sonnet is not typically escalated like Haiku. Low materiality — omitting non-applicable escalation guidance is correct.

**Improvement Path:**

No action needed on completeness. Score is stable at 0.95.

---

### Internal Consistency (0.95/1.00)

**Evidence:**

The iter3 agent table stub marker fix is confirmed. The agent table at line 123-125 shows:

```markdown
| Agent | Role | Tier | Mode | Model | Output Location |
|-------|------|------|------|-------|-----------------|
| `ux-lean-ux-facilitator` | Lean UX hypothesis and experiment facilitation specialist | T3 | Systematic | Sonnet | ... |
```

The `**STUB:**` notation appears as a separate bold paragraph immediately below the table (line 127), not as `ux-lean-ux-facilitator**` within the cell. This resolves the iter2 internal consistency gap where literal-string parsing would produce an incorrect agent name.

The new ICE source text ("Sean Ellis, GrowthHackers, circa 2015") does not create any internal contradictions. The ICE tie-breaking rule ("prefer the hypothesis in the higher-risk assumption quadrant Q1 > Q2 > Q4 > Q3") continues to align with the Assumption Mapping quadrant priority table (Q1=HIGHEST, Q2=MEDIUM, Q4=LOWEST, Q3=LOW).

The on_receive/on_send inline tables are internally consistent with the Task tool invocation example: the on_receive fields (`engagement_id`, `product_context`, `design_change`, `prior_experiment_results`, `upstream_artifacts`) map to the context fields shown in the Task tool prompt example (`Engagement ID`, `Topic/Product Context`, `Design Change`, `Prior experiments`, `Upstream artifacts`). The on_send fields (`hypothesis_backlog`, `assumption_map`, `experiment_designs`, `validated_learning_log`, `synthesis_judgments`) align with the Required Output Sections table.

Cross-references to `mcp-coordination.md` (Miro REQ, Figma ENH, Hotjar ENH for `/ux-lean-ux`) and `synthesis-validation.md` (MEDIUM confidence for assumption mapping and hypothesis generation) remain correct and unchanged.

**Gaps:**

No internal consistency gaps remain after the iter3 stub marker fix. The pre-existing `**` issue that scored 0.93 in iter2 is resolved.

**Improvement Path:**

No action needed on internal consistency.

---

### Methodological Rigor (0.96/1.00)

**Evidence:**

Iter3 introduced no methodological content changes — it corrected the ICE source attribution without weakening the methodology itself. The ICE scoring subsection (lines 262-274) retains:
- Three-dimension scoring table (Impact 1-10, Confidence 1-10, Ease 1-10) with question framing
- ICE formula: (Impact + Confidence + Ease) / 3
- Tie-breaking rule: prefer higher-risk assumption quadrant (Q1 > Q2 > Q4 > Q3)
- Calibration note for tiny teams ("30-second scoring pass per hypothesis")
- Re-scoring guidance ("Re-score after each Build-Measure-Learn cycle as evidence changes confidence levels")

The corrected source attribution ("a product prioritization framework originating from the growth hacking community") is more factually accurate than the previous Gothelf & Seiden Chapter 3 citation, and does not diminish the methodological value of the ICE scoring content.

All other methodology sections from iter2 remain complete and intact:
- Hypothesis Format with Lean UX 4-component structure
- Assumption Mapping with 4-quadrant ASCII diagram and priority table
- Experiment Types with 7-row decision matrix and 5-step quick decision path
- Build-Measure-Learn Cycle with 4-phase table and cycle duration guidance
- Validated Learning Log with structured entry format

**Gaps:**

The A/B test minimum sample size gap (noted in iter2 — "sufficient traffic for statistical power" without specific threshold) remains unaddressed. This is a minor scoping gap in the experiment selection guide. At 0.96, the score already reflects one minor unaddressed item from iter2.

**Improvement Path:**

- Add a minimum sample size reference or link to an external sample size calculator for A/B tests in the experiment selection guide quick decision path (e.g., "use a power analysis calculator targeting 80% power and p < 0.05")

---

### Evidence Quality (0.92/1.00)

**Evidence:**

**PRIMARY FIX VERIFIED:** The ICE source attribution has been corrected. The previous false citation of "Gothelf, J. & Seiden, J. (2021). Chapter 3: 'Driving Vision with Outcomes'" has been replaced with:

> "ICE scoring (Impact, Confidence, Ease) is a product prioritization framework originating from the growth hacking community (Sean Ellis, GrowthHackers, circa 2015). It is widely adopted in Lean UX contexts for lightweight hypothesis prioritization."

This attribution is factually accurate. ICE scoring is genuinely attributed to Sean Ellis and the GrowthHackers community (circa 2015). The attribution does not falsely assign the ICE formula to Lean UX authors. The cross-reference to `synthesis-validation.md § External Methodology Citations` is verifiable — that file contains Lean UX methodology citations though ICE scoring is not in its external citations table, making this cross-reference slightly aspirational but not false.

**REMAINING GAPS:**

Two source footnote citations were not converted to section-anchor format despite iter2 committing to full conversion of line-number citations. Both remain as line-number supplements:

1. Line 159: `> **Source:** P-003 hierarchy from parent SKILL.md [P-003 Compliance] (lines 174-196).`
   - The section-level anchor `[P-003 Compliance]` is present, but the supplementary `(lines 174-196)` remains as a brittle line reference.

2. Line 236: `> **Source:** Invocation pattern from parent SKILL.md [Invoking an Agent] (lines 200-250).`
   - The section-level anchor `[Invoking an Agent]` is present, but the supplementary `(lines 200-250)` remains as a brittle line reference.

These are the only remaining line-number citation instances in the document. While the section-level anchors make the citations usable, the line-number supplements remain unconverted — a gap given iter2's stated goal of complete line-number-to-section-anchor conversion.

The ORCHESTRATION.yaml path claim (pipeline-wave2 phase-1 lists hypothesis-backlog-template.md and assumption-map-template.md as artifacts) remains unverified but is secondary and low materiality.

**Improvement Path:**

- Remove the `(lines 174-196)` supplement from the P-003 Compliance source footnote: replace with `> **Source:** P-003 hierarchy from parent SKILL.md [skills/user-experience/SKILL.md § P-003 Compliance].`
- Remove the `(lines 200-250)` supplement from the Invoking the Agent source footnote: replace with `> **Source:** Invocation pattern from parent SKILL.md [skills/user-experience/SKILL.md § Invoking an Agent].`

---

### Actionability (0.96/1.00)

**Evidence:**

**PRIMARY FIX VERIFIED:** The on_receive/on_send session context fields are now enumerated as structured inline tables with 5 fields each. The tables appear at lines 216-234 with the format `| Field | Type | Required | Description |`. Evidence:

**on_receive (5 fields):**
- `engagement_id` | string | Yes | UX engagement identifier (format: `UX-{NNNN}`)
- `product_context` | string | Yes | Product name, domain, and target user description
- `design_change` | string | Yes | Description of the design change or area under hypothesis testing
- `prior_experiment_results` | array | No | Results from prior Build-Measure-Learn cycles
- `upstream_artifacts` | array | No | File paths to upstream handoff artifacts

**on_send (5 fields):**
- `hypothesis_backlog` | array | Yes | Hypothesis entries with ID, Lean UX format statement, status, and ICE score
- `assumption_map` | object | Yes | 4-quadrant assumption map with quadrant assignments and movement tracking
- `experiment_designs` | array | Yes | Per-hypothesis experiment designs with type, success criteria, and duration
- `validated_learning_log` | array | Yes | Completed Build-Measure-Learn cycle entries with evidence and decisions
- `synthesis_judgments` | array | Yes | AI judgment calls with confidence classification (HIGH/MEDIUM/LOW) and rationale

The iter2 gap is closed: a user or implementer reading only the SKILL.md can now determine the session context contract without reading the governance YAML separately.

All other actionability elements from iter2 remain intact:
- 4 invocation pathways (natural language, explicit, Task tool, Quick Reference table)
- Experiment selection guide with 7-row decision matrix and 5-step quick decision path
- Validated learning log format
- Common Workflows table with 6 command examples

**Gaps:**

No remaining actionability gaps. The 0.96 score (up from 0.95 in iter2) reflects the meaningful addition of inline session context tables.

**Improvement Path:**

The A/B test sample size gap noted in Methodological Rigor also has minor actionability implications (implementer does not know what "sufficient traffic" means). Adding a sample size reference would marginally improve actionability as well.

---

### Traceability (0.95/1.00)

**Evidence:**

**H-26 REFERENCE FIX VERIFIED:** The Registration section now reads: "This is an explicit exception to the H-26 registration requirement (parent-routed model)". The previous iter2 text was "This is an explicit H-26(c) exception for sub-skills." The new phrasing traces to the actual documented rule (H-26 in `skill-standards.md`) without requiring a non-existent sub-item label "(c)". The rationale note also reads "H-26 parent-routed model rationale" consistently.

The nav table Document Sections entry at line 58 correctly reads: `| [Registration](#registration) | H-26 parent-routed registration model and AGENTS.md confirmation |` — consistent with the body text.

Section-anchor citations are used throughout the majority of the document. All citations that were converted in iter2 remain in section-anchor format. The Requirements Traceability table links to verified entities (PROJ-022 PLAN.md, EPIC-003, FEAT-009, ORCHESTRATION.yaml path).

**REMAINING GAPS:**

The same two source footnote citations identified under Evidence Quality also affect traceability: `(lines 174-196)` and `(lines 200-250)`. These are supplementary line-number references appended to valid section anchors, creating minor brittleness. However, since the section-level anchors are present, traceability chains are not broken — the references are supplemented, not replaced. This is a lower-severity gap for traceability than for evidence quality.

**Improvement Path:**

- Remove the two supplementary line-number ranges from source footnotes (same fix as Evidence Quality)

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.92 | 0.94 | Remove two remaining line-number citation supplements: (a) replace `[P-003 Compliance] (lines 174-196)` with `[skills/user-experience/SKILL.md § P-003 Compliance]`; (b) replace `[Invoking an Agent] (lines 200-250)` with `[skills/user-experience/SKILL.md § Invoking an Agent]` — these are the only remaining unconverted line citations |
| 2 | Traceability | 0.95 | 0.97 | Same fix as Priority 1 — removing line-number supplements from the two source footnotes closes the traceability brittleness as well |
| 3 | Methodological Rigor | 0.96 | 0.97 | Add a minimum sample size reference for A/B tests in the experiment selection guide: "sufficient traffic for statistical power (use a power analysis calculator targeting 80% power, p < 0.05)" with a reference to a sample size calculator |
| 4 | Completeness | 0.95 | 0.96 | Cross-reference between `synthesis-validation.md § External Methodology Citations` and the ICE source: the citation note says "Referenced in [synthesis-validation.md § External Methodology Citations]" but the synthesis-validation.md file does not currently list Sean Ellis/ICE in its external citations table — add ICE to that table for completeness |

---

## Score Delta Analysis (Iter2 vs Iter3)

| Dimension | Iter2 Score | Iter3 Score | Delta | Fix Applied |
|-----------|-------------|-------------|-------|-------------|
| Completeness | 0.95 | 0.95 | 0.00 | No new completeness changes; existing fixes intact |
| Internal Consistency | 0.93 | 0.95 | +0.02 | Stub marker `**` moved outside agent table cell — clean agent name in table |
| Methodological Rigor | 0.96 | 0.96 | 0.00 | No regressions; ICE source correction does not affect methodology quality |
| Evidence Quality | 0.90 | 0.92 | +0.02 | ICE attribution corrected to Sean Ellis/GrowthHackers (accurate); 2 residual line citations remain |
| Actionability | 0.95 | 0.96 | +0.01 | on_receive/on_send fields enumerated as inline tables with 5 fields each |
| Traceability | 0.94 | 0.95 | +0.01 | H-26(c) reference normalized to "H-26 registration requirement (parent-routed model)" |
| **Composite** | **0.940** | **0.949** | **+0.009** | Net improvement across 4 of 6 dimensions |

**Gap analysis:** The composite is 0.949, missing the 0.950 threshold by 0.001. The single highest-priority fix (removing 2 line-number citation supplements) would raise Evidence Quality from 0.92 to approximately 0.93-0.94, adding 0.0015-0.003 to the composite, reaching 0.950-0.952. This is a one-line fix in two source footnotes.

**Observation:** The score trajectory (0.908 → 0.940 → 0.949) shows consistent improvement with diminishing returns as the deliverable approaches the threshold. The iter3 gap is the smallest of any iteration (0.001), confined to two specific unconverted citation instances.

---

## Iter3 Fix Verification Summary

| Fix | Description | Verified | Evidence |
|-----|-------------|----------|---------|
| Fix 1 (ICE attribution) | ICE source changed from Gothelf & Seiden Ch.3 to Sean Ellis/GrowthHackers 2015 | YES | Line 274: "originating from the growth hacking community (Sean Ellis, GrowthHackers, circa 2015)" |
| Fix 2 (H-26 reference) | H-26(c) → H-26 parent-routed model | YES | Line 590, 599: "explicit exception to the H-26 registration requirement (parent-routed model)" |
| Fix 3 (on_receive/on_send) | Fields enumerated as structured tables with 5 fields each | YES | Lines 218-234: two 5-row tables with field/type/required/description columns |
| Fix 4 (agent table stub marker) | `ux-lean-ux-facilitator**` → `ux-lean-ux-facilitator` (clean) | YES | Line 125: clean agent name in table; `**STUB:**` as separate paragraph line 127 |

All four stated iter3 fixes are verified as applied. The remaining gap is a scope omission: 2 line-number supplements were not removed as part of the full section-anchor conversion.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific line numbers and section references
- [x] Uncertain scores resolved downward: Evidence Quality scored at 0.92 (not 0.93) due to 2 residual line citations being a verifiable gap; Internal Consistency raised to 0.95 only with direct evidence of the `**` fix
- [x] Score trajectory considered: iter3 is a refined specification with all major gaps addressed; 0.949 composite reflects genuinely strong work with one narrow remaining gap
- [x] No dimension scored above 0.96 without evidence: Methodological Rigor at 0.96 reflects complete iter2 additions still intact; Actionability at 0.96 reflects the verified on_receive/on_send inline tables addition
- [x] Gap between threshold (0.95) and composite (0.949) is 0.001 — attributable to exactly two specific citation instances with specific fix path identified
- [x] Anti-leniency applied: Evidence Quality could have been scored 0.93 (line citations are supplementary, not primary); resolved downward to 0.92 per anti-leniency rule given iter2 committed to full conversion and these 2 instances remain

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.949
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.92
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Remove (lines 174-196) supplement from P-003 Compliance source footnote: replace with section-anchor-only format [skills/user-experience/SKILL.md § P-003 Compliance]"
  - "Remove (lines 200-250) supplement from Invoking the Agent source footnote: replace with section-anchor-only format [skills/user-experience/SKILL.md § Invoking an Agent]"
  - "Add Sean Ellis/ICE to synthesis-validation.md external citations table to make the cross-reference claim verifiable"
  - "Add minimum sample size guidance for A/B test traffic requirement (power analysis reference)"
```

---

*Score Report Version: 3.0*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-lean-ux/SKILL.md`*
*Prior Score: 0.940 (iter2)*
*Iteration: 3 of N (revision cycle continuing)*
*Created: 2026-03-04*
