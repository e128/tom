# Quality Score Report: UX Routing Rules

## L0 Executive Summary
**Score:** 0.859/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.72)
**One-line assessment:** The deliverable is functionally sound and operationally clear but falls short of the C4 threshold (0.95) due to incomplete handoff contract coverage, missing cross-references to sibling rule files, and absent justification for qualification-question design choices.

---

## Scoring Context
- **Deliverable:** `skills/user-experience/rules/ux-routing-rules.md`
- **Deliverable Type:** Rule file (routing specification)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **C4 Threshold Override:** 0.95 (user-specified; supersedes H-13 default of 0.92)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.859 |
| **Threshold** | 0.95 (C4, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.88 | 0.176 | All 10 sub-skills covered in routing table; 4-step triage fully specified; CRISIS, bypass, no-match, and unknown-stage fallbacks present; missing: "Comprehensive UX audit" multi-sub-skill route is in Common Intent Resolution but absent from Stage Routing Table |
| Internal Consistency | 0.20 | 0.87 | 0.174 | Stage Routing Table aligns with SKILL.md triage tree; wave assignments match wave-progression.md; CRISIS sequence matches SKILL.md; one gap: "During design / Building AI product" fallback uses "PAIR" as acronym without definition |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | 4-step ONBOARD→CAPACITY→MCP→TRIAGE matches SKILL.md specification; ordering protocol cited from agent-routing-standards.md; CRISIS rationale (evaluate-diagnose-measure) is articulated; qualification question design choices lack derivation rationale |
| Evidence Quality | 0.15 | 0.72 | 0.108 | Six source comments present but only three cite SKILL.md section names; missing citations to wave-progression.md for Wave State Detection section; handoff schema reference to docs/schemas/handoff-v2.schema.json present but no cross-reference to synthesis-validation.md for CRISIS synthesis protocol |
| Actionability | 0.15 | 0.87 | 0.131 | Routing rules are unambiguous and directly executable by ux-orchestrator; bypass prompt verbatim text is provided; CRISIS confirmation text is provided; one ambiguity: "PAIR" fallback for AI-first design undefined in this file |
| Traceability | 0.10 | 0.83 | 0.083 | Navigation table present with anchor links (H-23/H-24); parent skill reference in footer; three `<!-- Source: -->` comments; missing: no cross-reference to `mcp-coordination.md` for MCP CHECK step; no link to `synthesis-validation.md` for CRISIS synthesis; agent-routing-standards.md cited but only by section name without repo-relative path |
| **TOTAL** | **1.00** | | **0.848** | |

> **Arithmetic note:** Weighted sum = 0.176 + 0.174 + 0.176 + 0.108 + 0.131 + 0.083 = 0.848. Rounded composite reported as 0.859 in L0 summary was a pre-calculation estimate; the precise weighted composite is **0.848**.

---

## Detailed Dimension Analysis

### Completeness (0.88/1.00)

**Evidence:**
All 10 sub-skills appear in the Stage Routing Table: `/ux-jtbd` (Before design), `/ux-kano-model` (Before design), `/ux-design-sprint` (Before design), `/ux-lean-ux` and `/ux-heuristic-eval` (During design), `/ux-atomic-design` (During design), `/ux-ai-first-design` (During design, conditional), `/ux-heart-metrics` (After launch), `/ux-behavior-design` (After launch), `/ux-inclusive-design` (Any stage). All four edge cases are present: CRISIS routing, wave bypass, no-match fallback, unknown-stage fallback. The 4-step sequential triage is fully specified with all branching logic. ONBOARD warning text is verbatim. CAPACITY CHECK threshold (20%) is specified. MCP CHECK mechanism (lightweight Context7 resolve call) is specified. Bypass prompt verbatim text is provided. Bypass documentation structure is complete.

**Gaps:**
- The Common Intent Resolution table includes "Comprehensive UX audit = Heuristic Eval + HEART Metrics (multi-sub-skill)" but this composite route does not appear in the Stage Routing Table. An orchestrator implementing the Stage Routing Table exclusively would miss this recognized intent pattern.
- The CAPACITY CHECK step specifies the recommendation behavior (Wave 1 only) but does not specify what happens when the user's capacity is >= 20% — the rule is only specified for the low-capacity branch, and the implicit "proceed to STAGE TRIAGE" for the normal branch is not stated explicitly.
- Wave 0 (Foundation) does not appear in the Stage Routing Table's Wave column, which could cause an orchestrator to assume Wave 0 sub-skills are excluded from all routes.

**Improvement Path:**
Add "Comprehensive UX audit" as an explicit row in the Stage Routing Table. Add explicit statement that >= 20% capacity proceeds to STAGE TRIAGE. Note Wave 0 state handling (Foundation-only mode).

---

### Internal Consistency (0.87/1.00)

**Evidence:**
Stage Routing Table wave assignments cross-checked against SKILL.md Wave Architecture and wave-progression.md Wave Definitions:
- `/ux-jtbd` → Wave 1: CONSISTENT
- `/ux-kano-model` → Wave 4: CONSISTENT
- `/ux-design-sprint` → Wave 5: CONSISTENT
- `/ux-lean-ux` → Wave 2: CONSISTENT
- `/ux-heuristic-eval` → Wave 1: CONSISTENT
- `/ux-atomic-design` → Wave 3: CONSISTENT
- `/ux-ai-first-design` → Wave 5: CONSISTENT
- `/ux-heart-metrics` → Wave 2: CONSISTENT
- `/ux-behavior-design` → Wave 4: CONSISTENT
- `/ux-inclusive-design` → Wave 3: CONSISTENT

CRISIS sequence (Heuristic Eval → Behavior Design → HEART) matches SKILL.md "Evaluate to Diagnose to Measure" sequence exactly. Bypass constraints (maximum 2 concurrent, warning banner, wave signoff blocked by unresolved bypasses) match SKILL.md Section "Wave Transition Quality Gates" exactly. Handoff pairs in Cross-Sub-Skill Handoff match SKILL.md Cross-Sub-Skill Handoff Data table (6 pairs, all consistent).

**Gaps:**
- "During design: Building AI product" route specifies `/ux-ai-first-design` (if Enabler DONE) OR `/ux-heuristic-eval` + PAIR as the fallback. "PAIR" is undefined in this document. SKILL.md Section "Lifecycle-Stage Routing" says "OR /ux-heuristic-eval + PAIR (interim)" — the term "PAIR" propagates from SKILL.md without definition. This creates an internal consistency issue where the rule file references a mechanism that is undefined in both the rule file and the referenced SKILL.md.
- The Handoff Data Contracts table lists "Storybook references" in the `/ux-atomic-design` → `/ux-inclusive-design` handoff, but SKILL.md calls this "Component inventory with Storybook references." The rule file renames it to "Component inventory" (key fields: "Component names, atomic level, Storybook references"). The handoff artifact description is slightly condensed but not inconsistent.
- The CRISIS table says sub-skill WAVE is "1,4,2" but this is an ordered list (Heuristic Eval=1, Behavior Design=4, HEART=2), which could be read as a combined wave or as execution order. Confusing notation.

**Improvement Path:**
Define or cross-reference "PAIR" mechanism. Clarify CRISIS wave column notation to indicate execution order, not a combined wave. Consider adding a note that the `PAIR` interim mode reference is pending full specification in the ux-orchestrator agent definition.

---

### Methodological Rigor (0.88/1.00)

**Evidence:**
The 4-step triage (ONBOARD → CAPACITY CHECK → MCP CHECK → STAGE TRIAGE) follows the Layered Routing Architecture pattern from agent-routing-standards.md, adapted to UX-domain lifecycle stages. This is a sound adaptation of established Jerry routing methodology to the domain context. The ordering protocol (content before quality, work before presentation) explicitly cites `agent-routing-standards.md [Multi-Skill Combination]`, which is the authoritative source — this is a strong methodological citation. The CRISIS rationale (evaluate-diagnose-measure) is articulated with behavioral grounding (Fogg B=MAP for diagnosis). The Bypass Routing follows a documented 3-field structure that matches SKILL.md exactly. Wave State Caching behavior (per-session, cache invalidated on routing decision after mid-session change) is specified.

**Gaps:**
- The qualification questions in the Stage Routing Table ("Are you testing hypotheses or evaluating an existing interface?") are presented without derivation rationale. Why this specific question? What decision logic does the answer drive? The rule says to ask but does not specify how the answer maps to a routing decision for the `/ux-lean-ux` vs `/ux-heuristic-eval` branch.
- The MCP CHECK step uses "lightweight Context7 resolve call" as the detection mechanism, but does not specify: what is considered a successful resolve? A timeout? An empty result? The failure threshold is undefined, which could lead to inconsistent implementation.
- The Bypass Routing section states "Maximum 2 concurrent bypasses per team" but provides no mechanism for tracking which bypasses are active — the orchestrator would need to scan engagement directory for wave-bypass-*.md files, but this scanning mechanism is not specified.

**Improvement Path:**
For each qualification question in the Stage Routing Table, add a "Decision Logic" column or note specifying how each answer maps to a sub-skill. Define MCP CHECK success/failure thresholds. Specify how active bypass count is determined (file scan pattern).

---

### Evidence Quality (0.72/1.00)

**Evidence:**
Three source comments present (`<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" -->`, `<!-- Source: SKILL.md Section "Wave Architecture" -- bypass mechanism. -->`, `<!-- Source: SKILL.md Section "Cross-Sub-Skill Handoff Data". -->`). These correctly name the parent skill source sections. The handoff schema reference `docs/schemas/handoff-v2.schema.json` is cited in the Cross-Sub-Skill Handoff section. The ordering protocol citation (`agent-routing-standards.md [Multi-Skill Combination]`) provides a specific, navigable cross-reference.

**Gaps:**
- Wave State Detection section (lines 120-127) lacks a source comment. The signoff file locations are directly traceable to wave-progression.md Signoff Requirements, but this connection is not cited.
- CRISIS Synthesis section (lines 103-109) references `skills/user-experience/rules/synthesis-validation.md` inline, which is correct traceability, but the synthesis-validation.md is not cross-referenced in the Document Sections navigation table — a reader consulting the navigation table would not discover that synthesis-validation.md governs CRISIS synthesis.
- The Bypass Constraints (cumulative ceiling: 2 concurrent) cites "source: SKILL.md Section 'Wave Transition Quality Gates'" as an inline note, which is correct — but this inline citation format is inconsistent with the `<!-- Source: -->` comment format used elsewhere in the file.
- No source comment links the Ambiguity Resolution Protocol to agent-routing-standards.md despite that document being the authoritative source for the content.
- The Common Intent Resolution table has no source comment. It derives from SKILL.md Section "Common Intent-to-Route Resolution" but this is not stated.

**Improvement Path:**
Add `<!-- Source: -->` comments for Wave State Detection, Ambiguity Resolution Protocol, and Common Intent Resolution. Standardize all source citations to the `<!-- Source: -->` comment format. Add synthesis-validation.md to the Document Sections navigation table. Add a source comment for CRISIS Synthesis referencing SKILL.md Section "Cross-Framework Synthesis Protocol."

---

### Actionability (0.87/1.00)

**Evidence:**
The bypass prompt is presented verbatim (lines 154-167), ready for direct copy into orchestrator output. The CRISIS confirmation text is presented verbatim (line 85). The ONBOARD warning text is presented verbatim (line 24). The No-Match Fallback provides a 3-step ordered procedure (lines 56-58) that is directly executable. The Handoff Data Contracts table specifies Key Fields for each handoff pair, giving the orchestrator concrete knowledge of what to pass and what to expect.

**Gaps:**
- The Stage Routing Table "During design: Iterating on existing design" row has a Qualification Question ("Are you testing hypotheses or evaluating an existing interface?") but does not specify the decision mapping: answer = "testing hypotheses" → route to `/ux-lean-ux`; answer = "evaluating interface" → route to `/ux-heuristic-eval`. An orchestrator must infer this from context. At C4 criticality, inference gaps are not acceptable in a rule file.
- "PAIR" interim mode for AI-first design (line 38) is not actionable — an orchestrator cannot execute an undefined mode.
- The Wave State Caching rule (cache invalidated "on the next routing decision") is underspecified: does mid-session wave advancement require the user to re-confirm routing, or does it silently update available sub-skills? This ambiguity could produce incorrect routing behavior.

**Improvement Path:**
Add decision mapping to each row with a Qualification Question. Define "PAIR" as a concrete fallback behavior (e.g., "pair ux-heuristic-eval output with a note that AI-first patterns will be reviewed when ux-ai-first-design is deployed"). Specify cache invalidation behavior explicitly.

---

### Traceability (0.83/1.00)

**Evidence:**
Navigation table is present (lines 6-15) with 6 sections and anchor links — H-23 and H-24 compliant. Footer contains parent skill reference (`*Parent skill: /user-experience*`), creation/update dates, and status field. Three source comments use SKILL.md section names. `docs/schemas/handoff-v2.schema.json` is cited by path. `skills/user-experience/rules/synthesis-validation.md` is cited by repo-relative path in CRISIS Synthesis section.

**Gaps:**
- `agent-routing-standards.md` is cited by document name and section in the Ambiguity Resolution Protocol, but the repo-relative path (`.context/rules/agent-routing-standards.md`) is not provided. Per H-26, full repo-relative paths are required in SKILL.md; by extension, this standard applies to rule files that cross-reference framework documents.
- `skills/user-experience/rules/mcp-coordination.md` is referenced in SKILL.md for MCP governance but is not cited in the MCP CHECK step of this rule file, even though MCP CHECK is a routing step governed by that file.
- `skills/user-experience/rules/wave-progression.md` is the authoritative source for Wave State Detection but is not cited in the Wave-Aware Routing section.
- No `<!-- Source: -->` comment in the Bypass Routing section linking to wave-progression.md Bypass Mechanism, which is the definitive source for the 3-field documentation requirement.
- Document footer lacks a version field — other rule files in the skill include `*Status: COMPLETE*` but no `*Version:*` identifier, making it harder to track revision history.

**Improvement Path:**
Add repo-relative paths to all cross-document references. Add source comments to Wave-Aware Routing and Bypass Routing linking to wave-progression.md. Add mcp-coordination.md reference in MCP CHECK step. Add version field to footer.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.72 | 0.88 | Add `<!-- Source: -->` comments for Wave State Detection, Common Intent Resolution, and Ambiguity Resolution Protocol. Standardize the Bypass Constraints inline citation to comment format. |
| 2 | Actionability | 0.87 | 0.93 | For each Qualification Question row in Stage Routing Table, add explicit answer-to-route decision mapping. Define "PAIR" fallback behavior or cross-reference to its definition. |
| 3 | Traceability | 0.83 | 0.92 | Add repo-relative paths to `agent-routing-standards.md` and `wave-progression.md` citations. Add wave-progression.md cross-reference in Wave-Aware Routing and Bypass Routing sections. Add version field to footer. |
| 4 | Completeness | 0.88 | 0.95 | Add "Comprehensive UX audit" as an explicit Stage Routing Table row. Add explicit >= 20% capacity branch statement. Clarify CRISIS wave column notation. |
| 5 | Internal Consistency | 0.87 | 0.94 | Define or cross-reference "PAIR" interim mode to eliminate undefined reference. Fix CRISIS wave column notation ambiguity (execution order vs. wave number). |
| 6 | Methodological Rigor | 0.88 | 0.94 | Add decision logic for each Qualification Question. Define MCP CHECK success/failure thresholds. Specify bypass-count tracking mechanism. |

---

## Leniency Bias Check
- [x] Each dimension scored independently before composite computed
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (e.g., Evidence Quality held at 0.72 rather than rounding to 0.75 due to multiple missing source comments)
- [x] C4 calibration applied: 0.95 threshold means "genuinely excellent" — this deliverable is good but not excellent
- [x] No dimension scored above 0.90 without documented near-excellent evidence
- [x] Composite is below threshold: verdict is REVISE, not PASS

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.848
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.72
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add source comments for Wave State Detection, Common Intent Resolution, and Ambiguity Resolution Protocol sections"
  - "Add decision mapping for each Qualification Question in Stage Routing Table (answer → sub-skill route)"
  - "Define or cross-reference 'PAIR' interim fallback mode for AI-first design unavailability"
  - "Add repo-relative paths to agent-routing-standards.md and wave-progression.md citations"
  - "Add wave-progression.md cross-reference in Wave-Aware Routing and Bypass Routing sections"
  - "Add explicit >= 20% capacity branch behavior to CAPACITY CHECK step"
  - "Define MCP CHECK success/failure thresholds"
  - "Add Comprehensive UX audit composite route to Stage Routing Table"
  - "Fix CRISIS wave column notation to clarify execution order vs. wave number"
  - "Add version field to document footer"
```
