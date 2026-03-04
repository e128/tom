# Devil's Advocate Report: UX Framework Selection — Weighted Multi-Criteria Analysis (Revision 9)

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 9)
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied 2026-03-03 (confirmed — report at `projects/PROJ-020-feature-enhancements/work/analysis/tournament-iter5/s-003-steelman.md`)

---

## Summary

9 counter-arguments identified (0 Critical, 5 Major, 4 Minor). The deliverable has no Critical vulnerabilities — its core scoring methodology and selection logic are internally coherent. However, five Major findings reveal substantive gaps that a serious challenger must engage with: the C5 self-reference problem is more severe than the document acknowledges (the document's own acknowledgment of C5 as a "consistency check, not external validation" undermines the non-redundancy claim it relies on as a primary selection defense); the AI-First Design inclusion violates the very selection methodology the analysis establishes; the 10-framework ceiling is admitted to be analyst-assumed but its implications for the non-redundancy claim are never confronted; the "Tiny Teams" definition is narrow in ways that may make most findings inapplicable to the Jerry target user population; and the wave sequencing plan embeds a hidden dependency ordering problem that the analysis does not model. Recommendation: **REVISE** — the Major findings are addressable without structural changes to the selection, but they require substantive additions to the methodology section and the implementation specification.

---

## Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-I5 | C5 self-reference undermines the non-redundancy claim as a structural defense | Major | "C5 scores are portfolio-conditional by design — they measure a framework's marginal contribution to the selected portfolio assuming the other high-scoring frameworks are already included... C5 self-referentiality is methodologically appropriate for portfolio optimization but should not be cited as external evidence of selection quality." (Section 1, line 130-131) | Methodological Rigor |
| DA-002-I5 | AI-First Design inclusion violates the document's own selection standards | Major | "All scores for AI-First Design are PROJECTED PREDICTIONS about a framework-to-be-synthesized, not measurements of an existing framework's properties." (Section 3.8, line 840); Maturity C4=2 vs. minimum 8 for all other selected frameworks | Internal Consistency |
| DA-003-I5 | The "Tiny Teams" population is too narrowly defined to support the generalizability implied by the analysis | Major | "optimized for teams of 1-5 persons building AI-augmented software products in 2026" (line 3); "Teams of 6 or more will find this selection useful but should be aware that it explicitly down-weights frameworks designed for larger teams" (SCOPE BOUNDARY notice, line 24) | Evidence Quality |
| DA-004-I5 | The wave sequencing plan's dependency chain is brittle in a specific, unmodeled failure mode | Major | Wave 1 criteria-gate: "/ux-jtbd has produced at least one job statement the team has used to inform a product decision" — but the document never addresses what happens when a team's first Design Sprint conclusion contradicts or supersedes the JTBD job statement produced in Wave 1 | Actionability |
| DA-005-I5 | The symmetric uncertainty disclosure overstates the protection it provides | Major | "Under +/-0.25 uncertainty, Fogg or Kano MAY be displaced by Service Blueprinting (downward scenario)... The correct operational guidance is: all four frameworks (Fogg, Kano, Service Blueprinting, Double Diamond) are defensible choices whose relative ordering cannot be determined within the scoring methodology's precision." (Section 1, lines 203-212) — but the document then selects Fogg and Kano as final selections without resolving the uncertainty it just described | Evidence Quality |
| DA-006-I5 | The 10-framework ceiling assumption is unexamined in its interaction with the minimality claim | Minor | "The 10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions, not a user-specified requirement." (CC-002, line 28) — if the ceiling is raised to 11, Service Blueprinting enters and the minimality argument must be re-evaluated | Completeness |
| DA-007-I5 | The criterion-weight justification for C1 (25%) rests on analyst judgment presented as research-grounded | Minor | "the 25% weight reflects analyst judgment that team-size fit is the primary gate to all other selection dimensions. This is analyst judgment, not externally prescribed" (Section 1, line 183) | Methodological Rigor |
| DA-008-I5 | The UX failure mode coverage validation is circular with the selection | Minor | "This validation inverts the selection logic and tests the portfolio from the outcome side rather than the criteria side." (Section 1, line 356) — but the failure modes were presumably known when frameworks were selected, so the validation cannot be independent | Internal Consistency |
| DA-009-I5 | The HEART Framework's C3 correction from 6→4 creates a hidden criterion calibration problem | Minor | "C3 corrected from 6→4 per RT-002: Hotjar integration is Bridge MCP, not Native" (Score Calculation Verification, line 442) — but HEART scored 8.30 and remains #4 despite this major C3 change, indicating C3 has low effective discriminating power that the analysis does not address explicitly in the context of this specific correction | Traceability |

---

## Detailed Findings

### DA-001-I5: C5 Self-Reference Undermines the Non-Redundancy Claim as a Structural Defense [MAJOR]

**Claim Challenged:** The analysis uses the non-redundancy portfolio as a primary structural defense of the selection: "Verified non-redundancy: Each selected framework fills a distinct UX domain niche; no two selected frameworks provide the same capability (confirmed by C5 complementarity criterion and two-pass portfolio evaluation)." (Core Thesis, line 6)

**Counter-Argument:** The document explicitly and correctly acknowledges that C5 scores are portfolio-conditional: "C5 scores... should not be cited as external evidence of selection quality." (Section 1, line 131). But the Core Thesis bullets — the most-read portion of the document — cite C5 as confirming non-redundancy without this qualification. The steelman (SM-002) attempted to strengthen the minimality claim by citing three independent structural properties (cadence orthogonality, output differentiability, C5 portfolio-composition test). But the third property — the C5 portfolio-composition test — is tautologically self-referential. And the first two properties (cadence orthogonality, output differentiability) apply only to the Design Sprint / Lean UX pair, not to the full 10-framework selection. The broader non-redundancy claim across all 10 frameworks still rests primarily on C5 — which the document itself says is not external validation.

The implication: if a challenger starts from a different anchor set (e.g., selects Double Diamond first, then JTBD, then Lean UX), they could construct a similarly internally-consistent C5-scoring non-redundant portfolio that shares only 5 or 6 of the 10 frameworks with this analysis's selection. The document provides no evidence that would allow distinguishing between these two equally internally-valid portfolios. The non-redundancy claim is not independently validated; it is a consistency property of the specific selection, not a property of the frameworks themselves.

**Evidence:** Section 1, Complementarity Methodology Caveat (line 130): "C5 scores DO NOT provide independent validation of the selection; they are a consistency check confirming that the chosen set is non-redundant given the choices already made." The MINIMALITY CLAIM QUALIFICATION notice (line 22) further acknowledges that "A skeptic could categorize Design Sprint (#2) and Lean UX (#5) as sharing the same stage (Design) and primary function (iterative product development)."

**Impact:** If this counter-argument is valid, the "Verified non-redundancy" bullet in the Core Thesis is misleading. The selection is "internally consistent non-redundant" rather than "externally validated non-redundant." For a practitioner choosing between this portfolio and an alternative, the non-redundancy claim provides no comparative guidance.

**Dimension:** Methodological Rigor

**Response Required:** The Core Thesis bullet should be rewritten to accurately reflect what C5 confirms: "Internally consistent non-redundancy: the selected portfolio is self-consistent — removing any framework creates a gap in the portfolio's coverage given the specific frameworks selected. External validation of non-redundancy requires cross-portfolio comparison against alternative selections with the same methodology."

**Acceptance Criteria:** The Core Thesis non-redundancy bullet uses "internally consistent" rather than "verified" as the qualifier, and explicitly notes C5's self-referential nature. Alternatively, the document adds a cross-portfolio comparison demonstrating that at least one alternative 10-framework portfolio produces a lower C5 total across all selected frameworks — making external non-redundancy a verifiable claim.

---

### DA-002-I5: AI-First Design Inclusion Violates the Document's Own Selection Standards [MAJOR]

**Claim Challenged:** AI-First Design (rank #8, score 7.80P) is presented as a legitimate selection with the defense: "The selection of Option 1 is accepted with full transparency: the maturity score is 2/10 (the lowest in the selected set), the prerequisite is explicit, and the sensitivity analysis confirms this is the most weight-stable selection." (Section 3.8, line 834)

**Counter-Argument:** The analysis's own criterion definitions make AI-First Design's inclusion indefensible by the scoring methodology as applied to all other 39 frameworks. C4 (Maturity, 15% weight) is scored 2/10 for AI-First Design. The C4 rubric states: "1-2: Framework is very new (<2 years), has no authoritative source, is still being defined, or is declining/deprecated." AI-First Design is not just new — it has no authoritative source, has never been applied, and has not been codified. It is a framework-to-be-created, not a framework being evaluated. Every other framework in the 40-framework candidate universe, including all 10 selected frameworks, is being evaluated as an existing artifact. AI-First Design is being scored as a prediction about a future artifact.

The document's own scoring methodology is explicit: C1 and C2 scores for AI-First Design are "predictions about what the synthesized framework will achieve if the synthesis deliverable succeeds." This is categorically different from scoring an existing framework. The WSM formula produces 7.80(P) by applying real-weight arithmetic to hypothetical inputs. If a practitioner applied the same approach to *any* unbuilt framework by optimistically assigning C1=10, C2=8, C3=8, and C5=10, they could justify including virtually any claimed framework.

The existence of a C4=2 score is not a sufficient hedge: a C4=2 score implies the framework at least exists as a 2-year-old emerging framework. AI-First Design does not even meet this threshold. The honest C4 score for a non-existent synthesized framework is 0 or null — there is no score that can be assigned to a framework that does not exist.

**Evidence:** Section 3.8 (line 840): "All scores for AI-First Design are PROJECTED PREDICTIONS about a framework-to-be-synthesized, not measurements of an existing framework's properties." The C4 rubric (Section 1, line 112-114): scoring scale starts at 1-2 for frameworks that exist but are very new. The candidate universe scope (Section 1, line 52): "The universe is not claimed to be exhaustive... Frameworks that are purely theoretical... were excluded at the universe-generation stage."

**Impact:** If this counter-argument is valid, AI-First Design's inclusion creates a methodological inconsistency that undermines the scoring matrix's authority. The 40-framework scoring exercise purports to evaluate existing frameworks against measurable criteria. Inserting a non-existent framework with projected scores violates this premise. A reader who notes this inconsistency may reasonably discount the entire selection matrix as having been designed to produce a pre-determined outcome (include AI-First Design regardless of its current state).

**Dimension:** Internal Consistency

**Response Required:** The analysis must choose one of two defensible positions: (A) AI-First Design is treated as a conditional slot, not as a scored selection — remove it from the WSM table entirely and replace with "AI UX Domain (TBD — to be filled by AI-First Design synthesis or Service Blueprinting at implementation time)"; OR (B) AI-First Design is retained with an explicit methodological note that it is being evaluated as a *scope gap* rather than a *framework score*, and its rank (#8) should be interpreted as "this domain gap ranks #8 in priority for a synthesized framework" not "this framework scores 7.80 on the selection criteria."

**Acceptance Criteria:** Either (A) the WSM table removes AI-First Design from the scored rows and adds a footnote explaining the AI UX domain gap and its resolution path, or (B) the document adds an explicit "conditional slot" methodology section that distinguishes AI-First Design's evaluation basis from all other 39 frameworks and removes the "(P)" notation in favor of a distinct visual treatment (e.g., italic or separate row).

---

### DA-003-I5: "Tiny Teams" Population Is Too Narrowly Defined to Support the Generalizability Implied [MAJOR]

**Claim Challenged:** "The selection is optimized for teams of 1-5 persons building AI-augmented software products in 2026." (line 3) — The analysis proceeds as if this population is well-understood and measurable.

**Counter-Argument:** The "Tiny Teams" population label is used throughout the analysis as the primary justification for C1 weights (25%), specific framework selection decisions, and the entire implementation plan. But "teams of 1-5 persons building AI-augmented software products" covers an enormously heterogeneous population: a single developer building an LLM-powered note-taking app, a 5-person startup building an enterprise AI assistant, a 4-person design agency building a client's AI product, and a 3-person internal tools team at a 50-person company are all "Tiny Teams" by this definition. These teams have radically different UX challenges:

- The solo developer has no collaboration dynamics at all — Design Sprint requires "a team"
- The 5-person startup with users can run proper Kano surveys; the solo developer cannot
- The design agency has external clients whose approval gates all design decisions — none of the 10 sub-skills explicitly addresses client approval workflows
- The internal tools team has captive users for research and no market competition — frameworks optimized for market differentiation (Fogg, Kano) have lower relevance

The document's sensitivity analysis tests criterion-weight robustness but never tests population-segment robustness. A team of 1 person is fundamentally different from a team of 5 persons. C1 (Tiny Teams Applicability) treats this as a single dimension, but team size within the 1-5 range may be the most important segmentation variable for framework applicability — more important than any of the six explicit scoring criteria.

The SCOPE BOUNDARY notice (line 24) acknowledges teams of 6+ should look elsewhere but treats the 1-5 range as homogeneous. The C1 score definitions distinguish between "designed for 1-3 persons" (9-10) and "works well for small teams with adaptation" (7-8) — but the analysis population is defined as "1-5" making scores that are calibrated for "1-3" applicable to a 5-person team only approximately.

**Evidence:** Section 1 (line 63): "Teams smaller than 2 persons or larger than 5 should refer to the SCOPE BOUNDARY notice." The C1 score rubric (line 60-66) calibrates against "1-3 person teams" for top scores, creating a scale mismatch with the "1-5 person" target population. No sensitivity analysis tests what happens to the selection when the team size is 1 (solo) versus 5 (near-enterprise tiny).

**Impact:** If this counter-argument is valid, the analysis's selection is optimized for a specific subpopulation within "Tiny Teams" — likely 2-4 person teams with launched products and MCP tool access. Solo developers and 5-person teams may find the portfolio systematically suboptimal without additional guidance on segmentation-specific configuration.

**Dimension:** Evidence Quality

**Response Required:** Add a "Population Segment Variants" section (or subsection within Section 7.1) that specifies the primary target profile (e.g., "2-4 person product team with a launched or near-launch product") and notes where the selection diverges for edge cases: (a) solo developer (1 person): Design Sprint requires facilitation adjustment; Kano requires minimum viable user base; (b) 5-person team: most frameworks apply as-designed; (c) pre-launch teams: JTBD and Design Sprint are highest priority; Kano, HEART, Fogg require post-launch data.

**Acceptance Criteria:** Section 7 includes a table or subsection identifying at minimum two distinct Tiny Teams subprofiles (pre-launch/solo vs. post-launch/2-5 person team) and specifying which sub-skills are most relevant for each profile. The Core Thesis "optimized for teams of 1-5" language is qualified with a forward reference to these profiles.

---

### DA-004-I5: Wave Sequencing Plan Has a Brittle Dependency Chain in a Specific Unmodeled Failure Mode [MAJOR]

**Claim Challenged:** The Wave transition criteria (Section 7.4) specify: "Wave 1 → Wave 2: /ux-jtbd has produced at least one job statement the team has used to inform a product decision." (line 1386)

**Counter-Argument:** The wave sequencing plan treats JTBD (Wave 1) as a foundation that subsequent waves build on. But the analysis provides no guidance for the scenario where a subsequent wave's output contradicts the Wave 1 JTBD job statement — the most common failure mode of the JTBD-first sequencing pattern.

Here is the concrete failure scenario: A team completes Wave 1 JTBD, producing a job statement ("When I am reviewing code, I want to understand the AI's confidence level, so I can decide how much to trust its suggestion"). The team uses this job statement to inform a Wave 2 Lean UX hypothesis. The Wave 2 Lean UX cycle produces data showing users' actual primary pain point is the AI's explanation quality, not its confidence communication — invalidating the job statement's framing. The team is now in Wave 3, having committed their design direction (via Wave 1 JTBD) to a job framing that the Lean UX data contradicts.

The document recognizes this issue implicitly in the complementarity matrix: "JTBD (#6) → Design Sprint (#2): Job statement becomes the Sprint challenge statement." If the Sprint results contradict the job statement, the team faces a decision the analysis never addresses: retroactively revise the job statement (requiring re-validation), pivot the Sprint challenge statement (breaking traceability), or proceed with known tension between the job statement and the Sprint finding.

The Wave bypass/stall recovery protocol (Section 7.4, line 1394) addresses failure to meet readiness criteria but does not address the case where readiness criteria are met but subsequent waves produce contradicting data.

**Evidence:** Wave transition criteria (Section 7.4, line 1382-1390): the criteria specify when to advance but not what to do when later-wave outputs contradict earlier-wave anchors. The integration path table (Section 4, line 1137): "JTBD (#6) → Design Sprint (#2): Job statement becomes the Sprint challenge statement" — this integration assumes the job statement persists as valid through the Design Sprint, which may not hold.

**Impact:** If this counter-argument is valid, the wave sequencing plan will produce a specific failure mode for teams that faithfully follow it: they will reach Wave 3-4 with a committed design direction anchored to a Wave 1 job statement that subsequent waves have implicitly invalidated. The analysis's emphasis on JTBD as Wave 1's "foundational" skill makes this failure mode more likely, not less.

**Dimension:** Actionability

**Response Required:** Add a "Revision trigger" row to the Wave Transition Criteria table specifying: when a later-wave output contradicts a foundational Wave 1 output (JTBD job statement or heuristic evaluation findings), the team MUST create a revision worktracker task, document the contradiction explicitly, and either (a) update the earlier output and re-evaluate subsequent decisions, or (b) accept the contradiction with documented rationale. The analysis should specify that job statements are living artifacts, not stable foundations, and that the Build-Measure-Learn cycle may require revisiting pre-design conclusions.

**Acceptance Criteria:** Section 7.4 includes at least one sentence explicitly stating that JTBD job statements from Wave 1 are subject to revision when Wave 2+ evidence contradicts them, and specifying the revision process. A "Revision-Driven Backward Pass" row is added to the wave transition table or referenced as an explicit workflow.

---

### DA-005-I5: Symmetric Uncertainty Disclosure Overstates the Protection It Provides [MAJOR]

**Claim Challenged:** "The symmetric uncertainty analysis provides the full bidirectional picture" (Section 1, line 203) — The document presents the ±0.25 uncertainty analysis as adequate coverage of boundary uncertainty.

**Counter-Argument:** The ±0.25 uncertainty band is asserted without derivation from inter-rater reliability data. The document states the band is from "Single-rater scores carry +/-0.25 uncertainty" (Core Thesis, line 8) but never explains where 0.25 comes from. Is this a standard deviation from prior single-rater WSM studies? An analyst estimate? A value chosen because it produces a convenient compression zone description?

If the ±0.25 figure is arbitrary (or optimistic), the symmetric uncertainty analysis fails in two ways. First, it may understate the uncertainty: an actual inter-rater reliability study of multi-criteria UX framework evaluation would likely show disagreement exceeding 1 point on individual criteria for emerging or ambiguous frameworks (JTBD's C2 composability score, for example, is plausibly anywhere from 7-10 depending on whether one evaluates the Christensen school or the Ulwick ODI variant). If the real uncertainty band is ±0.50 per criterion, the WSM uncertainty propagates to roughly ±0.15 on the total score — meaning Service Blueprinting (7.40) and Double Diamond (7.45) may legitimately compete with Fogg (7.60) and Kano (7.65) for inclusion, not just under the ±0.25 scenario.

Second, the uncertainty band applies to all criteria equally, but the analysis acknowledges that criteria differ in their measurability: C4 (Maturity) is relatively objective (years in use, book publications, certifications) while C1 (Tiny Teams Applicability) and C2 (Composability) are highly subjective assessments based on analyst judgment. Applying a uniform ±0.25 band across all criteria ignores the heteroscedastic nature of the uncertainty — C1 and C2 uncertainty is likely larger than C4 uncertainty.

**Evidence:** FM-001 Disclosure (Section 1, line 192): "The detection of 3 scoring errors through adversarial review is evidence that the adversarial process functions as a quality control mechanism — it is NOT evidence that the remaining scores are error-free." The ±0.25 value is stated without derivation in the Core Thesis (line 8) and used throughout without justification. No reference to inter-rater reliability studies or calibration methodology is provided for the ±0.25 figure.

**Impact:** If the ±0.25 figure is optimistic, the "well-supported judgment calls" framing in the compression zone may be over-confident. A practitioner who takes the uncertainty band at face value may not appreciate that the true uncertainty in ranks 7-12 may require treating the full ranks 7-15 range as effectively undifferentiated — in which case 5-8 frameworks in the bottom of the selected set are arbitrary rather than well-supported.

**Dimension:** Evidence Quality

**Response Required:** Add a derivation or citation for the ±0.25 uncertainty figure: either (a) cite a methodology reference specifying that single-rater WSM on qualitative criteria carries ±0.25 uncertainty (if such a reference exists), or (b) re-characterize the ±0.25 as an "analyst calibration estimate" and provide the reasoning (e.g., "Based on the 3 scoring errors detected in adversarial review, which produced corrections of 0.05-0.20 points on weighted totals, ±0.25 is a conservative upper bound for rater error in this scoring context").

**Acceptance Criteria:** The FM-001 disclosure or the symmetric uncertainty analysis section includes either a literature citation for ±0.25 or an analyst-derived explanation of why ±0.25 is the appropriate uncertainty estimate for this specific scoring context. The explanation distinguishes between higher-uncertainty subjective criteria (C1, C2) and lower-uncertainty objective criteria (C4).

---

### DA-006-I5: 10-Framework Ceiling Assumption Is Unexamined in Its Interaction with the Minimality Claim [MINOR]

**Claim Challenged:** The 10-framework ceiling is noted as an analyst assumption (CC-002, line 28), but the analysis does not examine how raising this ceiling interacts with the minimality claim.

**Counter-Argument:** The minimality claim in the Core Thesis states "each framework fills a unique lifecycle niche." But Service Blueprinting (rank #12) and Cognitive Walkthrough (rank #17) are explicitly named as closing "documented gaps" (CC-002, line 28). If the portfolio has documented gaps at 10 frameworks, then 10 is not the minimal complete portfolio — it is the constrained-by-assumption portfolio. Calling it "minimal complete" at 10 while simultaneously documenting that 11 or 12 frameworks would close additional gaps creates a definitional tension: minimality and constraint cannot both be true simultaneously in the same logical framework.

**Evidence:** CC-002 (line 28): "Service Blueprinting and Cognitive Walkthrough close documented gaps if the ceiling is raised." Gap Analysis (Section 4): confirms service design and information architecture gaps exist. The V2 roadmap (Section 4) lists P1 items explicitly, confirming V1 is not complete even at its own scope.

**Dimension:** Completeness

**Response Required:** The document should clarify the intended meaning of "minimal" in the minimality claim: minimal given the 10-framework constraint (a constrained optimum), not minimal in the absolute sense (which would require closing all documented gaps).

**Acceptance Criteria:** The Core Thesis "verified non-redundancy" bullet or the MINIMALITY CLAIM QUALIFICATION notice explicitly states that "minimality" is relative to the 10-framework ceiling constraint, not an absolute claim about UX portfolio completeness.

---

### DA-007-I5: C1 Criterion Weight Justification Presents Analyst Judgment as Research-Grounded [MINOR]

**Claim Challenged:** "the 25% weight reflects analyst judgment that team-size fit is the primary gate to all other selection dimensions" (Section 1 Weighting Rationale, line 183), with citation to "tiny-teams-research.md research artifact (E-013 through E-017)."

**Counter-Argument:** The Weighting Rationale acknowledges "This is analyst judgment, not externally prescribed" for C1 at 25%. But it then immediately follows with "a practitioner prioritizing MCP integration over team-size fit could justifiably weight C3 higher" — presenting one alternative as if it is the only plausible deviation. A practitioner could equally justify C2 (Composability) at 25% instead of C1 — after all, a framework that cannot be operationalized as a Jerry skill is useless regardless of team size fit. Or C4 (Maturity) at 20% — after all, using immature frameworks in production introduces unquantifiable implementation risk.

The sensitivity analysis tests C1 reduction from 25% to 20% and C3 increase from 15% to 25% but does not test the case where C2 surpasses C1 in priority. If a practitioner weights C2 (Composability) at 25% and C1 at 20%, does the selection change? The document cannot answer this question because C2→25% was not included in the three sensitivity scenarios.

**Evidence:** Section 1 Sensitivity Analysis covers C1 (25%→20%), C2 (20%→15%), and C3 (15%→25%). The missing perturbation is C2 (20%→25%) with C1 reduced — the scenario where composability is the primary criterion rather than team-size fit. The C4 maturity perturbation is also untested.

**Dimension:** Methodological Rigor

**Response Required:** Either add a fourth sensitivity perturbation (C2=25% with C1 reduced to 20%) or explicitly explain why this perturbation is not informative. The "one alternative weighting" framing should acknowledge that multiple alternative weightings exist, not only the C3-priority variant.

**Acceptance Criteria:** The Weighting Rationale section includes either (a) a statement that at least two additional perturbation scenarios were considered and found to produce confirming results (with results documented), or (b) explicit acknowledgment that C2-priority weighting was not tested and the selection's robustness under that scenario is unknown.

---

### DA-008-I5: UX Failure Mode Coverage Validation Is Circular with the Selection [MINOR]

**Claim Challenged:** "This validation inverts the selection logic and tests the portfolio from the outcome side rather than the criteria side." (Section 1, line 356) — The failure mode coverage table is presented as independent validation.

**Counter-Argument:** The 7 UX failure modes listed in the coverage validation table (poor onboarding, confusing navigation, unclear error states, missing empty states, misaligned mental models, inaccessible core flows, building features nobody wants) are standard UX failure categories well-known to any UX practitioner. These categories were presumably known to the analyst before framework selection began. If the analyst knew these failure modes a priori, then frameworks were (possibly unconsciously) selected partly because they address these known failure modes — making the coverage validation circular.

A genuine out-of-sample validation would test the portfolio against UX failure modes not known to the analyst at selection time — new failure modes discovered post-selection through external sources. The current validation only demonstrates that the analyst selected frameworks that address the failure modes the analyst had in mind, which is not surprising.

**Evidence:** Section 1 (line 356-358): "By identifying the 7 most common UX failure modes in early-stage software products and mapping each to the frameworks that address it, this table provides empirical evidence that the selected set is not merely theoretically sound but operationally complete for its intended purpose." The claim of "empirical evidence" for operational completeness is the specific overclaim.

**Dimension:** Internal Consistency

**Response Required:** Remove the claim that the failure mode coverage validation provides "empirical evidence" of operational completeness. Replace with: "The failure mode coverage map demonstrates internal consistency between the selection criteria and the portfolio's intended coverage — it is not an independent validation. True operational completeness requires post-launch feedback from teams using the portfolio."

**Acceptance Criteria:** The failure mode coverage validation section does not use the phrase "empirical evidence" and does not claim "operational completeness" as a validated property. The section accurately characterizes the validation as a consistency check, not an independent test.

---

### DA-009-I5: HEART Framework's C3 Correction Creates a Hidden Criterion Calibration Problem [MINOR]

**Claim Challenged:** The note in the Score Calculation Verification (line 442) states that "Revision 1 (RT-002/RT-003): HEART C3 corrected 6→4" — a 33% reduction in HEART's MCP integration score.

**Counter-Argument:** HEART's C3 was corrected from 6→4 because Hotjar uses a Bridge MCP (via Zapier/Pipedream), not a Native MCP. The correction is correct. However, HEART's final score dropped only from an estimated 8.60 to 8.30 — still placing it at #4 with a substantial margin over frameworks at #5 and below. This robustness to a major C3 correction is not analyzed or explained.

The implicit question: if a 33% reduction in C3 (from 6 to 4) produces only a 0.30 point score change for HEART (8.60→8.30), then C3 has surprisingly low effective weight on HEART's total — less than its stated 15% weight would suggest. This happens because HEART's C1=9, C2=10, C4=8 mean it starts from a very high base, and C3 is only 15% of the total. But if C3 has this little impact on selection outcomes for frameworks with strong C1/C2, then C3's stated 15% weight may be functionally much lower than 15% in practice — a form of criterion weight deception where stated weights differ from effective weights.

**Evidence:** Score Calculation Verification (line 442): HEART C3 correction 6→4. Post-correction score 8.30 (Rank #4). Pre-correction implied score: 9×0.25+10×0.20+6×0.15+8×0.15+9×0.15+9×0.10 = 2.25+2.00+0.90+1.20+1.35+0.90 = 8.60. The FM-004 ceiling effect analysis (line 229) acknowledges that effective discriminating weight shifts toward C3 within the top 10, but does not analyze whether C3 corrections have been appropriately impactful on selection outcomes.

**Dimension:** Traceability

**Response Required:** The Score Calculation Verification note for HEART should include the pre-correction and post-correction scores (8.60→8.30) to make the correction impact visible. The FM-004 ceiling effect analysis should explicitly note that C3 corrections in the 6→4 range produce only 0.30-point total score changes for frameworks with high C1/C2, and confirm this is expected behavior consistent with the criterion weight design.

**Acceptance Criteria:** The HEART correction note includes both the pre-correction estimated score and the post-correction verified score, and a one-sentence explanation of why the correction impact (0.30 points) is appropriate given HEART's strong C1/C2 profile.

---

## Response Requirements

### P0: Critical Findings — MUST resolve before acceptance
*(None)*

### P1: Major Findings — SHOULD resolve; require justification if not

**DA-001-I5: C5 Non-Redundancy Claim Framing**
- Specific action: Rewrite Core Thesis non-redundancy bullet to say "internally consistent non-redundancy" rather than "verified non-redundancy"; add reference to C5 self-referential nature in the bullet itself or an adjacent note
- Acceptance criteria: The non-redundancy claim in the Core Thesis does not use "verified" without qualification; the C5 portfolio-conditional nature is referenced at point of claim

**DA-002-I5: AI-First Design Inclusion Methodology**
- Specific action: Adopt one of two approaches: (A) remove AI-First Design from scored WSM rows and treat as a conditional domain slot; OR (B) add explicit "conditional slot" methodology section distinguishing AI-First Design from the scored frameworks
- Acceptance criteria: A reader of the scoring matrix understands that AI-First Design's scores are projected, not measured, and that the WSM methodology as applied to the other 39 frameworks does not apply to AI-First Design in the same way

**DA-003-I5: Tiny Teams Population Segmentation**
- Specific action: Add a "Population Segment Variants" table (2-3 rows) to Section 7.1 covering: solo developer (1 person), small team pre-launch (2-3 persons), post-launch team (2-5 persons)
- Acceptance criteria: Each variant specifies which Wave to start from and which sub-skills are highest priority given the team's specific context

**DA-004-I5: Wave Sequencing Revision Protocol**
- Specific action: Add a "Revision-Driven Backward Pass" clause to Section 7.4 specifying what happens when later-wave findings contradict earlier-wave anchors
- Acceptance criteria: The Wave transition criteria section explicitly states that JTBD job statements are revisable and specifies the revision process

**DA-005-I5: Uncertainty Band Derivation**
- Specific action: Add a derivation or citation for ±0.25 to the FM-001 disclosure or the symmetric uncertainty analysis section
- Acceptance criteria: The ±0.25 is either (a) cited to a methodology reference or (b) explained as an analyst estimate with reasoning from observed correction magnitudes

### P2: Minor Findings — MAY resolve; acknowledgment sufficient

**DA-006-I5:** The document can acknowledge that "minimal" is relative to the 10-framework constraint; a sentence in the MINIMALITY CLAIM QUALIFICATION notice would suffice.

**DA-007-I5:** The document can note that the C2=25% perturbation was not tested and the selection's robustness under that scenario is unknown; a single sentence in the Sensitivity Analysis section would suffice.

**DA-008-I5:** Remove "empirical evidence" from the failure mode coverage validation description; replace with "internal consistency check."

**DA-009-I5:** Add pre-correction and post-correction scores for HEART in the Score Calculation Verification note.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Neutral-Negative | DA-006 identifies a minor gap in the minimality claim's scope qualifier. Other sections of the document are thorough. The net impact is small — the document is comprehensive, but has one unaddressed interaction (10-framework ceiling vs. minimality) that represents a completeness gap. |
| Internal Consistency | 0.20 | Negative | DA-002 (AI-First Design inclusion violates the scoring methodology's own premises) and DA-008 (circular validation) are genuine inconsistencies. DA-002 is the more significant: the scored framework paradigm is internally inconsistent with projecting scores for a non-existent framework. The inconsistency is acknowledged in the document but not resolved — the "full transparency" framing treats disclosure as resolution, which it is not. |
| Methodological Rigor | 0.20 | Negative | DA-001 (C5 self-reference undermines the non-redundancy claim) and DA-007 (C1 weight justification presents analyst judgment as research-grounded) both affect methodological rigor. The document's use of "verified" in the non-redundancy claim is directly contradicted by its own C5 methodology acknowledgment, which is a methodological rigor failure. |
| Evidence Quality | 0.15 | Negative | DA-003 (Tiny Teams population heterogeneity), DA-005 (uncertainty band lacks derivation). Both findings reduce confidence in the evidence quality claims. The ±0.25 band is used as a structural argument throughout the symmetric uncertainty analysis but is never derived from evidence — this is the most significant evidence quality gap. |
| Actionability | 0.15 | Negative | DA-004 (wave sequencing brittle dependency chain) directly reduces actionability. An implementer following the wave plan as written will encounter the backward-pass scenario without guidance. This is an actionability gap in an otherwise detailed implementation specification. |
| Traceability | 0.10 | Neutral | DA-009 is a minor traceability improvement (pre/post-correction scores should be visible). The overall traceability of the document is good — finding IDs are used consistently throughout. The impact is small. |

**Overall assessment:** Targeted revision required. 0 Critical findings. 5 Major findings, all addressable without structural changes to the selection. The core thesis (10-framework portfolio for Tiny Teams) remains defensible; the Major findings address methodological framing, consistency of claims with methodology, and implementation plan completeness. The Minor findings are presentation improvements. Estimated composite score impact from unaddressed Major findings: -0.04 to -0.08 on the S-014 dimensions most affected (Internal Consistency, Methodological Rigor, Evidence Quality).

---

## Execution Statistics
- **Total Findings:** 9
- **Critical:** 0
- **Major:** 5
- **Minor:** 4
- **Protocol Steps Completed:** 5 of 5

---

## H-15 Self-Review Checklist

- [x] All findings have specific evidence from the deliverable (section, line reference, and quote provided for each finding)
- [x] Severity classifications justified: 5 Major findings each address a substantive gap in methodology, consistency, evidence, or actionability that a challenger could exploit to reject the deliverable's claims; 4 Minor findings are improvements that do not block acceptance
- [x] Finding identifiers follow DA-NNN-I5 format (I5 = tournament iteration 5)
- [x] Summary table matches detailed findings (9 total, 0 Critical, 5 Major, 4 Minor)
- [x] No findings omitted or minimized: the deliverable was reviewed across all major sections including the scoring matrix, sensitivity analysis, coverage validation, implementation plan, and AI-First Design prerequisite specification
- [x] Leniency bias counteracted: the S-003 Steelman's identification of "zero Critical findings" was challenged; DA-002 (AI-First Design) and DA-001 (C5 self-reference) constitute substantive methodological challenges that the Steelman did not pre-empt despite SM-002 attempting to address the minimality claim specifically
- [x] Response requirements are specific, verifiable, and actionable — creator can act without guessing

---

*Strategy Execution Report: S-002 Devil's Advocate*
*Template: `.context/templates/adversarial/s-002-devils-advocate.md` v1.0.0*
*Deliverable: `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 9)*
*Executed: 2026-03-03 | Tournament Iteration: 5 (FINAL)*
*Finding Prefix: DA (from template Identity section)*
*H-16 Status: Compliant — S-003 Steelman applied before this execution*
