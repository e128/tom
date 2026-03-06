# Quality Score Report: ux-sprint-facilitator (Dual-File Agent Definition)

## L0 Executive Summary

**Score:** 0.917/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.84)

**One-line assessment:** Iter2 addresses three of the five iter1 defects cleanly (citation URLs/ISBNs added, Context7 placement corrected, wave entry post-completion check added), raising the composite from 0.884 to 0.917, but the C4 threshold of 0.95 remains out of reach due to persistent traceability gaps (three of four iter1 gaps unresolved) and an informal rather than formally documented ET-M-001 deviation justification — targeted fixes to these two dimensions are required.

---

## Scoring Context

- **Deliverable:** `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` + `skills/ux-design-sprint/agents/ux-sprint-facilitator.governance.yaml`
- **Deliverable Type:** H-34 dual-file agent definition (worker agent in /ux-design-sprint sub-skill)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Reference Pattern:** `skills/ux-behavior-design/agents/ux-behavior-diagnostician.md` + `.governance.yaml`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2 (prior iter1 = 0.884 REVISE)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.917 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Critical Findings** | 0 |
| **Delta from iter1** | +0.033 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.94 | 0.188 | All 7 XML sections; 13 post_completion_checks including newly added `verify_wave_entry_criteria_checked`; all 4 sprint days; 3 handoff targets; minor gap: bypass condition still lacks concrete evidence threshold |
| Internal Consistency | 0.20 | 0.93 | 0.186 | Context7 correctly moved to "Also available" section — contradiction resolved; `reasoning_effort: medium` at C4 uses an inline comment rationale not a formal MEDIUM standard deviation justification, inconsistency with ET-M-001 (C4=max) persists |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | No changes from iter1; four-day sprint comprehensively operationalized with quantitative thresholds, Decider authority model, assumption classification, pattern strength tiers; minor gap: five-day-to-four-day interview protocol adaptation not explicitly reconciled |
| Evidence Quality | 0.15 | 0.91 | 0.137 | All four citations now have verifiable identifiers (ISBN for Knapp, URL for Courtney, ISBN for Brown, URL for Nielsen); Courtney and Nielsen marked "not peer-reviewed" — honest disclosure; primary AJ&Smart source (Courtney) is practitioner, not academic, reducing overall evidence tier |
| Actionability | 0.15 | 0.91 | 0.137 | No changes from iter1; 5-phase workflow, concrete table structures, handoff YAML schemas, fallback behavior; Wave 5 bypass condition still lacks concrete evidence threshold |
| Traceability | 0.10 | 0.84 | 0.084 | Courtney non-resolvability gap resolved (URL added); three iter1 gaps persist: wave-progression.md cited without section anchor, handoff-v2.schema.json existence unverified, no ADR for Design Sprint 2.0 methodology selection |
| **TOTAL** | **1.00** | | **0.917** | |

**Composite Calculation:**
(0.94 × 0.20) + (0.93 × 0.20) + (0.93 × 0.20) + (0.91 × 0.15) + (0.91 × 0.15) + (0.84 × 0.10)
= 0.188 + 0.186 + 0.186 + 0.1365 + 0.1365 + 0.084
= **0.917**

---

## Detailed Dimension Analysis

### Completeness (0.94/1.00)

**Evidence:**
- All 7 required XML sections present: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`
- governance.yaml `post_completion_checks` now has 13 entries, including the iter1-recommended `verify_wave_entry_criteria_checked` (line 86). This directly closes the iter1 Priority 4 gap.
- S-010 self-review checklist has 14 items in the methodology section
- Five phases with detailed activities documented (Day 1-4 plus Synthesis)
- Three downstream handoff targets documented with full handoff YAML schemas
- session_context on_receive (6 items) and on_send (10 items) fully specified
- AI facilitation limitations section (6 items) and Single-Facilitator Reliability Note present
- Key distinctions from 6 sibling agents documented in `<identity>`
- Description is approximately 940 characters (under 1024), contains WHAT+WHEN+triggers
- Task in `disallowedTools`; model is `opus`
- P-003, P-020, P-022 in both `forbidden_actions` and `principles_applied`

**Gaps:**
- Wave 5 bypass condition ("team at product inception with existing user research") still lacks a concrete minimum evidence threshold. "Existing user research" is not defined with a quantitative or qualitative floor. This reduces actionability of the entry criteria check that `verify_wave_entry_criteria_checked` is now intended to enforce.
- The `character` field in persona is absent; per AD-M-006, this is an optional RECOMMENDED field but its presence in the reference pattern (diagnostician) would represent full alignment. Not a material gap.

**Improvement Path:**
- Define "existing user research" with a concrete criterion (e.g., "minimum 5 user interviews OR 30+ survey responses OR 1 confirmed qualitative study") to make the bypass condition enforceable by `verify_wave_entry_criteria_checked`
- This single change would raise Completeness from 0.94 to approximately 0.96

---

### Internal Consistency (0.93/1.00)

**Evidence:**
- The iter1 contradiction is fully resolved: Context7 MCP now appears under `**Also available:**` (line 112-113) with both tool names explicitly listed (`mcp__context7__resolve-library-id`, `mcp__context7__query-docs`). The `**Tools NOT available:**` section (lines 115-117) correctly lists only Task tool and Memory-Keeper. There is no longer a tool appearing under the wrong heading.
- governance.yaml `allowed_tools` (lines 33-42) correctly includes both Context7 MCP tools.
- All other cross-file consistencies from iter1 are intact: tool list alignment between .md and .governance.yaml, forbidden_actions text matches guardrails text, constitutional principles appear in both files, output levels and location are consistent.
- Handoff confidence calibration (0.65/0.75/0.85) in output section corresponds coherently to the on_send protocol.
- Theme strength thresholds (>= 3/5 users) cited in Phase 4 methodology match the identity expertise bullet and observation grid description.

**Gaps:**
- `reasoning_effort: medium` in governance.yaml line 8 is accompanied by a detailed inline comment: "ET-M-001: systematic cognitive mode with fixed 4-day sprint protocol; medium effort balances facilitation rigor with token cost for C4 worker. Worker agent (not orchestrator) per ET-M-001 guidance; C4 applies to overall deliverable quality gate." This comment is substantively correct and provides a reasonable rationale. However, the iter1 recommendation specified a formal MEDIUM standard deviation justification format ("MEDIUM standard deviation (ET-M-001): reasoning_effort set to medium (not max) for worker agent..."). The comment remains an inline note rather than a structured deviation declaration. Per the leniency bias rule, when uncertain between 0.93 and 0.94 for this dimension, resolving downward: ET-M-001 maps C4 to `max` and the deviation lacks formal justification format.
- This is the sole remaining consistency gap; it is low-severity but detectable.

**Improvement Path:**
- Convert the informal `reasoning_effort` comment to a formal MEDIUM standard deviation declaration. Format: `# MEDIUM standard deviation (ET-M-001): reasoning_effort set to medium (not max) for this worker agent because systematic cognitive mode with fixed 4-day protocol constrains interpretive variance such that medium depth is sufficient. C4 threshold applies to deliverable quality gate, not individual agent reasoning allocation. Worker agent (not orchestrator) per ET-M-001 guidance.` This replaces the current inline comment.
- This single formatting change would raise Internal Consistency from 0.93 to approximately 0.96

---

### Methodological Rigor (0.93/1.00)

**Evidence:**
- No changes from iter1; the score is held at 0.93 (not moved, confirmed stable).
- Design Sprint 2.0 four-day structure is comprehensively operationalized: Day 1 (9 activities), Day 2 (4 activities), Day 3 (6 activities), Day 4 (7 activities), Synthesis (7 activities), each with explicit inputs and outputs.
- Quantitative thresholds: >= 3/5 users for strong theme, 10-16 storyboard panels, 5 user interviews, 60-minute interview structure (5+5+30+15+5), 15-20 minute expert interviews.
- How Might We technique attributed to Brown (2009) with Sprint adoption citation (Knapp et al., 2016, Chapter 4).
- Decider authority model handles the edge case where no Decider is designated.
- Pattern confidence thresholds operationally defined: strong >= 3/5 = HIGH, moderate 2/5 = MEDIUM, weak 1/5 = noted but not actionable.
- Sprint question verdict taxonomy (Pass/Fail/Partial) with threshold criteria.
- Assumption classification (must-be-true/nice-to-have/unknown) with validation outcomes (validated/invalidated/inconclusive).

**Gaps:**
- The interview protocol timing (60 min, from "Knapp et al., 2016, Chapter 14 'Friday: Test'") is drawn from the five-day GV Sprint Day 5 chapter. There is no explicit reconciliation of how the Day 4 interview methodology adapts from the five-day original to the four-day compressed format. The sprint compresses two days into Day 4 (prototype + test), but the interview script structure comes from the five-day Day 5 chapter without acknowledging the structural difference.
- User recruitment timing between Day 3 and Day 4 is not addressed.

**Improvement Path:**
- Add a note in Phase 4 acknowledging the adaptation from five-day GV Sprint "Friday: Test" (Knapp et al., 2016, Chapter 14) and noting that in AJ&Smart Design Sprint 2.0, prototype construction and user interviews are both compressed into Day 4, requiring user recruitment to be scheduled during Day 3 or earlier.
- Minor improvement only; does not materially block C4 acceptance.

---

### Evidence Quality (0.91/1.00)

**Evidence:**
- All four citations in the References table (lines 522-527) now include verifiable identifiers:
  - **Knapp et al. (2016):** `ISBN: 978-1501121746` — verifiable book identifier. Publisher and year confirmed in citation.
  - **Courtney (2019):** `Available at [ajsmart.com/design-sprint](https://ajsmart.com/design-sprint)` — URL present and hyperlinked. Explicitly marked "Practitioner resource (not peer-reviewed)."
  - **Brown (2009):** `ISBN: 978-0061766084` — verifiable book identifier. Publisher and year confirmed in citation.
  - **Nielsen (2000):** `Available at [nngroup.com/articles/why-you-only-need-to-test-with-5-users/](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)` — full URL present and hyperlinked. Explicitly marked "Practitioner resource (not peer-reviewed)."
- In-text citations remain throughout methodology with chapter-level specificity.
- The iter1 Primary gap (zero citations with DOIs or URLs) is fully resolved.

**Remaining Evidence Quality Considerations:**
- Two of four sources (Knapp et al., Brown) use ISBNs rather than URLs. ISBN is a fully verifiable international standard identifier; this is acceptable. Preference for URLs does not constitute a gap for published books with ISBNs.
- Two of four sources (Courtney, Nielsen) are practitioner resources (not peer-reviewed), as disclosed. The primary methodology source — AJ&Smart Design Sprint 2.0 — is practitioner, not academic. This is an inherent property of the methodology's origin, not a citation deficiency. The disclosure satisfies P-022.
- The 85% problem detection rate (Nielsen, 2000) remains correctly cited with a now-resolvable URL.

**Gaps:**
- The primary methodology source (Courtney, 2019) is practitioner-only. While disclosed, this creates a modest ceiling on the evidence tier — all major claims about the four-day format trace to a single non-peer-reviewed practitioner source. This is unavoidable given the methodology's origin (no academic peer-reviewed paper exists for AJ&Smart Design Sprint 2.0 as a standalone methodology) but limits the maximum achievable evidence quality score for this agent definition.
- Knapp et al. (2016) and Brown (2009) lack direct publisher URLs; ISBNs are provided instead. Not a material gap, but a URL to the Sprint Book website would be slightly more accessible.

**Improvement Path:**
- Evidence Quality at 0.91 is close to the expected ceiling for an agent whose primary methodology source is a practitioner document. To reach 0.95, consider adding a note that the AJ&Smart Design Sprint 2.0 is a well-established industry practice adopted by numerous organizations (with an example reference or citation count) to support the practitioner source's authority. This would be a supplementary credibility note, not a replacement citation.

---

### Actionability (0.91/1.00)

**Evidence:**
- No changes from iter1; the score is confirmed at 0.91.
- 5-phase workflow with 33+ explicit activities providing clear execution path.
- Observation grid, storyboard, and assumption inventory table structures are fully specified.
- Handoff YAML schemas include all required fields: from_agent, to_agent, task, success_criteria, artifacts, key_findings, blockers, confidence, criticality.
- Fallback behavior covers 7 specific conditions with concrete responses.
- Degraded mode behavior is explicitly defined with a formatted disclosure template.
- On-send protocol provides a fully-typed YAML schema for orchestrator consumption.

**Gaps:**
- Wave 5 bypass condition ("team at product inception with existing user research") remains without a concrete minimum evidence threshold. This gap was identified in iter1 Priority 5 but was not addressed in iter2. The `verify_wave_entry_criteria_checked` post-completion check (now added) partially compensates, but without a defined threshold, the check's pass criterion remains subjective.
- Lightning demos research instruction ("use web search capabilities for competitive analysis and industry precedent") still lacks a minimum source count per demo or source quality criterion.

**Improvement Path:**
- Specify a concrete evidence floor for the Wave 5 bypass condition in Phase 1 step 1 (e.g., "minimum 5 user interviews OR 30+ survey responses OR 1 confirmed qualitative study documented in engagement context"). This also benefits Completeness.
- Specify lightning demos source quality expectations (e.g., "prefer primary product blogs, case studies, or design system documentation over aggregator sites").

---

### Traceability (0.84/1.00)

**Evidence:**
- The iter1 primary traceability gap (Courtney 2019 non-resolvable) is resolved: URL `https://ajsmart.com/design-sprint` is now provided with hyperlink.
- Footer traceability comment covers 13 standards: H-34, H-34b, AD-M-001, AD-M-004, AD-M-005, AD-M-006, AD-M-007, AD-M-008, ET-M-001, SR-002, SR-003, SR-009, AR-012.
- Parent skill and sub-skill SSOT references in footer with versions.
- Wave and project context documented.
- governance.yaml header comments reference `docs/schemas/agent-governance-v1.schema.json`.
- session_context schema references `docs/schemas/handoff-v2.schema.json`.
- In-text citations include chapter-level specificity (Chapter 4, Chapter 14).

**Gaps (Three of Four iter1 Gaps Unresolved):**
- **Gap 1: Missing section anchor for wave-progression.md.** The reference `skills/user-experience/rules/wave-progression.md v1.2.0` (lines 60, 132) lacks a section anchor. If the file changes structure, the reference becomes ambiguous. This was identified in iter1 and remains unaddressed.
- **Gap 2: Schema existence unverified.** `docs/schemas/handoff-v2.schema.json` is referenced in session_context (governance.yaml line 88) and in the output section (line 419) but no evidence that this file exists in the repository is documented. The reference diagnostician shares this pattern — systemic gap. An `[EXISTS: verified]` or `[PROVISIONAL]` annotation would resolve this.
- **Gap 3: No ADR for methodology choice.** The selection of AJ&Smart Design Sprint 2.0 over the original Google Ventures five-day Sprint is not traceable to an ADR or design decision record in the PROJ-022 project files. For C4 work, methodology selection decisions should be traceable to explicit design decisions. This gap was identified in iter1 and remains unaddressed.
- The iter1 gap 4 (frontmatter lacks machine-readable version) is structurally inherent to the dual-file architecture; traceability information in the markdown body footer is the accepted pattern per H-34. Not re-penalized.

**Improvement Path:**
- Add section anchors to wave-progression.md references: `skills/user-experience/rules/wave-progression.md#wave-5-process-intensives v1.2.0` (using the actual section heading once verified).
- Add an `[EXISTS: verified]` annotation to the `docs/schemas/handoff-v2.schema.json` reference, OR replace with `[PROVISIONAL: schema referenced but existence not confirmed at definition creation time]`.
- Add a reference to the PROJ-022 design decision (ADR or equivalent) that selected Design Sprint 2.0 as the sprint methodology. Can be brief: "Methodology selection: PROJ-022 PLAN.md §Sprint Sub-Skill Design" or a dedicated ADR file path if one exists.
- These three changes would raise Traceability from 0.84 to approximately 0.93.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.84 | 0.93 | (a) Add section anchor to wave-progression.md references. (b) Add `[PROVISIONAL]` or `[EXISTS: verified]` annotation to `docs/schemas/handoff-v2.schema.json`. (c) Add a reference to the PROJ-022 design decision or ADR that selected Design Sprint 2.0 methodology — even a PLAN.md section reference is sufficient. |
| 2 | Internal Consistency | 0.93 | 0.96 | Reformat the `reasoning_effort: medium` comment in governance.yaml line 8 as a formal MEDIUM standard deviation declaration: `# MEDIUM standard deviation (ET-M-001): reasoning_effort set to medium (not max) for this worker agent — systematic cognitive mode with fixed 4-day protocol constrains interpretive variance at medium depth. C4 applies to deliverable quality gate, not individual agent reasoning allocation.` |
| 3 | Completeness | 0.94 | 0.96 | Define "existing user research" in the Wave 5 bypass condition (Phase 1 step 1) with a concrete minimum evidence floor (e.g., "minimum 5 user interviews OR 30+ survey responses documented in engagement context"). This makes `verify_wave_entry_criteria_checked` mechanically enforceable. |
| 4 | Actionability | 0.91 | 0.95 | (a) Apply the bypass condition evidence floor from recommendation #3 (dual benefit). (b) Specify source quality expectations for lightning demos (e.g., "prefer primary product blogs, case studies, or design system documentation"). |
| 5 | Evidence Quality | 0.91 | 0.95 | Add a supplementary credibility note for Courtney (2019) acknowledging AJ&Smart's industry adoption track record to support the practitioner-source authority (e.g., "AJ&Smart's Design Sprint 2.0 has been adopted by organizations including Google, Airbnb, and LEGO per AJ&Smart.com"). Optional: add Sprint Book URL `https://www.thesprintbook.com` alongside ISBN for Knapp et al. (2016). |

---

## Iter2 Defect Verification

| Defect from Iter1 | Status | Evidence |
|-------------------|--------|---------|
| 1. Citation URLs/ISBNs missing | RESOLVED | Knapp: ISBN 978-1501121746; Courtney: URL https://ajsmart.com/design-sprint + "not peer-reviewed"; Brown: ISBN 978-0061766084; Nielsen: URL https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ + "not peer-reviewed" |
| 2. Context7 MCP listed under "Tools NOT available" | RESOLVED | Context7 now under "Also available" section (line 112-113); "Tools NOT available" (line 115-117) lists only Task and Memory-Keeper |
| 3. `verify_wave_entry_criteria_checked` missing from post_completion_checks | RESOLVED | Added at governance.yaml line 86 as 13th post_completion_check |
| 4. reasoning_effort informal comment (Priority 3, secondary) | PARTIAL | Comment is now more detailed but still uses inline format rather than formal "MEDIUM standard deviation:" declaration |
| 5. Wave bypass condition vague (Priority 5, not in primary defects) | NOT ADDRESSED | "existing user research" still lacks a concrete minimum evidence threshold |

---

## Leniency Bias Check

- [x] Each dimension scored independently — no dimension pulled up by strong neighbors
- [x] Evidence documented for each score — specific line references quoted per dimension; iter1 baseline used for delta scoring
- [x] Uncertain scores resolved downward — Internal Consistency uncertain at 0.93/0.94 boundary; resolved to 0.93 per leniency bias counteraction rule. Traceability uncertain at 0.84/0.86 boundary; resolved to 0.84.
- [x] Iteration calibration applied — iter2 with 3 defects partially addressed; 0.917 is within expected range for a focused partial-defect-closure iteration
- [x] No dimension scored above 0.95 — highest dimension is Completeness at 0.94, with documented specific evidence
- [x] C4 threshold (0.95) actively applied — composite 0.917 correctly triggers REVISE; the C4 threshold is substantially higher than the standard C2 threshold (0.92) and requires near-perfect execution across all dimensions
- [x] Delta from iter1 validated — +0.033 is proportionate to the three defects addressed (two high-impact: citations +0.013 Evidence Quality, Context7 fix +0.004 Internal Consistency; one medium-impact: post_completion_check +0.002 Completeness; Traceability benefit from Courtney URL: +0.006). Remaining gap to 0.95 is 0.033, reachable in iter3 with focused traceability and internal consistency fixes.

---

## Session Context Handoff Schema

```yaml
verdict: REVISE
composite_score: 0.917
threshold: 0.95
weakest_dimension: traceability
weakest_score: 0.84
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add section anchor to wave-progression.md references (e.g., #wave-5-process-intensives)"
  - "Add [PROVISIONAL] or [EXISTS: verified] annotation to docs/schemas/handoff-v2.schema.json reference"
  - "Add PROJ-022 design decision reference for methodology choice (Design Sprint 2.0 vs. five-day GV Sprint)"
  - "Reformat reasoning_effort comment as formal MEDIUM standard deviation declaration (ET-M-001)"
  - "Define concrete evidence floor for Wave 5 bypass condition (e.g., minimum 5 user interviews OR 30+ survey responses)"
```

---

*Scoring Agent: adv-scorer v1.0.0*
*Rubric: S-014 (LLM-as-Judge) — SSOT: `.context/rules/quality-enforcement.md`*
*Deliverables scored as a unit (dual-file architecture per H-34)*
*Calibration reference: iter1 score 0.884; iter2 delta +0.033*
*Created: 2026-03-04*
