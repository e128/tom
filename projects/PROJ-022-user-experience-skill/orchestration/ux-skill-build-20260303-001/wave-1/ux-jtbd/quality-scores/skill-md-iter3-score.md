# Quality Score Report: JTBD Sub-Skill SKILL.md (Iteration 3)

## L0 Executive Summary

**Score:** 0.924/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Actionability (0.86)
**One-line assessment:** All five iter3 fixes were correctly applied and verified, raising the composite from 0.897 to 0.924, but the C4 threshold of 0.95 remains unmet — the binding constraint is Actionability (0.86, unchanged because no actionability fixes were in scope for iter3), with secondary constraints from the supplementary Moesta/Spiek 2014 citation still lacking a specific publication title and the VERSION SOURCE field imprecision.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/SKILL.md`
- **Deliverable Type:** Sub-skill SKILL.md definition file for `/ux-jtbd` (Jobs-to-Be-Done)
- **Criticality Level:** C4
- **Quality Gate Threshold:** 0.95 (C4 requirement per scoring brief; standard H-13 threshold is 0.92)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Skill Standards Reference:** `.context/rules/skill-standards.md`
- **Prior Score (iter2):** 0.897 (REVISE)
- **Prior Score (iter1):** 0.851 (REVISE)
- **Iteration:** 3
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.924 |
| **Threshold** | 0.95 (C4, per scoring brief) |
| **Verdict** | REVISE |
| **Gap to Threshold** | 0.026 |
| **Strategy Findings Incorporated** | Yes — iter2 score report (`skills/ux-jtbd/output/quality-scores/skill-md-iter2-score.md`) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | Handoff-v2 disclaimer applied at both occurrences; Project Traceability subsection added; no output template created and no invocation clarification note added (iter2 gaps P5/P6 not in scope for iter3) |
| Internal Consistency | 0.20 | 0.93 | 0.186 | "Target behavior" note added at Methodology section header (line 234) — matches Purpose section disclosure; present-tense "The analyst follows" throughout methodology still creates minor tense gap despite the header note |
| Methodological Rigor | 0.20 | 0.95 | 0.190 | All three iter2 methodology gaps resolved: Christensen 2016 "Competing Against Luck" as primary (line 242), Moesta 2020 "Demand-Side Sales 101" as primary (line 244), third Ulwick format present (line 357); supplementary Moesta/Spiek 2014 "Re-Wired Group" citation still lacks specific publication title |
| Evidence Quality | 0.15 | 0.93 | 0.1395 | Handoff-v2 disclaimer at lines 446 and 582 resolves the broken traceability claim; Christensen 2016 and Moesta 2020 primary citations are now fully traceable; supplementary "Re-Wired Group (2014)" lacks a specific traceable document |
| Actionability | 0.15 | 0.86 | 0.129 | No actionability-specific fixes in iter3 scope; missing output template and invocation clarification note persist unchanged from iter2 |
| Traceability | 0.10 | 0.94 | 0.094 | Handoff-v2 disclaimer resolves broken link; Project Traceability subsection (lines 584-590) adds explicit links to PLAN.md, EPIC-002, ORCHESTRATION.yaml; VERSION SOURCE field still lists parent SKILL.md (minor imprecision, unchanged) |
| **TOTAL** | **1.00** | | **0.9245** | |

**Composite (rounded):** 0.924

**Arithmetic verification:**
(0.93 × 0.20) + (0.93 × 0.20) + (0.95 × 0.20) + (0.93 × 0.15) + (0.86 × 0.15) + (0.94 × 0.10)
= 0.186 + 0.186 + 0.190 + 0.1395 + 0.129 + 0.094
= **0.9245**

---

## Iter3 Fix Verification

The following table documents each claimed iter3 fix with verification status against the actual document:

| Claimed Fix | Location | Actually Applied? | Evidence |
|-------------|----------|-------------------|---------|
| `handoff-v2.schema.json` annotated "(planned — not yet committed to repository)" | Lines 446, 582 | YES — both occurrences fixed | Line 446: "...(`docs/schemas/handoff-v2.schema.json` — planned; not yet committed to repository)." Line 582: References table entry annotated with "(planned — not yet committed to repository)" |
| Christensen et al. 2016 "Competing Against Luck" as primary | Line 242 | YES | Theoretical Foundations table row 1: "Clayton Christensen et al. (2016)" as Originator; References section line 596 shows full citation: "Christensen, C.M., Dillon, K., Hall, T., Duncan, D.S. (2016). *Competing Against Luck*. Harper Business." |
| "The Innovator's Solution" 2003 demoted to precursor | Line 597 | YES (additional improvement) | New "Jobs-to-Be-Done Theory (foundational precursor)" row added for Christensen (2003) — beyond what was required |
| Moesta 2020 "Demand-Side Sales 101" as primary | Line 244 | YES | Theoretical Foundations table row 3: "Bob Moesta (2020)" as Originator; References section line 599 shows "Moesta, B. (2020). *Demand-Side Sales 101*. Lioncrest Publishing." |
| Third Ulwick outcome format "Minimize the variability of [quality measure]" | Line 357 | YES | Phase 4 activities list item 2 now shows all three formats: "Minimize the time it takes to...", "Minimize the likelihood of...", "Minimize the variability of [quality measure]" |
| "Target behavior" note at Methodology section header | Line 234 | YES | Blockquote note: "> **Note:** This methodology section describes target behavior for the fully-implemented `ux-jtbd-analyst` agent. The current agent definition is a Wave 1 stub; full implementation will follow this specification." |
| Requirements Traceability subsection added | Lines 584-590 | YES | "### Project Traceability" subsection in References section with three entries: PLAN.md, EPIC-002, ORCHESTRATION.yaml |

**All 5 primary iter3 fixes verified as correctly applied.**

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**

Iter2's primary completeness gap — the bare `handoff-v2.schema.json` reference — is now resolved at both occurrences. The fix is correct and complete:
- Line 446 (Cross-Framework Integration paragraph): "...via the Jerry handoff protocol (`docs/schemas/handoff-v2.schema.json` — planned; not yet committed to repository)."
- Line 582 (References table): Annotated with "(planned — not yet committed to repository)"

The Project Traceability subsection adds a new completeness element that was absent in iter2: explicit links to the project plan, parent work item, and orchestration plan. This is a net positive addition beyond the required iter3 fixes.

**Remaining gaps:**

1. **No output template:** `skills/ux-jtbd/references/ux-jtbd-output-template.md` was not created. The Output Specification section (lines 410-441) lists required sections but a developer must construct the output format from scratch. This was flagged as Priority 6 in iter2 recommendations and was not in scope for iter3.

2. **No invocation clarification note:** The "Invoking an Agent" section still does not clarify when direct invocation (Options 2/3) is appropriate vs. going through the ux-orchestrator. This was Priority 5 in iter2 recommendations and was not in scope for iter3.

3. **AGENTS.md registration unverified:** The claim at line 206 that "the `ux-jtbd-analyst` agent IS registered in `AGENTS.md` under the User-Experience Skill Agents section" was not verified in iter3 scoring. This is a carry-forward gap from iter2 (iter2 Priority 7).

**Score rationale:** 0.93 — the primary handoff-v2 disclaimer gap is resolved (+0.01 from iter2's 0.92); the three minor gaps above prevent reaching 0.95+. Applying anti-leniency between 0.92 and 0.93, the evidence supports 0.93.

**Improvement Path:**
- Create `skills/ux-jtbd/references/ux-jtbd-output-template.md` with the expected output artifact structure
- Add guidance note in "Invoking an Agent" section clarifying when each option is appropriate
- Verify `AGENTS.md` contains `ux-jtbd-analyst` in the User-Experience Skill Agents section

---

### Internal Consistency (0.93/1.00)

**Evidence:**

Iter2's tense inconsistency gap is directly addressed. The Methodology section header now carries the blockquote note at line 234:

> "**Note:** This methodology section describes target behavior for the fully-implemented `ux-jtbd-analyst` agent. The current agent definition is a Wave 1 stub; full implementation will follow this specification."

This creates a consistent framing pair: the Purpose section discloses the stub state (line 91-92), and now the Methodology section also explicitly frames all content as target behavior. The document is now internally consistent about the agent's current implementation state at both locations where methodology is described.

**Remaining minor tension:**

Within the Methodology section, the body text continues in present operational tense: "The analyst follows a 5-phase sequential workflow" (line 268), "The four forces model explains" (line 309), "Job mapping follows Ulwick's ODI methodology" (line 339). The section-level note hedges this, but an engineer reading quickly could still misread the sub-sections as describing current agent behavior. This is a stylistic precision issue, not a substantive contradiction.

**Score rationale:** 0.93 — the major tense inconsistency gap at the section level is resolved; the per-paragraph tense convention throughout the methodology body is an accepted minor residual. The note is clear enough that informed readers will understand the target-state framing. Applying anti-leniency: 0.93 not 0.94.

**Improvement Path:**
- Consider a consistent "(planned)" annotation on the first sentence of each Phase heading within the Methodology section body — e.g., "Phase 1 (planned): Context Gathering" — though this may reduce readability.

---

### Methodological Rigor (0.95/1.00)

**Evidence:**

All three iter2 methodology gaps are now resolved:

**1. Christensen 2016 "Competing Against Luck" (FIXED):**
The Theoretical Foundations table row 1 now reads: "Jobs-to-Be-Done Theory | Clayton Christensen et al. (2016) | Products are 'hired' for jobs; innovation comes from understanding why | Job statement format and hiring criteria identification." The 2003 "Innovator's Solution" has been added as a separate "foundational precursor" row, which is an accurate and sophisticated distinction. The full References section entry (line 596) provides the complete citation.

**2. Moesta 2020 "Demand-Side Sales 101" (FIXED):**
The Theoretical Foundations table row 3 now reads: "Switch Interview Framework | Bob Moesta (2020) | Four forces drive switching behavior: push, pull, anxiety, habit". The References section (line 599) provides: "Moesta, B. (2020). *Demand-Side Sales 101*. Lioncrest Publishing." This is the canonical primary source for the switch interview framework.

**3. Third Ulwick outcome format (FIXED):**
Phase 4 activities list item 2 (line 354-357) now reads:
- "Minimize the time it takes to [step action]"
- "Minimize the likelihood of [undesired outcome]"
- "Minimize the variability of [quality measure]"

All three Ulwick canonical outcome statement types are present and correctly labeled. The parenthetical "[quality measure]" is slightly more precise than "[step action]" for the third format — consistent with Ulwick's framing in "Jobs to Be Done: Theory to Practice".

**Remaining minor gap:**

The supplementary Moesta/Spiek citation at line 600 reads: "Moesta, B. and Spiek, C. Re-Wired Group (2014). See also: Klement, A. (2016). *When Coffee and Kale Compete*." The "Re-Wired Group (2014)" has no specific traceable publication title. This is now explicitly "supplementary" so it does not drive the primary methodology attribution. However, a rigorous methodology section should not cite an organization reference without a specific artifact. This is a minor evidence precision issue that does not undermine methodological correctness.

**Score rationale:** 0.95 — all three primary methodology fixes are verified and correctly applied. The 2003/2016 Christensen distinction is handled with sophisticated precision. The supplementary Moesta/Spiek 2014 citation gap is a minor evidence issue (handled in Evidence Quality) that does not reduce Methodological Rigor below 0.95.

---

### Evidence Quality (0.93/1.00)

**Evidence:**

**handoff-v2.schema.json (FIXED):** The primary evidence defect from iter2 is resolved. Both occurrences of the handoff schema reference now carry the "(planned — not yet committed to repository)" qualifier. This is honest, accurate, and removes the false traceability claim that was penalizing Evidence Quality in iter2.

**Christensen and Moesta primary citations (FIXED):** The primary JTBD framework sources are now fully traceable:
- Christensen, C.M., Dillon, K., Hall, T., Duncan, D.S. (2016). *Competing Against Luck*. Harper Business.
- Moesta, B. (2020). *Demand-Side Sales 101*. Lioncrest Publishing.

Both are ISBN-traceable published books with publisher attributions. This is the highest evidentiary standard for a SKILL.md document.

**Remaining weakness:**

Supplementary citation at line 600: "Moesta, B. and Spiek, C. Re-Wired Group (2014)." — organization reference without a specific traceable artifact (article, white paper, talk, or blog post). This is explicitly labeled supplementary, but the evidence standard for a supplementary citation should still be a specific named artifact. The 2014 date is likely a reference to Moesta/Spiek's Re-Wired Group workshop materials or podcast content, none of which is named.

**Score rationale:** 0.93 — the two primary evidence defects (handoff-v2 and citation precision) are resolved, raising from iter2's 0.88. The supplementary citation weakness prevents 0.95+. Applying anti-leniency between 0.92 and 0.94: 0.93.

**Improvement Path:**
- Replace "Moesta, B. and Spiek, C. Re-Wired Group (2014)" with a specific traceable reference — e.g., a named podcast episode, article, or workshop description with a URL or formal citation.

---

### Actionability (0.86/1.00)

**Evidence:**

No actionability-specific fixes were applied in iter3. The iter3 scope was: handoff-v2 disclaimer, citation corrections, third Ulwick format, methodology header note, requirements traceability. None of these directly address the actionability gaps identified in iter2.

The actionability strengths from iter2 remain intact:
- "Invoking an Agent" section with three concrete invocation methods and Task tool code block (lines 151-209)
- 5-phase sequential workflow with activities and outputs per phase
- Quick Reference with copy-paste command examples

The actionability gaps from iter2 remain unaddressed:

1. **No invocation guidance note:** The "Invoking an Agent" section still does not clarify when Options 1/2/3 are appropriate. A developer could invoke `ux-jtbd-analyst` directly via Option 2 without the orchestrator context, bypassing wave gating and lifecycle-stage triage. The document does not warn against this.

2. **No output template:** `skills/ux-jtbd/references/ux-jtbd-output-template.md` does not exist. The Output Specification section lists required sections but a practitioner constructing a JTBD analysis output must derive the format from the section descriptions rather than from a ready-to-use template.

**Score rationale:** 0.86 — unchanged from iter2. The actionability gap is structural (missing artifacts and guidance text), not addressable through citation or consistency fixes. This is the single most impactful dimension for closing the gap to the 0.95 threshold.

**Improvement Path:**
1. (High impact) Create `skills/ux-jtbd/references/ux-jtbd-output-template.md` with a complete output skeleton
2. (Medium impact) Add to the "Invoking an Agent" section: "Option 1 and 2 are for user-initiated requests through the `/user-experience` parent skill orchestrator. Option 3 is for orchestrator-to-agent dispatch. Direct invocation via Option 2 without an established engagement context bypasses wave gating and lifecycle-stage triage; only use when engagement is already established via the parent orchestrator."

---

### Traceability (0.94/1.00)

**Evidence:**

**Handoff-v2.schema.json (FIXED):** The broken traceability link at lines 446 and 582 is resolved. The "(planned — not yet committed to repository)" qualifier is present at both occurrences. This was the single most significant traceability defect in iter2.

**Project Traceability subsection (NEW):** Lines 584-590 add an explicit requirements traceability chain:
- `projects/PROJ-022-user-experience-skill/PLAN.md` — project plan
- EPIC-002 (Wave 1 deployment) — parent work item
- `projects/PROJ-022-user-experience-skill/orchestration/ux-skill-build-20260303-001/ORCHESTRATION.yaml` — orchestration plan

This is a significant positive addition. SKILL.md documents rarely include explicit upstream requirements traceability to their parent project plan and orchestration context.

**Verified accurate cross-references (from iter2, carried forward):**
- `skills/user-experience/rules/ux-routing-rules.md [Stage Routing Table]` — verified
- `skills/user-experience/rules/mcp-coordination.md [MCP Dependency Matrix]` — verified
- P-003 `disallowedTools: [Task]` claim — verified in agent file
- `ci-checks.md` P-003 enforcement claim — verified

**Remaining minor imprecision:**

VERSION comment at line 604: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/SKILL.md | PARENT: /user-experience skill -->` — the SOURCE field identifies the design source (parent SKILL.md) rather than the primary work item or creating agent. This is an acceptable convention but slightly imprecise as a provenance record. The footer (line 611) correctly attributes "Agent: ux-jtbd-analyst".

**Score rationale:** 0.94 — the handoff-v2 broken link is resolved and the Project Traceability addition is a genuine improvement beyond iter2's coverage. The VERSION SOURCE field imprecision prevents 0.95+. Applying anti-leniency: 0.94.

---

## Score Delta Analysis (All Iterations)

| Dimension | Iter1 | Iter2 | Iter3 | Delta (iter2→3) | Change Explanation |
|-----------|-------|-------|-------|-----------------|---------------------|
| Completeness | 0.75 | 0.92 | 0.93 | +0.01 | Handoff-v2 disclaimer resolves binding gap; Project Traceability added |
| Internal Consistency | 0.88 | 0.92 | 0.93 | +0.01 | "Target behavior" note at Methodology section header resolves tense inconsistency |
| Methodological Rigor | 0.90 | 0.90 | 0.95 | +0.05 | All three citation/format fixes applied: Christensen 2016, Moesta 2020, third Ulwick format |
| Evidence Quality | 0.87 | 0.88 | 0.93 | +0.05 | Handoff-v2 disclaimer + primary citation corrections eliminate broken evidence chain |
| Actionability | 0.84 | 0.86 | 0.86 | 0.00 | No actionability-specific fixes in iter3 scope |
| Traceability | 0.88 | 0.88 | 0.94 | +0.06 | Handoff-v2 disclaimer + Project Traceability subsection added |
| **Composite** | **0.851** | **0.897** | **0.924** | **+0.027** | |

**Composite arithmetic verification:**
(0.93 × 0.20) + (0.93 × 0.20) + (0.95 × 0.20) + (0.93 × 0.15) + (0.86 × 0.15) + (0.94 × 0.10)
= 0.186 + 0.186 + 0.190 + 0.1395 + 0.129 + 0.094
= **0.9245**

Rounded to 3 decimal places: **0.924**. Rounded DOWN per anti-leniency rule: **0.924**.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Actionability | 0.86 | 0.93 | Create `skills/ux-jtbd/references/ux-jtbd-output-template.md` with a complete output skeleton (L0 summary table, L1 job inventory section, L1 switch force section, L1 job map section, L2 strategic implications section, Synthesis Judgments Summary placeholder, Validation Required placeholder). This single artifact closes the largest remaining actionability gap. |
| 2 | Actionability | 0.86 | 0.93 | Add to "Invoking an Agent" section (after line 207): "**When to use each option:** Options 1 and 2 are for user-initiated requests routed through the `/user-experience` parent skill orchestrator. Option 3 is for orchestrator-to-agent dispatch only. Direct invocation via Option 2 without an established engagement context bypasses wave gating and lifecycle-stage triage; only use after engagement has been established via the parent orchestrator." |
| 3 | Evidence Quality | 0.93 | 0.95 | Replace line 600 "Moesta, B. and Spiek, C. Re-Wired Group (2014)" with a specific traceable artifact — e.g., a named blog post, podcast episode, or conference talk with a URL or formal citation. The most commonly cited Re-Wired Group reference is Moesta and Spiek's work published on the re-wiredgroup.com blog or the Jobs-to-Be-Done podcast. |
| 4 | Internal Consistency | 0.93 | 0.95 | Consider adding "(planned — target behavior)" notation to the Evaluation Workflow section heading (line 266) and each Phase heading, to make the "target behavior" framing consistent throughout all methodology body sections, not just the section-level header. |
| 5 | Completeness / Traceability | 0.93 / 0.94 | 0.95 | Verify that `AGENTS.md` contains `ux-jtbd-analyst` in the User-Experience Skill Agents section (per the claim at line 206). If absent, add it. |
| 6 | Traceability | 0.94 | 0.95 | Consider updating the VERSION comment SOURCE field from "SOURCE: skills/user-experience/SKILL.md" to "SOURCE: PROJ-022-user-experience-skill/PLAN.md" to improve provenance precision. |

---

## Gap to C4 Threshold Analysis

**Current composite:** 0.924
**Required threshold:** 0.950
**Gap:** 0.026

The gap cannot be closed by fixing a single dimension. Sensitivity analysis:

| Scenario | Change | New Composite |
|----------|--------|---------------|
| Actionability from 0.86 to 0.95 | +0.09 × 0.15 = +0.0135 | 0.938 |
| Actionability to 0.95 + Evidence to 0.95 | above + 0.02 × 0.15 = +0.003 | 0.941 |
| All dims except Actionability to 0.95 | varied | ~0.942 |
| Actionability 0.95, all other dims 0.95 | all at 0.95 | 0.950 |

**Conclusion:** All dimensions except Methodological Rigor (already at 0.95) need to reach 0.95 to clear the threshold. The priority-ordered recommendations above address the dimensions with the most remaining gap. Iter4 should focus on: (1) creating the output template, (2) adding the invocation guidance note, (3) fixing the supplementary Moesta/Spiek citation, (4) adding "(planned)" notation to Phase headings.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] All iter3 fixes verified against actual document line numbers — not assumed to be applied correctly
- [x] `handoff-v2.schema.json` disclaimer verified at both occurrences (lines 446 and 582)
- [x] Christensen 2016 "Competing Against Luck" verified in Theoretical Foundations table (line 242) AND References section (line 596)
- [x] Third Ulwick format verified at line 357 — all three formats present
- [x] "Target behavior" note verified at Methodology section header (line 234)
- [x] Project Traceability subsection verified at lines 584-590
- [x] Actionability held at 0.86 — no actionability fixes in iter3 scope; score not inflated
- [x] Uncertain scores resolved downward (Completeness at 0.93 not 0.94; Internal Consistency at 0.93 not 0.94)
- [x] Methodological Rigor raised to 0.95 — all three cited iter2 gaps are verified fixed; score increase is justified by evidence
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Composite arithmetic independently verified: 0.9245 rounds to 0.924
- [x] Score of 0.924 confirms REVISE verdict — still 0.026 below the C4 threshold of 0.95
- [x] Calibration check: iter2=0.897 for partial fixes; iter3=0.924 for five substantive fixes is a plausible +0.027 delta

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.924
threshold: 0.95
weakest_dimension: Actionability
weakest_score: 0.86
critical_findings_count: 0
iteration: 3
improvement_recommendations:
  - "Create skills/ux-jtbd/references/ux-jtbd-output-template.md with complete output skeleton (L0/L1/L2 sections, Synthesis Judgments, Validation Required placeholder)"
  - "Add invocation guidance note to 'Invoking an Agent' section: clarify when Options 1/2/3 are appropriate vs. when orchestrator dispatch is required"
  - "Replace supplementary Moesta/Spiek 2014 'Re-Wired Group' citation with a specific traceable artifact (named post, episode, or article with URL)"
  - "Add '(planned — target behavior)' notation to Evaluation Workflow and Phase headings within Methodology for tense consistency"
  - "Verify AGENTS.md contains ux-jtbd-analyst in User-Experience Skill Agents section (line 206 claim)"
  - "Consider updating VERSION comment SOURCE field from parent SKILL.md to PROJ-022 PLAN.md for provenance precision"
```

---

*Score Report Version: 1.0.0*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Skill Standards: `.context/rules/skill-standards.md`*
*Score History: iter1=0.851, iter2=0.897, iter3=0.924 | Deltas: +0.046, +0.027*
*Agent: adv-scorer*
*Created: 2026-03-04*
