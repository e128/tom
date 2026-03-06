# Quality Score Report: wave-progression.md (Iteration 2)

## L0 Executive Summary
**Score:** 0.890/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.82)
**One-line assessment:** The wave progression rules are structurally complete and operationally sound after revision — Wave 5 signoff entries and representative-output definitions were added — but three residual gaps in Evidence Quality (Wave 5 AI-First CONDITIONAL lacks source citation, Wave State Caching has no trace, bypass/signoff path asymmetry is unexplained) and a missing footer version field prevent reaching the 0.95 C4 threshold; targeted fixes to those four items would likely achieve PASS.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/wave-progression.md`
- **Deliverable Type:** Rule file (Foundation layer, /user-experience skill)
- **Criticality Level:** C4 (skill rule file equivalent to `.context/rules/`; AE-002 auto-C3 minimum; governance of wave deployment process)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold Applied:** 0.95 (C4 as requested by user; note H-13 standard threshold is 0.92)
- **Prior Score:** 0.841 (adv-scorer-wave-progression-001.md, iteration 1)
- **Strategy Findings Incorporated:** No additional adv-executor reports provided
- **Scored:** 2026-03-04T12:00:00Z
- **Reference Artifacts Read:** SKILL.md (Wave Architecture, Wave Transition Quality Gates, Wave Signoff Enforcement sections), ADR-PROJ022-002-wave-criteria-gates.md (STUB, PROVISIONAL), skills/user-experience/rules/ci-checks.md (lines 1-60), skills/user-experience/templates/ (file existence confirmed)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.890 |
| **Threshold (C4 requested)** | 0.95 |
| **Threshold (H-13 standard)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Delta from Prior Score** | +0.049 (0.841 -> 0.890) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 6 waves defined; all 5 transitions specified; Wave 5 signoff row present; representative output defined; minor: remediation monitoring gap |
| Internal Consistency | 0.20 | 0.90 | 0.180 | Wave definitions match SKILL.md verbatim; 0.85 threshold consistent across all sections; bypass/signoff path asymmetry unexplained |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | 8-step workflow with failure behaviors; measurable entry criteria; representative output defined; PROVISIONAL ADR explicitly acknowledged; remediation tracking undefined |
| Evidence Quality | 0.15 | 0.82 | 0.123 | Source comments on all major sections; ADR STUB status properly hedged; two claims still without source citations (Wave 5 AI-First CONDITIONAL, Wave State Caching) |
| Actionability | 0.15 | 0.91 | 0.137 | Orchestrator-executable workflow; exact warning banner text provided; step 5 N-value is inferrable; bypass prompt delegates to ux-routing-rules.md appropriately |
| Traceability | 0.10 | 0.86 | 0.086 | Navigation table and anchor links present; footer lacks version field; Wave 5 CONDITIONAL and caching rules still untraceable |
| **TOTAL** | **1.00** | | **0.890** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**

All 6 waves (0-5) are defined in the Wave Definitions table (lines 26-33) with names, sub-skills, entry criteria, and bypass conditions. All 5 wave transitions (0→1 through 4→5) appear in the Per-Transition Requirements table (lines 52-58) with quality check, threshold, and additional evidence. Wave 5 WAVE-5-SIGNOFF.md now appears in the Signoff File Locations table (line 88). Wave State Tracking correctly maps WAVE-5-SIGNOFF.md valid to "All waves complete" (line 162). Wave Transition Workflow step 2 now defines "representative output" as "the sub-skill's primary deliverable artifact as defined in its SKILL.md `output` section" — the prior iteration's gap is closed. Bypass mechanism covers all 3 required fields, 7-step lifecycle, 4 constraints, and cumulative ceiling. Post-Wave-5 operational state is explicitly defined (lines 200-202).

**Gaps:**

1. **Remediation monitoring undefined (Bypass Lifecycle step 6).** Step 6 states "User completes the unmet criterion per remediation plan" and step 6a documents the bypass with updated evidence, but no mechanism specifies when or how the orchestrator verifies that the remediation criterion has been fulfilled between sessions. The bypass can remain open indefinitely without active enforcement. This is a meaningful operational gap for a cumulative-ceiling enforcement mechanism.

2. **Wave 5 Post-Completion semantics are outlined (lines 200-202) but do not address what happens if Wave 5 sub-skills produce output that fails the S-014 0.85 gate.** The section covers the normal path (all waves complete, full operational mode) but not the failure path for Wave 5 deliverable quality.

**Improvement Path:**

- Add a row to the Bypass Lifecycle table for remediation check: "Step 6b: At wave signoff, orchestrator verifies remediation plan status against bypass documentation before proceeding to step 4 (unresolved bypass check)."
- Add a note or table row for Wave 5 quality gate failure path in the Post-Wave-5 section.

---

### Internal Consistency (0.90/1.00)

**Evidence:**

Wave Definitions table (lines 26-33) is a word-for-word match to SKILL.md Wave Architecture table (lines 260-267 of SKILL.md). The 0.85 threshold appears consistently across: Wave Transition Gates section (line 46), all 4 rows of Per-Transition Requirements (lines 55-58), Signoff File Validation criterion 2 (line 95), and ADR-PROJ022-002 decision (confirmed by ADR read). Bypass constraints match the cumulative ceiling described in SKILL.md Wave Architecture bypass paragraph. Wave State Tracking detection table (lines 154-162) is consistent with Signoff File Locations (lines 82-88) across all 6 entries. The deployment-vs-runtime distinction stated at line 24 is consistent with SKILL.md line 256.

**Gaps:**

1. **Bypass documentation path vs. signoff file path asymmetry (unexplained).** Line 123 specifies bypass files at `skills/user-experience/output/{engagement-id}/wave-bypass-{wave-N}.md`. Signoff files (lines 82-88) use `skills/user-experience/output/WAVE-N-SIGNOFF.md` (no engagement-id). These are different artifact types and different scoping strategies, but the document provides no explanation of why bypass files are engagement-scoped while signoff files are project-scoped. An implementor might introduce inconsistency. The prior report flagged this; it remains unaddressed.

2. **Step 6a placement.** Step 6a (line 196) appears after Step 6 with the prerequisite note "(prerequisite: Step 4 identified unresolved bypasses requiring remediation before signoff)" — but Step 4 checks for unresolved bypasses and blocks if found. Step 6a's trigger condition would only apply if bypasses from a different wave were being remediated during this wave's signoff. The conditionality is accurate but the placement between Steps 6 and 7 is confusing for a linear workflow — a reader may interpret step 6a as always executing.

**Improvement Path:**

- Add a brief explanatory sentence after the Bypass Mechanism section header or in the bypass documentation path: "Bypass files are scoped per engagement because the same wave may be bypassed differently in separate engagements. Signoff files are project-scoped because wave completion is project-wide."
- Reframe step 6a as a conditional branch: "6a (conditional, only if unresolved bypasses from prior waves exist): Update bypass documentation..."

---

### Methodological Rigor (0.90/1.00)

**Evidence:**

Entry criteria are measurable and specific: "at least 1 heuristic eval completed AND 1 JTBD job statement used in a product decision" (Wave 2), "Storybook with 5+ Atom stories AND 1 Persona Spectrum review" (Wave 4), "30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed" (Wave 5), "WSM >= 7.80" (Wave 5 AI-First). All criteria are verifiable facts, not subjective assessments. The 8-step Wave Transition Workflow (lines 188-198) specifies both action and failure behavior for each step, making it directly implementable. Bypass constraints include rationale for each rule (lines 127-132). The deployment-phase vs. runtime-execution distinction is methodologically critical and stated explicitly. S-014 scoring dimensions table is reproduced for reference (lines 63-71). Threshold justification (0.85 vs 0.92) is explained inline with cross-reference to the ADR.

**Gaps:**

1. **Remediation monitoring gap (same as Completeness gap 1).** The bypass lifecycle has no monitoring mechanism for remediation progress between sessions. Step 6a documents remediation evidence at signoff time, but the gap is that there is no intermediate check point. For a file defining a quality gate mechanism, an undefined monitoring interval is a methodological gap.

2. **The PROVISIONAL status of the 0.85 threshold is acknowledged (line 48) but the calibration plan is not linked to any worktracker entity.** The ADR mentions calibration after Wave 1 deployment, but no worktracker entity or ADR revision plan is referenced in the rule file, making the calibration commitment non-traceable from this document alone.

**Improvement Path:**

- Add remediation check to Bypass Lifecycle as described above.
- Add a note: "The calibration plan for the 0.85 provisional threshold is tracked in PROJ-022 worktracker [Enabler: Wave Gate Calibration, post-Wave-1]" or equivalent reference.

---

### Evidence Quality (0.82/1.00)

**Evidence:**

HTML source comments on all six major sections (lines 22, 39-40, 77, 109, 148, 184) trace each section to SKILL.md source sections. ADR-PROJ022-002 is cited (line 48) with proper STUB/PROVISIONAL hedging: "provisional threshold derivation (ADR is STUB; to be baselined during Wave 1 deployment)" — the prior iteration's "full derivation" overstatement is corrected. Template file paths (lines 102-103) reference files verified to exist by glob scan: `kickoff-signoff-template.md` and `wave-signoff-template.md`. Cross-reference to `ux-routing-rules.md` [Bypass Routing] (line 123) is verified to exist. CI gate references (UX-CI-007 and UX-CI-008 in the preamble) are verified to exist in ci-checks.md.

**Gaps:**

1. **Wave 5 AI-First CONDITIONAL criteria (WSM >= 7.80, Enabler DONE) have no source comment.** The Wave Definitions table entry at line 33 includes complex conditional criteria that appear nowhere else in the rule file without a source trace. This is the most complex wave condition and the only one not explained with a source comment. The SKILL.md states the same criteria, but there is no `<!-- Source: ... -->` linking the claim to SKILL.md or any other design document. A reader cannot verify WSM 7.80 is derived from a specific UX measurement framework rather than being an arbitrary number.

2. **Wave State Caching rules (lines 164-169) have no source comment.** Three specific cache invalidation triggers are stated: "On the next routing decision after a signoff file is committed during the session," "At the start of each new engagement session," and "When a bypass is granted or resolved." These are operational behavior specifications that cannot be traced to SKILL.md's Wave Architecture or Wave Signoff Enforcement sections (which do not mention caching). They may be novel implementation guidance specified here for the first time — which is fine, but should be marked as such (e.g., `<!-- Implementation guidance: not derived from SKILL.md; specified here as orchestrator operational behavior -->`).

3. **The cumulative bypass ceiling of "2" is stated without justification or source.** Line 129 states "Maximum 2 concurrent bypasses per team" with a rationale ("Prevents accumulation of technical UX debt through unbounded wave skipping") but no derivation of why 2 rather than 1 or 3. SKILL.md states the same ceiling (line 285) also without derivation. This is a design decision that should trace to an ADR or at minimum be acknowledged as a provisional value.

**Improvement Path:**

- Add `<!-- Source: SKILL.md Section "Wave Architecture" Wave Definitions table — Wave 5 AI-First conditional. WSM threshold: provisionally derived from Fogg behavior score range; to be validated in EPIC-001. -->` to the Wave Definitions section.
- Add `<!-- Implementation guidance: Cache invalidation triggers specified here as orchestrator behavior; not explicitly stated in SKILL.md. Derived from wave state detection requirements. -->` to the Wave State Caching section.
- Add a footnote or comment on the bypass ceiling: "The value of 2 is provisional; calibration guidance is in ADR-PROJ022-002 (STUB)."

---

### Actionability (0.91/1.00)

**Evidence:**

The Wave Transition Workflow table (lines 188-198) provides directly executable instructions with failure behaviors. Step 2 now defines "representative output" inline, removing ambiguity. The exact warning banner text is specified (line 131): `"[WAVE BYPASS] This output was produced before Wave {N} entry criteria were met."` — no orchestrator interpretation needed. Bypass Fields table (lines 115-119) provides field name, description, and example for each field. Wave State detection table (lines 154-162) is a direct lookup with no conditional logic. Per-Transition Requirements table specifies both threshold and additional evidence for each transition. Post-Wave-5 behavior is explicitly defined (lines 200-202).

**Gaps:**

1. **Step 5 of Wave Transition Workflow ("Generate WAVE-N-SIGNOFF.md using template") does not specify how N is determined contextually.** This is minor and inferrable from context (N = the wave being completed), but an explicit statement would remove any ambiguity for an orchestrator implementation. This was flagged in the prior report and remains unaddressed.

2. **Bypass prompt presentation procedure is cross-referenced to `ux-routing-rules.md` [Bypass Routing] (line 123)** but no summary of the bypass prompt structure is provided here. An implementor using only this file cannot construct the bypass prompt. The cross-reference is appropriate, but the dependency creates an incomplete actionable instruction set within this document.

**Improvement Path:**

- Minor: Add a parenthetical to step 5: "Generate WAVE-N-SIGNOFF.md (where N = the wave number being completed, not the wave being unlocked) using template."
- Add a one-sentence bypass prompt summary: "The bypass prompt presents the 3-field template (Unmet Criterion, Impact Assessment, Remediation Plan) and requires user completion before proceeding."

---

### Traceability (0.86/1.00)

**Evidence:**

Navigation table (lines 9-16) covers all 6 sections with anchor links using correct format (lowercase, hyphenated). All anchor links verified against section headings. Footer metadata (lines 206-212): parent skill, parent SKILL.md path, sibling rules (4 files), created date, updated date, status — all present. HTML source comments on 6 sections provide section-level traceability. Version comment in document header (line 1): `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md ... -->` — version is present in the HTML comment but not in the visible footer.

**Gaps:**

1. **Footer lacks a visible version field.** The HTML comment at line 1 includes `VERSION: 1.0.0` but this is invisible in rendered markdown. Other framework rule files (e.g., `agent-development-standards.md`, `quality-enforcement.md`) include version in visible footer text or header metadata blocks. A reader of the rendered document cannot determine the version. This matters for ADR citations and diff tracking.

2. **Wave 5 AI-First CONDITIONAL criteria are untraceable within the document.** As noted under Evidence Quality: `WSM >= 7.80` and `Enabler DONE` have no source comment. A reader cannot determine the origin of these thresholds.

3. **Wave State Caching rules (lines 164-169) are untraceable.** These implementation-specific rules have no `<!-- Source: ... -->` comment, making it unclear whether they derive from SKILL.md or are novel specifications.

4. **The document preamble references `ADR-PROJ022-001` (line 22) for "architectural rationale" but ADR-PROJ022-001 does not exist as a file** (glob scan of `projects/PROJ-022-user-experience-skill/decisions/` found only ADR-PROJ022-002). The reference is to a nonexistent file, reducing traceability for readers who attempt to follow the citation.

**Improvement Path:**

- Add `*Version: 1.0.0*` line to footer.
- Add source comments for Wave 5 AI-First CONDITIONAL and Wave State Caching.
- Verify ADR-PROJ022-001 file existence; either create the stub or update the reference to the correct document.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.86 | 0.93 | Fix broken ADR-PROJ022-001 cross-reference in line 22 (file does not exist); add source comments for Wave 5 AI-First CONDITIONAL and Wave State Caching; add visible version field to footer |
| 2 | Evidence Quality | 0.82 | 0.90 | Add source comment for Wave 5 AI-First WSM >= 7.80 threshold; mark Wave State Caching as implementation guidance (not SKILL.md-derived); acknowledge bypass ceiling of 2 as provisional |
| 3 | Internal Consistency | 0.90 | 0.95 | Add explanation for bypass (engagement-scoped) vs. signoff (project-scoped) path asymmetry; reframe step 6a as conditional branch |
| 4 | Completeness | 0.92 | 0.96 | Add remediation monitoring step to Bypass Lifecycle; add Wave 5 quality gate failure path to Post-Wave-5 section |
| 5 | Methodological Rigor | 0.90 | 0.95 | Add remediation check mechanism; link calibration plan to worktracker entity |
| 6 | Actionability | 0.91 | 0.95 | Add N-value clarification to step 5; add one-line bypass prompt summary |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence cited with specific line numbers for every score
- [x] Uncertain scores resolved downward: Traceability (resolved 0.86, not 0.88, because ADR-PROJ022-001 does not exist — a harder finding than the prior report's version-field gap); Evidence Quality (resolved 0.82, not 0.85, despite improved hedging because two claims still lack source citations and the bypass ceiling has no derivation)
- [x] Calibration anchor check: 0.890 composite for a second-iteration, well-structured rule file that addressed most prior gaps is consistent with the 0.85-0.90 range for good-but-not-excellent work
- [x] No dimension scored above 0.95; highest is Actionability and Completeness at 0.92 and 0.91 — justified by concrete workflow tables with example outputs
- [x] The broken ADR-PROJ022-001 cross-reference (Traceability) is assessed as a genuine traceability failure (the referenced file does not exist), not as a minor formatting issue
- [x] Prior score comparison: composite increased 0.049 from iteration 1, consistent with several gap closures (Wave 5 signoff rows, representative output definition, "full derivation" language correction)

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.890
threshold: 0.95
h13_standard_threshold: 0.92
weakest_dimension: Evidence Quality
weakest_score: 0.82
critical_findings_count: 0
iteration: 2
delta_from_prior: +0.049
improvement_recommendations:
  - "Fix broken ADR-PROJ022-001 cross-reference (line 22): file does not exist in projects/PROJ-022-user-experience-skill/decisions/"
  - "Add source comment for Wave 5 AI-First CONDITIONAL criteria (WSM >= 7.80, Enabler DONE) in Wave Definitions section"
  - "Mark Wave State Caching rules as implementation guidance, not SKILL.md-derived"
  - "Add visible Version: 1.0.0 field to footer (currently only in HTML comment)"
  - "Add explanation for bypass (engagement-scoped) vs. signoff (project-scoped) path asymmetry"
  - "Add remediation monitoring mechanism to Bypass Lifecycle (step 6b)"
  - "Acknowledge bypass ceiling of 2 as provisional in Bypass Constraints table"
  - "Add N-value clarification to Wave Transition Workflow step 5"
```

---

*Score Report: adv-scorer-wave-progression-002.md*
*Scoring Agent: adv-scorer v1.0.0*
*Deliverable: skills/user-experience/rules/wave-progression.md*
*SSOT: .context/rules/quality-enforcement.md*
*Prior Score Report: projects/PROJ-022-user-experience-skill/reviews/adv-scorer-wave-progression-001.md*
*Created: 2026-03-04*
