# Quality Score Report: ux-sprint-facilitator (Dual-File Agent Definition)

## L0 Executive Summary

**Score:** 0.884/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.78)

**One-line assessment:** Strong, well-structured agent definition that closely follows the reference pattern — complete methodology, all 7 XML sections, correct constitutional compliance — but falls below the C4 threshold (0.95) due to missing citation DOIs/URLs, a deviation from ET-M-001 reasoning_effort guidance without sufficient documented justification, and minor traceability gaps; targeted citation and justification improvements are required before acceptance.

---

## Scoring Context

- **Deliverable:** `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` + `skills/ux-design-sprint/agents/ux-sprint-facilitator.governance.yaml`
- **Deliverable Type:** H-34 dual-file agent definition (worker agent in /ux-design-sprint sub-skill)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Reference Pattern:** `skills/ux-behavior-design/agents/ux-behavior-diagnostician.md` + `.governance.yaml`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1 (first score)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.884 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Critical Findings** | 0 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 7 XML sections present; 14 S-010 checklist items; 12 post_completion_checks; all 4 sprint days fully specified; 3 handoff targets documented; one minor gap: `character` field omitted from persona (optional but present in diagnostician reference, not a hard gap) |
| Internal Consistency | 0.20 | 0.91 | 0.182 | Reasoning_effort declared `medium` in governance.yaml but ET-M-001 maps C4 to `max`; the inline comment provides rationale but this creates a detectable inconsistency between the governance file and the standard; all other claims are internally consistent across .md and .governance.yaml |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | Four-day Design Sprint 2.0 fully operationalized across 5 phases; each day has explicit activities, outputs, and transition criteria; quantitative thresholds documented (>= 3/5 users for strong theme, 10-16 storyboard panels, 5 users); Goldilocks prototype principle cited; Decider authority model present; AI facilitation limitations section is thorough and honest |
| Evidence Quality | 0.15 | 0.78 | 0.117 | Citations present for all 4 sources (Knapp 2016, Courtney 2019, Brown 2009, Nielsen 2000) but NONE have DOIs or URLs; Courtney (2019) citation is incomplete ("AJ&Smart" without publisher/ISBN/URL); Nielsen (2000) is a Nielsen Norman Group web article but no URL is provided; success criterion 9 explicitly requires DOIs or URLs; the reference diagnostician agent also lacks DOIs/URLs but success criteria for THIS scoring require them |
| Actionability | 0.15 | 0.91 | 0.137 | Complete 5-phase workflow with specific activities per day; observation grid tables are concrete; handoff YAML schemas are fully specified with all required fields; on-send protocol provides structured YAML for orchestrator consumption; degraded mode behavior is explicitly described; fallback behavior enumerates 7 specific conditions with concrete responses |
| Traceability | 0.10 | 0.78 | 0.078 | Traceability comment at bottom covers 13 standards (H-34, AD-M-001 through ET-M-001 etc.); SSOT references in footer are present; however: (1) no explicit ADR or requirement ID that mandated the four-day sprint format over five-day; (2) Courtney (2019) citation lacks a verifiable URL making the primary AJ&Smart citation non-resolvable; (3) the wave-progression.md reference (`v1.2.0`) is cited but no section anchor is provided; (4) the schema reference `docs/schemas/handoff-v2.schema.json` is cited but not confirmed to exist in the repo |
| **TOTAL** | **1.00** | | **0.884** | |

**Composite Calculation:**
(0.92 × 0.20) + (0.91 × 0.20) + (0.93 × 0.20) + (0.78 × 0.15) + (0.91 × 0.15) + (0.78 × 0.10)
= 0.184 + 0.182 + 0.186 + 0.117 + 0.137 + 0.078
= **0.884**

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**
- All 7 required XML sections present in .md body: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`
- S-010 Self-Review Checklist present with 14 items covering all sprint-specific checks
- governance.yaml `post_completion_checks` has 12 entries (exceeds the >= 8 minimum per success criterion 13): `verify_file_created`, `verify_navigation_table`, `verify_challenge_statement_hmw_format`, `verify_sprint_questions_testable`, `verify_all_four_days_documented`, `verify_storyboard_10_to_16_panels`, `verify_observation_grid_5_users`, `verify_pattern_analysis_threshold_applied`, `verify_sprint_verdicts_with_evidence`, `verify_assumption_validation_results`, `verify_synthesis_judgments_present`, `verify_handoff_data_populated`
- 5 phases with detailed activities documented (Day 1-4 plus Synthesis)
- Three downstream handoff targets documented (`/ux-lean-ux`, `/ux-heuristic-eval`, `/ux-jtbd`)
- session_context on_receive (6 items) and on_send (10 items) fully specified
- AI facilitation limitations section and Single-Facilitator Reliability Note are present (analogous to reference agent's Single-Diagnostician note)
- Key distinctions from 6 sibling agents documented
- Description is under 1024 characters (approximately 940), contains WHAT+WHEN+triggers
- Task in `disallowedTools`; model is `opus`
- P-003, P-020, P-022 in both `forbidden_actions` (governance.yaml line 28-30) and `principles_applied` (governance.yaml lines 67-69)

**Gaps:**
- The `character` field in `persona` is present in the reference diagnostician agent's governance.yaml? No — checking: the reference agent (ux-behavior-diagnostician.governance.yaml) does NOT have a `character` field either. Not a gap.
- `reasoning_effort` set to `medium` rather than `max` for C4 (addressed under Internal Consistency)
- The description mentions "synthesis confidence gates" but the agent does not have a dedicated `verify_confidence_gate_applied` post-completion check (minor gap)

**Improvement Path:**
- No material completeness improvements needed beyond resolving the reasoning_effort deviation
- Consider adding `verify_wave_entry_criteria_checked` to post_completion_checks (currently only S-010 item 1 covers this)

---

### Internal Consistency (0.91/1.00)

**Evidence:**
- .md and .governance.yaml are consistent in: tool list (both declare Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch), cognitive_mode (systematic), model (opus), output levels (L0, L1, L2), output location pattern, constitutional principles
- Forbidden actions text in .md guardrails section matches forbidden_actions in governance.yaml (same 3 NPT-009 entries)
- `disallowedTools: [Task]` in .md frontmatter is consistent with P-003 compliance in governance.yaml
- Handoff confidence calibration values (0.65/0.75/0.85) are defined in the output section and correspond coherently to the on_send protocol fields
- All 4 sprint days in the methodology section correspond exactly to the output section report structure
- The theme strength thresholds (>= 3 of 5 users) cited in Phase 4 methodology match the expertise bullet in `<identity>` and the observation grid description

**Gaps:**
- `reasoning_effort: medium` in governance.yaml (line 8) is internally inconsistent with ET-M-001 which states "C4=max". The comment provides a rationale ("C4 applies to overall deliverable quality gate") but this rationale is a deviation from the standard, not an override with documented justification (MEDIUM standard AD requires documented justification in the file). The comment is informal; it is not a documented justification per AD-M-009/ET-M-001. The reference agent (ux-behavior-diagnostician) also uses `medium` — this is a consistent choice across the skill but the inconsistency with ET-M-001 remains unresolved by formal justification.
- The `<capabilities>` section states "Context7 MCP is available" but then lists it under Tools NOT available formatting — this creates a subtle reading ambiguity. It appears in the first paragraph of `<capabilities>` as available, but is listed in the governance.yaml `allowed_tools` correctly. The .md body prose says "Context7 MCP is available for external library/framework documentation lookup" but formats it under the `**Tools NOT available:**` subsection heading, which is contradictory formatting (the tool IS available, not absent).

**Improvement Path:**
- Either formally justify `reasoning_effort: medium` for C4 workers in a governance comment using the documented-justification format ("MEDIUM standard deviation: ..."), OR change to `max` per ET-M-001 mapping
- Fix the `<capabilities>` section layout so Context7 MCP appears under a "Conditionally Available" heading or in the "Available capabilities" prose, not under "Tools NOT available"

---

### Methodological Rigor (0.93/1.00)

**Evidence:**
- Design Sprint 2.0 four-day structure is comprehensively operationalized: Day 1 (9 activities), Day 2 (4 activities with four-step sketch), Day 3 (6 activities), Day 4 (7 activities), Synthesis (7 activities) — each with explicit inputs and outputs
- Quantitative thresholds are precise and cited: >= 3 of 5 users for strong theme (Nielsen, 2000 rationale chain), 10-16 storyboard panels, 5 user interviews (Nielsen, 2000), 60-minute interview structure with timed segments (5+5+30+15+5 = 60 minutes), 15-20 minute expert interviews, 3-5 HMW interviews
- How Might We (HMW) facilitation technique is correctly attributed to Brown (2009) with the Sprint adoption citation (Knapp et al., 2016, Chapter 4)
- Decider authority model is explicitly handled including the edge case where no Decider is designated (facilitator presents ranked recommendation and asks for confirmation)
- Pattern confidence thresholds are operationally defined: strong >= 3/5 = HIGH, moderate 2/5 = MEDIUM, weak 1/5 = noted but not actionable
- Rumble vs. All-in-One decision options are present per the sprint methodology
- Prototype Goldilocks principle is cited from source (Knapp et al., 2016)
- Sprint question verdict taxonomy (Pass/Fail/Partial) is explicitly defined with threshold criteria
- Assumption classification (must-be-true/nice-to-have/unknown) with validation outcomes (validated/invalidated/inconclusive) is complete
- Wave entry criteria checked at Phase 1 step 1 with a specific artifact check (`WAVE-4-SIGNOFF.md`) and H-31 fallback
- AI facilitation limitations are explicitly disclosed (6 items) — consistent with P-022 compliance

**Gaps:**
- The interview protocol timing (60-minute structure) is cited as "Knapp et al., 2016, Chapter 14" but the chapter title reference ("Friday: Test") suggests this is from the five-day sprint book, not the AJ&Smart compressed version. There is no explicit reconciliation of how Day 4 interview methodology maps from the original five-day book to the four-day sprint context. This is a minor methodological gap — the sprint collapses prototype building and testing into Day 4, but the interview script structure is drawn from the five-day Day 5 chapter. The synthesis of these sources could be more explicit.
- No explicit mention of how the team recruits 5 representative users between Day 3 and Day 4 (this is a real facilitation gap in the original methodology that the agent does not address)

**Improvement Path:**
- Add a note in Phase 4 acknowledging that the Day 4 interview protocol is adapted from the five-day GV Sprint "Friday: Test" chapter (Knapp et al., 2016, Chapter 14) for the compressed AJ&Smart format, and that user recruitment should occur during or immediately after Day 3
- Minor improvement only — does not materially affect the score

---

### Evidence Quality (0.78/1.00)

**Evidence:**
- Four citations present in the References table: Knapp et al. (2016), Courtney (2019), Brown (2009), Nielsen (2000)
- Citations are correctly attributed and specific to the content they support (e.g., Knapp et al. Chapter 4 for HMW, Chapter 14 for interview protocol)
- In-text citations are present throughout methodology (not just in the references table)

**Gaps (Material):**
- **Zero citations include DOIs or URLs.** Success criterion 9 explicitly requires "All academic citations with DOIs or URLs." The References table provides book titles and journal references but no hyperlinks. Specifically:
  - Knapp et al. (2016): ISBN-trackable book, no ISBN or publisher URL
  - Courtney (2019): "AJ&Smart" — this is described as a methodology/course, not a traditional publication; no URL to the AJ&Smart website, no ISBN, no DOI
  - Brown (2009): Published book, no ISBN or publisher URL
  - Nielsen (2000): Web article on Nielsen Norman Group; this has a well-known URL (https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) but it is not included
- **Courtney (2019) citation is bibliographically incomplete.** "Courtney, J. (2019). *Design Sprint 2.0.* AJ&Smart." — no publication type specified, no URL, no format (book vs. online course vs. article), making it non-resolvable
- The reference diagnostician agent (ux-behavior-diagnostician) also lacks DOIs/URLs — indicating a skill-wide pattern rather than agent-specific negligence. However, the success criteria for this scoring round explicitly require them, so the absence is a scored gap
- The five-user 85% statistic (Nielsen, 2000) is correct and well-cited but the original Nielsen (2000) article is a web publication that should have a URL

**Improvement Path:**
- Add URLs to all four references:
  - Knapp et al. (2016): `https://www.thesprintbook.com` or ISBN
  - Courtney (2019): `https://ajsmart.com/design-sprint-2-0` (or current AJ&Smart URL)
  - Brown (2009): ISBN 978-0-06-176614-3 or publisher URL
  - Nielsen (2000): `https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/`
- Specify Courtney (2019) publication format (online methodology documentation vs. video course)
- This single change would raise Evidence Quality from 0.78 to approximately 0.91

---

### Actionability (0.91/1.00)

**Evidence:**
- 5-phase workflow with 33+ explicit activities providing clear execution path
- Each sprint day has specific outputs that serve as acceptance criteria for phase transition
- Observation grid table structure is fully specified with row/column format
- Storyboard table structure is fully specified (panel, screen state, user action, system response, emotional state)
- Assumption inventory table structure is fully specified
- Handoff YAML schemas are complete with all required fields per the handoff schema standard: from_agent, to_agent, task, success_criteria, artifacts, key_findings, blockers, confidence, criticality
- Fallback behavior covers 7 specific error conditions with concrete responses
- Degraded mode behavior is explicitly defined with formatted disclosure text
- On-send protocol provides a fully-typed YAML schema for orchestrator consumption

**Gaps:**
- The wave entry check (Phase 1, step 1) requires checking for `WAVE-4-SIGNOFF.md` — but the sprint facilitator is Wave 5, which should check for `WAVE-4-SIGNOFF.md` (a Wave 4 completion artifact). This is correct per the wave progression. However, the bypass condition ("team at product inception... with existing user research") does not specify what constitutes "existing user research" — no minimum evidence threshold is defined, making the bypass condition actionable only at the facilitator's discretion
- The lightning demos research instruction says "use web search capabilities" but does not specify a minimum number of sources per demo or a source quality criterion (e.g., domain-relevant vs. analogous domain)

**Improvement Path:**
- Specify the bypass condition with a concrete criterion (e.g., "existing user research means at minimum 5 user interviews or comparable qualitative evidence documented in the engagement context")
- Specify source quality expectations for lightning demos (e.g., "prefer primary design sources, product blogs, or case studies; avoid aggregator sites")

---

### Traceability (0.78/1.00)

**Evidence:**
- Footer traceability comment covers 13 standards: `H-34 (schema), H-34b (constitutional), AD-M-001, AD-M-004, AD-M-005, AD-M-006, AD-M-007, AD-M-008, ET-M-001, SR-002, SR-003, SR-009, AR-012`
- Parent skill and sub-skill SSOT references are present in footer with versions
- Wave and project context are documented
- governance.yaml references `docs/schemas/agent-governance-v1.schema.json` in header comment
- session_context schema references `docs/schemas/handoff-v2.schema.json`
- All four methodology citations include chapter-level specificity (e.g., "Chapter 4", "Chapter 14") for in-text traceability
- Upstream sub-skill data paths are specified (wave-progression.md, WAVE-4-SIGNOFF.md, /ux-jtbd output, /ux-heuristic-eval output)

**Gaps:**
- **Non-resolvable citation:** Courtney (2019) is the primary source for the AJ&Smart Design Sprint 2.0 format but lacks a URL, making it non-verifiable
- **Missing anchor:** wave-progression.md is referenced as `skills/user-experience/rules/wave-progression.md v1.2.0` but without a section anchor — if the file changes structure, the reference becomes ambiguous
- **Schema existence not verified:** `docs/schemas/handoff-v2.schema.json` is cited throughout but no verification that this file exists in the repo is documented in the agent definition. The reference diagnostician has the same pattern — a systemic gap
- **ADR traceability gap:** The agent definition was created as part of PROJ-022 but there is no reference to a specific ADR or design decision that mandated the four-day Design Sprint 2.0 over the five-day GV Sprint as the implementation approach. For C4 work, the choice of methodology should be traceable to a design decision record
- **Frontmatter lacks traceability**: The .md YAML frontmatter has no version or creation date field (these are official Claude Code fields that are absent; the footer in the markdown body carries version info but not in a machine-readable location)

**Improvement Path:**
- Add URLs to all citations (resolves both Evidence Quality and Traceability gaps simultaneously)
- Add section anchors to wave-progression.md references
- Confirm schema file existence or note a provisional reference
- Consider adding a reference to the PROJ-022 ADR or design decision that selected Design Sprint 2.0 as the sprint methodology

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.78 | 0.91 | Add URLs/DOIs to all four citations in the References table. Nielsen (2000) URL is well-known: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/. Courtney (2019) requires AJ&Smart URL and publication format specification. Knapp et al. (2016) add ISBN or Sprint Book URL. Brown (2009) add ISBN or publisher URL. |
| 2 | Traceability | 0.78 | 0.88 | (a) Add URLs to citations (same action as #1 — dual benefit). (b) Add section anchor to wave-progression.md reference. (c) Add an `\[PROVISIONAL\]` note to docs/schemas/handoff-v2.schema.json reference if schema existence is unverified. |
| 3 | Internal Consistency | 0.91 | 0.95 | Fix the `<capabilities>` section layout: move "Context7 MCP is available" to the **Available capabilities** paragraph, not under **Tools NOT available** heading. Currently the Context7 statement appears under a "NOT available" heading, which is directly contradictory. Second: add a formal MEDIUM standard deviation justification for `reasoning_effort: medium` at C4, replacing the informal comment. Format: "MEDIUM standard deviation (ET-M-001): reasoning_effort set to medium (not max) for worker agent in systematic cognitive mode with fixed 4-day protocol. The protocol structure bounds interpretive variance sufficiently at medium depth. C4 threshold applies to deliverable quality gate, not individual agent reasoning calls." |
| 4 | Completeness | 0.92 | 0.95 | Add `verify_wave_entry_criteria_checked` to post_completion_checks in governance.yaml. The S-010 item 1 covers this at the human-readable level but there is no machine-verifiable post-completion check for it. |
| 5 | Actionability | 0.91 | 0.95 | Specify the Wave 5 bypass condition with a concrete evidence threshold (e.g., minimum 5 user interviews or quantitative behavioral data). Remove ambiguity from "existing user research" criterion. |

---

## Leniency Bias Check

- [x] Each dimension scored independently — no dimension pulled up by strong neighbors
- [x] Evidence documented for each score — specific line references, quoted content, and gap descriptions per dimension
- [x] Uncertain scores resolved downward — Evidence Quality and Traceability both uncertain at the 0.78-0.82 boundary; resolved to 0.78 per leniency bias counteraction rule
- [x] First-draft calibration considered — this is an iteration 1 definition; 0.884 is within the expected 0.80-0.90 range for well-structured first iterations at C4
- [x] No dimension scored above 0.95 — highest dimension is Methodological Rigor at 0.93, supported by specific quantitative evidence
- [x] C4 threshold (0.95) actively applied — final composite of 0.884 is correctly below the C4 threshold, triggering REVISE verdict
- [x] Reference pattern comparison applied — ux-behavior-diagnostician used as calibration; the diagnostician is a version 1.2.0 (iteration 3) file while sprint facilitator is version 1.0.0 (iteration 1); the diagnostician's citation gaps (also no URLs) confirm a skill-wide pattern rather than unique negligence, but the success criteria for this scoring round require URLs

---

## Session Context Handoff Schema

```yaml
verdict: REVISE
composite_score: 0.884
threshold: 0.95
weakest_dimension: evidence_quality
weakest_score: 0.78
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add URLs/DOIs to all four citations in References table (Nielsen 2000, Knapp 2016, Courtney 2019, Brown 2009)"
  - "Fix capabilities section: Context7 MCP appears under 'Tools NOT available' heading but IS available — move to Available section"
  - "Formalize ET-M-001 deviation justification for reasoning_effort:medium at C4 (replace informal comment with documented-justification format)"
  - "Add wave_entry_criteria_checked post_completion_check to governance.yaml"
  - "Specify Wave 5 bypass condition with concrete evidence threshold (e.g., minimum 5 user interviews)"
```

---

*Scoring Agent: adv-scorer v1.0.0*
*Rubric: S-014 (LLM-as-Judge) — SSOT: `.context/rules/quality-enforcement.md`*
*Deliverables scored as a unit (dual-file architecture per H-34)*
*Calibration reference: `skills/ux-behavior-design/agents/ux-behavior-diagnostician.md` v1.2.0 (iteration 3)*
*Created: 2026-03-04*
