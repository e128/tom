# Quality Score Report: Wave Signoff Template

## L0 Executive Summary
**Score:** 0.893/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.82)
**One-line assessment:** The template is structurally sound and internally consistent, but two gaps prevent PASS: (1) the ADR-PROJ022-002 threshold citation is marked PROVISIONAL with the ADR still a STUB, reducing evidence quality; (2) the AGENTS.md acceptance criterion is underdefined and the Cross-Framework Synthesis Test section provides insufficient specificity for reliable, repeatable execution by a new operator.

---

## Scoring Context
- **Deliverable:** `skills/user-experience/templates/wave-signoff-template.md`
- **Deliverable Type:** Design (template artifact)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.893 |
| **Threshold** | 0.95 (C4 per scoring context) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All required sections present; per-wave customization and validation rules complete; one minor gap in bypass section documentation |
| Internal Consistency | 0.20 | 0.94 | 0.188 | Terminology and thresholds consistent throughout; one minor tension between "FAILED" status in sub-skills table vs. acceptance criteria checkbox — not a contradiction |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Well-structured, follows peer template (kickoff-signoff), CI gate descriptions cross-referenced; synthesis test section lacks sufficient specificity for test execution |
| Evidence Quality | 0.15 | 0.82 | 0.123 | ADR-PROJ022-002 cited as PROVISIONAL/STUB — the primary threshold source is unbaselined; SKILL.md footnote states status explicitly but the underlying evidence base is provisional |
| Actionability | 0.15 | 0.90 | 0.135 | Field descriptions and validation rules are clear and machine-checkable; per-wave evidence tables are actionable; CI gate mapping is complete |
| Traceability | 0.10 | 0.83 | 0.083 | Source annotations present in all sections; ADR-PROJ022-002 path cited but ADR is STUB so chain is incomplete; output location traces cleanly to SKILL.md |
| **TOTAL** | **1.00** | | **0.893** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**
The template contains all structurally required sections: navigation table (H-23 compliant), the full copy-paste template block, Field Descriptions table (all 13 fields defined), Per-Wave Customization (all 5 waves specified), and Validation Rules (13 CI checks listed). The per-wave tables precisely map to wave-progression.md Wave Definitions table for Waves 1-5.

The footer traceability block (lines 185-192) lists parent skill, sibling templates, and consuming rule files — a useful completeness feature not found in many templates.

**Gaps:**
1. The bypass section in the template body (lines 77-81) includes `| (none or list bypasses) | | | | | ACTIVE / RESOLVED |` as its only guidance. This is a placeholder that does not tell the operator what the columns (`Bypass ID`, `Sub-Skill`, `Unmet Criterion`, `Impact Assessment`, `Remediation Plan`, `Status`) should contain in the completed file. The Field Descriptions table does not include "Wave Bypass Usage" as a standalone row with description — it is listed as "Yes (even if empty)" but does not describe what a populated row requires. Cross-referencing wave-progression.md [Bypass Fields] reveals the three required fields (Unmet Criterion, Impact Assessment, Remediation Plan), but a user operating only from this template would not know this.
2. The template's Acceptance Criteria (line 75) references "AGENTS.md updated with Wave [N] agent entries" but no guidance is given in Field Descriptions on what this means or how to verify it. No CI gate (UX-CI-001 through UX-CI-013) validates AGENTS.md content.

**Improvement Path:**
- Expand Field Descriptions to include "Wave Bypass Usage" with a description linking explicitly to wave-progression.md [Bypass Fields].
- Add a note under "AGENTS.md updated" acceptance criterion explaining what entries are expected or pointing to the AGENTS.md registration requirement.

---

### Internal Consistency (0.94/1.00)

**Evidence:**
The 0.85 threshold appears consistently in the template body (line 39), Field Descriptions (implicitly via ci-checks.md reference), and Validation Rules (line 175). The distinction between the 0.85 wave-deployment-readiness threshold and H-13's 0.92 governance threshold and the C4 artifact quality gate of 0.95 is maintained consistently: the template states 0.85 for the wave quality gate composite score and separately specifies "C4 >= 0.95 quality gate" in the Acceptance Criteria (line 69), reflecting that sub-skill *artifact* quality is scored at C4 while the wave *gate* uses 0.85.

All wave names and numbers (1-5) are consistent across the template, Field Descriptions, Per-Wave Customization, and Validation Rules. Terminology ("PASS / FAIL", "DEPLOYED / FAILED", "YES / NO") is used consistently.

The comment on line 20 clarifies that Wave 0 uses KICKOFF-SIGNOFF.md, not this template — consistent with wave-progression.md [Signoff File Locations] and the sibling kickoff template.

**Gaps:**
The Validation Rules section (line 180) states: "No unresolved bypasses | All bypasses in table have status 'RESOLVED' (or table is empty)". However, the template body's bypass table shows a single row with `ACTIVE / RESOLVED` as status values. The Acceptance Criteria (line 74) says "Degraded-mode behavior verified for OPT MCP dependencies" — this acceptance criterion is not explicitly captured in the CI gates (UX-CI-001 through UX-CI-013). This is a minor tension, not a contradiction — the CI gates are a subset of checks, and the acceptance criteria are broader — but an operator might wonder why this criterion has no corresponding CI enforcement.

**Improvement Path:**
- Add a note in the Validation Rules section clarifying that acceptance criteria items without corresponding CI gates are human-verified rather than automated.

---

### Methodological Rigor (0.92/1.00)

**Evidence:**
The template follows a well-established peer structure: the `kickoff-signoff-template.md` sibling exists and is explicitly referenced. The Field Descriptions table uses "Required: Yes/No" which follows standard template specification practice. The Validation Rules section maps directly to CI gate IDs (UX-CI-007, UX-CI-008), grounding validation in executable checks rather than descriptive prose.

The version header (line 1) correctly cites source sections from SKILL.md, consistent with the pattern used by all other rule files in the skill. The output location (`skills/user-experience/output/WAVE-{N}-SIGNOFF.md`) is stated explicitly.

The Per-Wave Customization section mirrors the structure of wave-progression.md [Wave Transition Gates] Per-Transition Requirements table — an operator can cross-validate the evidence requirements between the two documents.

**Gaps:**
The Cross-Framework Synthesis Test section (lines 59-65) is the weakest structural element. It provides three rows:
- "Synthesis with Wave [N] sub-skills produces valid output" — no definition of "valid output"
- "Confidence classifications present in synthesis output" — minimal; covered by UX-CI-011 but no link provided
- "Handoff data contracts validated between Wave [N] sub-skills" — no definition of what "validated" means or what the handoff data contract structure is

For a template that a new operator must complete, these three rows are insufficiently specified. The synthesis-validation.md [Cross-Framework Synthesis Protocol] and [Synthesis Output Structure] sections define what "valid output" means, but this template does not reference those sections in the Cross-Framework Synthesis Test subsection. An operator completing Wave 1 signoff would not know that "produces valid output" means "CI gates UX-CI-011 through UX-CI-013 pass" or that "handoff data contracts validated" means something specific in synthesis-validation.md.

**Improvement Path:**
- Add a note below the Cross-Framework Synthesis Test table directing the operator to `synthesis-validation.md [Synthesis Output Structure]` for definition of "valid output".
- Add a note directing to `ci-checks.md [UX-CI-011, UX-CI-012, UX-CI-013]` for the automated verification that covers confidence classifications and traceability.
- Define "handoff data contracts validated" with a reference to synthesis-validation.md [Required Traceability] or the handoff schema.

---

### Evidence Quality (0.82/1.00)

**Evidence:**
The 0.85 threshold is attributed to `ADR-PROJ022-002-wave-criteria-gates.md` — this citation is honest (PROVISIONAL is stated in line 39 of the template and in the header comment on line 20). The SKILL.md is verified as a valid source document (confirmed by reading it). The S-014 6-dimension rubric citation to `.context/rules/quality-enforcement.md` is traceable (that file exists and defines the weights in its Quality Gate section).

**Gaps:**
The primary threshold source — ADR-PROJ022-002 — is confirmed by SKILL.md References section (line 598-599) to have status `[STUB: EPIC-001]`. The SKILL.md itself states the ADR is pending and the threshold "may be revised upward as calibration data from Wave 1 deployments becomes available." This means:

1. The central quantitative claim of this template (>= 0.85 threshold) rests on a STUB ADR. The threshold is not baselined.
2. The template acknowledges this with "PROVISIONAL" labels, which is correct per P-022 (no deception), but from a scoring perspective, citing a STUB ADR as a source reduces evidence quality.
3. No secondary or alternative evidence source is provided for the 0.85 threshold choice (e.g., comparative analysis of industry practice, derivation from H-13's 0.92 basis, or empirical justification). The SKILL.md footnote on threshold justification (line 283 of SKILL.md) offers a qualitative rationale ("deployment readiness vs governance artifact quality") but no quantitative derivation.

**Improvement Path:**
- The PROVISIONAL label correctly flags the uncertainty. To raise Evidence Quality, either: (a) baseline ADR-PROJ022-002 with formal C3 review before this template is finalized, or (b) add an alternative evidence source for the 0.85 threshold (e.g., reference to comparable frameworks' quality gate thresholds, or an explicit derivation argument in the template header comment).

---

### Actionability (0.90/1.00)

**Evidence:**
Field Descriptions table tells operators precisely what to put in each field: "ISO 8601 date of signoff", "Wave number (1-5)", "Non-empty string", "Engagement ID format UX-{NNNN}". The Validation Rules section (lines 161-182) maps each check to a machine-evaluable pass criterion — an operator can run through the checklist mechanically. Per-Wave Customization provides concrete, checkable evidence requirements: "at least 1 heuristic eval report exists at expected output path", "Storybook with 5+ Atom-level stories", "30+ users available for Kano survey".

The template body's placeholder text (`[score]`, `[evidence type per wave]`, `[test engagement ID or notes]`) is clear about what is expected, and the Field Descriptions disambiguate.

**Gaps:**
1. The Cross-Framework Synthesis Test table (noted under Methodological Rigor) also reduces actionability: "Handoff data contracts validated between Wave [N] sub-skills" gives no direction on *how* to validate. The "PASS / FAIL / N/A" structure is correct but the evaluation criteria are missing.
2. The Acceptance Criteria item "Degraded-mode behavior verified for OPT MCP dependencies" lacks a reference to how to verify this. No CI gate covers it (noted above). An operator must know to consult `mcp-coordination.md` for this criterion, but the template does not point there.

**Improvement Path:**
- In the Cross-Framework Synthesis Test table, add a "How to evaluate" column or a note below the table with specific pass criteria for each row.
- Add a note on the "Degraded-mode behavior" acceptance criterion pointing to `mcp-coordination.md [Degraded Mode Behavior]`.

---

### Traceability (0.83/1.00)

**Evidence:**
Every section of the template includes a `<!-- Source: ... -->` comment that cites the source document and section name. The template header (line 1) cites SKILL.md sections "Wave Architecture", "Wave Transition Quality Gates", "Wave Signoff Enforcement" — all three are verified sections in SKILL.md. Per-Wave Customization comments (line 116) trace to SKILL.md and wave-progression.md. Validation Rules comment (line 163) cites ci-checks.md [UX-CI-007, UX-CI-008] and ADR-PROJ022-002.

The footer block explicitly lists consuming files: `skills/user-experience/rules/ci-checks.md [UX-CI-007, UX-CI-008]` and `skills/user-experience/rules/wave-progression.md [Signoff Requirements]`. This is a strong traceability feature.

**Gaps:**
1. ADR-PROJ022-002 is cited as the threshold source but is a STUB — the traceability chain terminates at an unresolved stub. The path `docs/design/ADR-PROJ022-002-wave-criteria-gates.md` is cited but the file has STUB status per SKILL.md References. This is the most significant traceability gap.
2. The Cross-Framework Synthesis Test section (lines 59-65) cites no source comment. Given that this section derives from synthesis-validation.md [Cross-Framework Synthesis Protocol], the absence of a `<!-- Source: ... -->` comment breaks the traceability pattern established by all other sections. Confirmed by reading the full template — this subsection is the only one without a source annotation.
3. The Acceptance Criteria section (lines 67-76) also lacks a `<!-- Source: ... -->` comment. The checklist items derive from SKILL.md Sections "Wave Signoff Enforcement" and "P-003 Compliance", but this derivation is undocumented in the template.

**Improvement Path:**
- Add `<!-- Source: skills/user-experience/rules/synthesis-validation.md [Cross-Framework Synthesis Protocol], skills/user-experience/rules/ci-checks.md [UX-CI-011, UX-CI-012, UX-CI-013] -->` above the Cross-Framework Synthesis Test section.
- Add `<!-- Source: SKILL.md Sections "Wave Signoff Enforcement", "P-003 Compliance"; skills/user-experience/rules/ci-checks.md [CI Gate Summary] -->` above the Acceptance Criteria section.
- Accept that ADR-PROJ022-002 traceability gap can only be resolved by baselining the ADR.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.82 | 0.90 | Baseline ADR-PROJ022-002 with formal C3 review. Until baselined, add a derivation note in the template header comment explaining the 0.85 threshold rationale (qualitative + comparison to H-13 0.92 basis). This is a cross-cutting fix — it also improves Traceability. |
| 2 | Traceability | 0.83 | 0.92 | Add `<!-- Source: -->` comments above the Cross-Framework Synthesis Test section (cite synthesis-validation.md [Cross-Framework Synthesis Protocol] and ci-checks.md [UX-CI-011-013]) and the Acceptance Criteria section (cite SKILL.md [Wave Signoff Enforcement, P-003 Compliance] and ci-checks.md [CI Gate Summary]). |
| 3 | Methodological Rigor | 0.92 | 0.95 | Expand the Cross-Framework Synthesis Test table with evaluation criteria per row, or add a note below the table pointing to synthesis-validation.md [Synthesis Output Structure] for "valid output" definition and ci-checks.md [UX-CI-011-013] for confidence/traceability checks. |
| 4 | Completeness | 0.90 | 0.94 | (a) Expand Field Descriptions to include "Wave Bypass Usage" field description linking to wave-progression.md [Bypass Fields]. (b) Add clarification note on "AGENTS.md updated" acceptance criterion. |
| 5 | Actionability | 0.90 | 0.94 | (a) Add "how to evaluate" guidance in Cross-Framework Synthesis Test table. (b) Add reference to mcp-coordination.md [Degraded Mode Behavior] on the "Degraded-mode behavior" acceptance criterion. |
| 6 | Internal Consistency | 0.94 | 0.96 | Add a note in the Validation Rules section clarifying that acceptance criteria items without CI gate IDs are human-verified. This resolves the implicit tension between the full acceptance criteria list and the partial CI gate coverage. |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score
- [x] Uncertain scores resolved downward (Traceability 0.83 vs. temptation to score 0.88; Evidence Quality 0.82 vs. temptation to score 0.87 given honest PROVISIONAL labeling)
- [x] First-draft calibration considered (this is a v1.0.1 document — scored against polished-document standard, not first-draft)
- [x] No dimension scored above 0.95 without exceptional evidence

**Calibration notes:**
- Internal Consistency at 0.94 is intentionally near the top because the terminology and threshold consistency is genuinely strong — the three-way distinction (0.85 wave gate / 0.92 H-13 / 0.95 C4) is consistently maintained across the full document.
- Evidence Quality at 0.82 reflects the real structural gap: the primary quantitative source is a STUB ADR. The PROVISIONAL labeling is honest and correct (P-022 compliant), but honesty about a provisional source does not improve the underlying evidence quality — it only prevents the score from dropping further for deception.
- Traceability at 0.83 reflects two missing `<!-- Source: -->` comments in adjacent sections of the template body, plus the unresolved STUB ADR chain.

---

## Session Context Handoff Schema

```yaml
verdict: REVISE
composite_score: 0.893
threshold: 0.95
weakest_dimension: evidence_quality
weakest_score: 0.82
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Baseline ADR-PROJ022-002 with formal C3 review or add threshold derivation note to template header"
  - "Add Source comments above Cross-Framework Synthesis Test and Acceptance Criteria sections"
  - "Expand Cross-Framework Synthesis Test table with per-row evaluation criteria"
  - "Expand Field Descriptions to include Wave Bypass Usage field with link to wave-progression.md [Bypass Fields]"
  - "Add mcp-coordination.md reference on Degraded-mode behavior acceptance criterion"
  - "Add note in Validation Rules clarifying human-verified vs CI-gated acceptance criteria items"
```

---

*Score report: wave-signoff-template-score.md*
*Scoring agent: adv-scorer*
*Artifact version: 1.0.1 (2026-03-04)*
*Score date: 2026-03-04*
*SSOT: `.context/rules/quality-enforcement.md`*
