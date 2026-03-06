# Quality Score Report: Heuristic Report Template (Iteration 3)

## L0 Executive Summary

**Score:** 0.906/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.87)

**One-line assessment:** The template is structurally complete and well-traced but fails the C4 threshold (0.95) and the standard H-13 threshold (0.92) due to a missing `## Methodology` entry in the navigation table and two secondary evidence-quality and methodological gaps; targeted fixes to these three items should achieve threshold passage.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/templates/heuristic-report-template.md`
- **Deliverable Type:** Template (structured fill-in scaffold for evaluation reports)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Parent Artifacts Read:**
  - `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md` (v1.2.0)
  - `skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md` (v1.0.0)
  - `skills/ux-heuristic-eval/SKILL.md` (v1.0.0)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 3
- **Prior Scores:** Iter1: 0.843, Iter2: 0.919 (trajectory: +0.076, +0.076)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.906 |
| **Standard Threshold (H-13)** | 0.92 |
| **C4 Threshold (requested)** | 0.95 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (no adv-executor reports provided) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | All 11 required sections present; Coverage Matrix and Self-Review checklist are bonus; all 10 heuristic blocks scaffolded |
| Internal Consistency | 0.20 | 0.87 | 0.174 | `## Methodology` heading exists at line 87 but is absent from the navigation table -- H-23/NAV-004 violation; all other cross-references internally consistent |
| Methodological Rigor | 0.20 | 0.91 | 0.182 | 5-step workflow accurately encoded; AI supplement heuristics correctly conditioned; Coverage Matrix lacks column-count adjustment guidance for non-3-screen evaluations |
| Evidence Quality | 0.15 | 0.88 | 0.132 | Evidence field placeholders are appropriately specific; rules-file evidence quality standard (acceptable vs. unacceptable examples) not embedded inline in template |
| Actionability | 0.15 | 0.92 | 0.138 | REPEATABLE BLOCK markers, conditional comments, binary checklist, YAML inline comments all present; Coverage Matrix column count adjustment not instructed |
| Traceability | 0.10 | 0.94 | 0.094 | Full chain: template header → rules sections → skill → agent → external citations; ORCHESTRATION.yaml and Google PAIR access date added in iter3; Coverage Matrix format has no source citation |
| **TOTAL** | **1.00** | | **0.906** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**

All sections required by `heuristic-evaluation-rules.md` [Report Structure] (sections 1-9) are present:
1. Navigation table (lines 13-28) -- present with 11 entries
2. Executive Summary (lines 31-58) -- present with severity distribution table, top findings scaffold, overall assessment paragraph, coverage confirmation
3. Evaluation Context (lines 61-85) -- present with screens table, input modality, MCP status, degraded mode conditional block
4. Findings by Heuristic (lines 97-218) -- all 10 heuristic blocks (H1-H10) present with consistent REPEATABLE BLOCK markers; AI supplement sections correctly placed as conditional comments
5. Ranked Findings Summary (lines 247-255) -- present
6. Remediation Roadmap (lines 258-284) -- present with Low/Medium/High groupings and Suggested Implementation Order paragraph
7. Strategic Implications (lines 304-317) -- present with three guidance subsections
8. Synthesis Judgments Summary (lines 287-301) -- present with three example rows and confidence classification key
9. Handoff Data (lines 371-421) -- present with both Findings table and full YAML block

Template additionally includes:
- Heuristic Coverage Matrix (lines 221-244) -- bonus section not in rules minimum
- Limitations and Reliability (lines 320-352) -- bonus section with P-022 disclosure, input modality, and high-stakes recommendation
- Self-Review Checklist (lines 354-368) -- maps exactly to 10 rules-file verification items

**Gaps:**

None of the nine rules-required sections are missing. The template is complete relative to the authoritative requirements source.

**Improvement Path:**

No changes needed for this dimension to reach 0.95+. Completeness is already at 0.93 and the gap to 0.95+ is being driven by other dimensions.

---

### Internal Consistency (0.87/1.00)

**Evidence:**

All cross-section references are internally consistent:
- Severity scale (Executive Summary table, Finding format, Ranked Summary, Remediation Roadmap) uses "0-4" and Nielsen severity names consistently throughout
- Handoff threshold "severity >= 2" appears at lines 373 and in Self-Review item 9 (line 366) -- consistent with each other and with `heuristic-evaluation-rules.md` [Cross-Framework Handoff Threshold]
- Finding format fields (Heuristic, Severity, Screen/Flow, Evidence, Remediation, Effort) match exactly across the REPEATABLE BLOCK (lines 110-118), Ranked Findings Summary header (line 251), and Handoff Data header (line 377)
- Self-Review Checklist items map one-to-one with the rules file checklist
- Handoff YAML field annotations (`[handoff-v2]` vs. `[ux-ext]`) are applied consistently to all fields

**Gaps:**

**Critical inconsistency:** `## Methodology` is a `##`-level heading at line 87 and thus constitutes a "major section" per H-23/NAV-004. It is NOT listed in the navigation table (lines 15-28). The navigation table lists 11 entries but omits Methodology entirely. This violates H-23 (navigation table MUST include all major sections) and NAV-004 (all `##` headings SHOULD be listed). A reader using the navigation table to locate the methodology description would find no entry.

The Synthesis Judgments Summary appears at line 24 in the navigation table but is listed after "Limitations and Reliability" in the nav table (line 25), whereas in the document body the Synthesis Judgments Summary section (line 287) appears before Limitations and Reliability (line 320). This ordering inconsistency between the nav table and document body is a secondary internal inconsistency: nav table order does not match document order for these two sections.

**Improvement Path:**

1. Add `| [Methodology](#methodology) | Non-fill-in prose describing the 5-step evaluation workflow and AI supplement conditions |` to the navigation table at the correct position (after Evaluation Context, before Findings by Heuristic).
2. Reorder the navigation table entries to match document body order: move Synthesis Judgments Summary (currently entry 8) to appear after Remediation Roadmap (currently entry 6) and before Strategic Implications (currently entry 7), reflecting the actual document ordering.

---

### Methodological Rigor (0.91/1.00)

**Evidence:**

The template encodes rigorous methodology:
- Methodology section prose (lines 87-95) accurately summarizes the 5-step workflow from `heuristic-evaluation-rules.md [Evaluation Workflow]` without requiring fill-in -- this was the correct iter3 improvement
- The prose accurately cites the source: "`heuristic-evaluation-rules.md` [Evaluation Workflow]" with step numbers
- AI supplement heuristics are correctly conditioned on `AI Product Flag = true` with consistent placement (comments at lines 203-217, 237-240)
- P-022 disclosure for AI supplements in the Methodology section (line 91) matches the rules file AI-Interaction Supplement Heuristics section disclosure
- DEDUPLICATION CHECK comment (line 101) and F-{NNN} ID assignment instruction (line 102) are placed at the correct pre-population point
- The Effort field guidance uses Low/Medium/High consistently; Effort classification criteria live in the rules file as intended
- Coverage note (line 243) prompts evaluation of zero-finding heuristics with explicit rules reference

**Gaps:**

The Heuristic Coverage Matrix (lines 225-241) uses exactly 3 placeholder screen columns (`{{Screen_1}}`, `{{Screen_2}}`, `{{Screen_3}}`). There is no instruction telling the evaluator to add or remove columns when the screen count differs from 3. An evaluator with 5 screens would need to add 2 columns with no explicit guidance. The only instructional comment in this section concerns AI supplement rows (line 237), not column count. This is a methodological completeness gap specific to this section.

**Improvement Path:**

Add a comment immediately after the Coverage Matrix header: `<!-- Add or remove screen columns to match the number of screens in this engagement. Minimum 1 column; no maximum. The AI supplement row comments below are also conditional on AI Product Flag. -->`. This single-line addition closes the gap for evaluators with non-standard screen counts.

---

### Evidence Quality (0.88/1.00)

**Evidence:**

The template scaffolds evidence quality effectively for practitioners:
- The Evidence field placeholder "{{specific interface observation demonstrating the violation}}" (line 115) is specific and directive, matching the rules file's evidence standard
- Synthesis Judgments Summary rows include concrete example content in the judgment cells (lines 293-295) that model what high-quality synthesis judgments look like ("F-003 rated severity 3 vs. 2", "F-005 and F-008 consolidated")
- Strategic Implications subsections include model-quality guidance text (lines 308, 312, 316) with concrete examples embedded in the placeholder text
- The HEART mapping comment (line 381) gives specific category options and cites the rules file mapping table
- Footer citations (lines 427-429) are complete academic citations with author, year, title, and conference for Amershi et al. (2019) and HEART; Nielsen citations include (a)/(b)/(c) disambiguation and the 2020 revision; Google PAIR includes the access date (iter3 fix)

**Gaps:**

`heuristic-evaluation-rules.md` [Evidence Quality Standard] contains three specific examples of acceptable evidence (e.g., "The 'Save' button produces no visual feedback after click -- no spinner, no confirmation toast, no state change") and three categories of unacceptable evidence (subjective, speculative, circular). These examples are not embedded in the template itself. A practitioner using the template without reading the rules file would see only "{{specific interface observation demonstrating the violation}}" as guidance and might produce lower-quality evidence.

This is an appropriate separation-of-concerns design choice (template stays lean; examples live in rules), but it does reduce the template's standalone evidence-quality guidance. An inline comment pointing to the rules file evidence standard would improve this without bloating the template.

**Improvement Path:**

Add an inline comment directly below the Evidence field placeholder: `<!-- For evidence quality standard (acceptable vs. unacceptable examples), see heuristic-evaluation-rules.md [Evidence Quality Standard] -->`. This is a single-line addition that closes the navigation gap without duplicating the full standard in the template.

---

### Actionability (0.92/1.00)

**Evidence:**

The template is highly actionable:
- All fill-in fields use consistent `{{PLACEHOLDER}}` syntax -- practitioners know exactly what to replace
- REPEATABLE BLOCK markers (lines 109, 118) are clearly labeled and placed correctly at the H1 section; H2-H10 sections use `<!-- Repeat FINDING blocks as needed -->` comments
- Conditional comments for degraded mode (lines 79-83) and AI supplement sections (lines 203-217, 237-240) explicitly state "Include ONLY when" conditions
- The Handoff YAML (lines 385-421) has inline `[handoff-v2]` and `[ux-ext]` annotations on every field, directly actionable for YAML construction
- Self-Review Checklist uses binary `[ ]` checkboxes -- maximally actionable pre-persistence gate
- Comment at line 51 gives a count instruction: "Add up to 5 top findings by severity"
- The Remediation Roadmap Suggested Implementation Order (line 283) includes explicit sequencing guidance in its placeholder: "typically severity 4 first regardless of effort, then quick wins for momentum"

**Gaps:**

The Coverage Matrix column adjustment gap (identified under Methodological Rigor) is also an actionability gap: practitioners with non-3-screen evaluations cannot act without understanding they need to add/remove columns. This is a shared gap between the two dimensions.

**Improvement Path:**

The Coverage Matrix comment addition described under Methodological Rigor addresses this gap for both dimensions simultaneously.

---

### Traceability (0.94/1.00)

**Evidence:**

Strong traceability throughout:
- Header comment (lines 1-4): VERSION `1.2.0`, DATE `2026-03-04`, REVISION description, SKILL, AGENT, SOURCE with section-level references
- Methodology prose (line 89): cites `heuristic-evaluation-rules.md [Evaluation Workflow]` with step numbers
- Findings by Heuristic section header (line 99): cites `heuristic-evaluation-rules.md [Report Structure] section 4`
- Deduplication comment (line 101): cites `heuristic-evaluation-rules.md [Deduplication Rules]` by section name
- HEART mapping comment (line 381): cites `heuristic-evaluation-rules.md [Heuristic-to-HEART Category Mapping]`
- Handoff YAML header (lines 387-388): cites `docs/schemas/handoff-v2.schema.json` and schema version
- Self-Review Checklist (line 356): cites `heuristic-evaluation-rules.md [Self-Review Checklist (S-010)]`
- Self-Review items 2 and 4 (lines 359, 361): include explicit markdown links with relative paths to rules sections
- Synthesis Judgments Summary (line 289): cites `skills/user-experience/rules/synthesis-validation.md` by full path
- Footer (lines 425-431): complete academic citations with authors, year, title, conference; ORCHESTRATION.yaml path added in iter3
- All four Nielsen citations use (a)/(b)/(c) disambiguation consistent with SKILL.md [External References]

**Gaps:**

The Heuristic Coverage Matrix section has no explicit source citation for its format. Given that the Coverage Matrix format is defined in the template itself (not in the rules file), this is a minor gap -- there is no external source to cite. However, a comment noting that the matrix format is a template-defined extension (not from the rules file) would improve traceability clarity.

**Improvement Path:**

Add a comment at the Coverage Matrix section: `<!-- Matrix format: template-defined. Section purpose aligns with heuristic-evaluation-rules.md [Self-Review Checklist (S-010)] item 1 (all heuristics evaluated for every screen). -->`. This closes the traceability gap for this section.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.87 | 0.93 | Add `\| [Methodology](#methodology) \| Non-fill-in prose: 5-step evaluation workflow and AI supplement conditions \|` to the navigation table at position 3 (after Evaluation Context, before Findings by Heuristic). Also reorder nav table entries 7-8 to match document body order: Synthesis Judgments Summary before Strategic Implications. |
| 2 | Methodological Rigor | 0.91 | 0.94 | Add comment immediately after Coverage Matrix table header: `<!-- Add or remove screen columns to match the number of screens in this engagement. Minimum 1 column. The AI supplement row comments below are conditional on AI Product Flag = true. -->` |
| 3 | Evidence Quality | 0.88 | 0.92 | Add inline comment below Evidence field placeholder in the REPEATABLE BLOCK: `<!-- For acceptable vs. unacceptable evidence examples, see heuristic-evaluation-rules.md [Evidence Quality Standard] -->` |

**Composite impact estimate:** Applying all three fixes should raise Internal Consistency to ~0.93 (+0.06), Methodological Rigor to ~0.94 (+0.03), and Evidence Quality to ~0.91 (+0.03). Revised composite estimate:
- Completeness: 0.93 × 0.20 = 0.186
- Internal Consistency: 0.93 × 0.20 = 0.186
- Methodological Rigor: 0.94 × 0.20 = 0.188
- Evidence Quality: 0.91 × 0.15 = 0.137
- Actionability: 0.93 × 0.15 = 0.140 (also benefits from fix 2)
- Traceability: 0.95 × 0.10 = 0.095 (also benefits from fix 2 comment)

Estimated post-fix composite: **0.932** -- above H-13 threshold (0.92) but still below the requested C4 threshold (0.95). Further iteration would be required to reach 0.95.

**Gap to C4 threshold (0.95):** Reaching 0.95 requires additional improvement across all dimensions simultaneously, as the ceiling on each individual dimension must increase. The three fixes above are necessary but not sufficient for C4 passage.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Internal Consistency: chose 0.87 over 0.89 due to nav table ordering inconsistency; Evidence Quality: chose 0.88 over 0.90 due to absence of inline evidence quality guidance)
- [x] Iteration 3 calibration considered (0.843 -> 0.919 trajectory; iter3 improvements are real but do not clear the 0.92 standard threshold or the 0.95 C4 threshold)
- [x] No dimension scored above 0.95 without exceptional evidence (Traceability at 0.94 is justified by comprehensive citations; Actionability at 0.92 is at the top of "strong work with minor refinements needed" band)

---

## Session Context (adv-scorer -> orchestrator)

```yaml
verdict: REVISE
composite_score: 0.906
threshold_h13: 0.92
threshold_c4_requested: 0.95
weakest_dimension: internal_consistency
weakest_score: 0.87
critical_findings_count: 0
iteration: 3
score_trajectory:
  - iter: 1
    score: 0.843
  - iter: 2
    score: 0.919
  - iter: 3
    score: 0.906
note: "Iter3 score (0.906) is lower than iter2 (0.919) -- regression detected. The iter3 revision introduced the non-fill-in Methodology section without adding it to the navigation table, causing the Internal Consistency regression from what would have been an improvement otherwise."
improvement_recommendations:
  - "Add Methodology entry to navigation table and correct nav table ordering to match document body order"
  - "Add Coverage Matrix column-count adjustment comment for non-3-screen evaluations"
  - "Add Evidence Quality Standard reference comment in REPEATABLE BLOCK Evidence field"
```

---

*Score Report Version: 1.0.0*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Agent: adv-scorer*
*Deliverable: `skills/ux-heuristic-eval/templates/heuristic-report-template.md` v1.2.0*
*Created: 2026-03-04*
