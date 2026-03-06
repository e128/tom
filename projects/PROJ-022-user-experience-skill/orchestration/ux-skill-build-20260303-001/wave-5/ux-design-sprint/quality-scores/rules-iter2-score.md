# Quality Score Report: Design Sprint 2.0 Methodology Rules

## L0 Executive Summary
**Score:** 0.944/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness / Methodological Rigor / Actionability (tied at 0.94)
**One-line assessment:** Three targeted fixes from iter1 successfully resolved the Internal Consistency error and Evidence Quality citation gap, raising the composite from 0.930 to 0.944 — blocked from the 0.95 C4 threshold by two remaining structural items: SPR-039 MEDIUM tier asymmetry and the absent CRISIS mode synthesis rule.

---

## Scoring Context
- **Deliverable:** `skills/ux-design-sprint/rules/sprint-methodology-rules.md`
- **Deliverable Type:** Methodology Rules (operational constraints file)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 PASS Threshold:** 0.95 (governance source: `ux-sprint-facilitator.governance.yaml` `enforcement.quality_threshold: 0.95`)
- **Reference Pattern:** `skills/ux-behavior-design/rules/fogg-behavior-rules.md` v1.2.0 (scored 0.953 PASS)
- **Prior Score (iter1):** 0.930 REVISE
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.944 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Gap to Threshold** | 0.006 |
| **Delta vs. iter1** | +0.014 |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.94 | 0.188 | Template versioned (v1.0.0 fix applied); CRISIS mode synthesis rule still absent |
| Internal Consistency | 0.20 | 0.95 | 0.190 | SPR-028 "QG-003" -> "SPR-042" fix confirmed; all other cross-checks pass |
| Methodological Rigor | 0.20 | 0.94 | 0.188 | SPR-039 MEDIUM/HARD asymmetry persists; all other structural patterns intact |
| Evidence Quality | 0.15 | 0.95 | 0.1425 | Courtney adoption breadth added to Day 4 source block; all four citations complete |
| Actionability | 0.15 | 0.94 | 0.141 | SPR-039 MEDIUM creates ambiguous format enforcement signal; otherwise operationally dense |
| Traceability | 0.10 | 0.95 | 0.095 | Full traceability chain intact; Courtney Day 4 note strengthens citation traceability |
| **TOTAL** | **1.00** | | **0.944** | |

---

## Fix Verification (iter1 -> iter2)

| Fix | Applied | Evidence |
|-----|---------|----------|
| 1. SPR-028: "per QG-003" -> "per SPR-042" | CONFIRMED | Line 315: "Evidence Quality dimension receives a 0 score per SPR-042" |
| 2. Template version: "unversioned" -> "v1.0.0" | CONFIRMED | Line 437 Related Files: `design-sprint-template.md \| v1.0.0` |
| 3. Courtney adoption breadth note in Day 4 source block | CONFIRMED | Line 206: "practitioner resource (not peer-reviewed); adoption breadth: AJ&Smart has facilitated 400+ design sprints for organizations including Google, LEGO, Lufthansa, and the United Nations (per AJ&Smart published portfolio, self-reported)" |

---

## Detailed Dimension Analysis

### Completeness (0.94/1.00)

**Evidence:**

All 11 sections listed in the navigation table remain complete: Sprint Setup (SPR-001 through SPR-003), Day 1 Map (SPR-004 through SPR-009), Day 2 Sketch (SPR-010 through SPR-014), Day 3 Decide (SPR-015 through SPR-019), Day 4 Test (SPR-020 through SPR-026), Synthesis (SPR-027 through SPR-030), Confidence Classification (SPR-031 through SPR-034), Output Format (SPR-035 through SPR-039), Quality Gate Integration (SPR-040 through SPR-043), Related Files, and Self-Review Checklist (18 items). The Related Files dependency matrix now shows the template version as v1.0.0 (iter1 gap closed). Governance.yaml post_completion_checks (13 verifiable assertions) all map to rules in the file -- no new mismatches introduced by the fixes.

**Gaps:**

1. **CRISIS mode synthesis rule still absent:** The agent definition's Phase 5 Step 7 describes CRISIS mode behavior (priority ranking, quick-win identification). No discrete CRISIS mode discipline rule exists in this rules file — the iter1 Priority 5 recommendation was not applied. The Synthesis Rules section covers degraded mode (SPR-028) and incomplete sprint propagation (SPR-030), but CRISIS mode is a distinct third variant not formalized here. Against the fogg-behavior-rules.md reference pattern, which does not have a CRISIS analog, this represents a coverage gap between the rules file and the agent definition's described behavior.

**Improvement Path:**

- Add a CRISIS Mode subsection under Synthesis Rules (or a SPR-030a rule) formalizing: priority ranking requirement (day-level outputs prioritized over synthesis), quick-win identification flag, and CRISIS disclosure requirement. This closes the coverage gap vs. the agent definition Phase 5 Step 7.

---

### Internal Consistency (0.95/1.00)

**Evidence:**

The iter1 blocking defect is resolved: SPR-028 consequence now reads "per SPR-042" (line 315), correctly referencing the rule that defines Evidence Quality dimension zeroing for undisclosed degraded mode. All cross-file consistency checks from iter1 continue to pass:

1. **Rule IDs vs. governance.yaml post_completion_checks:** All 13 post_completion_checks map to rules in the file. No new rule IDs were added or removed; the mappings remain valid.
2. **Template reference existence and version:** `skills/ux-design-sprint/templates/design-sprint-template.md` exists. Related Files now shows v1.0.0 — no conflict with the template file's own version marker (the template was unversioned at iter1; the rules file now claims v1.0.0 which should be verified if the template itself carries a version marker).
3. **Related Files file versions:** SKILL.md v1.1.0, agent definition v1.0.0, governance YAML v1.0.0 — all unchanged and still consistent with their respective files.
4. **Citation alignment with agent definition:** All four citations (Knapp et al. 2016 ISBN 978-1501121746, Courtney 2019 ajsmart.com, Brown 2009 ISBN 978-0061766084, Nielsen 2000 nngroup.com) remain consistent between rules file and agent definition. The new Courtney adoption breadth text in Day 4 source block matches the agent definition References table wording.
5. **Confidence classification alignment:** synthesis-validation.md assignments (HIGH for Day 4 pattern analysis, MEDIUM for sketch selection) remain aligned with SPR-032 and the Confidence Classification section. Unchanged.
6. **Quality gate threshold:** SPR-040 C4 threshold (0.95) still traces to governance.yaml. Unchanged.

**Gaps:**

- No material gaps remain. Minor theoretical note: the template version "v1.0.0" claim in Related Files should match the template file's own frontmatter version. If the template file lacks a version marker (was truly unversioned at iter1), there is a small risk that v1.0.0 was assigned in the rules file without updating the template file itself. This is not verifiable from the rules file alone and does not constitute a confirmed inconsistency.

**Improvement Path:**

- Verify `skills/ux-design-sprint/templates/design-sprint-template.md` carries a v1.0.0 version marker or VERSION comment to ensure the Related Files claim is internally consistent.

---

### Methodological Rigor (0.94/1.00)

**Evidence:**

Unchanged from iter1. The file follows the structural pattern of fogg-behavior-rules.md v1.2.0 with high fidelity: VERSION header, nav table, section-level `> Source:` blocks with chapter-level citations, Discipline tables with consistent columns (ID | Rule | Tier | Consequence of Violation), Related Files dependency matrix, and Self-Review Checklist with rule references. The three fixes (SPR-028 cross-reference, template versioning, Courtney note) do not modify any methodology content.

All methodology-critical rules remain correctly structured: SPR-011 enforces the fixed four-step sketch sequence; SPR-015/SPR-018 enforce Decider authority with P-020 alignment; SPR-001 requires HMW format with Brown (2009) + Knapp et al. (2016) Chapter 4 citation; SPR-025 cites Nielsen (2000) for the five-user threshold; Day Compression Note correctly explains Courtney (2019) vs. Knapp et al. (2016) format difference.

**Gaps:**

1. **SPR-039 MEDIUM tier asymmetry remains:** SPR-039 classifies storyboard table format compliance as MEDIUM. SPR-016 (storyboard content completeness: 10-16 panels, all 4 required elements) is HARD. This creates a methodological asymmetry where an agent can produce a storyboard with valid content (HARD compliant per SPR-016) but non-standard column format without triggering a HARD rejection. The fogg-behavior-rules.md reference pattern classifies all output scoring-table format rules as HARD. This asymmetry was identified at iter1 (Priority 4) and was not fixed.

**Improvement Path:**

- Promote SPR-039 to HARD. Update consequence to: "Non-standard storyboard format prevents prototype construction traceability and fails SPR-035 (section completeness requires standard format per design-sprint-template.md v1.0.0)."

---

### Evidence Quality (0.95/1.00)

**Evidence:**

The iter1 gap is closed. The Day 4 source block (line 206) now includes the Courtney (2019) credibility qualifier: "practitioner resource (not peer-reviewed); adoption breadth: AJ&Smart has facilitated 400+ design sprints for organizations including Google, LEGO, Lufthansa, and the United Nations (per AJ&Smart published portfolio, self-reported)." This disclosure matches the agent definition References table wording and the self-reported nature of the portfolio claim is appropriately flagged.

All four primary citations have full bibliographic data throughout the file:
- **Knapp et al. (2016):** full authors, title, publisher, ISBN 978-1501121746 in header + source blocks + traceability comment
- **Courtney (2019):** author, practitioner qualification, adoption breadth, URL ajsmart.com in Day 4 source block + header
- **Brown (2009):** full author, title, publisher, ISBN 978-0061766084 in header + source blocks
- **Nielsen (2000):** author, title, journal (Nielsen Norman Group), full URL in Day 4 source block

Internal file version references are credible: synthesis-validation.md v1.1.0, wave-progression.md v1.2.0, mcp-coordination.md explicitly noted as "unversioned -- tracked via git history." No fabricated citations detected.

**Gaps:**

- The Courtney practitioner note appears only in the Day 4 source block. Days 1, 2, and 3 source blocks cite "Courtney (2019): AJ&Smart Day N format" without the practitioner qualification. This means the credibility note is not uniformly applied across all sections where Courtney is cited. Against the 0.95+ rubric ("All claims with credible citations"), the partial placement still represents a partial coverage gap — readers of Day 1, 2, or 3 source blocks in isolation cannot assess Courtney's credibility without reaching Day 4. The gap is minor (the Day 4 note and agent definition both provide the disclosure) but notable.

**Improvement Path:**

- No action required to maintain 0.95. Optionally: add a condensed credibility parenthetical "(AJ&Smart, practitioner, 400+ sprints)" to Day 1-3 source blocks to ensure uniform disclosure. This would raise Evidence Quality toward 0.96-0.97 in iter3 if needed.

---

### Actionability (0.94/1.00)

**Evidence:**

Unchanged from iter1. The file remains operationally dense: 43 numbered rules with explicit HARD/MEDIUM tier and consequence, 9 output section definitions with completeness criteria, 18 self-review checklist items with rule ID references, 6 S-014 dimension mappings with sprint-specific evaluation criteria, and structured handoff preparation rules (SPR-030, SPR-038). No actionability content was modified by the three fixes.

**Gaps:**

1. **SPR-039 MEDIUM ambiguity persists:** As noted under Methodological Rigor, SPR-039's MEDIUM tier means an agent receives no HARD-level enforcement signal for storyboard format non-compliance. The consequence ("Non-standard storyboard format degrades prototype construction traceability") does not provide a clear operational signal that format violations will fail quality gate checks. This reduces the actionability of SPR-039 as an operational constraint: agents may deprioritize format compliance when content completeness (SPR-016 HARD) is satisfied.

**Improvement Path:**

- Promote SPR-039 to HARD as described in Methodological Rigor. This resolves the MEDIUM ambiguity and provides an unambiguous enforcement signal.

---

### Traceability (0.95/1.00)

**Evidence:**

Unchanged from iter1 and strengthened by fix 3. The VERSION header, section-level `> Source:` blocks, sequential rule IDs (SPR-001 through SPR-043 without gaps), Self-Review Checklist rule references, and Related Files dependency matrix remain intact. The new Courtney adoption breadth text in the Day 4 source block strengthens the traceability of that citation: readers can now follow "Courtney (2019)" back to a specific practitioner with documented adoption context. The bottom traceability comment (line 482) references all four methodology sources, PROJ-022 EPIC-005, and governance standards (H-23, H-34, H-13, SR-002, SR-003).

SPR-034's explicit version citation (`synthesis-validation.md v1.1.0 minimum-confidence aggregation rule`) remains the strongest single traceability example in the file — it names the version, file, and specific rule being referenced.

**Gaps:**

- No material gaps. As noted in iter1, the bottom traceability comment does not cite wave-progression.md v1.2.0 explicitly, but this is trivial — it is captured in Related Files.

**Improvement Path:**

- No action required. This dimension meets threshold.

---

## Remaining Blocking Items (iter2 -> iter3)

The composite score is 0.944 — 0.006 below the 0.95 C4 threshold. Two changes would close this gap:

| Priority | Dimension Impact | Item | Fix | Score Delta |
|----------|-----------------|------|-----|-------------|
| 1 | Methodological Rigor (+0.01), Actionability (+0.01) | **SPR-039 tier promotion** | Change `| MEDIUM |` to `| HARD |` in SPR-039 Discipline row. Update consequence: "Non-standard storyboard format prevents prototype construction traceability and fails SPR-035 (section completeness requires standard format per design-sprint-template.md v1.0.0)." | +0.003 composite |
| 2 | Completeness (+0.01) | **CRISIS mode synthesis rule** | Add a CRISIS Mode Synthesis rule (SPR-030a or subsection in Synthesis Rules) formalizing: (a) priority ranking (day-level outputs before synthesis), (b) quick-win identification flag, (c) CRISIS disclosure requirement. Cite agent definition Phase 5 Step 7. | +0.002 composite |

Combined effect: +0.005 composite = 0.949. Close but still 0.001 short.

To definitively reach 0.95, a third micro-improvement also helps:

| Priority | Dimension Impact | Item | Fix | Score Delta |
|----------|-----------------|------|-----|-------------|
| 3 | Evidence Quality (+0.005) | **Uniform Courtney credibility note** | Add condensed parenthetical "(AJ&Smart, practitioner, 400+ sprints facilitated)" to Day 1, Day 2, and Day 3 source blocks where Courtney is cited. | +0.001 composite |

Combined effect of all three: +0.006 composite = 0.950 = PASS threshold (exact).

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Methodological Rigor + Actionability | 0.94 | 0.95 | **Promote SPR-039 to HARD.** Change tier from MEDIUM to HARD in the Output Format Discipline table. Update consequence: "Non-standard storyboard format prevents prototype construction traceability and fails SPR-035 (section completeness requires standard format per design-sprint-template.md v1.0.0)." This resolves the asymmetry with SPR-016 (HARD storyboard content) and aligns with fogg-behavior-rules.md's pattern of HARD output format enforcement. |
| 2 | Completeness | 0.94 | 0.95 | **Add CRISIS mode synthesis rule.** Under Synthesis Rules, add a SPR-030a rule (or a "CRISIS Mode Disclosure" subsection) formalizing the CRISIS mode additions from agent definition Phase 5 Step 7: priority ranking of day-level outputs over full synthesis, quick-win identification flag, and explicit CRISIS disclosure requirement. This closes the coverage gap between the rules file and agent definition. |
| 3 | Evidence Quality | 0.95 | 0.96 | **Add condensed Courtney credibility note to Day 1-3 source blocks.** Days 1, 2, and 3 source blocks cite Courtney (2019) without the practitioner qualification. Add "(AJ&Smart, practitioner, 400+ sprints facilitated)" parenthetical to ensure uniform credibility disclosure across all sections. Only required if items 1 and 2 alone do not reach 0.950; this item provides the closing delta. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score with specific locations (line numbers, rule IDs, section names)
- [x] Uncertain scores resolved downward: Completeness held at 0.94 (not 0.95) due to CRISIS mode gap; Methodological Rigor held at 0.94 (not 0.95) due to SPR-039 MEDIUM asymmetry; Actionability held at 0.94 (not 0.95) for same reason
- [x] All three iter1 fixes verified before applying score adjustments -- no assumed corrections
- [x] No dimension scored above 0.95 without specific evidence: IC scored 0.95 based on resolution of the sole blocking defect with all other cross-checks confirmed passing; Evidence Quality scored 0.95 based on confirmed addition of adoption breadth note with one minor partial-placement qualification noted
- [x] C4 threshold (0.95) actively applied: composite 0.944 < 0.95 = REVISE verdict; the file would PASS the baseline C2+ threshold (0.92) but does not meet the stricter C4 bar
- [x] Calibration check: iter2 score of 0.944 is consistent with a second-iteration deliverable that has closed its primary blocking defects but retains two structural gaps (SPR-039 tier, CRISIS mode rule) — expected range for second-iteration deliverables with targeted fixes is 0.93-0.96

---

## Session Context

```yaml
verdict: REVISE
composite_score: 0.944
threshold: 0.95
weakest_dimension: completeness_methodological_rigor_actionability
weakest_score: 0.94
critical_findings_count: 0
iteration: 2
delta_vs_prior: +0.014
improvement_recommendations:
  - "Promote SPR-039 from MEDIUM to HARD — resolves storyboard format/content tier asymmetry (line 398)"
  - "Add CRISIS mode synthesis rule (SPR-030a) formalizing agent definition Phase 5 Step 7 behavior"
  - "Add condensed Courtney credibility note to Day 1-3 source blocks for uniform disclosure"
```

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Reference Pattern: `skills/ux-behavior-design/rules/fogg-behavior-rules.md` v1.2.0 (scored 0.953 PASS)*
*Prior Score: iter1 = 0.930 REVISE*
*Created: 2026-03-04*
