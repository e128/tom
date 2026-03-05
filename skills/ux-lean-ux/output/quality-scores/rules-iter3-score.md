# Quality Score Report: lean-ux-methodology-rules.md (Iteration 3)

## L0 Executive Summary

**Score:** 0.958/1.00 | **Verdict:** PASS | **Weakest Dimension:** Evidence Quality (0.94)
**One-line assessment:** Iteration 3 closes all three iter2 gaps — ASM-008 severity-absent fallback added with MEDIUM-confidence documentation requirement, ICE attribution expanded to an explicit "no canonical primary source" statement with practitioner-channel clarification, and Related Files version pinning completed for versioned files and explicitly acknowledged for unversioned files — elevating the composite above the 0.95 C4 threshold.

---

## Scoring Context

- **Deliverable:** `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md`
- **Deliverable Type:** Methodology Rules File (sub-skill operational constraints)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (C4, user-specified)
- **Prior Scores:** iter1: 0.862, iter2: 0.942
- **Cross-references verified:** `skills/ux-lean-ux/SKILL.md` (v1.2.0), `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` (v1.1.0), `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.governance.yaml` (v1.1.0), `skills/user-experience/rules/synthesis-validation.md`
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.958 |
| **Threshold** | 0.95 (C4, user-specified) |
| **Verdict** | PASS |
| **Strategy Findings Incorporated** | No (standalone scoring) |
| **Delta to Threshold** | +0.008 |
| **Delta from iter2** | +0.016 |
| **Delta from iter1** | +0.096 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.97 | 0.194 | All 8 rule families present with full coverage; ASM-008 fills the final upstream-data-without-severity gap; navigation table complete; no missing sections |
| Internal Consistency | 0.20 | 0.96 | 0.192 | VLD-008 correctly cross-referenced in checklist item 14; QG-001 acknowledges C4 threshold; lifecycle table minor format issue remains but does not break functional consistency |
| Methodological Rigor | 0.20 | 0.97 | 0.194 | EXP-007 residual case present; EXP-003 HARD; ASM-008 correctly classified MEDIUM (fallback rule, not core enforcement); decision path exhaustive; no methodology errors found |
| Evidence Quality | 0.15 | 0.94 | 0.141 | ICE attribution note now explicitly states "No peer-reviewed citation available" with practitioner-channel disclosure; Croll Ch.10 present; BML-004 Ch.6 present; community-origin URL still absent but disclosure is sufficient at this level |
| Actionability | 0.15 | 0.96 | 0.144 | ASM-008 closes the upstream-data fallback gap with a concrete action (treat as Q1 Known-Uncertain, document as MEDIUM confidence); ICE-005 calibration example and QG-002 denominator mechanics both present |
| Traceability | 0.10 | 0.95 | 0.095 | Related Files section with governance YAML v1.1.0 pinned; unversioned files explicitly acknowledged with "tracked via git history" notation; wave-progression.md and synthesis-validation.md both referenced; footer traceability block complete |
| **TOTAL** | **1.00** | | **0.958** | |

---

## Detailed Dimension Analysis

### Completeness (0.97/1.00)

**Evidence:**

The rules file addresses all eight required operational areas with full content coverage:

1. **Build-Measure-Learn Cycle Rules** (BML-001 through BML-006): 5-step sequence, mandatory rules, partial scope table with 5 valid values, cycle termination conditions, error behavior for invalid Cycle Scope values (BML-003). Complete and error-defensive.
2. **Hypothesis Format Validation Rules** (HYP-001 through HYP-006): 4-component canonical format, lifecycle state transition table, validation discipline. Complete.
3. **Assumption Mapping Rules** (ASM-001 through ASM-008): Quadrant definitions, boundary criteria, assumption category classification, mapping discipline, upstream data integration rules (ASM-007), and now a severity-absent fallback (ASM-008). Complete.
4. **Experiment Type Selection Rules** (EXP-001 through EXP-007): 7-type matrix, exhaustive decision path with priority 7 residual case, selection discipline. Complete.
5. **ICE Scoring Rules** (ICE-001 through ICE-007): Three-dimension scale anchors with calibration examples, composite formula, tiebreaking, scoring discipline. Complete.
6. **Validated Learning Documentation Rules** (VLD-001 through VLD-008): Learning entry format, required fields, evidence quality standard, decision criteria, handoff filtering rule. Complete.
7. **Confidence Classification Rules** (CLS-001 through CLS-005): Three-tier classification, judgment type table, Lean UX confidence dynamics. Complete.
8. **Quality Gate Integration** (QG-001 through QG-004): S-014 dimension mapping, partial scope denominator mechanics, scoring discipline. Complete.

Navigation table: all 10 sections listed with correct anchor links (H-23 compliant).

ASM-008 (line 174) fills the final completeness gap from iter2: "When upstream heuristic evaluation findings are provided WITHOUT severity ratings, treat ALL such findings as severity-unknown and place them in Q1 (Known-Uncertain) for manual triage."

**Gaps:**

No material completeness gaps remain. The Wave 1 prerequisite is mentioned both in BML-001's context block (line 30) and the Related Files trailing note (line 455). A slightly more prominent Wave 1 gate in the BML section introduction would marginally strengthen completeness, but this is a cosmetic improvement at this point.

**Improvement Path:**

The 0.97 score reflects genuinely complete content. The remaining 0.03 gap is attributable to the Wave 1 prerequisite placement being in a subsidiary note rather than a dedicated rule entry — not worth a revision cycle at this quality level.

---

### Internal Consistency (0.96/1.00)

**Evidence:**

Rule IDs are unique and sequential across all 8 families: BML (001-006), HYP (001-006), ASM (001-008), EXP (001-007), ICE (001-007), VLD (001-008), CLS (001-005), QG (001-004). No duplicates, no gaps.

Cross-references are accurate and bidirectional where relevant:
- Checklist item 14 (line 478) cites VLD-008, which is now the formalized rule for handoff filtering. This resolves the iter1/iter2 "Handoff threshold rule" inconsistency completely.
- QG-001 (line 433) explicitly acknowledges the C4 threshold: "At C4 criticality (e.g., user-specified or auto-escalated), the threshold is >= 0.95." Consistent with governance YAML field `quality_threshold: 0.95`.
- BML-005 and ICE-007 both address PIVOT hypothesis scoring, and checklist item 15 correctly cross-cites both. Consistent.
- ASM-008 (severity-absent fallback) is MEDIUM tier and its consequence statement is consistent with ASM-003 (uncertain between quadrants, prefer higher-risk). The Q1 treatment for severity-unknown findings is internally consistent with the Q1 "test first" priority. No contradictions introduced.
- ICE-004 (Confidence MUST NOT exceed 5 without methodology-grounded evidence) is consistent with the Confidence scale anchor table where scores 6-7 require "User research findings, heuristic evaluation severity >= 2 findings." The threshold boundary is coherent.

**Gaps:**

The lifecycle state transition table (line 116) row "Any → -- | No backward transitions (VALIDATED/INVALIDATED are terminal) | --" has an empty Required Evidence field. This minor format inconsistency (all other rows have non-empty Required Evidence) was noted in iter1 and has not been addressed. It does not break functional understanding but is a formatting inconsistency in an otherwise rigorous document. At 0.96, this is the remaining 0.04 gap.

**Improvement Path:**

The lifecycle table row for terminal state enforcement could add "N/A -- terminal state" in the Required Evidence column to match the format of all other rows. This is a single-cell fix.

---

### Methodological Rigor (0.97/1.00)

**Evidence:**

The methodology correctly implements canonical Lean UX across all operational domains:

- **Hypothesis format**: "We believe [outcome] for [users] if [change] because [evidence]" matches Gothelf & Seiden (2021) Chapter 3 canonical format. Validation criteria are specific and rejection criteria are concrete.
- **4-quadrant assumption mapping**: Q1 (Unknown + High Risk) through Q4 (Unknown + Low Risk) axes correctly implemented. Boundary criteria use observable, measurable thresholds ("> 1 sprint of effort to recover" for HIGH risk; "directly evidence exists" for KNOWN).
- **Experiment selection decision path**: 7 priorities including residual case EXP-007 (Priority 7) for partial-match scenarios. The decision path is now exhaustive — no hypothesis can fall through without an experiment type assignment. EXP-003 escalated to HARD tier appropriately given Q1 assumption criticality.
- **ICE formula**: (Impact + Confidence + Ease) / 3 correctly implemented. Tiebreaking by assumption quadrant (Q1 > Q2 > Q4 > Q3) is methodologically sound.
- **PIVOT/PERSEVERE/KILL framework**: Decision criteria include required evidence types, not just definitions. VLD-003 through VLD-005 enforce logical consistency between result and decision fields.
- **Confidence dynamics**: Pre-experiment outputs are correctly designated MEDIUM (hypotheses as testable propositions, not validated conclusions). HIGH requires convergence with a second framework. This is an accurate representation of Lean UX epistemological design.
- **ASM-008 treatment**: Treating severity-unknown findings as severity-unknown and routing to Q1 for manual triage is methodologically correct — it errs toward over-testing rather than under-testing, consistent with ASM-003's higher-risk tie-breaking rule and the Lean UX principle of testing riskiest unknowns first.

**Gaps:**

A minor observation: BML-004's 4-week flag cites Gothelf & Seiden (2021) Chapter 6 "MVPs and Experiments" but the chapter title as cited ("MVPs and Experiments") should be verified against the actual table of contents. This is a citation precision question, not a methodological error. The 4-week threshold itself is defensible as a practitioner outer bound for tiny teams. This accounts for the remaining 0.03 gap.

**Improvement Path:**

Verify BML-004 Chapter 6 title against the Gothelf & Seiden (2021) 3rd edition table of contents. No functional revision required.

---

### Evidence Quality (0.94/1.00)

**Evidence:**

Primary source citations are present and specific:
- Gothelf & Seiden (2021) with chapter-level specificity for 4 sections (Chapter 3: Hypotheses, Chapter 4: Assumptions, Chapter 6: MVPs and Experiments, Chapter 7: BML cycle).
- Ries (2011) Chapter 7 "Measure" — specific.
- Croll & Yoskovitz (2013) Chapter 10: "Deciding What to Build" — specific (added in iter2, retained in iter3).
- Sean Ellis / GrowthHackers ICE framework attribution (line 226, lines 230-232): The attribution note now reads: "No canonical primary source exists for the ICE scoring framework; it is attributed to Sean Ellis through practitioner channels (GrowthHackers.com community, circa 2015). No peer-reviewed citation is available." This is an honest, complete disclosure of the citation limitation. It explicitly distinguishes the framework origin from the anchor operationalizations ("the specific percentage thresholds ... are author operationalizations adapted from the Sean Ellis / GrowthHackers ICE framework principles for tiny-team Lean UX contexts").

Concrete evidence examples in VLD section are high quality (specific metrics, sample sizes, statistical notation). Unacceptable evidence counterexamples are appropriately illustrative.

**Gaps:**

The ICE attribution disclosure is now functionally complete — it states "No peer-reviewed citation available" and "No canonical primary source exists." The only remaining gap is the absence of a specific URL (e.g., `https://growthhackers.com/articles/ice-scoring` or similar) to the community resource where ICE scoring was first formalized. The iter2 score report recommended adding a specific URL; the iter3 revision addressed the citation disclosure but stopped short of providing a URL.

At C4 scrutiny, the absence of a URL when one is potentially available is a minor evidence gap — the current text is honest and complete about the limitation, which is the primary standard. The difference between 0.94 and 0.96 here hinges entirely on whether a live URL to the GrowthHackers community resource is provided. Given that the URL may not be verifiable without live web access, and that the current disclosure is explicit about the community origin and limitation, 0.94 is the appropriate score. This is not a functional defect.

**Improvement Path:**

If a specific, verifiable URL to the GrowthHackers ICE scoring community resource is available, add it to the attribution note. This would raise Evidence Quality to approximately 0.96. Not required for PASS at the 0.95 composite threshold.

---

### Actionability (0.96/1.00)

**Evidence:**

ASM-008 (line 174) directly closes the iter2 actionability gap:

> "When upstream heuristic evaluation findings are provided WITHOUT severity ratings, treat ALL such findings as severity-unknown and place them in Q1 (Known-Uncertain) for manual triage. Document the missing severity as a MEDIUM confidence judgment in the Synthesis Judgments Summary. Consequence: unrated findings are not silently dropped, and the assumption map explicitly surfaces the severity gap for human review."

This gives the agent a concrete, unambiguous action sequence: (1) classify as severity-unknown, (2) place in Q1, (3) document as MEDIUM confidence in Synthesis Judgments Summary. Three specific steps, no undefined judgment required.

Other actionability strengths confirmed in iter3:
- ICE-005 calibration example (lines 287): "A Concierge MVP requiring 2 weeks of manual service delivery scores Ease 4-5 for a 3-person team (moderate coordination) but Ease 2-3 for a 1-person team." Concrete and computable.
- QG-002 denominator mechanics (lines 434): Examples provided for `hypothesis-generation` (2-step denominator) and `experiment-design` (4-step denominator). Computable without agent interpretation.
- EXP-002 success criteria requirement with example: "checkout completion rate increases by >= 10% over control." Unambiguous.
- Self-review checklist: 15 binary pass/fail items, each with rule ID citation. Operationalizable.

**Gaps:**

ICE-005 is classified MEDIUM (SHOULD NOT) rather than HARD (MUST). The rule is actionable in that it provides a calibration example, but an agent could technically comply with the literal rule tier by ignoring the example. At 0.96, this is a philosophical gap (SHOULD vs. MUST for team-size calibration) rather than a functional ambiguity.

**Improvement Path:**

Consider escalating ICE-005 to HARD if systematic miscalibration of Ease scores is observed in practice. Not required for PASS.

---

### Traceability (0.95/1.00)

**Evidence:**

The Related Files section (lines 440-453) now provides a complete dependency matrix:

| File | Version pinning status |
|------|----------------------|
| `skills/ux-lean-ux/SKILL.md` | v1.2.0 — pinned |
| `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` | v1.1.0 — pinned |
| `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.governance.yaml` | v1.1.0 — pinned (iter3 fix) |
| `skills/user-experience/rules/wave-progression.md` | "unversioned -- tracked via git history" — explicitly acknowledged |
| `skills/user-experience/rules/synthesis-validation.md` | v1.1.0 — pinned |
| `skills/user-experience/rules/mcp-coordination.md` | "unversioned -- tracked via git history" — explicitly acknowledged |
| `skills/ux-lean-ux/templates/` | "--" — no semantic version applicable |
| `.context/rules/quality-enforcement.md` | "--" — framework-level file; version tracked by framework versioning |

The governance YAML version (v1.1.0) is now correctly pinned in the Related Files table, matching the `version: 1.1.0` field at line 5 of the governance YAML. This was the primary traceability gap in iter2.

The "unversioned -- tracked via git history" notation for wave-progression.md and mcp-coordination.md is an honest, actionable acknowledgment: it tells the reader exactly how to check for changes (git history) and confirms the author verified these files do not carry semantic versions.

Footer traceability block (line 491) includes PROJ-022, EPIC-002, FEAT-009, methodology sources, and the ORCHESTRATION.yaml reference.

Per-section `> **Source:**` annotations provide forward traceability from rules to methodology origins.

**Gaps:**

The quality-enforcement.md and templates entries in Related Files show "--" in the Version column without an explanatory note. While reasonable (framework-level files are not version-pinned individually; templates directory has no semantic version), a brief note ("framework-level versioning" or "no semantic version") matching the pattern used for wave-progression.md would achieve uniform traceability documentation. This accounts for the remaining 0.05 gap from a perfect 1.00.

**Improvement Path:**

Add brief notes to quality-enforcement.md and templates entries in Related Files (e.g., "framework-managed" for quality-enforcement.md; "templates evolve with rule revisions" for templates directory). Cosmetic refinement, not required for PASS.

---

## Verification: iter2 Gap Resolution

| iter2 Gap | Status | Evidence |
|-----------|--------|----------|
| ASM-008 severity-absent fallback | RESOLVED | Line 174: rule present with Q1 routing, MEDIUM confidence documentation, and consequence statement |
| ICE attribution clarification | RESOLVED | Lines 230-232: explicit "No canonical primary source exists; no peer-reviewed citation available" statement with practitioner-channel disclosure |
| Related Files version pinning (governance YAML) | RESOLVED | Line 448: `version: v1.1.0` pinned; unversioned files acknowledged with "tracked via git history" |

All three iter2 blockers resolved. No new gaps introduced in iter3 revision.

---

## Gaps Remaining (per dimension below 1.00)

### Evidence Quality — 0.94

- **Gap:** ICE attribution disclosure is honest and complete but lacks a specific URL to the GrowthHackers community resource where ICE scoring was formalized. The text correctly states "No peer-reviewed citation available" and "attributed to Sean Ellis through practitioner channels (GrowthHackers.com community, circa 2015)" — this is the best available attribution for a community-origin framework. The absence of a live URL is a minor gap rather than a functional defect.
- **Fix (optional):** If verifiable, add `https://growthhackers.com/articles/ice-scoring` or equivalent URL. Not required for PASS.

### Internal Consistency — 0.96

- **Gap:** Lifecycle state transition table row for terminal states shows empty Required Evidence field ("--") while all other rows have populated Required Evidence. Minor formatting inconsistency.
- **Fix (optional):** Replace "--" with "N/A -- terminal state (no evidence required for state enforcement)" in the Required Evidence column.

### Traceability — 0.95

- **Gap:** quality-enforcement.md and templates entries in Related Files Version column show "--" without a brief explanatory note, unlike wave-progression.md and mcp-coordination.md which have "unversioned -- tracked via git history."
- **Fix (optional):** Add "framework-managed" note to quality-enforcement.md entry and "co-versioned with rules file" or similar to templates entry.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.94 | 0.96 | Add specific URL to GrowthHackers ICE scoring resource to the ICE attribution note, or confirm URL is not verifiable and leave current disclosure as-is. Current disclosure is sufficient for PASS. |
| 2 | Internal Consistency | 0.96 | 0.97 | Add "N/A -- terminal state" to Required Evidence column of the lifecycle table terminal state row. Single-cell fix. |
| 3 | Traceability | 0.95 | 0.97 | Add brief explanatory notes to quality-enforcement.md and templates entries in Related Files Version column to match the documentation pattern used for unversioned files. |

Note: None of these recommendations are required for PASS. They represent cosmetic precision improvements for a future polish pass if desired.

---

## Iteration History

| Iter | Score | Delta | Key Changes |
|------|-------|-------|-------------|
| 1 | 0.862 | — | Initial |
| 2 | 0.942 | +0.080 | BML-003 invalid scope error behavior; Related Files section with full dependency matrix; VLD-008 formalized; QG-001 C4 threshold; BML-004 Ch.6 citation; Croll Ch.10 citation; ICE attribution note; EXP-007 residual case; EXP-003 HARD escalation; ICE-005 calibration example; QG-002 denominator mechanics; wave-progression.md referenced; SKILL.md version pinned |
| 3 | 0.958 | +0.016 | ASM-008 severity-absent fallback rule (MEDIUM tier, Q1 routing); ICE attribution expanded to explicit "No canonical primary source exists; no peer-reviewed citation available"; governance YAML pinned to v1.1.0 in Related Files; unversioned files acknowledged with "tracked via git history" notation |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score with specific line references from the deliverable
- [x] Uncertain scores resolved downward: Evidence Quality uncertain between 0.94-0.96 — held at 0.94 because the GrowthHackers URL is still absent; Traceability uncertain between 0.95-0.96 — held at 0.95 because quality-enforcement.md and templates entries lack explanatory notes matching the documented unversioned-file pattern
- [x] Calibration check: 0.958 composite correctly maps to PASS (>= 0.95); gap is real but narrow (+0.008 above threshold)
- [x] No dimension scored above 0.97 without specific documented justification
- [x] Completeness and Methodological Rigor at 0.97: both justified — ASM-008 fills the last substantive completeness gap; all three prior rigor gaps resolved in iter2 and the ASM-008 addition is methodologically sound; no remaining errors in either dimension
- [x] First-draft calibration not applicable (third revision iteration); 0.958 for a rules file after three targeted revision cycles is calibrated correctly (not inflated — three cosmetic gaps remain and are documented; no score reaches 1.00)
- [x] C4 threshold (0.95) applied throughout; deliverable is 0.008 above threshold, which correctly maps to PASS

**Calibration note:** The +0.016 delta from iter2 to iter3 reflects three targeted, surgical fixes to documented gaps. The resulting 0.958 score reflects a genuinely high-quality rules file with only cosmetic defects remaining (URL omission, one empty table cell, two missing version notes). The three remaining gaps are explicitly documented and none blocks operational correctness. A score above 0.96 would require all three cosmetic fixes; the current score correctly places the file at PASS without overstating its perfection.

---

## Session Context Schema

```yaml
verdict: PASS
composite_score: 0.958
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.94
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Optional: add specific GrowthHackers URL to ICE attribution note (not required for PASS)"
  - "Optional: add N/A notation to lifecycle table terminal state row Required Evidence column"
  - "Optional: add explanatory notes to quality-enforcement.md and templates entries in Related Files version column"
```

---

*Score Report: rules-iter3-score.md*
*Deliverable: skills/ux-lean-ux/rules/lean-ux-methodology-rules.md*
*Scoring Agent: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*SSOT: .context/rules/quality-enforcement.md*
*Created: 2026-03-04*
