# Quality Score Report: bmap-diagnosis-template.md

## L0 Executive Summary

**Score:** 0.865/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.72)

**One-line assessment:** The template is structurally sound with correct section coverage, B=MAP convergence framing, and severity taxonomy, but has four specific gaps — handoff YAML diverges from the agent's own canonical handoff example, confidence calibration guidance is absent from the template, the `on_send` return protocol is not represented anywhere in the template, and no inline guidance directs the filling agent to cite Fogg methodology within each section.

---

## Scoring Context

- **Deliverable:** `skills/ux-behavior-design/templates/bmap-diagnosis-template.md`
- **Deliverable Type:** Output template for ux-behavior-diagnostician agent (B=MAP behavior bottleneck diagnosis)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Threshold:** 0.95 (not 0.92 — per `fogg-behavior-rules.md` QG-001 and quality-enforcement.md criticality levels)
- **Strategy Findings Incorporated:** No
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.865 |
| **Threshold** | 0.95 (C4, per QG-001) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.88 | 0.176 | All 8 required sections present; navigation table present; REPEATABLE BLOCK for interventions; judgment repeatable comment; missing: on_send protocol representation |
| Internal Consistency | 0.20 | 0.84 | 0.168 | B=MAP framing correct; severity taxonomy correct; step 4a/4b alignment correct; handoff success_criteria wording diverges from agent definition canonical; `heart_metric_mapping` vs `affected_heart_dimension` field name mismatch |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Fogg statement format embedded; convergence framing explicit; elimination algorithm 4 steps with 4a/4b; all 3 motivator pairs; 6 simplicity factors; 3 prompt dimensions; REFERENCE-ONLY banner present |
| Evidence Quality | 0.15 | 0.72 | 0.108 | Evidence columns present in all scoring tables; no inline methodology citation guidance; confidence calibration values absent from template (agent must consult separate file); degraded mode placeholder absent |
| Actionability | 0.15 | 0.88 | 0.132 | Clear placeholder syntax; scoring tables pre-populated; intervention repeatable block; wave entry verification section; upstream inputs table; major gap: no filled-example row showing correct evidence citation format |
| Traceability | 0.10 | 0.97 | 0.097 | Template header cites SKILL.md and methodology; Fogg (2020, Chapters 14-15) cited inline for behavior statement; Handoff section cites downstream agent; navigation table anchors all sections; version pinned |
| **TOTAL** | **1.00** | | **0.865** | |

---

## Detailed Dimension Analysis

### Completeness (0.88/1.00)

**Evidence:**

All 8 required sections from `fogg-behavior-rules.md` OUT-001 and the agent's Required Report Structure are present:

1. Executive Summary (L0) — line 29. Contains Primary Bottleneck, Severity, Top Intervention, Key Findings fields. Key Findings has exactly 3 entries (satisfies OUT-003 minimum; template could optionally indicate the 3-5 range).
2. Engagement Context (L1) — line 47. Contains Product, Target Users, Target Behavior Statement (Fogg format embedded), Observation Scope, Upstream Inputs table, Evidence Inventory table with quality classification, Wave Entry Verification.
3. Behavior State Map (L1) — line 77. Contains all 3 motivator pair rows, all 3 motivation dimension rows, all 6 simplicity factor rows with Limiting column, prompt assessment table (4 rows including match-to-state), and Action-Line Position summary.
4. Bottleneck Diagnosis (L1) — line 126. Contains Elimination Algorithm Trace with Steps 1, 2, 3, 4a, 4b — correctly representing both multiple-bottleneck and convergence_timing edge cases.
5. Intervention Recommendations (L1) — line 146. REFERENCE-ONLY banner present (INT-007). REPEATABLE BLOCK markers present. Includes all 6 required fields per INT-002: Description, Target factor, Category, Expected impact, Implementation effort, Classification.
6. Strategic Implications (L2) — line 167. Contains Behavioral Pattern Analysis, Systemic Bottleneck Trends, Behavior Design Maturity (4-option enum), Behavior Change Roadmap.
7. Synthesis Judgments Summary (L1) — line 182. Contains judgment table with 4 columns; repeatable comment present.
8. Handoff Data (L1) — line 194. YAML block present with handoff-v2 fields and ux_ext.

Navigation table (H-23) is present at lines 14-26 with correct anchor links for all 8 sections.

**Gaps:**

1. **On_send protocol not represented.** The agent definition's `<output>` section contains a distinct "On-Send Protocol" YAML block (lines 437-460 of agent definition) that the filling agent must produce when returning results to the orchestrator. This is separate from the file-persisted Handoff Data section and is not represented anywhere in the template. The template only covers the file output, not the orchestrator return payload. The agent must independently remember this second structured output requirement.

2. **Key Findings count guidance absent.** Template shows exactly 3 Key Findings fields in the Executive Summary. The rules specify 3-5 (OUT-003). Template does not communicate the upper bound of 5 or the rationale.

3. **Degraded mode disclosure banner location.** The agent rules (OUT-007) require the degraded mode banner to appear "immediately after the document header" when operating in Qualitative Assessment Mode. The template does not include a placeholder or commented-out banner at the header position. The agent must add it in the correct position from memory.

**Improvement Path:**

- Add a commented-out degraded mode banner placeholder immediately after the document header (before `## Document Sections`), marked as conditional: `<!-- CONDITIONAL: Include this block when operating in Qualitative Assessment Mode (no quantitative behavioral data) -->`
- Add a `<!-- REPEATABLE: Extend to 4-5 findings as evidence supports -->` comment after the 3rd Key Finding entry
- Add a commented `<!-- On-Send Protocol (return to orchestrator, NOT persisted to file) -->` section at the end of the template with the on_send YAML structure

---

### Internal Consistency (0.84/1.00)

**Evidence:**

Correct alignments:
- B=MAP convergence framing: template uses "Overall Motivation: {{Above threshold | Below threshold}}" and "Overall Ability: {{Above threshold | Below threshold}}" — consistent with convergence model, not multiplication
- Severity taxonomy: template uses `{{Critical | Major | Moderate}}` — matches agent definition and fogg-behavior-rules.md SEV-001 (no Minor level)
- Elimination algorithm steps: template shows Steps 1, 2, 3, 4a, 4b — correctly matches agent methodology Phase 3 step numbering, including the explicit 4a/4b distinction for multiple-bottleneck vs. convergence_timing
- Primary Bottleneck options in diagnosis: `{{Prompt | Ability | Motivation | Multiple | Convergence timing}}` — matches all 5 valid outputs of the algorithm
- Prompt type options: `{{Facilitator | Signal | Spark | Absent}}` — matches fogg-behavior-rules.md prompt type definitions

**Gaps:**

1. **Handoff success_criteria text mismatch.** Template (lines 200-201) states:
   - "HEART metric mapping covers the diagnosed bottleneck factor"
   - "Baseline measurement defined for the target behavior"

   Agent definition canonical handoff (lines 411-413) states:
   - "Metric baselines established for affected HEART dimension"
   - "Target thresholds set for post-intervention measurement"

   These are semantically compatible but textually different. A downstream consumer parsing the handoff YAML for specific success_criteria text would see inconsistency depending on whether they compare to the agent definition or the template. The template is the fill-in artifact, so it should be authoritative — but it diverges from the agent's own example without comment.

2. **`heart_metric_mapping` vs `affected_heart_dimension` field name.** Template `ux_ext` uses `heart_metric_mapping` as an array with `bottleneck`, `suggested_metric`, `measurement_approach` sub-fields (lines 216-220). The agent definition's output section canonical handoff YAML (lines 424-427) uses `affected_heart_dimension: "{happiness|engagement|adoption|retention|task_success}"` as a simple string. These are structurally different representations for the same downstream intent. The template is more expressive (array vs. string) but diverges from the agent's own stated contract. A downstream `/ux-heart-metrics` agent reading the handoff would encounter different structures from different invocations depending on which reference was followed.

3. **`task` field in handoff.** Template (line 200) has `task: "Measure behavioral change metrics for diagnosed bottleneck"`. Agent definition canonical handoff (line 411) has `task: "Establish HEART metric baselines for diagnosed behavioral bottleneck"`. Minor wording divergence — not a structural conflict, but adds noise when comparing template output to documentation.

**Improvement Path:**

- Align template success_criteria text with agent definition canonical handoff: update to "Metric baselines established for affected HEART dimension" and "Target thresholds set for post-intervention measurement"
- Resolve `heart_metric_mapping` vs `affected_heart_dimension`: choose one canonical field name and update both the template and agent definition to match; the array form (`heart_metric_mapping`) is more expressive and should be retained if the downstream agent needs it, but the agent definition's output section should match
- Align `task` field text between template and agent definition canonical handoff

---

### Methodological Rigor (0.92/1.00)

**Evidence:**

The template embeds the methodology correctly at every structural point:

- **Fogg behavior statement format:** Line 51 includes the exact format: `"After [{{CONTEXT}}], I will [{{SPECIFIC BEHAVIOR}}]" (Fogg, 2020, Chapters 14-15)` — cites the correct chapters, not Chapter 3 (which the SKILL.md revision history notes was a previous error)
- **Convergence framing in action-line position:** Line 122 correctly frames the summary as a convergence state description
- **6 simplicity factors:** All 6 are present in the table (Time, Money, Physical Effort, Brain Cycles, Social Deviance, Non-Routine)
- **3 motivator pairs:** All 3 present (Sensation, Anticipation, Belonging)
- **3 motivation dimensions:** All 3 present (Intrinsic, Extrinsic, Social)
- **Prompt type classification:** Facilitator | Signal | Spark | Absent — correct 4-option set
- **4-step elimination algorithm with 4a/4b:** Lines 132-136 show all steps including the explicit differentiation between 4a (Multiple bottleneck) and 4b (Convergence timing), with the correct trigger conditions described in the check column
- **Intervention category field:** Template includes a `Category` field row (line 158) with `{{Prompt redesign | Friction reduction | Motivation enhancement | Convergence alignment}}` — this is well-aligned with the intervention category matrix from fogg-behavior-rules.md
- **REFERENCE-ONLY banner:** Present at line 148 with exact text matching agent rules INT-007 requirement

**Gaps:**

1. **Behavior Design Maturity options incomplete.** Template (line 173) shows `{{Nascent | Developing | Mature | Optimized}}` — 4 options. This matches the agent definition. No gap.

2. **Intervention category "Convergence alignment" not in rules.** fogg-behavior-rules.md Intervention Category Matrix lists categories by bottleneck type (Prompt, Ability variants, Motivation, Multiple) but does not define "Convergence alignment" as an explicit category. The template introduces this 4th category in the Category dropdown but the rules file doesn't define when it applies. Minor gap — "Convergence alignment" is logically consistent with the convergence_timing edge case, but is undefined in the rules.

3. **No guidance on algorithm halt behavior.** Steps 4a and 4b in the elimination algorithm trace are shown as parallel rows without a note that they are alternative outcomes (the algorithm reaches step 4 only after steps 1-3 all pass). The check descriptions capture this ("Two or more factors borderline..." and "All factors score 4+...") but a template instruction comment would help the filling agent understand that Steps 1-2-3 are sequential and halt on first failure.

**Improvement Path:**

- Add "Convergence alignment" to the Intervention Category Matrix in fogg-behavior-rules.md (or remove from template if not applicable), so the template and rules are fully aligned
- Add an inline comment above the Elimination Algorithm Trace table noting: `<!-- Steps execute sequentially; halt at first Fail. Steps 4a/4b are alternative outcomes at Step 4, not separate steps. -->

---

### Evidence Quality (0.72/1.00)

**Rationale for 0.72 (not higher):** This dimension evaluates whether the template enables and enforces evidence-quality requirements. A template that leaves agents without calibration guidance, missing degraded-mode cues, and absent methodology citation requirements in each section will produce outputs with lower evidence quality even when the agent intends to comply. Applying leniency bias counteraction: uncertain scores resolved downward.

**Evidence:**

Correct elements:
- Evidence column present in all scoring tables (motivation pairs, ability factors)
- Evidence Inventory table with quality classification (Direct observation / Self-reported / Inferred) — directly implements the evidence quality classification from Phase 1 methodology
- Upstream Inputs table with "Received: Yes/No" — enables upstream evidence traceability

**Gaps:**

1. **Confidence calibration absent from template.** The agent definition (lines 430-432 of agent definition) provides explicit calibration values: 0.5 (qualitative-only), 0.6 (default mixed evidence), 0.7 (quantitative data available). The template handoff block (line 211) simply has `confidence: {{0.0-1.0}}` with no calibration guidance. The filling agent must independently recall the calibration values from a separate file. This is a usability gap that will produce inconsistently calibrated confidence values across different engagements and agents. The calibration table should be embedded as a comment in the template.

2. **No degraded mode banner placeholder.** fogg-behavior-rules.md OUT-007 requires the degraded mode banner "immediately after the document header" when operating in qualitative mode. The template has no placeholder or commented-out banner at the header position (between lines 12 and 14). The agent must remember to insert it in the correct position from memory. Absent structural cuing, the banner may appear in the wrong location or be omitted.

3. **No inline citation guidance per section.** The template sections for Bottleneck Diagnosis, Intervention Recommendations, and Strategic Implications do not include comments directing the filling agent to cite Fogg (2009) or Fogg (2020) for specific claims. The rules (fogg-behavior-rules.md [Traceability], agent self-review checklist item referencing Fogg citations) expect methodology citations throughout the report. A template with no citation prompts will produce reports with inconsistent citation coverage — typically concentrated in the behavior statement but absent from the analysis sections where the methodology is applied.

4. **Evidence quality scale anchors absent from scoring table comments.** The scoring tables show `{{SCORE}}` placeholders with a note that scores are 1-5, but the 1-5 scale anchors (e.g., 1=Absent/Extremely difficult, 5=Strong/Trivial) are not embedded as comments. An agent unfamiliar with the scale must consult fogg-behavior-rules.md separately. Scale anchor reminders embedded as comments would improve score calibration consistency.

**Improvement Path:**

- Add a commented confidence calibration table immediately above the `confidence:` field in the handoff YAML block: `<!-- Calibration: 0.5 qualitative-only (degraded mode), 0.6 default mixed evidence, 0.7 quantitative behavioral data present -->`
- Add a commented-out degraded mode banner placeholder immediately after line 12 (document header metadata), marked conditional
- Add brief inline comments in Bottleneck Diagnosis, Intervention Recommendations, and Strategic Implications sections directing the filling agent to cite Fogg (2009) or (2020) for methodology-derived claims
- Add 1-5 scale anchor comment rows in the motivation and ability scoring tables: `<!-- Scale: 1=Below threshold/Severe friction, 3=Borderline, 5=Above threshold/Trivial -->`

---

### Actionability (0.88/1.00)

**Evidence:**

Strong actionability:
- Placeholder syntax `{{PLACEHOLDER}}` is consistent throughout — agents know exactly what to fill in
- Enum options are provided for every choice field: `{{Critical | Major | Moderate}}`, `{{High | Medium | Low}}`, `{{Direct | Supporting}}` — eliminates ambiguity about valid values
- REPEATABLE BLOCK markers with explicit copy instructions at line 150
- Inline REPEATABLE comment for judgment table at line 190
- Wave entry verification section with specific bypass condition documented
- Upstream inputs table shows "Yes/No" for received status
- Intervention table includes all 6 fields required by INT-002

**Gaps:**

1. **No filled example row.** The template provides no annotated example row showing what a correctly completed entry looks like. For the motivation scoring table, an example like: `| Sensation | Pleasure | Pain | 2 | "78% of users exit the pricing page within 5 seconds; no visible value proposition above the fold [funnel analytics, Direct]" |` would significantly aid consistent output quality. Templates without examples produce high variance in how placeholders are filled.

2. **No explicit instruction for Synthesis Judgments entry count.** The Synthesis Judgments Summary table has a single placeholder row and a REPEATABLE comment, but no guidance on minimum count. fogg-behavior-rules.md CLS-001 requires every AI judgment call to be listed. For a typical engagement, this means 10+ rows (target behavior scoping, 3 motivator pairs, 3 motivation dimensions, 6 simplicity factors, 1 prompt classification, 1 bottleneck classification, 1 severity, 3-5 interventions). The template does not orient the filling agent to the expected volume.

3. **Intervention category field instruction is passive.** The category options `{{Prompt redesign | Friction reduction | Motivation enhancement | Convergence alignment}}` are correct but do not guide the agent on which category applies to which bottleneck. The intervention category matrix (fogg-behavior-rules.md) provides this mapping, but the template could include a brief embedded mapping comment for the most common cases.

**Improvement Path:**

- Add one complete filled example intervention block after the REPEATABLE BLOCK marker section, clearly marked `<!-- EXAMPLE (delete before use) -->`: shows all 6 fields completed with realistic values
- Add a count guidance comment to the Synthesis Judgments table: `<!-- Typical count: 10-15 entries for a complete engagement (target behavior, 3 pairs, 3 dimensions, 6 factors, 1 prompt, 1 bottleneck, 1 severity, 3-5 interventions) -->`
- Add a comment note to the Category field showing the bottleneck-to-category mapping in abbreviated form

---

### Traceability (0.97/1.00)

**Evidence:**

Excellent traceability:
- Template header (lines 1-4) cites SKILL.md, agent, and usage instructions — version-pinned to v1.2.0
- Behavior statement format cites `(Fogg, 2020, Chapters 14-15)` inline at line 51 — corrects the prior Chapter 3 error documented in SKILL.md revision history
- Navigation table maps all 8 sections to their level (L0/L1/L2) and purpose
- Synthesis Judgments Summary section header references `skills/user-experience/rules/synthesis-validation.md`
- Handoff Data section cites `ux-heart-analyst` as downstream consumer
- Wave Entry Verification section references specific Wave 3 completion artifacts (`WAVE-3-SIGNOFF.md`)
- Handoff YAML uses `from_agent: ux-behavior-diagnostician` — explicit agent identity

**Gap:**

1. **No reference to handoff-v2.schema.json in handoff YAML block.** fogg-behavior-rules.md OUT-006 requires the Handoff Data YAML to "conform to `docs/schemas/handoff-v2.schema.json`". The template YAML block has no comment citing this schema. A schema reference comment `<!-- Conforms to docs/schemas/handoff-v2.schema.json -->` above the YAML block would complete the traceability chain.

**Improvement Path:**

- Add `<!-- Conforms to docs/schemas/handoff-v2.schema.json + ux_ext extension (fogg-behavior-rules.md OUT-006) -->` as a comment immediately above the handoff YAML code block

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.84 | 0.92 | Resolve handoff YAML field divergence: align `heart_metric_mapping` vs `affected_heart_dimension` naming between template and agent definition; align success_criteria text; align task field text. Choose one canonical form and update both files. |
| 2 | Evidence Quality | 0.72 | 0.88 | Add confidence calibration comment above the `confidence:` placeholder in handoff YAML. Add commented degraded mode banner placeholder at header position. Add brief citation guidance comments in Bottleneck Diagnosis and Intervention sections. |
| 3 | Evidence Quality | 0.72 | 0.88 | Embed 1-5 scale anchor comments in motivation pair and simplicity factor scoring tables so filling agents do not need to consult fogg-behavior-rules.md for score definitions. |
| 4 | Completeness | 0.88 | 0.95 | Add commented on_send protocol section at end of template, marked `<!-- On-Send Protocol: Return to orchestrator (not persisted to file) -->` with the YAML structure from agent definition lines 437-460. |
| 5 | Completeness | 0.88 | 0.95 | Add conditional degraded mode banner placeholder immediately after the document header (before `## Document Sections`). |
| 6 | Actionability | 0.88 | 0.95 | Add one complete filled example intervention block after the REPEATABLE BLOCK markers, clearly marked as `<!-- EXAMPLE (delete before use) -->`. |
| 7 | Methodological Rigor | 0.92 | 0.95 | Add algorithm execution note above the Elimination Algorithm Trace table: steps 1-3 are sequential and halt on first Fail; steps 4a/4b are alternative outcomes at step 4. Add `<!-- EXAMPLE or N/A note for halt behavior -->`. |
| 8 | Traceability | 0.97 | 1.00 | Add schema reference comment above handoff YAML block: `<!-- Conforms to docs/schemas/handoff-v2.schema.json + ux_ext (fogg-behavior-rules.md OUT-006) -->`. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Evidence Quality: debated between 0.75 and 0.72; chose 0.72 per uncertainty rule; Internal Consistency: debated 0.86/0.84; chose 0.84)
- [x] C4 threshold (0.95) applied, not default C2 threshold (0.92)
- [x] No dimension scored above 0.95 without exceptional evidence (Traceability at 0.97 — justified by 7 specific evidence points with only 1 minor gap)
- [x] Template-document calibration considered: this is a fill-in template artifact, not a standalone analysis document; completeness and evidence quality criteria were interpreted for the template context (does it enable and cue the correct output?) not a completed output context

---

## Handoff Data (Session Context Protocol)

```yaml
verdict: REVISE
composite_score: 0.865
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.72
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Resolve handoff YAML field divergence: heart_metric_mapping vs affected_heart_dimension and mismatched success_criteria text"
  - "Add confidence calibration comment above confidence placeholder in handoff YAML"
  - "Add conditional degraded mode banner placeholder at document header position"
  - "Add 1-5 scale anchor comments in motivation and ability scoring tables"
  - "Add commented on_send protocol section at template end"
  - "Add filled example intervention block marked EXAMPLE (delete before use)"
  - "Add algorithm halt behavior note above Elimination Algorithm Trace table"
  - "Add handoff-v2.schema.json reference comment above YAML block"
```
