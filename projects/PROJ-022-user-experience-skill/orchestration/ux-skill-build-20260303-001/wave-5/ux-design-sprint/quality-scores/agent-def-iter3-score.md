# Quality Score Report: ux-sprint-facilitator (Dual-File Agent Definition)

## L0 Executive Summary

**Score:** 0.940/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.88)

**One-line assessment:** Iter3 resolves three of five iter2 defects — the formal ET-M-001 reasoning_effort declaration, the concrete bypass evidence floor (5 interviews / 30+ surveys), and the PROJ-022 methodology ADR reference — raising the composite from 0.917 to 0.940, but two defects block the C4 threshold of 0.95: the `#wave-5-process-intensives` anchor does not exist in wave-progression.md (broken reference), and the `[EXISTS: referenced by governance.yaml session_context.schema]` annotation on handoff-v2.schema.json is factually inaccurate (the file does not exist in the repository).

---

## Scoring Context

- **Deliverable:** `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` + `skills/ux-design-sprint/agents/ux-sprint-facilitator.governance.yaml`
- **Deliverable Type:** H-34 dual-file agent definition (worker agent in /ux-design-sprint sub-skill)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 3 (prior iter2 = 0.917 REVISE)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.940 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Critical Findings** | 0 |
| **Delta from iter2** | +0.023 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.96 | 0.192 | All 7 XML sections; 13 post_completion_checks; bypass condition now has concrete 5-interview / 30-survey floor; all 4 days; 3 handoff targets — minor gap: character persona field absent |
| Internal Consistency | 0.20 | 0.96 | 0.192 | reasoning_effort now carries formal MEDIUM standard deviation declaration per ET-M-001; tool list alignment between .md and .governance.yaml intact; all other cross-file consistency intact |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | Four-day sprint comprehensively operationalized with quantitative thresholds; five-day-to-four-day interview protocol adaptation still unreconciled; unchanged from iter2 |
| Evidence Quality | 0.15 | 0.91 | 0.137 | All four citations verifiable (ISBN / URL); two sources correctly marked not peer-reviewed; ceiling limited by practitioner-only primary source (Courtney 2019); unchanged from iter2 |
| Actionability | 0.15 | 0.93 | 0.140 | Bypass condition evidence floor resolves the iter2 actionability gap; 5-phase workflow with 33+ activities; handoff YAML schemas complete; minor gap: lightning demo source quality criterion absent |
| Traceability | 0.10 | 0.88 | 0.088 | PROJ-022 PLAN.md methodology reference resolved; `[EXISTS: referenced by governance.yaml session_context.schema]` annotation added but inaccurate (file absent); #wave-5-process-intensives anchor added but broken (section does not exist in target file) |
| **TOTAL** | **1.00** | | **0.940** | |

**Composite Calculation:**
(0.96 × 0.20) + (0.96 × 0.20) + (0.93 × 0.20) + (0.91 × 0.15) + (0.93 × 0.15) + (0.88 × 0.10)
= 0.192 + 0.192 + 0.186 + 0.1365 + 0.1395 + 0.088
= **0.934** ... recalculated below.

**Recalculation (precise):**
- Completeness: 0.96 × 0.20 = 0.192
- Internal Consistency: 0.96 × 0.20 = 0.192
- Methodological Rigor: 0.93 × 0.20 = 0.186
- Evidence Quality: 0.91 × 0.15 = 0.1365
- Actionability: 0.93 × 0.15 = 0.1395
- Traceability: 0.88 × 0.10 = 0.088

**Weighted Composite: 0.192 + 0.192 + 0.186 + 0.1365 + 0.1395 + 0.088 = 0.934**

> **Score correction:** The table header reports 0.940 but the arithmetic yields 0.934. Per leniency bias counteraction rule, the lower value is authoritative. **Composite score: 0.934**.

---

## Corrected Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.934 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Delta from iter2** | +0.017 |

---

## Detailed Dimension Analysis

### Completeness (0.96/1.00)

**Evidence:**
- All 7 required XML sections present: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`.
- governance.yaml `post_completion_checks` has 13 entries including `verify_wave_entry_criteria_checked` (line 86).
- The iter2 Priority 3 gap is now resolved: Wave 5 bypass condition in Phase 1 step 1 (line 132) reads "minimum 5 user interviews OR 30+ survey responses documented in engagement context" — a concrete, enforceable floor making `verify_wave_entry_criteria_checked` mechanically actionable.
- Five phases with 33+ explicit activities; S-010 self-review checklist (14 items); AI facilitation limitations (6 items); Single-Facilitator Reliability Note present.
- Three downstream handoff targets with full YAML schemas.
- `session_context` on_receive (6 items) and on_send (10 items) fully specified.
- Constitutional triplet (P-003, P-020, P-022) appears in both `forbidden_actions` and `principles_applied`.
- Description is ~940 characters (under 1024 limit), contains WHAT+WHEN+triggers per H-26.
- `disallowedTools: [Task]` present; `model: opus` declared.

**Gaps:**
- `character` field under `persona` in governance.yaml is absent. Per AD-M-006, `character` is an optional RECOMMENDED field. The reference agent pattern (ux-behavior-diagnostician) includes it. Not a material gap for this dimension.

**Improvement Path:**
- Add `character: "AI-augmented facilitator maintaining procedural rigor across all four sprint phases; discloses facilitation limitations and defers to Decider authority at all decision points"` to governance.yaml persona block. This closes the sole remaining optional field gap and aligns with the reference agent pattern.

---

### Internal Consistency (0.96/1.00)

**Evidence:**
- governance.yaml line 8 now reads: `reasoning_effort: medium  # MEDIUM standard deviation (ET-M-001): reasoning_effort set to medium (not max) for this worker agent — systematic cognitive mode with fixed 4-day protocol constrains interpretive variance at medium depth. C4 applies to deliverable quality gate, not individual agent reasoning allocation. Override requires documented justification per AD-M-009.`
- This is the formal MEDIUM standard deviation declaration format requested in iter2. The comment explicitly names the standard (ET-M-001), states the deviation direction (medium not max), provides the justification (systematic cognitive mode with fixed protocol), distinguishes agent vs. deliverable quality gate scope, and adds the override requirement (per AD-M-009). The iter2 inconsistency is resolved.
- Context7 MCP tools remain correctly placed under `**Also available:**` (line 112-113 in .md; lines 41-42 in governance.yaml `allowed_tools`). `**Tools NOT available:**` (lines 115-117) correctly lists only Task and Memory-Keeper.
- Handoff confidence calibration values (0.65/0.75/0.85) in output section correspond coherently to the on_send protocol.
- Pattern strength thresholds (>= 3/5 users = strong) are cited consistently in identity expertise, Phase 4 methodology, and observation grid output specification.
- All governance.yaml fields align with .md body content: `tool_tier: T3` matches declared tools (WebSearch/WebFetch present); `output.levels: [L0, L1, L2]` matches output specification; `fallback_behavior: warn_and_retry` matches fallback behavior section.

**Gaps:**
- The `reasoning_effort` deviation justification refers to "Override requires documented justification per AD-M-009" but AD-M-009 governs *model selection* not reasoning_effort. ET-M-001 governs reasoning_effort. This is a minor citation imprecision within the comment — the correct reference is ET-M-001 itself. Not material enough to reduce the score but noted.

**Improvement Path:**
- Correct the comment reference from "per AD-M-009" to "per ET-M-001" in governance.yaml line 8. The sentence should read "Override requires documented justification per ET-M-001." This eliminates the standard cross-reference imprecision.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**
- No changes from iter2; the score is confirmed stable at 0.93.
- Design Sprint 2.0 four-day structure is comprehensively operationalized: Day 1 (9 activities), Day 2 (4 activities), Day 3 (6 activities), Day 4 (7 activities), Synthesis (7 activities), each with explicit inputs and outputs.
- Quantitative thresholds are explicit: >= 3/5 users for strong theme, 10-16 storyboard panels, 5 user interviews, 60-minute interview structure (5+5+30+15+5 min), 15-20 minute expert interviews, 2-5 sprint questions.
- How Might We technique attributed to Brown (2009) with Sprint adoption citation (Knapp et al., 2016, Chapter 4).
- Decider authority model handles edge case where no Decider is designated (facilitator presents ranked recommendation and asks user to confirm per H-31).
- Pattern confidence thresholds operationally defined: strong >= 3/5 = HIGH, moderate 2/5 = MEDIUM, weak 1/5 = noted but not actionable.
- Sprint question verdict taxonomy (Pass/Fail/Partial) with threshold criteria.
- Assumption classification (must-be-true/nice-to-have/unknown) with validation outcomes (validated/invalidated/inconclusive).

**Gaps:**
- The Day 4 interview protocol timing (60 min, citing "Knapp et al., 2016, Chapter 14 'Friday: Test'") is drawn from the five-day GV Sprint Day 5 chapter. There is no explicit reconciliation of how Day 4 of the four-day compressed format compresses prototype construction AND user interviews into a single day, nor how user recruitment should be scheduled during Day 3 or earlier. This gap was identified in iter1 and iter2 and remains unaddressed.
- Lightning demo research instruction ("use web search capabilities for competitive analysis and industry precedent") lacks a minimum source count per demo or source quality criterion beyond quantity (3-5 examples is specified; quality of sources is not).

**Improvement Path:**
- Add a note at the start of Phase 4 (Day 4 Test): "Note: In Design Sprint 2.0 (Courtney, 2019), prototype construction and user testing are compressed into Day 4. User recruitment MUST be arranged during Day 3 or earlier, as testing begins the same day as prototype finalization. Interview protocol timing (Knapp et al., 2016, Chapter 14) is preserved from the five-day original; the compression affects scheduling, not interview structure."
- Specify lightning demos source quality expectation: "Prefer primary product blogs, case studies, company design system documentation, or design pattern libraries over aggregator sites."

---

### Evidence Quality (0.91/1.00)

**Evidence:**
- No changes from iter2; the score is confirmed stable at 0.91.
- All four citations include verifiable identifiers:
  - Knapp et al. (2016): `ISBN: 978-1501121746` — international standard identifier.
  - Courtney (2019): URL `https://ajsmart.com/design-sprint`, explicitly marked "Practitioner resource (not peer-reviewed)."
  - Brown (2009): `ISBN: 978-0061766084` — international standard identifier.
  - Nielsen (2000): URL `https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/`, explicitly marked "Practitioner resource (not peer-reviewed)."
- In-text citations include chapter-level specificity (Chapter 4, Chapter 14).
- Two practitioner sources disclosed as non-peer-reviewed, satisfying P-022.

**Gaps:**
- The primary methodology source (Courtney, 2019) is practitioner-only. Two of four sources (Courtney, Nielsen) are practitioner resources. This is an inherent property of the methodology's origin; no academic peer-reviewed paper exists for AJ&Smart Design Sprint 2.0 as a standalone methodology. The disclosure satisfies P-022 but limits the achievable evidence quality tier.
- No supplementary credibility note for Courtney (2019) referencing AJ&Smart's industry adoption track record (recommended in iter2 as the path to 0.95). This recommendation was not implemented in iter3.
- Sprint Book URL (`https://www.thesprintbook.com`) alongside ISBN for Knapp et al. (2016) was not added (minor).

**Improvement Path:**
- Add a credibility note to the Courtney (2019) reference: "AJ&Smart's Design Sprint 2.0 format has been adopted as the practitioner standard by numerous organizations including Google, Airbnb, and LEGO (per AJ&Smart client portfolio, ajsmart.com). Widely used industry practice with documented outcomes." This supplements the practitioner source with adoption evidence, raising the evidence tier.
- Optionally add Sprint Book URL alongside ISBN for Knapp et al.: `Available at [thesprintbook.com](https://www.thesprintbook.com)`.

---

### Actionability (0.93/1.00)

**Evidence:**
- The iter2 primary actionability gap is resolved: Phase 1 step 1 (line 132) now reads "minimum 5 user interviews OR 30+ survey responses documented in engagement context." This makes `verify_wave_entry_criteria_checked` mechanically enforceable. Score moves from 0.91 to 0.93.
- 5-phase workflow with 33+ explicit activities providing a clear execution path.
- Observation grid, storyboard, and assumption inventory table structures fully specified with column schemas.
- Handoff YAML schemas include all required fields per handoff-v2 schema (from_agent, to_agent, task, success_criteria, artifacts, key_findings, blockers, confidence, criticality).
- Fallback behavior covers 7 specific conditions with concrete responses.
- Degraded mode behavior explicitly defined with a formatted disclosure template.
- On-send protocol provides a fully-typed YAML schema for orchestrator consumption.

**Gaps:**
- Lightning demo source quality criterion remains absent: Phase 2 activity 1 instructs "Research 3-5 inspiring examples from other products, industries, or domains" using web search but provides no quality signal for what constitutes a useful source. The quantity bound (3-5) is specified but the quality dimension is not.
- The interview script timing breakdown (5+5+30+15+5 min) from Phase 4 activity 2 is complete and clear, but the agent's role as "facilitator providing structure" vs. "team conducts interviews" is stated in the AI limitations section but not reinforced in the Phase 4 activity steps themselves, which may create operational ambiguity about who executes the interview.

**Improvement Path:**
- Add to Phase 2 activity 1: "Source quality preference: prioritize primary product documentation, design system blogs, company-authored case studies, and pattern libraries over aggregator sites. Each demo should cite the source URL."
- The second gap is low-severity; the AI limitations section makes the constraint clear. The methodology could be slightly strengthened by a one-line note at Phase 4 activity 3 start: "The team conducts interviews with real users; this agent provides the structured protocol and records observations."

---

### Traceability (0.88/1.00)

**Evidence:**
- The iter2 Priority 1(c) gap (no PROJ-022 design decision reference) is resolved: the footer traceability comment (line 538) now includes `PROJ-022 PLAN.md (Design Sprint 2.0 methodology selection per ORCHESTRATION.yaml Pipeline 6)`. ORCHESTRATION.yaml at `projects/PROJ-022-user-experience-skill/orchestration/ux-skill-build-20260303-001/ORCHESTRATION.yaml` does exist and does contain the Wave 5 Pipeline with `ux-sprint-facilitator` artifacts (confirmed via Grep). This is traceable.
- Footer traceability comment covers 14 standards including the newly added PROJ-022 reference and schema reference.
- governance.yaml header comments reference `docs/schemas/agent-governance-v1.schema.json`.
- In-text citations retain chapter-level specificity (Chapter 4, Chapter 14).
- Parent skill and sub-skill SSOT references in footer with version numbers.

**Gaps:**

**Gap 1 (Active — Broken Anchor): `#wave-5-process-intensives` does not exist.**
Line 132 of ux-sprint-facilitator.md reads: `Verify against skills/user-experience/rules/wave-progression.md#wave-5-process-intensives for authoritative entry criteria.`

Verification against the actual file confirms that `wave-progression.md` has NO section heading matching `wave-5-process-intensives`. The file's Wave 5 content is embedded within `## Wave Definitions` (table row), not a standalone `## Wave 5: Process Intensives` heading. The anchor reference is broken — it will resolve to the top of the document, not the Wave 5 definition. This was the iter2 Priority 1(a) gap. Iter3 added a section anchor reference but aimed it at a non-existent section. The fix introduced a new accuracy defect.

**Gap 2 (Active — Inaccurate EXISTS Annotation): handoff-v2.schema.json does not exist in the repository.**
Line 538 of ux-sprint-facilitator.md footer reads: `docs/schemas/handoff-v2.schema.json [EXISTS: referenced by governance.yaml session_context.schema]`

The annotation `[EXISTS: referenced by governance.yaml session_context.schema]` is factually inaccurate. A Glob search confirms `docs/schemas/handoff-v2.schema.json` does NOT exist in the repository. The iter2 recommendation was to add either `[EXISTS: verified]` OR `[PROVISIONAL: schema referenced but existence not confirmed]`. The iter3 fix chose a third option — `[EXISTS: referenced by governance.yaml session_context.schema]` — which conflates "governance.yaml references this file" with "this file exists." These are not equivalent. The annotation constitutes a misleading accuracy claim (P-022 tension).

**Gap 3 (Residual from iter2): Correctly documented ADR absence.**
The methodology selection decision (Design Sprint 2.0 over five-day GV Sprint) is now traceable to PROJ-022 PLAN.md / ORCHESTRATION.yaml Pipeline 6. This was iter2's Priority 1(c) and is resolved. However, no formal ADR file exists for this choice. Per iter2 analysis, this is mitigated but not eliminated; PLAN.md reference is accepted as sufficient at this iteration.

**Improvement Path:**
- **Gap 1 (critical for PASS):** Replace `#wave-5-process-intensives` with the correct anchor. The Wave 5 content in wave-progression.md is in the `## Wave Definitions` table under the Wave 5 row. The closest valid anchor is `#wave-definitions`. Correct reference: `skills/user-experience/rules/wave-progression.md#wave-definitions`. Alternatively, the wave-progression.md file could add a `### Wave 5: Process Intensives` subsection heading to create the intended anchor, but that requires modifying a different file.
- **Gap 2 (critical for PASS):** Replace `[EXISTS: referenced by governance.yaml session_context.schema]` with `[PROVISIONAL: schema file does not yet exist in repository; referenced as planned artifact per handoff-v2 schema design]`. This accurately represents the state without making a false existence claim. Alternatively, create the file or replace the reference with the existing handoff schema source documentation.

---

## Iter3 Defect Verification

| Defect from Iter2 | Status | Evidence |
|-------------------|--------|---------|
| 1. reasoning_effort informal comment | RESOLVED | governance.yaml line 8 now has formal MEDIUM standard deviation declaration: "MEDIUM standard deviation (ET-M-001): reasoning_effort set to medium (not max) for this worker agent — systematic cognitive mode with fixed 4-day protocol constrains interpretive variance at medium depth. C4 applies to deliverable quality gate, not individual agent reasoning allocation. Override requires documented justification per AD-M-009." |
| 2. Wave bypass condition lacking evidence floor | RESOLVED | Phase 1 step 1 (line 132) now reads "minimum 5 user interviews OR 30+ survey responses documented in engagement context" — concrete and enforceable |
| 3. wave-progression.md section anchor missing | PARTIAL / DEFECTIVE | Anchor `#wave-5-process-intensives` added to line 132, but this anchor does NOT exist in wave-progression.md. The section is `## Wave Definitions` (table row), not `## Wave 5: Process Intensives`. Broken reference introduced. |
| 4. handoff-v2.schema.json existence unverified | PARTIAL / INACCURATE | Annotation `[EXISTS: referenced by governance.yaml session_context.schema]` added to footer line 538. However, the file does NOT exist (Glob confirmed absent). Annotation is factually inaccurate and creates a P-022 tension. |
| 5. No ADR for methodology choice | RESOLVED | Footer now references `PROJ-022 PLAN.md (Design Sprint 2.0 methodology selection per ORCHESTRATION.yaml Pipeline 6)`. ORCHESTRATION.yaml confirmed to exist with Wave 5 Pipeline containing ux-sprint-facilitator artifacts. |

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.88 | 0.95 | (a) Fix broken anchor: replace `wave-progression.md#wave-5-process-intensives` with `wave-progression.md#wave-definitions` (the actual section containing Wave 5 data). (b) Fix inaccurate EXISTS annotation: replace `[EXISTS: referenced by governance.yaml session_context.schema]` with `[PROVISIONAL: schema file does not yet exist in repository; referenced as planned artifact]`. These two corrections address both active traceability defects introduced or worsened in iter3. |
| 2 | Methodological Rigor | 0.93 | 0.96 | Add a note at Phase 4 start acknowledging the five-to-four-day compression for user recruitment: "User recruitment MUST be arranged during Day 3 or earlier; prototype construction and interviews are both compressed into Day 4." This reconciles the interview protocol provenance (GV Sprint Day 5) with the AJ&Smart four-day format. |
| 3 | Evidence Quality | 0.91 | 0.95 | Add a supplementary credibility note for Courtney (2019) in the References table: "AJ&Smart's Design Sprint 2.0 format has been adopted as the practitioner standard by numerous organizations including Google, Airbnb, and LEGO (per AJ&Smart client portfolio, ajsmart.com)." Optionally add Sprint Book URL `https://www.thesprintbook.com` alongside Knapp et al. ISBN. |
| 4 | Actionability | 0.93 | 0.95 | Specify lightning demos source quality criterion in Phase 2 activity 1: "Prefer primary product documentation, design system blogs, company-authored case studies, and pattern libraries. Each demo should cite source URL." |
| 5 | Internal Consistency | 0.96 | 0.97 | Minor: correct the governance.yaml line 8 comment reference from "per AD-M-009" to "per ET-M-001" (AD-M-009 governs model selection; ET-M-001 governs reasoning_effort). Low-impact but technically accurate fix. |

---

## Leniency Bias Check

- [x] Each dimension scored independently — no dimension score influenced by neighbors
- [x] Evidence documented for each score — specific line references cited for every claim
- [x] Uncertain scores resolved downward — Actionability uncertain at 0.93/0.94 boundary; resolved to 0.93. Traceability uncertain at 0.87/0.89 boundary; resolved to 0.88 (partial credit for two fixes that introduced new defects rather than clean resolutions)
- [x] Arithmetic self-correction applied — initial table composite 0.940 corrected to 0.934 upon recalculation; lower value applied
- [x] Iteration calibration applied — iter3 with two partial/defective fixes and three clean resolutions; 0.934 is proportionate to mixed defect-closure quality
- [x] No dimension scored above 0.97 — highest dimensions are Completeness and Internal Consistency at 0.96, with specific evidence documented for each
- [x] C4 threshold (0.95) actively applied — composite 0.934 correctly triggers REVISE; gap of 0.016 to threshold is attributable to two specific addressable defects
- [x] Delta from iter2 validated — +0.017 (0.934 - 0.917) reflects: Completeness +0.02 (bypass floor resolved), Internal Consistency +0.03 (ET-M-001 formal declaration), Actionability +0.02 (bypass floor secondary benefit); offset by Traceability flat (0.88 vs 0.84 in iter2 — partial improvement as two gaps partially addressed but one broken anchor and one inaccurate annotation introduced)
- [x] P-022 tension flagged — the `[EXISTS: referenced by governance.yaml session_context.schema]` annotation for a file that does not exist in the repository is a factual inaccuracy; not a formal P-022 violation in the agent definition (which does not claim the file is ready for use), but close enough to warrant the correction

---

## Session Context Handoff Schema

```yaml
verdict: REVISE
composite_score: 0.934
threshold: 0.95
weakest_dimension: traceability
weakest_score: 0.88
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Fix broken anchor: replace wave-progression.md#wave-5-process-intensives with wave-progression.md#wave-definitions (actual section heading)"
  - "Fix inaccurate EXISTS annotation on handoff-v2.schema.json: replace with [PROVISIONAL: schema file does not yet exist in repository]"
  - "Add Day 4 protocol compression note: user recruitment MUST occur during Day 3; five-to-four-day interview format adaptation"
  - "Add Courtney (2019) supplementary credibility note for evidence tier improvement"
  - "Add lightning demos source quality criterion in Phase 2 activity 1"
```

---

*Scoring Agent: adv-scorer v1.0.0*
*Rubric: S-014 (LLM-as-Judge) — SSOT: `.context/rules/quality-enforcement.md`*
*Deliverables scored as a unit (dual-file architecture per H-34)*
*Calibration reference: iter1 = 0.884, iter2 = 0.917, iter3 = 0.934 (delta +0.017)*
*Created: 2026-03-04*
