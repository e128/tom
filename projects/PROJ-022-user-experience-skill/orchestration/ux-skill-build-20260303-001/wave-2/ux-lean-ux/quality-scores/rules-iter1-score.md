# Quality Score Report: Lean UX Methodology Rules

## L0 Executive Summary

**Score:** 0.862/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.82) / Traceability (0.82, tied)

**One-line assessment:** The rules file is methodologically sound with well-structured operational constraints across all 8 topic areas, but falls short of the 0.95 C4 threshold due to a weak ICE attribution chain, missing SKILL.md version pin, an unresolved "Handoff threshold rule" ID gap in the self-review checklist, and absence of a formal cross-dependency traceability section.

---

## Scoring Context

- **Deliverable:** `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md`
- **Deliverable Type:** Methodology Rules File (sub-skill operational constraints)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (C4, user-specified)
- **Cross-references verified:** `skills/ux-lean-ux/SKILL.md` (v1.2.0), `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` (v1.1.0), `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md` (v1.2.0), `skills/user-experience/rules/synthesis-validation.md` (v1.1.0)
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.862 |
| **Threshold** | 0.95 (C4, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (standalone scoring, no adv-executor reports provided) |
| **Delta to Threshold** | -0.088 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.88 | 0.176 | All 8 operational areas covered; self-review checklist item 14 lacks a formal rule ID reference |
| Internal Consistency | 0.20 | 0.86 | 0.172 | Rule IDs unique and well-structured; "Handoff threshold rule" in checklist item 14 has no formal rule ID in the rules file |
| Methodological Rigor | 0.20 | 0.87 | 0.174 | Canonical Lean UX format correctly applied; experiment selection path is sound; minor gap in terminal case coverage |
| Evidence Quality | 0.15 | 0.82 | 0.123 | ICE attribution lacks a formal published citation; scale anchors are author operationalizations not directly cited from primary sources |
| Actionability | 0.15 | 0.90 | 0.135 | HARD/MEDIUM tier classification complete; scale anchors include specific quantitative thresholds; self-review checklist is operationalizable |
| Traceability | 0.10 | 0.82 | 0.082 | No SKILL.md version pin; no formal cross-dependency section; checklist item 14 cites a non-existent rule ID |
| **TOTAL** | **1.00** | | **0.862** | |

---

## Detailed Dimension Analysis

### Completeness (0.88/1.00)

**Evidence:**

The rules file addresses all eight required operational areas for the Lean UX facilitation agent:

1. **Build-Measure-Learn Cycle Rules** (BML-001 through BML-006): 5-step sequence with mandatory rules, partial scope table, and cycle termination conditions. Complete.
2. **Hypothesis Format Validation Rules** (HYP-001 through HYP-006): 4-component format, ID format, lifecycle states, validation discipline. Complete.
3. **Assumption Mapping Rules** (ASM-001 through ASM-007): Quadrant definitions, boundary criteria, assumption category classification, mapping discipline. Complete.
4. **Experiment Type Selection Rules** (EXP-001 through EXP-007): 7-type matrix, decision path with priority ordering, selection discipline. Complete.
5. **ICE Scoring Rules** (ICE-001 through ICE-007): Three-dimension scale anchors, composite formula, tiebreaking, scoring discipline. Complete.
6. **Validated Learning Documentation Rules** (VLD-001 through VLD-007): Learning entry format, required fields, evidence quality standard, decision criteria. Complete.
7. **Confidence Classification Rules** (CLS-001 through CLS-005): Three-tier classification, judgment types requiring classification, Lean UX confidence dynamics. Complete.
8. **Quality Gate Integration** (QG-001 through QG-004): S-014 dimension mapping, scoring discipline. Complete.
9. **Self-Review Checklist**: 15-item checklist covering all rule areas.

The navigation table correctly lists all 9 sections with anchor links (H-23 compliant).

**Gaps:**

- Self-review checklist item 14 reads "Handoff Data includes only VALIDATED or INVALIDATED hypotheses | Handoff threshold rule" but "Handoff threshold rule" is not a defined rule ID in this file. The concept exists in the agent definition's output section but has no formal rule designation here. This is a coverage gap for a C4 rules file — every checklist item should cite a rule ID that exists within the file or an explicitly named external reference.
- The rules file has no explicit section documenting incoming dependencies (e.g., that Wave 1 completion is a prerequisite per SKILL.md) nor outgoing data dependencies (what downstream files consume this rules file's outputs). Compare with `synthesis-validation.md` which includes a sibling rules list and Constitutional References section.
- No rule governs what happens when `Cycle Scope` is provided with an invalid value (outside the 5 valid enum values). BML-003 says "only the specified phases execute" but does not define the error behavior for unknown scope values.

**Improvement Path:**

Add a formal rule ID `HYP-007` or `VLD-008` (or an `HDF-001` section) for the handoff threshold rule currently cited as "Handoff threshold rule" in checklist item 14. Add a brief Dependencies section listing upstream Wave 1 requirements and downstream synthesis consumers.

---

### Internal Consistency (0.86/1.00)

**Evidence:**

Rule IDs are unique across the document: BML (001-006), HYP (001-006), ASM (001-007), EXP (001-007), ICE (001-007), VLD (001-007), CLS (001-005), QG (001-004). No duplicate IDs found.

Cross-references are internally consistent:
- ICE-002 ("uncertain between adjacent scores, choose LOWER") is consistent with methodology Section ICE Scoring narrative: "When uncertain between two adjacent scores, choose the LOWER score."
- ASM-003 ("uncertain between adjacent quadrants, place in HIGHER-risk") is consistent with Step 2 methodology narrative: "When uncertain between adjacent quadrants, place the assumption in the HIGHER-risk quadrant."
- VLD-003 (PERSEVERE on INVALIDATED = FORBIDDEN) is correctly cited in QG-004 and self-review item 10.
- BML-005 (PIVOT hypotheses MUST be scored) is consistent with ICE-007 (PIVOT hypotheses MUST be scored before next cycle) — both rules address the same requirement and cross-cite each other in the checklist (item 15 cites both BML-005 and ICE-007).
- The Lean UX Confidence Dynamics section correctly states that pre-experiment outputs are inherently MEDIUM, which is consistent with CLS-002 (NEVER classify pre-experiment judgment as HIGH without multiple independent data sources).
- Decision criteria table (PERSEVERE/PIVOT/KILL) is consistent with the decision field requirements in the learning entry format and VLD-003 through VLD-005.

**Gaps:**

- Self-review checklist item 14 cites "Handoff threshold rule" which is not a rule ID in this file. This creates an internal traceability break where the checklist references a rule that does not exist in the document. The concept is defined in the agent definition's `<output>` section ("Handoff threshold: Only hypotheses with status VALIDATED or INVALIDATED...") but is not formalized in this rules file.
- The lifecycle state transitions table shows "Any → -- | No backward transitions (VALIDATED/INVALIDATED are terminal) | --" with an empty Required Evidence field. While the meaning is clear, the table row format is inconsistent with other rows that have non-empty Required Evidence fields. Minor.
- QG-001 states "quality gate threshold (>= 0.92 for C2+) applies to the overall facilitation report" — this is technically correct per quality-enforcement.md but the user-specified threshold for this deliverable is 0.95 (C4). The document does not acknowledge the C4 threshold override, potentially causing confusion for agents executing this rules file.

**Improvement Path:**

Formalize the handoff threshold as a rule (e.g., `HDF-001`) in a new "Handoff Rules" sub-section or append to the Validated Learning Documentation section. Update checklist item 14 to cite this rule ID. Update QG-001 to acknowledge the C4 threshold (>= 0.95) as an override of the base C2+ threshold.

---

### Methodological Rigor (0.87/1.00)

**Evidence:**

The methodology correctly implements the canonical Lean UX Build-Measure-Learn framework:

- **Hypothesis format**: "We believe [outcome] for [users] if [change] because [evidence]" matches Gothelf & Seiden (2021) canonical format.
- **4-quadrant assumption mapping**: Q1 (Unknown + High Risk), Q2 (Known + High Risk), Q3 (Known + Low Risk), Q4 (Unknown + Low Risk) correctly maps the risk/knowledge axes. Actions per quadrant (TEST FIRST / MONITOR / ACCEPT / DEFER) are correct per Gothelf & Seiden.
- **Experiment type selection decision path**: 6-priority ordered criteria with rationale for each. Priorities are defensible: A/B test (highest confidence) first, demand validation tests before building, complexity-matched tests (Concierge/Wizard) for complex workflows, early-stage tests last.
- **ICE formula**: (Impact + Confidence + Ease) / 3 is the standard calculation.
- **Decision framework**: PIVOT/PERSEVERE/KILL definitions are correct. PERSEVERE → validated hypothesis feeds to HEART Metrics is the correct downstream integration.
- **Lifecycle states**: DRAFT → ACTIVE → VALIDATED/INVALIDATED/DEFERRED are consistent with the Lean UX methodology. "No backward transitions (VALIDATED/INVALIDATED are terminal)" is methodologically accurate.
- **Confidence dynamics**: Correctly identifies that pre-experiment Lean UX outputs are inherently MEDIUM confidence (hypotheses are unvalidated propositions by design). HIGH requires convergence with a second framework.

**Gaps:**

- The experiment selection decision path (6 priorities) does not include an explicit "else: apply engineering judgment" clause for when no priority matches. The current text implies the list is exhaustive (priorities 1-6 cover all cases through specificity), but this is not stated. A conservative reader could be uncertain what to do if conditions for priorities 1-6 do not cleanly apply.
- EXP-003 states "Q1 assumptions SHOULD use experiment types with MEDIUM or HIGH confidence yield" — but this is classified as MEDIUM tier. Given that Q1 assumptions are the highest-risk unknowns that could invalidate the entire approach (per ASM-006 which is HARD), the guidance on experiment confidence for Q1 assumptions arguably merits HARD rather than MEDIUM classification. This is a rigor judgment call.
- The ICE Confidence scale (scores 6-7 = "Moderate evidence: heuristic evaluation severity >= 2 findings") cross-references heuristic evaluation findings. This is a reasonable upstream integration but is not stated as a dependency anywhere in the rules file (no mention of Wave 1 prerequisite in the rule body itself).

**Improvement Path:**

Add an explicit "residual case" to the experiment selection decision path indicating that when multiple criteria partially match, EXP-007 (highest confidence yield within resource constraints) governs selection. Consider escalating EXP-003 from MEDIUM to HARD given the criticality of Q1 assumption validation.

---

### Evidence Quality (0.82/1.00)

**Evidence:**

Cited sources are present and credible:

- Gothelf & Seiden (2021): cited for hypothesis format (Chapter 3), assumption mapping (Chapter 4), BML cycle foundation (Chapter 7). Chapter-level citations are specific.
- Ries (2011) "The Lean Startup": cited for BML cycle foundation and validated learning (Chapter 7: "Measure"). Chapter-level citation is specific.
- Croll & Yoskovitz (2013) "Lean Analytics": cited for experiment design patterns and measurement strategies. No chapter-level specificity.
- ICE scoring: attributed to "Sean Ellis, GrowthHackers, circa 2015" — this is an honest acknowledgment of the community origin but "circa 2015" is not a citable primary source. ICE scoring has no canonical paper; it emerged from blog posts and community usage. The attribution is the best available but weaker than a published citation.

Concrete evidence examples in the rules are high quality:
- "Checkout completion rate increased from 23% to 31% (n=450, p<0.05) over 2-week A/B test period" (acceptable evidence in VLD)
- "3 of 5 Wizard of Oz participants completed the workflow without assistance" (acceptable evidence in VLD)
- "Fake door click-through rate was 2.1% (below 5% threshold); 89 unique visitors during test period" (acceptable evidence in VLD)

Unacceptable evidence examples are equally concrete and appropriately illustrate the contrast.

**Gaps:**

- **ICE scale anchors are not cited to a primary source.** The specific percentage thresholds used for Impact (1% / 10% / 25% / 50% / 75% boundaries), the evidence tier descriptions for Confidence, and the effort-time thresholds for Ease appear to be the author's operationalization rather than directly cited from Ellis/GrowthHackers or Gothelf & Seiden. At C4 quality gate scrutiny, these operationalizations require either: (a) citation to a source that uses these thresholds, or (b) an explicit disclosure that they are framework adaptations ("operationalized for tiny-team Lean UX contexts").
- **Croll & Yoskovitz (2013) citation lacks chapter or page specificity.** The heuristic eval rules file (v1.2.0, by contrast) provides specific publication details. The Lean UX rules file's citation for Croll & Yoskovitz does not specify which chapter covers the experiment design patterns referenced.
- **No external validation of the 4-week cycle duration flag in BML-004.** The rule states cycles > 4 weeks "SHOULD be flagged as over-scoped" and "Lean UX targets 1-2 week cycles for tiny teams" — but no citation supports the 1-2 week cycle duration recommendation specifically for tiny teams. Gothelf & Seiden discuss cycle duration generally but without a specific tiny-team duration recommendation.

**Improvement Path:**

Add an explicit annotation to the ICE scale anchors: "Scale boundaries operationalized for tiny-team contexts; adapted from Sean Ellis ICE framework principles (GrowthHackers, 2015). Specific percentage thresholds are practitioner adaptations." Provide a Croll & Yoskovitz chapter reference. Add a citation to BML-004's 1-2 week cycle duration recommendation.

---

### Actionability (0.90/1.00)

**Evidence:**

The rules file provides genuinely actionable operational guidance:

- **Tier classification**: Every rule is classified as HARD or MEDIUM with explicit consequences ("Untested assumptions propagate", "Fabricated learning entries violate P-022", etc.). Agents executing this file can determine what to enforce strictly versus what to treat as guidance.
- **ICE scale anchors**: Specific quantitative thresholds are provided at each score level. Impact uses percentage user coverage; Confidence uses evidence type categories with concrete examples; Ease uses calendar-day ranges. An agent has enough specificity to make consistent 1-10 assignments.
- **Experiment success criteria requirement** (EXP-002): "specific metric + threshold (e.g., 'checkout completion rate increases by >= 10% over control')" — the example makes the requirement unambiguous.
- **Quadrant boundary criteria**: "assumption failure would require > 1 sprint of effort to recover" for HIGH risk is a measurable threshold. The LOW/HIGH Knowledge distinction uses observable evidence types (direct experiment data vs. team intuition).
- **Decision criteria table**: Specifies exact evidence requirements for PERSEVERE, PIVOT, and KILL, not just definitions.
- **Self-review checklist**: 15 items, each with a specific rule ID citation. All items are verifiable binary pass/fail checks.
- **Partial scope table**: Maps each Cycle Scope value to specific steps executed — no ambiguity about what a `hypothesis-generation` scope invocation should produce.

**Gaps:**

- ICE-005 states "The Ease dimension MUST account for actual team size and resources. A 1-person team SHOULD NOT score Ease identically to a 5-person team for the same experiment." This rule is classified MEDIUM and uses SHOULD NOT — but it does not provide a concrete adjustment factor or calibration method. An agent executing this rule has the principle but not the method.
- QG-002 states "Completeness scoring MUST account for partial scope: assess against the scoped steps only" — but does not specify HOW the scoring denominator changes (e.g., is a `hypothesis-generation` scope scored out of 5 steps or out of 1 step?). The principle is clear; the mechanics are not.
- No rule specifies what to do when upstream JTBD or heuristic data arrives in an unexpected format (e.g., no severity rating provided for heuristic findings). ASM-007 references "heuristic evaluation findings with severity >= 2" but does not specify the fallback if severity is absent.

**Improvement Path:**

Add a team-size calibration example to ICE-005 (e.g., "a 1-person team with a 5-person experiment design baseline should reduce Ease by 1-2 points"). Add a denominator clarification to QG-002. Add an ASM-008 fallback rule for upstream data without severity ratings.

---

### Traceability (0.82/1.00)

**Evidence:**

Strong traceability elements present:

- **Footer traceability block**: "PROJ-022 EPIC-002, FEAT-009. Standards: H-23 (navigation), H-34 (agent-dev), SR-002 (input validation), SR-003 (output filtering). Methodology: Gothelf & Seiden (2021), Ries (2011), Croll & Yoskovitz (2013), Sean Ellis / GrowthHackers (circa 2015). Synthesis validation: skills/user-experience/rules/synthesis-validation.md. Quality gate: .context/rules/quality-enforcement.md."
- **VERSION comment**: "SOURCE: skills/ux-lean-ux/SKILL.md, skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md" with date 2026-03-04.
- **Per-section source citations**: Each major section has `> **Source:**` annotation linking to the methodology origin.
- **Self-review checklist**: Items cite specific rule IDs (e.g., "HYP-001", "ASM-001, ASM-002") enabling post-review traceability from checklist to rule.
- **Quality gate dimension mapping**: The QG section maps S-014 dimensions to Lean UX evaluation criteria, enabling traceability from quality scoring to rule application.

**Gaps:**

- **No SKILL.md version pin.** The VERSION comment cites `SOURCE: skills/ux-lean-ux/SKILL.md` but does not pin the version (v1.2.0). If SKILL.md is updated to v1.3.0, there is no way to determine whether this rules file was written against v1.2.0 or an earlier version. Compare with synthesis-validation.md which records "Revision: iter3 — adversarial findings from iter1 (0.879) and iter2 (0.889)" in its footer.
- **No formal dependency matrix.** The heuristic-evaluation-rules.md comparison standard has a self-contained footer listing: "Sibling rules: ..., Parent SKILL.md: ..." — the Lean UX rules file has this in the SSOT field only. No section lists which files depend on this rules file (incoming) or which files this rules file depends on (outgoing) for operational execution. The synthesis-validation.md has a proper constitutional references section as a standalone traceability mechanism.
- **Checklist item 14 cites "Handoff threshold rule"** — a rule that does not exist with this designation in the rules file. This breaks the traceability chain from checklist item to rule.
- **No reference to wave-progression.md.** The rules file governs agent behavior in Wave 2 (Data-Ready) but does not reference `skills/user-experience/rules/wave-progression.md` for the wave entry conditions. An executor of this file cannot determine from the file itself that Wave 1 completion is required before these rules are operational.
- **The `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.governance.yaml` is not cited** as a related file. The governance YAML defines enforcement mechanisms (quality_threshold: 0.95, quality_gate: S-014) that this rules file should reference for traceability completeness.

**Improvement Path:**

Add a "Related Files" or "Dependencies" section (analogous to synthesis-validation.md's "Constitutional References") listing: parent SKILL.md (version-pinned), agent governance YAML, wave-progression.md, synthesis-validation.md. Pin the SKILL.md version in the VERSION comment. Formalize the handoff threshold as a named rule. Add wave-progression.md reference to establish the operational context boundary.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.82 | 0.90 | Add a "Related Files" / "Dependencies" section listing: SKILL.md v1.2.0 (version-pinned), ux-lean-ux-facilitator.governance.yaml, wave-progression.md, synthesis-validation.md. Add wave-progression.md reference for Wave 2 entry conditions. |
| 2 | Internal Consistency | 0.86 | 0.93 | Formalize the handoff threshold as a rule ID (e.g., `HDF-001` in a new Handoff Rules sub-section or as `VLD-008`). Update self-review checklist item 14 to cite this rule ID. Update QG-001 to acknowledge C4 threshold (>= 0.95) as override. |
| 3 | Evidence Quality | 0.82 | 0.88 | (a) Add annotation to ICE scale anchors: "Scale boundaries operationalized for tiny-team contexts; adapted from Sean Ellis ICE framework (GrowthHackers, 2015). Specific percentage thresholds are practitioner adaptations." (b) Add Croll & Yoskovitz chapter reference (Chapter 5 or 6 covers measurement design). (c) Cite BML-004's 1-2 week cycle recommendation to Gothelf & Seiden (2021) Chapter 7 or equivalent source. |
| 4 | Completeness | 0.88 | 0.93 | (a) Add explicit error behavior for invalid `Cycle Scope` values to BML-003. (b) Add a brief "Dependencies" note stating Wave 1 prerequisite. |
| 5 | Methodological Rigor | 0.87 | 0.92 | Add explicit "residual case" clause to experiment selection decision path (e.g., "When no single priority matches exclusively, apply EXP-007: select type with highest confidence yield within resource constraints"). Consider escalating EXP-003 from MEDIUM to HARD. |
| 6 | Actionability | 0.90 | 0.93 | (a) Add team-size calibration example to ICE-005. (b) Add denominator clarification to QG-002 for partial scope completeness scoring. (c) Add ASM-008 fallback for upstream data without severity ratings. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score with specific rule IDs, section citations, and cross-file comparisons
- [x] Uncertain scores resolved downward (e.g., Evidence Quality: uncertain between 0.82-0.85, chose 0.82 due to unresolved ICE anchor citation gap)
- [x] First-draft calibration not applicable (this is a first-scored version of a v1.0.0 rules file; calibration anchors applied: 0.85 = strong work with minor refinements needed)
- [x] No dimension scored above 0.95; highest is Actionability at 0.90, which has documented specific gaps
- [x] C4 threshold (0.95) applied; deliverable is 0.088 below threshold, which correctly maps to REVISE

**Calibration note:** The 0.862 composite sits in the REVISE band (0.85-0.91). The six identified gaps are real and fixable: four are precision/traceability issues (no new content required, just formalization of existing concepts), one is a citation annotation, and one is a methodology completeness item. Estimated revision effort: 1-2 hours to address all six recommendations, with a projected score increase to 0.93-0.95 after fixes.

---

## Session Context Schema

```yaml
verdict: REVISE
composite_score: 0.862
threshold: 0.95
weakest_dimension: Evidence Quality (tied with Traceability)
weakest_score: 0.82
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add Related Files / Dependencies section with version-pinned SKILL.md reference and wave-progression.md link"
  - "Formalize handoff threshold as rule ID (HDF-001 or VLD-008); update checklist item 14"
  - "Annotate ICE scale anchors as practitioner adaptations; add Croll & Yoskovitz chapter reference; cite BML-004 cycle duration"
  - "Add invalid Cycle Scope error behavior to BML-003; add Wave 1 prerequisite dependency note"
  - "Add residual case clause to experiment selection decision path"
  - "Add ICE-005 team-size calibration example; QG-002 partial scope denominator clarification; ASM-008 upstream data fallback"
```

---

*Score Report: rules-iter1-score.md*
*Deliverable: skills/ux-lean-ux/rules/lean-ux-methodology-rules.md*
*Scoring Agent: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*SSOT: .context/rules/quality-enforcement.md*
*Created: 2026-03-04*
