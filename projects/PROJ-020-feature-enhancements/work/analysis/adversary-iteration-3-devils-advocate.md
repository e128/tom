# Devil's Advocate Report: UX Framework Selection -- Weighted Multi-Criteria Analysis

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 2 -- post-Steelman)
**Criticality:** C3 (Significant -- framework selection governs production Jerry `/user-experience` skill implementation)
**Date:** 2026-03-02
**Reviewer:** adv-executor (S-002)
**H-16 Compliance:** S-003 Steelman applied 2026-03-02 (confirmed -- Steelman report at `adversary-iteration-2-steelman.md`; 9 improvements incorporated into Revision 2 deliverable)

---

## Summary

10 counter-arguments identified (2 Critical, 5 Major, 3 Minor). The deliverable is methodologically sophisticated and has been substantially strengthened through two prior adversarial iterations plus Steelman improvements. However, it contains a structural weight-validity problem that was acknowledged but not resolved (criteria weights cannot simultaneously be "necessary conditions" AND weighted contributors), a circular scoring methodology that the Steelman's portfolio-theory defense does not fully neutralize, and the AI-First Design inclusion is procedurally compromised in a way that the cost-comparison framing obscures rather than resolves. The core selection of frameworks #1-7 and #9-10 is defensible. Framework #8 (AI-First Design) and the scoring methodology's self-referential complementarity calculation remain the two pressure points that require substantive response.

**Recommendation:** REVISE -- address the 2 Critical findings before proceeding to S-014 scoring. The 5 Major findings require either substantive resolution or explicit acceptance of the limitation with a documented rationale. The core selection decision is sound but two methodological claims are currently untenable in their present form.

---

## Findings Summary

| ID | Finding | Severity | Section |
|----|---------|----------|---------|
| DA-001-20260302 | Dependency-chain weighting is internally self-contradictory | Critical | Section 1, Weighting Rationale |
| DA-002-20260302 | Complementarity scores are post-hoc rationalization, not independent measurement | Critical | Section 2, Scoring Matrix |
| DA-003-20260302 | AI-First Design violates the selection's own merit-based criteria regardless of cost-comparison framing | Major | Section 3.7 |
| DA-004-20260302 | "Tiny Teams" criterion is a narrative fit test, not a differentiating filter | Major | Section 1, Criterion 1 |
| DA-005-20260302 | Score compression makes rank-ordering statistically meaningless below rank 5 | Major | Section 2, Scoring Matrix |
| DA-006-20260302 | MCP category distinctions are meaningful for scoring but the Bridge MCP warning is applied inconsistently | Major | Sections 3.4, 3.5, 3.9 |
| DA-007-20260302 | Design Sprint at #1 (9.15) depends on a C1 score of 10 that is not defensible for a 5-day process | Major | Section 2, Score Calculation Verification |
| DA-008-20260302 | The "equal-weight discriminator" argument eliminates the sensitivity analysis's ability to demonstrate robustness | Minor | Section 1, Sensitivity Analysis |
| DA-009-20260302 | Double Diamond exclusion relies on a circular argument | Minor | Section 5.1 |
| DA-010-20260302 | The HIGH RISK user research gap disclosure undermines the framework's fitness-for-purpose claim | Minor | Section 4, Gap Analysis |

---

## Detailed Findings

### DA-001-20260302: Dependency-Chain Weighting is Internally Self-Contradictory [CRITICAL]

**Claim Challenged:**
> "The 25%/20%/15%/15%/15%/10% weighting is not arbitrary -- it embeds a principled logical ordering derived from the constraints of the context. Criteria 1 and 2 function as **necessary conditions**: a framework that fails either is disqualified regardless of its other merits. Criteria 3, 4, and 5 are **equal-weight discriminators** among frameworks that have already cleared the first two filters."
> — Section 1, Weighting Rationale [SM-002]

**Counter-Argument:**
If Criteria 1 and 2 are genuine necessary conditions -- meaning frameworks that fail either are "disqualified regardless of other merits" -- then they should function as HARD GATES, not as weighted contributors. A necessary condition either passes or fails; it does not contribute a weighted score of 2.50 or 2.00 out of 10 to a composite. The current scoring system gives partial credit on C1 and C2 to every framework, including frameworks that purportedly "fail" these criteria. This is not a dependency-chain logic -- it is a weighted average that happens to assign the highest two weights to the first two criteria. The Steelman's reformulation as "dependency-chain" is a rhetorical reframing of a conventional weight assignment, not a methodological distinction.

The concrete evidence of the contradiction: HEART Framework scores C1=9 and C2=10 -- both "passing" by any reasonable interpretation. Yet HEART also has a Bridge-MCP-only integration (C3=4). Under true necessary-condition logic, HEART would be evaluated as: "passed C1, passed C2, now we discriminate on C3/C4/C5." But that is not how the scoring works -- C1 and C2 contribute to the weighted total the same way C3-C6 do. A framework scoring 5/10 on C1 does not get "disqualified"; it gets a partial score of 1.25 contribution, which is a penalty, not a disqualification.

The impact: the "dependency-chain" defense of the weighting rationale is not falsifiable. ANY two highest-weight criteria can be retroactively framed as "necessary conditions" and ANY lower-weight criteria can be framed as "equal-weight discriminators." This makes the weighting argument unfalsifiable and therefore not a methodological justification -- it is a post-hoc narrative. The Steelman strengthened this argument rhetorically but did not resolve the logical contradiction.

**Evidence:**
Looking at the score matrix: AI-First Design scores C4=2/10 on Maturity (a "discriminator" criterion). Under the purported logic, AI-First Design cleared the "necessary conditions" (C1=10, C2=8) and then competed on discriminators. But the 2/10 on C4 reduces its weighted total by 1.50 * 0.15 = 0.225 points relative to a 10/10 -- it doesn't eliminate the framework. This is discriminator logic, not gating logic, which is correct -- but it means C1 and C2 are also discriminators, not gates. The "necessary conditions" framing misrepresents how the math actually works.

**Impact:** If the dependency-chain argument is not a genuine methodological distinction but a rhetorical one, the primary defense of the weighting scheme collapses to: "we assigned higher weights to criteria we care about more, and lower weights to criteria we care about less." That is a legitimate weighting approach -- but it is not the same as a "principled logical ordering derived from constraints," which is the claim the deliverable makes. The distinction matters for intellectual honesty and for the defensibility of the weighting under challenge.

**Dimension:** Internal Consistency

**Response Required:** The deliverable must choose one of two positions and commit:
1. C1 and C2 ARE genuine necessary conditions -- in which case the scoring system must implement a hard gate (frameworks scoring below a threshold on C1 or C2 are eliminated from ranking, and the weighted scores of C1/C2 do not contribute to remaining frameworks' totals)
2. C1 and C2 ARE the highest-weighted criteria -- in which case the "dependency-chain / necessary conditions" framing must be replaced with the accurate description: "C1 and C2 receive the highest weights because they are our primary selection priorities"

**Acceptance Criteria:** Either (a) a revised methodology implementing true hard gates for C1 and C2, with demonstration that the top 10 selection is unchanged, OR (b) revised weighting rationale text that accurately describes the weighting as priority-based rather than necessity-based, with no claim of logical gating behavior.

---

### DA-002-20260302: Complementarity Scores Are Post-Hoc Rationalization, Not Independent Measurement [CRITICAL]

**Claim Challenged:**
> "Complementarity is a portfolio-level criterion by definition -- it measures a framework's marginal contribution to the selected set given the other frameworks already in the portfolio... The portfolio-conditional evaluation used here is standard in multi-criteria portfolio selection theory (see Keeney & Raiffa, 1976; Belton & Stewart, 2002 MCDA frameworks)."
> — Section 1 [SM-005]; Section 2 note

**Counter-Argument:**
The Steelman defense claims that complementarity scoring is "portfolio-conditional by design" and cites MCDA portfolio selection theory as validation. This defense has a fatal circularity problem that the academic citation does not resolve.

The sequence of decisions in this analysis is: (1) Score all 40 frameworks on C1-C5. (2) Identify which frameworks are the "other high scorers." (3) Score each framework's complementarity "assuming the other high scorers are selected." (4) Use those complementarity scores as part of the calculation that determines which frameworks are the high scorers.

This is not "portfolio-conditional evaluation" in the MCDA sense. In legitimate MCDA portfolio optimization (Keeney & Raiffa, Belton & Stewart), complementarity is evaluated against an independently specified portfolio, or the portfolio optimization is solved simultaneously using a formal algorithm (integer programming, etc.). What this analysis does is different: it uses the complementarity scores to determine the portfolio, but evaluates complementarity based on the portfolio already being known. The result is that the selection confirms itself.

The concrete consequence: JTBD receives a complementarity score of 10/10 and Microsoft Inclusive Design receives 10/10 -- both "only frameworks" filling unique niches. But these scores were assigned AFTER the analyst already decided that JTBD and Microsoft Inclusive Design would be in the top 10. If either had scored lower on C1-C4, they would have been out of the competitive set, and another framework (say Service Blueprinting at 7.35) would have become "the only strategic discovery framework" or "the only ethical design framework," earning similar high complementarity scores. The complementarity score is not measuring an intrinsic property; it is measuring "we selected this framework and there is no other selected framework in its category."

The Steelman's chess-piece analogy ("value of a chess piece without knowing the position") makes the circularity sound principled, but chess piece valuation is done against an independently fixed board position, not against a board that was arranged by the valuation itself.

**Evidence:**
Double Diamond scores C5=5/10 (significantly redundant with Design Sprint/Lean UX). This low complementarity score is the primary reason it was cut (Section 5.1: "Critically low complementarity score (5/10) because Design Sprint and Lean UX together completely cover the same process territory"). But Design Sprint and Lean UX were selected partly BECAUSE they score high on complementarity in a set that doesn't include Double Diamond. If the analyst had started with Double Diamond instead of Design Sprint, the complementarity scores would have reshuffled: Double Diamond would be the process framework at 10/10, and Design Sprint would be "redundant" at 3/10. The selection self-validates its own choices through the complementarity criterion.

**Impact:** If complementarity scores are circular rather than independent measurements, then the "coherent non-redundant portfolio" claim is not evidence of selection quality -- it is tautological. The portfolio is non-redundant because the scoring method defines non-redundancy as the absence of other similar frameworks, which are excluded because they are redundant with the portfolio that was already determined by the process that uses redundancy as a selection criterion. This circularity does not make the selection wrong, but it means the complementarity scores should not be cited as independent validation of the selection's quality.

**Dimension:** Methodological Rigor

**Response Required:** The deliverable must either:
1. Acknowledge that complementarity scores are portfolio-conditional and therefore do not provide independent validation -- they are a consistency check, not an external test. The "empirical validation" claim must be qualified.
2. OR redesign the complementarity scoring to use a reference portfolio defined independently of the scoring process (e.g., "evaluated against a representative 5-framework baseline portfolio specified before scoring began").

**Acceptance Criteria:** Either (a) explicit acknowledgment that complementarity scores are self-referential and cannot serve as independent evidence of selection quality, with revision of the relevant claims, OR (b) a redesigned complementarity methodology with an independently specified reference portfolio.

---

### DA-003-20260302: AI-First Design Violates the Selection's Own Merit-Based Criteria Regardless of Cost-Comparison Framing [MAJOR]

**Claim Challenged:**
> "The selection of Option 1 is accepted with full transparency: the maturity score is 2/10 (the lowest in the selected set), the prerequisite is explicit, and the sensitivity analysis confirms this is the most weight-sensitive selection. These are not rationalizations -- they are the decision-makers' acknowledgment that a known cost is worth a known benefit."
> — Section 3.7 (SM-006 cost-comparison framing)

**Counter-Argument:**
The cost-comparison framing is rhetorically sophisticated but it smuggles a category violation into the analysis. The analysis is a framework SELECTION exercise: evaluating 40 candidate frameworks against 6 criteria and selecting the top 10. AI-First Design is not a framework that is being selected -- it is a framework that must be CREATED before it can be selected. The C4 maturity score of 2/10 assigned to AI-First Design is not evidence that it is an immature framework; it is evidence that the THING BEING SCORED DOES NOT EXIST YET.

This distinction matters: when the analysis assigns scores to Design Sprint, JTBD, or Nielsen's Heuristics, it is scoring real, existent, independently verifiable objects with track records, practitioner communities, and failure modes. When it scores "AI-First Design," it is scoring a PROSPECTIVE SYNTHESIS of three practitioner sources. The 10/10 scores on C1 (Tiny Teams Applicability) and C5 (Complementarity) are not measurements of an existing framework's properties -- they are predictions about the properties of a framework that has not been written yet. The analysis is comparing apples (existing frameworks) against an orange that will theoretically exist once someone grows the orange tree.

The cost-comparison argument (Option 1 vs. Option 2 vs. Option 3) reframes this as "which option has the best total cost" -- but this does not resolve the category problem. The question is not "should the AI product UX domain be addressed?" (it should). The question is "does including an unbuilt framework in a framework SELECTION analysis compromise the analysis's integrity?" It does, because every statement about AI-First Design's framework properties is speculation masquerading as measurement.

A specific example: the C1 score of 10/10 for Tiny Teams Applicability is justified as "Framework was designed for or is naturally optimized for 1-3 person teams; AI can automate 50%+ of its activities." But AI-First Design has not been designed yet. The analysis is predicting properties of a future artifact, not measuring properties of an existing one. If the synthesis deliverable, once written, turns out to have complex processes requiring UX specialist expertise, the C1=10 score is simply wrong -- and by the time anyone discovers this, the skill has already been scoped based on the selection.

**Evidence:**
Section 3.7: "Unlike the other 9 selected frameworks, AI-First Design does NOT have an authoritative, codified framework document." All other 39 frameworks in the competition are scored against their actual documented methodology. AI-First Design is scored against a future deliverable that will synthesize "Nudelman 'UX for AI' 2025, Adam Fard AI UX articles 2025-2026, NN Group AI interaction patterns 2026." The evidence for its scores is projective, not empirical.

**Impact:** If AI-First Design's scores are predictions rather than measurements, the analysis is not a 40-framework competition -- it is a 39-framework competition with one additional entry that received predicted scores. This does not necessarily mean AI-First Design should be excluded from a skill implementation plan. But it means including it in a scored selection matrix alongside existing frameworks misrepresents the nature of the comparison. The transparency notice is necessary but not sufficient -- it acknowledges the risk without resolving the methodological category violation.

**Dimension:** Methodological Rigor

**Response Required:** One of:
1. Remove AI-First Design from the scored selection matrix and address it separately as a "V1 skill development candidate" with a different evaluation framework appropriate for prospective framework synthesis.
2. OR retain AI-First Design in the selection but explicitly qualify all its scores as "projected scores contingent on synthesis deliverable achieving these properties" and add a validation gate: AI-First Design's sub-skill implementation is conditional on the synthesis deliverable demonstrating the projected properties.

**Acceptance Criteria:** AI-First Design's scores are either (a) removed from the comparative selection matrix, with the domain addressed through a separate prospective evaluation, OR (b) all scores are explicitly labeled as projective and a validation gate is specified that must be met before implementation proceeds.

---

### DA-004-20260302: "Tiny Teams" Criterion Is a Narrative Fit Test, Not a Differentiating Filter [MAJOR]

**Claim Challenged:**
> "Tiny Teams Applicability (25%): A framework that cannot be executed by a 2-3 person team is irrelevant regardless of its other merits. This is the filter criterion that must be satisfied before any other criterion is evaluated."
> — Section 1, Weighting Rationale

**Counter-Argument:**
The Tiny Teams criterion claims to be the most important differentiating criterion at 25% weight. But a close inspection of the scores reveals that it barely differentiates the top 20 frameworks. Of the 10 selected frameworks, 6 score 9-10/10 on C1 and 4 score 8/10. The gap between rank 1 (Design Sprint, C1=10) and rank 11 (Double Diamond, C1=8) is not 25% weight applied to a discriminating scale -- it is a 2-point difference on a 10-point scale in a criterion where 70% of candidates cluster between 7-10.

The score rubric itself reveals the problem: scores of 7-8 mean "Framework works well for small teams with some adaptation" and 9-10 means "Framework was designed for or is naturally optimized for 1-3 person teams." Nearly every modern UX framework in active use works "well for small teams with some adaptation." Design Sprint is not dramatically better than Double Diamond for a 2-person team -- both require roughly the same headcount for their core process. The "5-day process" of Design Sprint arguably REQUIRES more coordination overhead than Double Diamond's more flexible diverge-converge structure.

More critically: the frameworks that score 1-2 on C1 (Contextual Design: 2, GOMS Model: 2, Usability Engineering Lifecycle: 2) are eliminated not by the 25% weight but because they are enterprise/specialist frameworks that nobody would have selected anyway. The weight punishes frameworks that nobody was going to choose. Among the genuinely competitive frameworks (scores 6-40), the C1 scores cluster so tightly (7-10) that the 25% weight amplifies tiny score differences into large rank movements -- differences that may not reflect genuine Tiny Teams differentiation.

**Evidence:**
Fogg Behavior Model (rank 10, C1=8) vs. Service Blueprinting (rank 11, C1=7): the 1-point C1 difference at 25% weight contributes 0.25 points to the total -- the ENTIRE margin separating selection (7.60) from non-selection (7.35). Yet the claim that Fogg is "designed for Tiny Teams" while Service Blueprinting "works for small teams with some adaptation" is a weak distinction. A 2-person team applying Service Blueprinting (a visualization exercise) and a 2-person team applying Fogg's B=MAP diagnostic framework face comparable operational constraints. The C1 score difference of 1 point is not well-evidenced; it is a judgment call that has a 0.25-point decisive impact on selection.

**Impact:** If C1 provides weak differentiation among competitive frameworks (the ones actually competing for selection) while providing strong differentiation only for clearly disqualified enterprise frameworks, then C1's 25% weight is doing most of its work in a range that was never competitive to begin with. This is a criterion that appears to carry selection weight but mostly validates an obvious baseline filter. The analysis would reach nearly the same results at 15% weight for C1.

**Dimension:** Evidence Quality

**Response Required:** Provide evidence that the C1 score distinctions (specifically 8 vs. 9 vs. 10) are meaningfully calibrated and not subjective assignments. This requires: (a) define the empirical criteria that distinguish a C1=8 from a C1=9 framework with at least one concrete distinguishing test, and (b) verify that the 1-point differences in C1 between adjacent frameworks in the competitive band (ranks 8-15) are supported by specific evidence from the source research artifacts.

**Acceptance Criteria:** C1 score distinctions for frameworks scoring 7-10 are supported by specific evidence from the research artifacts, not just "consistent with" the rubric definitions.

---

### DA-005-20260302: Score Compression Makes Rank-Ordering Statistically Meaningless Below Rank 5 [MAJOR]

**Claim Challenged:**
> The scoring matrix presents ranks 1-10 as the selected set with ranks 11-40 as rejected. The selection is presented as a justified multi-criteria outcome. The verified scores range from 9.15 (Design Sprint) to 7.60 (Fogg Behavior Model).
> — Section 2, Full Scoring Matrix

**Counter-Argument:**
The competitive band for the selected set spans 7.60-9.15. The top 5 are meaningfully separated (9.15, 9.05, 8.55, 8.30, 8.25 -- gaps of 0.10-0.50 points). But from rank 5 downward, the scores are:

Lean UX: 8.25, JTBD: 8.05, Microsoft Inclusive Design: 8.00, AI-First Design: 7.80, Kano: 7.65, Fogg: 7.60 -- and the 11th (non-selected): Service Blueprinting: 7.35.

The difference between rank 5 (Lean UX, 8.25) and rank 11 (Service Blueprinting, 7.35) is 0.90 points. But the difference between rank 7 (Microsoft Inclusive Design, 8.00) and rank 11 (Service Blueprinting, 7.35) is only 0.65 points. And between rank 10 (Fogg, 7.60) and rank 11 (Service Blueprinting, 7.35) is 0.25 points -- a gap of 0.25 on a 10-point scale (2.5%).

At this compression level, a single 1-point adjustment on any criterion for either Fogg or Service Blueprinting flips the selection outcome. The note in the deliverable acknowledges: "AI-First Design is the most weight-sensitive selection -- at 20% weight it drops 0.50 points, narrowing the gap with Service Blueprinting to marginal." But this underestimates the problem: at the current weights, Fogg vs. Service Blueprinting separation is ALREADY marginal (0.25 points). The analysis presents a definitive "top 10" as if the selection boundary is clearly justified, when for ranks 7-11, the selection outcome is within the margin of rounding error and subjective score calibration.

**Evidence:**
From Section 2: Fogg Behavior Model total = 7.60. Service Blueprinting total = 7.35. The C1 scores are Fogg=8, Service Blueprinting=7 -- a 1-point difference that contributes 0.25 points at 25% weight, which is the entire margin of difference. If a single evaluator had assigned Service Blueprinting C1=8 instead of 7 (a perfectly defensible judgment for a framework that requires modest facilitation skill), Service Blueprinting would replace Fogg in the selection. The analysis does not acknowledge that ranks 8-11 are effectively within a statistical tie given the subjective nature of 1-10 scoring.

**Impact:** Presenting ranks 8-11 as a definitive selection outcome rather than a tie-breaker region undermines the analysis's credibility. A reader who understands multi-criteria scoring would expect the analysis to acknowledge score uncertainty in the competitive band and treat ranks 8-11 as "roughly equivalent alternatives where specific domain needs might tip the choice." Instead, it presents a definitive rank ordering that implies more precision than the scoring method supports.

**Dimension:** Internal Consistency

**Response Required:** Acknowledge that ranks 7-11 are within a score compression zone where the rank ordering is not decisively supported by the point differences. Specifically: (a) add a note that frameworks scoring within 0.50 points of the selection threshold should be treated as co-equivalent and selection from this zone is a judgment call, not a scored determination, and (b) identify which specific selection decisions in ranks 7-11 are actually well-evidenced versus which are within the margin of calibration error.

**Acceptance Criteria:** The analysis explicitly identifies the score compression zone (approximately 7.60-8.00) and acknowledges that selections within this zone are not decisively determined by the scoring methodology alone.

---

### DA-006-20260302: Bridge MCP Warning Is Applied Inconsistently Across Frameworks [MAJOR]

**Claim Challenged:**
> "Bridge MCP integrations score 3-4 on C3 (not 6+), because the criterion definition requires 'production-ready MCP servers' for scores of 9-10 and permits 'some manual bridging' for 7-8. Bridge MCP through Zapier/Pipedream exceeds 'manual bridging' and should be scored accordingly."
> — Section 1, Criterion 3 note (RT-002 revision)

**Counter-Argument:**
The Bridge MCP categorization and the resulting scoring adjustment were a legitimate Red Team finding (RT-002), and the correction of HEART (6→4) and Fogg (4→3) on C3 is appropriate. However, the Bridge MCP warning is applied to HEART and Fogg -- frameworks that rely on Hotjar Bridge MCP -- but the analysis does not audit whether other frameworks' MCP integrations are genuinely "Native" vs. inflated.

Specifically, three concerns:

1. **Design Sprint's C3=8 relies on Whimsical (Community MCP).** The analysis categorizes Whimsical as "Community MCP" and uses it as a supporting integration for Design Sprint. The rubric assigns 9-10 only for "production-ready MCP servers." Community MCP servers are not production-ready by the analysis's own definition -- they are community-maintained and may not have the stability, security, or API coverage of official integrations. If Whimsical Community MCP is given the same weight as Figma/Miro official MCPs in contributing to Design Sprint's C3=8, the Bridge MCP correction logic (applied to Hotjar) should also reduce scores for frameworks that partially rely on Community MCP servers.

2. **JTBD's C3=5 relies on WebSearch and Context7, neither of which is a design tool MCP.** The rubric specifies "2+ tools with existing production-ready MCP servers (Figma, Miro, Storybook, Zeroheight)." WebSearch and Context7 are general-purpose tools, not the design tool MCPs the criterion was defined around. JTBD's MCP integration is scored at 5 ("can use MCP tools tangentially; the core methodology steps are not natively supported by MCP tools") but its tool list includes no design-tool MCPs at all. This is internally consistent, but it means the "MCP integration" criterion conflates two different things: integration with design-tool MCPs (Figma, Miro, Storybook) and integration with general-purpose MCP-capable tools (Context7, WebSearch).

3. **Fogg Behavior Model, post-correction, scores C3=3 and yet remains in the top 10 because its MCP-integrated workflow step (Hotjar funnel analysis) is central to the framework's value proposition in this analysis.** The warning says "This is Fogg's only MCP integration path; teams without Hotjar should use manual analytics export for the Measure step." If Fogg's primary data source for diagnosis is not reliably MCP-connected, the "AI agents can execute the diagnostic step through MCP" claim for Fogg falls apart for any team without Hotjar. This is acknowledged but its impact on the framework's C1 and C2 scores is not re-evaluated: if Fogg requires manual analytics export as its normal path (no Hotjar MCP), does it really score 8/10 on Tiny Teams Applicability and 9/10 on Composability as a Jerry sub-skill?

**Evidence:**
Section 3.9: "Hotjar (Bridge MCP via Zapier/Pipedream) -- Funnel analysis and session recordings provide the behavioral data for M/A/P diagnosis. WARNING: Bridge MCP only -- requires paid Zapier/Pipedream subscription and custom configuration. **This is Fogg's only MCP integration path; teams without Hotjar should use manual analytics export for the Measure step.**" If manual analytics export is the typical path for Fogg's core diagnostic step, then Fogg's skill operability is significantly lower than the C2=9 (Composability) score implies.

**Impact:** The MCP categorization correction was a genuine quality improvement. But it was applied inconsistently: Hotjar-dependent frameworks were penalized on C3, but the implications of Hotjar unavailability for C1 and C2 scores were not traced through. And the Community MCP / design-tool MCP conflation in the C3 rubric may be producing scores that are not comparable across frameworks.

**Dimension:** Internal Consistency

**Response Required:** Audit whether the Bridge/Community MCP distinction has cascading implications for C1 and C2 scores for HEART and Fogg specifically. If Fogg's primary MCP integration path is unavailable to most Tiny Teams (no Hotjar), verify that C2=9 (Composability as Jerry sub-skill) is still justified. Clarify whether Community MCP counts toward C3 at the same level as Native MCP or with a discount.

**Acceptance Criteria:** C1 and C2 scores for HEART and Fogg are verified as still accurate given the Bridge MCP constraint on their primary data integration. Community vs. Native MCP scoring discount policy is explicitly stated.

---

### DA-007-20260302: Design Sprint at #1 (9.15) Depends on a C1 Score of 10 That Is Not Defensible for a 5-Day Process [MAJOR]

**Claim Challenged:**
> Design Sprint scores C1=10: "Framework was designed for or is naturally optimized for 1-3 person teams; AI can automate 50%+ of its activities; the framework explicitly values speed and iteration over comprehensive staffing."
> — Section 2, Scoring Matrix (row 1)

**Counter-Argument:**
The Criterion 1 rubric for a score of 9-10 requires: "Framework was designed for or is naturally optimized for 1-3 person teams; AI can automate 50%+ of its activities; the framework explicitly values speed and iteration over comprehensive staffing."

Design Sprint 2.0 (Google Ventures) was designed for a 5-7 person cross-functional team. The original GV Sprint book explicitly specifies: Decider, Facilitator, Designer, Prototyper, Interviewer, and 2-3 Experts for a total of 6-8 participants. The AJ&Smart Design Sprint 2.0 simplification targets 4-5 participants. The "designed for or naturally optimized for 1-3 person teams" condition is not met by either version.

The analysis's justification for C1=10 in Section 3.1 is "A 2-person team (one product/dev + one designer or PM) runs the Design Sprint with AI as a third participant." But this is not evidence that the framework "was designed for or is naturally optimized for" 1-3 persons -- it is evidence that a 2-person team CAN adapt the framework using AI augmentation. The framework was designed for 4-7 participants; AI augmentation makes it executable by fewer. This is a 7-8 score profile ("works well for small teams with some adaptation; AI can meaningfully accelerate 25-50% of activities"), not a 9-10 profile ("designed for or naturally optimized for 1-3 person teams").

Furthermore, the "AI can automate 50%+ of activities" claim for a 5-day process requires scrutiny. The activities that cannot be automated by AI in a Design Sprint are among the most important: the Decider's decision on Thursday (Day 3), the user interviews on Friday (Day 5 -- the analysis itself states "AI cannot substitute for real users -- the Friday test is the empirical validation step that AI cannot automate"), and the Expert Interviews on Monday. The activities AI CAN automate (variant generation, prototype drafting, note synthesis) are support activities. If the empirically critical activities (user testing, Decider judgment) cannot be automated, it is not clear that AI automates "50%+" in terms of decision weight, even if it accelerates 50%+ of activity hours.

**Evidence:**
Section 3.1 explicitly acknowledges: "AI cannot substitute for real users -- the Friday test is the empirical validation step that AI cannot automate. Fallback for Friday: at minimum, conduct a cognitive walkthrough with a team member playing the user role while AI evaluates against Nielsen's Heuristics." This fallback removes the Design Sprint's primary empirical validation mechanism. A Design Sprint that cannot run user testing on Friday is not the Design Sprint that earned its 9.15 score -- it is a 4-day idea generation and prototyping exercise.

**Impact:** If Design Sprint's C1 score is 10 rather than the more defensible 8, its weighted total is inflated by 0.50 points (2 points × 25% weight). With C1=8, Design Sprint's total would be 8.65 rather than 9.15. It would still be the highest-scoring framework, but the margin over Nielsen's (9.05 → 8.95 with same correction applied if warranted) would narrow. More importantly, the C1=10 score treats "AI adaptation of a multi-person framework" as equivalent to "designed for small teams" -- a category distinction the rubric explicitly separates.

**Dimension:** Evidence Quality

**Response Required:** Provide specific evidence from the source research artifacts that Design Sprint's original methodology "was designed for or is naturally optimized for 1-3 person teams." If the source research characterizes Design Sprint as a 4-7 person framework that has been adapted for smaller teams via AI augmentation, the score should be 7-8, not 9-10.

**Acceptance Criteria:** Design Sprint's C1 score is validated against its source research characterization (not against the AI-augmentation scenario described in Section 3.1). If the source research characterizes it as designed for 4-7 persons, the score is corrected to 8 (or justified for 10 with specific source citations that support "designed for 1-3 persons").

---

### DA-008-20260302: The "Equal-Weight Discriminator" Argument Undermines the Sensitivity Analysis's Robustness Claim [MINOR]

**Claim Challenged:**
> "9 of 10 selected frameworks maintain their position when the highest-weight criterion (Tiny Teams Applicability) is reduced by 20% of its value (25% → 20%) and redistributed to Complementarity. In a 40-framework competitive field, this stability indicates that the selected frameworks are genuine multi-criteria leaders."
> — Section 1, Sensitivity Analysis [SM-003]

**Counter-Argument:**
The sensitivity analysis tests a single weight variation: C1 from 25% to 20%, with the freed 5% moved to C5 (Complementarity). This is presented as demonstrating robust multi-dimensional leadership. However, if C1 is genuinely a "necessary condition" that most competitive frameworks satisfy (as DA-004 establishes), then reducing C1's weight to 20% should not dramatically change rankings -- because C1 is barely discriminating in the competitive band. Finding that 9/10 selections are stable after a weight reduction on a weakly-discriminating criterion is not strong evidence of robustness.

The single variation tested (C1: 25%→20%) is also the variation most likely to preserve the existing selection, because it redistributes to C5 (Complementarity), which is self-referential (DA-002). A more informative sensitivity test would vary the weights of criteria that actually discriminate in the competitive band -- for example, C3 (MCP Integration) where the scores genuinely vary (3-10 range) and the criterion distinguishes Atomic Design (10) from Fogg (3) and HEART (4). Testing what happens when C3 weight increases from 15% to 25% would reveal whether the high-MCP frameworks are robustly top-10 or whether the current weighting is what keeps low-MCP frameworks (HEART, Fogg, JTBD) in the selection.

**Evidence:**
Section 1 shows only one sensitivity test. JTBD scores C3=5, HEART=4, Fogg=3 -- these are significant MCP integration gaps for frameworks positioned as AI-augmented skill implementations. If MCP integration were weighted at 25% instead of 15%, the resulting additions to these frameworks' totals from C3 vs. hypothetical replacements like Service Blueprinting (C3=7) or even Double Diamond (C3=5) might change the composition more than the C1 variation test shows.

**Impact:** Minor -- the selection is likely still robust overall. But presenting a one-variation sensitivity analysis as comprehensive robustness evidence is an overstatement, particularly when the tested variation is the one least likely to produce rank changes.

**Dimension:** Evidence Quality

**Recommendation:** Add at least one additional sensitivity test varying C3 (MCP Integration) weight from 15% to 25%, since MCP integration is the criterion with the most score variance in the competitive band (HEART=4, Fogg=3 vs. Atomic Design=10, Design Sprint=8) and is the criterion most relevant to the AI-augmented skill-implementation purpose.

---

### DA-009-20260302: Double Diamond Exclusion Relies on a Circular Argument [MINOR]

**Claim Challenged:**
> "Critically low complementarity score (5/10) because Design Sprint and Lean UX together completely cover the same process territory Double Diamond occupies. The Double Diamond's diverge-converge logic is embedded in Design Sprint's Monday-Wednesday (diverge to understand, converge to decide) and Thursday-Friday (build one solution, test)."
> — Section 5.1

**Counter-Argument:**
The argument for Double Diamond's exclusion is: "Design Sprint already covers its territory." But the argument for Design Sprint's inclusion is: "Design Sprint is the most complete end-to-end design process." These two claims are doing circular work: Double Diamond is excluded because Design Sprint is in, and Design Sprint's value is partially justified by its ability to cover the Double Diamond territory. If Double Diamond had been selected first and Design Sprint had been the challenger, the analysis would have noted that "Design Sprint's diverge-converge structure duplicates Double Diamond's core logic and scores lower on Maturity (8 vs. 9) and global recognition."

The analysis also claims Design Sprint C2=10 (Composability) vs. Double Diamond C2=9. This 1-point difference contributes 0.20 points at 20% weight to the total gap. Yet both frameworks have clear, discrete phases with defined outputs -- the claim that Design Sprint has "3-7 discrete, sequenced phases each with clear inputs, outputs, and completion criteria" applies equally to Double Diamond (Discover, Define, Develop, Deliver). The specific distinction that earns Design Sprint a 10 vs. Double Diamond's 9 is not explained.

**Evidence:**
Section 2 Scoring Matrix: Double Diamond C2=9 (explanation: "has clear structure but requires some interpretation to map to a skill; phases may overlap or have fuzzy boundaries"). Design Sprint C2=10 (explanation: implied by daily protocol structure). The distinction is not unreasonable, but a 1-point gap on C2 + the higher C4 score for Double Diamond (9 vs. 8) means Double Diamond's exclusion is primarily driven by a C5 score that is circular (as established in DA-002).

**Impact:** Minor -- this does not change the overall selection analysis. But it is worth acknowledging that Double Diamond's exclusion is more contingent on C5 circularity than the analysis presents.

**Dimension:** Traceability

**Recommendation:** Acknowledge in Section 5.1 that Double Diamond's exclusion is primarily a C5 outcome (determined by having selected Design Sprint and Lean UX first) rather than an objective finding, and note that under an alternate starting selection, Double Diamond and Design Sprint/Lean UX might have traded positions.

---

### DA-010-20260302: The HIGH RISK User Research Gap Disclosure Undermines the Fitness-for-Purpose Claim [MINOR]

**Claim Challenged:**
> The core thesis states the analysis "selects 10 UX frameworks that collectively maximize UX outcome coverage for AI-augmented Tiny Teams."
> Yet the gap analysis states: "The selected 10 does not include a dedicated remote user research framework. This gap carries real risk and should NOT be minimized."
> — Core Thesis (preamble); Section 4, Gap Analysis (RT-004)

**Counter-Argument:**
The core thesis claims the selection "maximizes UX outcome coverage." The HIGH RISK disclosure says the selection has a gap in one of the foundational activities of UX -- user research -- that "carries real risk" and explicitly states: "AI-generated personas and simulated usability testing reflect training data biases, not the team's specific user population. The UX industry consensus (NN Group, Baymard Institute, JTBD practitioners) is that real user contact is the empirical foundation of UX quality and is not substitutable by AI synthesis alone."

These two claims are in tension. A selection that "maximizes UX outcome coverage" and a selection with a HIGH RISK gap in the empirical foundation of UX quality are difficult to hold simultaneously. The Steelman's framing (SM-008) presents this as "conscious scope decision with documented trade-offs." This is a fair framing for a pragmatic engineering decision. But the core thesis's "maximize UX outcome coverage" language overstates what the selection achieves -- it should say "maximizes UX outcome coverage within the constraints of the V1 scope" or "maximizes coverage across deliverable-focused UX activities" to distinguish it from research-dependent activities.

**Evidence:**
The HIGH RISK disclosure uses strong language: "SHOULD NOT rely on these alone." This is appropriate -- the analysis is being honest about a real limitation. But this honest limitation is in direct conflict with the "maximizes UX outcome coverage" claim in the core thesis, which was added by the Steelman (SM-001) as the strongest formulation of the thesis.

**Impact:** Minor -- this is primarily a presentation consistency issue. The limitation is properly disclosed. But the core thesis should be brought into alignment with the disclosed limitation.

**Dimension:** Internal Consistency

**Recommendation:** Qualify the core thesis claim from "maximizes UX outcome coverage" to "maximizes UX outcome coverage for deliverable-focused UX activities within a V1 scope that intentionally excludes a dedicated user research framework (see Section 4 HIGH RISK gap)." This makes the thesis and the gap analysis internally consistent.

---

## Recommendations

### P0: Critical -- MUST resolve before acceptance

**DA-001: Weighting Rationale -- Necessity vs. Priority**
- Action: Revise Section 1 Weighting Rationale to either (a) implement genuine hard gates for C1 and C2 (frameworks below threshold score are eliminated before weighted scoring), or (b) accurately describe C1 and C2 as "highest-weight priority criteria" rather than "necessary conditions / gatekeepers." Option (b) is the lower-effort path and does not require scoring recalculation.
- Acceptance criteria: No internal contradiction between the "necessary conditions" claim and the weighted-average scoring method. The weighting rationale description matches how the math actually works.

**DA-002: Complementarity Scoring -- Self-Referential Validation**
- Action: Add an explicit acknowledgment to the Complementarity scoring note and the sensitivity analysis section that complementarity scores are portfolio-conditional and do not provide independent validation of the selection. The "empirical validation" language for the failure mode coverage table should not be conflated with the C5 scoring, which is self-referential.
- Acceptance criteria: The deliverable does not use complementarity scores as independent evidence of selection quality. The complementarity methodology is described accurately as a consistency check, not an external test.

### P1: Major -- SHOULD resolve; require justification if not

**DA-003: AI-First Design -- Category Violation**
- Action: Add an explicit qualification to all AI-First Design scores that they are projective predictions contingent on synthesis deliverable properties. Add a validation gate: AI-First Design's sub-skill proceeds to implementation only after the synthesis deliverable demonstrates the projected C1=10 and C2=8 properties through an expert review.
- Acceptance criteria: Scores labeled as projective; implementation gate specified.

**DA-004: Tiny Teams Criterion -- Calibration Evidence**
- Action: Provide specific evidence from source research artifacts for C1 score distinctions between 8, 9, and 10 in the competitive band (frameworks scoring 7-10). At minimum, verify that Fogg (C1=8) vs. Service Blueprinting (C1=7) distinction is supported by source material rather than analyst judgment.
- Acceptance criteria: C1 scores for ranks 7-15 are traceable to specific source evidence.

**DA-005: Score Compression -- Acknowledge the Tie Zone**
- Action: Add a note to the Top 10 selection that frameworks scoring within 0.50 points of the selection boundary (approximately 7.35-8.00) are within a score compression zone where rank ordering is not decisively determined by the scoring methodology. Selections in this zone are judgment calls informed by the scores, not deterministic algorithmic outcomes.
- Acceptance criteria: Score compression zone acknowledged; ranks 8-11 not presented as decisively determined.

**DA-006: Bridge MCP Consistency**
- Action: Verify that Fogg's C1=8 and C2=9 scores are still justified given the Bridge MCP-only path for its primary diagnostic data source. Explicitly state whether Community MCP tools count the same as Native MCP in C3 scoring or at a discount.
- Acceptance criteria: Fogg's C1/C2 scores are validated with acknowledgment of Hotjar dependency; Community/Native MCP scoring policy stated.

**DA-007: Design Sprint C1 Score**
- Action: Verify Design Sprint's C1=10 against source research characterization. If the survey or tiny teams research characterizes Design Sprint as designed for 4-7 participants (not 1-3), revise to C1=8 and recalculate the weighted total (would become 8.65). Verify the selection is unchanged.
- Acceptance criteria: Design Sprint's C1 score is traceable to source research characterization, not to the AI-augmentation scenario described in Section 3.1.

### P2: Minor -- MAY resolve; acknowledgment sufficient

**DA-008: Sensitivity Analysis**
- Recommendation: Add a second sensitivity test varying C3 (MCP Integration) weight from 15% to 25% to show robustness against the criterion with highest score variance in the competitive band. Acknowledgment that the current test is a single-variation analysis is sufficient if the additional test is not added.

**DA-009: Double Diamond Exclusion**
- Recommendation: Add a sentence to Section 5.1 acknowledging that Double Diamond's exclusion is primarily a C5 (complementarity) outcome driven by the prior selection of Design Sprint and Lean UX, and would be reconsidered if either were excluded. Acknowledgment sufficient.

**DA-010: Core Thesis Qualification**
- Recommendation: Qualify "maximizes UX outcome coverage" to "maximizes UX outcome coverage for deliverable-focused UX activities within V1 scope" to align with the HIGH RISK gap disclosure. This is a one-sentence revision to the core thesis preamble.

---

## Scoring Impact

| Dimension | Weight | Impact | DA Findings | Rationale |
|-----------|--------|--------|-------------|-----------|
| Completeness | 0.20 | Neutral | DA-008, DA-009 | No completeness gaps identified at Critical/Major level. Minor gaps in sensitivity analysis coverage (DA-008) and Double Diamond documentation (DA-009). Core analysis is complete. |
| Internal Consistency | 0.20 | Negative | DA-001, DA-005, DA-010 | DA-001 identifies a contradiction between the "necessary conditions" claim and the weighted-average scoring method. DA-005 identifies that presenting rank compression as decisive undermines internal consistency. DA-010 identifies tension between core thesis and gap disclosure. |
| Methodological Rigor | 0.20 | Negative | DA-002, DA-003, DA-004 | DA-002 identifies that complementarity scoring is self-referential, not independent measurement. DA-003 identifies a category violation in scoring a prospective framework alongside existing ones. DA-004 challenges whether the highest-weight criterion is doing meaningful discriminatory work. |
| Evidence Quality | 0.15 | Negative | DA-004, DA-007 | DA-004 challenges whether C1 score distinctions in the competitive band are evidenced vs. judgments. DA-007 challenges whether Design Sprint's C1=10 is supported by source research. |
| Actionability | 0.15 | Positive | DA-003, DA-006 | The proposed resolutions (validation gate for AI-First Design, Bridge MCP policy clarification) would improve actionability by making implementation prerequisites explicit. Net positive if addressed. |
| Traceability | 0.10 | Neutral | DA-001, DA-009 | DA-001 resolution options both trace to the scoring methodology. DA-009 is a minor traceability improvement. No critical traceability gaps found. |

**Net assessment:** Internal Consistency and Methodological Rigor take the most hits. The scoring methodology has two structural issues (DA-001: false gating claim, DA-002: circular complementarity) that reduce confidence in the methodology's self-description, even if the final selection is largely defensible on other grounds.

---

## Execution Statistics

- **Total Findings:** 10
- **Critical:** 2 (DA-001, DA-002)
- **Major:** 5 (DA-003, DA-004, DA-005, DA-006, DA-007)
- **Minor:** 3 (DA-008, DA-009, DA-010)
- **Protocol Steps Completed:** 5 of 5
- **H-15 Self-Review:** Applied -- all findings verified against specific deliverable evidence; no findings cite general UX knowledge without deliverable reference; severity classifications verified against template criteria.
- **H-16 Compliance:** CONFIRMED -- S-003 Steelman executed before S-002; Steelman output loaded and reviewed as Step 1 of execution protocol; Revision 2 deliverable incorporates Steelman improvements (SM-001 through SM-009).

---

*Devil's Advocate Report Version: 1.0*
*Strategy: S-002 (Devil's Advocate)*
*Template: `.context/templates/adversarial/s-002-devils-advocate.md`*
*SSOT: `.context/rules/quality-enforcement.md`*
*Date: 2026-03-02*
*Execution ID: 20260302*
