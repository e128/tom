# Quality Score Report: Heuristic Evaluation Rules

## L0 Executive Summary

**Score:** 0.878/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Actionability (0.82)

**One-line assessment:** The rules file is structurally complete and methodologically sound, but two gaps block acceptance at the C4 >= 0.95 threshold: the Effort classification criteria are undefined, leaving the agent with an undocumented judgment call on every finding, and the Synthesis Judgments Summary section relies on an external file (`synthesis-validation.md`) without summarizing what counts as a judgment call.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md`
- **Deliverable Type:** Rules file (agent operational constraints and methodology)
- **Criticality Level:** C4
- **Quality Gate Threshold:** 0.95 (C4 per invocation context)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Reference Files:**
  - SKILL.md: `skills/ux-heuristic-eval/SKILL.md`
  - Agent definition: `skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md`
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.878 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 7 required sections present with depth; minor divergence in self-review checklist item count between rules file (10 items) and agent definition (6 items) |
| Internal Consistency | 0.20 | 0.91 | 0.182 | No contradictions across rules file, SKILL.md, and agent definition; severity scale, finding format, handoff threshold, and AI supplement names all align |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | Nielsen heuristics accurately represented; severity taxonomy correct; deduplication logic structured; pass/fail criteria for individual checkpoints not explicitly defined |
| Evidence Quality | 0.15 | 0.88 | 0.132 | All 5 external citations present with author, year, title, venue; no inline URLs but academic-style citation is appropriate; Amershi et al. uses "et al." without full co-author list |
| Actionability | 0.15 | 0.82 | 0.123 | Finding format, deduplication edge cases, and severity decision criteria are highly actionable; Effort classification criteria completely absent; Synthesis Judgments Summary relies on external file without inline definition |
| Traceability | 0.10 | 0.85 | 0.085 | H-23 navigation table present and correct; VERSION header and footer present; S-010/P-022 cross-references traceable; no requirements traceability section linking to PROJ-022/EPIC-002 |
| **TOTAL** | **1.00** | | **0.878** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**

All 7 sections declared in the navigation table are present and substantively populated:

1. **Nielsen's 10 Heuristics** -- All 10 heuristics present (H1-H10) with definitions, 4-5 evaluation checkpoints each, common violation examples, and severity guidance. No heuristic is missing or abbreviated.
2. **AI-Interaction Supplement Heuristics** -- AI-1 (Transparency), AI-2 (Controllability), AI-3 (Error Recovery) present with P-022 disclosure, evaluation checkpoints, common violations, and severity guidance. Both required citations (Amershi 2019, Google PAIR 2019) present.
3. **Severity Scale** -- Complete 5-row table (0-4) with Name, Definition, Decision Criteria, and Remediation Priority columns. Supplemented by Rating Discipline and Cross-Framework Handoff Threshold subsections.
4. **Finding Documentation Rules** -- Required field template, field requirements table with 7 fields, evidence quality standard with 3 acceptable and 3 unacceptable examples. F-{NNN} format specified.
5. **Deduplication Rules** -- Consolidate/Do Not Consolidate criteria, edge case table with 4 scenarios, rationale for each.
6. **Single-Evaluator Reliability** -- P-022 disclosure present; 35%/75-80% statistics cited; AI compensation table (3 rows); Residual Limitations table (4 rows); High-Stakes Evaluation Recommendation with three trigger conditions.
7. **Report Structure** -- 9 required sections with level designations, content requirements, section ordering rationale, and a 10-item self-review checklist.

**Gaps:**

- The self-review checklist in the Report Structure section contains 10 items. The agent definition's Step 5 self-review lists only 6 items (missing: finding IDs sequential check, degraded mode disclosure check, handoff data severity filter check, and the 10-item count itself). The rules file is the authoritative expanded version, but the agent definition diverges. This creates a completeness risk in practice if the agent references its own Step 5 checklist rather than the rules file.
- The Report Structure section references section 8 (Synthesis Judgments Summary) as requiring content "per `skills/user-experience/rules/synthesis-validation.md`" but does not provide inline content requirements beyond what is in section 8's content requirements column. A reader of only this rules file cannot determine what constitutes a judgment call without loading the external file.

**Improvement Path:**

Expand the self-review checklist in the agent definition to match the 10-item rules file checklist. Add an inline definition of "AI judgment call" in the Report Structure section, supplemented by the cross-reference to `synthesis-validation.md`.

---

### Internal Consistency (0.91/1.00)

**Evidence:**

Cross-referenced all three documents (rules file, SKILL.md, agent definition) for contradictions:

- **Severity scale:** Rules file has 5 columns including "Decision Criteria." SKILL.md and agent definition have 4 columns (no "Decision Criteria"). The rules file provides an additive richer version -- no contradiction, the rules file is the authoritative source. All three documents agree on 0-4 range, severity names, and remediation priority language.
- **Finding format:** Identical 6-field template (Heuristic, Severity, Screen/Flow, Evidence, Remediation, Effort) across all three documents.
- **AI supplement heuristics:** AI-1, AI-2, AI-3 named identically across all three documents. Amershi 2019 and Google PAIR 2019 citations present in rules file and agent definition methodology; SKILL.md references the same citations.
- **Cross-framework handoff threshold:** Severity >= 2 stated consistently in rules file (Severity Scale section, Deduplication Rules), SKILL.md ([Cross-Framework Integration]), and agent definition output section.
- **AI Product Flag gating:** All three documents state AI supplement heuristics are applied only when AI Product Flag is true. Marking convention `[AI-SUPPLEMENT]` consistent.
- **Degraded mode disclosure:** P-022 disclosure language consistent across SKILL.md and agent definition. Rules file does not repeat the full disclosure verbatim (it's in Single-Evaluator Reliability), but the principle is present.
- **Heuristic numbering notation:** Rules file uses H1-H10 (no hyphen). This is consistent within the rules file and consistent with SKILL.md and agent definition. It does not conflict with Jerry HARD rule notation (H-13, H-34 with hyphen) because the context is clearly UX-domain shorthand. No confusion risk within the rules file itself.

**Gaps:**

- The self-review checklist in the rules file has 10 items; the agent definition Step 5 has 6 items. This is not a contradiction but a coverage divergence -- the agent definition omits 4 checks that the rules file requires. As the rules file is the SSOT for rules, this is a completeness gap in the agent definition rather than an inconsistency within the rules file itself.
- The SKILL.md Output Specification lists 8 required sections (not counting the navigation table as section 1). The rules file's Report Structure lists 9 sections (explicitly including the navigation table as section 1). The agent definition `<output>` Required Report Structure shows the navigation table in the markdown template. All three are consistent if the navigation table is counted as section 1; the SKILL.md simply doesn't count it separately. No material contradiction.

**Improvement Path:**

Align the agent definition Step 5 self-review checklist with the 10-item rules file checklist. No changes needed to the rules file itself for this dimension.

---

### Methodological Rigor (0.88/1.00)

**Evidence:**

- **Nielsen heuristic definitions:** All 10 definitions accurately reflect the Nielsen Norman Group canonical language. Definitions sourced from the 1994 original and noted as "revised 2020" where applicable.
- **Evaluation checkpoints:** 4-5 checkpoints per heuristic, phrased as yes/no questions that an evaluator can answer based on observable interface artifacts. Examples from the document: "Does every user action produce visible feedback within 1 second?" (H1), "Does the interface use terminology that the target users would recognize?" (H2), "Can users undo or redo recent actions?" (H3). These are valid, operationalizable criteria.
- **Severity taxonomy:** The 0-4 scale accurately represents Nielsen's published severity taxonomy. The "Decision Criteria" column is an extension that aids operationalization without contradicting the canonical scale.
- **Deduplication methodology:** The three-condition consolidation rule (same heuristic, same root cause, same remediation) is methodologically sound. The Do Not Consolidate rule (any one differs) is correctly stated as the converse.
- **Single-evaluator reliability statistics:** The "35% of usability problems / 75-80% coverage across 3-5 evaluators" claim is consistent with Nielsen (1994c) and is a well-known finding in the HCI literature.
- **Rating discipline:** The "default to lower rating when uncertain" principle is appropriately conservative and methodologically justified.
- **AI supplement disclosure:** P-022 disclosure is explicit that AI-1 through AI-3 are framework-defined, not published Nielsen extensions. Source attribution to Amershi et al. (2019) and Google PAIR (2019) is appropriate.

**Gaps:**

- **Pass/fail criteria for checkpoints:** The evaluation checkpoints are yes/no questions but the rules file does not define what constitutes a passing vs. failing answer beyond the severity guidance. For example, H1 checkpoint 1 ("Does every user action produce visible feedback within 1 second?") does not define edge cases: what if feedback appears at 1.2 seconds? What if feedback appears for some actions but not others on the same screen? The severity guidance provides post-hoc classification, but pre-evaluation decision criteria are absent. This is a standard limitation of heuristic evaluation methodology but it reduces rigor.
- **AI supplement rigor:** The AI-1 through AI-3 heuristics are shorter than the Nielsen heuristics: 4 checkpoints each vs. 4-5 for Nielsen heuristics. AI-3 (Error Recovery) overlaps significantly with H3 (User Control and Freedom) and H9 (Help Users Recognize, Diagnose, and Recover from Errors). The rules file does not address this overlap or provide guidance on when to apply AI-3 vs. H3/H9. An evaluator could double-count or under-count findings.
- **Effort classification:** The finding format requires an "Effort" field (Low/Medium/High), but neither the Finding Documentation Rules nor any other section defines what criteria determine each effort level. This is a methodological gap -- the methodology specifies that effort must be classified but does not specify how.

**Improvement Path:**

Add an Effort Classification subsection to Finding Documentation Rules that defines Low/Medium/High by observable criteria (e.g., scope of change, estimated engineering days, or dependency on external systems). Add a note in the AI supplement section addressing the overlap between AI-3 and H3/H9 with guidance on when findings should be classified under Nielsen vs. AI supplement heuristics.

---

### Evidence Quality (0.88/1.00)

**Evidence:**

Five external citations are present and appear accurate:

1. "Jakob Nielsen, '10 Usability Heuristics for User Interface Design' (1994, revised 2020). Nielsen Norman Group." -- Real, canonical source for the 10 heuristics.
2. "Jakob Nielsen, 'Severity Ratings for Usability Problems' (1994). Nielsen Norman Group." -- Real, standard severity taxonomy source.
3. "Jakob Nielsen, 'How to Conduct a Heuristic Evaluation' (1994)." -- Real, cited as Nielsen 1994c in Single-Evaluator Reliability section; the "(1994c)" parenthetical establishes a three-citation Nielsen series (1994a, 1994b, 1994c) consistent with SKILL.md References table, which confirms all three.
4. "Amershi, S. et al. (2019). 'Guidelines for Human-AI Interaction.' ACM CHI 2019." -- This is a real publication (CHI 2019 Paper). The "et al." form is appropriate for a rules file; the SKILL.md confirms the same citation pattern.
5. "Google PAIR (2019). 'People + AI Guidebook.' pair.withgoogle.com/guidebook." -- Real publication. URL is consistent with the known guidebook location.

The 35%/75-80% single-evaluator statistics are well-supported by the cited Nielsen 1994c source.

Evidence quality examples provided in the Finding Documentation Rules are specific and clearly distinguish acceptable from unacceptable evidence. The three acceptable examples are observable interface artifacts; the three unacceptable examples correctly identify the failure modes (subjective, speculative, circular).

**Gaps:**

- Citations use academic-style formatting without inline URLs. For a rules file, this is acceptable, but it means the agent cannot verify citation accuracy without web lookup. Given that all citations are verifiable through well-known sources (nngroup.com for Nielsen, ACM Digital Library for Amershi), this is a minor gap.
- The Amershi et al. (2019) citation does not include the full co-author list. The paper has 18 authors (Saleema Amershi, Dan Weld, Mihaela Vorvoreanu, et al.). For a rules file, "et al." is standard. The SKILL.md uses the same format. Not a material gap but worth noting.
- The Google PAIR guidebook citation has no access date or version number. The guidebook may be updated post-2019. This does not affect the AI-1 through AI-3 heuristic definitions, which are derived from published principles, but reduces precision.

**Improvement Path:**

Add access dates to the web-based citations (Google PAIR guidebook). No other material changes needed.

---

### Actionability (0.82/1.00)

**Evidence:**

High-actionability elements:

- Per-heuristic evaluation checkpoints are yes/no questions that directly drive finding identification. An agent can answer "Does every user action produce visible feedback within 1 second?" by observing the interface.
- The evidence quality standard provides 3 specific acceptable examples and 3 specific unacceptable examples. An agent can compare its evidence formulation against these templates before accepting it.
- The finding format is a fill-in-the-blank template with 6 fields. Each field has explicit acceptance criteria ("Rejection Criterion" column).
- Deduplication decision rules are binary (consolidate if ALL three conditions true; separate if ANY one differs) with 4 edge cases explicitly resolved.
- The 0-4 severity scale has "Decision Criteria" providing observable conditions for each level: "User can complete the task without difficulty" (severity 1), "No obvious workaround. Affects primary user flows" (severity 3).
- The self-review checklist provides 10 binary checks before report persistence.
- Finding IDs are sequential F-{NNN} in ranked order -- a clear, mechanical assignment rule.

**Gaps (material):**

1. **Effort classification undefined:** The finding format requires "Effort: Low | Medium | High." The Field Requirements table states the rejection criterion is "Missing or non-standard effort classification." However, nowhere in the rules file is there a definition of what constitutes Low, Medium, or High effort. An agent following these rules must make an undocumented subjective judgment for every finding. This is the most significant actionability gap.

2. **Synthesis Judgments Summary relies entirely on external file:** The Report Structure section specifies section 8 as "Each AI judgment call listed (per `skills/user-experience/rules/synthesis-validation.md`)." The content requirements column says "includes severity calibration decisions, deduplication decisions, and effort estimates." This provides partial guidance (3 types of judgment calls are named), but the phrase "per `skills/user-experience/rules/synthesis-validation.md`" implies additional judgment types defined externally. An agent reading only this rules file cannot determine if the listed three types are exhaustive or a partial subset. If the agent does not load `synthesis-validation.md` before generating section 8, it may produce an incomplete Synthesis Judgments Summary.

3. **Handoff Data column "Candidate HEART Category":** Section 9 (Handoff Data) requires a column "Candidate HEART Category" with values from "Happiness/Engagement/Adoption/Retention/Task success." No guidance is provided in this rules file for how to assign a HEART category to a heuristic finding. This cross-framework mapping requires knowledge not contained in the rules file.

**Improvement Path:**

1. Add an "Effort Classification" subsection to Finding Documentation Rules defining Low, Medium, and High by specific criteria (e.g., Low = no architectural change, estimated < 1 day; Medium = component-level change, 1-5 days; High = architectural change or > 5 days). These are illustrative; the team should define the actual thresholds.
2. Inline the list of judgment call types in the Report Structure section (or confirm that severity calibration, deduplication, and effort estimates are the exhaustive set), eliminating the external-file dependency for this section.
3. Add a "HEART Category Mapping Heuristic" note in the Handoff Data section or cross-reference to a mapping table. Alternatively, mark the column as "agent best-judgment" with examples (e.g., H1 findings typically map to Task Success; H8 findings typically map to Happiness).

---

### Traceability (0.85/1.00)

**Evidence:**

- **H-23 navigation table:** Present at line 9-18. Format: `| Section | Purpose |` with 7 entries, each using anchor link syntax (e.g., `[Nielsen's 10 Heuristics](#nielsens-10-heuristics)`). Compliant with H-23/NAV-001.
- **VERSION header:** Present as HTML comment at line 1: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/ux-heuristic-eval/SKILL.md, skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md | PARENT: /ux-heuristic-eval sub-skill -->`. Compliant.
- **VERSION footer:** Present at bottom as HTML comment: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/ux-heuristic-eval/SKILL.md, skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md, Nielsen (1994a, 1994b, 1994c, 2020), Amershi et al. (2019), Google PAIR (2019) -->`. The footer enumerates all external sources. Compliant and thorough.
- **Plain-text footer:** Lines 474-480 provide plain-text metadata (`*Rule file: heuristic-evaluation-rules.md*`, `*Version: 1.0.0*`, `*Parent sub-skill: /ux-heuristic-eval*`, etc.). Consistent with the HTML comment VERSION header.
- **Standard cross-references:** P-022 referenced by ID in two sections (Severity Rating Discipline, Single-Evaluator Reliability). S-010 referenced by name in Finding Documentation Rules and Report Structure. Both traceable to `quality-enforcement.md`.
- **Source attribution per heuristic:** A single source statement at the top of the Nielsen's 10 Heuristics section covers all 10 heuristics. The Severity Scale section cites its source. The AI supplements section cites both sources. Per-subsection attribution is sufficient; requiring per-heuristic footnotes would be excessive for a rules file.

**Gaps:**

- **No requirements traceability section:** The SKILL.md has a [Requirements Traceability] section linking to PROJ-022 PLAN.md, EPIC-002, and ORCHESTRATION.yaml. The rules file has no equivalent. For a C4 rules file, traceability to the work item that commissioned it provides assurance that the rules implement the correct requirements. This is not required by H-23 or any explicit HARD rule for rules files, but it represents a best practice gap at C4 criticality.
- **Cross-reference to `synthesis-validation.md` unverified:** Section 8 of the Report Structure references `skills/user-experience/rules/synthesis-validation.md`. This cross-reference is consistent with the SKILL.md References table, which also lists `synthesis-validation.md`. However, the rules file cannot verify that `synthesis-validation.md` exists and contains the judgment call definitions. This is a documentation dependency that reduces standalone traceability.
- **Plain-text footer version notation:** The bottom of the file uses `*Version: 1.0.0*` (plain text italic) while the top uses the `<!-- VERSION: 1.0.0 -->` HTML comment format. Both convey the same version information. The dual-format is not a violation of any standard, but the HTML comment format is the framework convention (matching all other rules files).

**Improvement Path:**

Add a requirements traceability table or footer linking to PROJ-022 EPIC-002 and ORCHESTRATION.yaml. This follows the SKILL.md pattern and closes the C4 traceability gap.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Actionability | 0.82 | 0.90+ | **Add Effort Classification criteria.** Add a subsection to Finding Documentation Rules defining Low/Medium/High effort with observable criteria (scope of change, estimated engineering investment, or dependency count). Without this, the Effort field is an undocumented judgment call on every finding. |
| 2 | Actionability | 0.82 | 0.90+ | **Inline judgment call types in Report Structure section 8.** Either confirm that severity calibration, deduplication, and effort estimates are the exhaustive set of AI judgment calls, or enumerate additional types. Remove the external-file dependency for determining what to include in section 8. |
| 3 | Actionability | 0.82 | 0.90+ | **Add HEART Category mapping guidance to Handoff Data section.** Provide a heuristic-to-HEART mapping table or note (e.g., H1/H9 -> Task Success; H8 -> Happiness) so the agent can populate section 9 without relying on undocumented cross-framework knowledge. |
| 4 | Methodological Rigor | 0.88 | 0.92+ | **Address AI supplement heuristic overlap with Nielsen H3/H9.** AI-3 (Error Recovery) overlaps with H3 (User Control and Freedom) and H9 (Help Users Recognize, Diagnose, and Recover from Errors). Add guidance on when a finding should be classified under a Nielsen heuristic vs. an AI supplement heuristic to prevent double-counting or under-counting. |
| 5 | Methodological Rigor | 0.88 | 0.92+ | **Add Effort classification criteria** (also satisfies Priority 1). This is both a methodological gap (the methodology is incomplete) and an actionability gap (the agent cannot execute it). |
| 6 | Completeness | 0.90 | 0.93+ | **Align agent definition self-review checklist.** The agent definition Step 5 has 6 items vs. the rules file's authoritative 10 items. Update the agent definition to match. (This does not require changes to the rules file.) |
| 7 | Traceability | 0.85 | 0.90+ | **Add requirements traceability footer.** Add a table or footer linking this rules file to PROJ-022 EPIC-002 and ORCHESTRATION.yaml, following the SKILL.md pattern. |
| 8 | Evidence Quality | 0.88 | 0.90+ | **Add access dates to web citations.** Add "Retrieved: 2026-03-04" or equivalent to the Google PAIR guidebook citation. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score (specific quotes and sections identified)
- [x] Uncertain scores resolved downward (Actionability considered 0.84 before confirming the Effort gap was material -- resolved to 0.82)
- [x] First-draft calibration considered (this is a first-iteration rules file; score of 0.878 is consistent with 0.85-0.90 band for well-structured first drafts)
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] C4 threshold (0.95) applied, not the default C2+ threshold (0.92)

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.878
threshold: 0.95
weakest_dimension: Actionability
weakest_score: 0.82
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add Effort classification criteria (Low/Medium/High) to Finding Documentation Rules with observable thresholds"
  - "Inline judgment call types in Report Structure section 8 to remove external-file dependency"
  - "Add HEART Category mapping guidance to Handoff Data section (section 9)"
  - "Address AI-3 overlap with H3/H9 -- add classification guidance for evaluators"
  - "Align agent definition Step 5 self-review checklist to match 10-item rules file checklist"
  - "Add requirements traceability footer linking to PROJ-022 EPIC-002"
  - "Add access dates to web-based citations (Google PAIR guidebook)"
```

---

*Score Report: rules-iter1-score.md*
*Scoring Agent: adv-scorer v1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md`*
*Scored: 2026-03-04*
