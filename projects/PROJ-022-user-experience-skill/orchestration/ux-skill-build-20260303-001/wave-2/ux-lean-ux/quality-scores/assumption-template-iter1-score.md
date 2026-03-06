# Quality Score Report: Assumption Map Template (assumption-map-template.md)

## L0 Executive Summary
**Score:** 0.847/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.72)
**One-line assessment:** Structurally strong and methodologically thorough template, blocked from PASS by a concrete cross-document category inconsistency (4-category taxonomy in the template vs. the 3-category taxonomy in methodology rules and agent definition) that will cause practitioner confusion and self-review check failures.

---

## Scoring Context

- **Deliverable:** `skills/ux-lean-ux/templates/assumption-map-template.md`
- **Deliverable Type:** Design (Worksheet Template)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (C4 specified by requester)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1 (first score)

**Note on threshold:** The standard H-13 threshold is >= 0.92 for C2+. The requester specified >= 0.95 for this C4 deliverable. Both thresholds are noted; this deliverable falls below both.

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.847 |
| **Standard Threshold (H-13)** | 0.92 |
| **C4 Requester Threshold** | 0.95 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 9 template sections present with full instructional scaffolding; boundary definitions, ICE table, handoff YAML, self-review checklist all complete |
| Internal Consistency | 0.20 | 0.72 | 0.144 | "Business Viability" 4th category present in template but absent from methodology rules (3-category) and agent definition Step 2 (3-category); category count in handoff YAML also propagates the discrepancy |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | Gothelf & Seiden ICE attribution corrected; 7-anchor ICE reference tables match rules file scale; boundary judgment prompts cite methodology source; Q4 escalation condition is a genuine addition not present in rules |
| Evidence Quality | 0.15 | 0.87 | 0.131 | All methodology claims cite Gothelf & Seiden (2021), Sean Ellis (circa 2015), and handoff schema; boundary judgment rationale attributes to named source; degraded mode disclosure check included in self-review |
| Actionability | 0.15 | 0.88 | 0.132 | Every quadrant section includes specific action label, priority, and per-row recommended action column; experiment type selection guide is present and maps to 7 types; distribution health check gives concrete percentage guidance |
| Traceability | 0.10 | 0.83 | 0.083 | Template header cites SKILL.md, agent methodology step, and heuristic-report-template as structural pattern; footer carries orchestration path; synthesis-validation.md cited in Synthesis Judgments section; but Q4 "Escalation Condition" column has no rule-file backing reference |
| **TOTAL** | **1.00** | | **0.847** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**
The template covers all nine sections listed in its own navigation table, and each section is structurally complete:
- Product Context: engagement header fields, design change description block, and a 5-row prior research input table (lines 8-49).
- Quadrant Boundary Definitions: full two-axis instructional section with definitions, evidence required, and boundary judgment prompts (lines 53-107).
- Assumption Inventory: category table, repeatable row block with instructional placeholders, and quantity guidance (8-15 range, lines 111-131).
- 4-Quadrant Map (Q1-Q4): all four quadrant sub-sections with distinct action/priority labels and per-row columns appropriate to each quadrant action type (lines 135-212).
- Quadrant Distribution Summary: count table plus health check guidance (lines 215-226).
- Prioritized Testing Queue: ICE reference table with 3 dimension anchor rows and a 7-type experiment selection guide (lines 229-261).
- Synthesis Judgments Summary: judgment table with 4 sample types and full confidence classification definitions (lines 264-282).
- Self-Review Checklist: 11 items covering all major completeness obligations (lines 285-300).
- Handoff Data: upstream consumption table plus a handoff YAML with both handoff-v2 and ux-lean-ux extension fields (lines 302-356).

**Gaps:**
1. The self-review checklist has 11 items (lines 289-299), but item 11 ("Degraded mode disclosure is present if operating without Miro MCP") does not map to any checklist item in the methodology rules `Self-Review Checklist` (which has 15 items). Items 6-11 of the rules checklist are absent from the template checklist: specifically, checks for sequential hypothesis IDs, ICE re-scoring after cycles, lifecycle state transitions, PIVOT hypothesis scoring, and the KILL decision rationale requirement. The template checklist is assumption-map-scoped (not full-cycle), but the methodology rules checklist at item 15 includes "PIVOT hypotheses from Step 4" which is relevant even at assumption-mapping scope since the template feeds Step 3.
2. The template does not include a section or placeholder for tracking assumption movement between quadrants (ASM-005 in rules), though this is a MEDIUM rule.

**Improvement Path:**
Add assumption movement tracking (even as a commented optional section) to satisfy ASM-005. Consider expanding the self-review checklist to cover items from the rules file that are applicable to assumption-map scope.

---

### Internal Consistency (0.72/1.00)

**Evidence of contradiction:**
This is the primary quality defect. The template introduces a **4th assumption category, "Business Viability"**, which does not exist in two authoritative cross-reference documents:

1. **`lean-ux-methodology-rules.md` Assumption Category Classification table** (lines 153-159): defines exactly 3 categories: Value, Usability, Feasibility. No Business Viability.
2. **`ux-lean-ux-facilitator.md` `<methodology>` Step 2** (lines 203-206): defines exactly 3 categories: Value assumptions, Usability assumptions, Feasibility assumptions. No Business Viability.
3. **`SKILL.md` does not introduce a 4th category** in any assumption mapping section.

The template introduces Business Viability in four locations:
- Assumption Categories table (line 122, with its own definition and upstream signal)
- Assumption Inventory repeatable row placeholder `{Value / Usability / Feasibility / Business Viability}` (line 128)
- Self-Review Checklist item 2: "Every assumption has a category classification (Value, Usability, Feasibility, or **Business Viability**)" (line 290)
- Handoff YAML extension fields: `categories_represented: value, usability, feasibility, business_viability` (lines 349-353)

This inconsistency is consequential: a practitioner using the template and following self-review item 2 will accept Business Viability assumptions as valid, but the methodology rules (ASM-004) require exactly one of the 3 defined categories. The facilitator agent (following its `<methodology>` Step 2) would reject Business Viability as a valid category classification. The self-review checklist in the template would pass an assumption the rules file's self-review would reject.

**Secondary consistency gap:**
The ICE "Confidence" dimension description in the template (line 241, "Some indirect evidence (analytics, benchmarks, related findings)") abbreviates the midpoint anchor differently from the rules file (lines 244-245: "Analytics trends, competitor benchmarks, related heuristic findings, general UX principles"). The omission of "general UX principles" at the mid-anchor is minor but reduces the 1-1 correspondence between template and authoritative source.

**Consistent elements:**
Quadrant definitions, action labels, priority ordering, boundary judgment language, ICE formula, and rating discipline language are all consistent between template, rules file, and agent definition.

**Improvement Path:**
Remove "Business Viability" from the template entirely and align with the 3-category taxonomy (Value, Usability, Feasibility) in the methodology rules. If Business Viability is intentionally being added, the methodology rules and agent definition Step 2 must be updated first, and this template updated to match as a downstream consumer.

---

### Methodological Rigor (0.88/1.00)

**Evidence:**
- The 4-quadrant framework is correctly represented with the canonical Known/Unknown x High Risk/Low Risk axes (lines 79-107). The ASCII diagram matches the agent definition's Step 2 diagram.
- The boundary judgment prompts use the correct directional discipline: "choose Unknown" when uncertain about knowledge classification (line 66); "choose High Risk" when uncertain about risk classification (line 75). Both cite Gothelf & Seiden (2021).
- The ICE reference table (lines 237-241) provides 1/5/10 anchor rows. The 1-anchor and 10-anchor match the rules file anchors; the 5-anchor ("Some indirect evidence (analytics, benchmarks, related findings)") is an abbreviated but directionally consistent approximation of the rules file's 4-5 anchor definition.
- The experiment type selection guide (lines 255-260) correctly orders the 7 experiment types by condition, consistent with the rules file selection priority order.
- Q4 adds an "Escalation Condition" column (line 204) not present in the agent definition's Step 2 quadrant table. This is an enhancement, not a contradiction, and is methodologically sound (assumptions can move quadrants per ASM-005).

**Gap:**
The ICE reference table in the template shows only 3 rows (scores 1, 5, 10) for each dimension. The methodology rules file provides 6 anchors per dimension (1, 2-3, 4-5, 6-7, 8-9, 10). The abbreviated 3-row reference is operationally usable but loses the granularity of the 2-3 / 6-7 / 8-9 ranges that practitioners need to avoid score anchoring at 1, 5, or 10. The fuller anchor table would produce more calibrated scores.

**Improvement Path:**
Expand the ICE reference table to the 6-anchor format from the rules file, or add a note directing practitioners to the rules file for the full scale.

---

### Evidence Quality (0.87/1.00)

**Evidence:**
- Template header cites three authoritative sources: SKILL.md, agent methodology step, and heuristic-report-template.md as structural pattern (lines 1-3).
- Footer cites Gothelf & Seiden (2021) with full publication details, Sean Ellis / GrowthHackers (circa 2015) with attribution, and handoff schema (lines 361-365).
- Boundary judgment prompts explicitly attribute the rating discipline to "Gothelf & Seiden, 2021" (lines 66, 75) rather than asserting it without backing.
- The ICE rating discipline note (line 243) cites P-022 compliance as the principle, providing constitutional traceability for the conservatism rule.
- Synthesis Judgments section cites synthesis-validation.md (line 268) rather than self-asserting the confidence model.
- Distribution health check percentages (line 225) are presented as guidance ("typically shows") rather than as hard claims, which is epistemically appropriate given they are heuristic benchmarks.

**Gap:**
The Q4 "Escalation Condition" column and the distribution health check percentages (30-50% Q1, etc.) have no cited source. These are methodologically sound guidance items but appear without attribution. The heuristic percentages in particular could cause practitioners to anchor too strongly if they believe them to be empirically validated.

**Improvement Path:**
Add a note such as "Heuristic guidance based on Lean UX practitioner experience; calibrate against your product domain" for the distribution health check percentages.

---

### Actionability (0.88/1.00)

**Evidence:**
- Every quadrant section includes a distinct **Action** label in bold with specific instructions:
  - Q1: "Design experiments to validate or invalidate these assumptions before committing engineering resources" (line 143)
  - Q2: "Document the evidence supporting each assumption. Set review triggers" with specific example triggers (lines 162-163)
  - Q3: "Accept and move on. These assumptions do not warrant experimentation effort. Archive for reference." (line 181)
  - Q4: "Defer to a future Build-Measure-Learn cycle. If team capacity allows after high-priority assumptions are resolved, include these in opportunistic testing." (lines 200-201)
- The Prioritized Testing Queue feeds directly into experiment design and hypothesis backlog steps (line 231).
- The experiment type selection guide (lines 255-260) provides condition-matched choices with concrete decision criteria.
- The handoff YAML provides structured fields for downstream consumption with explicit field-type annotations distinguishing handoff-v2 fields from ux-lean-ux extension fields (lines 316-356).
- The "Queue coverage" metric placeholder (line 253) quantifies completeness of the handoff.

**Gap:**
The Q2 monitoring trigger column provides examples ("Re-evaluate if user segment demographics shift") but does not give quantitative trigger criteria guidance (e.g., "choose thresholds that are measurable, not just observable"). A practitioner might set vague monitoring triggers. The heuristic report template offers more specific remediation guidance by effort band; this template could add similar specificity for monitoring trigger selection.

**Improvement Path:**
Add a brief note to the Q2 instructions: "Monitoring triggers SHOULD be quantitative where possible (e.g., 'conversion rate drops below 15%') rather than qualitative observations."

---

### Traceability (0.83/1.00)

**Evidence:**
- Template metadata comment block (lines 1-4) explicitly states source documents: SKILL.md section and subsection, agent `<methodology>` step number, and the structural pattern reference to heuristic-report-template.md.
- Footer (lines 361-365) provides full citation chain: Gothelf & Seiden (2021) with edition, Sean Ellis with origin community and date, handoff schema with JSON Schema version, and ORCHESTRATION.yaml path.
- The Synthesis Judgments section (line 268) cites synthesis-validation.md with the specific section name "[Confidence Classification]" — enabling practitioners to locate the referenced rule.
- Quadrant boundary definitions carry source attribution embedded in the boundary judgment language.

**Gap:**
1. The Q4 "Escalation Condition" column (introduced at line 204) has no rule-file backing reference. ASM-005 in the rules file covers assumption movement but does not explicitly define escalation conditions for Q4 in the format the template uses.
2. The comment on line 55 ("Do not modify this section") has no rule-file rule ID reference. Contrast this with the self-review checklist items which reference rule IDs.
3. The distribution health check percentages (line 225) have no cited source, as noted under Evidence Quality.

**Improvement Path:**
Add a comment reference to ASM-005 near the Q4 escalation condition column header. Consider adding rule ID references to the boundary definitions comment (e.g., ASM-003 for the uncertainty direction rule).

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.72 | 0.90 | Remove "Business Viability" from all 4 locations in the template (category table line 122, inventory placeholder line 128, self-review item 2 line 290, handoff YAML lines 349-353) and align with the 3-category taxonomy (Value, Usability, Feasibility) from lean-ux-methodology-rules.md and agent definition Step 2. If Business Viability is intentionally a new category, update the rules file and agent definition first. |
| 2 | Methodological Rigor | 0.88 | 0.93 | Expand the ICE reference table from 3 anchors (1/5/10) to the 6-anchor format from the rules file ICE Scoring section, or add a cross-reference directing practitioners to the full scale in lean-ux-methodology-rules.md. |
| 3 | Traceability | 0.83 | 0.90 | Add rule ID reference (ASM-005) near the Q4 Escalation Condition column. Add note to distribution health check percentages clarifying these are heuristic practitioner guidance, not empirically validated thresholds. |
| 4 | Completeness | 0.90 | 0.93 | Add an optional (commented) assumption movement tracking sub-section to satisfy ASM-005 for practitioners who iterate the map across multiple cycles. Consider adding a note to the self-review checklist directing practitioners to the full 15-item rules-file checklist for full-cycle execution. |
| 5 | Evidence Quality | 0.87 | 0.92 | Add a brief qualifier to the distribution health check percentages: "Heuristic guidance from Lean UX practice; calibrate against your product domain and prior mapping experience." |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score (specific line numbers cited)
- [x] Uncertain scores resolved downward: Internal Consistency uncertain between 0.72 and 0.75 due to one secondary ICE midpoint deviation; chose 0.72 (the lower bound) given the Business Viability inconsistency is a hard contradiction across 4 locations in a governing document
- [x] First-draft calibration considered: this is version 1.0.0 of the template; 0.847 is above typical first-draft range but justified by the evident structural investment
- [x] No dimension scored above 0.90 without exceptional documented evidence (Completeness at 0.90 is the ceiling; all other high-scoring dimensions are 0.87-0.88)

---

## Session Context

```yaml
verdict: REVISE
composite_score: 0.847
threshold: 0.92
c4_requester_threshold: 0.95
weakest_dimension: internal_consistency
weakest_score: 0.72
critical_findings_count: 0
primary_defect: "Business Viability 4th category in template contradicts 3-category taxonomy in lean-ux-methodology-rules.md and agent definition Step 2"
iteration: 1
improvement_recommendations:
  - "Remove Business Viability category from template (4 locations) or promote it to rules file first"
  - "Expand ICE reference table from 3-anchor to 6-anchor format per rules file"
  - "Add ASM-005 rule ID reference to Q4 Escalation Condition column"
  - "Add qualifier to distribution health check percentages"
  - "Add optional assumption movement tracking section (ASM-005)"
```

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Template Scored: `skills/ux-lean-ux/templates/assumption-map-template.md` v1.0.0*
*Cross-References: `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md`, `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md`, `skills/ux-heuristic-eval/templates/heuristic-report-template.md`*
*Created: 2026-03-04*
