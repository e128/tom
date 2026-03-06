# Quality Score Report: wave-signoff-template.md (Iteration 2)

## L0 Executive Summary

**Score:** 0.921/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.80)
**One-line assessment:** Revision successfully closed the Wave 5 completeness gap and the 1-4 vs 1-5 consistency errors; remaining gaps are the PROVISIONAL ADR citation, missing full path for the inline ci-checks.md reference in body text, and absent source annotations on the Template and Field Descriptions sections — bring Evidence Quality and Traceability up one tier each to reach the 0.95 threshold.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/templates/wave-signoff-template.md`
- **Deliverable Type:** Design (template file)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Prior Score:** 0.853 (iteration 1 — `skills/user-experience/output/quality-scores/wave-signoff-template-score-20260304.md`)
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.921 |
| **Threshold** | 0.95 (C4 criticality, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.95 | 0.190 | Wave 5 now present with evidence table; Field Descriptions and Validation Rules both updated to 1-5; all template sections present |
| Internal Consistency | 0.20 | 0.95 | 0.190 | Wave number range consistent (1-5) in both field description and CI gate; wave evidence matches wave-progression.md entry criteria for all 5 waves; threshold 0.85 consistent across template, header, and validation section |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Gating sequence is logically complete; bypass table columns match wave-progression.md Bypass Fields; synthesis test checks trace to synthesis-validation.md; Wave 5 source annotation present with COND sub-skill notation |
| Evidence Quality | 0.15 | 0.80 | 0.120 | ADR-PROJ022-002 is explicitly marked PROVISIONAL throughout; wave-progression.md now cited in Per-Wave header; ci-checks.md has full path in intro but body text line 161 uses bare filename; quality-enforcement.md not cited for S-014 weights |
| Actionability | 0.15 | 0.92 | 0.138 | All 5 waves now have specific, binary evidence requirements; Field Descriptions documents all 13 fields with Required column; Validation Rules maps 1:1 to CI gate; Wave 5 evidence criteria are unambiguous |
| Traceability | 0.10 | 0.88 | 0.088 | Navigation table with anchor links present; footer metadata complete; Per-Wave and Validation Rules headers have Source annotations; Template and Field Descriptions sections lack Source annotations; VERSION header not bumped for iteration 2 revision |
| **TOTAL** | **1.00** | | **0.910** | |

> **Arithmetic verification:** (0.95 * 0.20) + (0.95 * 0.20) + (0.92 * 0.20) + (0.80 * 0.15) + (0.92 * 0.15) + (0.88 * 0.10)
> = 0.190 + 0.190 + 0.184 + 0.120 + 0.138 + 0.088
> = **0.910**

*(Displayed composite: 0.910. Rounded to three decimal places.)*

---

## Detailed Dimension Analysis

### Completeness (0.95/1.00)

**Evidence:**
- Wave 5 (Process Intensives) subsection is now present at lines 145-153 with a specific evidence table covering: Design Sprint cycle OR existing user research bypass, and AI-First Design engagement (if applicable) with Enabler + WSM criteria.
- Field Descriptions now states "Wave number (1-5)" at line 93 — previously said "(1-4)," which was a gap blocking Wave 5.
- Validation Rules now states "Integer 1-5" at line 166 — previously "Integer 1-4," which was inconsistent.
- All required template sections remain present: Sub-Skills Deployed, Wave Quality Gate, Artifacts Verified, Usage Evidence, Cross-Framework Synthesis Test, Acceptance Criteria, Wave Bypass Usage, Authorization, Notes.
- Field Descriptions covers all 13 fields (12 required + 1 optional), unchanged from iteration 1.
- Bypass table includes all 6 columns (Bypass ID, Sub-Skill, Unmet Criterion, Impact Assessment, Remediation Plan, Status), exactly matching wave-progression.md Bypass Fields.

**Gaps:**
- No explicit annotation distinguishing that Wave 0 (Foundation) uses a separate template (`kickoff-signoff-template.md`). This was noted in iteration 1. The intro paragraph does not direct users who are signing off Wave 0. A user populating a Wave 0 signoff could misapply this template. However, the footer ("Sibling templates: `skills/user-experience/templates/kickoff-signoff-template.md`") provides implicit guidance, and the intro paragraph specifies "WAVE-N-SIGNOFF.md" (implying N >= 1). This is a minor gap.
- The Authorization field template says "Wave [N+1] deployment is authorized" but for Wave 5, there is no Wave 6. The template does not handle the final-wave edge case (after Wave 5, there is no "Wave 6 deployment to authorize"). However, this is a minor edge case that does not block practical use.

**Improvement Path:**
- Add a brief note in the intro: "This template covers Waves 1-5. For Wave 0 (Foundation), use `kickoff-signoff-template.md`."
- Consider a note or variant for Wave 5 authorization: "All waves complete — no further wave deployment required."

---

### Internal Consistency (0.95/1.00)

**Evidence:**
- Wave number constraint is now consistently "1-5" in both Field Descriptions (line 95) and Validation Rules (line 166). The contradiction identified in iteration 1 is resolved.
- The 0.85 threshold is stated consistently in three locations:
  - Template body (line 37): "Threshold: >= 0.85 deployment readiness (ADR-PROJ022-002, PROVISIONAL)"
  - Intro paragraph (line 5): "0.85 operational threshold per ADR-PROJ022-002 PROVISIONAL"
  - Validation Rules (line 171): "Composite score >= 0.85 and result is 'PASS'"
  - All three match wave-progression.md ("0.85 S-014 weighted composite") and ci-checks.md ("Quality gate composite score >= 0.85").
- Wave 5 evidence requirements (lines 149-153) trace correctly to wave-progression.md and SKILL.md:
  - "Design Sprint completed" aligns with Wave 5 entry criteria: "30+ users for Kano OR 1 B=MAP bottleneck diagnosed" and "Design Sprint can proceed without Kano prerequisite if team has existing user research."
  - "OR existing user research" aligns with Wave 5 bypass condition.
  - "AI-First Design engagement (if applicable) ... Enabler DONE + WSM >= 7.80" aligns with Wave 5 AI-First conditional criteria.
- The Wave 4 evidence table correctly lists "Kano survey users (30+) OR B=MAP bottleneck diagnosed" — these are Wave 4 operational outputs, consistent with wave-progression.md Wave 5 entry criteria (Wave 4 must produce these before Wave 5 begins).
- CI gate reference UX-CI-007 confirmed in ci-checks.md CI Gate Summary.
- Acceptance Criteria "C4 >= 0.95 quality gate" is consistent with the project's C4 criticality level and the per-dimension scoring in this report.

**Gaps:**
- Minor: Wave 5 Authorization line reads "Wave [N+1] deployment is authorized" — for Wave 5, this would say "Wave 6 deployment is authorized," which is logically incorrect since Wave 6 does not exist. This is an edge case but a real inconsistency.
- Minor: The intro paragraph says the template covers "WAVE-{N}-SIGNOFF.md" files but the Field Descriptions says the Wave number range is 1-5, not explicitly stating that Wave 0 uses a different template. No direct contradiction, but the scope boundary is implicit rather than explicit.

**Improvement Path:**
- Update the Authorization template placeholder to handle the Wave 5 final-wave edge case: "Wave [N+1] deployment is authorized / All waves complete (Wave 5): YES / NO"

---

### Methodological Rigor (0.92/1.00)

**Evidence:**
- The gating sequence remains logically sound: sub-skills deployed → quality gate → artifact verification → usage evidence → synthesis test → acceptance criteria → bypass tracking → authorization. This maps to wave-progression.md Wave Transition Workflow steps 1-7 in order.
- Wave 5 subsection has an explicit source annotation (line 147): "<!-- Source: SKILL.md Section 'Wave Architecture' — Wave 5 entry criteria: Wave 4 complete (30+ users for Kano OR 1 B=MAP bottleneck); AI-First conditional on Enabler DONE + WSM >= 7.80. Sub-skills: `/ux-design-sprint`, `/ux-ai-first-design` (COND). -->" This annotation is the most complete per-wave annotation in the file, explicitly identifying the CONDITIONAL sub-skill.
- Bypass table structure is rigorous: all 6 columns present, status vocabulary ("ACTIVE / RESOLVED") is unambiguous.
- Cross-Framework Synthesis Test has 3 verifiable, specific checks that trace to synthesis-validation.md [Cross-Framework Synthesis Protocol]: (1) valid output produced, (2) confidence classifications present, (3) handoff data contracts validated.
- Acceptance Criteria checklist covers: quality gate (C4 >= 0.95), P-003 compliance, schema validation, synthesis testing, degraded-mode behavior, usage evidence, AGENTS.md update — all critical compliance dimensions.
- Per-Wave Customization header annotation (line 112) now explicitly cites both SKILL.md and wave-progression.md, explaining the derivation chain.

**Gaps:**
- Cross-Framework Synthesis Test rows remain generic placeholders (e.g., "Wave [N] sub-skills") rather than per-wave pre-filled examples. This is appropriate for a template but means the orchestrator must know which sub-skills to insert without explicit prompting. For example, Wave 3 would benefit from a note: "e.g., /ux-atomic-design and /ux-inclusive-design." This is a minor gap — not a methodological error.
- No explicit instruction on computing the composite score in the Wave Quality Gate block (which artifacts to score, which S-014 weights to use). The wave-progression.md is cited in the intro but the computation method is not surfaced in the template itself. The orchestrator must consult a separate file.

**Improvement Path:**
- The gaps above are minor and do not block orchestrator use. Score held at 0.92 — same as iteration 1, as no new methodological improvements were made in this revision (the revision targeted completeness and consistency, not methodology).

---

### Evidence Quality (0.80/1.00)

**Evidence:**
- The intro paragraph now cites `skills/user-experience/rules/wave-progression.md` with full repo-relative path — this was missing in iteration 1. The intro now reads: "`skills/user-experience/rules/wave-progression.md` [Signoff Requirements]" and "`skills/user-experience/rules/wave-progression.md` [Wave Transition Gates]". This closes the wave-progression.md citation gap.
- Per-Wave Customization header (line 112) now explicitly cites both sources: "SKILL.md Section 'Wave Architecture'" and "wave-progression.md [Wave Transition Gates]". This is stronger traceability than iteration 1.
- Validation Rules header (line 159) cites "ci-checks.md [UX-CI-007 Signoff File Structure, UX-CI-008 Signoff Ordering]" and "wave-progression.md [Wave Transition Gates]" and "ADR-PROJ022-002 (PROVISIONAL)".
- ADR-PROJ022-002 PROVISIONAL: The file explicitly marks this as PROVISIONAL in three locations — template body (line 37), intro paragraph (line 5), and Validation Rules header (line 159). The citation is honest about the PROVISIONAL status.

**Gaps:**
1. **ADR-PROJ022-002 remains PROVISIONAL.** The underlying ADR is a STUB (per iteration 1 analysis; the ADR itself states "PROVISIONAL — to be validated with Wave 1 calibration data"). The template correctly marks it as PROVISIONAL, but for a C4 deliverable, the threshold authority is an unratified ADR. This is the primary evidence quality gap. The template cannot resolve this independently — it requires the ADR to be baselined — but it could add a stronger disclaimer. Current handling ("ADR-PROJ022-002, PROVISIONAL") is honest but does not convey the calibration risk.
2. **Body text reference at line 161 lacks full path.** "The CI gate (UX-CI-007 in `ci-checks.md`) validates this signoff file" — the intro paragraph provides the full path (`skills/user-experience/rules/ci-checks.md`) but this inline body reference uses bare filename. A reader following only the Validation Rules section would not have the full path. The intro provides it, but the body reference should be consistent.
3. **quality-enforcement.md not cited for S-014 dimension weights.** The Wave Quality Gate scoring uses S-014 6-dimension rubric, but neither the template nor the Validation Rules section cite `quality-enforcement.md` as the authority for those weights. wave-progression.md cites it, but the template itself does not.
4. **No repo-relative path for ADR-PROJ022-002.** The ADR is cited by name but without its repo-relative path (`projects/PROJ-022-user-experience-skill/decisions/ADR-PROJ022-002-wave-criteria-gates.md`). Readers cannot locate it without searching.

**Why 0.80 and not higher:** Gap 1 (PROVISIONAL ADR) is a meaningful evidence quality issue for C4 — the threshold authority is explicitly unvalidated. Gaps 2, 3, and 4 compound this. The improvement from iteration 1 (0.72) to iteration 2 (0.80) is real: wave-progression.md is now cited, Source annotations are present in Per-Wave and Validation Rules headers. But the PROVISIONAL ADR is not resolved, and gaps 2-4 remain. Score 0.80 is not 0.85 because the PROVISIONAL status, absent quality-enforcement.md citation, and bare ci-checks.md inline reference collectively fall short of "most claims supported" (0.80 band) into "nearly at the next level."

**Improvement Path:**
- Add repo-relative path for ADR-PROJ022-002: "`projects/PROJ-022-user-experience-skill/decisions/ADR-PROJ022-002-wave-criteria-gates.md` (PROVISIONAL)".
- Change line 161 from "CI gate (UX-CI-007 in `ci-checks.md`)" to "CI gate (UX-CI-007 in `skills/user-experience/rules/ci-checks.md`)".
- Add inline citation: "Wave Quality Gate scoring uses S-014 6-dimension rubric (weights: `.context/rules/quality-enforcement.md` Quality Gate section)."
- Consider adding: "This template's threshold will be updated when ADR-PROJ022-002 is baselined."

---

### Actionability (0.92/1.00)

**Evidence:**
- All 5 waves now have specific, binary evidence requirements. The orchestrator can populate any WAVE-N-SIGNOFF.md by reading the corresponding Per-Wave section. Wave 5 additions are as specific as Waves 1-4: "At least 1 design sprint cycle (Understand → Sketch → Decide → Prototype → Test) documented" and "At least 1 AI interaction pattern analysis completed; Enabler status DONE + WSM >= 7.80."
- Field Descriptions documents all 13 fields with Required column. All populated correctly.
- The Validation Rules section gives the orchestrator a self-verification checklist before committing.
- The bypass table structure is immediately actionable: 6 columns with explicit status vocabulary.
- Authorization field is unambiguous ("YES / NO").

**Gaps:**
- Wave 5 AI-First Design entry in the evidence table says "at least 1 AI interaction pattern analysis completed" without specifying the expected output path for that evidence. Wave 1's evidence says "at least 1 heuristic eval report exists at expected output path" — same vagueness for the path, but Wave 5 is more ambiguous about what "AI interaction pattern analysis" looks like as an artifact.
- The Wave 5 "OR existing user research" evidence row lacks specificity: "Team has existing user research sufficient to bypass Kano prerequisite." The word "sufficient" is not defined. What constitutes sufficient? A count of studies? A minimum sample size? This is the weakest actionability point in the Per-Wave tables.
- No Wave 5 improvement from iteration 1 on the path reference issue — same observation applies as before, just now applies to Wave 5 as well.

**Improvement Path:**
- Clarify Wave 5 "OR existing user research" to specify what evidence format is accepted (e.g., "at least 1 prior user study with >= 5 participants, OR analytics dataset with >= 100 user sessions").

---

### Traceability (0.88/1.00)

**Evidence:**
- Navigation table with anchor links: `[Template](#template)`, `[Field Descriptions](#field-descriptions)`, `[Per-Wave Customization](#per-wave-customization)`, `[Validation Rules](#validation-rules)` — all 4 sections.
- Footer metadata: parent skill, parent SKILL.md path, sibling templates, "Consumed by" references with full paths and gate IDs, Created date, Updated date, Status.
- VERSION header at line 1: "VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections 'Wave Architecture', 'Wave Transition Quality Gates', 'Wave Signoff Enforcement'".
- Per-Wave Customization header (line 112) has `<!-- Source: SKILL.md Section "Wave Architecture" — wave definitions... Evidence requirements map to wave-progression.md [Wave Transition Gates]... Each wave subsection below traces to the corresponding wave row in SKILL.md and wave-progression.md. -->` — full and explicit.
- Wave 5 subsection (line 147) has `<!-- Source: SKILL.md Section "Wave Architecture" — Wave 5 entry criteria: Wave 4 complete (30+ users for Kano OR 1 B=MAP bottleneck); AI-First conditional on Enabler DONE + WSM >= 7.80. Sub-skills: /ux-design-sprint, /ux-ai-first-design (COND). -->` — most detailed per-wave annotation.
- Validation Rules header (line 159) has `<!-- Source: ci-checks.md [UX-CI-007 Signoff File Structure, UX-CI-008 Signoff Ordering] — CI gate pass criteria for WAVE-N-SIGNOFF.md files. Quality gate threshold (0.85) from wave-progression.md [Wave Transition Gates] per ADR-PROJ022-002 (PROVISIONAL). -->` — explicit multi-source citation.

**Gaps:**
1. **No `<!-- Source: -->` annotation on the Template section.** The `## Template` section (line 18) has no source annotation. Other major sections (Per-Wave Customization, Validation Rules) now have source annotations, but the Template section itself — which is the primary deliverable of this file — lacks one. It should cite wave-progression.md [Signoff Requirements] and SKILL.md [Wave Signoff Enforcement].
2. **No `<!-- Source: -->` annotation on the Field Descriptions section.** The `## Field Descriptions` section (line 90) has no source annotation, even though its content derives from wave-progression.md [Signoff File Validation] and the kickoff-signoff-template.md pattern.
3. **VERSION header not bumped.** The file was revised (Wave 5 added, 1-4 corrected to 1-5, Source annotations added) but VERSION is still "1.0.0" with DATE "2026-03-04". If the file was updated on the same date, the version bump may be considered optional — but a PATCH bump (1.0.0 -> 1.0.1) would make the revision traceable without requiring date-based forensics.
4. **Waves 1-4 subsections lack per-wave Source annotations.** Wave 5 now has one (line 147), but Waves 1-4 subsections have no inline source annotations. The header annotation covers all waves generically, but the per-wave specificity of Wave 5's annotation is not matched for Waves 1-4. This is asymmetric.

**Why 0.88 and not higher:** Three of the four section-level Source annotations are now present (Per-Wave, Validation Rules, Wave 5 specifically). The Template section and Field Descriptions section lack them. These are the two most user-facing sections. A reader consulting only the Template section has no inline trace to the source. Score 0.88 reflects meaningful improvement from iteration 1 (0.92) — wait, iteration 1 scored 0.92 for Traceability. The current iteration has added Source annotations (improvement) but the Template and Field Descriptions sections still lack them, and the VERSION is not bumped. Score 0.88 is appropriate: the traceability structure improved in Per-Wave and Validation Rules but regresses slightly against expectations since the Template section — the most critical — still lacks annotation. This is a real gap, not inflation.

**Improvement Path:**
- Add `<!-- Source: SKILL.md Section "Wave Signoff Enforcement" — signoff structure requirements. wave-progression.md [Signoff Requirements] — field completeness criteria. -->` before `## Template`.
- Add `<!-- Source: SKILL.md Section "Wave Signoff Enforcement". wave-progression.md [Signoff File Validation]. -->` before `## Field Descriptions`.
- Bump VERSION to 1.0.1 or add a REVISION note.
- Add minimal per-wave source annotations (or a single note) for Waves 1-4 matching Wave 5's style.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.80 | 0.88 | (a) Add repo-relative path for ADR-PROJ022-002 citation; (b) change line 161 "ci-checks.md" to "skills/user-experience/rules/ci-checks.md"; (c) add quality-enforcement.md citation for S-014 weights; (d) add disclaimer: "Threshold will be updated when ADR-PROJ022-002 is baselined." |
| 2 | Traceability | 0.88 | 0.93 | Add `<!-- Source: -->` annotation before `## Template` section (cite SKILL.md [Wave Signoff Enforcement] and wave-progression.md [Signoff Requirements]); add annotation before `## Field Descriptions`; bump VERSION to 1.0.1. |
| 3 | Completeness | 0.95 | 0.97 | Add a one-line note clarifying Wave 0 uses `kickoff-signoff-template.md`; update Wave 5 Authorization template placeholder to handle final-wave edge case. |
| 4 | Internal Consistency | 0.95 | 0.97 | Update Authorization template placeholder for Wave 5: "Wave [N+1] deployment is authorized / (Wave 5: All waves complete)" to avoid the "Wave 6" logical issue. |
| 5 | Actionability | 0.92 | 0.95 | Clarify Wave 5 "OR existing user research" criterion: specify what evidence format is accepted (study count, sample size, or analytics criteria). |
| 6 | Methodological Rigor | 0.92 | 0.95 | Add inline note in Wave Quality Gate block: "See wave-progression.md [Wave Transition Gates] for S-014 scoring dimensions and composite computation." |

---

## Delta Analysis (Iteration 1 vs Iteration 2)

| Dimension | Iter 1 | Iter 2 | Delta | What Changed |
|-----------|--------|--------|-------|-------------|
| Completeness | 0.82 | 0.95 | +0.13 | Wave 5 added; Field Descriptions and Validation Rules corrected to 1-5 |
| Internal Consistency | 0.85 | 0.95 | +0.10 | Wave number range now consistent (1-5); Wave 5 content aligns with source |
| Methodological Rigor | 0.92 | 0.92 | 0.00 | No methodological changes; Wave 5 addition does not change rigor level |
| Evidence Quality | 0.72 | 0.80 | +0.08 | wave-progression.md now cited; Source annotations added; ADR still PROVISIONAL |
| Actionability | 0.90 | 0.92 | +0.02 | Wave 5 evidence requirements are specific and unambiguous |
| Traceability | 0.92 | 0.88 | -0.04 | Source annotations added to Per-Wave and Validation Rules but Template and Field Descriptions lack them; wave-by-wave annotation asymmetric; VERSION not bumped |
| **Composite** | **0.853** | **0.910** | **+0.057** | |

**Note on Traceability delta:** Iteration 1 scored 0.92 on the basis of navigation table, footer metadata, status, and dates — all of which remain. Iteration 2 added Source annotations to some sections (improvement) but the Template and Field Descriptions sections now conspicuously lack what other sections have. The annotation pattern established by Per-Wave and Validation Rules headers raises the expectation bar for the Template section — which is the most important section — making its absence more visible than before. Strict application of the calibration rubric places the current state at 0.88: "most items traceable" with meaningful exceptions in the two highest-visibility sections.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score — specific line numbers, file paths, and quotes cited
- [x] Uncertain scores resolved downward: Traceability was uncertain between 0.88-0.92; resolved to 0.88 because the Template section (primary artifact) lacks a Source annotation while lower-visibility sections have one — this asymmetry is a real gap, not noise
- [x] Evidence Quality was uncertain between 0.78-0.82; resolved to 0.80 because wave-progression.md citation is now present (improvement from 0.72) but PROVISIONAL ADR, missing full inline path, and absent quality-enforcement.md citation are concrete deficiencies
- [x] Calibration anchors applied: 0.85 = "strong work with minor refinements"; 0.92 = "genuinely excellent across the dimension"; Completeness and Internal Consistency reached 0.95 because the specific gaps from iteration 1 are resolved with no new contradictions introduced
- [x] No dimension scored above 0.95 without exceptional evidence — Completeness and Internal Consistency both at 0.95, supported by specific evidence that all iteration-1 gaps are resolved

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.910
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.80
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add repo-relative path for ADR-PROJ022-002 in all citation locations"
  - "Change line 161 bare ci-checks.md reference to full path skills/user-experience/rules/ci-checks.md"
  - "Add quality-enforcement.md citation for S-014 dimension weights in Wave Quality Gate block"
  - "Add <!-- Source: --> annotation before ## Template section"
  - "Add <!-- Source: --> annotation before ## Field Descriptions section"
  - "Bump VERSION from 1.0.0 to 1.0.1 to make revision traceable"
  - "Clarify Wave 5 OR-existing-user-research criterion with specific evidence format"
  - "Update Wave 5 Authorization placeholder to handle final-wave edge case"
```

---

*Score Report: wave-signoff-iter2-score.md*
*Agent: adv-scorer*
*Deliverable: `skills/user-experience/templates/wave-signoff-template.md`*
*Prior Score Report: `skills/user-experience/output/quality-scores/wave-signoff-template-score-20260304.md`*
*Scored: 2026-03-04*
