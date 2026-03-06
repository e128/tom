# Quality Score Report: UX Framework Selection -- Weighted Multi-Criteria Analysis

## L0 Executive Summary

**Score:** 0.900/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Methodological Rigor (0.83)
**One-line assessment:** Revision 4 is a substantially polished deliverable that genuinely resolves the Critical and Major findings from all 9 prior strategies; it does not yet reach the 0.95 C4 threshold primarily because one methodological tension (the "necessary conditions vs. weighted average" contradiction) was acknowledged but not fully resolved, and a cluster of minor residual internal consistency items and a structural claim-without-hard-evidence gap remain.

---

## Scoring Context

- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
- **Deliverable Type:** Analysis (Weighted Multi-Criteria Decision Matrix)
- **Criticality Level:** C4
- **Quality Threshold:** 0.95 (C4 tournament)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Prior Score (Baseline):** 0.838 (Revision 2, pre-DA/PM/S-010/S-007/S-011/S-012/S-013)
- **Current Revision:** Revision 4
- **Strategies Incorporated:** S-001, S-003, S-002, S-004, S-010, S-007, S-011, S-012, S-013
- **Scored:** 2026-03-03T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.900 |
| **Threshold** | 0.95 (H-13, C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | Yes -- 9 strategy reports reviewed |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 7 failure modes covered; triage lifecycle added; gaps documented with V2 paths; parent skill routing in Section 7; minor gap: AI sub-skill limits documented for only 2/10 frameworks |
| Internal Consistency | 0.20 | 0.87 | 0.174 | SR-001/SR-002/CV-012 rank collisions resolved; sensitivity arithmetic corrected; Hotjar label inconsistency fixed; residual: "necessary conditions vs. weighted average" tension remains unresolved in Section 1 |
| Methodological Rigor | 0.20 | 0.83 | 0.166 | Two sensitivity perturbations added; complementarity two-pass documented; single-rater bias disclosed; DA-001 acknowledged but not resolved at the method level; no inter-rater verification for 30 non-top-10 frameworks |
| Evidence Quality | 0.15 | 0.93 | 0.140 | 23 evidence entries; score verification table; AI-First Design synthesis sources enumerated; forward-looking framing added to Section 3; AI personas claim now cited; minor: absolute source paths not provided |
| Actionability | 0.15 | 0.95 | 0.143 | All 10 sub-skills named; routing decision guide and parent skill in Section 7; MCP maintenance contract; three-tier Kano modes; JTBD data sufficiency gate; fallback behaviors explicit |
| Traceability | 0.10 | 0.93 | 0.093 | Evidence IDs E-001 to E-023 with section linkages; 4-revision change log with finding-to-change mapping; RT/SM/DA/PM/SR/CV/CC/FM/IN cross-references inline; minor: relative source paths could be absolute |
| **TOTAL** | **1.00** | | **0.900** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**

The deliverable covers all required analytical components at a depth appropriate for a C4 decision. Section 1 contains the UX failure mode coverage validation (7 failure modes, all mapped). Section 4's complementarity matrix now includes a "Triage Existing Product" lifecycle row (RT-007). The gap analysis enumerates excluded domains with V2 candidates. Section 7 adds the parent skill triage mechanism and MCP maintenance contract. All 10 sub-skills have "When to use this vs. other sub-skills" disambiguation tables. The HIGH RISK user research gap is labeled with appropriate severity and a V2 recommendation. Section 3 includes the AI Execution Mode Taxonomy distinguishing deterministic execution from synthesis hypothesis outputs (IN-003).

**Gaps:**

- Eight of the 10 selected frameworks lack documented AI substitution limits at the step level (AG-5 from S-013 inversion). Only Design Sprint and JTBD have explicit "AI augmentation prerequisites" blocks. The other 8 frameworks have their AI automation claims in the Tiny Teams enablement patterns but without documented fallbacks for AI execution failures at specific steps. This represents a completeness gap for a C4 deliverable that will govern skill implementation.
- The ethics sub-domain coverage in Section 4 identifies four uncovered ethics domains (algorithmic bias, data privacy, dark patterns, AI transparency) but does not propose V2 paths for any of them except a vague mention of REFLECT Framework. At C4, four uncovered ethics domains deserve V2 candidate specificity.

**Improvement Path:**

Add "AI execution limits" subsections to the 8 frameworks lacking them, or add a single Section 3 introduction note documenting that the AI augmentation limits described for Design Sprint (PM-005) and JTBD (PM-007) represent the pattern all frameworks should follow when implementing. Add V2 candidate specificity for the ethics sub-domain gaps.

---

### Internal Consistency (0.87/1.00)

**Evidence:**

The Critical rank collision findings (SR-001, CV-012) are verified resolved in the Revision 4 change log: Section 3.7 is now Microsoft Inclusive Design (Rank #7) and Section 3.8 is AI-First Design (Rank #8). The non-selected matrix sort order is corrected and verified (SR-002). All sensitivity analysis arithmetic corrections are applied (CV-009 through CV-011). The Hotjar Bridge MCP label inconsistency in Lean UX is resolved (SR-003, CV-013). Kano/Fogg rank cross-references in Sections 4 and 6 are noted as verified (SR-005).

**Gaps:**

The most significant residual internal consistency issue is the tension introduced by DA-001 (devil's advocate): the weighting rationale states that C1 and C2 function as "highest-weight priority criteria" (revised from the prior "necessary conditions/gatekeepers" framing), but the Section 1 text still contains language that creates a logical tension. Specifically, the dependency-chain framing in the weighting rationale explains the criteria as though they operate as gatekeepers, while the Revision 3 fix (DA-001) added a clarification that the math works as a weighted average. These two framings coexist in Section 1 -- the dependency-chain language is strong and persuasive but imprecisely describes how the scoring math actually works. A reader who follows the dependency-chain logic to its conclusion will expect a hard gate; the math produces a weighted contribution. This is not a fatal inconsistency, but it is a structural tension that leaves an internal contradiction visible to careful readers.

Additionally, the Revision 4 change log (at document end) notes SR-005 as "Verified Kano #9 / Fogg #10 rank labels consistent throughout Sections 4-6; already correct as-is post-SR-001 fixes" -- but the scoring report from S-010 identified explicit evidence that Fogg was labeled #9 and Kano #10 in multiple locations. If this was pre-existing correct labeling, the verification claim is accurate; if it was corrected, the change log entry undersells the fix. This ambiguity creates a minor traceability gap.

**Improvement Path:**

Revise the weighting rationale to eliminate the dependency-chain/gatekeeper language and replace it with a clean "graduated priority ordering" framing that accurately describes how the weighted average works, while still communicating the primacy of C1 and C2. The current framing is the strongest residual internal consistency vulnerability.

---

### Methodological Rigor (0.83/1.00)

**Evidence:**

The core MCDM methodology (Kepner-Tregoe weighted criteria) is correctly applied. The two-pass complementarity methodology is documented and its circularity explicitly acknowledged (FM-003, DA-002). Single-rater bias is disclosed with ±0.25 uncertainty for non-top-10 scores (FM-001). Two weight perturbations are tested (C1 and C2, SR-004), confirming stability across both. The AI Execution Mode Taxonomy (IN-003) distinguishes deterministic from synthesis outputs methodologically. The score compression zone at ranks 7-11 is explicitly acknowledged as judgment rather than algorithmic determination (DA-005). The revision history documents all significant corrections with specific evidence.

**Gaps:**

The methodological rigor score is held at 0.83 by two remaining weaknesses:

1. **DA-001 resolution quality.** The Revision 3 fix added a clarification paragraph but left the dependency-chain language intact. The result is a section that simultaneously argues (a) C1/C2 are the highest-weight priorities because they are "necessary conditions for the target context" and (b) the math works as a weighted average, not a hard gate. This is intellectually honest but methodologically imprecise -- it describes the intent of the weighting while conceding its implementation differs from that intent. At C4 criticality, where the deliverable's methodology will be treated as a reference for future similar analyses, this imprecision is a genuine rigor gap.

2. **No inter-rater verification for the selection boundary.** FM-001 identified that single-rater scoring of 40 frameworks creates material risk at the boundary. The corrective action was a disclosure note (FM-001 in the Revision 4 log: "acknowledged limitation in FM-001 disclosure block"). The recommended mitigation was a partial inter-rater check for the 5 most decision-relevant frameworks (Design Sprint #1, AI-First Design #8, Service Blueprinting #11, Double Diamond #11, Cognitive Walkthrough #16). This check was not performed -- only acknowledged as a limitation. At C4 criticality, acknowledging a methodology limitation without implementing the recommended mitigation leaves a material rigor gap. The non-selected framework scores have documented ±0.25 uncertainty but no verification that this uncertainty does not place any excluded framework within the selection threshold.

3. **AI-First Design maturity vs. selection validity.** The deliverable's handling of AI-First Design is methodologically coherent (cost-comparison framing, prerequisite blocking dependency, maturity score corrected to 2/10), but the fundamental methodological concern -- that all AI-First Design scores are projected predictions about a framework that does not exist -- remains. The DA-003 category notice correctly labels all scores as (P), but the methodology still proceeds to compare a projected score against measured scores for the other 9 frameworks. This is acknowledged as a limitation but the methodological asymmetry is not resolved.

**Improvement Path:**

(1) Replace the dependency-chain/gatekeeper framing with clean graduated-priority language that accurately represents how the weighted average actually discriminates. (2) Document a statement of bounded uncertainty for the selection boundary: explicitly calculate which excluded frameworks would enter the top 10 if their scores contained the ±0.25 uncertainty in either direction, and confirm that no excluded framework enters the top 10 within that uncertainty band. This converts a "we acknowledge uncertainty" disclosure into a "we verified the uncertainty does not invalidate the selection" argument -- a meaningful rigor upgrade.

---

### Evidence Quality (0.93/1.00)

**Evidence:**

The evidence base for Revision 4 is genuinely strong. Twenty-three evidence entries (E-001 through E-023) are fully present in the Evidence Summary with source artifact, type, and section usage. The score calculation verification table covers all 10 selected frameworks with explicit arithmetic. AI-First Design synthesis sources are enumerated in CC-003 (NN Group, Nudelman, Adam Fard, Microsoft Responsible AI, Google PAIR). Forward-looking capability claims are framed with the CC-004 notice at the top of Section 3. The AI personas limitation claim in the HIGH RISK gap is now cited (NN Group, Baymard Institute, JTBD practitioners). Bridge MCP warnings are consistently applied across all three Hotjar-dependent frameworks (HEART, Lean UX, Fogg). Community MCP production readiness caveats are added for Whimsical, LottieFiles, and Sketch (FM-002).

**Gaps:**

- Evidence paths remain relative (e.g., "ux-frameworks-survey.md") rather than absolute project-relative paths (e.g., `projects/PROJ-020-feature-enhancements/work/research/ux-frameworks-survey.md`). FM-018 identified this as a traceability risk; the Revision 4 log notes FM-009 through FM-023 were "acknowledged in methodology limitations disclosure" but FM-018 is not individually addressed.
- The AI-First Design framework synthesis sources are enumerated as "planned synthesis inputs" -- meaning they document what will be used, not what was verified. This is the correct disclosure given the framework does not yet exist, but the evidence quality for this framework remains inherently bounded.
- The MCDA methodology citations (Keeney & Raiffa 1976; Belton & Stewart 2002) are used to ground the complementarity scoring methodology. These citations are legitimate academic references but the specific application (portfolio-conditional complementarity in framework selection for AI skill portfolios) is novel to this context -- citing general MCDA theory as evidence for a specific application is a minor evidence quality gap.

**Improvement Path:**

Update evidence paths to full project-relative paths. This is a minor but completable improvement that eliminates the FM-018 open finding.

---

### Actionability (0.95/1.00)

**Evidence:**

This is the strongest dimension in the deliverable. Every selected framework has: (1) a proposed Jerry sub-skill name, (2) required MCP integrations with explicit classification (Native/Community/Bridge), (3) a Tiny Teams enablement pattern, (4) a "When to use this vs. other sub-skills" disambiguation table, (5) a complementarity note. Section 7 provides a parent skill triage mechanism, sub-skill routing decision guide, and MCP maintenance contract. The Kano Model has a three-tier implementation guide (pre-launch JTBD substitution, qualitative approximation, full quantitative). JTBD has a data sufficiency gate with confidence labeling. HEART has explicit degraded-mode behavior (goal-setting mode with no analytics data). Fogg has explicit degraded-mode behavior (qualitative B=MAP hypothesis with LOW confidence). The AI-First Design prerequisite blocking dependency is explicitly modeled with worktracker entity requirements and acceptance criteria. The alternative substitution path (Service Blueprinting) is documented with conditions under which it activates.

**Gaps:**

- The Design Sprint Friday testing protocol specifies "3+ external user sessions" as the minimum viable bar but the fallback for teams that cannot recruit any external users (0 sessions) is "explicit acknowledgment before implementation begins" -- which is governance, not an alternative methodology. For a Tiny Team at a pre-launch stage with no user base, this gap is the most likely execution failure mode and deserves a more concrete alternative.
- Lean UX's hypothesis backlog management does not include a pruning/retirement criterion (FM-023). Without pruning criteria, backlog accumulation is a known Lean UX execution failure mode. Acknowledged in Revision 4 log but addressed only via "methodology limitations disclosure" rather than an explicit pruning guideline.

**Improvement Path:**

Add a Design Sprint zero-user fallback: define what outputs the skill should produce when the Friday test cannot be completed (e.g., "produces an untested prototype; recommend immediate post-launch user testing within first 5 users"). Add a Lean UX backlog hygiene note: "Retire hypotheses after a sprint cycle regardless of outcome; keep active backlog below sprint capacity."

---

### Traceability (0.93/1.00)

**Evidence:**

The four-revision change log at the end of the document traces every finding from every strategy to specific section modifications. Evidence IDs are present in the Evidence Summary. Inline annotations throughout the document use brackets like [SM-001], [RT-003], [CC-004], [FM-002] to trace each addition back to its originating finding. AI-First Design synthesis sources are enumerated with planned paths. The revision history is detailed and honest -- the Revision 4 log explicitly notes when a finding was "acknowledged" rather than resolved.

**Gaps:**

- Evidence source paths are relative, not absolute (FM-018 open).
- The change log entry for SR-005 (Kano/Fogg rank labels) states "already correct as-is" but the S-010 report provided explicit evidence of the errors in Sections 4 and 6. If the fix was absorbed by SR-001 (section reordering), this should be stated rather than "already correct as-is." This creates a minor traceability ambiguity about whether the rank labels in Sections 4 and 6 were specifically verified or assumed correct post-SR-001.
- The Revision 4 log handles FM-016 through FM-023 as a block: "acknowledged in methodology limitations disclosure" -- without identifying which specific section each finding was addressed in or what text was added. For a C4 deliverable, per-finding attribution in the change log is the expected standard.

**Improvement Path:**

Convert FM-016 through FM-023 in the change log from a block acknowledgment to individual entries. Update evidence paths to absolute project-relative paths. Clarify SR-005 resolution in the change log.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Methodological Rigor | 0.83 | 0.90 | Replace the dependency-chain/gatekeeper weighting framing with clean graduated-priority language that accurately describes the weighted average implementation. This is the highest-impact single change -- it resolves the DA-001 residual tension that has been carried through Revisions 2-4. |
| 2 | Methodological Rigor | 0.83 | 0.90 | Add a boundary uncertainty verification: calculate which excluded frameworks would enter the top 10 under ±0.25 score uncertainty and confirm none do. This converts the FM-001 limitation disclosure into a verified claim. |
| 3 | Internal Consistency | 0.87 | 0.92 | Revise the weighting rationale simultaneously with Priority 1 -- the dependency-chain language in Section 1 is the root cause of the internal consistency gap. A single Section 1 rewrite resolves both dimensions. |
| 4 | Completeness | 0.92 | 0.95 | Add "AI execution limits" documentation to the 8 frameworks lacking it (Atomic Design, HEART, Lean UX, Microsoft Inclusive Design, Kano, Fogg, Nielsen's, AI-First Design). Even a single sentence per framework identifying which steps AI cannot execute unilaterally closes this gap. |
| 5 | Completeness | 0.92 | 0.95 | Add V2 candidate specificity for the four uncovered ethics sub-domains (algorithmic bias, data privacy, dark patterns, AI transparency). Naming one candidate per domain (even "no established framework; custom Jerry research task") converts acknowledged gaps into a managed V2 roadmap. |
| 6 | Evidence Quality | 0.93 | 0.95 | Convert relative evidence paths to full project-relative paths in the Evidence Summary (FM-018). Minor but completable. |
| 7 | Traceability | 0.93 | 0.95 | Expand FM-016 through FM-023 in the change log from a block entry to individual entries with specific section references. Clarify the SR-005 resolution entry. |
| 8 | Actionability | 0.95 | 0.97 | Add Design Sprint zero-user fallback and Lean UX backlog pruning guideline. These are minor additions that close the two remaining actionability gaps. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computed
- [x] Evidence documented for each score -- specific findings, sections, and strategy reports cited
- [x] Uncertain scores resolved downward (Methodological Rigor chose 0.83 not 0.85; Internal Consistency chose 0.87 not 0.90)
- [x] Revision 4 calibration considered -- this is a well-revised deliverable that has absorbed 9 strategy outputs; first-draft anchor is not the right comparison frame, but the C4 0.95 threshold is correctly treated as a high bar
- [x] No dimension scored above 0.95 without exceptional evidence (Actionability at 0.95 is justified by the density of concrete implementation guidance)
- [x] Composite arithmetic verified: (0.92 x 0.20) + (0.87 x 0.20) + (0.83 x 0.20) + (0.93 x 0.15) + (0.95 x 0.15) + (0.93 x 0.10) = 0.184 + 0.174 + 0.166 + 0.1395 + 0.1425 + 0.093 = **0.900**

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.900
threshold: 0.95
weakest_dimension: Methodological Rigor
weakest_score: 0.83
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Replace dependency-chain/gatekeeper weighting framing with graduated-priority language accurately representing the weighted average (resolves DA-001 residual tension, impacts Methodological Rigor and Internal Consistency)"
  - "Add boundary uncertainty verification: confirm no excluded framework enters top 10 under ±0.25 score uncertainty (converts FM-001 limitation disclosure into verified claim)"
  - "Add AI execution limits documentation to 8 frameworks lacking it (Atomic Design, HEART, Lean UX, Microsoft Inclusive Design, Kano, Fogg, Nielsen, AI-First Design)"
  - "Add V2 candidate specificity for four uncovered ethics sub-domains (algorithmic bias, data privacy, dark patterns, AI transparency)"
  - "Convert relative evidence paths to full project-relative paths in Evidence Summary (FM-018)"
  - "Expand FM-016 through FM-023 change log entries from block to individual per-finding entries"
  - "Add Design Sprint zero-user fallback and Lean UX backlog pruning guideline"
```

---

## Critical Findings Resolution Verification

The following table records whether the Critical findings from all 9 strategy outputs were genuinely resolved (not merely acknowledged) in Revision 4:

| Finding | Source | Severity | Resolution Status | Evidence of Resolution |
|---------|--------|----------|-------------------|----------------------|
| RT-001 (criteria not validated against UX failure modes) | S-001 | Critical | RESOLVED | Section 1 UX Failure Mode Coverage Validation table with 7 failure modes mapped |
| RT-002 (MCP integration score inflation for Bridge MCPs) | S-001 | Critical | RESOLVED | Native/Community/Bridge categorization in Section 1; HEART C3=4, Fogg C3=3; Bridge MCP WARNINGs throughout |
| RT-003 (AI-First Design circular reference) | S-001 | Critical | RESOLVED (with acknowledged residual risk) | Maturity corrected to 2/10; SYNTHESIZED label; RT-003 TRANSPARENCY NOTICE; BLOCKING prerequisite worktracker dependency; DA-003 (P) notation on all scores; alternative (Service Blueprinting) documented |
| CV-009 (sensitivity analysis AI-First Design @20% score incorrect) | S-011 | Critical | RESOLVED | AI-First Design @20% corrected to 7.80; "most weight-stable" characterization |
| SR-001 (rank number collision) | S-010 | Critical | RESOLVED | Microsoft Inclusive Design Rank #7; AI-First Design Rank #8; sections reordered |
| SR-002 (non-selected matrix not sorted) | S-010 | Critical | RESOLVED | Non-selected matrix re-sorted by corrected weighted totals in Revision 4 change log |
| DA-001 (dependency-chain weighting self-contradictory) | S-002 | Critical | PARTIALLY RESOLVED | Changed "necessary conditions/gatekeepers" to "highest-weight priority criteria"; clarification added; but dependency-chain language coexists with weighted-average math in the text -- tension remains |
| DA-002 (complementarity self-referential) | S-002 | Critical | RESOLVED | Two-pass methodology documented; C5 explicitly labeled as consistency check not independent validation; MCDA academic grounding provided |
| PM-001 (AI-First Design synthesis not a BLOCKING dependency) | S-004 | Critical | RESOLVED | BLOCKING prerequisite added; worktracker entity requirement; acceptance criteria; alternative path documented |
| PM-002 (no parent skill routing mechanism) | S-004 | Critical | RESOLVED | Section 7 added with full parent skill triage mechanism, sub-skill routing guide, MCP maintenance contract |
| PM-003 (Hotjar-dependent sub-skills have no non-Hotjar paths) | S-004 | Critical | RESOLVED | Primary non-Hotjar data paths added to HEART, Lean UX, Fogg; degraded-mode behavior documented |
| PM-004 (no cross-skill disambiguation guide) | S-004 | Critical | RESOLVED | Section 7 routing decision guide; "When to use this vs. other sub-skills" table in all 10 framework entries |
| IN-001 (forward-looking enablement patterns stated as present-tense facts) | S-013 | Critical | RESOLVED | CC-004 forward-looking framing notice at Section 3 introduction |
| IN-002 (Figma dependency risk undisclosed) | S-013 | Critical | RESOLVED | Figma dependency risk analysis added to Section 1 C3 criterion; 6/10 Figma-dependent frameworks documented with fallback paths |
| IN-003 (AI execution modes not differentiated) | S-013 | Critical | RESOLVED | AI Execution Mode Taxonomy (deterministic vs. synthesis hypothesis) added to Section 1 |
| FM-001 (single-rater bias) | S-012 | Critical | PARTIALLY RESOLVED | Disclosed as limitation with ±0.25 uncertainty; inter-rater check recommended but not performed |
| FM-002 (community MCP production readiness unverified) | S-012 | Critical | RESOLVED | Community MCP production readiness caveat added to Section 1 C3 criterion |
| FM-003 (complementarity circular dependency) | S-012 | Critical | RESOLVED (overlaps DA-002) | Two-pass methodology; iteration sequence documented; convergence in one iteration confirmed |
| FM-004 (weight ceiling effect undisclosed) | S-012 | Critical | RESOLVED | C1+C2 ceiling effect analysis added to Section 1 Weighting Rationale (FM-004) |
| FM-005 (AI-First Design no go/no-go gate) | S-012 | Critical | RESOLVED | BLOCKING prerequisite with worktracker entity; validation gate documented |

**Summary:** 17 of 20 Critical findings fully resolved. 3 partially resolved: DA-001 (weighting framing tension persists), FM-001 (disclosed but no inter-rater check executed). No unresolved Critical findings that block acceptance as a fatal flaw -- the partial resolutions leave residual quality gaps that cap the score but do not constitute blocking issues.

---

*Quality Score Report Version: 1.0*
*Strategy: S-014 (LLM-as-Judge)*
*Template: SSOT quality-enforcement.md 6-dimension weighted composite*
*Deliverable: `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 4)*
*Scored: 2026-03-03T00:00:00Z*
*Scoring Agent: adv-scorer*
