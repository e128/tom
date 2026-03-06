# Quality Score Report: bmap-diagnosis-template.md (Iteration 2)

## L0 Executive Summary

**Score:** 0.917/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.84)
**One-line assessment:** Seven of eight iter1 defects are resolved; the score jumped 52 points (0.865 -> 0.917), but three blocking gaps keep it below the 0.95 C4 threshold: the algorithm halt-behavior note is unaddressed, `heart_metric_mapping` vs `affected_heart_dimension` inconsistency was moved to the rules file rather than resolved across all files, and the "Convergence alignment" intervention category remains undefined in the rules methodology.

---

## Scoring Context

- **Deliverable:** `skills/ux-behavior-design/templates/bmap-diagnosis-template.md`
- **Deliverable Type:** Output template for ux-behavior-diagnostician agent (B=MAP behavior bottleneck diagnosis)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Threshold:** 0.95 (per `fogg-behavior-rules.md` QG-001 and `quality-enforcement.md` criticality levels)
- **Strategy Findings Incorporated:** No
- **Prior Score:** 0.865 (iter1)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.917 |
| **Threshold** | 0.95 (C4, per QG-001) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Score Delta from Iter1** | +0.052 |

---

## Iter1 Defect Verification

| # | Iter1 Defect | Status | Evidence |
|---|-------------|--------|----------|
| 1 | Handoff YAML field divergence: `heart_metric_mapping` vs `affected_heart_dimension` | PARTIALLY FIXED | Template now uses `affected_heart_dimension` (matches agent def), but `fogg-behavior-rules.md` line 340 still says `heart_metric_mapping` in OUT table completeness criteria — inconsistency relocated, not resolved |
| 2 | Handoff `success_criteria` text mismatch | FIXED | Lines 208-209 now match agent definition exactly |
| 3 | Handoff `task` field wording mismatch | FIXED | Line 206 now matches agent definition |
| 4 | Confidence calibration absent from handoff YAML | FIXED | Line 217 comment: `# Calibration: 0.5 qualitative-only...` added |
| 5 | Degraded mode banner placeholder absent | FIXED | Lines 14-15 conditional commented block added at header position |
| 6 | `docs/schemas/handoff-v2.schema.json` reference absent | FIXED | Line 201 comment added above YAML block |
| 7 | On-send protocol not represented in template | FIXED | Lines 229-255 commented on-send block added at template end |
| 8 | Algorithm halt-behavior note absent from Elimination Algorithm Trace | NOT FIXED | No comment above or within the Elimination Algorithm Trace table explaining that steps 1-3 execute sequentially halting on first Fail, and that 4a/4b are alternative outcomes at Step 4 |

**New defects introduced by revision:**
- `fogg-behavior-rules.md` completeness criteria table (line 340) still specifies `heart_metric_mapping` while template now uses `affected_heart_dimension` — partial fix created a new cross-file inconsistency
- `fogg-behavior-rules.md` Related Files table (line 391) references template at v1.2.0; template is now v1.3.0 — version reference stale

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | All 8 sections present; degraded mode block, on-send block, and schema comment added; algorithm halt note still absent |
| Internal Consistency | 0.20 | 0.89 | 0.178 | Success_criteria and task text aligned; affected_heart_dimension aligned with agent def; rules file still says heart_metric_mapping — partial fix created new inconsistency locus |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | Scale anchors added; Fogg citations correct; convergence framing correct; 4-step algorithm correct; "Convergence alignment" category still undefined in rules |
| Evidence Quality | 0.15 | 0.84 | 0.126 | Calibration guidance added; degraded mode block added; scale anchors added; no inline citation guidance in Bottleneck Diagnosis or Strategic Implications sections; no filled-example row |
| Actionability | 0.15 | 0.91 | 0.137 | Strong placeholder syntax; all enums present; on-send block added; scale anchors help calibration; no filled example row; synthesis judgments count guidance still absent |
| Traceability | 0.10 | 0.93 | 0.093 | Schema comment added; version header updated to 1.3.0; rules file version reference to template is stale (v1.2.0 vs v1.3.0); on-send block links back to agent def |
| **TOTAL** | **1.00** | | **0.917** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**

All 8 required sections remain present and structurally intact per OUT-001:

1. Executive Summary (L0) — line 32. Primary Bottleneck, Severity, Top Intervention, Key Findings with 3 entries.
2. Engagement Context (L1) — line 50. Product, Target Users, Behavior Statement (Fogg format), Scope, Upstream Inputs table, Evidence Inventory table with quality classification, Wave Entry Verification.
3. Behavior State Map (L1) — line 80. Motivation pair table (3 rows), motivation dimension table (3 rows), simplicity factors table (6 rows with Limiting column), prompt assessment table (4 rows), Action-Line Position summary.
4. Bottleneck Diagnosis (L1) — line 131. Elimination Algorithm Trace with Steps 1, 2, 3, 4a, 4b with correct check descriptions and result options.
5. Intervention Recommendations (L1) — line 151. REFERENCE-ONLY banner, REPEATABLE BLOCK markers, 6 required fields per INT-002.
6. Strategic Implications (L2) — line 172. Pattern Analysis, Trend Analysis, Maturity (4-option enum), Roadmap.
7. Synthesis Judgments Summary (L1) — line 187. Judgment table with 4 columns, REPEATABLE comment.
8. Handoff Data (L1) — line 199. YAML block with handoff-v2 fields, ux_ext, confidence calibration comment, schema reference comment.

**Additions since iter1 that raised this dimension:**
- Degraded mode conditional block added at lines 14-15 — addresses OUT-007 placement requirement
- On-send protocol commented block added at lines 229-255 — fills the orchestrator return gap
- `docs/schemas/handoff-v2.schema.json` reference comment at line 201
- Scale anchor comments in scoring tables (lines 84, 101)

**Remaining gap:**

The algorithm halt-behavior note is still absent. The Elimination Algorithm Trace table (lines 133-141) shows Steps 1, 2, 3, 4a, 4b without any structural note clarifying:
- Steps 1, 2, 3 execute sequentially; the algorithm halts at the first step that produces a Fail
- Steps 4a and 4b are alternative outcome branches at Step 4, not independent steps
- When step 1 Fails, steps 2-4 are not primary bottleneck checks (they may become secondary observations)

This gap was raised as Priority 7 in iter1 improvement recommendations and explicitly listed as defect #8 in the iter1 score. Its persistence is the clearest unaddressed revision item.

**Improvement Path:**
Add `<!-- ALG: Steps execute sequentially; halt at first Fail result. Steps 4a and 4b are alternative outcomes at Step 4 (not separate sequential steps). Secondary factors may be noted as observations after primary bottleneck is identified per ALG-002. -->` immediately above the Elimination Algorithm Trace table header.

---

### Internal Consistency (0.89/1.00)

**Evidence:**

Improvements from iter1:
- `success_criteria` text now matches agent definition exactly: "Metric baselines established for affected HEART dimension" (line 208) and "Target thresholds set for post-intervention measurement" (line 209) — structural alignment achieved
- `task` field: line 206 now reads "Establish HEART metric baselines for diagnosed behavioral bottleneck" — matches agent definition
- `affected_heart_dimension` field (line 221) as a simple string now aligns with agent definition's handoff canonical (agent def line 427)

Correct alignments preserved from iter1:
- B=MAP convergence framing: `{{Above threshold | Below threshold}}` — not multiplication
- Severity taxonomy: `{{Critical | Major | Moderate}}` (3-option, no Minor)
- Bottleneck options: `{{Prompt | Ability | Motivation | Multiple | Convergence timing}}`
- Prompt type options: `{{Facilitator | Signal | Spark | Absent}}`
- Step numbering: 1, 2, 3, 4a, 4b

**Remaining gap — partial fix created new inconsistency:**

The template (v1.3.0) now uses `affected_heart_dimension` as a simple string in the ux_ext block (line 221):
```yaml
affected_heart_dimension: "{{happiness|engagement|adoption|retention|task_success}}"
```

However, `fogg-behavior-rules.md` Output Format Rules table (line 340) still states:
> `ux_ext (bottleneck_factor, severity, heart_metric_mapping)`

The rules file has not been updated to reflect the field name change from `heart_metric_mapping` to `affected_heart_dimension`. A diagnostician reading `fogg-behavior-rules.md` for completeness requirements would expect to see `heart_metric_mapping` in the output, but the template guides them to produce `affected_heart_dimension`. This is a direct specification-template mismatch.

Additionally, `fogg-behavior-rules.md` Related Files table (line 391) shows the output template at version v1.2.0, but the template is now v1.3.0. This version reference is stale.

These inconsistencies reduce the score below the iter1 internal consistency level improvement that was achievable — the fix addressed the template-to-agent-definition gap but created a template-to-rules-file gap.

**Improvement Path:**
- Update `fogg-behavior-rules.md` OUT table line 340 to read: `ux_ext (bottleneck_factor, severity, affected_heart_dimension)`
- Update `fogg-behavior-rules.md` Related Files table to show template version v1.3.0
- Both changes are in the rules file (a sibling artifact that should have been updated as part of the template revision)

---

### Methodological Rigor (0.93/1.00)

**Evidence:**

Strong improvements from iter1:
- Scale anchor comments added to motivation pair table (line 84): `<!-- Scale: 1=Absent/Actively aversive, 2=Weak/Below threshold, 3=Borderline/Investigate, 4=Present/Above threshold, 5=Strong/Multiple converging evidence -->`
- Scale anchor comments added to simplicity factors table (line 101): `<!-- Scale: 1=Extremely difficult/Severe friction, 2=Difficult/High friction, 3=Moderate/Borderline, 4=Easy/Low friction, 5=Trivial/Negligible friction -->`
- These directly enable correct scoring calibration without requiring the filling agent to consult `fogg-behavior-rules.md` separately

Preserved from iter1 (strong elements):
- Fogg behavior statement format with correct citation: `(Fogg, 2020, Chapters 14-15)` — line 54
- B=MAP convergence framing — not multiplication
- All 3 motivator pairs (Sensation, Anticipation, Belonging)
- All 6 simplicity factors
- 4-step elimination algorithm with 4a/4b
- REFERENCE-ONLY banner in intervention section
- Intervention Category field with `{{Prompt redesign | Friction reduction | Motivation enhancement | Convergence alignment}}`

**Remaining gap:**

The "Convergence alignment" intervention category in line 163:
```
| Category | {{Prompt redesign | Friction reduction | Motivation enhancement | Convergence alignment}} |
```

This category is not defined in `fogg-behavior-rules.md` Intervention Category Matrix (lines 224-234). The Matrix covers Prompt, Ability (6 sub-categories), Motivation, and Multiple — but has no entry for "Convergence alignment" as a standalone category. When a filling agent encounters a `convergence_timing` bottleneck outcome, the template offers "Convergence alignment" as the appropriate category, but the rules file provides no definition for what interventions belong in this category, what effort level they represent, or what examples apply.

This is a methodological gap because it introduces an intervention classification that lacks a normative definition in the methodology rules. A diagnostician applying this template for a `convergence_timing` diagnosis cannot verify their category choice against the rules.

This gap was identified in iter1 and was not closed.

**Improvement Path:**
- Add a "Convergence alignment" row to the Intervention Category Matrix in `fogg-behavior-rules.md`: define the category (e.g., "Address timing misalignment between when M, A, and P converge above threshold"), typical examples (e.g., "contextual trigger timing adjustment; habit stacking to co-locate prompt with existing behavior"), and typical effort (Medium-High)
- This is a rules-file change but the template and rules must be jointly consistent

---

### Evidence Quality (0.84/1.00)

**Evidence:**

Significant improvements from iter1 that raised this dimension from 0.72:
- Confidence calibration comment added in handoff YAML (line 217): `# Calibration: 0.5 qualitative-only (degraded mode), 0.6 default mixed evidence, 0.7 quantitative behavioral data present` — eliminates the need for filling agents to look up calibration values in the agent definition
- Degraded mode conditional block at lines 14-15 — provides both the placement cue and the full banner text for the filling agent
- Scale anchor comments in motivation and ability tables — directly reduces the evidence quality gap caused by ambiguous scoring

**Remaining gaps:**

1. **No inline citation guidance in analysis sections.** The Bottleneck Diagnosis section (line 131), Intervention Recommendations section (line 151), and Strategic Implications section (line 172) contain no inline comments directing the filling agent to cite Fogg methodology for each claim. The `fogg-behavior-rules.md` Quality Gate Dimension Mapping (line 366) explicitly lists "Fogg citations present for methodology claims" as a Methodological Rigor criterion. Without citation cues in the template sections where methodology is applied, filling agents predictably produce reports with Fogg citations concentrated in the behavior statement and absent from the analysis sections. This gap was identified in iter1 and was not addressed.

   For example, the Bottleneck Diagnosis section has no comment like:
   `<!-- Cite Fogg (2020) for the elimination algorithm ordering rationale at Step 1 (prompt-first per intervention difficulty gradient); cite Fogg (2009) for convergence model at Steps 2-3 -->`

2. **No filled-example row.** The template provides no annotated example showing correct evidence citation format in any scoring table. An example row such as:
   `| Sensation | Pleasure | Pain | 2 | "78% of users exit pricing page within 5 seconds; no value proposition above fold [funnel analytics, Direct observation]" |`
   would demonstrate the expected specificity and classification format. This gap was identified in iter1 and was not addressed.

   Without an example, evidence entries across engagements will vary in specificity and citation format, reducing the downstream synthesis confidence that can be assigned to any given factor assessment.

**Calibration note:** Scoring 0.84 (not lower) reflects that two of the four iter1 Evidence Quality gaps were meaningfully addressed — calibration guidance and degraded mode placement are genuinely useful additions. The two remaining gaps (citation guidance, filled example) are important but not fatal; they represent guidance completeness, not structural absence.

**Improvement Path:**
- Add `<!-- Cite Fogg (2020) for intervention difficulty gradient; Fogg (2009) for convergence model factor independence -->` above the Elimination Algorithm Trace table
- Add `<!-- Cite Fogg (2009) for simplicity factor definitions; Fogg (2020) for ability-as-most-common-bottleneck claim -->` above the ability scoring table
- Add one complete filled example intervention block after the REPEATABLE BLOCK markers, clearly marked `<!-- EXAMPLE (delete before use): -->`

---

### Actionability (0.91/1.00)

**Evidence:**

Strong improvements from iter1:
- Scale anchor comments in scoring tables now let filling agents calibrate scores without external reference
- On-send protocol block (lines 229-255) gives filling agents the complete orchestrator return payload structure — previously they had to construct this from memory

Preserved strong elements from iter1:
- Consistent `{{PLACEHOLDER}}` syntax throughout
- Enum options for all choice fields
- REPEATABLE BLOCK markers with explicit copy instructions
- Wave entry verification with specific bypass condition
- Intervention table with all 6 required fields per INT-002

**Remaining gaps:**

1. **No filled example row.** This gap affects both Evidence Quality and Actionability. For actionability specifically: the absence of an annotated example intervention block means filling agents cannot verify their output format against a concrete reference. Templates without examples produce higher variance in output quality because each filling agent interprets the placeholder semantics independently.

2. **Synthesis Judgments count guidance absent.** The Synthesis Judgments Summary table (lines 191-193) still has only a single placeholder row and a `<!-- REPEATABLE: Add row for each AI judgment -->` comment. No guidance on expected count. Per `fogg-behavior-rules.md` CLS-001 and the agent methodology, a complete engagement typically produces 10-15 judgment entries (target behavior scoping, 3 motivator pairs, 3 motivation dimensions, 6 simplicity factors, 1 prompt classification, 1 bottleneck classification, 1 severity, 3-5 interventions). Without count guidance, filling agents may produce incomplete Synthesis Judgments tables — listing only the most obvious judgments and omitting the routine factor ratings. This gap was identified in iter1 and was not addressed.

**Improvement Path:**
- Add `<!-- Typical count: 10-15 entries for a complete engagement. One row per: target behavior scoping, each motivator pair (3), each motivation dimension (3), each simplicity factor (6), prompt classification (1), bottleneck classification (1), severity assignment (1), each intervention (3-5). -->` immediately above the Synthesis Judgments table
- Add one complete filled example intervention block after the REPEATABLE BLOCK markers

---

### Traceability (0.93/1.00)

**Evidence:**

Strong improvements from iter1:
- `docs/schemas/handoff-v2.schema.json` reference added at line 201: `<!-- Conforms to docs/schemas/handoff-v2.schema.json + ux_ext extension (fogg-behavior-rules.md OUT-006) -->` — directly closes the iter1 gap
- Template version updated to v1.3.0 in the header (line 1)
- On-send protocol block (lines 229-255) includes explicit agent identity `from_agent: ux-behavior-diagnostician` and references the output path pattern

Preserved strong elements from iter1:
- Template header cites SKILL.md, agent, date, and usage instruction
- Behavior statement cites `(Fogg, 2020, Chapters 14-15)` inline
- Navigation table maps all 8 sections with L0/L1/L2 designations
- Synthesis Judgments header references `skills/user-experience/rules/synthesis-validation.md`
- Handoff YAML identifies `to_agent: ux-heart-analyst`

**Remaining gap:**

`fogg-behavior-rules.md` Related Files table (line 391) references the output template at v1.2.0:
```
| Output template | skills/ux-behavior-design/templates/bmap-diagnosis-template.md | v1.2.0 | ...
```

The template is now at v1.3.0. This stale version reference means the rules file's dependency matrix does not accurately reflect the current template version. A developer checking the rules file to understand the dependency chain would see v1.2.0 and might retrieve or reference an outdated version.

This is a minor but real traceability gap — the version chain is broken in the rules file even as the template itself has a correct version header.

**Improvement Path:**
- Update `fogg-behavior-rules.md` Related Files table to show `bmap-diagnosis-template.md | v1.3.0`
- This change is in the rules file, not the template, but the template scoring should reflect the full traceability chain

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.89 | 0.95 | Update `fogg-behavior-rules.md` line 340 OUT table to replace `heart_metric_mapping` with `affected_heart_dimension`. Update Related Files table to show template version v1.3.0. These two changes close the partial-fix inconsistency that remained from iter1. |
| 2 | Completeness | 0.93 | 0.97 | Add algorithm halt-behavior comment immediately above the Elimination Algorithm Trace table: `<!-- ALG: Steps execute sequentially; halt at first Fail. Steps 4a/4b are alternative outcomes at Step 4 (not separate steps). After halt, secondary factors may be noted as observations per ALG-002. -->` |
| 3 | Methodological Rigor | 0.93 | 0.97 | Add "Convergence alignment" row to `fogg-behavior-rules.md` Intervention Category Matrix (lines 224-234) with category definition, example interventions, and typical effort level. This closes the rules-vs-template gap for the fourth intervention category. |
| 4 | Evidence Quality | 0.84 | 0.92 | Add inline citation guidance comments in the Bottleneck Diagnosis section (cite Fogg 2020 for algorithm ordering) and Intervention Recommendations section (cite Fogg 2020 for intervention categories). One-line comments suffice. |
| 5 | Actionability | 0.91 | 0.96 | Add Synthesis Judgments count guidance comment: `<!-- Typical count: 10-15 entries for a complete engagement (target behavior, 3 pairs, 3 dimensions, 6 factors, 1 prompt, 1 bottleneck, 1 severity, 3-5 interventions). -->` |
| 6 | Evidence Quality | 0.84 | 0.92 | Add one complete filled example intervention block after the REPEATABLE BLOCK markers, clearly marked `<!-- EXAMPLE (delete before use) -->`. This is the most impactful single change for Evidence Quality. |
| 7 | Traceability | 0.93 | 0.97 | Update `fogg-behavior-rules.md` Related Files table entry for the output template from v1.2.0 to v1.3.0. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented with specific line references for each score
- [x] Uncertain scores resolved downward: Evidence Quality debated 0.84/0.86 — chose 0.84 given two of four iter1 gaps remain unaddressed; Internal Consistency debated 0.89/0.91 — chose 0.89 because partial fix introduced a new inconsistency locus
- [x] C4 threshold (0.95) applied throughout, not the default C2 threshold (0.92)
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] First-draft calibration considered: this is iteration 2 with significant improvement (+0.052); scoring above 0.90 is appropriate but the four remaining gaps (algorithm note, rules file consistency, "Convergence alignment", citation guidance) are concrete and specific
- [x] Anti-leniency check: actively looked for new defects introduced by the revision — found the partial-fix inconsistency (heart_metric_mapping still in rules file), stale version reference, and confirmed the two persistent iter1 gaps (algorithm halt note, "Convergence alignment" definition)
- [x] Score vs. prior: 0.917 vs. 0.865 — delta of +0.052 is consistent with closing 7 of 8 iter1 defects while identifying 2 new minor defects and confirming 2 persistent gaps

---

## Handoff Data (Session Context Protocol)

```yaml
verdict: REVISE
composite_score: 0.917
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.84
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Update fogg-behavior-rules.md line 340 to replace heart_metric_mapping with affected_heart_dimension in OUT table completeness criteria"
  - "Update fogg-behavior-rules.md Related Files table: template version v1.2.0 -> v1.3.0"
  - "Add algorithm halt-behavior comment above Elimination Algorithm Trace table (steps 1-3 sequential halt; 4a/4b are alternatives at Step 4)"
  - "Add Convergence alignment row to fogg-behavior-rules.md Intervention Category Matrix with definition and examples"
  - "Add inline Fogg citation guidance comments in Bottleneck Diagnosis and Intervention Recommendations sections"
  - "Add Synthesis Judgments count guidance comment (typical 10-15 entries per complete engagement)"
  - "Add one filled example intervention block marked EXAMPLE (delete before use)"
```
