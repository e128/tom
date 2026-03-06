# Quality Score Report: HEART Methodology Rules

## L0 Executive Summary

**Score:** 0.923/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.88)
**One-line assessment:** Substantially improved from iter1 (0.900 -> 0.923) with all three structural gaps resolved (Workflow Phase Sequencing, Measurement Plan Mode, self-review rule IDs), but two unnamed benchmark citations in the Adoption and Retention worked examples block passage of the 0.95 C4 threshold.

---

## Scoring Context

- **Deliverable:** `skills/ux-heart-metrics/rules/heart-methodology-rules.md`
- **Deliverable Type:** Research (Methodology Rules)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Threshold Override:** 0.95 (user-specified; standard H-13 is 0.92)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2

### Cross-References Verified

| File | Verified |
|------|---------|
| `skills/ux-heart-metrics/SKILL.md` | Yes |
| `skills/ux-heart-metrics/agents/ux-heart-analyst.md` | Yes |
| `skills/ux-heart-metrics/agents/ux-heart-analyst.governance.yaml` | Yes |
| Prior score iter1 (`skills/ux-heart-metrics/output/quality-scores/rules-iter1-score.md`) | Yes |

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.923 |
| **Threshold** | 0.95 (C4 user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Prior Score (iter1)** | 0.900 |
| **Score Delta** | +0.023 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.94 | 0.188 | All 10 rule families present (DS/GD/SI/MS/CR/SE/DF/DL/WF/MP); 64 rules; 14-item self-review checklist with rule IDs |
| Internal Consistency | 0.20 | 0.92 | 0.184 | No logical contradictions; rules file version 1.1.0 vs. SKILL.md version 1.2.0 is a minor coherence gap |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | WF-001 through WF-004 add explicit macro-phase sequencing; MP rules follow condition-action-consequence; DS-001 disambiguation complete |
| Evidence Quality | 0.15 | 0.88 | 0.132 | Bain/Reichheld fix closes iter1 gap; Adoption and Retention worked examples still cite unnamed benchmarks |
| Actionability | 0.15 | 0.94 | 0.141 | Phase Summary table maps input/output/rules per phase; MP output modification table (standard vs. mode behavior columns); 64 rules with consequences |
| Traceability | 0.10 | 0.92 | 0.092 | Self-review checklist now has Rule IDs column; SI-006 cited for Synthesis Judgments Summary is a misattribution; P-020 constitution path absent from All-Five Override |
| **TOTAL** | **1.00** | | **0.923** | |

---

## Detailed Dimension Analysis

### Completeness (0.94/1.00)

**Evidence:**

All 10 rule families are now present and structurally complete. The iter1 gaps are fully resolved:

1. **Workflow Phase Sequencing Rules (WF) — added.** WF-001 through WF-004 provide explicit macro-phase constraints with consequences. WF-001 mandates the Phase 1 through Phase 5 ordering. WF-002 mandates phase completion before next phase begins. WF-003 links Measurement Plan mode detection to Phase 1. WF-004 mandates the internal GSM sequence (3a/3b/3c). The Phase Summary table maps each phase to its input, output, and governing rule sections.

2. **Measurement Plan Mode Rules (MP) — added.** MP-001 through MP-012 cover trigger condition (MP-001 through MP-003), P-022 disclosure with verbatim text (MP-004 through MP-005), output modifications in tabular form (MP-006 through MP-010), and validation closure (MP-011 through MP-012). The trigger-disclosure-modification-validation structure is complete.

3. **Self-Review Checklist — rule IDs added.** The checklist expanded from 13 items to 14 items and now includes a "Rule IDs" column cross-referencing specific rules for each check. Item 14 (WF-001/WF-002 phase ordering) covers the new WF family. Item 8 (MP-004/MP-005/MP-011) covers the new MP family.

Rule count by family: DS(6), GD(6), SI(6), MS(8), CR(4), SE(10), DF(4), DL(4), WF(4), MP(12) = 64 rules total.

**Gaps:**

1. **Self-review item 9 misattributes SI-006.** Item 9 reads "Synthesis Judgments Summary lists each AI judgment call | SI-006 | Missing or empty Synthesis Judgments Summary." SI-006 governs incorporation of upstream sub-skill signals, not the Synthesis Judgments Summary requirement. The correct rule reference would be the Quality Gate Integration section or synthesis-validation.md. This is a minor cross-reference error, not a missing section.

**Improvement Path:**

Correct self-review item 9 Rule IDs from "SI-006" to a reference pointing to `skills/user-experience/rules/synthesis-validation.md [Synthesis Judgments Summary]` or to the Quality Gate Integration table in this file.

---

### Internal Consistency (0.92/1.00)

**Evidence:**

No logical contradictions found in the revised file. Cross-checks:

- **WF-003 and MP-001 alignment:** WF-003 says Phase 1 MUST determine Measurement Plan mode activation. MP-001 says mode activates when analytics infrastructure is "none" or absent. The agent definition `<input>` section rule 5 says "If analytics infrastructure is 'none', prepare to operate in Measurement Plan mode." All three are consistent.

- **MP-001 trigger and agent definition alignment:** The mode activation condition "none or absent" (MP-001) maps precisely to the agent definition's "analytics infrastructure is 'none'" (input validation rule 5). Consistent.

- **MP-008 dual-tagging and CR-001:** MP-008 adds `[PRE-INSTRUMENTATION]` alongside `[REFERENCE-ONLY]` in Measurement Plan mode. CR-001 requires `[REFERENCE-ONLY]` on all threshold values. CR-003 says REFERENCE-ONLY MUST NOT be applied to MEDIUM-confidence outputs. There is no contradiction: CR-003 prohibits applying the tag to MEDIUM outputs, which does not conflict with adding a second tag to LOW outputs in a specialized mode.

- **DS-001 disambiguation:** The iter1 ambiguity is resolved. The section now explicitly separates inclusion criteria ("ANY of the following apply: DS-001 through DS-003") from exclusion criteria ("DS-004, DS-005") into distinct subsections, eliminating the conflated framing.

- **GD-001 and Goal Adjudication alignment:** GD-001 mandates exactly one goal per dimension. The Goal Adjudication section operationalizes this with a 4-step tie-breaking protocol for selecting among multiple plausible goals. Consistent.

- **SI-001 (2-4 signals) and SE-001 (single signal, multiple metrics):** These govern different pipeline steps (Signal Identification vs. Signal-to-Metric edge cases) and are complementary, not contradictory.

**Gaps:**

1. **Version number mismatch.** The rules file is version 1.1.0. SKILL.md is version 1.2.0. The VERSION header of the rules file (line 1) was last updated for "iter1 quality gate revisions" but the file has clearly been revised for iter2 (iter1 gaps resolved, new WF/MP sections added). The version should read 1.2.0 to match SKILL.md. This is a minor internal coherence gap, not a logical contradiction.

**Improvement Path:**

Update the VERSION metadata in line 1 from "1.1.0" to "1.2.0" to align with SKILL.md versioning. Update the footer version block (line 598) accordingly.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**

The iter1 primary gap (no macro-phase sequencing in the rules SSOT) is fully resolved. Assessment of the revised document:

1. **WF rules follow condition-action-consequence pattern.** WF-001 states the sequence (action), names consequences explicitly (producing metrics without dimension selection yields wrong dimensions; setting thresholds without metric formulas produces meaningless targets). WF-002 similarly mandates completion before progression with consequence (gaps propagate; GSM chain breaks). WF-003 connects mode detection to downstream phase impact (late detection causes rework). WF-004 links to the internal GSM sequence with consequence (breaking the Goal-Signal-Metric traceability chain).

2. **MP rules follow condition-action-consequence pattern.** MP-001 (trigger: analytics = none) → MP-004 (action: verbatim disclosure) → MP-006 through MP-010 (output modifications) → MP-011/MP-012 (validation closure). The mode lifecycle is fully specified.

3. **Goal adjudication protocol is 4-step with tie-breaking decision criteria.** Step 1 (lifecycle alignment), Step 2 (upstream evidence), Step 3 (measurability), Step 4 (user authority) provides a deterministic resolution path.

4. **Threshold Fallback Methodology constraints are precise.** Step 2 minimum 14 days, Step 3 improvement range 10-15%, Step 4 minimum 4 weeks. The "Fallback Constraints" table makes each constraint machine-verifiable.

**Gaps:**

1. **MP-009 mentions "estimated implementation effort per metric" without a format specification.** MP-009 mandates that the dashboard specification include "estimated implementation effort per metric" in Measurement Plan mode, but no rule or template specifies the expected format (days? story points? engineer-hours? t-shirt sizes?). An agent executing this rule has ambiguous output format guidance.

**Improvement Path:**

Add a format constraint to MP-009: "Estimated implementation effort MUST be expressed in relative terms (e.g., small/medium/large or 1-3 days / 3-5 days / >5 days) unless the team's estimation units are specified in the UX CONTEXT input." This reduces agent ambiguity.

---

### Evidence Quality (0.88/1.00)

**Evidence:**

All four primary citations are present, properly attributed, and bibliographically complete:

1. **Rodden, Hutchinson & Fu (2010):** Full bibliographic entry in References. Cited at 5 locations: dimension definitions, GSM process rules, threshold fallback (line 191), WF rules (line 31), and dashboard specification (line 401). The WF rules section added a new citation placement appropriate to the macro-phase sequencing derivation from GSM sequential discipline.

2. **Reichheld (2003):** Full bibliographic entry (HBR vol/issue citation preserved). Cited in the Happiness worked example as "Bain & Company / Reichheld (2003)" — the iter1 gap is resolved. The bibliographic chain from inline citation to References table is now unbroken.

3. **Few (2006):** Full bibliographic entry (Analytics Press). Cited in dashboard specification rules source note and the dashboard specification section reference.

4. **Baymard Institute (2020-2024):** Full entry with URL, date range, practitioner verification note. Cited at three locations: threshold fallback (line 191), threshold documentation worked example (line 207), Task Success worked example (line 544: "Baymard Institute, 2024").

**Gaps:**

1. **Adoption worked example threshold is uncited.** Line 530: "Threshold based on mobile app onboarding benchmarks." No specific benchmark publication is named. The 0.9+ rubric criteria requires "all claims with credible citations." The >= 75% onboarding completion target is a threshold claim; the unnamed benchmark fails the citation standard. This is the primary evidence quality gap remaining after iter1 revisions.

2. **Retention worked example threshold is uncited.** Line 537: "SaaS median 30-day retention benchmark; calibrate against own baseline." No specific SaaS retention benchmark publication is named. The >= 45% target is a threshold claim citing an unnamed "SaaS median benchmark." This is the second unnamed benchmark.

Both benchmarks are tagged `[REFERENCE-ONLY]` with LOW confidence, which correctly signals uncertainty, but the rubric's evidence quality criterion requires that the source (even if uncertain) be named. A practitioner cannot verify or update an unnamed benchmark.

**Improvement Path:**

For the Adoption worked example (line 530): change "mobile app onboarding benchmarks" to a specific citation such as "Mixpanel Industry Benchmarks (2023) report mobile app median onboarding completion of 35-40%; target set via Fallback Step 3 (benchmark + 15% improvement)" OR acknowledge this is a Step 3 fallback from a 2-week internal baseline and remove the benchmark attribution entirely.

For the Retention worked example (line 537): change "SaaS median 30-day retention benchmark" to a specific citation such as "Mixpanel/Amplitude SaaS retention benchmarks (2023)" or acknowledge this is Step 3 (fallback estimate) and remove the unnamed benchmark attribution.

---

### Actionability (0.94/1.00)

**Evidence:**

Actionability remains the strongest dimension. The new sections add substantially actionable content:

- **Phase Summary table** (WF rules section): Maps each of the 5 phases to its input, output, and governing rule sections. An agent or engineer can execute each phase knowing exactly what goes in, what comes out, and which rules apply.

- **MP output modification table** (MP-006 through MP-010): Two-column format (Standard Behavior vs. Measurement Plan Behavior) makes the mode-specific changes immediately identifiable. This is the clearest possible specification for an agent implementing mode-based behavior switching.

- **MP-004 verbatim disclosure text:** The exact required text is provided in a fenced code block. An agent does not need to infer the disclosure — it copies the specified text. This is optimal actionability for a compliance requirement.

- **Self-review checklist expansion:** 14 items with rejection criteria and rule IDs enable unambiguous pass/fail assessment before output persistence.

- **Worked examples for all 5 HEART dimensions:** All 5 dimensions have complete GSM table rows with all columns populated. Templates remain copy-paste ready with `{placeholder}` syntax.

**Gaps:**

1. **MP-009 lacks effort estimation format.** Noted in Methodological Rigor. The format ambiguity reduces actionability specifically for the instrumentation priority section of Measurement Plan mode dashboard specifications.

**Improvement Path:**

Add format specification to MP-009 as noted in Methodological Rigor gap above.

---

### Traceability (0.92/1.00)

**Evidence:**

The iter1 traceability gaps are substantially addressed:

- **Self-review Rule IDs column:** Items 1 through 14 now reference specific rule IDs. Item 1 → DS-001/DS-006. Item 2 → GD-001/SI-001/MS-001. Item 3 → MS-002. Item 4 → CR-001/CR-004. Item 5 → MS-006. Item 6 → CR-003. Item 7 → H-23. Item 8 → MP-004/MP-005/MP-011. Item 9 → SI-006 (misattribution — see gap). Item 10 → MP-010. Item 11 → GD-001. Item 12 → SE-001/SE-010. Item 13 → DF-001/DF-004/DL-001/DL-004. Item 14 → WF-001/WF-002.

- **WF rule IDs:** WF-001 through WF-004 follow the established ID namespace pattern.

- **MP rule IDs:** MP-001 through MP-012 follow the established ID namespace pattern.

- **Footer traceability comment** (line 606): Includes PROJ-022, EPIC-003, Wave 2, H-23/H-34/SR-002/SR-003/H-13/H-15, methodology citations, and ORCHESTRATION.yaml path.

- **MP source attribution** (line 227): "Agent definition `<input>` section defines the mode activation logic; this section is the rules SSOT for mode behavior." Explicit cross-reference to the dual-file architecture.

**Gaps:**

1. **Self-review item 9 Rule ID misattribution.** Item 9 cites SI-006 for the Synthesis Judgments Summary requirement. SI-006 governs incorporation of upstream sub-skill findings into signal identification, not the Synthesis Judgments Summary as an output artifact. The correct traceability reference is the Quality Gate Integration section (line 469) or `skills/user-experience/rules/synthesis-validation.md`.

2. **All-Five Override section lacks P-020 constitution path.** Line 118 references P-020 inline but does not include a repo-relative path to `docs/governance/JERRY_CONSTITUTION.md`. The iter1 recommendation explicitly identified this as an improvement; it was not implemented.

**Improvement Path:**

Correct self-review item 9 Rule IDs to reference the Quality Gate Integration section anchor or synthesis-validation.md. Add "(P-020: `docs/governance/JERRY_CONSTITUTION.md`)" to the All-Five Override section after the P-020 inline reference.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.88 | 0.93+ | Name specific publications for the Adoption and Retention benchmark citations. For Adoption: cite a specific source (e.g., Mixpanel Industry Benchmarks 2023) OR change to explicit Fallback Step 3 derivation from baseline (removing the unnamed benchmark claim). For Retention: similarly cite a specific SaaS benchmark publication (e.g., Mixpanel/Amplitude 2023 SaaS benchmarks) OR convert to an explicit Fallback Step 3 derivation. |
| 2 | Internal Consistency | 0.92 | 0.94+ | Update the VERSION header (line 1) and footer block (line 598) from 1.1.0 to 1.2.0 to align with SKILL.md versioning. One-line edit to each location. |
| 3 | Traceability | 0.92 | 0.95+ | (a) Correct self-review item 9 Rule IDs from "SI-006" to reference the Quality Gate Integration section or synthesis-validation.md. (b) Add P-020 constitution path to All-Five Override section: "(P-020: `docs/governance/JERRY_CONSTITUTION.md`)". |
| 4 | Methodological Rigor | 0.93 | 0.96+ | Add effort format specification to MP-009: "Estimated implementation effort MUST be expressed in relative terms (small/medium/large or day-range estimates)." |
| 5 | Completeness | 0.94 | 0.96+ | Correct self-review item 9 Rule IDs (same as Traceability P3a above — dual benefit). |

---

## Score Computation Verification

| Dimension | Score | Weight | Product |
|-----------|-------|--------|---------|
| Completeness | 0.94 | 0.20 | 0.1880 |
| Internal Consistency | 0.92 | 0.20 | 0.1840 |
| Methodological Rigor | 0.93 | 0.20 | 0.1860 |
| Evidence Quality | 0.88 | 0.15 | 0.1320 |
| Actionability | 0.94 | 0.15 | 0.1410 |
| Traceability | 0.92 | 0.10 | 0.0920 |
| **Sum** | | **1.00** | **0.9230** |

Rounded to 3 decimal places: **0.923**

---

## Iteration History

| Iteration | Score | Delta | Weakest Dimension | Verdict | Primary Gap |
|-----------|-------|-------|------------------|---------|-------------|
| 1 | 0.900 | -- | Methodological Rigor (0.88) | REVISE | Missing Workflow Phase Sequencing; Missing Measurement Plan Mode Rules; Bain/Reichheld attribution |
| 2 | 0.923 | +0.023 | Evidence Quality (0.88) | REVISE | Unnamed Adoption and Retention benchmark citations |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Completeness: uncertain between 0.94-0.95; chose 0.94 because item 9 Rule ID misattribution reduces traceability for that coverage area. Methodological Rigor: uncertain between 0.93-0.94; chose 0.93 because MP-009 effort format is underspecified. Traceability: uncertain between 0.92-0.93; chose 0.92 because two gaps remain from iter1 recommendations that were not implemented.)
- [x] C4 revision calibration considered: iter2 deliverable with 3 structural additions (WF, MP, checklist IDs) scoring above first-draft range (0.65-0.80) is appropriate; 0.923 is at the strong-to-excellent boundary consistent with a well-executed revision that resolves major gaps but leaves secondary evidence quality gaps unaddressed
- [x] No dimension scored above 0.95 (highest is Completeness and Actionability at 0.94, with documented justification)
- [x] Anti-leniency verification: Evidence Quality held at 0.88 despite Bain/Reichheld fix. Two unnamed benchmarks (Adoption line 530, Retention line 537) are real citation gaps. The 0.9+ rubric criterion states "all claims with credible citations" -- unnamed benchmarks fail this standard even when tagged [REFERENCE-ONLY].

**Leniency bias assessment:** Score delta of +0.023 from iter1 reflects genuine structural improvements (WF + MP + checklist). Evidence Quality held at 0.88 -- same as iter1 -- because the primary iter1 evidence quality gap (Bain/Reichheld) was resolved but two secondary gaps (Adoption, Retention unnamed benchmarks) were not addressed and hold the dimension below 0.90. The composite 0.923 falls 0.027 below the 0.95 threshold, driven primarily by Evidence Quality. Score is not inflated.

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.923
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.88
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Name specific publications for Adoption benchmark (line 530: 'mobile app onboarding benchmarks' is unnamed) -- highest impact fix"
  - "Name specific publications for Retention benchmark (line 537: 'SaaS median 30-day retention benchmark' is unnamed)"
  - "Update VERSION header and footer from 1.1.0 to 1.2.0 to align with SKILL.md versioning"
  - "Correct self-review item 9 Rule IDs from SI-006 to Quality Gate Integration or synthesis-validation.md reference"
  - "Add P-020 constitution path to All-Five Override section"
  - "Add effort format specification to MP-009"
```

---

*Score Report: rules-iter2-score.md*
*Deliverable: skills/ux-heart-metrics/rules/heart-methodology-rules.md*
*Scorer: adv-scorer (S-014 LLM-as-Judge)*
*SSOT: .context/rules/quality-enforcement.md*
*Prior score: rules-iter1-score.md (0.900)*
*Created: 2026-03-04*
