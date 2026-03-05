# Quality Score Report: Fogg B=MAP Behavior Methodology Rules

## L0 Executive Summary

**Score:** 0.954/1.00 | **Verdict:** PASS | **Weakest Dimension:** Completeness (0.93)
**One-line assessment:** All 7 iter1 defects confirmed fixed with no regressions introduced; the artifact now meets the C4 >= 0.95 threshold, with one residual minor gap (self-review checklist missing an action-line position verification item) and a pre-existing tier-vocabulary pattern (6 MEDIUM-tier rules still use "MUST" language) that, while noted, does not block acceptance at this scoring level.

---

## Scoring Context

- **Deliverable:** `skills/ux-behavior-design/rules/fogg-behavior-rules.md`
- **Deliverable Type:** Methodology rules file (sub-skill operational constraints for ux-behavior-design)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md` (Quality Gate section)
- **C4 Pass Threshold:** >= 0.95 (per QG-001 in the artifact; governance source: PROJ-022 ORCHESTRATION.yaml)
- **H-13 Baseline:** >= 0.92 (C2+)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2 (prior score: 0.893, REVISE)
- **Iter1 Defects Verified Fixed:** 7/7 confirmed

---

## Iter1 Defect Verification

Each of the 7 improvements from `rules-iter1-score.md` is verified before scoring proceeds.

| # | Iter1 Defect | Status | Verification Evidence |
|---|-------------|--------|----------------------|
| 1 | Add "Consequence of Violation" column to CLS-001–005 | FIXED | CLS table now has 4 columns `\| ID \| Rule \| Tier \| Consequence of Violation \|`; all 5 CLS rules have specific violation consequences (lines 315-319) |
| 2 | Add action-line position requirement to OUT-004 | FIXED | OUT-004 (line 349) now ends with "AND an explicit action-line position statement describing whether the user is above or below the action line and which factor(s) need to change" |
| 3 | Resolve wave-progression.md version conflict (unversioned vs. v1.2.0) | FIXED | Related Files table (line 392) now shows `v1.2.0`, matching the agent definition |
| 4 | Review SEV-003 and PRM-004 tier assignments (MUST in MEDIUM) | FIXED | SEV-003 (line 270): "severity SHOULD be derived from factor score patterns" (was "MUST"). PRM-004 (line 172): "Prompt timing SHOULD be assessed" (was "MUST") |
| 5 | Add source citations to MOT-005 and CLS-004 | FIXED | MOT-005 (line 93) now cites "Source: P-001 (truth and accuracy); Fogg (2020) evidence-based scoring principle." CLS-004 (line 318) now cites "Source: skills/user-experience/rules/synthesis-validation.md (v1.1.0) minimum-confidence aggregation rule." |
| 6 | Rewrite SEV-003 consequence from feature description to violation consequence | FIXED | SEV-003 consequence (line 270): "Inconsistent severity classification when operating qualitatively; teams cannot prioritize behavioral issues without a systematic severity estimate" — now states a consequence of violation, not a benefit |
| 7 | Add governance traceability for >= 0.95 C4 threshold in QG-001 | FIXED | QG-001 (line 375): "(governance source: PROJ-022 ORCHESTRATION.yaml C4 scoring specification)" now appended to threshold statement |

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.954 |
| **C4 Threshold** | 0.95 |
| **H-13 Baseline** | 0.92 |
| **Verdict** | PASS |
| **Delta from Iter1** | +0.061 (0.893 -> 0.954) |
| **Strategy Findings Incorporated** | No (standalone scoring) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | All 10 rule sections present; action-line position added to OUT-004; self-review checklist still missing corresponding verification item |
| Internal Consistency | 0.20 | 0.95 | 0.190 | Convergence framing consistent throughout; tier vocabulary fixed for SEV-003 and PRM-004; 6 other MEDIUM-tier rules still use "MUST" language (pre-existing, not regression) |
| Methodological Rigor | 0.20 | 0.97 | 0.194 | Fogg citations precise with DOI; convergence enforcement complete; elimination algorithm correctly ordered and cited; severity heuristics honestly disclosed; action-line position now enforceable per OUT-004 |
| Evidence Quality | 0.15 | 0.96 | 0.144 | CLS consequence column fully populated; MOT-005 and CLS-004 citations added; template reference acknowledged as planned; no new evidence gaps introduced |
| Actionability | 0.15 | 0.95 | 0.143 | 18-item self-review checklist maps to rule IDs; missing action-line check item is a minor gap; SEV-003 consequence rewritten as violation consequence; ALG-005 consequence is present but brief |
| Traceability | 0.10 | 0.97 | 0.097 | QG-001 C4 threshold cites ORCHESTRATION.yaml; wave-progression.md version resolved; MOT-005 and CLS-004 citations resolved; mcp-coordination.md remains unversioned (pre-existing, acknowledged in table) |
| **TOTAL** | **1.00** | | **0.954** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence for score:**
The artifact covers 10 rule sections totaling 53 rules (BMAP-001–005, MOT-001–006, ABL-001–007, PRM-001–005, ALG-001–005, INT-001–007, SEV-001–003, CLS-001–005, OUT-001–007, QG-001–004). Navigation table lists all 12 sections with anchor links. The 18-item self-review checklist is comprehensive, and the Related Files dependency matrix maps 8 files. The quality gate section maps all 6 S-014 dimensions to Behavior Design evaluation criteria. OUT-004 now enforces the action-line position requirement, closing the most significant completeness gap from iter1.

**Remaining gaps:**

1. **Self-review checklist missing action-line position check.** OUT-004 was correctly amended to require "an explicit action-line position statement" in the Behavior State Map. However, the self-review checklist (lines 401-424) was not updated to include a corresponding verification step. Checklist items 6-8 cover ability factors, limiting factor, and prompt assessment, but none verify the action-line position. An agent following the 18-item checklist could produce a report that passes all checklist items yet still omit the action-line position statement. The OUT-004 rule catches this at the output filtering level, but the self-review checklist (S-010) is the agent's first line of defense. This is a minor incompleteness introduced by the iter2 revision (the fix added a rule requirement but did not close the loop in the checklist).

**Gap impact assessment:**
This gap is minor — OUT-004 itself is a HARD rule and will catch the omission at output review. The self-review checklist is a convenience verification layer, not the sole enforcement mechanism. The impact on output quality is low; the impact on process completeness is moderate.

**Improvement Path:**
Add checklist item 8a (between current items 8 and 9): "Action-line position statement present in Behavior State Map (above/below action line; factor(s) needed to change)" | OUT-004

---

### Internal Consistency (0.95/1.00)

**Evidence for score:**
The B=MAP convergence framing is fully consistent throughout. BMAP-001 prohibits multiplication framing; the convergence model is stated in the section header, the convergence principles table, and the action-line principle. The elimination algorithm order (prompt -> ability -> motivation -> multiple) is consistent between the algorithm section, the algorithm discipline rules (ALG-001), and the intervention design section (INT-003). The quality gate threshold (>= 0.95 at C4) is consistent between QG-001 and the governance source cited (ORCHESTRATION.yaml). The wave-progression.md version is now consistent between the rules file (v1.2.0) and the agent definition (v1.2.0).

SEV-003 and PRM-004 are now internally consistent: both use "SHOULD" language aligned with MEDIUM tier vocabulary. The evidence chain within each section is logically consistent: motivation scores determine threshold judgments (MOT-006), ability scores determine limiting factor (ABL-002), limiting factor determines ability threshold (ABL-006), threshold judgments feed the elimination algorithm (ALG-001), and bottleneck classification drives intervention targeting (INT-005).

**Remaining gaps:**

1. **Six MEDIUM-tier rules still use "MUST" language.** The iter1 report specifically flagged SEV-003 and PRM-004 (fixed). However, six other MEDIUM-tier rules retain "MUST" language: MOT-006 ("MUST state whether motivation is 'above threshold' or 'below threshold'"), ABL-006 ("MUST state whether ability is 'above threshold' or 'below threshold'"), PRM-005 ("placement MUST be classified as 'Competing'"), ALG-005 ("diagnosis MUST specify which factors are borderline"), INT-006 ("Each intervention MUST be classified as 'Direct' or 'Supporting'"), and OUT-003 ("MUST contain exactly 3-5 key findings bullets"). Per `quality-enforcement.md` Tier Vocabulary, "MUST" is a HARD tier keyword; MEDIUM tier uses "SHOULD." These six rules are internally inconsistent with the tier vocabulary specification.

   **Magnitude assessment:** These six MUST-in-MEDIUM inconsistencies are pre-existing (they appeared in iter1 and were not flagged in the iter1 improvement recommendations). The iter1 report only flagged SEV-003 and PRM-004. This scoring cycle resolves them but does not treat them as a regression. Their impact is lower than the fixed defects because: (a) MEDIUM rules with MUST language tend to be over-enforced rather than under-enforced — the agent will treat them as harder requirements than intended; (b) the practical behavior difference between "MUST" and "SHOULD" in MEDIUM-tier rules is smaller than in HARD-tier rules; (c) all six rules describe clearly correct agent behavior regardless of tier vocabulary. However, they represent a genuine internal inconsistency against the quality-enforcement.md tier vocabulary specification.

**Improvement Path:**
For each of the 6 MUST-in-MEDIUM rules, either (a) upgrade to HARD tier if the consequence warrants it, or (b) change "MUST" to "SHOULD" to align with MEDIUM tier vocabulary. Based on the consequences documented:
- MOT-006 and ABL-006: threshold judgments are required for the elimination algorithm — consider upgrading to HARD
- PRM-005, ALG-005, INT-006, OUT-003: these are recommendations with documented consequences — "SHOULD" is more appropriate

---

### Methodological Rigor (0.97/1.00)

**Evidence for score:**
The Fogg (2009) DOI (10.1145/1541948.1541999) is cited at the document header and in section blockquotes. The three primary structural elements — convergence model, elimination algorithm, intervention difficulty gradient — are each grounded in specific Fogg citations with chapter numbers. BMAP-004 cites Fogg (2020) Chapters 14-15 for the behavior statement format (consistent with the agent definition). ABL section cites Fogg (2009) Section 4: "Simplicity as a Function of a Person's Scarcest Resource." PRM section cites Fogg (2009) Section 5: "Triggers." ALG section cites Fogg (2020) Chapters 2-3 for intervention difficulty ordering.

The limiting factor principle is correctly stated: "Improving any factor except the limiting one does not raise overall ability above the action threshold" — accurately reflecting Fogg's scarcest resource concept. The convergence_timing edge case (ALG-004) correctly requires all three factors to score 4+ before the classification is applied, preventing misuse as a fallback. The severity classification section correctly discloses its heuristic nature.

The action-line position is now formally enforced (OUT-004), which strengthens methodological rigor by ensuring the B=MAP motivation-ability plane is always represented in the output. PRM-004 (timing assessment relative to action-line) correctly uses "SHOULD" (MEDIUM), acknowledging that timing assessment relative to the action line is best practice but may not always be directly observable.

**Remaining minor gaps:**

1. **The convergence_timing edge case description (line 202) partially overlaps with ALG-004 (line 211) but the algorithm narrative does not cite ALG-004.** ALG-004 is the HARD enforcement rule for convergence_timing. The narrative description at Step 4 is consistent with ALG-004, but the algorithm procedure text does not cross-reference the rule. This is cosmetic; the rigor is present.

**No new methodological gaps introduced by the revision.**

---

### Evidence Quality (0.96/1.00)

**Evidence for score:**
All five evidence quality defects from iter1 are resolved:
- CLS-001–005 now have consequence documentation — the "why this rule matters" evidence chain is complete for all 53 rules
- MOT-005 cites P-001 and Fogg (2020) for the score cap rule
- CLS-004 cites synthesis-validation.md (v1.1.0) for the minimum-confidence aggregation rule
- SEV-003's consequence accurately represents what failure looks like
- QG-001 cites ORCHESTRATION.yaml for the C4 threshold

Primary methodology citations are well-formed and specific. The severity classification section honestly discloses that "10% and 50% thresholds are calibration anchors... not empirically validated benchmarks." The confidence classification section cites synthesis-validation.md v1.1.0 with specific section names.

**Remaining minor gaps:**

1. **Template file existence not verified.** OUT-001 references `skills/ux-behavior-design/templates/bmap-diagnosis-template.md` (v1.2.0). The Related Files table also references this file. This reference was present in iter1 and was noted as a gap; it was not in the 7 priority improvements. The file cannot be confirmed to exist from within the rules file itself. However, both the agent definition and SKILL.md also reference this template, suggesting it is a genuine artifact rather than a phantom reference. The risk is low but the gap persists. The Related Files table honestly documents the version (v1.2.0) which implies it exists.

2. **mcp-coordination.md remains listed as "unversioned — tracked via git history."** This was flagged in iter1 as a traceability gap. Unlike wave-progression.md (which now shows v1.2.0), the mcp-coordination.md entry explicitly acknowledges it has no version number. The acknowledgment ("tracked via git history") is honest per P-022 but weakens evidence quality slightly.

Neither gap is a regression; both were present in iter1. Their collective impact at the evidence quality level is minor.

---

### Actionability (0.95/1.00)

**Evidence for score:**
The 18-item self-review checklist is specific and maps to rule IDs. The intervention discipline rules are highly specific: INT-001 mandates "3-5 specific intervention recommendations," INT-002 mandates 6 specific fields per intervention, INT-003 mandates prioritization order, INT-004 mandates LOW confidence on ALL interventions. These give implementers unambiguous criteria. The quality gate section gives concrete per-S-014-dimension evaluation criteria.

SEV-003 consequence rewrite is effective — "Inconsistent severity classification when operating qualitatively; teams cannot prioritize behavioral issues without a systematic severity estimate" directly tells an agent what goes wrong if the rule is not followed.

The intervention category matrix is comprehensive and specific, mapping each bottleneck type to concrete example interventions with effort estimates. The degraded mode disclosure requirements (OUT-007, ABL-005) are specific: "MUST appear immediately after the document header" (not just "somewhere in the document").

**Remaining minor gaps:**

1. **Self-review checklist missing action-line position item.** As documented under Completeness, the checklist does not include a check for the action-line position statement that OUT-004 now requires. An agent conducting S-010 self-review will not verify this specific output element. The OUT-004 rule itself is actionable; the checklist gap reduces the self-review coverage slightly.

2. **ALG-005 consequence is brief.** "Unordered multiple bottleneck recommendations leave teams without a starting point" is present and improved from prior versions, but remains terse compared to the detailed consequences in HARD rules. It does not specify which specific output element would be malformed. This was present in iter1 and was not in the 7 priority improvements — not a regression.

**Improvement Path:**
Add action-line position to self-review checklist (see Completeness improvement path). This single addition closes both the Completeness and Actionability gaps.

---

### Traceability (0.97/1.00)

**Evidence for score:**
The QG-001 C4 threshold now traces to PROJ-022 ORCHESTRATION.yaml. The wave-progression.md version conflict is resolved (both the rules file and agent definition now agree on v1.2.0). MOT-005 and CLS-004 now have source citations, closing the two largest traceability gaps in the evidence quality dimension. The document header VERSION comment cites all source files with versions. The footer traceability comment cites PROJ-022 EPIC-004, all governance standards, and the ORCHESTRATION.yaml. Rule ID patterns map 1:1 to section prefixes (BMAP/MOT/ABL/PRM/ALG/INT/SEV/CLS/OUT/QG), providing consistent cross-referencing.

**Remaining minor gaps:**

1. **mcp-coordination.md listed as "unversioned — tracked via git history."** This was present in iter1. The honest disclosure is correct per P-022 but does not constitute a full traceability chain — a reader cannot pin the rules file to a specific version of mcp-coordination.md.

2. **Self-review checklist items do not cross-reference all OUT rules.** Checklist item 16 references H-23 (navigation). Checklist item 18 references OUT-006 (handoff data). But checklist items 1-15 reference only non-OUT rules. OUT-001 (all 8 sections present), OUT-002 (navigation), OUT-003 (3-5 key findings), OUT-004 (scoring tables including action-line), OUT-005 (algorithm trace), and OUT-007 (degraded mode banner) are not individually traced in the checklist. OUT-004 specifically is not traceable from the checklist even though it now has a new requirement. This creates a minor traceability gap between the rule set and the verification mechanism.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness + Actionability | 0.93 / 0.95 | 0.96 | Add checklist item between items 8 and 9: "Action-line position statement present in Behavior State Map (above/below action line; factor(s) needed to change) \| OUT-004". This single item closes the checklist gap introduced by the OUT-004 fix. |
| 2 | Internal Consistency | 0.95 | 0.97 | Review 6 remaining MUST-in-MEDIUM rules (MOT-006, ABL-006, PRM-005, ALG-005, INT-006, OUT-003). For each: either upgrade to HARD (if violation consequence warrants enforcement) or change "MUST" to "SHOULD" (if MEDIUM guidance is the intent). MOT-006 and ABL-006 are candidates for HARD because threshold judgments feed the elimination algorithm. |
| 3 | Evidence Quality | 0.96 | 0.97 | Verify bmap-diagnosis-template.md exists at the cited path. If it does not exist, add a note: "(planned artifact; will be created during Wave 4 Phase 2 implementation)". If it exists, no action needed. |
| 4 | Traceability | 0.97 | 0.98 | Add version or commit reference to mcp-coordination.md in the Related Files table, or update the note from "unversioned -- tracked via git history" to include the specific commit hash or date of last known version. |

---

## Regression Check

The following potential regressions introduced by the iter2 revision were investigated:

| Potential Regression | Investigation Result | Verdict |
|---------------------|---------------------|---------|
| SEV-003 consequence rewrite: did changing from feature-description to violation-consequence alter the meaning? | New consequence ("Inconsistent severity classification when operating qualitatively; teams cannot prioritize behavioral issues without a systematic severity estimate") accurately represents the consequence of not following the SHOULD guidance. No meaning lost. | No regression |
| PRM-004 language change from MUST to SHOULD: does this weaken an important enforcement? | PRM-004 governs timing assessment relative to the action line. Changing to SHOULD acknowledges that timing can only be directly assessed when behavioral data is available; in Qualitative Assessment Mode it is advisory. The change is methodologically sound. | No regression |
| SEV-003 language change from MUST to SHOULD: does this weaken severity discipline? | SEV-003 governs qualitative severity estimation from factor scores. Changing to SHOULD acknowledges this is guidance for cases where conversion data is unavailable. SEV-001 (HARD) still mandates severity classification; SEV-003 (MEDIUM, SHOULD) provides the qualitative estimation guidance. The enforcement hierarchy is intact. | No regression |
| OUT-004 amendment: does the new action-line requirement create inconsistency with checklist? | The checklist was not updated to include the action-line position check. This is a minor incompleteness, not a logical contradiction. No inconsistency created. | Minor gap, not regression |
| Wave-progression.md version change (unversioned -> v1.2.0): does this match reality? | The agent definition references v1.2.0. The SKILL.md v1.5.0 references this file without a version pin. The change from "unversioned" to "v1.2.0" is an improvement that resolves the iter1 inconsistency. | No regression |
| CLS consequence column addition: were the consequences correctly attributed to the right rules? | CLS-001: P-022 violation for missing classification — correct. CLS-002: MEDIUM/HIGH intervention misleads teams — correct. CLS-003: HIGH without quantitative data — correct. CLS-004: minimum-confidence aggregation — correct. CLS-005: estimated severity at MEDIUM — correct. | No regression |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific line-number references
- [x] Uncertain scores resolved downward: Completeness scored 0.93 (not 0.95) due to self-review checklist gap
- [x] First-draft calibration considered — this is iteration 2; scored against 0.95 C4 benchmark
- [x] No dimension scored above 0.97 without exceptional evidence
- [x] Regression check performed independently of forward scoring
- [x] Pre-existing gaps distinguished from newly introduced gaps

**Anti-leniency decisions made:**
- Completeness held at 0.93 (not 0.95+) because the OUT-004 fix introduced a corresponding self-review checklist gap that the revision did not close. This is a real omission directly traceable to the iter2 change.
- Internal Consistency held at 0.95 (not 0.97) because 6 MUST-in-MEDIUM rules persist. While these are pre-existing (not regressions), they are genuine internal inconsistencies against the tier vocabulary specification documented in quality-enforcement.md. They cannot be dismissed simply because they were not in the iter1 priority list.
- Evidence Quality scored 0.96 (not 0.98) because the template file existence and mcp-coordination.md versioning gaps persist. The iter2 revision did not address these, and they represent verifiable evidence chain weaknesses.

**Composite calculation:**
(0.93 * 0.20) + (0.95 * 0.20) + (0.97 * 0.20) + (0.96 * 0.15) + (0.95 * 0.15) + (0.97 * 0.10)
= 0.186 + 0.190 + 0.194 + 0.144 + 0.143 + 0.097
= 0.954

---

## Session Context Handoff

```yaml
verdict: PASS
composite_score: 0.954
threshold: 0.95
weakest_dimension: completeness
weakest_score: 0.93
critical_findings_count: 0
iteration: 2
delta_from_prior: +0.061
improvement_recommendations:
  - "Add action-line position to self-review checklist between items 8 and 9 (OUT-004)"
  - "Review 6 MUST-in-MEDIUM rules: MOT-006, ABL-006, PRM-005, ALG-005, INT-006, OUT-003 — upgrade to HARD or change to SHOULD"
  - "Verify bmap-diagnosis-template.md exists at cited path (v1.2.0)"
  - "Add version or commit reference to mcp-coordination.md in Related Files table"
```

---

*Score Report Version: 1.0.0*
*Scored by: adv-scorer (S-014 LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-behavior-design/rules/fogg-behavior-rules.md` v1.1.0*
*Context files reviewed: rules-iter1-score.md (prior score), SKILL.md v1.5.0, ux-behavior-diagnostician.md v1.2.0, quality-enforcement.md v1.6.0*
*Created: 2026-03-04*
