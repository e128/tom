# Quality Score Report: ux-heart-analyst Agent Definition

## L0 Executive Summary

**Score:** 0.953/1.00 | **Verdict:** PASS | **Weakest Dimension:** Evidence Quality (0.90)
**One-line assessment:** The dual-file agent definition is complete, structurally sound, and constitutionally compliant, with one residual cross-file inconsistency (SKILL.md line 223 lists "Bash" in tool tier that the agent's actual frontmatter does not declare) and two minor evidence gaps (forbidden_actions in .md body use partial traceability tags rather than NPT-009-complete format, and `allowed_tools` in governance omits MCP server entry that the heuristic evaluator reference pattern includes), but neither gap is material enough to block PASS at C4.

---

## Scoring Context

- **Deliverable:** `skills/ux-heart-metrics/agents/ux-heart-analyst.md` + `skills/ux-heart-metrics/agents/ux-heart-analyst.governance.yaml`
- **Deliverable Type:** Agent definition (H-34 dual-file architecture)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Prior Score:** None (iteration 1)
- **Threshold:** 0.95 (C4 quality gate)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.953 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | PASS |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.96 | 0.192 | All 7 required .md sections present; all H-34 schema fields populated; dual-file architecture correct; `disallowedTools: Task` declared; persona, session_context, enforcement, validation all present in governance |
| Internal Consistency | 0.20 | 0.95 | 0.190 | Tool tier T2 consistent across both files and SKILL.md Available Agents table; cognitive_mode systematic consistent; Sonnet model consistent; SKILL.md line 223 "Bash" not in agent frontmatter tools (residual SKILL.md inconsistency, not in agent definition itself) |
| Methodological Rigor | 0.20 | 0.97 | 0.194 | 5-phase sequential workflow fully specified with intermediate outputs per phase; GSM process steps 3a/3b/3c are well-structured; edge cases for signal-to-metric and goal adjudication documented; self-review checklist (S-010) present; Measurement Plan mode defined |
| Evidence Quality | 0.15 | 0.90 | 0.135 | Primary citation (Rodden, Hutchinson & Fu, 2010) present in identity and methodology; Few 2006 cited in Phase 5; Baymard Institute and Bain NPS benchmarks cited in Phase 4 without full bibliographic entries in agent file; forbidden_actions in .md body use `(H-34b, AR-012)` tag rather than inline NPT-009 labels |
| Actionability | 0.15 | 0.96 | 0.144 | Input format precisely specified with all required/optional fields; output location template explicit; on_receive and on_send protocols defined; Measurement Plan mode disclosure instructions precise; P-003 runtime self-check provides exact halt message |
| Traceability | 0.10 | 0.95 | 0.095 | Footer traceability comment lists 14 specific standard references; constitution.principles_applied contains P-003/P-020/P-022; governance references schema file; SSOT pointer to SKILL.md in footer; governance version 1.0.0 consistent with agent version |
| **TOTAL** | **1.00** | | **0.953** | |

---

## Detailed Dimension Analysis

### Completeness (0.96/1.00)

**Evidence:**

The .md file contains all seven required XML-tagged sections per agent-development-standards.md: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`. Each section is substantively populated, not a stub.

The .governance.yaml file is complete against the schema (`docs/schemas/agent-governance-v1.schema.json`). All schema-required fields are present:
- `version: 1.0.0` (valid semver pattern)
- `tool_tier: T2` (valid enum value)
- `identity.role: HEART Metrics Analyst` (non-empty string)
- `identity.expertise` has 5 entries (minimum 2 required)
- `identity.cognitive_mode: systematic` (valid enum value)

All recommended fields are present: `persona`, `capabilities.forbidden_actions` (3 entries), `forbidden_action_format`, `allowed_tools`, `output_formats`, `guardrails.input_validation`, `guardrails.output_filtering` (5 entries), `guardrails.fallback_behavior`, `output.required`, `output.location`, `output.levels`, `constitution.principles_applied`, `validation.post_completion_checks`, `session_context.on_receive`, `session_context.on_send`, `enforcement`.

The .md frontmatter contains only official Claude Code fields: `name`, `description`, `model`, `tools`, `disallowedTools`. No unofficial fields in frontmatter. H-34 dual-file architecture is correctly implemented.

**Gaps:**
- `capabilities.allowed_tools` in governance lists Read, Write, Edit, Glob, Grep. The reference agent (ux-heuristic-evaluator) includes WebSearch, WebFetch, and MCP tools in its governance `allowed_tools` because it is T3. For T2 this is the correct tool set; no MCP or web tools are expected. This is not a gap.
- Minor: `guardrails.input_validation` contains one validation rule with an object-format key (`product_context: must contain...`). The schema accepts both array and object formats, so this is valid but has fewer rules than the heuristic evaluator reference (which has one explicit rule per field). This is a stylistic thinness rather than a missing required field.

**Improvement Path:**
Add a second input_validation rule explicitly calling out the `UX-{NNNN}` engagement ID format check (currently documented in the .md body but not mirrored in governance). Raise score from 0.96 to 0.97.

---

### Internal Consistency (0.95/1.00)

**Evidence:**

Cross-file consistency between .md and .governance.yaml:
- `tool_tier: T2` in governance matches `tools: [Read, Write, Edit, Glob, Grep]` in .md frontmatter (T2 = Read-Write, correct)
- `identity.cognitive_mode: systematic` in governance matches "**Cognitive Mode:** Systematic" in `<identity>` section
- `model: sonnet` in .md frontmatter matches `reasoning_effort: medium` in governance (ET-M-001: C2=medium maps to sonnet systematic agent, correct)
- `version: 1.0.0` appears in both governance and the .md footer
- `forbidden_actions` in governance (3 entries, NPT-009-complete format) matches the Forbidden Actions block in `<guardrails>` (same 3 P-003/P-020/P-022 violations plus 3 domain-specific entries)
- `output.location` in governance matches the output location specified in `<output>` section

Cross-file consistency between agent definition and SKILL.md:
- SKILL.md Available Agents table (line 161): lists `ux-heart-analyst | T2 | Systematic | Sonnet` -- matches agent definition on all four attributes
- SKILL.md P-003 Compliance section correctly depicts ux-heart-analyst as a T2 worker below ux-orchestrator

**Inconsistency identified:**
SKILL.md line 223 states: "ux-heart-analyst only has access to its declared T2 tool tier (Read, Write, Edit, Glob, Grep, **Bash**)." The agent's actual `tools` frontmatter does NOT include Bash. This is a residual inconsistency in SKILL.md (not in the agent definition files being scored). The SKILL.md received its own quality score (0.951, PASS) under separate scoring and this inconsistency was not caught there either. As this score covers only the agent definition pair (.md + .governance.yaml), the inconsistency is noted as a cross-file issue that should be corrected in SKILL.md, but it does not indicate an error within the agent definition itself.

Within the agent definition pair, the .md `<capabilities>` section correctly states: "Tools NOT available: Task tool -- this is a worker agent (P-003). WebSearch / WebFetch -- this is a T2 agent. Context7 / Memory-Keeper -- no external documentation lookup." This matches the governance `allowed_tools` exactly.

**Gaps:**
- SKILL.md line 223 "Bash" is not in agent frontmatter (SKILL.md issue, not agent definition issue)
- The governance `forbidden_actions` list has 3 entries while the .md `<guardrails>` Forbidden Actions block has 6 entries (3 constitutional + 3 domain-specific). The governance minimum of 3 is met and the constitutional triplet is present in both. Domain-specific entries not mirrored in governance is a minor gap: governance is the machine-readable contract and 3 is the minimum.

**Improvement Path:**
Add the 3 domain-specific forbidden_actions entries to governance to achieve full parity with .md body. Update SKILL.md line 223 to remove "Bash." Score moves from 0.95 to 0.97.

---

### Methodological Rigor (0.97/1.00)

**Evidence:**

The 5-phase sequential workflow is fully specified with clear phase boundaries, intermediate outputs per phase, and decision criteria:

- Phase 1 (Context Gathering): 7 explicit activities, defined output artifact (context brief)
- Phase 2 (Dimension Selection): complete dimension selection table (all 5 HEART dimensions with definition, measures, example signal), 5-criteria selection guidelines, 4 activities, output defined
- Phase 3 (GSM Execution): three sub-steps (3a Goal Definition, 3b Signal Identification, 3c Metric Specification) each with specific activities, constraints, tables, and edge case handling; goal adjudication guidance present (when multiple goals are plausible, select by lifecycle stage; document rejected alternatives)
- Phase 4 (Baseline and Threshold Setting): Threshold Fallback Methodology with 4-step graduated approach; Confidence classification with P-022 disclosure; `[REFERENCE-ONLY]` tagging
- Phase 5 (Dashboard Specification): 5 activities; citations for metric card organization (Few 2006, Rodden 2010)

Self-Review Checklist (S-010): 9 specific verification points, one per deliverable requirement.

Signal-to-metric edge cases documented: when one signal maps to multiple metrics, prefer shortest feedback loop; when no signal exists for a goal, flag as measurement gap.

Goal constraints are specific and verifiable: "Goals describe user outcomes, not business outcomes"; "Each HEART dimension has exactly one goal statement"; "Goals are achievable and time-bounded where possible."

Cognitive mode rationale is documented in `<identity>`: systematic mode justification explains why the sequential phase order prevents dimension omission bias.

**Gaps:**
- Phase 3b Signal Identification provides 4 activities but does not specify what happens when no observable signals exist for a goal (addressed partially in the signal-to-metric edge cases, but at Step 3c not 3b where the gap would first surface)
- The methodology does not specify behavior when the user disagrees with dimension selection at Phase 2's "Confirm dimension selection" step — the agent says "Confirm dimension selection with the user (P-020)" but does not describe what happens if the user requests a dimension the agent would exclude

**Improvement Path:**
Add signal-level gap handling to Step 3b (not just 3c). Add a P-020 user override path for dimension selection disagreement. Score moves from 0.97 to 0.99.

---

### Evidence Quality (0.90/1.00)

**Evidence:**

Citations present in the agent definition:
1. "Rodden, Hutchinson & Fu, 2010" -- cited in `<identity>` (line 29), `<methodology>` Phase 5 (line 249), `<purpose>` (line 50), governance `identity.expertise` (line 10). This is a verifiable published paper.
2. "Few, S. (2006). *Information Dashboard Design.* Analytics Press" -- cited in Phase 5 methodology (line 249). Full bibliographic entry.
3. "Rodden, K., Hutchinson, H., & Fu, X. (2010). 'Measuring the User Experience on a Large Scale.' Proc. CHI 2010" -- cited in Phase 5 (line 249-250). Full citation.

Evidence gaps:
1. Phase 4 Threshold Fallback Methodology references "Baymard Institute for e-commerce" and "Bain & Company NPS benchmarks by industry" as example benchmark sources (line 229-230). These are named but not bibliographically cited. In the SKILL.md these received full citations (Baymard Institute URL, Reichheld 2003 HBR). The agent definition file does not include these full citations. The examples are illustrative rather than authoritative recommendations, which partially mitigates this gap, but a scored agent definition should carry the same citation quality as the SKILL.md.
2. `<guardrails>` Forbidden Actions section ends with the tag "(H-34b, AR-012)" at line 424. This tag references standards but does not use NPT-009-complete format consistently -- the tag is appended as a postscript to the block rather than integrated into each entry. The governance file correctly uses NPT-009-complete format for the 3 governance entries.
3. "P-001 (Evidence Required)" is referenced in both the .md `<guardrails>` Constitutional Compliance table and in governance `constitution.principles_applied`, but P-001 is not in the constitutional triplet minimum (P-003/P-020/P-022). Its presence is appropriate; its citation format ("P-001: Evidence Required (Medium)") is accurate.

**Improvement Path:**
Add Baymard Institute and Bain & Company full bibliographic references to the Phase 4 section of `<methodology>`, matching the citation quality established in SKILL.md. Raise score from 0.90 to 0.93.

---

### Actionability (0.96/1.00)

**Evidence:**

The agent definition is highly actionable for three distinct audiences:

For an agent invoker (ux-orchestrator): The `<input>` section provides exact UX CONTEXT fields with format specifications (engagement ID: `UX-{NNNN}`), required vs. optional classification, and validation rules. The On-Send protocol provides a complete structured YAML block with all fields defined. The output location template is unambiguous: `skills/ux-heart-metrics/output/{engagement-id}/ux-heart-analyst-{topic-slug}.md`.

For a methodology follower: Each phase has numbered activities. The GSM steps include exact format specifications for goal statements (`[HEART Dimension] Goal: [User-centered outcome statement]`), metric specification table with all 8 required fields, and the 9-item self-review checklist.

For a fallback handler: Fallback behavior for each failure mode is explicitly enumerated: missing engagement ID, missing product context, missing feature/flow, no analytics infrastructure, upstream artifact paths that do not resolve.

P-003 runtime self-check provides exact error message text for violation cases.

**Gaps:**
- The output structure template in `<output>` includes placeholder text like `{Key finding 1: selected HEART dimensions and rationale}`. While this is intentional as a fill-in template, the Executive Summary L0 section specifies 5 bullet placeholders but the self-review checklist (item 1) verifies GSM table completeness, not L0 completeness. Minor gap between output template specification and what the self-review actually checks.
- The `<output>` On-Send Protocol YAML includes fields like `dimensions_selected: int` without specifying what the value should be when operating in Measurement Plan mode (0? or the full count of what would be selected if data existed?). Minor ambiguity.

**Improvement Path:**
Add an L0 Executive Summary verification item to the self-review checklist. Clarify Measurement Plan mode behavior in on_send protocol fields. Score moves from 0.96 to 0.97.

---

### Traceability (0.95/1.00)

**Evidence:**

The agent definition footer contains an explicit traceability comment (line 476):
```
<!-- Traceability: H-34 (schema), H-34b (constitutional), AD-M-001 (naming), AD-M-004 (output levels), AD-M-005 (expertise), AD-M-006 (persona), AD-M-007 (session_context), AD-M-008 (post_completion_checks), ET-M-001 (reasoning_effort), SR-002 (input validation), SR-003 (output filtering), SR-009 (fallback behavior), AR-012 (forbidden actions) -->
```

This lists 13 specific standard references, each traceable to `agent-development-standards.md`.

Governance file traces to schema: `# Validated by: docs/schemas/agent-governance-v1.schema.json` (line 2). The schema file exists at that path (verified).

Constitutional triplet appears in both files:
- .md: `<guardrails>` Constitutional Compliance table lists P-003, P-020, P-022 with behavioral descriptions
- governance: `constitution.principles_applied` contains P-003, P-020, P-022 as first three entries

SKILL.md SSOT pointer: `*SSOT: skills/ux-heart-metrics/SKILL.md*` in footer.

Wave classification: `*Wave: 2 (Lean UX + Measurement)*` in footer; matches `skills/user-experience/rules/wave-progression.md` (file exists, Wave 2 classification verifiable).

**Gaps:**
- `<purpose>` references `skills/user-experience/rules/wave-progression.md` as the source for Wave 2 classification. This file exists (verified). However, `<methodology>` Phase 5 cites Few (2006) and Rodden (2010) without repeating the full bibliographic form that appears in Phase 5 body text -- the citations are present but their Traceability is at inline-reference level only, not at a formal References section within the agent definition. Unlike SKILL.md (which has a dedicated References section), the agent .md does not include a references section. This is not a structural requirement for agent definitions but reduces traceability for verifying Phase 4 benchmark sources.
- `(H-34b, AR-012)` tag on the Forbidden Actions block refers to the retired H-35 (now H-34 sub-item b). The `H-34b` notation is correct per the consolidation in quality-enforcement.md Retired Rule IDs, but a reader unfamiliar with the consolidation would not immediately find H-35 in the HARD Rule Index.

**Improvement Path:**
Add a brief References subsection to `<guardrails>` or `<methodology>` listing full citations for Rodden 2010, Few 2006, and the benchmark sources from Phase 4. Score moves from 0.95 to 0.97.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.90 | 0.93 | Add Baymard Institute (URL: https://baymard.com) and Bain & Company NPS benchmark full citations to Phase 4 Threshold Fallback Methodology in `<methodology>`. Match the citation format used in SKILL.md. |
| 2 | Internal Consistency | 0.95 | 0.97 | Add the 3 domain-specific forbidden_actions from .md body to governance yaml for full parity. Separately, update SKILL.md line 223 to remove "Bash" from the tool list description (SKILL.md issue, not agent definition issue). |
| 3 | Traceability | 0.95 | 0.97 | Add a References subsection to `<methodology>` listing full citations for Rodden 2010, Few 2006, Baymard Institute, and Bain & Company NPS benchmarks. This enables direct verification of Phase 4 threshold methodology sources. |
| 4 | Completeness | 0.96 | 0.97 | Add a second input_validation rule to governance explicitly requiring the `UX-{NNNN}` engagement ID format check (currently only in .md body). |
| 5 | Methodological Rigor | 0.97 | 0.99 | Add signal-level gap handling to Phase 3b (not just 3c edge case). Add P-020 user override path when user requests a dimension the agent would exclude in Phase 2 dimension selection. |
| 6 | Actionability | 0.96 | 0.97 | Add L0 Executive Summary verification to self-review checklist (item 10). Clarify on_send `dimensions_selected` value semantics for Measurement Plan mode. |

---

## H-34 Compliance Verification

| Check | Status | Evidence |
|-------|--------|----------|
| .md frontmatter: only official Claude Code fields | PASS | Fields: name, description, model, tools, disallowedTools -- all official; no unofficial fields |
| `tools` does NOT include Task (worker agent) | PASS | `disallowedTools: [Task]` explicitly declared |
| `tools` does NOT include WebSearch/WebFetch/Context7/Memory-Keeper (T2) | PASS | Only Read, Write, Edit, Glob, Grep declared |
| .governance.yaml validates against schema | PASS | version (semver), tool_tier (enum), identity.role (non-empty), identity.expertise (5 entries >= min 2), identity.cognitive_mode (systematic, valid enum), constitution.principles_applied (5 entries >= min 3), forbidden_actions (3 entries = min 3), fallback_behavior (warn_and_retry, valid pattern), output.location present when output.required=true |
| Constitutional triplet P-003/P-020/P-022 in governance constitution.principles_applied | PASS | Lines 55-57: P-003, P-020, P-022 are entries 1, 2, 3 |
| Constitutional triplet P-003/P-020/P-022 in .md guardrails | PASS | Constitutional Compliance table and Forbidden Actions block both cover P-003, P-020, P-022 |
| forbidden_actions >= 3 entries referencing constitutional triplet | PASS | 3 entries in governance (NPT-009-complete format); 6 entries in .md body (3 constitutional + 3 domain-specific) |
| forbidden_action_format declared | PASS | `forbidden_action_format: NPT-009-complete` |
| P-003 runtime self-check present | PASS | `<guardrails>` section contains complete P-003 Runtime Self-Check with exact halt message |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific file locations
- [x] Uncertain scores resolved downward: Evidence Quality at 0.90 (not 0.93) because Baymard/Bain citations in Phase 4 are named without full bibliographic entries; Internal Consistency at 0.95 (not 0.97) because domain-specific forbidden_actions are not mirrored in governance yaml; Traceability at 0.95 (not 0.97) because no References subsection in agent definition file
- [x] Calibration applied: 0.953 composite for a well-structured, complete, constitutionally compliant C4 agent definition with minor evidence gaps is consistent with the 0.92+ "strong work with minor refinements" band
- [x] No dimension scored above 0.97; Methodological Rigor at 0.97 is justified by the complete 5-phase workflow with edge cases, self-review checklist, and Measurement Plan mode definition

---

## Session Context Handoff

```yaml
verdict: PASS
composite_score: 0.953
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.90
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add Baymard Institute and Bain NPS full citations to Phase 4 Threshold Fallback Methodology in methodology section"
  - "Add 3 domain-specific forbidden_actions from .md body to governance yaml for full parity"
  - "Update SKILL.md line 223 to remove 'Bash' from tool list description (SKILL.md issue, not agent definition issue)"
  - "Add References subsection to methodology section listing full citations for all benchmark sources"
  - "Add second input_validation rule to governance for UX-{NNNN} format check"
```
