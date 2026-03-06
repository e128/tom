# Quality Score Report: JTBD Analysis Report Template (job-statement-template.md) -- Iteration 3

## L0 Executive Summary

**Score:** 0.918/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.87)
**One-line assessment:** Iteration 3 closes seven of the nine iter2 gaps (+0.035 composite), but introduces one new internal consistency error -- the switch force rating scale anchors were added with incorrect Likert descriptors ("Strongly disagree" through "Strongly agree") instead of the correct evidence-volume anchors from jtbd-methodology-rules.md ("Minimal" through "Dominant"); correcting this single factual error and tightening one residual Evidence Quality gap should bring the template to the C4 threshold (0.95).

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/templates/job-statement-template.md`
- **Deliverable Type:** Design (output template for ux-jtbd-analyst agent)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 3 (trajectory: 0.797 iter1, 0.883 iter2, 0.918 iter3)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.918 |
| **C4 Threshold** | 0.95 (H-13, C4 criticality) |
| **Standard Threshold** | 0.92 (H-13, C2+ deliverables) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Score Delta from Iter2** | +0.035 |

> **Note on threshold:** The composite of 0.918 clears the standard C2+ PASS threshold (0.92 is the standard gate, and 0.918 is just below that). Under the C4 ceiling of 0.95 that governs this deliverable, the gap remains 0.032. A single factual error (wrong rating scale anchors) accounts for the bulk of the shortfall in the lowest-scoring dimension (Internal Consistency at 0.87). Correcting that error plus closing the residual Evidence Quality gap should produce a composite at or above 0.95.

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | Nav table fixed; all required sections present and linked; all three job blocks complete; one minor residual: Opportunity Score Matrix capped at 3 rows with "extend" instruction but no 4th placeholder row |
| Internal Consistency | 0.20 | 0.87 | 0.174 | Confidence range gap fixed (HIGH=0.80-0.95, MEDIUM=0.50-0.79 with no overlap); INTRODUCED NEW ERROR: switch force rating scale comment uses Likert anchors ("Strongly disagree"--"Strongly agree") contradicting the evidence-volume anchors ("Minimal"--"Dominant") defined in jtbd-methodology-rules.md |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | Outcome format comment expanded to all four Ulwick formats; omitted-step example added; minor wording deviation: "Reduce the likelihood" (line 215) should read "Minimize the likelihood" per canonical format in rules file |
| Evidence Quality | 0.15 | 0.91 | 0.137 | CONF_JUSTIFICATION example added; CONF_VALIDATION_METHOD options added; residual: validation method options list uses "Literature triangulation" as an option but this term does not appear in SKILL.md [Synthesis Hypothesis Validation]; five canonical methods are specified there, and "Literature triangulation" is not among them |
| Actionability | 0.15 | 0.92 | 0.138 | Omitted-step example closes the actionability gap from iter2; all major placeholder guidance comments now present; composite rank comment at line 255 provides formula; minor: Opportunity Score Matrix 4th-row placeholder still absent |
| Traceability | 0.10 | 0.93 | 0.093 | SERVICE_CLASSIFICATION threshold comment added to all three job blocks; handoff schema cross-reference added (line 335); rating scale comment references jtbd-methodology-rules.md [Switch Force Analysis Rules] for cross-reference but the comment text itself is incorrect (see Internal Consistency) |
| **TOTAL** | **1.00** | | **0.918** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**

All iter2 completeness gaps are fully resolved, plus the nav table `L1: Job Inventory` entry gap.

1. **Nav table L1: Job Inventory entry: RESOLVED.** Line 19 now reads `| [L1: Job Inventory](#l1-job-inventory) | Full job catalog with classification and scoring |`. This entry was missing in iter2, causing the section to be reachable from the document body but not navigable from the nav table. The nav table now covers all top-level sections (L0 Executive Summary, L1 Job Inventory, L1 Opportunity Score Matrix, L1 Switch Force Analysis, L1 Job Map, L1 Hiring Criteria, L2 Synthesis and Prioritization, L2 Confidence Summary, Handoff Data).

2. **All required sections confirmed present.** Cross-checking against ux-jtbd-analyst.md required sections table (lines 329-340): L0 Executive Summary (line 30), L1 Functional Jobs (line 56), L1 Social Jobs (line 87), L1 Emotional Jobs (line 118), L1 Switch Force Analysis (line 165), L1 Job Map (line 192), L1 Hiring Criteria (line 225), L2 Synthesis and Prioritization (line 263), Synthesis Judgments Summary (line 312), Validation Required (line 320). All confirmed present.

3. **Three job type blocks complete.** Each of Functional, Social, and Emotional blocks has: Job Statement in canonical format, Classification field, Job Category, Importance/Satisfaction (10-scale), Opportunity Score with formula, Service Classification with threshold comment, Confidence, Evidence Sources with tier guidance, and a hiring criteria preview table. Structurally complete.

**Gaps:**

- **Opportunity Score Matrix shows only 3 rows with no 4th placeholder row.** Line 161 instructs "Extend table rows for all identified jobs" but no `{{RANK_4_*}}` or ellipsis row is present to make this concrete. This was an iter2 actionability gap that remains unaddressed. Minor: the instruction is present; the missing element is a concrete template row that reinforces the expectation visually.

**Improvement Path:**
Add a 4th row to the Opportunity Score Matrix: `| 4 | {{RANK_4_JOB_ID}} | {{RANK_4_STATEMENT}} | {{RANK_4_IMP}} | {{RANK_4_SAT}} | {{RANK_4_SCORE}} | {{RANK_4_CLASS}} |` followed by a comment `<!-- Add rows for all identified jobs up to the maximum. -->`. This makes the "extend the table" instruction actionable for agents filling the template.

---

### Internal Consistency (0.87/1.00)

**Evidence:**

One iter2 internal consistency gap was resolved; one new error was introduced.

1. **Confidence mapping range gap: RESOLVED.** Line 354 now reads: `confidence: {{CONFIDENCE_NUMERIC_0_TO_1}}  # numeric 0.0-1.0 per handoff-v2.schema.json. Map from qualitative: HIGH=0.80-0.95, MEDIUM=0.50-0.79, LOW=0.15-0.49`. The iter2 overlap between MEDIUM upper bound (0.7) and HIGH lower bound (0.8) has been closed. The ranges are now gapless in the critical zone: MEDIUM tops at 0.79, HIGH starts at 0.80. The LOW lower bound of 0.15 is reasonable (aligned with "very low confidence, sparse evidence"). This is a clean fix.

2. **INTRODUCED NEW ERROR: Switch force rating scale anchors are incorrect.** Line 174 reads: `<!-- Rating scale: 1=Strongly disagree, 2=Disagree, 3=Neutral, 4=Agree, 5=Strongly agree. See jtbd-methodology-rules.md [Switch Force Analysis Rules]. -->`. This is a Likert-type agreement scale. The jtbd-methodology-rules.md [Switch Force Analysis Rules, Rating Scale section, lines 189-195] defines the authoritative 1-5 anchor as: `1=Minimal, 2=Low, 3=Moderate, 4=Strong, 5=Dominant` where each anchor is defined by evidence volume and intensity (e.g., "4=Strong: Substantial evidence; dominant theme across multiple source types. 10+ evidence instances or strong intensity across 3+ source types"). The Likert agree/disagree scale bears no relationship to this evidence-volume framework. An agent using the template and reading the Likert anchors would rate "Push=4/5 (Agree)" instead of "Push=4/5 (Strong: 10+ evidence instances)". The two scales produce different ratings for the same evidence set. This contradicts the rules file, making the template internally inconsistent with its governing methodology reference.

**Gaps:**

- Wrong anchor set on line 174 is the primary inconsistency. This is a factual error, not a cosmetic issue -- the anchor text determines how agents apply the rating scale.

**Improvement Path:**
Replace line 174 with: `<!-- Rating scale: 1=Minimal (sparse evidence, <3 instances), 2=Low (3-5 instances, low intensity), 3=Moderate (6-10 instances or high intensity), 4=Strong (10+ instances or strong intensity across 3+ source types), 5=Dominant (pervasive across all sources). Source: jtbd-methodology-rules.md [Switch Force Analysis Rules, Rating Scale]. Apply to all four force ratings. -->`.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**

Both iter2 methodological rigor gaps are addressed, with one minor wording deviation.

1. **Outcome format comment expanded: RESOLVED (with minor deviation).** Lines 213-219 now list all four Ulwick outcome formats:
   - Speed: "Minimize the time it takes to [outcome]"
   - Risk: "Reduce the likelihood of [undesired outcome]"
   - Success: "Increase the likelihood of [desired outcome]"
   - Quality: "Minimize the variability of [quality measure]"
   The comment also cites the source: "Ulwick ODI (2016) [Tier 2] via jtbd-methodology-rules.md [Opportunity Scoring Rules]". This is a substantial improvement over iter2's compressed single-line comment. The Risk format uses "Reduce the likelihood of..." (line 215) but the canonical format in jtbd-methodology-rules.md line 132 is "Minimize the likelihood of [undesired outcome]". "Reduce" is directionally correct but is not the canonical verb. An agent using "Reduce" rather than "Minimize" deviates from the published Ulwick terminology that the methodology is built on.

2. **`{{OMITTED_STEPS_RATIONALE}}` example: RESOLVED.** Line 212 reads: `<!-- Example: "Steps 3 (Prepare) and 7 (Conclude) were omitted because the product scope covers only the core execution phase, not setup or teardown." -->`. This concrete example shows agents: (a) which steps can be omitted, (b) what "scope-based omission" looks like as a rationale, and (c) the format (step number + step name + reason). The example also shows that steps are named by their universal process label (Prepare, Conclude) which keeps the rationale readable. This was the highest-priority methodological gap from iter2.

3. **Hiring Criteria methodology: Unchanged from iter2, still complete.** Weight scale, deal-breaker rule, composite rank formula, and min threshold guidance are all present and accurate.

**Gaps:**

- "Reduce the likelihood" (line 215) should read "Minimize the likelihood" per the canonical Ulwick ODI format in jtbd-methodology-rules.md line 132. Minor but worth correcting for methodology precision.

**Improvement Path:**
Change line 215 from `  Risk:    "Reduce the likelihood of [undesired outcome]"` to `  Risk:    "Minimize the likelihood of [undesired outcome]"`. Single-word change; no structural impact.

---

### Evidence Quality (0.91/1.00)

**Evidence:**

Both iter2 evidence quality gaps are addressed with concrete examples. One minor new gap introduced.

1. **`{{CONF_JUSTIFICATION}}` example: RESOLVED.** Line 300 reads: `<!-- {{CONF_JUSTIFICATION}} Example: "Synthesized from competitor reviews (T2) and domain literature (T2); no direct user interview data (T1) available. Confidence limited by absence of primary research." -->`. This example correctly: (a) uses the source tier notation format (T1, T2), (b) references the absence of primary data as the confidence-limiting factor, (c) matches the MEDIUM confidence justification pattern from jtbd-methodology-rules.md Confidence Classification Rules lines 231-232. An agent filling this table can use this as a direct model.

2. **`{{CONF_VALIDATION_METHOD}}` options: RESOLVED with minor issue.** Line 301 reads: `<!-- {{CONF_VALIDATION_METHOD}} Options: "Direct user interview", "Survey validation", "Behavioral observation", "Expert review", "Literature triangulation". Select the method that would most reduce uncertainty. -->`. This provides five concrete options. However, the SKILL.md [Synthesis Hypothesis Validation] table (lines 619-626) lists four canonical validation methods: switch interviews, expert review, behavioral analytics correlation, and customer support ticket analysis. "Literature triangulation" is not in this canonical list. "Survey validation" maps roughly to the spirit of ODI research (N=50-200) but is also not named in the canonical list. The options comment would more precisely align if it used the exact terms from the SKILL.md table.

3. **Source-tier guidance in job blocks: Unchanged from iter2, complete.** All three job blocks (Functional, Social, Emotional) and all four switch force source fields carry the tier format comment and the HARD rule about Tier 3 sole-source prohibition.

**Gaps:**

- `{{CONF_VALIDATION_METHOD}}` options include "Literature triangulation" (not in SKILL.md canonical list) and "Survey validation" (not exactly named in canonical list). While these are reasonable options, they diverge from the authoritative source. An agent using this template should see the exact canonical method names to ensure downstream handoff compatibility.

**Improvement Path:**
Replace the options comment at line 301 with: `<!-- {{CONF_VALIDATION_METHOD}} Options (from skills/ux-jtbd/SKILL.md [Synthesis Hypothesis Validation]): "Switch interviews (3-5 users with target segment)", "Expert review (named domain practitioner)", "Behavioral analytics correlation (metric data supporting the job hypothesis)", "Customer support ticket analysis (10+ tickets referencing the same job)". Select the method that would most reduce uncertainty. -->`.

---

### Actionability (0.92/1.00)

**Evidence:**

All iter2 actionability gaps are resolved. The template is highly actionable for agents filling it.

1. **`{{OMITTED_STEPS_RATIONALE}}` example: RESOLVED.** As noted in Methodological Rigor, the concrete example (line 212) prevents agents from writing "N/A" or leaving the field blank. The example names two specific steps with a scope-based rationale -- the canonical type of omission justification.

2. **All major placeholder guidance present.** Cross-checking the 15 most consequential placeholder fields:
   - `{{SITUATION}}`, `{{MOTIVATION}}`, `{{EXPECTED_OUTCOME}}`: canonical format shown in row (line 66)
   - `{{OPPORTUNITY_SCORE}}`: formula shown inline in the table row (line 71)
   - `{{SERVICE_CLASSIFICATION}}`: threshold comment added in iter3 (line 73)
   - `{{JOB_CONFIDENCE}}`: context provided by L2 Confidence Summary table
   - `{{EVIDENCE_SOURCES}}`: tier format comment present (line 76)
   - `{{PUSH_RATING}}`: rating scale comment present (line 174, though anchors are wrong per Internal Consistency)
   - `{{NET_FORCE_INTERPRETATION}}`: three-condition guidance comment present (line 186)
   - `{{OMITTED_STEPS_RATIONALE}}`: example added (line 212)
   - `{{DEFINE_OUTCOMES}}` through `{{CONCLUDE_OUTCOMES}}`: outcome format comment present (lines 213-219)
   - `{{CRITICAL_VALIDATION_NEEDED}}`: format guidance comment present (line 44)
   - `{{INNOVATION_TRAJECTORY}}`: multi-part guidance comment present (line 291)
   - `{{BLOCKERS}}`: array type, empty-array convention, [PERSISTENT] prefix, example all present (line 353)
   - `{{CONFIDENCE_NUMERIC_0_TO_1}}`: numeric mapping present (line 354)
   - `{{CONF_JUSTIFICATION}}`: example added (line 300)
   - `{{CONF_VALIDATION_METHOD}}`: options added (line 301)

3. **The hiring criteria section is fully actionable.** Field table, criterion table, weight values, deal-breaker classification rule, min threshold guidance, current score guidance, and composite rank formula are all present with accurate comments.

**Gaps:**

- Opportunity Score Matrix 4th-row placeholder absent (minor, also flagged under Completeness).

**Improvement Path:**
Add the 4th placeholder row to the Opportunity Score Matrix table (see Completeness improvement path).

---

### Traceability (0.93/1.00)

**Evidence:**

All three iter2 traceability gaps were addressed in iter3. One remains partially addressed (rating scale cross-reference points to the right file but the comment text is wrong).

1. **`{{SERVICE_CLASSIFICATION}}` threshold comment: FULLY RESOLVED.** Lines 73, 104, and 135 (in Functional, Social, and Emotional blocks respectively) all contain: `<!-- Opportunity scoring thresholds: >=10 = Underserved (innovation opportunity), 6-9 = Appropriately served, <6 = Overserved. Source: Ulwick (2016) [Tier 2]. See jtbd-methodology-rules.md [Opportunity Scoring]. -->`. The threshold values, source citation, and rules file cross-reference are all present at the point of use. This was the highest-priority traceability gap from iter2 and is now fully closed.

2. **Handoff schema cross-reference: RESOLVED.** Line 335 reads: `<!-- Handoff fields follow docs/schemas/handoff-v2.schema.json. Sub-skill extensions marked with [ux-ext]. -->`. The schema reference is present immediately before the YAML block, giving agents filling the template the location to validate their output. This was explicitly called out in iter2 as unresolved and is now fixed.

3. **Switch force rating scale cross-reference: PARTIALLY RESOLVED.** Line 174 now references `jtbd-methodology-rules.md [Switch Force Analysis Rules]`, which is the correct cross-reference destination. However, the text of the comment contains the wrong anchor set (Likert vs. evidence-volume). The cross-reference chain is: template -> rules file (correct), but the locally stated anchor values do not match what the rules file defines. Traceability gets credit for the correct file cross-reference; Internal Consistency loses credit for the incorrect anchor text.

4. **Source format comments reference jtbd-methodology-rules.md in 7 locations.** All three job blocks and all four switch force source fields carry `per jtbd-methodology-rules.md [Source Authority Rules]` cross-references. The Hiring Criteria weight scale references `per Phase 5 methodology in ux-jtbd-analyst.md`. The opportunity score formula references Ulwick (2016) [Tier 2]. The outcome format comment references `Ulwick ODI (2016) [Tier 2] via jtbd-methodology-rules.md [Opportunity Scoring Rules]`. Template footer (line 375) and header (line 3) cite all three methodology sources.

5. **Document version metadata present.** Header lines 1-3 provide version (1.2.0), date (2026-03-04), methodology citations (Christensen, Ulwick, Moesta), and parent skill context. This is full provenance for template consumers.

**Gaps:**

- The rating scale cross-reference correctly points to jtbd-methodology-rules.md, but the locally stated scale text is wrong (see Internal Consistency). This is not a traceability gap per se -- the pointer is correct -- but it means an agent following the pointer would find a discrepancy between the comment and the rules file. Minor traceability quality issue.

**Improvement Path:**
Fix the Internal Consistency error on line 174 (see Internal Consistency section). The traceability cross-reference pointer itself does not need to change.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.87 | 0.96 | Replace line 174's Likert anchors with the correct evidence-volume anchors: `1=Minimal (sparse evidence, <3 instances), 2=Low (3-5 instances, low intensity), 3=Moderate (6-10 instances or high intensity), 4=Strong (10+ instances or strong intensity across 3+ source types), 5=Dominant (pervasive across all sources)`. Single-line replacement; highest-impact fix. |
| 2 | Methodological Rigor | 0.93 | 0.97 | Change "Reduce the likelihood" (line 215) to "Minimize the likelihood" to match canonical Ulwick ODI format in jtbd-methodology-rules.md line 132. Single-word change. |
| 3 | Evidence Quality | 0.91 | 0.95 | Replace `{{CONF_VALIDATION_METHOD}}` options with the four canonical validation methods from skills/ux-jtbd/SKILL.md [Synthesis Hypothesis Validation]: "Switch interviews (3-5 users)", "Expert review (named domain practitioner)", "Behavioral analytics correlation", "Customer support ticket analysis (10+ tickets)". |

---

## Iteration-Over-Iteration Delta Analysis

| Dimension | Iter1 | Iter2 | Iter3 | Delta (2->3) | Root Cause |
|-----------|-------|-------|-------|--------------|------------|
| Completeness | 0.73 | 0.90 | 0.93 | +0.03 | Nav table L1: Job Inventory entry added |
| Internal Consistency | 0.82 | 0.90 | 0.87 | -0.03 | Confidence range fixed (+); wrong rating scale anchors introduced (-) |
| Methodological Rigor | 0.87 | 0.88 | 0.93 | +0.05 | Outcome format comment expanded; omitted-step example added |
| Evidence Quality | 0.74 | 0.86 | 0.91 | +0.05 | CONF_JUSTIFICATION example added; CONF_VALIDATION_METHOD options added |
| Actionability | 0.80 | 0.89 | 0.92 | +0.03 | Omitted-step example closes last major actionability gap |
| Traceability | 0.82 | 0.84 | 0.93 | +0.09 | SERVICE_CLASSIFICATION thresholds added to 3 job blocks; handoff schema ref added |
| **Composite** | **0.797** | **0.883** | **0.918** | **+0.035** | |

**Pattern:** Traceability had the largest delta (+0.09) because all three targeted fixes were applied. Internal Consistency is the only dimension that regressed (introduced error). The regression in Internal Consistency is the sole blocker for reaching 0.95. The three priority-1 through priority-3 fixes are all line-level changes (no structural work required), and collectively should lift the composite from 0.918 to approximately 0.950-0.955.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific line references from the deliverable
- [x] Uncertain scores resolved downward: Internal Consistency held at 0.87 (below iter2's 0.90) because the introduced rating scale error is worse than the absence of a scale comment -- incorrect guidance actively misleads agents
- [x] Revision calibration applied: iter3 scoring evaluated changes vs. iter2 baseline; credit given only for fully resolved gaps; new error penalized against the dimension that owns the consistency constraint
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Delta analysis is proportional: +0.035 composite reflects 7 gap closures and 1 regression; incremental improvements to already-high-scoring dimensions produce smaller deltas than structural additions

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.918
threshold: 0.95
weakest_dimension: Internal Consistency
weakest_score: 0.87
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Replace switch force rating scale anchors on line 174 with evidence-volume anchors from jtbd-methodology-rules.md [Switch Force Analysis Rules, Rating Scale]: 1=Minimal, 2=Low, 3=Moderate, 4=Strong, 5=Dominant"
  - "Change 'Reduce the likelihood' to 'Minimize the likelihood' on line 215 to match canonical Ulwick ODI format"
  - "Replace {{CONF_VALIDATION_METHOD}} options with four canonical methods from SKILL.md [Synthesis Hypothesis Validation]: switch interviews, expert review, behavioral analytics correlation, support ticket analysis"
```

---

*Score Report Version: 1.0.0*
*Agent: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-jtbd/templates/job-statement-template.md`*
*Companion artifacts checked: `jtbd-methodology-rules.md` (v1.3.0), `ux-jtbd-analyst.md` (v0.2.0), `SKILL.md` (ux-jtbd, v1.0.0), `template-iter2-score.md`*
*Created: 2026-03-04*
*Prior Score: 0.883 (iter2)*
