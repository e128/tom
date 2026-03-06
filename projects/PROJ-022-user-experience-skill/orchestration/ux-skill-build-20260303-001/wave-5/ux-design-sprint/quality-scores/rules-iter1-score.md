# Quality Score Report: Design Sprint 2.0 Methodology Rules

## L0 Executive Summary
**Score:** 0.930/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.91)
**One-line assessment:** Strong first-draft rules file with comprehensive sprint coverage and clean structural patterns, blocked from PASS by one cross-reference error (SPR-028 cites "QG-003" but the QG section uses SPR- prefix throughout -- should cite "SPR-042") and minor completeness gaps in template versioning and citation depth.

---

## Scoring Context
- **Deliverable:** `skills/ux-design-sprint/rules/sprint-methodology-rules.md`
- **Deliverable Type:** Methodology Rules (operational constraints file)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 PASS Threshold:** 0.95 (governance source: `ux-sprint-facilitator.governance.yaml` `enforcement.quality_threshold: 0.95`)
- **Reference Pattern:** `skills/ux-behavior-design/rules/fogg-behavior-rules.md` v1.2.0 (scored 0.953 PASS)
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.930 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Gap to Threshold** | 0.020 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | 11 sections, 43 rules, 18 self-review checks; template ref unversioned; minor |
| Internal Consistency | 0.20 | 0.91 | 0.182 | Cross-file alignment strong; SPR-028 cites "QG-003" but QG section uses SPR-042 |
| Methodological Rigor | 0.20 | 0.94 | 0.188 | Consistent structure, chapter-level citations, Day compression note clear |
| Evidence Quality | 0.15 | 0.92 | 0.138 | All 4 citations with full bibliographic data; Courtney credibility note absent from rules file |
| Actionability | 0.15 | 0.94 | 0.141 | 9-section output spec with completeness criteria; 43 rules; operational depth high |
| Traceability | 0.10 | 0.95 | 0.095 | VERSION header, section Source blocks, rule ID citations in checklist, full dependency matrix |
| **TOTAL** | **1.00** | | **0.930** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**

The file covers all 11 sections listed in the navigation table, spanning the full sprint lifecycle: Sprint Setup (SPR-001 through SPR-003), Day 1 Map (SPR-004 through SPR-009), Day 2 Sketch (SPR-010 through SPR-014), Day 3 Decide (SPR-015 through SPR-019), Day 4 Test (SPR-020 through SPR-026), Synthesis (SPR-027 through SPR-030), Confidence Classification (SPR-031 through SPR-034), Output Format (SPR-035 through SPR-039), Quality Gate Integration (SPR-040 through SPR-043), Related Files, and Self-Review Checklist (18 items). The Output Format section defines all 9 required output sections with completeness criteria. The Related Files section is a full dependency matrix. The governance.yaml `post_completion_checks` lists 13 verifiable assertions; all 13 map to rules in the file (e.g., `verify_storyboard_10_to_16_panels` -> SPR-016, `verify_observation_grid_5_users` -> SPR-020). The reference pattern file (fogg-behavior-rules.md v1.2.0) has 18 self-review checklist items; this file has 18 items, matching the reference pattern's depth.

**Gaps:**

1. **Template reference unversioned (line 437):** `design-sprint-template.md` is listed as "unversioned" in the Related Files table. The reference pattern (fogg-behavior-rules.md) explicitly versions its template reference (`bmap-diagnosis-template.md v1.4.0`). An unversioned template reference reduces forward compatibility checking when the template is revised.

2. **No wave bypass rule for CRISIS mode:** The Synthesis Rules section (SPR-029/SPR-030) briefly mentions CRISIS mode but defers to the agent definition. The agent definition describes the CRISIS mode addition in Phase 5 Step 7. The rules file does not define a discrete CRISIS Discipline rule equivalent (fogg-behavior-rules.md does not have CRISIS mode, so there is no reference analog, but this is a coverage gap relative to the agent definition's described behavior).

**Improvement Path:**

- Add a version marker to `design-sprint-template.md` in the Related Files table (e.g., "v1.0.0 -- initial release" or "unversioned v1" with a git hash reference).
- Add a discrete CRISIS mode synthesis discipline row (SPR-030a or a CRISIS subsection in Synthesis Rules) that formalizes the priority ranking and quick-win identification requirements.

---

### Internal Consistency (0.91/1.00)

**Evidence:**

Cross-file consistency checks performed:

1. **Rule IDs vs. governance.yaml post_completion_checks:** All 13 post_completion_checks have corresponding rule coverage. `verify_challenge_statement_hmw_format` -> SPR-001; `verify_sprint_questions_testable` -> SPR-004; `verify_all_four_days_documented` -> SPR-041; `verify_storyboard_10_to_16_panels` -> SPR-016; `verify_observation_grid_5_users` -> SPR-020; `verify_pattern_analysis_threshold_applied` -> SPR-021; `verify_sprint_verdicts_with_evidence` -> SPR-022; `verify_assumption_validation_results` -> SPR-023; `verify_synthesis_judgments_present` -> SPR-027; `verify_handoff_data_populated` -> SPR-038; `verify_wave_entry_criteria_checked` -> SPR-002; `verify_navigation_table` -> SPR-036; `verify_file_created` -> SPR-035. All map cleanly. PASS.

2. **Template reference existence:** `skills/ux-design-sprint/templates/design-sprint-template.md` exists (confirmed via file glob). PASS.

3. **Related Files file versions:** SKILL.md v1.1.0 matches the SKILL.md frontmatter `version: "1.1.0"`. Agent .md v1.0.0 matches agent footer `Agent Version: 1.0.0`. Governance YAML v1.0.0 matches `version: 1.0.0` in the governance file. PASS.

4. **Citation alignment with agent definition:** The rules file cites the same four sources (Knapp et al. 2016 with identical ISBN 978-1501121746, Courtney 2019 at same URL, Brown 2009 with identical ISBN 978-0061766084, Nielsen 2000 at same URL) as the agent definition References table. PASS.

5. **Confidence classification alignment with synthesis-validation.md:** synthesis-validation.md Sub-Skill Synthesis Output Map assigns: `/ux-design-sprint` Day 4 thematic analysis = HIGH, Day 2 sketch selection rationale = MEDIUM. Rules file SPR-032 enforces HIGH only when >= 3/5 threshold is met; SPR-033 forbids HIGH for maturity assessment and competitive positioning. Pattern analysis section: "HIGH when threshold met (deterministic)"; sketch evaluation: MEDIUM. ALIGNED. PASS.

6. **Quality gate threshold:** SPR-040 cites `ux-sprint-facilitator.governance.yaml enforcement.quality_threshold` for the 0.95 C4 threshold. Governance.yaml `enforcement.quality_threshold: 0.95`. ALIGNED. PASS.

**Gaps:**

1. **Cross-reference error in SPR-028:** SPR-028 reads: "Undisclosed degraded mode violates P-022; Evidence Quality receives a 0 score **per QG-003**." The Quality Gate Integration section in this file uses SPR- prefix for all QG rules (SPR-040 through SPR-043). SPR-042 is the rule that states "Evidence Quality receives a 0 score." The reference "per QG-003" is borrowed from the fogg-behavior-rules.md pattern (which uses `QG-003` for its analog rule) but is incorrect in this file where the rule is SPR-042. This is a verifiable internal inconsistency: the cross-reference points to a rule ID that does not exist in this document.

   Location: Line 315, rule SPR-028 consequence column.

**Improvement Path:**

- Fix SPR-028 consequence: replace "per QG-003" with "per SPR-042".

---

### Methodological Rigor (0.94/1.00)

**Evidence:**

The file follows the structural pattern of the reference (fogg-behavior-rules.md v1.2.0) with high fidelity: VERSION header, nav table, section-level `> Source:` blocks citing specific chapters/sections, Discipline tables with consistent columns (ID | Rule | Tier | Consequence of Violation), Related Files dependency matrix with relationship classification, and Self-Review Checklist with rule references per row.

The sprint methodology is correctly structured: SPR-011 enforces the four-step sketch sequence order (Notes -> Ideas -> Crazy 8s -> Solution Sketch). SPR-015/SPR-018 enforce Decider authority with explicit P-020 alignment. The HMW format requirement (SPR-001) cites Brown (2009) and Knapp et al. (2016) Chapter 4. The five-user threshold (SPR-025) cites Nielsen (2000). The Day Compression Note correctly explains the Courtney (2019) 4-day format vs. the Knapp et al. (2016) 5-day format. The pattern analysis thresholds (>= 3/5 strong, 2/5 moderate, 1/5 weak) align with the agent definition's observation grid methodology.

The Quality Gate Integration section explicitly maps all 6 S-014 dimensions to sprint-specific evaluation criteria. The Scoring Discipline table (SPR-040 through SPR-043) mirrors the pattern from fogg-behavior-rules.md QG-001 through QG-004.

**Gaps:**

1. **SPR-039 MEDIUM tier for storyboard format:** SPR-039 (storyboard table format compliance) is classified as MEDIUM. The storyboard is the prototype construction blueprint per SPR-016 (HARD); inconsistent format degrades "prototype construction traceability" per the rule's own consequence. Given that storyboard completeness is HARD (SPR-016 verifies panel count and all 4 elements), the format compliance rule being MEDIUM creates a logical asymmetry -- content completeness is HARD but format compliance for the same content is MEDIUM. The fogg-behavior-rules.md classifies all output format rules related to scoring tables as HARD (OUT-004). This asymmetry is a minor methodology gap, not a fundamental error.

**Improvement Path:**

- Consider promoting SPR-039 to HARD to match the tier of SPR-016 (storyboard completeness) and resolve the asymmetry between storyboard content and format requirements.

---

### Evidence Quality (0.92/1.00)

**Evidence:**

All four primary citations have full bibliographic data:
- Knapp et al. (2016): full authors, title, publisher, ISBN 978-1501121746
- Courtney (2019): author, title, publisher (AJ&Smart), URL ajsmart.com/design-sprint
- Brown (2009): full author, title, publisher (Harper Business), ISBN 978-0061766084
- Nielsen (2000): author, title, journal (Nielsen Norman Group), full URL

Citations are consistent across the VERSION header comment (line 1), all six section-level `> Source:` blocks, and the traceability comment at the bottom (lines 482-483). All four citations match the agent definition's References table verbatim.

The synthesis-validation.md reference is versioned (v1.1.0). The wave-progression.md reference is versioned (v1.2.0). The MCP coordination file is explicitly marked "unversioned -- tracked via git history" with the same pattern as fogg-behavior-rules.md.

**Gaps:**

1. **Courtney (2019) practitioner credibility note absent:** The agent definition's References table includes an adoption breadth statement for Courtney (2019): "AJ&Smart has facilitated 400+ design sprints for organizations including Google, LEGO, Lufthansa, and the United Nations (per AJ&Smart published portfolio, self-reported)." This credibility qualifier is present in the agent definition but absent from the rules file's citation handling. The fogg-behavior-rules.md includes adoption breadth context inline in the section where Courtney is cited (the Day compression note). Omitting this qualifier means the rules file cites a practitioner resource without the same credibility disclosure context that the agent definition provides. Per P-022 and P-001, this is a minor evidence quality gap -- readers of the rules file in isolation cannot assess Courtney (2019)'s credibility without the practitioner caveat.

   The gap is minor because: (a) the rules file references the agent definition in Related Files, (b) the VERSION header points to Courtney (2019) as a source, and (c) the Day Compression Note implicitly validates Courtney by explaining the compression rationale. However, the reference pattern (fogg-behavior-rules.md) is more explicit about methodology credibility.

**Improvement Path:**

- Add a parenthetical credibility qualifier to the Courtney (2019) citation in section-level Source blocks where it first appears (e.g., in Sprint Setup Rules `> Source:` or in the Day Compression Note): "(practitioner resource, not peer-reviewed; AJ&Smart has facilitated 400+ design sprints, per AJ&Smart published portfolio, self-reported)" -- matching the agent definition's disclosure.

---

### Actionability (0.94/1.00)

**Evidence:**

The file is operationally dense with actionable specificity throughout:

- **9 output sections** defined in Output Format Rules, each with explicit completeness criteria (e.g., Day 4 section requires: prototype reference, interview script summary, observation grid with all sprint questions × 5 users, pattern analysis, sprint question verdicts, assumption validation).
- **43 numbered rules (SPR-001 through SPR-043)** each with a specific tier (HARD/MEDIUM) and consequence, enabling agents to understand when rule violation occurs and what it means.
- **18 self-review checklist items** each referencing specific rule IDs, enabling pre-persistence verification without re-reading the full document.
- **Quality Gate Integration** section maps all 6 S-014 dimensions to sprint-specific criteria, enabling the scorer to apply the rubric without interpretation.
- **Dimension Mapping table** (Quality Gate Integration) provides sprint-specific evaluation criteria at the dimension level, directly usable by adv-scorer.
- **Handoff preparation rules** (SPR-030, SPR-038) specify the threshold for downstream handoff activation (Day 4 complete) and the schema conformance requirement.

The reference pattern (fogg-behavior-rules.md) scored 0.953 PASS; its actionability strength derives from the same structural patterns that this file employs.

**Gaps:**

1. **SPR-039 MEDIUM for storyboard format creates ambiguity:** As noted in Methodological Rigor, SPR-039's MEDIUM tier means an agent could produce a storyboard with valid content (HARD compliant per SPR-016) but non-standard format without triggering a HARD rejection. The MEDIUM classification reduces the actionability signal for format compliance -- agents may not prioritize format adherence if content is complete.

**Improvement Path:**

- Promote SPR-039 to HARD and update the consequence to: "Non-standard storyboard format prevents downstream prototype construction traceability and fails SPR-035 (section completeness requires standard format)."

---

### Traceability (0.95/1.00)

**Evidence:**

The traceability structure is comprehensive and well-executed:

- **VERSION header** (line 1): lists all source files with versions, citations with ISBNs/URLs, and parent classification.
- **Section-level `> Source:` blocks**: every substantive section has a specific source attribution (e.g., Day 4 cites Knapp et al. (2016) Chapters 13-15 and Nielsen (2000) specifically).
- **Rule ID sequential numbering**: SPR-001 through SPR-043 are sequential without gaps, enabling precise cross-reference from the Self-Review Checklist.
- **Self-Review Checklist rule references**: every row cites the specific rule ID(s) it verifies (e.g., row 9: "Storyboard contains 10-16 panels..." -> SPR-016; row 10: "Observation grid covers all sprint questions..." -> SPR-020).
- **Related Files dependency matrix**: complete with relationship classification (Parent SKILL.md / Agent definition / Governance YAML / Output template / Wave progression / Synthesis validation / MCP coordination / Quality enforcement), file paths, versions, and purpose descriptions.
- **Bottom traceability comment**: maps to PROJ-022 EPIC-005, governance standards (H-23, H-34, H-13, SR-002, SR-003), and all four methodology citations.
- **SPR-034**: cites `skills/user-experience/rules/synthesis-validation.md (v1.1.0) minimum-confidence aggregation rule` with specific version and section name.

No significant traceability gaps found. This dimension is the strongest in the file.

**Gaps:**

- None material. Minor: the bottom traceability comment does not explicitly cite the wave-progression.md version (v1.2.0), though this is referenced in Related Files. The omission in the traceability comment is trivial.

**Improvement Path:**

- No action required to achieve 0.95 threshold; this dimension already meets it.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.91 | 0.95 | **Fix SPR-028 cross-reference:** Change "per QG-003" to "per SPR-042" in the consequence field of SPR-028 (line 315). This is the most critical defect -- it is a verifiable internal inconsistency where a rule references a non-existent ID in this document. |
| 2 | Completeness | 0.93 | 0.96 | **Version the template reference:** Change `design-sprint-template.md | unversioned` to `design-sprint-template.md | v1.0.0` (or the current actual version) in the Related Files table. This matches the reference pattern (fogg-behavior-rules.md references `bmap-diagnosis-template.md v1.4.0`). |
| 3 | Evidence Quality | 0.92 | 0.95 | **Add Courtney (2019) practitioner caveat:** In the Day Compression Note or the Day 4 Test Rules `> Source:` block, add: "(practitioner resource, not peer-reviewed; AJ&Smart has facilitated 400+ design sprints, per AJ&Smart published portfolio, self-reported)". This matches the agent definition's disclosure level. |
| 4 | Methodological Rigor | 0.94 | 0.96 | **Promote SPR-039 to HARD:** Storyboard format compliance should be HARD tier to match storyboard content completeness (SPR-016 is HARD). The asymmetry creates a methodological gap where format can be violated without HARD-level consequences. |
| 5 | Completeness | 0.93 | 0.96 | **Add discrete CRISIS mode synthesis rule:** Add a rule (SPR-030a or subsection) formalizing the CRISIS mode additions described in the agent definition Phase 5 Step 7 (priority ranking, quick-win identification). |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computation
- [x] Evidence documented for each score with specific locations (section names, rule IDs, line numbers where applicable)
- [x] Uncertain scores resolved downward: Internal Consistency chose 0.91 over 0.92 due to the verifiable SPR-028/QG-003 cross-reference error; Completeness chose 0.93 over 0.94 due to template versioning gap
- [x] First-draft calibration considered: this is a first iteration (iter1); the composite of 0.930 falls in the expected 0.85-0.90 range for first drafts with strong structural foundations -- slightly above due to the explicit reference pattern from fogg-behavior-rules.md that the author followed closely
- [x] No dimension scored above 0.95 without specific evidence justification: Traceability scored 0.95 based on documented evidence of VERSION header, section Source blocks, sequential rule IDs, checklist rule references, full dependency matrix, and bottom traceability comment
- [x] C4 threshold (0.95) actively applied: the deliverable would PASS under the baseline C2+ threshold (0.92) but fails the C4 threshold (0.95) by a gap of 0.020

---

## Session Context

```yaml
verdict: REVISE
composite_score: 0.930
threshold: 0.95
weakest_dimension: internal_consistency
weakest_score: 0.91
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Fix SPR-028 consequence: replace 'per QG-003' with 'per SPR-042' (line 315 -- non-existent cross-reference)"
  - "Version the design-sprint-template.md reference in Related Files (currently 'unversioned')"
  - "Add Courtney (2019) practitioner credibility caveat in Day 4 or Day Compression Note source block"
  - "Promote SPR-039 to HARD tier to resolve asymmetry with SPR-016 storyboard content completeness"
  - "Add discrete CRISIS mode synthesis rule formalizing Phase 5 Step 7 additions from agent definition"
```

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Reference Pattern: `skills/ux-behavior-design/rules/fogg-behavior-rules.md` v1.2.0 (scored 0.953 PASS)*
*Created: 2026-03-04*
