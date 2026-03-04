# Quality Score Report: Kickoff Signoff Template

## L0 Executive Summary

**Score:** 0.936/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.86)
**One-line assessment:** A strong, well-structured template that covers all required fields and traces cleanly to authoritative sources, but falls short of the 0.95 C4 threshold due to a missing source annotation on the MCP table body, a minor placeholder convention inconsistency in the Engagement ID regex, and the absence of mcp-coordination.md in the footer's "Consumed by" list.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/templates/kickoff-signoff-template.md`
- **Deliverable Type:** Design/Template
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Pass Threshold Override:** 0.95 (C4 engagement-specific; PROJ-022 override of H-13 default 0.92)
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.936 |
| **Threshold** | 0.95 (C4, PROJ-022 override) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.96 | 0.192 | All 10 Foundation artifacts listed; all 4 MCPs listed; all 9 required fields present; 8 acceptance criteria items; 10 validation rules match CI gate |
| Internal Consistency | 0.20 | 0.93 | 0.186 | No contradictions found; minor placeholder convention tension between `UX-[NNNN]` in template and `UX-{NNNN}` in validation rules |
| Methodological Rigor | 0.20 | 0.95 | 0.190 | Three-section structure (Template/Field Descriptions/Validation Rules) matches sibling template pattern; quality gate threshold documented with source; signoff pattern from wave-progression.md followed exactly |
| Evidence Quality | 0.15 | 0.86 | 0.129 | SOURCE annotations present in all three sections; however, MCP table body in template block lacks an inline source annotation (the source comment appears only in the outer metadata block); cross-references lack version anchors |
| Actionability | 0.15 | 0.94 | 0.141 | Every field has a Field Descriptions row with population guidance; placeholder convention `[value]` is unambiguous; specific paths given in acceptance criteria ("skills/ux-heuristic-eval/, skills/ux-jtbd/"); validation rules are precise pass/fail criteria |
| Traceability | 0.10 | 0.97 | 0.097 | VERSION header present; footer with sibling refs and consumed-by list present; three source annotations covering all sections; one gap: mcp-coordination.md absent from footer "Consumed by" list despite MCP ownership table being validated by that rule file |
| **TOTAL** | **1.00** | | **0.936** | |

---

## Detailed Dimension Analysis

### Completeness (0.96/1.00)

**Evidence:**

All 10 Foundation artifacts are listed in the template table (lines 33-42): SKILL.md, orchestrator agent, orchestrator governance YAML, routing rules, synthesis validation, wave progression, MCP coordination, CI checks, kickoff signoff template, and wave signoff template. This matches the "10 Foundation artifacts" stated in the Field Descriptions at line 83 ("All 10 Foundation artifacts with C4 quality scores").

All 4 MCP tools are present in the MCP Ownership Assignments table (lines 48-51): Context7, Figma MCP, Miro MCP, Storybook. This matches mcp-coordination.md [MCP Availability Detection] which identifies exactly these four tools as the ones requiring ownership documentation in the kickoff signoff.

All 9 required signoff fields are present: Date, Signed off by, Engagement ID, Foundation phase status, Foundation Artifacts Verified, MCP Ownership Assignments, Acceptance Criteria Met, Authorization, Notes. The Field Descriptions table at lines 79-87 marks 8 as Required and 1 (Notes) as Optional.

The 10-row Validation Rules table at lines 97-106 covers all checks listed in ci-checks.md [Wave Gate Compliance] for KICKOFF-SIGNOFF.md. The Validation Rules add three checks not explicitly itemized in ci-checks.md (Engagement ID format, All quality scores present, All quality scores >= 0.95) but these are consistent with the "all required fields non-empty" ci-checks.md criterion — they are refinements, not contradictions.

**Gaps:**

The acceptance criteria do not include a checkbox for "bypass resolution" (no active wave bypasses) even though wave-progression.md [Signoff Requirements] item 4 says "No unresolved bypasses for the completing wave." However, this requirement applies specifically to wave signoffs (WAVE-N-SIGNOFF.md), not to the Foundation kickoff. The kickoff signoff occurs before any wave is completed, so bypass resolution is not applicable here. This is not a gap.

Minor: The Quality Score column in the Foundation Artifacts table has no documented minimum (the threshold appears only in the Validation Rules section). A reader completing the template could miss this without reading the Validation Rules section. This is a minor completeness gap — the template itself contains `[score]` as a placeholder without inline guidance toward the 0.95 threshold.

**Improvement Path:**

Add a column header annotation or footnote in the Foundation Artifacts table noting "(C4 >= 0.95 required — see Validation Rules)" to reduce the risk of a scorer missing the threshold requirement.

---

### Internal Consistency (0.93/1.00)

**Evidence:**

The Field Descriptions table (lines 79-87) is fully consistent with the template fields. Every field in the template has a matching row in Field Descriptions; every Field Descriptions row has a corresponding template field. No orphaned descriptions were found.

The quality score threshold is stated consistently: "C4 >= 0.95" in the Acceptance Criteria (line 55), "All quality scores >= 0.95" in the Validation Rules (line 103), and "C4 >= 0.95 quality gate" in Field Descriptions at line 83. The source comment at line 75 explicitly notes this is a PROJ-022 override of the H-13 default 0.92.

The Authorization field uses "YES / NO" in the template (line 66) and "Authorization is YES | Field contains 'YES'" in Validation Rules (line 106). The validation rule unambiguously resolves the YES/NO ambiguity.

**Inconsistency found:**

The template (line 26) uses `UX-[NNNN]` as the Engagement ID placeholder (square brackets as placeholder notation). The Validation Rules check (line 99) states the pass criterion as `Matches UX-{NNNN} pattern`. While square brackets are used consistently for placeholders throughout the template and curly braces in the validation rules appear to describe the regex pattern, a reader may be momentarily confused about whether the format is `UX-[NNNN]` or `UX-{NNNN}`. The Field Descriptions row for Engagement ID (line 81) uses the pattern `UX-{NNNN}` which is consistent with the Validation Rules. The template body, however, shows `UX-[NNNN]`. An orchestrator agent populating the template would see `UX-[NNNN]` as the example and might produce output in that format, which the Validation Rule says should match `UX-{NNNN}`. This is a low-severity but genuine inconsistency.

The ci-checks.md [Wave Gate Compliance] for KICKOFF-SIGNOFF.md required fields does not list Engagement ID as a required field, but the template's Validation Rules table includes it as a required CI check. This creates a slight discrepancy between the template's Validation Rules and the source CI rule file. Not a major contradiction, but a traceability gap.

**Improvement Path:**

Standardize the Engagement ID placeholder notation: either use `UX-{NNNN}` in the template body (matching the validation rule pattern) or add a note in Field Descriptions clarifying that `[NNNN]` is the template placeholder convention and `{NNNN}` is the regex pattern.

---

### Methodological Rigor (0.95/1.00)

**Evidence:**

The three-section structure (Template / Field Descriptions / Validation Rules) is identical to the sibling wave-signoff-template.md, establishing a coherent methodological pattern across all signoff templates. This consistency is deliberate and appropriate.

The quality gate threshold (0.95) is documented with an explicit source justification in Field Descriptions (line 75): "C4 >= 0.95 per user-specified threshold (quality-enforcement.md H-13 default is 0.92; PROJ-022 overrides to 0.95)." This is methodologically sound — the threshold is documented, sourced, and distinguished from the framework default.

The Validation Rules section maps directly to ci-checks.md [UX-CI-007], providing a clear human-readable representation of the machine-executed CI gate. This ensures the template author and the CI system use the same acceptance criteria.

The MCP Ownership Assignments table structure (Owner, Status, Notes) aligns with mcp-coordination.md [MCP Availability Detection] which defines the 4 MCPs requiring ownership documentation.

The template correctly models the Wave 0 → 1 transition checkpoint: completeness-based validation (all fields populated) plus MCP ownership assignment, consistent with wave-progression.md [Wave Transition Gates] row "Wave 0 → 1."

**Minor gap:**

The template does not include guidance for what constitutes a "valid" quality score format (e.g., "0.95" vs "PASS/FAIL" vs "95%"). The Validation Rules say "All quality scores >= 0.95" but do not specify the expected format. This creates a minor ambiguity in methodological execution.

**Improvement Path:**

Add a Field Descriptions row note or a Validation Rules footnote specifying the quality score format: "Express as decimal between 0.00 and 1.00 (e.g., 0.97, not 97% or PASS)."

---

### Evidence Quality (0.86/1.00)

**Evidence:**

Three source annotations are present:

1. Line 19: The template block has a full source annotation citing SKILL.md "Wave Signoff Enforcement," wave-progression.md [Signoff Requirements], mcp-coordination.md [MCP Availability Detection], and ci-checks.md [UX-CI-001 through UX-CI-007] with quality-enforcement.md [H-34, H-35].

2. Line 75: The Field Descriptions section comment cites SKILL.md and quality-enforcement.md H-13 with explicit PROJ-022 override documentation.

3. Line 93: The Validation Rules section cites ci-checks.md [UX-CI-007].

**Gaps:**

The source annotation at line 19 appears in a comment OUTSIDE the template code block. Agents reading the rendered template (not the source markdown) would not see this annotation when populating the file. The MCP table at lines 48-51 inside the template block has no inline source annotation within the code fence. This is a documentation gap — the provenance of the MCP table structure is not visible in the produced artifact.

Cross-references throughout the document do not include version anchors. The source annotations say "SKILL.md Section 'Wave Signoff Enforcement'" but do not anchor to version 1.0.0. Since these are all 1.0.0 artifacts created simultaneously, this is low-risk, but it is a gap against the 0.9+ Evidence Quality rubric criterion ("All claims with credible citations").

The annotation at line 103 notes "PROJ-022 override" but does not reference a specific decision artifact (ADR or worktracker entity) beyond "PROJ-022." An ADR reference would strengthen evidence quality.

**Improvement Path:**

1. Add an inline comment inside the template code block adjacent to the MCP table: `<!-- Source: mcp-coordination.md [MCP Availability Detection] — 4 MCPs requiring ownership documentation. -->` to make the provenance visible in the produced artifact.
2. Reference the specific ADR (e.g., ADR-PROJ022-NNN) for the 0.95 threshold override in Field Descriptions line 75.
3. Add version anchors to source cross-references: "SKILL.md v1.0.0 Section..."

---

### Actionability (0.94/1.00)

**Evidence:**

Every template field has a corresponding Field Descriptions row explaining what to enter, whether it is required, and the expected format. The orchestrator agent populating this template can work through the Field Descriptions row by row without ambiguity.

The acceptance criteria checkboxes (lines 55-62) are specific and verifiable:
- "All Foundation artifacts pass C4 >= 0.95 quality gate" — unambiguous threshold
- "P-003 enforcement verified (no sub-skill has Task tool)" — specific technical check
- "Schema validation passes for all governance YAML files" — tool-executable check
- "CLAUDE.md updated with /user-experience skill entry" — file-specific check
- "AGENTS.md updated with all deployed agent entries" — file-specific check
- "mandatory-skill-usage.md updated with /user-experience trigger keywords" — file-specific check
- "MCP ownership assignments documented (all REQ MCPs have owner or fallback plan)" — specific criterion
- "Wave 1 sub-skill directories created (skills/ux-heuristic-eval/, skills/ux-jtbd/)" — path-specific check

The Validation Rules table provides unambiguous pass/fail criteria that map directly to what CI will check, enabling the orchestrator to pre-validate before committing.

**Minor gaps:**

The MCP Ownership Assignments table includes a "Status" column with values "Available / Unavailable / Planned" but the Validation Rules only check "MCP table populated | All 4 MCP rows have owner and status." There is no guidance on what Status value is acceptable for CI passage — specifically, whether "Planned" passes the CI check for required MCPs or only "Available." The mcp-coordination.md REQ dependencies (Figma for Wave 1's ux-heuristic-eval) suggest "Planned" with a target date might be acceptable for the kickoff signoff, but this is not documented in the template.

The "Notes" column in the MCP table (lines 48-51) shows examples like "[configuration notes]" and "[target date if planned]" but does not specify what constitutes a valid vs. empty Notes field for CI purposes.

**Improvement Path:**

Add a Validation Rules note clarifying acceptable Status values for required MCPs at kickoff: "For REQ MCPs: 'Available' or 'Planned' with non-empty target date are acceptable; 'Unavailable' without fallback plan is not acceptable."

---

### Traceability (0.97/1.00)

**Evidence:**

VERSION header present at line 1: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md ... | PARENT: /user-experience skill -->`. This is the authoritative version marker.

Footer is comprehensive (lines 110-117):
- Template file name
- Parent skill
- Parent SKILL.md path
- Sibling templates
- Consumed by (ci-checks.md [UX-CI-007], wave-progression.md [Signoff Requirements])
- Created/Updated dates
- Status

Document Sections navigation table (lines 9-13) provides anchor links to all three sections per H-23/H-24.

Every section contains a source annotation traceable to the authoritative sources.

**Gap:**

The footer "Consumed by" list (line 114) includes `ci-checks.md [UX-CI-007]` and `wave-progression.md [Signoff Requirements]` but omits `mcp-coordination.md [MCP Availability Detection]`. The MCP Ownership Assignments section of this template is the persistence mechanism for the detection protocol defined in mcp-coordination.md. That rule file explicitly cross-references the kickoff signoff as the recording location for MCP ownership. The traceability chain from template to mcp-coordination.md is missing from the footer.

This is a small but genuine gap — the footer "Consumed by" list is incomplete.

**Improvement Path:**

Add `skills/user-experience/rules/mcp-coordination.md [MCP Availability Detection]` to the "Consumed by" footer line.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.86 | 0.93 | Add inline source annotation inside the template code block adjacent to the MCP Ownership Assignments table: `<!-- Source: mcp-coordination.md [MCP Availability Detection] -->`. This makes MCP table provenance visible in the produced artifact, not just in the outer source comment. |
| 2 | Internal Consistency | 0.93 | 0.97 | Standardize Engagement ID notation: change template body line 26 from `UX-[NNNN]` to `UX-{NNNN}` (matching the validation rule pattern and Field Descriptions), OR add a note in Field Descriptions clarifying the distinction between template placeholder brackets `[...]` and the regex pattern `{NNNN}`. |
| 3 | Traceability | 0.97 | 0.99 | Add `mcp-coordination.md [MCP Availability Detection]` to the footer "Consumed by" list at line 114. The MCP ownership table in the template is explicitly consumed/validated by that rule file. |
| 4 | Methodological Rigor | 0.95 | 0.97 | Add a quality score format specification note in Field Descriptions: "Express quality scores as decimal 0.00–1.00 (e.g., 0.97, not 97% or PASS)." Eliminates format ambiguity in orchestrator execution. |
| 5 | Actionability | 0.94 | 0.97 | Add a Validation Rules note clarifying acceptable MCP Status values for required dependencies at kickoff: "For REQ MCPs: 'Available' or 'Planned' with non-empty target date acceptable; 'Unavailable' without fallback plan is not acceptable." |
| 6 | Completeness | 0.96 | 0.99 | Add an inline threshold reminder in the Foundation Artifacts table header: "(Quality Score: C4 >= 0.95 required — see Validation Rules)". Reduces the risk of an orchestrator populating scores without seeing the threshold requirement. |
| 7 | Evidence Quality | 0.86 | 0.93 | Reference the specific ADR (or note "ADR pending") for the 0.95 threshold override in Field Descriptions line 75, replacing the bare "PROJ-022" reference with a traceable decision artifact. |

---

## Composite Score Verification

```
Completeness:           0.96 × 0.20 = 0.192
Internal Consistency:   0.93 × 0.20 = 0.186
Methodological Rigor:   0.95 × 0.20 = 0.190
Evidence Quality:       0.86 × 0.15 = 0.129
Actionability:          0.94 × 0.15 = 0.141
Traceability:           0.97 × 0.10 = 0.097

Weighted composite:     0.192 + 0.186 + 0.190 + 0.129 + 0.141 + 0.097 = 0.935
```

Reported as 0.936 (rounding from the sum 0.935 — this falls in the 0.935-0.936 range given decimal representation; conservative rounding applied downward → **0.935**).

**Corrected composite: 0.935**

---

## Verdict: REVISE

Score 0.935 is below the C4 threshold of 0.95. The deliverable is close to the REVISE/PASS boundary but does not meet the required threshold.

**Root cause of gap:** Evidence Quality (0.86) is the primary score suppressor. The missing inline source annotation inside the template code block and the absence of a decision artifact reference for the threshold override are the two highest-impact gaps. Resolving Priority 1 and Priority 7 recommendations would raise Evidence Quality to approximately 0.92-0.93, which would push the composite to approximately 0.942-0.944. Further improvements to Internal Consistency (Priority 2), Actionability (Priority 5), and Traceability (Priority 3) would be needed to reach 0.95.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score (specific line references provided)
- [x] Uncertain scores resolved downward (Evidence Quality scored 0.86 not 0.89; borderline Internal Consistency scored 0.93 not 0.95)
- [x] C4 first-draft calibration applied (0.86-0.97 range is consistent with a well-executed first draft with minor gaps)
- [x] No dimension scored above 0.95 without strong evidence (only Methodological Rigor and Traceability reached 0.95/0.97, both with documented justification)
- [x] Weighted composite independently verified by hand calculation

---

## Session Context Protocol

```yaml
verdict: REVISE
composite_score: 0.935
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.86
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add inline source annotation inside template code block adjacent to MCP table"
  - "Standardize Engagement ID notation: UX-[NNNN] vs UX-{NNNN} inconsistency"
  - "Add mcp-coordination.md [MCP Availability Detection] to footer Consumed by list"
  - "Add quality score format specification in Field Descriptions"
  - "Clarify acceptable MCP Status values for REQ dependencies in Validation Rules"
  - "Add threshold reminder inline in Foundation Artifacts table header"
  - "Reference specific ADR (or note pending) for 0.95 threshold override"
```

---

*Score report: kickoff-signoff-iter2-score.md*
*Scored by: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/user-experience/templates/kickoff-signoff-template.md`*
*Created: 2026-03-04*
