# Quality Score Report: HEART Methodology Rules

## L0 Executive Summary

**Score:** 0.900/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Methodological Rigor (0.88)
**One-line assessment:** Solid, well-evidenced rules file covering all 5 HEART dimensions with complete templates and worked examples, but falls short of the 0.95 C4 threshold primarily due to the absence of an explicit cross-phase sequencing rule in the SSOT itself, minor inline attribution gaps for Bain & Company NPS benchmarks, and the Measurement Plan mode content living only in the agent definition rather than the rules file.

---

## Scoring Context

- **Deliverable:** `skills/ux-heart-metrics/rules/heart-methodology-rules.md`
- **Deliverable Type:** Research (Methodology Rules)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Threshold Override:** 0.95 (user-specified; standard H-13 is 0.92)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1 (first score)

### Cross-References Verified

| File | Verified |
|------|---------|
| `skills/ux-heart-metrics/SKILL.md` | Yes |
| `skills/ux-heart-metrics/agents/ux-heart-analyst.md` | Yes |
| `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md` | Yes |
| `skills/user-experience/rules/synthesis-validation.md` | Yes |

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.900 |
| **Threshold** | 0.95 (C4 user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.89 | 0.178 | All 5 HEART dimensions + all GSM steps + 5 worked examples; Measurement Plan mode rule content absent from rules SSOT |
| Internal Consistency | 0.20 | 0.92 | 0.184 | No contradictions found; rules self-consistent across GD/SI/MS/CR/SE/DF/DL rule sets |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | GSM sequential rules present with violation consequences; no explicit cross-phase sequencing section in rules SSOT |
| Evidence Quality | 0.15 | 0.88 | 0.132 | All 4 required citations present with full bibliographic entries; inline "Bain & Company" NPS benchmark lacks Reichheld (2003) anchor |
| Actionability | 0.15 | 0.93 | 0.1395 | 5 worked examples, copy-paste templates, 13-item self-review checklist, specific numeric constraints |
| Traceability | 0.10 | 0.91 | 0.091 | Systematic rule IDs (DS/GD/SI/MS/CR/SE/DF/DL), PROJ-022 footer comment, S-014 mapping table |
| **TOTAL** | **1.00** | | **0.900** | |

---

## Detailed Dimension Analysis

### Completeness (0.89/1.00)

**Evidence:**

All 5 HEART dimensions are explicitly defined with definitions, example signals, and a lifecycle stage alignment table (lines 33-50). The document covers all 3 GSM steps (GD-001 through GD-006 goal rules, SI-001 through SI-006 signal rules, MS-001 through MS-008 metric rules). The 4-step threshold fallback methodology is complete with worked examples and explicit constraints. Confidence classification covers all 7 output types per the synthesis-validation.md SSOT. Goal adjudication protocol provides a 4-step tie-breaking process. Signal-to-metric edge cases cover 3 patterns (single signal/multiple metrics, no signal available, multiple signals/one metric). Dashboard specification covers metric card format (8 fields), visualization type selection table, refresh frequency rules (DF-001 to DF-004), and layout rules (DL-001 to DL-004). The Quality Gate Integration section maps all 6 S-014 dimensions to HEART-specific criteria. The GSM Worksheet Template section provides a blank template, metric card template, AND worked examples for all 5 HEART dimensions. Self-Review Checklist has 13 items with rejection criteria.

**Gaps:**

1. **Measurement Plan mode disclosure rules are absent from this rules file.** The `<input>` section of `ux-heart-analyst.md` defines the Measurement Plan mode behavior and the required disclosure header. However, the rules file — which is the stated SSOT for agent methodology — does not contain a Measurement Plan mode section or rules governing when and how the disclosure must appear. The Self-Review Checklist item 8 says "Measurement Plan mode disclosure present if analytics infrastructure is unavailable" but never defines what that disclosure must contain or what triggers it. This is a completeness gap: the rules SSOT is incomplete for this mode.

2. **No explicit workflow sequencing section.** The 5-phase workflow (Context Gathering through Dashboard Specification) is defined in the agent definition's `<methodology>` section and referenced in the agent's output specification. The rules file covers content for phases 2-5 but lacks an explicit workflow sequencing rule or phase-order constraint. A separate agent reading only this rules file would not know the prescribed execution order.

**Improvement Path:**

Add a "Measurement Plan Mode Rules" section (between Threshold Fallback and Confidence Classification) defining: the trigger condition (analytics infrastructure = none or absent), the required disclosure header text, and mode-specific output modifications. Add a "Workflow Execution Sequence" section with explicit phase-order rules (analogous to the GSM sequential constraint in line 83: "The three steps...MUST execute in order").

---

### Internal Consistency (0.92/1.00)

**Evidence:**

- **GD-001 and Goal Adjudication alignment:** GD-001 says "exactly one goal statement" and the Goal Adjudication section operationalizes this constraint with a 4-step tie-breaking protocol. No contradiction.
- **SI-001 (2-4 signals) and SE-001 (single signal, multiple metrics):** SI-001 sets 2-4 signals per dimension; SE-001 addresses when a single signal maps to multiple metrics. These are complementary and not contradictory — SI-001 governs the Goal-to-Signal step, SE-001 governs the Signal-to-Metric step.
- **MS-006 (threshold source documentation) and Threshold Fallback Methodology:** MS-006 requires citing the fallback step number; the threshold documentation format table (lines 163-169) demonstrates this with "Fallback Step" as a required column. Consistent.
- **CR-001 and CR-003:** CR-001 requires [REFERENCE-ONLY] on all threshold values; CR-003 explicitly states it MUST NOT be applied to MEDIUM-confidence outputs. These are complementary and self-consistent.
- **DS-006 and "All-Five Override" section:** DS-006 limits tiny teams to 2-3 dimensions; the All-Five Override section explicitly notes P-020 user authority can override this but SHOULD include the capacity implication note. No contradiction — user authority (P-020) appropriately takes precedence.
- **Quality Gate Integration table Completeness criterion:** States "Dimension selection covers all 5 dimensions (included and excluded with rationale)" — consistent with DS-004/DS-005 exclusion documentation requirements.
- **Worked examples confidence levels:** All 5 worked examples consistently assign LOW confidence to threshold values and all signal/metric rows — consistent with CR-001 and the confidence classification table.

**Gaps:**

No contradictions found. The one-level-below-MEDIUM inconsistency is: the Engagement worked example uses "Fallback Step 3 (baseline + 15% improvement)" in a note (line 431) and "Fallback Step 2" in a separate note (line 432), both within the same dimension. This is not an inconsistency — two different signals have two different fallback derivations, which is correct.

**Improvement Path:**

Internal consistency is a strength of this document. No material improvement needed on this dimension.

---

### Methodological Rigor (0.88/1.00)

**Evidence:**

The GSM process is specified with explicit sequential ordering ("MUST execute in order -- no step may be skipped or reordered," line 83). Six goal rules, six signal rules, and eight metric rules are each stated with consequences of violation. The lifecycle stage alignment table provides a systematic heuristic for dimension selection. The 4-step threshold fallback is graduated with explicit constraints: Step 2 minimum 14 days, Step 3 10-15% range, Step 4 minimum 4 weeks. Goal adjudication protocol applies a 4-step decision protocol with lifecycle alignment as primary criterion. Dashboard visualization type selection includes rationale for each recommendation. Edge case handling covers three distinct patterns with explicit rule IDs.

The reference to Rodden et al. (2010) as the source authority for the GSM sequential constraint (line 85) grounds the methodology in established academic literature.

**Gaps:**

1. **No explicit cross-phase sequencing rule in this rules file.** The GSM Process Rules section governs the Goal→Signal→Metric sequence within Phase 3, but there is no analogous rule governing Phase 1 (Context Gathering) → Phase 2 (Dimension Selection) → Phase 3 (GSM Execution) → Phase 4 (Threshold Setting) → Phase 5 (Dashboard Specification) ordering. An agent reading only this rules file has explicit ordering only for the GSM micro-steps, not for the macro-phase sequence. The macro-phase workflow is defined in the agent definition (`<methodology>` section) but not in the rules SSOT.

2. **Dimension selection criteria are guidelines, not rules with explicit violations.** The "Dimension Inclusion Rules" table (DS-001 through DS-006) correctly uses MUST/SHOULD language, but DS-001 says to include when it "meets one or more criteria and excluded only with documented justification" — this conflates the inclusion and exclusion criteria into a single ambiguous statement. The exclusion criteria (DS-004, DS-005) are stated separately, but the general inclusion framing is weaker than the precise exclusion rules.

**Improvement Path:**

Add a "Workflow Phase Sequencing Rules" section with explicit phase-order constraints analogous to the GSM sequential rule (lines 83-84). Tighten DS-001's framing to explicitly separate inclusion criteria from exclusion criteria to reduce ambiguity.

---

### Evidence Quality (0.88/1.00)

**Evidence:**

All four required citations are present and verified:

1. **Rodden, Hutchinson & Fu (2010):** Full bibliographic entry in References table (lines 484-485). Cited inline at HEART Dimension Selection source note (line 29), GSM Process Rules source note (line 85), Threshold Fallback source note (line 150), and Dashboard Specification source note (line 308). Four citation placements — strongest evidence quality.

2. **Reichheld (2003):** Full bibliographic entry in References table (lines 485-486) with HBR citation including volume and issue numbers (81(12), 46-54). Cited inline in the Measurement Gap worked example (line 287: "Reichheld, 2003"). Two citation placements.

3. **Few (2006):** Full bibliographic entry in References table (lines 487). Cited inline in Dashboard Specification section source attribution (line 308). Two placements including publisher (Analytics Press).

4. **Baymard Institute:** Present in References table (lines 487-488) with URL, date range (2020-2024), and a practitioner note to verify current values. Cited inline in the threshold documentation worked example (line 166: "Baymard Institute e-commerce benchmark") and Task Success worked example (line 451: "Baymard Institute, 2024"). Three citation placements.

All threshold sources are documented per MS-006. Worked examples correctly attribute derivation sources.

**Gaps:**

1. **Inline Bain & Company NPS attribution is disconnected from bibliographic anchor.** The Happiness worked example (line 423) notes "Threshold based on Bain & Company e-commerce NPS benchmark" but this inline citation does not reference "Reichheld (2003)" which is the bibliographic entry that contains the Bain & Company NPS attribution. A reader following the evidence chain would need to infer the connection between "Bain & Company" and the Reichheld (2003) citation. The Threshold Fallback source note (line 150) does link "Reichheld (2003) / Bain & Company (NPS)" but the worked example itself lacks this connection.

2. **Engagement worked example thresholds cite only fallback step numbers** (lines 430-432) without benchmark publications. This is correct per the rules (Fallback Step 3 means no benchmark was available), but the evidence chain is thinner for Engagement than for Task Success or Happiness.

**Improvement Path:**

Change the Happiness worked example (line 423) threshold citation from "Bain & Company e-commerce NPS benchmark" to "Bain & Company / Reichheld (2003) e-commerce NPS benchmark" to close the bibliographic chain. This is a one-line edit.

---

### Actionability (0.93/1.00)

**Evidence:**

This is the strongest dimension. Actionability evidence:

- **Worked examples cover all 5 HEART dimensions** (lines 419-453): Happiness (e-commerce NPS), Engagement (SaaS feature depth), Adoption (mobile onboarding), Retention (subscription product), Task Success (checkout flow). Each provides a populated GSM table row with all 8 metric specification fields.
- **Explicit templates:** GSM worksheet template (lines 386-393) and metric card template (lines 396-413) are copy-paste ready with placeholder syntax `{placeholder}`.
- **Numeric constraints throughout:** Step 2 minimum 14 days, Step 3 improvement range 10-15%, Step 4 minimum 4 weeks (lines 176-179). SI-001 specifies 2-4 signals per goal. DS-006 specifies 2-3 dimensions for tiny teams.
- **Rule IDs on every rule:** All 45+ rules have systematic IDs (DS/GD/SI/MS/CR/SE/DF/DL prefix), enabling precise cross-reference.
- **Self-Review Checklist has rejection criteria** (not just "check this"): each item states what constitutes a rejection condition (lines 460-474).
- **Exclusion documentation format** provides a copy-paste markdown table template (lines 69-73).
- **Threshold fallback documentation format** provides a copy-paste table (lines 162-169).
- **Alert condition specifications are precise:** "< 75% for 3 consecutive days" pattern demonstrated in MS-007 (not just "below target").

**Gaps:**

1. The "Measurement Gap" example (lines 282-288) demonstrates the SE-004/SE-005/SE-006 rules effectively, but the recommended instrumentation note ("Estimated implementation: 2-3 days with survey tool integration (e.g., Hotjar, Qualtrics)") references Hotjar/Qualtrics without citation. This is a minor actionability gap — the tool recommendations are helpful but presented without evidence basis.

**Improvement Path:**

Actionability is the strongest dimension. The minor tool-name references without citation are acceptable in a worked example context and do not materially reduce actionability. Consider adding "(examples: Hotjar, Qualtrics, SurveyMonkey; not exhaustive)" to make the tool suggestions explicitly non-prescriptive.

---

### Traceability (0.91/1.00)

**Evidence:**

- **Systematic rule IDs:** 45+ rules with prefix-based namespacing: DS (dimension selection, 6 rules), GD (goal definition, 6 rules), SI (signal identification, 6 rules), MS (metric specification, 8 rules), CR (confidence/REFERENCE-ONLY, 4 rules), SE (signal-to-metric edge cases, 10 rules), DF (dashboard frequency, 4 rules), DL (dashboard layout, 4 rules).
- **Footer traceability comment** (lines 511-512) includes: PROJ-022, EPIC-003, Wave 2, standards H-23/H-34/SR-002/SR-003/H-13/H-15, methodology citations, and ORCHESTRATION.yaml path.
- **References section** (lines 479-499): 4 primary methodology citations with full bibliographic entries + 7 framework standards citations with repo-relative paths.
- **Quality Gate Integration section** explicitly maps the 6 S-014 dimensions to HEART-specific scoring criteria, enabling scorers to trace how HEART outputs connect to the quality rubric.
- **Confidence Classification section** cites synthesis-validation.md as the source for confidence assignments.
- **Self-Review Checklist item 7** traces to H-23 (navigation). Item 1 traces to the Dimension Selection section.
- **Source/SSOT VERSION block** (line 1) traces to SKILL.md and agent definition.

**Gaps:**

1. The Self-Review Checklist items reference H-23 and "S-010, H-15" in the header but the individual checklist items do not include rule ID cross-references. For example, item 3 ("Every metric has all 8 specification fields populated") should reference MS-002 explicitly.
2. The "All-Five Override" section (lines 75-78) references P-020 but does not include a traceability footnote to the constitution or quality-enforcement.md.

**Improvement Path:**

Add rule ID cross-references to Self-Review Checklist items (e.g., "item 3 (MS-002)" and "item 4 (CR-001)") and a "(P-020: `docs/governance/JERRY_CONSTITUTION.md`)" citation in the All-Five Override section.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.89 | 0.93+ | Add a "Measurement Plan Mode Rules" section (after Threshold Fallback) with: (a) trigger condition definition, (b) required disclosure header text verbatim, (c) mode-specific output modifications (instrumentation-first output, no current-state values). This moves the mode rules from the agent definition into the rules SSOT. |
| 2 | Methodological Rigor | 0.88 | 0.92+ | Add a "Workflow Phase Sequencing Rules" section with explicit phase-order constraints: "Phases MUST execute in the order Phase 1 (Context Gathering) → Phase 2 (Dimension Selection) → Phase 3 (GSM Execution) → Phase 4 (Threshold Setting) → Phase 5 (Dashboard Specification). Each phase MUST complete before the next phase begins." |
| 3 | Evidence Quality | 0.88 | 0.92+ | In the Happiness worked example (line 423), change threshold citation from "Bain & Company e-commerce NPS benchmark" to "Bain & Company / Reichheld (2003) e-commerce NPS benchmark" to close the bibliographic chain from inline citation to References entry. One-line edit. |
| 4 | Traceability | 0.91 | 0.94+ | Add rule ID cross-references to Self-Review Checklist items: item 2 → "(GD-001, SI-001, MS-002)", item 3 → "(MS-002)", item 4 → "(CR-001)", item 5 → "(MS-006)", item 6 → "(Confidence Classification section)". |
| 5 | Methodological Rigor | 0.88 | 0.92+ | Tighten DS-001 framing: split "A dimension is included when it meets one or more criteria and excluded only with documented justification" into two separate sub-rules — one for inclusion criteria (DS-001a: include when meets ANY criterion) and one for the exclusion requirement (DS-001b: exclusion REQUIRES documentation per DS-004/DS-005). |
| 6 | Internal Consistency | 0.92 | 0.94+ | Verify the Engagement worked example threshold notes ("Fallback Step 3" and "Fallback Step 2") are in the correct order — Step 2 (baseline measurement) should logically precede Step 3 (baseline + improvement target). If Step 3 is used for Signal 1 and Step 2 for Signal 2, add a note explaining that different signals may apply different fallback steps. |

---

## Score Computation Verification

| Dimension | Score | Weight | Product |
|-----------|-------|--------|---------|
| Completeness | 0.89 | 0.20 | 0.1780 |
| Internal Consistency | 0.92 | 0.20 | 0.1840 |
| Methodological Rigor | 0.88 | 0.20 | 0.1760 |
| Evidence Quality | 0.88 | 0.15 | 0.1320 |
| Actionability | 0.93 | 0.15 | 0.1395 |
| Traceability | 0.91 | 0.10 | 0.0910 |
| **Sum** | | **1.00** | **0.9005** |

Rounded to 3 decimal places: **0.900**

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Completeness: uncertain between 0.89-0.91; chose 0.89. Rigor: uncertain between 0.88-0.90; chose 0.88)
- [x] C4 first-draft calibration considered: first-pass rules file should score 0.85-0.90 per calibration anchors; 0.900 is at the upper end of this range, which is appropriate given the document's completeness and template coverage
- [x] No dimension scored above 0.95 (highest is Actionability at 0.93, which has clear justification: 5 worked examples + 2 copy-paste templates + 13-item checklist with rejection criteria)
- [x] Anti-leniency verification against specific criteria: Rodden 2010 citation (PASS 4 locations), Reichheld 2003 (PASS), Few 2006 (PASS), Baymard (PASS); all 5 HEART dimensions covered (PASS); GSM process complete (PASS); threshold fallback matches SKILL.md (PASS); worked examples per dimension (PASS 5/5)

**Leniency bias assessment:** No significant leniency inflation detected. The composite 0.900 reflects a strong but not excellent deliverable. The gaps identified (Measurement Plan mode, cross-phase sequencing, Bain/Reichheld attribution, self-review checklist traceability) are real and specific, not manufactured to justify a lower score.

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.900
threshold: 0.95
weakest_dimension: Methodological Rigor
weakest_score: 0.88
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add Measurement Plan Mode Rules section (trigger, disclosure text, mode behavior)"
  - "Add Workflow Phase Sequencing Rules section with explicit phase-order constraints"
  - "Fix Bain & Company NPS citation to reference Reichheld (2003) in Happiness worked example"
  - "Add rule ID cross-references to Self-Review Checklist items 2-6"
  - "Split DS-001 into DS-001a (inclusion) and DS-001b (exclusion documentation required)"
  - "Clarify Engagement worked example fallback step ordering (Step 2 vs Step 3 per signal)"
```

---

*Score Report: rules-iter1-score.md*
*Deliverable: skills/ux-heart-metrics/rules/heart-methodology-rules.md*
*Scorer: adv-scorer (S-014 LLM-as-Judge)*
*SSOT: .context/rules/quality-enforcement.md*
*Created: 2026-03-04*
