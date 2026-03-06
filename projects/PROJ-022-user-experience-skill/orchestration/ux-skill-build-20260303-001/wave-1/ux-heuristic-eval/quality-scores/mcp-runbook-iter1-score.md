# Quality Score Report: MCP Runbook -- Heuristic Evaluation Sub-Skill

## L0 Executive Summary

**Score:** 0.892/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.87)
**One-line assessment:** The runbook is structurally complete and methodologically sound but falls short of the C4 threshold (0.95) due to four targeted gaps: a minor wording inconsistency in the degraded mode banner versus SKILL.md, the parent mcp-coordination.md Context7 table omitting ux-heuristic-evaluator from agent columns, a missing workflow-integration point specifying when to invoke Context7 within the 5-step evaluation workflow, and PLAN.md citations lacking section anchors.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/rules/mcp-runbook.md`
- **Deliverable Type:** Other (Operational Runbook / Rules File)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Quality Gate:** >= 0.95 weighted composite
- **Standard Quality Gate:** >= 0.92 weighted composite (H-13)
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.892 |
| **C4 Threshold** | 0.95 |
| **Standard Threshold (H-13)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 5 required sections present with depth; nav table H-23 compliant; no `## References` section (footer only) |
| Internal Consistency | 0.20 | 0.88 | 0.176 | Consistent with parent files overall; minor banner wording divergence vs. SKILL.md; parent mcp-coordination.md Context7 agent columns omit ux-heuristic-evaluator |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | 4-step Context7 protocol exactly matches mcp-tool-standards.md; 4-condition failure table; screenshot mode extraction table well-structured |
| Evidence Quality | 0.15 | 0.87 | 0.1305 | All canonical tool names accurate; MCP-001 cited correctly; PLAN.md reference lacks section anchor |
| Actionability | 0.15 | 0.88 | 0.132 | Per-heuristic Context7 trigger table is directly executable; workflow-integration timing gap (when to invoke Context7 within 5-step evaluation) |
| Traceability | 0.10 | 0.93 | 0.093 | VERSION header, footer block, nav table all present; standards cited with anchors throughout |
| **TOTAL** | **1.00** | | **0.892** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**

All five required sections are present:

1. **Context7 Usage for Heuristic Evaluation** (lines 19-50) -- Present. Includes the 4-step protocol, a 7-row heuristic-to-Context7 trigger table with concrete resolve/query examples, and a 4-row "When NOT to Use" table. Comprehensive.
2. **Figma MCP Dependency** (lines 53-77) -- Present. Covers current status (UNAVAILABLE), fallback mode reference, and a 6-row capability comparison table (screenshot-input vs. Figma MCP). Includes forward-looking note about agent definition updates when Figma becomes available.
3. **Screenshot-Input Mode Protocol** (lines 80-127) -- Present. 4-format input suitability table, 7-row extraction-target-to-heuristic mapping, degraded mode banner template, and 4-row heuristic-specific limitations table with confidence impact classification.
4. **MCP Failure Handling** (lines 130-151) -- Present. 4-condition Context7 failure table and a numbered 4-step full-MCP-outage procedure.
5. **Tool Usage Constraints** (lines 154-179) -- Present. Tool tier definition, prohibited tools table with per-tool rationale, and a 4-condition citation requirements protocol.

Navigation table (H-23) present with 5 entries using anchor links. All `##` sections covered.

**Gaps:**

- No formal `## References` section. The document ends with a footer block (lines 182-189) rather than a structured references section. This is a minor gap -- the footer provides traceability but does not follow the `## References` table pattern used in peer rule files (e.g., mcp-coordination.md uses a References-equivalent footer block, so this is consistent with peer files, but a formal section would strengthen completeness for C4).
- The nav table has 5 entries covering all 5 `##` content sections. The footer traceability block is not listed as a navigable section. Minor.

**Improvement Path:**

Add a `## References` section with a structured table (Source | Content | Path) referencing mcp-tool-standards.md, mcp-coordination.md, SKILL.md, and agent-development-standards.md with repo-relative paths. This would bring completeness to 0.95+.

---

### Internal Consistency (0.88/1.00)

**Evidence:**

Consistent with parent files on all major structural elements:

- **Figma REQ classification:** Runbook line 57 states `/ux-heuristic-eval` has Figma classified as REQ. Confirmed in mcp-coordination.md [MCP Dependency Matrix] line 30: `| /ux-heuristic-eval | REQ | -- | ENH | -- | -- | -- |`. Consistent.
- **Context7 canonical tool names:** Runbook uses `mcp__context7__resolve-library-id` and `mcp__context7__query-docs` (lines 25-26, 162). Matches mcp-tool-standards.md [Canonical Tool Names] exactly. Consistent.
- **T3 tier composition:** Runbook lines 160-162 define T1/T2/T3 components. Matches agent-development-standards.md [Tool Security Tiers] table (T3 = T2 + WebSearch, WebFetch, Context7). Consistent.
- **Degraded mode disclosure requirement:** Runbook line 109 cites P-022 and references mcp-coordination.md [Degraded Mode Disclosure]. Consistent with parent mcp-coordination.md lines 95-102. Consistent.
- **Memory-Keeper prohibition:** Runbook line 169 prohibits Memory-Keeper with rationale "Sub-skill state is engagement-scoped per P-002." Consistent with mcp-coordination.md lines 26-27 scope note: "No sub-skill agent requires Memory-Keeper; all sub-skill state is engagement-scoped per P-002." Consistent.
- **MCP failure fallback:** Runbook lines 138-141 match the 4-condition table in mcp-tool-standards.md [Error Handling] point-for-point. Consistent.

**Gaps (Inconsistencies Found):**

1. **Degraded mode banner wording divergence:** Runbook banner (lines 112-117) reads:
   ```
   [DEGRADED MODE] This evaluation was produced without Figma MCP access.
   Input was provided via screenshot-input mode. Some features are reduced:
   - Cannot inspect component states (hover, focus, active, disabled)
   - Cannot verify responsive behavior across breakpoints
   - Cannot access style tokens or design system variables programmatically
   ```
   SKILL.md banner (lines 308-313) reads:
   ```
   [DEGRADED MODE] This evaluation was produced without Figma MCP access.
   Input was provided via screenshot-input mode. Some features are reduced:
   - Cannot inspect component states or interactive behaviors
   - Cannot verify responsive behavior across breakpoints
   ```
   The runbook has 3 bullets; SKILL.md has 2 bullets with slightly different wording on bullet 1 ("or interactive behaviors" vs. "(hover, focus, active, disabled)"). The runbook's version is more specific and technically superior, but the divergence creates a discoverability issue: which version should the agent use? The authoritative version should be declared.

2. **Parent mcp-coordination.md Context7 Usage table omits ux-heuristic-evaluator:** mcp-coordination.md lines 135-138 list Context7 Resolve as used by "ux-atomic-architect, ux-ai-design-guide" and Context7 Query as used by "ux-atomic-architect, ux-inclusive-evaluator, ux-ai-design-guide" -- but does NOT include `ux-heuristic-evaluator`. The runbook correctly asserts that ux-heuristic-evaluator uses Context7 (consistent with SKILL.md tool tier T3 and the heuristic-evaluator's declared allowed tools in SKILL.md frontmatter line 16). This is a deficiency in the parent file rather than the runbook, but it means the runbook's assertion is unsupported by the parent's agent-to-tool mapping table. An agent reading the parent file would not find ux-heuristic-evaluator listed as a Context7 user. The runbook should note this discrepancy explicitly, or the parent file should be corrected.

**Improvement Path:**

1. Align degraded mode banner wording with SKILL.md (or explicitly declare that the runbook's version is authoritative for this sub-skill and update SKILL.md to match). A cross-reference note would resolve this.
2. Either update mcp-coordination.md to add ux-heuristic-evaluator to the Context7 Usage table, or add a note in the runbook acknowledging the discrepancy with a pointer to the SKILL.md tool declaration as the authority.

---

### Methodological Rigor (0.90/1.00)

**Evidence:**

- **Context7 protocol accuracy:** Lines 25-28 implement the exact 4-step protocol from mcp-tool-standards.md [Context7 Integration]: (1) resolve-library-id call, (2) query-docs call with resolved ID, (3) respect per-question call limit, (4) WebSearch fallback if no match. Correctly operationalized.
- **Heuristic-to-Context7 mapping:** The 7-row trigger table (lines 32-41) maps specific Nielsen heuristics to specific Context7 library examples with concrete resolve/query call examples. This is methodologically sound -- it prevents arbitrary Context7 usage by anchoring each tool invocation to a specific evaluation need.
- **Screenshot mode extraction methodology:** The 7-row extraction table (lines 97-106) maps extraction targets to specific heuristics with concrete observation criteria. This operationalizes the screenshot evaluation workflow at a level that prevents evaluators from applying heuristics superficially.
- **Failure handling rigor:** The failure table (lines 137-141) covers all 4 failure conditions from mcp-tool-standards.md [Error Handling] and adds a runbook-specific disclosure note ("Note 'Context7 no coverage' in the evaluation output next to the affected finding") that strengthens operational guidance beyond the parent.
- **Heuristic-specific limitation classification:** Lines 122-127 classify limitations by heuristic with confidence impact ratings (LOW confidence, "note as inferred"). This provides methodologically sound disclosure guidance rather than generic warnings.
- **Prohibited tools rationale:** Each prohibition in lines 167-169 is accompanied by a specific rationale tied to a governing principle (P-003 for Task, P-002 for Memory-Keeper). Methodologically rigorous.

**Gaps:**

- **No workflow integration point for Context7:** The runbook does not specify at what step within the 5-step evaluation workflow (defined in SKILL.md [Evaluation Workflow]) the agent should invoke Context7. Should the agent probe Context7 upfront for all potentially-referenced libraries (front-loaded), or invoke on-demand as each heuristic is evaluated (lazy)? For a C4 runbook, this ambiguity is a methodological gap. An agent following the runbook strictly cannot determine the invocation timing without consulting the SKILL.md separately.
- **No retry policy for Context7 timeouts:** The failure table (line 141) covers "MCP server timeout or error" with "Continue evaluation without Context7. Use WebSearch." But the parent mcp-coordination.md [MCP Availability Detection] specifies a "1 retry after timeout" policy for MCP probes. The runbook does not specify whether Context7 tool calls themselves should be retried (as distinct from the initial availability probe). This is a minor procedural gap.

**Improvement Path:**

1. Add an "Invocation Timing" subsection under Context7 Usage specifying when during the evaluation workflow to invoke Context7 (recommended: on-demand per heuristic, not front-loaded).
2. Add a retry note to the timeout failure condition in the Context7 failure table: "One retry before declaring unavailable per mcp-coordination.md [MCP Availability Detection]."

---

### Evidence Quality (0.87/1.00)

**Evidence:**

- **MCP-001 citation (line 21):** "Per MCP-001 (`.context/rules/mcp-tool-standards.md` [Context7 Integration]):" -- correct principle identifier, correct file path, correct section anchor. Fully traceable.
- **Canonical tool names:** `mcp__context7__resolve-library-id` and `mcp__context7__query-docs` match mcp-tool-standards.md [Canonical Tool Names] exactly. No incorrect tool identifiers found.
- **mcp-tool-standards.md Error Handling citation (line 134):** "Per `mcp-tool-standards.md` [Error Handling]:" -- section anchor present. Traceable.
- **mcp-coordination.md citations:** Lines 65 and 145 cite specific sections ([MCP Availability Detection] and [Degraded Mode Disclosure]) with anchor links. Valid and resolvable.
- **agent-development-standards.md citations (lines 158, 173):** Section anchors [Tool Security Tiers] and [Tier Constraints] present. Valid.
- **P-022 citations (lines 109, 149):** Constitutional principle references. Accurate.
- **VERSION header (line 1):** SOURCE field lists mcp-coordination.md and SKILL.md. GOVERNANCE field cites mcp-tool-standards.md (MCP-001). Full metadata provenance.
- **Nielsen Norman Group examples in trigger table (lines 39-40):** Accurate UX framework examples for Context7 usage.

**Gaps:**

- **PLAN.md reference without section anchor (lines 57, 77, 76):** "see `projects/PROJ-022-user-experience-skill/PLAN.md`" appears without a section anchor. The PLAN.md is a large document; linking without a section makes the reference harder to verify. Compare with mcp-coordination.md which uses `(see \`projects/PROJ-022-user-experience-skill/PLAN.md\`)` consistently at the same level of specificity -- so this is consistent with the parent file pattern, but still a weakness for C4 evidence quality.
- **Nielsen NNG as Context7 source:** Line 39-40 uses `resolve: "Nielsen Norman Group"` as a Context7 example. Context7 is primarily a developer-focused library documentation tool. Whether Nielsen Norman Group articles are resolvable via Context7's library resolution mechanism is unverified in the runbook. If NNG is not available on Context7, the fallback to WebSearch would apply, but the runbook presents NNG as a Context7 source without acknowledging this uncertainty. Minor evidence quality concern.

**Improvement Path:**

1. Add section anchors to PLAN.md references where possible (e.g., `PLAN.md [Wave 1 Scope]` or `PLAN.md [MCP Adapter Implementation Timeline]`).
2. Add a parenthetical note to the NNG Context7 example: "resolve availability unverified; WebSearch fallback applies per MCP-001 if resolve returns no match."

---

### Actionability (0.88/1.00)

**Evidence:**

- **Per-heuristic Context7 trigger table (lines 32-41):** Each row maps a specific heuristic evaluation step to a specific Context7 library example with concrete resolve/query syntax. An agent executing a heuristic evaluation can use this table as a direct lookup guide during evaluation. Highly actionable.
- **"When NOT to Use Context7" table (lines 43-50):** 4 scenarios with specific alternatives. Prevents unnecessary Context7 calls. Directly actionable.
- **Supported input formats table (lines 86-92):** 4 formats with suitability ratings and operational notes. An agent receiving input can immediately classify the input type and apply the appropriate evaluation approach. Actionable.
- **Extraction targets table (lines 97-106):** 7 extraction targets with specific observation criteria. An agent examining a screenshot can use this table as a systematic checklist. Actionable.
- **Screenshot limitations table (lines 121-127):** Per-heuristic confidence classification. An agent can annotate findings with confidence levels during evaluation. Actionable.
- **Failure handling table (lines 137-141):** Each failure condition maps to a single specific fallback action. No ambiguity in the failure response paths. Actionable.
- **Citation requirements protocol (lines 175-179):** 4-condition protocol distinguishing citation requirements by source type. An agent generating findings can select the correct citation format for each finding. Actionable.
- **Prohibited tools table (lines 166-169):** Clear prohibition with rationale. An agent sees immediately that Task and Memory-Keeper are off-limits. Actionable.

**Gaps:**

- **Missing workflow integration timing:** The Context7 trigger table specifies WHICH libraries to resolve for WHICH heuristics but does not specify WHEN within the evaluation workflow to make those calls. The SKILL.md defines a 5-step evaluation workflow (Input Collection, Systematic Evaluation, Severity Rating, Deduplication, Report Generation). An agent following this workflow needs to know whether Context7 calls belong in Step 2 (Systematic Evaluation, as each heuristic is evaluated) or as a preparation step before Step 2 begins. Without this, an agent must infer the timing, reducing actionability.
- **No explicit trigger for when screenshot mode should be announced to the user:** The limitations table (lines 121-127) says findings should be annotated as "LOW confidence; note as inferred," but the runbook does not specify at what point the agent should communicate the degraded mode status to the user. Line 109 references the degraded mode banner "at the top of the evaluation report," which is clear for the output artifact, but there is no guidance on whether to notify the user interactively during evaluation execution (before producing the report). Moderate gap.

**Improvement Path:**

1. Add an "Invocation Timing" note to the Context7 Usage section: "Invoke Context7 on-demand during Step 2 (Systematic Evaluation) as each heuristic is evaluated, not as a front-loaded preparation step. This minimizes unnecessary tool calls and respects the per-question call limit."
2. Add a note under Screenshot-Input Mode Protocol: "Notify the user of degraded mode status at the start of evaluation (before producing findings), not only in the output report."

---

### Traceability (0.93/1.00)

**Evidence:**

- **VERSION header (line 1):** `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/rules/mcp-coordination.md, skills/ux-heuristic-eval/SKILL.md | PARENT: /ux-heuristic-eval sub-skill | GOVERNANCE: .context/rules/mcp-tool-standards.md (MCP-001) | PROJECT: projects/PROJ-022-user-experience-skill/PLAN.md -->` -- full provenance metadata in the standard format.
- **Navigation table (lines 7-15):** 5 entries with anchor links covering all 5 `##` content sections. H-23 compliant.
- **Footer block (lines 182-189):** Sub-skill, parent skill, parent MCP coordination file, governance SSOT, agent identifier, project -- complete traceability chain in the standard footer format.
- **MCP-001 citations (lines 21, 134, 142):** Each cites the governing principle with file path and section anchor. Fully traceable.
- **mcp-coordination.md cross-references (lines 65, 109, 145):** Each cites the specific section with anchor links [MCP Availability Detection], [Degraded Mode Disclosure]. Traceable.
- **agent-development-standards.md citations (lines 158, 173):** Section anchors present. Traceable.
- **P-002, P-022 references:** Constitutional principle numbers cited directly.

**Gaps:**

- **PLAN.md references without section anchors (lines 57, 77):** "see `projects/PROJ-022-user-experience-skill/PLAN.md`" -- no section anchor. Reduces traceability precision for the scope-deferral claims.
- **No anchor in the nav table entry for Tool Usage Constraints:** Nav table entry reads "Tool Usage Constraints" with anchor `#tool-usage-constraints`. The section heading (line 154) is `## Tool Usage Constraints`. Anchor resolves correctly. No issue -- included for completeness of check.

**Improvement Path:**

Add section anchors to PLAN.md references. Example: `PLAN.md [MCP Adapter Scope]` would be acceptable if the PLAN.md contains such a section heading; otherwise a note like "see PLAN.md -- post-PROJ-022 scope deferred items" is sufficient for context without pretending an anchor exists.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.88 | 0.93 | Resolve degraded mode banner wording divergence with SKILL.md: either declare the runbook version authoritative (add a cross-reference note) and update SKILL.md to match, OR align the runbook banner to SKILL.md wording exactly. One sentence of clarification resolves this. |
| 2 | Internal Consistency | 0.88 | 0.93 | Address the mcp-coordination.md Context7 Usage table omission of ux-heuristic-evaluator: update the parent file to add ux-heuristic-evaluator to the Context7 Resolve and Context7 Query agent columns, OR add a note in the runbook acknowledging the discrepancy and citing SKILL.md frontmatter line 16 as the authority for allowed tools. |
| 3 | Actionability | 0.88 | 0.93 | Add "Invocation Timing" guidance to Context7 Usage section: specify that Context7 calls are made on-demand during Step 2 (Systematic Evaluation) of the SKILL.md 5-step workflow, not front-loaded. One paragraph addition. |
| 4 | Completeness | 0.90 | 0.95 | Add a formal `## References` section with a structured table referencing mcp-tool-standards.md, mcp-coordination.md, SKILL.md, and agent-development-standards.md with repo-relative paths and section anchors. |
| 5 | Evidence Quality | 0.87 | 0.92 | Add section anchors to PLAN.md references (e.g., `PLAN.md [MCP Adapter Timeline]` or similar) for precision traceability. |
| 6 | Evidence Quality | 0.87 | 0.92 | Add a parenthetical note to the "Nielsen Norman Group" Context7 example in the trigger table acknowledging that NNG articles may not be resolvable via Context7's library index; WebSearch fallback applies per MCP-001 if resolve returns no match. |
| 7 | Methodological Rigor | 0.90 | 0.94 | Add a retry policy note to the Context7 timeout failure condition: "One retry attempted before declaring unavailable (per mcp-coordination.md [MCP Availability Detection] detection protocol)." |
| 8 | Actionability | 0.88 | 0.93 | Add early user notification guidance to Screenshot-Input Mode Protocol: specify that degraded mode status should be communicated to the user at evaluation start (interactively), not only in the output report. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computed
- [x] Evidence documented for each score with specific line number references
- [x] Uncertain scores resolved downward (Internal Consistency scored 0.88 not 0.90 due to two distinct inconsistencies)
- [x] First-draft calibration considered -- v1.0.0 document; 0.892 is appropriate for a strong first-iteration C4 rules file
- [x] No dimension scored above 0.95 without exceptional evidence (Traceability at 0.93 is the highest, justified by comprehensive VERSION header, footer, nav table, and inline citations)
- [x] C4 threshold (0.95) applied -- deliverable at 0.892 falls below both C4 threshold and standard H-13 threshold (0.92); REVISE verdict is correct
- [x] Score not inflated to soften verdict -- 0.892 reflects genuine quality with specific, actionable gaps identified

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.892
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.87
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Resolve degraded mode banner wording divergence with SKILL.md (declare authority or align)"
  - "Address mcp-coordination.md Context7 table omission of ux-heuristic-evaluator (update parent or add discrepancy note)"
  - "Add Context7 invocation timing guidance (on-demand during Step 2 of 5-step workflow)"
  - "Add formal References section with structured table and repo-relative paths"
  - "Add section anchors to PLAN.md references"
  - "Add NNG Context7 availability caveat to trigger table example"
  - "Add Context7 retry policy note to timeout failure condition"
  - "Add early user notification guidance for degraded mode (interactive, not report-only)"
```

---

*Score Report: mcp-runbook-iter1-score.md*
*Scoring Agent: adv-scorer*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-heuristic-eval/rules/mcp-runbook.md`*
*Criticality: C4*
*Verdict: REVISE*
*Created: 2026-03-04*
