# Quality Score Report: Heuristic Report Template (Iteration 5)

## L0 Executive Summary

**Score:** 0.916/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.88)
**One-line assessment:** Template is structurally complete and internally consistent at 0.916, but misses the C4 threshold of 0.95 by 0.034; closing the Evidence Quality gap (single example vs. available three from rules file) plus minor Traceability and Completeness polish would push it over the line.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/templates/heuristic-report-template.md`
- **Deliverable Type:** Design (Template)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (C4 per user instruction)
- **Prior Scores:** Iter1=0.843, Iter2=0.919, Iter3=0.906, Iter4=0.934
- **Scored:** 2026-03-04T00:00:00Z
- **Parent Artifacts Reviewed:**
  - `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md`
  - `skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md`
  - `skills/ux-heuristic-eval/SKILL.md`

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.916 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |
| **Iteration** | 5 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 12 required sections present; all placeholders populated; finding block complete |
| Internal Consistency | 0.20 | 0.93 | 0.186 | No contradictions across template, rules file, and agent spec; handoff threshold stated consistently |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | H1-H10 enumerated; AI supplements conditional; finding ID delay enforced; Coverage Matrix has blind-spot guidance |
| Evidence Quality | 0.15 | 0.88 | 0.132 | One evidence example provided (iter4 addition); rules file has three; only the "Save button" example included |
| Actionability | 0.15 | 0.92 | 0.138 | All sections provide actionable fill-in instructions; effort tiers structured; Self-Review Checklist is checkbox-format |
| Traceability | 0.10 | 0.90 | 0.090 | Header cites source files; YAML distinguishes handoff-v2 vs. ux-ext; footer has full academic citations; minor: relative paths in checklist |
| **TOTAL** | **1.00** | | **0.916** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**
The template covers all 12 required sections, verified against `heuristic-evaluation-rules.md` [Report Structure] (9 required sections) plus Methodology, Limitations and Reliability, and Self-Review Checklist (required by P-022 and H-15 respectively). The nav table lists all 12 sections in document-body order, matching the iter4 revision intent. Every required placeholder is present: `{{TOPIC}}`, `{{ENGAGEMENT_ID}}`, `{{PRODUCT_NAME}}`, `{{EVALUATION_DATE}}`, `{{EVALUATOR}}`, `{{COUNT_SEV0-4}}`, `{{TOTAL_FINDINGS}}`, `{{CRITICAL_COUNT}}`, `{{HEURISTIC_COUNT}}`, `{{SCREEN_COUNT}}`. The repeatable finding block (lines 110-120) is complete with all 6 required fields. Handoff YAML (lines 389-425) includes both handoff-v2 schema fields and ux-ext extension fields with comments distinguishing their origins.

**Gaps:**
- Minor: the agent `<output>` section spec in `ux-heuristic-evaluator.md` lists sections in a slightly different order than the template (Synthesis Judgments Summary appears after Remediation Roadmap in the agent spec, but appears correctly after Ranked Findings in the template body, which matches the rule file's section ordering table). This order ambiguity is not a completeness gap, but it is a minor alignment issue.
- Minor: `{{PRODUCT_DOMAIN}}` placeholder in Evaluation Context is defined in the template but not in the nav table description -- the nav table says "Product, target users, screens, input modality, MCP status, evaluation scope" but does not mention "domain". Not a meaningful gap.

**Improvement Path:**
To reach 0.95+: verify the section ordering is unambiguous relative to the rule file's [Section Ordering] (lines 469-471 of rules file). Add `{{PRODUCT_DOMAIN}}` to nav table description for the Evaluation Context entry.

---

### Internal Consistency (0.93/1.00)

**Evidence:**
Systematic cross-check against three parent documents reveals no contradictions:

1. **Finding block structure** (template lines 111-120) matches `heuristic-evaluation-rules.md` [Required Fields Per Finding] (lines 336-344) exactly: Finding ID, Heuristic, Severity, Screen/Flow, Evidence, Remediation, Effort.
2. **Severity scale** (0-4 with Nielsen names) is stated consistently in Executive Summary table, finding block comment, and Coverage Matrix. The names match `heuristic-evaluation-rules.md` [Severity Scale] (lines 307-313) and `ux-heuristic-evaluator.md` [Step 3: Severity Rating] (lines 162-169).
3. **Handoff threshold** (severity >= 2) appears consistently in: Handoff Data section header (line 377), Handoff Data table comment (line 385), and is implicit in the YAML `handoff_findings_count` comment (line 424).
4. **AI supplement conditionality** is consistently marked across: Findings by Heuristic sections (lines 205-219), Coverage Matrix rows (lines 241-244), and Handoff YAML (conditional fields noted). The `[AI-SUPPLEMENT]` marker is used consistently.
5. **Self-Review Checklist** (lines 362-371, 10 items) matches `heuristic-evaluation-rules.md` [Self-Review Checklist (S-010)] (lines 493-502, 10 items) item for item.
6. **Synthesis Judgments confidence classification** (lines 302-304) correctly describes HIGH and MEDIUM but omits LOW -- this matches `heuristic-evaluation-rules.md` [Report Structure] section 8 which lists HIGH and MEDIUM only (LOW is not a defined level for this sub-skill per synthesis-validation.md reference).

**Gaps:**
- The agent `<output>` Required Report Structure (lines 217-260 of `ux-heuristic-evaluator.md`) lists 8 sections in a different order than both the template and the rules file: the agent spec lists Ranked Findings Summary before Strategic Implications, but the template (correctly following the rules file) places Strategic Implications after Remediation Roadmap and before Limitations. This is a consistency gap between the template and the agent spec, not between template and rules file. The template correctly follows the more authoritative rules file ordering.

**Improvement Path:**
Confirm the agent `<output>` section spec section ordering matches the template and rules file. If the agent spec is authoritative, update the template; if the template/rules file ordering is intended, update the agent spec.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**
The template enforces the 5-step evaluation workflow defined in `heuristic-evaluation-rules.md` through structural mechanisms:

1. **Step 1 (Input Collection):** Evaluation Context section (lines 63-85) captures all required fields: Product, Domain, Target Users, Screens/Flows, Input Modality, MCP Status, Evaluation Scope, and conditional degraded mode block.
2. **Step 2 (Systematic Evaluation):** All 10 heuristics are enumerated (H1-H10, lines 105-201) with section headers and repeated finding blocks. AI supplement sections are commented out with explicit conditionality (lines 205-219).
3. **Step 3 (Severity Rating):** Finding block enforces `{{0-4}} ({{Nielsen severity name}})` format. The comment at line 117 includes the evidence example to discourage vague evidence.
4. **Step 4 (Deduplication and Ranking):** Deduplication check comment (lines 102-103) directs to rule file section before population. Finding ID assignment delay instruction (line 103) enforces ranking-first ID assignment.
5. **Step 5 (Report Generation):** Self-Review Checklist enforces the S-010 pre-persistence verification protocol.
6. **Coverage Matrix** (lines 229-248) provides the cross-screen heuristic grid with systematic blind-spot detection guidance in the coverage note (line 247).
7. **P-022 compliance:** Methodology section explicitly discloses AI supplement origin (line 92): "NOT published extensions of Nielsen's original framework."

**Gaps:**
- The Coverage Matrix comment (line 227) says "template-defined extension" for the format origin, which is accurate per iter4 revision intent. However, the exact protocol for adding/removing screen columns is described only in the comment, not as a placeholder. A `{{ADD_OR_REMOVE_SCREEN_COLUMNS_NOTE}}` placeholder or clearer instruction would make this more actionable.
- The Methodology section (lines 88-94) is non-fill-in prose, which is the correct design decision. However, there is no comment instructing the evaluator NOT to modify this section. A single line `<!-- Do not modify this section -- it describes the standard methodology applied to every evaluation. -->` would prevent accidental customization.

**Improvement Path:**
Add column guidance as explicit instruction text (not just comment) in the Coverage Matrix section. Add a "do not modify" comment to the Methodology section to protect the fixed prose.

---

### Evidence Quality (0.88/1.00)

**Evidence:**
The iter4 revision added one concrete evidence example to the finding block comment (line 117):
> "The 'Save' button produces no visual feedback after click -- no spinner, no confirmation toast, no state change."

This example is a direct quote from `heuristic-evaluation-rules.md` [Evidence Quality Standard] (line 361). This is the correct approach -- the template uses the authoritative example from the rules file.

**Gaps:**
The rules file [Evidence Quality Standard] provides THREE acceptable evidence examples (lines 361-363) and THREE unacceptable examples (lines 366-368):

Acceptable (rules file):
1. "The 'Save' button produces no visual feedback after click..." -- INCLUDED in template
2. "The error message reads 'Error 422' with no plain-language explanation or recovery suggestion" -- NOT INCLUDED
3. "The settings page uses 'Provisioning Cadence' while the dashboard uses 'Update Schedule' for the same feature" -- NOT INCLUDED

Unacceptable (rules file):
1. "The form feels confusing" -- NOT INCLUDED
2. "Users probably struggle here" -- NOT INCLUDED
3. "This violates H1" -- NOT INCLUDED

The template currently provides only 1/3 of available positive examples and 0/3 of negative examples. The rules file explicitly defines both acceptable and unacceptable evidence. A template that includes only one example leaves evaluators without contrast training -- they can copy the Save button example but may still produce vague evidence for other finding types (H2 terminology, H4 consistency, H9 error messages). The current comment text says "for acceptable vs. unacceptable evidence examples, see heuristic-evaluation-rules.md [Evidence Quality Standard]" but this requires a context switch; inline contrast examples are stronger instruction.

**Improvement Path:**
Add the second and third acceptable examples from the rules file to the evidence comment. Add one unacceptable example with contrast. This would bring the evidence guidance from representative (one case) to comprehensive (three cases + negative contrast), justifying a score increase to 0.92-0.93.

---

### Actionability (0.92/1.00)

**Evidence:**
Every section provides immediately actionable guidance:

1. **Executive Summary:** Structured placeholders for severity distribution, top findings (with format `**F-{{NNN}}:** {{one-line}} (Severity {{N}}, {{heuristic}})`), and explicit "up to 5" instruction.
2. **Remediation Roadmap:** Three effort tiers (Quick Wins / Medium / High) with priority numbering. "Suggested Implementation Order" (line 287) provides decision logic: "typically severity 4 first regardless of effort, then quick wins for momentum."
3. **Self-Review Checklist:** All 10 items are checkbox-format, each citing the exact rule to verify. Items 2 and 4 include linked references to the rules file.
4. **Handoff YAML:** Complete schema with comment annotations distinguishing field origins and required formats. The evaluator can fill in the YAML without consulting external documentation for most fields.
5. **Coverage Matrix coverage note** (line 247): Explicitly identifies the action condition: "Flag any heuristic with zero findings across all screens. If 3+ heuristics have zero findings, note as a potential systematic blind spot."
6. **Synthesis Judgments:** Three example rows covering the three most common judgment types (severity calibration, deduplication, effort estimate) with HIGH/MEDIUM confidence classification definitions.

**Gaps:**
- The Strategic Implications section (lines 308-321) provides example prompts in `{{...}}` placeholder text but does not provide structural sub-sections or a minimum content guidance (e.g., "identify at least one cross-product pattern"). A product team receiving the template may leave this section sparse without understanding what depth is expected.
- The "Overall Usability Assessment" (line 56-57) description says "one paragraph" but does not define what the paragraph must cover (strengths, weaknesses, release readiness). These three elements are mentioned in the description text but not structured.

**Improvement Path:**
Add minimum content guidance to Strategic Implications (e.g., "Minimum: one pattern per cross-product, org maturity, and design evolution subsection"). Add structured prompts to the Overall Usability Assessment placeholder.

---

### Traceability (0.90/1.00)

**Evidence:**
Traceability mechanisms are present at multiple levels:

1. **File header comments** (lines 1-4): VERSION, DATE, REVISION, SKILL, SOURCE, USAGE. SOURCE cites three specific artifacts.
2. **Section-level citations:** Coverage Matrix comment cites `heuristic-evaluation-rules.md [Self-Review Checklist (S-010)] item 1` (line 227). Methodology section cites `heuristic-evaluation-rules.md [Evaluation Workflow]` (line 90). Deduplication check comment cites `heuristic-evaluation-rules.md [Deduplication Rules]` (line 102). Synthesis Judgments Summary cites `skills/user-experience/rules/synthesis-validation.md` (line 293). Self-Review Checklist items 2 and 4 link to the rules file with anchor fragments (line 363-364).
3. **Handoff YAML field comments** (lines 394-425): Every field annotated with `[handoff-v2]` or `[ux-ext]` markers, plus schema reference at line 391-392.
4. **Footer** (lines 429-434): Full academic citations (Nielsen 1994a/b/c/2020, Amershi 2019, Google PAIR 2019, Rodden 2010). ORCHESTRATION.yaml path for build traceability.
5. **Footer source line** (line 430): `*Source: SKILL.md [Output Specification], agent [output] section, heuristic-evaluation-rules.md [Report Structure]*` matches header SOURCE comment.

**Gaps:**
- Self-Review Checklist items 2 and 4 use relative path syntax (`../../rules/heuristic-evaluation-rules.md`) which resolves correctly from the template's location but would break if the file is referenced from a different directory context. All other citations use skill-relative paths (`skills/user-experience/rules/synthesis-validation.md` or just section anchors). Minor consistency gap.
- The Synthesis Judgments Summary cites `skills/user-experience/rules/synthesis-validation.md` (line 293) but this document is not in the parent artifacts reviewed -- this citation cannot be verified from the reviewed artifacts. If this file has evolved, the template's confidence classification descriptions (HIGH/MEDIUM at lines 302-304) may be out of sync. This is a moderate traceability risk.

**Improvement Path:**
Change relative paths in checklist items 2 and 4 to skill-relative paths matching the pattern used elsewhere. Verify `synthesis-validation.md` confidence classification definitions match the template's HIGH/MEDIUM descriptions at lines 302-304.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.88 | 0.92 | Add the second and third acceptable evidence examples from `heuristic-evaluation-rules.md` [Evidence Quality Standard] to the finding block comment (H2 terminology example and H4 consistency example). Add one unacceptable example with contrast ("The form feels confusing" -- vague, no interface reference). This brings inline evidence guidance from one case to full-contrast coverage. |
| 2 | Traceability | 0.90 | 0.93 | (a) Replace relative paths in Self-Review Checklist items 2 and 4 with skill-relative paths. (b) Verify `synthesis-validation.md` HIGH/MEDIUM definitions match template lines 302-304. (c) Add anchor reference for which section of synthesis-validation.md governs the confidence protocol. |
| 3 | Completeness | 0.92 | 0.95 | (a) Add "do not modify" comment to Methodology section to protect fixed prose. (b) Add explicit column count guidance to Coverage Matrix as instruction text (not comment). (c) Add minimum content guidance to Strategic Implications subsections. |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score (specific line references from deliverable)
- [x] Uncertain scores resolved downward (Evidence Quality at 0.88 not rounded up to 0.90)
- [x] C4 calibration applied (0.95 threshold; deliverable at 0.916 is correctly REVISE not PASS)
- [x] No dimension scored above 0.95 (highest is Internal Consistency and Methodological Rigor at 0.93)
- [x] Trajectory calibration considered: iter4=0.934, iter5=0.916 represents a score regression; anti-leniency requires scoring what is present, not what was expected

**Trajectory note:** The iter4 score of 0.934 was achieved by a different scorer or scoring context. This iter5 score of 0.916 is lower, reflecting a stricter application of the Evidence Quality rubric (the iter4 improvement -- adding one evidence example -- was scored generously in prior iterations; the 0.9+ criteria requires "all claims with credible citations" and the single-example coverage is genuinely below the 0.9 band). The trajectory from 0.843 to the current 0.916 represents genuine improvement; the gap to 0.95 is small and closable with the three targeted fixes above.

---

## Session Context Protocol

```yaml
verdict: REVISE
composite_score: 0.916
threshold: 0.95
weakest_dimension: evidence_quality
weakest_score: 0.88
critical_findings_count: 0
iteration: 5
improvement_recommendations:
  - "Add second and third acceptable evidence examples from rules file Evidence Quality Standard to finding block comment"
  - "Add one unacceptable evidence example with contrast for negative instruction"
  - "Replace relative paths in Self-Review Checklist items 2 and 4 with skill-relative paths"
  - "Verify synthesis-validation.md HIGH/MEDIUM confidence definitions match template lines 302-304"
  - "Add do-not-modify comment to Methodology section"
  - "Add explicit column count guidance to Coverage Matrix as instruction text"
  - "Add minimum content guidance to Strategic Implications subsections"
```

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Parent Skill: `/ux-heuristic-eval`*
*Project: PROJ-022 User Experience Skill*
*Scored: 2026-03-04*
