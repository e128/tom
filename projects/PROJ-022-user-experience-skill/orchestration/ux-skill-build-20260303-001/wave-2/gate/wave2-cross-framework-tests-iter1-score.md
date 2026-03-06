# Quality Score Report: Wave 2 Cross-Framework Testing -- /user-experience Skill

## L0 Executive Summary

**Score:** 0.918/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Methodological Rigor (0.88)

**One-line assessment:** The Wave 2 cross-framework test document is high-quality, well-evidenced work that falls narrowly below the 0.95 C4 threshold primarily due to a filename convention inaccuracy in the verdict section and a secondary issue where HEART signal identifiers are not fully resolved to a concrete finding-ID format in the synthesized evidence; targeted corrections to these two items should push the score past threshold.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/work/wave-2-cross-framework-tests.md`
- **Deliverable Type:** Analysis (cross-framework synthesis readiness test document)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (C4 quality gate)
- **Scored:** 2026-03-04T00:00:00Z
- **Strategy Findings Incorporated:** No (standalone scoring)
- **Prior Score:** None (iteration 1)
- **Wave 1 Reference:** `skills/user-experience/work/wave-1-cross-framework-tests.md` (version 1.2.0, used for calibration)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.918 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.94 | 0.188 | All 5 tests present, verdict table, required actions (4 items), signoff readiness mapping, 14-entry references table; version header present |
| Internal Consistency | 0.20 | 0.92 | 0.184 | All agent names, template field names, and on-send protocol fields verified against source files; one minor inconsistency in synthesis output filename convention (engagement-id in path, not filename) |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | Tests follow Wave 1 analytical depth; HEART handoff gap analysis is a genuine Wave 2 improvement; but HEART signal identifiers left as "metric names (free-text)" without fully resolving the synthesis-level ID assignment logic; filename pattern inaccuracy in verdict section |
| Evidence Quality | 0.15 | 0.90 | 0.135 | Section-anchor citations throughout (preferred format); verified HEART on-send protocol, hypothesis-backlog-template [Handoff YAML], and synthesis-validation.md sections against actual files; minor gap: external citations referenced in test body lack independent bibliographic entries in references table |
| Actionability | 0.15 | 0.93 | 0.140 | 4 required actions are specific with concrete verification steps; blocking vs. non-blocking distinction clear; HEART finding ID assignment includes the specific regex to verify against; item 2 (HEART handoff formalization) explicitly non-blocking |
| Traceability | 0.10 | 0.95 | 0.095 | Version header present; all test criteria trace to specific source sections; references table complete; synthesis-validation.md section-anchor format used consistently throughout |
| **TOTAL** | **1.00** | | **0.918** | |

**Weighted composite computation:**
- (0.94 × 0.20) + (0.92 × 0.20) + (0.88 × 0.20) + (0.90 × 0.15) + (0.93 × 0.15) + (0.95 × 0.10)
- = 0.188 + 0.184 + 0.176 + 0.135 + 0.1395 + 0.095
- = 0.9175 (rounded to 0.918)

---

## Detailed Dimension Analysis

### Completeness (0.94/1.00)

**Evidence:**

The document is structurally complete at the same level as Wave 1:
- All 5 tests are present with matching structure to Wave 1 (test objective, pass criterion, method, per-sub-test analysis, result)
- Verdict table covers all 7 test results (Test 1, 2, 3, 4, 5a, 5b, 5c) with key evidence column
- Required Actions section has 4 well-defined items (vs. 3 in Wave 1), reflecting Wave 2's additional HEART handoff formalization action
- Signoff Readiness table maps all 5 test results to `wave-signoff-template.md` rows with anchor links
- References table has 14 entries (vs. 10 in Wave 1), adding HEART methodology rules, Lean UX agent definition, and HEART agent definition
- Version header present: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: ... -->`
- Navigation table covers all 10 major sections with correct anchor links

**Gaps:**

- The references table omits `docs/schemas/handoff-v2.schema.json` even though the document explicitly notes it is "planned -- not yet committed to the repository." Wave 1 similarly omitted this. Given the document itself explains the planned status, this is a minor completeness gap rather than an error.
- The version is 1.0.0 for Wave 2 vs. 1.2.0 for Wave 1 (which had three revision iterations). This is appropriate for a first iteration but means the document has not yet benefited from adversarial revision cycles.

**Improvement Path:**

Add a references entry for `docs/schemas/handoff-v2.schema.json` noting its planned status. Consider adding the `skills/user-experience/rules/wave-progression.md` reference since the document claims Wave 2 sub-skill status but does not cite the wave-progression rules that define Wave 2 criteria.

---

### Internal Consistency (0.92/1.00)

**Evidence:**

All key factual claims were verified against source files:

1. **Agent names:** `ux-lean-ux-facilitator` confirmed in `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` frontmatter (`name: jerry:ux-lean-ux-facilitator`). `ux-heart-analyst` confirmed in `skills/ux-heart-metrics/agents/ux-heart-analyst.md` frontmatter (`name: jerry:ux-heart-analyst`).

2. **On-send protocol fields (Lean UX):** The document's Test 3 table of ux-ext fields (`total_hypotheses`, `hypothesis_status_distribution`, `q1_assumptions`, `degraded_mode`, `handoff_hypotheses_count`, etc.) matches exactly the on-send protocol in `hypothesis-backlog-template.md` (lines 409-422).

3. **On-send protocol fields (HEART):** The document's HEART handoff table fields (`from_agent`, `engagement_id`, `dimensions_selected`, `total_metrics`, `metrics_with_baseline`, `measurement_plan_mode`, `artifact_path`, `confidence_goal_metric`, `confidence_thresholds`) match exactly the on-send protocol in `ux-heart-analyst.md` `<output>` section.

4. **Confidence levels:** `/ux-lean-ux` MEDIUM for assumption mapping/hypothesis generation — verified in `synthesis-validation.md` [Sub-Skill Synthesis Output Map] line 61. `/ux-heart-metrics` MEDIUM (goal-metric) and LOW (threshold) — verified in `synthesis-validation.md` lines 69-70.

5. **Template references:** `hypothesis-backlog-template.md [Handoff YAML]` — verified to exist as a named section in the template at the correct location.

**Inconsistency identified:**

The verdict section and Test 5 Overall Result both contain the statement: "These gates apply to both standard synthesis output filenames (`ux-orchestrator-synthesis-{engagement-id}.md`) and crisis-mode output filenames (`ux-orchestrator-crisis-{engagement-id}.md`)."

The actual CI gate implementation in `ci-checks.md` uses the file patterns:
```
skills/user-experience/output/*/ux-orchestrator-synthesis.md
skills/user-experience/output/*/ux-orchestrator-crisis.md
```

The engagement ID appears in the **directory path** (`output/*/` where `*` matches the engagement ID directory), NOT in the **filename**. The filenames are simply `ux-orchestrator-synthesis.md` and `ux-orchestrator-crisis.md`. The document incorrectly renders the filenames as `ux-orchestrator-synthesis-{engagement-id}.md`.

This same inconsistency exists in Wave 1 (wave-1-cross-framework-tests.md verdict section). It is a minor but verifiable factual error in both documents.

**Improvement Path:**

Correct both filename references in the Verdict section and Test 5 Overall Result to:
- `ux-orchestrator-synthesis.md` (in the `output/{engagement-id}/` directory)
- `ux-orchestrator-crisis.md` (in the `output/{engagement-id}/` directory)

---

### Methodological Rigor (0.88/1.00)

**Evidence of rigor:**

1. **Test 1 Step 1 (Signal Extraction):** Correctly identifies `HYP-{NNN}` and `ASM-{NNN}` as the Lean UX signal identifiers, citing the hypothesis backlog template's specific sections. The Rule 3 activation note is a genuine insight: Wave 2 is the first wave where HEART Metrics provides the metric dimension enabling Rule 3 (same metric impact) matching that was not available in Wave 1.

2. **Test 2 Mixed-Confidence Resolution Rule:** Correctly applies the minimum-confidence rule to HEART's dual-confidence outputs (MEDIUM goal-metric + LOW threshold = LOW when combined). Cites `synthesis-validation.md [Mixed-Confidence Resolution Rule]` and connects it specifically to the HEART use case.

3. **Test 3 HEART handoff gap analysis:** The step-by-step table documenting which of the 9 handoff-v2 fields are explicitly in the on-send vs. which are "reconstructable from report structure" is a methodological addition over Wave 1. The resolution paths are concrete and accurate.

4. **Test 4 degraded mode differentiation:** The document correctly distinguishes between two different degraded mode scenarios for Wave 2 sub-skills: (a) Lean UX Miro MCP unavailability (minimal synthesis impact because text outputs are complete) vs. (b) HEART Measurement Plan mode (reduces signal volume from "metrics below target" to "measurement plan specifications" but synthesis remains feasible via goal-signal-metric mappings). This nuance is correct and absent in Wave 1 which only had one degraded mode scenario.

5. **Test 5 UX-CI-013 scope analysis:** Correctly notes that Wave 2 has a broader LOW-confidence surface than Wave 1 because HEART threshold recommendations are always LOW, not just direct opposition contradictions.

**Evidence of rigor gaps:**

1. **HEART finding identifier resolution:** The document states "Metric names serve as finding identifiers within the HEART output" and "HEART Metrics does not use a `{PREFIX}-{NNN}` format natively -- metric names are descriptive strings." While the document correctly identifies the synthesis-level re-prefixing requirement (e.g., `HM-001`), it does not fully trace through what the specific orchestrator logic would look like for assigning these IDs. Wave 1's `F-{NNN}` re-prefixing discussion was more concrete because the Wave 1 heuristic eval template uses `F-{NNN}` format natively. The HEART case requires the orchestrator to assign new IDs to free-text metric names — the document acknowledges this but does not verify that the ux-orchestrator agent's `<methodology>` section actually documents this step (which it should per Required Action #1).

2. **Filename convention inaccuracy (already noted under Internal Consistency):** The incorrect `ux-orchestrator-synthesis-{engagement-id}.md` filename format in the verdict section also represents a methodological rigor issue — the test was supposed to verify CI gate evaluability, but the stated output filename pattern does not match what the CI gate actually checks.

3. **HEART signal extraction concrete example gap:** The convergence scenario table in Test 1 Step 2 uses concrete example metric names (e.g., "Checkout Completion Rate", "7-Day Return Rate") that are reasonable but not verifiable against the HEART agent's actual output templates — the HEART agent definition does not define specific metric examples. This is a minor rigor note (Wave 1 had the same characteristic with its convergence scenarios).

**Improvement Path:**

1. Correct the filename pattern in the verdict section (highest impact).
2. Add a verification note that the ux-orchestrator `<methodology>` section has been reviewed for HEART ID assignment logic, or flag this as an unresolved gap in Required Action #1.
3. The HEART signal identifier discussion would benefit from confirming that the `ux-orchestrator` agent's synthesis protocol (when it assigns `HM-{NNN}` identifiers) will preserve the original metric name as the "source finding description" in the traceability chain.

---

### Evidence Quality (0.90/1.00)

**Evidence:**

1. **Section-anchor citation format used correctly throughout:** All references to synthesis-validation.md, ci-checks.md, and agent definitions use the `[Section Name]` format rather than line numbers. This is the preferred format per the scoring rubric ("Citations use section-anchor format (not line numbers)").

2. **Key claims verified against actual source files:**
   - `hypothesis-backlog-template.md [Handoff YAML]` -- verified to exist, contains all cited fields
   - `ux-heart-analyst.md <output> section on-send protocol` -- verified, field-for-field match
   - `synthesis-validation.md [Sub-Skill Synthesis Output Map]` -- verified, `/ux-lean-ux` row (line 61: MEDIUM), `/ux-heart-metrics` rows (lines 69-70: MEDIUM + LOW)
   - `synthesis-validation.md [Mixed-Confidence Resolution Rule]` -- verified section exists as cited
   - `synthesis-validation.md [Failure Mode Handling]` "MCP Degraded Synthesis Inputs" row -- verified
   - `ci-checks.md [UX-CI-011]`, `[UX-CI-012]`, `[UX-CI-013]` -- all verified, implementation patterns match the text's analysis

3. **HEART on-send field claims verified:** The document states the on-send uses a "streamlined" protocol without explicit `to_agent`, `task`, etc. This is accurate -- the actual on-send YAML in `ux-heart-analyst.md` confirms only 10 fields (from_agent, engagement_id, dimensions_selected, dimensions_excluded, total_metrics, metrics_with_baseline, metrics_requiring_instrumentation, measurement_plan_mode, artifact_path, confidence_goal_metric, confidence_thresholds).

**Gaps:**

1. **External citations in test body lack Wave 2-level bibliographic entries:** The Test 1 Signal Extraction section mentions "Lean UX Build-Measure-Learn cycle (Gothelf & Seiden, 2021)" and "HEART framework GSM process (Rodden, Hutchinson & Fu, 2010)" but does not provide independent bibliographic entries in the Wave 2 document's references table. These citations are inherited from synthesis-validation.md (which does have full bibliographic entries), but the Wave 2 test document itself does not cite these externally.

2. **Wave 1 established precedent of providing bibliographic support** within the test document for methodology references. Wave 2 delegates this entirely to the synthesis-validation.md source. This is a defensible approach but a slight reduction in evidence self-sufficiency.

**Improvement Path:**

Either (a) add a minimal "Methodology Citations" subsection to the references table pointing to `synthesis-validation.md [External Methodology Citations]` for full bibliographic entries, or (b) add inline links to synthesis-validation.md citations for the Lean UX and HEART framework references in the test body.

---

### Actionability (0.93/1.00)

**Evidence:**

The 4 Required Actions are specific and well-constructed:

1. **HEART finding ID assignment confirmation:** Includes concrete verification step: "Verify by checking that UX-CI-012 regex `[A-Z]{2,}-[0-9]{3}` matches all finding ID references in synthesis output." Names the specific encoding location (ux-orchestrator `<methodology>` section).

2. **HEART handoff-v2 formalization:** Explicitly labeled "MEDIUM-priority enhancement" that "does not block signoff" -- clear priority and blocking status. Specifies the 6 fields that need to be added (`to_agent`, `task`, `success_criteria`, `key_findings`, `blockers`, `criticality`).

3. **Wave signoff population:** Clear instruction to populate WAVE-2-SIGNOFF.md using the verdict table as source, with explicit mapping guidance.

4. **Conditional PASS resolution:** Clear: "The condition (orchestrator HEART finding ID assignment) must be verified before the wave gate can be marked PASS unconditionally."

**Minor gap:**

Required Action #1 instructs that HEART finding ID assignment "SHOULD be encoded in the ux-orchestrator agent's `<methodology>` section" but does not verify whether this encoding currently exists or is absent. The action is stated as future work without confirming the current state. This means the signoff reader cannot determine whether this is a new addition or an existing capability that just needs verification.

**Improvement Path:**

Required Action #1 should include a verification step for the current state: "Check whether ux-orchestrator `<methodology>` currently documents HEART ID assignment. If absent, add it; if present, verify it covers the `HM-{NNN}` format."

---

### Traceability (0.95/1.00)

**Evidence:**

1. **Version header complete:** `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: synthesis-validation.md, skills/ux-lean-ux/SKILL.md, skills/ux-heart-metrics/SKILL.md, skills/user-experience/SKILL.md, skills/user-experience/rules/ci-checks.md, skills/user-experience/templates/wave-signoff-template.md | REVISION: Initial Wave 2 cross-framework test document -->`

2. **Every test criterion traces to a source section:**
   - Signal Extraction criteria for Lean UX and HEART: "synthesis-validation.md [Signal Extraction Criteria]"
   - Convergence matching rules: "synthesis-validation.md [Convergence Thresholds]"
   - Contradiction types: "synthesis-validation.md [Contradiction Handling]"
   - Failure mode handling: "synthesis-validation.md [Failure Mode Handling]"
   - CI gate definitions: "ci-checks.md [UX-CI-011]", "[UX-CI-012]", "[UX-CI-013]"

3. **References table** with 14 entries, all verified as existing files: synthesis-validation.md, ux-lean-ux SKILL.md, ux-heart-metrics SKILL.md, parent SKILL.md, ci-checks.md, wave-signoff-template.md, hypothesis-backlog-template.md, assumption-map-template.md, heart-methodology-rules.md, Lean UX agent definition, HEART agent definition, agent-development-standards.md, quality-enforcement.md.

4. **The Signoff Readiness table** maps test results to signoff template rows with anchor links to each test section -- providing complete traceability from test results to wave gate artifact.

**Gaps:**

None significant. The document has essentially complete traceability. The only minor note is that `skills/user-experience/rules/wave-progression.md` is not in the references table even though the document identifies Wave 2 sub-skills. Given the primary purpose is synthesis readiness testing (not wave gate testing), this is not a notable gap.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.92 | 0.95 | Fix the synthesis output filename pattern in Verdict section and Test 5 Overall Result: `ux-orchestrator-synthesis.md` (not `ux-orchestrator-synthesis-{engagement-id}.md`). The engagement ID is in the directory path, not the filename. Affects both the standard and CRISIS filename references. |
| 2 | Methodological Rigor | 0.88 | 0.93 | Add a verification note in Required Action #1 (or in Test 3 finding ID clarification) confirming whether the ux-orchestrator `<methodology>` section currently documents HEART finding ID assignment (`HM-{NNN}` format). If it does not, flag this as a concrete gap in the orchestrator that must be resolved before wave signoff. |
| 3 | Methodological Rigor | 0.88 | 0.93 | Clarify in Required Action #1 the traceability chain for HEART IDs: the orchestrator assigns `HM-{NNN}` as the synthesis-level ID, and the source metric name (e.g., "Checkout Completion Rate") is preserved as the source finding description. This makes the traceability protocol concrete rather than implicit. |
| 4 | Evidence Quality | 0.90 | 0.93 | Add a brief "Methodology Citation Sources" note in the references table pointing to `synthesis-validation.md [External Methodology Citations]` for full bibliographic entries for Lean UX (Gothelf & Seiden, 2021) and HEART (Rodden, Hutchinson & Fu, 2010) citations used in the test body. |
| 5 | Actionability | 0.93 | 0.95 | Update Required Action #1 to include the current-state check: "Verify whether ux-orchestrator `<methodology>` currently documents HEART ID assignment. If absent, this is a required addition; if present, verify it covers `HM-{NNN}` format." |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score
- [x] Uncertain scores resolved downward (Methodological Rigor scored 0.88 rather than 0.91 due to two verifiable gaps)
- [x] First-draft calibration considered (Wave 2 doc is version 1.0.0, first iteration; Wave 1 reached its final state at 1.2.0 after 3 iterations)
- [x] No dimension scored above 0.95 without exceptional evidence (Traceability at 0.95 justified by complete reference table, version header, and section-anchor citation discipline throughout)
- [x] Composite computed mathematically, not impressionistically

**Calibration note:** The Wave 1 reference document (v1.2.0, post-revision) provides a quality anchor. Wave 2 at v1.0.0 is comparable in depth and rigor to Wave 1's first iterations but has not yet incorporated adversarial feedback. The 0.918 composite reflects genuinely strong work that needs two targeted corrections (filename pattern + HEART ID assignment confirmation) rather than substantive methodology gaps.

---

## Iteration History

| Iteration | Score | Verdict | Key Change |
|-----------|-------|---------|------------|
| 1 (this) | 0.918 | REVISE | Initial score |

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Wave: 2 (Data-Ready)*
*Project: PROJ-022 User Experience Skill*
*Created: 2026-03-04*
