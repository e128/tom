# Quality Score Report: Wave 2 Signoff -- /user-experience Skill

## L0 Executive Summary
**Score:** 0.872/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness (0.80)
**One-line assessment:** The Wave 2 signoff is structurally sound with accurate artifact scores and strong traceability, but has two concrete gaps that block C4 acceptance: the file is placed in `work/` rather than the canonical `output/` directory, and the Usage Evidence section documents sub-skill capability rather than the actual Wave 2 usage evidence (completed hypothesis cycle or product launch with analytics) required by the wave-signoff-template Per-Wave Customization for Wave 2.

---

## Scoring Context
- **Deliverable:** `skills/user-experience/work/WAVE-2-SIGNOFF.md`
- **Deliverable Type:** Other (Wave signoff governance document)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md` [Quality Gate]
- **Threshold (this engagement):** 0.95 (C4 strict threshold per scoring request)
- **Scored:** 2026-03-04

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.872 |
| **Threshold (C4)** | 0.95 |
| **Threshold (H-13)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.80 | 0.160 | All template sections present; VERSION header; 9 artifacts listed. Two concrete gaps: file at `work/` not canonical `output/` per wave-progression.md; Usage Evidence documents capability not operational usage. |
| Internal Consistency | 0.20 | 0.93 | 0.186 | All 9 artifact scores verified to match required values exactly; agent names correct; sub-skill averages arithmetically accurate; 5/5 cross-framework test results consistent with wave-2-cross-framework-tests.md. |
| Methodological Rigor | 0.20 | 0.82 | 0.164 | Wave gate threshold cited with ADR, PASS justified by composite > 0.85; CI gates enumerated. Significant gap: usage evidence type does not satisfy Wave 2's per-transition requirement (hypothesis cycle or product launch), substituting deployment capability instead. |
| Evidence Quality | 0.15 | 0.90 | 0.135 | All 9 score report paths verified to exist as real files; wave-2-cross-framework-tests.md cited with test numbers; ci-checks.md and synthesis-validation.md referenced throughout. Minor: usage evidence rows lack operational artifact citations. |
| Actionability | 0.15 | 0.91 | 0.137 | Wave 3 authorization is explicit YES; HEART finding ID (HM-{NNN}) note is specific and implementable; Convergence Matching Rule 3 note is useful; zero blockers stated clearly. |
| Traceability | 0.10 | 0.90 | 0.090 | VERSION header present with DATE/SOURCE/REVISION; HTML comment source annotations in multiple sections; score report file paths for all 9 artifacts verified to exist; footer fields complete. File placement gap (work/ vs. output/) is a minor traceability break. |
| **TOTAL** | **1.00** | | **0.872** | |

**Composite calculation:**
(0.80 × 0.20) + (0.93 × 0.20) + (0.82 × 0.20) + (0.90 × 0.15) + (0.91 × 0.15) + (0.90 × 0.10)
= 0.160 + 0.186 + 0.164 + 0.135 + 0.137 + 0.090
= **0.872**

---

## Artifact Score Verification

All 9 required artifact scores were verified against the provided reference values:

| Artifact | Required Score | Signoff Score | Required Iters | Signoff Iters | Match |
|----------|---------------|---------------|----------------|---------------|-------|
| ux-lean-ux SKILL.md | 0.952 | 0.952 | 4 | 4 | EXACT |
| ux-lean-ux agent def | 0.952 | 0.952 | 5 | 5 | EXACT |
| ux-lean-ux rules | 0.958 | 0.958 | 3 | 3 | EXACT |
| ux-lean-ux mcp-runbook | 0.962 | 0.962 | 3 | 3 | EXACT |
| ux-lean-ux hypothesis template | 0.957 | 0.957 | 3 | 3 | EXACT |
| ux-lean-ux assumption template | 0.957 | 0.957 | 4 | 4 | EXACT |
| ux-heart-metrics SKILL.md | 0.951 | 0.951 | 3 | 3 | EXACT |
| ux-heart-metrics agent def | 0.953 | 0.953 | 1 | 1 | EXACT |
| ux-heart-metrics rules | 0.952 | 0.952 | 3 | 3 | EXACT |

**Score report path existence (confirmed via file system):**
- `skills/ux-lean-ux/output/quality-scores/skill-md-iter4-score.md` — EXISTS
- `skills/ux-lean-ux/output/quality-scores/agent-def-iter5-score.md` — EXISTS
- `skills/ux-lean-ux/output/quality-scores/rules-iter3-score.md` — EXISTS
- `skills/ux-lean-ux/output/quality-scores/mcp-runbook-iter3-score.md` — EXISTS
- `skills/ux-lean-ux/output/quality-scores/hypothesis-template-iter3-score.md` — EXISTS
- `skills/ux-lean-ux/output/quality-scores/assumption-template-iter4-score.md` — EXISTS
- `skills/ux-heart-metrics/output/quality-scores/skill-md-iter3-score.md` — EXISTS
- `skills/ux-heart-metrics/output/quality-scores/agent-def-iter1-score.md` — EXISTS
- `skills/ux-heart-metrics/output/quality-scores/rules-iter3-score.md` — EXISTS

All 9 score report paths resolve to real files. Zero fabricated citations.

---

## Detailed Dimension Analysis

### Completeness (0.80/1.00)

**Evidence:**
- All 8 required template sections are present and populated: Sub-Skills Deployed, Wave Quality Gate, Artifacts Verified, Usage Evidence, Cross-Framework Synthesis Test, Acceptance Criteria Met, Wave Bypass Usage, Authorization.
- Navigation table covers all sections with anchor links (H-23 compliant).
- VERSION header present: `VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: ...`
- All 9 artifacts listed with Score, Iterations, Verdict, Score Report path, and Status columns (extends beyond the template's 3-column format — this is a positive enhancement).
- Score Notes sub-section provides narrative context for notable artifact scores.
- Cross-Framework Artifact section present with wave-2-cross-framework-tests.md.
- Acceptance criteria section: all 8 items checked [x].
- Wave Bypass Usage: table present with empty rows indicating no bypasses.

**Gaps:**

1. **File placement error (CRITICAL gap for CI compliance):** The signoff is stored at `skills/user-experience/work/WAVE-2-SIGNOFF.md`. The canonical location per `skills/user-experience/rules/wave-progression.md` [Signoff File Locations] is `skills/user-experience/output/WAVE-2-SIGNOFF.md`. The `output/` directory is where wave-progression.md's state detection logic looks for the file. The `work/` directory is for in-progress work items, not closure deliverables. CI gate UX-CI-008 (Signoff Ordering) checks for the file at the `output/` path. This is a structural compliance failure.

2. **Usage Evidence type mismatch (SIGNIFICANT gap):** Wave 2 is "Data-Ready" and the template's Per-Wave Customization for Wave 2 (section "Wave 2 (Data-Ready)") specifies required evidence as:
   - "Product launched with analytics — Documented product launch with analytics instrumentation reference"
   - "OR Lean UX hypothesis cycle — At least 1 completed hypothesis cycle (hypothesis -> experiment -> result)"

   The signoff provides three usage evidence rows:
   - "Lean UX methodology completeness" — describes what the sub-skill contains, not a completed cycle
   - "HEART Metrics methodology completeness" — same issue; describes methodology presence
   - "Cross-framework synthesis tested" — valid evidence for CI readiness, but not the Wave 2 operational usage requirement

   None of the three rows demonstrate an actual completed Lean UX hypothesis cycle or product launch. This means the Wave 2 transition evidence requirement per `wave-progression.md` [Per-Transition Requirements] row "Wave 2 → 3: Documented usage artifact (product launch OR hypothesis cycle)" is not satisfied.

**Improvement Path:**
- Move the signoff file to `skills/user-experience/output/WAVE-2-SIGNOFF.md` or add a file at the canonical location that is the authoritative copy.
- Revisit the Usage Evidence section: either (a) acknowledge that Wave 2 operational usage evidence has not yet been produced (which would require a bypass or wave gate deferral), or (b) provide a reference to an actual completed hypothesis cycle artifact or product launch documentation.

---

### Internal Consistency (0.93/1.00)

**Evidence:**
- All 9 artifact scores match the required reference values exactly (see Artifact Score Verification table above).
- Sub-skill averages are arithmetically consistent: ux-lean-ux avg = (0.952+0.952+0.958+0.962+0.957+0.957)/6 = 5.738/6 = 0.9563 ≈ 0.956 (matches "0.956 (avg across 6 artifacts)"); ux-heart-metrics avg = (0.951+0.953+0.952)/3 = 2.856/3 = 0.952 (matches "0.952 (avg across 3 artifacts)").
- Wave composite 0.954 is consistent: overall average of all 9 artifact scores = 8.594/9 = 0.9549 ≈ 0.954.
- Agent names match SKILL.md declarations: `ux-lean-ux-facilitator` (confirmed in ux-lean-ux/SKILL.md agents field), `ux-heart-analyst` (confirmed in ux-heart-metrics/SKILL.md agents field).
- Sub-skill names `/ux-lean-ux` and `/ux-heart-metrics` are consistent throughout.
- Cross-framework tests: 5/5 PASS is consistent with wave-2-cross-framework-tests.md which concludes with all 5 tests PASS in the Verdict section.
- Acceptance criteria "9/9 PASS" is consistent with 9 artifacts in the Artifacts Verified tables.
- Wave 2 label "Data-Ready" is consistent with SKILL.md Wave Architecture and wave-progression.md Wave Definitions.
- Score Note "ux-heart-metrics agent definition (0.953, 1 iteration): Passed on first scoring iteration" is consistent with the Artifacts Verified table showing 1 iteration.
- Authorization text references Wave 1's 2 bypasses for transparency — consistent with WAVE-1-SIGNOFF.md which shows 2 bypasses.

**Gaps:**

1. **Composite score methodology tension:** The Wave Quality Gate section cites `wave-progression.md` [Wave Transition Workflow] Step 2: "Score the primary deliverable artifact for each sub-skill." This implies scoring the primary deliverable only, not an average of all artifacts. However, the composite 0.954 is calculated as an average across all 9 artifacts. The document describes what it does ("avg across N artifacts") but does not explain the departure from the Step 2 specification. This is a minor inconsistency in methodology description — it is not a factual error but could be read as a divergence from the documented process.

**Improvement Path:**
- Clarify whether 0.954 represents the average of primary deliverable scores per Step 2 or the average of all artifacts. If the latter, acknowledge it as an operational choice that exceeds the minimum Step 2 requirement.

---

### Methodological Rigor (0.82/1.00)

**Evidence:**
- Wave gate threshold (0.85) is cited with source (`docs/design/ADR-PROJ022-002-wave-criteria-gates.md`), PROVISIONAL annotation, and calibration plan reference. This is methodologically complete.
- S-014 6-dimension rubric invoked with weight references to `.context/rules/quality-enforcement.md` [Quality Gate].
- PASS justification: composite 0.954 > 0.85 threshold = PASS. Arithmetic is correct.
- CI gate references are specific and enumerated (UX-CI-001, UX-CI-002, UX-CI-004, UX-CI-005, UX-CI-011, UX-CI-012, UX-CI-013). Each maps to a real gate in ci-checks.md.
- Bypass section uses the correct table structure and correctly states "none" with the empty table format.
- Authorization cites the wave-progression.md source in an HTML comment.
- Cross-framework tests follow the 5-test structure established in Wave 1 (consistent methodology).
- HTML comment in Acceptance Criteria correctly distinguishes automated (CI gate ID) from human-verified items.
- HTML comment in Cross-Framework section correctly cites synthesis-validation.md sections for evaluation criteria.

**Gaps:**

1. **Usage evidence type does not satisfy Wave 2 transition requirements (SIGNIFICANT methodological gap):** Per `wave-progression.md` [Per-Transition Requirements], Wave 2 → 3 requires "Documented usage artifact (product launch OR hypothesis cycle)." Per the template's [Per-Wave Customization] Wave 2 section, the evidence types are: "Product launched with analytics — Documented product launch with analytics instrumentation reference" OR "Lean UX hypothesis cycle — At least 1 completed hypothesis cycle (hypothesis -> experiment -> result)."

   The signoff's Usage Evidence table provides documentation of sub-skill capabilities and cross-framework test passage, not operational usage. This means the wave gate's evidence check (wave-progression.md [Wave Transition Workflow] Step 3: "Verify additional evidence requirements") has not been satisfied methodologically, even though the document asserts PASS.

2. **Score report for cross-framework artifact is indirect:** The cross-framework artifact row does not cite a Score or Score Report path; instead it references the Cross-Framework Synthesis Test section. This is consistent with how Wave 1 handled cross-framework tests (which had a dedicated score report path), but differs from the Wave 1 format where the cross-framework tests artifact had a formal score and score report (`skills/user-experience/output/quality-scores/cross-framework-tests-iter3-score.md` with score 0.958). Wave 2 omits the formal score for this artifact. The Wave 2 cross-framework tests document does have associated quality scores (`wave2-cross-framework-tests-iter1-score.md` exists in the output/quality-scores directory), but this is not referenced in the signoff.

**Improvement Path:**
- Address the usage evidence gap: either provide a reference to a completed Lean UX hypothesis cycle artifact, document that Wave 2 operational usage is pending and apply a bypass, or clarify that "stub deployment readiness" is the intended Wave 2 evidence type with a wave-progression.md update.
- Add the wave2-cross-framework-tests score and score report path to the Cross-Framework Artifact table row for consistency with Wave 1 format.

---

### Evidence Quality (0.90/1.00)

**Evidence:**
- All 9 score report paths resolve to actual files in the repository (confirmed by file system Glob). Zero fabricated citations.
- Cross-framework test references are specific: "See `wave-2-cross-framework-tests.md` Test 1," "Test 2," etc. — directly traceable to the source document's test sections.
- CI gate numbers (UX-CI-001, UX-CI-002, UX-CI-004, UX-CI-005, UX-CI-011, UX-CI-012, UX-CI-013) all exist in ci-checks.md.
- Usage evidence row for cross-framework synthesis cites `skills/user-experience/work/wave-2-cross-framework-tests.md` — file confirmed to exist.
- Sub-skill SKILL.md files confirmed to exist (ux-lean-ux/SKILL.md, ux-heart-metrics/SKILL.md).
- Agent definition files cited are consistent with SKILL.md agent declarations.
- Score Notes section provides specific justifications with factual grounding (e.g., "0.962: Highest individual artifact score in Wave 2, reflecting the MCP runbook's focused scope").
- Authorization notes reference the ux-orchestrator methodology section for Wave 1 re-prefixing pattern — consistent with WAVE-1-SIGNOFF.md Authorization notes.

**Gaps:**

1. **Usage evidence rows lack operational artifact citations:** The three usage evidence rows cite SKILL.md files and a cross-framework tests file, but do not cite operational artifacts (e.g., a hypothesis backlog document, an assumption map, a product analytics configuration). This is acceptable for a Wave 2 stub-deployment signoff, but means the evidence for operational usage is testimonial rather than artifact-backed.

2. **Wave2 cross-framework tests score report not cited:** The file `skills/user-experience/output/quality-scores/wave2-cross-framework-tests-iter1-score.md` exists but is not referenced in the Cross-Framework Artifact table row (unlike Wave 1 which cited `cross-framework-tests-iter3-score.md`).

**Improvement Path:**
- If operational usage has occurred, add artifact paths (hypothesis backlog file, assumption map file, product analytics config) to the Usage Evidence section.
- Add the `wave2-cross-framework-tests-iter1-score.md` score report path to the Cross-Framework Artifact row.

---

### Actionability (0.91/1.00)

**Evidence:**
- Wave 3 authorization statement is explicit and unambiguous: "Wave 3 deployment is authorized: YES"
- Operational note about HEART finding ID assignment is specific: "the ux-orchestrator must assign `{PREFIX}-{NNN}` identifiers (e.g., `HM-001`) to HEART metric findings in synthesis report rows" — this is a concrete, actionable instruction with an example.
- "Consistent with the Wave 1 re-prefixing pattern for heuristic eval (`HE-{NNN}`) and JTBD (`JT-{NNN}`) finding IDs" provides context that makes the action implementable without ambiguity.
- "This mapping should be confirmed in the ux-orchestrator agent's methodology section" — names the specific location where action is needed.
- Convergence Matching Rule 3 note is specific: "(same metric impact) is now operational with HEART providing metric dimensions, expanding synthesis capability beyond Wave 1" — actionable knowledge for the ux-orchestrator.
- Zero open blockers stated clearly, enabling Wave 3 to proceed without prerequisite resolution.

**Gaps:**

1. **Usage evidence gap has unaddressed Wave 3 implications:** If Wave 2 operational usage evidence (hypothesis cycle or product launch) has not been produced, there may be a Wave 3 entry criteria concern (Wave 3 requires "launched product with analytics OR 1 completed Lean UX hypothesis cycle"). The Authorization notes do not address this dependency or flag it as a Wave 3 prerequisite. This is a minor actionability gap — the reader does not know whether the Wave 3 entry criteria are met.

**Improvement Path:**
- In the Authorization Notes, explicitly confirm whether Wave 3 entry criteria (launched product with analytics OR 1 completed Lean UX hypothesis cycle) are met, and if not, note it as a prerequisite that must be satisfied before the first Wave 3 engagement.

---

### Traceability (0.90/1.00)

**Evidence:**
- VERSION header: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/SKILL.md, skills/user-experience/rules/wave-progression.md, skills/user-experience/templates/wave-signoff-template.md, skills/user-experience/work/wave-2-cross-framework-tests.md | REVISION: Initial Wave 2 signoff -->`
- Wave Quality Gate section includes `<!-- Source: ... -->` citations to ADR-PROJ022-002 and wave-progression.md.
- Wave Bypass section includes no `<!-- Source: ... -->` comment (present in Wave 1 signoff but absent here).
- Authorization section includes `<!-- Source: wave-progression.md [Wave State Tracking] ... -->`.
- Cross-Framework section includes `<!-- Evaluation criteria: synthesis-validation.md ... CI gates: ci-checks.md ... -->`.
- Acceptance Criteria section includes `<!-- Source: SKILL.md Sections ... ci-checks.md ... -->`.
- Document footer: Version, Parent Skill, Wave, Project, Created fields all present.
- Score report file paths for all 9 artifacts provided and verified to exist.
- Parent skill (`/user-experience`), wave ("2 (Data-Ready)"), and project ("PROJ-022") all traceable in the document footer and header.

**Gaps:**

1. **File placement breaks CI traceability chain:** wave-progression.md [Signoff File Locations] states WAVE-2-SIGNOFF.md should be at `skills/user-experience/output/WAVE-2-SIGNOFF.md`. The wave state detection logic and CI gate UX-CI-008 look for this file at the `output/` path. The file at `work/WAVE-2-SIGNOFF.md` is not in the canonical traced location, so the wave state detection mechanism cannot find it. This means the traceability from the signoff document to wave state authorization is broken at the CI gate level.

2. **Authorization HTML comment is incomplete:** The Authorization comment cites only `wave-progression.md [Wave State Tracking]`. The template's Authorization comment cites both `wave-progression.md [Post-Wave-5 Operational State]` and `wave-progression.md [Wave State Tracking]`. For a non-final wave, only the State Tracking reference is needed, so this is not a gap.

3. **wave2-cross-framework-tests score report not cited in the traceability chain:** The Cross-Framework Artifact row has no Score Report path, breaking the chain from test results to quality validation for that artifact. (See Methodological Rigor gap #2.)

**Improvement Path:**
- Move or copy the signoff to `skills/user-experience/output/WAVE-2-SIGNOFF.md`.
- Consider adding `<!-- Source: ... -->` comment to the Wave Bypass section for structural symmetry with other sections.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.80 | 0.93+ | Move or copy the signoff file to `skills/user-experience/output/WAVE-2-SIGNOFF.md`. This is the canonical path per wave-progression.md [Signoff File Locations] and is required for CI gate UX-CI-008 to detect the wave as signed off. The current placement at `work/WAVE-2-SIGNOFF.md` makes the signoff invisible to the wave state detection mechanism. |
| 2 | Completeness + Methodological Rigor | 0.80 / 0.82 | 0.92+ | Address the Usage Evidence type gap. Either: (a) provide references to an actual completed Lean UX hypothesis cycle artifact or product launch documentation (if these exist), (b) add a Wave Bypass entry for the unmet Wave 2 → 3 evidence requirement with 3-field documentation per bypass mechanism, or (c) update wave-progression.md to clarify that stub-deployment evidence satisfies Wave 2's evidence requirement. Without resolution, the wave gate evidence check (Step 3 of the Wave Transition Workflow) is technically unmet. |
| 3 | Methodological Rigor | 0.82 | 0.90+ | Add the `wave2-cross-framework-tests-iter1-score.md` score and score report path to the Cross-Framework Artifact row in Artifacts Verified, for consistency with Wave 1 format (`cross-framework-tests-iter3-score.md` was cited with score 0.958). |
| 4 | Internal Consistency | 0.93 | 0.95+ | Clarify the composite score methodology: note whether 0.954 is an average of all artifact scores (enhancement over Step 2 minimum) or a subset. Add a sentence in the Wave Quality Gate section explaining that the overall average is used as a conservative measure. |
| 5 | Actionability | 0.91 | 0.95+ | In the Authorization Notes, explicitly confirm whether Wave 3 entry criteria are met ("launched product with analytics OR 1 completed Lean UX hypothesis cycle") or note this as a prerequisite for the first Wave 3 engagement. |

---

## Leniency Bias Check
- [x] Each dimension scored independently before composite was computed
- [x] Evidence documented for each score with specific file references and line-level verification
- [x] Uncertain scores resolved downward (Internal Consistency scored 0.93 not 0.95 due to composite methodology tension; Methodological Rigor scored 0.82 not 0.88 despite strong citation quality because the usage evidence gap is a structural methodology failure)
- [x] First-draft calibration considered (this is iteration 1; the 0.872 composite is consistent with first-draft scoring expectations for a well-structured document with concrete gaps)
- [x] No dimension scored above 0.95 (highest is 0.93 for Internal Consistency, which has documented exceptional evidence: all 9 scores verified exactly, arithmetic confirmed, agent names cross-referenced)

---

## Session Handoff Schema

```yaml
verdict: REVISE
composite_score: 0.872
threshold: 0.95
weakest_dimension: Completeness
weakest_score: 0.80
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Move signoff to canonical path: skills/user-experience/output/WAVE-2-SIGNOFF.md (CI gate UX-CI-008 compliance)"
  - "Address Usage Evidence gap: provide completed hypothesis cycle artifact OR apply formal bypass for unmet Wave 2 evidence requirement"
  - "Add wave2-cross-framework-tests score and score report path to Cross-Framework Artifact row"
  - "Clarify composite score methodology in Wave Quality Gate section"
  - "Confirm Wave 3 entry criteria status in Authorization Notes"
```

---

*Scoring Agent: adv-scorer v1.0.0*
*Rubric: S-014 LLM-as-Judge (6-dimension weighted composite)*
*SSOT: `.context/rules/quality-enforcement.md` [Quality Gate]*
*Deliverable scored: `skills/user-experience/work/WAVE-2-SIGNOFF.md`*
*Score report: `skills/user-experience/output/quality-scores/wave2-signoff-iter1-score.md`*
*Created: 2026-03-04*
