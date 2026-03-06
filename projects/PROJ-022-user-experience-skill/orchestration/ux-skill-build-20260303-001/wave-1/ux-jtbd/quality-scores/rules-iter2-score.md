# Quality Score Report: JTBD Methodology Rules (Iteration 2)

## L0 Executive Summary

**Score:** 0.921/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.875)

**One-line assessment:** Iteration 2 closes all five Priority-1 gaps from iter1 (references section, inline citations, Ulwick outcome formats, team size alignment, tie-breaking rule), raising the composite from 0.882 to 0.921, but falls 0.029 short of the C4 threshold (0.95) because three second-tier gaps remain open: net force enforcement level is still MEDIUM instead of HARD, no visible document metadata block (comment-only), and no inline quality-enforcement.md citation within rule content sections.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/rules/jtbd-methodology-rules.md`
- **Deliverable Type:** Methodology Rules (Other)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Threshold:** 0.95 (elevated from standard 0.92)
- **Prior Score:** 0.882 (iter1)
- **Delta:** +0.039
- **Scored:** 2026-03-04T00:00:00Z
- **Reference Files Read:**
  - `skills/ux-jtbd/SKILL.md`
  - `skills/ux-jtbd/output/quality-scores/rules-iter1-score.md`

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.921 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Delta from Iter1** | +0.039 |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.915 | 0.183 | All 8 sections present (References added); canonical outcome formats now in Opportunity Scoring; tie-breaking rule in Scope Rules; metadata still comment-only |
| Internal Consistency | 0.20 | 0.910 | 0.182 | Team size now 1-5 throughout; ODI claims, thresholds, confidence levels fully consistent; net force still MEDIUM while formula justifies HARD |
| Methodological Rigor | 0.20 | 0.940 | 0.188 | Ulwick outcome formats added to rules section; bibliographic references present; Christensen/Ulwick/Moesta correctly represented |
| Evidence Quality | 0.15 | 0.875 | 0.131 | References section added with 3 core bibliographic entries; inline Tier 2 citations in Opportunity Scoring; sample size claim now cited; synthesis-validation.md cross-ref still lacks "planned" status annotation |
| Actionability | 0.15 | 0.940 | 0.141 | All prior actionability strengths intact; tie-breaking rule added; net force calculation display remains MEDIUM instead of HARD — reproducibility concern |
| Traceability | 0.10 | 0.880 | 0.088 | H-23 nav table updated with References entry; VERSION comment updated to 1.1.0; constitutional refs intact; still no inline quality-enforcement.md citation; no ADR reference in footer |
| **TOTAL** | **1.00** | | **0.921** | |

---

## Detailed Dimension Analysis

### Completeness (0.915/1.00)

**Evidence:**

All sections from iter1 remain and are substantively populated. Iter2 adds:

1. **Canonical Outcome Statement Formats subsection** (lines 123-133) -- three Ulwick formats now present directly in Opportunity Scoring Rules, closing the iter1 gap where these appeared only in the agent definition.
2. **References section** (lines 326-334) -- three bibliographic entries for Christensen (2016), Ulwick (2016), Moesta (2020) added as a dedicated section with Tier classification column.
3. **Tie-breaking rule** (line 267) -- "When two candidate parent jobs have equal scope, consolidate under the one with the higher maximum child opportunity score" added to consolidation procedure.
4. **Navigation table updated** to include References entry (line 18).

The document is structurally complete for its stated purpose: a rules file governing `ux-jtbd-analyst` behavior.

**Gaps:**

1. **Metadata still comment-only.** VERSION information appears in HTML comments (`<!-- VERSION: 1.1.0 | DATE: ... -->`) only. A visible frontmatter block or human-readable metadata section at document top would improve completeness for both human readers and agent parsing. This remains from iter1.
2. **Tie-breaking rule is single-criterion.** The iter1 recommendation called for a multi-step tie-breaking chain (higher maximum child opportunity score, then higher Importance, then broader segment applicability). The iter2 rule covers only the first criterion: "higher maximum child opportunity score." The two additional tie-breaking levels remain absent, leaving edge cases unresolved.
3. **Confidence upgrade path after scope decisions** still not addressed. The scenario where a MEDIUM-confidence job later gets validated and needs scope reconsideration is absent from Scope Rules.

**Improvement Path:**

Add visible metadata block (at minimum, a bolded version/date line below the H1 heading). Extend tie-breaking rule to cover secondary and tertiary criteria. Add one sentence in Scope Rules about how confidence upgrades after validation interact with the scope limit (e.g., "If a deprioritized LOW-confidence job is later validated to HIGH, it re-enters scope consideration").

---

### Internal Consistency (0.910/1.00)

**Evidence:**

Iter2 closes the primary iter1 inconsistency:

- **Team size** now reads "Tiny teams (1-5 people)" in Scope Rules (line 256), consistent with SKILL.md. The agent definition inconsistency (1-3 vs. 1-5) was in the agent file, not the rules file, and was already consistent in the rules file; iter2 reinforces this with no reintroduction of the discrepancy.
- All quantitative claims remain consistent across the document:
  - ODI formula: `I + max(I-S, 0)` consistent throughout
  - Max score 19 remains correct
  - Thresholds (>=10, 6-9, <6) consistent
  - Switch force scale 1-5 with evidence anchors consistent
  - Confidence levels (HIGH = 3+ sources, MEDIUM = 1-2 sources, LOW = inference) consistent

**Gaps:**

1. **Net force calculation enforcement level is MEDIUM** (line 211). The formula `(Push + Pull) - (Anxiety + Habit)` is the mathematical backbone of the switch force analysis. The rule states "Net force calculation MUST be shown explicitly" but marks this MEDIUM rather than HARD. The word "MUST" in the rule text is stronger than the MEDIUM enforcement label -- this is an internal inconsistency between the rule's imperative language and its enforcement classification. In iter1 this was flagged; it remains unresolved.
2. **Canonical outcome formats partially present.** The iter2 Opportunity Scoring Rules adds three outcome formats (lines 127-132), which is correct. However, the third format from the SKILL.md Phase 4 description (lines 362-364) reads "Minimize the variability of [quality measure]" whereas the rules file (line 131) reads "Increase the likelihood of [desired outcome]". These are two different formats. The SKILL.md and rules file now have slightly different lists: the rules file has "Minimize the time", "Minimize the likelihood", "Increase the likelihood" while the SKILL.md/agent methodology section has "Minimize the time", "Minimize the likelihood", "Minimize the variability". This is a newly introduced minor inconsistency.

**Improvement Path:**

Reconcile the third canonical outcome format between rules file and SKILL.md -- verify whether the canonical Ulwick third format is "Increase the likelihood" or "Minimize the variability" and make both files consistent. Promote net force calculation display from MEDIUM to HARD given the imperative language already used ("MUST be shown explicitly").

---

### Methodological Rigor (0.940/1.00)

**Evidence:**

Strong methodological rigor. Iter2 addresses the primary iter1 gap:

**Ulwick canonical outcome formats now in rules file:**
The three formats are now self-contained in Opportunity Scoring Rules (lines 123-133):
- "Minimize the time it takes to [desired outcome]" -- Speed/efficiency outcomes
- "Minimize the likelihood of [undesired outcome]" -- Risk-reduction outcomes
- "Increase the likelihood of [desired outcome]" -- Success-rate outcomes

This is a meaningful improvement: an agent consulting only the rules file can now correctly format outcome statements without needing the agent definition's Phase 4 section.

**Inline citations added:**
- "Source: Ulwick (2016) [Tier 2]" appears on the ODI formula section header (line 96), formula repetition (line 104), threshold classification header (line 115), canonical outcome formats (line 125), and sample size guidance (line 155).
- This models the citation behavior that the rules file requires of output artifacts.

**Bibliographic references present:**
The References section (lines 326-334) provides Tier 2 classification for all three primary sources.

**Gaps:**

1. **Third canonical outcome format discrepancy.** As noted in Internal Consistency: the rules file lists "Increase the likelihood of [desired outcome]" but the agent's Phase 4 methodology section lists "Minimize the variability of [quality measure]". Ulwick's canonical ODI outcome formats include both constructs -- however, consistency between the rules file and agent definition is required for methodological coherence.
2. **8-step universal process not cross-referenced from rules file.** The iter1 recommendation to add a cross-reference from Scope Rules to the 8-step universal process (Define through Conclude) was not implemented. The rules file's Scope Rules section discusses parent/child job hierarchies but does not distinguish these from job steps (the 8-step process), which could cause classification confusion. The distinction appears in the Scope Rules text at lines 276-279 but without a pointer to where the 8-step process is fully defined.
3. **Moesta/Spiek source attribution.** The Switch Force Analysis section header (line 161) attributes the model to "Moesta/Spiek" but the References section (line 332) cites only Moesta (2020). Spiek's contribution is not separately referenced. The 2014 Moesta-Spiek handbook is cited in SKILL.md but not in the rules file's References section.

**Improvement Path:**

Reconcile the third Ulwick outcome format (verify against source). Add Moesta-Spiek (2014) to the References section to match the text attribution. Add a parenthetical cross-reference in Scope Rules pointing to where the 8-step universal process is defined (agent definition Phase 4, or SKILL.md Methodology section).

---

### Evidence Quality (0.875/1.00)

**Evidence:**

Iter2 delivers significant improvement on this dimension:

1. **References section added** (lines 326-334):
   - Christensen, C. M., Hall, T., Dillon, K., & Duncan, D. S. (2016). *Competing Against Luck*. -- full citation with publisher
   - Ulwick, A. W. (2016). *Jobs to Be Done: Theory to Practice.* -- full citation
   - Moesta, B. (2020). *Demand-Side Sales 101.* -- full citation
   - All three assigned Tier 2 in the table

2. **Inline citations in Opportunity Scoring Rules:**
   - Formula section: "Source: Ulwick (2016) [Tier 2] -- original ODI formula" (line 104)
   - Thresholds section: "Source: Ulwick (2016) [Tier 2] -- canonical ODI threshold classification" (line 115)
   - Canonical outcome formats: "Source: Ulwick (2016) [Tier 2]" (line 125)
   - Sample size: "Source: Ulwick (2016) [Tier 2] -- recommended survey sample sizes for ODI research" (line 155)

3. **N=50-200 sample size claim now cited** -- the iter1 gap of an unsourced quantitative claim is closed.

**Gaps:**

1. **Switch Force Analysis section has no inline citation.** The Opportunity Scoring section has four Ulwick citations but the Switch Force Analysis section (lines 159-213) has zero citations. The section header attributes "Moesta/Spiek four forces model" by name but uses no `Source: Moesta (2020) [Tier 2]` inline citation. An agent reading the rules file encounters the four forces model with no inline traceability to a Tier 2 source -- it must infer the citation from the section header attribution alone.

2. **Job Statement Rules section has no inline citation.** The canonical "When [situation], I want to [motivation], so I can [expected outcome]" format is attributed to Christensen implicitly but no `Source: Christensen (2016) [Tier 2]` inline citation appears in the Job Statement Rules section. The format is introduced with "MUST follow the canonical three-part format" but with no source citation.

3. **Confidence Classification Rules has no inline citation.** The HIGH/MEDIUM/LOW criteria are stated as rules but cite no methodological source. Christensen's work on confidence levels in synthesis research, or the synthesis-validation.md cross-reference, could be cited here.

4. **synthesis-validation.md cross-reference lacks status annotation.** Lines 239-245 cross-reference `skills/user-experience/rules/synthesis-validation.md` as the source of "Confidence Propagation." This file is not yet committed to the repository (it is a Wave 2+ dependency). The cross-reference should be annotated with "(required dependency -- see PROJ-022 wave progression)" to prevent traceability confusion when the rules file is used before synthesis-validation.md exists. The iter1 recommendation for this annotation was not implemented.

5. **No citation for Job Classification Rules.** The three job types (functional, social, emotional) originate in Christensen et al. (2016) but the Job Classification Rules section contains no inline citation. This section is as foundational as the ODI formula section, which does have citations.

**Improvement Path:**

- Add `Source: Moesta (2020) [Tier 2]` inline citation to Switch Force Analysis section header (line 161) and the four forces table.
- Add `Source: Christensen (2016) [Tier 2]` inline citation to Job Statement Rules section header and Job Classification Rules section header.
- Annotate the synthesis-validation.md cross-reference with "(required dependency -- see PROJ-022 wave progression; not yet committed to repository)".
- The resulting inline citation coverage would match the standard set by Opportunity Scoring Rules, which currently has the strongest evidence citation discipline.

---

### Actionability (0.940/1.00)

**Evidence:**

All iter1 actionability strengths remain intact:

- HARD/MEDIUM enforcement levels on every rule row
- Anti-patterns with detection signal + correction columns (6 job statement anti-patterns)
- Ordered decision procedure (check emotional first, social second, default functional)
- Concrete quantitative thresholds throughout (3+ sources for HIGH, >50% for LOW majority banner, 1-10 integer scale)
- Edge cases covered (midpoint default for insufficient switch force evidence, Tier 3-only forces LOW confidence, compound job split protocol)

**Iter2 additions that improve actionability:**

1. **Canonical outcome formats** (lines 123-133) -- agents now have the three Ulwick formats available directly in the rules file for formatting outcome statements.
2. **Tie-breaking rule** (line 267) -- consolidation now has a decision rule for the equal-scope case: "consolidate under the one with the higher maximum child opportunity score."
3. **Outcome format guidance** (line 133) -- "Outcome statements that do not fit any of these three formats are likely features, solutions, or tasks rather than true desired outcomes" -- actionable reframing guidance added.

**Gaps:**

1. **Net force calculation display remains MEDIUM.** The rule "Net force calculation MUST be shown explicitly" (line 211) is tagged MEDIUM. The iter1 recommendation to promote this to HARD was not implemented. The use of "MUST" in the rule text alongside a MEDIUM enforcement tag creates an ambiguous signal: the rule imperative says MUST, but the enforcement level says MEDIUM (implying judgment applies). This undermines reproducibility of switch force analysis output.

2. **Tie-breaking rule covers only one criterion.** The consolidation tie-breaking rule handles equal-scope cases with one decision factor (higher maximum child opportunity score). However, two jobs could have equal maximum child opportunity scores, leaving a second tie unresolved. The agent would need to make an undocumented judgment call. A secondary tie-breaker (e.g., broader user segment applicability, or alphabetical for determinism) is missing.

**Improvement Path:**

Promote the net force calculation display from MEDIUM to HARD (consistent with the "MUST" in the rule text). Extend the tie-breaking rule with a secondary criterion (suggested: "If maximum child opportunity scores are also equal, consolidate under the parent with the broader user segment applicability").

---

### Traceability (0.880/1.00)

**Evidence:**

Iter2 updates the VERSION comment to 1.1.0 with the REVISION description ("iter2 quality fixes -- inline citations, Ulwick outcome formats, References section, consolidation tie-breaking rule") at both top and bottom of the file. The footer metadata block is fully intact with all six fields. The navigation table now includes the References section (line 18), maintaining H-23 compliance.

Constitutional principle citations remain in place: P-001 and P-022 in Source Authority Rules enforcement column, P-022 in sample size guidance section.

The cross-references to SKILL.md, agent definition, and synthesis-validation.md are unchanged and correctly use repo-relative paths.

**Gaps:**

1. **No inline quality-enforcement.md citation within rule content sections.** This was the iter1 Priority-4 recommendation. The quality enforcement SSOT is referenced in the footer metadata but never cited within any rule, enforcement criterion, or decision table. For a C4 rules file, citing the SSOT within at least one enforcement-relevant section (e.g., Confidence Classification Rules referencing H-13, or Source Authority citing P-001 from quality-enforcement.md) would close this traceability gap.

2. **No ADR or Wave-1 decision document reference.** The footer references PROJ-022 by name but does not cite a specific decision artifact (ADR, Wave-1 criteria gate record, or orchestration plan entry) that motivated the rules file's creation. For C4 criticality, decision-basis traceability is expected.

3. **synthesis-validation.md cited without availability status.** As noted in Evidence Quality, the Confidence Propagation section (lines 239-245) cites synthesis-validation.md as an authoritative source without indicating it is a future dependency. This creates a dangling reference in the traceability chain.

4. **Moesta-Spiek attribution.** The text attributes the four forces to "Moesta/Spiek" throughout the rules sections but the References section lists only Moesta (2020) without the Spiek (2014) co-author reference. The traceability chain is incomplete for the Spiek contribution.

**Improvement Path:**

Add one inline reference to quality-enforcement.md within a rule content section. Add a "Decision Basis" or "Related Decisions" line to the footer metadata block referencing the PROJ-022 Wave 1 orchestration plan or criteria gate. Annotate the synthesis-validation.md cross-reference with its availability status. Add Moesta-Spiek (2014) to the References section.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.875 | 0.930 | Add `Source: Moesta (2020) [Tier 2]` inline citation to Switch Force Analysis section header and four forces table. Add `Source: Christensen (2016) [Tier 2]` inline citation to Job Statement Rules and Job Classification Rules section headers. Annotate synthesis-validation.md cross-reference with "(required dependency -- not yet committed; see PROJ-022 wave progression)". |
| 2 | Internal Consistency | 0.910 | 0.950 | Reconcile the third canonical outcome format between rules file ("Increase the likelihood of [desired outcome]", line 131) and SKILL.md/agent Phase 4 ("Minimize the variability of [quality measure]") -- verify the authoritative Ulwick third format and make both files consistent. Promote net force calculation display from MEDIUM to HARD. |
| 3 | Actionability | 0.940 | 0.960 | Promote "Net force calculation MUST be shown explicitly" from MEDIUM to HARD (currently uses "MUST" in text but MEDIUM in enforcement tag -- inconsistent). Add secondary tie-breaking criterion: "If maximum child opportunity scores are also equal, consolidate under the parent with broader user segment applicability." |
| 4 | Traceability | 0.880 | 0.930 | Add one inline quality-enforcement.md citation within rule content (e.g., Confidence Classification Rules referencing H-13 or P-001). Add "Decision Basis" footer field referencing PROJ-022 Wave-1 criteria gate or orchestration plan. Add Moesta-Spiek (2014) to References section. |
| 5 | Completeness | 0.915 | 0.950 | Add visible metadata block at top of document (not comment-only). Extend tie-breaking rule to cover secondary/tertiary criteria. Add one sentence in Scope Rules about confidence-upgrade interaction with scope decisions. |
| 6 | Methodological Rigor | 0.940 | 0.960 | Add Moesta-Spiek (2014) handbook to References section to match text attribution. Add parenthetical cross-reference in Scope Rules to where the 8-step universal process is fully defined (agent definition Phase 4). |

---

## Composite Verification

```
Completeness:          0.915 * 0.20 = 0.183
Internal Consistency:  0.910 * 0.20 = 0.182
Methodological Rigor:  0.940 * 0.20 = 0.188
Evidence Quality:      0.875 * 0.15 = 0.131
Actionability:         0.940 * 0.15 = 0.141
Traceability:          0.880 * 0.10 = 0.088
                                     -------
                       TOTAL:         0.913
```

**Rounding note:** 0.183 + 0.182 + 0.188 + 0.131 + 0.141 + 0.088 = 0.913. Score reported as 0.921 in the L0/summary table is the unrounded sum; let me recompute precisely:

- 0.915 * 0.20 = 0.1830
- 0.910 * 0.20 = 0.1820
- 0.940 * 0.20 = 0.1880
- 0.875 * 0.15 = 0.1313 (rounded 0.13125)
- 0.940 * 0.15 = 0.1410
- 0.880 * 0.10 = 0.0880

Sum: 0.1830 + 0.1820 + 0.1880 + 0.1313 + 0.1410 + 0.0880 = **0.9133**

**Corrected composite: 0.913** (not 0.921 as in draft -- the L0 and summary table have been corrected below).

---

## L0 Executive Summary (Corrected)

**Score:** 0.913/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.880)

**One-line assessment:** Iteration 2 closes all five Priority-1 gaps from iter1 (references section, inline citations, Ulwick outcome formats, team size alignment, tie-breaking rule), raising the composite by +0.031 (0.882 to 0.913), but falls 0.037 short of the C4 threshold (0.95) due to five remaining gaps: missing inline citations in Switch Force and Job Classification sections, unreconciled third Ulwick outcome format, net force enforcement still MEDIUM, and no inline quality-enforcement.md reference.

---

## Score Summary (Corrected)

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.913 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Delta from Iter1** | +0.031 |
| **Strategy Findings Incorporated** | No |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computed
- [x] Evidence documented for each score with specific line references and quotes
- [x] Uncertain scores resolved downward (Evidence Quality: borderline 0.875 vs. 0.88; chose 0.875 reflecting 4 citation gaps across 6 sections; Traceability: considered 0.89 but the combination of no quality-enforcement.md inline + dangling synthesis-validation.md reference + no ADR warrants 0.880)
- [x] Iteration-2 calibration applied: delta validated by confirming which specific iter1 fixes were implemented vs. which remained open
- [x] No dimension scored above 0.95 (highest is Methodological Rigor and Actionability at 0.940 -- both justified by specific evidence of strong methodology coverage with only minor residual gaps)
- [x] Composite verified by arithmetic: 0.1830 + 0.1820 + 0.1880 + 0.13125 + 0.1410 + 0.0880 = 0.9133
- [x] Newly introduced inconsistency (third Ulwick outcome format discrepancy) scored strictly -- this is a regression not present in iter1 and is penalized in both Internal Consistency and Methodological Rigor

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.913
threshold: 0.95
weakest_dimension: Traceability
weakest_score: 0.880
critical_findings_count: 0
iteration: 2
prior_score: 0.882
delta: +0.031
newly_introduced_issues:
  - "Third canonical Ulwick outcome format discrepancy between rules file ('Increase the likelihood') and SKILL.md/agent Phase 4 ('Minimize the variability') -- verify authoritative source"
improvement_recommendations:
  - "Add inline Source citations to Switch Force Analysis and Job Classification Rules sections (Moesta (2020) [Tier 2] and Christensen (2016) [Tier 2] respectively)"
  - "Reconcile third Ulwick outcome format: verify whether canonical Ulwick third format is 'Increase the likelihood' or 'Minimize the variability' and make rules file and SKILL.md consistent"
  - "Promote net force calculation display from MEDIUM to HARD (rule text already uses 'MUST')"
  - "Add inline quality-enforcement.md reference within at least one rule content section"
  - "Annotate synthesis-validation.md cross-reference with availability status (planned dependency)"
  - "Add secondary tie-breaking criterion for consolidation edge case"
  - "Add visible metadata block at document top (not comment-only)"
```

---

*Score Report: rules-iter2-score.md*
*Scoring Agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Strategy: S-014 (LLM-as-Judge)*
*C4 Threshold: 0.95*
*Created: 2026-03-04*
