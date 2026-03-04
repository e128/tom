# Devil's Advocate Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (Iteration 7)
**H-16 Compliance:** S-003 Steelman applied 2026-03-03 (confirmed — `tournament-iter7/s-003-steelman.md`, findings SM-001-I7 through SM-008-I7)

---

## Step 1: Role Assumption

I adopt the Devil's Advocate role with a clear mandate to argue against the deliverable's positions. My goal is to find the strongest possible reasons why this specification is wrong, incomplete, or flawed — even where prior iterations have resolved critical issues. The deliverable is at 0.867 after six iterations, and this role requires surfacing arguments that survived prior scrutiny or were introduced by R6 revisions.

The deliverable proposes a `/user-experience` parent orchestrator with 10 sub-skills delivering AI-augmented UX methodology to tiny teams (2-5 people). It is a C4 deliverable: public, irreversible once posted, architecture-defining for the Jerry framework.

---

## Summary

9 counter-arguments identified (1 Critical, 4 Major, 4 Minor). The deliverable's core architecture is sound and its prior six iterations have eliminated obvious structural flaws. However, it contains one Critical internal contradiction: the Haiku model is assigned to the most MCP-integration-dependent sub-skill in the portfolio (`/ux-heuristic-eval` at T3 tool tier), creating a capability-tier mismatch that undermines the actionability of the entire Wave 1 launch. Four Major findings address: the BOOTSTRAP-VALIDATED retroactive validation timeline being unenforceable as written, the expert panel qualification standard conflicting with the pre-launch evaluator qualification standard, the override audit log's file-based persistence being inconsistent with the wave state's Memory-Keeper-based persistence without documented rationale, and the WSM sensitivity analysis claim remaining partially vague despite S-003 recommendations. Recommendation: **REVISE** to address the Critical and Major findings before S-014 scoring.

---

## Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-I7 | Haiku model assigned to T3/MCP-dependent sub-skill creates capability-tier mismatch | Critical | Sub-Skill Model Selection table assigns `haiku` to `/ux-heuristic-eval`; same sub-skill is T3 with Required Figma MCP and Enhancement Storybook MCP | Methodological Rigor |
| DA-002-I7 | BOOTSTRAP-VALIDATED retroactive validation is unenforceable as specified | Major | "within 90 days of the first criterion-(a)-qualified evaluator joining the community" has no mechanism to detect or enforce this event | Actionability |
| DA-003-I7 | Expert panel qualification (Benchmark Classification) conflicts with pre-launch blind evaluator qualification | Major | Benchmark Classification table requires "2+ qualified reviewers" but does not define qualification; pre-launch AC defines qualification differently (criterion a/b-i/b-ii) | Internal Consistency |
| DA-004-I7 | Override audit log file-based persistence lacks rationale in the Cross-Session State specification | Major | Cross-Session State table covers wave status, hypothesis backlog, MCP registry via Memory-Keeper; `work/audit/override-log.md` is file-based but this asymmetry is not documented in the specification section | Internal Consistency |
| DA-005-I7 | WSM sensitivity analysis inline evidence claim is inconsistent with the deliverable's own text | Major | Research Backing section says "Full sensitivity analysis available in `ux-framework-selection.md`" but the inline score deltas cited by S-003 as a required strengthening have not been incorporated | Evidence Quality |
| DA-006-I7 | Crisis mode WARN escalation counter reset condition is ambiguous | Minor | "WARN escalation: 3 consecutive WARN states across ANY sub-skills within one wave... Sub-skill switching does not reset the counter" but it is unspecified whether wave-level reset (completing a wave) resets the counter | Internal Consistency |
| DA-007-I7 | Part-time UX "most common segment" claim's inferential basis is stated but not separated from the design decision | Minor | "based on Gartner's Tiny Teams research" is the stated basis; S-003 noted this is inferred, not directly measured — the distinction matters for a C4 deliverable | Evidence Quality |
| DA-008-I7 | Wave 2 entry criterion asymmetry: Lean UX requires "1 JTBD job statement used in a product decision" but HEART has no equivalent usage requirement | Minor | Wave entry criteria table: Wave 2 requires "Completed at least 1 heuristic evaluation report AND 1 JTBD job statement that was used in a product decision" — HEART (also Wave 2) is listed with Lean UX but HEART's own entry criterion is not separately specified | Completeness |
| DA-009-I7 | Zeroheight MCP pre-commitment blocking criterion is Wave 3 entry, but Zeroheight is Enhancement MCP (not Required) for Atomic Design | Minor | Wave 3 MCP Pre-Commitment states "Wave 3 entry is BLOCKED without this integration assessment" but Zeroheight appears as Enhancement (dashed arrow) in the MCP integration diagram, not Required (solid arrow) | Internal Consistency |

---

## Detailed Findings

### DA-001-I7: Haiku Model Assigned to T3/MCP-Dependent Sub-Skill [CRITICAL]

**Claim Challenged:** "Heuristic Evaluation: `haiku` — Checklist-based systematic evaluation against 10 discrete heuristics; procedural, not reasoning-intensive" (Sub-Skill Model Selection table)

**Counter-Argument:** Haiku is the fastest and most cost-efficient model in the tier, optimized for procedural tasks with low reasoning demand. However, `/ux-heuristic-eval` is assigned T3 tool tier and requires Figma MCP (Required, solid arrow in MCP integration diagram). The Figma MCP interaction — reading design file structure, extracting frames, interpreting visual design artifacts — involves multimodal reasoning about visual contexts that is not "procedural" in the sense Haiku handles optimally. The model selection rationale ("checklist-based, not reasoning-intensive") describes the heuristic evaluation methodology, not the complexity of the Figma API interaction layer.

More importantly: `agent-development-standards.md` Mode-to-Design Implications table states that the `systematic` cognitive mode typical recommendation is `sonnet or haiku (procedural)`. The deliverable's Haiku selection is defensible in isolation for the evaluation logic. But `/ux-heuristic-eval` is Wave 1 — it is the first sub-skill most teams will use. If Haiku's multimodal or tool-coordination capability is insufficient for reliable Figma MCP operation at T3, the Wave 1 experience fails, and the entire wave gating model collapses for teams that never see Wave 2.

**Evidence:** Sub-Skill Model Selection table (line 1227): `haiku | Heuristic Evaluation | Checklist-based systematic evaluation against 10 discrete heuristics; procedural, not reasoning-intensive`. Sub-skill description (line 180): `Tool Tier | T3`, `Required MCP | Figma (design file reading, frame extraction)`. MCP integration diagram (line 539): `Figma ==>|Required| HE`. The T3 tier combined with Required MCP is the most complex tool profile assigned to the Haiku model anywhere in the deliverable.

**Impact:** If Haiku cannot reliably navigate the Figma MCP API (rate limit handling, OAuth token management, frame extraction, visual context interpretation), Wave 1 sub-skill quality fails consistently, the quality benchmark (>= 7 of 10 heuristic violations) cannot be met, and the "zero-dependency" Wave 1 claim becomes false for any team using Figma MCP. The non-MCP fallback (screenshot-input mode) degrades the experience but is available — however, the model selection justification should acknowledge that Haiku with Figma MCP is the chosen design and that model escalation to Sonnet may be required based on pre-launch testing.

**Dimension:** Methodological Rigor

**Response Required:** The creator must either: (a) justify specifically why Haiku's tool-coordination capability is sufficient for Figma MCP's T3 complexity (citing evidence or test results), OR (b) upgrade Heuristic Eval to Sonnet and revise the model selection rationale, OR (c) add an explicit pre-launch test criterion: "Pre-launch validation includes a model capability test confirming Haiku can reliably navigate Figma MCP OAuth and frame extraction with >= X% success rate on a reference design file."

**Acceptance Criteria:** The model selection rationale for `/ux-heuristic-eval` must address the T3/MCP interaction complexity specifically, not just the heuristic evaluation logic. If Haiku is retained, a pre-launch model capability benchmark must be added to the Acceptance Criteria. If Sonnet is substituted, the model selection table must be updated.

---

### DA-002-I7: BOOTSTRAP-VALIDATED Retroactive Validation is Unenforceable [MAJOR]

**Claim Challenged:** "within 90 days of the first criterion-(a)-qualified evaluator joining the community, all BOOTSTRAP-VALIDATED benchmarks must be re-evaluated by the criterion-(a) evaluator" (Pre-Launch Validation AC, line 861)

**Counter-Argument:** The BOOTSTRAP-VALIDATED retroactive re-evaluation requirement is contingent on a triggering event — "the first criterion-(a)-qualified evaluator joining the community" — that has no defined detection or notification mechanism. Criterion (a) is "Jerry Framework users who did not author or contribute to the sub-skill under review." This is already a broad category that includes any external contributor. The requirement does not specify: (a) who monitors for criterion-(a) qualification, (b) what "joining the community" means operationally (first PR? first registered user? first skill invocation?), (c) how BOOTSTRAP-VALIDATED benchmarks are tracked in aggregate so the re-evaluator knows what to re-evaluate, (d) what happens if the criterion-(a) evaluator agrees to re-evaluate but finds 2 of 4 BOOTSTRAP-VALIDATED Wave 1 benchmarks fail — does this trigger a full Wave 1 WARN state, or is it per-benchmark?

The solo bypass "peer review submission requirement" (replacing the 30-day auto-stand) has the same enforcement gap: the deliverable says the solo evaluation "must be submitted for peer review" but does not specify the submission channel, what constitutes submission, or what happens if no peer review is received within the extended indefinite window.

**Evidence:** Pre-Launch Validation AC (line 861): "BOOTSTRAP-VALIDATED" tag, "within 90 days of the first criterion-(a)-qualified evaluator joining the community, all BOOTSTRAP-VALIDATED benchmarks must be re-evaluated." No detection mechanism, no tracking registry, no failure escalation path specified for the re-evaluation outcome.

**Impact:** Without a detection mechanism, BOOTSTRAP-VALIDATED benchmarks may never trigger re-evaluation even after qualified evaluators join the community. The governance requirement exists on paper but has no operational enforcement path. This is a completeness gap in the Actionability dimension — a concrete commitment is made but the operational mechanism to fulfill it is absent.

**Dimension:** Actionability

**Response Required:** Specify: (a) a concrete trigger for "criterion-(a)-qualified evaluator joining the community" (first PR merged, explicit role claim in AGENTS.md, or similar verifiable event), (b) a registry or tracking mechanism for BOOTSTRAP-VALIDATED benchmarks (e.g., a `BOOTSTRAP-STATUS.md` file listing each BOOTSTRAP-VALIDATED benchmark with status and 90-day clock), (c) the failure escalation path if re-evaluation fails (per-benchmark WARN, or Wave 1 WARN?).

**Acceptance Criteria:** The pre-launch validation AC must specify: (1) the operational definition of "criterion-(a)-qualified evaluator joining," (2) a named artifact tracking BOOTSTRAP-VALIDATED benchmark status, (3) the outcome of a failed re-evaluation (what state does the wave enter?).

---

### DA-003-I7: Expert Panel Qualification Conflicts Across Two Contexts [MAJOR]

**Claim Challenged:** The Benchmark Classification table (line 871-879) specifies "Expert panel review: 2+ qualified reviewers" for synthesis-type sub-skills (Lean UX, Behavior Design, Design Sprint, AI-First Design). The synthesis-type expert qualification does not cross-reference the qualification standard defined at line 681.

**Counter-Argument:** The deliverable defines expert qualification at line 681 for MEDIUM-confidence synthesis validation: "minimum 2 years UX practice experience (product design, user research, or UX consulting), non-team-member, non-involvement declaration required." This is qualification standard A.

The Benchmark Classification table specifies "2+ qualified reviewers" for synthesis-type expert panels without defining what "qualified" means in this context. The pre-launch validation AC (line 861) defines a separate and different qualification standard for blind evaluation: criterion (a) = did not author or contribute to the sub-skill, criterion (b-i) = peer-reviewed UX evaluation experience in any context, criterion (b-ii) = completion of tutorial walkthrough with self-assessment.

These are three distinct qualification standards for three overlapping reviewer roles, and none cross-references the others explicitly:
- Synthesis validation expert = 2 years UX practice, non-team-member
- Benchmark expert panel = "qualified reviewers" (undefined)
- Pre-launch blind evaluator = criterion (a) + (b-i) or (b-ii)

S-003 finding SM-002-I7 identified this gap and recommended cross-referencing. The R6 revision did not incorporate this cross-reference. A developer implementing Wave 1 reading all three sections would have no clear guidance on whether the same pool of reviewers serves all three functions, or whether different qualification thresholds apply to each.

**Evidence:** Line 681: "minimum 2 years UX practice experience... non-team-member, non-involvement declaration required." Line 875 (Benchmark Classification): "Expert panel review: 2+ qualified reviewers assess risk categorization completeness" (no qualification definition). Line 861 (Pre-Launch Validation): criterion (a)/(b-i)/(b-ii) evaluator qualifications (different standard).

**Impact:** Implementation teams cannot determine which evaluator pool satisfies each review requirement. The ambiguity may result in under-qualified reviewers passing synthesis benchmarks (if criterion b-ii alone is used) or over-constraining the expert panel search (if the 2-year standard is applied where criterion b-ii would suffice). Either outcome undermines the confidence gate architecture.

**Dimension:** Internal Consistency

**Response Required:** Add a "Reviewer Qualification Cross-Reference" to the Benchmark Classification table explicitly mapping each review type (synthesis validation expert, benchmark expert panel, pre-launch blind evaluator) to a named qualification standard. Where standards differ, state the difference and the rationale.

**Acceptance Criteria:** The Benchmark Classification table must either (a) explicitly cross-reference the qualification standard from line 681 for synthesis-type expert panels, or (b) state that a different qualification applies and specify it. A reviewer implementing the benchmarks must be able to identify the correct qualification standard for each review type from a single section.

---

### DA-004-I7: Override Audit Log File-Based Persistence Lacks Rationale in Specification [MAJOR]

**Claim Challenged:** Cross-Session State section (line 1243-1252) specifies three Memory-Keeper keys for wave status, hypothesis backlog, and MCP registry. The Human Override Audit log (`work/audit/override-log.md`) is referenced in Key Design Decisions (line 689) but absent from the Cross-Session State specification table.

**Counter-Argument:** The Cross-Session State section defines where persistent state lives. Wave signoff status (Memory-Keeper), hypothesis backlog (Memory-Keeper), MCP registry (Memory-Keeper) — these are session-boundary data that need cross-session persistence. The Human Override Audit is equally a cross-session concern: overrides must be traceable across sessions, not just within a session. The R6 revision added the ABANDON state log to `wave-progression.md` (line 642), which is also file-based.

The deliverable has two patterns for persistent state — Memory-Keeper keys and repository files (`work/audit/override-log.md`, `wave-progression.md`, `WAVE-N-SIGNOFF.md`). There is no section that explains when each pattern is appropriate. S-003 finding SM-006-I7 suggested a rationale (override audit requires repository-commit immutability; Memory-Keeper is for ephemeral session state). But SM-006-I7 was a Steelman finding and its recommended clarification was not incorporated in the specification section that defines state persistence.

The result: the Cross-Session State section is incomplete as a specification because it describes only one of two persistence patterns, and an implementer reading only that section would not know that override audit is file-based or why.

**Evidence:** Cross-Session State table (lines 1248-1252): three Memory-Keeper keys listed. Human Override Audit reference at line 689: "Audit log persisted to `work/audit/override-log.md`." No entry in Cross-Session State for the override log. ABANDON log reference at line 642: "ABANDON is logged in `wave-progression.md`" — also file-based, also absent from Cross-Session State.

**Impact:** Implementers cannot determine the complete persistence architecture from the Cross-Session State section. State that should be tracked may be implemented using the wrong persistence pattern (e.g., override audit placed in Memory-Keeper when it needs repository immutability). The specification is incomplete.

**Dimension:** Internal Consistency

**Response Required:** Expand the Cross-Session State section to include both persistence patterns: Memory-Keeper keys (current) and file-based persistent artifacts (override-log.md, wave-progression.md, WAVE-N-SIGNOFF.md). Add a brief rationale for when each pattern is appropriate (immutability requirement → file-based; session boundary state → Memory-Keeper).

**Acceptance Criteria:** The Cross-Session State section must list all persistent state locations (both Memory-Keeper keys and file-based artifacts), with rationale for which pattern applies to each. An implementer must be able to determine the complete persistence architecture from this section alone.

---

### DA-005-I7: WSM Sensitivity Analysis Inline Evidence Claim Remains Incomplete [MAJOR]

**Claim Challenged:** "Full sensitivity analysis available in `ux-framework-selection.md`" (Research Backing section, line 983) and the C1 Sensitivity Analysis paragraph added by R6 (line 983).

**Counter-Argument:** The R6 revision added a C1 Sensitivity Analysis paragraph that states: "the WSM ranking changes minimally -- the top-3 frameworks (Nielsen's, Design Sprint, Atomic Design) remain in top-3 positions." However, the specific score deltas that S-003 finding SM-003-I7 recommended incorporating ("at C1=0.15, Nielsen's Heuristics moves from 9.05 to 8.71; Design Sprint from 8.65 to 8.40; Atomic Design from 8.55 to 8.29") were not added to the document. The current text makes the claim but does not provide the inline evidence that would make it verifiable without reading `ux-framework-selection.md`.

This is a particularly sharp inconsistency because the deliverable elsewhere demonstrates high evidence discipline (WHO citation for disability statistics, Gartner citation for Tiny Teams, Midjourney ARR citation with source). The WSM sensitivity analysis is one of the deliverable's strongest methodological claims — "five arithmetic verification rounds, sensitivity analysis confirming top-3 stability" — yet the inline evidence for the stability claim is absent. A reader cannot verify the stability claim from the deliverable alone.

The counter-argument goes further: if the sensitivity analysis is available in `ux-framework-selection.md`, why does the deliverable not reproduce the three key data points that confirm the claim? Either the data points are there and reproducible, in which case their absence from the deliverable is an editorial oversight; or they are not there, in which case the claim "full sensitivity analysis available" may overstate what the artifact contains.

**Evidence:** Research Backing > C1 Sensitivity Analysis paragraph (line 983): "the WSM ranking changes minimally" with no inline score deltas. SM-003-I7 Steelman finding (s-003-steelman.md, line 38): "adding the three specific score deltas inline: at C1=0.15, Nielsen's moves from 9.05 to 8.71; Design Sprint from 8.65 to 8.40; Atomic Design from 8.55 to 8.29." These deltas are not present in the current deliverable text.

**Impact:** The WSM stability claim remains unverifiable from the deliverable itself. Reviewers who do not read `ux-framework-selection.md` cannot assess whether the sensitivity analysis confirms what the deliverable claims. For a C4 deliverable that will be public, this is a material gap in Evidence Quality.

**Dimension:** Evidence Quality

**Response Required:** Incorporate the three specific score deltas into the C1 Sensitivity Analysis paragraph inline. Optionally, note that these are from `ux-framework-selection.md` to preserve traceability.

**Acceptance Criteria:** The C1 Sensitivity Analysis paragraph must include the score values for at least the top-3 frameworks under the reduced C1 weight scenario, making the stability claim verifiable without reading the referenced artifact.

---

### DA-006-I7: WARN Escalation Counter Reset Condition is Ambiguous [MINOR]

**Claim Challenged:** "WARN escalation: 3 consecutive WARN states across ANY sub-skills within one wave... Sub-skill switching does not reset the counter." (Wave enforcement 3-state behavior, line 641)

**Counter-Argument:** The counter states that sub-skill switching does not reset the WARN counter. It does not state whether completing a wave (progressing from Wave N to Wave N+1 via WAVE-N-SIGNOFF.md) resets the counter. A team could accumulate 2 WARN states in Wave 2, then advance to Wave 3 (presumably with a PASS-state WAVE-2-SIGNOFF.md), then trigger 1 WARN state in Wave 3. Under the current language, it is ambiguous whether this is 3 consecutive WARNs (triggering crisis mode) or 1 WARN (counter reset at wave transition).

The current language is: "across ANY sub-skills within one wave" — which implies the counter is wave-scoped. But "sub-skill switching does not reset the counter" implies counter persistence within a wave. The ABANDON state description (line 642) references "crisis mode" without clarifying whether ABANDON resolves the counter.

**Evidence:** Line 641: "3 consecutive WARN states across ANY sub-skills within one wave (not per-sub-skill)... Sub-skill switching does not reset the counter." The phrase "within one wave" may mean counter is wave-scoped (resets at wave transition), or it may mean the counter applies to any WARN regardless of wave. No explicit statement on wave-transition reset behavior.

**Impact:** If wave transitions do not reset the counter, a team experiencing WARNs across multiple waves will trigger crisis mode under unexpected conditions. If they do reset, a team could evade crisis mode escalation by deliberately triggering wave transitions. The ambiguity creates implementation uncertainty.

**Dimension:** Internal Consistency

**Response Required:** Clarify whether the WARN counter resets at wave transitions (when WAVE-N-SIGNOFF.md achieves PASS state for Wave N). Add a one-sentence clarification.

**Acceptance Criteria:** The WARN escalation description explicitly states the counter reset behavior at wave boundaries.

---

### DA-007-I7: Part-Time UX "Most Common" Claim Basis Is Inferential but Framed as Stated [MINOR]

**Claim Challenged:** "Part-time UX is the most common segment based on Gartner's Tiny Teams research." (Population segments table footnote, line 84-85)

**Counter-Argument:** The S-003 Steelman (SM-008-I7) noted this is an inference from Gartner's trend data, not a directly measured statistic. The deliverable presents it with "based on Gartner's Tiny Teams research" which implies Gartner measured and reported it. Gartner's 2026 Strategic Technology Trends report identifies Tiny Teams as a trend but does not appear to include a quantitative breakdown of "solo practitioner vs. part-time UX vs. dedicated UX" allocation within tiny teams.

The distinction matters because the deliverable uses "Part-time UX is the most common segment" to justify Portfolio Fit = HIGH for part-time UX, the design calibration for Waves 1-2, and multiple design decisions. If the "most common" designation is an inference rather than a measurement, the chain of design decisions built on it is less robust than presented. This is not fatal to the argument — the inference is reasonable — but a C4 deliverable should distinguish between "Gartner reports X" and "Gartner data implies X."

**Evidence:** Line 84: "Part-time UX (20-50% allocation) is the most common segment based on Gartner's Tiny Teams research." Line 46: Gartner citation confirms the Tiny Teams trend but does not report part-time UX breakdown. SM-008-I7 in s-003-steelman.md identified this as inferential.

**Impact:** If reviewers investigate and find Gartner does not directly report the part-time UX prevalence, the claim may be challenged as unsupported. A small wording change ("Gartner's Tiny Teams data implies part-time UX as the most common allocation pattern" vs. "based on Gartner's Tiny Teams research") would accurately represent the inferential status.

**Dimension:** Evidence Quality

**Response Required:** Add a parenthetical acknowledging the inferential basis: e.g., "(inferred from Gartner Tiny Teams trend data; direct measurement not available)" or equivalent.

**Acceptance Criteria:** The "most common segment" claim distinguishes between reported data and inference.

---

### DA-008-I7: Wave 2 Entry Criterion Covers Lean UX Prerequisite but Not HEART-Specific Prerequisite [MINOR]

**Claim Challenged:** Wave entry criteria table, Wave 2: "Completed at least 1 heuristic evaluation report AND 1 JTBD job statement that was used in a product decision" (line 628)

**Counter-Argument:** Wave 2 includes two sub-skills — Lean UX and HEART Metrics — but the entry criterion is specified from Lean UX's perspective (heuristic eval output + JTBD job statement). HEART Metrics is a post-launch measurement framework. A team could satisfy the Wave 2 entry criterion (complete 1 heuristic eval + 1 JTBD job statement) without having a launched product to measure. They would then unlock HEART Metrics but have no data to feed it.

HEART requires "an analytics data source" (Wave 3 entry criterion states this, not Wave 2). The Wave 2 sub-skills are grouped together under one entry criterion, but their actual prerequisites differ: Lean UX needs Wave 1 research outputs (correct, covered by the criterion), while HEART needs a launched product with analytics. A team using HEART Metrics in Wave 2 with no launched product will produce a GSM template with hypothetical goals and estimated signals, not measured metrics.

**Evidence:** Wave entry table (line 628): Wave 2 criterion covers Lean UX prerequisites. HEART description (line 243): "You shipped the product. Now measure whether it actually works for humans." HEART Key Output (line 250): "HEART GSM populated template, metric dashboard specification, anomaly detection report" — all require real metric data. The Wave 2 criterion does not verify that a product has launched.

**Impact:** Teams unlocking Wave 2 without a launched product can invoke HEART Metrics but will produce low-quality outputs (placeholder GSM templates). The skill's narrative says "You shipped the product" — this is a de facto prerequisite not enforced by the Wave 2 gating criterion. Either the criterion should add a HEART-specific prerequisite ("for HEART: launched product with active analytics source"), or the HEART sub-skill description should clarify it is only fully functional post-launch, and teams pre-launch should use Lean UX only.

**Dimension:** Completeness

**Response Required:** Clarify Wave 2 entry criteria to differentiate between the Lean UX pathway (no launched product required) and the HEART pathway (launched product with analytics source required). Either add a HEART-specific prerequisite or explicitly state that HEART produces placeholder outputs pre-launch.

**Acceptance Criteria:** Wave 2 entry criteria adequately account for both sub-skills' actual prerequisite states.

---

### DA-009-I7: Zeroheight MCP BLOCK Criterion Inconsistent with Enhancement MCP Classification [MINOR]

**Claim Challenged:** "Wave 3 entry is BLOCKED without this integration assessment" for Zeroheight MCP (line 604); Zeroheight appears as Enhancement MCP (dashed arrow) in MCP integration diagram (line 557).

**Counter-Argument:** The MCP integration diagram uses a clear legend: solid arrows = Required MCP (degraded mode + explicit error on failure); dashed arrows = Enhancement MCP (cosmetic limitation on failure). Zeroheight appears with a dashed arrow to `/ux-atomic-design`, classifying it as Enhancement. The MCP Server Classification table confirms: Enhancement MCP unavailability produces "cosmetic limitation warning, not a hard failure."

Yet the Wave 3 MCP Pre-Commitment section elevates Zeroheight to a Wave 3 BLOCK criterion, requiring documented feasibility assessment, cost authorization, and fallback workflow before Wave 3 entry. This creates a contradiction: if Zeroheight is Enhancement MCP (failure = cosmetic limitation), why does absence of Zeroheight integration *assessment* block Wave 3? The concern may be financial (the $99/month cost authorization), but cost authorization for an Enhancement MCP does not logically require blocking wave progression — it requires cost review before purchasing.

**Evidence:** MCP integration diagram (line 557): `ZH -.->|Enhancement| AD` (dashed = Enhancement). MCP Operational Constraints legend (line 566): "Dashed arrows (-.>) = Enhancement MCP (cosmetic limitation on failure)." Wave 3 MCP Pre-Commitment (line 604): "Wave 3 entry is BLOCKED without this integration assessment." MCP Integration Quality AC (line 852): "Enhancement MCP unavailability produces a cosmetic limitation warning, not a hard failure."

**Impact:** The BLOCK criterion for Zeroheight sends inconsistent signals to implementers. If Zeroheight is Enhancement, the wave should not block on its absence — it should warn. If Zeroheight is functionally Required for Wave 3, the MCP diagram should use a solid arrow. The misclassification could cause unnecessary Wave 3 delays (teams blocked waiting for Zeroheight assessment when they could proceed with the cosmetic-limitation fallback) or confusion about MCP tier semantics.

**Dimension:** Internal Consistency

**Response Required:** Either: (a) reclassify Zeroheight as Required MCP in the MCP diagram (solid arrow) and update the legend, if Wave 3 genuinely cannot deliver design system documentation without it; or (b) revise the Wave 3 MCP Pre-Commitment to produce a WARN (not BLOCK) for teams without Zeroheight, consistent with Enhancement MCP failure behavior.

**Acceptance Criteria:** Zeroheight's failure behavior is consistent between the MCP integration diagram classification (Enhancement vs. Required) and the Wave 3 entry criterion (WARN vs. BLOCK).

---

## Recommendations

### P0 (Critical -- MUST resolve before acceptance)

**DA-001-I7:** Resolve Haiku/T3 capability mismatch for `/ux-heuristic-eval`. Options: (a) add explicit pre-launch model capability benchmark AC, (b) upgrade to Sonnet with updated rationale, or (c) add documented justification for Haiku at T3. Without resolution, the Wave 1 sub-skill's model selection is internally inconsistent with its tool tier classification.

### P1 (Major -- SHOULD resolve; require justification if not)

**DA-002-I7:** Make BOOTSTRAP-VALIDATED retroactive validation enforceable by: specifying the "criterion-(a)-qualified evaluator joining" trigger operationally, defining a BOOTSTRAP-STATUS.md tracking artifact, and specifying the escalation path for failed re-evaluation.

**DA-003-I7:** Add a reviewer qualification cross-reference table mapping each review context (synthesis validation expert, benchmark expert panel, pre-launch blind evaluator) to the applicable qualification standard with rationale where they differ.

**DA-004-I7:** Expand Cross-Session State to list all persistent state artifacts (both Memory-Keeper keys and file-based), with rationale for which persistence pattern applies to each. Override audit and ABANDON log must appear in this section.

**DA-005-I7:** Incorporate the three WSM sensitivity analysis score deltas inline in the C1 Sensitivity Analysis paragraph, making the stability claim verifiable from the deliverable itself.

### P2 (Minor -- MAY resolve; acknowledgment sufficient)

**DA-006-I7:** Clarify WARN counter reset behavior at wave transitions (one sentence).

**DA-007-I7:** Add parenthetical distinguishing Gartner-reported from Gartner-inferred for the "most common segment" claim.

**DA-008-I7:** Differentiate Wave 2 entry criteria between Lean UX pathway (no launched product required) and HEART pathway (launched product with analytics required).

**DA-009-I7:** Align Zeroheight's Wave 3 enforcement behavior (WARN vs. BLOCK) with its Enhancement MCP classification.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | DA-008-I7 (Wave 2 HEART prerequisite gap) and DA-002-I7 (BOOTSTRAP-VALIDATED tracking registry absent) create specification completeness gaps |
| Internal Consistency | 0.20 | Negative | DA-003-I7 (expert qualification conflict), DA-004-I7 (Cross-Session State incomplete), DA-006-I7 (WARN counter reset ambiguity), DA-009-I7 (Zeroheight BLOCK vs. Enhancement) — four internal consistency issues |
| Methodological Rigor | 0.20 | Negative | DA-001-I7 (Critical: Haiku/T3 mismatch directly undermines the model selection methodology for the most critical Wave 1 sub-skill) |
| Evidence Quality | 0.15 | Negative | DA-005-I7 (WSM inline evidence incomplete despite S-003 recommendation), DA-007-I7 (inferential basis not distinguished) |
| Actionability | 0.15 | Negative | DA-002-I7 (BOOTSTRAP-VALIDATED enforcement gap means a concrete commitment is unactionable as specified) |
| Traceability | 0.10 | Neutral | Findings trace to specific sections; DA-003-I7 is a traceability concern but within the document, not across documents |

**Overall Assessment:** Targeted revision required. The deliverable's core architecture is sound and 6 prior iterations have eliminated structural issues. The remaining findings are precision gaps — 4 of the 5 non-Critical findings are internal consistency issues where two parts of the document make incompatible claims. DA-001-I7 (Critical) is the only finding that questions a design decision (Haiku model selection) rather than a documentation gap. Addressing the 5 P0/P1 findings should move the deliverable closer to the 0.92 threshold by improving Internal Consistency and Evidence Quality, the two dimensions most affected.

---

## Execution Statistics

- **Total Findings:** 9
- **Critical:** 1
- **Major:** 4
- **Minor:** 4
- **Protocol Steps Completed:** 5 of 5
