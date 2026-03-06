# Inversion Report: /user-experience Skill -- AI-Augmented UX for Tiny Teams

**Strategy:** S-013 Inversion Technique
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied in prior iterations (I3, I5 confirmed in deliverable's adversarial validation section)
**Goals Analyzed:** 6 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 4

---

## Summary

Inversion analysis against the I8 post-R7 revision identifies 0 Critical, 1 Major, and 7 Minor findings. The deliverable has successfully addressed all prior Critical and Major assumption vulnerabilities identified in previous iterations through systematic mitigation. The one remaining Major finding (IN-001) concerns the wave model's structural constraint on adoption: the sequential dependency chain assumes teams will commit to building through all five waves, but this assumption has not been stress-tested against the most plausible failure mode -- teams that extract value from Wave 1 and then plateau indefinitely. Seven Minor findings surface residual assumption gaps in MCP reliability framing, solo practitioner data collection prerequisites, the "two people doing what used to take eight" throughput claim, the AI-First Design conditional expiry mechanism, expert panel bootstrapping, the 90-day cross-validation deadline governance, and the wave re-entry guard enforcement independence. Overall assessment: **ACCEPT with targeted mitigation for IN-001**; the deliverable is structurally robust and recommendation-ready at C4 quality.

---

## Findings Summary

| ID | Assumption / Anti-Goal | Type | Confidence | Severity | Evidence | Affected Dimension |
|----|------------------------|------|------------|----------|----------|--------------------|
| IN-001-iter8 | Wave model assumes teams will progress through dependencies; plateau after Wave 1 is the dominant failure mode and is not addressed | Anti-Goal | Medium | Major | Wave deployment model, Tiny Teams Capability Map | Completeness |
| IN-002-iter8 | MCP reliability framing assumes documented fallbacks eliminate adoption risk; community MCP failure silently degrades to fallback without user notification of capability loss | Assumption | High | Minor | Known Limitations: Figma SPOF, Whimsical classification MEDIUM-LOW | Evidence Quality |
| IN-003-iter8 | "Two people doing what used to take eight" assumes throughput equivalence; deliverable does not define throughput scope limits | Assumption | Medium | Minor | Tiny Teams Capability Map, Vision section | Internal Consistency |
| IN-004-iter8 | AI-First Design 90-day Enabler expiry assumes the substitution path (Design Sprint only) is acceptable for teams who need AI UX patterns before the Enabler completes | Assumption | Medium | Minor | Known Limitations: AI-First Design Conditional Status, Substitution path | Completeness |
| IN-005-iter8 | Expert panel bootstrapping for synthesis-type benchmarks assumes 2+ qualified reviewers are readily available at Wave 1 launch for a new community skill | Assumption | Medium | Minor | Benchmark Classification table, Pre-Launch Validation AC | Actionability |
| IN-006-iter8 | 180-day cross-validation deadline assumes that a "BOOTSTRAP-VALIDATED" benchmark remains safe to use during the 180-day window; benchmark degradation timeline is not specified | Assumption | Low | Minor | Pre-Launch Validation AC, BOOTSTRAP-VALIDATED annotation | Methodological Rigor |
| IN-007-iter8 | Wave re-entry guard ("BLOCK Wave N+1 routing until blocker-resolution entry logged") assumes the orchestrator independently enforces this without relying on `wave-progression.md` content integrity | Assumption | Medium | Minor | Wave enforcement 3-state behavior, ABANDON state definition | Internal Consistency |
| IN-008-iter8 | Solo practitioner fitness claim for Wave 4 assumes "external data sources" are accessible; no definition of what constitutes a sufficient external source for HEART metric data and B=MAP behavioral data | Assumption | Medium | Minor | Tiny Teams Population Segments table, Solo Practitioner row | Completeness |

---

## Detailed Findings

### IN-001-iter8: Wave Plateau as Dominant Adoption Failure Mode [MAJOR]

**Type:** Anti-Goal
**Original Assumption:** The wave model's criteria-gated progression creates a virtuous path from Wave 1 through Wave 5; teams that start will continue progressing.
**Inversion:** To guarantee failure at enabling tiny teams to achieve enterprise-grade UX capability, design the system so teams extract value from Wave 1 and stop there -- never progressing to the cross-framework synthesis that requires Wave 3-5 capabilities.
**Plausibility:** High. Wave 1 (Heuristic Eval + JTBD) provides immediately usable outputs at zero MCP cost. Wave 2 requires Miro (cost) and user data collection. Wave 3 requires Storybook (infrastructure) and Figma (cost). For part-time UX teams (explicitly the most common segment), each wave transition introduces tangible friction that the criteria-gating does not eliminate -- it formalizes it. Real-world adoption patterns in staged tooling consistently show sharp drop-offs after initial stages when subsequent stages introduce new infrastructure requirements.
**Consequence:** If 80%+ of teams plateau at Wave 1, the portfolio's promise of "two people doing what used to take eight" is empirically false for the median adopter. The deliverable's capability map becomes a theoretical maximum rather than an achieved outcome. The Tiny Teams Capability Map is accurate only for Wave 1 coverage columns; the remaining 6 roles' capability coverage requires Wave 2-5.
**Evidence:** The deliverable acknowledges this partially ("Part-time UX teams should treat wave progression beyond Wave 2 as aspirational") but does not frame Wave 1 plateau as a design failure mode requiring mitigation. The acceptance criteria include post-launch tracking of "wave progression rate -- percentage of teams that advance beyond Wave 1 within 90 days (target: baseline establishment)" -- using "baseline establishment" rather than a defined success threshold means there is no defined pass/fail condition for the wave model's primary assumption. The issue closure condition is Wave 1 MVL only, which structurally front-loads delivery value at the wave that the median team may never progress beyond.
**Dimension:** Completeness
**Mitigation:** Add a Wave 1 standalone value proposition section explicitly documenting what capability coverage teams achieve if they ONLY deploy Wave 1 and never progress further. Quantify: Wave 1 covers UX Evaluator/Auditor and Product Strategist (partial) -- 2 of 8 roles in the Capability Map. The deliverable should be honest that "two people doing what used to take eight" requires Wave 3-4 deployment for the remaining 6 role equivalencies. Optionally, add a wave progression success threshold to the post-launch metric (e.g., "target: >= 30% of teams advance beyond Wave 1 within 90 days") to create a testable design assumption.
**Acceptance Criteria:** Deliverable explicitly states which capability coverage is available at Wave 1 only versus requiring Wave 3+ (Capability Map enhancement); or post-launch wave progression metric has a defined success threshold rather than "baseline establishment."

---

### IN-002-iter8: Community MCP Silent Degradation Risk [MINOR]

**Type:** Assumption
**Original Assumption:** Documented fallback paths for all sub-skills eliminate the adoption risk from MCP server unavailability or failure.
**Inversion:** If community MCP servers (Whimsical classified MEDIUM-LOW) fail silently or degrade gradually rather than failing with an error code, the fallback path is never triggered -- users receive degraded output without notification.
**Plausibility:** Medium. The deliverable documents 429 (rate limit), 403 (auth), and 404 (file not found) as known failure codes -- these produce explicit errors. But community MCPs may degrade through API version drift (endpoints still responding but returning incorrect data formats), schema changes (returning 200 with changed structure), or behavioral changes (returning fewer results than expected without signaling error). These silent degradation modes bypass the documented fallback trigger logic.
**Consequence:** Outputs from affected sub-skills may be incomplete or incorrect while the orchestrator's MCP connectivity pre-check reports "available." The Whimsical community MCP (Design Sprint enhancement) and the bridge-based Hotjar MCP are most susceptible -- they lack the "official product" stability classification.
**Evidence:** MCP Operational Constraints table classifies Whimsical as "MEDIUM-LOW -- third-party maintained" and includes "Verify GitHub activity before implementation." The quarterly audit cadence addresses this at the infrastructure level but not at the runtime output validation level.
**Dimension:** Evidence Quality
**Mitigation:** Add a note to the MCP Operational Constraints table that community MCPs (Whimsical, Hotjar bridge) require output schema validation in addition to connectivity checks. The orchestrator's pre-check should include a lightweight schema probe (not just ping) for community-tier MCPs.

---

### IN-003-iter8: Throughput Claim Scope Underspecified [MINOR]

**Type:** Assumption
**Original Assumption:** "Two people doing what used to take eight" is a valid throughput equivalence claim for the defined portfolio scope.
**Inversion:** If the throughput claim is interpreted as covering all UX work a typical 8-person UX team performs, the claim is false by design -- the deliverable explicitly excludes user research depth, creative/strategic judgment, and several UX disciplines (dark patterns, algorithmic bias, privacy design). The portfolio covers "discipline scope," not "throughput."
**Plausibility:** High. The deliverable correctly hedges this in the Capability Map section ("This portfolio spans the same UX discipline scope as a 6-8 person UX team -- it does NOT match the throughput or depth"). However, the Vision section's tagline "Two people doing what used to take eight. That is the tiny teams promise" appears before the hedge, and the hedge appears only in the Capability Map section. A reader who encounters the vision statement without reaching the capability map disclaimer may form an overstated expectation.
**Consequence:** Minor: if the hedge is present in the document, the claim is defensible. The issue is framing order -- the bold claim leads, the qualification trails by several thousand words.
**Evidence:** Vision: "Two people, one product, zero UX specialists -- and the product is going to feel like a team of eight built it." Capability Map hedge: "This portfolio spans the same UX discipline scope as a 6-8 person UX team -- it does NOT match the throughput or depth."
**Dimension:** Internal Consistency
**Mitigation:** Add a one-sentence throughput qualification to the Vision section itself, adjacent to the primary claim, so readers do not need to reach the Capability Map to understand the scope of the promise. E.g., "Two people doing what used to take eight [in terms of methodology coverage -- throughput and depth remain human-proportional; see Capability Map for full scope definition]."

---

### IN-004-iter8: AI-First Design Substitution Path Assumption [MINOR]

**Type:** Assumption
**Original Assumption:** If the AI-First Design Enabler does not complete within 90 days, teams building AI products are adequately served by the substitution path (Design Sprint only + interim `/ux-heuristic-eval` with PAIR Guidebook heuristics).
**Inversion:** A team building a conversational AI product where 80%+ of UX challenges are AI-specific (trust calibration, explanation design, error handling for hallucinations) cannot be adequately served by generic heuristics plus a Design Sprint. The substitution path provides design rigor but not AI-specific UX methodology.
**Plausibility:** Medium. The substitution path is explicitly documented as a fallback, not as equivalent coverage. Teams are informed. The question is whether the 90-day expiry and auto-substitution are communicated clearly enough that teams understand the capability gap they are accepting.
**Consequence:** Minor: teams proceeding with the substitution path should have clear expectations set. The deliverable does this ("Interim path: The parent orchestrator routes AI product UX requests to /ux-heuristic-eval with supplemental PAIR Guidebook heuristics until the Enabler completes") but does not specify that the interim path covers an estimated X% of AI UX use cases.
**Evidence:** AI-First Design conditional status section, substitution path definition; Known Limitations section reiterates the conditional status.
**Dimension:** Completeness
**Mitigation:** Add an estimate of interim path coverage for AI-product UX use cases (e.g., "Interim path covers design-quality evaluation but does NOT cover AI-specific interaction patterns, trust calibration, or AI failure UX") so teams can make informed decisions about whether to wait for the Enabler or proceed with the substitution path.

---

### IN-005-iter8: Expert Panel Bootstrapping Availability [MINOR]

**Type:** Assumption
**Original Assumption:** Expert panels for synthesis-type benchmark reviews (Lean UX, Behavior Design, Design Sprint, AI-First Design) can be sourced from the Jerry community at Wave 1 launch.
**Inversion:** At Wave 1 launch, the Jerry community has zero completed sub-skill evaluations. The expert panel qualification requires "minimum 2 years UX practice, non-team-member." The Jerry community is primarily a software development/framework community. Finding 2+ qualified UX practitioners from this community at launch may not be feasible.
**Plausibility:** Medium. The pre-launch validation section has a bootstrapping fallback (criteria b-i: peer-reviewed UX evaluation experience; b-ii: tutorial walkthrough). But the expert panel qualification for synthesis-type benchmarks is defined separately from pre-launch validation evaluator qualification. The distinction is documented ("two pools serve distinct functions; qualification standards are intentionally different") but the expert panel bootstrap path is not defined.
**Consequence:** Minor: if expert panels cannot be sourced at Wave 1 launch, synthesis-type benchmarks (Lean UX, Behavior Design) may have undefined quality baselines at launch. This is a Wave 2+ concern, not a Wave 1 MVL blocker, since synthesis-type sub-skills are in Wave 2+.
**Evidence:** Benchmark Classification table: "/ux-lean-ux: Synthesis -- Expert panel review: 2+ qualified reviewers assess risk categorization completeness." Pre-Launch Validation AC does not define an expert panel bootstrap path equivalent to the b-i/b-ii criteria for pre-launch evaluators.
**Dimension:** Actionability
**Mitigation:** Add an expert panel bootstrapping path for synthesis-type benchmarks parallel to the b-i/b-ii pre-launch evaluator bootstrapping path, or explicitly note that synthesis-type benchmark expert panels use the same bootstrapping criteria as pre-launch evaluators.

---

### IN-006-iter8: BOOTSTRAP-VALIDATED 180-Day Safety Window [MINOR]

**Type:** Assumption
**Original Assumption:** A BOOTSTRAP-VALIDATED benchmark is safe to use for 180 days without cross-validation, and degradation from BOOTSTRAP-VALIDATED to UNVERIFIED-BENCHMARK at day 181 is an acceptable signal mechanism.
**Inversion:** If the BOOTSTRAP-VALIDATED benchmark quality baseline is significantly lower than a fully-verified benchmark, teams using Wave 1 sub-skills during the 180-day window may be making design decisions against an unverified quality standard. The 180-day window assumes the bootstrap validation adequately approximates the true benchmark -- but this assumption is not tested.
**Plausibility:** Low. The bootstrapping fallbacks (b-i: UX evaluation experience, b-ii: tutorial completion) are explicitly tagged as lower-confidence than criterion-a evaluation. The 180-day window is a pragmatic governance mechanism, not a quality guarantee.
**Consequence:** Minor: the deliverable does disclose this through the BOOTSTRAP-VALIDATED annotation and the UNVERIFIED-BENCHMARK downgrade mechanism. Teams are warned. The risk is that "180 days" may be perceived as a quality guarantee period rather than a governance window.
**Evidence:** Pre-Launch Validation AC: "BOOTSTRAP-VALIDATED: Wave 1 evaluations using the fallback qualification path are tagged BOOTSTRAP-VALIDATED and are NOT equivalent to fully-verified quality benchmarks."
**Dimension:** Methodological Rigor
**Mitigation:** Add clarifying language that BOOTSTRAP-VALIDATED status indicates "lower confidence in the quality baseline, not a quality guarantee" and that the 180-day window is a governance deadline, not a safety certification.

---

### IN-007-iter8: Wave Re-Entry Guard Enforcement Independence [MINOR]

**Type:** Assumption
**Original Assumption:** The wave re-entry guard after ABANDON is enforced by the orchestrator independently of `wave-progression.md` content integrity.
**Inversion:** The ABANDON state re-entry guard specifies: "After ABANDON, the orchestrator MUST consult `wave-progression.md` and BLOCK Wave N+1 routing until a documented blocker-resolution entry is logged." If `wave-progression.md` is edited, deleted, or corrupted, the guard is bypassed. The enforcement depends on file system integrity rather than an independently enforced state.
**Plausibility:** Low-Medium. `wave-progression.md` editing by the user is a P-020 user authority scenario -- the user has the right to modify files. The question is whether an inadvertent deletion or corruption bypasses a safety mechanism.
**Consequence:** Minor: the orchestrator's enforcement of the re-entry guard depends on a file that the user controls. This is consistent with Jerry's overall file-based state model, but the ABANDON guard is a safety mechanism meant to prevent teams from cycling through ABANDON/re-entry without actually resolving blockers.
**Evidence:** ABANDON state: "the orchestrator MUST consult `wave-progression.md` and BLOCK Wave N+1 routing until a documented blocker-resolution entry is logged."
**Dimension:** Internal Consistency
**Mitigation:** Add a note that `wave-progression.md` deletion or absence is treated as an UNKNOWN state (not PASS), requiring the user to reconstruct the log before routing resumes. This makes the guard resilient to accidental deletion.

---

### IN-008-iter8: Solo Practitioner Wave 4 External Data Source Definition [MINOR]

**Type:** Assumption
**Original Assumption:** Solo practitioners can satisfy Wave 4 prerequisites (HEART metric data, B=MAP behavioral data) via "external data sources."
**Inversion:** For a solo practitioner building a new product with no live users, "external data sources" for HEART metrics (requires product analytics) and B=MAP behavioral data (requires observed user behavior) may not exist. The wave qualification note says "Wave 4 data-collection prerequisites (HEART metric data, B=MAP behavioral data) may require external data sources" but does not define what constitutes a qualifying external source when no product analytics exist.
**Plausibility:** Medium. The target use case for Wave 4 is post-launch measurement -- "After Launch" is literally the lifecycle stage for both HEART and Behavior Design. A pre-launch solo practitioner has no qualifying data by definition, making Wave 4 inaccessible until launch.
**Consequence:** Minor: Wave 4 being post-launch is correct by design. The issue is that "external data sources" as a qualifier implies substitution is possible (e.g., competitive analytics, industry benchmarks) when it may not be for the sub-skill to function meaningfully.
**Evidence:** Tiny Teams Population Segments table, Solo Practitioner row: "Wave 4 data-collection prerequisites (HEART metric data, B=MAP behavioral data) may require external data sources."
**Dimension:** Completeness
**Mitigation:** Clarify that Wave 4 is exclusively post-launch for solo practitioners with no live product -- no external data source substitution is defined for pre-launch contexts, and the "may require external data sources" note applies to post-launch practitioners who have not yet instrumented their own analytics.

---

## Recommendations

### Major (MUST Mitigate)

**IN-001-iter8: Wave Plateau as Dominant Adoption Failure Mode**

- **Action:** Add explicit Wave 1 standalone capability coverage statement to the Capability Map or Vision section, documenting that Wave 1 covers ~2 of 8 role equivalencies (UX Evaluator/Auditor + partial Product Strategist) -- not the full "two people doing what used to take eight" promise. Add a defined success threshold to the wave progression post-launch metric (e.g., "target: >= 30% of teams advance beyond Wave 1 within 90 days").
- **Acceptance Criteria:** (a) Deliverable contains explicit statement of Wave 1-only capability coverage (not requiring reader to cross-reference Capability Map); OR (b) post-launch wave progression metric has a defined pass/fail threshold rather than "baseline establishment."

### Minor (SHOULD Mitigate or Acknowledge)

**IN-002-iter8:** Add silent degradation note to MCP Operational Constraints table for community-tier MCPs (Whimsical, Hotjar bridge) distinguishing connectivity failure (explicit error) from behavioral degradation (schema drift, reduced output quality).

**IN-003-iter8:** Add one-sentence throughput qualification to Vision section adjacent to the "two people doing what used to take eight" claim, linking explicitly to the Capability Map scope definition.

**IN-004-iter8:** Specify what AI-product UX use cases the interim path covers and does not cover, so teams can make informed decisions about waiting for the Enabler versus proceeding with Design Sprint + PAIR heuristics.

**IN-005-iter8:** Define an expert panel bootstrapping path for synthesis-type benchmarks, or state that the same b-i/b-ii criteria from pre-launch validation apply to expert panels.

**IN-006-iter8:** Add clarifying language that BOOTSTRAP-VALIDATED is a governance tag indicating lower confidence, not a safety certification for the 180-day window.

**IN-007-iter8:** Specify that `wave-progression.md` absence or deletion is treated as UNKNOWN state requiring reconstruction before wave routing resumes.

**IN-008-iter8:** Clarify that Wave 4 "external data sources" qualifier applies to post-launch practitioners only; no substitution path exists for pre-launch contexts.

---

## Scoring Impact

Assessment against the 6 S-014 dimensions, mapping Inversion findings:

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Neutral-Negative | IN-001-iter8: Wave plateau failure mode not framed as a design risk requiring Wave 1 standalone capability disclosure. IN-004-iter8: AI-First Design interim path coverage scope not defined. IN-008-iter8: Solo practitioner Wave 4 data source definition ambiguous. Three gaps, all Minor-to-Major, but collectively create an incomplete picture of what teams actually achieve at each wave stage. |
| Internal Consistency | 0.20 | Neutral | IN-003-iter8: Vision claim vs. Capability Map hedge is present but sequentially displaced. IN-007-iter8: ABANDON guard enforcement depends on file integrity. Both are addressable without structural revision. |
| Methodological Rigor | 0.20 | Positive | No Critical or Major methodological assumption failures. All six S-013 protocol steps completed. Both inversion phases (anti-goals + assumption stress-testing) applied. Prior iterations' work has resolved the structural rigor gaps that were present in earlier drafts. The confidence gate architecture, wave enforcement 3-state behavior, P-020 compliance, and override audit mechanism represent systematic methodology that holds up under inversion. |
| Evidence Quality | 0.15 | Neutral | IN-002-iter8: Community MCP silent degradation assumption surfaces a gap in the evidence basis for fallback reliability. However, the deliverable's citation discipline and cross-reference fidelity are strong overall. |
| Actionability | 0.15 | Positive | Mitigations for all findings are targeted and do not require structural revision. Most are single-sentence additions or clarifying qualifications. The one Major finding (IN-001) has two acceptable resolution paths (Capability Map enhancement OR post-launch metric threshold). |
| Traceability | 0.10 | Positive | All findings trace to specific deliverable sections with verbatim evidence references. IN-NNN-iter8 identifiers used consistently. Prior iterations' work is fully traceable through the [Rnfix:] annotation system. |

**Overall Inversion Assessment:** The deliverable has successfully resolved all prior Critical and Major assumption vulnerabilities. One Major finding (IN-001) remains: the wave plateau failure mode is the most plausible adoption risk and the deliverable does not yet frame it as a design concern requiring explicit capability disclosure at the Wave 1 level. Seven Minor findings are residual gaps that require clarifying additions rather than structural revision.

**Recommendation: ACCEPT with targeted mitigation for IN-001-iter8.** The deliverable is structurally robust at C4 quality. The Minor findings should be logged for R8, but none of them would individually or collectively prevent acceptance.

---

## Execution Statistics

- **Total Findings:** 8
- **Critical:** 0
- **Major:** 1
- **Minor:** 7
- **Protocol Steps Completed:** 6 of 6

---

## Strategy Execution Report: S-013 Inversion Technique

### Execution Context
- **Strategy:** S-013 (Inversion Technique)
- **Template:** `.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 8 (post-R7 revision)

### Execution Context Notes

Per the orchestrator's focus direction, this execution specifically stress-tested:
1. **What if Tiny Teams don't need UX frameworks?** -- Addressed via anti-goal analysis (IN-001). The inversion reveals the real risk is not that teams don't need UX frameworks, but that the wave model assumes teams will build through the full progression when Wave 1 plateau is the statistically dominant adoption pattern. The need is real; the adoption path assumption is the vulnerability.
2. **What if MCP integration is unreliable?** -- Addressed via IN-002. All documented failures are explicit error codes. The gap is silent degradation from community MCPs, which bypasses the documented fallback trigger logic.
3. **What if the wave model constrains rather than enables adoption?** -- Addressed via IN-001 and IN-003. The wave model's criteria-gating creates real adoption friction at each wave boundary, and the "two people doing what used to take eight" promise requires Wave 3-4 deployment for 6 of 8 role equivalencies. The constraint is partially acknowledged but not framed as the dominant failure mode risk.

Prior iterations' systematic addressing of Critical and Major assumption vulnerabilities means the I8 deliverable is in a significantly stronger position than earlier drafts. The remaining findings are genuine but do not compromise the deliverable's core value proposition or structural integrity.
