# Quality Score Report: ux-sprint-facilitator (Dual-File Agent Definition)

## L0 Executive Summary

**Score:** 0.949/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.94)

**One-line assessment:** Iter5 substantially improves Evidence Quality — the single blocking defect — by adding specific organization names (Google, LEGO, Lufthansa, United Nations), a quantitative adoption claim (400+ sprints), and an industry-adoption characterization to the Courtney (2019) References table entry; however, the adoption claim is self-reported from AJ&Smart's own published portfolio without independent third-party corroboration, and "The 4-day format has become the dominant practitioner variant, widely adopted by sprint facilitators since 2019" is an unsourced assertion, holding Evidence Quality at 0.94 rather than 0.95 — composite rises from 0.944 to 0.949, landing 0.001 below the C4 threshold of 0.95; single remaining fix: add one independent secondary source corroborating four-day format adoption.

---

## Scoring Context

- **Deliverable:** `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` + `skills/ux-design-sprint/agents/ux-sprint-facilitator.governance.yaml`
- **Deliverable Type:** H-34 dual-file agent definition (worker agent in /ux-design-sprint sub-skill)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 5 (prior scores: iter1 = 0.884, iter2 = 0.917, iter3 = 0.934, iter4 = 0.944)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.949 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Critical Findings** | 0 |
| **Delta from iter4** | +0.005 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.96 | 0.192 | All 7 XML sections; 13 post_completion_checks; bypass condition has concrete evidence floor; all 4 days documented; 3 handoff targets — unchanged from iter4 |
| Internal Consistency | 0.20 | 0.96 | 0.192 | All iter4 consistency items intact; minor unresolved cross-reference (governance.yaml line 8 "per AD-M-009" should read "per ET-M-001") — unchanged from iter4 |
| Methodological Rigor | 0.20 | 0.94 | 0.188 | Day 4 compression note and lightning demo source quality criterion present; user recruitment scheduling requirement ("Day 3 or earlier") still absent from compression note — unchanged from iter4 |
| Evidence Quality | 0.15 | 0.94 | 0.141 | Courtney (2019) References table entry now includes 400+ sprints, named organizations (Google, LEGO, Lufthansa, United Nations), self-reported attribution; adoption claim is self-reported without independent corroboration; "dominant practitioner variant" assertion unsourced; +0.03 improvement from iter4 but short of 0.95 bar |
| Actionability | 0.15 | 0.94 | 0.141 | Lightning demo source quality criterion present; Phase 4 Activity 3 execution ambiguity unresolved — unchanged from iter4 |
| Traceability | 0.10 | 0.95 | 0.095 | Both iter3/iter4 traceability defects remain fully resolved; no new gaps — unchanged from iter4 |
| **TOTAL** | **1.00** | | **0.949** | |

**Composite Calculation:**
(0.96 × 0.20) + (0.96 × 0.20) + (0.94 × 0.20) + (0.94 × 0.15) + (0.94 × 0.15) + (0.95 × 0.10)
= 0.192 + 0.192 + 0.188 + 0.141 + 0.141 + 0.095
= **0.949**

---

## Detailed Dimension Analysis

### Completeness (0.96/1.00)

**Evidence:**
- All 7 required XML sections present: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`.
- governance.yaml `post_completion_checks` has 13 entries including `verify_wave_entry_criteria_checked` (line 86).
- Wave 5 bypass condition in Phase 1 step 1 specifies "minimum 5 user interviews OR 30+ survey responses documented in engagement context" — concrete, enforceable floor.
- Five phases with 33+ explicit activities; S-010 self-review checklist (14 items); AI facilitation limitations section (6 items); Single-Facilitator Reliability Note present.
- Three downstream handoff targets with full YAML schemas.
- `session_context` on_receive (6 items) and on_send (10 items) fully specified.
- Constitutional triplet (P-003, P-020, P-022) in both `forbidden_actions` and `principles_applied`.
- Description under 1024 characters, contains WHAT+WHEN+triggers per H-26.
- `disallowedTools: [Task]` present; `model: opus` declared.
- No regression from iter4; iter5 References table addition does not alter completeness ceiling.

**Gaps:**
- `character` field under `persona` in governance.yaml is absent. Per AD-M-006, `character` is optional-RECOMMENDED. Unchanged from iter4.

**Improvement Path:**
- Add `character: "AI-augmented facilitator maintaining procedural rigor across all four sprint phases; discloses facilitation limitations and defers to Decider authority at all decision points"` to governance.yaml persona block. Low-priority; not blocking PASS at the current margin.

---

### Internal Consistency (0.96/1.00)

**Evidence:**
- governance.yaml line 8 carries formal MEDIUM standard deviation declaration with ET-M-001 reference, justification rationale, and C4 scope distinction. Unchanged.
- Context7 MCP tools listed under `**Also available:**` (lines 112-113 in .md; lines 41-42 in governance.yaml `allowed_tools`); `**Tools NOT available:**` (lines 115-117) correctly lists only Task and Memory-Keeper.
- Handoff confidence calibration values (0.65/0.75/0.85) are coherent with the on_send protocol.
- Pattern strength thresholds (>= 3/5 users = strong) cited consistently in identity expertise, Phase 4 methodology, and observation grid output specification.
- All governance.yaml fields align with .md body: `tool_tier: T3` matches declared tools; `output.levels: [L0, L1, L2]` matches output specification; `fallback_behavior: warn_and_retry` matches fallback section.
- The iter5 References table change (Courtney entry extended) does not introduce any inconsistency — the new content is additive to the existing Content cell and consistent with the "practitioner resource (not peer-reviewed)" characterization retained in the same entry.
- No new inconsistencies introduced by iter5 change.

**Gaps:**
- governance.yaml line 8 comment still reads "Override requires documented justification per AD-M-009." AD-M-009 governs model selection; ET-M-001 governs reasoning_effort. Non-material cross-reference imprecision. Unchanged from iter4.

**Improvement Path:**
- Correct governance.yaml line 8 comment: change "per AD-M-009" to "per ET-M-001." Single-token fix, low priority.

---

### Methodological Rigor (0.94/1.00)

**Evidence:**
- Day 4 compression note at lines 178-179 describes morning/afternoon structure: "Prototype construction occurs in the morning; user testing in the afternoon." Discloses format divergence from GV Sprint.
- Lightning demo source quality criterion at line 149: "Source quality criterion: prefer documented case studies, published design teardowns, or verifiable product examples over anecdotal or unsourced references."
- Day 1 (9 activities), Day 2 (4 activities), Day 3 (6 activities), Day 4 (7 activities), Synthesis (7 activities) — all with explicit inputs and outputs.
- Quantitative thresholds intact: >= 3/5 users for strong theme, 10-16 storyboard panels, 5 user interviews, 60-minute interview structure (5+5+30+15+5 min).
- Decider authority model handles designated and undesignated Decider edge cases.
- Unchanged from iter4.

**Gaps:**
- The Day 4 compression note still does NOT include the user recruitment scheduling requirement ("User recruitment MUST be arranged during Day 3 or earlier"). This operational requirement was identified in iter3 and remains absent from the note in iter5. The structural consequence of compression (morning/afternoon structure) is disclosed; the scheduling implication is not.
- The iter5 change (References table update) does not affect Methodological Rigor — this dimension tracks methodology procedural completeness, not evidence citation quality.

**Improvement Path:**
- Extend the Day 4 compression note (lines 178-179 block) with one sentence: "User recruitment MUST be arranged during Day 3 or earlier, as prototype construction and user testing are both scheduled on Day 4." This closes the remaining scheduling gap.

---

### Evidence Quality (0.94/1.00)

**Evidence:**
Iter5 adds the following to the Courtney (2019) References table Content cell (line 526):

> "Practitioner resource (not peer-reviewed); adoption breadth: AJ&Smart has facilitated 400+ design sprints for organizations including Google, LEGO, Lufthansa, and the United Nations (per AJ&Smart published portfolio). The 4-day format has become the dominant practitioner variant, widely adopted by sprint facilitators since 2019."

This is a substantial improvement over iter4's References table entry (which was silent on adoption breadth) and over the Single-Facilitator Reliability Note phrase added in iter4 (which characterized methodology provenance without adding adoption evidence).

Specific improvements made:
1. Quantitative adoption claim: "400+ design sprints" — specific and falsifiable
2. Named organizations: Google, LEGO, Lufthansa, United Nations — four distinct, verifiable, high-profile organizations
3. Source attribution: "per AJ&Smart published portfolio" — explicit provenance for the claim
4. Industry-adoption characterization: "dominant practitioner variant, widely adopted by sprint facilitators since 2019"

All four prior citations retain verifiable identifiers:
- Knapp et al. (2016): ISBN 978-1501121746
- Courtney (2019): URL ajsmart.com/design-sprint, "Practitioner resource (not peer-reviewed)"
- Brown (2009): ISBN 978-0061766084
- Nielsen (2000): URL nngroup.com/articles/why-you-only-need-to-test-with-5-users/, "Practitioner resource (not peer-reviewed)"

**Why Evidence Quality reaches 0.94 and not 0.95:**

The rubric at 0.9+: "All claims with credible citations." Two of four sources remain practitioner-only (Courtney, Nielsen). That is an inherent ceiling acknowledged since iter1. The iter5 fix addresses it via adoption-breadth evidence but with two limitations that prevent reaching 0.95:

1. **Self-reported attribution.** The 400+ sprints claim and the named organizations are sourced exclusively from "AJ&Smart published portfolio" — AJ&Smart is itself the subject of the claim. Self-reported adoption data is credible in context (practitioners routinely self-disclose client portfolios) but does not constitute independent corroboration. The rubric's 0.9+ criterion requires credibility across claims; self-report reduces the credibility tier of this specific claim.

2. **Unsourced industry-wide assertion.** "The 4-day format has become the dominant practitioner variant, widely adopted by sprint facilitators since 2019" makes a broad industry claim ("dominant," "sprint facilitators" generally) with no citation. This is not attributed to AJ&Smart's portfolio — it is a standalone assertion about the design sprint community at large. The iter4 recommendation explicitly identified a secondary source path: "cite a secondary practitioner source that corroborates the four-day format." That secondary source was not added.

**Leniency counteraction ruling:** At the 0.94/0.95 boundary with two specific defects identified (self-reported attribution, unsourced industry assertion), per the leniency counteraction rule ("when uncertain between adjacent scores, choose the LOWER one"), Evidence Quality is scored at 0.94.

**Evidence tier comparison:**
- Iter4 (0.91): No organization names, no adoption evidence, description of methodology provenance category only
- Iter5 (0.94): Specific org names, quantitative claim, self-reported attribution, unsourced industry adoption assertion
- Required for 0.95: Independent third-party corroboration OR attributed secondary source for the "dominant practitioner variant" claim

**Gaps:**
- "The 4-day format has become the dominant practitioner variant, widely adopted by sprint facilitators since 2019" — no citation for this industry-level claim
- Adoption claim is self-reported (AJ&Smart's own portfolio) without independent corroboration
- No secondary source added per iter4's "alternatively or additionally" recommendation

**Improvement Path:**
- Add a secondary source citation for the industry-adoption characterization. Options:
  - A published conference proceedings or practitioner journal article describing Design Sprint 2.0 application
  - The Sprint Stories publication or AJ&Smart Sprint Conference proceedings (if citable by title/date)
  - Attribute the "dominant practitioner variant" sentence: add "(per [secondary source name/URL])" or remove the unsourced industry-scope assertion and rely only on the attributed AJ&Smart portfolio claim
  - Minimum viable fix: remove "The 4-day format has become the dominant practitioner variant, widely adopted by sprint facilitators since 2019" (unsourced assertion) and replace with a cited source, OR add "(per AJ&Smart, 2023)" or similar attribution to make it a named-source claim rather than a floating assertion

---

### Actionability (0.94/1.00)

**Evidence:**
- Lightning demo source quality criterion at line 149 resolves the iter3 primary actionability gap.
- 5-phase workflow with 33+ explicit activities providing a clear execution path.
- Observation grid, storyboard, and assumption inventory table structures fully specified with column schemas.
- Handoff YAML schemas include all required fields.
- Fallback behavior covers 7 specific conditions with concrete responses.
- Degraded mode behavior explicitly defined with formatted disclosure template.
- On-send protocol provides a fully-typed YAML schema for orchestrator consumption.
- Unchanged from iter4.

**Gaps:**
- Phase 4 Activity 3 (line 188) reads: "Conduct structured interviews with 5 representative users (Nielsen, 2000)." The subject of "conduct" is ambiguous — the AI limitations section (lines 245-246) clarifies "User interviews require real users" and "The team must recruit and interview 5 representative users," but this clarification is sections away from the activity step. Unchanged from iter4.

**Improvement Path:**
- Add one line to Phase 4 Activity 3 start: "The team conducts interviews with real users; this agent provides the structured protocol, observation grid, and analysis framework." Resolves execution ambiguity at the activity level and eliminates the need to cross-reference the AI limitations section during facilitation.

---

### Traceability (0.95/1.00)

**Evidence:**
- Both iter3/iter4 traceability defects remain fully resolved:
  - Anchor `#wave-definitions` at line 132 resolves to `## Wave Definitions` in wave-progression.md (verified in iter4, no regression)
  - `[PROVISIONAL: schema file does not yet exist in repository; referenced as planned artifact by governance.yaml session_context.schema]` at footer line 540 remains accurate
- Footer traceability comment at line 540 covers 14 standards including PROJ-022 PLAN.md reference.
- governance.yaml header references `docs/schemas/agent-governance-v1.schema.json`.
- Parent skill and sub-skill SSOT references in footer with version numbers.
- In-text citations retain chapter-level specificity (Chapter 4, Chapter 14).
- The iter5 References table addition does not affect Traceability — no new cross-references introduced that could be broken.
- No regression from iter4.

**Gaps:**
- No active traceability gaps. The iter3 Gap 3 (no formal ADR for methodology choice) remains mitigated by PROJ-022 PLAN.md / ORCHESTRATION.yaml Pipeline 6 reference — accepted as sufficient.
- The AD-M-009 vs. ET-M-001 citation imprecision in governance.yaml line 8 is classified under Internal Consistency, not Traceability.

**Improvement Path:**
- No priority improvements needed for Traceability. Dimension is at 0.95 — at the C4 passing threshold.

---

## Iter5 Defect Verification

| Defect from Iter4 | Status | Evidence |
|-------------------|--------|---------|
| 1. Courtney (2019) adoption credibility note absent from References table | PARTIAL — SUBSTANTIAL BUT SHORT | References table Content cell now includes "400+ design sprints for organizations including Google, LEGO, Lufthansa, and the United Nations (per AJ&Smart published portfolio)" and "The 4-day format has become the dominant practitioner variant, widely adopted by sprint facilitators since 2019" — specific org names and quantitative claim added, but claim is self-reported and "dominant practitioner variant" assertion is unsourced industry claim |
| 2. User recruitment scheduling requirement absent from Day 4 compression note | UNRESOLVED | Lines 178-179 Day 4 compression note still describes morning/afternoon structure only; "User recruitment MUST be arranged during Day 3 or earlier" not present — unchanged from iter4 |
| 3. Phase 4 Activity 3 execution ambiguity | UNRESOLVED | Line 188 still reads "Conduct structured interviews with 5 representative users (Nielsen, 2000)" without explicit team-executes statement — unchanged from iter4 |
| 4. governance.yaml line 8 "per AD-M-009" should read "per ET-M-001" | UNRESOLVED | Governance.yaml line 8 comment unchanged — minor, unchanged from iter4 |

---

## Score Delta Analysis

| Iteration | Evidence Quality | Composite | Delta |
|-----------|-----------------|-----------|-------|
| iter1 | — | 0.884 | baseline |
| iter2 | — | 0.917 | +0.033 |
| iter3 | — | 0.934 | +0.017 |
| iter4 | 0.91 | 0.944 | +0.010 |
| iter5 | 0.94 | 0.949 | +0.005 |
| Required for PASS | 0.95+ | 0.950 | +0.001 |

The iter5 fix raises Evidence Quality from 0.91 to 0.94 (+0.03 improvement in the dimension, +0.005 composite). The deliverable is 0.001 below the C4 threshold of 0.95. A single targeted change — attributing the "dominant practitioner variant" assertion or removing it in favor of a cited secondary source — is sufficient to cross the threshold.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.94 | 0.95 | In the Courtney (2019) References table Content cell, either: (a) attribute "The 4-day format has become the dominant practitioner variant, widely adopted by sprint facilitators since 2019" with a secondary source citation (e.g., a published case study, conference proceedings, or named AJ&Smart publication with date), OR (b) remove this unsourced industry-scope assertion and retain only the attributed AJ&Smart portfolio claim. Either path eliminates the unsourced assertion that is the single gap between 0.94 and 0.95. |
| 2 | Methodological Rigor | 0.94 | 0.96 | Extend Day 4 compression note (lines 178-179) with: "User recruitment MUST be arranged during Day 3 or earlier, as prototype construction and user testing are both scheduled on Day 4." |
| 3 | Actionability | 0.94 | 0.95 | Add one line to Phase 4 Activity 3: "The team conducts interviews with real users; this agent provides the structured protocol, observation grid, and analysis framework." |
| 4 | Internal Consistency | 0.96 | 0.97 | Correct governance.yaml line 8 comment from "per AD-M-009" to "per ET-M-001." |
| 5 | Completeness | 0.96 | 0.97 | Add `character` field to governance.yaml persona block per AD-M-006 optional-RECOMMENDED pattern. Very low priority. |

### Minimum Viable Fix for PASS

Priority 1 alone is mathematically sufficient:

| Scenario | Evidence Quality | Composite | Verdict |
|----------|-----------------|-----------|---------|
| Current (iter5) | 0.94 | 0.949 | REVISE |
| Fix Priority 1 only | 0.95 | 0.950 | PASS (exactly) |
| Fix Priority 1+2 | 0.95 | 0.952 | PASS (with margin) |
| Fix Priority 1+2+3 | 0.95 | 0.953 | PASS (with margin) |

---

## Leniency Bias Check

- [x] Each dimension scored independently — iter5 change evaluated only for its direct impact on Evidence Quality; no pull-up from adjacent dimensions
- [x] Evidence documented for each score — specific line reference (line 526) cited for the iter5 fix; exact text quoted in Evidence Quality analysis; two specific defects (self-reported attribution, unsourced assertion) documented with location
- [x] Uncertain scores resolved downward — Evidence Quality uncertain at 0.94/0.95 boundary with two identified defects; resolved to 0.94 per leniency counteraction rule ("when uncertain between adjacent scores, choose the LOWER one")
- [x] First-draft calibration not applicable — iter5 (fifth revision); calibration applied against iter4 baseline
- [x] No dimension scored above 0.96 without exceptional evidence — highest dimension (Completeness, Internal Consistency) at 0.96 with specific line-level evidence cited
- [x] Iter5 fix evaluated critically against specific iter4 recommendation — recommendation was "Add adoption credibility note to References table: cite AJ&Smart client portfolio or published case studies to add adoption-breadth evidence above practitioner-source baseline"; fix adds AJ&Smart client portfolio evidence (satisfies primary recommendation) but does not add independent secondary source (satisfies "alternatively" path only partially); the "dominant practitioner variant" assertion is new and unsourced, introducing a new gap not present in iter4
- [x] Composite arithmetic self-checked: (0.96×0.20) + (0.96×0.20) + (0.94×0.20) + (0.94×0.15) + (0.94×0.15) + (0.95×0.10) = 0.192 + 0.192 + 0.188 + 0.141 + 0.141 + 0.095 = 0.949
- [x] C4 threshold (0.95) actively applied — composite 0.949 correctly triggers REVISE; the 0.001 gap is real and attributable to a specific unsourced assertion in the Courtney (2019) entry that can be fixed with a single targeted edit

---

## Session Context Handoff Schema

```yaml
verdict: REVISE
composite_score: 0.949
threshold: 0.95
weakest_dimension: evidence_quality
weakest_score: 0.94
critical_findings_count: 0
iteration: 5
improvement_recommendations:
  - "Attribute or remove unsourced 'dominant practitioner variant' assertion in Courtney (2019) References table entry: add secondary source citation OR remove the assertion; this is the single change needed to cross 0.95 threshold"
  - "Extend Day 4 compression note with user recruitment scheduling: 'User recruitment MUST be arranged during Day 3 or earlier'"
  - "Add explicit team-executes statement at Phase 4 Activity 3: 'The team conducts interviews with real users; this agent provides the structured protocol, observation grid, and analysis framework'"
  - "Minor: correct governance.yaml line 8 comment cross-reference from AD-M-009 to ET-M-001"
```

---

*Scoring Agent: adv-scorer v1.0.0*
*Rubric: S-014 (LLM-as-Judge) — SSOT: `.context/rules/quality-enforcement.md`*
*Deliverables scored as a unit (dual-file architecture per H-34)*
*Calibration reference: iter1 = 0.884, iter2 = 0.917, iter3 = 0.934, iter4 = 0.944, iter5 = 0.949 (delta +0.005)*
*Created: 2026-03-04*
