# Strategy Execution Report: Inversion Technique (S-013)

## Execution Context

- **Strategy:** S-013 (Inversion Technique)
- **Template:** `.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Criticality:** C4
- **Goals Analyzed:** 5 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 9

---

## Inversion Report: UX Framework Selection (Weighted Multi-Criteria Analysis)

**Strategy:** S-013 Inversion Technique
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman was applied as part of the C4 tournament sequence (SM-001 through SM-009 Steelman marks present in deliverable confirming prior strengthening)
**Goals Analyzed:** 5 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 9

---

## Summary

The UX Framework Selection analysis presents a multi-criteria decision matrix selecting 10 frameworks for an AI-augmented Tiny Teams UX skill portfolio. Inversion analysis identified 5 primary goals whose inversions reveal 3 Critical and 6 Major assumption vulnerabilities. The most severe cluster concerns the projected AI-First Design framework: the entire AI product UX domain coverage depends on a not-yet-created synthesis deliverable whose scores are projections, not measurements -- if that synthesis fails or diverges from projections, the portfolio has an unmitigated domain gap with no automated fallback trigger. A secondary cluster concerns the Figma single-point-of-failure risk across 6 frameworks and the user research gap: the analysis correctly identifies both as risks but underestimates the operational consequence of both occurring simultaneously. The deliverable is recommended for **REVISE** with targeted mitigations before implementation proceeds.

---

## Findings Summary

| ID | Assumption / Anti-Goal | Type | Confidence | Severity | Evidence | Affected Dimension |
|----|------------------------|------|------------|----------|----------|--------------------|
| IN-001-20260303 | Projected AI-First Design scores will be confirmed by synthesis deliverable | Assumption | Low | Critical | Section 3.8: "All AI-First Design scores are PROJECTED PREDICTIONS"; C4=2/10 | Completeness |
| IN-002-20260303 | No automated gate enforces synthesis deliverable validation before score revision | Anti-Goal | N/A | Critical | Section 3.8: validation gate defined but no enforcement mechanism specified | Methodological Rigor |
| IN-003-20260303 | Figma MCP availability is stable across the 6 dependent frameworks | Assumption | Medium | Critical | Section 1 C3: "Figma is listed as primary MCP for 6 of 10 selected frameworks" | Internal Consistency |
| IN-004-20260303 | C5 (Complementarity) self-referential scoring provides independent portfolio validation | Assumption | Low | Major | Section 1 C5: "C5 scores do NOT provide independent validation of the selection" | Evidence Quality |
| IN-005-20260303 | Single-rater scoring bias does not affect the top-10 selection | Assumption | Medium | Major | Section 1 FM-001: "All 40 frameworks scored by a single analyst. No inter-rater reliability check." | Evidence Quality |
| IN-006-20260303 | The 10-framework ceiling is an appropriate portfolio scope constraint | Assumption | Low | Major | Section header CC-002: "10-framework ceiling is an analyst-assumed constraint, not a user-specified requirement" | Completeness |
| IN-007-20260303 | User research gap does not block the portfolio from achieving its core thesis | Assumption | Medium | Major | Section 4 HIGH RISK gap: "does not include a dedicated remote user research framework" | Completeness |
| IN-008-20260303 | The community MCP servers used in skills will remain production-ready at implementation time | Assumption | Low | Major | Section 1 C3 FM-002: "Community MCP servers...have not been independently verified" | Methodological Rigor |
| IN-009-20260303 | Synthesis hypothesis outputs from AI will be distinguishable from validated findings by non-specialist users | Assumption | Medium | Major | Section 1 AI Execution Mode Taxonomy: distinction between "Deterministic execution" and "Synthesis hypothesis" | Actionability |

---

## Detailed Findings

### IN-001-20260303: AI-First Design Projected Scores Unvalidated [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.8 (AI-First Design), Section 2 (Scoring Matrix row 8) |
| **Strategy Step** | Step 4: Stress-Test Each Assumption |

**Type:** Assumption
**Original Assumption:** The synthesized AI-First Design framework will achieve C1=10/10 (Tiny Teams Applicability) and C2=8/10 (Composability) as projected, earning its 7.80 weighted total and justifying its rank-8 position.
**Inversion:** The synthesis deliverable, once produced, reveals that the synthesized framework requires UX specialist expertise (reducing C1 to 6-7), or that the framework phases cannot be discretely encoded as a Jerry agent workflow (reducing C2 to 5-6). Under C1=6, C2=6 the recalculated score is: 6×0.25+6×0.20+8×0.15+2×0.15+10×0.15+7×0.10 = 1.50+1.20+1.20+0.30+1.50+0.70 = **6.40** -- dropping AI-First Design from rank 8 to approximately rank 18-20, below Service Blueprinting (7.40).
**Plausibility:** High. AI product UX is inherently specialized -- practitioners with AI UX expertise are rare, and synthesizing multi-source guidance into a non-specialist-accessible framework is a non-trivial intellectual task. The sources cited (Nudelman, Fard, NN Group) target practitioners, not generalists.
**Confidence:** Low (the scores are projections by definition)
**Consequence:** The portfolio's AI product UX domain coverage disappears. The fallback (Service Blueprinting) is documented in the analysis but there is no automated trigger to execute the fallback if synthesis produces lower-than-projected scores. Without this fallback, the portfolio silently loses its AI-product UX domain coverage -- the precise gap that justified AI-First Design's inclusion.
**Evidence:** "All AI-First Design scores are PROJECTED PREDICTIONS about a framework-to-be-synthesized, not measurements of an existing framework's properties. The C1=10 and C2=8 scores are predictions about what the synthesized framework will achieve if the synthesis deliverable succeeds." (Section 3.8 DA-003 CATEGORY NOTICE)
**Dimension:** Completeness (0.20 weight)
**Mitigation:** Add explicit score re-validation gate: before any sub-skill implementation begins, the synthesis deliverable's actual C1 and C2 properties must be scored using the same rubric as all other frameworks, and if the recalculated total falls below Fogg (7.60), the automatic trigger is to replace AI-First Design with Service Blueprinting. This gate must be a worktracker acceptance criterion, not an advisory recommendation.
**Acceptance Criteria:** The synthesis Enabler worktracker entity includes a blocking acceptance criterion: "Independent scoring of synthesized framework's C1 and C2 properties using the same rubric as the scoring matrix must yield a weighted total >= 7.60 before /ux-ai-first implementation is approved." If not met, the worktracker item blocks implementation and automatically recommends Service Blueprinting substitution.

---

### IN-002-20260303: Validation Gate Has No Enforcement Mechanism [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.8, Section 2 (score notation) |
| **Strategy Step** | Step 2: Invert the Goals (Anti-Goals) |

**Type:** Anti-Goal
**Original Assumption (implicit):** The validation gate described in Section 3.8 ("AI-First Design's sub-skill implementation is CONDITIONAL on the synthesis deliverable demonstrating the projected C1=10 and C2=8 properties through expert review") will actually be enforced before implementation proceeds.
**Inversion:** To guarantee the validation gate fails, do the following: (a) create the synthesis deliverable, (b) note that the analysis says the gate must be cleared but the only enforcement is the analyst's intention -- no worktracker entity exists (the analysis explicitly notes "The worktracker entity does not yet exist"), (c) start implementation immediately because the BLOCKING prerequisite has no formal tracking entity to block against, and (d) observe that the score revision requirement ("these scores MUST be revised") has no automated verification mechanism.
**Plausibility:** High. The analysis itself notes: "creating it is a required action before the PROJ-020 implementation phase starts" -- confirming the enforcement mechanism does not yet exist. Intent without enforcement is not a gate.
**Consequence:** /ux-ai-first gets implemented against unvalidated projected scores. If the synthesis reveals lower properties, the skill ships against a framework that didn't earn its portfolio slot. The portfolio user experiences this as a skill that doesn't work as advertised -- the non-specialist cannot execute it -- validating the exact concern the maturity score was meant to surface.
**Evidence:** "The worktracker entity does not yet exist; creating it is a required action before the PROJ-020 implementation phase starts." (Section 3.8, Prerequisite management) AND "DA-003 CATEGORY NOTICE: These scores MUST be revised before implementation proceeds." (no mechanism for this revision is specified)
**Dimension:** Methodological Rigor (0.20 weight)
**Mitigation:** Create the worktracker Enabler entity for AI-First Design Framework Synthesis before this analysis document is finalized. The acceptance criteria in IN-001 must be encoded as blocking criteria in that entity. The analysis should be updated to reference the worktracker entity ID (once created) so there is a traceable link between the analysis recommendation and the enforcement mechanism.
**Acceptance Criteria:** Section 3.8 contains a worktracker entity ID reference (e.g., "EN-XXX: AI-First Design Framework Synthesis") with blocking status notation. The entity exists in the PROJ-020 worktracker with IN-001's acceptance criteria encoded as a blocking acceptance condition.

---

### IN-003-20260303: Figma Single-Point-of-Failure Across 6 Frameworks [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 1 C3 (Criterion 3 description), Section 7.3 (MCP Maintenance Contract) |
| **Strategy Step** | Step 3: Map All Assumptions -- Technical/Environmental |

**Type:** Assumption
**Original Assumption:** Figma MCP remains available as the primary integration for Design Sprint, Nielsen's Heuristics, Atomic Design, HEART (indirect), Microsoft Inclusive Design, and AI-First Design. The analysis classifies it as "Native MCP (Official)" providing "strong stability signal."
**Inversion:** Figma restricts or monetizes MCP API access (the analysis itself documents precedent: "Dev Mode became paid in 2023; additional pricing changes in 2024"), causing 6 of 10 sub-skills to simultaneously lose their primary integration path. Each sub-skill's fallback (Storybook for Atomic Design, Miro for Design Sprint, screenshots for Nielsen's Heuristics) provides partial coverage, but no sub-skill maintains full functionality without Figma. The `/user-experience` skill appears to function but delivers degraded outputs across 60% of its portfolio without surfacing this to the user.
**Plausibility:** Medium-to-High. Figma has a documented history of API access monetization. The transition from free to paid for Dev Mode (2023) affected a large segment of professional users. An MCP-specific monetization event is not implausible, particularly if Figma determines that AI agent automation represents commercial use at scale.
**Consequence:** 6 of 10 sub-skills degrade simultaneously. The analysis documents fallback paths in Section 1 (Figma dependency risk [IN-002 -- 2026-03-02]) but: (a) fallback paths are incomplete for Nielsen's Heuristics (screenshots provide image input but do not replace structured component evaluation), (b) fallback paths are not surfaced in the sub-skill routing table (Section 7.3) which a user would consult at invocation, (c) no degraded-mode output labeling is specified for the 6 affected skills (unlike the explicit degraded-mode behavior documented for HEART and Fogg), and (d) the simultaneous degradation of 60% of the portfolio is not characterized as a portfolio-level risk, only as a per-skill footnote.
**Evidence:** "Figma is listed as a required or primary MCP integration for 6 of the 10 selected frameworks... This creates a single point of failure... The Figma MCP is classified as 'Native (Official)' providing strong stability signal, but this classification reflects current status, not a contractual guarantee." (Section 1 C3, Figma dependency risk [IN-002 -- 2026-03-02])
**Dimension:** Internal Consistency (0.20 weight)
**Mitigation:** (1) Add portfolio-level Figma degradation scenario to Section 7.3 MCP Maintenance Contract: if Figma MCP becomes unavailable, the maintenance owner must activate documented fallbacks across all 6 affected sub-skills simultaneously. (2) Complete the fallback documentation gap for Nielsen's Heuristics (currently "design screenshots can be provided as image inputs" -- specify precisely how the skill's heuristic evaluation outputs change in this mode). (3) Add a Figma MCP health check to the quarterly audit cadence with explicit escalation criteria (e.g., if Figma announces pricing changes for API access, trigger sub-skill fallback review before the change takes effect). (4) Evaluate whether a Penpot (open-source, official experimental MCP) bootstrap path reduces the single-vendor dependency for at least the most critical sub-skills.
**Acceptance Criteria:** Section 7.3 contains a portfolio-level Figma degradation scenario with explicit per-skill fallback status (complete/partial/none) for all 6 affected sub-skills. Nielsen's Heuristics has a complete non-Figma fallback path documented. Quarterly audit cadence includes a Figma pricing/access change watch item.

---

### IN-004-20260303: C5 Circular Scoring Provides No External Portfolio Validation [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 (Criterion 5 description), Section 2 (Scoring Matrix) |
| **Strategy Step** | Step 3: Map All Assumptions -- Process assumptions |

**Type:** Assumption
**Original Assumption:** The six-criterion scoring methodology provides sufficient external validation that the 10 selected frameworks form an optimal portfolio, with C5 providing portfolio composition validation.
**Inversion:** C5 is explicitly self-referential (the analysis documents this in FM-003 and DA-002): frameworks score high on C5 because the other high-scoring frameworks are already included, which is a function of their own prior rankings, creating a circularity. If the analysis had started with a different provisional top-10 in Round 1, the C5 scores would reshuffle. The validation is internally consistent but not externally validated.
**Plausibility:** High -- the analysis itself confirms this limitation explicitly and thoroughly.
**Consequence:** Three of the four weakest selections (Microsoft Inclusive Design 8.00, AI-First Design 7.80 projected, Kano 7.65, Fogg 7.60) each hold their positions partly because C5 (15% weight) was assigned after their C1/C2 positions were established. An independently assembled portfolio starting from different assumptions might produce a materially different bottom-4. The compression zone (ranks 7-12, scores 7.35-8.00) means the selection outcome is as much a function of the two-pass methodology as of the frameworks' objective merits.
**Evidence:** "The practical implication: a framework scoring 10/10 on C5 does so because the selected portfolio has no other framework in its category -- if the portfolio had been assembled differently, the C5 scores would reshuffle. C5 self-referentiality is methodologically appropriate for portfolio optimization but should not be cited as external evidence of selection quality." (Section 1, C5 complementarity methodology caveat DA-002 response)
**Dimension:** Evidence Quality (0.15 weight)
**Mitigation:** Add an external validation step using a methodology independent of the scoring matrix. The most practical option for this deliverable is a UX practitioner interview or a structured comparison against a published UX skill inventory (e.g., UXPA's published competency framework or NN Group's UX discipline taxonomy). The goal is not to replace the scoring matrix but to confirm that no critical domain was missed due to the circular C5 scoring. At minimum, document clearly in the deliverable's summary that the C5 validation is a consistency check, not external confirmation, and that the analysis has not been validated against any external practitioner-assembled portfolio.
**Acceptance Criteria:** A cross-reference comparison against at least one external UX competency framework or practitioner inventory is added to Section 4 Coverage Analysis, confirming that the 10 selected domains map to recognized UX practice areas. Alternatively, a qualified caveat in the Executive Summary explicitly states the internal-only nature of the validation.

---

### IN-005-20260303: Single-Rater Bias Affects Non-Selected Framework Comparison Baseline [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 (FM-001 Methodology limitations), Section 2 (Full Scoring Matrix) |
| **Strategy Step** | Step 3: Map All Assumptions -- Resource assumptions |

**Type:** Assumption
**Original Assumption:** Although the top 10 selections had partial adversarial validation (RT-002, RT-003, DA-007 corrections), the full 40-framework scoring provides a reliable comparison baseline with ±0.25 uncertainty adequately communicating the precision limits.
**Inversion:** The ±0.25 uncertainty band on non-selected frameworks produces meaningful boundary effects. The analysis itself demonstrates this: Double Diamond (7.45) and Service Blueprinting (7.40) both enter the top 10 under a +0.25 shift (Section 1 FM-001 extension). However, the underlying assumption is that rater bias is uniform (±0.25 applied equally to all non-selected frameworks). Systematic bias in a specific criterion -- for example, consistently scoring frameworks higher on C1 for frameworks the analyst is more familiar with -- would produce directional shifts, not symmetric uncertainty. This directional risk is not characterized.
**Plausibility:** Medium. The correction history demonstrates systematic adjustments (RT-002: HEART C3 corrected 6→4; RT-003: AI-First Design maturity corrected; DA-007: Design Sprint C1 corrected 10→8) -- all in the direction of *downward* correction from initial scores. This pattern suggests initial scores may have a known optimism bias (initial scores trend high, corrections trend down). If this pattern applies to non-selected frameworks, some may be systematically underscored.
**Consequence:** The gap between Fogg (#10, 7.60) and Service Blueprinting (#12, 7.40) is 0.20 points -- less than the ±0.25 uncertainty band. This is a known and documented compression zone. However, the corrections applied to top-10 frameworks all trended downward. If the same downward correction pattern applies to Service Blueprinting (currently uncorrected), its score might increase rather than decrease under independent review, strengthening rather than weakening the case for its inclusion.
**Evidence:** "All 40 frameworks were scored by a single analyst (ps-analyst). No inter-rater reliability check was performed on the full matrix. Red Team adversarial review (S-001) identified three scoring errors... that were corrected through adversarial review rather than a second rater." (Section 1 FM-001) AND "Revision 4 (S-011 CV-001 through CV-008): Arithmetic corrections applied to 7 non-selected framework totals" confirming non-selected scores were corrected but not independently validated.
**Dimension:** Evidence Quality (0.15 weight)
**Mitigation:** For the compression zone frameworks specifically (Double Diamond 7.45, Service Blueprinting 7.40), conduct a structured secondary review of their C1 and C2 scores (the two highest-weight criteria) using a second evaluator or structured rubric verification. This is a targeted, low-cost intervention that addresses the highest-risk boundary. Document the review outcome in Section 1 FM-001 with the result: if scores hold, confidence in the selection boundary increases; if scores shift, the selection should be reconsidered.
**Acceptance Criteria:** FM-001 includes a note on whether compression-zone frameworks (Double Diamond, Service Blueprinting) were subjected to secondary scoring validation on C1 and C2. If yes, the result is documented. If not feasible, FM-001 explicitly names this as a remaining limitation with the specific implication for the selection boundary.

---

### IN-006-20260303: 10-Framework Ceiling Is Unvalidated Analyst Assumption [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 header (CC-002 disclosure) |
| **Strategy Step** | Step 1: State the Goals -- Implicit goal identification |

**Type:** Assumption
**Original Assumption:** A portfolio of 10 frameworks is the appropriate scope for the `/user-experience` skill, providing sufficient domain coverage without overloading the user with options.
**Inversion:** To guarantee the portfolio fails its coverage goal, select a ceiling that creates exactly enough room for high-scorers but excludes the most operationally critical near-threshold frameworks. The current ceiling does precisely this: Service Blueprinting (7.40, strong for multi-channel service products) and Cognitive Walkthrough (6.70, strong for complex navigation triage) are both excluded. Section 4 identifies coverage gaps in IA and service design that would be filled by exactly these two excluded frameworks.
**Plausibility:** High -- the analysis itself flags this. CC-002 states: "The 10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions, not a user-specified requirement."
**Consequence:** The ceiling assumption creates a false trade-off between coverage completeness and portfolio manageability. If 12 frameworks are operationally viable (the analysis suggests they are, naming the two additions explicitly), the current 10-framework ceiling leaves documented coverage gaps that the analysis acknowledges are real product risks (service design gap, information architecture gap). The ceiling assumption is the mechanism by which these gaps persist.
**Evidence:** "The 10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions, not a user-specified requirement. If implementation capacity or portfolio scope considerations permit additional frameworks, Service Blueprinting (rank #12, score 7.40) and Cognitive Walkthrough (rank #17, score 6.70) are the strongest additions that would close documented gaps." (CC-002, document header)
**Dimension:** Completeness (0.20 weight)
**Mitigation:** Escalate the 10-framework ceiling question to explicit user confirmation before implementation proceeds. The analysis already identifies this as requiring user confirmation (CC-002: "Confirm the ceiling is acceptable for the intended implementation phase before proceeding"). The finding here is that this confirmation has not been documented as a blocking prerequisite in the worktracker. Add a worktracker item: "User confirms or modifies the 10-framework ceiling before implementation begins; if ceiling is raised to 11-12, Service Blueprinting and Cognitive Walkthrough are added per the analysis."
**Acceptance Criteria:** A documented user decision on the framework ceiling exists in the worktracker (either "10 confirmed" with user sign-off, or "ceiling raised to N" with the additional frameworks identified). This decision gates implementation start.

---

### IN-007-20260303: User Research Gap Creates Systemic Validation Risk for Portfolio Claims [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 4 (HIGH RISK gap), Section 3.6 (JTBD data sufficiency), Section 3.2 (Design Sprint Friday testing fallback) |
| **Strategy Step** | Step 2: Invert the Goals -- Anti-goals for the "maximize UX outcome coverage" claim |

**Type:** Anti-Goal
**Original Assumption (implicit):** The portfolio achieves its stated thesis of "maximizing UX outcome coverage for deliverable-focused UX activities" despite lacking a dedicated user research framework.
**Inversion:** To guarantee the portfolio fails its coverage thesis, construct a scenario where the most common reason for poor UX outcomes -- building for the wrong users with wrong assumptions -- is not addressable by any framework in the portfolio. This is not a hypothetical: the analysis documents it as a "HIGH RISK gap." The inversion question is: does the analysis adequately reflect this gap in the coverage claims, or does it understate it?
**Plausibility:** High -- the gap is real and documented. The concern surfaced by inversion is that the analysis's mitigation language ("minimum viable research, not comprehensive") understates the operational consequence for teams who rely on this analysis for guidance.
**Consequence:** A team following this analysis in good faith selects JTBD + Design Sprint as their research methods. For consumer products targeting specialized populations (e.g., senior users, users with disabilities, non-English speakers), or products entering competitive markets, these minimum-viable methods produce systematically biased outputs -- AI-generated job statements from App Store reviews reflect the existing user population, not the target one. Teams following the analysis's guidance may build confidently on a research foundation that the analysis itself acknowledges is insufficient.
**Evidence:** "Products with untested user assumptions -- particularly consumer products, products for specialized populations, or products entering competitive markets -- SHOULD NOT rely on these alone." (Section 4 HIGH RISK gap) AND "AI-generated personas and simulated usability testing reflect training data biases, not the team's specific user population." AND "The UX industry consensus (NN Group, Baymard Institute, JTBD practitioners) is that real user contact is the empirical foundation of UX quality and is not substitutable by AI synthesis alone."
**Dimension:** Completeness (0.20 weight)
**Mitigation:** The analysis already contains the correct warning language. The gap is in *presentation weight*: the HIGH RISK warning is buried in Section 4 rather than surfaced at the top-level scope boundary alongside CC-001 and CC-002. Move the user research gap warning to the document header, co-located with the existing scope boundary notices, so that users reading only the summary and framework descriptions encounter this constraint before relying on the selected portfolio. The warning should include the specific context categories (consumer products, specialized populations, competitive markets) as the scope where this analysis is insufficient as the primary research guide.
**Acceptance Criteria:** A scope boundary notice equivalent in visibility to CC-001 and CC-002 appears in the document header or executive summary stating the user research limitation and the categories of products where this analysis is insufficient without supplementary research methods.

---

### IN-008-20260303: Community MCP Production Readiness Assumed at Implementation Time [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 C3 (FM-002 Community MCP caveat), Section 3.2 (Design Sprint Whimsical), Section 3.9 (Kano Model) |
| **Strategy Step** | Step 3: Map All Assumptions -- Environmental/Temporal |

**Type:** Assumption
**Original Assumption:** The community MCP servers (Whimsical for Design Sprint as secondary alternative, Sketch, LottieFiles) will remain production-ready and actively maintained at the time sub-skills are implemented.
**Inversion:** A community MCP server relied upon as a secondary alternative (e.g., Whimsical for Design Sprint when Figma MCP degrades) becomes unmaintained or incompatible between the time this analysis was written (2026-03-02) and implementation. Given that community MCP servers are third-party maintained with no contractual SLA, this is not a low-probability event -- MCP ecosystem churn is high in early-adoption phases.
**Plausibility:** High. The analysis explicitly acknowledges this: FM-002 states that community MCPs "have not been independently verified for current maintenance status, version compatibility, or production uptime." The analysis defines an acceptable maintenance signal (GitHub repository with a commit within 6 months) but does not verify this signal at analysis time. The gap between analysis date and implementation could introduce undetected MCP drift.
**Consequence:** A Design Sprint fallback that relies on Whimsical as the non-Figma alternative may find Whimsical's community MCP non-functional. Since this is a secondary fallback (not a primary dependency), the immediate consequence is limited -- but it means the "documented fallback path" is not a validated fallback path, it is a theoretical one. In a scenario where Figma MCP also degrades (IN-003), the combined failure leaves Design Sprint without an operational prototyping integration.
**Evidence:** "Community MCP servers (Whimsical, LottieFiles, Sketch) are listed as available integrations based on the mcp-design-tools-survey.md snapshot at analysis time. These servers are third-party maintained and have not been independently verified for current maintenance status, version compatibility, or production uptime." (Section 1 C3, FM-002)
**Dimension:** Methodological Rigor (0.20 weight)
**Mitigation:** Before sub-skill implementation begins, verify community MCP maintenance status using the analysis's own criteria (GitHub repository, last commit within 6 months of implementation date). Add this verification to the implementation checklist in Section 7.3 MCP Maintenance Contract. If a community MCP fails the verification, the sub-skill implementation removes that integration from the fallback path before shipping, rather than shipping with a documented-but-unverified fallback.
**Acceptance Criteria:** Section 7.3 MCP Maintenance Contract includes a pre-implementation verification step: "Verify community MCP repositories (list them) have commits within 6 months of implementation date. Remove from fallback documentation any community MCPs that fail this check." This verification is a prerequisite gate for implementation, not an advisory.

---

### IN-009-20260303: Non-Specialists Will Misidentify Synthesis Hypothesis Outputs as Validated Findings [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 (AI Execution Mode Taxonomy), Section 3.1 (Nielsen's AI Reliability Tiers), Section 3.6 (JTBD data sufficiency) |
| **Strategy Step** | Step 2: Invert the Goals -- Anti-goals for AI augmentation quality |

**Type:** Assumption
**Original Assumption:** The analysis's "Synthesis hypothesis" output labeling and non-specialist guidance will be sufficient to prevent non-specialist users from treating AI-synthesized outputs as validated findings.
**Inversion:** A non-specialist receives a structurally-correct, plausible-sounding JTBD job statement generated by AI from 2 App Store reviews (below the MEDIUM confidence threshold of 3-9 data points). The skill correctly labels it "LOW confidence -- hypothesis only." The non-specialist reads "hypothesis" as "good starting point I can work from immediately" rather than "do not make major product decisions on this without additional validation." The confidence label is present but its operational meaning is not universally understood by non-specialists.
**Plausibility:** High. "Synthesis hypothesis" is UX research jargon. Non-specialists are the explicit target audience for the majority of these sub-skills (C6 Accessibility scores for the selected frameworks average ~8/10). The analysis's own documentation of the risk acknowledges it: "Plausible-sounding outputs may reflect training data biases rather than the team's specific user population." The risk is real; the question is whether the labeling convention is sufficient mitigation.
**Consequence:** Non-specialist teams make major product decisions (feature roadmap, marketing positioning, user acquisition targeting) anchored to AI-generated synthesis hypotheses they believed were validated. The skill technically fulfilled its contract (labeled the output correctly) but the label did not change behavior. This is the highest-frequency failure mode for AI-augmented UX work in the target user population.
**Evidence:** "AI synthesis of qualitative data routinely produces outputs that are structurally correct and plausible-sounding but anchored to the training data's generalized understanding of the product category rather than the specific team's user population. This applies beyond JTBD to any step where AI synthesizes qualitative inputs." (Section 1, AI Execution Mode Taxonomy) AND "Non-specialists should verify all synthesis hypothesis outputs through at least minimal human validation (expert review, 2-3 user data points, or a Switch interview) before treating them as strategic anchors."
**Dimension:** Actionability (0.15 weight)
**Mitigation:** Replace confidence labels (LOW/MEDIUM/HIGH) with behavioral directives that specify the required action for each level. Current: "LOW confidence -- hypothesis only" (informational). Proposed pattern: "LOW confidence -- DO NOT use this output for product decisions without completing [specific validation action] first. To validate, do: [specific next step]." This converts the label from a warning to a conditional gate. The analysis already defines the validation steps (Switch interviews for JTBD, 2-3 user data points for synthesis) -- the gap is that these are stated in separate sections rather than embedded in the confidence label definition.
**Acceptance Criteria:** The AI Execution Mode Taxonomy table in Section 1 and the data sufficiency table in Section 3.6 specify behavioral directives (required next action) for each confidence level, not just confidence labels. Each sub-skill description that uses synthesis hypothesis outputs specifies the minimum validation action required before proceeding.

---

## Recommendations

### Critical Assumptions (MUST Mitigate)

| Finding | Mitigation Action | Acceptance Criteria |
|---------|-----------------|---------------------|
| IN-001-20260303 | Add explicit score re-validation gate to synthesis Enabler worktracker entity as a blocking acceptance criterion | Synthesis Enabler entity exists with blocking AC: score re-validation required if total drops below 7.60 |
| IN-002-20260303 | Create the synthesis Enabler worktracker entity NOW; link it from Section 3.8 with entity ID | Section 3.8 references worktracker Enabler entity ID; entity exists and is in BLOCKED state pending analysis approval |
| IN-003-20260303 | Add portfolio-level Figma degradation scenario to Section 7.3; complete Nielsen's Heuristics non-Figma fallback; add Figma pricing watch to quarterly audit | Section 7.3 contains per-skill Figma fallback status table; Nielsen's fallback path is complete; Figma watch item in audit cadence |

### Major Assumptions (SHOULD Mitigate)

| Finding | Mitigation Action | Acceptance Criteria |
|---------|-----------------|---------------------|
| IN-004-20260303 | Add external validation cross-reference or qualified caveat about C5 internal-only validation | Section 4 or Executive Summary contains explicit caveat with recommended external validation path |
| IN-005-20260303 | Conduct secondary C1/C2 review for Double Diamond and Service Blueprinting specifically | FM-001 documents whether compression-zone secondary review was performed |
| IN-006-20260303 | Escalate 10-framework ceiling to explicit user confirmation with worktracker blocking item | Worktracker item exists for ceiling confirmation as a blocking prerequisite to implementation start |
| IN-007-20260303 | Move HIGH RISK user research gap warning to document header alongside CC-001, CC-002 | Document header contains scope boundary notice equivalent to CC-001/CC-002 for user research limitation |
| IN-008-20260303 | Add community MCP pre-implementation verification step to Section 7.3 MCP Maintenance Contract | Section 7.3 includes community MCP GitHub verification as a pre-implementation gate |
| IN-009-20260303 | Replace confidence labels with behavioral directives specifying required validation action | AI Execution Mode Taxonomy and per-skill data sufficiency tables specify required next action per confidence level |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | **Negative** | IN-001 (AI-First Design projected coverage), IN-006 (10-framework ceiling excludes documented gaps), IN-007 (user research gap understated at header level). Three critical-to-major findings reduce confidence that the portfolio achieves its stated "maximize coverage" thesis for all user contexts. |
| Internal Consistency | 0.20 | **Negative** | IN-003 (Figma SPOF): 6 of 10 frameworks share a critical dependency whose degradation is not handled consistently across the portfolio. The per-skill fallback documentation exists but is inconsistent in completeness and absent at the portfolio level. |
| Methodological Rigor | 0.20 | **Negative** | IN-002 (enforcement gap for validation gate), IN-008 (community MCP unverified at analysis time). The methodology defines correct gates and checks but leaves critical ones unimplemented or unverified. |
| Evidence Quality | 0.15 | **Negative** | IN-004 (C5 circularity), IN-005 (single-rater bias in compression zone). The scoring evidence is internally rigorous but lacks external validation precisely at the decision boundary where it matters most (ranks 7-12 compression zone). |
| Actionability | 0.15 | **Mixed-Negative** | IN-009 (synthesis hypothesis labeling insufficient for non-specialists). The sub-skill descriptions provide actionable guidance for practitioners. However, the confidence labeling system -- which is the primary mechanism for non-specialist safety in AI-synthesis-heavy frameworks -- does not translate to behavioral directives. The analysis tells non-specialists what to do but not with the specificity needed to change behavior at point of output receipt. |
| Traceability | 0.10 | **Positive** | The analysis's extensive cross-referencing (SM-NNN, DA-NNN, RT-NNN, IN-NNN, FM-NNN, CC-NNN, CV-NNN markers), correction history, evidence table, and assumption declarations provide strong traceability. Prior adversarial strategy outputs are consistently cited. No finding here. |

---

## Execution Statistics

- **Total Findings:** 9
- **Critical:** 3
- **Major:** 6
- **Minor:** 0
- **Protocol Steps Completed:** 6 of 6

---

## Anti-Goal Inventory

**Goal 1: Select 10 frameworks that maximize UX outcome coverage for Tiny Teams**
Anti-goal: "To guarantee coverage failure, select a ceiling that excludes the frameworks filling documented gaps, and ensure the one synthesized framework cannot have its coverage confirmed before implementation."
Deliverable vulnerability: IN-001 (projected scores unvalidated), IN-006 (ceiling unvalidated), IN-007 (user research gap understated).

**Goal 2: Enable non-specialists to execute UX frameworks with AI augmentation**
Anti-goal: "To guarantee non-specialist execution failure, provide confidence labels that look informative but do not change behavior."
Deliverable vulnerability: IN-009.

**Goal 3: Provide a non-redundant, well-justified portfolio of frameworks**
Anti-goal: "To guarantee portfolio quality failure, use a validation criterion that is self-referential and cannot provide external confirmation of selection quality."
Deliverable vulnerability: IN-004, IN-005.

**Goal 4: Provide an operationally stable skill portfolio with MCP integrations**
Anti-goal: "To guarantee operational instability, architect 60% of the portfolio against a single vendor with a documented history of API monetization, without a unified degradation handling protocol."
Deliverable vulnerability: IN-003, IN-008.

**Goal 5: Provide clear implementation prerequisites so development can proceed immediately**
Anti-goal: "To guarantee implementation proceeds on faulty assumptions, define validation gates as advisory text without corresponding worktracker enforcement mechanisms."
Deliverable vulnerability: IN-002.

---

*Strategy Template: S-013 Inversion Technique v1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Created: 2026-03-03*
*Agent: adv-executor*
