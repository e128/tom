# Quality Score Report: MCP Runbook -- Heuristic Evaluation Sub-Skill

## L0 Executive Summary

**Score:** 0.893/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.86)
**One-line assessment:** The runbook is operationally strong with well-traced citations and no internal contradictions, but falls short of the C4 threshold (0.95) due to three missing heuristic-specific limitation rows (H4, H9, H10), an unsupported WebFetch/Figma URL capability claim, and confidence-impact judgments in the limitations table that lack source traceability.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/rules/mcp-runbook.md`
- **Deliverable Type:** Rules/Runbook
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold Applied:** 0.95 (C4 as specified by user; SSOT H-13 minimum is 0.92 for C2+)
- **Iteration:** 4 (trajectory: 0.892 → 0.922 → 0.913 → 0.893)
- **Scored:** 2026-03-04T00:00:00Z
- **Prior Iteration Applied Fixes:** ORCHESTRATION.yaml reference, Bash tool clarification, PLAN.md reference, extended limitations table (7/10 heuristics), version pins on rule files

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.893 |
| **Threshold (C4, user-specified)** | 0.95 |
| **Threshold (SSOT H-13, C2+)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (no adv-executor reports provided) |
| **Trajectory** | 0.892 → 0.922 → 0.913 → 0.893 (declining from iter2 peak) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.87 | 0.174 | 7/10 heuristic limitation rows present; H4, H9, H10 missing; Bash discrepancy documented without resolution path |
| Internal Consistency | 0.20 | 0.93 | 0.186 | No contradictions; all discrepancies explicitly documented; banner text matches parent artifacts exactly |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | Sound step-by-step protocol aligned with mcp-tool-standards.md; workflow-step Context7 mapping is rigorous; incomplete limitations table reduces rigor |
| Evidence Quality | 0.15 | 0.86 | 0.129 | Most claims cited with version and section; WebFetch/Figma URL claim unverified; pre-evaluation notification lacks citation; confidence-impact judgments unsourced |
| Actionability | 0.15 | 0.89 | 0.134 | Failure handling and Context7 protocol are precise and executable; 3 missing limitation rows reduce actionability for H4/H9/H10 |
| Traceability | 0.10 | 0.91 | 0.091 | References section with path+content; in-document citations with version numbers and anchors; confidence-impact judgments in limitations table not traced |
| **TOTAL** | **1.00** | | **0.893** | |

---

## Detailed Dimension Analysis

### Completeness (0.87/1.00)

**Evidence:**

The runbook covers all its stated sections: Context7 protocol (4-step, with when-to-use and when-not-to-use tables), the workflow-step-to-Context7 mapping for all 5 evaluation steps, Figma current status with capability comparison table, screenshot-input mode with supported formats and extraction targets, MCP failure handling for both Context7 failure modes and full outage, tool tier breakdown with prohibited tools and citation requirements, and a References section with 5 source documents.

The iter3 fix to "extend limitations table" added rows for H2 (Match Between System and Real World), H6 (Recognition Rather Than Recall), and H8 (Aesthetic and Minimalist Design), completing 7 of 10 heuristic limitation rows.

**Gaps:**

1. **H4 (Consistency and Standards) — missing limitation row.** H4 is directly impacted by screenshot-input mode: cross-screen consistency cannot be verified without interactive navigation, and platform convention adherence for hover/focus states is unobservable. This is a significant omission given that H4 is a primary heuristic frequently violated in static designs.

2. **H9 (Help Users Recognize, Diagnose, and Recover from Errors) — missing limitation row.** Error states typically require triggering (form submission, invalid input). Screenshot-input mode cannot capture dynamic error presentation. Finding confidence for H9 violations found in screenshots that happen to capture error states versus those inferred from form design is meaningfully different.

3. **H10 (Help and Documentation) — missing limitation row.** Tooltip and contextual help visibility may be screenshot-dependent (e.g., hover-triggered tooltips not visible). Lower impact than H4/H9 but still a gap.

4. **Bash discrepancy — documented but unresolved.** The runbook correctly notes the Bash discrepancy (SKILL.md lists Bash in `allowed-tools`; agent frontmatter does not). However, it provides no resolution path: Is Bash intended for the agent? Will the agent frontmatter be updated? Is it intentionally excluded? The forward reference notes the Context7 table update but says nothing about Bash.

**Improvement Path:**

Add three rows to the heuristic-specific limitations table: H4, H9, H10 with limitation description and finding confidence impact. Add a one-sentence resolution statement for the Bash discrepancy (e.g., "Bash is excluded from the agent `tools` field intentionally because [reason]; the SKILL.md entry will be corrected in PROJ-022 EPIC-002 cleanup" or "Bash will be added to the agent frontmatter in Wave 1 implementation").

---

### Internal Consistency (0.93/1.00)

**Evidence:**

- The degraded mode banner (3 bullet points) matches the canonical template in `skills/user-experience/rules/mcp-coordination.md` [Degraded Mode Disclosure] exactly: "Cannot inspect component states (hover, focus, active, disabled)", "Cannot verify responsive behavior across breakpoints", "Cannot access style tokens or design system variables programmatically."
- The runbook states Figma is classified as REQ for `/ux-heuristic-eval` — confirmed by mcp-coordination.md dependency matrix row.
- The Context7 4-step protocol matches mcp-tool-standards.md v1.3.1 [Context7 Integration] exactly.
- The NNG fallback caveat appears consistently in two table rows with identical phrasing.
- The tool tier breakdown (T1 cumulative into T3) is internally consistent with agent-development-standards.md tier model.
- The known discrepancy between SKILL.md `allowed-tools` (includes Bash) and agent frontmatter `tools` (excludes Bash) is explicitly called out in a Note block rather than silently ignored, avoiding a hidden contradiction.
- The "authoritative tool declaration is in the agent definition frontmatter" statement is consistent with H-34 agent definition standards.

**Gaps:**

No actual contradictions detected. The only minor consistency observation: the runbook footer lists the agent model as "Haiku" (`*Agent: `ux-heuristic-evaluator` (T3, Systematic, Haiku)*`) — this is correct per the agent definition frontmatter `model: haiku`. Consistent.

**Improvement Path:**

No improvement needed on Internal Consistency. The explicit documentation of discrepancies (Bash, mcp-coordination.md Context7 table) is the correct handling approach.

---

### Methodological Rigor (0.90/1.00)

**Evidence:**

The runbook uses a well-structured dual-methodology approach:

1. **Protocol definition** (Context7 4-step procedure) — mirrors the canonical protocol from mcp-tool-standards.md, scoped to the heuristic evaluation domain.
2. **Trigger classification** (When-to-Use table) — maps specific evaluation steps to specific heuristics with example queries, making the invocation decision deterministic rather than discretionary.
3. **Workflow integration** (When to Query Context7 in the 5-Step Workflow) — overlays Context7 invocation on the evaluation methodology from SKILL.md, explicitly noting where Context7 is NOT needed (steps 3 and 4) with rationale.
4. **Failure handling** (MCP Failure Handling section) — uses a structured table keyed on failure condition with specific fallback action, sourced from mcp-tool-standards.md.
5. **Screenshot-input protocol** — provides structured extraction targets mapped to heuristics with explicit "What to Look For" guidance.

The "Notify the user at evaluation start, not only in the output report" instruction is a methodologically important timing constraint.

**Gaps:**

The incomplete limitations table (missing H4, H9, H10) reduces methodological rigor: an agent following the runbook has no guidance on finding confidence degradation for those three heuristics. This is a structural incompleteness in the methodology rather than a minor detail.

**Improvement Path:**

Complete the limitations table. Consider whether the "Acceptable (reduced quality)" suitability rating for "Text descriptions of interface" needs any methodological guidance on what reduced quality means in practice (e.g., which heuristics are most affected by text-only descriptions).

---

### Evidence Quality (0.86/1.00)

**Evidence for strong evidence quality:**

- References to mcp-tool-standards.md include version number (v1.3.1) and specific section anchors ([Context7 Integration], [Error Handling]).
- References to agent-development-standards.md include version number (v1.2.0) and specific section ([Tool Security Tiers], [Tier Constraints]).
- The ORCHESTRATION.yaml path and PLAN.md [Context] section reference were added in iter3.
- The NNG caveat ("Context7 indexes software libraries, not UX consultancy content") sets accurate expectations with methodological honesty.
- The Figma capability comparison table accurately distinguishes "current" from "future" capabilities without overstating.

**Specific gaps:**

1. **WebFetch/Figma URL claim (line: "Figma export URLs (public links) — Acceptable — WebFetch can retrieve publicly shared Figma frames as images").** This claim is asserted without evidence. WebFetch retrieves URLs as text/HTML. Whether Claude Code can process a Figma public link URL as an image via WebFetch is not verified and depends on whether the URL returns an image binary, a Figma viewer page (HTML), or a download redirect. If this fails at runtime, the "Acceptable" suitability rating is incorrect. The claim should either be verified and cited or qualified with "if the URL returns a directly accessible image resource."

2. **Pre-evaluation notification requirement (line: "Notify the user of screenshot-input mode status at evaluation start (before analyzing input), not only in the output report").** This is a runbook-specific operational requirement. P-022 is cited for the output disclosure but not for this pre-evaluation notification. The source of this timing requirement should be cited (or noted as a runbook-defined operational constraint not derived from a parent rule).

3. **Finding confidence impact labels ("LOW impact," "MEDIUM impact" not labeled) in the limitations table.** The "Impact on Finding Confidence" column values ("Findings about dynamic feedback are LOW confidence; note as inferred", etc.) contain confidence assessments that are editorial judgments. These are plausible and consistent with the methodology, but no source is cited for why H1 dynamic feedback is LOW confidence versus, say, MEDIUM. An explicit "Editorial assessment; no external citation" note or a reference to the synthesis-validation.md confidence scale would improve evidence quality.

**Improvement Path:**

1. Replace or qualify the WebFetch/Figma URL claim with a tested verification or an explicit uncertainty note.
2. Add a "(runbook-defined operational requirement; not derived from parent rule)" note or a P-022 citation to the pre-evaluation notification rule.
3. Add an "(Editorial assessment, calibrated against synthesis-validation.md confidence scale)" attribution to the confidence-impact column values, or replace informal labels with the formal HIGH/MEDIUM/LOW classification from synthesis-validation.md.

---

### Actionability (0.89/1.00)

**Evidence:**

The runbook is operationally strong:

- The Context7 4-step protocol is directly executable by the agent (steps numbered, tools named, conditions stated).
- The "When NOT to Use Context7" table eliminates ambiguity for 4 common false-positive scenarios.
- The failure handling table maps each failure condition to a specific action with no ambiguity (e.g., "Fall back to WebSearch for that library. Note 'Context7 no coverage' in the evaluation output next to the affected finding").
- The screenshot extraction target table maps interface elements to heuristics with "What to Look For" guidance — agents can act on this directly without interpretation.
- The prohibited tools table provides both the tool name and the specific prohibition reason.
- The citation requirements section (4 numbered rules) is precise and covers all tool types.

**Gaps:**

The absence of limitation rows for H4, H9, and H10 means an agent evaluating those heuristics in screenshot mode has no guidance on confidence level or required disclosures. This creates an actionability gap: the agent must improvise where the runbook should provide explicit guidance.

**Improvement Path:**

Complete the three missing heuristic limitation rows. Each needs: Heuristic (H4/H9/H10), Limitation (specific capability absent), Impact on Finding Confidence (LOW/MEDIUM with brief rationale). No other changes needed for actionability.

---

### Traceability (0.91/1.00)

**Evidence:**

- The References section is structured with three columns: Source, Content, Path — providing full traceability for all 5 source documents.
- The frontmatter comment enumerates: VERSION, DATE, SOURCE, PARENT, GOVERNANCE, PROJECT, REVISION — all key traceability fields.
- In-document citations include version numbers where applicable (mcp-tool-standards.md v1.3.1, agent-development-standards.md v1.2.0).
- The forward reference note explicitly tracks the pending mcp-coordination.md Context7 table update as a "PROJ-022 action item, to be resolved when Wave 1 deployment is complete" — this is proper traceability for an open item.
- Section-level citations reference specific anchors (e.g., `[MCP Availability Detection]`, `[Context7 Integration]`, `[Error Handling]`).

**Gaps:**

The "Impact on Finding Confidence" column values in the limitations table (H1: "note as inferred", H3: "findings limited to visible UI elements; flow-level assessment is inferred", etc.) are editorial assessments not traced to any source. Synthesis-validation.md is the most likely source for confidence classifications in this sub-skill's context, but it is not cited in this table. This is a minor but real traceability gap for what are effectively quality-affecting judgments.

**Improvement Path:**

Add a table footer note: "Confidence impact labels derived from editorial assessment consistent with `skills/user-experience/rules/synthesis-validation.md` [Sub-Skill Synthesis Output Map]. Not externally cited." This makes the traceability gap explicit and honest (P-022) while not requiring a full citation chain for each cell.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.87 | 0.92+ | Add 3 missing heuristic-specific limitation rows: H4 (Consistency and Standards -- cannot verify cross-screen consistency or platform hover/focus conventions), H9 (Help Users Recover from Errors -- cannot trigger error states to observe dynamic error presentation), H10 (Help and Documentation -- hover-triggered tooltips not visible in screenshots). Each row needs: Limitation column, Impact on Finding Confidence column with confidence level. |
| 2 | Evidence Quality | 0.86 | 0.91+ | Correct or qualify the WebFetch/Figma URL claim. Either: (a) verify the claim by testing a real Figma public share URL with WebFetch and documenting the result, (b) change suitability from "Acceptable" to "Acceptable if URL returns direct image resource (verify before use)", or (c) remove from the supported formats table entirely if unverified. |
| 3 | Completeness | 0.87 | 0.90+ | Add a resolution statement for the Bash discrepancy. The current note documents the gap but does not resolve it. Add one sentence: either "Bash is intentionally excluded from the agent definition; the SKILL.md `allowed-tools` entry will be corrected during EPIC-002 implementation" or "Bash will be added to the agent frontmatter when the agent body is fully implemented in Wave 1." |
| 4 | Evidence Quality | 0.86 | 0.90+ | Add sourcing for confidence-impact labels in the heuristic limitations table. A table footer note attributing these to editorial assessment aligned with synthesis-validation.md is sufficient. Also add a note or P-022 citation for the pre-evaluation notification timing requirement. |
| 5 | Traceability | 0.91 | 0.94+ | Add a one-line attribution for confidence-impact judgments in the limitations table footer (covered by Recommendation 4 above; can be combined). |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific quotes and locations
- [x] Uncertain scores resolved downward (Evidence Quality: uncertain between 0.87 and 0.86; chose 0.86)
- [x] First-draft calibration not applicable (iteration 4); trajectory decline from iter2 peak (0.922) considered
- [x] No dimension scored above 0.95 (highest is Internal Consistency at 0.93 with documented evidence)
- [x] C4 threshold (0.95 as user-specified) applied; composite 0.893 is clearly below both 0.92 and 0.95 thresholds

**Trajectory analysis:** The scoring trajectory (0.892 → 0.922 → 0.913 → 0.893) shows iter2 was the peak. Iter3 applied 5 fixes but may have introduced or exposed issues not present in the prior score. The iter3 claimed "extended limitations table" but only added 3 of the expected 6 missing rows (H2, H6, H8 were added; H4, H9, H10 remain absent). The WebFetch/Figma URL claim may have been present in prior iterations without being caught. The declining trajectory suggests diminishing returns on targeted fixes; the remaining gaps require substantive content additions rather than reference fixes.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.893
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.86
critical_findings_count: 0
iteration: 4
improvement_recommendations:
  - "Add 3 missing heuristic limitation rows: H4 (cross-screen consistency), H9 (error state triggering), H10 (hover tooltip visibility)"
  - "Correct or qualify WebFetch/Figma URL claim -- unverified capability assertion"
  - "Resolve Bash discrepancy with explicit resolution statement (intentional exclusion or planned addition)"
  - "Add sourcing for confidence-impact labels in limitations table; cite or attribute the pre-evaluation notification requirement"
  - "Add limitations table footer attributing confidence-impact assessments to synthesis-validation.md scale"
```

---

*Score Report Version: 1.0*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-heuristic-eval/rules/mcp-runbook.md` (v1.3.0)*
*Iteration: 4*
*Scored: 2026-03-04*
