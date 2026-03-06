# Quality Score Report: HEART Metrics Sub-Skill SKILL.md

## L0 Executive Summary

**Score:** 0.951/1.00 | **Verdict:** PASS | **Weakest Dimension:** Evidence Quality (0.93)
**One-line assessment:** All 7 iter2 fixes are verifiably present and correct -- the three citation gaps (Baymard Institute with URL, Reichheld 2003 HBR full entry, Few 2006 full entry) are resolved, goal adjudication and signal-to-metric edge case guidance are added, the tools/allowed-tools duplication is eliminated, and the AGENTS.md line-number reference is replaced with a section name -- pushing the composite to 0.951 and clearing the C4 threshold of 0.95.

---

## Scoring Context

- **Deliverable:** `skills/ux-heart-metrics/SKILL.md`
- **Deliverable Type:** Design (Sub-skill specification)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Prior Score:** 0.928 (iter2, `skills/ux-heart-metrics/output/quality-scores/skill-md-iter2-score.md`)
- **Delta from iter2:** +0.023

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.951 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | PASS |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.96 | 0.192 | tools/allowed-tools duplication resolved; all 13 sections intact; PLANNED annotations consistent; wave note still absent from When to Use but covered in header and Purpose |
| Internal Consistency | 0.20 | 0.95 | 0.190 | tools duplication eliminated; AGENTS.md section-name reference present; T2/Systematic/Sonnet consistent; Context7 MCP tools absent from allowed-tools while described as planned -- disclosed but structurally unresolved |
| Methodological Rigor | 0.20 | 0.96 | 0.192 | Goal adjudication guidance added (lines 308-309); signal-to-metric edge case guidance added (lines 354-355); Phase 5 dashboard citation added (Few 2006 + Rodden 2010); all prior methodology strengths retained |
| Evidence Quality | 0.15 | 0.93 | 0.1395 | Baymard full citation with URL (line 802); Reichheld 2003 HBR full bibliographic entry (line 803); Few 2006 full entry (line 804); Baymard is a dataset reference rather than a named study but URL is provided |
| Actionability | 0.15 | 0.95 | 0.1425 | Comprehensive: 5-phase workflow, worked example, 3 invocation options, 6 workflows, Measurement Plan mode; {target} placeholder still lacks [LOW confidence] annotation in blank template |
| Traceability | 0.10 | 0.95 | 0.095 | AGENTS.md section-name reference verified; Baymard/Reichheld/Few all in References with full entries; heart-methodology-rules.md PLANNED in both References and Degraded Mode |
| **TOTAL** | **1.00** | | **0.951** | |

---

## Fix Verification (Iter2 Claimed Fixes)

The following table verifies each of the 7 claimed iter2 fixes against the actual SKILL.md content:

| Fix | Claim | Verification | Status |
|-----|-------|-------------|--------|
| 1 | Baymard Institute full bibliographic citation with URL | Line 802: `Baymard Institute. "UX Benchmark" dataset (2020-2024). Available at https://baymard.com/ux-benchmark.` | VERIFIED |
| 2 | NPS Reichheld 2003 HBR formal citation | Line 803: `Reichheld, F.F. (2003). "The One Number You Need to Grow." *Harvard Business Review*, 81(12), 46-54.` | VERIFIED |
| 3 | Phase 5 dashboard citation with Few 2006 and Rodden et al 2010 | Line 439 (Phase 5 output text) cites `Few, S. (2006). *Information Dashboard Design.* Analytics Press` and `Rodden et al., 2010`; full entry at line 804 | VERIFIED |
| 4 | Goal adjudication guidance for multiple plausible goals | Lines 308-309: `> **Goal adjudication:** When multiple goals are plausible for a single dimension, select the goal most directly tied to the product's current lifecycle stage.` | VERIFIED |
| 5 | Signal-to-metric edge case guidance | Lines 354-355: `> **Signal-to-metric edge cases:** When a single signal maps to multiple metrics, prefer the metric with the shortest feedback loop... When no signal exists for a goal, flag this as a measurement gap...` | VERIFIED |
| 6 | Removed duplicate tools field (allowed-tools is authoritative) | Frontmatter contains only `allowed-tools` (lines 30-35); `tools` field absent | VERIFIED |
| 7 | Replaced AGENTS.md line 309 with section name reference | Line 231: `...registered in \`AGENTS.md\` under the User-Experience Skill Agents section...` (no line number) | VERIFIED |

---

## Detailed Dimension Analysis

### Completeness (0.96/1.00)

**Evidence:**

All structural completeness requirements are met in v1.2.0:

1. **`allowed-tools` correct and unambiguous** -- Lines 30-35 declare T2 tools (Read, Write, Edit, Glob, Grep). The `tools` field that created the duplication in iter2 is now absent. The frontmatter is unambiguous about permitted tool access.
2. **`version: "1.2.0"`** -- Present in YAML frontmatter (line 3). Matches semantic versioning pattern.
3. **`activation-keywords`** -- Present with 13 keyword entries (lines 14-28), covering all primary and secondary routing terms.
4. **`heart-methodology-rules.md` marked [PLANNED: Wave 2 Phase 2]** -- Consistently annotated in both Degraded Mode section and References section.
5. **All 13 structural sections** -- Document Sections nav table, Triple-Lens table, Purpose, When to Use, Available Agents, Invoking an Agent, P-003 Compliance, Methodology, MCP Integration, Output Specification, Cross-Framework Integration, Synthesis Hypothesis Validation, Constitutional Compliance, Quick Reference, References -- all present and in correct order.
6. **Deployment status disclosed** -- Purpose section (line 104) explicitly states "Wave 2 sub-skill" with stub status. Document header (line 46) identifies "Wave 2 (Lean UX + Measurement)."

**Gaps:**

1. **Wave availability note absent from When to Use Activation Path table** -- The Activation Path section describes routing without a note such as "Available after Wave 2 entry criteria are met (see `skills/user-experience/SKILL.md` [Wave Architecture])." This is a LOW-impact gap: the wave assignment is covered in the header and Purpose section, so readers can find it, but the When to Use section is not fully self-contained on this point.

**Improvement Path:**

Add "Available after Wave 2 entry criteria are met (see `skills/user-experience/SKILL.md` [Wave Architecture])" to the When to Use section's Activation Path table or as a callout. This is a minor refinement; the major completeness gaps have all been resolved.

---

### Internal Consistency (0.95/1.00)

**Evidence:**

The v1.2.0 revision resolves both major internal consistency gaps identified in iter2:

1. **`tools`/`allowed-tools` duplication eliminated** -- The frontmatter no longer contains a `tools` field. Only `allowed-tools` is declared. The ambiguity about whether Bash was permitted has been removed.
2. **AGENTS.md section-name reference** -- Line 231 now reads: "The `ux-heart-analyst` agent IS registered in `AGENTS.md` under the User-Experience Skill Agents section, ensuring agent-level discoverability. Verified 2026-03-04." No fragile line number. Independently verified: AGENTS.md line 309 confirms the registration exists in the "User-Experience Skill Agents" section.
3. **T2/Systematic/Sonnet consistent** -- Available Agents table (line 161: T2, Systematic, Sonnet), P-003 diagram (line 246: T2, Systematic, Sonnet), and parent SKILL.md registration all consistent.
4. **MCP dependency claims verified** -- No REQ MCPs confirmed against mcp-coordination.md [MCP Dependency Matrix] (`-- | -- | -- | -- | ENH | --` for `/ux-heart-metrics`). Free ($0) cost tier claim consistent with mcp-coordination.md [Cost Tiers].
5. **Synthesis confidence levels consistent** -- MEDIUM for goal-metric mapping, LOW for threshold recommendations in both this SKILL.md (lines 99-100, 692-693) and synthesis-validation.md [Sub-Skill Synthesis Output Map] (lines 69-70).
6. **Context7 "planned" annotation retained** -- MCP Integration section (line 458) explicitly states `ux-heart-analyst` is not yet listed in `mcp-coordination.md` [Context7 Usage] agent table, with annotation that integration is planned for Wave 2.

**Gaps:**

1. **Context7 MCP tools absent from `allowed-tools` while described as planned in MCP Integration** -- The `allowed-tools` field lists T2 tools only (Read, Write, Edit, Glob, Grep). The MCP Integration section describes planned Context7 usage with protocol steps. This is a forward-looking inconsistency: the document describes behavior that the current tool declaration does not support. The "planned" annotation discloses the gap, but a reader inspecting `allowed-tools` alone would not know Context7 usage is described elsewhere. This is the only remaining consistency gap and is substantially mitigated by the explicit disclosure note.

**Improvement Path:**

When the Wave 2 MCP coordination update is completed, add `mcp__context7__resolve-library-id` and `mcp__context7__query-docs` to `allowed-tools`. Until then, the current disclosure annotation is the appropriate interim approach.

---

### Methodological Rigor (0.96/1.00)

**Evidence:**

The v1.2.0 revision closes all three iter2 methodology gaps:

1. **Goal adjudication guidance added (lines 308-309)** -- A blockquote note appears under Step 1 (Goal Definition): "When multiple goals are plausible for a single dimension, select the goal most directly tied to the product's current lifecycle stage. Document rejected alternatives in the GSM worksheet notes column." This is practical, actionable, and appropriately placed at the point of use.

2. **Signal-to-metric edge case guidance added (lines 354-355)** -- A blockquote note appears under Step 3 (Metric Specification): "When a single signal maps to multiple metrics, prefer the metric with the shortest feedback loop for iteration decisions. When no signal exists for a goal, flag this as a measurement gap requiring instrumentation investment before the metric can be tracked." This addresses both the one-to-many and zero-metric edge cases.

3. **Dashboard specification citation added (line 439)** -- Phase 5 output description now reads: "Dashboard layout follows metric visualization best practices per Few, S. (2006). *Information Dashboard Design.* Analytics Press; and Rodden, K., Hutchinson, H., & Fu, X. (2010). 'Measuring the User Experience on a Large Scale.' Proc. CHI 2010, for HEART-specific metric card organization." Two distinct citations are provided: one for general dashboard design principles and one for HEART-specific metric organization.

4. **All prior methodology strengths retained** -- 5-phase GSM workflow with inputs/outputs for each phase, HEART dimensions table with example signals, dimension selection guidelines (5 considerations), leading/lagging signal distinction, 8-field metric specification format, and Threshold Fallback Methodology (4-step graduated approach) are all intact.

5. **NPS calibration guidance retained** -- Happiness dimension (line 278) still includes "calibrate against Bain & Company's industry-specific NPS benchmarks or internal historical data."

**Gaps:**

No significant methodology gaps remain. The dashboard specification guidance (Phase 5) remains somewhat high-level -- it specifies visualization types (counter, time series, funnel) but does not provide decision criteria for choosing among them. This is a minor refinement opportunity, not a material methodology gap.

**Improvement Path:**

Add a brief one-row decision table for visualization type selection (e.g., "counter for current-state absolute values; time series for trend tracking; funnel for multi-step completion flows") to Phase 5 activities. This is a SOFT-tier enhancement, not required for PASS.

---

### Evidence Quality (0.93/1.00)

**Evidence:**

The v1.2.0 revision completes the bibliographic framework with three new formal entries:

1. **Baymard Institute full citation (line 802)** -- `Baymard Institute. "UX Benchmark" dataset (2020-2024). Available at https://baymard.com/ux-benchmark. Cart abandonment and checkout usability benchmarks. Note: practitioners should verify current benchmark values against the latest dataset release.` This provides: organization name, publication name, year range, URL, and a practitioner caveat about data currency. The citation is traceable and verifiable.

2. **Reichheld 2003 HBR full bibliographic entry (line 803)** -- `Reichheld, F.F. (2003). "The One Number You Need to Grow." *Harvard Business Review*, 81(12), 46-54. Originally developed at Bain & Company with Satmetrix Systems. Industry-specific NPS benchmarks available via Bain & Company.` This is a complete academic-style citation with author, year, title, journal, volume, issue, and pages. It correctly attributes both the publication and the Bain & Company practical benchmark source.

3. **Few 2006 full bibliographic entry (line 804)** -- `Few, S. (2006). *Information Dashboard Design: The Effective Visual Communication of Data.* Analytics Press. Best practices for metric visualization and dashboard layout.` Complete book citation with full title, publisher, and purpose annotation.

4. **HEART primary citations retained** -- Rodden, K., Hutchinson, H., & Fu, X. (2010) CHI '10 proceedings citation preserved with full details at line 799-800.

5. **All evidence claims link to verifiable sources** -- NPS calibration guidance (line 278) now has a formal bibliographic backing (Reichheld 2003). Dashboard methodology (Phase 5, line 439) now has explicit citations (Few 2006, Rodden 2010). Checkout benchmark (lines 350-352, 619) now has a traceable URL.

**Gaps:**

1. **Baymard Institute citation is a dataset reference, not a named study** -- The citation identifies the "UX Benchmark" dataset rather than a specific published study with findings. The 85% checkout completion target cited in the worked example (line 619: `>= 85% (Baymard Institute e-commerce checkout usability benchmark)`) traces to this dataset but the specific benchmark value is not pinned to a year or report version within the citation. A note like "verify current benchmark values against the latest dataset release" (present in line 802) partially addresses this but does not resolve the specificity gap for the 85% figure itself.

2. **`heart-methodology-rules.md` planned reference** -- The Degraded Mode section (line 471) cites `skills/ux-heart-metrics/rules/heart-methodology-rules.md` [PLANNED: Wave 2 Phase 2] as a content source. The methodology self-containedness claim in Degraded Mode rests on a planned artifact. This is appropriately disclosed but represents a pending evidence commitment.

**Improvement Path:**

If a more specific Baymard Institute study citation becomes available (e.g., the specific cart abandonment report with year and finding statement), replace the dataset URL with the study citation. The current URL-based citation is acceptable for a dataset that is updated regularly, but pinning the 85% figure to a specific year's data would strengthen traceability.

---

### Actionability (0.95/1.00)

**Evidence:**

The v1.2.0 revision maintains full actionability coverage:

1. **Goal adjudication and signal-to-metric edge case guidance** -- Both additions directly improve practitioner decision-making at key ambiguity points in the GSM process. Goal adjudication (lines 308-309) and signal-to-metric edge cases (lines 354-355) give concrete decision rules.
2. **Measurement Plan mode (no analytics infrastructure)** -- Complete 6-row table with output type, instrumentation guidance, metric specification behavior, current-state analysis limitation, threshold setting deferral, and dashboard handling. P-022 disclosure banner format specified (line 488).
3. **Three invocation options** -- Natural language, explicit agent request, and Task tool code block all present with examples.
4. **Worked example (Checkout Flow)** -- Dimension selection table, GSM table, and Metric Specifications table all populated with realistic values including updated Baymard Institute benchmark attribution (line 619).
5. **Six common workflows** -- Quick Reference table covers: define UX metrics, measure UX health post-launch, establish baselines, create dashboard spec, quantify heuristic findings, CRISIS measurement.
6. **Do NOT Use table** -- Six rows with specific alternative routing guidance and rationale.
7. **Registration exception rationale** -- H-26(c) exception explained with wave gating and AP-02 prevention rationale.

**Gaps:**

1. **`{target}` placeholder in Output Format Template lacks `[LOW confidence]` annotation** -- Line 575: `| {name} | {dimension} | {formula} | {source} | {frequency} | {target} | {condition} | {value or TBD} |`. A practitioner copying this blank template would not see the LOW confidence reminder for threshold values until reading the Synthesis Hypothesis Validation section. This is the only actionability gap identified in iter2 and remains unresolved. It is a MINOR gap -- the Threshold Fallback Methodology section and Synthesis Hypothesis Validation section both provide this guidance -- but the blank template is the highest-use artifact for practitioners.

**Improvement Path:**

Change the `{target}` placeholder to `{target [LOW confidence -- see Threshold Fallback Methodology]}` or add a footnote to the Metric Specifications row in the blank template. Low effort, high practitioner value.

---

### Traceability (0.95/1.00)

**Evidence:**

The v1.2.0 revision closes the major traceability gaps from iter2:

1. **AGENTS.md section-name reference (line 231)** -- "registered in `AGENTS.md` under the User-Experience Skill Agents section" -- no fragile line number. Verified against AGENTS.md: `ux-heart-analyst` appears at line 309 under the "User-Experience Skill Agents" section heading.
2. **Baymard Institute URL in References (line 802)** -- `https://baymard.com/ux-benchmark` provides a traceable source.
3. **Reichheld 2003 full entry in References (line 803)** -- Author, year, title, journal, volume, issue, pages. Fully traceable.
4. **Few 2006 full entry in References (line 804)** -- Author, year, full title, publisher. Fully traceable.
5. **`heart-methodology-rules.md` marked [PLANNED: Wave 2 Phase 2] in both References (line 785) and Degraded Mode (line 471)** -- Consistent annotation at both points of reference.
6. **Handoff schema planned note in Cross-Framework Integration (line 625)** -- `docs/schemas/handoff-v2.schema.json -- planned; not yet committed to repository; schema specified in .context/rules/agent-development-standards.md [Handoff Protocol]`.
7. **Requirements traceability table intact** -- PLAN.md, EPIC-003, and ORCHESTRATION.yaml all listed with paths.
8. **Version header (line 38) and footer (lines 808-816)** -- Complete revision history including all 7 fixes in the HTML comment, creation date, revision date, and summary.

**Gaps:**

1. **ux-routing-rules.md handoff contract fields not independently verified** -- The upstream handoff contracts (lines 632-636) cite specific field names from `skills/user-experience/rules/ux-routing-rules.md` [Handoff Data Contracts]. This file is not included in the cross-reference set for this scoring pass. This is a scoring environment limitation, not a document defect -- the citations are present and properly formatted.

**Improvement Path:**

No action required for this iteration. The ux-routing-rules.md handoff fields should be added to the cross-reference verification set in future scoring passes.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Actionability | 0.95 | 0.97 | Add `[LOW confidence -- see Threshold Fallback Methodology]` annotation to `{target}` placeholder in blank Output Format Template Metric Specifications table (line 575). Low effort; high practitioner value at the point of use. |
| 2 | Completeness | 0.96 | 0.98 | Add wave availability note to When to Use Activation Path table: "Available after Wave 2 entry criteria are met (see `skills/user-experience/SKILL.md` [Wave Architecture])." |
| 3 | Evidence Quality | 0.93 | 0.96 | When a specific Baymard Institute study becomes citable (e.g., specific cart abandonment report with year and finding), replace the dataset URL citation with the study citation to pin the 85% figure to a specific data point. |
| 4 | Internal Consistency | 0.95 | 0.97 | When Wave 2 MCP coordination is complete, add `mcp__context7__resolve-library-id` and `mcp__context7__query-docs` to `allowed-tools`. The current "planned" disclosure is adequate for PASS but leaves a forward-looking inconsistency. |
| 5 | Methodological Rigor | 0.96 | 0.98 | Add a brief visualization type decision table to Phase 5 (e.g., counter for current-state, time series for trends, funnel for multi-step flows). SOFT-tier enhancement; not required. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score -- specific line numbers and file cross-references cited for all 7 fixes and all scoring rationale
- [x] Uncertain scores resolved downward -- Evidence Quality at 0.93 (not 0.95) because the Baymard citation is a dataset reference without a pinned specific study; Actionability at 0.95 (not 0.97) because the blank template `{target}` placeholder still lacks the LOW confidence annotation; Internal Consistency at 0.95 (not 0.97) because Context7 MCP tools are absent from `allowed-tools` while described as planned
- [x] Calibration anchors applied -- 0.95 represents "genuinely excellent" per the calibration guidance; 0.96 is awarded only where specific verifiable evidence supports it (both Completeness and Methodological Rigor have concrete checklist evidence for the claimed improvements)
- [x] No dimension scored above 0.96 -- Completeness and Methodological Rigor at 0.96 are justified by: multiple verifiable closed gaps (tools duplication eliminated, 3 methodology additions verified at specific lines); Evidence Quality held at 0.93 despite three citation resolutions because the Baymard dataset reference remains less specific than a named study
- [x] Score trajectory plausibility check -- +0.023 from 0.928 to 0.951 across 7 targeted fixes is consistent; each fix addresses a documented gap; the composite lands just above threshold as expected from targeted precision improvements to a near-threshold document
- [x] First-draft calibration not applicable (iteration 3)

---

## Session Context (Handoff Schema)

```yaml
verdict: PASS
composite_score: 0.951
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.93
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Add [LOW confidence] annotation to {target} placeholder in blank Output Format Template."
  - "Add wave availability note to When to Use Activation Path table."
  - "When specific Baymard Institute study becomes citable, replace dataset URL citation."
  - "Add Context7 MCP tools to allowed-tools when Wave 2 MCP coordination is complete."
  - "Add visualization type decision table to Phase 5 (SOFT-tier enhancement)."
```

---

*Quality Score Report*
*Deliverable: `skills/ux-heart-metrics/SKILL.md`*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Iteration: 3 (prior: 0.928 iter2, 0.887 iter1)*
*Created: 2026-03-04*
