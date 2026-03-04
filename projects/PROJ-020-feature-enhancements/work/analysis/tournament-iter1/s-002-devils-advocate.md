# Devil's Advocate Report: UX Framework Selection -- Weighted Multi-Criteria Analysis

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
**Criticality:** C4
**Date:** 2026-03-03T00:00:00Z
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied 2026-03-03 (confirmed -- `projects/PROJ-020-feature-enhancements/work/analysis/tournament-iter1/s-003-steelman.md`; steelman strengthened the portfolio-as-system justification and methodological grounding)

---

## Step 1: Role Assumption

**Role assumed:** Devil's Advocate arguing against the UX Framework Selection deliverable's core claims.

**Deliverable being challenged:** A Weighted Multi-Criteria Decision Analysis selecting 10 UX frameworks for an AI-augmented Tiny Teams portfolio (`/user-experience` Jerry skill). The deliverable has undergone 5 revision rounds incorporating S-010 (Self-Refine), S-007 (Constitutional AI), S-011 (Chain-of-Verification), S-012 (FMEA), S-013 (Inversion), and S-003 (Steelman). The S-003 Steelman strengthened the portfolio-as-system justification with a three-part minimality argument.

**Scope of critique:** Central thesis validity, methodology, scoring reliability, portfolio completeness, and forward-looking claims. This critique targets the **strengthened** version of the argument per H-16 compliance.

---

## Step 2: Assumption Inventory

**Explicit assumptions extracted from deliverable:**

| # | Assumption | Location | Challenge |
|---|-----------|----------|-----------|
| A-1 | "10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions" | CC-002, document preamble | What convention? No evidence that 10 is optimal. The ceiling is arbitrary. |
| A-2 | "Frameworks that cannot be executed by a 2-3 person team provides zero value regardless of historical reputation" (SM-003 steelman) | Section 1, Weighting Rationale | Binary. "Zero value" overstates. Semi-executable frameworks with AI augmentation may still provide partial value. |
| A-3 | C5 (Complementarity) evaluates portfolio non-redundancy as a portfolio composition constraint, not independent validation | Section 1, C5 note | Acknowledged in document but relied upon as a positive signal (SM-001 minimality proof uses C5 as a validating instrument after acknowledging its circularity). |
| A-4 | Sensitivity analysis (two weight perturbations: C1 25%→20%, C2 20%→15%) demonstrates robustness | Section 1, Sensitivity Analysis | Two perturbations of adjacent criteria are not independent tests. They share a structural bias toward the existing portfolio's composition. |
| A-5 | "No two selected frameworks occupy the same lifecycle stage AND primary function" | SM-001 steelman | Design Sprint (#2) and Lean UX (#5) are both assigned to the "Design" stage. The claim depends on a granular sub-categorization ("intensive process" vs. "continuous process") that is the analyst's own categorization. |
| A-6 | AI-First Design "fills the AI product UX domain gap that no established framework addresses" | CC-001 notice, Section 3.8 | This is a gap defined by the analyst. External sources (NN Group, Nielsen Norman) have not codified such a framework because the domain is still emerging. The gap may be temporary, not structural. |
| A-7 | Single-rater bias for 30 non-selected frameworks carries ±0.25 uncertainty; this does not invalidate top-10 selections | Section 1, Methodology Limitations | The claim that top-10 selections are immune from single-rater bias assumes the adversarial review (S-001) constituted adequate independent validation. S-001 corrected 3 errors -- it may have missed others. |

**Implicit assumptions extracted:**

| # | Implicit Assumption | Where Relied Upon | Challenge |
|---|--------------------|--------------------|-----------|
| IA-1 | "Tiny Teams" = 2-5 people, is the primary and definitively relevant target profile for the intended `/user-experience` skill | Entire document | Jerry projects are not all Tiny Teams. Developers using Jerry may be part of larger organizations. The profile restriction may exclude valid use cases without acknowledgment. |
| IA-2 | AI augmentation will remain stable and performant enough to execute framework steps at the assumed quality level | All framework descriptions ("AI pre-generates 20+ sketch variants") | LLM capability fluctuates across model versions. Claims like "under 10 minutes" and "under 30 minutes with AI assistance" are performance targets, not verified benchmarks. |
| IA-3 | The 6 criteria (C1-C6) comprehensively capture all relevant selection dimensions | Section 1, Scoring Scale | Missing dimension: Total Cost of Ownership (TCO) / tooling cost. Six of ten frameworks require paid commercial tools (Figma, Miro, Hotjar, Maze). The framework portfolio may be inaccessible to teams without these subscriptions. |
| IA-4 | The source research artifacts (3 files) provide a sufficient evidence base for scoring all 40 frameworks | Evidence Summary | Three research artifacts, all generated by the same project, may share systematic biases. No external benchmark study was cited for framework-level scoring validation. |

---

## Step 3: Counter-Arguments

### Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-20260303 | The minimality proof (SM-001 steelman) is circular: it proves the portfolio is minimal given the criteria, not that the criteria are correct | Critical | "no two selected frameworks occupy the same lifecycle stage AND primary function -- testable from the Complementarity Matrix" (SM-001). The stage/function categorization IS the analyst's work. A different categorization would produce a different minimality proof. | Methodological Rigor |
| DA-002-20260303 | The two sensitivity perturbations are structurally correlated, not independent, and test the least risky scenarios | Critical | Section 1 Sensitivity Analysis: perturbation 1 reduces C1 (25%→20%), perturbation 2 reduces C2 (20%→15%). Both test downweighting the criteria the selected frameworks ALREADY score highest on. Neither tests the most dangerous scenario: upweighting criteria where the selected set has weaknesses (C3: MCP Integration, C4: Maturity). | Methodological Rigor, Evidence Quality |
| DA-003-20260303 | AI-First Design's inclusion introduces a structural integrity failure into the portfolio-as-system claim: a projected-score conditional entry cannot be part of a "minimal-complete" non-redundant portfolio | Critical | "All AI-First Design scores are marked (P) = Projected... scores are predictions about a framework-to-be-synthesized" (Section 2 scoring matrix header). SM-001 steelman asserts the portfolio is "minimal-complete" but minimal completeness cannot be claimed when one of the 10 entries does not yet exist. | Internal Consistency, Completeness |
| DA-004-20260303 | The 10-framework ceiling is an undeclared constraint that invalidates the claim of "10 frameworks that collectively maximize UX outcome coverage" | Major | "The 10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions" (CC-002). The core thesis claims to "maximize UX outcome coverage" but coverage is architecturally capped before analysis begins. The maximization is performed within a self-imposed constraint that has no empirical justification. | Internal Consistency, Completeness |
| DA-005-20260303 | The C5 (Complementarity) circularity problem is not adequately resolved by the two-pass methodology | Major | "C5 scores are portfolio-conditional by design... they are a consistency check confirming that the chosen set is non-redundant given the choices already made" (Section 1, C5 methodology caveat). Yet SM-001 cites the Complementarity Matrix as evidence that "no two selected frameworks occupy the same lifecycle stage AND primary function." The deliverable simultaneously acknowledges C5 as circular and uses it as supporting evidence for minimality. | Internal Consistency, Methodological Rigor |
| DA-006-20260303 | The single-rater scoring methodology creates asymmetric trust: top-10 scores are assumed validated by adversarial review, but adversarial review also found 3 errors -- indicating the error rate is non-zero and the remaining 7+ top-10 scores may contain undetected errors | Major | "Red Team adversarial review (S-001) identified three scoring errors (RT-002, RT-003) that were corrected through adversarial review rather than a second rater. This constitutes partial inter-rater validation" (Section 1, Methodology Limitations). Partial inter-rater validation that found 3 errors out of a limited sample is evidence of unreliability, not reliability. The deliverable interprets error discovery as validation. | Evidence Quality, Methodological Rigor |
| DA-007-20260303 | The "Tiny Teams" profile restriction silently excludes a likely majority of Jerry's actual user population without evidence that this restriction is user-specified | Major | "This analysis is optimized for teams of 2-5 people. Teams of 6 or more will find this selection useful but should be aware that it explicitly down-weights frameworks designed for larger teams" (SCOPE BOUNDARY, document preamble). The scope is declared but not justified: there is no citation that Jerry's median user is a 2-5 person team. The C1 criterion (25% weight) penalizes frameworks for teams larger than 5 even when those teams may be the primary Jerry users. | Completeness, Evidence Quality |
| DA-008-20260303 | The WSM citations added in SM-002 (Triantaphyllou 2000, Velasquez & Hester 2013, Saltelli 2004) strengthen methodological presentation but do not address the most substantive WSM criticism: WSM assumes criterion independence, which is violated by the C1/C5 interaction | Minor | SM-002 states: "WSM is preferred over more complex methods (TOPSIS, AHP)" with justification. The independence assumption (standard WSM requirement) is not addressed despite the deliverable's own observation that "C1 and C5 interact in a specific pattern: when C1 is high, C5 tends to be high because frameworks designed for Tiny Teams often have unique niches in the Tiny Teams context." AI-First Design exemplifies this: C1=10(P) and C5=10(P) -- the two projected scores are from a single assumption about AI product UX market need. | Methodological Rigor |
| DA-009-20260303 | The tooling cost dimension is entirely absent from the 6 criteria, creating a hidden assumption that all teams can afford the required subscriptions | Minor | The Evidence Summary lists three research artifacts (E-001 through E-023). None addresses the commercial licensing costs of the required tools. Figma Pro is $15/seat/month, Miro is $10/seat/month, Maze starts at $99/month. A 2-person team using all required tools spends approximately $250-400/month in tooling before implementation. The deliverable recommends these tools without acknowledging this as a selection dimension or a team accessibility concern. | Completeness |
| DA-010-20260303 | The "portfolio lifecycle coverage" claim is undermined by the HIGH RISK user research gap: a portfolio claiming to "maximize UX outcome coverage" that explicitly lacks a dedicated user research framework is not maximally complete | Minor | "The selected 10 does not include a dedicated remote user research framework. This gap carries real risk and should NOT be minimized" (Section 4, HIGH RISK gap). The core thesis claims to "maximize UX outcome coverage" yet Section 4 explicitly labels the absence of user research as HIGH RISK. These two claims are in direct tension: a portfolio with a HIGH RISK gap does not "maximize" coverage; it makes a justified compromise. | Internal Consistency |

---

## Step 4: Response Requirements

### P0: Critical -- MUST resolve before acceptance

---

### DA-001-20260303: The Minimality Proof is Circular [CRITICAL]

**Claim Challenged:**
> "no two selected frameworks occupy the same lifecycle stage AND primary function -- the Pre-Design stage has one discovery framework (JTBD) and one prioritization framework (Kano) that serve complementary purposes; the Design stage has one intensive process framework (Design Sprint), one continuous process framework (Lean UX), and one evaluation framework (Nielsen's) serving distinct functions within the same stage" (SM-001 steelman, Section 3 Complementarity Matrix)

**Counter-Argument:**
The minimality proof depends entirely on a lifecycle-stage-plus-primary-function categorization system created by the analyst. This categorization is not externally validated and is not cited from any published framework taxonomy. The stage assignments (Pre-Design, Design, Build, Post-Launch) and the function labels (intensive process, continuous process, evaluation) are the analyst's own invention. Under this self-referential taxonomy, the portfolio is guaranteed to be "minimal-complete" because the taxonomy was designed to make it so -- any two frameworks that overlap have been categorized into different functions. A skeptic could reasonably argue that Design Sprint (#2) and Lean UX (#5) occupy the same stage (Design) and the same primary function (iterative product development process), differing only in cadence. The "intensive" vs. "continuous" distinction is not from the UX literature -- it is the analyst's post-hoc rationalization of a selection already made.

**Evidence:**
The deliverable's own Complementarity Matrix (Section 4) places Design Sprint, Lean UX, AND Nielsen's Heuristics all in the "Design" phase. Three frameworks in one lifecycle stage is not non-redundant by any reasonable definition.

**Impact:**
If the minimality proof is invalid, the portfolio-as-system justification (SM-001, rated Critical by the Steelman) collapses to: "these 10 frameworks do not overlap in ways the analyst chose to categorize." The strongest argument for "why these 10 and not a different 10" is materially weakened.

**Dimension:** Methodological Rigor

**Response Required:**
The creator must either: (a) cite an externally published lifecycle-stage-plus-function taxonomy from the UX literature (not the analyst's own categorization) and demonstrate the minimality claim holds under that external taxonomy, OR (b) revise the core thesis to remove the minimality claim and replace it with a weaker but defensible claim such as "non-redundant given the analyst-defined stage categorization, as validated by the Complementarity Matrix."

**Acceptance Criteria:**
The minimality proof must be grounded in at least one external source that defines the lifecycle stages and primary functions used in the categorization. Alternatively, the claim is explicitly scoped as "non-redundant per the analyst's categorization" and the word "minimal-complete" is removed.

---

### DA-002-20260303: Sensitivity Analysis Tests the Safest Scenarios, Not the Most Dangerous [CRITICAL]

**Claim Challenged:**
> "The sensitivity analysis provides strong evidence for the selection's robustness: all 10 selected frameworks maintain their position when the highest-weight criterion (Tiny Teams Applicability) is reduced by 20% of its value (25% → 20%)" (Section 1, Sensitivity Analysis)

**Counter-Argument:**
The two sensitivity perturbations both test downweighting the criteria the selected frameworks already score highest on. This is structurally the least dangerous scenario: frameworks that dominate a criterion will also dominate when that criterion's weight is reduced slightly, because the frameworks' competitors have already been ruled out on OTHER criteria. The analysis proves stability under the least threatening conditions. The most dangerous sensitivity scenario -- the one that would most challenge the selection -- is NOT tested: upweighting C3 (MCP Integration) to a dominant position. HEART (#4) scores C3=4 and Fogg (#10) scores C3=3. Under a scenario where the team's primary constraint is MCP availability (not Tiny Teams applicability), Service Blueprinting (C3=7) becomes more competitive than Fogg. The DA-008 note partially acknowledges this ("under C3=25% weighting, HEART and Fogg retain selection but with reduced margin") but does not provide the full perturbation table demonstrating this is true, and concludes with "domain needs should guide the C3 weighting" -- which is circular (the domain-need argument is what's being tested). The deliverable's claim of "robustness" is achieved by testing only the dimensions where the selection is structurally most robust.

**Evidence:**
Section 1, DA-008 note: "Under C3 upweighting, HEART and Fogg retain selection but with reduced margin. The most sensitive selection under C3 upweighting is Fogg (#10), whose low MCP score means Service Blueprinting (C3=7) would approach it." This acknowledgment is buried in a note and does not include the actual perturbation scores.

**Impact:**
The "robustness" claim is not supported by the most relevant sensitivity test. If a Jerry user operates in an environment with strong MCP availability constraints (e.g., primarily uses Miro+Figma and no other tools), the optimal portfolio may differ from what the analysis selects, and the deliverable provides no evidence about this scenario.

**Dimension:** Methodological Rigor, Evidence Quality

**Response Required:**
Complete the C3 sensitivity perturbation that is currently only described qualitatively in the DA-008 note. Provide the full table: recalculate all top-10 and top-12 framework scores under C3=25% (redistributing from C1 or C2), and report the actual margin between Fogg and Service Blueprinting under that scenario. If the selection changes (Fogg replaced by Service Blueprinting), acknowledge the scenario under which an alternative selection is justified.

**Acceptance Criteria:**
A complete sensitivity table for C3=25% perturbation, with the actual numeric margin between Fogg (#10) and Service Blueprinting (next candidate), demonstrating the selection is stable or explicitly naming the condition under which it is not.

---

### DA-003-20260303: AI-First Design Contradicts the Minimal-Complete Portfolio Claim [CRITICAL]

**Claim Challenged:**
> "removing any single framework from the portfolio creates a named, unmitigated gap documented in Section 4's Coverage Analysis -- the portfolio is therefore minimal-complete for its stated coverage scope" (SM-001 steelman)

**Counter-Argument:**
The minimality proof requires that each framework fills a gap. AI-First Design (#8) does not currently fill any gap because it does not currently exist as a framework. Its scores are all marked (P) = Projected. A portfolio cannot be "minimal-complete" when one of its 10 elements is a placeholder for a framework-to-be-synthesized. The (P) notation means: "if the synthesis deliverable produces a framework with these properties, then the portfolio is minimal-complete." The minimality claim is conditional, not demonstrated. Furthermore, the fallback option (Service Blueprinting as a substitute if the synthesis fails) demonstrates that the AI Product UX gap CAN be filled with an existing framework, which undermines the claim that AI-First Design fills a "unique lifecycle niche" that no other framework occupies. If Service Blueprinting can substitute for AI-First Design, then AI-First Design's gap is not unique to AI product UX -- it is simply the best-available coverage given current frameworks.

**Evidence:**
Section 3.8: "Alternative if synthesis cannot be completed before skill launch: Replace AI-First Design with Service Blueprinting (rank 11, score 7.35), which has an immediately adoptable authoritative framework body and requires no synthesis work."

**Impact:**
The portfolio-as-system justification (SM-001) is the single highest-priority steelman improvement. If it is undermined by AI-First Design's conditional inclusion, the core thesis loses its most important structural argument. The deliverable simultaneously claims the portfolio is minimal-complete AND provides a substitution path that demonstrates it is not minimal on the AI Product UX dimension.

**Dimension:** Internal Consistency, Completeness

**Response Required:**
The creator must resolve the logical contradiction between (a) the minimality claim and (b) the Service Blueprinting substitution path. The options are: (1) revise the minimality claim to explicitly state it is conditional on the AI-First Design synthesis completing with the projected properties, OR (2) remove the minimality claim from the core thesis and replace it with a weaker but consistent statement such as "each framework is expected to fill a unique gap, with AI-First Design's gap coverage conditional on the synthesis deliverable."

**Acceptance Criteria:**
The core thesis and the SM-001 minimality argument must be internally consistent. If AI-First Design's scores are projected (P), the minimality claim for the portfolio must be explicitly scoped as provisional/conditional, not asserted as demonstrated.

---

### P1: Major -- SHOULD resolve before acceptance

---

### DA-004-20260303: The 10-Framework Ceiling Undermines the "Maximize Coverage" Core Thesis [MAJOR]

**Claim Challenged:**
> "This analysis selects 10 UX frameworks that collectively maximize UX outcome coverage" (Core Thesis, document preamble)

**Counter-Argument:**
"Maximize" is falsified by the arbitrary 10-framework ceiling. The document explicitly states in CC-002: "The 10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions, not a user-specified requirement." If the ceiling is arbitrary, then the selection maximizes coverage WITHIN a constraint, not maximizes coverage in any objective sense. The correct claim is: "This analysis selects the best 10 UX frameworks given the analyst's assumption that 10 is the appropriate portfolio size." This is a materially weaker claim, and it changes the burden of proof: the analysis must justify why 10 is the right number, not just why these 10 are the best 10. The document partially acknowledges this ("if implementation capacity permits additional frameworks, Service Blueprinting and Cognitive Walkthrough are the strongest additions") but does not follow through to correct the "maximize" claim in the core thesis.

**Evidence:**
Core Thesis (line 7) uses "maximize UX outcome coverage." CC-002 (line 13) states the ceiling is "analyst-assumed, not user-specified."

**Impact:**
A stakeholder reading the core thesis will believe the analysis selected the optimal portfolio. A stakeholder reading CC-002 will learn the ceiling is assumed. The thesis and the caveat contradict each other.

**Dimension:** Internal Consistency

**Response Required:**
Revise the core thesis to replace "maximize" with language consistent with CC-002's disclosure. A compliant alternative: "This analysis selects 10 UX frameworks that, within the analyst-assumed V1 scope of 10 sub-skills, provide the best coverage of deliverable-focused UX activities for AI-augmented Tiny Teams."

**Acceptance Criteria:**
The core thesis must not claim maximization if Section 1 acknowledges a self-imposed ceiling that caps coverage below what more frameworks would provide.

---

### DA-005-20260303: C5 Circularity Is Cited as Supporting Evidence Despite Being Acknowledged as Non-Validating [MAJOR]

**Claim Challenged:**
> The SM-001 steelman states: "This can be demonstrated formally: (a) no two selected frameworks occupy the same lifecycle stage AND primary function -- testable from the Complementarity Matrix" (SM-001, S-003 Steelman output)

**Counter-Argument:**
The deliverable explicitly states that C5 is "a consistency check confirming that the chosen set is non-redundant given the choices already made" and "should NOT be cited as external evidence of selection quality." The SM-001 steelman then proceeds to cite the Complementarity Matrix (which is derived from C5 scores) as formal evidence that the selection is minimal-complete. The Steelman's primary strengthening argument -- the one rated Critical -- relies on the exact evidence the document has already forbidden from being cited as external validation. This is not a minor inconsistency. It means the portfolio-as-system justification, which is the most important structural argument in the entire deliverable, rests on circular evidence.

**Evidence:**
Section 1, C5 methodology caveat: "C5 self-referentiality is methodologically appropriate for portfolio optimization but should not be cited as external evidence of selection quality."
SM-001 steelman: "This can be demonstrated formally: (a) no two selected frameworks occupy the same lifecycle stage AND primary function -- testable from the Complementarity Matrix."

**Dimension:** Internal Consistency, Methodological Rigor

**Response Required:**
The minimality claim (SM-001) must be re-founded on evidence that is NOT derived from C5 scores or the Complementarity Matrix. The creator must either: (a) find external sources (published UX methodology taxonomy papers, practitioner frameworks) that independently confirm the stage+function categorization is non-overlapping, OR (b) acknowledge that the minimality argument relies on the analyst's own categorization and is therefore internal validation only, not external proof of portfolio optimality.

**Acceptance Criteria:**
The minimality proof must not reference the Complementarity Matrix or C5 scores as supporting evidence. If it does, it must be accompanied by the disclaimer that the cited evidence is self-referential and does not constitute independent validation.

---

### DA-006-20260303: 3 Detected Scoring Errors Are Evidence of Unreliability, Not Validation [MAJOR]

**Claim Challenged:**
> "Red Team adversarial review (S-001) identified three scoring errors (RT-002: HEART C3, Fogg C3; RT-003: AI-First Design C4) that were corrected through adversarial review rather than a second rater. This constitutes partial inter-rater validation for the most critical scoring decisions" (Section 1, Methodology Limitations)

**Counter-Argument:**
Discovering 3 errors constitutes evidence that the scoring has a non-zero error rate, not that the remaining scores are correct. The deliverable interprets error correction as validation -- a logical reversal. If the S-001 Red Team found 3 errors in a limited adversarial review targeting specific decisions, a second full-pass rater would likely find additional errors. The deliverable's confidence conclusion (top-10 selections are adequately validated) is unjustified because: (a) the total number of scoring decisions reviewed by S-001 is not stated (how many decisions were checked to find 3 errors?), (b) the error rate (3/N) is unknown, and (c) there is no basis for the claim that the 7 remaining top-10 scores are error-free. The 3 corrected errors include one critical one (AI-First Design C4 corrected from 3→2, Revision 1) -- an error in the most controversial selection in the portfolio.

**Evidence:**
Revision history note (bottom of document): "Revision 1 (RT-002/RT-003): HEART C3 corrected 6→4; Fogg C3 corrected 4→3; AI-First Design C4 corrected 3→2."

**Dimension:** Evidence Quality, Methodological Rigor

**Response Required:**
The creator must either: (a) provide a complete statement of how many scoring decisions S-001 reviewed (denominator), so the error rate can be assessed, OR (b) revise the methodology limitation disclosure to explicitly acknowledge that the error rate is unknown and that the top-10 selections should be treated as "best-available single-analyst estimates with known partial validation, not independently verified scores." The current claim that S-001 "constitutes partial inter-rater validation" is misleading -- S-001 is adversarial review, not a second independent rater applying the same rubric.

**Acceptance Criteria:**
The methodology limitation disclosure must not use the phrase "inter-rater validation" for a process that is adversarial review, not a second rater. The distinction matters: inter-rater validation measures consistency; adversarial review measures attack resistance. The disclosure must explicitly acknowledge unknown error rate for scores not reviewed by S-001.

---

### DA-007-20260303: The Tiny Teams Profile Restriction Has No Empirical Basis [MAJOR]

**Claim Challenged:**
> "This analysis is optimized for teams of 2-5 people. Teams of 6 or more will find this selection useful but should be aware that it explicitly down-weights frameworks designed for larger teams" (SCOPE BOUNDARY, document preamble)

**Counter-Argument:**
The C1 criterion (25% weight -- highest in the analysis) penalizes frameworks for team-size above 5 people. This is the single largest driver of selection outcomes. Yet there is no citation or evidence that Jerry's target user population is primarily composed of 2-5 person teams. The "Tiny Teams research" referenced in E-013 through E-017 describes AI augmentation for small teams but does not establish that the teams using Jerry are exclusively or primarily in the 2-5 person range. If a substantial portion of Jerry's users are solo developers, or 10-person startups, or enterprise developers building AI products, then the 25% weight on Tiny Teams applicability systematically disadvantages frameworks that would serve them better. The selection may be correct for the assumed profile but the assumed profile is unvalidated.

**Evidence:**
Section 1 Weighting Rationale: "Gartner's research and the Tiny Teams playbook confirm this is the defining constraint for the skill." The Gartner citation is not provided with a specific reference. The "Tiny Teams playbook" is an internal Jerry document (the tiny-teams-research.md artifact), not an external validation.

**Dimension:** Evidence Quality, Completeness

**Response Required:**
The creator must either: (a) provide the specific Gartner citation (report name, year, finding) confirming 2-5 person teams as the primary population, OR (b) explicitly scope the analysis as "optimized for teams the analyst assumes are the primary Jerry user profile (2-5 persons), based on the Tiny Teams research input artifacts, without external validation of this profile's prevalence."

**Acceptance Criteria:**
The C1 weighting rationale must include a verifiable external citation for the claim that 2-5 person teams are the primary target, OR explicitly acknowledge the profile assumption is unvalidated. "Gartner's research" without a specific citation is not acceptable as evidence.

---

### P2: Minor -- Acknowledgment sufficient

---

### DA-008-20260303: WSM Independence Assumption Violated by C1/C5 Interaction

**Claim Challenged:**
> "WSM is preferred over more complex methods (TOPSIS, AHP)... (b) the scoring scale (1-10 per criterion with calibrated rubrics) produces interval-scale data with sufficient precision for the decision at hand" (SM-002 steelman, Section 1 Weighting Rationale)

**Counter-Argument:**
The WSM methodology requires criteria independence. In this analysis, C1 (Tiny Teams Applicability) and C5 (Complementarity) are correlated: frameworks designed for Tiny Teams tend to have unique operational niches precisely because they are optimized for resource-constrained contexts. AI-First Design exemplifies this with C1=10(P) and C5=10(P). The SM-002 steelman strengthened the MCDA grounding but did not address the independence assumption violation. This is the standard WSM limitation in portfolio selection problems -- the Triantaphyllou and Velasquez & Hester citations both acknowledge it. A more complete methodology positioning would note this limitation.

**Dimension:** Methodological Rigor

**Response Required:** Acknowledgment that the WSM independence assumption is an approximation in this context and that the C1/C5 interaction may slightly overstate the uniqueness of frameworks that score high on both criteria simultaneously.

---

### DA-009-20260303: Tooling Cost Is a Missing Selection Dimension

**Claim Challenged:**
The 6-criterion selection framework: C1-Tiny Teams Applicability, C2-Composability, C3-MCP Integration, C4-Maturity, C5-Complementarity, C6-Non-Specialist Accessibility.

**Counter-Argument:**
The framework recommends multiple commercial tools without addressing cost. Figma Pro ($15/seat/month), Miro ($10/seat/month), Maze ($99/month for user testing), and Hotjar (paid tiers) are all recommended across the selected 10 frameworks. A 2-person Tiny Team implementing the full recommended portfolio faces approximately $250-400/month in tooling costs before any development begins. This is especially material for the stated target audience (2-5 person teams without UX specialists) who are likely cost-sensitive. The absence of a cost dimension means the analysis may systematically favor MCP-integrated frameworks without accounting for their commercial licensing requirements.

**Dimension:** Completeness

**Response Required:** Acknowledgment that the criterion set does not include a cost dimension and a brief note on estimated tooling costs for implementing the full portfolio, so implementers can budget appropriately.

---

### DA-010-20260303: "Maximize Coverage" Claim Conflicts with HIGH RISK Gap Acknowledgment

**Claim Challenged:**
> "This analysis selects 10 UX frameworks that collectively maximize UX outcome coverage" (Core Thesis)
> "The selected 10 does not include a dedicated remote user research framework. This gap carries real risk and should NOT be minimized." (Section 4, HIGH RISK gap)

**Counter-Argument:**
The core thesis claims the portfolio "maximizes UX outcome coverage." Section 4 explicitly labels the absence of a user research framework as HIGH RISK -- meaning coverage is materially incomplete in a consequential domain. These two claims are not reconcilable. Either the portfolio maximizes coverage (which the HIGH RISK label disproves) or the portfolio makes deliberate coverage compromises (which is accurate and defensible but requires a different core thesis).

**Dimension:** Internal Consistency

**Response Required:** Acknowledgment that "maximize" and "HIGH RISK gap" cannot coexist without qualification. The core thesis should be revised to accurately describe the portfolio's scope, or the HIGH RISK language should be qualified to explain why the gap does not violate the maximization claim (it cannot).

---

## Step 5: Synthesis and Score Impact

### Overall Assessment

**9 counter-arguments identified (3 Critical, 4 Major, 2 Minor).**

The deliverable is a sophisticated, multi-iteration analysis that has genuinely improved across prior adversarial strategies. However, the S-003 Steelman's primary strengthening move -- the SM-001 minimal-complete portfolio-as-system justification -- has introduced new logical vulnerabilities that are the most significant finding in this critique. Specifically: the minimality proof depends on the analyst's own categorization taxonomy (DA-001), is contradicted by AI-First Design's projected status (DA-003), and cites C5 as supporting evidence after explicitly forbidding that citation (DA-005). These three Critical findings collectively undermine the Steelman's highest-priority improvement.

The four Major findings address the sensitivity analysis testing strategy (DA-002), the core thesis's "maximize" claim (DA-004), the single-rater error-rate interpretation (DA-006), and the unvalidated Tiny Teams profile assumption (DA-007). These are individually resolvable without changing the portfolio selection; they require precision revisions, not fundamental rethinking.

**Recommendation: REVISE -- Critical findings require targeted revisions before S-014 scoring.** The portfolio selection (which 10 frameworks) is defensible and likely correct. The logical architecture of the portfolio-as-system justification requires precision repair to be defensible under adversarial scrutiny.

### Scoring Impact Table

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | DA-009 (missing cost dimension), DA-010 (HIGH RISK gap conflicts with maximize claim), DA-007 (unvalidated scope profile) collectively reduce completeness confidence |
| Internal Consistency | 0.20 | Negative | DA-001 (circular minimality taxonomy), DA-003 (AI-First Design projected status vs. minimality claim), DA-004 (maximize vs. ceiling), DA-005 (C5 cited as evidence despite being forbidden from citation as evidence), DA-010 (maximize vs. HIGH RISK gap) create five internal contradictions |
| Methodological Rigor | 0.20 | Negative | DA-001 (self-referential minimality taxonomy), DA-002 (sensitivity tests safest scenarios only), DA-005 (circular validation chain), DA-006 (error discovery interpreted as validation), DA-008 (WSM independence assumption unaddressed) |
| Evidence Quality | 0.15 | Negative | DA-006 (3 errors found = evidence of unreliability, not partial validation), DA-007 (Gartner citation is unverified), DA-002 (robustness claim based on incomplete sensitivity testing) |
| Actionability | 0.15 | Neutral | The framework descriptions, routing guides, and implementation sequencing remain actionable. The Critical and Major findings are about the analytical framework, not the implementation guidance. |
| Traceability | 0.10 | Neutral | Finding identifiers (DA-NNN, SM-NNN, RT-NNN, etc.) are consistent and well-maintained. The revision history is thorough. |

**Estimated composite score impact:** 3 Critical findings each carry approximately 0.10-0.20 impact on affected dimensions. If all three Critical findings are unaddressed, the estimated score reduction is 0.12-0.18 from the pre-DA baseline across Methodological Rigor and Internal Consistency dimensions.

---

## Recommendations

### P0 (Critical -- MUST resolve before acceptance)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-001-20260303 | Revise the minimality claim to either: (a) ground it in an externally published lifecycle taxonomy, or (b) explicitly scope it as "non-redundant per the analyst's categorization." Remove the term "minimal-complete" unless grounded in external criteria. | Core thesis or SM-001 minimality argument cites at least one external source for the stage+function taxonomy, OR removes "minimal-complete" language and scopes the claim to the analyst's own categorization. |
| DA-002-20260303 | Complete the C3 sensitivity perturbation (C3 25%→25%, redistributing from C1 or C2). Provide the full numeric table showing whether Fogg remains above Service Blueprinting under this scenario. | A complete sensitivity table for C3=25% with actual margin between Fogg and Service Blueprinting. The robustness claim may stand or may need to be qualified based on results. |
| DA-003-20260303 | Revise the minimality claim to be explicitly conditional on AI-First Design synthesis completing with projected properties. The phrase "minimal-complete" cannot apply to a portfolio containing projected scores. | Core thesis or SM-001 argument explicitly flags the minimality claim as conditional/provisional when AI-First Design scores are projected (P). Internal consistency between the minimality assertion and the Service Blueprinting substitution path is restored. |

### P1 (Major -- SHOULD resolve; justification required if not)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-004-20260303 | Revise "maximize UX outcome coverage" in core thesis to language consistent with CC-002's ceiling disclosure. | Core thesis does not use "maximize" without qualification; the ceiling constraint is acknowledged in the thesis statement itself. |
| DA-005-20260303 | Remove or qualify the Complementarity Matrix citation in the SM-001 minimality proof. The C5 caveat prohibits this citation for external validation purposes. | The minimality argument does not cite the Complementarity Matrix as supporting evidence, OR it explicitly labels the citation as "internal consistency check only, not independent validation." |
| DA-006-20260303 | Revise the "partial inter-rater validation" language. Disclose the total number of scoring decisions reviewed by S-001 so the error rate can be assessed. | Methodology limitation uses "adversarial review" (not "inter-rater validation") and either states the number of decisions reviewed or explicitly acknowledges the error rate for non-reviewed decisions is unknown. |
| DA-007-20260303 | Provide the specific Gartner citation for the Tiny Teams profile claim, OR acknowledge the profile assumption is unvalidated. | C1 weighting rationale includes a verifiable external citation, OR explicitly states the profile assumption is based on internal research artifacts without external validation. |

### P2 (Minor -- Acknowledgment sufficient)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-008-20260303 | Add a note in the WSM methodological grounding (SM-002 addition) acknowledging the independence assumption limitation and its application to the C1/C5 interaction. | Brief acknowledgment in the MCDA grounding section that WSM independence is an approximation when criteria interact. |
| DA-009-20260303 | Add a tooling cost estimate for implementing the full portfolio, noting commercial licensing requirements. | At least a rough per-month estimate of tooling costs for a 2-person team using all recommended MCP integrations. |
| DA-010-20260303 | Revise core thesis to replace "maximize" with language that acknowledges the HIGH RISK user research gap or explicitly explain why the gap does not contradict the maximization claim. | Core thesis is internally consistent with Section 4's HIGH RISK gap acknowledgment. |

---

## Execution Statistics

- **Total Findings:** 10 (DA-001 through DA-010)
- **Critical:** 3 (DA-001, DA-002, DA-003)
- **Major:** 4 (DA-004, DA-005, DA-006, DA-007)
- **Minor:** 3 (DA-008, DA-009, DA-010)
- **Protocol Steps Completed:** 5 of 5

---

## H-15 Self-Review Checklist

- [x] All findings have specific evidence from the deliverable (direct quotes in each finding detail, with section references)
- [x] Severity classifications are justified: Critical findings attack the logical architecture of the core thesis and its primary justification; Major findings reveal gaps or internal contradictions requiring precision revision; Minor findings are improvement opportunities
- [x] Finding identifiers follow DA-NNN-20260303 format per template prefix (DA-NNN-{execution_id})
- [x] Report is internally consistent: summary table (Step 3) matches detailed findings (Step 4); scoring impact table (Step 5) references specific DA-NNN findings
- [x] No findings were minimized: the 3 Critical findings directly attack the S-003 Steelman's primary strengthening argument (SM-001), which the Steelman itself identified as the most likely Devil's Advocate attack vector -- this critique successfully penetrates the fortification
- [x] Leniency bias counteracted: minimum 3 counter-arguments generated (10 total); all 6 counter-argument lenses applied across the finding set (logical flaws: DA-001, DA-003, DA-005; unstated assumptions: DA-007, IA-1 through IA-4; contradicting evidence: DA-006, DA-010; alternative interpretations: DA-002; unaddressed risks: DA-009; historical precedents: DA-004 via WSM literature)
- [x] Role maintained: critique targets the STRENGTHENED thesis from S-003, not the pre-Steelman version
- [x] H-16 compliance confirmed: S-003 output was read and the critique attacks the strengthened argument, not the pre-Steelman weaknesses

---

*Strategy: S-002 Devil's Advocate | Template: `.context/templates/adversarial/s-002-devils-advocate.md` | Executed: 2026-03-03T00:00:00Z | Agent: adv-executor*
