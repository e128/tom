# Quality Score Report: JTBD Sub-Skill SKILL.md (Iteration 4)

## L0 Executive Summary

**Score:** 0.946/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Actionability (0.93)
**One-line assessment:** All five iter4 fixes verified and correctly applied — Actionability jumped from 0.86 to 0.93 (output template and invocation guidance now present), four dimensions reached 0.95, but the C4 threshold of 0.95 remains unmet by 0.004 because the output template lacks a worked example and the Traceability VERSION SOURCE field imprecision persists; one targeted fix closes the gap.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/SKILL.md`
- **Deliverable Type:** Sub-skill SKILL.md definition file for `/ux-jtbd` (Jobs-to-Be-Done)
- **Criticality Level:** C4
- **Quality Gate Threshold:** 0.95 (C4 requirement per scoring brief; standard H-13 threshold is 0.92)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Skill Standards Reference:** `.context/rules/skill-standards.md`
- **Prior Score (iter3):** 0.924 (REVISE)
- **Prior Score (iter2):** 0.897 (REVISE)
- **Prior Score (iter1):** 0.851 (REVISE)
- **Iteration:** 4
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.946 |
| **Threshold** | 0.95 (C4, per scoring brief) |
| **Verdict** | REVISE |
| **Gap to Threshold** | 0.004 |
| **Strategy Findings Incorporated** | Yes — iter3 score report (`skills/ux-jtbd/output/quality-scores/skill-md-iter3-score.md`) |

---

## Iter4 Fix Verification

The following table documents each claimed iter4 fix with verification status against the actual document:

| Claimed Fix | Location | Actually Applied? | Evidence |
|-------------|----------|-------------------|---------|
| Output Format Template added (complete output skeleton with L0/L1/L2, job tables, switch analysis, synthesis judgments) | Lines 448-528 | YES | Full markdown template present: UX Context header, L0 Executive Summary (5 bullets), L1 Functional/Social/Emotional Jobs tables (labeled columns), Switch Trigger Analysis table (4 forces), Force Balance Assessment line, Job Map table (8 universal steps), Hiring Criteria table, L2 Strategic Implications, Synthesis Judgments Summary (numbered list), Validation Required (3 fields) |
| Invocation guidance added (when to use each option) | Lines 153-157 | YES | "### When to Use Each Option" subsection present with three guidance bullets: Option 1 for most users (orchestrator handles routing automatically), Option 2 for when orchestrator context already established (explicit warning that direct invocation bypasses wave gating), Option 3 for orchestrator-internal dispatch (not typically invoked directly by users) |
| Moesta/Spiek 2014 citation replaced with specific traceable reference ("The Jobs-to-Be-Done Handbook") | Line 688 | YES | "Moesta, B. and Spiek, C. (2014). *The Jobs-to-Be-Done Handbook: Practical Techniques for Improving Your Application of Jobs-to-Be-Done*. Re-Wired Group." — vague "Re-Wired Group (2014)" is replaced by a specifically titled publication with full citation format. Also adds Alan Klement and the "When Coffee and Kale Compete" (2016) cross-reference. |
| Phase headings annotated with "(planned)" throughout methodology body | Lines 272, 276, 291, 311, 341, 369 | YES | "### Evaluation Workflow (planned -- target behavior)" (line 272); "#### Phase 1: Context Gathering (planned)" (line 276); "#### Phase 2: Job Identification (planned)" (line 291); "#### Phase 3: Switch Force Analysis (planned)" (line 311); "#### Phase 4: Job Mapping (planned)" (line 341); "#### Phase 5: Job Statement Synthesis (planned)" (line 369) — all six structural headings now carry the annotation |
| AGENTS.md entry verified at line 307, verification note added | Line 212 | YES | "Verified 2026-03-04" added to the sentence asserting registration in AGENTS.md. Independent verification by adv-scorer confirms `ux-jtbd-analyst` is present at AGENTS.md line 307: "ux-jtbd-analyst \| \`skills/ux-jtbd/agents/ux-jtbd-analyst.md\` \| Jobs-to-Be-Done research and analysis \| Divergent" |

**All five iter4 fixes verified as correctly applied.**

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.95 | 0.190 | Output template (lines 448-528), invocation guidance (lines 153-157), and AGENTS.md verification (line 212) resolve all three iter3 completeness gaps; no substantive requirements gap remains |
| Internal Consistency | 0.20 | 0.95 | 0.190 | All six methodology headings now carry "(planned)" annotations, reinforcing the section-level "target behavior" note; framing chain is complete and mutually consistent at all levels |
| Methodological Rigor | 0.20 | 0.95 | 0.190 | Unchanged from iter3 at 0.95 — no regression; supplementary Moesta/Spiek 2014 citation now also carries a specific title, marginal improvement in evidence precision but not enough to change score band |
| Evidence Quality | 0.15 | 0.95 | 0.1425 | Supplementary Moesta/Spiek 2014 citation now names "*The Jobs-to-Be-Done Handbook*" — all citations now reference specific traceable publications; primary and supplementary sources alike have Author/Year/Title/Publisher format |
| Actionability | 0.15 | 0.93 | 0.1395 | Two binding gaps resolved: output template (complete 13-section skeleton at lines 448-528) and invocation guidance (explicit when-to-use note at lines 153-157); template uses placeholders without worked example, which limits immediate practitioner actionability |
| Traceability | 0.10 | 0.94 | 0.094 | AGENTS.md claim now carries verified date (line 212); supplementary citation is now traceable; VERSION SOURCE field still reads "SOURCE: skills/user-experience/SKILL.md" (minor imprecision, unchanged from iter3) |
| **TOTAL** | **1.00** | | **0.946** | |

**Composite (rounded):** 0.946

**Arithmetic verification:**
(0.95 × 0.20) + (0.95 × 0.20) + (0.95 × 0.20) + (0.95 × 0.15) + (0.93 × 0.15) + (0.94 × 0.10)
= 0.190 + 0.190 + 0.190 + 0.1425 + 0.1395 + 0.094
= **0.946**

---

## Detailed Dimension Analysis

### Completeness (0.95/1.00)

**Evidence:**

All three iter3 completeness gaps are resolved:

**1. Output template (FIXED):** Lines 448-528 contain a complete, ready-to-use markdown template. The template covers every section listed in the Required Output Sections table (Job Statement Inventory, Switch Force Analysis, Job Map, Hiring Criteria, Opportunity Scores, Synthesis Judgments Summary, Validation Required). The template structure is:
- UX Context header with 5 labeled fields
- L0 Executive Summary with 5 bullet placeholders
- L1 Functional Jobs table with Job Statement / Outcome Expectations / Priority / Source columns
- L1 Social Jobs table (same structure)
- L1 Emotional Jobs table (same structure)
- Switch Trigger Analysis table with all four forces (Push/Pull/Anxiety/Habit) and Finding/Evidence columns
- Force Balance Assessment free-text line
- Job Map table with all 8 universal process steps, Domain-Specific Action, Outcome Expectations, and Opportunity Score columns
- Hiring Criteria table with Criterion / Measurement / Relative Weight columns
- L2 Strategic Implications with 4 bullets
- Synthesis Judgments Summary with numbered list
- Validation Required with 3 labeled fields

**2. Invocation guidance (FIXED):** Lines 153-157 add a "When to Use Each Option" subsection immediately before the three option descriptions. Each option has a specific one-sentence rationale directing users to the appropriate choice.

**3. AGENTS.md verification (FIXED):** Line 212 adds "Verified 2026-03-04." Independent adv-scorer verification confirms the claim is accurate (AGENTS.md line 307).

**Remaining gaps:**

None substantive. The output template uses `{placeholder}` notation throughout, which is appropriate for a template artifact. The methodology describes target behavior for a Wave 1 stub agent, which is explicitly and consistently disclosed. No requirement is left unaddressed.

**Score rationale:** 0.95 — all completeness gaps from iter3 are resolved with substantive content. The rubric criterion "All requirements addressed with depth" is met. Anti-leniency check: the template completeness and invocation guidance are genuine additions that directly address the stated gaps. 0.95 is justified.

**Improvement Path:**

None required to meet the quality gate. A worked example alongside the template (showing a populated JTBD analysis for a hypothetical product) would further improve practitioner onboarding but is not required for completeness at the 0.95 standard.

---

### Internal Consistency (0.95/1.00)

**Evidence:**

Iter3's residual tense inconsistency concern — that body text within methodology phases continued in present operational tense despite the section-level "target behavior" note — is now addressed structurally.

The full framing chain is:
1. **Purpose section (line 91-92):** "The current agent definition is a Wave 1 stub" — discloses stub state to all readers
2. **Methodology section header (line 240):** Blockquote note states "This methodology section describes target behavior for the fully-implemented `ux-jtbd-analyst` agent. The current agent definition is a Wave 1 stub."
3. **Evaluation Workflow heading (line 272):** "### Evaluation Workflow (planned -- target behavior)" — annotates the entire workflow as planned
4. **All Phase headings (lines 276, 291, 311, 341, 369):** Each Phase carries "(planned)" annotation

This four-level disclosure chain is internally consistent. The present-tense body text ("The analyst follows...", "The four forces model explains...") within each phase is correctly framed by the "(planned)" annotation in the heading above it. Readers encountering any phase will see the annotation before the body text.

**No remaining consistency tensions.** The document is consistent about:
- The agent's current stub state (Purpose + Methodology header)
- The target behavior framing (Methodology header + Evaluation Workflow + Phase headings)
- The methodology content as specification, not current implementation (all four annotation levels)
- The copyright claim in the footer attributing authorship correctly to the project

**Score rationale:** 0.95 — the tense inconsistency gap from iter3 is resolved through structural annotation at every relevant heading. The framing chain is complete. Anti-leniency check: the body text still uses present tense, but this is an intentional specification-style convention, not an inconsistency, because all structural signposts now correctly label the content as planned/target behavior. 0.95 is the correct score.

**Improvement Path:**

None required. The present-tense specification style within phase bodies is a legitimate technical writing convention for specifying target behavior.

---

### Methodological Rigor (0.95/1.00)

**Evidence:**

No change from iter3. All three iter3 methodology gaps were resolved in iter3. Iter4's citation fix (Moesta/Spiek 2014 title) marginally improves evidence precision but does not open a new methodological gap or resolve one that was penalizing Methodological Rigor. The score was 0.95 in iter3 and remains 0.95 in iter4.

The three methodology pillars remain correctly attributed:
- Jobs-to-Be-Done Theory: Clayton Christensen et al. (2016) *Competing Against Luck*
- Outcome-Driven Innovation: Anthony Ulwick (2005, 2016) *Jobs to Be Done: Theory to Practice*
- Switch Interview Framework: Bob Moesta (2020) *Demand-Side Sales 101*

The 5-phase workflow is well-structured with clear inputs, activities, and outputs per phase. The job statement format, four forces framework, Ulwick universal job process, and three canonical outcome formats are all correctly specified.

**Remaining gaps:**

None substantive. The methodology is correct and complete for a specification document. The supplementary citation now also carries a specific title, which is a minor improvement.

**Score rationale:** 0.95 — unchanged from iter3. No regression. No new methodological issues introduced by iter4 changes.

**Improvement Path:**

None required. The methodology section is at the quality ceiling for a SKILL.md specification document of this type.

---

### Evidence Quality (0.15/1.00)

**Evidence:**

Iter3's binding evidence gap — the supplementary "Moesta, B. and Spiek, C. Re-Wired Group (2014)" citation lacking a specific traceable artifact — is now resolved.

Line 688 now reads:
> "Moesta, B. and Spiek, C. (2014). *The Jobs-to-Be-Done Handbook: Practical Techniques for Improving Your Application of Jobs-to-Be-Done*. Re-Wired Group. Practitioner's guide to switch interview techniques. See also: Klement, A. (2016). *When Coffee and Kale Compete*."

This citation now has:
- Authors named individually (Moesta and Spiek)
- Year (2014)
- Specific publication title in italics
- Publisher (Re-Wired Group)
- Publication type note ("Practitioner's guide")
- Cross-reference to a related work (Klement 2016)

This matches the citation formality level of all other references in the section. The primary sources remain fully traceable:
- Christensen, C.M., Dillon, K., Hall, T., Duncan, D.S. (2016). *Competing Against Luck*. Harper Business.
- Ulwick, A.W. (2016). *Jobs to Be Done: Theory to Practice*. IDEA BITE PRESS. URL provided.
- Moesta, B. (2020). *Demand-Side Sales 101*. Lioncrest Publishing.

All six references in the JTBD Framework References table now have Author/Year/Title/Publisher citation format. The evidence chain from claims to sources is complete.

**Remaining gaps:**

Minor: The Moesta/Spiek "The Jobs-to-Be-Done Handbook" is a self-published Re-Wired Group work; it may not have an ISBN or formal library listing. However, it is a real and commonly cited JTBD practitioner resource. The absence of a URL or ISBN is noted but consistent with the citation style of the Christensen 2003 and Christensen 2016 entries, which also lack ISBNs.

**Score rationale:** 0.95 — the supplementary citation now names a specific traceable publication. All references meet the standard for Author/Year/Title/Publisher format. The rubric criterion "All claims with credible citations" is met. Anti-leniency check: the absence of ISBNs and URLs for some citations is a minor precision gap, but the citation style is internally consistent and meets academic reference standards for this document type. 0.95 is justified; the evidence quality concerns that prevented reaching 0.95 in iter3 are resolved.

**Improvement Path:**

Optional: Adding URLs to the Christensen 2016 and Moesta/Spiek 2014 references (e.g., publisher page URLs or Amazon/Google Books links) would further improve traceability but is not required at the 0.95 standard.

---

### Actionability (0.93/1.00)

**Evidence:**

Both iter3 actionability gaps are now resolved with substantive additions:

**1. Output template (FIXED, high impact):**
Lines 448-528 provide a complete output skeleton. A practitioner can copy this template and populate it directly for any JTBD engagement. The template is:
- Structurally complete (all 13 sections present)
- Column-labeled (every table has populated headers matching the methodology descriptions)
- Self-documenting (each row includes placeholder text describing what should fill the column)

This directly closes the largest actionability gap: a developer implementing this sub-skill now has a ready-to-use output format.

**2. Invocation guidance (FIXED, medium impact):**
Lines 153-157 ("When to Use Each Option") clarify: Option 1 is the recommended default for most users; Option 2 is for when an engagement context already exists via the parent orchestrator (with an explicit warning that direct invocation bypasses wave gating); Option 3 is orchestrator-internal dispatch, not typically invoked by users.

**Remaining limitation:**

The output template uses placeholder notation (`{placeholder}`) throughout without a worked example. A practitioner sees the structure but must derive what populated content looks like from the methodology descriptions. For example, the Functional Jobs table row shows:
> `| When [situation], I want to [motivation], so I can [outcome] | {3-5 outcomes} | {HIGH/MED/LOW} | {evidence source} |`

This is clear as a template instruction but does not demonstrate what a real populated JTBD analysis row looks like. A worked example alongside the template (even a single hypothetical row) would raise actionability to 0.95.

**Score rationale:** 0.93 — significant jump from iter3's 0.86. Both missing elements are now present and substantive. The template is complete and ready to use. The invocation guidance is specific and actionable. The remaining gap (absence of worked example) prevents reaching 0.95. Anti-leniency check: uncertain between 0.92 and 0.94; the two fixes are genuine, substantive improvements, not cosmetic. 0.93 is appropriate.

**Improvement Path:**

1. (High impact) Add a worked example section below the output template showing a single populated JTBD analysis for a hypothetical product (e.g., a project management tool), demonstrating one functional job with 3 outcome expectations, one switch force per category, and 2 job map steps. Even a brief example closes the imagination gap for practitioners unfamiliar with the JTBD format.

---

### Traceability (0.94/1.00)

**Evidence:**

**AGENTS.md claim (IMPROVED):** Line 212 now reads: "The `ux-jtbd-analyst` agent IS registered in `AGENTS.md` under the User-Experience Skill Agents section (line 307), ensuring agent-level discoverability. Verified 2026-03-04." The claim is now backed by a verification timestamp. Independent adv-scorer verification confirms this claim is accurate.

**Supplementary citation (IMPROVED, minor):** The Moesta/Spiek 2014 citation now names a specific publication, improving the traceability of the supplementary reference source.

**Verified cross-references (carried forward from iter2/3):**
- `skills/user-experience/rules/ux-routing-rules.md [Stage Routing Table]` — claimed verified, consistent with routing architecture
- `skills/user-experience/rules/mcp-coordination.md [MCP Dependency Matrix]` — claimed verified
- P-003 `disallowedTools: [Task]` claim — previously verified against agent file
- `ci-checks.md` P-003 enforcement claim — honestly presented as a forward reference to planned CI infrastructure

**Remaining imprecision (unchanged):**

VERSION comment at the bottom: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/SKILL.md | PARENT: /user-experience skill -->` — the SOURCE field identifies the design template source (parent SKILL.md) rather than the primary work item or creating agent. This is a consistent imprecision across all four iterations, not addressed by iter4 scope. The footer correctly attributes authorship ("Agent: ux-jtbd-analyst"), so provenance is partially recorded.

**Score rationale:** 0.94 — the AGENTS.md claim is now verified and time-stamped; the supplementary citation is traceable. The VERSION SOURCE imprecision persists as a minor issue. Anti-leniency: 0.94 not 0.95 because the VERSION SOURCE field does not meet the standard for a complete provenance record. This is the same reasoning as iter3.

**Improvement Path:**

1. Update the VERSION comment SOURCE field from `SOURCE: skills/user-experience/SKILL.md` to `SOURCE: PROJ-022-user-experience-skill/PLAN.md` (or `SOURCE: ux-jtbd-analyst/PROJ-022`) to accurately reflect the work item origin rather than the design template source. This is a one-line change.

---

## Score Delta Analysis (All Iterations)

| Dimension | Iter1 | Iter2 | Iter3 | Iter4 | Delta (iter3→4) | Change Explanation |
|-----------|-------|-------|-------|-------|-----------------|---------------------|
| Completeness | 0.75 | 0.92 | 0.93 | 0.95 | +0.02 | Output template + invocation guidance + AGENTS.md verification resolve all three iter3 gaps |
| Internal Consistency | 0.88 | 0.92 | 0.93 | 0.95 | +0.02 | Phase heading "(planned)" annotations complete the four-level framing chain |
| Methodological Rigor | 0.90 | 0.90 | 0.95 | 0.95 | 0.00 | No change — already at ceiling; citation improvement is marginal |
| Evidence Quality | 0.87 | 0.88 | 0.93 | 0.95 | +0.02 | Moesta/Spiek 2014 citation now names "*The Jobs-to-Be-Done Handbook*"; all citations at Author/Year/Title/Publisher format |
| Actionability | 0.84 | 0.86 | 0.86 | 0.93 | +0.07 | Output template (lines 448-528) and invocation guidance (lines 153-157) resolve both binding gaps |
| Traceability | 0.88 | 0.88 | 0.94 | 0.94 | 0.00 | No change — AGENTS.md verification timestamp improves marginally but not enough to change score band |
| **Composite** | **0.851** | **0.897** | **0.924** | **0.946** | **+0.022** | |

**Composite arithmetic verification:**
(0.95 × 0.20) + (0.95 × 0.20) + (0.95 × 0.20) + (0.95 × 0.15) + (0.93 × 0.15) + (0.94 × 0.10)
= 0.190 + 0.190 + 0.190 + 0.1425 + 0.1395 + 0.094
= **0.946**

---

## Gap to C4 Threshold Analysis

**Current composite:** 0.946
**Required threshold:** 0.950
**Gap:** 0.004

The gap is now very small. Sensitivity analysis for iter5:

| Scenario | Change Required | New Composite |
|----------|----------------|---------------|
| Actionability from 0.93 to 0.95 | +0.02 × 0.15 = +0.003 | 0.949 (still below) |
| Actionability to 0.95 + Traceability to 0.95 | above + 0.01 × 0.10 = +0.001 | 0.950 (threshold met) |
| Traceability to 0.95 only | +0.01 × 0.10 = +0.001 | 0.947 (still below) |
| Actionability to 0.96 + Traceability to 0.95 | above | 0.951 (PASS) |

**Conclusion:** Two fixes close the gap: (1) a worked example in the output template or equivalent addition that raises Actionability from 0.93 to 0.95, AND (2) updating the VERSION SOURCE field which raises Traceability from 0.94 to 0.95. Either fix alone is insufficient; both are required. Both are small, targeted changes.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Actionability | 0.93 | 0.95 | Add a worked example row or section alongside the output template (lines 448-528) showing a single populated JTBD analysis entry — e.g., one functional job statement with situation/motivation/outcome filled in, one switch force row with a specific finding and evidence source, two job map steps with populated outcome expectations and an opportunity score calculation. A 15-20 line worked example demonstrates the expected output quality and eliminates the imagination gap for practitioners new to JTBD format. |
| 2 | Traceability | 0.94 | 0.95 | Update the VERSION comment at line 692 from `SOURCE: skills/user-experience/SKILL.md` to `SOURCE: PROJ-022-user-experience-skill/PLAN.md` (or add the work item ID). This is a single-token change that accurately reflects the provenance origin as the project work item rather than the design template source. |

**Note:** Both recommendations are required to close the 0.004 gap to the 0.95 threshold. Each recommendation in isolation raises the composite to approximately 0.949, which is still below the C4 threshold. Both must be applied together in iter5.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] All five iter4 fixes verified against actual document line numbers — not assumed correct
- [x] Output template verified section by section: UX Context, L0, L1 Functional/Social/Emotional, Switch Trigger Analysis, Force Balance, Job Map (all 8 steps), Hiring Criteria, L2, Synthesis Judgments, Validation Required
- [x] Invocation guidance verified at lines 153-157 — specific and actionable, not vague
- [x] Moesta/Spiek citation verified: "*The Jobs-to-Be-Done Handbook*" title present with Author/Year/Title/Publisher format
- [x] Phase heading annotations verified: all six headings (Evaluation Workflow + 5 phases) carry "(planned)" notation
- [x] AGENTS.md claim verified independently: `ux-jtbd-analyst` confirmed at line 307 in AGENTS.md
- [x] Actionability raised from 0.86 to 0.93 — not 0.95, because worked example is absent; uncertain between 0.92 and 0.94, resolved downward to 0.93
- [x] Traceability held at 0.94 — VERSION SOURCE field imprecision persists unchanged; no basis for raising to 0.95
- [x] Methodological Rigor held at 0.95 — no regression; citation improvement is marginal, not a new raise
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Composite arithmetic independently verified: (0.95×0.20)+(0.95×0.20)+(0.95×0.20)+(0.95×0.15)+(0.93×0.15)+(0.94×0.10) = 0.946
- [x] Score of 0.946 confirms REVISE verdict — 0.004 below the C4 threshold of 0.95
- [x] Calibration check: iter3=0.924 for five substantive fixes; iter4=0.946 for five more targeted fixes is a plausible +0.022 delta consistent with the diminishing returns pattern across iterations

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.946
threshold: 0.95
weakest_dimension: Actionability
weakest_score: 0.93
critical_findings_count: 0
iteration: 4
improvement_recommendations:
  - "Add worked example to output template (lines 448-528): one populated functional job statement row, one switch force row with specific finding and evidence, two job map steps with opportunity score calculation — raises Actionability from 0.93 to 0.95"
  - "Update VERSION comment SOURCE field at line 692 from 'SOURCE: skills/user-experience/SKILL.md' to 'SOURCE: PROJ-022-user-experience-skill/PLAN.md' — raises Traceability from 0.94 to 0.95"
  - "Both fixes required together: each in isolation yields ~0.949, still below threshold; applied together they yield ~0.950-0.951 (PASS)"
```

---

*Score Report Version: 1.0.0*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Skill Standards: `.context/rules/skill-standards.md`*
*Score History: iter1=0.851, iter2=0.897, iter3=0.924, iter4=0.946 | Deltas: +0.046, +0.027, +0.022*
*Agent: adv-scorer*
*Created: 2026-03-04*
