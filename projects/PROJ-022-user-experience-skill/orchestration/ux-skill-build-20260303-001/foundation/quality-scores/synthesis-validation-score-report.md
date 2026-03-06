# Quality Score Report: Synthesis Validation Rules

## L0 Executive Summary

**Score:** 0.799/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.72)

**One-line assessment:** The deliverable is methodologically sound and operationally usable, but falls well short of the C4 threshold (0.95) due to a missing sub-skill entry, an internal inconsistency in convergence-to-confidence mapping, absent cross-references to sibling rule files, and gaps in contradiction handling for n-way conflicts.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/synthesis-validation.md`
- **Deliverable Type:** Research (Foundation rule file)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold Applied:** 0.95 (C4 criticality — not 0.92 standard; user-specified)
- **Reference Spec:** `skills/user-experience/SKILL.md` (Synthesis Hypothesis Validation and Cross-Framework Synthesis Protocol sections)
- **Scored:** 2026-03-04T00:00:00Z
- **Strategy Findings Incorporated:** No

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.799 |
| **Threshold** | 0.95 (C4, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.82 | 0.164 | `/ux-atomic-design` absent from sub-skill synthesis map; failure modes partially covered |
| Internal Consistency | 0.20 | 0.80 | 0.160 | HIGH confidence assignment for 2-framework convergence contradicts Gate Definitions qualifier |
| Methodological Rigor | 0.20 | 0.83 | 0.166 | Sound 4-step protocol; gap in n-way contradiction handling and "same UX problem" operationalization |
| Evidence Quality | 0.15 | 0.72 | 0.108 | Source comments present on 5/7 sections; no cross-refs to wave-progression.md or mcp-coordination.md |
| Actionability | 0.15 | 0.84 | 0.126 | Operationally specific for standard cases; confidence override mechanism underspecified |
| Traceability | 0.10 | 0.75 | 0.075 | Navigation table compliant; missing VERSION header, no SKILL.md file path, ux-routing-rules ref incomplete |
| **TOTAL** | **1.00** | | **0.799** | |

---

## Detailed Dimension Analysis

### Completeness (0.82/1.00)

**Evidence:**

The deliverable covers the three required confidence levels (HIGH, MEDIUM, LOW) with gate definitions, enforcement mechanisms, and classification immutability rules that are substantively complete and detailed. The 4-step Cross-Framework Synthesis Protocol includes a trigger condition, per-step inputs/outputs/validation checks, and per-sub-skill Signal Extraction Criteria. Failure Mode Handling addresses the primary failure scenario (LOW > 50% majority) and documents a known scope limitation (v1.0.0 text-only synthesis).

**Gaps:**

1. **Missing sub-skill in Synthesis Output Map:** SKILL.md defines 10 sub-skills. The deliverable's Sub-Skill Synthesis Output Map contains entries for: `/ux-jtbd`, `/ux-lean-ux`, `/ux-design-sprint` (2 entries), `/ux-inclusive-design`, `/ux-kano-model` (2 entries), `/ux-behavior-design` (2 entries), `/ux-heart-metrics` (2 entries), `/ux-ai-first-design`. That is 9 of 10 sub-skills represented across 12 rows. **`/ux-atomic-design` (ux-atomic-architect, Wave 3) is absent entirely.** This is a concrete gap — the orchestrator has no default confidence guidance for atomic design synthesis steps (e.g., component taxonomy synthesis, design token recommendation synthesis).

2. **Failure modes incomplete:** The section covers only the "LOW > 50% majority" case and the "text-only mode" scope limitation. Missing: (a) handling when a sub-skill output is structurally malformed and cannot be parsed for signals in Step 1; (b) handling when only one sub-skill output exists at synthesis trigger time (trigger says "two or more" but what happens if one arrives late?).

**Improvement Path:**

Add a `/ux-atomic-design` row (or rows) to the Sub-Skill Synthesis Output Map with synthesis step descriptions and default confidence classification consistent with the methodology (component taxonomy synthesis is likely MEDIUM; design token recommendation without empirical usage data is likely LOW). Add 2 failure mode entries for malformed sub-skill output and late-arriving output scenarios.

---

### Internal Consistency (0.80/1.00)

**Evidence:**

The deliverable's Gate Definitions table accurately reflects SKILL.md's Confidence Gate Protocol table. The enforcement mechanism text for HIGH, MEDIUM, and LOW gates matches SKILL.md's "Gate Enforcement" section verbatim in substance. The Sub-Skill Synthesis Output Map aligns with SKILL.md's Sub-Skill Synthesis Output Map for all 11 shared entries (the deliverable adds a "Rationale" column and uses "Default Confidence" vs. SKILL.md's "Typical Confidence" — this enhancement is consistent in spirit). Classification immutability rules (HIGH may be downgraded, MEDIUM may not be upgraded, LOW is permanent) are internally self-consistent and do not contradict other sections.

**Gaps:**

1. **HIGH confidence inconsistency between Gate Definitions and Convergence Thresholds:** The Gate Definitions section states HIGH requires "3+ frameworks converge on the same finding, OR 2 frameworks converge with strong quantitative evidence." The Convergence Thresholds table assigns HIGH to "Moderate convergence: 2 frameworks identify the same UX problem" — without the qualifier "with strong quantitative evidence." These two rules are inconsistent: an orchestrator following the Convergence Thresholds table would assign HIGH for any 2-framework convergence, while the Gate Definitions would require quantitative evidence for 2-framework HIGH. The more restrictive Gate Definitions rule should govern, but the table contradicts it.

2. **CONTRA-ID format not reflected in Synthesis Output Structure:** The Contradiction Handling section introduces the `CONTRA-{NNN}` sequential identifier format. The Synthesis Output Structure section lists "Contradictions" as a required output section but does not reference CONTRA-IDs in its description of required content. An orchestrator reading the output structure section alone would not know to apply CONTRA-IDs.

**Improvement Path:**

Revise the Convergence Thresholds table to add the qualifier to "Moderate convergence" row: "2 frameworks identify the same UX problem **with strong quantitative evidence** — assign HIGH; without strong quantitative evidence — assign MEDIUM." Add a note in the Synthesis Output Structure Contradictions row referencing CONTRA-{NNN} format per the Contradiction Handling section.

---

### Methodological Rigor (0.83/1.00)

**Evidence:**

The confidence classification system is grounded in evidence convergence logic with clear thresholds. The 4-step sequential synthesis protocol (Signal Extraction → Convergence Detection → Contradiction Identification → Unified Output) is well-structured with distinct inputs, outputs, and validation checks per step. Signal Extraction Criteria per sub-skill type are specific and operationally clear (severity >= 2 for heuristic eval; metrics below target for HEART; unvalidated assumptions and invalidated hypotheses for Lean UX; etc.). The Convergence Matching Rules (same screen/flow, same user problem, same metric impact, partial overlap) provide operational criteria. Contradiction types (direct opposition, priority conflict, methodology conflict) with distinct confidence assignments are methodologically sound.

**Gaps:**

1. **N-way contradiction handling undefined:** Step 3 validation states "Every contradiction has exactly 2 opposing positions; no resolution is attempted." This rule implicitly assumes binary contradiction only. When 3+ frameworks produce conflicting signals (e.g., Framework A recommends simplification, Framework B recommends feature addition, Framework C is neutral), the protocol provides no guidance. The two-position structure of the CONTRA-ID format cannot accommodate a 3-way conflict.

2. **"Same user problem" lacks operational definition:** Convergence Rule 2 states "Signals that describe the same user-facing problem (even using different vocabulary) are convergent." This is the most subjectively applied rule — determining whether HEART's "low task success for checkout" is the "same user problem" as JTBD's "friction in the progress job" requires judgment. No operationalization criteria are provided (e.g., minimum overlap dimension requirements, example application, or required evidence for claiming equivalence). An orchestrator making this call inconsistently would produce unreliable convergence groupings.

3. **Confidence override mechanism underspecified:** The Sub-Skill Synthesis Output Map notes "actual confidence may differ based on evidence quality in each engagement" but provides no criteria or decision procedure for when/how an orchestrator overrides a default. This gap interacts with the HIGH/2-frameworks inconsistency noted under Internal Consistency.

**Improvement Path:**

Add a sub-section "N-way Conflict Resolution" specifying that when 3+ frameworks conflict, each pair of opposing positions is documented as a separate CONTRA entry with a cross-reference between related CONTRAs, OR convert to a single CONTRA with Position A, Position B, Position C fields. Add 2-3 worked examples of "same user problem" equivalence determination to Convergence Rule 2. Add a confidence override table with criteria (e.g., "upgrade from MEDIUM to HIGH when: N data points available, methodology X applied, evidence type Y present").

---

### Evidence Quality (0.72/1.00)

**Evidence:**

Source comments citing SKILL.md sections appear on 5 of the 7 content sections: Confidence Classification (`<!-- Source: SKILL.md Section "Synthesis Hypothesis Validation" -->`), Sub-Skill Synthesis Output Map (`<!-- Source: SKILL.md Section "Synthesis Hypothesis Validation" -->`), Cross-Framework Synthesis Protocol (`<!-- Source: SKILL.md Section "Cross-Framework Synthesis Protocol" -->`), Convergence Thresholds (`<!-- Source: SKILL.md Section "Cross-Framework Synthesis Protocol" -->`), Contradiction Handling (`<!-- Source: SKILL.md Section "Cross-Framework Synthesis Protocol" -->`). The Rationale column in the Sub-Skill map provides evidence-based justifications for confidence defaults (e.g., "Secondary research lacks direct user observation" for `/ux-jtbd`).

**Gaps:**

1. **No source comment on Synthesis Output Structure section:** The section defines required output sections and required traceability fields. No source comment indicates whether this derives from SKILL.md or is new content introduced in this rule file.

2. **No source comment on Failure Mode Handling section:** The failure mode behavior ("LOW > 50% majority" banner) is referenced in SKILL.md — a source comment would confirm alignment.

3. **No cross-reference to `wave-progression.md`:** The evaluation criteria specify cross-references to wave-progression.md. Wave-progression is not referenced anywhere in the deliverable despite the fact that synthesis confidence may be affected by wave deployment state (sub-skills not yet deployed cannot contribute convergence signals).

4. **No cross-reference to `mcp-coordination.md`:** The evaluation criteria specify cross-references to mcp-coordination.md. This rule file governs MCP availability which affects whether synthesis inputs contain MCP-enhanced data (Figma-informed findings vs. text-only findings) — a distinction that could affect confidence classification.

5. **"5 users per Sprint methodology" is unattributed:** The Sub-Skill map entry for `/ux-design-sprint` Day 4 interview thematic analysis justifies HIGH confidence with "Based on direct user interviews (5 users per Sprint methodology)" — the "5 users" figure is a specific methodological claim from the GV Sprint Book that should be cited.

**Improvement Path:**

Add source comments to Synthesis Output Structure and Failure Mode Handling. Add a cross-reference to `wave-progression.md` in the synthesis trigger section (noting that synthesis operates only on deployed sub-skill outputs). Add a cross-reference to `mcp-coordination.md` noting that MCP-enhanced vs. text-only inputs may affect evidence strength assessment. Add citation for the "5 users per Sprint methodology" claim.

---

### Actionability (0.84/1.00)

**Evidence:**

The gate definitions, enforcement mechanisms, and advancement rules are operationally specific enough for an orchestrator to apply without ambiguity in standard cases. The CONTRA-{NNN} identifier format, required fields (Position A, Position B, Resolution, Confidence), and "user decision required" resolution approach provide clear output formatting. Signal extraction thresholds per sub-skill type (severity >= 2, metrics below target, assumption status) are actionable classification criteria. The output path `skills/user-experience/output/{engagement-id}/ux-orchestrator-synthesis.md` is fully specified.

**Gaps:**

1. **Confidence override mechanism absent:** The orchestrator is told defaults "may differ based on evidence quality" but is given no decision procedure for applying an override. A rule file that says "defaults may vary" without specifying how provides uncertain operational guidance.

2. **Sub-skill output format assumed:** Step 1 assumes sub-skill outputs have a "findings/recommendations sections" structure. If a sub-skill output uses different section naming or structure, the signal extraction step has no fallback. The rule file should either reference the canonical output template or specify a structural fallback.

3. **Synthesis trigger timing unspecified:** The trigger condition ("two or more sub-skill outputs exist for the same engagement ID") does not specify when synthesis executes — immediately after the second output arrives, after all expected sub-skills complete, or on user request. For an orchestrator running sub-skills sequentially vs. in parallel, this distinction matters for intermediate-state management.

**Improvement Path:**

Add a "Confidence Override Criteria" sub-section with explicit conditions for upgrading or downgrading from default. Add a note in Step 1 specifying "If a sub-skill output does not contain a findings/recommendations section, log a warning and exclude that output from convergence analysis." Specify synthesis trigger timing: "Synthesis executes after all sub-skill invocations for the engagement are complete, not incrementally after each sub-skill output."

---

### Traceability (0.75/1.00)

**Evidence:**

The navigation table is present with anchor links for all 7 sections — compliant with H-23/H-24. Source comments on 5 of 7 sections link to SKILL.md section names. The footer includes parent skill reference (`/user-experience`), creation date, update date, and status. The Classification Immutability section references `ux-routing-rules.md` by name.

**Gaps:**

1. **No VERSION header comment:** Other rule files in the Jerry framework include `<!-- VERSION: X.Y.Z | DATE: ... | SOURCE: ... -->` headers. This file has no VERSION header, making it difficult to track version evolution and identify when it was last substantively revised.

2. **SKILL.md referenced by section name only, not by file path:** Source comments say `<!-- Source: SKILL.md Section "..." -->` but do not include the full repo-relative path `skills/user-experience/SKILL.md`. If the file moves or is referenced from a different directory, the source comment provides insufficient traceability.

3. **`ux-routing-rules.md` cross-reference lacks file path:** The Classification Immutability section references `ux-routing-rules.md [Cross-Sub-Skill Handoff]` without a repo-relative path. This is inconsistent with the Jerry framework convention of using full paths in rule files.

4. **No cross-references to `wave-progression.md` or `mcp-coordination.md`:** As noted under Evidence Quality — these sibling rule files are relevant to synthesis behavior and should be referenced for traceability.

5. **Synthesis Output Structure lacks source traceability:** The section introduces the required output sections and traceability fields without a source comment — it is unclear whether these requirements derive from SKILL.md or are new constraints introduced in this rule file.

**Improvement Path:**

Add a VERSION header comment (`<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/SKILL.md#synthesis-hypothesis-validation | STATUS: COMPLETE -->`). Update all source comments to use full repo-relative path. Update `ux-routing-rules.md` reference to include the full path `skills/user-experience/rules/ux-routing-rules.md`. Add cross-references to `wave-progression.md` and `mcp-coordination.md`.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.80 | 0.92 | Reconcile HIGH confidence criteria between Gate Definitions (requires "strong quantitative evidence" for 2-framework convergence) and Convergence Thresholds table (assigns HIGH to all 2-framework convergence). Add the qualifier to the "Moderate convergence" row, or revise the Gate Definition to match the table. |
| 2 | Completeness | 0.82 | 0.93 | Add `/ux-atomic-design` (ux-atomic-architect) entry to Sub-Skill Synthesis Output Map with synthesis step, default confidence, and rationale. Recommended: component taxonomy synthesis = MEDIUM (heuristic model); design token recommendation = LOW (requires empirical usage data). |
| 3 | Methodological Rigor | 0.83 | 0.92 | Add "N-way Conflict Resolution" procedure for 3+ framework conflicts. Add operationalization criteria for "same user problem" equivalence in Convergence Rule 2 with worked examples. Add a confidence override decision procedure (criteria for departing from default confidence). |
| 4 | Evidence Quality | 0.72 | 0.88 | Add source comments to Synthesis Output Structure and Failure Mode Handling sections. Add cross-references to `skills/user-experience/rules/wave-progression.md` and `skills/user-experience/rules/mcp-coordination.md`. Add citation for "5 users per Sprint methodology" claim. |
| 5 | Traceability | 0.75 | 0.88 | Add VERSION header. Update source comments to include full repo-relative file path. Update `ux-routing-rules.md` reference to include full path. |
| 6 | Actionability | 0.84 | 0.92 | Specify synthesis trigger timing (after all sub-skills complete, not incrementally). Add Step 1 fallback for malformed sub-skill output. Add confidence override criteria sub-section. |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score — specific quotes and section references used throughout
- [x] Uncertain scores resolved downward — Convergence Thresholds HIGH inconsistency was scored as Internal Consistency 0.80 (not rounded up to 0.85)
- [x] First-draft calibration considered — the deliverable is a first-draft Foundation rule file; composite of 0.799 is consistent with the typical 0.65-0.80 range for well-executed first drafts
- [x] No dimension scored above 0.95 — highest is Actionability at 0.84
- [x] C4 threshold of 0.95 applied — this is significantly higher than the standard H-13 0.92 threshold; the deliverable does not approach this bar

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.799
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.72
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Reconcile HIGH confidence criteria: Gate Definitions vs. Convergence Thresholds table (2-framework convergence qualifier)"
  - "Add /ux-atomic-design entry to Sub-Skill Synthesis Output Map (missing 1 of 10 sub-skills)"
  - "Add N-way conflict resolution procedure for 3+ framework contradictions"
  - "Operationalize 'same user problem' equivalence criteria in Convergence Rule 2"
  - "Add source comments to Synthesis Output Structure and Failure Mode Handling sections"
  - "Add cross-references to wave-progression.md and mcp-coordination.md"
  - "Add VERSION header comment with full repo-relative source path"
  - "Specify synthesis trigger timing (after all sub-skills complete)"
  - "Add confidence override decision procedure with explicit criteria"
```

---

*Score report generated by adv-scorer*
*Deliverable: skills/user-experience/rules/synthesis-validation.md*
*Reference spec: skills/user-experience/SKILL.md*
*Scoring strategy: S-014 LLM-as-Judge | SSOT: .context/rules/quality-enforcement.md*
*Report path: skills/user-experience/reviews/synthesis-validation-score-report.md*
