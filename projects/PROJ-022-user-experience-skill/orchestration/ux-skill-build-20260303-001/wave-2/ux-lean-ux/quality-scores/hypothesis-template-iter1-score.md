# Quality Score Report: Hypothesis Backlog Template

## L0 Executive Summary
**Score:** 0.865/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.82)
**One-line assessment:** Template is methodologically rigorous and highly actionable but contains a notable placeholder syntax inconsistency with the Wave 1 sibling template, a Synthesis Judgments level mismatch (L2 in nav vs L1 in SKILL.md), and a missing PIVOT-hypothesis checklist item from the rules file -- three targeted fixes needed before this reaches the 0.95 C4 threshold.

## Scoring Context
- **Deliverable:** `skills/ux-lean-ux/templates/hypothesis-backlog-template.md`
- **Deliverable Type:** Design (output template for a UX sub-skill agent)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.865 |
| **Threshold** | 0.95 (C4 custom, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.87 | 0.174 | 11 of 12 required sections present; PIVOT hypothesis checklist item missing; Synthesis Judgments level mismatch |
| Internal Consistency | 0.20 | 0.82 | 0.164 | Single-brace `{PLACEHOLDER}` vs double-brace `{{PLACEHOLDER}}` in sibling Wave 1 template; Synthesis Judgments labeled L2 in nav table, L1 in SKILL.md output spec |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | All 5 methodology steps, correct hypothesis format, ICE scale, assumption quadrant framework, experiment types, decision framework all accurately rendered |
| Evidence Quality | 0.15 | 0.88 | 0.132 | All 4 methodology citations present in footer; synthesis-validation.md cross-reference correct; lean-ux-methodology-rules.md not cited within template |
| Actionability | 0.15 | 0.85 | 0.1275 | Clear REPEATABLE BLOCK markers; decision reference tables; `{DEGRADED_MODE_DISCLOSURE}` is an unfilled sub-placeholder rather than copy-pasteable text |
| Traceability | 0.10 | 0.83 | 0.083 | Header block and footer provide good traceability; lean-ux-methodology-rules.md not referenced in template; checklist rule IDs (HYP-xxx, ICE-xxx, ASM-xxx) absent |
| **TOTAL** | **1.00** | | **0.865** | |

## Detailed Dimension Analysis

### Completeness (0.87/1.00)

**Evidence:**

All 11 required output sections from SKILL.md [Output Specification] are present:
- Executive Summary (L0) -- lines 35-69 with hypothesis status table, top-N hypotheses, Q1 assumptions, experiment recommendations
- Engagement Context (L1) -- lines 73-96 with product, domain, users, prior research inputs table, MCP status, cycle scope
- Hypothesis Backlog (L1) -- lines 98-117 with full ICE table, Lean UX format, all lifecycle status values
- Assumption Map (L1) -- lines 119-162 with ASCII quadrant visualization, inventory table, quadrant summary
- Experiment Designs (L1) -- lines 165-193 with repeatable block, type selection reference
- Validated Learning Log (L1) -- lines 196-222 with repeatable block, decision framework reference
- Synthesis Judgments Summary -- lines 225-244 with 5 pre-populated row templates and confidence classification legend
- Strategic Implications (L2) -- lines 247-266 with 4 subsections (organizational patterns, maturity, velocity, product strategy)
- Limitations and Reliability (L2) -- lines 269-301 with single-facilitator disclosure, input mode, high-stakes recommendations
- Self-Review Checklist -- lines 304-320 with 12 items
- Handoff Data -- lines 322-377 with structured table and YAML block

**Gaps:**

1. **PIVOT hypothesis checklist item missing.** `lean-ux-methodology-rules.md` Self-Review Checklist contains 15 items; the template checklist has 12. The missing item is rules file item 15: "PIVOT hypotheses from Step 4 are added to the backlog with ICE scores before the next cycle begins" (BML-005, ICE-007). This is a HARD rule in the rules file (`BML-005: NEVER proceed with unscored pivot hypotheses`).

2. **Synthesis Judgments level mismatch.** The navigation table (line 27) labels Synthesis Judgments Summary as "L2: AI judgment calls with confidence classification" but `skills/ux-lean-ux/SKILL.md` [Output Specification] table (line 452) labels it "Synthesis Judgments Summary | L1." The agent output section (lines 389-394) also labels it as "Synthesis Judgments Summary (L1)." The template uses L2.

3. **`{DEGRADED_MODE_DISCLOSURE}` placeholder unfilled (line 288).** The Input Mode Limitations section contains the literal placeholder `{DEGRADED_MODE_DISCLOSURE}` rather than copy-pasteable mode-conditional text. The Engagement Context section (lines 89-94) has the conditional block as an HTML comment, but the Limitations section does not provide equivalent ready-to-use text -- requiring the user to understand they must replicate the earlier comment block.

**Improvement Path:**
- Add checklist item 13: "[ ] 13. PIVOT hypotheses generated from Step 4 are added to the backlog with ICE scores before the next cycle (BML-005, ICE-007)" to bring the checklist to 13 items matching all critical HARD rule verifications.
- Change Synthesis Judgments navigation table label from "L2" to "L1" (line 27).
- Replace `{DEGRADED_MODE_DISCLOSURE}` with the actual degraded mode text block (currently in comment form in lines 89-94), formatted as a conditional instruction with the copy-paste block.

---

### Internal Consistency (0.82/1.00)

**Evidence:**

Internally, the template is self-consistent:
- Hypothesis format `We believe {outcome} for {users} if {change} because {evidence}` matches exactly: agent methodology (line 134-148 of agent file), SKILL.md methodology (lines 244-258), and rules file HYP format spec.
- ICE scale reference table (lines 111-115) matches the agent methodology ICE scale table verbatim for the 1/5/10 anchors on all three dimensions.
- Assumption quadrant visualization (lines 125-145) matches SKILL.md, agent definition, and rules file visualizations identically.
- Lifecycle status values (DRAFT/ACTIVE/VALIDATED/INVALIDATED/DEFERRED) are consistent throughout the template and match the rules file lifecycle state transition table.
- Decision framework reference (lines 216-221) PERSEVERE/PIVOT/KILL definitions match agent methodology Step 4 decision framework.
- ICE formula `{(I+C+E)/3}` in the backlog table header (line 106) is consistent with the ICE Scoring Scale Reference (lines 109-115).
- YAML handoff block correctly labels fields as `[handoff-v2]` vs `[ux-ext]` -- consistent with sibling heuristic-report-template.md pattern.

**Gaps:**

1. **Placeholder syntax inconsistency with sibling Wave 1 template.** The heuristic-report-template.md (Wave 1 reference template) uses `{{DOUBLE_BRACE}}` syntax throughout for all fill-in fields. The hypothesis-backlog-template.md uses `{SINGLE_BRACE}` syntax. This inconsistency creates a divergent user experience across templates in the same skill ecosystem. A user filling in multiple templates would encounter two different placeholder conventions. Both templates claim `<!-- USAGE: Fill {PLACEHOLDER} fields -->` vs `<!-- USAGE: Fill {{PLACEHOLDER}} fields -->`, cementing the divergence at the template header level.

2. **Synthesis Judgments level contradiction.** The navigation table assigns this section "L2" (line 27) while the SKILL.md output specification table assigns it "L1" and the agent output section assigns it "L1." Within the template itself, no L-level label appears on the section heading, so the contradiction lives only between the nav table and the authoritative specification -- but the nav table is what a reader sees first and uses for context loading decisions.

3. **Self-Review Checklist items misaligned with rules file.** The template has 12 checklist items; the rules file has 15. While the 12 template items are internally consistent and accurate, the discrepancy with the authoritative rules file creates a risk of incomplete verification.

**Improvement Path:**
- Standardize placeholder syntax to `{{DOUBLE_BRACE}}` format throughout, matching the established pattern in heuristic-report-template.md. This is a bulk replacement across all `{SINGLE_BRACE}` occurrences in the template.
- Change nav table Synthesis Judgments entry from "L2" to "L1."
- Add the missing checklist item for PIVOT hypotheses (see Completeness gap 1).

---

### Methodological Rigor (0.92/1.00)

**Evidence:**

The template implements all required methodology elements with high fidelity:

- **Build-Measure-Learn cycle coverage:** All 5 methodology steps are represented as distinct sections: Hypothesis Backlog (Step 1), Assumption Map (Step 2), Experiment Designs (Step 3), Validated Learning Log (Step 4), and the overall template structure enables Step 5 synthesis.
- **Canonical hypothesis format:** Line 106 correctly implements the 4-component format with all required fields in the backlog table: `We believe {outcome} for {users} if {change} because {evidence}`. HTML comment on line 100 mandates "all 4 components: outcome, users, change, evidence."
- **ICE scoring rigor:** Formula `{(I+C+E)/3}` explicitly in table header; lower-scoring discipline referenced via P-022 citation in lines 101 and 121. Scale reference table provides 3 concrete anchors per dimension.
- **Assumption quadrant methodology:** ASCII visualization (lines 125-145) accurately represents the 4-quadrant Known/Unknown x High Risk/Low Risk framework. Ordering of inventory table (Q1 first comment on line 152) matches methodology priority. Quadrant summary table (lines 156-161) correctly specifies actions per quadrant.
- **Experiment type selection:** Type reference table (lines 184-192) matches SKILL.md and agent definition exactly with correct Time/Confidence/Min. User Base columns. Comment (line 168) provides type selection guidance for Q1 assumptions.
- **Decision framework:** PERSEVERE/PIVOT/KILL reference table (lines 216-221) with "When" and "Action" columns correctly implements the rules file decision criteria.
- **Lifecycle management:** Status enumeration in backlog table header is complete and ordered (DRAFT/ACTIVE/VALIDATED/INVALIDATED/DEFERRED).
- **ICE Re-Score Impact field:** The Learning entry block includes `- **ICE Re-Score Impact:** {describe any ICE score changes...}` (line 212) which extends the rules file Learning Entry Format with a methodologically sound addition. ICE-003 in the rules file mandates re-scoring after cycles; this field makes that requirement explicit in the template.
- **Handoff threshold:** Lines 325-326 correctly state the VALIDATED/INVALIDATED-only handoff threshold, matching SKILL.md and rules file.

**Gaps:**

- The `Cycle scope values` comment (lines 14-15) lists the valid scope values correctly but does not explicitly flag that `learning-documentation` scope requires prior experiment results (as the rules file BML-002 and the agent input section specify). A usage note would improve template robustness.
- The experiment descriptions in the type reference table (lines 184-192) use "N/A" for Sample Size for qualitative experiments -- this is correct but the template's experiment block (line 177) documents `{number of participants or traffic requirement, if quantitative; "N/A" for qualitative-only experiments}` which is appropriately nuanced.

**Improvement Path:**
- Add a usage note to the Cycle Scope comment: "IMPORTANT: When cycle_scope is learning-documentation, prior experiment results MUST be provided via input. Without them, Steps 4-5 cannot produce learning entries without fabricating data (VLD-007, BML-002)."

---

### Evidence Quality (0.88/1.00)

**Evidence:**

All methodology citations in the template footer are accurate and appropriately attributed:
- Line 383: Gothelf & Seiden (2021) "Lean UX: Applying Lean Principles to Improve User Experience." 3rd ed. O'Reilly. -- matches agent definition and rules file citations.
- Line 384: Sean Ellis, GrowthHackers (circa 2015) for ICE scoring -- matches attribution in agent definition line 39 and rules file ICE section.
- Line 385: Ries (2011) and Croll & Yoskovitz (2013) for experiment taxonomy -- matches agent methodology and rules file experiment section citations.
- Line 386: Handoff schema `docs/schemas/handoff-v2.schema.json` -- matches sibling heuristic-report-template.md citation.
- Line 229: `skills/user-experience/rules/synthesis-validation.md` cross-reference in Synthesis Judgments section -- correct citation for synthesis gate compliance.

The confidence classification legend (lines 240-243) accurately describes HIGH/MEDIUM/LOW criteria matching the agent methodology table and the rules file CLS classification criteria. The LOW classification is correctly included (the heuristic-report-template.md revision note on line 1 shows LOW was added to bring it to version 1.9.0 -- this template correctly includes LOW from the start).

**Gaps:**

1. **No citation of `lean-ux-methodology-rules.md` within the template.** The template's self-review checklist (lines 308-319) references H-23 and S-010 but does not cross-reference the rules file that defines BML-001 through QG-004. Since the rules file is the operative constraint source for this template, a header-level citation would improve evidence traceability. Compare: the heuristic-report-template.md explicitly cites `heuristic-evaluation-rules.md` in its checklist (line 402).

2. **ICE Re-Score Impact field has no source citation.** Lines 212 adds this field to the learning entry without a citation for why it was added. It is a sound extension of ICE-003 (mandatory re-scoring rule), but the template does not make this traceability explicit.

**Improvement Path:**
- Add `<!-- USAGE: See lean-ux-methodology-rules.md for rule IDs governing each section -->` to the template header (after line 4).
- Add a comment linking ICE Re-Score Impact to ICE-003: `<!-- ICE Re-Score Impact documents compliance with ICE-003 (lean-ux-methodology-rules.md): scores MUST be re-scored after each cycle -->`.

---

### Actionability (0.85/1.00)

**Evidence:**

The template is highly actionable for its intended use case:
- REPEATABLE BLOCK markers are clearly labeled as `<!-- REPEATABLE BLOCK: EXPERIMENT START/END -->` and `<!-- REPEATABLE BLOCK: LEARNING START/END -->` with explicit copy instructions in comments.
- REPEATABLE ROW markers on the backlog table (line 107) and assumption inventory table (line 151) tell the user exactly what to copy.
- Decision reference tables (experiment type selection, learning decision framework) give the user copy-pasteable decision guidance embedded in context.
- The ICE Scoring Scale Reference (lines 109-115) with 3 concrete anchor descriptions per dimension (1/5/10) provides enough calibration for a user to score immediately.
- HTML comment guidance throughout is consistently instructional: lines 100-102 (hypothesis format requirements), 121-122 (assumption quadrant placement), 167-168 (experiment selection guidance).
- Handoff YAML is fully structured with field comments `# [handoff-v2]` and `# [ux-ext]` distinguishing schema types.
- The `<!-- Cycle scope values: ... -->` comment (line 14) provides the exact valid enum values.

**Gaps:**

1. **`{DEGRADED_MODE_DISCLOSURE}` as an unfilled sub-placeholder (line 288).** The Input Mode Limitations section contains `{DEGRADED_MODE_DISCLOSURE}` as a literal fill-in, but the actual disclosure text is only available as an HTML comment in the Engagement Context section (lines 89-94). This requires the template user to: (a) notice the placeholder, (b) locate the comment in the Engagement Context section, (c) copy and reformulate it for the Limitations section. Contrast: the Engagement Context section's degraded mode block (lines 90-94) is copy-pasteable immediately. The Limitations section should have the same copy-pasteable block with conditional instructions.

2. **ICE formula instruction vs. example.** The backlog table header (line 106) shows `{(I+C+E)/3}` as the ICE Score column value. While this is technically the formula, it looks like a fill-in instruction rather than a computed value. A note like `<!-- ICE Score = (I+C+E)/3 -- compute this value and replace with a decimal -->` would clarify intent and prevent users from literally filling in the formula string.

**Improvement Path:**
- Replace `{DEGRADED_MODE_DISCLOSURE}` at line 288 with the actual conditional disclosure structure matching the Engagement Context section pattern:
  ```
  <!-- If Miro MCP available: "Full collaborative board access available. No mode-specific limitations." -->
  <!-- If degraded mode: [DEGRADED MODE] This output was produced without Miro MCP access. (copy block from Engagement Context) -->
  ```
- Add a clarifying note to the ICE Score column: `<!-- ICE Score = (I+C+E)/3 decimal, e.g., 6.33 -->`.

---

### Traceability (0.83/1.00)

**Evidence:**

The template establishes traceability through:
- Template header comment block (lines 1-4): cites `SKILL.md [Output Specification], agent <output> section, agent <methodology> section` -- providing three explicit source references.
- Template footer (lines 381-387): cites all 4 methodology sources with full publication details, handoff schema reference, and ORCHESTRATION.yaml path.
- Synthesis Judgments section (line 229): `skills/user-experience/rules/synthesis-validation.md` cross-reference.
- Self-review checklist: H-23 and S-010 rule IDs cited on items 8 -- connecting checklist items to governance rules.
- Navigation table label "L2: Strategic Implications" and "L1: Hypothesis Backlog" correctly reflect the L-level system defined in AD-M-004.

**Gaps:**

1. **No citation of `lean-ux-methodology-rules.md`.** The rules file (`skills/ux-lean-ux/rules/lean-ux-methodology-rules.md`) is the authoritative rule source for BML, HYP, ASM, EXP, ICE, VLD, CLS, and QG rule families -- all of which govern content in this template. The template does not reference this file anywhere. Compare: heuristic-report-template.md explicitly cites `heuristic-evaluation-rules.md` three times within the template body (lines 93, 402, 403, 407, 408).

2. **Self-review checklist items lack rules file IDs.** Checklist items cite H-23 and S-010 but do not cite the BML, HYP, ASM, EXP, ICE, VLD rule IDs that each item verifies. The sibling rules file explicitly maps each checklist item to its rule reference (e.g., item 4: ASM-001, ASM-002). Including these rule IDs in the checklist would complete the traceability chain for quality auditing.

3. **ICE Re-Score Impact field lacks traceability to ICE-003.** This field was added to the Learning entry block but no comment traces it to its governing rule (ICE-003 in lean-ux-methodology-rules.md).

**Improvement Path:**
- Add `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md` citation to the template header comment block (after line 3).
- Update self-review checklist items with rule IDs matching the rules file's Self-Review Checklist:
  - Item 1: add `(HYP-001)`
  - Item 2: add `(HYP-005)`
  - Item 3: add `(ICE-001)`
  - Item 4: add `(ASM-001, ASM-002)`
  - Item 5: add `(EXP-002, EXP-006)`
  - Item 6: add `(VLD-001)`
  - Item 7: add `(CLS-001)`
- Add comment on ICE Re-Score Impact line: `<!-- ICE-003: scores MUST be re-scored after each cycle as evidence accumulates -->`.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.82 | 0.92 | Standardize placeholder syntax from `{SINGLE_BRACE}` to `{{DOUBLE_BRACE}}` throughout -- bulk replacement to match heuristic-report-template.md established pattern |
| 2 | Internal Consistency | 0.82 | 0.92 | Change nav table entry for Synthesis Judgments Summary from "L2" to "L1" to match SKILL.md output spec and agent output section |
| 3 | Completeness | 0.87 | 0.93 | Add missing PIVOT hypothesis checklist item: "[ ] 13. PIVOT hypotheses generated from Step 4 are added to the backlog with ICE scores (BML-005, ICE-007)" |
| 4 | Actionability | 0.85 | 0.92 | Replace `{DEGRADED_MODE_DISCLOSURE}` at line 288 with actionable conditional text block matching the Engagement Context section pattern |
| 5 | Traceability | 0.83 | 0.90 | Add `lean-ux-methodology-rules.md` citation to template header block and update self-review checklist items with their corresponding rule IDs |
| 6 | Evidence Quality | 0.88 | 0.93 | Add `lean-ux-methodology-rules.md` as a header-level citation; add ICE-003 comment to ICE Re-Score Impact field |
| 7 | Methodological Rigor | 0.92 | 0.95 | Add cycle scope usage note warning that `learning-documentation` scope requires prior experiment results (BML-002, VLD-007) |

---

## Leniency Bias Check
- [x] Each dimension scored independently
- [x] Evidence documented for each score
- [x] Uncertain scores resolved downward (Internal Consistency 0.82 vs possible 0.85; Traceability 0.83 vs possible 0.87)
- [x] First-draft calibration considered (this is a first-iteration template; 0.865 composite is within normal range for a strong first draft)
- [x] No dimension scored above 0.95 without exceptional evidence (Methodological Rigor at 0.92 is the highest, justified by accurate full methodology coverage)

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.865
threshold: 0.95
weakest_dimension: Internal Consistency
weakest_score: 0.82
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Standardize placeholder syntax from single-brace to double-brace throughout (matches heuristic-report-template.md)"
  - "Change Synthesis Judgments nav table label from L2 to L1"
  - "Add missing PIVOT hypothesis checklist item referencing BML-005, ICE-007"
  - "Replace {DEGRADED_MODE_DISCLOSURE} placeholder with actionable conditional text block"
  - "Add lean-ux-methodology-rules.md citation to template header and self-review checklist rule IDs"
  - "Add lean-ux-methodology-rules.md header citation and ICE-003 comment on ICE Re-Score Impact field"
  - "Add cycle scope usage note for learning-documentation scope requirement"
```

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-lean-ux/templates/hypothesis-backlog-template.md`*
*Cross-references verified: heuristic-report-template.md, SKILL.md, ux-lean-ux-facilitator.md, lean-ux-methodology-rules.md*
*Created: 2026-03-04*
