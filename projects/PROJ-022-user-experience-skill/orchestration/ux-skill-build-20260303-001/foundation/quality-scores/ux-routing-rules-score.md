# Quality Score Report: UX Routing Rules

## L0 Executive Summary

**Score:** 0.89/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.84)
**One-line assessment:** Strong structural completeness and actionability fall below the C4 threshold of 0.95 due to missing source citations on keyword selection, handoff key-field provenance, and a redundant ordering-rules section that dilutes authority clarity.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/ux-routing-rules.md`
- **Deliverable Type:** Design (routing rule file for ux-orchestrator agent)
- **Criticality Level:** C4 (rules file — auto-C3 per AE-002; scored at C4 per request)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Threshold:** >= 0.95 (C4 quality level requested)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.89 |
| **Threshold** | 0.95 (C4 per request) |
| **Standard Threshold** | 0.92 (H-13, C2+) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 7 sections present; minor handoff pair gap (no Heuristic Eval->HEART Metrics contract row) |
| Internal Consistency | 0.20 | 0.90 | 0.180 | No contradictions; CRISIS sequence matches SKILL.md; ordering rules duplicated across two sections |
| Methodological Rigor | 0.20 | 0.91 | 0.182 | Deterministic triage logic with explicit criteria throughout; minor citation gap in fallback escalation |
| Evidence Quality | 0.15 | 0.84 | 0.126 | Strong HTML comment citations; CRISIS keyword list and handoff key-field names lack source attribution |
| Actionability | 0.15 | 0.91 | 0.1365 | Copy-pasteable bypass prompt, numbered protocols, concrete file-existence checks; minor indirection in handoff validation step 2 |
| Traceability | 0.10 | 0.87 | 0.087 | Section-level tracing to SKILL.md is complete; handoff key-field column lacks provenance for specific field names |
| **TOTAL** | **1.00** | | **0.89** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**
All 7 navigation table sections are present and fully populated:
- Lifecycle Stage Router: 4-step triage fully specified (ONBOARD, CAPACITY CHECK, MCP CHECK, STAGE TRIAGE) with Stage Routing Table covering all 10 sub-skills plus CRISIS.
- Common Intent Resolution: 7 user-expression patterns mapped to routes.
- Multi-Sub-Skill Routing: ordering rules, 6-step execution protocol, 3 common combination examples, 3 constraints.
- CRISIS Routing: entry criteria with 4 keywords, 3-step execution sequence, rationale for evaluate-diagnose-measure ordering, CRISIS-specific synthesis additions.
- Wave-Aware Routing: 6-row state detection table, routing behavior for unavailable sub-skills, wave state caching rules.
- Bypass Routing: copy-pasteable prompt template, documentation table, 3 constraints with cumulative ceiling.
- Cross-Sub-Skill Handoff: 6-row data contracts table, 3-step validation protocol, confidence propagation rule.

**Gaps:**
1. The "Comprehensive UX audit" common intent pattern maps to Heuristic Eval + HEART Metrics, but the Handoff Data Contracts table contains no row for `ux-heuristic-eval` -> `ux-heart-metrics`. The multi-sub-skill execution protocol (Step 4) references passing handoff data "per Cross-Sub-Skill Handoff" for this exact combination — the contract is missing for the most prominently advertised multi-sub-skill use case.
2. The SKILL.md Cross-Sub-Skill Handoff Data section lists 6 handoff pairs; the routing rules file lists the same 6. However, SKILL.md's "Sprint to Iterate to Measure" canonical sequence implies JTBD job statements flow ultimately into Lean UX (via Design Sprint), but there is no JTBD -> Lean UX handoff contract (only JTBD -> Design Sprint and Design Sprint -> Lean UX). This is a minor gap but leaves an implicit assumption unspecified.

**Improvement Path:**
Add a `/ux-heuristic-eval` -> `/ux-heart-metrics` handoff row to the Handoff Data Contracts table specifying key fields (e.g., "severity-rated finding IDs, affected metrics candidates, baseline measurement gaps"). This is the most prominent multi-sub-skill combination in the document and the only one missing a contract.

---

### Internal Consistency (0.90/1.00)

**Evidence:**
- CRISIS sequence (Heuristic Eval -> Behavior Design -> HEART) is identical in Stage Routing Table row, CRISIS Routing section header, and CRISIS Execution Sequence table. Matches SKILL.md exactly.
- CAPACITY CHECK note on Wave 1 vs. Free cost tier correctly disambiguates the two dimensions: "the Wave 1 recommendation is based on team capacity constraints, not cost" — this prevents a contradiction with mcp-coordination.md's cost tier table (which shows JTBD as Free, yet JTBD is Wave 1).
- Multi-sub-skill maximum-2 constraint cites RT-M-007 and is consistent with agent-routing-standards.md specification.
- Bypass cumulative ceiling (max 2 concurrent) matches SKILL.md Wave Architecture section verbatim.
- Wave signoff file progression (KICKOFF -> WAVE-1 -> WAVE-2 -> WAVE-3 -> WAVE-4 -> WAVE-5) is internally consistent and matches SKILL.md Wave Definitions table ordering.
- Confidence propagation rule (MEDIUM as MEDIUM, LOW as LOW, HIGH may downgrade) is consistent with SKILL.md Synthesis Hypothesis Validation section.

**Gaps:**
The Ambiguity Resolution Protocol subsection (within "Lifecycle Stage Router") and the Multi-Sub-Skill Routing section both specify the same content-before-quality / work-before-presentation ordering rules. The two sections are not contradictory, but the duplication creates an authority ambiguity: if a future editor updates one and not the other, the file becomes inconsistent. The Ambiguity Resolution Protocol section is scoped to STAGE TRIAGE ambiguity while Multi-Sub-Skill Routing governs execution ordering — the distinction is meaningful, but the identical language obscures it.

**Improvement Path:**
In the Ambiguity Resolution Protocol subsection, replace the ordering-rule bullets with a forward reference: "The orchestrator applies the ordering protocol from [Multi-Sub-Skill Routing](#multi-sub-skill-routing) to resolve ambiguous STAGE TRIAGE matches." This eliminates duplication and makes Multi-Sub-Skill Routing the single authoritative source for ordering rules.

---

### Methodological Rigor (0.91/1.00)

**Evidence:**
- Every section opens with an HTML comment citing its source in SKILL.md by exact section name: `<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — 4-step sequential triage. -->`. This is applied to Lifecycle Stage Router, Common Intent Resolution, Multi-Sub-Skill Routing, CRISIS Routing, Wave-Aware Routing, Bypass Routing, and Cross-Sub-Skill Handoff.
- The 4-step triage is deterministic: each step has explicit decision criteria (session flag, < 20% time threshold, lightweight resolve call, intent pattern match). No vague language in binding rules.
- CRISIS rationale section explicitly names the evaluate-diagnose-measure pattern and provides a causal chain: heuristic severity inventory -> behavioral bottleneck root cause -> quantitative baseline for tracking. The methodology order is justified, not just asserted.
- Handoff Validation uses enumerated steps with explicit criteria: artifact existence, key fields non-empty, confidence propagation rule. The protocol is procedural and verifiable.
- Ordering rules cite `agent-routing-standards.md` [Multi-Skill Combination] as their source, grounding sub-skill routing methodology in the parent framework's established standards.
- Wave bypass constraint (cumulative ceiling) cites its source specifically: "source: SKILL.md Section 'Wave Transition Quality Gates'".

**Gaps:**
The No-Match Fallback section's step 1 cites H-31 ("Ask the user... per H-31") but step 2 (escalating to display the full Stage Routing Table) does not cite why this escalation path was chosen over other options. The three-step escalation is reasonable but is not attributed to any rule or methodology source. Step 3 (gap acknowledgment per P-022) correctly cites P-022.

**Improvement Path:**
Add a parenthetical citation to step 2: "(presenting all options per H-31 structured question format — progressively broader presentation reduces cognitive load while maintaining user authority over routing)." This closes the citation gap and makes the three-step escalation fully evidenced.

---

### Evidence Quality (0.84/1.00)

**Evidence:**
- HTML comment citations on all 7 major sections point to specific SKILL.md sections by name.
- Cross-references to sibling rule files use bracket notation with section identifiers: `wave-progression.md [Wave State Tracking]`, `synthesis-validation.md [Cross-Framework Synthesis Protocol]`, `mcp-coordination.md [Cost Tiers]`.
- All 5 referenced sibling rule files exist on disk (verified: wave-progression.md, synthesis-validation.md, mcp-coordination.md, ci-checks.md, plus ux-routing-rules.md itself).
- Handoff data contracts cite the Jerry handoff schema: `docs/schemas/handoff-v2.schema.json`.
- CRISIS rationale cites Nielsen's 10 heuristics and Fogg B=MAP as methodological sources for the two diagnosis sub-skills.
- Bypass constraint ceiling cites "source: SKILL.md Section 'Wave Transition Quality Gates'" with specific ceiling number (2).

**Gaps:**
1. **CRISIS keyword list lacks selection rationale.** The 4 CRISIS entry keywords ("CRISIS", "urgent UX", "users abandoning", "critical usability issue") are listed without citation. It is unclear whether these were derived from the SKILL.md Common Intent Resolution table, from a user research study on crisis language, or from the author's judgment. Given that CRISIS mode is a high-stakes routing path (fixed 3-skill sequence, no user sub-skill selection), the keyword trigger criteria should be traceable to an explicit source.
2. **Handoff Data Contracts "Key Fields" column is unattributed.** The specific field names — "Job statement text, push/pull forces, hiring criteria" for JTBD -> Design Sprint; "Prototype description, interview findings, validated/invalidated hypotheses" for Design Sprint -> Lean UX — do not appear in SKILL.md's handoff table (which lists only the artifact name, not field names). These appear to be derived from the UX methodologies themselves (switch interview output, Day 4 protocol output) but no citation is provided connecting them to those methodologies.

**Improvement Path:**
1. Add a comment to the CRISIS Entry section: `<!-- CRISIS keywords derived from SKILL.md Common Intent Resolution table + Lifecycle-Stage Routing "CRISIS: Urgent UX problems" pattern. -->`. If additional keyword sources exist (e.g., domain research), cite them.
2. Add a footnote or inline citation to the Handoff Data Contracts table: "Key fields derived from the output specification of each sending sub-skill's methodology (see each sub-skill's agent definition `<output>` section for authoritative field lists)." This makes the provenance traceable even before sub-skill agent definitions are written.

---

### Actionability (0.91/1.00)

**Evidence:**
- Bypass prompt is a copy-pasteable template with explicit placeholder format (`/ux-{name}`, `Wave {N}`), concrete example text for each of the 3 fields, and specific example values ("No completed heuristic evaluation from Wave 1", "Backfill Wave 1 heuristic evaluation within 2 sprints"). Immediately usable.
- Bypass documentation table specifies 8 fields with explicit content descriptions including ISO 8601 date format for the bypass date field.
- Wave state detection is a concrete file-existence check — an implementer can write a deterministic function directly from the 6-row table.
- CRISIS execution sequence table has 4 columns (Step, Sub-Skill, Purpose, Handoff to Next) making each step independently verifiable.
- Multi-sub-skill execution protocol is a 6-step numbered table with explicit validation criteria at each step.
- No-Match Fallback is a 3-step escalation with specific user-facing language at each step.
- Confidence propagation rule specifies all three cases: MEDIUM -> MEDIUM, LOW -> LOW, HIGH may downgrade.

**Gaps:**
Handoff Validation step 2 states "Required handoff fields for the specific sub-skill pair are non-empty" but does not specify which fields are required for each pair. An implementer must cross-reference step 2 against the Key Fields column in the Handoff Data Contracts table above — this is a two-hop reference within the same document, which is acceptable but adds friction. A forward reference ("see Key Fields column in the Handoff Data Contracts table above") would close this gap.

**Improvement Path:**
In Handoff Validation step 2, add: "(Required fields per pair: see 'Key Fields' column in the [Handoff Data Contracts](#handoff-data-contracts) table above.)" This makes the validation step self-contained without duplicating the contract table.

---

### Traceability (0.87/1.00)

**Evidence:**
- Every section has an HTML comment citing source document and section name. For Wave State Detection: `<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Wave Architecture" — signoff file gating. See also: skills/user-experience/rules/wave-progression.md [Wave State Tracking] ... -->`. This dual-citation pattern (SKILL.md + sibling rule file) is applied to Wave State Detection and Wave State Caching.
- Ordering protocol cited in two places: Ambiguity Resolution Protocol section and Multi-Sub-Skill Routing section, both citing `agent-routing-standards.md` [Multi-Skill Combination].
- Handoff protocol cites `docs/schemas/handoff-v2.schema.json` at the top of the Cross-Sub-Skill Handoff section.
- Bypass constraint ceiling cites "source: SKILL.md Section 'Wave Transition Quality Gates'" with specific page-level attribution.
- All sibling rule files referenced by name exist on disk.
- Footer metadata includes parent SKILL.md path, sibling rule file names, creation date, and status.

**Gaps:**
The "Key Fields" column in the Handoff Data Contracts table — e.g., "Job statement text, push/pull forces, hiring criteria" — has no traceable source. The SKILL.md handoff table lists artifact names only. These field names are consistent with switch interview outputs from JTBD methodology and AJ&Smart Design Sprint Day 4 protocols, but the routing rules file does not cite either of those methodology sources for the field specifications. A reader auditing the routing rules file cannot verify these field names without knowledge of the underlying UX frameworks.

**Improvement Path:**
Add a footer note to the Handoff Data Contracts table: "Key field names are derived from each sending sub-skill's output specification. Authoritative field lists will be specified in each sub-skill agent's `<output>` section when deployed. Until then, these fields represent the minimum required output from each methodology (JTBD: switch interview protocol; Design Sprint: Day 4 interview synthesis; Heuristic Eval: Nielsen severity classification; Atomic Design: Storybook story schema; Lean UX: hypothesis backlog template)."

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.84 | 0.92+ | Add source citation for CRISIS keyword list (HTML comment referencing SKILL.md section). Add methodology citations for handoff Key Fields column. Both are single-line additions. |
| 2 | Completeness | 0.90 | 0.95+ | Add missing `/ux-heuristic-eval` -> `/ux-heart-metrics` handoff contract row to Handoff Data Contracts table (the "Comprehensive UX audit" path is the most prominent multi-sub-skill use case and must have a complete contract). |
| 3 | Traceability | 0.87 | 0.93+ | Add a table footer note to Handoff Data Contracts attributing Key Fields to each sub-skill's methodology source. Link sub-skill field origins to deployed agent definitions (or note as "pending agent definition"). |
| 4 | Internal Consistency | 0.90 | 0.95+ | Collapse the duplicate ordering-rules content in Ambiguity Resolution Protocol into a forward reference to Multi-Sub-Skill Routing, making the latter the single authoritative source. |
| 5 | Actionability | 0.91 | 0.95+ | Add a forward reference in Handoff Validation step 2 pointing to the Key Fields column in the Handoff Data Contracts table to eliminate the two-hop cross-reference. |
| 6 | Methodological Rigor | 0.91 | 0.95+ | Add a citation comment to No-Match Fallback step 2 explaining why the progressive-broadening escalation path was chosen. |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score with specific line-level references
- [x] Uncertain scores resolved downward (Evidence Quality at 0.84 vs. initial impression of 0.87; Traceability at 0.87 vs. 0.90)
- [x] First-draft / first-version calibration considered — this is v1.0.0 of a new skill component; scores adjusted accordingly
- [x] No dimension scored above 0.95 without exceptional evidence — highest score is 0.91 for Methodological Rigor and Actionability
- [x] C4 threshold of 0.95 actively enforced — gaps that would be acceptable at C2/C3 are flagged here

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.89
threshold: 0.95
weakest_dimension: evidence_quality
weakest_score: 0.84
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add source citation for CRISIS keyword list and handoff Key Fields column (Evidence Quality)"
  - "Add /ux-heuristic-eval -> /ux-heart-metrics handoff contract row (Completeness)"
  - "Add table footer attributing Key Fields to methodology sources (Traceability)"
  - "Collapse duplicate ordering-rules in Ambiguity Resolution Protocol to forward reference (Internal Consistency)"
  - "Add forward reference in Handoff Validation step 2 to Key Fields column (Actionability)"
  - "Add citation to No-Match Fallback step 2 escalation path (Methodological Rigor)"
```

---

*Rule file: ux-routing-rules-score.md*
*Scores deliverable: `skills/user-experience/rules/ux-routing-rules.md`*
*Scoring agent: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*Scored: 2026-03-04*
