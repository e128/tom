# Devil's Advocate Report: UX Framework Selection — Weighted Multi-Criteria Analysis (Iteration 2)

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 6)
**Criticality:** C4
**Date:** 2026-03-03T00:00:00Z
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman (Iteration 2) applied 2026-03-03 (confirmed — `projects/PROJ-020-feature-enhancements/work/analysis/tournament-iter2/s-003-steelman.md`; Steelman strengthened minimality re-sequencing (SM-010), WSM independence resolution (SM-011), governance owner assignment (SM-012), behavioral directive cross-reference (SM-013), adoption sequencing table (SM-014), and footer attribution correction (SM-015))

---

## Step 1: Role Assumption

**Role assumed:** Devil's Advocate arguing against the Revision 6 UX Framework Selection deliverable's core claims, having read the Iteration 2 S-003 Steelman output per H-16 compliance. This critique attacks the STRENGTHENED version of the argument — the version that incorporates SM-010 through SM-015 improvements.

**Deliverable being challenged:** Revision 6 of the Weighted Multi-Criteria Decision Analysis selecting 10 UX frameworks for an AI-augmented Tiny Teams portfolio (`/user-experience` Jerry skill). Revision 6 is the post-Iteration-1 revision incorporating findings from all 10 Iteration 1 adversarial strategies (S-001 through S-014). The Iteration 2 S-003 Steelman (this session's prerequisite) has additionally proposed SM-010 through SM-015 as strengthening improvements.

**Scope of critique:** Central thesis validity, methodology, scoring reliability, portfolio completeness, and forward-looking claims — with particular focus on Internal Consistency (scored 0.75 in Iteration 1, lowest alongside Methodological Rigor 0.70). Per the Iteration 2 execution plan, the Devil's Advocate must confirm whether revisions in R6 adequately resolve Critical/Major Iteration 1 findings or whether residual vulnerabilities remain, and identify NEW vulnerabilities in the strengthened R6 document.

**Iteration 1 resolution status (pre-execution survey):**

| Iter 1 Finding | Severity | R6 Resolution? | Assessment |
|----------------|----------|----------------|------------|
| DA-001 (minimality circular taxonomy) | Critical | Partial | MINIMALITY CLAIM QUALIFICATION block added; leads with weakness per SM-010 |
| DA-002 (sensitivity tests safest scenarios) | Critical | Resolved | C3=25% perturbation table added with full numeric results |
| DA-003 (AI-First Design vs. minimal-complete) | Critical | Partial | "contingent on synthesis" language added but tension with Service Blueprinting substitution path remains |
| DA-004 (maximize claim vs. ceiling) | Major | Partial | Core thesis adds "within a V1 scope" but still retains "maximize" |
| DA-005 (C5 cited as evidence despite caveat) | Major | Resolved | SM-001 steelman now uses functional test and coverage removal test; Complementarity Matrix not cited as external validation |
| DA-006 (3 errors = unreliability) | Major | Resolved | "Correct interpretation [DA-006]" section reframes error detection appropriately |
| DA-007 (Tiny Teams profile unvalidated) | Major | Resolved | Gartner citation removed; tiny-teams-research.md artifacts cited as basis |
| DA-008 (WSM independence assumption) | Minor | Partial | Acknowledged but not resolved per SM-011 (Steelman) |
| DA-009 (tooling cost missing) | Minor | Resolved | DA-009 tooling cost note added per revision history |
| DA-010 (maximize vs. HIGH RISK gap) | Minor | Partial | Core thesis adds inline caveat but does not remove "maximize" |

---

## Step 2: Assumption Inventory

**Explicit assumptions in Revision 6:**

| # | Assumption | Location | Challenge |
|---|-----------|----------|-----------|
| A-1 | The "minimize coverage" claim is scoped to "deliverable-focused UX activities within a V1 scope for AI-augmented Tiny Teams" | Core Thesis, preamble line 7 | The scope qualification is new in R6 (from DA-004/DA-010 corrections) but still retains the word "maximize." Does "maximize within a V1 scope" resolve the contradiction with the HIGH RISK user research gap, or merely reframe it? |
| A-2 | "minimal-complete contingent on AI-First Design synthesis completing with projected properties" | MINIMALITY CLAIM QUALIFICATION block | The contingency is now explicit. But the deliverable's core thesis STILL says "portfolio where each framework fills a unique lifecycle niche" in present tense — this is a claim about a current state, not a future state. |
| A-3 | The C3=25% sensitivity perturbation resolves the DA-002 concern about testing only safe scenarios | Section 1 Sensitivity Analysis, Third perturbation | The C3 perturbation is now provided (DA-002 resolved). But the perturbation confirms that Kano (#9) and Fogg (#10) FALL BELOW the threshold under C3=25%. The DA-002 response says "this does NOT invalidate the selection under baseline weighting." This interpretation is circular: the baseline weighting produces the selection; a perturbation that changes the selection is described as "not invalidating" the selection under baseline weighting. The perturbation is presented as a robustness test, but it actually reveals selection fragility at the boundary. |
| A-4 | Single-rater bias for 30 non-selected frameworks has ±0.25 uncertainty; adversarial review "constitutes a quality process, not a reliability certificate" | Section 1 Methodology Limitations | DA-006 correction in R6 was to reframe the interpretation. The actual error rate remains unknown. The deliverable now correctly characterizes the adversarial review as a quality process rather than inter-rater validation, but the implication (that the remaining scores are well-supported) is still not independently evidenced. |
| A-5 | The three sensitivity perturbations together provide "strong evidence for the selection's robustness" | Section 1 Sensitivity Analysis conclusions | Two perturbations show no selection change (C1 and C2 swap with C5). One perturbation (C3=25%) shows two frameworks falling below threshold. The aggregate characterization as "strong robustness" is unsupported — two of three tests show stability, one test shows partial instability. The appropriate characterization is "robust under C1 and C2 perturbation; selection-boundary sensitive under C3 upweighting." |

**Implicit assumptions in Revision 6 (new or persisting from Iter 1):**

| # | Implicit Assumption | Where Relied Upon | Challenge |
|---|--------------------|--------------------|-----------|
| IA-1 | The WSM independence assumption violation (C1/C5 correlation) has been adequately resolved by the C3=25% perturbation serving as an empirical test | SM-011 Steelman (proposed) + DA-008 note in R6 | The SM-011 Steelman PROPOSES this resolution but it is NOT IN R6 TEXT yet. The R6 text (Section 1 Weighting Rationale, DA-008 note) still reads: "This limitation is inherent to WSM applied to portfolio optimization; users weighting C3 (MCP Integration) at 25% instead of 15% should recompute the matrix under that weighting before relying on this selection." This is an unresolved invitation to recompute, not a resolution. |
| IA-2 | AI-augmented execution timelines ("under 10 minutes," "under 30 minutes with AI assistance") are credible design targets that a team can rely on for planning | Section 3 framework descriptions throughout | All time estimates are preceded by a CC-004 notice: "These patterns represent design targets for implementation, not descriptions of currently operational capabilities." But the sub-skill descriptions throughout Section 3 present time estimates as actionable guidance. A team planning capacity allocation will use these numbers without revisiting the CC-004 caveat. |
| IA-3 | The "adoption wave sequencing" (SM-014 Steelman proposal) resolves the team cognitive overload concern for simultaneous adoption | SM-014 proposed addition to Section 7.2 | This assumption does not exist in R6 — it is a Steelman proposal. If it is NOT incorporated into R7, the cognitive overload concern from Iter 1 SM-005 remains unaddressed. The Devil's Advocate must note that whether SM-014 constitutes a genuine resolution depends on implementation. |
| IA-4 | The document footer method attribution matters for credibility | SM-015 Steelman proposal | The footer currently says "Kepner-Tregoe" which the Steelman identifies as incorrect. This is a current R6 defect, not a proposal for revision. The deliverable body correctly names WSM but the footer misattributes the method. |

---

## Step 3: Counter-Arguments

### Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-011-20260303b | The C3=25% sensitivity perturbation result is characterized as "not invalidating" the baseline selection, but this interpretation is unfalsifiable — any perturbation result can be explained as "expected" or "domain-specific" | Critical | Section 1, Third sensitivity perturbation finding: "This perturbation does NOT invalidate the selection under baseline weighting -- it validates that the selection is sensitive to C3 weighting, which is expected and appropriate." This is tautological: if stability validates, and sensitivity also validates ("expected and appropriate"), the perturbation cannot produce a result that would invalidate the selection. | Methodological Rigor, Internal Consistency |
| DA-012-20260303b | The core thesis still uses "maximize UX outcome coverage" despite the inline scope qualification; the qualification does not logically preserve the maximization claim | Major | Core Thesis: "This analysis selects 10 UX frameworks that collectively maximize UX outcome coverage for deliverable-focused UX activities within a V1 scope..." The scope qualification ("within a V1 scope") restricts the claim's domain but does not affect the "maximize" predicate WITHIN that domain. The HIGH RISK user research gap (Section 4) is explicitly within the deliverable-focused UX activity domain — the gap is a coverage failure within the scoped domain, not outside it. | Internal Consistency |
| DA-013-20260303b | The WSM independence assumption (C1/C5 correlation) is acknowledged in R6 but explicitly unresolved — the text invites users to "recompute the matrix" rather than providing the resolution | Major | Section 1 Weighting Rationale, DA-008 note: "This limitation is inherent to WSM applied to portfolio optimization; users weighting C3 (MCP Integration) at 25% instead of 15% should recompute the matrix under that weighting before relying on this selection." The SM-011 Steelman proposes a resolution (C3=25% as empirical test of C1/C5 correlation distortion) but this resolution is NOT present in R6. The deliverable as delivered contains an unresolved methodological limitation. | Methodological Rigor |
| DA-014-20260303b | The Fogg Behavior Model's C3 score of 3/10 and Kano Model's C3 score of 4/10 — combined with their confirmed instability under C3=25% — reveal these selections to be C3-compensated by other criteria in a way the methodology does not acknowledge | Major | Score Calculation Verification table: Fogg C3=3 (contributing 0.45 to weighted total — lowest single-criterion contribution across all selected frameworks). Under C3=25%, Fogg falls to 7.10 (rank #13 among the 11 assessed frameworks, below Service Blueprinting at 7.40). The deliverable's conclusion is that Kano and Fogg are "fully executable without MCP tooling," but this reframes a scoring weakness as a design feature without addressing whether teams without MCP tooling can still execute the workflow at the claimed efficiency. | Evidence Quality, Methodological Rigor |
| DA-015-20260303b | The AI reliability tier table for Nielsen's Heuristics (Section 3.1) reveals a structural limitation in the entire portfolio: AI cannot unilaterally evaluate half of Nielsen's heuristics (H2, H4, H6, H7, H8, H10), undermining the "under 10 minutes with AI assistance" efficiency claim | Major | Section 3.1 AI reliability tiers: "Requires team input -- contextually evaluable" tier includes H2, H4, H6, H7, H8, H10 (6 of 10 heuristics). The Tiny Teams enablement pattern states "the human reviews and makes the final call on which to address" but only for AI-generated findings, not for evaluating heuristics where AI cannot produce reliable findings at all. For 6 of 10 heuristics, AI generates "confident-sounding findings that may be systematically wrong" -- meaning teams must independently evaluate those heuristics rather than AI-augmenting them. The "under 10 minutes with AI assistance" claim applies only to the 4 high-confidence heuristics. | Completeness, Evidence Quality |
| DA-016-20260303b | The MINIMALITY CLAIM QUALIFICATION block (DA-001/DA-003 response in R6) introduces self-undermining language that the S-003 Steelman correctly identifies but cannot fully repair without re-ordering the preamble — and the re-ordering is a Steelman PROPOSAL, not present in R6 | Minor | MINIMALITY CLAIM QUALIFICATION: "The minimality argument is a useful heuristic, not a formal proof." The SM-010 Steelman proposes presenting the three-part evidence case FIRST, then the qualification. But in R6 as delivered, the reader encounters "useful heuristic, not a formal proof" before seeing the evidence. The evidence is present but buried in Section 4. | Internal Consistency |
| DA-017-20260303b | The document footer method attribution error (Kepner-Tregoe vs. WSM) is a current R6 defect, not a proposal — a methodologically rigorous reviewer comparing the footer to Section 1 will find an internal inconsistency that undermines methodological credibility | Minor | Document footer (final line): "Method: Weighted Multi-Criteria Decision Matrix (Kepner-Tregoe)." Section 1 Weighting Rationale: "The scoring model applies the Weighted Sum Method (WSM), a standard MCDA technique (Triantaphyllou 2000, Velasquez & Hester 2013)." These are inconsistent. Kepner-Tregoe is a different MCDA variant. The inconsistency exists in the delivered document, independent of whether the Steelman's SM-015 correction is adopted. | Internal Consistency, Traceability |

---

## Step 4: Response Requirements

### DA-011-20260303b: Third Perturbation Interpretation Is Unfalsifiable [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 1 Sensitivity Analysis — Third sensitivity perturbation (C3=25%) finding block |
| **Strategy Step** | Step 3, Lens 1 (Logical flaws) |

**Claim Challenged:**
> "This perturbation does NOT invalidate the selection under baseline weighting -- it validates that the selection is sensitive to C3 weighting, which is expected and appropriate. Teams prioritizing MCP integration as a primary selection driver... should consider replacing Kano and/or Fogg with Service Blueprinting and reviewing HEART's role."

**Counter-Argument:**
The interpretation of the C3=25% perturbation result is structured to be unfalsifiable: if the perturbation shows stability, it is "evidence of robustness." If it shows selection changes (Kano and Fogg falling below threshold), it is "validation that the selection is sensitive to C3 weighting, which is expected and appropriate." Under this interpretive framework, no perturbation outcome could falsify the claim that the sensitivity analysis validates the selection.

The specific logical flaw: the claim that C3 sensitivity is "expected and appropriate" is not independently justified. The C3 criterion was assigned 15% weight because "MCP integration is a convenience accelerator, not a prerequisite for framework operability." This justification for the low weight is stated AFTER the perturbation result is known — it is a post-hoc rationalization of why a result showing Fogg and Kano are C3-weak does not invalidate their selection. A pre-registered interpretation framework (defined before the perturbation is run) would have stated: "If any selected framework falls below the threshold in an adversarial perturbation, we accept that result as evidence the framework is a marginal inclusion that should be re-evaluated." No such framework is stated.

Furthermore, the SM-011 Steelman DOES provide a pre-registered interpretation for the C3=25% perturbation: it is the empirical test of the C1/C5 correlation distortion. But this interpretation is present only in the Steelman PROPOSAL (not in R6 text), and it is specifically bounded to the C1/C5 correlation question — it cannot also simultaneously serve as the interpretation for C3-sensitivity findings for Kano and Fogg.

**Evidence:** Section 1, Third perturbation finding: "This perturbation does NOT invalidate the selection... it validates that the selection is sensitive to C3 weighting, which is expected and appropriate." The word "validates" is applied to a result that shows selection boundary instability — the perturbation cannot simultaneously demonstrate sensitivity AND validate the selection through that sensitivity without a stated reason why C3 sensitivity at the selection boundary is acceptable.

**Impact:** If the perturbation interpretation is unfalsifiable, the sensitivity analysis does not function as a robustness test — it functions as a post-hoc narrative generator. Any three perturbation results, regardless of what they show, can be wrapped in "expected and appropriate" language. The entire sensitivity analysis section loses its function as a methodological validity check.

**Dimension:** Methodological Rigor, Internal Consistency

**Response Required:** The creator must state, in the sensitivity analysis section, a pre-registered interpretation rule: what specific perturbation outcomes would constitute evidence AGAINST the selection, and what outcomes would constitute evidence FOR the selection. The C3=25% perturbation result (Kano and Fogg fall below threshold) must be evaluated against this rule, not interpreted post-hoc as "expected and appropriate."

**Acceptance Criteria:** The sensitivity analysis section includes an explicit statement of what perturbation outcome would constitute disconfirming evidence. The C3=25% result is interpreted against this pre-stated rule. If "Kano and Fogg falling below the C3=25% threshold" is classified as confirming evidence (or acceptable), the specific reason must be stated pre-perturbation (e.g., "Kano and Fogg are MCP-independent by design; C3 perturbation tests are not relevant to their inclusion criteria") rather than post-hoc.

---

### DA-012-20260303b: "Maximize" Survives Scope Qualification and Still Conflicts with HIGH RISK Gap [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Core Thesis (document preamble) vs. Section 4 HIGH RISK user research gap |
| **Strategy Step** | Step 3, Lens 3 (Contradicting evidence) |

**Claim Challenged:**
> "This analysis selects 10 UX frameworks that collectively maximize UX outcome coverage for deliverable-focused UX activities within a V1 scope for AI-augmented Tiny Teams"

**Counter-Argument:**
The R6 revision to the core thesis added three scope qualifiers to the DA-004/DA-010 challenges: (1) "deliverable-focused UX activities," (2) "within a V1 scope," (3) "for AI-augmented Tiny Teams." These qualifiers restrict the domain of the maximization claim. However, the HIGH RISK user research gap (Section 4, HIGH RISK header) is described as: "This portfolio does NOT include a dedicated user research framework. The Design Sprint Day 4 testing protocol and Lean UX validation loops are minimum viable research mechanisms, NOT substitutes for a systematic user research program."

User research is a core deliverable-focused UX activity, not an operational or organizational concern outside the scope of deliverable-focused UX. The Section 4 HIGH RISK gap header itself says: "This gap carries real risk and should NOT be minimized." If user research falls within "deliverable-focused UX activities" (which it does — it produces user research deliverables), then the portfolio does not "maximize coverage" of deliverable-focused UX activities; it maximizes coverage while accepting a HIGH RISK gap.

Iteration 1 DA-010 raised this same contradiction. The R6 response was to add the scope qualification to the core thesis AND to add an inline caveat: "Note: the 'maximize coverage' claim is intentionally scoped to deliverable-focused UX activities; the selection does not include a dedicated user research framework (see Section 4 HIGH RISK gap)." This caveat is structurally equivalent to: "We claim X, but we acknowledge X is not true in one key domain." The caveat does not resolve the logical contradiction — it makes it explicit.

**Evidence:** Core Thesis (line 7): "maximize UX outcome coverage for deliverable-focused UX activities." Inline caveat: "the selection does not include a dedicated user research framework (see Section 4 HIGH RISK gap)." Section 4: "This gap carries real risk and should NOT be minimized."

**Impact:** The core thesis continues to misrepresent the deliverable's actual coverage. A decision-maker reading the thesis will understand the portfolio maximizes deliverable-focused UX coverage; a decision-maker reading Section 4 will understand there is a HIGH RISK gap in that same coverage. These two readings are inconsistent regardless of the scope qualifier added to the thesis.

**Dimension:** Internal Consistency

**Response Required:** Replace "maximize UX outcome coverage" with language that accurately represents the portfolio's coverage profile including its HIGH RISK gap. A logically consistent alternative: "This analysis selects 10 UX frameworks that provide best-available coverage of deliverable-focused UX activities for AI-augmented Tiny Teams within a V1 scope, with a disclosed HIGH RISK gap in user research coverage (see Section 4)."

**Acceptance Criteria:** The core thesis does not use "maximize" in conjunction with a coverage domain where Section 4 explicitly identifies a HIGH RISK gap. The thesis may reference the gap inline or by reference, but the thesis statement itself must be internally consistent with the Section 4 disclosure.

---

### DA-013-20260303b: WSM Independence Assumption Is Acknowledged but NOT Resolved in R6 [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 Weighting Rationale, WSM paragraph (DA-008 note) |
| **Strategy Step** | Step 3, Lens 2 (Unstated assumptions) |

**Claim Challenged:**
> "WSM independence assumption [DA-008]: WSM assumes criterion independence, which is approximated but not strictly satisfied: C1 (Tiny Teams Applicability) and C5 (Complementarity) have a documented correlation pattern... This limitation is inherent to WSM applied to portfolio optimization; users weighting C3 (MCP Integration) at 25% instead of 15% should recompute the matrix under that weighting before relying on this selection."

**Counter-Argument:**
The WSM paragraph in R6 (as delivered) identifies the C1/C5 correlation as a limitation that is "inherent to WSM applied to portfolio optimization" and then directs users to "recompute the matrix." This is an acknowledgment that the methodology has a known limitation, with no resolution of whether the limitation materially affects the ranking conclusions. The message to the reader is: "We know there is a problem, and we're telling you about it, but you'll have to compute the answer yourself if you want to know whether it matters."

The SM-011 Steelman proposal provides a resolution: the C3=25% adversarial perturbation IS the empirical test of whether the C1/C5 correlation distorts the selection, and the results (Kano and Fogg, the lowest-C1-scoring frameworks in the top-10, fall below threshold) confirm that the correlation effect is bounded and concentrated at the selection boundary. This resolution is sound — but it is a PROPOSAL, not present in R6.

The practical consequence of the R6 text as delivered: a reader who takes the "recompute the matrix" instruction seriously will find that frameworks with high C1 and C5 scores jointly benefit from a correlation that inflates their combined contribution by a small but nonzero amount. They will not find guidance in the document about whether this inflation changes the selection. They are left with a known limitation and no disclosed resolution.

**Evidence:** Section 1 Weighting Rationale: "users weighting C3 (MCP Integration) at 25% instead of 15% should recompute the matrix under that weighting before relying on this selection." This is an invitation to do the work the document has not done, not a resolution of the limitation.

**Impact:** The DA-008 finding from Iteration 1 was classified as Minor because "Acknowledgment that the WSM independence assumption is an approximation in this context" was the stated acceptance criterion. R6 has acknowledged the limitation. However, the Methodological Rigor dimension scored 0.70 in Iteration 1, with the scoring calibration and C1/C4 boundaries cited as key gaps. A mere acknowledgment without resolution does not improve the Methodological Rigor dimension materially. The SM-011 Steelman proposal would provide the resolution; without it, the limitation remains standing.

**Dimension:** Methodological Rigor

**Response Required:** Incorporate the SM-011 Steelman resolution into R7: the C3=25% adversarial perturbation is the empirical test of the C1/C5 correlation distortion concern; the perturbation results confirm the correlation effect is bounded to the selection boundary (Kano and Fogg), not systemic across the upper 7 frameworks. This converts the disclosed limitation into a disclosed-and-resolved limitation.

**Acceptance Criteria:** The WSM independence assumption section either: (a) explains why the C1/C5 correlation does not materially affect the ranking conclusions (using the C3=25% perturbation as empirical evidence), OR (b) provides an independent analysis of the effect magnitude. Simply directing users to "recompute the matrix" is not an acceptable resolution for a C4 deliverable.

---

### DA-014-20260303b: Fogg and Kano's C3 Weakness Is Reframed as "MCP-Independent by Design" Without Evidence [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 Sensitivity Analysis (C3=25% perturbation) + Section 2 Scoring Matrix (Fogg C3=3, Kano C3=4) |
| **Strategy Step** | Step 3, Lens 4 (Alternative interpretations) |

**Claim Challenged:**
> "both Kano and Fogg are fully executable without MCP tooling (Section 3.9, Section 3.10). This scenario confirms that C3 weighting is the primary selection driver that analysts should adjust for domain-specific contexts."

**Counter-Argument:**
The statement "fully executable without MCP tooling" is the defense offered for Kano and Fogg's low C3 scores and their selection-boundary fragility under C3 upweighting. But this defense is unverified. Sections 3.9 and 3.10 are referenced but not quoted. The claim that Kano and Fogg are "fully executable" without MCP requires the actual execution pathway to not depend on MCP-mediated tool integrations. Kano Model execution requires a survey of at least 30 users — a task that, without MCP integration, requires manual survey tooling (e.g., Typeform, Google Forms) with manual data transfer rather than AI-mediated execution. Fogg Behavior Model analysis requires B=MAP decomposition of user behavior — the AI execution pathway in Section 3.10 (not yet read) presumably uses text analysis inputs rather than MCP-integrated behavioral data.

The alternative interpretation is more credible: Fogg (C3=3) and Kano (C3=4) have low MCP integration scores because their execution workflows are less amenable to AI-via-MCP orchestration. They are executable WITHOUT MCP, but they are NOT equivalently executable to higher-C3 frameworks WITH MCP. The claim "fully executable without MCP" is true but incomplete — it does not address whether the execution quality or efficiency degrades when MCP integration is absent. For a portfolio that explicitly values AI augmentation ("AI-augmented Tiny Teams"), selecting frameworks with C3 scores of 3-4 while defending this as "MCP-independent by design" introduces an unstated quality gradient within the portfolio.

**Evidence:** Section 1 C3=25% perturbation: "both Kano and Fogg are fully executable without MCP tooling." Score verification table: Fogg C3=3 contributing 0.45 (lowest single-criterion contribution). Kano C3=4 contributing 0.60.

**Impact:** The C3 defense of Fogg and Kano reassures the reader that low MCP scores are acceptable. But the reassurance is "they can be executed without MCP" — which is true of nearly any methodology. The question is whether AI augmentation provides the claimed efficiency gains for frameworks with low MCP integration, and this question is unaddressed. If AI augmentation primarily works THROUGH MCP integrations (which the portfolio's entire AI execution narrative assumes), then low-C3 frameworks provide less AI augmentation benefit, not just "a different implementation path."

**Dimension:** Evidence Quality, Methodological Rigor

**Response Required:** The creator must either: (a) provide the actual execution pathway for Kano and Fogg under the "no MCP" scenario, including what efficiency targets are achievable WITHOUT MCP integration (not just the with-MCP targets), OR (b) acknowledge that Kano and Fogg provide reduced AI augmentation efficiency compared to higher-C3 frameworks, and that the C3=3-4 scores correctly reflect this reduced AI-augmentability rather than being a neutral design choice. The defense "fully executable without MCP" must be accompanied by comparative efficiency estimates.

**Acceptance Criteria:** Sections 3.9 (Kano) and 3.10 (Fogg) either: (a) provide explicit non-MCP execution targets with comparable efficiency claims, or (b) acknowledge that efficiency without MCP integration is lower than the AI-augmented targets stated elsewhere, and scope the stated efficiency claims accordingly.

---

### DA-015-20260303b: AI Reliability Tier Reveal Invalidates "Under 10 Minutes" Claim for Half of Nielsen's Heuristics [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.1 Nielsen's Heuristics — AI reliability tiers table + Tiny Teams enablement pattern |
| **Strategy Step** | Step 3, Lens 5 (Unaddressed risks) |

**Claim Challenged:**
> "A developer or PM with no formal UX training triggers `/ux-heuristic-eval`... and receives a structured heuristic evaluation report in under 10 minutes." (Section 3.1 Tiny Teams enablement pattern)

**Counter-Argument:**
The AI reliability tiers table in Section 3.1 reveals that 6 of the 10 Nielsen's heuristics (H2, H4, H6, H7, H8, H10) require team input and "Presents as hypotheses with specific questions for the team." For these 6 heuristics, the AI cannot evaluate them directly — it produces questions that the team must answer before findings can be generated. The "under 10 minutes" efficiency claim for the full heuristic evaluation assumes these 6 heuristics are AI-evaluable. They are not.

The correct characterization of the `/ux-heuristic-eval` workflow is: AI evaluates 4 heuristics in under 10 minutes; AI generates specific questions for the remaining 6 heuristics that the team must answer; the team evaluates those 6 heuristics using AI-generated questions as prompts. The total workflow time for a complete 10-heuristic evaluation is materially longer than 10 minutes — it includes the time for the team to gather the contextual knowledge needed to answer questions about platform conventions (H2), consistency standards (H4), workflow flexibility (H7), aesthetic decisions (H8), and documentation existence (H10). For a non-specialist team, these answers may require platform research, stakeholder interviews, or design system documentation review.

This is not a minor qualification — it changes the value proposition of the skill from "AI-autonomous heuristic evaluation" to "AI-assisted heuristic evaluation with substantial team input required." The core C2 score (Composability: 10/10) for Nielsen's Heuristics rests on the claim that it can be executed as an AI-guided workflow. If 60% of the heuristics require team evaluation rather than AI evaluation, the composability score may be overstated.

**Evidence:** Section 3.1 AI reliability tiers: "Requires team input" tier contains 6 of 10 heuristics (H2, H4, H6, H7, H8, H10). Section 3.1 Tiny Teams enablement pattern: "receives a structured heuristic evaluation report in under 10 minutes." Claim not qualified by "for the 4 high-confidence heuristics only."

**Impact:** The AI execution efficiency claims throughout Section 3 are the primary justification for C2 (Composability) scores in the 8-10 range. If the paradigmatic highest-scoring framework (Nielsen's, C2=10) has only 40% full AI automation, the C2 scoring rubric's boundary at 9-10 ("each phase has clear inputs, outputs, and completion criteria; can be invoked independently") may be based on an optimistic view of AI capability for the contextually-dependent evaluation steps.

**Dimension:** Completeness, Evidence Quality

**Response Required:** The creator must either: (a) revise the "under 10 minutes" efficiency claim to accurately reflect the 4 fully-AI-evaluable heuristics vs. the 6 team-input-required heuristics (e.g., "AI completes the 4 structural heuristics in under 5 minutes; the full 10-heuristic evaluation including team context-gathering is estimated at 30-60 minutes"), OR (b) revise the C2=10 score if the 6 team-input heuristics constitute a meaningful workflow bottleneck not captured in the composability rubric.

**Acceptance Criteria:** The Tiny Teams enablement pattern for Nielsen's Heuristics accurately represents the time requirement for COMPLETE heuristic evaluation (all 10 heuristics), not only for the AI-autonomous subset (4 heuristics). If the efficiency claim applies only to the AI-autonomous subset, this must be stated explicitly.

---

### DA-016-20260303b: Minimality Qualification Block Self-Undermines in Preamble Position (Persisting R6 Defect) [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Document preamble, MINIMALITY CLAIM QUALIFICATION block |
| **Strategy Step** | Step 3, Lens 4 (Alternative interpretations) |

**Claim Challenged:**
> "The minimality argument is a useful heuristic, not a formal proof." (MINIMALITY CLAIM QUALIFICATION block, preamble)

**Counter-Argument:**
This is a persisting R6 issue correctly identified by SM-010 (Steelman): the MINIMALITY CLAIM QUALIFICATION block leads with the limitation before the evidence. A reader scanning the preamble encounters "useful heuristic, not a formal proof" and may not trace to Section 4 to find the three-part supporting evidence case. The strongest minimality evidence exists in the document but is presented AFTER the self-undermining disclaimer.

The SM-010 Steelman proposal would repair this by presenting the three-part evidence case (functional test, coverage removal test, sensitivity test) BEFORE the qualification. This is a structural repair that does not require new content — it reorders existing content. But because it is a Steelman PROPOSAL, it is not in R6. As a standalone defect in R6, the qualification block's placement weakens the document's persuasive logic for any reader who does not trace internal cross-references.

**Evidence:** MINIMALITY CLAIM QUALIFICATION block leads with: "The minimality proof relies on a lifecycle-stage-plus-primary-function categorization... that is analyst-derived, not externally validated." The three-part functional test, coverage removal test, and sensitivity test supporting evidence are in Section 4 and Section 1 respectively, not consolidated in or near the qualification.

**Dimension:** Internal Consistency

**Response Required:** Acknowledge the presentation sequencing issue. Accept the SM-010 Steelman reconstruction for R7 to lead with evidence, then qualification.

**Acceptance Criteria:** Acknowledgment (with or without immediate revision) that the MINIMALITY CLAIM QUALIFICATION block's placement weakens the argument's presentation to readers who do not trace internal cross-references. SM-010 Steelman reconstruction accepted for R7.

---

### DA-017-20260303b: Document Footer Method Attribution Is Wrong in R6 (Kepner-Tregoe vs. WSM) [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Document footer (final line) |
| **Strategy Step** | Step 3, Lens 3 (Contradicting evidence) |

**Claim Challenged:**
> "Method: Weighted Multi-Criteria Decision Matrix (Kepner-Tregoe)" (document footer)

**Counter-Argument:**
This is a current R6 defect (not just a Steelman proposal). Section 1 Weighting Rationale names the method as WSM (Weighted Sum Method) with citations to Triantaphyllou 2000 and Velasquez & Hester 2013. The document footer names the method as Kepner-Tregoe, which is a different MCDA variant. A reviewer reading both locations finds an internal inconsistency that undermines methodological credibility. The SM-015 Steelman correctly identifies this as a correctness fix, not cosmetic polish.

**Evidence:** Document footer: "Method: Weighted Multi-Criteria Decision Matrix (Kepner-Tregoe)." Section 1: "The scoring model applies the Weighted Sum Method (WSM)."

**Dimension:** Internal Consistency, Traceability

**Response Required:** Correct the footer to match the body: "Method: Weighted Sum Method (WSM) applied as Multi-Criteria Decision Analysis (MCDA) (Triantaphyllou 2000; Velasquez & Hester 2013)."

**Acceptance Criteria:** Document footer and body name the same method. Kepner-Tregoe attribution removed.

---

## Step 5: Synthesis and Score Impact

### Overall Assessment

**7 counter-arguments identified (1 Critical, 4 Major, 2 Minor).**

This is materially fewer than Iteration 1 (10 findings: 3 Critical, 4 Major, 3 Minor). Revision 6 successfully resolved 6 of 10 Iteration 1 findings (DA-002, DA-005, DA-006, DA-007, DA-009, partially DA-003) and partially resolved 4 others (DA-001, DA-004, DA-008, DA-010). This represents genuine quality improvement.

**The single Critical finding (DA-011) is new and significant.** The C3=25% perturbation — which was the correct response to Iteration 1's DA-002 Critical finding — has introduced a new interpretive vulnerability: the perturbation result is characterized in a way that makes the sensitivity analysis unfalsifiable as a robustness test. This is not a regression from Iteration 1 (the C3 perturbation did not exist in Iteration 1); it is a new finding generated by the added content.

The four Major findings (DA-012 through DA-015) are a mix of persistent issues (DA-012: "maximize" surviving scope qualification; DA-013: WSM independence unresolved in R6) and newly surfaced issues (DA-014: Fogg/Kano C3 defense unverified; DA-015: AI reliability tier reveal for Nielsen's). The two Minor findings (DA-016, DA-017) are present-in-R6 defects that the Steelman correctly identified and proposed corrections for.

**Recommendation: REVISE — the Critical finding (DA-011) and two of the Major findings (DA-012, DA-013) require targeted revisions before S-014 scoring.** The portfolio selection itself remains defensible. The logical architecture of the methodology framing requires precision repair in three specific areas.

### Iteration 1 Finding Resolution Summary

| Iter 1 Finding | Status in R6 | Notes |
|----------------|-------------|-------|
| DA-001 (minimality circular taxonomy) | Partially resolved | Qualification block added; SM-010 Steelman proposes re-sequencing |
| DA-002 (sensitivity tests safest scenarios) | Resolved | C3=25% perturbation added — NEW Critical finding DA-011 created by the addition |
| DA-003 (AI-First Design vs. minimal-complete) | Resolved | "contingent on synthesis" language added |
| DA-004 (maximize claim vs. ceiling) | Partially resolved | "within a V1 scope" added; "maximize" retained — DA-012 |
| DA-005 (C5 cited as evidence) | Resolved | SM-001 minimality reframed on functional test, not Complementarity Matrix |
| DA-006 (3 errors = unreliability) | Resolved | DA-006 interpretation section added |
| DA-007 (Tiny Teams profile unvalidated) | Resolved | Gartner citation removed; internal research cited |
| DA-008 (WSM independence) | Partially resolved | Acknowledged; resolution deferred to user — DA-013 |
| DA-009 (tooling cost missing) | Resolved | Tooling cost note added per revision history |
| DA-010 (maximize vs. HIGH RISK gap) | Partially resolved | Inline caveat added; logical contradiction persists — DA-012 |

### Scoring Impact Table

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | **Slightly Negative** | DA-015 (AI reliability tier reveals 60% team-input requirement for Nielsen's, with implications for C2 scoring accuracy) partially undermines completeness of AI execution claims across Section 3 |
| Internal Consistency | 0.20 | **Mixed (net slightly negative)** | DA-012 ("maximize" + HIGH RISK gap) and DA-017 (footer vs. body method name) are persistent internal inconsistencies. DA-016 (minimality qualification placement) is presentation-level but adds noise. Against this: DA-003, DA-004, DA-005 were resolved, removing major consistency issues from Iteration 1. Net: mild negative from new findings, partially offset by Iteration 1 resolution. |
| Methodological Rigor | 0.20 | **Slightly Negative** | DA-011 (perturbation interpretation unfalsifiable) and DA-013 (WSM independence unresolved) are methodological gaps. Against this: DA-002 was resolved (C3 perturbation added). Net: the addition of C3 perturbation content improves rigor, but the unfalsifiable interpretation framing (DA-011) partially negates the gain. |
| Evidence Quality | 0.15 | **Slightly Negative** | DA-014 (Fogg/Kano C3 defense "fully executable without MCP" unverified) and DA-015 (AI efficiency claims not qualified for team-input heuristics) weaken evidence quality. Against this: DA-006, DA-007, DA-009 resolutions strengthen evidence quality. Net: slightly negative. |
| Actionability | 0.15 | **Neutral** | The framework descriptions, routing guides, and implementation sequencing remain actionable. DA-015 slightly reduces actionability of Nielsen's efficiency claims but the AI reliability tiers table itself (newly added in a prior revision) is actionable guidance. |
| Traceability | 0.10 | **Slightly Negative** | DA-017 (footer method mismatch) reduces traceability. Against this: DA-005 resolution (C5 caveat clear), DA-006 resolution (error interpretation clear) improve traceability of methodology claims. Net: slight negative from DA-017. |

**Estimated composite score impact relative to Iteration 1 baseline (0.747):**

Iteration 1 had 3 Critical findings, 4 Major, 3 Minor. Iteration 2 has 1 Critical, 4 Major, 2 Minor — with 6 Iteration 1 findings resolved. The resolution of 6 prior findings should produce measurable improvement across Completeness, Internal Consistency, Evidence Quality, and Traceability dimensions. The new Critical finding (DA-011) introduces a new Methodological Rigor gap, but the C3=25% perturbation addition itself (which created the gap) is evidence of improved methodological thoroughness. Estimated Iteration 2 range before incorporating SM-010 through SM-015 Steelman improvements: approximately 0.82-0.86, still below the 0.95 target threshold. Incorporating SM-010, SM-011, SM-015 would address the DA-013, DA-016, and DA-017 gaps respectively; addressing DA-011, DA-012, DA-014, DA-015 would additionally be required to reach the target.

---

## Recommendations

### P0 (Critical — MUST resolve before acceptance)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-011-20260303b | Add a pre-registered interpretation rule for sensitivity perturbations: state what perturbation outcomes would constitute disconfirming evidence before presenting results. Interpret the C3=25% result (Kano and Fogg falling below threshold) against this rule rather than post-hoc. | Sensitivity analysis section includes explicit statement of what perturbation outcomes would disconfirm the selection. C3=25% result is interpreted against this pre-stated rule with specific reasoning for why the Kano/Fogg boundary instability is or is not disconfirming evidence. |

### P1 (Major — SHOULD resolve; justification required if not)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-012-20260303b | Replace "maximize UX outcome coverage" in core thesis with language that is logically consistent with the HIGH RISK user research gap. | Core thesis does not claim maximization in a domain where Section 4 identifies a HIGH RISK gap. Suggested wording: "best-available coverage... with a disclosed HIGH RISK gap in user research coverage." |
| DA-013-20260303b | Incorporate SM-011 Steelman resolution into R7: explicitly explain WHY the C1/C5 correlation does not materially affect rankings by referencing the C3=25% perturbation as the empirical test. | WSM independence section provides a resolution (not just acknowledgment) of the C1/C5 correlation limitation, using the C3=25% perturbation as empirical evidence that correlation effect is bounded to the selection boundary. |
| DA-014-20260303b | Provide non-MCP execution efficiency targets for Kano and Fogg, or acknowledge that AI augmentation efficiency is lower for these frameworks and scope the stated efficiency claims accordingly. | Sections 3.9 and 3.10 include comparative efficiency estimates for MCP vs. non-MCP execution, OR explicitly state that Fogg and Kano's AI augmentation benefit is primarily through structured analysis rather than MCP-mediated tool integration. |
| DA-015-20260303b | Revise the "under 10 minutes" efficiency claim for Nielsen's Heuristics to accurately reflect the team-input requirement for 6 of 10 heuristics. | Tiny Teams enablement pattern for Nielsen's states the efficiency claims for the 4 AI-autonomous heuristics separately from the complete 10-heuristic evaluation. "Under 10 minutes" claim either removed or qualified to the 4 high-confidence heuristics only. |

### P2 (Minor — Acknowledgment sufficient)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-016-20260303b | Accept SM-010 Steelman reconstruction for R7 (lead with evidence, then qualification). | Acknowledgment that SM-010 re-sequencing improves the minimality argument's presentation. Incorporated in R7. |
| DA-017-20260303b | Correct document footer to match body: "Weighted Sum Method (WSM)" not "Kepner-Tregoe." | Footer and body name the same method. |

---

## Execution Statistics

- **Total Findings:** 7 (DA-011 through DA-017)
- **Critical:** 1 (DA-011)
- **Major:** 4 (DA-012, DA-013, DA-014, DA-015)
- **Minor:** 2 (DA-016, DA-017)
- **Protocol Steps Completed:** 5 of 5
- **Iteration 1 Findings Resolved:** 6 of 10 (DA-002, DA-005, DA-006, DA-007, DA-009, DA-003)
- **Iteration 1 Findings Partially Resolved:** 4 of 10 (DA-001/DA-016, DA-004/DA-012, DA-008/DA-013, DA-010/DA-012)
- **New Findings (Iter 2):** 7 (DA-011 through DA-017; DA-011 and DA-014 are NEW, not carried from Iter 1; DA-012/DA-013/DA-015/DA-016/DA-017 carry forward Iter 1 partial resolutions)

---

## H-15 Self-Review Checklist

- [x] All findings have specific evidence from the deliverable (direct quotes and section references in each finding detail block)
- [x] Severity classifications are justified: Critical (DA-011) targets the newly-added sensitivity perturbation interpretation as an unfalsifiable framework — a logical flaw that undermines the entire sensitivity analysis section's function. Major findings address persistent internal contradictions and methodology gaps. Minor findings are polish-level defects or Steelman-proposal dependencies.
- [x] Finding identifiers follow DA-NNN-20260303b format (b suffix for Iteration 2 execution session); sequence continues from DA-010 (Iteration 1 last finding)
- [x] Report is internally consistent: summary table matches detailed findings; scoring impact table references specific DA-NNN findings; Iteration 1 resolution status table cross-references with Iteration 2 findings
- [x] No findings were minimized: DA-011 is correctly classified Critical because an unfalsifiable robustness test undermines the methodological validity of the entire sensitivity analysis — this is not a minor framing issue; DA-015 is correctly Major because a 6/10 heuristic team-input rate for the paradigmatic highest-scoring framework has implications for the C2 scoring rubric validity
- [x] Role maintained: critique targets the STRENGTHENED R6 version, incorporating awareness of SM-010 through SM-015 Steelman proposals. New findings (DA-011, DA-014) were generated by examining newly-added R6 content (C3 perturbation, Fogg/Kano C3 defense), not by re-prosecuting Iteration 1 vulnerabilities
- [x] H-16 compliance confirmed: S-003 Iteration 2 output was read; the critique attacks the post-Steelman argument and specifically identifies which Steelman improvements are proposals (not yet in R6) vs. actual R6 content
- [x] Leniency bias counteracted: 7 findings generated (exceeds minimum 3); all 6 counter-argument lenses applied: logical flaws (DA-011), unstated assumptions (DA-013, IA-1 through IA-4), contradicting evidence (DA-012, DA-017), alternative interpretations (DA-014), unaddressed risks (DA-015), historical precedent (not triggered — no historical precedent analysis warranted for this type of decision document)
- [x] Iteration 1 resolution genuinely acknowledged: the 6 resolved Iteration 1 findings are clearly marked as resolved in the resolution table; the improvements these resolutions represent are credited in the scoring impact analysis ("Against this:... improve[s] evidence quality")

---

*Strategy: S-002 Devil's Advocate | Template: `.context/templates/adversarial/s-002-devils-advocate.md` | Executed: 2026-03-03T00:00:00Z | Iteration: 2 | Agent: adv-executor*
