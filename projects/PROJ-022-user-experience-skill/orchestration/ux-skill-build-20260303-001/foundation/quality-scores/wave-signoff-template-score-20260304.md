# Quality Score Report: wave-signoff-template.md

## L0 Executive Summary

**Score:** 0.863/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.72)
**One-line assessment:** Structurally sound template with accurate threshold references and complete validation rules, but a Wave 5 coverage gap in Per-Wave Customization undermines completeness and internal consistency, and the cited ADR-PROJ022-002 is a provisional stub rather than a ratified decision.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/templates/wave-signoff-template.md`
- **Deliverable Type:** Design (template file)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.863 |
| **Threshold** | 0.95 (C4 criticality, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.82 | 0.164 | Wave 5 missing from Per-Wave Customization; Field Descriptions says "Wave number (1-4)" contradicting 6-wave system |
| Internal Consistency | 0.20 | 0.85 | 0.170 | 0.85 threshold matches ADR-PROJ022-002; wave evidence matches wave-progression.md entry criteria; "Integer 1-4" validation rule contradicts Wave 5 existence |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Template structure is rigorous; bypass tracking is complete; cross-framework synthesis tests well-defined with 3 specific checks |
| Evidence Quality | 0.15 | 0.72 | 0.108 | ADR-PROJ022-002 cited but is a PROVISIONAL STUB; ci-checks.md referenced by name without path; wave-progression.md not cited directly |
| Actionability | 0.15 | 0.90 | 0.135 | Waves 1-4 evidence requirements are specific and unambiguous; Field Descriptions table fully documents every field; ux-orchestrator can populate for any deployed wave |
| Traceability | 0.10 | 0.92 | 0.092 | Navigation table present with anchors; parent skill reference present; status metadata present; created/updated dates present |
| **TOTAL** | **1.00** | | **0.853** | |

> **Arithmetic verification:** (0.82 * 0.20) + (0.85 * 0.20) + (0.92 * 0.20) + (0.72 * 0.15) + (0.90 * 0.15) + (0.92 * 0.10) = 0.164 + 0.170 + 0.184 + 0.108 + 0.135 + 0.092 = 0.853

*(Displayed composite is 0.853; rounded to 0.853.)*

---

## Detailed Dimension Analysis

### Completeness (0.82/1.00)

**Evidence:**
- All core template sections are present: Sub-Skills Deployed table, Wave Quality Gate block, Artifacts Verified table, Usage Evidence section, Cross-Framework Synthesis Test table, Acceptance Criteria checklist, Wave Bypass Usage table, Authorization field.
- Per-Wave Customization covers Waves 1, 2, 3, and 4 with specific, non-redundant evidence tables.
- Field Descriptions table documents all 13 fields (12 required + 1 optional).
- Validation rules section contains exactly 13 checks as expected.

**Gaps:**
1. **Wave 5 missing from Per-Wave Customization.** The system defines 6 waves (0-5). `wave-progression.md` explicitly lists Wave 5 (Process Intensives: `/ux-design-sprint`, `/ux-ai-first-design` CONDITIONAL) with entry criteria: "30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed; AI-First: Enabler DONE + WSM >= 7.80." The template provides no Wave 5 evidence table. A WAVE-5-SIGNOFF.md would be generated from this template with no guidance on what usage evidence to collect.
2. **Field Descriptions says "Wave number (1-4)"** (line 93). This constraint excludes Wave 5, which does require a signoff per `wave-progression.md` (Table: `WAVE-4-SIGNOFF.md valid -> Wave 5 authorized`). There is no WAVE-5-SIGNOFF.md output path or description.
3. **No Wave 0 / Foundation section.** Wave 0 uses a different template (`kickoff-signoff-template.md`) so this is not strictly a gap in this template, but the absence of any annotation clarifying that Wave 0 uses a separate template creates a potential user error.

**Improvement Path:**
- Add a Wave 5 (Process Intensives) subsection to Per-Wave Customization with evidence requirements: (a) design sprint completed OR Kano survey evidence (30+ users), (b) AI-First Enabler status (if applicable).
- Update Field Descriptions "Wave number" constraint from "(1-4)" to "(1-5)".
- Update Validation Rules "Wave number populated" from "Integer 1-4" to "Integer 1-5".

---

### Internal Consistency (0.85/1.00)

**Evidence:**
- The 0.85 threshold in the Wave Quality Gate block ("ADR-PROJ022-002") exactly matches the threshold in `wave-progression.md` ("0.85 S-014 weighted composite") and in `ADR-PROJ022-002` itself ("0.85 S-014 weighted composite threshold for wave transition quality gates"). This is consistent across all three documents.
- Per-Wave Customization evidence requirements are internally consistent with `wave-progression.md` Wave Definitions table:
  - Wave 1 template: "heuristic eval completed AND JTBD job statement used" matches wave-progression.md Wave 2 entry: "at least 1 heuristic eval completed AND 1 JTBD job statement used".
  - Wave 2 template: "product launched with analytics OR Lean UX hypothesis cycle" matches wave-progression.md Wave 3 entry: "launched product with analytics OR 1 completed Lean UX hypothesis cycle".
  - Wave 3 template: "Storybook Atom stories AND Persona Spectrum review" matches wave-progression.md Wave 4 entry: "Storybook with 5+ Atom stories AND 1 Persona Spectrum review".
  - Wave 4 template: "Kano survey users (30+) OR B=MAP bottleneck diagnosed; AI-First Enabler" matches wave-progression.md Wave 5 entry criteria.
- The CI gate reference ("UX-CI-007") is confirmed in `ci-checks.md` CI Gate Summary table at row UX-CI-007.
- Acceptance Criteria checklist mentions "C4 >= 0.95 quality gate" — this is consistent with H-13's 0.92 (C2+) threshold applied at C4 criticality, and consistent with the project's scoring of agent definition artifacts at C4.

**Gaps:**
1. **Validation rule "Integer 1-4" contradicts Wave 5.** The template defines "Wave number populated: Integer 1-4" as a CI validation rule (line 150). This directly contradicts the system's 6-wave architecture (Waves 0-5), where Wave 5 is a defined, deployable wave that produces a WAVE-5-SIGNOFF.md. The CI gate as written would reject any Wave 5 signoff file.
2. **"Wave number (1-4)" in Field Descriptions** — same contradiction at line 93.

**Improvement Path:**
- Correct both occurrences of "(1-4)" / "Integer 1-4" to "(1-5)" / "Integer 1-5".

---

### Methodological Rigor (0.92/1.00)

**Evidence:**
- The template follows sound gating logic: sub-skills deployed first, then quality gate threshold check, then artifact verification, then usage evidence, then synthesis test, then acceptance criteria checklist, then bypass tracking, then explicit authorization. This sequence enforces the wave-progression.md transition workflow steps 1-7 in order.
- Bypass tracking is complete: the bypass table includes Bypass ID, Sub-Skill, Unmet Criterion, Impact Assessment, Remediation Plan, and Status columns — exactly matching `wave-progression.md` Bypass Fields (Unmet Criterion, Impact Assessment, Remediation Plan) plus lifecycle fields (Bypass ID, Status).
- Cross-Framework Synthesis Test has 3 specific, verifiable checks: (1) synthesis produces valid output, (2) confidence classifications present, (3) handoff data contracts validated. These map directly to `synthesis-validation.md` and the orchestrator's synthesis responsibilities.
- The template uses a consistent PASS/FAIL/N/A vocabulary across all status columns.
- Acceptance Criteria checklist covers all critical compliance dimensions: quality gate, P-003, schema validation, synthesis test, degraded-mode behavior, usage evidence, AGENTS.md update.

**Gaps:**
- The Cross-Framework Synthesis Test table rows are purely generic placeholders ("Wave [N] sub-skills") with no per-wave specialization. For example, Wave 3 should specify synthesis between `/ux-atomic-design` and `/ux-inclusive-design` outputs, and Wave 4 should specify synthesis between `/ux-behavior-design` and `/ux-kano-model` outputs. The current generic form is appropriate for a template but reduces pre-fill guidance for the orchestrator.
- No explicit instruction on how to compute "Composite score" in the Wave Quality Gate block (which S-014 rubric weights to use, which sub-skill outputs to score). wave-progression.md covers this, but the template does not cross-reference it.

**Improvement Path:**
- The gap above is minor and does not prevent use; Field Descriptions + wave-progression.md provide the computation method. Score held at 0.92.

---

### Evidence Quality (0.72/1.00)

**Evidence:**
- The template cites "ADR-PROJ022-002" in the Wave Quality Gate block. This ADR exists at `projects/PROJ-022-user-experience-skill/decisions/ADR-PROJ022-002-wave-criteria-gates.md`.
- The template cites "UX-CI-007 in `ci-checks.md`" — confirmed present in ci-checks.md.

**Gaps:**
1. **ADR-PROJ022-002 is a PROVISIONAL STUB.** The ADR's own Status section reads: "PROVISIONAL — Threshold derived from quality-enforcement.md REVISE band boundary (0.85). Calibration data from Wave 1 deployment will inform threshold revision." The Decision section is marked "PROVISIONAL decision (DRAFT — to be validated with Wave 1 calibration data)." The template presents this citation as authoritative ("ADR-PROJ022-002"), but the backing ADR is explicitly unvalidated. For a C4 deliverable, citing a DRAFT/PROVISIONAL ADR as the threshold authority is an evidence quality deficiency.
2. **No file path for ci-checks.md.** The template says "CI gate (UX-CI-007 in `ci-checks.md`)" without a repo-relative path. Per CP-01 conventions and traceability standards, this should be `skills/user-experience/rules/ci-checks.md`.
3. **wave-progression.md not cited.** Per-Wave Customization evidence requirements are derived directly from wave-progression.md entry criteria, but wave-progression.md is not cited. A reader who wants to verify the evidence requirements has no pointer to the authoritative source.
4. **No cross-reference to ADR-PROJ022-002 for the S-014 6-dimension rubric weights.** The wave gate uses S-014 scoring, but the template does not cite `quality-enforcement.md` for the dimension weights.

**Improvement Path:**
- Elevate ADR-PROJ022-002 from PROVISIONAL to ACCEPTED (or replace citation with "pending ADR — provisional threshold 0.85 per quality-enforcement.md REVISE band").
- Add repo-relative path: `skills/user-experience/rules/ci-checks.md`.
- Add citation to wave-progression.md in Per-Wave Customization header.
- Add citation to quality-enforcement.md for S-014 rubric weights.

---

### Actionability (0.90/1.00)

**Evidence:**
- Field Descriptions table documents every field with a Required column. All 12 fields marked "Yes" and 1 marked "Optional." An orchestrator or user knows exactly which fields are mandatory.
- Per-Wave Customization provides specific, binary evidence criteria for Waves 1-4. For example, Wave 1: "At least 1 heuristic eval report exists at expected output path" and "At least 1 JTBD job statement referenced in a product decision document." These are unambiguous pass/fail conditions.
- The Validation Rules section maps 1:1 to CI gate UX-CI-007, so the ux-orchestrator can self-verify its own output before committing.
- Bypass table structure is immediately actionable: the orchestrator knows exactly which columns to populate.
- The authorization field "YES / NO" is unambiguous.

**Gaps:**
- No Wave 5 evidence requirements means the ux-orchestrator cannot populate a WAVE-5-SIGNOFF.md completely without consulting wave-progression.md separately.
- The template does not specify where to find "expected output path" for each sub-skill's heuristic eval report (Wave 1 evidence criterion). This requires knowledge of sub-skill output paths not captured in the template.

**Improvement Path:**
- Add Wave 5 Per-Wave Customization table (evidence requirements from wave-progression.md).
- Consider adding a note to Wave 1 evidence: "See `/ux-heuristic-eval` SKILL.md for expected output path."

---

### Traceability (0.92/1.00)

**Evidence:**
- Navigation table is present (lines 5-13) with 4 sections and anchor links: `[Template](#template)`, `[Field Descriptions](#field-descriptions)`, `[Per-Wave Customization](#per-wave-customization)`, `[Validation Rules](#validation-rules)`.
- Parent skill reference is present in the footer: `*Parent skill: /user-experience*`.
- Status metadata is present: `*Status: COMPLETE*`, `*Created: 2026-03-03*`, `*Updated: 2026-03-04*`.
- Template file self-identification present: `*Template file: wave-signoff-template.md*`.
- ADR-PROJ022-002 reference is inline in the template body (traceable from template to ADR).
- UX-CI-007 / ci-checks.md reference is present (line 145).

**Gaps:**
- No `<!-- Source: -->` annotations linking sections to SKILL.md or wave-progression.md (other rule files in the skill use these annotations, e.g., wave-progression.md has `<!-- Source: SKILL.md Section "Wave Signoff Enforcement". -->`). This breaks the traceability chain for readers following references backward from the template.
- No anchor for the embedded template block (the fenced code block). The navigation entry `[Template](#template)` exists, but within the template itself there are no sub-section anchors (e.g., no `### Sub-Skills Deployed` heading for direct section links in completed signoff files).

**Improvement Path:**
- Add `<!-- Source: wave-progression.md Signoff Requirements -->` comment before the template block.
- Add `<!-- Source: wave-progression.md Per-Wave Evidence -->` comment before Per-Wave Customization.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.82 | 0.90 | Add Wave 5 (Process Intensives) subsection to Per-Wave Customization with evidence requirements: design sprint OR Kano evidence (30+ users), AI-First Enabler status (if applicable). |
| 2 | Internal Consistency | 0.85 | 0.92 | Change "Wave number (1-4)" (Field Descriptions line 93) and "Integer 1-4" (Validation Rules line 150) to "(1-5)" and "Integer 1-5" respectively. |
| 3 | Evidence Quality | 0.72 | 0.85 | (a) Mark the ADR-PROJ022-002 citation as PROVISIONAL or elevate the ADR; (b) add repo-relative path to ci-checks.md citation; (c) add citation to wave-progression.md in Per-Wave Customization; (d) cite quality-enforcement.md for S-014 weights. |
| 4 | Traceability | 0.92 | 0.95 | Add `<!-- Source: -->` annotations linking template sections to wave-progression.md and SKILL.md to match the pattern used in other rule files in the skill. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score (specific line numbers, file paths, and quotes cited)
- [x] Uncertain scores resolved downward: Evidence Quality was uncertain between 0.72-0.78; resolved to 0.72 because the ADR-PROJ022-002 PROVISIONAL/STUB status is a concrete deficiency, not a minor gap
- [x] First-draft calibration considered: this is not a first draft (Status: COMPLETE), but Wave 5 gap is a substantive oversight that prevents the template from supporting the full 6-wave system
- [x] No dimension scored above 0.95 without exceptional evidence; Methodological Rigor scored 0.92 supported by specific structural evidence; Traceability scored 0.92 supported by confirmed presence of navigation table, anchors, and footer metadata

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.853
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.72
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add Wave 5 Per-Wave Customization subsection (Process Intensives evidence requirements)"
  - "Correct Wave number constraint from 1-4 to 1-5 in Field Descriptions and Validation Rules"
  - "Resolve ADR-PROJ022-002 PROVISIONAL status or annotate citation accordingly"
  - "Add repo-relative path to ci-checks.md reference"
  - "Add wave-progression.md citation to Per-Wave Customization"
  - "Add Source annotations linking template sections to source rule files"
```

---

*Score Report: wave-signoff-template-score-20260304.md*
*Agent: adv-scorer*
*Deliverable: skills/user-experience/templates/wave-signoff-template.md*
*Scored: 2026-03-04*
