# Quality Score Report: JTBD Sub-Skill SKILL.md (Iteration 5)

## L0 Executive Summary

**Score:** 0.941/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.92)
**One-line assessment:** Both iter5 fixes are present and verified, but the worked example introduces two new internal consistency defects — an opportunity score formula error (example computes delta-only, contradicting the documented Ulwick ODI formula) and a column structure mismatch between the template and the worked example — that drop Internal Consistency from 0.95 to 0.92 and net the composite below the iter4 score; fix the worked example formula and align column headers to reach 0.95.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/SKILL.md`
- **Deliverable Type:** Sub-skill SKILL.md definition file for `/ux-jtbd` (Jobs-to-Be-Done)
- **Criticality Level:** C4
- **Quality Gate Threshold:** 0.95 (C4 requirement per scoring brief; standard H-13 threshold is 0.92)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Skill Standards Reference:** `.context/rules/skill-standards.md`
- **Prior Score (iter4):** 0.946 (REVISE)
- **Prior Score (iter3):** 0.924 (REVISE)
- **Prior Score (iter2):** 0.897 (REVISE)
- **Prior Score (iter1):** 0.851 (REVISE)
- **Iteration:** 5
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.941 |
| **Threshold** | 0.95 (C4, per scoring brief) |
| **Verdict** | REVISE |
| **Gap to Threshold** | 0.009 |
| **Delta vs. Iter4** | -0.005 (regression due to new defects in worked example) |
| **Strategy Findings Incorporated** | Yes — iter4 score report (`skills/ux-jtbd/output/quality-scores/skill-md-iter4-score.md`) |

---

## Iter5 Fix Verification

The following table documents each claimed iter5 fix with verification status against the actual document:

| Claimed Fix | Location | Actually Applied? | Evidence |
|-------------|----------|-------------------|---------|
| Worked Example (Onboarding Flow) added after output template | Lines 530-549 | YES — with defects | Header "**Worked Example (Onboarding Flow)**" at line 530; description at line 532; Functional Job table (lines 534-537): 1 row with job statement, outcome expectation ("Minimize the time it takes to identify the tool's primary use case"), priority=8.2, source="User interviews (3 participants)"; Switch Force table (lines 539-542): 1 Push force row with finding and evidence; Job Map table (lines 544-549): 2 rows (Define + Locate) with Importance/Satisfaction/Opportunity Score/Priority columns. Present and substantive, but contains a formula error and column structure mismatch. See Defects section below. |
| VERSION SOURCE field updated in both occurrences | Lines 25 and 712 | YES — clean | Line 25: `<!-- VERSION: 1.0.0 \| DATE: 2026-03-04 \| SOURCE: PROJ-022-user-experience-skill/PLAN.md \| PARENT: /user-experience skill -->`. Line 712: identical. Both occurrences updated from `SOURCE: skills/user-experience/SKILL.md` to `SOURCE: PROJ-022-user-experience-skill/PLAN.md` as specified. |

### Worked Example Defects (New Issues Introduced by Iter5)

| Defect | Location | Evidence |
|--------|----------|----------|
| **Opportunity Score formula mismatch** | Line 547-548 (Job Map worked example) | The methodology at line 364 states the formula as: "Importance + max(Importance - Satisfaction, 0)." For Step 1 (Importance=9.1, Satisfaction=4.2): formula yields 9.1 + 4.9 = **14.0**, but the worked example shows **4.9**. For Step 2 (Importance=7.8, Satisfaction=6.1): formula yields 7.8 + 1.7 = **9.5**, but the worked example shows **1.7**. The worked example consistently computes only the delta (Importance - Satisfaction) without adding Importance. This contradicts the documented formula. |
| **Column structure mismatch between template and worked example** | Lines 497-506 (template) vs. lines 544-549 (worked example) | The output template Job Map table has columns: Step \| Universal Process \| Domain-Specific Action \| Outcome Expectations \| Opportunity Score (5 columns). The worked example Job Map table has columns: Step \| Universal Process \| Domain-Specific Action \| Importance \| Satisfaction \| Opportunity Score \| Priority (7 columns, with Importance and Satisfaction disaggregated, Outcome Expectations removed, Priority added). A practitioner copying the template will produce a different structure from the worked example, creating confusion about which format to use. |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.95 | 0.190 | No change from iter4; all requirements addressed with depth; worked example addition is a positive addition that does not open any completeness gap |
| Internal Consistency | 0.20 | 0.92 | 0.184 | Worked example introduces opportunity score formula mismatch (delta-only vs. Importance+max(delta,0)) and column structure mismatch (5-column template vs. 7-column worked example) — two new concrete inconsistencies |
| Methodological Rigor | 0.20 | 0.94 | 0.188 | Methodology text itself remains correct and complete (unchanged); worked example teaches an incorrect formula, creating a methodological regression limited to the example rows |
| Evidence Quality | 0.15 | 0.95 | 0.1425 | No change from iter4; all citations remain at Author/Year/Title/Publisher format; worked example cites "User interviews (3 participants)" and "3 interview transcripts" — appropriate for illustrative example |
| Actionability | 0.15 | 0.94 | 0.141 | Worked example substantially closes the imagination gap from iter4; job statement row is correct, switch force row is specific; formula error in job map rows limits full credit for practitioners who use the example as a calculation guide |
| Traceability | 0.10 | 0.95 | 0.095 | VERSION SOURCE field updated in both occurrences (lines 25 and 712) from `skills/user-experience/SKILL.md` to `PROJ-022-user-experience-skill/PLAN.md` — the iter4 imprecision is resolved; full traceability chain now present |
| **TOTAL** | **1.00** | | **0.941** | |

**Composite (rounded):** 0.941

**Arithmetic verification:**
(0.95 × 0.20) + (0.92 × 0.20) + (0.94 × 0.20) + (0.95 × 0.15) + (0.94 × 0.15) + (0.95 × 0.10)
= 0.190 + 0.184 + 0.188 + 0.1425 + 0.141 + 0.095
= **0.9405 → rounded to 0.941**

---

## Detailed Dimension Analysis

### Completeness (0.95/1.00)

**Evidence:**

No change from iter4. All requirements are addressed with depth. The worked example is additive and positive for completeness — it adds practical illustration without removing or creating gaps elsewhere. The template (lines 448-528) remains complete. The invocation guidance (lines 153-157) remains present. The AGENTS.md verification (line 212) remains accurate.

**Gaps:**

None substantive. No new completeness gaps introduced by iter5 changes.

**Score rationale:** 0.95 — carried forward from iter4. No regression, no improvement that would justify raising to 0.96. Anti-leniency check: 0.95 is appropriate; the document addresses all requirements with depth, consistent with the rubric's 0.9+ criterion.

**Improvement Path:**

None required for completeness.

---

### Internal Consistency (0.92/1.00)

**Evidence:**

Iter4 was 0.95. The iter5 worked example introduces two concrete, verifiable inconsistencies:

**Defect 1 — Opportunity Score Formula Mismatch (Significant):**

The methodology Phase 4 (line 364) states the Ulwick ODI formula explicitly:
> "Calculate opportunity score: Importance + max(Importance - Satisfaction, 0)"

The worked example Job Map table (lines 547-548) shows:
- Step 1: Importance=9.1, Satisfaction=4.2, Opportunity Score=**4.9**
- Step 2: Importance=7.8, Satisfaction=6.1, Opportunity Score=**1.7**

Applying the documented formula:
- Step 1: 9.1 + max(9.1 - 4.2, 0) = 9.1 + 4.9 = **14.0** (not 4.9)
- Step 2: 7.8 + max(7.8 - 6.1, 0) = 7.8 + 1.7 = **9.5** (not 1.7)

The worked example has computed Opportunity Score = Importance - Satisfaction (the delta only). This is a different formula — it happens to be a commonly seen simplified heuristic, but it directly contradicts the formula documented one page earlier in the same document. A practitioner reading the methodology then the worked example encounters a contradiction. A practitioner using the worked example as a calculation guide will produce systematically incorrect opportunity scores.

**Defect 2 — Job Map Column Structure Mismatch (Minor but Concrete):**

The output template Job Map table (lines 497-506) has 5 columns:
```
Step | Universal Process | Domain-Specific Action | Outcome Expectations | Opportunity Score
```

The worked example Job Map table (lines 544-549) has 7 columns:
```
Step | Universal Process | Domain-Specific Action | Importance | Satisfaction | Opportunity Score | Priority
```

The worked example disaggregates Importance and Satisfaction (which the template's "Opportunity Score" column implicitly rolls up) and adds a Priority column. Practitioners copying the template will produce a 5-column job map; practitioners copying the worked example will produce a 7-column job map. The document does not explain or justify the column difference.

**Score rationale:** 0.92 — drop from iter4's 0.95. The two defects are genuine inconsistencies introduced by iter5, not pre-existing. The formula error is the more serious: it directly contradicts an explicitly stated formula in the same document. The column mismatch is a structural inconsistency. Together they warrant a 0.03 point drop. Anti-leniency check: uncertain between 0.91 and 0.93; resolved downward to 0.92.

**Improvement Path:**

1. (Critical) Fix the opportunity score formula in the worked example. Step 1: 9.1 + 4.9 = **14.0**. Step 2: 7.8 + 1.7 = **9.5**. Update both rows in lines 547-548.
2. (Minor) Align the Job Map column structure between the template and the worked example. Either: (a) update the template to show Importance and Satisfaction as separate columns (7-column format) and add Priority, to match the worked example's more granular format; OR (b) simplify the worked example to match the 5-column template format. Option (a) is preferred — the 7-column format provides richer pedagogical value because it shows the calculation inputs explicitly.

---

### Methodological Rigor (0.94/1.00)

**Evidence:**

Iter4 was 0.95. The methodology text itself is unchanged and remains correct. All five phases are well-structured with inputs, activities, and outputs. The three theoretical foundations (Christensen ODI, Ulwick ODI, Moesta switch interview) are correctly attributed and complete.

The regression from 0.95 to 0.94 is driven by the worked example: it teaches practitioners an incorrect opportunity score computation. The methodology specification is correct; the example contradicts it. A reader who absorbs both will be confused about which to follow. This is a methodological rigor issue because the document's practical guidance (the worked example) diverges from its stated methodology. However, the regression is modest because the error is confined to the worked example, not the methodology specification itself.

**Score rationale:** 0.94 — minor regression from 0.95. The formula error in the worked example is a methodological rigor concern, but the methodology text is correct. Anti-leniency check: uncertain between 0.93 and 0.95; resolved downward to 0.94 because the worked example's role is precisely to demonstrate the methodology, and it demonstrates it incorrectly.

**Improvement Path:**

Fix the opportunity score formula in the worked example (same fix as Internal Consistency — one change resolves both dimension gaps).

---

### Evidence Quality (0.95/1.00)

**Evidence:**

No change from iter4. All six JTBD Framework References retain Author/Year/Title/Publisher format. The worked example cites "User interviews (3 participants)" for the Functional Job source and "3 interview transcripts" for the Push force evidence — both are appropriate citation styles for an illustrative example (not primary research claims). No new citation issues are introduced.

**Score rationale:** 0.95 — no change from iter4. Anti-leniency check: the worked example uses generic-but-plausible citations; this is appropriate for an example artifact. No regression.

**Improvement Path:**

None required.

---

### Actionability (0.94/1.00)

**Evidence:**

Iter4 was 0.93, penalized for absence of worked example. The iter5 worked example closes most of the remaining gap:

**What works:**
- The functional job statement row shows a concrete, plausible example: "When I am onboarding to a new tool, I want to understand its core value quickly so I can decide whether to invest time learning" — this is a well-formed JTBD job statement in the canonical format.
- The outcome expectation is correctly phrased in the Ulwick minimize-form: "Minimize the time it takes to identify the tool's primary use case."
- The switch force Push row ("Current onboarding takes 15+ minutes before first value") is specific and illustrative.
- The overall structure demonstrates the expected output quality.

**What limits full credit:**
- The opportunity score formula in the job map rows is incorrect, as documented under Internal Consistency. A practitioner using the worked example to guide their opportunity score calculations will apply the wrong formula. This limits actionability for the most analytically demanding output section.
- The column structure mismatch between template and worked example leaves practitioners uncertain which Job Map format to use.

**Score rationale:** 0.94 — raise from iter4's 0.93. The worked example substantially addresses the iter4 gap and provides genuine practical illustration. The formula error prevents raising to 0.95 because the job map section — the most technically demanding part of the analysis — teaches an incorrect calculation method. Anti-leniency check: uncertain between 0.93 and 0.95; resolving to 0.94. The example is meaningfully better than iter4's template-only approach, but the formula error is a practitioner-facing defect.

**Improvement Path:**

Fix opportunity score formula in worked example (same fix as Internal Consistency). Once corrected, Actionability should reach 0.95.

---

### Traceability (0.95/1.00)

**Evidence:**

Iter4 was 0.94, penalized for VERSION SOURCE field imprecision (`SOURCE: skills/user-experience/SKILL.md` vs. the correct work item origin).

Both VERSION comment occurrences are now updated:
- Line 25: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: PROJ-022-user-experience-skill/PLAN.md | PARENT: /user-experience skill -->`
- Line 712: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: PROJ-022-user-experience-skill/PLAN.md | PARENT: /user-experience skill -->`

The SOURCE field now correctly identifies the project work item (`PROJ-022-user-experience-skill/PLAN.md`) rather than the design template source. The footer also retains "Agent: ux-jtbd-analyst" and "SSOT: `.context/rules/quality-enforcement.md`", maintaining the full provenance record.

All other traceability claims carried forward from iter4 remain valid:
- AGENTS.md registration claim verified at line 307 with "Verified 2026-03-04" timestamp
- Cross-references to `ux-routing-rules.md`, `synthesis-validation.md`, `mcp-coordination.md` remain consistent with routing architecture
- P-003 enforcement claims remain consistent with agent definition structure

**Score rationale:** 0.95 — the VERSION SOURCE imprecision from iter4 is resolved. The traceability chain is now complete. Anti-leniency check: 0.95 is justified; the rubric criterion "Most items traceable" is met at the 0.9+ level. The raise from 0.94 to 0.95 is warranted by the direct resolution of the single documented gap.

**Improvement Path:**

None required.

---

## Score Delta Analysis (All Iterations)

| Dimension | Iter1 | Iter2 | Iter3 | Iter4 | Iter5 | Delta (iter4→5) | Change Explanation |
|-----------|-------|-------|-------|-------|-------|-----------------|---------------------|
| Completeness | 0.75 | 0.92 | 0.93 | 0.95 | 0.95 | 0.00 | No change; worked example does not affect completeness |
| Internal Consistency | 0.88 | 0.92 | 0.93 | 0.95 | 0.92 | **-0.03** | Worked example introduces formula error + column mismatch — two new inconsistencies |
| Methodological Rigor | 0.90 | 0.90 | 0.95 | 0.95 | 0.94 | **-0.01** | Worked example contradicts stated formula; methodology text itself unchanged |
| Evidence Quality | 0.87 | 0.88 | 0.93 | 0.95 | 0.95 | 0.00 | No change; citation quality unchanged |
| Actionability | 0.84 | 0.86 | 0.86 | 0.93 | 0.94 | +0.01 | Worked example closes imagination gap but formula error limits full raise |
| Traceability | 0.88 | 0.88 | 0.94 | 0.94 | 0.95 | +0.01 | VERSION SOURCE field updated in both occurrences — iter4 imprecision resolved |
| **Composite** | **0.851** | **0.897** | **0.924** | **0.946** | **0.941** | **-0.005** | Net regression: traceability gain (+0.001) and actionability gain (+0.0015) offset by internal consistency (-0.006) and methodological rigor (-0.002) losses |

**Composite arithmetic verification:**
(0.95 × 0.20) + (0.92 × 0.20) + (0.94 × 0.20) + (0.95 × 0.15) + (0.94 × 0.15) + (0.95 × 0.10)
= 0.190 + 0.184 + 0.188 + 0.1425 + 0.141 + 0.095
= **0.9405 → rounded to 0.941**

---

## Gap to C4 Threshold Analysis

**Current composite:** 0.941
**Required threshold:** 0.950
**Gap:** 0.009

The two worked-example defects reversed the iter4 progress. The gap has widened from 0.004 (iter4) to 0.009 (iter5). However, both defects are fixable with a single targeted edit to the worked example.

Sensitivity analysis for iter6:

| Scenario | Fix | New Composite |
|----------|-----|---------------|
| Fix opportunity score formula only | IC → 0.94, MR → 0.95, Actionability → 0.95 | (0.95×0.20)+(0.94×0.20)+(0.95×0.20)+(0.95×0.15)+(0.95×0.15)+(0.95×0.10) = 0.190+0.188+0.190+0.1425+0.1425+0.095 = **0.948** (still below) |
| Fix formula + align column structures | IC → 0.95, MR → 0.95, Actionability → 0.95 | (0.95×0.20)+(0.95×0.20)+(0.95×0.20)+(0.95×0.15)+(0.95×0.15)+(0.95×0.10) = 0.190+0.190+0.190+0.1425+0.1425+0.095 = **0.950** (PASS) |

**Conclusion:** Two targeted fixes close the gap: (1) correct the opportunity score formula in the worked example (both rows), AND (2) align the Job Map column structure between the template and the worked example. Both fixes are confined to lines 544-549 and lines 497-506. Together they restore all five dimensions to 0.95 and yield a composite of exactly 0.950.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.92 | 0.95 | Fix the opportunity score formula in the worked example Job Map rows (lines 547-548). Step 1: Importance=9.1, Satisfaction=4.2 → correct Opportunity Score = 9.1 + max(9.1-4.2, 0) = 9.1 + 4.9 = **14.0** (not 4.9). Step 2: Importance=7.8, Satisfaction=6.1 → correct Opportunity Score = 7.8 + max(7.8-6.1, 0) = 7.8 + 1.7 = **9.5** (not 1.7). Update the table values accordingly. |
| 2 | Internal Consistency / Actionability | 0.92 / 0.94 | 0.95 | Align the Job Map column structure between the output template (lines 497-506) and the worked example (lines 544-549). Preferred fix: update the template Job Map to use the 7-column format that matches the worked example (Step \| Universal Process \| Domain-Specific Action \| Importance \| Satisfaction \| Opportunity Score \| Priority) and remove the generic "Outcome Expectations" column. This makes the template match the richer worked example format, showing practitioners how to record the calculation inputs explicitly. |

**Note:** Both recommendations must be applied together. Fix 1 alone yields ~0.948 (still below threshold). Fix 1 + Fix 2 together yields ~0.950 (threshold met exactly). Both fixes are targeted changes to approximately 12 lines total.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Both iter5 fixes verified against actual document line numbers before scoring
- [x] Worked example verified section by section: Functional Job table (lines 534-537), Switch Force table (lines 539-542), Job Map table (lines 544-549)
- [x] Opportunity score formula verified arithmetically against the formula documented in Phase 4 (line 364): 9.1 + max(4.9, 0) = 14.0 (not 4.9); 7.8 + max(1.7, 0) = 9.5 (not 1.7)
- [x] Column structure mismatch verified by comparing template columns (lines 497-506) vs. worked example columns (lines 544-549)
- [x] Internal Consistency dropped from 0.95 to 0.92 — regression confirmed with two specific, independently verifiable defects
- [x] Methodological Rigor dropped from 0.95 to 0.94 — minor regression confirmed; magnitude is limited because the specification text is correct
- [x] Actionability raised from 0.93 to 0.94 — partial raise; example is substantively helpful but formula error limits full credit; uncertain between 0.93 and 0.95, resolved downward per anti-leniency rule
- [x] Traceability raised from 0.94 to 0.95 — raise confirmed by VERSION SOURCE update in both occurrences
- [x] Composite regression from 0.946 to 0.941 is mathematically correct; the net of all gains and losses is -0.005
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] First-draft calibration not applicable (iter5); calibration check: +0.001 net from traceability gain vs. -0.006 from IC drop is internally consistent with the two verified defects
- [x] Score of 0.941 confirms REVISE verdict — 0.009 below the C4 threshold of 0.95

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.941
threshold: 0.95
weakest_dimension: Internal Consistency
weakest_score: 0.92
critical_findings_count: 0
iteration: 5
improvement_recommendations:
  - "Fix opportunity score formula in worked example Job Map rows (lines 547-548): Step 1 should show 14.0 (9.1 + 4.9), not 4.9; Step 2 should show 9.5 (7.8 + 1.7), not 1.7 — corrects contradiction with Phase 4 formula at line 364"
  - "Align Job Map column structure between output template (lines 497-506) and worked example (lines 544-549): update template to 7-column format (Step | Universal Process | Domain-Specific Action | Importance | Satisfaction | Opportunity Score | Priority) to match worked example, removing the generic Outcome Expectations column"
  - "Both fixes required together: Fix 1 alone yields ~0.948, still below threshold; Fix 1 + Fix 2 together yields ~0.950 (PASS)"
  - "Regression note: iter5 worked example caused composite to drop from 0.946 to 0.941; both remaining defects are in lines 497-549 (worked example and template Job Map only)"
```

---

*Score Report Version: 1.0.0*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Skill Standards: `.context/rules/skill-standards.md`*
*Score History: iter1=0.851, iter2=0.897, iter3=0.924, iter4=0.946, iter5=0.941 | Deltas: +0.046, +0.027, +0.022, -0.005*
*Agent: adv-scorer*
*Created: 2026-03-04*
