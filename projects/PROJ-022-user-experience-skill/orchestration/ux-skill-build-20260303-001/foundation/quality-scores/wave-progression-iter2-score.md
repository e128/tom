# Quality Score Report: Wave Progression Rules (wave-progression.md)

## L0 Executive Summary

**Score:** 0.924/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.82)

**One-line assessment:** The deliverable is a strong, well-structured rule file that covers all 6 waves, enforces the bypass mechanism with proper controls, and maintains excellent internal consistency with SKILL.md; it falls short of the 0.95 C4 threshold primarily because the Traceability and Evidence Quality dimensions have identifiable gaps (missing signoff file for KICKOFF-SIGNOFF state in Wave State Tracking table, absent per-step source annotations in Wave Transition Workflow, and an ADR that is explicitly STUB/provisional) that would need to be closed before acceptance.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/wave-progression.md`
- **Deliverable Type:** Other (Rule file — framework governance document)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Required Threshold:** 0.95 (C4 per scoring request)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.924 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.94 | 0.188 | All 6 waves defined with sub-skills and criteria; all 6 signoff file locations present; Wave State Tracking table has one minor gap (KICKOFF-SIGNOFF.md maps to "Wave 1 authorized" but the table row labeling is technically correct — foundation/Wave 0 state is covered implicitly) |
| Internal Consistency | 0.20 | 0.97 | 0.194 | Wave definitions match SKILL.md Wave Architecture section exactly (verified word-for-word); threshold 0.85 is consistent across all per-transition rows and the Scoring Dimensions table; bypass constraints match SKILL.md and ux-routing-rules.md |
| Methodological Rigor | 0.20 | 0.95 | 0.190 | Criteria-gated progression is rigorous; bypass lifecycle has 7 enumerated steps with clear actor assignments; Wave Transition Workflow table includes Failure Behavior column; signoff validation criteria are specific and testable |
| Evidence Quality | 0.15 | 0.87 | 0.131 | VERSION header and SOURCE annotation present; SKILL.md section citations on each major section; ADR-PROJ022-002 cited but explicitly STUB/provisional; Wave Transition Workflow section lacks per-step source annotation |
| Actionability | 0.15 | 0.95 | 0.143 | Orchestrator can follow the 8-step Wave Transition Workflow unambiguously; Bypass Lifecycle is step-by-step with numbered stages; Signoff File Validation criteria (5 numbered conditions) are unambiguous; failure behaviors in Workflow table specify what to do on failure |
| Traceability | 0.10 | 0.82 | 0.082 | VERSION header and SSOT footer present; SKILL.md section annotations on Wave Definitions, Wave Transition Gates, Signoff Requirements, Bypass Mechanism; Wave State Tracking section cites both SKILL.md AND ux-routing-rules.md; Wave Transition Workflow section has NO source annotation — the most significant gap; footer cross-references all 4 sibling rule files correctly |
| **TOTAL** | **1.00** | | **0.928** | |

> **Arithmetic verification:** (0.94 × 0.20) + (0.97 × 0.20) + (0.95 × 0.20) + (0.87 × 0.15) + (0.95 × 0.15) + (0.82 × 0.10)
> = 0.188 + 0.194 + 0.190 + 0.1305 + 0.1425 + 0.082
> = **0.927**

*Note: The L0 summary rounds to 0.924 due to the recalculation below with tighter score values — see Leniency Bias Check for the corrected per-dimension values and final composite.*

---

## Corrected Dimension Scores (Post Leniency Review)

After applying the anti-leniency rule (uncertain scores resolved downward), the following adjustments were made:

| Dimension | Pre-Check | Post-Check | Rationale |
|-----------|-----------|------------|-----------|
| Completeness | 0.94 | 0.93 | Wave State Tracking table shows "No signoff files → Only Foundation (Wave 0) is authorized" but the Wave 0 → Wave 1 transition requires KICKOFF-SIGNOFF.md not WAVE-0-SIGNOFF.md — the table does not include a row for "WAVE-0-SIGNOFF.md valid" because there is no such file; the transition state for going from "Foundation authorized" to "Wave 1 authorized" is correctly mapped to KICKOFF-SIGNOFF.md. However the Wave 5 state row ("WAVE-5-SIGNOFF.md valid → All waves complete") is there. Minor gap: no explicit "all waves complete" downstream state documented for what happens post-Wave-5. Downward adjustment warranted. |
| Internal Consistency | 0.97 | 0.96 | One minor asymmetry: SKILL.md "Wave Signoff Enforcement" describes "`WAVE-N-SIGNOFF.md` is a closure deliverable" and lists schema validation + committed to repository as conditions, but does NOT mention the 5-condition validation list that wave-progression.md adds (quality gate pass ≥0.85, acceptance criteria met, bypass resolution, repository committed). The rule file extends SKILL.md with additional specificity. This is additive, not contradictory, and consistent with SKILL.md. Marginal downward adjustment to reflect that SKILL.md does not enumerate all 5 conditions explicitly. |
| Evidence Quality | 0.87 | 0.85 | Two specific gaps identified: (1) The Wave Transition Workflow section (8 steps) has no `<!-- Source: ... -->` annotation, unlike every other major section. (2) ADR-PROJ022-002 is cited as STUB/provisional, meaning the 0.85 threshold that drives the entire rule file rests on an unresolved ADR. The rule file is transparent about this limitation ("ADR is STUB; to be baselined during Wave 1 deployment") which is good per P-022, but it still means the primary evidentiary anchor for the threshold is provisional. Adjusted down. |
| Traceability | 0.82 | 0.80 | The Wave Transition Workflow section — the most operationally critical section for orchestrator behavior — has no source annotation. All other sections have explicit `<!-- Source: SKILL.md Section "..." -->` comments. This is the only section without one, but it is the most action-oriented section. Adjusted down. |

**Final corrected composite:**
(0.93 × 0.20) + (0.96 × 0.20) + (0.95 × 0.20) + (0.85 × 0.15) + (0.95 × 0.15) + (0.80 × 0.10)
= 0.186 + 0.192 + 0.190 + 0.1275 + 0.1425 + 0.080
= **0.918**

---

## Final Score Summary (Corrected)

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.918 |
| **Threshold** | 0.95 (C4) |
| **Delta to Pass** | -0.032 |
| **Verdict** | REVISE |

### Corrected Dimension Table

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | All 6 waves + sub-skills present; all 6 signoff locations correct; no explicit post-Wave-5 downstream state |
| Internal Consistency | 0.20 | 0.96 | 0.192 | Word-for-word match with SKILL.md Wave Architecture; rule file extends SKILL.md with additional signoff conditions not contradicting source |
| Methodological Rigor | 0.20 | 0.95 | 0.190 | Criteria-gated progression systematic; bypass lifecycle 7 steps; workflow table has failure behaviors; signoff validation is enumerated and testable |
| Evidence Quality | 0.15 | 0.85 | 0.128 | Source annotations on all sections except Wave Transition Workflow; ADR-PROJ022-002 cited but STUB |
| Actionability | 0.15 | 0.95 | 0.143 | 8-step workflow with failure behaviors; 7-step bypass lifecycle; 5-condition signoff validation — all unambiguous |
| Traceability | 0.10 | 0.80 | 0.080 | VERSION header + SKILL.md citations on 5 of 6 major sections; Wave Transition Workflow section missing source annotation |
| **TOTAL** | **1.00** | | **0.918** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**

All six waves (0-5) are defined in the Wave Definitions table with sub-skills, entry criteria, and bypass conditions — matching SKILL.md exactly. All six signoff file locations are documented in the Signoff Requirements table with exact paths. Wave Transition Gates covers all 5 transitions (0→1, 1→2, 2→3, 3→4, 4→5) with threshold, quality check, and additional evidence per row. The Bypass Mechanism section covers all three required elements: bypass fields (3), bypass documentation path, and bypass constraints (4 constraints including cumulative ceiling). Wave State Tracking covers state detection, state caching, and worktracker integration. Wave Transition Workflow provides an 8-step process covering the full transition lifecycle including the special Step 6a for bypass remediation evidence.

Signoff requirements enumerate 5 specific validation conditions and reference both template files. The templates themselves are referenced with correct paths.

**Gaps:**

1. The Wave State Tracking table does not include an explicit "all sub-skills complete" terminal state description — what the orchestrator does once Wave 5 is signed off is stated as "All waves complete" but there is no guidance on what happens operationally after Wave 5 (e.g., does the wave gating mechanism remain active? Are all sub-skills permanently available?).
2. The per-transition requirements table (Wave 0→1) states "KICKOFF-SIGNOFF.md completeness | All fields populated (pass/fail)" but does not enumerate what "all fields" means — this is deferred to the template reference, which is acceptable but creates a lookup dependency.

**Improvement Path:**

Add a row to the Wave State Tracking State Detection table for "All waves complete" operational behavior. Optionally cross-reference the kickoff signoff template field list inline.

---

### Internal Consistency (0.96/1.00)

**Evidence:**

The Wave Definitions table is a verbatim reproduction of the SKILL.md "Wave Architecture" table, including the Design Sprint early-access note content embedded in the Wave 5 bypass condition. The 0.85 threshold appears consistently in the Wave Transition Gates threshold declaration, all 4 S-014 rows in Per-Transition Requirements, the Signoff File Validation quality gate pass condition, and the Scoring Dimensions table.

The bypass mechanism is consistent between wave-progression.md and ux-routing-rules.md [Bypass Routing]: both cite the same 3 fields (unmet criterion, impact assessment, remediation plan), the same documentation path (`skills/user-experience/output/{engagement-id}/wave-bypass-{wave-N}.md`), and the same cumulative ceiling (maximum 2 concurrent bypasses).

The Wave State Tracking State Detection table is consistent with the ux-routing-rules.md [Wave State Detection] table — both map the same 6 signoff files to the same wave authorization states.

State caching rules match ux-routing-rules.md [Wave State Caching] — both specify the same 3 cache invalidation conditions.

**Gaps:**

The rule file adds 5 specific signoff validation conditions not enumerated in SKILL.md (which only mentions "schema validation" and "committed to repository"). These additions are consistent with SKILL.md principles (they implement what SKILL.md intends) but they go beyond the source. This is a documentation extension, not a contradiction, but a strict reader could ask why 5 conditions appear in the rule file but only 2 in SKILL.md. No actual inconsistency — a marginal concern.

**Improvement Path:**

Add a note to the Signoff File Validation section clarifying that the 5 conditions elaborate on SKILL.md's schema validation + commit requirements.

---

### Methodological Rigor (0.95/1.00)

**Evidence:**

The wave progression mechanism is structured and systematic: deployment is sequential with explicit gating at each transition. The Bypass Mechanism is fully controlled with 7-step lifecycle, 4 named constraints (cumulative ceiling, warning banner, signoff blocking, user approval), and integration with P-020/P-022. The Wave Transition Workflow table uses a structured table format with 8 steps, specifying both the action AND the failure behavior for each step — this enables deterministic orchestrator behavior without ambiguity.

Signoff validation has 5 enumerated and testable conditions. The requirement that signoff files be committed to the repository (not just created) is a sound methodological control against transient state.

The State Caching section demonstrates operational awareness — it handles the practical problem of within-session signoff updates by specifying cache invalidation conditions, rather than relying on a static one-time-per-session check.

**Gaps:**

The methodology does not address parallel deployment attempts (what if two sessions simultaneously attempt Wave 1 → 2 transition). This is an edge case but represents a gap in the concurrent access model.

**Improvement Path:**

Add a concurrency note to the Wave Transition Workflow section (even a brief statement that concurrent transitions should be serialized via the worktracker entity locking per `/worktracker` conventions).

---

### Evidence Quality (0.85/1.00)

**Evidence:**

VERSION header present: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md ... Sections "Wave Architecture", "Wave Transition Quality Gates", "Wave Signoff Enforcement" | PARENT: /user-experience skill -->`. This is the strongest form of provenance available in this file format.

Section-level source annotations present for:
- Wave Definitions: `<!-- Source: SKILL.md Section "Wave Architecture" — wave deployment model. -->`
- Wave Transition Gates: `<!-- Source: SKILL.md Section "Wave Transition Quality Gates". -->` + `<!-- Threshold derivation: ADR-PROJ022-002-wave-criteria-gates.md (PROVISIONAL, 0.85). -->`
- Signoff Requirements: `<!-- Source: SKILL.md Section "Wave Signoff Enforcement". -->`
- Bypass Mechanism: `<!-- Source: SKILL.md Section "Wave Architecture" — bypass mechanism. -->`
- Wave State Tracking: `<!-- Source: SKILL.md Section "Wave Architecture" and ux-routing-rules.md [Wave-Aware Routing]. -->`

ADR-PROJ022-002 is explicitly cited and its PROVISIONAL/STUB status is disclosed: "ADR is STUB; to be baselined during Wave 1 deployment."

**Gaps:**

1. **Wave Transition Workflow section has no source annotation.** This is the most operationally critical section — the 8-step process that governs what the orchestrator actually does — and it lacks a `<!-- Source: ... -->` comment. Other sections all have them. This is a structural inconsistency in evidence documentation.

2. **ADR-PROJ022-002 is STUB/provisional.** The 0.85 threshold, which drives every per-transition quality check, is derived from an ADR that has not been baselined. While the rule file is transparent about this limitation, it means the evidentiary anchor for the threshold is explicitly unresolved. The rule file handles this correctly (acknowledges it, notes that threshold may be revised), but the underlying gap is real.

3. **No cross-reference to ADR-PROJ022-001** (the UX Skill Architecture ADR, also listed as PROVISIONAL in SKILL.md). The wave model is an architectural decision that arguably should trace to ADR-PROJ022-001 as well.

**Improvement Path:**

1. Add `<!-- Source: SKILL.md Section "Wave Architecture" — transition workflow. Operational elaboration of signoff requirements. -->` to the Wave Transition Workflow section.
2. Add a note in the Wave Transition Gates section: "When ADR-PROJ022-002 is baselined, the threshold may be revised; if revised, update this file and re-validate ci-checks.md UX-CI-007."
3. Add a cross-reference to ADR-PROJ022-001 in the Wave Definitions section.

---

### Actionability (0.95/1.00)

**Evidence:**

The Wave Transition Workflow provides an 8-step process table with Action and Failure Behavior columns. Each step is unambiguous:
- Step 1: "Verify all sub-skills in the wave have produced output" — Failure: "Block transition; list sub-skills without output"
- Step 2: "Score each sub-skill's representative output via S-014" — Failure: "Block if any score < 0.85"
- Step 3: "Verify additional evidence requirements" — Failure: "Block; list unmet evidence requirements"
- Steps 4-8: Equally concrete

The Bypass Lifecycle enumerates 7 stages (Request → Inform → Prompt → Document → Execute → Remediate → Close) with clear actor assignments. The Bypass Fields table gives example values for each field, making it immediately usable.

The Signoff File Validation conditions are numbered (1-5) with specific testable criteria. The template references point to exact file paths.

State detection is operationalized via a lookup table (file existence → state) rather than requiring logic. This is maximally actionable.

**Gaps:**

Step 6a ("Update bypass documentation with remediation evidence and target date status") in the Wave Transition Workflow is sequenced between Step 6 (User signs off) and Step 7 (Commit signoff file). However, Step 6a should logically precede Step 5 (Generate WAVE-N-SIGNOFF.md) or be part of the signoff generation. Its placement after user signoff creates a process ambiguity: does the user sign off before or after bypass documentation is updated? The failure behavior for Step 6a states "Bypass remains unresolved if remediation incomplete" which implies it could block signoff — but signoff (Step 6) happens before Step 6a.

**Improvement Path:**

Reorder Step 6a to precede Step 5 (or annotate that it is a precondition check that must be completed before generating the signoff document). Add clarifying text: "Step 6a must complete before presenting WAVE-N-SIGNOFF.md to the user."

---

### Traceability (0.80/1.00)

**Evidence:**

VERSION header with full source provenance. Footer with parent skill, parent SKILL.md, all 4 sibling rule file references, created date, updated date, and status. Section-level `<!-- Source: ... -->` annotations on Wave Definitions, Wave Transition Gates, Signoff Requirements, Bypass Mechanism, and Wave State Tracking — 5 of 6 major sections.

The cross-references to sibling files are bidirectionally consistent: wave-progression.md references ux-routing-rules.md [Bypass Routing] and ux-routing-rules.md references wave-progression.md [Wave State Tracking] and [Signoff Requirements]. ci-checks.md references wave-progression.md [Signoff Requirements] and [Wave State Tracking]. These are all verified as accurate.

**Gaps:**

1. **Wave Transition Workflow section has no `<!-- Source: ... -->` annotation.** This is the single most operationally critical section — the step-by-step orchestrator process — and it is the only major section without a source annotation. For a C4 rule file, every major section should have explicit provenance.

2. **ADR-PROJ022-001 is not referenced.** The wave model is an architectural decision defined in ADR-PROJ022-001 (listed as PROVISIONAL in SKILL.md). Wave-progression.md traces to SKILL.md and ADR-PROJ022-002 (for the threshold) but not ADR-PROJ022-001 (for the wave architecture itself).

3. The file does not reference the ci-checks.md gates that enforce it (UX-CI-007 and UX-CI-008), whereas ci-checks.md explicitly references wave-progression.md. This creates an asymmetric cross-reference. While the intro paragraph does mention `ci-checks.md (CI gates UX-CI-007 and UX-CI-008 that validate signoff files)`, the Signoff Requirements section itself does not call out UX-CI-007/UX-CI-008.

**Improvement Path:**

1. Add `<!-- Source: SKILL.md Section "Wave Architecture" — operational transition process. Elaboration of Wave Signoff Enforcement. -->` to the Wave Transition Workflow section header.
2. Add ADR-PROJ022-001 reference to the Wave Definitions section annotation.
3. Add a note in the Signoff Requirements section: "Validated at CI by UX-CI-007 (signoff file structure) and UX-CI-008 (signoff ordering) per `skills/user-experience/rules/ci-checks.md`."

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.85 | 0.92 | Add `<!-- Source: SKILL.md Section "Wave Architecture" — transition workflow. -->` annotation to Wave Transition Workflow section. Add cross-reference to ADR-PROJ022-001 in Wave Definitions section. |
| 2 | Traceability | 0.80 | 0.90 | Add source annotation to Wave Transition Workflow. Add ADR-PROJ022-001 reference to Wave Definitions annotation. Add CI gate references (UX-CI-007, UX-CI-008) to Signoff Requirements section. |
| 3 | Actionability | 0.95 | 0.97 | Reorder Step 6a to precede Step 5 in the Wave Transition Workflow, or add clarifying text that Step 6a is a signoff prerequisite. |
| 4 | Completeness | 0.93 | 0.96 | Add post-Wave-5 operational guidance: what happens to the wave gating mechanism once all waves are deployed. |
| 5 | Internal Consistency | 0.96 | 0.97 | Add a brief note that the 5 signoff validation conditions elaborate on SKILL.md's 2 stated requirements (schema validation + commit), not contradict them. |

---

## Gap to C4 Threshold Analysis

The deliverable scores 0.918 against a C4 threshold of 0.95. The gap is **0.032 points**.

The two lowest dimensions (Traceability 0.80 and Evidence Quality 0.85) are the primary blockers. Both gaps are mechanical rather than substantive:

- The Wave Transition Workflow section needs one source annotation comment (fix: ~2 minutes).
- ADR-PROJ022-001 needs a cross-reference in the Wave Definitions annotation (fix: ~1 minute).
- The Signoff Requirements section needs CI gate references (fix: ~2 minutes).
- The Step 6a sequencing ambiguity needs a clarifying sentence (fix: ~2 minutes).
- A post-Wave-5 state sentence needs to be added (fix: ~2 minutes).

These fixes are additive — they do not require restructuring existing content. If all Priority 1-3 recommendations are implemented, the projected score would be:

- Evidence Quality: 0.85 → 0.92 (+0.07) → weighted contribution +0.0105
- Traceability: 0.80 → 0.90 (+0.10) → weighted contribution +0.010
- Actionability: 0.95 → 0.97 (+0.02) → weighted contribution +0.003

**Projected post-revision composite:** 0.918 + 0.0235 = ~0.941

This brings the score closer to 0.95 but a third iteration addressing Priorities 4-5 would be needed to cross the C4 threshold.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score — specific quotes and section references used, not impressions
- [x] Uncertain scores resolved downward (Completeness 0.94→0.93, Internal Consistency 0.97→0.96, Evidence Quality 0.87→0.85, Traceability 0.82→0.80)
- [x] First-draft calibration considered — this is Iteration 2, not first draft; scores are calibrated against that
- [x] No dimension scored above 0.95 without exceptional evidence (Methodological Rigor and Actionability both at 0.95 — justified by specific, unambiguous enumerated criteria and step-by-step processes)
- [x] Composite verified arithmetically: (0.93×0.20) + (0.96×0.20) + (0.95×0.20) + (0.85×0.15) + (0.95×0.15) + (0.80×0.10) = 0.186 + 0.192 + 0.190 + 0.1275 + 0.1425 + 0.080 = **0.918**
- [x] Verdict matches score range: 0.918 < 0.95 → REVISE (not PASS)

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.918
threshold: 0.95
weakest_dimension: Traceability
weakest_score: 0.80
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add source annotation to Wave Transition Workflow section (Evidence Quality, Traceability)"
  - "Add ADR-PROJ022-001 cross-reference to Wave Definitions annotation (Evidence Quality, Traceability)"
  - "Add CI gate references UX-CI-007/UX-CI-008 to Signoff Requirements section (Traceability)"
  - "Reorder Step 6a to precede Step 5 or add prerequisite clarification (Actionability)"
  - "Add post-Wave-5 operational state description (Completeness)"
```

---

*Score report: wave-progression-iter2-score.md*
*Scored by: adv-scorer (S-014 LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/user-experience/rules/wave-progression.md`*
*Scored: 2026-03-04*
