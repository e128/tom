# Quality Score Report: MCP Runbook -- Heuristic Evaluation Sub-Skill (Iteration 2)

## L0 Executive Summary

**Score:** 0.922/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.89)
**One-line assessment:** Three of four iter1 fixes landed cleanly (References section, degraded mode banner alignment, Context7 workflow timing), lifting the score from 0.892 to 0.922 -- above the standard H-13 threshold but still below the C4 gate of 0.95; four targeted gaps remain: no NNG Context7 availability caveat, PLAN.md references lack section anchors, no Context7 retry policy note, and no interactive degraded-mode notification guidance.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/rules/mcp-runbook.md`
- **Deliverable Type:** Other (Operational Runbook / Rules File)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Quality Gate:** >= 0.95 weighted composite
- **Standard Quality Gate:** >= 0.92 weighted composite (H-13)
- **Prior Score (Iter 1):** 0.892
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.922 |
| **C4 Threshold** | 0.95 |
| **Standard Threshold (H-13)** | 0.92 |
| **Verdict** | REVISE |
| **Delta from Iter 1** | +0.030 |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.94 | 0.188 | References section added (lines 195-202); nav table updated to 6 entries; all required sections fully covered |
| Internal Consistency | 0.20 | 0.91 | 0.182 | Degraded mode banner now matches SKILL.md exactly (3 bullets); parent mcp-coordination.md Context7 agent table still omits ux-heuristic-evaluator without runbook reconciliation note |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | Context7 5-step workflow mapping added (lines 52-62) with per-step action/no-action directives; retry policy for Context7 timeout still absent |
| Evidence Quality | 0.15 | 0.89 | 0.1335 | References section improves provenance; two gaps persist: PLAN.md references lack section anchors, NNG listed as Context7 source without availability caveat |
| Actionability | 0.15 | 0.92 | 0.138 | Workflow integration timing fully resolved with per-step mapping table; interactive degraded-mode notification timing still unspecified |
| Traceability | 0.10 | 0.94 | 0.094 | Formal References section with repo-relative paths strengthens chain; VERSION header and footer block intact; PLAN.md anchor gap persists |
| **TOTAL** | **1.00** | | **0.922** | |

---

## Iter1 Fix Verification

| Fix | Status | Evidence |
|-----|--------|---------|
| Degraded mode banner aligned with SKILL.md (3 bullets) | CONFIRMED | Lines 124-130: 3 bullets -- "Cannot inspect component states (hover, focus, active, disabled)", "Cannot verify responsive behavior across breakpoints", "Cannot access style tokens or design system variables programmatically" -- match SKILL.md lines 311-313 exactly |
| Context7 invocation timing for 5-step workflow | CONFIRMED | Lines 52-62: "When to Query Context7 in the 5-Step Workflow" subsection added; per-step table with explicit action/no-action directives for all 5 steps, including rationale |
| References section added | CONFIRMED | Lines 195-202: formal `## References` section with Source \| Content \| Path table; 3 entries covering mcp-coordination.md, mcp-tool-standards.md, SKILL.md; nav table entry added at line 16 |
| Address parent mcp-coordination.md Context7 table omission | NOT CONFIRMED | Runbook still asserts ux-heuristic-evaluator uses Context7 (line 22) without a reconciliation note acknowledging the discrepancy with the parent's agent-to-tool mapping table (mcp-coordination.md lines 135-138, which omits ux-heuristic-evaluator) |

---

## Detailed Dimension Analysis

### Completeness (0.94/1.00)

**Evidence:**

All six sections present and fully developed:

1. **Context7 Usage for Heuristic Evaluation** (lines 19-63) -- Now includes the new "When to Query Context7 in the 5-Step Workflow" subsection (lines 52-62), providing complete coverage of when, what, and how to use Context7 during evaluation. The 7-row heuristic trigger table, 4-row "When NOT" table, and the new 5-row workflow timing table together make this section comprehensive.
2. **Figma MCP Dependency** (lines 66-90) -- Status, fallback mode, and capability comparison table. Complete.
3. **Screenshot-Input Mode Protocol** (lines 93-140) -- 4-format table, 7-row extraction table, degraded mode banner, 4-row heuristic-specific limitations table. Complete.
4. **MCP Failure Handling** (lines 143-164) -- 4-condition Context7 failure table and 4-step full-outage procedure. Complete.
5. **Tool Usage Constraints** (lines 167-192) -- Tool tier, prohibited tools, citation requirements. Complete.
6. **References** (lines 195-202) -- Formal structured table with 3 entries. Nav table updated to include this section.

Navigation table (H-23) compliant: 6 entries with anchor links covering all 6 `##` content sections (line 16 added References entry).

**Gaps:**

- The footer traceability block (lines 206-212) and the formal References section (lines 195-202) now coexist. The footer provides agent-identity metadata; the References section provides source traceability. These serve distinct purposes and are not redundant in a way that creates confusion. The footer is standard in peer rule files and the References section adds structured machine-readable provenance. Additive, not a completeness gap.
- No gaps requiring score reduction at C4 below 0.94.

**Improvement Path:**

To reach 0.97+: Add section anchors to PLAN.md references in lines 70, 78, and 122 (also improves Evidence Quality and Traceability). Current score is 0.94.

---

### Internal Consistency (0.91/1.00)

**Evidence (Confirmed Consistent):**

- **Degraded mode banner:** Lines 124-130 now contain exactly 3 bullets: (1) "Cannot inspect component states (hover, focus, active, disabled)", (2) "Cannot verify responsive behavior across breakpoints", (3) "Cannot access style tokens or design system variables programmatically." This matches SKILL.md lines 311-313 exactly. The iter1 wording divergence is fully resolved.
- **Figma REQ classification:** Line 70 states Figma classified as REQ in mcp-coordination.md. Confirmed at mcp-coordination.md line 30. Consistent.
- **Context7 canonical tool names:** `mcp__context7__resolve-library-id` and `mcp__context7__query-docs` throughout runbook. Match mcp-tool-standards.md [Canonical Tool Names] exactly. Consistent.
- **T3 tier composition:** Lines 171-175 define T1+T2+T3 tools. Matches agent-development-standards.md [Tool Security Tiers]. Consistent.
- **Memory-Keeper prohibition:** Line 182 rationale cites P-002. Consistent with mcp-coordination.md scope note. Consistent.
- **5-step workflow references:** New subsection (lines 52-62) references "Step 1 (Input Collection)", "Step 2 (Systematic Evaluation)", "Step 3 (Severity Rating)", "Step 4 (Deduplication and Ranking)", "Step 5 (Report Generation / Self-Review)" -- these names match SKILL.md [Evaluation Workflow] table exactly. Internally consistent.

**Gaps (Inconsistency Persisting):**

- **Parent mcp-coordination.md Context7 Usage table omission (UNRESOLVED):** The runbook asserts at line 22: "The `ux-heuristic-evaluator` agent is T3 (External) and has `mcp__context7__resolve-library-id` and `mcp__context7__query-docs` in its allowed tools." This assertion is accurate per SKILL.md frontmatter line 16. However, mcp-coordination.md lines 135-138 list Context7 Resolve as used by "ux-atomic-architect, ux-ai-design-guide" and Context7 Query as used by "ux-atomic-architect, ux-inclusive-evaluator, ux-ai-design-guide" -- `ux-heuristic-evaluator` is absent from both rows. The runbook does not add a reconciliation note acknowledging this discrepancy and pointing to SKILL.md as the authority. An agent reading both files will find an unexplained gap between the runbook's assertion and the parent's agent-to-tool mapping table. This is a genuine cross-document consistency defect.

**Improvement Path:**

Add a one-sentence reconciliation note to the Context7 Usage section (after line 22): "Note: the `ux-heuristic-evaluator` agent is not yet reflected in the parent mcp-coordination.md [Context7 Usage] agent columns; the authoritative tool declaration is `skills/ux-heuristic-eval/SKILL.md` frontmatter `allowed-tools` field." This one sentence would raise Internal Consistency to 0.95+.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**

- **Context7 workflow integration (FIXED):** Lines 52-62 provide a complete per-step Context7 mapping:
  - Step 1: Query for domain-specific accessibility guidelines (with rationale: ensures scope before systematic evaluation)
  - Step 2: On-demand query per heuristic while evaluating (rationale: minimizes unnecessary calls, respects per-question limit)
  - Step 3: No Context7 needed (rationale: internal classification using Nielsen's 0-4 scale from built-in knowledge)
  - Step 4: No Context7 needed (rationale: operates on own findings, no external reference required)
  - Step 5: Query for calibration benchmarks if uncertain (rationale: resolves borderline severity ratings)
  The "No Context7 needed" explicit declarations for Steps 3 and 4 are methodologically superior -- they prevent unnecessary tool calls by stating non-requirement explicitly, not just omitting the step from a positive list.
- **Protocol accuracy:** Lines 26-29 implement the exact 4-step Context7 protocol from mcp-tool-standards.md. Correct.
- **Heuristic-to-Context7 trigger table:** 7-row mapping with concrete resolve/query syntax. Methodologically sound.
- **Screenshot extraction methodology:** 7-row extraction table with specific observation criteria per heuristic. Operationally rigorous.
- **Failure handling:** 4-condition table covers all cases from mcp-tool-standards.md [Error Handling].

**Gaps:**

- **Context7 retry policy absent (UNRESOLVED):** The failure table row at line 154 reads "Context7 MCP server timeout or error" with fallback "Continue evaluation without Context7. Use WebSearch for all external documentation lookups." The parent mcp-coordination.md [MCP Availability Detection] specifies: "One retry is attempted after a timeout before declaring the MCP unavailable." The runbook does not carry forward this retry policy to individual Context7 tool calls (as distinct from the initial availability probe). The methodological question -- should the agent retry a timed-out Context7 call once before falling back to WebSearch, or immediately fall back? -- is left unanswered. This is a narrow but genuine procedural gap.

**Improvement Path:**

Add a retry note to line 154: append "(One retry attempted before declaring unavailable, per mcp-coordination.md [MCP Availability Detection] detection protocol.)" to the MCP server timeout row. One-line fix. This would raise Methodological Rigor to 0.96.

---

### Evidence Quality (0.89/1.00)

**Evidence:**

- **References section (NEW, FIXED):** Lines 195-202 provide a formal structured table with Source | Content | Path columns. Three entries with repo-relative paths: mcp-coordination.md, mcp-tool-standards.md, SKILL.md. Adds provenance traceability beyond the footer block.
- **MCP-001 citations:** Lines 22, 147, 186 cite MCP-001 with file path and section anchor. Accurate.
- **Canonical tool names:** All Context7 tool references use exact canonical names from mcp-tool-standards.md [Canonical Tool Names].
- **mcp-coordination.md cross-references with anchors:** Lines 78, 122, 158 cite specific sections with anchor links [MCP Availability Detection], [Degraded Mode Disclosure]. Valid.
- **agent-development-standards.md citations:** Lines 171, 186 include section anchors [Tool Security Tiers] and [Tier Constraints]. Valid.
- **P-002, P-022 references:** Constitutional principle numbers cited correctly.
- **5-step workflow references in new subsection:** Step names in lines 58-62 match SKILL.md [Evaluation Workflow] exactly (verified against SKILL.md lines 257-262).

**Gaps (Both Unresolved from Iter1):**

1. **PLAN.md references without section anchors (UNRESOLVED):** Three occurrences: line 70 ("see `projects/PROJ-022-user-experience-skill/PLAN.md`"), line 78 ("see `projects/PROJ-022-user-experience-skill/PLAN.md`"), line 122 ("see `projects/PROJ-022-user-experience-skill/PLAN.md`"). No section anchor in any. For a C4 document, scope-deferral claims should point to verifiable sections in the referenced document. The PLAN.md is a substantive planning document where specific sections address MCP adapter scope; generic references without anchors reduce evidence precision.

2. **Nielsen Norman Group as Context7 source without availability caveat (UNRESOLVED):** Line 40 in the trigger table reads: `| AI-supplement heuristics | Referencing AI interaction design patterns | \`resolve: "Nielsen Norman Group"\` then \`query: "AI transparency and explainability UX guidelines"\` |`. Context7 is a developer-focused documentation tool that indexes software libraries, SDKs, and frameworks. The Nielsen Norman Group is a UX research organization whose content (articles, reports, guidelines) is not a software library and is unlikely to be indexed by Context7's library resolver. Presenting NNG as a Context7 source without acknowledging this uncertainty is an evidence quality issue. An agent following this guidance would attempt `resolve: "Nielsen Norman Group"` and likely receive no match, then fall back to WebSearch -- which is the correct path but is not communicated in the runbook's trigger table row.

**Improvement Path:**

1. Add section anchors to PLAN.md references: at minimum "see `PLAN.md` (MCP adapter implementation deferred to post-PROJ-022 scope, per project plan)." If no exact section heading maps to these claims, a descriptive parenthetical is acceptable for C4 evidence standards.
2. Add a parenthetical to the NNG trigger table row: "(Context7 resolve availability unverified for NNG; WebSearch fallback per MCP-001 likely applies.)"

---

### Actionability (0.92/1.00)

**Evidence:**

- **Context7 invocation timing (FIXED):** Lines 52-62 provide per-step directives. The explicit "No Context7 needed" for Steps 3 and 4 with rationale makes the agent's decision tree for every workflow step unambiguous. An agent executing the 5-step evaluation workflow can consult this table at each step and receive a clear action or non-action directive. This resolves the primary actionability gap from iter1.
- **Per-heuristic trigger table:** Lines 33-41 map specific heuristics to specific Context7 examples. Directly executable.
- **Input format suitability table:** Lines 99-103 enable immediate classification of received input.
- **Extraction targets table:** Lines 110-118 provide systematic screenshot inspection guidance.
- **Failure handling table:** Lines 148-154 give single-action responses to each failure condition.
- **Citation requirements protocol:** Lines 188-191 distinguish citation requirements by source type.

**Gaps:**

- **Interactive degraded-mode notification timing (UNRESOLVED):** Lines 122-130 specify that the degraded mode banner appears "at the top of the evaluation report." This is clear for the output artifact. However, the runbook provides no guidance on whether the agent should notify the user interactively at the start of evaluation execution -- before screenshots are analyzed and before the report is produced. In a multi-turn evaluation session, the user may submit screenshots expecting full Figma capability; finding out about degraded mode only in the final report is a poor user experience and potentially a P-022 compliance concern (delayed disclosure of capability limitation). The iter1 recommendation to "notify the user of degraded mode status at the start of evaluation (before producing findings)" remains unaddressed.

**Improvement Path:**

Add a one-sentence directive to the Limitations of Screenshot-Based Evaluation section (after line 130): "Notify the user of screenshot-input mode status at evaluation start (before analyzing input), not only in the output report." This follows the degraded mode banner requirement in mcp-coordination.md [Degraded Mode Behavior] enforcement rules (rule 1: "the orchestrator MUST inform the user per P-022") and applies the same principle to the agent level.

---

### Traceability (0.94/1.00)

**Evidence:**

- **VERSION header (line 1):** `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/rules/mcp-coordination.md, skills/ux-heuristic-eval/SKILL.md | PARENT: /ux-heuristic-eval sub-skill | GOVERNANCE: .context/rules/mcp-tool-standards.md (MCP-001) | PROJECT: projects/PROJ-022-user-experience-skill/PLAN.md -->` -- full provenance metadata.
- **Navigation table (lines 7-16):** 6 entries with anchor links. All `##` sections covered including the new References section. H-23 compliant.
- **Footer block (lines 206-212):** Sub-skill, parent skill, MCP coordination file, governance SSOT, agent identity, project -- complete traceability chain.
- **References section (lines 195-202):** Formal structured table with 3 entries linking to the three governing source documents with repo-relative paths. This is the primary iter1 traceability improvement.
- **MCP-001 citations with section anchors:** Lines 22, 147, 186. Fully traceable.
- **Cross-document citations with section anchors:** mcp-coordination.md [MCP Availability Detection] (line 158), [Degraded Mode Disclosure] (line 122). Valid.
- **5-step workflow references:** The new subsection's step names are named consistently with SKILL.md [Evaluation Workflow], enabling readers to locate the referenced workflow steps.

**Gaps:**

- **PLAN.md references without section anchors (UNRESOLVED):** Three occurrences (lines 70, 78, 122). For scope-deferral claims, the reader cannot locate the specific PLAN.md section that authorizes the deferral. This is the only remaining traceability gap.

**Improvement Path:**

Add section anchors or descriptive qualifiers to the three PLAN.md references. Example acceptable format: "`projects/PROJ-022-user-experience-skill/PLAN.md` (MCP Adapter Architecture section)" or "`PLAN.md [MCP Adapter Timeline]`" if that section heading exists. If no specific section heading maps to the claim, a parenthetical descriptor is sufficient for traceability at C4 standards.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.91 | 0.95 | Add one-sentence reconciliation note after line 22: "Note: `ux-heuristic-evaluator` is not yet listed in the parent mcp-coordination.md Context7 agent columns; the authoritative tool declaration is `skills/ux-heuristic-eval/SKILL.md` frontmatter `allowed-tools` field." Resolves the cross-document agent-to-tool mapping discrepancy. |
| 2 | Evidence Quality | 0.89 | 0.93 | Add availability caveat to the Nielsen Norman Group row in the trigger table (line 40): "(Context7 resolve availability unverified for NNG; WebSearch fallback per MCP-001 likely applies.)" -- one parenthetical. |
| 3 | Evidence Quality | 0.89 | 0.93 | Add section anchors or descriptive qualifiers to the three PLAN.md references (lines 70, 78, 122): replace generic `PLAN.md` references with `PLAN.md [MCP Adapter Architecture]` or equivalent section pointer. |
| 4 | Methodological Rigor | 0.93 | 0.96 | Add retry note to the Context7 timeout failure row (line 154): append "(One retry attempted before declaring unavailable, per mcp-coordination.md [MCP Availability Detection].)" |
| 5 | Actionability | 0.92 | 0.95 | Add interactive notification directive to Screenshot-Input Mode Protocol: "Notify the user of screenshot-input mode status at evaluation start (before analyzing input), not only in the output report." Insert after line 130, before the heuristic-specific limitations table. |

---

## Gap Summary: Resolved vs. Remaining

| Gap | Iter1 Recommendation | Iter2 Status |
|-----|---------------------|-------------|
| Degraded mode banner wording divergence | Align banner with SKILL.md or declare authority | RESOLVED -- banner now matches SKILL.md exactly |
| Context7 workflow integration timing | Add invocation timing guidance for 5-step workflow | RESOLVED -- "When to Query Context7 in the 5-Step Workflow" subsection added |
| Formal References section | Add `## References` with structured table | RESOLVED -- References section at lines 195-202 |
| Parent mcp-coordination.md omits ux-heuristic-evaluator | Update parent OR add discrepancy note in runbook | UNRESOLVED -- no reconciliation note added |
| NNG as Context7 source without caveat | Add parenthetical noting resolve uncertainty | UNRESOLVED |
| PLAN.md references without section anchors | Add anchors or descriptive qualifiers | UNRESOLVED |
| Context7 retry policy absent | Add retry note to timeout failure condition | UNRESOLVED |
| Interactive degraded-mode notification | Add early user notification directive | UNRESOLVED |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computed
- [x] Evidence documented for each score with specific line number references
- [x] Uncertain scores resolved downward: Internal Consistency scored 0.91 not 0.93 because the parent table discrepancy remains unreconciled; Evidence Quality scored 0.89 not 0.91 because two distinct evidence gaps remain unaddressed
- [x] Calibration applied: 0.922 for an operational rules file at iteration 2 with 3 of 4 major fixes applied is consistent with the 0.85-0.90 "good work" band -- this document is at the upper end having resolved most primary gaps
- [x] No dimension scored above 0.95: highest is 0.94 (Completeness, Traceability) -- both justified by specific evidence
- [x] C4 threshold (0.95) applied: 0.922 clears the standard H-13 threshold (0.92) but does not meet the C4 gate -- REVISE verdict is correct
- [x] Score not inflated to approach PASS: the 4 unresolved gaps are real, specific, and documented; each requires a targeted one-sentence to one-paragraph fix
- [x] Delta from iter1 (+0.030) is proportionate to the scope of fixes applied (3 of 4 primary recommendations addressed)

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.922
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.89
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add reconciliation note for parent mcp-coordination.md Context7 agent table omission of ux-heuristic-evaluator (one sentence, Internal Consistency priority 1)"
  - "Add NNG Context7 availability caveat to trigger table row (line 40, one parenthetical)"
  - "Add section anchors to PLAN.md references (lines 70, 78, 122)"
  - "Add Context7 retry policy note to timeout failure condition (line 154, one clause)"
  - "Add interactive degraded-mode notification directive to Screenshot-Input Mode Protocol (one sentence after line 130)"
```

---

*Score Report: mcp-runbook-iter2-score.md*
*Scoring Agent: adv-scorer*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-heuristic-eval/rules/mcp-runbook.md`*
*Criticality: C4*
*Prior Score: 0.892 (iter1)*
*Current Score: 0.922 (iter2)*
*Verdict: REVISE*
*Created: 2026-03-04*
