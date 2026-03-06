# Quality Score Report: ci-checks.md

## L0 Executive Summary

**Score:** 0.814/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Methodological Rigor (0.72)

**One-line assessment:** The CI gate framework is structurally sound with 13 gates defined and good source traceability, but 5 of 13 gates lack implementation patterns, one bash script contains a counting logic bug (UX-CI-003), and minor internal inconsistencies exist between the body and summary table — targeted fixes to implementation completeness and script correctness will bring this above threshold.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/ci-checks.md`
- **Deliverable Type:** Rule file (CI/CD verification rules)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Custom Threshold:** >= 0.95 (C4 deliverable per scoring instructions)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.814 |
| **Threshold** | 0.95 (C4, per scoring request) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.80 | 0.160 | 13 gates defined in summary; 5 gates lack implementation patterns in body sections |
| Internal Consistency | 0.20 | 0.82 | 0.164 | Gate ID/name mismatch (UX-CI-003 body vs. table); UX-CI-003 script logic bug; UX-CI-007 field discrepancy |
| Methodological Rigor | 0.20 | 0.72 | 0.144 | UX-CI-005, UX-CI-006, UX-CI-009-013 have no bash scripts; UX-CI-001/003 scripts have correctness issues |
| Evidence Quality | 0.15 | 0.84 | 0.126 | Source annotations present on most sections; UX-CI-005/006 and Output sections lack `Source:` comments |
| Actionability | 0.15 | 0.83 | 0.125 | Pass criteria unambiguous for all 13; 8 of 13 are immediately scriptable; 5 require further specification |
| Traceability | 0.10 | 0.95 | 0.095 | VERSION header, footer with sibling refs, navigation table with anchors all present; high traceability |
| **TOTAL** | **1.00** | | **0.814** | |

---

## Detailed Dimension Analysis

### Completeness (0.80/1.00)

**Evidence:**

All 13 CI gates appear in the summary table (UX-CI-001 through UX-CI-013) with Gate ID, Gate Name, Scope, Pass Criteria, and Blocking classification — this part is complete. Six gates in the body have full scope + pass criteria + implementation pattern:

- UX-CI-001 (Task Tool Grep): scope, pass criteria, implementation bash script
- UX-CI-002 (disallowedTools Declaration): scope, pass criteria, implementation bash script
- UX-CI-003 (Forbidden Actions Declaration): scope, pass criteria, implementation bash script
- UX-CI-004 (Governance YAML Schema): scope, pass criteria, implementation bash script
- UX-CI-007 (Signoff File Structure): required fields enumerated for both file types
- UX-CI-008 (Signoff Ordering): pass criteria and exception case stated

**Gaps:**

1. **UX-CI-005 (Required Governance Fields):** Body section lists required fields in a bullet list but contains zero implementation pattern. No bash script, no pseudo-code, no validation logic. The scope is implicitly all governance YAML files but is not restated. This gate is underdeveloped relative to peer gates.

2. **UX-CI-006 (Frontmatter-Governance Consistency):** Body section states only a pass criteria sentence ("name field equals filename without extension"). No implementation pattern whatsoever. No scope declaration in the body (summary table provides scope indirectly via "Agent dual-file pairs"). Substantially thinner than UX-CI-001 through UX-CI-004.

3. **UX-CI-009 (Keyword Collision Check):** Body section describes a 3-step implementation approach (extract, cross-reference, flag) but provides no bash script or tooling pattern. The description is narrative rather than implementable.

4. **UX-CI-010 (Negative Keyword Coverage):** Body section provides pass criteria only. No implementation pattern.

5. **UX-CI-011, UX-CI-012, UX-CI-013 (Output Quality Checks):** Three gates share a body section ("Output Quality Checks") with minimal content per gate. Each gate has a scope and pass criteria but zero implementation pattern. UX-CI-012 (Traceability) does not define what a "source finding ID" looks like structurally, making automated checking ambiguous.

**Rubric calibration:** The 0.9+ threshold requires "All requirements addressed with depth." Depth specifically requires implementation patterns — the stated purpose of this file is "automated CI checks." Five gates (38% of the total 13) lack implementation patterns. This is a notable gap that precludes the 0.9+ band.

**Improvement Path:** Add implementation patterns (bash scripts or equivalent) for UX-CI-005, UX-CI-006, UX-CI-009, UX-CI-010, UX-CI-011, UX-CI-012, UX-CI-013. For text-matching gates (UX-CI-011-013), define the grep/awk patterns that check synthesis output files.

---

### Internal Consistency (0.82/1.00)

**Evidence:**

Gate IDs are sequential UX-CI-001 through UX-CI-013. The Blocking classification is consistently applied: six gates are "Yes" (blocking) and seven are "Warning" — this split is internally consistent with the principle that P-003, schema, and wave signoff violations block CI while routing and output quality gates warn. Source annotations reference the correct SKILL.md sections throughout.

**Gaps:**

1. **UX-CI-003 body section title vs. summary table name mismatch.** Body section heading: "CI Gate: Forbidden Actions Declaration." Summary table Gate Name: "Forbidden Actions P-003." These are logically equivalent but the inconsistency creates friction when navigating the document; a reader following the summary table finds a differently-named section. Minor but real.

2. **UX-CI-003 bash script logic bug — counting inconsistency.** The script contains:
   ```bash
   fa_count=$(grep -c 'P-0[0-9][0-9]' "$yaml_file" || true)
   ...
   if [ "$fa_count" -lt 3 ]; then
     echo "FAIL: $yaml_file has fewer than 3 forbidden_actions entries"
   ```
   This counts lines containing principle references (P-0xx patterns), not `forbidden_actions` array entries. A YAML file with one `forbidden_actions` entry that contains "P-003, P-020, P-022" on a single line would count as 1 but satisfy the 3-principle check; conversely, a file with multiple principles on multiple lines would overcount. The variable name `fa_count` implies it counts `forbidden_actions` entries but actually counts principle reference lines. This is an internal logic inconsistency between the script behavior and its documented intent.

3. **UX-CI-007 required fields discrepancy.** The body section for UX-CI-007 (Signoff File Structure) lists "Foundation artifacts verified table (all rows present)" as a required KICKOFF-SIGNOFF.md field. The SKILL.md "Wave Signoff Enforcement" and wave-progression.md "Signoff File Validation" instead list "MCP ownership assignments present" as a specific KICKOFF-SIGNOFF.md requirement (referenced in UX-CI-007 pass criteria in the summary table: "All required fields non-empty"). The body section omits the MCP ownership assignment field while the summary table's scope description implies it is covered. Minor inconsistency.

4. **SKILL.md ux-ai-first-design Figma classification discrepancy.** SKILL.md Section "MCP Integration Architecture" (line ~411) shows `/ux-ai-first-design` as "**REQ**" for Figma. mcp-coordination.md [MCP Dependency Matrix] shows `/ux-ai-first-design` as "**COND**" for Figma. The ci-checks.md document does not address this discrepancy, which means the CI gate scope for schema validation may cover files with different expected governance structures depending on which source is authoritative. This cross-document inconsistency affects UX-CI-004 scope correctness but originates outside ci-checks.md; noted here as a consistency concern, not penalized as a ci-checks.md authoring failure.

**Improvement Path:** Align UX-CI-003 body section heading with summary table name. Fix the `fa_count` counting logic to count array entries (not principle reference lines). Add MCP ownership assignment field to UX-CI-007 KICKOFF-SIGNOFF required fields list.

---

### Methodological Rigor (0.72/1.00)

**Evidence:**

The document correctly establishes the pattern: each gate should have scope, pass criteria, and an implementation pattern. UX-CI-001 through UX-CI-004 follow this pattern well and are testable. The scope declarations use glob patterns (`skills/ux-*/agents/*.md`) that are precise and actionable. The blocking/warning classification follows a principled logic (constitutional violations = blocking; operational quality = warning).

**Gaps:**

1. **Absent implementation patterns for 5+ gates (systematic gap, not isolated).** UX-CI-005, UX-CI-006, UX-CI-009, UX-CI-010, UX-CI-011, UX-CI-012, UX-CI-013 — 7 of 13 gates — lack implementation patterns. A CI rule file without implementation patterns for more than half its gates cannot be considered methodologically rigorous. The pattern established by UX-CI-001-004 is not sustained.

2. **UX-CI-001 frontmatter extraction fragility.** The bash script uses:
   ```bash
   tools_line=$(grep -A 20 '^---' "$agent_file" | grep -E '^tools:' | head -1)
   ```
   The pattern `grep -A 20 '^---'` will match both the opening `---` and closing `---` of YAML frontmatter, potentially including document body content if the body contains a line starting with `---`. A more rigorous approach would extract only the frontmatter between the first and second `---` delimiters. This is a real implementation correctness issue, not hypothetical — Markdown files routinely contain horizontal rules (`---`) in the body.

3. **UX-CI-003 bash script counting bug (repeated from Internal Consistency).** `fa_count=$(grep -c 'P-0[0-9][0-9]' ...)` counts lines with principle references, not `forbidden_actions` array entries. The check `[ "$fa_count" -lt 3 ]` will produce a false PASS for a YAML file that references P-003, P-020, P-022 in a single entry (count = 1 < 3 triggers FAIL even though the check is satisfied conceptually), or a false PASS for a file with 3 lines each containing only one principle reference but only 1 actual `forbidden_actions` entry. The methodology for counting forbidden_actions entries is incorrect.

4. **UX-CI-004 uses `jsonschema-validate` without specifying the tool.** The implementation pattern calls `jsonschema-validate "$yaml_file" docs/schemas/agent-governance-v1.schema.json` without specifying which tool provides `jsonschema-validate`. This is a non-standard command name not found in common distributions. A rigorous implementation pattern would specify the exact tool (e.g., `python -m jsonschema`, `yajsv`, or a project-specific script) per H-05 (UV-only Python environment).

5. **UX-CI-009 narrative approach vs. automated gate.** The 3-step description for keyword collision detection is process-oriented ("Extract positive keywords from the new sub-skill's description") rather than script-oriented. This makes UX-CI-009 a manual process description masquerading as a CI gate. For a file titled "CI Checks Rules," this is a methodological gap.

**Improvement Path:** Add bash scripts or equivalent for all 7 gates lacking them. Fix UX-CI-001 frontmatter extraction to use proper YAML delimiter boundary detection. Fix UX-CI-003 to count `forbidden_actions` array entries correctly. Specify the exact JSON Schema validation tool with `uv run` invocation per H-05. Convert UX-CI-009 to an automated script or explicitly classify it as a manual gate.

---

### Evidence Quality (0.84/1.00)

**Evidence:**

Strong: The document header contains a full VERSION comment with source traceability: `SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "P-003 Compliance", "Wave Transition Quality Gates"`. Each major section has an HTML source comment, e.g.:

- P-003 Enforcement section: `<!-- Source: SKILL.md Section "P-003 Compliance" — single-level nesting enforcement. --> <!-- Source: H-34 (agent definition standards...), H-01 (P-003). -->`
- Schema Validation section: `<!-- Source: H-34 (agent definition standards) — dual-file architecture. -->`
- Wave Gate Compliance section: `<!-- Source: skills/user-experience/rules/wave-progression.md [Signoff Requirements] ... -->`
- Trigger Map Validation section: `<!-- Source: agent-routing-standards.md RT-M-004 — keyword collision detection. -->`
- Output Quality Checks section: `<!-- Source: SKILL.md ... Sections "Synthesis Hypothesis Validation", "Cross-Framework Synthesis Protocol" ... -->`

Cross-references include specific section names and sub-section anchors, enabling direct lookup.

**Gaps:**

1. **UX-CI-005 (Required Governance Fields) subsection lacks a `Source:` annotation.** This subsection is nested within Schema Validation but adds new content (the specific list of required fields). The Schema Validation section header annotation references H-34 generally but does not specifically anchor to `agent-development-standards.md [Governance Fields]` table. A reader cannot determine which authoritative source defines the specific required field list.

2. **UX-CI-006 (Frontmatter-Governance Consistency) subsection lacks a `Source:` annotation.** Same issue as UX-CI-005 — nested within Schema Validation without its own source annotation.

3. **H-35 retired rule handling.** The document body at line 79 states "per H-34(b)" for minimum 3 entries in `capabilities.forbidden_actions`. The VERSION header references "H-35" directly (the retired sub-item). While the parenthetical `(b)` and inline note clarify this, the header's direct reference to the retired H-35 ID may cause confusion. The header comment says `[H-35]` (constitutional compliance) as if it is a live rule ID, which contradicts `quality-enforcement.md` Retired Rule IDs table. This is a minor evidence quality issue.

4. **No citations for threshold values.** The UX-CI-007 pass criteria references "Quality gate composite score (>= 0.85)" without citing `wave-progression.md` [Wave Transition Gates] as the authoritative threshold source. A CI gate checking a threshold should cite the source of that threshold.

**Improvement Path:** Add `Source:` annotations to UX-CI-005 and UX-CI-006 subsections pointing to `agent-development-standards.md [Governance Fields]`. Update the header VERSION comment to reference H-34 consistently (H-35 is retired). Add citation to wave-progression.md for the 0.85 composite threshold in UX-CI-007.

---

### Actionability (0.83/1.00)

**Evidence:**

For the 8 gates with bash scripts and explicit pass criteria, actionability is high. Each bash script includes `exit 1` on failure and `echo "PASS:..."` on success — a CI engineer can integrate these directly. The Blocking/Warning classification in the summary table provides unambiguous merge-blocking guidance. The summary table format (single table, all 13 gates) enables a CI engineer to quickly assess what will block a PR.

The pass criteria for UX-CI-008 (Signoff Ordering) is concrete and checkable: "WAVE-2-SIGNOFF.md cannot exist without WAVE-1-SIGNOFF.md." The exception (bypass documentation) is explicitly stated.

**Gaps:**

1. **UX-CI-009 is not actionable as written.** The 3-step description ("Extract positive keywords from the new sub-skill's description. Cross-reference against all existing trigger map rows...") requires human judgment. There is no script, no grep pattern, no tooling. A CI engineer cannot implement this gate without significant additional specification.

2. **UX-CI-011, UX-CI-012, UX-CI-013 pass criteria are stated but not implementable.** "Every finding in the output includes a confidence classification (HIGH, MEDIUM, or LOW)" — this requires pattern matching against synthesis output, but the exact format of confidence classifications in those files is not defined here. The reader must consult synthesis-validation.md to understand the format. A CI gate that requires consulting another rule file to implement is partially but not fully actionable.

3. **UX-CI-012 traceability check is ambiguous.** "Every finding includes a source sub-skill name and source finding ID" — what is a "source finding ID"? Is it `HE-003`? Is it `SIGNAL-1`? The format is not defined in ci-checks.md. synthesis-validation.md [Required Traceability] defines it as `HE-003` format but the CI gate does not cross-reference this definition, leaving the check partially ambiguous.

4. **UX-CI-004 tool ambiguity (repeated from Methodological Rigor).** `jsonschema-validate` is not a standard command. An engineer implementing this gate cannot determine which tool to install.

**Improvement Path:** Convert UX-CI-009 to an automated grep-based check or explicitly document it as a manual gate with a manual verification checklist. Add explicit format references for UX-CI-012 (traceability) pointing to synthesis-validation.md [Required Traceability]. Specify the JSON Schema validation tool for UX-CI-004.

---

### Traceability (0.95/1.00)

**Evidence:**

This is the strongest dimension. Evidence:

- **VERSION header:** `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "P-003 Compliance", "Wave Transition Quality Gates" | PARENT: /user-experience skill -->` — full version, date, source, parent.
- **Navigation table:** Present with anchor links for all 6 major sections plus CI Gate Summary.
- **Footer:** `*Rule file: ci-checks.md * Parent skill: /user-experience * Parent SKILL.md: skills/user-experience/SKILL.md * Sibling rules: ux-routing-rules.md, synthesis-validation.md, wave-progression.md, mcp-coordination.md * Created/Updated/Status*` — complete.
- **Source annotations:** Every major section has at least one HTML comment with source traceability.
- **Sibling cross-references in intro paragraph:** The document intro explicitly cross-references which sibling rule files consume which CI gates (e.g., "wave-progression.md (wave signoff validation criteria consumed by UX-CI-007/UX-CI-008)") — this bidirectional traceability is strong.
- **Framework rule file references:** H-34, H-01, RT-M-004, agent-development-standards.md, agent-routing-standards.md all cited with section anchors.

**Gaps:**

1. **UX-CI-005 and UX-CI-006 subsections lack individual source annotations** (noted also under Evidence Quality). While the parent section has an annotation, the sub-gates introduce new content without individual traceability.

2. **H-35 reference in VERSION header.** The header cites "[H-35]" which is a retired rule ID per quality-enforcement.md. Should reference H-34(b) or simply H-34 with the note that H-35 was retired into it. Minor.

These are minor and limited to two subsections. The overall traceability of this document is genuinely strong; the 0.95 score reflects this while penalizing the two subsection gaps and the retired rule reference.

**Improvement Path:** Add per-subsection `Source:` annotations to UX-CI-005 and UX-CI-006. Update the VERSION header to reference H-34 (not H-35).

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Methodological Rigor | 0.72 | 0.88 | Add bash scripts for UX-CI-005, UX-CI-006, UX-CI-009, UX-CI-010, UX-CI-011, UX-CI-012, UX-CI-013; fix UX-CI-001 frontmatter extraction fragility; fix UX-CI-003 forbidden_actions counting logic; specify JSON Schema tool in UX-CI-004 |
| 2 | Completeness | 0.80 | 0.92 | Add implementation patterns (scope + bash scripts) to all 7 gates that lack them; define structural format for traceability IDs in UX-CI-012 |
| 3 | Internal Consistency | 0.82 | 0.93 | Align UX-CI-003 body heading with summary table name; fix UX-CI-003 script `fa_count` to count array entries; add MCP ownership assignments to UX-CI-007 KICKOFF-SIGNOFF required field list |
| 4 | Actionability | 0.83 | 0.93 | Convert UX-CI-009 to automated script or mark as manual gate; add format reference for UX-CI-012 traceability check; specify `uv run` invocation for UX-CI-004 schema validation tool |
| 5 | Evidence Quality | 0.84 | 0.93 | Add `Source:` annotations to UX-CI-005 and UX-CI-006 subsections; update VERSION header to reference H-34 instead of retired H-35; add wave-progression.md citation for 0.85 threshold in UX-CI-007 |
| 6 | Traceability | 0.95 | 0.97 | Add per-subsection source annotations to UX-CI-005 and UX-CI-006; replace H-35 with H-34 in VERSION header |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computed
- [x] Evidence documented for each score with specific line references and quote excerpts
- [x] Uncertain scores resolved downward (Methodological Rigor: considered 0.74, settled at 0.72 due to systematic gap across 7 gates; Internal Consistency: considered 0.83, settled at 0.82 due to script logic bug)
- [x] First-draft calibration considered (this is iteration 2; a first draft would be lower)
- [x] No dimension scored above 0.95 without exceptional evidence (Traceability at 0.95 reflects genuinely strong bidirectional cross-referencing with VERSION header, footer, and section annotations)

**Anti-leniency note:** The Methodological Rigor score of 0.72 is below 0.70 calibration anchor (acceptable with significant gaps). The choice was between 0.70 and 0.74. The evidence supports 0.72: the pattern established by UX-CI-001-004 is strong (genuine rigor where implemented), but 7 of 13 gates lacking implementation patterns is a systematic failure mode, not isolated. A rule file titled "CI Checks Rules" that cannot produce CI-runnable scripts for more than half its gates falls clearly into the "0.70-0.89: Sound methodology, minor gaps" range only if "minor" is generously interpreted. The 7/13 absence rate is not minor; it is chosen at 0.72 (just above the significant-gaps floor) because the framework is correctly designed and the existing 6 scripts are genuinely sound.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.814
threshold: 0.95
weakest_dimension: methodological_rigor
weakest_score: 0.72
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add bash scripts for UX-CI-005, UX-CI-006, UX-CI-009, UX-CI-010, UX-CI-011, UX-CI-012, UX-CI-013 (7 gates missing implementation patterns)"
  - "Fix UX-CI-003 fa_count to count forbidden_actions array entries, not principle reference lines"
  - "Fix UX-CI-001 frontmatter extraction to respect YAML delimiter boundaries (prevent body false matches)"
  - "Specify JSON Schema validation tool in UX-CI-004 with uv run invocation per H-05"
  - "Add Source annotations to UX-CI-005 and UX-CI-006 subsections"
  - "Align UX-CI-003 body heading with summary table gate name"
  - "Add MCP ownership assignment field to UX-CI-007 KICKOFF-SIGNOFF required field list"
  - "Define traceability ID format in UX-CI-012 with reference to synthesis-validation.md"
  - "Update VERSION header H-35 reference to H-34 (retired rule ID)"
```
