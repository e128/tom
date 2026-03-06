# Quality Score Report: MCP Runbook -- Heuristic Evaluation Sub-Skill

## L0 Executive Summary

**Score:** 0.930/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.92) / Traceability (0.92) (tied)

**One-line assessment:** Iter6 fixes are all confirmed present and correctly implemented -- the synthesis-validation.md category mismatch is cleanly resolved, the Step 5 WebSearch parenthetical closes the NNG/Context7 inconsistency, and the forward references now name PROJ-022 Wave 1 as the tracking initiative -- but the document scores 0.930, unchanged from iter5, because the forward references still defer to "task IDs to be assigned when Wave 1 signoff completes" rather than providing actual identifiers, keeping Evidence Quality and Traceability at 0.92 rather than 0.94+.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/rules/mcp-runbook.md`
- **Deliverable Type:** Rules document (operational MCP runbook for sub-skill)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scoring Iteration:** 7 (trajectory: 0.892 -> 0.922 -> 0.913 -> 0.893 -> 0.930 -> 0.910 -> 0.930)
- **Threshold:** 0.95 (C4)
- **Scored:** 2026-03-04
- **Parent Artifacts Read:** `skills/user-experience/rules/mcp-coordination.md`, `skills/ux-heuristic-eval/SKILL.md`, `skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md`, `.context/rules/mcp-tool-standards.md`

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.930 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (standalone S-014 scoring) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | All major MCP topics covered; two forward references still lack actual ticket IDs (deferred to "Wave 1 signoff"), reducing ceiling marginally |
| Internal Consistency | 0.20 | 0.95 | 0.190 | Step 5 WebSearch parenthetical resolves the last identified NNG/Context7 inconsistency; no contradictions remain |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | 5-step workflow mapping is now unambiguous; Step 2 invocation threshold ("requires external standard confirmation") remains judgment-dependent |
| Evidence Quality | 0.15 | 0.92 | 0.138 | Synthesis-validation.md category mismatch cleanly resolved with standalone definitions; deferred task IDs for forward references are a minor unsupported claim |
| Actionability | 0.15 | 0.92 | 0.138 | Specific protocol steps, per-heuristic examples, verbatim banner text, and per-failure-condition fallbacks are concrete; Step 2 threshold remains vague |
| Traceability | 0.10 | 0.92 | 0.092 | Version header and section citations are precise; forward references now name the tracking initiative but still lack actual ticket IDs for audit |
| **TOTAL** | **1.00** | | **0.930** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**
The runbook addresses all six expected topic areas for a sub-skill MCP runbook:
1. Context7 protocol: 4-step sequential procedure, per-heuristic usage examples with concrete resolve/query strings, "When NOT to Use" table, and workflow step mapping (Steps 1-5).
2. Figma MCP status: current unavailability, screenshot fallback reference, 6-row capability comparison table (screenshot-input mode vs. Figma MCP mode).
3. Screenshot-input mode protocol: supported input formats (4 rows), text-description caveats blockquote (H1/H3/H5/H7/H9 with confidence guidance), extraction target table, heuristic-specific limitations table (all 10 heuristics), impact rating attribution note.
4. MCP failure handling: Context7-specific table (4 failure conditions) and full MCP outage 4-step procedure.
5. Tool tier constraints: T1/T2/T3 breakdown with Bash discrepancy note, prohibited tools table, citation requirements (4 rules).
6. References: 5-entry table with paths, content descriptions, and footnote forward references.

**Gaps:**
Both forward references ("Context7 agent table update" and "SKILL.md Bash correction") now state they are "tracked under PROJ-022 Wave 1 implementation cleanup. Specific task IDs to be assigned when Wave 1 signoff completes." This is an improvement in disclosure language, but the underlying completeness gap remains: the parent `mcp-coordination.md` Context7 agent table does not include `ux-heuristic-evaluator`, and the SKILL.md `allowed-tools` Bash entry is inconsistent with the agent definition. These are acknowledged governance gaps that reduce completeness at C4 standard. Additionally, the Step 2 invocation trigger ("requires external standard confirmation") lacks a deterministic criterion -- a gap noted in iter6 but not addressed in iter6 fixes. Neither gap is critical, but both prevent reaching the 0.95 level.

**Improvement Path:**
Option A (preferred): Resolve the parent mcp-coordination.md agent table entry now by adding `ux-heuristic-evaluator` to the Context7 agent table -- this closes the completeness gap rather than deferring it. Option B: Assign specific PROJ-022 Wave 1 task IDs to both forward references, making the deferred resolution auditable. Refine the Step 2 invocation trigger to a deterministic condition: "when the finding cites a named platform convention, component library, or accessibility standard as the basis for a violation."

---

### Internal Consistency (0.95/1.00)

**Evidence:**
The iter6 Step 5 parenthetical fix is confirmed present at line 64: "Query for severity calibration benchmarks if uncertain about rating consistency (Resolve via WebSearch if Context7 returns no NNG results -- per the When to Use table above.)" This closes the inconsistency identified in iter6 where Step 5 directed the agent toward Context7 for NNG content, while the "When to Use" table above it stated NNG "will likely fall back to WebSearch per MCP-001." The workflow table now explicitly states the recovery path inline, making it self-consistent without requiring cross-table lookup.

Additional consistency checks all pass:
- Text-description mode caveats (H1/H3/H5/H7/H9) and screenshot limitations table (all 10 heuristics) serve different scopes and are correctly distinct. H9 is identified as HIGH impact in both sections independently and consistently ("highest-uncertainty heuristic in text-only mode" in the blockquote; "HIGH impact; error recovery quality cannot be assessed without triggering error states" in the table).
- The impact rating attribution at line 159 now explicitly states these definitions are "not derived from synthesis-validation.md (which defines HIGH/MEDIUM/LOW for cross-framework synthesis convergence gates, a different classification purpose)" -- resolving the iter6 category mismatch and making the two frameworks consistent in their claimed purposes.
- Bash discrepancy note states Bash "appears in SKILL.md allowed-tools but is not included in the current agent definition frontmatter" and clarifies this is "intentional" -- consistent with the footer line `Agent: ux-heuristic-evaluator (T3, Systematic, Haiku)` which does not claim Bash availability.
- Degraded mode banner text matches the template defined in `mcp-coordination.md` [Degraded Mode Disclosure].
- NNG caveat appears in both "When to Use Context7" table rows that reference NNG content (AI-supplement heuristics, severity calibration), with identical explanatory text in both locations.

**Gaps:**
No material internal inconsistencies remain. The deferred task IDs could theoretically create a future inconsistency if the items are resolved differently than described, but that is speculative rather than a current inconsistency. Score reflects a genuinely consistent document.

**Improvement Path:**
None required at this dimension. Score maintained as the natural ceiling given the deferred items.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**
The Step 5 WebSearch parenthetical makes the 5-step workflow table unambiguous for a systematic agent operating on a checklist. An evaluator following the workflow now has explicit recovery guidance at the exact point where NNG context7 resolution would fail, without needing to cross-reference a separate table. This is a substantive methodological improvement over iter5.

The overall methodological structure remains rigorous:
- Context7 protocol: 4-step sequential procedure with exact canonical tool names, explicit call limit compliance instruction, and fallback trigger.
- Workflow step mapping: each step specifies whether Context7 is invoked, what triggers invocation, and the rationale. Steps 3 and 4 explicitly state "No Context7 needed" with rationale -- preventing unnecessary tool calls.
- Failure handling: per-condition fallback table for Context7 failures, 4-step procedure for full outage. No generic "handle gracefully" language.
- Citation requirements: differentiates Context7-sourced, WebSearch-sourced, and knowledge-based references, operationalizing T3 tier citation guardrails.
- Tool tier tier breakdown: explains the cumulative T3 model and the authoritative vs. scope declaration distinction (agent frontmatter vs. SKILL.md `allowed-tools`).

**Gaps:**
The Step 2 invocation trigger retains "query only when the evaluator encounters a heuristic violation that requires external standard confirmation" as the activation condition. This is judgment-dependent: an evaluator has no deterministic criterion for deciding when a violation "requires external standard confirmation." The gap was noted in iter6 recommendations but was not a priority-1, -2, or -3 fix, so it remains. For a systematic agent operating on a checklist (the declared cognitive mode), judgment-dependent trigger conditions are a methodological fragility. This keeps rigor at 0.93 rather than 0.95.

**Improvement Path:**
Refine the Step 2 trigger condition to: "query only when the finding cites a named platform convention, component library, or accessibility standard as the basis for a violation (e.g., the evaluator states 'this violates Material Design's navigation guidance' or 'this fails WCAG 3.3.1')." This converts a judgment call into a deterministic text-matching condition.

---

### Evidence Quality (0.92/1.00)

**Evidence:**
The iter6 primary evidence quality gap is cleanly resolved. Line 159: "Impact ratings are defined as: HIGH = finding cannot be assessed without interactive input; MEDIUM = finding partially observable with significant gaps expected; LOW = finding directly observable in static screenshots. These are editorial assessment specific to screenshot-input mode, not derived from `skills/user-experience/rules/synthesis-validation.md` (which defines HIGH/MEDIUM/LOW for cross-framework synthesis convergence gates, a different classification purpose). P-022 disclosure: these ratings reflect evaluator judgment about screenshot-mode limitations, not empirical measurement."

This fix is correct and complete: (a) standalone definitions are provided with clear, specific criteria for each level, (b) the disavowal of synthesis-validation.md is explicit and includes an accurate description of what synthesis-validation.md actually defines (convergence gates), and (c) the P-022 disclosure is retained. A reader relying on this attribution can now correctly understand the impact rating framework without consulting synthesis-validation.md.

Other evidence quality remains strong: MCP-001 cited with `.context/rules/mcp-tool-standards.md` v1.3.1 [Context7 Integration] and "Source: FEAT-028 AC-1." `agent-development-standards.md` cited with version v1.2.0 [Tool Security Tiers]. Parent mcp-coordination.md cited with specific section anchors [MCP Availability Detection], [Degraded Mode Disclosure], [MCP Dependency Matrix]. NNG caveat explains the mechanism ("Context7 indexes software libraries, not UX consultancy content").

**Gaps:**
The two forward references contain claims that are asserted but not yet evidenced: "tracked under PROJ-022 Wave 1 implementation cleanup" is a tracking claim, but "Specific task IDs to be assigned when Wave 1 signoff completes" means no actual tracking entry exists yet. This is a minor evidence quality gap: the claim that items are "tracked" is made without a verifiable artifact (ticket ID, action item link) supporting it. A reviewer cannot confirm the tracking claim. This keeps Evidence Quality at 0.92 rather than 0.94.

**Improvement Path:**
Assign actual PROJ-022 task IDs to both forward reference items before Wave 1 signoff, or create the parent mcp-coordination.md agent table entry now and close the reference entirely. Either action converts the "tracked but unidentified" claim into a verifiable evidence trail.

---

### Actionability (0.92/1.00)

**Evidence:**
The runbook consistently provides specific, implementable guidance across all sections:
- Context7 protocol: exact canonical tool names (`mcp__context7__resolve-library-id`, `mcp__context7__query-docs`), 4-step sequential procedure.
- Per-heuristic example queries: each "When to Use Context7" table row provides a concrete `resolve: "{library}"` call and `query: "{specific question}"` string -- directly copy-pasteable.
- Degraded mode disclosure: verbatim banner text with exact three bullet points, specified to appear at report top.
- Failure handling: each of 4 Context7 failure conditions maps to a specific fallback action with output annotation instruction (e.g., "Note 'Context7 no coverage' in the evaluation output next to the affected finding").
- Text-description caveats: specifies exact flagging language ("inferred from description; verify with screenshot or interactive evaluation") for each affected heuristic.
- User notification timing: "Notify the user of screenshot-input mode status at evaluation start (before analyzing input), not only in the output report" -- specific timing instruction.
- Prohibited tools: both reason and consequence stated for each tool.
- Citation requirements: 4 rules with type-specific guidance (Context7-sourced, WebSearch-sourced, knowledge-based).

**Gaps:**
The Step 2 invocation threshold ("requires external standard confirmation") remains judgment-dependent. An evaluator uncertain whether a violation requires confirmation has no deterministic decision criterion. This is the primary actionability gap. The Step 2 "requires external standard confirmation" condition would benefit from the same deterministic reformulation noted under Methodological Rigor. This keeps actionability at 0.92 rather than 0.94+.

**Improvement Path:**
Reformulate the Step 2 trigger to a deterministic condition (as noted under Methodological Rigor). No other actionability gaps were identified.

---

### Traceability (0.92/1.00)

**Evidence:**
Version header (line 1) explicitly lists source documents (mcp-coordination.md, SKILL.md), revision history, and a precise change summary for the iter6 revision ("replaced synthesis-validation.md impact rating attribution with standalone screenshot-impact definitions, added WebSearch fallback parenthetical to Step 5 Context7 workflow for NNG queries, added PROJ-022 Wave 1 tracking note to both forward references"). Every major section begins with a governance attribution citing the specific rule (MCP-001), path, version, and section anchor. The References table provides 5 entries with full repo-relative paths and content descriptions. The ORCHESTRATION.yaml is referenced, establishing build-sequence dependency. Footer lines provide full provenance: sub-skill, parent skill, MCP governance SSOT, agent details, project, creation date.

The iter6 traceability improvement is confirmed: both forward references now read "tracked under PROJ-022 Wave 1 implementation cleanup. Specific task IDs to be assigned when Wave 1 signoff completes." This is an improvement over iter5's informal "tracked as a forward reference" language -- it names a specific initiative.

**Gaps:**
The fundamental traceability gap persists: no concrete worktracker ticket IDs exist for either forward reference item. "Tracked under PROJ-022 Wave 1 implementation cleanup" names the initiative but not the specific tracking artifact. At audit time, a reviewer cannot look up a specific ticket to verify whether the Bash discrepancy was resolved or the mcp-coordination.md agent table was updated. The traceability chain from the document's forward reference to a verifiable resolution action remains broken. This is the same gap as iter6 -- the language improvement is notable but does not close the audit trail. Score: 0.92 (marginal improvement from 0.91 due to naming the tracking initiative, but not reaching 0.93 because the actual audit trail does not exist).

**Improvement Path:**
Create PROJ-022 worktracker task entities for both items (mcp-coordination.md Context7 agent table update and SKILL.md Bash entry correction) and record their IDs in the forward reference notes. Example: "Forward reference: PROJ-022 Wave 1 cleanup task [ID-TBD after Wave 1 kickoff]." Alternatively, resolve the mcp-coordination.md agent table entry now (a low-effort change) and remove that forward reference entirely.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability / Evidence Quality / Completeness | 0.92 / 0.92 / 0.93 | 0.94 / 0.94 / 0.95 | Resolve the mcp-coordination.md parent agent table entry now by adding `ux-heuristic-evaluator` to the Context7 agent table. This single low-effort change closes the most consequential forward reference (parent document inconsistency), converting a deferred gap into a confirmed-resolved state. The second forward reference (Bash discrepancy) should receive an actual PROJ-022 task ID. |
| 2 | Methodological Rigor / Actionability | 0.93 / 0.92 | 0.95 / 0.94 | Reformulate the Step 2 Context7 invocation trigger from "requires external standard confirmation" to a deterministic condition: "when the finding cites a named platform convention, component library, or accessibility standard as the basis for a violation (e.g., evaluator states 'this violates Material Design navigation guidance' or 'this fails WCAG 3.3.1')." This converts a judgment-dependent threshold into a text-matching condition, directly supporting the systematic cognitive mode. |
| 3 | All dimensions (score plateau) | 0.930 composite | 0.95 | The document has plateaued at 0.930 across two iterations (iter5 and iter7 both score 0.930). The gap to 0.95 requires resolving the two forward reference governance gaps, not just adding tracking language. If Wave 1 task IDs cannot be assigned yet, the alternative is to resolve the parent document gaps directly (mcp-coordination.md agent table, SKILL.md Bash entry) so the forward references can be converted from "deferred" to "resolved." The 0.020 gap to threshold requires substantive closure of at least two dimensions to 0.94+. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score -- specific line numbers and text quoted from the deliverable
- [x] Uncertain scores resolved downward: Traceability held at 0.92 (not bumped to 0.93) because the naming-the-initiative improvement is marginal without actual ticket IDs
- [x] Iter6 fixes verified as confirmed present before scoring upward: Step 5 parenthetical (line 64), standalone impact definitions (line 159), tracking language in both forward references (lines 197 and 227)
- [x] Score calibration: 0.930 composite = "strong work with minor refinements needed" (0.85 calibration anchor description) -- appropriate for a document with known deferred items that prevent full governance closure
- [x] No dimension scored above 0.95 without exceptional evidence -- Internal Consistency receives 0.95 because the document genuinely has no remaining contradictions after the Step 5 fix
- [x] C4 threshold (0.95) applied correctly -- composite 0.930 is REVISE, not PASS
- [x] Oscillating trajectory acknowledged: trajectory (0.892 -> 0.922 -> 0.913 -> 0.893 -> 0.930 -> 0.910 -> 0.930) suggests the document has reached a plateau around 0.920-0.930 bounded by the deferred governance items; iter6 fixes correctly restored the 0.930 level from iter6's 0.910, but did not break through it

**Anti-leniency note:** The Internal Consistency dimension was the one candidate for generous scoring -- at 0.95, it is the highest dimension. The rationale is that the Step 5 fix genuinely eliminates the last identified inconsistency, and the document does not have active contradictions. Scoring it lower would not reflect the actual state of the document. The appropriate anti-leniency application is to hold Traceability, Evidence Quality, and Completeness at 0.92-0.93 rather than inflating them because the forward reference governance gaps are real, documented, and unresolved despite two revision iterations that addressed disclosure language rather than root resolution.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.930
threshold: 0.95
weakest_dimension: Evidence Quality (tied with Traceability)
weakest_score: 0.92
critical_findings_count: 0
iteration: 7
improvement_recommendations:
  - "Resolve mcp-coordination.md parent agent table entry now (add ux-heuristic-evaluator to Context7 agent table) to close the primary governance gap instead of deferring it -- this is the lowest-effort highest-impact action"
  - "Assign actual PROJ-022 Wave 1 task IDs to the Bash discrepancy forward reference, or fix the SKILL.md allowed-tools Bash entry directly"
  - "Reformulate Step 2 Context7 invocation trigger from judgment-dependent to deterministic: 'when the finding cites a named platform convention, component library, or accessibility standard'"
```

---

*Score Report: mcp-runbook-iter7-score.md*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*Deliverable Version: v1.6.0 (iter6 revision)*
*Project: PROJ-022 User Experience Skill*
*Scoring Iteration: 7*
*Created: 2026-03-04*
