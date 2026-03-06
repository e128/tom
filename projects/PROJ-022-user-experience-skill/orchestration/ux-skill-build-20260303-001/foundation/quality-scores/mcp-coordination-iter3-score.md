# Quality Score Report: MCP Coordination Rules

## L0 Executive Summary
**Score:** 0.956/1.00 | **Verdict:** PASS | **Weakest Dimension:** Evidence Quality (0.92)
**One-line assessment:** The iter3 revision fully resolves all six iter2 gaps — the critical REQ/COND matrix contradiction is corrected, Memory-Keeper scope is explicitly stated, all source annotations carry anchor links, the timeout definition is operationalized, and elaboration attribution is distinguished from sourced content — producing a governance artifact that meets the C4 quality threshold of 0.95.

---

## Scoring Context
- **Deliverable:** `skills/user-experience/rules/mcp-coordination.md`
- **Deliverable Type:** Rule File (governance artifact)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Prior Score (iter2):** 0.884 (REVISE)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 3

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.956 |
| **Threshold** | 0.95 (C4 override; standard H-13 is 0.92) |
| **Verdict** | PASS |
| **Strategy Findings Incorporated** | No — standalone S-014 scoring |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.96 | 0.192 | All 10 sub-skills in matrix; all 6 MCPs covered; Memory-Keeper scope note fully resolves iter2 gap; COND instantiation note closes taxonomy completeness; minor residual: no MCP-M-001/MCP-M-002 registration entry for ux-orchestrator in Agent Integration Matrix per mcp-tool-standards.md |
| Internal Consistency | 0.20 | 0.97 | 0.194 | Critical REQ/COND contradiction fully resolved; wave-conditionality vs. MCP-dependency distinction explicitly documented; COND instantiation note confirms zero current COND dependencies; internal taxonomy applied consistently across all tables |
| Methodological Rigor | 0.20 | 0.96 | 0.192 | Timeout definition added (> 5s, 1 retry); failure conditions enumerated (a/b/c); probe implementation elaboration properly attributed; all enforcement rules retain MUST-level language; adapter architecture pattern unchanged and sound |
| Evidence Quality | 0.15 | 0.92 | 0.138 | All source annotations now include anchor links to SKILL.md; elaboration vs. source distinction documented in MCP Availability Detection; canonical tool names present; minor residual: Context7 Usage source annotation references line numbers in parenthetical (e.g., "SKILL.md lines 434-439") but those line references are inherently fragile — anchor links would be more durable; still substantively accurate |
| Actionability | 0.15 | 0.96 | 0.144 | Future MCP Probes now links to Adapter Architecture Pattern step 1; timeout definition makes detection protocol fully implementable; all enforcement rules retain specific behavioral outcomes; cost tier routing cross-reference unchanged and sufficient |
| Traceability | 0.10 | 0.97 | 0.097 | VERSION upgraded to 1.1.0; GOVERNANCE and PROJECT fields added to header; all source annotations carry anchor links to SKILL.md sections; revision history note at footer documents what iter3 addressed; all 5 sibling rules present in footer |
| **TOTAL** | **1.00** | | **0.957** | |

> **Computed composite:** (0.96 × 0.20) + (0.97 × 0.20) + (0.96 × 0.20) + (0.92 × 0.15) + (0.96 × 0.15) + (0.97 × 0.10) = 0.192 + 0.194 + 0.192 + 0.138 + 0.144 + 0.097 = **0.957**

---

## Detailed Dimension Analysis

### Completeness (0.96/1.00)

**Evidence:**

All 10 sub-skills appear in the MCP Dependency Matrix (lines 28-39). All 6 design-tool MCPs are columns. All 8 sections listed in the navigation table are present in the document body.

The Memory-Keeper scope exclusion note (lines 26-27) is thorough: it names the three canonical Memory-Keeper tool identifiers (`mcp__memory-keeper__store`, `mcp__memory-keeper__retrieve`, `mcp__memory-keeper__search`), cites MCP-002 with a link to `mcp-tool-standards.md [Memory-Keeper Integration]`, identifies that `ux-orchestrator` is the only agent using Memory-Keeper, and explains the rationale (sub-skill state is engagement-scoped per P-002). This fully resolves the iter2 completeness gap.

The COND instantiation note (lines 53-54) fills the taxonomy completeness gap: it confirms that no current sub-skill carries a COND MCP dependency, provides a concrete example of when COND would apply (Hotjar Bridge + MAU threshold), and explicitly distinguishes COND from wave deployment conditionality. This closes the previously implicit gap.

All degraded modes are defined: Context7 (2 entries in Currently Exercisable Fallbacks), plus all 6 future adapter tools in Future Adapter Fallbacks. All 6 planned adapters are in the Planned Adapters table with priority, rationale, and authentication method.

**Gaps:**

One minor completeness gap remains: `mcp-tool-standards.md` Section "Agent Integration Matrix" is the SSOT for MCP tool-to-agent mappings. The `ux-orchestrator` agent (Memory-Keeper: store, retrieve, search) does not appear in that matrix — but adding new agents to the framework's central Agent Integration Matrix is an upstream governance action that belongs to `mcp-tool-standards.md` maintenance, not to `mcp-coordination.md`. This document correctly documents what `ux-orchestrator` does with Memory-Keeper; it cannot update the SSOT itself. At the rule-file scope, completeness is 0.96.

**Improvement Path:**

File a follow-on task to update `mcp-tool-standards.md` Agent Integration Matrix to add `ux-orchestrator` (Memory-Keeper: store, retrieve, search) and `ux-atomic-architect`, `ux-inclusive-evaluator`, `ux-ai-design-guide` (Context7: resolve, query). This is an upstream governance action outside this document's scope.

---

### Internal Consistency (0.97/1.00)

**Evidence:**

The critical iter2 contradiction is fully resolved. The MCP Dependency Matrix (line 39) now shows `/ux-ai-first-design` Figma = `**REQ**`, matching SKILL.md line 411 exactly.

The source annotation (line 24) provides explicit resolution reasoning: "Note: `/ux-ai-first-design` has Figma **REQ** dependency (SKILL.md line 411). The sub-skill itself is conditionally deployed (Wave 5 COND entry criteria: Enabler DONE + WSM >= 7.80, per SKILL.md [Wave Architecture](../SKILL.md#wave-architecture) line 267), but when invoked, Figma is a required dependency — wave deployment conditionality and MCP dependency classification are independent dimensions." This is the exact "Option A" resolution recommended in iter2.

The COND instantiation note (line 53) reinforces internal consistency: "No current sub-skill has a COND MCP dependency in the matrix above. All dependencies are classified as REQ or ENH." This ensures the COND definition in the taxonomy table does not create false reader expectations about the current matrix.

The Figma Dependency Risk Profile (lines 110-111) now correctly includes `/ux-ai-first-design` as a REQ dependency (4 REQ sub-skills: ux-heuristic-eval, ux-inclusive-design, ux-design-sprint, ux-ai-first-design), consistent with the matrix.

All other consistency checks from iter2 remain sound: REQ/ENH taxonomy applied consistently, degraded mode descriptions align with risk profile fallbacks, cost tier text-only mode aligns with Free tier sub-skills, Context7 enforcement rules match `mcp-tool-standards.md` MCP-001 exactly.

**Gaps:**

One sub-minor tension: The Figma Dependency Risk section (lines 112-117) includes `/ux-ai-first-design` in the Quality Impact table ("Significant: AI interaction patterns benefit from visual prototyping"). The source annotation note clarifies that the REQ dependency applies when the sub-skill is invoked. The COND instantiation note says "No current sub-skill has a COND MCP dependency." These two together are logically sound — `/ux-ai-first-design` is conditionally deployed but when deployed its Figma dependency is REQ. The document does not contradict itself on this; it explains the distinction. No actual inconsistency; deducting 0.03 for the minor cognitive complexity this explanation chain imposes on a reader needing to integrate three sections to fully understand the `/ux-ai-first-design` posture.

**Improvement Path:**

Consider adding a single cross-reference sentence to the Figma Dependency Risk section: "Note: `/ux-ai-first-design` is a conditional sub-skill (see [MCP Dependency Matrix](#mcp-dependency-matrix) source annotation for the wave-conditionality vs. MCP-dependency distinction)." This makes the chain self-contained within the Figma risk section.

---

### Methodological Rigor (0.96/1.00)

**Evidence:**

The timeout definition (line 185) is now precise and implementable: "a timeout is defined as > 5 seconds with no response from the MCP server. One retry is attempted after a timeout before declaring the MCP unavailable." This closes the iter2 gap exactly as recommended.

The failure conditions (line 187) are now enumerated: "(a) timeout exceeding 5 seconds after 1 retry, (b) error response from the MCP server, or (c) MCP server unreachable." Three named conditions provide exhaustive coverage of MCP failure modes.

The probe implementation (line 185) remains specific: `mcp__context7__resolve-library-id` with "WCAG" as the test library — testable and deterministic.

The REQ/ENH/COND taxonomy enforcement rules (lines 57-59) retain MUST-level language with specific behavioral outcomes for each classification.

The Adapter Architecture Pattern (lines 213-220) is unchanged from iter2 and remains rigorous: 5-step pattern (health probe, authentication, read operations, write operations, fallback path) applicable uniformly to all future adapters.

The Security Considerations (lines 234-240) retain MUST NOT language for four specific prohibited behaviors. The reference to `/eng-team` integration (line 235) with link to SKILL.md cross-skill section is appropriate.

**Gaps:**

The Future MCP Probes clarification (line 192) adds: "Each probe endpoint specification follows the Adapter Architecture Pattern step 1 (health probe endpoint) defined in [Future MCP Adapters](#future-mcp-adapters)." This is correct but slightly circular — the Adapter Architecture Pattern says step 1 is a "health probe endpoint" without specifying what that endpoint is for each tool. A reader cannot implement a Figma probe from this specification alone. This is the appropriate level of detail for a pre-implementation architecture document, but it is a mild methodological gap at the C4 rigor bar.

**Improvement Path:**

When Figma/Miro/Storybook adapters move into implementation scope (post-PROJ-022), the probe endpoint specifications should be the first artifact produced and cross-referenced here. No immediate action needed; the current level of detail is appropriate for architecture-only scope.

---

### Evidence Quality (0.92/1.00)

**Evidence:**

All source annotations now include anchor links to SKILL.md sections:
- Line 24: `SKILL.md [MCP Integration Architecture](../SKILL.md#mcp-integration-architecture)`
- Line 45: `SKILL.md [MCP Integration Architecture](../SKILL.md#mcp-integration-architecture)`
- Line 65: cites `SKILL.md [MCP Integration Architecture](../SKILL.md#mcp-integration-architecture)` — text-only mode
- Line 108: `SKILL.md [Figma Dependency Risk Profile](../SKILL.md#figma-dependency-risk-profile)`
- Line 129: `SKILL.md [Current Jerry MCP Integration](../SKILL.md#current-jerry-mcp-integration)` and `mcp-tool-standards.md MCP-001`
- Line 163: `SKILL.md [Cost Tiers](../SKILL.md#cost-tiers)`
- Line 179: `SKILL.md [Lifecycle-Stage Routing](../SKILL.md#lifecycle-stage-routing) — MCP CHECK step (SKILL.md line 303)`
- Line 205: `SKILL.md [MCP Integration Architecture](../SKILL.md#mcp-integration-architecture) — architecture + fallback paths only`

The MCP Availability Detection source annotation (line 179) now explicitly distinguishes elaborated content: "Probe implementation details (WCAG test call, caching, timeout handling, retry policy) are elaborations operationalizing the SKILL.md specification; the SKILL.md defines the MCP CHECK step conceptually and this section provides the concrete implementation protocol." This resolves the iter2 attribution gap.

MCP-001 is cited with full context in two places (preamble line 5, Context7 Usage section line 133). Canonical tool names use exact `mcp__context7__` format throughout. Cross-references to 5 sibling rule files are present in both preamble and footer.

**Minor gaps:**

Some source annotations use fragile line-number references: line 24 ("SKILL.md lines 400-411"), line 45 ("SKILL.md line 413"), line 163 ("SKILL.md lines 426-432"), line 205 ("SKILL.md lines 396-445"). Line numbers in a living document are inherently fragile — if SKILL.md is edited, these line references become inaccurate while the anchor links remain valid. The anchor links are present and correct; the line numbers are supplementary and non-authoritative, but their presence creates a dual-source risk. This is a minor evidence quality gap (not a correctness issue, but a durability concern).

The Context7 UX Framework Examples table (lines 150-158) cites specific libraries and agents. The "Nielsen Norman Group" entry maps to `ux-heuristic-evaluator` with usage "Heuristic definitions and severity scales." Nielsen Norman Group is a research organization, not a library with a Context7 entry. `mcp__context7__resolve-library-id` would likely return no match for "Nielsen Norman Group" — the WebSearch fallback would apply. The entry is not wrong, but it creates an implicit expectation that Context7 covers NNG content, which it likely does not.

**Improvement Path:**

1. Remove line-number references from source annotations; rely on anchor links alone. This reduces fragility without losing traceability.
2. Mark "Nielsen Norman Group" in the Context7 UX Framework Examples table with a note: "WebSearch fallback expected (not a Context7-indexed library); include in examples as reference point for research source, not Context7 coverage." Or replace with a Context7-compatible entry (e.g., "WCAG 2.2 specification" via a W3C package reference).

---

### Actionability (0.96/1.00)

**Evidence:**

The 4-step detection protocol (lines 181-188) is now fully implementable: step 1 specifies the probe call, timeout value (5s), and retry count (1); step 2 specifies caching behavior; step 3 enumerates all three failure conditions; step 4 specifies disclosure text format with explicit placeholders.

The Future MCP Probes table (lines 194-199) includes the clarification (line 192) that links Figma/Miro/Storybook probe implementations to the Adapter Architecture Pattern step 1. This acknowledges the gap without overpromising.

The Degraded Mode Disclosure template (lines 97-102) remains copy-paste ready with three placeholder variables.

The Enforcement Rules (lines 57-59) maintain three distinct behavioral paths with MUST-level language for REQ and COND dependencies. The orchestrator can implement these as conditional branches.

The Security Considerations (lines 234-240) use MUST NOT language for four specific prohibited behaviors — each is testable (no tokens in context, no tokens in output files, env var storage, no auth state in error messages).

Cost Tier Routing (lines 171-173) references `ux-routing-rules.md [Lifecycle Stage Router]` for the CAPACITY CHECK decision point. This cross-reference is complete: rule file and section named.

**Gaps:**

The Future Adapter Fallbacks table (lines 84-91) lists 6 future tools with degraded mode descriptions. The degraded mode for "Hotjar (Bridge)" is "Manual analytics input: user provides behavioral data via text description." This is functionally correct but does not indicate what format the user should provide behavioral data in (e.g., structured table, free-text narrative, specific metrics). For a governance artifact at C4 criticality, this minor specification gap in the most complex fallback path (behavioral analytics involves heatmaps, session recordings, funnel data) is worth noting.

**Improvement Path:**

Enhance the Hotjar degraded mode description: "Manual analytics input: user provides behavioral data via structured description (e.g., funnel drop-off rates, heatmap observations, session recording summaries) or screen-recorded video." This gives agent implementors a concrete input specification.

---

### Traceability (0.97/1.00)

**Evidence:**

The VERSION header (line 1) is upgraded to v1.1.0 and now includes anchor-level section references: `Sections "MCP Integration Architecture" (#mcp-integration-architecture), "Current Jerry MCP Integration" (#current-jerry-mcp-integration), "Figma Dependency Risk Profile" (#figma-dependency-risk-profile), "Cost Tiers" (#cost-tiers), "Lifecycle-Stage Routing" (#lifecycle-stage-routing)`. GOVERNANCE and PROJECT fields are added.

The footer (lines 244-254) now includes:
- Rule file name and version
- Parent skill
- Parent SKILL.md path
- MCP governance SSOT with MCP-001/MCP-002 citation
- Canonical tool names SSOT
- Project scope reference
- All 5 sibling rules
- Created and updated dates
- A complete revision history note listing all 5 categories of iter3 changes

The revision note (line 253) provides explicit traceability back to what the iteration addressed: "Revision: iter3 — addressed Internal Consistency (REQ/COND clarification, degraded mode separation), Completeness (Memory-Keeper scope note, COND instantiation), Traceability (anchor links, PROJ-022 path, MCP-001 citations), Methodological Rigor (timeout definition, failure conditions), Evidence Quality (canonical tool names, source annotation precision)."

Every section has a source annotation with an anchor link. The Dependency Classifications section (line 45) traces to the SKILL.md definition. The Figma risk section (line 108) traces to the risk profile with anchor. The cost tiers (line 163) trace to SKILL.md cost tiers section. The MCP availability detection (line 179) traces to lifecycle-stage routing with line number.

**Gaps:**

The SKILL.md line numbers in source annotations (noted under Evidence Quality) are also a minor traceability concern — line-number-based traceability is less durable than anchor-link traceability. Anchor links are present and correct. The line numbers are supplementary and could be removed without harming traceability. This is a 0.03 deduction shared with Evidence Quality.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.92 | 0.95 | Remove supplementary line-number references from source annotations (e.g., "SKILL.md lines 400-411"); retain anchor links only. Line-number references are fragile in living documents and create dual-source traceability risk. |
| 2 | Evidence Quality | 0.92 | 0.95 | Mark "Nielsen Norman Group" in Context7 UX Framework Examples table with a note that it is a WebSearch fallback resource (not a Context7-indexed library), or replace with a Context7-compatible entry. Prevents false expectation that Context7 covers NNG content. |
| 3 | Internal Consistency | 0.97 | 0.99 | Add a cross-reference sentence in the Figma Dependency Risk section pointing to the MCP Dependency Matrix source annotation for the wave-conditionality vs. MCP-dependency distinction. Makes the reasoning self-contained within the risk section. |
| 4 | Actionability | 0.96 | 0.98 | Enhance Hotjar degraded mode description to specify the expected input format for manual analytics data (funnel drop-off rates, heatmap observations, session recording summaries). Gives sub-skill implementors a concrete input specification. |
| 5 | Completeness | 0.96 | 0.97 | File follow-on task to update `mcp-tool-standards.md` Agent Integration Matrix to register `ux-orchestrator` (Memory-Keeper) and Context7-using UX agents. Upstream governance action; outside this document's scope but necessary for SSOT completeness. |

---

## Leniency Bias Check
- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score: specific line numbers and quoted content used for all scoring claims
- [x] Uncertain scores resolved downward: Evidence Quality was the most uncertain dimension at the high end; scored 0.92 not 0.95 due to fragile line-number references and Nielsen Norman Group mapping ambiguity — both are concrete, documented gaps
- [x] First-draft calibration not applicable: this is iteration 3 of a mature governance artifact; but C4 threshold is 0.95, a high bar; composite of 0.957 exceeds threshold by only 0.007, which is appropriate for a document with minor residual gaps
- [x] No dimension scored above 0.97 without exceptional evidence: highest dimension scores (Internal Consistency 0.97, Traceability 0.97) are justified by full resolution of the prior critical contradiction and comprehensive anchor-link traceability across all sections
- [x] Anti-leniency check applied: actively sought remaining gaps in each dimension; found Nielsen Norman Group mapping ambiguity (Evidence Quality), Hotjar input format gap (Actionability), `/ux-ai-first-design` multi-section explanation chain (Internal Consistency), and upstream SSOT registration gap (Completeness) — none rose to score-depressing level given iter3 revisions, but all are documented

---

## Delta Analysis (iter2 -> iter3)

| Dimension | iter2 Score | iter3 Score | Delta | Explanation |
|-----------|------------|------------|-------|-------------|
| Completeness | 0.92 | 0.96 | +0.04 | Memory-Keeper scope note fully resolves prior gap; COND instantiation note closes taxonomy completeness |
| Internal Consistency | 0.72 | 0.97 | +0.25 | Critical REQ/COND contradiction resolved; wave-conditionality distinction explicitly documented |
| Methodological Rigor | 0.92 | 0.96 | +0.04 | Timeout definition (> 5s, 1 retry) and three enumerated failure conditions close the operationalizability gap |
| Evidence Quality | 0.90 | 0.92 | +0.02 | Anchor links added to all source annotations; elaboration vs. source distinction documented; residual gaps (line-number fragility, NNG mapping) prevent full 0.95+ |
| Actionability | 0.92 | 0.96 | +0.04 | Future MCP Probes cross-reference to Adapter Architecture Pattern closes the vagueness gap; timeout makes detection protocol fully implementable |
| Traceability | 0.90 | 0.97 | +0.07 | Anchor links in VERSION header and all source annotations; revision history note; GOVERNANCE and PROJECT header fields |
| **Composite** | **0.884** | **0.957** | **+0.073** | All six iter2 improvement recommendations addressed; composite crosses C4 threshold |

---

## Session Context (Handoff Schema)

```yaml
verdict: PASS
composite_score: 0.957
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.92
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Remove fragile line-number references from source annotations; retain anchor links only"
  - "Mark Nielsen Norman Group in Context7 UX Framework Examples as WebSearch fallback, not Context7-indexed"
  - "Add cross-reference in Figma Dependency Risk section to MCP Dependency Matrix source annotation for wave-conditionality distinction"
  - "Enhance Hotjar degraded mode to specify expected manual analytics input format"
  - "File follow-on task to update mcp-tool-standards.md Agent Integration Matrix with ux-* agents"
```

---

*Score report: mcp-coordination-iter3-score.md*
*Deliverable scored: `skills/user-experience/rules/mcp-coordination.md`*
*Scoring agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Prior score: 0.884 (iter2, REVISE)*
*Created: 2026-03-04*
