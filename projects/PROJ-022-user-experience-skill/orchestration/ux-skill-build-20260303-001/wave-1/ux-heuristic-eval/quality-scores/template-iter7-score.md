# Quality Score Report: Heuristic Report Template (v1.6.0)

## L0 Executive Summary

**Score:** 0.9055/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.87)
**One-line assessment:** The template is methodologically strong and well-traced with all three iter6 fixes confirmed present, but two internal inconsistencies (Synthesis Judgments category mismatches vs. rules file, degraded mode disclosure with 2 vs. 3 bullets) hold Internal Consistency below 0.90, pulling the composite to 0.9055 — 0.0145 below the C4 threshold of 0.92.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/templates/heuristic-report-template.md`
- **Deliverable Type:** Design (Template — fill-in-the-blank report template)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scoring Iteration:** 7
- **Score Trajectory:** 0.843 → 0.919 → 0.906 → 0.934 → 0.916 → 0.940 → 0.9055 (iter7)
- **Prior Score (iter6):** 0.940
- **C4 Threshold:** 0.95 (as specified in invocation) — see NOTE below
- **Scored:** 2026-03-04T00:00:00Z

> **NOTE on threshold:** The invocation specified "threshold >= 0.95" for C4 criticality. The SSOT `quality-enforcement.md` specifies >= 0.92 as the quality gate threshold (H-13). This report uses 0.92 as the SSOT threshold for PASS/REVISE/ESCALATE determination per H-13. The requestor may apply 0.95 as an aspirational target; this report flags both thresholds.

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.9055 |
| **SSOT Threshold (H-13)** | 0.92 |
| **C4 Aspirational Target** | 0.95 |
| **Verdict** | REVISE |
| **Gap to SSOT Threshold** | 0.0145 |
| **Gap to C4 Target** | 0.0445 |
| **Strategy Findings Incorporated** | No — no adv-executor reports provided |
| **Prior Iter6 Score** | 0.940 |
| **Score Delta** | -0.0345 (score decreased from iter6) |

> **Score decrease note:** The iter7 score (0.9055) is lower than iter6 (0.940). This is consistent with the oscillating trajectory observed across iters 2-6 (0.919→0.906→0.934→0.916→0.940). The decrease reflects stricter application of anti-leniency: iter7 identifies two concrete internal inconsistencies that were under-penalized in iter6. The three iter6 fixes are confirmed present and do produce improvements in Evidence Quality and Actionability, but the Internal Consistency dimension was scored at 0.87 due to specific contradictions found on close cross-document comparison.

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.1840 | All 11 required sections present; finding block covers all 6 fields; handoff YAML complete |
| Internal Consistency | 0.20 | 0.87 | 0.1740 | Two specific contradictions vs. parent documents found (see detail below) |
| Methodological Rigor | 0.20 | 0.93 | 0.1860 | 5-step workflow embedded; immutable methodology section; evidence/effort guidance inline |
| Evidence Quality | 0.15 | 0.88 | 0.1320 | 2+3 evidence examples at point of use; missing 3rd unacceptable example from rules file |
| Actionability | 0.15 | 0.91 | 0.1365 | Three iter6 fixes confirmed; Strong remediation structure; one weak subsection remains |
| Traceability | 0.10 | 0.93 | 0.0930 | Full chain from template → rules → agent → SSOT; field-level handoff markers |
| **TOTAL** | **1.00** | | **0.9055** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**
The template covers all 8 sections required by `heuristic-evaluation-rules.md` [Report Structure] (Executive Summary, Evaluation Context, Findings by Heuristic, Ranked Findings Summary, Remediation Roadmap, Strategic Implications, Synthesis Judgments Summary, Handoff Data) plus adds 3 structural extensions (Heuristic Coverage Matrix, Limitations and Reliability, Self-Review Checklist). All 10 heuristic sections (H1-H10) have repeatable finding blocks. AI supplement heuristics (AI-1/AI-2/AI-3) are provided as conditional comment blocks. The finding block includes all 6 required fields from Finding Documentation Rules. The handoff YAML covers all `handoff-v2` required fields and all `ux-ext` extension fields. The iter6 fix to the Overall Usability Assessment replaced a vague placeholder with a structured 3-element requirement.

**Gaps:**
- The `Input Modality Limitations` subsection (line 355) has a minimal placeholder (`{{Describe any limitations specific to the input mode...}}`) with conditional screenshot comments. For non-screenshot input modes, evaluators receive no scaffolding on what limitations to document.
- The `Heuristic Coverage Matrix` "Coverage note" placeholder (line 256) provides adequate guidance but could be more specific about what "potential systematic blind spot" means operationally.

**Improvement Path:**
Add a concrete instruction inside `Input Modality Limitations` subsection similar to: `<!-- If Figma MCP: document any design tokens or prototype states not accessible. If text description: note inability to evaluate visual hierarchy or spacing precisely. -->` This would close the coverage gap for non-screenshot input modes.

---

### Internal Consistency (0.87/1.00)

**Evidence:**
Two specific internal inconsistencies found through cross-document comparison:

**Inconsistency 1 — Synthesis Judgments categories (CONFIRMED):**
The template's minimum-content instruction (line 302) lists five judgment categories:
> `severity calibration, deduplication, effort estimation, confidence classification, scope boundary`

The rules file [Report Structure] section 8 (line 466) defines the exhaustive judgment call types as:
> `(a) severity calibration judgments, (b) deduplication decisions, (c) effort estimates, (d) AI-supplement applicability decisions, (e) cross-heuristic pattern grouping`

The template maps `confidence classification` where the rules say `AI-supplement applicability decisions`, and maps `scope boundary` where the rules say `cross-heuristic pattern grouping`. These are not synonyms. A template user following the template comment would document confidence classifications and scope boundaries — neither of which appears in the rules file's exhaustive list. Conversely, they would not be prompted to document AI-supplement applicability decisions or cross-heuristic pattern grouping.

**Inconsistency 2 — Degraded mode disclosure (CONFIRMED):**
The template's conditional degraded mode comment block (lines 81-84) lists 2 limitations:
> "Cannot inspect component states or interactive behaviors"
> "Cannot verify responsive behavior across breakpoints"

The SKILL.md [Figma Fallback: Screenshot-Input Mode] (lines 303-306) lists 3 limitations:
> "Cannot inspect component states (hover, focus, active, disabled)"
> "Cannot verify responsive behavior across breakpoints"
> "Cannot access style tokens or design system variables programmatically"

The third limitation is absent from the template's degraded mode comment block. An evaluator following the template would produce an incomplete degraded mode disclosure compared to what the rules document specifies.

**Minor observation (NOT inconsistency, properly noted):**
The template's evidence comment (lines 119-124) lists 2 unacceptable examples while the rules file [Evidence Quality Standard] lists 3 (the template omits "This violates H1" — circular). This was partially addressed by the iter6 fix adding the second unacceptable example, but the third remains absent from the template. This affects Evidence Quality dimension, not Internal Consistency, since the rules file is an independent source rather than a contradiction within the same document.

**Improvement Path:**
1. Align the Synthesis Judgments comment categories exactly with the rules file: replace `confidence classification` → `AI-supplement applicability` and `scope boundary` → `cross-heuristic pattern grouping`.
2. Add the third degraded mode limitation to the template comment block: add `- Cannot access style tokens or design system variables programmatically`.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**
The template operationalizes the 5-step evaluation workflow through its section structure. The immutable Methodology section (lines 88-98) locks in the standard workflow description with source citations. Evidence quality guidance is embedded in the finding block comment at the exact point of use. Effort classification criteria are cross-referenced from the rules. Deduplication instructions appear before the findings section (lines 104-105). The ID assignment sequencing instruction is explicit and correct: "Assign F-{NNN} IDs only after all findings are ranked by severity." The Heuristic Coverage Matrix is a methodological strengthening not required by the rules file but that provides completeness verification. The P-022 disclosure about AI supplements being non-published extensions (line 94) demonstrates methodological honesty. The AI supplement heuristics are conditionally gated and properly labeled `[AI-SUPPLEMENT]`.

**Gaps:**
- No per-heuristic prompt within individual heuristic sections (H1-H10) to remind evaluators of the specific evaluation checkpoints from the rules file. The rules file provides 4-5 checkpoints per heuristic; the template provides only a heading and the repeatable block. An evaluator using the template without reading the rules file would miss the structured checkpoint approach.

**Improvement Path:**
Consider adding a brief checkpoint reminder comment inside each H1-H10 section, e.g., `<!-- H1 checkpoints: action feedback, loading states, completion confirmation, state change visibility, current location indicator -->`. This would make the template more self-contained for evaluators who do not keep the rules file open.

---

### Evidence Quality (0.88/1.00)

**Evidence:**
The iter6 fix is confirmed: line 124 contains `"Users probably struggle here" (unacceptable -- speculative claim, no observed behavior or interface element reference)`. The template now has 3 acceptable and 2 unacceptable examples inline in the finding block comment. The cross-reference to `heuristic-evaluation-rules.md [Evidence Quality Standard]` is present. The evidence field description (`{{specific interface observation demonstrating the violation}}`) is specific and action-oriented. The methodology section cites Nielsen (1994a, 1994b, 1994c, 2020), Amershi et al. (2019), and Google PAIR (2019) — all sourced from verifiable academic and practitioner publications. The HEART framework citation in the footer (Rodden, Hutchinson & Fu 2010) includes conference and title. The handoff schema citation (`docs/schemas/handoff-v2.schema.json`) is verifiable. The P-022 disclosure for AI supplements is explicit and specific about the source publications.

**Gaps:**
- The template's inline evidence comment omits the third unacceptable example from the rules file: `"This violates H1" (circular, restates the heuristic without evidence)`. This example is pedagogically valuable — it covers a common evaluator failure mode (circular reasoning) that is distinct from the two present examples (subjective feeling and speculative claim). A template that omits this example provides slightly weaker evidence quality guidance than the rules document it derives from.

**Improvement Path:**
Add the third unacceptable example to the finding block comment: `Unacceptable: "This violates H1" (unacceptable -- circular, restates the heuristic without citing a specific observable interface element).`

---

### Actionability (0.91/1.00)

**Evidence:**
All three iter6 actionability fixes are confirmed present and materially improve the dimension:

1. **Strategic Implications minimum instruction** (line 321): `<!-- Required: identify at least one pattern per subsection. Minimum two sentences per subsection. -->` — Prevents empty sections; the three subsections each have meaningful placeholder text showing what to write.

2. **Synthesis Judgments minimum instruction** (line 302): `<!-- Required: document at minimum one judgment per category present... (5 categories listed) -->` — Prevents empty tables; the example table rows (lines 308-311) show evaluators what to document.

3. **Overall Usability Assessment** (line 56): `{{One paragraph covering: (1) key strengths observed, (2) critical weaknesses identified, (3) overall release readiness assessment. All three elements required.}}` — This is markedly more actionable than a vague placeholder; the three required elements are explicit.

Additional strengths: The Remediation Roadmap groups findings by effort level with priority ordering guidance. The "Suggested Implementation Order" paragraph placeholder (line 296) provides specific guidance on sequencing (severity 4 first, then quick wins, then medium/high by severity). The Handoff YAML template is ready for direct ingestion by downstream sub-skills. The Self-Review Checklist provides 10 binary items that are directly actionable pre-persistence.

**Gaps:**
- `Input Modality Limitations` subsection (line 355) has placeholder `{{Describe any limitations specific to the input mode used for this evaluation.}}` with no minimum-content instruction analogous to the fixes applied to Strategic Implications and Synthesis Judgments. Evaluators can leave this section with a single vague sentence and nothing in the template prevents it.
- The Coverage note in the Heuristic Coverage Matrix (line 256) is a placeholder paragraph rather than a structured field, which could result in evaluators skipping the blind-spot identification.

**Improvement Path:**
Add a minimum-content instruction to `Input Modality Limitations`: `<!-- Required: document at least one limitation specific to the input mode used. For screenshot-input, use the bullet comments below as a starting point. -->` This mirrors the approach applied to Strategic Implications and Synthesis Judgments in iter6.

---

### Traceability (0.93/1.00)

**Evidence:**
Full traceability chain verified:
- Template header (lines 1-4): VERSION 1.6.0, DATE 2026-03-04, REVISION history, SKILL, AGENT, SOURCE documents.
- Template footer (lines 442-447): Template Version, sub-skill, project, source documents (3), external citations (Nielsen 1994a/b/c/2020, Amershi 2019, PAIR 2019, HEART 2010), handoff schema path, ORCHESTRATION.yaml path.
- Finding block: references `heuristic-evaluation-rules.md [Evidence Quality Standard]` inline.
- Methodology section: references `heuristic-evaluation-rules.md [Evaluation Workflow]` and cites Nielsen source.
- Self-Review Checklist: references `heuristic-evaluation-rules.md [Self-Review Checklist (S-010)]` and `heuristic-evaluation-rules.md#finding-documentation-rules` and `heuristic-evaluation-rules.md#deduplication-rules`.
- Synthesis Judgments: references `skills/user-experience/rules/synthesis-validation.md`.
- Heuristic Coverage Matrix: references `heuristic-evaluation-rules.md [Self-Review Checklist (S-010)]`.
- Handoff YAML: field-level markers `[handoff-v2]` and `[ux-ext]` with schema citation.
- Deduplication comment: references `heuristic-evaluation-rules.md [Deduplication Rules]`.
- ORCHESTRATION.yaml link: confirmed at line 447.

**Gaps:**
- The `Single-Evaluator Disclosure` section (line 341) cites "(Nielsen, 1994c)" without the full title inline. The footer provides the full citation. This is a minor gap by academic standards but is not a broken chain.
- The Heuristic-to-HEART mapping in the Handoff Data section (lines 398-399) references `heuristic-evaluation-rules.md [Heuristic-to-HEART Category Mapping]` in a comment, which is present and verifiable — no gap.

**Improvement Path:**
No significant changes needed. The minor inline citation gap is convention-level, not a substantive traceability failure.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.87 | 0.92+ | Align Synthesis Judgments comment categories exactly with rules file: `confidence classification` → `AI-supplement applicability`; `scope boundary` → `cross-heuristic pattern grouping` |
| 2 | Internal Consistency | 0.87 | 0.92+ | Add third degraded mode limitation to template comment block: `- Cannot access style tokens or design system variables programmatically` (line 83 area) |
| 3 | Evidence Quality | 0.88 | 0.92+ | Add third unacceptable example to finding block: `"This violates H1" (unacceptable -- circular, restates the heuristic without observable interface reference)` |
| 4 | Actionability | 0.91 | 0.93+ | Add minimum-content instruction to `Input Modality Limitations` subsection: `<!-- Required: document at least one limitation specific to the input mode used. -->` |
| 5 | Completeness | 0.92 | 0.94 | Add conditional comment inside `Input Modality Limitations` for non-screenshot modes (Figma, text description) to guide evaluators on what limitations to document |

---

## Iter6 Fix Verification (Three Fixes — All Confirmed)

| Fix | Expected Location | Status | Quote from Deliverable |
|-----|------------------|--------|------------------------|
| Fix 1: Second unacceptable evidence example | Finding block comment, line 124 | CONFIRMED | `"Users probably struggle here" (unacceptable -- speculative claim, no observed behavior or interface element reference).` |
| Fix 2a: Strategic Implications minimum instruction | Line 321, after section heading | CONFIRMED | `<!-- Required: identify at least one pattern per subsection. Minimum two sentences per subsection. -->` |
| Fix 2b: Synthesis Judgments minimum instruction | Line 302, after section heading | CONFIRMED | `<!-- Required: document at minimum one judgment per category present in the evaluation (severity calibration, deduplication, effort estimation, confidence classification, scope boundary). -->` |
| Fix 2c: Overall Usability Assessment structured placeholder | Line 56 | CONFIRMED | `{{One paragraph covering: (1) key strengths observed, (2) critical weaknesses identified, (3) overall release readiness assessment. All three elements required.}}` |
| Fix 3: Version bump 1.5.0 → 1.6.0 | Header line 1 and footer line 442 | CONFIRMED | `VERSION: 1.6.0` in header; `Template Version: 1.6.0` in footer |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Internal Consistency resolved to 0.87, not 0.89)
- [x] First-draft calibration not applicable (iteration 7); oscillating trajectory considered
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Score decrease from iter6 (0.940 → 0.9055) accepted as correct; iter6 was lenient on Internal Consistency

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.9055
threshold: 0.92
weakest_dimension: internal_consistency
weakest_score: 0.87
critical_findings_count: 0
iteration: 7
improvement_recommendations:
  - "Align Synthesis Judgments comment categories with rules file (confidence classification -> AI-supplement applicability; scope boundary -> cross-heuristic pattern grouping)"
  - "Add third degraded mode limitation: Cannot access style tokens or design system variables programmatically"
  - "Add third unacceptable evidence example: This violates H1 (circular)"
  - "Add minimum-content instruction to Input Modality Limitations subsection"
  - "Add non-screenshot conditional guidance to Input Modality Limitations"
```

---

*Score Report Version: 1.0*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Parent Artifacts Read: heuristic-evaluation-rules.md (v1.2.0), ux-heuristic-evaluator.md (v1.0.0), SKILL.md (v1.0.0)*
*Project: PROJ-022 User Experience Skill*
*Created: 2026-03-04*
