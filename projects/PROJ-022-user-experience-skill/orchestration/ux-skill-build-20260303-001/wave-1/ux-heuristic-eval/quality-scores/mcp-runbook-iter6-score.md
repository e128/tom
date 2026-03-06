# Quality Score Report: MCP Runbook -- Heuristic Evaluation Sub-Skill

## L0 Executive Summary

**Score:** 0.910/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.86)

**One-line assessment:** The runbook is well-structured and operationally complete, but three specific issues prevent reaching the C4 threshold (0.95): the LOW/MEDIUM/HIGH impact ratings are attributed to a classification framework that uses those labels for a different purpose (synthesis convergence, not screenshot impact), the NNG/Context7 Step 5 implicit inconsistency is unacknowledged at the point of use, and two unresolved forward references have no tracking identifiers.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/rules/mcp-runbook.md`
- **Deliverable Type:** Rules document (operational MCP runbook for sub-skill)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scoring Iteration:** 6 (trajectory: 0.892 -> 0.922 -> 0.913 -> 0.893 -> 0.930)
- **Threshold:** 0.95 (C4)
- **Scored:** 2026-03-04

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.910 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (standalone S-014 scoring) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | All major MCP topics covered; text-description caveats and Bash note added; two acknowledged-but-unresolved gaps slightly limit ceiling |
| Internal Consistency | 0.20 | 0.93 | 0.186 | Screenshot vs. text-description sections are correctly distinct; H9 HIGH impact consistent in both locations; Bash discrepancy documented accurately |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | Workflow step mapping is thorough; NNG/Step 5 implicit inconsistency (query Context7 for severity calibration, but NNG won't resolve in Context7) unaddressed at point of use |
| Evidence Quality | 0.15 | 0.86 | 0.129 | Most claims cited precisely; however, impact ratings (LOW/MEDIUM/HIGH) attributed to synthesis-validation.md confidence classification framework, which defines those labels for synthesis convergence gates, not screenshot impact assessment -- this is a category mismatch |
| Actionability | 0.15 | 0.92 | 0.138 | Specific protocol steps, copy-paste banner text, per-failure-condition fallbacks, and per-heuristic example queries are concrete and implementable |
| Traceability | 0.10 | 0.91 | 0.091 | Strong references with specific anchors and versions; forward references lack tracking identifiers (no worktracker ticket IDs) |
| **TOTAL** | **1.00** | | **0.910** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**
The runbook covers all six expected topic areas for a sub-skill MCP runbook: (1) Context7 protocol with per-heuristic usage examples and workflow step mapping, (2) Figma MCP status and capability comparison table, (3) screenshot-input mode protocol including text-description mode caveats (added in iter5 for H1/H3/H5/H7/H9), (4) MCP failure handling with per-condition fallback table, (5) tool tier constraints and citation requirements, and (6) a References section. The text-description caveats section is substantive, covering all five elevated-uncertainty heuristics with specific confidence guidance. The Bash discrepancy note is present and explains both sides (SKILL.md vs. agent frontmatter).

**Gaps:**
Two acknowledged-but-unresolved gaps slightly reduce the completeness ceiling. First, the parent `mcp-coordination.md` Context7 agent table does not include `ux-heuristic-evaluator`, and this is noted as a forward reference with no completion date or tracking identifier. Second, the Bash discrepancy between SKILL.md `allowed-tools` and agent frontmatter is documented but unresolved, also as an informal forward reference. These are known gaps, explicitly flagged, but they represent incomplete state in the sub-skill's governance posture. At C4 standard, acknowledged gaps in parent document consistency count against completeness even when transparently disclosed.

**Improvement Path:**
Add worktracker ticket IDs to both forward references (e.g., "PROJ-022 EPIC-002 action item #N") so they are formally tracked rather than informally noted. Alternatively, resolve the parent mcp-coordination.md agent table entry now rather than deferring it.

---

### Internal Consistency (0.93/1.00)

**Evidence:**
The document maintains strong internal consistency across several dimensions:

1. **Text-description vs. screenshot sections are correctly distinct.** The text-description mode caveats blockquote (lines 108-115) lists H1, H3, H5, H7, H9 as elevated-uncertainty heuristics. The screenshot limitations table (lines 148-157) lists all 10 heuristics with impact ratings. These are correctly different: text-description uncertainty affects a different subset than screenshot-mode uncertainty. H9 is independently identified as HIGH impact in both contexts (text-description: "highest-uncertainty heuristic in text-only mode" and screenshot: "HIGH impact; error recovery quality cannot be assessed without triggering error states") -- correctly consistent.

2. **Tool tier footnote is consistent with the Bash finding.** The footnote correctly states Bash appears in SKILL.md `allowed-tools` but not in the agent definition frontmatter, and explains this is intentional. The footer line `Agent: ux-heuristic-evaluator (T3, Systematic, Haiku)` does not claim Bash is available.

3. **NNG caveat appears consistently** in both places it is referenced in the "When to Use Context7" table (AI-supplement heuristics row and severity calibration row), using identical explanatory text.

4. **Degraded mode banner text** in the screenshot-input section matches the banner defined in `mcp-coordination.md` [Degraded Mode Disclosure].

**Gaps:**
The document's "When to Query Context7 in the 5-Step Workflow" table (Step 5 entry) states the evaluator should "Query for severity calibration benchmarks if uncertain about rating consistency." The "When to Use" table above this section explicitly notes that NNG queries "will likely fall back to WebSearch per MCP-001." These two pieces of guidance are not contradictory in isolation, but they create a workflow inconsistency: Step 5 directs the agent toward Context7 for a query that Context7 is acknowledged to not serve. A careful reading resolves this (WebSearch fallback applies), but the Step 5 entry creates unnecessary ambiguity by directing "Query for severity calibration benchmarks" without noting that this will proceed via WebSearch, not Context7.

**Improvement Path:**
Add a parenthetical to the Step 5 "Context7 Action" cell: "(Resolve via WebSearch if Context7 returns no NNG results per the When to Use table above.)"

---

### Methodological Rigor (0.90/1.00)

**Evidence:**
The runbook employs a structured, layered methodology appropriate for an operational rules document:

- The Context7 protocol section is mapped to the 5-step workflow defined in SKILL.md, providing clear invocation timing guidance rather than vague "use when needed" instructions.
- The "When NOT to Use Context7" table prevents over-invocation, respecting the per-question call limit.
- The Figma capability comparison table (screenshot vs. Figma MCP mode) is specific and complete, covering 6 capability dimensions.
- The screenshot limitations table uses consistent LOW/MEDIUM/HIGH impact ratings with rationales for each heuristic.
- The failure handling section uses a per-condition table rather than generic fallback guidance.
- Citation requirements distinguish between Context7-sourced, WebSearch-sourced, and knowledge-based references, operationalizing T3 tier constraints.

**Gaps:**
The NNG/Step 5 issue identified in the Internal Consistency section is also a methodological rigor gap. The 5-step workflow table is a core methodology artifact, and Step 5 providing workflow guidance that creates ambiguity about which tool path applies (Context7 vs. WebSearch) weakens the rigor of the most operationally critical section (self-review before report generation). An evaluator following Step 5 literally would attempt Context7 for NNG content, fail, fall back to WebSearch, and proceed -- but the workflow table does not make this recovery explicit, requiring the agent to cross-reference the "When to Use" table to understand the correct path. For a systematic agent operating on a checklist, this is a methodological fragility.

**Improvement Path:**
Annotate the Step 5 "Context7 Action" cell with the fallback path inline, as noted above under Internal Consistency. This single change closes the methodological rigor gap without requiring restructuring.

---

### Evidence Quality (0.86/1.00)

**Evidence (strong areas):**
- MCP-001 cited with full path and version: `.context/rules/mcp-tool-standards.md` v1.3.1 [Context7 Integration] -- Source: FEAT-028 AC-1.
- `agent-development-standards.md` cited with version v1.2.0 [Tool Security Tiers].
- Parent mcp-coordination.md cited by specific section anchors: [MCP Availability Detection], [Degraded Mode Disclosure].
- NNG caveat explains *why* Context7 won't serve NNG queries: "Context7 indexes software libraries, not UX consultancy content."
- The impact ratings attribution includes an explicit P-022 disclosure: "ratings reflect evaluator judgment about screenshot-mode limitations, not empirical measurement."

**Gaps:**
The impact ratings attribution states they are "aligned with `skills/user-experience/rules/synthesis-validation.md` confidence classification framework." This attribution is a category mismatch. The synthesis-validation.md "Confidence Classification" section defines HIGH/MEDIUM/LOW gates for cross-framework synthesis hypotheses, based on the number of frameworks converging on a finding (HIGH = 3+ frameworks converge; MEDIUM = 2 frameworks OR 1 with strong evidence; LOW = single framework with weak evidence). The mcp-runbook.md uses LOW/MEDIUM/HIGH as impact ratings for screenshot-mode limitations -- a completely different classification purpose. The labels happen to be the same (LOW/MEDIUM/HIGH) but they represent different measurement frameworks. Citing synthesis-validation.md as the source of the impact rating framework is misleading.

This is the primary evidence quality gap. A reader relying on this attribution to understand or calibrate the impact ratings would consult synthesis-validation.md, find gate definitions that are about cross-framework convergence, and be unable to map those definitions to screenshot impact assessment.

The forward references also lack tracking identifiers. "PROJ-022 Wave 1 implementation cleanup" and "tracked as a forward reference alongside the Context7 agent table update" are informal notes without worktracker ticket numbers or acceptance criteria, making them unverifiable at audit time.

**Improvement Path:**
1. Replace the synthesis-validation.md attribution with a standalone definition: "Impact ratings (LOW/MEDIUM/HIGH) classify the degree to which each screenshot-mode limitation affects finding reliability: HIGH = finding cannot be assessed without interactive input; MEDIUM = finding partially observable, significant gaps expected; LOW = finding directly observable in static screenshots, gaps are edge cases." Remove the synthesis-validation.md cross-reference or change it to note that the label vocabulary (HIGH/MEDIUM/LOW) is borrowed from that framework, not the gate definitions.
2. Add PROJ-022 worktracker action item IDs to forward references.

---

### Actionability (0.92/1.00)

**Evidence:**
The runbook consistently provides specific, implementable guidance:

- **Context7 protocol:** 4-step sequential procedure with exact tool names (`mcp__context7__resolve-library-id`, `mcp__context7__query-docs`).
- **Per-heuristic example queries:** Each "When to Use Context7" row provides a concrete resolve target and query string (e.g., `resolve: "Material Design"` then `query: "loading indicator feedback patterns"`).
- **Degraded mode disclosure:** Exact banner text to paste verbatim, including the three bullet points.
- **Failure handling:** Each failure condition maps to a specific fallback action, not generic "handle gracefully."
- **Text-description caveats:** Each heuristic entry specifies exactly how to flag affected findings ("inferred from description; verify with screenshot or interactive evaluation").
- **Prohibited tools table:** States both the tool and the reason, enabling the agent to understand the constraint, not just apply it blindly.
- **User notification timing:** "Notify the user of screenshot-input mode status at evaluation start (before analyzing input), not only in the output report" -- specific timing instruction, not vague guidance.

**Gaps:**
The "When to Query Context7 in the 5-Step Workflow" table (Step 2 entry) says "query for heuristic-specific best practices as needed while evaluating each heuristic" and notes "query only when the evaluator encounters a heuristic violation that requires external standard confirmation." The threshold condition ("requires external standard confirmation") is judgment-dependent and could lead to inconsistent invocation behavior. An evaluator unsure whether a violation "requires confirmation" has no decision criterion. A slightly more specific threshold (e.g., "when the finding cites a specific platform standard, component library, or accessibility criterion by name") would improve actionability. This is a minor gap.

**Improvement Path:**
Refine the Step 2 Context7 invocation trigger from "requires external standard confirmation" to a more deterministic condition: "when the finding cites a named platform convention, component library, or accessibility standard as the basis for a violation."

---

### Traceability (0.91/1.00)

**Evidence:**
- Version header explicitly lists source documents and revision history with change rationale.
- Every section begins with a governance attribution (e.g., "Per MCP-001 (`.context/rules/mcp-tool-standards.md` v1.3.1 [Context7 Integration])").
- The References table provides 5 entries with specific paths, content descriptions, and document-level anchors where applicable.
- The synthesis-validation.md reference is document-level ("confidence classification framework") -- confirmed to match the actual section heading in synthesis-validation.md.
- Parent mcp-coordination.md gaps are identified and acknowledged in both the body and the References footer note.
- The footer lines provide full provenance: sub-skill, parent skill, MCP governance SSOT, project, creation date.
- The ORCHESTRATION.yaml is listed in References, establishing the build-sequence dependency.

**Gaps:**
The two forward references ("Context7 agent table update" and "SKILL.md Bash correction") are noted in the document but have no worktracker ticket IDs or acceptance criteria. These are traceability gaps: at audit time, there is no way to verify whether these forward references were resolved or abandoned. A reader reviewing the document post-Wave-1 completion cannot determine the disposition of these items without searching the worktracker independently. The traceability chain from document to resolution action is broken.

**Improvement Path:**
Add explicit worktracker entity references to both forward reference notes. Example: "Forward reference: PROJ-022 EPIC-002 Task [ID] -- SKILL.md Bash entry correction, target Wave 1 completion." This makes the traceability chain auditable.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.86 | 0.92 | Replace the synthesis-validation.md impact rating attribution with a standalone definition of LOW/MEDIUM/HIGH as screenshot-impact categories. The current attribution creates a category mismatch with synthesis-validation.md's convergence-based gate definitions. If borrowing the vocabulary, add a note that only the label names are borrowed, not the gate definitions. |
| 2 | Methodological Rigor / Internal Consistency | 0.90 / 0.93 | 0.93 / 0.95 | Add a parenthetical to the Step 5 workflow table "Context7 Action" cell noting that NNG severity calibration queries will proceed via WebSearch fallback per the "When to Use" table. This resolves the implicit inconsistency where Step 5 directs toward Context7 for content Context7 won't serve. |
| 3 | Traceability / Completeness | 0.91 / 0.93 | 0.94 / 0.95 | Add worktracker entity references (PROJ-022 ticket IDs) to both forward reference notes (Bash discrepancy and Context7 agent table update). This makes the forward references auditably tracked rather than informally noted. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computation
- [x] Evidence documented for each score -- specific text cited from the deliverable
- [x] Uncertain scores resolved downward: Evidence Quality resolved to 0.86 rather than 0.88 on recognizing the synthesis-validation.md category mismatch is genuine, not trivial
- [x] Iteration trajectory considered: iter5 scored 0.930; this iteration scored 0.910 -- the downward revision reflects stricter C4 standard application and identification of the synthesis-validation.md attribution issue not flagged in prior iterations
- [x] No dimension scored above 0.95 -- highest is 0.93 (Completeness, Internal Consistency)
- [x] C4 threshold (0.95) applied correctly -- composite 0.910 is REVISE, not PASS

**Anti-leniency note:** This scoring was performed with fresh context from all parent documents. The synthesis-validation.md attribution issue (Evidence Quality) was identified by directly reading synthesis-validation.md and verifying that the HIGH/MEDIUM/LOW gate definitions there describe cross-framework convergence count, not screenshot-impact levels. This is a genuine evidence quality gap that was not flagged in the scoring trajectory through iter5, explaining the downward movement from the iter5 score of 0.930.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.910
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.86
critical_findings_count: 0
iteration: 6
improvement_recommendations:
  - "Replace synthesis-validation.md impact rating attribution with standalone LOW/MEDIUM/HIGH screenshot-impact category definitions to remove category mismatch"
  - "Add WebSearch fallback parenthetical to Step 5 workflow table Context7 Action cell to resolve NNG/Context7 implicit inconsistency"
  - "Add PROJ-022 worktracker ticket IDs to both forward references (Bash and Context7 agent table) to create auditable traceability"
```

---

*Score Report: mcp-runbook-iter6-score.md*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*Deliverable Version: v1.5.0 (iter5 revision)*
*Project: PROJ-022 User Experience Skill*
*Created: 2026-03-04*
