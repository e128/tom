# Quality Score Report: mcp-runbook.md (iter1)

## L0 Executive Summary

**Score:** 0.879/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness (0.82)
**One-line assessment:** A well-structured and operationally detailed MCP runbook with strong Context7 integration mapping, Figma capability comparison tables, and degraded mode protocols, but missing a self-review checklist, a quality gate integration section, and any rule ID system -- three structural gaps that collectively keep this below the 0.95 C4 threshold.

---

## Scoring Context

- **Deliverable:** `skills/ux-inclusive-design/rules/mcp-runbook.md`
- **Deliverable Type:** MCP Integration Runbook
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.879 |
| **Threshold** | 0.95 (C4, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

> **Threshold note:** The standard S-014 PASS threshold is >= 0.92 (H-13). The user-specified C4 threshold is >= 0.95. The composite of 0.879 does not meet H-13 (0.92) -- this deliverable requires revision before it can meet any quality gate.

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.82 | 0.164 | 8 navigation sections present; Context7, Figma, Storybook, failure handling covered; missing self-review checklist, quality gate integration section, and rule ID governance system |
| Internal Consistency | 0.20 | 0.93 | 0.186 | Context7 trigger table aligns with 7-step workflow from inclusive-design-rules.md; Figma/Storybook classification (REQ/ENH) consistent with SKILL.md; T3 tier constraint description correctly references agent-development-standards.md |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | Per-step Context7 invocation mapping is systematic; screenshot requirements table covers 5 input types; failure handling covers 4 scenarios; T3 tier citation requirements operationalized; WebSearch escalation paths specified |
| Evidence Quality | 0.15 | 0.90 | 0.135 | MCP-001 governance cited; mcp-tool-standards.md v1.3.1 referenced; agent-development-standards.md v1.2.0 cited; cross-references to parent mcp-coordination.md valid; WCAG 2.2 and ARIA APG 1.2 listed in References |
| Actionability | 0.15 | 0.90 | 0.135 | Context7 "When to Use" and "When NOT to Use" tables are unambiguous; screenshot requirements table specifies minimum requirements per input type; MCP failure handling provides step-by-step actions; degraded mode disclosure banner is copy-ready |
| Traceability | 0.10 | 0.79 | 0.079 | VERSION header present; GOVERNANCE ID INDEX footer present but references only 5 items (MCP-001, P-002, P-022, H-34, T3 citation guardrails) -- no rule ID namespace for the runbook's own operational constraints |
| **TOTAL** | **1.00** | | **0.879** | |

---

## Detailed Dimension Analysis

### Completeness (0.82/1.00)

**Evidence:**
All 8 navigation table sections are implemented and populated. Coverage includes: Context7 usage for inclusive design with per-step trigger mapping, pre-resolved Library ID Resolution Table (7 libraries), Figma MCP dependency with capability comparison table (7 capabilities x 2 modes), Screenshot-Input Mode Protocol (P-022 banner, capability table, screenshot requirements table), Storybook dependency section, MCP failure handling (4 scenarios), Tool Usage Constraints with prohibited tools table and citation requirements.

**Gaps:**
Three structural elements present in the companion rules file and Wave 2 exemplars are absent:

1. **No Self-Review Checklist:** The `heart-methodology-rules.md` and `inclusive-design-rules.md` both include a self-review checklist (S-010 requirement). The MCP runbook has no equivalent verification checklist. Agents using this runbook cannot self-certify compliance before persisting output.

2. **No Quality Gate Integration section:** The `inclusive-design-rules.md` has a dedicated "Quality Gate Integration" section mapping evaluation outputs to S-014 dimensions. The MCP runbook has no equivalent section mapping MCP operational compliance to quality dimensions -- an omission that reduces its utility for scoring.

3. **No rule ID system:** Unlike the rules file (EV-xxx, CC-xxx, etc.), the runbook defines operational constraints as prose without assigned rule IDs. For example, the P-022 degraded mode disclosure obligation, the one-retry-before-unavailable rule, and the T3 citation requirements are not assigned IDs. This prevents cross-referencing from the GOVERNANCE ID INDEX or from the self-review checklist.

**Improvement Path:**
Add a Self-Review Checklist section (S-010). Add a Quality Gate Integration section mapping MCP compliance to S-014 dimensions. Assign rule IDs to key operational constraints (e.g., MR-001 for the degraded mode disclosure trigger, MR-002 for the one-retry rule).

---

### Internal Consistency (0.93/1.00)

**Evidence:**
The Context7 per-step trigger table (lines 65-73) correctly maps to the 7-step evaluation workflow in `inclusive-design-rules.md` [Workflow Phase Sequencing Rules]. Steps 1, 6, and 7 are correctly identified as not requiring Context7 queries. Figma is classified as REQ in line 99, consistent with the parent `mcp-coordination.md` reference. Storybook is classified as ENH at line 173, and the no-disclosure-banner rule for ENH is correctly stated at line 186. The T3 tier breakdown at lines 239-242 is consistent with `agent-development-standards.md` v1.2.0 [Tool Security Tiers] -- T3 = T2 + WebSearch, WebFetch, Context7.

**Gaps:**
Lines 239-241 note that "The ux-inclusive-evaluator agent excludes Bash from its actual tool set" -- this is correct, but the note says Bash "is not required for accessibility evaluation" yet the T3 tier definition includes Bash in the cumulative model. The note clarifies the distinction between the cumulative tier model and the agent's actual tool set, but an agent reading this without the surrounding context could be confused. This is a clarity issue, not a factual inconsistency.

**Improvement Path:**
Restructure the T3 tier note to lead with "Actual tools per agent definition frontmatter: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Context7 (no Bash)" for clarity.

---

### Methodological Rigor (0.90/1.00)

**Evidence:**
Context7 invocation follows the two-step protocol (resolve-library-id then query-docs) with explicit WebSearch escalation paths per step. The screenshot requirements table (lines 159-166) specifies minimum requirements per input type with resolution targets (375px, 768px, 1440px for responsive evaluation). MCP failure handling covers four distinct scenarios with step-by-step actions and explicit non-blocking declarations. The T3 citation requirements section (lines 251-259) distinguishes between Context7-sourced, WebSearch-sourced, and knowledge-based references.

**Gaps:**
The runbook specifies "One retry attempted before declaring unavailable" (line 201) but does not define the retry timeout (how long to wait before the second attempt). The cited `mcp-coordination.md` detection protocol is the intended reference but the timeout is not repeated here for operational completeness.

**Improvement Path:**
Add the retry timeout value from `mcp-coordination.md` (or a cross-reference note: "retry interval defined in `mcp-coordination.md` [MCP Availability Detection]") to make the runbook self-contained on this point.

---

### Evidence Quality (0.90/1.00)

**Evidence:**
MCP-001 governance obligation is cited at line 24 with full file reference (`.context/rules/mcp-tool-standards.md` v1.3.1). Parent runbook `mcp-coordination.md` is cited as the degraded mode disclosure source. T3 tier constraints are cited with version (agent-development-standards.md v1.2.0). References table (lines 264-276) provides 9 entries with paths for all internal references and brief bibliographic entries for external specifications.

**Gaps:**
The Library ID Resolution Table (lines 82-90) notes "Library IDs are resolved dynamically by Context7" but provides no source for the pre-resolved identifiers in the "Expected Library Name" column. A note clarifying "pre-resolved IDs verified as of {date}" or acknowledging they may drift over time would improve evidence quality for operational confidence.

**Improvement Path:**
Add a note to the Library ID Resolution Table: "Expected names verified against Context7 as of 2026-03-04. Re-verify if resolution fails on first attempt."

---

### Actionability (0.90/1.00)

**Evidence:**
The Context7 "When NOT to Use" table (lines 53-59) provides six concrete exclusion scenarios -- agents have clear guidance on when to skip tool calls. The P-022 degraded mode disclosure banner (lines 131-138) is formatted as a copy-ready code block. Screenshot requirements table gives specific minimum counts per input type. MCP failure handling steps are numbered and explicit. The prohibited tools table (lines 246-249) with rationale per tool is actionable.

**Gaps:**
The per-evaluation-step Context7 timing section (lines 65-73) uses the term "on-demand" without defining what triggers a query within a step. For example, "on-demand at the criterion level" (Step 2) is clear, but Step 5 says "Query for component library accessibility APIs when the input references a specific design system library" -- this condition is vague. When does "referencing" trigger a query vs. when the evaluator can rely on its training knowledge?

**Improvement Path:**
Add a threshold rule: "Query Context7 for component library APIs when the input artifact references a specific named design system (e.g., Material UI, Radix UI) and the evaluation requires verifying that component's accessibility properties. Do not query when the evaluation is generic (no named component library referenced)."

---

### Traceability (0.79/1.00)

**Evidence:**
VERSION header at line 1 includes version, date, source references, parent, governance reference, and project. GOVERNANCE ID INDEX footer at line 279 lists 5 governance items. File footer includes sub-skill, parent skill, parent MCP coordination, MCP governance SSOT, agent, project, and creation date.

**Gaps:**
The GOVERNANCE ID INDEX contains only 5 entries (MCP-001, P-002, P-022, H-34, T3 citation guardrails) -- none of which are runbook-specific rule IDs. The runbook defines numerous operational constraints (degraded mode trigger, retry logic, screenshot requirements, library resolution precedence) but none are assigned IDs that could be cross-referenced. Compare with `inclusive-design-rules.md` which has ~70 rules across 17 families indexed in the GOVERNANCE ID INDEX.

The lack of runbook-native rule IDs means:
- The self-review checklist cannot reference rule IDs (and there is no self-review checklist)
- Other files cannot cite specific runbook rules by ID
- Future revisions cannot be traced to specific rule changes

**Improvement Path:**
Assign operational rule IDs (e.g., MR-001 through MR-010) to the key constraints defined in this runbook. Update the GOVERNANCE ID INDEX to enumerate them.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.82 | 0.92 | Add Self-Review Checklist section with S-010 verification items for MCP operational compliance (e.g., "degraded mode disclosure present if Figma unavailable", "Context7 not used for topics in 'When NOT to Use' list") |
| 2 | Traceability | 0.79 | 0.90 | Assign rule IDs (MR-001 through MR-NNN) to key operational constraints; update GOVERNANCE ID INDEX |
| 3 | Completeness | 0.82 | 0.92 | Add Quality Gate Integration section mapping MCP compliance to S-014 dimensions (e.g., "Evidence Quality: all Context7-sourced data cited with library name and query") |
| 4 | Methodological Rigor | 0.90 | 0.94 | Add retry timeout specification or cross-reference to mcp-coordination.md detection protocol |
| 5 | Actionability | 0.90 | 0.94 | Add threshold rule for Step 5 Context7 invocation trigger (when named component library present vs. generic evaluation) |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score -- specific line numbers cited throughout
- [x] Uncertain scores resolved downward (Traceability 0.79, Completeness 0.82 -- both lower than impression would suggest given good structural coverage)
- [x] First-draft calibration considered (iter1 -- 0.879 reflects a good but structurally incomplete first draft)
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Composite 0.879 does not clear H-13 (0.92) -- REVISE verdict is correct
