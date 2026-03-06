<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/ux-kano-model/rules/kano-methodology-rules.md | SCORED BY: adv-scorer (S-014) | ITERATION: 1 -->

# Quality Score Report: Kano Methodology Rules

## L0 Executive Summary

**Score:** 0.869/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness (0.82)

**One-line assessment:** The rules file is methodologically sound and internally consistent but fails to reach C4 threshold (0.95) primarily because survey question design rules are entirely absent, the Q > 10% threshold is unsourced, and survey administration discipline (randomization, priming avoidance) is missing from the enforceable rule layer.

---

## Scoring Context

- **Deliverable:** `skills/ux-kano-model/rules/kano-methodology-rules.md`
- **Deliverable Type:** Methodology rules file (sub-skill operational constraints)
- **Criticality Level:** C4 (threshold >= 0.95 per scoring prompt; H-13 floor >= 0.92)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.869 |
| **Threshold (C4)** | 0.95 |
| **Threshold (H-13 floor)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.82 | 0.164 | 5x5 table, CS formulas, sample/split/lifecycle/priority/confidence/self-review all present; survey question design rules section entirely absent |
| Internal Consistency | 0.20 | 0.93 | 0.186 | No contradictions found; EVT-004/CSC-001 R/Q distinction correct; sample tiers match agent definition exactly; priority ordering consistent across sections |
| Methodological Rigor | 0.20 | 0.87 | 0.174 | Systematic rule IDs, HARD/MEDIUM tiers, source citations per section; gaps in survey administration discipline and partial-response handling |
| Evidence Quality | 0.15 | 0.84 | 0.126 | Three primary sources cited throughout; practitioner estimates labeled; Q > 10% threshold (SPL-005) has zero source citation |
| Actionability | 0.15 | 0.88 | 0.132 | Concrete markers, formula example, 14-item checklist, tie-breaking rules; LCY-003 re-evaluation interval unspecified; R > 20% user-segment rule in agent but not in rules file |
| Traceability | 0.10 | 0.87 | 0.087 | Systematic rule IDs, VERSION header, dependency matrix, footer traceability; rule-to-requirement chain absent; SPL-005 threshold fully untraced |
| **TOTAL** | **1.00** | | **0.869** | |

---

## Detailed Dimension Analysis

### Completeness (0.82/1.00)

**Evidence:**

Present and well-developed:
- 5x5 functional x dysfunctional evaluation table: Canonical table reproduced at lines 32-38 with all 25 cells labeled M/O/A/I/R/Q and the 5-point response scale defined (lines 43-48).
- CS coefficient formulas: Better and Worse formulas present at lines 70-73 with range annotations.
- R/Q exclusion from CS coefficient computation: CSC-001 explicitly governs denominator construction; CSC-003 covers zero-denominator edge case.
- Feature lifecycle dynamics: LCY-001 through LCY-005 cover evidence requirements, confidence classification, one-way migration constraint, and longitudinal tracking.
- Statistical significance requirements: SSC-001 through SSC-005 cover all sample size tiers from 0 to 50+ with confidence disclosure requirements.
- Self-review checklist: 14-item checklist at lines 283-298 covers all rule sections with rule ID back-references.
- Cross-references: Related Files dependency matrix at lines 266-274 lists parent SKILL.md, agent definition, governance YAML, wave-progression.md, synthesis-validation.md, templates, and quality-enforcement.md with versions.

**Gaps:**

1. **Survey question design rules: Entirely absent.** The artifact claims to provide "operational constraints and methodology rules for the ux-kano-analyst agent" but contains no section governing survey question pair construction. The agent definition (ux-kano-analyst.md, Phase 2) has guidance for crafting functional/dysfunctional question pairs, but that guidance is not backed by enforceable HARD/MEDIUM rules in this rules file. A Kano methodology rules file that does not govern the question pair — the instrument on which all downstream classification depends — has a material coverage gap. Specifically missing: rules on language requirements (concrete, no developer jargon), balance requirements (avoiding leading questions), dysfunctional question formulation discipline, and verification that both functional and dysfunctional questions are present for each feature.

2. **Survey administration discipline: Absent.** No rules governing randomization of feature order, priming avoidance, or respondent selection criteria. These appear in the agent Phase 2 methodology as guidance but not as enforceable rules.

3. **Partial-response handling: Absent.** No rule covering what to do when a respondent answers the functional question but not the dysfunctional question (or vice versa) for a feature. The agent has no fallback rule to enforce here.

**Improvement Path:**
Add a "Survey Question Design Rules" section with HARD rules governing: (a) functional question phrasing format ("How would you feel if this product had [X]?"), (b) dysfunctional question phrasing format ("How would you feel if this product did NOT have [X]?"), (c) language requirements (concrete, non-jargon, balanced tone), (d) completeness requirement (both questions must be present for each feature), and (e) administration discipline (randomization, priming avoidance). Add a rule for partial-response handling.

---

### Internal Consistency (0.93/1.00)

**Evidence:**

The document demonstrates strong internal consistency across all sections:

- **EVT-004 / CSC-001 coherence:** EVT-004 (line 57) states R/Q MUST be retained in the display table; CSC-001 (line 81) states R/Q MUST be excluded from the CS denominator. These two rules correctly govern different aspects of the same data and do not contradict each other.
- **Sample size tiers:** The Confidence Tier Mapping table (lines 97-104) exactly matches the sample size disclosures in Phase 3 of the agent definition (lines 181-186 of ux-kano-analyst.md) and the agent's expertise section. No divergence in thresholds.
- **Split detection threshold:** SPL-001 (50% majority) matches Phase 3 of the agent definition verbatim.
- **Priority ordering:** PMC-006 (Must-be > Performance > Attractive > Indifferent) is consistent with the Actionability criterion in the Quality Gate Integration table (line 248) and with Phase 4 of the agent definition.
- **Lifecycle migration:** The one-way migration assertion in LCY-004 is consistent with the Migration Trajectory diagram (line 145) and the lifecycle assessment in agent Phase 4.
- **Confidence classification:** CLS-002 (directional classifications MUST NOT be HIGH) is consistent with the agent Forbidden Actions (line 403 of agent: "NEVER present directional classifications (5-8 respondents) as statistically validated").
- **Quality Gate Integration mapping:** The S-014 dimension mappings in lines 243-249 are internally consistent with the rules defined in each section above them.

**Gaps:**

- QG-001 references ">= 0.92 (H-13, C2+)" as the baseline threshold but does not acknowledge that C4 deliverables carry a higher threshold (the artifact is scored at C4 which requires >= 0.95). This is not a contradiction but a mild incompleteness in the rule itself: it could cause a future scorer applying this rules file to under-enforce the quality gate for C4 analyses.

**Improvement Path:**
Update QG-001 to note: "For C4 deliverables (architecture/governance changes), the threshold is >= 0.95 per quality-enforcement.md criticality levels."

---

### Methodological Rigor (0.87/1.00)

**Evidence:**

Strong methodological structure:
- Rule sections map to the 5-phase agent workflow: EVT rules (Phase 3 table application), CSC rules (Phase 4 coefficients), SSC rules (Phase 3 confidence), SPL rules (Phase 3 split detection), LCY rules (Phase 4 lifecycle), PMC rules (Phase 4 priority matrix), CLS rules (Phase 5 synthesis), QG rules (quality gate integration).
- Every rule has a tier assignment (HARD/MEDIUM) with a consequence-of-violation column — consequences are specific and causally linked to the rule.
- Source citations appear at the section level before each rule table, attributing the foundational methodology correctly.
- The CS coefficient formulas match the Berger et al. (1993) standard. R/Q exclusion from the denominator is correctly enforced.
- The five-tier Confidence Classification (HIGH/MEDIUM/LOW) with specific criteria for each judgment type is methodologically sophisticated.
- The minimum-confidence rule (CLS-005) is particularly rigorous: it prevents confidence inflation when findings draw from multiple judgment types.
- The priority matrix axis definitions (PMC-001) correctly use |Worse| (absolute value) for the y-axis, reflecting the standard Matzler & Hinterhuber (1998) visualization.

**Gaps:**

1. **Survey question design methodology absent from rules.** The most fundamental instrument of the Kano methodology — the functional/dysfunctional question pair — has no rule section. Without rules governing question construction, the rules file cannot enforce methodological correctness at the instrument level.

2. **Partial-response handling not specified.** The methodology does not define what constitutes a valid response pair for 5x5 table application (both functional AND dysfunctional required), nor what to do when one answer is missing.

3. **Q > 10% threshold (SPL-005) has no methodological basis stated.** The rule mandates behavior on this threshold but provides no source citation. If this is a practitioner convention, it should be labeled as such (as the 5-8 respondent directional range is).

4. **R > 20% user-segment disagreement signal:** The agent definition (Phase 4, step 3) identifies "high R count (> 20% of responses) indicating user segment disagreement" as a priority conflict trigger, but this signal has no corresponding rule in the rules file.

**Improvement Path:**
(1) Add Survey Question Design Rules section. (2) Add a rule for partial-response handling. (3) Add practitioner-estimate label or citation to SPL-005 threshold. (4) Add a rule for the R > 20% segment disagreement detection signal.

---

### Evidence Quality (0.84/1.00)

**Evidence:**

Well-sourced sections:
- Three primary sources are consistently cited: Kano et al. (1984), Berger et al. (1993), and Matzler & Hinterhuber (1998). These are the canonical Kano methodology references.
- The 20-respondent threshold is explicitly attributed: "Statistically reliable (Berger et al., 1993)" (line 103).
- The 5-8 directional range is labeled as practitioner guidance with a transparency note: "The 5-8 respondent directional range is practitioner guidance consistent with Berger et al. discussion of small-sample analysis" (lines 93-94).
- The 50% split threshold is attributed: "conventional cutoff per Berger et al. (1993)" (SPL-001, line 128).
- The 50+ segment analysis minimum is labeled: "practitioner recommendation" (line 104 note in agent methodology).
- The lifecycle migration trajectory cites both Kano et al. (1984) and Matzler & Hinterhuber (1998).
- The Confidence Classification source correctly cites synthesis-validation.md Section "Confidence Classification."
- CSC-001 R/Q exclusion cites Berger et al. (1993).

**Gaps:**

1. **SPL-005 Q > 10% threshold: Zero evidence.** The rule "When Q (Questionable) responses exceed 10% for a feature, the feature MUST be flagged" (line 132) has no citation, no practitioner-estimate label, and no transparency note. Unlike the 5-8 respondent range (which is explicitly labeled as practitioner guidance) or the 50% split threshold (attributed to Berger et al.), the 10% Q threshold is stated as a HARD rule with no evidence basis. This is the most significant evidence gap in the file.

2. **LCY-004 one-way migration: Citation exists but no page-level evidence.** The claim that lifecycle migration is definitively one-way is attributed to the Kano model but without specifying what in Kano et al. (1984) or Matzler & Hinterhuber (1998) establishes this as a one-way constraint. The direction is well-established in the literature, but the confidence of the HARD tier here would benefit from more specific attribution.

3. **No volume/page citations.** All citations use author-year format only. For a C4 deliverable, adding page numbers or specific sections would strengthen evidence quality. This is a minor gap.

**Improvement Path:**
(1) Add a practitioner-estimate label to SPL-005 (e.g., "10% Q threshold is a practitioner convention; no published threshold exists in the primary literature. Teams may calibrate this based on survey instrument complexity") or provide a source citation. (2) For LCY-004, cite the specific discussion in Matzler & Hinterhuber (1998) regarding the unidirectional nature of feature migration.

---

### Actionability (0.88/1.00)

**Evidence:**

Highly actionable overall:
- Six named output markers are defined with specific triggering conditions: `[SPLIT CLASSIFICATION]`, `[DOMAIN EXPERT REQUIRED]`, `[QUESTION CLARITY ISSUE]`, `[BOUNDARY]`, `[CATEGORY-QUADRANT MISMATCH]`, `[ANECDOTAL -- NOT FOR DESIGN DECISIONS]`. Each is triggered by a specific measurable condition.
- SPL-003 provides a concrete example of what a domain expert resolution prompt should contain, including suggested criteria ("Is competitive pressure making this an expected feature?").
- CSC-004 provides a specific example of correct calculation notation: "Better = (3+5)/(3+5+4+2) = 0.57; R=1, Q=0 excluded."
- SSC-004 specifies two locations where the 20+ respondent recommendation must appear (Executive Summary AND Sample Size Disclosure section).
- PMC-006 includes tie-breaking rules within categories (|Worse| descending for Must-be/Performance; Better descending for Attractive).
- The Quality Gate Integration section translates abstract S-014 dimensions into Kano-specific evaluation criteria, making scoring directly actionable.
- The 14-item self-review checklist is checkable and each item traces to a specific rule ID.

**Gaps:**

1. **LCY-003 re-evaluation interval: Unspecified.** The rule states features approaching transition boundaries "SHOULD be flagged for re-evaluation with a recommended re-evaluation interval" but does not specify what interval to recommend (e.g., 6 months, 12 months, or "next competitive review cycle"). The agent is left to infer this, which varies execution.

2. **R > 20% segment disagreement action: Absent from rules.** The agent definition Phase 4 identifies high R count (> 20%) as a priority conflict signal and mandates `[DOMAIN EXPERT REQUIRED]` markers. This actionable trigger exists in the agent but not as an enforceable rule in the rules file.

3. **PMC-004 boundary case action: Underspecified.** PMC-004 mandates a `[BOUNDARY]` marker for features within 0.05 of the 0.5 threshold but does not specify what action follows beyond the marker (e.g., should the agent recommend collecting additional data, waiting for more responses, or proceeding with the current classification with a caveat?).

**Improvement Path:**
(1) Add a recommended re-evaluation interval to LCY-003 (e.g., "re-survey within 6-12 months or at next competitive review, whichever is sooner"). (2) Add an R > 20% rule to the Split Detection or Priority Matrix section. (3) Expand PMC-004 to specify what action follows the `[BOUNDARY]` marker.

---

### Traceability (0.87/1.00)

**Evidence:**

Good traceability infrastructure:
- VERSION header (line 1) cites date, source files (SKILL.md v1.2.0, agent definition), parent, and revision note.
- Navigation table (lines 9-20) with correct anchor links satisfies H-23.
- Rule IDs are systematic, unique, and follow section-prefixed numbering: EVT-001 through EVT-005, CSC-001 through CSC-005, SSC-001 through SSC-005, SPL-001 through SPL-005, LCY-001 through LCY-005, PMC-001 through PMC-007, CLS-001 through CLS-005, QG-001 through QG-004.
- Self-review checklist items (lines 283-298) trace back to specific rule IDs (e.g., "CSC-001", "EVT-001, EVT-002", "SPL-001, SPL-003").
- Related Files section (lines 266-274) provides bidirectional dependency mapping with relationship type, version, and purpose.
- Footer traceability comment (line 309) cites project, phase, wave, applicable standards (H-23, H-34, SR-002, SR-003), and all three methodology sources.
- Quality Gate Integration section (lines 238-258) traces S-014 dimensions back to quality-enforcement.md.
- Confidence Classification traces to synthesis-validation.md with specific section names.

**Gaps:**

1. **Rule-to-requirement chain: Absent.** The rules file does not trace individual rules back to specific requirements in parent SKILL.md, the project's orchestration plan, or any formal requirements document. It is not possible to determine from this file alone which SKILL.md sections motivated which rules. For a C4 deliverable, requirement traceability (from rule to requirement) is expected.

2. **SPL-005 Q > 10% threshold: No traceability.** The 10% threshold appears as a rule with no source, no practitioner label, and no traceability path. It cannot be verified against any reference.

3. **LCY-002 MEDIUM confidence mandate: No source trace.** The rule "Lifecycle predictions MUST be classified as MEDIUM confidence" (LCY-002) has no citation establishing why MEDIUM (rather than LOW or HIGH) is the appropriate floor. This appears to be a design decision that should trace to synthesis-validation.md confidence taxonomy or a stated rationale.

**Improvement Path:**
(1) Add a "Requirements Traceability" row or column to the Related Files section mapping key rule groups to the SKILL.md sections or project requirements that motivated them. (2) Add a source or practitioner-estimate label to SPL-005. (3) Add a rationale note to LCY-002 citing why MEDIUM is the appropriate confidence floor for lifecycle predictions (pattern documented but timing domain-dependent).

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.82 | 0.92+ | Add "Survey Question Design Rules" section with HARD rules for: functional question format ("How would you feel if this product had [X]?"), dysfunctional question format ("How would you feel if this product did NOT have [X]?"), language requirements (concrete, non-jargon, balanced tone), completeness (both questions required per feature). Add rule for partial-response handling (respondent answered functional but not dysfunctional, or vice versa). |
| 2 | Evidence Quality | 0.84 | 0.92+ | Add practitioner-estimate label to SPL-005 Q > 10% threshold, or provide a citation. The current HARD rule has zero evidence basis — it is the most significant evidence gap in the file. Pattern: label as "practitioner convention; no published threshold in primary literature; teams may calibrate based on survey instrument complexity." |
| 3 | Methodological Rigor | 0.87 | 0.93+ | (a) Add R > 20% user-segment disagreement signal as a formal rule in Split Detection Rules or Priority Matrix Construction Rules, mirroring the agent Phase 4 step 3 behavior. (b) Add partial-response handling rule. (c) Add practitioner-estimate label to SPL-005. |
| 4 | Actionability | 0.88 | 0.93+ | (a) Specify a recommended re-evaluation interval in LCY-003 (e.g., "6-12 months or at next competitive review, whichever is sooner"). (b) Add R > 20% rule with `[DOMAIN EXPERT REQUIRED]` marker. (c) Expand PMC-004 to specify what action follows a `[BOUNDARY]` marker beyond the flag itself. |
| 5 | Traceability | 0.87 | 0.93+ | (a) Add rationale note to LCY-002 for MEDIUM confidence floor. (b) Add source trace to SPL-005. (c) Add rule-to-SKILL.md requirement mapping — even a simple column in Related Files showing "rules governing Phase X → SKILL.md Section Y" would satisfy this for a rules file. |
| 6 | Internal Consistency | 0.93 | 0.96+ | Update QG-001 to acknowledge C4 threshold (>= 0.95) in addition to the H-13 floor (>= 0.92), preventing future scorers from applying the wrong threshold to C4-level Kano analyses. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score with specific line references and section names
- [x] Uncertain scores resolved downward (Completeness: gap is real, not minor; 0.82 not 0.85)
- [x] First-draft calibration considered (this is iteration 1; 0.869 is within expected first-draft range 0.65-0.80, above it slightly due to the document's structural maturity)
- [x] No dimension scored above 0.95 without exceptional evidence (highest is Internal Consistency at 0.93, which is warranted by the complete absence of contradictions)
- [x] C4 threshold (0.95) applied as the standard; the composite of 0.869 is well below both 0.95 and 0.92

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.869
threshold: 0.95
weakest_dimension: completeness
weakest_score: 0.82
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add Survey Question Design Rules section with HARD rules for question format, language requirements, completeness, and partial-response handling"
  - "Add source citation or practitioner-estimate label to SPL-005 Q > 10% threshold (currently an unsourced HARD rule)"
  - "Add R > 20% user-segment disagreement as a formal rule in Split Detection or Priority Matrix section"
  - "Specify recommended re-evaluation interval in LCY-003 (currently unspecified)"
  - "Add rule-to-requirement traceability mapping connecting rule groups to parent SKILL.md sections"
  - "Update QG-001 to acknowledge C4 threshold (>= 0.95) in addition to H-13 floor (>= 0.92)"
```

---

*Score Report Version: 1.0.0*
*Scored by: adv-scorer (S-014 LLM-as-Judge)*
*Artifact: `skills/ux-kano-model/rules/kano-methodology-rules.md` v1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Iteration: 1 of N*
*Created: 2026-03-04*
