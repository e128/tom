# Quality Score Report: JTBD Analysis Report Template (job-statement-template.md)

## L0 Executive Summary

**Score:** 0.797/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.74)

**One-line assessment:** The template has solid methodological coverage and internal structure but fails on three linked gaps -- a missing Hiring Criteria section required by the agent definition, absent source-tier guidance in citation placeholders, and ambiguous/unexplained placeholders in the L1 Job Inventory -- that together pull the score below the 0.85 revision threshold and well below the 0.95 C4 threshold.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/templates/job-statement-template.md`
- **Deliverable Type:** Design (output template for ux-jtbd-analyst agent)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.797 |
| **C4 Threshold** | 0.95 (H-13, C4 criticality) |
| **Standard Threshold** | 0.92 (H-13, C2+ deliverables) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

> **Note on C4 threshold:** The scoring prompt specifies a C4 quality threshold of 0.95. The composite of 0.797 is well below both the 0.92 standard threshold and the 0.95 C4 threshold. Verdict is REVISE (score >= 0.50; substantive rework needed on specific identified gaps before re-scoring).

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.73 | 0.146 | Missing dedicated Hiring Criteria section; job type split (Functional/Social/Emotional) absent as distinct L1 subsections |
| Internal Consistency | 0.20 | 0.82 | 0.164 | Formulas and force model consistent; `{{CONFIDENCE_NUMERIC}}` contradicts agent def's `confidence: MEDIUM` string default in handoff YAML |
| Methodological Rigor | 0.20 | 0.87 | 0.174 | All 4 Ulwick outcome formats represented; 8-step job map present; P-022 disclosure, judgments summary, and validation section all included |
| Evidence Quality | 0.15 | 0.74 | 0.111 | Citation placeholders present but zero source-tier (Tier 1/2/3) guidance in any placeholder; rules file mandates tier classification on every citation |
| Actionability | 0.15 | 0.80 | 0.120 | Most placeholders clear; `{{BLOCKERS}}`, `{{INNOVATION_TRAJECTORY}}`, `{{NET_FORCE_INTERPRETATION}}`, and hiring criteria rows in Job Inventory are under-specified or unexplained |
| Traceability | 0.10 | 0.82 | 0.082 | Header/footer cross-refs present; synthesis-validation.md and jtbd-methodology-rules.md cited in comments; rating scale anchor cross-reference absent from switch force and criterion placeholders |
| **TOTAL** | **1.00** | | **0.797** | |

---

## Detailed Dimension Analysis

### Completeness (0.73/1.00)

**Evidence:**

The template contains 9 sections (header block, L0 Executive Summary, L1 Job Inventory, L1 Opportunity Score Matrix, L1 Switch Force Analysis, L1 Job Map, L2 Synthesis and Prioritization, L2 Confidence Summary, Handoff Data). The nav table at lines 14-26 lists all sections with anchor links -- H-23/H-24 compliant.

**Gaps:**

1. **Missing Hiring Criteria section (HIGH IMPACT).** The agent definition (`ux-jtbd-analyst.md` lines 329-340) lists "L1: Hiring Criteria | Criterion table with measurement and weight" as a required output section. Phase 5 of the methodology (agent def lines 259-293) specifies hiring criteria with weighting (deal-breaker=3, important=2, nice-to-have=1) and composite rank computation. The SKILL.md output template (lines 508-511) has an explicit Hiring Criteria section. This section is entirely absent from `job-statement-template.md`. There are criterion rows embedded inside the L1 Job Inventory block (lines 68-72) but they are unlabeled and a filling agent would not know these map to hiring criteria from Phase 5.

2. **Absent Functional/Social/Emotional job type split (MEDIUM IMPACT).** The agent definition required sections table (lines 330-340) specifies separate "L1: Functional Jobs", "L1: Social Jobs", "L1: Emotional Jobs" sections. The SKILL.md output template (lines 471-484) shows these as three separate subsection tables. The template collapses all job types into a single "L1: Job Inventory" repeatable block. While the block includes a `{{CLASSIFICATION}}` field, there is no structural separation of job types, which means the rendered output cannot be scanned by type.

3. **Missing Competitive Job Analysis section.** The agent definition capabilities section (line 99-100) lists "Competitive job analysis" as a key capability, and Phase 1 Step 4 (lines 133-138) requires cataloging the competitive landscape. No competitive job analysis section appears in the template.

**Improvement Path:**
Add a dedicated "L1: Hiring Criteria" section after the Job Map section with the criterion table (Criterion | Measurement | Weight | Minimum Threshold | Current Score columns). Restructure the Job Inventory into three subsections: Functional Jobs, Social Jobs, Emotional Jobs, each as a repeatable block. Add a minimal "L1: Competitive Landscape" subsection under Job Inventory or as a standalone L1 section.

---

### Internal Consistency (0.82/1.00)

**Evidence:**

- Opportunity score formula at line 63 (`{{OPPORTUNITY_SCORE}} = {{IMPORTANCE}} + max({{IMPORTANCE}} - {{SATISFACTION}}, 0)`) exactly matches the rules file formula (line 101 of jtbd-methodology-rules.md).
- Net force formula at line 105 (`({{PUSH_RATING}} + {{PULL_RATING}}) - ({{ANXIETY_RATING}} + {{HABIT_RATING}}) = {{DRIVING_TOTAL}} - {{RESISTING_TOTAL}} = **{{NET_FORCE}}**`) matches the rules file formula (line 198).
- Four force directions (Push=Drives change, Pull=Drives change, Anxiety=Resists change, Habit=Resists change) at lines 100-103 match the rules file table exactly.
- P-022 disclosure text at lines 180-182 is substantively consistent with the agent definition's transparency requirements.
- Handoff YAML `success_criteria` at lines 213-215 is consistent with the agent definition's output filtering requirements.

**Gaps:**

1. **`confidence` field type mismatch in Handoff Data.** The template YAML at line 224 shows `confidence: {{CONFIDENCE_NUMERIC}}` with the placeholder name implying a numeric (0.0-1.0) value. The agent definition's session context on-send block (lines 345-358) specifies `confidence: MEDIUM` as the default -- a string level. The handoff-v2 schema (per agent-development-standards.md) defines `confidence` as a number (0.0-1.0). The agent definition's on-send block uses the enum label ("MEDIUM") rather than the numeric value, which creates ambiguity: should the template produce the numeric float or the string label? The placeholder name `{{CONFIDENCE_NUMERIC}}` resolves this in favor of the schema spec, but the agent definition's own example contradicts it.

2. **`blockers` YAML field type ambiguity.** Line 223 shows `blockers: {{BLOCKERS}}` with no type hint or example. The handoff-v2 schema defines `blockers` as an array. An agent filling this template without schema knowledge might write `blockers: none` (string) instead of `blockers: []` (empty array) or `blockers: ["[PERSISTENT] Missing primary data"]` (array with string entries).

**Improvement Path:**
Add a YAML comment on line 224: `# numeric 0.0-1.0: MEDIUM=0.5, HIGH=0.8, LOW=0.3`. Add a YAML comment on line 223: `# array; use [] if no blockers; prefix persistent blockers with [PERSISTENT]`.

---

### Methodological Rigor (0.87/1.00)

**Evidence:**

- All four Ulwick canonical outcome formats are present in the rules file and the Job Map comment at line 133 provides the "Minimize time/likelihood/variability" guidance directly in the template. The fourth format ("Minimize the variability of [quality measure]") added in jtbd-methodology-rules.md v1.2.0 is included.
- All 8 Ulwick universal job steps are present (Define through Conclude) with the correct labels at lines 123-130.
- The Switch Force Analysis section at lines 92-109 implements the Moesta four forces model correctly.
- The P-022 disclosure section at lines 180-201 correctly includes: transparency statement, synthesis judgments enumeration, and validation required table -- all three required elements per synthesis-validation.md.
- The Confidence Summary section at line 172-178 correctly includes per-job confidence classification with justification and validation method columns.
- The low-confidence majority banner instruction at line 178 cross-references the synthesis-validation.md protocol correctly.
- The Job Inventory block includes a criteria sub-table (lines 68-72) consistent with the hiring criteria methodology from Phase 5.

**Gaps:**

1. **Job Map comment at line 133 is insufficient for outcome format guidance.** The comment reads `<!-- Outcome format: "Minimize the time/likelihood/variability of [action/outcome/measure]" -->` but this compresses three distinct formats into one ambiguous pattern. The agent filling Step 1's `{{DEFINE_OUTCOMES}}` might write "Minimize the time/likelihood/variability of defining requirements" rather than selecting the appropriate format for the outcome type. A more explicit multi-line comment listing all four formats separately would improve methodological adherence.

2. **No omitted-step guidance for Job Map.** Line 132 has `{{OMITTED_STEPS_RATIONALE}}` but no comment explaining when omission is appropriate. The agent definition (Phase 4, Step 1) says "Not every job uses all 8 steps -- omit steps that do not apply, but document the omission rationale." A comment with 1-2 examples would help.

**Improvement Path:**
Expand the Job Map outcome format comment to list all four formats on separate lines. Add a comment to `{{OMITTED_STEPS_RATIONALE}}` with an example: `<!-- If no steps omitted: "All 8 steps apply." Example omission: "Step 7 (Modify) omitted -- job execution is one-shot with no feedback loop." -->`.

---

### Evidence Quality (0.74/1.00)

**Evidence:**

The template does include evidence-citation placeholders in key locations:
- `{{EVIDENCE_SOURCES}}` in the Job Inventory table (line 66)
- `{{PUSH_SOURCE}}`, `{{PULL_SOURCE}}`, `{{ANXIETY_SOURCE}}`, `{{HABIT_SOURCE}}` in the Switch Force table (lines 100-103)
- `{{CONF_JUSTIFICATION}}` and `{{CONF_VALIDATION_METHOD}}` in the Confidence Summary
- `{{PRIMARY_EVIDENCE_TYPE}}` in the P-022 disclosure

**Gaps:**

1. **Zero source-tier guidance in any citation placeholder (HIGH IMPACT).** The rules file (jtbd-methodology-rules.md lines 308-314) mandates HARD rules: "Every job statement MUST cite at least one evidence source with its tier classification." Citation format is `Source: {author or source name} ({year}) [Tier {N}]`. None of the evidence placeholders in the template instruct the filling agent to include a tier classification. `{{EVIDENCE_SOURCES}}` at line 66 has no comment explaining the required format. `{{PUSH_SOURCE}}` at line 100 has no comment explaining Tier 1/2/3. An agent filling these without reading the rules file could write `{{EVIDENCE_SOURCES}} = "competitor reviews"` rather than `"Competitor App Store reviews (2024-2026) [Tier 1]"`.

2. **`{{CONF_JUSTIFICATION}}` has no format guidance.** The rules file (lines 226-229) defines specific HIGH/MEDIUM/LOW justification criteria. The placeholder at line 174 gives no hint about what justification entails or how to format it. Compare with the rules file example: "Job statement synthesized from competitor reviews and domain literature without direct user validation."

3. **`{{PRIMARY_EVIDENCE_TYPE}}` in the P-022 disclosure (line 182) is under-specified.** The agent needs to produce something like "secondary research (competitor reviews, domain literature)" but the placeholder name alone is insufficient -- no comment explains what values are valid here.

**Improvement Path:**
Add a comment after line 66: `<!-- Format: "Source name (Year) [Tier 1|2|3]". Tier 1=primary research, Tier 2=published methodology, Tier 3=tertiary. Multiple sources: comma-separated. HARD rule: no Tier 3 sole source. -->`. Add a similar format comment for each `{{*_SOURCE}}` placeholder in the Switch Force section. Add a comment for `{{CONF_JUSTIFICATION}}` with an example value. Add a comment for `{{PRIMARY_EVIDENCE_TYPE}}` with example values.

---

### Actionability (0.80/1.00)

**Evidence:**

Most placeholders are clearly named and self-explanatory:
- `{{JOB_ID}}`, `{{JOB_TITLE}}`, `{{SITUATION}}`, `{{MOTIVATION}}`, `{{EXPECTED_OUTCOME}}` in Job Inventory are unambiguous
- `{{RANK_1_JOB_ID}}` through `{{RANK_3_CLASS}}` in the Opportunity Score Matrix are clear
- `{{DOWNSTREAM_AGENT}}` in the YAML is clear
- REPEATABLE BLOCK comments at lines 50-51, 94, 117 explain what to duplicate

**Gaps:**

1. **Hiring criteria rows in Job Inventory are unexplained (HIGH IMPACT).** Lines 68-72 contain a criterion sub-table with `{{CRITERION_1}}`, `{{MEASUREMENT_1}}`, `{{WEIGHT_1}}`, `{{SCORE_1}}` placeholders inside the Job Inventory repeatable block. There is no comment explaining what these represent or that they correspond to Phase 5 hiring criteria. An agent filling this template would not know these rows are for hiring criteria (which the template label calls only "Criterion"). The disconnect between the Phase 5 methodology and these rows is not bridged.

2. **`{{BLOCKERS}}` in the YAML handoff is ambiguous (MEDIUM IMPACT).** No type example or comment. The agent could produce a string, a null, or an array. The handoff-v2 schema requires an array.

3. **`{{INNOVATION_TRAJECTORY}}` in L2 Synthesis has no guidance (MEDIUM IMPACT).** Line 166 is a bare placeholder with the comment on line 164 only naming the sub-section. No hint about what content is expected. Compare with `{{CROSS_JOB_PATTERNS}}` at line 143 which at least has the comment "List 3-5 cross-job patterns (e.g., shared triggers, force patterns, underserved steps)."

4. **`{{NET_FORCE_INTERPRETATION}}` has no format guidance (LOW IMPACT).** Line 107 gives this placeholder no example. The rules file (lines 200-205) defines interpretation by net force sign (positive/zero/negative) with strategic implications. A comment referencing this table would help.

5. **`{{CRITICAL_VALIDATION_NEEDED}}` in the L0 Executive Summary is unexplained (LOW IMPACT).** Line 42 has no comment or example about what form this should take.

**Improvement Path:**
Add a comment above the criterion sub-table (line 68): `<!-- Hiring criteria from Phase 5: criteria users apply when "hiring" a product. Deal-breaker=weight 3, Important=weight 2, Nice-to-have=weight 1. -->`. Add comment to `{{INNOVATION_TRAJECTORY}}` (line 166): `<!-- Describe where AI augmentation opportunities exist, competitive differentiation direction, and organizational recommendations. 2-4 sentences. -->`. Add comment to `{{NET_FORCE_INTERPRETATION}}` (line 107): `<!-- Positive net force: switching likely; focus on reducing anxiety/habit. Zero: uncertain; target weakest resisting force. Negative: switching unlikely; must increase push/pull or reduce barriers. -->`. Fix `{{BLOCKERS}}` with a YAML comment.

---

### Traceability (0.82/1.00)

**Evidence:**

- Template header (lines 1-4) cites: skill, agent, methodology references (Christensen 2016, Ulwick 2016, Moesta 2020), and a usage instruction.
- Footer (lines 244-247) cites: template version, sub-skill, project, methodology, agent, and parent skill.
- Line 190 comment cross-references `jtbd-methodology-rules.md` for synthesis judgment enumeration guidance.
- Line 201 comment cross-references `synthesis-validation.md` for MEDIUM-to-HIGH validation methods.
- Line 178 comment cross-references `synthesis-validation.md` for low-confidence majority banner.
- L0 Executive Summary caveat (line 44) ties the output to the overall synthesis confidence.

**Gaps:**

1. **No cross-reference to jtbd-methodology-rules.md for rating scales.** The switch force rating `{{PUSH_RATING}}` (1-5) and the job inventory importance/satisfaction scores (1-10) have no comment pointing agents to the anchor definitions in jtbd-methodology-rules.md (lines 186-193 for force scale, lines 108-111 for importance/satisfaction scales). An agent filling these numbers has no way to know the anchor definitions without reading the rules file.

2. **No cross-reference for Service Classification thresholds.** The `{{SERVICE_CLASSIFICATION}}` field at line 64 and the Opportunity Score Matrix column `{{RANK_1_CLASS}}` have no comment explaining the Underserved/Appropriately served/Overserved thresholds (>=10/6-9/<6). Line 88 has a comment with the thresholds only in the Opportunity Score Matrix section but not in the Job Inventory block.

3. **No traceability to handoff-v2 schema for the Handoff Data YAML block.** The schema reference (`docs/schemas/handoff-v2.schema.json`) is acknowledged in SKILL.md as "planned" but the template does not include even a comment pointing agents to the handoff schema for validation.

**Improvement Path:**
Add a comment to the `{{PUSH_RATING}}` row in the Switch Force table: `<!-- 1-5 integer scale per jtbd-methodology-rules.md [Switch Force Analysis Rules]. 1=Minimal, 3=Moderate, 5=Dominant. -->`. Add a comment to the `{{SERVICE_CLASSIFICATION}}` field: `<!-- See jtbd-methodology-rules.md [Opportunity Scoring Rules]: >=10=Underserved, 6-9=Appropriately served, <6=Overserved. -->`. Add a YAML comment above the handoff block referencing the schema location.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.73 | 0.88 | Add a dedicated "### L1: Hiring Criteria" section (after Job Map, before Synthesis) with criterion table columns: Criterion, Measurement, Weight (3/2/1), Minimum Threshold, Current Score/10. Update the nav table entry. Add a brief comment explaining the deal-breaker/important/nice-to-have weighting scheme. This section is explicitly required by the agent definition and SKILL.md output template but is entirely absent. |
| 2 | Evidence Quality | 0.74 | 0.88 | Add source-tier format comments to every evidence placeholder: `{{EVIDENCE_SOURCES}}` (line 66), `{{PUSH_SOURCE}}`/`{{PULL_SOURCE}}`/`{{ANXIETY_SOURCE}}`/`{{HABIT_SOURCE}}` (lines 100-103). Required format per jtbd-methodology-rules.md: `Source: {name} ({year}) [Tier 1|2|3]`. This directly addresses the HARD citation rule that is not reflected anywhere in the template. |
| 3 | Completeness | 0.73 | 0.88 | Split the L1 Job Inventory into three subsections: "### Functional Jobs", "### Social Jobs", "### Emotional Jobs", each with its own repeatable block. This aligns the template with both the agent definition's required sections table and the SKILL.md output template. Update the nav table. |
| 4 | Actionability | 0.80 | 0.90 | Label and explain the hiring criteria sub-table inside the Job Inventory block (lines 68-72): add a comment above it saying "Hiring criteria -- see Phase 5 methodology. Deal-breaker weight=3, Important=2, Nice-to-have=1." Also add guidance comments to `{{INNOVATION_TRAJECTORY}}`, `{{NET_FORCE_INTERPRETATION}}`, `{{BLOCKERS}}`, and `{{CRITICAL_VALIDATION_NEEDED}}`. |
| 5 | Internal Consistency | 0.82 | 0.92 | Fix the `confidence` field in the Handoff YAML: add a comment clarifying whether the value is a 0.0-1.0 numeric (per handoff-v2 schema) or the string enum "MEDIUM/HIGH/LOW" (per agent def on-send example). Recommend numeric per schema spec. Fix `{{BLOCKERS}}` with a YAML comment showing array syntax. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Completeness held at 0.73 despite partial coverage; Evidence Quality held at 0.74 despite some placeholder presence)
- [x] First-draft calibration considered: this is iteration 1; a composite of 0.797 on iteration 1 is within the expected 0.65-0.80 first-draft range
- [x] No dimension scored above 0.95 (highest is Methodological Rigor at 0.87)

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.797
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.74
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add dedicated L1 Hiring Criteria section (required by agent definition and SKILL.md)"
  - "Add source-tier format comments to all citation placeholders (HARD rule in jtbd-methodology-rules.md)"
  - "Split L1 Job Inventory into Functional/Social/Emotional subsections"
  - "Label and explain hiring criteria sub-table rows inside Job Inventory block"
  - "Fix confidence field type ambiguity and blockers array format in Handoff YAML"
```

---

*Score Report Version: 1.0.0*
*Agent: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-jtbd/templates/job-statement-template.md`*
*Companion artifacts checked: `jtbd-methodology-rules.md`, `ux-jtbd-analyst.md`, `SKILL.md` (ux-jtbd), `synthesis-validation.md`*
*Created: 2026-03-04*
