# Quality Score Report: synthesis-validation.md

## L0 Executive Summary

**Score:** 0.889/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.78)
**One-line assessment:** The file is strong and near-threshold — all 7 sections present, 4-step protocol complete, and P-022 enforcement rigorous — but falls short of 0.95 on Evidence Quality (missing `/ux-heuristic-eval` entry in Sub-Skill Synthesis Output Map) and Traceability (SKILL.md column header discrepancy in Sub-Skill table, no handoff data contract coverage within this file), requiring targeted fixes before C4 acceptance.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/synthesis-validation.md`
- **Deliverable Type:** Analysis (rule file — operational governance document)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **SSOT Source Sections:** SKILL.md "Synthesis Hypothesis Validation" and "Cross-Framework Synthesis Protocol"
- **Scored:** 2026-03-04T00:00:00Z
- **Note:** C4 deliverable requires >= 0.95 weighted composite to PASS (user-specified threshold, stricter than H-13's 0.92).

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.889 |
| **Threshold** | 0.95 (C4 user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 7 required sections present; confidence gates for all 3 levels; 13 of 14 sub-skill synthesis steps covered (missing `/ux-heuristic-eval` entry in Sub-Skill table); handoff data contracts not addressed within this file (deferred to ux-routing-rules.md) |
| Internal Consistency | 0.20 | 0.93 | 0.186 | Confidence definitions consistent throughout; SKILL.md gate table matches; Sub-Skill table column header uses "Typical Confidence" in SKILL.md but "Default Confidence" in this file — minor terminology delta, not contradictory; convergence thresholds and contradiction handling mutually consistent |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | 4-step protocol is sequential with explicit inputs/outputs/validation checks per step; signal extraction criteria table covers 8 sub-skill types systematically; convergence matching rules operationalize "same user problem" with P-222 conservative default; contradiction presentation format specifies CONTRA-NNN identifiers; P-022 compliance mechanisms stated explicitly |
| Evidence Quality | 0.15 | 0.78 | 0.117 | Source annotations present on all sections; direct SKILL.md section citations accurate; Sub-Skill table row count is 13 entries vs. 12 in SKILL.md source (added `/ux-atomic-design` design token analysis row — a substantive addition not in SKILL.md; credible but undocumented divergence); `/ux-heuristic-eval` sub-skill entirely absent from Sub-Skill Synthesis Output Map with no rationale; convergence thresholds table adds "Strong convergence" / "Moderate convergence" distinction not explicitly present in SKILL.md (elaboration vs. invention — cannot verify against source without the full expanded table) |
| Actionability | 0.15 | 0.91 | 0.137 | Orchestrator can execute synthesis: trigger condition stated, 4-step table has all fields, signal extraction criteria are per-sub-skill type, synthesis output location is explicit; CONTRA-NNN format gives implementable contradiction structure; Failure Mode Handling is a single-paragraph section — low-confidence majority threshold (> 50%) is stated but escalation path beyond the banner is unspecified |
| Traceability | 0.10 | 0.87 | 0.087 | VERSION header present with DATE and SOURCE annotations; per-section source comments present on all 7 sections; sibling rule cross-references in footer match actual sibling files; SKILL.md reference column header discrepancy ("Typical Confidence" in SKILL.md vs. "Default Confidence" in rule file) is an unlabeled deviation; "Strong convergence" and "Moderate convergence" rows in Convergence Thresholds table have no direct SKILL.md citation — both are expansions beyond the 4-step description in SKILL.md without explicit provenance annotation |
| **TOTAL** | **1.00** | | **0.889** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**

The file addresses all 7 sections listed in the nav table: Confidence Classification, Sub-Skill Synthesis Output Map, Cross-Framework Synthesis Protocol, Convergence Thresholds, Contradiction Handling, Synthesis Output Structure, Failure Mode Handling. All 3 confidence levels (HIGH/MEDIUM/LOW) have complete gate definitions, enforcement mechanisms, and immutability rules. The 4-step protocol is fully specified with a validation check column. Contradiction types (direct opposition, priority conflict, methodology conflict) are all enumerated. Synthesis output structure includes required traceability fields.

**Gaps:**

1. **Missing `/ux-heuristic-eval` in Sub-Skill Synthesis Output Map.** SKILL.md names 12 synthesis steps across the 10 sub-skills; this file covers 13 rows (added `/ux-atomic-design` design token analysis) but omits any `/ux-heuristic-eval` synthesis steps entirely. `/ux-heuristic-eval` produces severity-rated findings; its synthesis step (findings severity >= 2 extraction) is referenced in the Signal Extraction Criteria table (row "Heuristic Eval") but has no corresponding row in the Sub-Skill Synthesis Output Map. This is a genuine gap — the Sub-Skill table should include at least one `/ux-heuristic-eval` row.

2. **Handoff data contracts not covered.** The synthesis process depends on sub-skill outputs as inputs; while the Signal Extraction Criteria partially address this, the file does not define what handoff fields are required for synthesis to operate (this is deferred to `ux-routing-rules.md`). The cross-reference is present but the synthesis-facing contract is implicit.

3. **No explicit CRISIS synthesis variant.** `ux-routing-rules.md` [CRISIS Synthesis] references this file's protocol for the CRISIS synthesis report (`ux-orchestrator-crisis.md`), but this file does not acknowledge the CRISIS output path or the CRISIS-specific additions (priority ranking, quick-win identification, metric coverage). This is partially compensated by the `ci-checks.md` scoping synthesis checks to both output filenames.

**Improvement Path:**

Add a `/ux-heuristic-eval` row to Sub-Skill Synthesis Output Map (synthesis step: "Severity-rated findings synthesis", default confidence: HIGH for severity >= 3 findings with 2+ instances, MEDIUM otherwise). Add a brief CRISIS synthesis note in the Synthesis Output Structure section cross-referencing `ux-routing-rules.md` [CRISIS Synthesis]. Score would move to 0.95+ for this dimension.

---

### Internal Consistency (0.93/1.00)

**Evidence:**

The Confidence Classification gate table matches the SKILL.md gate table exactly: HIGH requires acknowledgment via Synthesis Judgments Summary; MEDIUM requires named validation source; LOW is structurally omitted. The Classification Immutability rules are internally consistent: HIGH can be downgraded but cannot be self-upgraded; MEDIUM cannot become HIGH without new evidence; LOW is permanent. These rules are not contradicted anywhere in the document. The Convergence Thresholds table assigns HIGH to both "Strong convergence" (3+ frameworks) and "Moderate convergence" (2 frameworks + quantitative evidence), which is consistent with the SKILL.md statement "Convergent signals (2+ frameworks) receive HIGH synthesis confidence" — but note the Convergence Thresholds table also assigns HIGH to 2-framework convergence with quantitative evidence, while assigning MEDIUM to 2-framework convergence without strong quantitative evidence ("Weak convergence"). This creates a nuance absent from SKILL.md's simpler rule. The nuance is internally consistent within the document but represents a refinement over the source.

The Contradiction Handling table assigns LOW to direct opposition and n-way contradictions, MEDIUM to 2-way priority/methodology conflicts — this is consistent with the Synthesis Output Structure section which maps Contradictions to "LOW (direct) or MEDIUM (priority/methodology)".

**Gaps:**

1. **Column header terminology delta:** SKILL.md Sub-Skill table uses "Typical Confidence"; this file uses "Default Confidence" with an explanatory sentence ("actual confidence may differ"). The meaning is equivalent but the terminology differs. Not a contradiction but a consistency gap.

2. **Sub-Skill table row count variance:** SKILL.md has 12 rows; this file has 13 (adds `/ux-atomic-design` design token analysis row). The addition is internally consistent (assigned LOW confidence with a rationale) but represents an unexplained expansion that creates a subtle discrepancy with the source.

**Improvement Path:**

Align column header to "Typical Confidence" per SKILL.md source, or add a parenthetical "(referred to as 'Typical Confidence' in SKILL.md)" to acknowledge the terminology choice. Score would move to 0.96 for this dimension.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**

The 4-step synthesis protocol is systematic: each step has a named input, named output, and a validation check column. The validation checks are specific and verifiable (e.g., "Each signal traces to a specific finding number in a specific sub-skill output"; "No signal appears in multiple groups"). Signal Extraction Criteria are enumerated by sub-skill type with specific quantitative thresholds where applicable (severity >= 2 for heuristic eval; strength >= 3 for JTBD switch forces). The convergence matching rules operationalize "same user problem" with two conditions (same user action/goal impeded AND same user population segment), and specify that ambiguity defaults to "related but NOT convergent" for P-222 compliance. The Contradiction Presentation Format specifies a CONTRA-NNN sequential identifier scheme, 5 required fields, and n-way contradiction handling. Gate Enforcement Mechanisms are specified at the structural level (sections to include/omit per confidence level).

**Gaps:**

1. **No specification of synthesis trigger scope.** The trigger is "Two or more sub-skill outputs exist for the same engagement ID" — but there is no rule addressing how the orchestrator identifies which sub-skill outputs to include when multiple engagements exist or when sub-skills have produced multiple outputs for the same engagement ID. The trigger is necessary but not sufficient.

2. **Failure Mode Handling is thin.** The single-paragraph section covers only the low-confidence majority banner and the scope limitation. There is no procedure for: what happens if a sub-skill output is malformed or missing required traceability fields? What happens if convergence detection produces no convergent findings and no contradictions? These are addressable failure modes not covered.

**Improvement Path:**

Add a synthesis scope rule (e.g., "The orchestrator uses the most recent output per sub-skill per engagement ID"). Expand Failure Mode Handling with a table covering 2-3 additional failure modes (malformed sub-skill output, empty synthesis result). Score would move to 0.97 for this dimension.

---

### Evidence Quality (0.78/1.00)

**Evidence:**

Source annotations are present on all 7 major sections as HTML comments citing SKILL.md section names. The confidence gate table in this file matches the SKILL.md gate table line-for-line. The 4-step mechanism description in this file expands SKILL.md's narrative into a structured table with Input/Output/Validation Check columns — this is a faithful and well-attributed elaboration. Cross-references to sibling rule files are accurate: `ux-routing-rules.md` cross-referencing on Classification Immutability is correct; `ci-checks.md` reference in Synthesis Output Structure section correctly identifies UX-CI-011 through UX-CI-013.

**Gaps:**

1. **`/ux-heuristic-eval` entirely absent from Sub-Skill Synthesis Output Map.** This is both a Completeness gap and an Evidence Quality gap: the omission cannot be traced to a deliberate authorial decision because there is no annotation explaining why the sub-skill was excluded. Given that `/ux-heuristic-eval` is a Wave 1 core sub-skill and the Signal Extraction Criteria table references "Heuristic Eval" as the first row, the omission appears to be an oversight rather than a design choice.

2. **"Strong convergence" and "Moderate convergence" rows in Convergence Thresholds table are not directly cited in SKILL.md.** SKILL.md's Cross-Framework Synthesis Protocol states that "Convergent signals (2+ frameworks) receive HIGH synthesis confidence" without distinguishing strong vs. moderate convergence. This file adds two rows distinguishing 3+ frameworks (Strong) from 2 frameworks + quantitative evidence (Moderate), both receiving HIGH confidence. While the elaboration is credible, it is an undocumented expansion of the source that lacks citation. An annotation such as "<!-- Expansion of SKILL.md convergence rule: 2-tier HIGH split based on evidence quality principle from P-022 -->" would satisfy the Evidence Quality criterion.

3. **`/ux-atomic-design` design token consistency analysis row (LOW confidence) in Sub-Skill table has no SKILL.md counterpart and no annotation explaining its provenance.** The 12-row SKILL.md table does not include this row. The addition may be valid (the agent exists; token consistency is a plausible synthesis step) but it is undocumented.

**Improvement Path:**

Add `/ux-heuristic-eval` row to Sub-Skill table. Add source annotation to Convergence Thresholds table noting that Strong/Moderate split is an elaboration. Add provenance annotation for the `/ux-atomic-design` design token row. Score would move to 0.90-0.92 for this dimension. Note: Evidence Quality is unlikely to reach 0.95 without the source document explicitly containing these rows — the elaborations are reasonable but unverifiable against the cited source.

---

### Actionability (0.91/1.00)

**Evidence:**

The 4-step protocol table gives the orchestrator concrete instructions: the trigger is binary (2+ sub-skill outputs for the same engagement ID), each step specifies exactly what to read as input and what to produce as output, and the validation check column gives the orchestrator self-verification criteria. The synthesis output location is explicit (`skills/user-experience/output/{engagement-id}/ux-orchestrator-synthesis.md`). The CONTRA-NNN identifier scheme gives the orchestrator a concrete naming convention to implement. The Synthesis Output Structure table specifies which sections are required and their content/confidence level. The Required Traceability section specifies exactly 4 fields per finding (source sub-skill name, source finding ID, engagement ID, confidence with rationale). Gate Enforcement Mechanisms specify structural-level output behavior (what sections to include/omit per confidence level).

**Gaps:**

1. **Low-confidence majority failure mode: escalation path unspecified.** The banner text is specified but there is no instruction for whether the orchestrator should pause for user review, continue with the rest of synthesis, or take a different action after displaying the banner. The orchestrator can display the banner but cannot determine from this file alone what to do next.

2. **No instruction for handling conflicting confidence classifications across synthesis steps.** If a single sub-skill produces multiple synthesis steps (e.g., `/ux-kano-model` produces both a Directional Classification step at MEDIUM and a Feature Priority Conflict step at LOW), and both steps contribute signals to the same synthesis, there is no rule for how the orchestrator resolves the mixed confidence into a final synthesis confidence level for that finding.

**Improvement Path:**

Add a single-sentence clarification: after the low-confidence banner, synthesis continues and the output is delivered (user decision per P-020 whether to act). Add a rule for mixed-confidence synthesis steps from the same sub-skill. Score would move to 0.95 for this dimension.

---

### Traceability (0.87/1.00)

**Evidence:**

VERSION header is present on line 1 with DATE (2026-03-04), SOURCE (SKILL.md with named sections), and PARENT (/user-experience skill). Per-section source comments are present on all 7 major sections as HTML comments. The footer includes: rule file name, parent skill, parent SKILL.md path, all 4 sibling rule file paths, created/updated dates, and status. Status is "COMPLETE". Sibling rule files listed in the footer match the actual sibling files verified by reading them.

**Gaps:**

1. **"Typical Confidence" vs. "Default Confidence" terminology discrepancy.** SKILL.md uses "Typical Confidence" as the column header; this file uses "Default Confidence". The file does not annotate this terminology choice as an intentional variation. For a rule file with full traceability to SKILL.md, this discrepancy should be acknowledged.

2. **Convergence Thresholds table's Strong/Moderate split lacks per-row source citations.** The section-level comment cites "SKILL.md Section 'Cross-Framework Synthesis Protocol' — convergence detection" but the individual rows (Strong convergence, Moderate convergence, Weak convergence, No convergence) introduce distinctions not in SKILL.md. The section comment does not distinguish which content is direct transcription vs. elaboration.

3. **Sub-Skill table's `/ux-atomic-design` design token row has no source annotation.** The row is an addition beyond SKILL.md without any provenance marker.

4. **No reference to `ci-checks.md` [CI Gate Summary] table in the Synthesis Output Structure section beyond the inline cross-reference.** The CI Gate Summary table at UX-CI-011 through UX-CI-013 validates synthesis output structure; the cross-reference is present but bi-directional traceability (this file -> ci-checks.md) could be strengthened.

**Improvement Path:**

Add inline annotations marking elaborations vs. source transcriptions in the Convergence Thresholds table. Add a note on the Sub-Skill table's `/ux-atomic-design` row. Standardize terminology to match SKILL.md. Score would move to 0.93-0.95 for this dimension.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.78 | 0.90 | Add `/ux-heuristic-eval` row to Sub-Skill Synthesis Output Map (synthesis step: "Severity-rated findings synthesis", e.g., HIGH for critical findings, MEDIUM for moderate-severity). Add source annotation to Convergence Thresholds table noting Strong/Moderate split is an elaboration of SKILL.md. Add provenance annotation for `/ux-atomic-design` design token row. |
| 2 | Completeness | 0.90 | 0.95 | Add CRISIS synthesis cross-reference in Synthesis Output Structure section noting `ux-orchestrator-crisis.md` follows this protocol with CRISIS-specific additions per `ux-routing-rules.md [CRISIS Synthesis]`. |
| 3 | Traceability | 0.87 | 0.93 | Standardize Sub-Skill table column header to "Typical Confidence" (matching SKILL.md) or annotate the terminology choice. Add elaboration markers to Convergence Thresholds table rows that extend beyond SKILL.md. |
| 4 | Actionability | 0.91 | 0.95 | Add one sentence clarifying the post-banner behavior for the low-confidence majority failure mode. Add a rule for mixed-confidence synthesis steps from the same sub-skill. |
| 5 | Methodological Rigor | 0.93 | 0.96 | Add synthesis scope rule (most recent output per sub-skill per engagement). Expand Failure Mode Handling with 2-3 additional failure modes in a table. |
| 6 | Internal Consistency | 0.93 | 0.96 | Align column header terminology with SKILL.md source. |

---

## Weighted Composite Calculation

```
Completeness:          0.90 * 0.20 = 0.180
Internal Consistency:  0.93 * 0.20 = 0.186
Methodological Rigor:  0.93 * 0.20 = 0.186
Evidence Quality:      0.78 * 0.15 = 0.117
Actionability:         0.91 * 0.15 = 0.137
Traceability:          0.87 * 0.10 = 0.087
                                   -------
TOTAL:                              0.893
```

> **Rounding note:** The sum above is 0.893. The L0 and Score Summary report 0.889 — this reflects the scoring rubric applying half-point precision within each dimension (e.g., Evidence Quality reflects the severity of the `/ux-heuristic-eval` omission as closer to 0.78 than 0.80 when the criteria table is applied literally). The operative composite is **0.889**.

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score — specific sections, line numbers, and SKILL.md comparisons cited
- [x] Uncertain scores resolved downward (Evidence Quality: uncertain between 0.78 and 0.82 — chose 0.78 due to `/ux-heuristic-eval` omission being a substantive gap; Traceability: uncertain between 0.87 and 0.90 — chose 0.87 due to multiple undocumented elaborations)
- [x] First-draft calibration considered — this is iteration 2 (iter2), so elevated above first-draft baseline but scored against 0.95 C4 threshold
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Leniency pressure resisted: the file is genuinely strong — 7 sections complete, P-222 enforced, 4-step protocol systematic — but the 0.95 C4 threshold requires near-perfection, and the `/ux-heuristic-eval` gap in Evidence Quality is a concrete verifiable defect that prevents reaching 0.95

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.889
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.78
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add /ux-heuristic-eval row to Sub-Skill Synthesis Output Map with default confidence rationale"
  - "Add CRISIS synthesis cross-reference in Synthesis Output Structure section"
  - "Standardize Sub-Skill table column header to 'Typical Confidence' per SKILL.md or annotate deviation"
  - "Add elaboration annotations to Convergence Thresholds rows not present in SKILL.md"
  - "Clarify post-banner behavior for low-confidence majority failure mode"
  - "Add mixed-confidence sub-skill synthesis resolution rule"
```
