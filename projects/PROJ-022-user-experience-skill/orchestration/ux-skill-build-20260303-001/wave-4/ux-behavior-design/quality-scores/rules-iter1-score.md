# Quality Score Report: Fogg B=MAP Behavior Methodology Rules

## L0 Executive Summary

**Score:** 0.893/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.82)
**One-line assessment:** A well-structured, methodologically sound rules file that is close to the C4 threshold but blocked by three specific defects: missing "Consequence of Violation" column in the Confidence Classification rule tables, a version discrepancy in the Related Files table for wave-progression.md, and a missing action-line position requirement in the output format rules.

---

## Scoring Context

- **Deliverable:** `skills/ux-behavior-design/rules/fogg-behavior-rules.md`
- **Deliverable Type:** Methodology rules file (sub-skill operational constraints)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md` (Quality Gate section)
- **C4 Pass Threshold:** >= 0.95 (per QG-001 in the artifact itself; H-13 baseline is >= 0.92)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.893 |
| **C4 Threshold** | 0.95 |
| **H-13 Baseline** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (standalone scoring) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 10 rule sections present with navigation, self-review, related files; missing action-line position in OUT rules |
| Internal Consistency | 0.20 | 0.88 | 0.176 | Convergence model framing consistent throughout; wave-progression.md version conflict between rules file (unversioned) and agent definition (v1.2.0); CLS table format breaks column pattern |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Fogg citations precise with DOI; convergence enforcement at rule level; elimination algorithm correctly ordered; severity heuristics honestly disclosed |
| Evidence Quality | 0.15 | 0.82 | 0.123 | Fogg (2009)/(2020) properly cited; CLS-001–005 rule table drops "Consequence of Violation" column, breaking evidence chain for 5 rules; template reference not verified to exist |
| Actionability | 0.15 | 0.91 | 0.137 | 18-item self-review checklist directly maps to rule IDs; output format provides completeness criteria; intervention matrix specific; ALG-005 (MEDIUM) has no consequence documented |
| Traceability | 0.10 | 0.90 | 0.090 | Source callouts per section with DOI; dependency matrix with versions; footer traceability comment; rule ID pattern consistent (BMAP/MOT/ABL/PRM/ALG/INT/SEV/CLS/OUT/QG); unversioned references weaken chain |
| **TOTAL** | **1.00** | | **0.893** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence for score:**
The rules file covers 10 distinct rule sections with a total of 50 rules (BMAP-001–005, MOT-001–006, ABL-001–007, PRM-001–005, ALG-001–005, INT-001–007, SEV-001–003, CLS-001–005, OUT-001–007, QG-001–004). Each section addresses a distinct aspect of the B=MAP methodology. The navigation table lists all 12 sections with correct anchor links. The self-review checklist has 18 items. The Related Files dependency matrix maps 8 upstream/downstream/sibling files. Quality gate integration maps all 6 S-014 dimensions to Behavior Design evaluation criteria.

**Gaps identified:**

1. **Missing action-line position in output format rules.** The SKILL.md (line 391) explicitly lists "action-line position" as a required output element in the Phase 2 Behavior Mapping output ("B=MAP state map: motivation scores, ability scores with limiting factor, prompt assessment, action-line position"). The agent definition (line 185) similarly requires it ("B=MAP state map: motivation scores (3 pairs + 3 dimensions), ability scores (6 simplicity factors with limiting factor), prompt assessment (type, timing, placement), action-line position"). However, OUT-004 in the rules file states "The Behavior State Map MUST include all scoring tables: motivation pairs (3 rows), motivation dimensions (3 rows), simplicity factors (6 rows), and prompt assessment (4 rows)" — with no mention of the action-line position requirement. This is a completeness gap: the rules file does not enforce a requirement that both SKILL.md and the agent definition specify.

2. **CLS-001–005 rule table omits "Consequence of Violation" column.** Every other rule table in the document (BMAP, MOT, ABL, PRM, ALG, INT, SEV) includes a "Consequence of Violation" column in the table header `| ID | Rule | Tier | Consequence of Violation |`. The Confidence Classification Discipline table drops the last column: `| ID | Rule | Tier |`. Five rules (CLS-001 through CLS-005) lack consequence documentation, which is a structural omission that the self-review checklist does not catch.

**Improvement Path:**
- Add action-line position to OUT-004: "The Behavior State Map MUST include all scoring tables: motivation pairs (3 rows), motivation dimensions (3 rows), simplicity factors (6 rows), prompt assessment (4 rows), AND an action-line position statement."
- Add the "Consequence of Violation" column to the CLS-001–005 rule table, with entries such as: CLS-001 → "Judgment calls without confidence classification cannot be validated by downstream synthesis pipeline; P-022 violation"; CLS-002 → "Intervention classified MEDIUM/HIGH misleads teams into false confidence; intervention effectiveness requires empirical validation"; CLS-003 → "HIGH classification without quantitative data overstates certainty of factor rating; P-022 violation".

---

### Internal Consistency (0.88/1.00)

**Evidence for score:**
The B=MAP convergence framing is applied consistently. BMAP-001 explicitly forbids multiplication framing ("NEVER describe behavior as the 'product' or 'multiplication' of M, A, and P"). The SKILL.md Phase 2 description (line 136) echoes: "This is NOT a multiplication model -- it is a convergence model." The agent definition (line 34) likewise states: "not through multiplication but through concurrent sufficiency."

The quality gate threshold is internally consistent: QG-001 states "At C4 criticality... the threshold is >= 0.95" — this matches the invocation context (C4) and the SKILL.md Quality Gate Integration table which cites ">= 0.92 (H-13, C2+)."

The algorithm halt rule (ALG-002) is consistent with the algorithm procedure: "If Step 1 identifies a prompt bottleneck, Steps 2-4 do NOT execute as primary bottleneck identification." The elimination procedure itself (Step 1 through Step 4) uses "HALT" consistently.

**Gaps identified:**

1. **wave-progression.md version discrepancy.** The Related Files table states: `| Wave progression | skills/user-experience/rules/wave-progression.md | unversioned -- tracked via git history |`. However, the agent definition (ux-behavior-diagnostician.md line 56) states: "This agent is part of Wave 4 (Advanced Analytics, per `skills/user-experience/rules/wave-progression.md` v1.2.0)". These two files conflict: the rules file says wave-progression.md is unversioned; the agent definition says it is v1.2.0. One reference is incorrect.

2. **CLS rule table column inconsistency.** All other rule tables use `| ID | Rule | Tier | Consequence of Violation |`. The CLS section uses `| ID | Rule | Tier |`. This creates a structural inconsistency within the document. A reader following the HARD rule pattern would notice the consequence column is missing for CLS rules, potentially causing uncertainty about whether omission was intentional.

3. **Severity discipline tier assignment inconsistency.** SEV-003 is classified as MEDIUM tier. Its description states "Severity MUST be derived from factor score patterns." The word "MUST" is a HARD tier keyword per the quality-enforcement.md Tier Vocabulary ("MUST, SHALL, NEVER, FORBIDDEN, REQUIRED, CRITICAL" → HARD). However, the tier column says MEDIUM. This is a minor but real inconsistency: MEDIUM tier uses "SHOULD, RECOMMENDED, PREFERRED." A rule using "MUST" should be HARD.

**Improvement Path:**
- Resolve wave-progression.md version reference: either add a version number to the rules file's Related Files entry if the file has one, or remove the version reference from the agent definition.
- Add "Consequence of Violation" column to CLS-001–005 rule table.
- Review SEV-003 tier: if the consequence is meaningful (systematic severity estimation without quantitative data is important), upgrade to HARD. If truly optional, change "MUST" to "SHOULD."

---

### Methodological Rigor (0.92/1.00)

**Evidence for score:**
The Fogg (2009) DOI is cited at the document header and in the first major section blockquote: `DOI: 10.1145/1541948.1541999`. The three primary structural elements of the methodology (convergence model, elimination algorithm, intervention difficulty gradient) are each grounded in specific citations. The elimination algorithm section sources Fogg (2020) Chapters 2-3 for intervention difficulty ordering and Fogg (2009) for action threshold. The behavior statement format cites Fogg (2020) Chapters 14-15 (line 48). The simplicity factors section cites Fogg (2009) Section 4: "Simplicity as a Function of a Person's Scarcest Resource."

The limiting factor principle is correctly stated: "Improving any factor except the limiting one does not raise overall ability above the action threshold" — this accurately reflects Fogg's scarcest resource concept.

The convergence_timing edge case (ALG-004) is correctly documented: "only when all three factors score 4+ AND the behavior does not occur" — preventing misuse as a fallback. ALG-004 cites Fogg (2009) for environmental context factors.

The severity classification section correctly discloses: "The 10% and 50% thresholds are calibration anchors for the /user-experience skill's target audience (tiny teams, 1-5 people)" — honest about the heuristic nature of thresholds.

**Gaps identified:**

1. **No rule enforcing the action-line position output.** The Fogg (2009) paper's core visual artifact is the motivation-ability plane with the action line. SKILL.md and the agent definition both require an action-line position statement in the output. The rules file (specifically OUT-004) does not enforce this. While this is primarily a completeness gap, it also weakens methodological rigor: the action-line position is a key analytical step that makes the B=MAP diagnosis interpretable. Without it, a diagnosis could technically comply with all output rules yet omit one of the methodology's primary analytical artifacts.

2. **PRM-004 (MEDIUM) ambiguity.** PRM-004 states "Prompt timing MUST be assessed relative to the moment when the user's motivation-ability position is above the action line." Again, "MUST" appears in a MEDIUM-tier rule — the same tier vocabulary inconsistency as SEV-003. This is a methodology rigor issue: timing assessment is important enough to mandate.

**Improvement Path:**
- Add action-line position to OUT-004 (addresses both Completeness and Methodological Rigor).
- Review PRM-004 tier assignment; upgrade to HARD if timing assessment is genuinely required.

---

### Evidence Quality (0.82/1.00)

**Evidence for score:**
Primary methodology citations are well-formed. Fogg (2009) is cited with full DOI at the document header and repeated in section blockquotes. Fogg (2020) is cited with specific chapter numbers: "Chapters 14-15" for behavior statement format (matching the agent definition which also specifies Chapters 14-15), "Chapters 2-3" for intervention difficulty ordering. The severity classification source honestly discloses heuristic origin: "Severity thresholds are framework-internal heuristics derived from conversion rate analysis patterns."

Confidence Classification sourcing is clear: "Source: `skills/user-experience/rules/synthesis-validation.md` (v1.1.0) Section 'Confidence Classification' and Section 'Sub-Skill Synthesis Output Map'."

**Gaps identified (driving score to 0.82 — the weakest dimension):**

1. **CLS-001–005: No consequence documentation.** As noted under Completeness and Consistency, the consequence column is missing from the Confidence Classification rule table. This affects Evidence Quality because the consequence provides the rationale chain — why these rules matter, what failure looks like. Without consequences, CLS rules are assertions without grounding. This is the most significant evidence quality defect in the document.

2. **Template file existence not verified.** OUT-001 references `skills/ux-behavior-design/templates/bmap-diagnosis-template.md` as the required structure source. The Related Files table also references it at version v1.2.0. However, there is no in-document verification that this file exists. If the template does not exist, OUT-001 through OUT-007 reference a non-existent source, undermining the evidence basis for the output format rules.

3. **MOT-005 evidence standard is asserted without methodological grounding.** MOT-005 states "Motivation scores MUST NOT exceed 3 when the only evidence is team assumptions or general UX principles. Scores of 4-5 require direct evidence (analytics, user research, interview data)." This rule is correct and important, but it lacks a source citation. The other score-evidence rules (MOT-003, ABL-003) cite P-001, but MOT-005 cites nothing. It would be stronger with a reference to either P-001 (truth/accuracy) or a Fogg citation on evidence-based motivation assessment.

4. **CLS-004 minimum-confidence rule lacks source.** CLS-004 states "The minimum-confidence rule applies: when a single finding draws from multiple judgment types with different confidence levels, the finding's confidence is the LOWEST among all contributing judgments." This is a sound rule, but no source is provided — not synthesis-validation.md (which is cited for the section), not the quality-enforcement.md, not any constitutional principle. It appears to be a framework-internal rule without traceability.

**Improvement Path (priority ordered):**
1. Add "Consequence of Violation" column to CLS-001–005 with specific consequences for each.
2. Verify template file existence; if it does not exist, note that it is a planned artifact.
3. Add source citation to MOT-005 (P-001 or Fogg, 2020 on evidence-based scoring).
4. Add source attribution to CLS-004 (synthesis-validation.md or framework-internal heuristic disclosure matching the pattern used in the severity section).

---

### Actionability (0.91/1.00)

**Evidence for score:**
The 18-item self-review checklist is the strongest actionability asset. Each item maps directly to a rule ID (e.g., "Check 1: BMAP-004", "Check 4: MOT-001", "Check 9: ALG-001, ALG-003"). This makes post-completion verification deterministic. An agent following the checklist will touch every major rule category.

The intervention discipline rules are highly specific: INT-001 mandates "3-5 specific intervention recommendations" (not a vague range), INT-002 mandates 6 specific fields per intervention (description, target factor, expected impact, implementation effort, classification, supporting reasoning), INT-003 mandates prioritization by effort-to-impact, INT-004 mandates LOW confidence on ALL interventions. These rules give implementers no ambiguity about what constitutes compliant output.

The quality gate dimension mapping table gives concrete evaluation criteria per S-014 dimension, making scoring predictable and actionable for reviewers.

**Gaps identified:**

1. **ALG-005 (MEDIUM): No consequence documented.** ALG-005 states "For `multiple` bottleneck classification, the diagnosis MUST specify which factors are borderline and recommend addressing the cheapest-to-fix factor first." Unlike ALG-001–004 (HARD rules with consequences), ALG-005 (MEDIUM) has a consequence column entry of nothing visible in the table. The rule uses "MUST" language but is marked MEDIUM with no stated consequence. Implementers cannot easily determine what happens if they violate this rule.

2. **SEV-003 consequence not actionable.** SEV-003 is MEDIUM tier and its consequence states only "Provides a systematic severity estimation when quantitative data is unavailable" — this reads as a benefit statement, not a consequence of violation. What happens if SEV-003 is not followed? The consequence column should state what goes wrong (e.g., "Inconsistent severity classification when operating qualitatively; teams cannot prioritize behavioral issues without a severity estimate").

**Improvement Path:**
- Add violation consequence to ALG-005: e.g., "Unordered multiple bottleneck diagnosis leaves teams without a starting intervention point; multiple bottleneck diagnoses without prioritization are not actionable."
- Rewrite SEV-003 consequence as a violation consequence, not a feature description.

---

### Traceability (0.90/1.00)

**Evidence for score:**
The document header contains a full VERSION comment with source files and versions: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/ux-behavior-design/SKILL.md (v1.5.0), skills/ux-behavior-design/agents/ux-behavior-diagnostician.md (v1.2.0), Fogg (2009) DOI:10.1145/1541948.1541999, Fogg (2020) -->`. The footer traceability comment cites PROJ-022 EPIC-004 and all governance standards referenced.

Each major section contains a `> **Source:**` blockquote with a specific Fogg citation (section and DOI where applicable). The Related Files dependency matrix maps each file to its relationship type (parent, agent, governance, template, wave, synthesis, MCP, quality enforcement), version, and purpose. Rule IDs follow a predictable prefix pattern (BMAP, MOT, ABL, PRM, ALG, INT, SEV, CLS, OUT, QG) that maps 1:1 to the section they appear in.

The quality gate section traces directly to `.context/rules/quality-enforcement.md` Section "Quality Gate" and correctly identifies the >= 0.95 C4 threshold.

**Gaps identified:**

1. **Unversioned references weaken the traceability chain.** Two files in the Related Files table are listed as "unversioned -- tracked via git history": `wave-progression.md` and `mcp-coordination.md`. This means changes to those files cannot be cross-referenced from a specific version of the rules file. The note "tracked via git history" is an acknowledgment but not a resolution of the traceability gap.

2. **CLS-004 has no traceable source.** As noted under Evidence Quality, CLS-004's minimum-confidence rule has no citation. Without a source, the rule cannot be traced to a governing principle, framework, or prior decision.

3. **QG-001 threshold discrepancy not reconciled.** QG-001 states "Baseline threshold: >= 0.92 (H-13, C2+). At C4 criticality... the threshold is >= 0.95." The quality-enforcement.md SSOT does not explicitly state a C4-specific override; it states >= 0.92 as the general threshold. The artifact itself (QG-001) and the Related Files table state ">= 0.95 at C4" but this appears to be a framework extension that is not back-traced to a specific governing decision. The traceability chain for the C4 threshold would benefit from a citation to the governance decision that established the 0.95 C4 override (e.g., a reference to the ORCHESTRATION.yaml or orchestrator context that specified C4 scoring for this artifact).

**Improvement Path:**
- Add version numbers to wave-progression.md and mcp-coordination.md, or replace "unversioned" with the current git commit hash or date-stamp for traceability.
- Add source citation to CLS-004.
- Add a reference explaining the governance source of the >= 0.95 C4 threshold (or acknowledge it is an orchestrator-specified context for this scoring session).

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.82 | 0.90 | Add "Consequence of Violation" column to CLS-001–005 rule table with specific consequences for each of the 5 rules. This single fix resolves the most significant structural defect in the document. |
| 2 | Completeness | 0.90 | 0.95 | Add action-line position requirement to OUT-004: "The Behavior State Map MUST include all scoring tables... AND an explicit action-line position statement describing whether the user is above or below the action line and which factor(s) need to change." |
| 3 | Internal Consistency | 0.88 | 0.94 | Resolve the wave-progression.md version discrepancy: the rules file says "unversioned" but the agent definition says "v1.2.0." Choose one authoritative statement and apply it consistently to both files. |
| 4 | Internal Consistency | 0.88 | 0.94 | Review SEV-003 and PRM-004 tier assignments: both use "MUST" language but are classified MEDIUM. Upgrade to HARD or change language to "SHOULD" to align tier vocabulary with the tier-vocabulary table in quality-enforcement.md. |
| 5 | Evidence Quality | 0.82 | 0.90 | Add source citation to MOT-005 (P-001 for truth/accuracy) and CLS-004 (synthesis-validation.md or "framework-internal heuristic" disclosure). |
| 6 | Actionability | 0.91 | 0.95 | Fix SEV-003 consequence column: rewrite from a feature description ("Provides a systematic severity estimation") to a violation consequence ("Inconsistent severity classification when quantitative data is absent; teams cannot prioritize behavioral issues systematically"). |
| 7 | Traceability | 0.90 | 0.94 | Add source traceability for the >= 0.95 C4 threshold in QG-001 (reference the governance decision or orchestrator context that specified C4 for this artifact). |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific line-number references where applicable
- [x] Uncertain scores resolved downward (Evidence Quality: chose 0.82 over 0.85 due to 4 distinct evidence gaps)
- [x] First-draft calibration considered (this is iteration 1; scored against 0.92-0.95 benchmark, not impressionistically)
- [x] No dimension scored above 0.95 without exceptional evidence (Methodological Rigor is the highest at 0.92)

**Anti-leniency decisions made:**
- Internal Consistency reduced to 0.88 (not 0.90+) specifically because the SEV-003/PRM-004 tier-vocabulary mismatch is a genuine inconsistency that the document governance model requires to be internally self-consistent.
- Evidence Quality reduced to 0.82 (not 0.86+) because missing consequences for an entire 5-rule table is a structural defect, not a cosmetic one — the consequence column provides the evidence chain for why rules matter.
- Completeness held at 0.90 (not 0.93+) because the action-line position gap is a real omission traceable to SKILL.md and agent definition, not an ambiguous case.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.893
threshold: 0.95
weakest_dimension: evidence_quality
weakest_score: 0.82
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add Consequence of Violation column to CLS-001–005 rule table (5 rules missing consequences)"
  - "Add action-line position requirement to OUT-004 (gap vs. SKILL.md and agent definition)"
  - "Resolve wave-progression.md version conflict between rules file (unversioned) and agent definition (v1.2.0)"
  - "Review SEV-003 and PRM-004 tier assignments — MUST language in MEDIUM-tier rules"
  - "Add source citations to MOT-005 and CLS-004"
  - "Rewrite SEV-003 consequence from feature description to violation consequence"
  - "Add governance traceability for >= 0.95 C4 threshold in QG-001"
```

---

*Score Report Version: 1.0.0*
*Scored by: adv-scorer (S-014 LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-behavior-design/rules/fogg-behavior-rules.md` v1.0.0*
*Context files reviewed: SKILL.md v1.5.0, ux-behavior-diagnostician.md v1.2.0, quality-enforcement.md v1.6.0*
*Created: 2026-03-04*
