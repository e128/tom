# Quality Score Report: bmap-diagnosis-template.md (Iteration 3)

## L0 Executive Summary

**Score:** 0.960/1.00 | **Verdict:** PASS | **Weakest Dimension:** Evidence Quality (0.92)
**One-line assessment:** All seven iter2 improvement recommendations are resolved — algorithm halt comment added, heart_metric_mapping fixed in rules file, version reference updated, Convergence alignment category defined, inline citation guidance added, example intervention block added, synthesis judgments count guidance added — producing a genuinely polished template that meets the C4 threshold of 0.95.

---

## Scoring Context

- **Deliverable:** `skills/ux-behavior-design/templates/bmap-diagnosis-template.md`
- **Deliverable Type:** Output template for ux-behavior-diagnostician agent (B=MAP behavior bottleneck diagnosis)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Threshold:** 0.95 (per `fogg-behavior-rules.md` QG-001 and `quality-enforcement.md` criticality levels)
- **Strategy Findings Incorporated:** No
- **Prior Score:** 0.917 (iter2), 0.865 (iter1)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 3

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.960 |
| **Threshold** | 0.95 (C4, per QG-001) |
| **Verdict** | PASS |
| **Strategy Findings Incorporated** | No |
| **Score Delta from Iter2** | +0.043 |

---

## Iter2 Defect Verification

| # | Iter2 Defect | Status | Evidence |
|---|-------------|--------|----------|
| 1 | Algorithm halt-behavior note absent from Elimination Algorithm Trace | FIXED | Template line 138: `<!-- ALG: Steps 1-3 execute sequentially; halt at first Fail result and output that factor as primary bottleneck. Steps 4a and 4b are alternative outcome branches at Step 4 (not separate sequential steps): 4a applies when multiple factors are borderline; 4b applies when all factors pass but behavior is absent (convergence_timing edge case). After halt, secondary factors may be noted as observations per ALG-002. Cite Fogg (2020) for intervention difficulty gradient ordering; cite Fogg (2009) for convergence model factor independence. -->` |
| 2 | `heart_metric_mapping` still in `fogg-behavior-rules.md` OUT table completeness criteria | FIXED | `fogg-behavior-rules.md` line 341: `ux_ext (bottleneck_factor, severity, affected_heart_dimension)` — field name now consistent with template and agent definition |
| 3 | `fogg-behavior-rules.md` Related Files table showed template at v1.2.0 | FIXED | `fogg-behavior-rules.md` line 392: `bmap-diagnosis-template.md | v1.4.0` — version reference updated |
| 4 | "Convergence alignment" category undefined in `fogg-behavior-rules.md` Intervention Category Matrix | FIXED | `fogg-behavior-rules.md` line 234: new row added — `Convergence timing | Convergence alignment | Contextual trigger timing adjustment; habit stacking to co-locate prompt with existing behavior; environmental context redesign to synchronize M, A, and P above threshold simultaneously (Fogg, 2009) | Medium-High` |
| 5 | No inline citation guidance in Bottleneck Diagnosis or Intervention Recommendations sections | FIXED | Template line 138 (ALG trace): Fogg (2020) + Fogg (2009) inline citation guidance embedded in algorithm comment. Template line 118: `<!-- Cite Fogg (2009) Section 5 "Triggers" for prompt type definitions; cite Fogg (2020) for prompt-as-cheapest-intervention ordering rationale -->`. Motivation (line 84) and ability (line 102) sections also have Fogg citation guidance. |
| 6 | No filled-example intervention block | FIXED | Template lines 161-170: `<!-- EXAMPLE (delete before use): --> <!-- ### Intervention 1: Add Primary CTA Above Fold on Pricing Page --> [full table with all 6 required fields populated with realistic values]` |
| 7 | Synthesis Judgments count guidance absent | FIXED | Template line 210: `<!-- REPEATABLE: Add row for each AI judgment. Typical count: 10-15 entries for a complete engagement. One row per: target behavior scoping (1), each motivator pair (3), each motivation dimension (3), each simplicity factor (6), prompt classification (1), bottleneck classification (1), severity assignment (1), each intervention (3-5). -->` |

**New defects introduced by revision:** None detected. The iter3 revision addressed all 7 iter2 recommendations without introducing regressions. Template version updated to v1.4.0 consistent with rules file reference.

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.97 | 0.194 | All 8 sections structurally intact; algorithm halt note added; all iter2 structural gaps closed; minor residual: Intervention section still uses `{{N}}` placeholder only — no count guidance comment for the 3-5 range |
| Internal Consistency | 0.20 | 0.97 | 0.194 | `affected_heart_dimension` now consistent across template, agent definition, and rules file; bottleneck taxonomy, severity taxonomy, and convergence framing all aligned; Convergence timing row added to rules matches template Category enum |
| Methodological Rigor | 0.20 | 0.97 | 0.194 | All Fogg citations present with section-level specificity; scale anchors correct and complete; elimination algorithm now fully annotated with halt semantics; Convergence alignment category defined in rules; intervention difficulty gradient ordering documented |
| Evidence Quality | 0.15 | 0.92 | 0.138 | Calibration comment, degraded mode block, scale anchors, inline citation guidance, and filled example all present; residual: filled example is in the Intervention section only — Behavior State Map scoring tables still lack a filled example row showing expected evidence citation format |
| Actionability | 0.15 | 0.97 | 0.146 | Synthesis judgments count guidance added; example intervention block demonstrates expected output; all enums, REPEATABLE markers, on-send block, and scale anchors present; template is self-sufficient for agent use without external reference |
| Traceability | 0.10 | 0.97 | 0.097 | Rules file version reference updated to v1.4.0; rules file OUT table uses correct field name; schema reference, on-send block, and agent identity all present; all cross-file references are now consistent |
| **TOTAL** | **1.00** | | **0.963** | |

> **Composite calculation:** (0.97 × 0.20) + (0.97 × 0.20) + (0.97 × 0.20) + (0.92 × 0.15) + (0.97 × 0.15) + (0.97 × 0.10) = 0.194 + 0.194 + 0.194 + 0.138 + 0.146 + 0.097 = 0.963. Reported as 0.960 (rounding from dimension-level evidence to avoid false precision on the 0.003 margin).

---

## Detailed Dimension Analysis

### Completeness (0.97/1.00)

**Evidence:**

All 8 required sections are present and structurally intact per OUT-001:

1. **Executive Summary (L0)** — lines 32-48: Primary Bottleneck, Severity, Top Intervention (with 3 sub-fields), Key Findings (3 entries). Fully populated.
2. **Engagement Context (L1)** — lines 50-78: Product, Target Users, Behavior Statement (Fogg format with citation), Scope, Upstream Inputs table, Evidence Inventory table with quality classification, Wave Entry Verification. Complete.
3. **Behavior State Map (L1)** — lines 80-132: Motivation pair table (3 rows with scale anchor comment at line 84-85), motivation dimension table (3 rows), simplicity factors table (6 rows with scale anchor comment at line 102-103, Limiting column), prompt assessment table (4 rows with citation comment at line 118), Action-Line Position summary. Complete.
4. **Bottleneck Diagnosis (L1)** — lines 134-153: Elimination Algorithm Trace with comprehensive algorithm behavior comment at line 138 (halting logic, step semantics, 4a/4b clarification, citation guidance). Steps 1-4b with check descriptions, Result options, Evidence columns. Primary Bottleneck, Severity, Confidence fields. Complete.
5. **Intervention Recommendations (L1)** — lines 155-184: REFERENCE-ONLY banner, REPEATABLE BLOCK markers, full example block (lines 161-170), active placeholder block with all 6 INT-002 fields. Complete.
6. **Strategic Implications (L2)** — lines 186-199: Pattern Analysis, Trend Analysis, Maturity (4-option enum), Roadmap (3 items). Complete.
7. **Synthesis Judgments Summary (L1)** — lines 201-211: Judgment table with 4 columns (Judgment, Classification, Confidence, Rationale), REPEATABLE comment with count guidance (10-15 typical entries, broken down by type). Complete.
8. **Handoff Data (L1)** — lines 213-241: YAML block with handoff-v2 fields, confidence calibration comment (line 232), ux_ext fields, schema reference (line 216), on-send protocol commented block (lines 244-270). Complete.

**Degraded mode conditional block** (lines 14-15) correctly placed after header per OUT-007.

**Gaps:**

Minor gap: The Intervention Recommendations section uses `### Intervention {{N}}:` but has no comment specifying the expected range (3-5 interventions per INT-001). The count requirement is documented in the rules file (INT-001) but not surfaced as a template comment where the filling agent constructs interventions. This is a low-severity gap — the REPEATABLE BLOCK markers imply repetition, and the rules reference is available, but a `<!-- Produce 3-5 interventions per INT-001 -->` comment would eliminate the need for cross-reference during filling.

**Improvement Path:**
Add `<!-- Produce 3-5 interventions (INT-001). Fewer than 3 limits options; more than 5 diffuses focus. -->` immediately after the REFERENCE-ONLY banner in the Intervention Recommendations section.

---

### Internal Consistency (0.97/1.00)

**Evidence:**

All three previously identified inconsistency loci are resolved:

1. **`affected_heart_dimension` consistency chain:** Template (v1.4.0) line 239 uses `affected_heart_dimension: "{{happiness|engagement|adoption|retention|task_success}}"`. Agent definition line 427 uses `affected_heart_dimension: "{happiness|engagement|adoption|retention|task_success}"`. `fogg-behavior-rules.md` line 341 now uses `ux_ext (bottleneck_factor, severity, affected_heart_dimension)`. All three files consistent.

2. **Convergence timing consistency:** Template intervention category enum at line 178: `{{Prompt redesign | Friction reduction | Motivation enhancement | Convergence alignment}}`. Rules file Intervention Category Matrix line 234: `Convergence timing | Convergence alignment | ...`. The template uses "Convergence alignment" as the category name (appropriate — it names the intervention type, not the bottleneck type); the rules file row header is "Convergence timing" (the bottleneck classification) with "Convergence alignment" as the category. Internally consistent.

3. **Version references:** Template header (line 1): `VERSION: 1.4.0`. `fogg-behavior-rules.md` Related Files table (line 392): `bmap-diagnosis-template.md | v1.4.0`. Consistent.

Preserved correct alignments from prior iterations:
- B=MAP convergence framing: `{{Above threshold | Below threshold}}` — not multiplication
- Severity taxonomy: `{{Critical | Major | Moderate}}` (3-option, no Minor)
- Bottleneck options: `{{Prompt | Ability | Motivation | Multiple | Convergence timing}}`
- Prompt type options: `{{Facilitator | Signal | Spark | Absent}}`
- Step numbering: 1, 2, 3, 4a, 4b
- `success_criteria` and `task` text match agent definition exactly

**Gaps:**

One minor residual: The algorithm comment at line 138 uses the phrase "output that factor as primary bottleneck" while the table header field is `**Primary Bottleneck:**` and the algorithm discipline rule ALG-002 says "primary bottleneck identification." The phrasing is consistent in spirit; this is not a contradiction, only a minor vocabulary variation that causes no functional inconsistency.

The Step 3 check at line 143 reads "Motivation above threshold (at least one motivator pair active)?" — the rules file (MOT-006) states "Majority of dimensions at 1-2 indicates below threshold" which is consistent with this phrasing (one motivator pair active = above threshold). No inconsistency detected.

**Improvement Path:**
No material improvement required for this dimension. Score reflects that all three iter2 inconsistency loci are resolved and no new inconsistencies were introduced.

---

### Methodological Rigor (0.97/1.00)

**Evidence:**

All Fogg methodology elements are correctly and specifically represented:

1. **Scale anchors complete:** Motivation table (lines 84-85): 5-point scale with textual anchors (1=Absent/Actively aversive through 5=Strong/Multiple converging evidence). Ability table (lines 102-103): 5-point scale with textual anchors (1=Extremely difficult/Severe friction through 5=Trivial/Negligible friction). Both cite correct Fogg section sources.

2. **Fogg citations at correct granularity:**
   - Behavior statement: `(Fogg, 2020, Chapters 14-15)` at line 54 — correct section
   - Motivation: `<!-- Cite Fogg (2009) Section 3 "Core Motivators" when classifying motivation type; cite Fogg (2020) when claiming motivation is hardest factor to change -->` at line 84
   - Ability: `<!-- Cite Fogg (2009) Section 4 "Simplicity as a Function of a Person's Scarcest Resource" for factor definitions; cite Fogg (2020) for ability-as-most-common-bottleneck claim -->` at line 102
   - Prompt: `<!-- Cite Fogg (2009) Section 5 "Triggers" for prompt type definitions; cite Fogg (2020) for prompt-as-cheapest-intervention ordering rationale -->` at line 118
   - Algorithm: `<!-- ... Cite Fogg (2020) for intervention difficulty gradient ordering; cite Fogg (2009) for convergence model factor independence. -->` at line 138

3. **Algorithm halt semantics fully documented:** Line 138 comment clearly distinguishes sequential steps (1-3 halt on first Fail) from alternative branches (4a/4b at Step 4). ALG-002 compliance is now structurally enforced by the template comment.

4. **Convergence alignment defined:** The `Convergence timing` row in the rules file Intervention Category Matrix now provides definition ("Contextual trigger timing adjustment; habit stacking to co-locate prompt with existing behavior; environmental context redesign to synchronize M, A, and P above threshold simultaneously") with Fogg (2009) citation and Medium-High effort rating. The template Category enum ("Convergence alignment") maps to this rules entry.

5. **Convergence framing correct:** Action-Line Position summary (line 130) uses "above | below the action line" — threshold-based, not multiplicative.

**Gaps:**

The Behavior State Map motivation pair table (line 84) and ability table (line 102) have section-level citation comments but the individual factor rows do not have example citations. This is appropriate for a template — over-prescribing individual row citations would constrain valid evidence presentation. The section-level comments are sufficient.

One minor observation: The algorithm comment at line 138 says "halt at first Fail result and output that factor as primary bottleneck" — the Step 4a/4b logic where no single factor produces a Fail is explained as alternative outcomes. This is methodologically correct per the algorithm specification, but the phrasing "halt at first Fail" technically does not cover the case where no step Fails (Step 4 is reached because 1-3 all Pass). The comment then correctly handles this with "4a applies when multiple factors are borderline; 4b applies when all factors pass but behavior is absent." The sequential description is complete.

**Improvement Path:**
No material improvement required. Score of 0.97 reflects that all methodology elements are correctly represented with section-specific citation guidance, and the Convergence alignment gap from iter2 is fully resolved.

---

### Evidence Quality (0.92/1.00)

**Evidence:**

Substantial improvements from iter2 verified:

1. **Inline citation guidance:** Four sections now have `<!-- Cite Fogg... -->` comments specifying WHICH Fogg source supports WHICH claim (lines 84, 102, 118, 138). This directly enables filling agents to produce properly cited reports.

2. **Filled example intervention block:** Lines 161-170 contain a complete example:
   ```
   <!-- EXAMPLE (delete before use): -->
   <!-- ### Intervention 1: Add Primary CTA Above Fold on Pricing Page -->
   <!-- | Dimension | Value | -->
   <!-- |-----------|-------| -->
   <!-- | Description | Add a prominent "Start Free Trial" button above the fold on the pricing page; current CTA is below 3 pricing tiers requiring scroll | -->
   <!-- | Target factor | Prompt | -->
   <!-- | Category | Prompt redesign | -->
   <!-- | Expected impact | High | -->
   <!-- | Implementation effort | Low | -->
   <!-- | Classification | Direct | -->
   ```
   This example demonstrates: correct field names, realistic description, specific target factor, valid Category value, correct impact/effort vocabulary, and Direct classification for a primary bottleneck intervention.

3. **Confidence calibration guidance:** Line 232: `# Calibration: 0.5 qualitative-only (degraded mode), 0.6 default mixed evidence, 0.7 quantitative behavioral data present` — provides calibration without requiring external reference.

4. **Degraded mode conditional block:** Lines 14-15 provides the full banner text at the header position per OUT-007.

**Remaining gap:**

The filled example is present only in the Intervention Recommendations section. The Behavior State Map scoring tables (motivation pairs at lines 87-96, simplicity factors at lines 104-111) do not have filled example rows. The scale anchor comments explain what each score MEANS (1=Absent through 5=Strong) but do not show the expected evidence citation FORMAT. A filling agent completing a motivation pair row must construct the evidence entry format independently.

For example, in the motivation pair table, an agent filling the Sensation row might write "No value proposition above fold" (vague, no source) when the expected format (per the rules file Evidence Quality criteria) would be: "78% of users exit pricing page within 5 seconds; no value proposition above fold [funnel analytics, Direct observation]."

This gap is materially smaller than in iter2 — the example intervention block demonstrates the evidence citation philosophy (specific, sourced, quality-classified) and the scale anchors give scoring context. But the gap remains because the scoring table format is distinct from the intervention table format.

**Calibration note:** Scoring 0.92 (not lower) because: (a) four of five iter2 Evidence Quality gaps are resolved; (b) the remaining gap is a guidance completeness gap in a specific table format, not a structural absence; (c) the example intervention block provides substantial evidence quality guidance even if it does not cover the scoring tables; (d) the scale anchor comments provide the interpretation framework that makes scoring table evidence less ambiguous.

**Improvement Path:**
Add one filled example row to the Motivation Assessment table, clearly marked as a comment:
```
<!-- EXAMPLE ROW (delete before use): | Sensation | Pleasure | Pain | 2 | "78% exit pricing page in <5s; no value proposition above fold [funnel data, Direct observation]" | -->
```
This single example row would close the remaining Evidence Quality gap and raise this dimension to 0.96+.

---

### Actionability (0.97/1.00)

**Evidence:**

The iter2 actionability gaps are fully resolved:

1. **Synthesis Judgments count guidance:** Line 210: `<!-- REPEATABLE: Add row for each AI judgment. Typical count: 10-15 entries for a complete engagement. One row per: target behavior scoping (1), each motivator pair (3), each motivation dimension (3), each simplicity factor (6), prompt classification (1), bottleneck classification (1), severity assignment (1), each intervention (3-5). -->` — provides complete enumeration of expected judgment types with counts, eliminating ambiguity about completeness.

2. **Example intervention block:** Lines 161-170 provide a complete annotated example showing exactly what a filled intervention looks like. This is the highest-impact actionability addition from iter3.

3. **On-send protocol block** (lines 244-270): Provides complete orchestrator return payload structure with all field names, types, and value enumerations.

4. **Scale anchor comments** in scoring tables: Filling agents can calibrate scores without consulting the rules file.

The template is now structurally self-sufficient — a filling agent can produce a complete, correctly formatted output by following the template alone, without needing to cross-reference `fogg-behavior-rules.md` for basic format or scoring guidance.

Preserved strong elements from prior iterations:
- Consistent `{{PLACEHOLDER}}` syntax throughout
- Enum options for all choice fields
- REPEATABLE BLOCK markers with explicit copy instructions
- Wave entry verification with specific bypass condition
- All 6 required INT-002 fields in intervention block

**Gaps:**

Minor: The intervention count range (3-5) is not surfaced as a comment in the template's Intervention Recommendations section. Filling agents must consult INT-001 in the rules file to know the expected count. This was identified as a completeness gap above (shared observation) — its actionability impact is low given that the template structure (REPEATABLE BLOCK + example) implies iteration.

**Improvement Path:**
Add `<!-- Produce 3-5 interventions per INT-001 -->` after the REFERENCE-ONLY banner. Low effort, closes both the completeness and actionability minor gaps simultaneously.

---

### Traceability (0.97/1.00)

**Evidence:**

All traceability chains are now complete and consistent:

1. **Cross-file version chain:** Template header `VERSION: 1.4.0` (line 1) matches `fogg-behavior-rules.md` Related Files entry `v1.4.0` (line 392). Chain: template -> rules -> agent definition -> SKILL.md is intact.

2. **Field name traceability:** `affected_heart_dimension` traces from agent definition output specification (line 427) through template (line 239) through rules file completeness criteria (line 341). Three-file consistency verified.

3. **Schema reference:** Line 216: `<!-- Conforms to docs/schemas/handoff-v2.schema.json + ux_ext extension (fogg-behavior-rules.md OUT-006) -->` — provides both the schema source and the rules file reference for the ux_ext extension.

4. **Methodology citation traceability:** Each Fogg citation in template comments specifies the exact source, section, and claim being cited (lines 84, 102, 118, 138). Fogg (2009) vs. Fogg (2020) distinction is maintained correctly throughout.

5. **Agent identity:** On-send protocol block (line 247) `from_agent: ux-behavior-diagnostician` and Handoff YAML (line 219) `from_agent: ux-behavior-diagnostician` are consistent with agent definition `name: jerry:ux-behavior-diagnostician`.

6. **Navigation table:** All 8 sections listed with L0/L1/L2 designations and anchor links (lines 19-28). H-23 compliant.

**Gaps:**

The template header comment at line 3 reads `<!-- SOURCE: SKILL.md [Output Specification], SKILL.md [Methodology] -->`. It does not explicitly reference `fogg-behavior-rules.md` as a source, even though the rules file is the primary methodology enforcement document that this template operationalizes. A reader of the template header would see the agent definition and SKILL.md as sources but not the rules file. This is a minor traceability gap — the handoff YAML comment at line 216 references `fogg-behavior-rules.md OUT-006`, establishing the connection, but the template-level source header is incomplete.

**Improvement Path:**
Update template header line 3 to: `<!-- SOURCE: SKILL.md [Output Specification], SKILL.md [Methodology], fogg-behavior-rules.md [Methodology Rules] -->`

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.92 | 0.96 | Add one filled example row to the Motivation Assessment table in a `<!-- EXAMPLE ROW (delete before use): -->` comment: `| Sensation | Pleasure | Pain | 2 | "78% exit pricing page in <5s; no value proposition above fold [funnel data, Direct observation]" |`. This demonstrates the expected evidence specificity and quality-classification format for scoring tables. |
| 2 | Completeness / Actionability | 0.97 | 0.98 | Add `<!-- Produce 3-5 interventions per INT-001. Fewer than 3 limits options; more than 5 diffuses focus. -->` immediately after the REFERENCE-ONLY banner in the Intervention Recommendations section. Closes both the completeness and actionability minor gaps simultaneously. |
| 3 | Traceability | 0.97 | 0.98 | Update template header line 3 to include `fogg-behavior-rules.md [Methodology Rules]` as a source reference. One-character change; closes the template-level source header gap. |

**Note:** All three remaining recommendations are minor polish items. The template meets the C4 quality gate (>= 0.95) in its current state. These recommendations are documented for completeness per H-15 but are not required for acceptance.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented with specific line references for each score
- [x] Uncertain scores resolved downward: Evidence Quality debated 0.92/0.94 — chose 0.92 because the scoring table example gap is real and distinct from the intervention example; this is the third iteration and the gap was noted in iter1 and iter2 without being addressed for the scoring tables specifically
- [x] C4 threshold (0.95) applied throughout, not the default C2 threshold (0.92)
- [x] No dimension scored above 0.97 without documented exceptional evidence
- [x] Anti-leniency check: actively searched for new defects introduced by the revision — none found; all iter2 recommendations were addressed cleanly
- [x] Calibration anchors applied: 0.97 = genuinely strong work with only minor refinements remaining; 0.92 = acceptable with one identified guidance gap; composite of 0.960 is appropriate for a third iteration that closed all 7 prior recommendations
- [x] Score vs. prior: 0.960 vs. 0.917 — delta of +0.043 is consistent with closing all 7 iter2 recommendations while finding no new defects; score trajectory (0.865 -> 0.917 -> 0.960) shows consistent improvement per revision cycle
- [x] PASS verdict verified: 0.960 >= 0.95 C4 threshold. Composite exceeds threshold by 0.010 margin; not a borderline case.

---

## Handoff Data (Session Context Protocol)

```yaml
verdict: PASS
composite_score: 0.960
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.92
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Add filled example row to Motivation Assessment table showing evidence citation format (priority 1 — closes Evidence Quality residual gap)"
  - "Add intervention count guidance comment (3-5 per INT-001) after REFERENCE-ONLY banner in Intervention Recommendations section"
  - "Update template header line 3 to include fogg-behavior-rules.md as a source reference"
```
