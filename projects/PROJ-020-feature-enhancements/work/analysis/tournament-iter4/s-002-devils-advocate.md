# Devil's Advocate Report: UX Framework Selection -- Weighted Multi-Criteria Analysis

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
**Criticality:** C4 (Critical -- architecture/governance, irreversible portfolio decision)
**Date:** 2026-03-03T00:00:00Z
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied 2026-03-03 (confirmed -- steelman report at `projects/PROJ-020-feature-enhancements/work/analysis/tournament-iter4/s-003-steelman.md`; 1 Critical / 4 Major / 3 Minor improvements identified and used to target this critique against a strengthened version per H-16)

---

## Step 1: Role Assumption

The Devil's Advocate role is assumed against Revision 8 of the UX Framework Selection analysis. This is a C4-criticality irreversible portfolio decision: it will determine which 10 UX frameworks constitute the Jerry `/user-experience` skill for the foreseeable future. The role's mandate is to argue against the deliverable's positions, assumptions, and claims -- finding the strongest possible counter-arguments to the central thesis, methodology, and selection decisions. The steelman output (SM-010-I4 through SM-017-I4) has strengthened the deliverable's argument; this critique now attacks that strengthened version.

**H-16 Compliance Confirmed:** S-003 Steelman output exists at the path stated above. The critique targets the strengthened version of the deliverable, not the original Revision 8 draft.

**Deliverable under challenge:** Revision 8 argues that a portfolio of 10 UX frameworks optimally covers the Jerry `/user-experience` skill requirements through a 6-criterion Weighted Sum Method analysis of 40 candidates, validated by sensitivity analysis, FMEA, adversarial review, and lifecycle coverage validation.

---

## Step 2: Assumption Inventory

**Explicit assumptions (stated in deliverable):**

1. A 10-framework ceiling is the right portfolio size (acknowledged as analyst-assumed, not user-specified).
2. Weighted Sum Method is the appropriate MCDA technique (AHP and TOPSIS explicitly rejected).
3. The 6 criteria (C1-C6) with their specific weights (25/20/15/15/15/10) correctly represent team priorities.
4. AI-First Design can achieve C1 >= 9 and C2 >= 8 in a synthesis deliverable (explicitly projected, not verified).
5. The ±0.25 uncertainty band adequately characterizes single-rater scoring uncertainty.
6. "Tiny Teams" of 2-5 persons is the correct target cohort for this portfolio.
7. V1 scope deliberately excludes user research; minimum viable research from Design Sprint and Lean UX is sufficient.
8. Service Blueprinting is correctly scored at 7.40 (the single most important near-threshold competitor).

**Implicit assumptions (not stated but relied upon):**

A. The 40-framework universe is complete -- that no important UX framework exists outside the evaluated set.
B. The criteria definitions are stable -- that "MCP Integration" means the same thing in 6 months as it does today.
C. The sub-skills described in Section 3 are implementable with current LLM capabilities -- that [DESIGN TARGET] claims will actually be achieved at implementation time.
D. The 30-respondent Kano threshold is a hard operational floor, not a guideline that teams will rationalize downward.
E. The V2 roadmap items (user research, dark patterns, algorithmic bias) will actually be addressed in a follow-on project, not deferred indefinitely.
F. A "named owner" for MCP maintenance will reliably prevent the maintenance contract from becoming a dead letter over time.
G. The lifecycle coverage claimed in Section 4 is complete -- that 7 failure modes cover the most important UX risks.
H. The WSM criteria are genuinely independent -- that scoring one criterion does not contaminate scores on others.

**Priority assumption failures (most damaging if wrong):** Assumptions A (framework universe completeness), C (sub-skill implementability), E (V2 follow-through), and G (failure mode completeness) represent the highest-consequence assumption failures -- each would invalidate the portfolio's operational utility without invalidating its internal logical structure.

---

## Step 3: Counter-Arguments

### Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-I4 | The preamble revision -- even post-SM-010-I4 -- does not resolve the document's fundamental signal-to-noise problem; the structural improvement is prescribed but not yet applied in Revision 8 | Critical | Revision 8 preamble opens with a 36-item revision metadata block before the Core Thesis; SM-010-I4 is a reconstruction in the steelman report, not a change applied to the deliverable | Completeness, Actionability |
| DA-002-I4 | The 40-framework evaluation universe is asserted complete but never justified: the candidate generation process is opaque | Major | Section 2 states "all 40 catalog entries were scored" and the Seed List Audit confirms 10 seeds were evaluated, but the methodology for generating the 40-candidate universe is not documented anywhere in the deliverable | Completeness, Methodological Rigor |
| DA-003-I4 | The 10-framework ceiling is the single most consequential assumption in the analysis and is addressed only defensively, not analytically | Major | The document states "10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions, not a user-specified requirement" (CC-002). No analysis is provided of what cognitive load, maintenance burden, or skill routing complexity the ceiling addresses. | Methodological Rigor, Evidence Quality |
| DA-004-I4 | The WSM independence assumption resolution ("at most 0.10-0.20 points of score distortion") was computed using the very scores it claims to validate -- the bounding pair identification is circular | Major | The bounding pair uses AI-First Design (C1=10, C5=10, "perfect correlation") and JTBD/Microsoft (C1=8, C5=10). These scores were set by the same single rater under the same assumptions. If the rater systematically over-scores correlated criteria together, the bound understates true distortion. The document does not account for correlated rater error. | Methodological Rigor, Internal Consistency |
| DA-005-I4 | The V2 roadmap contains four P1 items -- user research, Service Blueprinting, dark patterns, algorithmic bias -- that are not optional improvements but documented HIGH RISK and high-consequence gaps. Deferring them to "V2" without a committed delivery timeline or owner creates an acceptance threshold illusion | Major | Section 4 documents the user research gap as "HIGH RISK" and specifically warns teams against relying on Design Sprint/Lean UX substitutes. Section 4 also enumerates dark patterns (P1) and algorithmic bias (P1) as unaddressed. The V2 scoping trigger criteria (Section 4) require 2 triggers in a single month -- a bar that a new skill portfolio may never reach if usage is limited | Completeness, Actionability |
| DA-006-I4 | The AI Execution Mode Taxonomy across Sections 3.1-3.10 creates a confidence labeling system that has no teeth: synthesis hypothesis outputs labeled MEDIUM or LOW confidence require "user acknowledgment" or "validation" that the skill cannot verify was actually obtained | Major | Section 7.5 Synthesis Hypothesis Validation Protocol specifies that MEDIUM confidence synthesis requires user confirmation of "expert review from [name] with [qualification]" or "N user data points from [source]." The enforcement mechanism ("Skill surfaces confirmation prompt") relies on the user self-attesting. No mechanism exists to verify the attestation is truthful. A user under time pressure will simply confirm to proceed. | Actionability, Evidence Quality |
| DA-007-I4 | The 5-wave implementation sequencing plan has a cascade failure mode that is not analyzed: if Wave 1 stalls (the most common failure mode for new practices), the entire implementation stops, but the document treats bypass conditions as exceptional rather than the likely path | Major | Section 7.4 Wave bypass/stall recovery protocol exists but frames stalls as "when a wave stalls... the following bypass conditions apply" -- presenting stalls as edge cases. The wave transition criteria are ambitious (Wave 2 requires "at least one DONE story" with artifacts at specified paths; Wave 3 requires "Storybook installed with >= 5 Atom stories"). For teams adopting this skill portfolio alongside other work, wave stalls may be the norm, not the exception. No success-rate data or adoption curve benchmarks are cited. | Actionability, Evidence Quality |
| DA-008-I4 | The document's self-described "honest characterization" of AI-First Design as highest-risk contains a stale claim that SM-016-I4 identifies but Revision 8 does not yet fix | Minor | Section 3.8 inclusion decision logic still reads: "the sensitivity analysis confirms this is the most weight-sensitive selection" -- a claim contradicted by CV-009 (which established AI-First Design is the most weight-stable). SM-016-I4 flags this as a stale claim requiring correction, but Revision 8 was produced before SM-016-I4 could be incorporated. | Internal Consistency, Traceability |
| DA-009-I4 | The JTBD "Good -- fills the 'what to build' gap; limited by no quantitative outcome guarantee" coverage map entry (Section 4) understates the preventive value that is established elsewhere in the same document -- an internal inconsistency that SM-014-I4 identifies but Revision 8 does not yet fix | Minor | Section 4 Domain Coverage Map: "Strategic Problem Framing: Jobs to Be Done (#6) -- Good -- fills the 'what to build' gap; limited by no quantitative outcome guarantee." Section 1 UX Failure Mode Coverage Validation describes JTBD as providing "dual-layer protection: preventive (pre-design, JTBD) + detective (in-design, Design Sprint)" -- a substantially stronger characterization. SM-014-I4 flags this as an inconsistency. | Internal Consistency, Evidence Quality |
| DA-010-I4 | The document footer still reads "Date: 2026-03-02" despite Revision 8 being completed on 2026-03-03 -- a traceability defect that SM-015-I4 identifies but Revision 8 does not yet fix | Minor | Document footer: "*PS Analyst Agent v2.3.0 | ... | Date: 2026-03-02*". Revision 8 header and revision log both show 2026-03-03. SM-015-I4 flags this. | Traceability |

---

## Step 4: Response Requirements

### P0 Findings (Critical -- MUST resolve before acceptance)

**DA-001-I4: Preamble revision not applied to deliverable**

The steelman finding SM-010-I4 prescribes a specific structural fix (thesis-first preamble) but only as a reconstruction in the steelman report. Revision 8 is the actual deliverable and must be updated. This is not a style preference -- at C4 criticality, the document's primary analytical contribution must be immediately visible to any reader who will use it to make an irreversible implementation decision.

**What the creator must demonstrate to resolve:**
- Apply SM-010-I4's reconstructed preamble structure to the Revision 8 deliverable itself: a "Core Thesis" block appears BEFORE the revision metadata block and BEFORE the four qualification notices.
- The qualification notices (MINIMALITY CLAIM QUALIFICATION, SCOPE BOUNDARY, 10-FRAMEWORK CEILING PROVENANCE, HIGH RISK gap) are not removed but repositioned to follow the thesis.

**Acceptance criteria:** Revision 9 opens with a structured Core Thesis block (portfolio value proposition, lifecycle coverage, arithmetic verification, uncertainty bounds) before any revision metadata or qualification notices appear.

---

### P1 Findings (Major -- SHOULD resolve; require justification if not)

**DA-002-I4: 40-framework universe generation methodology opaque**

**What the creator must demonstrate to resolve:**
- Document the methodology by which the 40-framework candidate universe was generated. This can be brief but must answer: (a) what sources generated candidates (literature, survey research, professional communities, seed list + expansion), (b) what inclusion/exclusion criteria determined whether a framework made the 40-candidate list, (c) whether the universe was reviewed for coverage bias (e.g., Western UX frameworks over-represented; enterprise-scale frameworks over-represented).
- If the universe was simply "all frameworks identified by ps-researcher survey + seed list," that is acceptable but must be stated. The opaqueness -- not the content -- is the finding.

**Acceptance criteria:** Section 6 Seed List Audit or Section 1 Methodology includes a "Candidate Universe Generation" paragraph explaining the provenance of the 40-candidate list. The paragraph must answer questions (a)-(c) above.

---

**DA-003-I4: 10-framework ceiling not analytically justified**

**What the creator must demonstrate to resolve:**
- Provide at minimum a brief analytical justification for why 10 is the correct portfolio size: what specific skill routing complexity, maintenance burden, or cognitive load constraint the ceiling enforces. A reference to "standard Jerry skill portfolio size conventions" is insufficient -- what is the actual operational constraint?
- Alternatively: acknowledge explicitly that the ceiling is arbitrary and that the optimal number is unknown, and explain why the analysis proceeds with this arbitrary ceiling rather than a derived one.

**Acceptance criteria:** CC-002 notice or a new "Portfolio Size Justification" subsection provides either (a) the operational rationale for 10 frameworks, or (b) an explicit acknowledgment that the ceiling is an arbitrary convention with the operational implications of raising it explained.

---

**DA-004-I4: WSM independence bound computation uses scores being validated (circular)**

**What the creator must demonstrate to resolve:**
- Acknowledge that the 0.10-0.20 bound is a bound on score distortion under the scoring model as executed, not a bound on scoring accuracy. The distinction is: the bound shows how much C1/C5 correlation would shift scores IF the scores are correct; it does not show how much systematic rater bias in scoring correlated criteria simultaneously would affect results.
- Add one sentence to the WSM independence resolution block distinguishing "score distortion from correlation" (what is computed) from "rater bias in correlated scoring" (what is not computed and remains a residual uncertainty).

**Acceptance criteria:** The WSM independence resolution block contains a sentence distinguishing the 0.10-0.20 distortion bound (model-level) from the unquantified residual uncertainty from potential correlated rater bias (rater-level). The bound is not retracted -- only its scope is clarified.

---

**DA-005-I4: V2 roadmap high-risk items deferred without commitment or timeline**

**What the creator must demonstrate to resolve:**
- The four P1 V2 items (user research framework, dark patterns audit, algorithmic bias review, Service Blueprinting) are explicitly labeled HIGH RISK or the document explains why they are not HIGH RISK. If they are HIGH RISK, the V2 scoping trigger criteria in Section 4 must be evaluated against the expected usage patterns: will those triggers actually fire for a newly-launched skill with limited initial usage?
- Either: (a) tighten the V2 trigger criteria to conditions that are likely to be met within 2-3 sprint cycles of launch, or (b) explicitly acknowledge that V2 may not happen and explain what the operational consequence is for users who encounter the HIGH RISK gap without a V2 available.

**Acceptance criteria:** The HIGH RISK user research gap section and the V2 scoping trigger criteria are aligned: either the triggers are adjusted to match the reality that new-skill adoption starts slow, or the analysis explicitly states the consequence of indefinite V2 deferral.

---

**DA-006-I4: Synthesis hypothesis confidence gates are unverifiable self-attestation**

**What the creator must demonstrate to resolve:**
- The Section 7.5 Synthesis Hypothesis Validation Protocol gates rely entirely on user self-attestation for MEDIUM and LOW confidence outputs. The document must acknowledge this limitation explicitly and explain why self-attestation is accepted as the enforcement mechanism.
- Alternatively: propose a verification mechanism beyond self-attestation. For example, for MEDIUM confidence synthesis, the skill could require pasting the name and qualification of the expert reviewer before proceeding, creating an audit trail. This is still self-attestable but introduces a friction cost that reduces trivial attestation.

**Acceptance criteria:** Section 7.5 acknowledges that the MEDIUM/HIGH confidence gates rely on user self-attestation and cannot be machine-verified. The document either accepts this limitation explicitly or specifies a higher-friction verification mechanism that makes trivial bypass less likely.

---

**DA-007-I4: Wave adoption cascade failure not analyzed**

**What the creator must demonstrate to resolve:**
- The wave bypass/stall recovery protocol (PM-003) exists but frames stalls as exceptional. The document must provide either: (a) a realistic adoption curve expectation (e.g., "most teams will stall at Wave 2 because launching a product with analytics configured is a prerequisite many will not meet quickly -- plan for this"), or (b) an explicit acknowledgment that the wave sequencing is aspirational and that teams should expect to use the bypass conditions frequently.
- Additionally, the bypass conditions themselves should be stress-tested: if a team uses the Wave 1→2 bypass (JTBD DONE but heuristic eval stalled) and proceeds to Wave 2 with only Lean UX, are they building on a foundation that will cause problems later?

**Acceptance criteria:** Section 7.4 contains either a realistic adoption curve narrative acknowledging that stalls are common (not exceptional), or an explicit caveat that the sequential wave model assumes implementation capacity and tool access that many teams will not have at Wave 1 entry.

---

### P2 Findings (Minor -- MAY resolve; acknowledgment sufficient)

**DA-008-I4: Stale "most weight-sensitive" claim in Section 3.8**

SM-016-I4 has identified this. Incorporating SM-016-I4's corrected text into Revision 9 resolves this finding. Acknowledgment: the stale claim exists in Revision 8 because SM-016-I4 was produced in the tournament-iter4 steelman, after Revision 8 was frozen.

**Response required:** Incorporate SM-016-I4's reconstructed inclusion decision logic into Revision 9.

---

**DA-009-I4: JTBD coverage map entry inconsistency**

SM-014-I4 has identified this. Incorporating SM-014-I4's strengthened coverage quality text into Revision 9 resolves this finding.

**Response required:** Incorporate SM-014-I4's strengthened JTBD entry into the Section 4 Domain Coverage Map.

---

**DA-010-I4: Document footer date stale**

SM-015-I4 has identified this. A one-line fix.

**Response required:** Update footer to "Last revised: 2026-03-03 (Revision 8)" as specified in SM-015-I4.

---

## Step 5: Scoring Impact

### Synthesis

**Overall assessment:** REVISE -- targeted revision required to address 1 Critical and 4 Major findings. The deliverable's analytical core is sound. The core decision (selection of 10 frameworks from 40 candidates, validated by sensitivity analysis and adversarial review) withstands Devil's Advocate scrutiny at the logical level. The counter-arguments above do not invalidate the selection. They do expose:

1. **One presentation gap that constitutes a document integrity failure** (DA-001-I4): The SM-010-I4 fix is prescribed but not applied to the actual deliverable. A document that has been through 8 revisions but still opens with revision metadata before the thesis is presenting its best argument behind a noise barrier. At C4 criticality, this is a material gap.

2. **One methodological gap with no resolution path offered** (DA-002-I4): The candidate universe generation methodology is opaque. This is not a subjective concern -- it is a reproducibility gap. If the analysis were replicated, a different researcher would not know where the 40-candidate list came from.

3. **Two design decisions that require analytical justification, not just acknowledgment** (DA-003-I4, DA-004-I4): The 10-framework ceiling and the WSM independence bound both receive defensive treatment rather than analytical treatment. The document is honest about their limitations but does not complete the argument.

4. **Two operational specification gaps where the enforcement mechanisms stated may not work in practice** (DA-005-I4, DA-006-I4): The V2 trigger criteria may never fire; the synthesis hypothesis gates rely on unverifiable attestation. These gaps do not invalidate the analysis but reduce its operational completeness.

5. **One structural completeness gap** (DA-007-I4): Wave adoption stall is treated as exceptional when it may be the norm.

**Findings that do NOT require significant revision:** DA-008-I4, DA-009-I4, and DA-010-I4 are direct carry-forwards from steelman findings that are not yet incorporated into the deliverable. They are not new counter-arguments -- they are the steelman's own improvement list. Incorporating SM-014-I4, SM-015-I4, and SM-016-I4 from the steelman report resolves all three.

### Scoring Impact Table

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | DA-001-I4: Core Thesis preamble structure prescribed but not applied; DA-002-I4: candidate universe generation methodology missing; DA-005-I4: HIGH RISK V2 items lack commitment timeline |
| Internal Consistency | 0.20 | Negative | DA-009-I4: JTBD coverage map entry contradicts Section 1 failure mode description; DA-008-I4: stale "weight-sensitive" claim in Section 3.8 contradicts CV-009 correction applied elsewhere |
| Methodological Rigor | 0.20 | Negative | DA-002-I4: opaque candidate universe generation undermines reproducibility; DA-003-I4: 10-framework ceiling analytically unjustified; DA-004-I4: WSM independence bound circular within model |
| Evidence Quality | 0.15 | Negative | DA-004-I4: the 0.10-0.20 correlation bound conflates score distortion with rater accuracy without acknowledging the distinction; DA-006-I4: confidence gate enforcement relies on unverifiable self-attestation |
| Actionability | 0.15 | Negative | DA-005-I4: V2 trigger criteria may not fire under realistic adoption conditions; DA-006-I4: MEDIUM/LOW confidence gates do not prevent trivial bypass; DA-007-I4: wave stall framed as exceptional rather than expected |
| Traceability | 0.10 | Negative (minor) | DA-010-I4: document footer date stale; SM-010-I4 prescribed but not applied means steelman improvements are not traceable to the deliverable itself |

**Composite impact estimate:** The Critical finding (DA-001-I4) affects Completeness and Actionability. Four Major findings affect Methodological Rigor, Internal Consistency, Evidence Quality, and Actionability. Three Minor findings affect Internal Consistency and Traceability. Pre-revision estimated composite score: approximately 0.87-0.90 (below the 0.92 threshold). Post-revision estimated composite score if all P0/P1 findings are addressed: approximately 0.93-0.96 (above threshold, meeting the >= 0.95 tournament target).

---

## Execution Statistics

- **Total Findings:** 10
- **Critical:** 1 (DA-001-I4)
- **Major:** 6 (DA-002-I4 through DA-007-I4)
- **Minor:** 3 (DA-008-I4, DA-009-I4, DA-010-I4)
- **Protocol Steps Completed:** 5 of 5

---

## Recommended Revision Priority

**P0 -- MUST resolve before acceptance:**

| # | Finding | Action | Acceptance Criteria |
|---|---------|--------|---------------------|
| 1 | DA-001-I4 | Apply SM-010-I4's thesis-first preamble structure to the actual deliverable (not just the steelman reconstruction) | Revision 9 opens with Core Thesis block before revision metadata and qualification notices |

**P1 -- SHOULD resolve:**

| # | Finding | Action | Acceptance Criteria |
|---|---------|--------|---------------------|
| 2 | DA-002-I4 | Add "Candidate Universe Generation" paragraph to Section 1 or Section 6 | Explains source and inclusion criteria for the 40-candidate list |
| 3 | DA-003-I4 | Add analytical justification for 10-framework ceiling or explicitly acknowledge its arbitrariness with operational implications | CC-002 notice or new subsection provides justification or honest acknowledgment |
| 4 | DA-004-I4 | Add one sentence to WSM independence resolution distinguishing model-level distortion bound from rater-level correlated bias | The 0.10-0.20 bound is not retracted; its scope is clarified |
| 5 | DA-005-I4 | Align V2 trigger criteria with realistic adoption conditions, or acknowledge the consequence of indefinite V2 deferral | HIGH RISK gap section and V2 triggers are aligned on likelihood of triggering |
| 6 | DA-006-I4 | Acknowledge self-attestation limitation in Section 7.5, or add a friction mechanism to reduce trivial bypass | Section 7.5 contains explicit acknowledgment of attestation limitation |
| 7 | DA-007-I4 | Add adoption curve narrative to Section 7.4 acknowledging stalls are common, not exceptional | Section 7.4 contains realistic adoption curve expectation or explicit stall-is-normal caveat |

**P2 -- MAY resolve:**

| # | Finding | Action | Acceptance Criteria |
|---|---------|--------|---------------------|
| 8 | DA-008-I4 | Incorporate SM-016-I4 corrected inclusion decision logic into Section 3.8 | Stale "weight-sensitive" claim replaced with correct "weight-stable/execution-risk" framing |
| 9 | DA-009-I4 | Incorporate SM-014-I4 strengthened JTBD entry into Section 4 coverage map | Coverage quality upgraded to "Excellent for preventive framing" |
| 10 | DA-010-I4 | Update footer date to 2026-03-03 (Revision 8) | Footer date matches revision log |

---

*Strategy Execution Report generated by adv-executor | S-002 Devil's Advocate | Template: `.context/templates/adversarial/s-002-devils-advocate.md` | Deliverable: Revision 8 | H-16 compliance: confirmed (S-003 steelman applied prior)*
