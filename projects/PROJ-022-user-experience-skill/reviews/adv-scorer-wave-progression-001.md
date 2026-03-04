# Quality Score Report: wave-progression.md

## L0 Executive Summary
**Score:** 0.841/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.78)
**One-line assessment:** The wave progression model is structurally sound and operationally actionable, but a missing Wave 5 signoff entry, a provisional ADR cited as a full derivation, and a Signoff File Locations table that omits Wave 5 keep this below the 0.92 H-13 threshold (and well below the 0.95 C4 threshold used for this scoring request).

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/wave-progression.md`
- **Deliverable Type:** Rule file (Foundation layer, /user-experience skill)
- **Criticality Level:** C4 (governance rule file, AE-002 applies: `.context/rules/` equivalent for skill rules)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold Applied:** 0.92 (H-13 standard) / 0.95 (C4 threshold as requested)
- **Scored:** 2026-03-04T00:00:00Z
- **Reference Spec Read:** `skills/user-experience/SKILL.md` Wave Architecture section (lines 254-292), ADR-PROJ022-002 (PROVISIONAL stub)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.841 |
| **Threshold (H-13)** | 0.92 |
| **Threshold (C4 requested)** | 0.95 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.82 | 0.164 | Wave 5 missing from Signoff File Locations table; all other waves/transitions/bypass fields present |
| Internal Consistency | 0.20 | 0.84 | 0.168 | Wave definitions verbatim-match SKILL.md; Wave 5 omission from signoff table vs. presence in state tracking creates structural tension |
| Methodological Rigor | 0.20 | 0.86 | 0.172 | 8-step workflow with failure behaviors; measurable entry criteria; PROVISIONAL ADR status explicitly acknowledged |
| Evidence Quality | 0.15 | 0.78 | 0.117 | Source comments on all sections; ADR cited but is a STUB; "full derivation" claim overreaches the stub content |
| Actionability | 0.15 | 0.88 | 0.132 | Orchestrator-ready workflow table; bypass lifecycle with 7 steps; wave state detection table is a direct lookup |
| Traceability | 0.10 | 0.88 | 0.088 | Navigation table, anchor links, footer metadata, HTML source comments, cross-references all present |
| **TOTAL** | **1.00** | | **0.841** | |

---

## Detailed Dimension Analysis

### Completeness (0.82/1.00)

**Evidence:**
- All 6 waves (0-5) defined with names, sub-skills, entry criteria, and bypass conditions.
- All 5 transitions (0→1, 1→2, 2→3, 3→4, 4→5) have explicit quality checks, thresholds, and additional evidence requirements in the Per-Transition Requirements table.
- Bypass mechanism covers all 3 required fields (Unmet Criterion, Impact Assessment, Remediation Plan), plus a 7-step lifecycle, 4 constraints, and cumulative ceiling.
- Signoff validation specifies 5 criteria (schema completeness, quality gate pass, acceptance criteria met, bypass resolution, repository committed).

**Gaps:**
1. **Wave 5 signoff file absent from Signoff File Locations table (line 79-85).** The table rows run Foundation through Wave 4. Wave 5 has no corresponding `WAVE-5-SIGNOFF.md` entry. The Wave State Tracking table (line 154-158) correctly states that `WAVE-4-SIGNOFF.md` valid → Wave 5 authorized — but there is no row for Wave 5 signoff that would authorize a hypothetical Wave 6 or mark Wave 5 complete. For a 6-wave model this is a structural gap in the signoff coverage.
2. **The Signoff Requirements section documents the signoff *for unlocking the next wave* but does not address what constitutes Wave 5 *completion* (there is no Wave 6 to unlock).** The signoff model is implicitly designed as a "unlock next wave" mechanism; what happens at the end of Wave 5 is undefined.

**Improvement Path:**
- Add a `WAVE-5-SIGNOFF.md` row to the Signoff File Locations table with location `skills/user-experience/output/WAVE-5-SIGNOFF.md`.
- Add a clarifying note explaining Wave 5 signoff semantics: does it mark project completion or is it optional since there is no Wave 6?

---

### Internal Consistency (0.84/1.00)

**Evidence:**
- Wave Definitions table at line 24-31 is a word-for-word match to SKILL.md lines 260-267. No paraphrasing errors.
- The 0.85 threshold is consistent across: Wave Transition Gates (line 44), Per-Transition Requirements table (lines 53-56), Signoff File Validation (line 92), and the ADR citation (line 38).
- Bypass mechanism description matches ux-routing-rules.md [Bypass Routing] section exactly: same 3 fields, same cumulative ceiling of 2, same warning banner text pattern.
- Wave State Tracking detection table is internally consistent with the Signoff File Locations table for waves 0-4.

**Gaps:**
1. **Wave 5 structural tension:** Signoff File Locations (line 79-85) ends at Wave 4. Wave State Tracking (line 154-158) also ends at Wave 4 authorized. The Wave Definitions (line 31) defines Wave 5 with entry criteria and bypass conditions. This creates a gap: the document defines Wave 5 entry requirements but provides no signoff tracking state for Wave 5 itself. A reader implementing the orchestrator could infer that Wave 5 has no signoff requirement, which contradicts the Wave Signoff Enforcement pattern applied to waves 1-4.
2. **Bypass documentation path:** Line 120 specifies `skills/user-experience/output/{engagement-id}/wave-bypass-{wave-N}.md`. The Signoff File Locations use `skills/user-experience/output/WAVE-N-SIGNOFF.md` (no engagement-id). This is not a contradiction (different artifact types with different scoping) but the asymmetry is unexplained and could create confusion for implementors.

**Improvement Path:**
- Add Wave 5 row to both the Signoff File Locations table and the Wave State Tracking table.
- Add a brief note explaining why bypass files use `{engagement-id}` scoping while signoff files do not.

---

### Methodological Rigor (0.86/1.00)

**Evidence:**
- The deployment-phase vs. runtime-execution distinction is stated explicitly at line 22: "Waves are deployment phases for incremental skill build-out, not runtime execution order." This is a methodologically important distinction that prevents misapplication.
- Entry criteria are measurable: "at least 1 heuristic eval completed AND 1 JTBD job statement used in a product decision" (Wave 2), "30+ users for Kano survey" (Wave 5), "WSM >= 7.80" (Wave 5 AI-First). These are concrete numerical thresholds, not subjective assessments.
- The 8-step Wave Transition Workflow table (lines 184-191) specifies both the action and the failure behavior for each step, enabling deterministic orchestrator implementation.
- Bypass constraints include a cumulative ceiling (maximum 2 concurrent), signoff blocking for unresolved bypasses, and user approval requirement — all three are independently justified with rationale in the table.
- The S-014 scoring dimensions table (lines 63-69) is included for reference, ensuring scorers use the correct rubric.
- PROVISIONAL ADR status is explicitly acknowledged (line 38).

**Gaps:**
1. **Wave Transition Workflow step 2 specifies "Score each sub-skill's representative output" but does not define what constitutes a "representative output."** For a new sub-skill, there may be no prior output. The procedure for creating a test output to score is not specified.
2. **Bypass Lifecycle step 6 ("Remediate: User completes the unmet criterion per remediation plan") has no monitoring or enforcement mechanism specified.** The orchestrator's role in tracking remediation progress is undefined — does it check at every session? At wave signoff only? This gap makes the remediation closure partially non-deterministic.

**Improvement Path:**
- Add a note to Wave Transition Workflow step 2 defining "representative output": the most recent output artifact from the sub-skill in the current engagement.
- Add a row to the Bypass Lifecycle table covering remediation tracking: when and how the orchestrator checks whether the remediation plan has been fulfilled.

---

### Evidence Quality (0.78/1.00)

**Evidence:**
- HTML source comments on every major section trace content to SKILL.md sections: `<!-- Source: SKILL.md Section "Wave Architecture" -->` (line 20), `<!-- Source: SKILL.md Section "Wave Transition Quality Gates" -->` (line 37), `<!-- Source: SKILL.md Section "Wave Signoff Enforcement" -->` (line 75), `<!-- Source: SKILL.md Section "Wave Architecture" — bypass mechanism. -->` (line 106).
- ADR-PROJ022-002 is cited by full filename (line 38) and the ADR file verifiably exists at `projects/PROJ-022-user-experience-skill/decisions/ADR-PROJ022-002-wave-criteria-gates.md`.
- Template file paths (lines 99-100) are cited and both files verifiably exist: `kickoff-signoff-template.md` and `wave-signoff-template.md` confirmed by glob scan.
- Cross-reference to `ux-routing-rules.md [Bypass Routing]` (line 120) verified — that section exists at line 144 of ux-routing-rules.md.

**Gaps:**
1. **"Full derivation" language overreaches the ADR stub.** Line 46 states: "See `ADR-PROJ022-002-wave-criteria-gates.md` for full derivation." The ADR is explicitly a STUB with `<!-- STUB: Created during PROJ-022 Foundation phase. Full ADR to be written during EPIC-001. -->`. Claiming "full derivation" when the source is a stub is inaccurate per P-022. The SKILL.md handles this correctly with "Formal threshold derivation is tracked in `ADR-PROJ022-002-wave-criteria-gates.md` (pending)" — the rule file should match this hedged language.
2. **Wave 5 AI-First CONDITIONAL status has no evidence citation.** The `(COND)` tag appears in the Wave Definitions table but the condition (Enabler DONE + WSM >= 7.80) has no source comment. This is the most complex wave condition and the only one without an explicit source trace.
3. **Wave State Caching rules (lines 162-165) have no source citation.** These operational rules for cache invalidation are not traceable to SKILL.md or any other document.

**Improvement Path:**
- Change "full derivation" to "provisional threshold derivation" or match SKILL.md's "(pending)" language.
- Add source comment for Wave 5 AI-First conditional criteria.
- Add source comment for Wave State Caching rules, or note these are implementation guidance derived from the wave model (no explicit SKILL.md source).

---

### Actionability (0.88/1.00)

**Evidence:**
- Wave Transition Workflow table (steps 1-8) is directly executable by the orchestrator: each step has a named action and a specific failure behavior with example output ("Block transition; list sub-skills without output").
- Bypass Lifecycle is a 7-step sequence with actor (orchestrator or user) implied at each step.
- Wave State Tracking detection table is a direct lookup: file exists → state. No ambiguity.
- Bypass constraints table includes the exact warning banner text: `"[WAVE BYPASS] This output was produced before Wave {N} entry criteria were met."` — no orchestrator interpretation required.
- Per-Transition Requirements table specifies both quality threshold and additional evidence for each transition, giving the orchestrator a complete gate checklist.

**Gaps:**
1. **Step 5 of Wave Transition Workflow ("Generate WAVE-N-SIGNOFF.md using template") does not specify how N is determined contextually.** If the orchestrator is handling Wave 3 → 4, it needs to know to generate WAVE-3-SIGNOFF.md. This is inferrable but not explicit.
2. **The bypass prompt presentation procedure is delegated to `ux-routing-rules.md`** (line 120: "See `ux-routing-rules.md` [Bypass Routing] for full documentation structure"). This is appropriate cross-referencing, but a reader implementing solely from wave-progression.md would not have the complete bypass prompt text. The cross-reference is adequate but the dependency should be noted more prominently.

**Improvement Path:**
- Minor: add a note in step 5 clarifying that N is the wave being completed (not the wave being unlocked).
- The bypass prompt delegation is acceptable; consider adding a one-line summary of the prompt structure for implementor orientation.

---

### Traceability (0.88/1.00)

**Evidence:**
- Navigation table at lines 5-15 covers all 6 sections with anchor links: `[Wave Definitions](#wave-definitions)`, `[Wave Transition Gates](#wave-transition-gates)`, `[Signoff Requirements](#signoff-requirements)`, `[Bypass Mechanism](#bypass-mechanism)`, `[Wave State Tracking](#wave-state-tracking)`, `[Wave Transition Workflow](#wave-transition-workflow)`.
- Anchor link format is correct (lowercase, hyphenated).
- Footer metadata (lines 195-199): parent skill, created date, updated date, status — all present.
- HTML source comments on every section (6 comments total) provide section-level traceability to SKILL.md.
- Cross-references: `ux-routing-rules.md`, `ADR-PROJ022-002`, template paths.

**Gaps:**
1. **Wave 5 AI-First CONDITIONAL criteria (Enabler DONE + WSM >= 7.80) has no source trace.** This is repeated from the Completeness and Evidence Quality analysis — the omission affects traceability too.
2. **Wave State Caching rules (lines 160-165) have no source comment.** A reader cannot verify whether these rules derive from SKILL.md or are novel orchestrator behavior specified here.
3. **The document footer does not include a version field.** Other rule files in the framework use version numbers per AD-M-002. Absence makes it harder to reference a specific version in ADR citations.

**Improvement Path:**
- Add source comments for Wave 5 AI-First CONDITIONAL and Wave State Caching.
- Add a `Version: 1.0.0` field to the footer.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.82 | 0.90 | Add WAVE-5-SIGNOFF.md row to Signoff File Locations table; add Wave 5 row to Wave State Tracking table; clarify Wave 5 completion semantics (no Wave 6 to unlock) |
| 2 | Evidence Quality | 0.78 | 0.88 | Change "full derivation" (line 46) to "provisional threshold derivation" matching SKILL.md's hedged language; add source comments for Wave 5 CONDITIONAL criteria and Wave State Caching rules |
| 3 | Internal Consistency | 0.84 | 0.92 | Resolve structural tension: Wave 5 defined with entry criteria but no signoff tracking state; add explanatory note on bypass vs. signoff path asymmetry |
| 4 | Methodological Rigor | 0.86 | 0.92 | Define "representative output" in Workflow step 2; add remediation tracking mechanism to Bypass Lifecycle (step 6 currently has no enforcement path) |
| 5 | Actionability | 0.88 | 0.93 | Clarify step 5 N-value determination; add one-line bypass prompt summary for orientation |
| 6 | Traceability | 0.88 | 0.93 | Add version field to footer; source comments for Wave 5 CONDITIONAL and caching rules |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computation
- [x] Evidence documented for each score with specific line citations
- [x] Uncertain scores resolved downward (Internal Consistency: resolved 0.84 not 0.87; Evidence Quality: resolved 0.78 not 0.82)
- [x] First-draft calibration considered: this is a first production version of a new skill rule file; 0.841 is consistent with good first-draft range (0.80-0.88 for well-structured first-draft rule files)
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Wave 5 signoff omission assessed as a genuine structural gap, not a minor formatting issue — scored accordingly in Completeness and Internal Consistency
- [x] "Full derivation" language vs. STUB ADR assessed as a P-022 accuracy issue, not as a minor stylistic difference — scored accordingly in Evidence Quality

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.841
threshold: 0.92
c4_threshold_requested: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.78
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add WAVE-5-SIGNOFF.md row to Signoff File Locations table and Wave State Tracking table"
  - "Change 'full derivation' (line 46) to 'provisional threshold derivation' to match ADR STUB status"
  - "Add source comments for Wave 5 CONDITIONAL AI-First criteria and Wave State Caching rules"
  - "Define 'representative output' in Wave Transition Workflow step 2"
  - "Add remediation tracking mechanism to Bypass Lifecycle step 6"
  - "Add version field to footer"
```

---

*Score Report: adv-scorer-wave-progression-001.md*
*Scoring Agent: adv-scorer v1.0.0*
*Deliverable: skills/user-experience/rules/wave-progression.md*
*SSOT: .context/rules/quality-enforcement.md*
*Created: 2026-03-04*
