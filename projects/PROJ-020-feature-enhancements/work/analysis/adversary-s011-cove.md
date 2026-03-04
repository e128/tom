# Chain-of-Verification Report: UX Framework Selection Analysis

**Strategy:** S-011 Chain-of-Verification
**Deliverable:** projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md
**Criticality:** C4
**Date:** 2026-03-02
**Reviewer:** adv-executor (S-011)
**H-16 Compliance:** S-003 Steelman applied (confirmed -- prior output at adversary-iteration-2-steelman.md)
**Claims Extracted:** 28 | **Verified:** 15 | **Discrepancies:** 13

---

## Summary

Chain-of-Verification uncovered 13 discrepancies across 28 testable claims. The most significant findings are systematic arithmetic errors in the weighted-score totals for 7 of the 30 non-top-10 frameworks in the Full Scoring Matrix (Section 2), and systematic errors in the sensitivity analysis score recalculations at the alternate 20% weight. These are not rounding errors -- the errors range from 0.05 to 0.50 points and indicate that independent arithmetic was not applied to the non-selected frameworks and sensitivity values were not recalculated from the raw scores. The top-10 arithmetic is fully correct. The rank numbering for AI-First Design and Microsoft Inclusive Design is internally inconsistent across sections (each is referenced as both #7 and #8). The fundamental selection conclusions are not threatened by any finding because the selection is determined by the top-10 scores (all verified correct), but the non-selected framework scores undermine the evidential credibility of the full scoring matrix. Recommendation: **REVISE** -- correct the arithmetic errors and rank numbering inconsistencies before final acceptance.

---

## Findings Summary

| ID | Severity | Finding | Section |
|----|----------|---------|---------|
| CV-001 | Major | Double Diamond weighted total stated as 7.55; arithmetic yields 7.45 | Section 2, Full Scoring Matrix, row 11 |
| CV-002 | Major | Design Thinking weighted total stated as 7.25; arithmetic yields 7.10 | Section 2, Full Scoring Matrix, row 12 |
| CV-003 | Major | Hook Model weighted total stated as 7.00; arithmetic yields 6.80 | Section 2, Full Scoring Matrix, row 13 |
| CV-004 | Major | UX Strategy weighted total stated as 7.00; arithmetic yields 6.75 | Section 2, Full Scoring Matrix, row 14 |
| CV-005 | Major | Cognitive Walkthrough weighted total stated as 6.90; arithmetic yields 6.70 | Section 2, Full Scoring Matrix, row 16 |
| CV-006 | Minor | UX Honeycomb weighted total stated as 6.85; arithmetic yields 6.70 | Section 2, Full Scoring Matrix, row 17 |
| CV-007 | Minor | Gestalt Principles weighted total stated as 6.90; arithmetic yields 6.95 | Section 2, Full Scoring Matrix, row 19 |
| CV-008 | Major | Service Blueprinting weighted total stated as 7.35; arithmetic yields 7.40 | Section 2, Full Scoring Matrix, row 15 |
| CV-009 | Critical | Sensitivity analysis AI-First Design score @20% weight stated as 7.30; arithmetic yields 7.80 | Section 1, Sensitivity Analysis table |
| CV-010 | Major | Sensitivity analysis Design Sprint score @20% weight stated as 8.95; arithmetic yields 9.10 | Section 1, Sensitivity Analysis table |
| CV-011 | Major | Sensitivity analysis Nielsen's Heuristics score @20% weight stated as 8.95; arithmetic yields 9.05 | Section 1, Sensitivity Analysis table |
| CV-012 | Major | AI-First Design and Microsoft Inclusive Design each assigned conflicting rank numbers across sections | Sections 3.8, 4, 5, 6 |
| CV-013 | Minor | Lean UX section 3.5 labels Hotjar as "third-party MCP" but Section 1 MCP inventory and Section 3.4 HEART correctly label it "Bridge MCP (requires Zapier/Pipedream)" | Section 3.5 |

---

## Detailed Findings

### CV-001: Double Diamond Weighted Total Arithmetic Error [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 2, Full Scoring Matrix, row 11 |
| **Strategy Step** | Step 3: Independent Verification (arithmetic recalculation from raw scores) |

**Evidence (from deliverable):**
> `| 11 | Double Diamond (UK Design Council) | 8 | 9 | 5 | 9 | 5 | 8 | 7.55 | No |`

**Analysis:**
Independent arithmetic using the formula C1*(0.25) + C2*(0.20) + C3*(0.15) + C4*(0.15) + C5*(0.15) + C6*(0.10) applied to the stated raw scores (8,9,5,9,5,8):

- 8*0.25 = 2.00
- 9*0.20 = 1.80
- 5*0.15 = 0.75
- 9*0.15 = 1.35
- 5*0.15 = 0.75
- 8*0.10 = 0.80
- **Sum = 7.45**

Stated total: 7.55. Discrepancy: +0.10 overstated.

This error does not change Double Diamond's rank (11) or its exclusion decision, but it means the gap between Double Diamond (stated 7.55) and the 10th-place Fogg (7.60) is only 0.05 -- presented as 0.05. The corrected gap is 0.15 (7.45 vs. 7.60), which actually strengthens the exclusion case. The risk is that the stated value (7.55) contradicts the independent arithmetic and could mislead any future re-analysis.

**Recommendation:**
Correct row 11 weighted total from **7.55** to **7.45**. Verify all remaining non-top-10 rows against the same formula.

---

### CV-002: Design Thinking Weighted Total Arithmetic Error [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 2, Full Scoring Matrix, row 12 |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| 12 | Design Thinking (IDEO/d.school) | 7 | 8 | 5 | 10 | 4 | 9 | 7.25 | No |`

**Analysis:**
Independent arithmetic from raw scores (7,8,5,10,4,9):

- 7*0.25 = 1.75
- 8*0.20 = 1.60
- 5*0.15 = 0.75
- 10*0.15 = 1.50
- 4*0.15 = 0.60
- 9*0.10 = 0.90
- **Sum = 7.10**

Stated total: 7.25. Discrepancy: +0.15 overstated.

Section 5.2 discusses Design Thinking at "Score: 7.25." The Section 6 seed list audit also states Design Thinking score as 7.25. Both reference the incorrect value. The overstatement of 0.15 narrows the gap with the 10th-place Fogg from 0.35 to 0.50 -- the correction strengthens the exclusion case but the error should be corrected for evidential integrity.

**Recommendation:**
Correct row 12 weighted total from **7.25** to **7.10**. Update Section 5.2 header ("Score: 7.25" -> "Score: 7.10") and Section 6 seed list audit row accordingly.

---

### CV-003: Hook Model Weighted Total Arithmetic Error [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 2, Full Scoring Matrix, row 13 |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| 13 | Hook Model (Nir Eyal) | 8 | 8 | 4 | 7 | 5 | 8 | 7.00 | No |`

**Analysis:**
Independent arithmetic from raw scores (8,8,4,7,5,8):

- 8*0.25 = 2.00
- 8*0.20 = 1.60
- 4*0.15 = 0.60
- 7*0.15 = 1.05
- 5*0.15 = 0.75
- 8*0.10 = 0.80
- **Sum = 6.80**

Stated total: 7.00. Discrepancy: +0.20 overstated.

The overstatement of 0.20 is material. Section 5.4 discusses the Hook Model as "Score: 7.00." The corrected value of 6.80 widens its gap from 10th-place Fogg (7.60) from 0.60 to 0.80, and positions it below Cognitive Walkthrough (corrected to 6.70) by only 0.10. The exclusion decision is unchanged but the stated score is incorrect.

**Recommendation:**
Correct row 13 weighted total from **7.00** to **6.80**. Update Section 5.4 header score accordingly.

---

### CV-004: UX Strategy Weighted Total Arithmetic Error [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 2, Full Scoring Matrix, row 14 |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| 14 | UX Strategy (Jaime Levy) | 8 | 8 | 4 | 6 | 7 | 6 | 7.00 | No |`

**Analysis:**
Independent arithmetic from raw scores (8,8,4,6,7,6):

- 8*0.25 = 2.00
- 8*0.20 = 1.60
- 4*0.15 = 0.60
- 6*0.15 = 0.90
- 7*0.15 = 1.05
- 6*0.10 = 0.60
- **Sum = 6.75**

Stated total: 7.00. Discrepancy: +0.25 overstated.

The overstatement is 0.25. Section 5.5 discusses UX Strategy at "Score: 7.00." This is the second framework given an incorrect rounded total of 7.00 -- both Hook Model and UX Strategy are listed at 7.00 in the matrix, but neither arithmetically yields 7.00. The corrected values would be 6.80 (Hook) and 6.75 (UX Strategy). Their tied rank listing at 13/14 is coincidental but each is individually incorrect.

**Recommendation:**
Correct row 14 weighted total from **7.00** to **6.75**. Update Section 5.5 header score accordingly.

---

### CV-005: Cognitive Walkthrough Weighted Total Arithmetic Error [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 2, Full Scoring Matrix, row 16 |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| 16 | Cognitive Walkthrough | 8 | 8 | 4 | 7 | 5 | 7 | 6.90 | No |`

**Analysis:**
Independent arithmetic from raw scores (8,8,4,7,5,7):

- 8*0.25 = 2.00
- 8*0.20 = 1.60
- 4*0.15 = 0.60
- 7*0.15 = 1.05
- 5*0.15 = 0.75
- 7*0.10 = 0.70
- **Sum = 6.70**

Stated total: 6.90. Discrepancy: +0.20 overstated.

This finding is especially significant because Cognitive Walkthrough is explicitly named as a **V2 priority candidate** for the `/user-experience` skill throughout the document. In Section 1, it is stated: "V2 candidate: Cognitive Walkthrough, rank 16, score 6.90." In Section 4 (Complementarity Matrix), it is stated: "Cognitive Walkthrough (rank #16, score 6.90) is the natural V2 candidate." Both references cite the incorrect 6.90 value. The corrected value of 6.70 does not invalidate the V2 recommendation, but the incorrect score is a factual error in a specifically-cited recommendation.

**Recommendation:**
Correct row 16 weighted total from **6.90** to **6.70**. Update all V2 candidate references: Section 1 UX Failure Mode Coverage table (Feature discoverability V2 candidate mention), Section 4 gap analysis, Section 4 Complementarity Matrix text. Change "score 6.90" to "score 6.70" in each reference.

---

### CV-006: UX Honeycomb Weighted Total Arithmetic Error [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 2, Full Scoring Matrix, row 17 |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| 17 | UX Honeycomb (Peter Morville) | 7 | 8 | 4 | 9 | 4 | 8 | 6.85 | No |`

**Analysis:**
Independent arithmetic from raw scores (7,8,4,9,4,8):

- 7*0.25 = 1.75
- 8*0.20 = 1.60
- 4*0.15 = 0.60
- 9*0.15 = 1.35
- 4*0.15 = 0.60
- 8*0.10 = 0.80
- **Sum = 6.70**

Stated total: 6.85. Discrepancy: +0.15 overstated.

The UX Honeycomb exclusion rationale is not affected, but the stated total is incorrect. The corrected score (6.70) ties with Cognitive Walkthrough (corrected 6.70), requiring a tiebreaker explanation for their rank ordering (17 vs. 16). Per the current raw scores, the rankings as rows 16/17 may need reordering depending on whether rank order follows the corrected totals.

**Recommendation:**
Correct row 17 weighted total from **6.85** to **6.70**. Note that rows 16 and 17 would then be tied at 6.70 -- document tiebreaker rationale or verify raw scores for both.

---

### CV-007: Gestalt Principles Weighted Total Minor Error (Direction Reversed) [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 2, Full Scoring Matrix, row 19 |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| 19 | Gestalt Principles of Perception | 7 | 7 | 5 | 10 | 5 | 8 | 6.90 | No |`

**Analysis:**
Independent arithmetic from raw scores (7,7,5,10,5,8):

- 7*0.25 = 1.75
- 7*0.20 = 1.40
- 5*0.15 = 0.75
- 10*0.15 = 1.50
- 5*0.15 = 0.75
- 8*0.10 = 0.80
- **Sum = 6.95**

Stated total: 6.90. Discrepancy: -0.05 understated (direction reversed from CV-001 through CV-006). The error is small and the exclusion decision is unaffected. This finding is Minor because the magnitude is small (0.05) and the direction of error is opposite to the other arithmetic errors, suggesting a rounding treatment difference rather than systematic overstatement.

**Recommendation:**
Correct row 19 weighted total from **6.90** to **6.95**. At 6.95, Gestalt Principles ranks above the corrected Cognitive Walkthrough (6.70) and UX Honeycomb (6.70) and ties near Octalysis (6.70 corrected; verify separately).

---

### CV-008: Service Blueprinting Weighted Total Error (Direction Reversed) [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 2, Full Scoring Matrix, row 15 |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| 15 | Service Blueprinting | 7 | 8 | 7 | 8 | 8 | 6 | 7.35 | No |`

**Analysis:**
Independent arithmetic from raw scores (7,8,7,8,8,6):

- 7*0.25 = 1.75
- 8*0.20 = 1.60
- 7*0.15 = 1.05
- 8*0.15 = 1.20
- 8*0.15 = 1.20
- 6*0.10 = 0.60
- **Sum = 7.40**

Stated total: 7.35. Discrepancy: -0.05 understated.

This finding is especially significant because Service Blueprinting is the primary V2 candidate identified throughout the document. The sensitivity analysis states: "Service Blueprinting (11th) | 7.35 | 7.40 | Near threshold" -- interestingly the sensitivity analysis @20% column correctly shows 7.40, but this is labeled as the @20% weight score, not the @25% weight score. The @25% weight score (from the main matrix) is stated as 7.35 but arithmetically yields 7.40. The sensitivity table thus has the two columns effectively correct for Service Blueprinting, but they are inverted relative to the weight change: the "correct" Service Blueprinting total (7.40) appears in the @20% column when it should be in the @25% column.

Multiple downstream claims reference "Service Blueprinting (next candidate, 7.35)": Revision 1 note states "Service Blueprinting (next candidate, 7.35) is not affected by these corrections"; Section 4 Gap Analysis mentions "Service Blueprinting (rank #11, score 7.35)"; Section 5.3 header says "Score: 7.35"; Section 6 seed list mentions "Service Blueprinting (rank #11, score 7.35)." All should read 7.40.

At the corrected value of 7.40, Service Blueprinting is 0.20 points below the 10th-place Fogg (7.60) rather than the stated 0.25. The gap is still clear; the exclusion decision is unchanged.

**Recommendation:**
Correct row 15 weighted total from **7.35** to **7.40**. Update all downstream references: Section 2 note ("Service Blueprinting (next candidate, 7.35)" -> 7.40), Section 4 Gap Analysis, Section 5.3 header, Section 6 seed list, Revision 1 note.

---

### CV-009: Sensitivity Analysis -- AI-First Design @20% Weight Score Is Incorrect [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 1, Sensitivity Analysis table |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| AI-First Design | 7.80 | 7.30 | **Down 2 -- most weight-sensitive** |`

**Analysis:**
The sensitivity analysis recalculates scores under an alternate weighting where C1 (Tiny Teams) drops from 25% to 20% and C5 (Complementarity) increases from 15% to 20%.

New formula for @20%: C1*(0.20) + C2*(0.20) + C3*(0.15) + C4*(0.15) + C5*(0.20) + C6*(0.10)

AI-First Design raw scores: C1=10, C2=8, C3=8, C4=2, C5=10, C6=7

- 10*0.20 = 2.00
- 8*0.20 = 1.60
- 8*0.15 = 1.20
- 2*0.15 = 0.30
- 10*0.20 = 2.00
- 7*0.10 = 0.70
- **Sum = 7.80**

Stated @20% score: **7.30**. Arithmetic yields: **7.80**. Discrepancy: **-0.50 understated**.

This is the most significant finding in the entire CoVe analysis. The deliverable's core analytical argument in Section 1 regarding AI-First Design states:

> "The one sensitive selection (AI-First Design, rank 8) drops 0.50 points, narrowing the gap with Service Blueprinting (7.35-7.40) to marginal -- but remains in the top 10."

This argument rests entirely on the claim that AI-First Design drops to 7.30 under the alternate weighting. However, independent arithmetic using the stated raw scores and the stated alternate formula yields 7.80 -- **identical to the @25% score**. This makes physical sense: AI-First Design scores C1=10 and C5=10, which are exactly the two criteria whose weights are swapped (C1 decreases by 5%, C5 increases by 5%). When both swapped criteria are scored identically (both at 10), the weighted sum cannot change: -0.05*10 + 0.05*10 = 0. The score should be invariant under this specific weight redistribution for AI-First Design.

The claim "drops 0.50 points" is arithmetically impossible given the raw scores. The deliverable's conclusion that AI-First Design is "the most weight-sensitive selection" is also directly contradicted: a framework that scores identically under both weightings (7.80 vs. 7.80) is the **least** weight-sensitive selection among those with C1 = C5. The sensitivity analysis conclusion is inverted.

The actual most weight-sensitive selection is Lean UX, which has C1=9 and C5=8 (unequal, so the redistribution does affect it): @25%=8.25, @20%: 9*0.20+9*0.20+6*0.15+8*0.15+8*0.20+9*0.10 = 1.80+1.80+0.90+1.20+1.60+0.90 = **8.20** (drop of 0.05). Even Lean UX barely changes, confirming the analysis is broadly stable -- but the specific claim about AI-First Design being weight-sensitive is false.

**Recommendation:**
Correct the @20% weight score for AI-First Design from **7.30** to **7.80**. Revise the sensitivity analysis conclusion: AI-First Design is NOT the most weight-sensitive selection -- it is invariant because C1=C5=10. The corrected conclusion should state: "All 10 selected frameworks maintain their position under the alternate weighting; AI-First Design's score is invariant (7.80) because its C1 and C5 scores are identical (10=10), so redistributing weight between them has no effect." This conclusion is actually a STRONGER argument for AI-First Design's robustness, not weaker.

---

### CV-010: Sensitivity Analysis -- Design Sprint @20% Weight Score Incorrect [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1, Sensitivity Analysis table |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| Design Sprint | 9.15 | 8.95 | Stable #1 |`

**Analysis:**
Design Sprint raw scores: C1=10, C2=10, C3=8, C4=8, C5=9, C6=9

@20% formula: 10*0.20+10*0.20+8*0.15+8*0.15+9*0.20+9*0.10
= 2.00+2.00+1.20+1.20+1.80+0.90
= **9.10**

Stated @20% score: 8.95. Arithmetic yields: 9.10. Discrepancy: -0.15 understated.

The exclusion decision is unaffected (Design Sprint remains #1), but the stated value is incorrect.

**Recommendation:**
Correct Design Sprint @20% score from **8.95** to **9.10**. The "Stable #1" conclusion stands.

---

### CV-011: Sensitivity Analysis -- Nielsen's Heuristics @20% Weight Score Incorrect [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1, Sensitivity Analysis table |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**
> `| Nielsen's Heuristics | 9.05 | 8.95 | Stable #2 |`

**Analysis:**
Nielsen's raw scores: C1=9, C2=10, C3=7, C4=10, C5=9, C6=9

@20% formula: 9*0.20+10*0.20+7*0.15+10*0.15+9*0.20+9*0.10
= 1.80+2.00+1.05+1.50+1.80+0.90
= **9.05**

Stated @20% score: 8.95. Arithmetic yields: 9.05. Discrepancy: -0.10 understated. Notably, at 9.05 Nielsen's @20% ties its own @25% score (9.05), meaning it too is nearly invariant -- C1=9 and C5=9, so the redistribution cancels out almost exactly. The "Stable #2" conclusion stands but the specific value is incorrect.

**Recommendation:**
Correct Nielsen's @20% score from **8.95** to **9.05**. The sensitivity table conclusion is unchanged.

---

### CV-012: AI-First Design and Microsoft Inclusive Design Rank Numbering Conflict [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Multiple sections (coverage analysis, complementarity matrix, lifecycle table, seed list) |
| **Strategy Step** | Step 4: Consistency Check |

**Evidence (from deliverable):**

The scoring matrix (Section 2) establishes:
- Row 7: Microsoft Inclusive Design -- rank #7
- Row 8: AI-First Design -- rank #8

However, multiple downstream references in the document conflict:

Section 3.8 (Microsoft Inclusive Design header):
> `| **Verified weighted score** | 8.00 (Rank #8) |`

Section 4 Coverage Map row:
> `| **AI Product UX** | AI-First Design (#7) |`
> `| **Accessibility & Inclusion** | Microsoft Inclusive Design (#8) |`

Section 4 Complementarity Matrix diagram:
> `ACCESSIBILITY LAYER: Microsoft Inclusive Design (#7) -- always active`
> `AI PRODUCT LAYER: AI-First Design (#8) -- always active`

Section 4 Integration Paths table:
> `| AI-First Design (#7) | Atomic Design (#3) |`

Section 4 Lifecycle Phase Summary:
> `| Build | Atomic Design (#3), Microsoft Inclusive Design (#8) | AI-First Design (#8) |`

Section 6 Seed list:
> `Design Sprint #1, HEART #4, JTBD #6, AI-First Design #7, Microsoft Inclusive Design #8`

Section 6 Non-seed winners note:
> `AI-First Design (#7) -- frameworks not on the seed list that earned their place`

Revision log entry:
> `RT-003 ... rank updated to #8`

**Summary of contradictions:** AI-First Design is labeled as #7 in 4 places and #8 in 4 places. Microsoft Inclusive Design is labeled as #7 in 2 places and #8 in 3 places. The scoring matrix (Section 2, the primary source) shows Microsoft Inclusive Design at rank #7 (score 8.00) and AI-First Design at rank #8 (score 7.80). All inconsistent references should be corrected to match the scoring matrix.

**Recommendation:**
Standardize throughout: Microsoft Inclusive Design = **#7**, AI-First Design = **#8**. Apply corrections to: Section 3.8 attribute table, Section 4 Coverage Map table, Section 4 Complementarity Matrix diagram, Section 4 Integration Paths table, Section 4 Lifecycle Phase Summary (secondary framework column), Section 6 seed list commentary.

---

### CV-013: Lean UX Section 3.5 Labels Hotjar Inconsistently [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 3.5 |
| **Strategy Step** | Step 4: Consistency Check |

**Evidence (from deliverable):**

Section 1 MCP inventory table:
> `| **Bridge MCP (requires Zapier/Pipedream)** | Hotjar -- WARNING: requires paid Zapier/Pipedream subscription`

Section 3.4 HEART Framework MCP integrations:
> `- **Hotjar** (Bridge MCP via Zapier/Pipedream) -- ... WARNING: Requires paid Zapier/Pipedream subscription`

Section 3.9 Fogg Behavior Model MCP integrations:
> `- **Hotjar** (Bridge MCP via Zapier/Pipedream) -- ... WARNING: Bridge MCP only -- requires paid Zapier/Pipedream subscription`

Section 3.5 Lean UX MCP integrations:
> `- **Hotjar** (third-party MCP) -- Behavioral data for the Measure phase`

**Analysis:**
Section 3.5 uses the term "third-party MCP" for Hotjar, while every other section in the deliverable consistently uses "Bridge MCP via Zapier/Pipedream" with an accompanying WARNING about setup complexity. The inconsistency is minor because the claim does not affect any scoring or selection decision, but it creates a false impression in Section 3.5 that Hotjar for Lean UX is a simpler integration than for HEART and Fogg. The Bridge MCP warning should be applied consistently.

**Recommendation:**
Replace "Hotjar (third-party MCP)" in Section 3.5 with "**Hotjar** (Bridge MCP via Zapier/Pipedream) -- Behavioral data for the Measure phase. **WARNING: Same setup complexity as HEART/Fogg: requires paid Zapier/Pipedream subscription and custom configuration.**"

---

## Claim Inventory (Full)

| ID | Claim Type | Claim | Source | Verification Result |
|----|-----------|-------|--------|---------------------|
| CL-001 | Quoted value | Design Sprint weighted total = 9.15 | Section 2 score calculation table | VERIFIED |
| CL-002 | Quoted value | Nielsen's weighted total = 9.05 | Section 2 score calculation table | VERIFIED |
| CL-003 | Quoted value | Atomic Design weighted total = 8.55 | Section 2 score calculation table | VERIFIED |
| CL-004 | Quoted value | HEART weighted total = 8.30 | Section 2 score calculation table | VERIFIED |
| CL-005 | Quoted value | Lean UX weighted total = 8.25 | Section 2 score calculation table | VERIFIED |
| CL-006 | Quoted value | JTBD weighted total = 8.05 | Section 2 score calculation table | VERIFIED |
| CL-007 | Quoted value | Microsoft Inclusive Design weighted total = 8.00 | Section 2 score calculation table | VERIFIED |
| CL-008 | Quoted value | AI-First Design weighted total = 7.80 | Section 2 score calculation table | VERIFIED |
| CL-009 | Quoted value | Kano Model weighted total = 7.65 | Section 2 score calculation table | VERIFIED |
| CL-010 | Quoted value | Fogg Behavior Model weighted total = 7.60 | Section 2 score calculation table | VERIFIED |
| CL-011 | Quoted value | Double Diamond weighted total = 7.55 | Section 2 full matrix | MATERIAL DISCREPANCY (CV-001) |
| CL-012 | Quoted value | Service Blueprinting weighted total = 7.35 | Section 2 full matrix | MATERIAL DISCREPANCY (CV-008) |
| CL-013 | Quoted value | Design Thinking weighted total = 7.25 | Section 2 full matrix | MATERIAL DISCREPANCY (CV-002) |
| CL-014 | Quoted value | Hook Model weighted total = 7.00 | Section 2 full matrix | MATERIAL DISCREPANCY (CV-003) |
| CL-015 | Quoted value | UX Strategy weighted total = 7.00 | Section 2 full matrix | MATERIAL DISCREPANCY (CV-004) |
| CL-016 | Quoted value | Cognitive Walkthrough score = 6.90 (V2 candidate) | Section 1, Section 4 | MATERIAL DISCREPANCY (CV-005) |
| CL-017 | Quoted value | UX Honeycomb weighted total = 6.85 | Section 2 full matrix | MINOR DISCREPANCY (CV-006) |
| CL-018 | Quoted value | Gestalt Principles weighted total = 6.90 | Section 2 full matrix | MINOR DISCREPANCY (CV-007) |
| CL-019 | Behavioral claim | AI-First Design @20% weight drops to 7.30 | Section 1 sensitivity analysis | MATERIAL DISCREPANCY (CV-009) |
| CL-020 | Behavioral claim | Design Sprint @20% weight = 8.95 | Section 1 sensitivity analysis | MATERIAL DISCREPANCY (CV-010) |
| CL-021 | Behavioral claim | Nielsen's @20% weight = 8.95 | Section 1 sensitivity analysis | MATERIAL DISCREPANCY (CV-011) |
| CL-022 | Historical assertion | HEART C3 corrected from 6 to 4 per RT-002 | Section 2 note, Section 3.4 | VERIFIED |
| CL-023 | Historical assertion | Fogg C3 corrected from 4 to 3 per RT-002 | Section 2 note, Section 3.9 | VERIFIED |
| CL-024 | Historical assertion | AI-First Design C4 corrected from 3 to 2 per RT-003 | Section 2 note, Section 3.7 | VERIFIED |
| CL-025 | Cross-reference | Microsoft Inclusive Design is rank #7 per scoring matrix | Section 2 matrix vs. downstream sections | MATERIAL DISCREPANCY (CV-012 -- conflicting ranks) |
| CL-026 | Cross-reference | AI-First Design is rank #8 per scoring matrix | Section 2 matrix vs. downstream sections | MATERIAL DISCREPANCY (CV-012 -- conflicting ranks) |
| CL-027 | Behavioral claim | Hotjar is Bridge MCP requiring Zapier/Pipedream | Section 1 MCP inventory | MINOR DISCREPANCY for Section 3.5 (CV-013) |
| CL-028 | Behavioral claim | 9 of 10 frameworks stable under alternate weighting | Section 1 sensitivity analysis conclusion | VERIFIED (all 10 are actually stable; AI-First Design invariant at 7.80 -- selection claim is correct even though stated score is wrong) |

---

## Recommendations

### Critical (MUST correct before acceptance)

**CV-009: Sensitivity analysis AI-First Design @20% score**
- Finding: Score stated as 7.30; arithmetic yields 7.80 (invariant because C1=C5=10)
- Correction: Change 7.30 to 7.80 in the sensitivity analysis table
- Revise conclusion: AI-First Design is invariant under this weight redistribution (not the "most weight-sensitive selection"). The conclusion "all 10 selections are robustly supported" should be strengthened accordingly.

### Major (SHOULD correct)

**CV-001:** Double Diamond: correct 7.55 to **7.45**

**CV-002:** Design Thinking: correct 7.25 to **7.10** (also Section 5.2 header and Section 6 seed list row)

**CV-003:** Hook Model: correct 7.00 to **6.80** (also Section 5.4 header)

**CV-004:** UX Strategy: correct 7.00 to **6.75** (also Section 5.5 header)

**CV-005:** Cognitive Walkthrough: correct 6.90 to **6.70** in all V2 candidate references throughout document (Section 1 failure mode coverage, Section 4 gap analysis, Section 4 complementarity matrix text)

**CV-008:** Service Blueprinting: correct 7.35 to **7.40** in matrix row, Section 5.3 header, Section 4 gap analysis references, Section 2 note ("Service Blueprinting (next candidate, 7.35)" -> 7.40), and all "score 7.35" references throughout

**CV-010:** Design Sprint sensitivity @20%: correct 8.95 to **9.10**

**CV-011:** Nielsen's sensitivity @20%: correct 8.95 to **9.05**

**CV-012:** Rank numbering -- standardize Microsoft Inclusive Design as **#7**, AI-First Design as **#8** across all sections:
- Section 3.8 attribute table (currently incorrectly says Rank #8 for Microsoft Inclusive Design)
- Section 4 Coverage Map (AI-First Design currently shown as #7; correct to #8)
- Section 4 Complementarity Matrix diagram (Microsoft Inclusive shows as #7; correct to #7 -- this one is correct; AI-First shows as #8 -- this one is correct)
- Section 4 Integration Paths (AI-First as #7; correct to #8)
- Section 4 Lifecycle Phase Summary secondary column
- Section 6 seed list commentary

### Minor (MAY correct)

**CV-006:** UX Honeycomb: correct 6.85 to **6.70**

**CV-007:** Gestalt Principles: correct 6.90 to **6.95**

**CV-013:** Lean UX Section 3.5 Hotjar label: change "third-party MCP" to "Bridge MCP via Zapier/Pipedream" with WARNING consistent with other sections

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Neutral | All 40 frameworks are present in the scoring matrix; all 10 selected frameworks have detailed justifications. The arithmetic errors are in the recorded totals, not in any missing framework coverage. |
| Internal Consistency | 0.20 | Negative | CV-012 (rank numbering conflicts), CV-009 (sensitivity analysis conclusion inconsistent with raw scores), CV-013 (Hotjar label inconsistency) all reduce internal consistency. The deliverable references Microsoft Inclusive Design as both #7 and #8 within the same document, which is a direct internal contradiction. |
| Methodological Rigor | 0.20 | Negative | CV-001 through CV-008 (seven arithmetic errors in non-top-10 totals) and CV-009 through CV-011 (three arithmetic errors in sensitivity analysis) indicate that the non-selected framework totals and sensitivity values were not independently recomputed from raw scores. The top-10 Score Calculation Verification table (Section 2) shows rigorous arithmetic for the selected frameworks, but this rigor was not applied to the full matrix or the sensitivity analysis. |
| Evidence Quality | 0.15 | Negative | CV-005 and CV-008 specifically affect claims cited as evidence for V2 recommendations (Cognitive Walkthrough as the V2 candidate at "score 6.90," Service Blueprinting as "score 7.35"). The incorrect scores mean that the V2 priority evidence citations are factually wrong. |
| Actionability | 0.15 | Neutral | The selection decisions for the top 10 are not affected by any finding. The corrections are numerical updates that strengthen the document's evidential basis without reversing any conclusion. CV-009 actually improves actionability for AI-First Design (its robustness is greater than claimed). |
| Traceability | 0.10 | Negative | CV-012 (rank numbering conflicts) degrades traceability: readers following cross-references between sections encounter conflicting rank numbers. The Revision 1 log entry states "rank updated to #8" for AI-First Design, but at least 4 downstream sections still reference it as #7. |

---

## Execution Statistics

- **Total Findings:** 13
- **Critical:** 1 (CV-009)
- **Major:** 8 (CV-001, CV-002, CV-003, CV-004, CV-005, CV-008, CV-010, CV-011, CV-012)
- **Minor:** 3 (CV-006, CV-007, CV-013) -- **Note: CV-007 is understated in the deliverable (direction reversed)**; the other Minors are overstated
- **Claims Extracted:** 28
- **Verified:** 15 (53.6%)
- **Minor Discrepancy:** 2 (7.1%)
- **Material Discrepancy:** 11 (39.3%)
- **Unverifiable:** 0
- **Protocol Steps Completed:** 5 of 5

---

*Strategy Execution Report: S-011 Chain-of-Verification*
*Template: .context/templates/adversarial/s-011-cove.md*
*Deliverable: projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md*
*Executed: 2026-03-02T00:00:00Z*
*Finding Prefix: CV (per S-011 template Identity section)*
