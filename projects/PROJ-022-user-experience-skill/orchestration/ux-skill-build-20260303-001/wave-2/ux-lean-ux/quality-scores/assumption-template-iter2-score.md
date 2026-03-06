# Quality Score Report: Assumption Map Template (assumption-map-template.md) — Iteration 2

## L0 Executive Summary

**Score:** 0.914/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.86)
**One-line assessment:** The primary iter1 defect (Business Viability 4th category) is fully resolved across all 4 locations; the template now scores above both calibration anchors for "good work" and is close to the 0.92 H-13 threshold, but falls short of the C4 gate (0.95) primarily due to sparse rule-ID citations in the self-review checklist and a missing companion template cross-reference.

---

## Scoring Context

- **Deliverable:** `skills/ux-lean-ux/templates/assumption-map-template.md`
- **Deliverable Version:** 1.1.0
- **Deliverable Type:** Design (Worksheet Template)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Standard Threshold (H-13):** 0.92 (C2+)
- **Applied Threshold:** 0.95 (C4, requester-specified per lean-ux-methodology-rules.md QG-001)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2 (revision after iter1 score 0.847)
- **Prior Score:** 0.847 (iter1)
- **Delta:** +0.067

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.914 |
| **Standard Threshold (H-13)** | 0.92 |
| **C4 Threshold** | 0.95 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Iter1 Primary Defect Resolved** | YES — Business Viability removed from all 4 locations |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 9 sections present; movement tracking added; 6-anchor ICE tables; health-check note added; self-review checklist has 11 items but 9 of 11 lack explicit rule ID citations |
| Internal Consistency | 0.20 | 0.93 | 0.186 | Business Viability removed from all 4 locations; category enumeration is exactly Value/Usability/Feasibility everywhere; 6-anchor ICE tables match rules file verbatim; no remaining hard contradictions |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Correct 2x2 Known/Unknown x High/Low Risk matrix; full 6-anchor ICE scales; conservative direction rules (ASM-003 pattern); Q4 escalation condition rule-grounded; condensed experiment guide is a design choice, not an error |
| Evidence Quality | 0.15 | 0.91 | 0.137 | Gothelf & Seiden (2021) cited with edition; Sean Ellis/GrowthHackers attribution present; health-check qualifier added; ICE source cited to section-anchor; Q4 escalation logic lacks specific citation beyond ASM-005 |
| Actionability | 0.15 | 0.91 | 0.137 | Distinct action/priority/column per quadrant; full ICE anchors enable calibrated scoring; Q2 monitoring trigger examples remain qualitative; no explicit note added to prefer quantitative triggers |
| Traceability | 0.10 | 0.86 | 0.086 | Version header, footer citation chain, ASM-005 in Q4 column header, ASM-004 and H-23 in checklist; 9 of 11 checklist items lack rule IDs; no companion template cross-reference within document body |
| **TOTAL** | **1.00** | | **0.914** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**
The template covers all 9 sections in its navigation table. All 4 quadrant sub-sections are present with distinct action labels, priority designations, and per-row column structures appropriate to each quadrant's action type:

- Q1 (Unknown + High Risk): Recommended Action column (line 149)
- Q2 (Known + High Risk): Monitoring Trigger column (line 168)
- Q3 (Known + Low Risk): Notes column (line 187)
- Q4 (Unknown + Low Risk): Escalation Condition (ASM-005) column (line 204)

The following iter1 gaps are now resolved:
1. Movement tracking added as an optional section (lines 227-236) with a repeatable row block and citation to ASM-005 — satisfies the MEDIUM rule without making it mandatory.
2. Distribution health check carries the heuristic qualifier note (line 225, italicized).
3. ICE reference table expanded from 3 anchors to full 6 anchors per dimension (lines 250-281) — verbatim match to rules file.
4. The self-review checklist item 2 now reads "Value, Usability, or Feasibility) per ASM-004" — correct 3-category enumeration with rule ID.

**Gaps:**
The self-review checklist (lines 329-339) has 11 items. Items 2 and 10 carry explicit rule ID citations (ASM-004 and H-23). Items 1, 3-9, 11 do not cite rule IDs. The companion hypothesis-backlog-template.md cites rule IDs on every checklist item (e.g., "HYP-001", "ASM-001, ASM-002", "ICE-001", "EXP-002, EXP-006"). This pattern discrepancy is a completeness gap: a practitioner using the assumption-map checklist cannot trace most items to their governing rule without consulting the rules file independently.

**Improvement Path:**
Add rule ID references to checklist items 1, 3-9, 11. Example: item 1 → "(ASM-001)", item 3 → "(no rule ID — operational guidance)", item 4 → "(ASM-001, ASM-002)", item 5 → "(ASM-001)", item 6 → "(ASM-006, ICE-001)", item 7 → "(ICE-006)", item 8 → "no rule ID needed", item 9 → "(CLS-001)", item 11 → "(P-022)".

---

### Internal Consistency (0.93/1.00)

**Evidence — Primary Defect Resolved:**
Business Viability is completely absent from the iter2 template. Confirmed at all 4 locations identified in iter1:

1. Assumption Categories table (lines 118-122): Three rows only — Value, Usability, Feasibility. No 4th row.
2. Assumption Inventory placeholder (line 128): `{{Value / Usability / Feasibility}}` — 3 options.
3. Self-Review Checklist item 2 (line 330): "Value, Usability, or Feasibility" — 3 options, ASM-004 cited.
4. Handoff YAML categories_represented (lines 388-391): `value: {{N}}, usability: {{N}}, feasibility: {{N}}` — 3 fields.

**Evidence — Consistency Verification:**
- ICE 6-anchor tables (lines 250-281): Compared against rules file ICE Scoring Rules § Scale Anchors. All 6 Impact anchors match verbatim. All 6 Confidence anchors match verbatim. All 6 Ease anchors match verbatim. No abbreviation or deviation.
- Quadrant definitions: Q1=Unknown+High Risk (line 85-86), Q2=Known+High Risk (line 85), Q3=Known+Low Risk (line 97), Q4=Unknown+Low Risk (line 97) — consistent with rules Quadrant Definitions table.
- Boundary judgment direction: "choose Unknown" (line 67), "choose High Risk" (line 76) — consistent with ASM-003.
- ICE formula: `(Impact + Confidence + Ease) / 3` (line 246) — consistent with rules.
- Conservative rating discipline: "choose the LOWER score" (line 283) — consistent with ICE-002.
- Placeholder syntax: All placeholders use `{{DOUBLE_BRACE}}` throughout — no single-brace inconsistencies.

**Minor remaining gap:**
The Synthesis Judgments section (lines 310-315) provides 4 sample judgment type rows (quadrant placement, category classification, ICE scoring, priority ordering). The rules file Confidence Classification Rules section enumerates 6 judgment types (assumption quadrant placement, hypothesis prioritization, experiment type recommendation, hypothesis generation, upstream data integration, pivot direction). The template's 4-row example is a subset. However, the template instructs "Repeat rows for each judgment call" — it is not exhaustive by design, and does not contradict the rules file. This is a scope choice, not a contradiction.

**Improvement Path:**
No critical changes required. Optionally, expand the sample rows in Synthesis Judgments to cover all 6 judgment types from the rules file, making the template more complete as a self-contained reference.

---

### Methodological Rigor (0.92/1.00)

**Evidence:**
The 4-quadrant framework is correctly implemented throughout:
- ASCII diagram (lines 80-108): Correct axis orientation — HIGH RISK at top, UNKNOWN at right, Q1 (Unknown+High Risk) in upper-right, Q2 (Known+High Risk) in upper-left, Q3 (Known+Low Risk) in lower-left, Q4 (Unknown+Low Risk) in lower-right. This matches the agent definition's Step 2 diagram exactly.
- Each quadrant section uses distinct action language appropriate to the quadrant priority: "Validate Immediately" (Q1), "Monitor" (Q2), "Accept" (Q3), "Defer" (Q4) — consistent with rules Quadrant Definitions table.
- Boundary judgment prompts use the "skeptical colleague" test (known axis, line 67) and "blast radius" test (risk axis, line 76) — both methodologically sound heuristics, attributed to Gothelf & Seiden (2021).
- The Q4 Escalation Condition column (line 204) is a methodologically sound enhancement: assumptions can move quadrants per ASM-005, and providing a column to pre-define escalation conditions helps practitioners anticipate scope changes. This is a genuine enhancement over the agent definition's Step 2 table, not a deviation.
- Assumption categories correctly reflect the three-tier Value/Usability/Feasibility taxonomy from Lean UX methodology (Gothelf & Seiden, 2021, Chapter 4).

**Remaining gap:**
The experiment type selection guide (lines 295-300) condenses to 5 bullet conditions. The rules file provides a 7-entry selection decision path with priority ordering (priority 1-7). The template guide maps 5 conditions to experiment types without explicit priority ordering. While adequate for a quick reference, practitioners applying the condensed guide might select a lower-priority experiment type when a higher-priority type applies. The template cross-references the rules file for ICE scoring (line 248) but does not similarly cross-reference for experiment type selection.

**Improvement Path:**
Add a cross-reference at line 300: "For the full 7-condition priority-ordered experiment type decision path, see `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md` [Experiment Type Selection Rules § Selection Decision Path]."

---

### Evidence Quality (0.91/1.00)

**Evidence:**
The template carries a well-structured citation chain:
- Header (lines 1-4): SOURCE comment identifies three referent documents: SKILL.md with section and subsection, agent methodology step number, and heuristic-report-template.md as structural pattern.
- Footer (lines 399-404): Full citations — Gothelf & Seiden (2021) with full title, edition, and publisher; Sean Ellis/GrowthHackers (circa 2015) with community attribution; handoff schema with JSON Schema draft version; ORCHESTRATION.yaml path.
- Boundary judgment prompts (lines 67, 76): Both explicitly attribute "rating discipline per Gothelf & Seiden, 2021" — epistemic honesty about the source of the directional rule.
- ICE source (line 246): "ICE scoring framework originated in the growth hacking community (Sean Ellis, GrowthHackers, circa 2015). Adapted here for assumption testing prioritization." — matches the rules file's own attribution note (rules lines 225-231) verbatim.
- ICE scale citation (line 248): Section-anchor format — `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md [ICE Scoring Rules § Scale Anchors]` — enables direct navigation.
- Distribution health check (line 225): The iter1 gap is resolved — the heuristic note now reads: "*Note: These percentages are heuristic practitioner guidance from Lean UX practice, not empirically validated thresholds. Calibrate against your product domain and prior mapping experience.*"
- Synthesis Judgments section (line 308): Cites `skills/user-experience/rules/synthesis-validation.md [Confidence Classification]` — section-anchor format, traceable.

**Remaining gap:**
The Q4 "Escalation Condition" column concept — that assumptions in Q4 should have pre-defined escalation conditions to a higher-risk quadrant — is logically grounded in ASM-005 (assumption movement tracking, MEDIUM) but the specific pre-emptive trigger framing does not appear in the rules file. The column header cites ASM-005, which is appropriate for the movement tracking aspect, but the proactive trigger framing is an author enhancement not explicitly attributed. This is a minor evidence quality gap.

**Improvement Path:**
Add a parenthetical to the Q4 column guidance: "ASM-005 governs the recording of quadrant moves once they occur; defining escalation triggers in advance is practitioner guidance based on standard risk management practice."

---

### Actionability (0.91/1.00)

**Evidence:**
Every quadrant section contains distinct, implementable guidance:
- Q1 (lines 139-154): Priority "HIGHEST", action "Design experiments to validate or invalidate these assumptions before committing engineering resources. Q1 assumptions flow directly to the Prioritized Testing Queue." Per-row Recommended Action column requires a specific experiment type per assumption.
- Q2 (lines 158-173): Priority "MEDIUM", action "Document the evidence supporting each assumption. Set review triggers" with example triggers in the placeholder text ("Re-evaluate if user segment demographics shift"). Per-row Monitoring Trigger column.
- Q3 (lines 177-192): Priority "LOW", action "Accept and move on. These assumptions do not warrant experimentation effort. Archive for reference." Per-row Notes column.
- Q4 (lines 196-211): Priority "LOWEST", action "Defer to a future Build-Measure-Learn cycle. If team capacity allows after high-priority assumptions are resolved, include these in opportunistic testing." Per-row Escalation Condition (ASM-005) column.
- Prioritized Testing Queue (lines 285-301): Full 9-column table with ICE dimensions, linked hypothesis IDs, and experiment type options. Queue coverage metric tracks handoff completeness.
- Experiment type guide (lines 295-300): 5 condition-matched choices.
- Handoff YAML (lines 356-395): Fully annotated with `[handoff-v2]` and `[ux-ext]` labels enabling agents to distinguish core schema fields from extensions.
- Self-review checklist (lines 329-339): 11 actionable pre-persistence checks.

**Remaining gap:**
The Q2 Monitoring Trigger placeholder example (line 168) provides "Re-evaluate if user segment demographics shift" and "Re-evaluate quarterly against updated analytics" — both qualitative or periodic rather than quantitative-threshold-based. The iter1 score recommended: "Add a brief note: 'Monitoring triggers SHOULD be quantitative where possible.'" This note was not added to the iter2 template. A practitioner following the template might set unmeasurable monitoring triggers, which would fail to fire reliably.

**Improvement Path:**
Add the following note to the Q2 Action paragraph (after line 163): "Monitoring triggers SHOULD be quantitative where possible (e.g., 'Re-evaluate if conversion rate drops below 15%') rather than qualitative observations that may not fire reliably."

---

### Traceability (0.86/1.00)

**Evidence:**
- Template version metadata (line 1): `<!-- TEMPLATE: assumption-map-template.md | VERSION: 1.1.0 | DATE: 2026-03-04 -->` — provides version history anchor.
- Header traceability comment (lines 1-4): SOURCE identifies SKILL.md section + subsection, agent methodology step number, structural pattern reference.
- Footer (lines 399-404): Full citation chain with version, methodology attribution, schema reference, ORCHESTRATION path.
- Q4 column header (line 204): "Escalation Condition (ASM-005)" — rule ID embedded directly in column title.
- Self-review checklist item 2 (line 330): "(Value, Usability, or Feasibility) per ASM-004" — rule ID cited.
- Self-review checklist item 10 (line 338): "(H-23)" — rule ID cited.
- ICE scale source (line 248): section-anchor format to rules file.
- Synthesis Judgments citation (line 308): section-anchor to synthesis-validation.md.
- Version 1.1.0 footer matches header VERSION comment — consistent.

**Gaps:**

1. Self-review checklist rule ID coverage is sparse. Items 1, 3, 4, 5, 6, 7, 8, 9, 11 lack rule IDs:
   - Item 1 (unique ASM IDs) → should cite ASM-001
   - Item 3 (source citation) → operational guidance, no rule ID needed
   - Item 4 (exactly one quadrant, rationale) → should cite ASM-001, ASM-002
   - Item 5 (no duplicates) → should cite ASM-001
   - Item 6 (Q1/Q2 in Testing Queue with ICE) → should cite ASM-006, ICE-001
   - Item 7 (1-10 scale) → should cite ICE-006
   - Item 8 (distribution summary counts) → operational, no rule ID needed
   - Item 9 (Synthesis Judgments coverage) → should cite CLS-001
   - Item 11 (degraded mode disclosure) → should cite P-022
   The hypothesis-backlog-template.md checklist provides rule IDs throughout. Inconsistency between sister templates reduces traceability of this document.

2. No within-document cross-reference to the companion hypothesis-backlog-template.md. The template's Handoff Data section (line 345) states: "Structured data for downstream consumption by the hypothesis backlog (Step 1), experiment design (Step 3), and ux-orchestrator coordination." The hypothesis backlog template is the primary consumer of this document's output but is not cited by file path or template name within the document body.

3. The Quadrant Boundary Definitions section comment (line 56): "Do not modify this section -- it provides the classification criteria..." has no rule ID reference. Contrast with the rules file where quadrant boundary criteria are governed by ASM-001 through ASM-003.

**Improvement Path:**
1. Add rule ID citations to checklist items 1, 4, 5, 6, 7, 9, 11 using the pattern established in hypothesis-backlog-template.md.
2. Add a cross-reference in the Handoff Data section: "See companion template: `skills/ux-lean-ux/templates/hypothesis-backlog-template.md` for the downstream consumer of this handoff."
3. Add to the Quadrant Boundary Definitions comment: "(ASM-001, ASM-002, ASM-003 govern placement requirements)"

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.86 | 0.92 | Add rule ID citations to self-review checklist items 1, 4, 5, 6, 7, 9, 11 following the hypothesis-backlog-template pattern. Add companion template cross-reference in Handoff Data section. Add rule IDs to Quadrant Boundary Definitions comment. |
| 2 | Completeness | 0.92 | 0.94 | Add rule ID references to checklist items 1, 3-9, 11 (this overlaps with Priority 1 and would improve Completeness simultaneously). |
| 3 | Actionability | 0.91 | 0.93 | Add a note to Q2 Action instructions: "Monitoring triggers SHOULD be quantitative where possible (e.g., 'Re-evaluate if conversion rate drops below 15%') rather than qualitative observations." |
| 4 | Methodological Rigor | 0.92 | 0.93 | Add cross-reference to experiment type selection guide: "For full 7-condition priority-ordered decision path, see `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md` [Experiment Type Selection Rules § Selection Decision Path]." |
| 5 | Evidence Quality | 0.91 | 0.93 | Add note to Q4 escalation condition guidance clarifying the proactive trigger framing as practitioner guidance beyond ASM-005 scope. |
| 6 | Internal Consistency | 0.93 | 0.95 | Optionally expand Synthesis Judgments sample rows from 4 to 6 to cover all judgment types enumerated in the rules file, making the template more complete as a self-contained reference. |

---

## Iteration History

| Iteration | Score | Verdict | Primary Issue | Resolution Status |
|-----------|-------|---------|---------------|------------------|
| 1 | 0.847 | REVISE | Business Viability 4th category introduced in 4 locations; contradicts 3-category rules | RESOLVED in iter2 |
| **2** | **0.914** | **REVISE** | Sparse rule-ID citations in self-review checklist; no companion template cross-reference | Pending iter3 |

**Score improvement:** +0.067 from iter1 to iter2.
**Gap to C4 threshold:** 0.95 - 0.914 = 0.036 remaining.
**Gap to standard H-13 threshold:** 0.92 - 0.914 = 0.006 remaining (very close to standard gate).

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific line numbers and content references
- [x] Uncertain scores resolved downward: Evidence Quality and Actionability uncertain between 0.91 and 0.92; chose 0.91 (lower) due to specific documented gaps; Traceability uncertain between 0.86 and 0.88; chose 0.86 (lower) given 9 of 11 checklist items lack rule IDs — a systematic pattern, not an isolated gap
- [x] Revision calibration considered: iter2 with major primary defect resolved; score of 0.914 is appropriate for a well-structured template with minor refinement gaps
- [x] No dimension scored above 0.93 without documented evidence (Internal Consistency at 0.93 justified by verbatim ICE table match and complete Business Viability removal across all 4 locations)
- [x] Calibration anchor check: 0.914 sits appropriately between 0.92 (genuinely excellent) and 0.85 (strong with minor refinements) — the template is above 0.85 quality but below 0.92 due to the traceability gaps

---

## Session Context

```yaml
verdict: REVISE
composite_score: 0.914
prior_score: 0.847
delta: +0.067
threshold: 0.92
c4_threshold: 0.95
gap_to_c4: 0.036
gap_to_standard: 0.006
weakest_dimension: traceability
weakest_score: 0.86
critical_findings_count: 0
primary_defect_iter1_resolved: true
iter1_primary_defect: "Business Viability 4th category — removed from all 4 locations"
iter2_primary_gap: "Self-review checklist rule IDs: 9 of 11 items lack rule ID citations; no companion template cross-reference"
iteration: 2
improvement_recommendations:
  - "Add rule IDs to self-review checklist items 1, 4, 5, 6, 7, 9, 11 (ASM-001, ASM-002, ASM-006, ICE-001, ICE-006, CLS-001, P-022)"
  - "Add companion template cross-reference in Handoff Data section (hypothesis-backlog-template.md)"
  - "Add rule IDs to Quadrant Boundary Definitions comment (ASM-001, ASM-002, ASM-003)"
  - "Add quantitative trigger guidance note to Q2 Action instructions"
  - "Add experiment type selection cross-reference to rules file decision path"
  - "Add note clarifying Q4 escalation condition framing vs. ASM-005 scope"
```

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Template Scored: `skills/ux-lean-ux/templates/assumption-map-template.md` v1.1.0*
*Cross-References: `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md` (v1.1.0), `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` (v1.1.0), `skills/ux-lean-ux/SKILL.md` (v1.2.0), `skills/ux-lean-ux/templates/hypothesis-backlog-template.md` (v1.1.0)*
*Prior Score Report: `skills/ux-lean-ux/output/quality-scores/assumption-template-iter1-score.md`*
*Created: 2026-03-04*
