# Steelman Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

## Steelman Context

- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Deliverable Type:** Enhancement Issue (GitHub Issue body / design specification)
- **Criticality Level:** C4 (Critical -- architecture addition, irreversible once merged, tournament mode)
- **Strategy:** S-003 (Steelman Technique)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Steelman By:** adv-executor | **Date:** 2026-03-03T00:00:00Z | **Original Author:** Saucer Boy voice / Jerry framework
- **Iteration:** 4 (R3 applied 18 structural fixes from Iter 3 critique findings; this steelman evaluates the post-R3 revision)

---

## Summary

**Steelman Assessment:** The post-R3 deliverable has closed 18 structural critique findings -- the architecture is now well-specified, the enforcement mechanisms are defined (WAVE-N-SIGNOFF 3-state behavior, blind evaluation rubric, handoff contract, synthesis warning consistency). What remains are primarily argument-completeness gaps: the deliverable correctly states its claims but does not yet draw the strongest available conclusion from each claim. This iteration identifies two persistent Criticals (Part-time UX framing, time-to-first-value -- both carried from Iter 3, neither yet incorporated), one new Major surfaced by R3's blind evaluation rubric addition (the 15% threshold is stated but not calibrated), one persistent Major (adversarial quality provenance), and four Minors. The document is structurally sound; the remaining work is persuasion depth.

**Improvement Count:** 2 Critical, 2 Major, 4 Minor

**Original Strength:** Post-R3, this is a technically rigorous specification with well-defined enforcement mechanisms, honest limitations, and verifiable acceptance criteria. It is among the most thoroughly specified enhancement issues in the Jerry project corpus. The remaining gaps are in the persuasion layer -- not in what the document says but in whether it draws the maximum-strength conclusion from the evidence it already possesses.

**Recommendation:** Incorporate improvements. The 2 Critical findings remain from Iter 3 -- they are the clearest unaddressed barriers to maximum persuasive strength. The new Major (SM-004-I4: blind rubric calibration rationale) is specific and actionable. With these addressed, the deliverable should approach the quality gate ceiling.

---

## Steelman Reconstruction

The following reconstruction presents the deliverable in its strongest form at Iteration 4. Changes are annotated with `[SM-NNN-I4]` identifiers. Sections not annotated are preserved as-is from the post-R3 deliverable.

---

### The Problem > Who This Is For: Tiny Teams Population Segments (persistent strengthening -- SM-001-I4)

*[Population segments table preserved as-is.]*

The paragraph following the table currently reads:

> Teams in the "part-time UX" segment should treat wave progression beyond Wave 2 as aspirational and focus on the zero-MCP-cost sub-skills (HEART, JTBD, Kano, Behavior Design). Wave 1 requires zero MCP tool cost. Wave 2 MCP cost depends on Miro usage -- Lean UX requires Miro (free tier available; paid Starter tier $8/user/month for advanced features), while HEART has no required MCP.

[SM-001-I4] This guidance is correct but frames the "part-time UX" population as a constrained edge case rather than the primary design reality. The Part-time UX segment -- one person with less than 20% of their time on UX -- describes the **majority** of 2-5 person startups. The document's four-row segment table implies rough population parity; this understates the dominant case.

**Strengthened addition after the population segments table:**

> **The median tiny team is the "Part-time UX" case.** Across 2-5 person startups, having a dedicated UX specialist at any percentage of time is the exception. The skill portfolio is designed for this constraint as the primary design center, not as a fallback. Wave 1-2 sub-skills (Heuristic Eval, JTBD, Lean UX, HEART) function with zero required MCP cost and require no UX background to operate. Wave 1-2 are not "what you settle for" without a UX specialist -- they are a meaningful UX capability gain for a team that previously had none. A part-time UX person running Wave 1 gains structured heuristic evaluation and job statement synthesis: two capabilities that previously required either a UX contractor or going without.

---

### Key Design Decisions > 5. Wave Deployment (persistent strengthening -- SM-002-I4)

*[Wave deployment table, enforcement, bypass, and gantt preserved as-is.]*

[SM-002-I4] The wave progression section now correctly specifies entry criteria, WAVE-N-SIGNOFF enforcement with 3-state behavior, and bypass documentation. What it still does not answer is: **when does the team receive its first tangible output from the Wave 1 investment?** The enforcement mechanism is defined; the value delivery timing is not.

**Strengthened addition after the wave stall bypass paragraph:**

> **Time to first value: the Wave 1 window.** Wave 1 is designed to deliver the first structured UX output within a single working session after kickoff. KICKOFF-SIGNOFF.md completion is a one-time setup exercise of approximately 20 minutes. A developer with no UX background can then invoke `/ux-heuristic-eval` with a design screenshot and receive a severity-rated findings report against all 10 Nielsen heuristics -- without completing any prior wave, without MCP tools, and without UX documentation. From kickoff to first heuristic findings report: under 2 hours. This is the concrete return on the Wave 1 entry investment (8-13 days implementation effort). The 3-state wave enforcement (PASS / WARN / BLOCK) governs access to Wave 2+; it does not delay Wave 1 value. Teams apprehensive about the 30-50 day total estimate should anchor on Wave 1: 8-13 days of effort, value delivered in the first session after completion.

---

### Research Backing > Adversarial Validation (persistent strengthening -- SM-003-I4)

*[Tournament summary table preserved as-is.]*

The adversarial validation section records process metrics (8 iterations, 13 revisions, 9 strategies, 13 P0 findings) and concludes: "not that the analysis is perfect, but that it has been systematically attacked from nine different angles and survived." This is a process claim. It asserts that the tournament ran; it does not demonstrate what the tournament changed.

[SM-003-I4] The quality provenance argument -- showing that the tournament produced specific corrections, not merely procedural compliance -- is the strongest version of this section:

**Strengthened addition after the tournament summary table:**

> **What the tournament changed.** The pre-tournament deliverable had three categories of weakness that the adversarial process surfaced and corrected:
>
> 1. **Arithmetic errors (Chain-of-Verification):** Five arithmetic errors in the WSM scoring were found and corrected across 5 error-correction rounds. The selection ranking changed for 3 of the 10 frameworks. The final scores reflect verified calculations, not a first-pass analysis.
>
> 2. **Design contradiction (FMEA):** The Behavior Design sub-skill had a contradiction between its LOW-confidence structural omission gate and its output labeled "design intervention recommendations." A LOW-confidence sub-skill cannot produce prescriptive design recommendations. Resolution required a deliberate design decision: rename to "Reference Intervention Patterns," reclassify as MEDIUM confidence, and restructure the output contract. This is not a cosmetic fix -- it changed what the sub-skill promises to deliver.
>
> 3. **Enforcement closure gaps (Pre-Mortem, Red Team):** The original specification had no Issue Closure Condition (any AC could be treated as blocking), no WAVE-N-SIGNOFF.md enforcement (wave gates were aspirational, not checked), and no pre-launch external validation requirement (quality benchmarks were defined but not demonstrated). All three are now closed with specific mechanisms.
>
> A document that has survived 9 adversarial strategies, corrected 5 arithmetic errors, resolved a design contradiction, and closed 3 enforcement gaps is structurally different from a first-draft specification that merely references a tournament. The selection is not "10 highest-scoring frameworks from a possibly-flawed analysis" -- it is the result of a self-correcting process with documented specific corrections.

---

### Acceptance Criteria > Pre-Launch Validation (new strengthening -- SM-004-I4)

*[Pre-launch validation AC preserved as-is.]*

The R3 fix (RT-001-I3) correctly added a blind evaluation rubric with a 15% threshold and 3-dimension scoring (completeness, actionability, time-to-insight). This is the right architecture. However, the 15% threshold and the 3-dimension choice are stated without explaining their derivation -- a reviewer challenging the benchmark could ask "why 15%?" and "why those three dimensions?"

[SM-004-I4] **Strengthened pre-launch validation AC with calibration rationale:**

Replace:

> Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions.

With:

> Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions. **Calibration rationale:** The 3 dimensions -- completeness, actionability, and time-to-insight -- are selected because they map to the three most common failure modes of AI-augmented analysis outputs: (a) completeness catches systematic omission bias (AI models trained on summarized content tend to miss edge cases present in original research); (b) actionability catches specificity degradation (AI outputs that are technically correct but insufficiently specific for a team to act on them); (c) time-to-insight catches efficiency regression (a benchmark that takes 2x as long to produce is not an improvement even if the output quality is equivalent). The 15% threshold is conservative by design: an 85% quality floor against a human-produced reference output is the minimum bar for a structured methodology tool that teams will use to make product decisions. A lower threshold (e.g., 25%) would permit AI-augmented outputs that meaningfully underperform manual analysis; a higher threshold (e.g., 5%) would be unrealistically demanding for AI tools producing structured synthesis. The 15% threshold should be revisited after Wave 1 beta usage if empirical performance data suggests recalibration is appropriate.

---

### Key Design Decisions > 2. Parent Orchestrator Routes via Lifecycle-Stage Triage (new strengthening -- SM-005-I4)

*[Routing triage flowchart and common intent resolution table preserved as-is.]*

The WAVE-N-SIGNOFF BLOCK state is defined as: "Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process." The mechanism is correct. The user experience of the BLOCK state is not described -- specifically, what the orchestrator communicates to the user when it blocks routing.

[SM-005-I4] **Strengthened BLOCK state user experience:**

Add after the 3-state behavior definition:

> **BLOCK state user experience (the orchestrator message):** When WAVE-{N}-SIGNOFF.md does not exist, the orchestrator produces the following structured response:
>
> > "Wave {N+1} sub-skills ({list}) require Wave {N} completion. `WAVE-{N}-SIGNOFF.md` has not been created. To advance: (1) complete the Wave {N} entry criteria ({list from wave table}), (2) complete `WAVE-{N}-SIGNOFF.md` using the template at `skills/user-experience/templates/wave-signoff-template.md`, and (3) re-invoke `/user-experience`. If your team has a documented reason to proceed despite incomplete Wave {N} criteria, use the bypass process -- the orchestrator will walk you through the 3-field bypass documentation."
>
> The BLOCK state does not terminate the session. The user can still invoke Wave 1-{N} sub-skills directly. This preserves user authority (P-020) while enforcing the wave prerequisite gate.

---

### Estimated Scope (minor strengthening -- SM-006-I4)

*[Scope estimates and comparable delivery reference preserved.]*

[SM-006-I4] The scope section closes with an operational note: "If Wave 1 completion exceeds 15 days, the per-sub-skill estimates for subsequent waves should be revised upward." This is useful but tonally flat given the document's consistent McConkey framing. The other major persuasion sections (Problem, Known Limitations, Capability Map) all close with a mountain metaphor callback; the Scope section is the only exception.

**Strengthened closing for Estimated Scope:**

Add after the current last line:

> Wave 1 is the first drop-in. Eight to thirteen days. That is the commitment. Every subsequent wave is a follow-on line off the same peak -- you ski them when the first one goes clean.

---

### V2 Roadmap > V2 Candidates (minor strengthening -- SM-007-I4)

*[V2 candidates table preserved.]*

The Service Blueprinting P1 entry reads: "Covers end-to-end service process niche; also the auto-substitute if AI-First Design Enabler expires." The P1 ranking appears inconsistent with its WSM score (7.40) compared to other V2 candidates that are unlisted. The dual-purpose justification -- primary gap coverage AND pre-committed substitution path -- is the explanation for P1 status, but it is not stated.

[SM-007-I4] **Strengthened Service Blueprinting V2 P1 justification:**

Replace the Service Blueprinting row description with:

> Covers end-to-end service process niche; **dual-purpose P1 priority**: (1) fills the service design lifecycle gap not covered by any V1 framework; (2) is the pre-committed auto-substitute if the AI-First Design Enabler expires at Wave 5 -- this substitution path is declared in the Known Limitations section, making Service Blueprinting the only V2 candidate with a pre-activated adoption trigger. Score 7.40 ranks lower than AI-First Design (7.80P) but Service Blueprinting's P1 V2 status is partially pre-approved by the V1 conditional design: if the AI-First Design Enabler expires, Service Blueprinting activates without further prioritization debate.

---

### Relationship to Existing Jerry Skills (minor strengthening -- SM-008-I4)

*[Mermaid ecosystem diagram and integration table preserved.]*

The ecosystem integration section maps directional relationships but does not demonstrate compound value -- the case that using Jerry skills in sequence produces more than the sum of individual outputs.

[SM-008-I4] **Strengthened addition after the integration table:**

> **The compound workflow story.** The highest-value use of the Jerry ecosystem is the full discovery-to-measurement loop:
>
> 1. `/problem-solving` (`ps-researcher`) provides competitive context for JTBD job analysis.
> 2. `/ux-jtbd` converts that research into specific job statements defining the product challenge.
> 3. `/ux-design-sprint` uses the JTBD job statement as its challenge statement input -- "why are we sprinting?" answered before Day 1.
> 4. `/nasa-se` converts Sprint findings (validated prototype with Day 4 test data) into technical requirements with UX-grounded acceptance criteria.
> 5. `/ux-heart-metrics` measures whether the shipped product achieves the goals defined by the job statements from Step 2 -- the loop closes.
> 6. `/adversary` provides quality gates on the UX deliverables at wave transitions.
>
> A team running this full loop produces a product where user research (JTBD) directly informs the sprint challenge, the sprint prototype directly informs technical requirements, and UX metrics measure against the original job-to-be-done. Teams already using `/problem-solving` and `/nasa-se` get compounding return from adding `/user-experience` -- the integration is not cosmetic. The incremental adoption question becomes: "what does adding Wave 1 cost against our existing Jerry workflow?" rather than "is a 30-50 day investment justified?"

---

### Best Case Scenario (updated for Iter 4)

The `/user-experience` skill proposal is most compelling under the following conditions:

1. **Team size 2-5, with UX as a part-time responsibility.** This is the median scenario, not an edge case. Wave 1-2 deliver the highest capability-per-hour return for this configuration.

2. **Teams already in the Figma + Miro workflow.** The Minimal tier (~$23/seat/month) unlocks 9 of 10 sub-skills for teams already paying Figma and Miro subscriptions. The incremental cost of `/user-experience` is effectively zero tool-cost for these teams.

3. **Products with iterative design cycles (bi-weekly releases or faster).** The Lean UX hypothesis cycle and Heuristic Eval iteration pattern are optimized for high-cadence iteration.

4. **Jerry framework users already practicing methodology-driven development.** Teams already using `/problem-solving` and `/nasa-se` get the full compound return from the discovery-to-measurement loop.

5. **Teams blocked on methodology knowledge, not on time.** The skill removes the methodology knowledge barrier. It does not remove the time barrier -- users still need to provide screenshots, conduct interviews, and interpret findings.

**Key assumptions that must hold:**
- MCP server availability for Figma-dependent sub-skills (mitigated by documented non-MCP fallbacks)
- AI LLM capability sufficient to apply 10-heuristic evaluation, B=MAP diagnosis, and Kano classification with acceptable accuracy (mitigated by per-sub-skill quality benchmarks with blind external validation)
- Teams willing to invest 8-13 days for Wave 1 before first return (mitigated: first deliverable on day 1 of Wave 1 completion, under 2 hours from kickoff)

**Confidence in the Steelmanned version:** HIGH. The two persistent Critical findings (SM-001-I4, SM-002-I4) are argument completeness gaps, not substantive flaws -- the underlying claims are valid, the strongest conclusion has simply not yet been drawn from the available evidence. R3's structural fixes (WAVE-N-SIGNOFF enforcement, blind evaluation rubric, synthesis warning consistency, handoff contract) have closed the enforcement gaps identified in prior iterations. The deliverable is structurally sound and defensible; the remaining improvements are persuasion-layer additions.

---

## Improvement Findings Table

| ID | Improvement | Severity | Original (Before) | Strengthened (After) | Dimension |
|----|-------------|----------|-------------------|----------------------|-----------|
| SM-001-I4 | "Part-time UX" framed as primary design center, not constrained edge case | Critical | Segment listed as one of four with MEDIUM fit rating and caveat guidance; implicit population parity | Explicit statement that Part-time UX is the median tiny team scenario; Wave 1-2 described as genuine capability gain, not fallback option | Evidence Quality / Actionability |
| SM-002-I4 | Time-to-first-value story for Wave 1 | Critical | Wave enforcement (PASS/WARN/BLOCK) defined; entry criteria specified; time-to-first-output absent | Added: KICKOFF-SIGNOFF ~20 min; first heuristic findings report under 2 hours; Wave 1 value independent of 30-50 day total; anchor on 8-13 day Wave 1 | Actionability / Completeness |
| SM-003-I4 | Adversarial validation demonstrates specific corrections, not just process completion | Major | Tournament summary table: 8 iterations, 13 revisions, 9 strategies, 13 P0 findings. Claims "systematic attack from nine angles and survived" -- process claim without outcome specifics | Added: three categories of pre-tournament weakness with named examples (5 arithmetic errors corrected, Behavior Design contradiction resolved, 3 enforcement gaps closed) | Evidence Quality / Traceability |
| SM-004-I4 | Blind evaluation rubric calibration rationale | Major | 15% threshold stated; 3 dimensions listed (completeness, actionability, time-to-insight); no derivation for why these choices are correct | Each dimension maps to a specific AI output failure mode; 15% threshold justified as conservative floor for methodology tool; recalibration trigger defined | Methodological Rigor / Evidence Quality |
| SM-005-I4 | BLOCK state user experience message defined | Minor | BLOCK state behavior: "refuses to route and directs user to complete signoff" -- correct mechanism, absent UX for the block | Concrete orchestrator message template showing path to resolution and direct invocation as fallback -- preserves P-020 while enforcing gate | Completeness / Actionability |
| SM-006-I4 | McConkey metaphor close for Estimated Scope | Minor | Scope section ends with a calibration note ("if Wave 1 exceeds 15 days, revise upward") -- correct but tonally inconsistent with rest of document | One-sentence McConkey callback: "Wave 1 is the first drop-in. Eight to thirteen days. That is the commitment." -- ties scope section to commitment framing | Internal Consistency |
| SM-007-I4 | Service Blueprinting V2 P1 dual-purpose justification | Minor | P1 status stated; single-sentence rationale; WSM score (7.40) lower than unlisted candidates without explanation | Dual-purpose justification: gap coverage + pre-committed substitution path; explains why score rank does not match priority rank | Traceability |
| SM-008-I4 | Compound workflow value of Jerry ecosystem integration | Minor | Integration table maps directional relationships; compound value of sequential use not demonstrated | 6-step full discovery-to-measurement loop showing how each skill adds value to the downstream skill; reframes adoption question as marginal cost against existing Jerry workflow | Actionability / Completeness |

---

## Improvement Details

### SM-001-I4: "Part-time UX" as Primary Design Center

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | The Problem > Who This Is For: Tiny Teams Population Segments |
| **Affected Dimension** | Evidence Quality / Actionability |

**Original Content (lines 74-81):**

> Segment table with four rows listing "Part-time UX" as one of four equally-weighted segments with MEDIUM portfolio fit, followed by: "Teams in the 'part-time UX' segment should treat wave progression beyond Wave 2 as aspirational..."

**Strengthened Content:** See reconstruction above. Key addition: "The median tiny team is the 'Part-time UX' case. Wave 1-2 are not 'what you settle for' without a UX specialist -- they are a meaningful UX capability gain for a team that previously had none."

**Rationale:** The four-row segment table implies comparable population distribution across segments. The Part-time UX case -- where UX is a secondary responsibility for one person -- describes the majority of 2-5 person startups. By placing it as one of four rows with a MEDIUM fit rating and a caveat, the document inadvertently signals to the most likely reader (a part-time UX person in a small team) that the skill may not be for them. Reframing it as the primary design center is more accurate and rhetorically stronger: the skill was designed for the harder constraint, not the easier one. The MEDIUM fit rating also deserves qualification -- for Wave 1-2, the fit is HIGH; the MEDIUM rating reflects limitations at Wave 3-5 for this segment, not the overall portfolio.

**Best Case Conditions:** Most effective for readers who ARE in the Part-time UX category -- the intended primary audience. This framing validates their constraint rather than treating it as exceptional.

---

### SM-002-I4: Time-to-First-Value Story

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions > 5. Wave Deployment |
| **Affected Dimension** | Actionability / Completeness |

**Original Content:** The wave progression section (post-R3) now defines entry criteria, 3-state enforcement, and bypass documentation. It specifies when teams can advance between waves. It does not specify when teams receive first value from the Wave 1 implementation investment.

**Strengthened Content:** See reconstruction above. Key addition: "From kickoff to first heuristic findings report: under 2 hours. Teams apprehensive about the 30-50 day total estimate should anchor on Wave 1: 8-13 days of effort, value delivered in the first session after completion."

**Rationale:** The 3-state enforcement mechanism (PASS/WARN/BLOCK) is now fully defined -- it tells a team when they can proceed to Wave 2. The persuasion gap is different: a team deciding whether to begin Wave 1 implementation is asking "when do I see something useful?" not "when can I proceed to Wave 2?" The under-2-hours-to-first-output claim is the answer to the adoption decision question. Without it, the enforcement mechanism framing inadvertently emphasizes gates and restrictions (when you cannot advance) rather than value delivery (when you gain capability). Making the time-to-first-value explicit converts the framing from a gating document to a value delivery document with guardrails.

**Best Case Conditions:** Most compelling for teams evaluating whether to begin implementation. The "under 2 hours to first output" claim is credible for heuristic evaluation (screenshot input, structured report output) and creates a concrete first-session commitment rather than a 30-50 day horizon.

---

### SM-003-I4: Adversarial Validation Quality Provenance

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Research Backing > Adversarial Validation |
| **Affected Dimension** | Evidence Quality / Traceability |

**Original Content (lines 946-960):**

> Tournament summary table recording 8 iterations, 13 revisions, 9 strategies, 13 P0 findings. Closing statement: "not that the analysis is perfect, but that it has been systematically attacked from nine different angles and survived."

**Strengthened Content:** See reconstruction above. Added three categories of pre-tournament weakness with specific named examples: (1) arithmetic errors found and corrected, (2) Behavior Design contradiction resolved with named design decision, (3) three enforcement gaps closed with specific mechanism names.

**Rationale:** "Systematic attack from nine angles" asserts process effort, not outcome quality. A skeptical reviewer could argue that a flawed analysis can run through an adversarial tournament and emerge substantively unchanged if the attack strategies are not sharp enough. The quality provenance argument is different: it shows the tournament found specific errors and produced specific corrections. The corrections are verifiable (the R2/R3 change annotations in the document are the evidence trail). The difference between "the process ran" and "the process worked" is the difference between procedural compliance and substantive quality improvement. This finding has been present since Iter 3; it has not been incorporated, suggesting it belongs in the author's next revision pass.

**Best Case Conditions:** Strongest when the reader has encountered analyses that underwent "review" but emerged unchanged. The specific-corrections framing proves the adversarial process had teeth.

---

### SM-004-I4: Blind Evaluation Rubric Calibration Rationale

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Pre-Launch Validation |
| **Affected Dimension** | Methodological Rigor / Evidence Quality |

**Original Content (lines 840):**

> "Comparison uses a blind evaluation rubric: 3 independent evaluators score both the AI-augmented output and a manually-produced reference output on completeness, actionability, and time-to-insight without knowing which is AI-augmented. Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions."

**Strengthened Content:** See reconstruction above. Each dimension maps to a specific AI output failure mode; 15% threshold justified as conservative floor for methodology tool; recalibration trigger defined for post-beta empirical data.

**Rationale:** R3's addition of the blind evaluation rubric is a genuine structural improvement -- it closes the "benchmarks defined but not demonstrated" enforcement gap. The remaining weakness is that the rubric looks arbitrary to a reviewer: why completeness, actionability, and time-to-insight? Why 15%? The failure-mode mapping shows the three dimensions were derived from known AI output weaknesses, not chosen arbitrarily. The 15% calibration rationale shows it is conservative by design, not permissive. This is important because the pre-launch validation AC is the most concrete quality enforcement mechanism in the specification -- if the rubric itself appears arbitrary, the entire quality gate loses credibility. Making the derivation explicit transforms the rubric from a stated requirement to a justified methodology.

**Best Case Conditions:** Strongest when the reader is a practitioner who has used AI tools to produce structured analysis outputs and encountered the specific failure modes (omission bias, specificity degradation, efficiency regression) the dimensions are designed to catch.

---

### SM-005-I4: BLOCK State User Experience Message

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions > 5. Wave Deployment > Wave Enforcement 3-State Behavior |
| **Affected Dimension** | Completeness / Actionability |

**Original Content (lines 628):**

> "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process."

**Strengthened Content:** See reconstruction above. Concrete orchestrator message template showing the specific content of the BLOCK response: lists unmet criteria, references template location, explains bypass path, and notes that direct Wave 1-N invocation remains available.

**Rationale:** The BLOCK mechanism is correct. The user experience of the block -- what the orchestrator actually says -- matters for adoption. A BLOCK state that produces an opaque refusal will feel punitive; a BLOCK state that produces a clear resolution path will feel helpful. The message template also makes the P-020 compliance argument explicit: the user is not permanently blocked, they can still use Wave 1-N sub-skills directly. Without this distinction, a user experiencing a BLOCK might interpret it as the skill being broken rather than a prerequisite check. The message template is specifiable now and should be part of the AC, not deferred to implementation.

**Best Case Conditions:** Most relevant for implementers defining the orchestrator behavior. Defines the user experience of the gate rather than just the gate's existence.

---

### SM-006-I4: McConkey Metaphor Close for Estimated Scope

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Estimated Scope |
| **Affected Dimension** | Internal Consistency |

**Original Content (line 1150):**

> "If Wave 1 completion (parent + 2 sub-skills, ~8-13 days) exceeds 15 days, the per-sub-skill estimates for subsequent waves should be revised upward."

**Strengthened Content:** One-sentence McConkey callback: "Wave 1 is the first drop-in. Eight to thirteen days. That is the commitment. Every subsequent wave is a follow-on line off the same peak -- you ski them when the first one goes clean."

**Rationale:** The document uses the McConkey mountain metaphor consistently throughout -- opener ("boldest line"), Problem ("skiing with your eyes closed"), Limitations ("respect the mountain"), Capability Map ("line nobody thought was skiable"). The Estimated Scope section is the only major persuasion section without this voice. The current closing note is technically correct but reads like a different document. Adding the McConkey close ties the scope section back to the commitment framing and reinforces that Wave 1 is the manageable first commitment, not the 30-50 day full mountain. This is a voice consistency fix, not a content gap.

---

### SM-007-I4: Service Blueprinting V2 P1 Dual-Purpose Justification

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | V2 Roadmap > V2 Candidates |
| **Affected Dimension** | Traceability |

**Original Content (line 887):**

> `| **P1** | No service design coverage | `/ux-service-blueprinting` (rank #12, score 7.40) | Covers end-to-end service process niche; also the auto-substitute if AI-First Design Enabler expires |`

**Strengthened Content:** See reconstruction above. Explicitly states the dual-purpose justification and explains why score rank (7.40) does not conflict with V2 priority rank (P1): the substitution path is pre-committed by the V1 conditional design.

**Rationale:** The P1 designation for Service Blueprinting (7.40) while higher-scoring frameworks are absent from the V2 table creates an apparent inconsistency that a traceability reviewer will notice. The explanation -- that the substitution path is pre-activated by the AI-First Design Enabler expiry trigger -- resolves the inconsistency but is not stated. Making it explicit closes a traceability gap that is currently latent but would surface in any detailed review of V2 prioritization rationale.

---

### SM-008-I4: Compound Workflow Value of Jerry Ecosystem Integration

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Relationship to Existing Jerry Skills |
| **Affected Dimension** | Actionability / Completeness |

**Original Content (lines 988-995):**

> Integration table mapping directional relationships between `/user-experience` and 6 other Jerry skills. Individual integrations described; no sequential workflow demonstration.

**Strengthened Content:** See reconstruction above. Added 6-step full discovery-to-measurement loop showing compound value; reframes adoption question as marginal cost against existing Jerry workflow rather than standalone 30-50 day investment.

**Rationale:** The integration table is accurate but static. It shows connections exist, not why they matter in sequence. The compound workflow argument makes three claims the table cannot: (1) each skill in the chain adds specific value to the downstream skill; (2) the loop closes (HEART measures against the original JTBD job-to-be-done); (3) for teams already using `/problem-solving` and `/nasa-se`, the adoption question becomes "what is the marginal cost of adding Wave 1 to our existing workflow?" rather than "is a 30-50 day investment justified?" The last point is the strongest adoption argument for the existing Jerry user base -- the primary audience for a GitHub enhancement issue in the Jerry repository.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Positive | SM-002 (wave deployment time-to-value), SM-005 (BLOCK state UX), SM-008 (compound workflow) fill identified completeness gaps |
| Internal Consistency | 0.20 | Positive | SM-001 (Part-time UX framing removes implicit population ranking inconsistency), SM-006 (McConkey close restores voice consistency in Scope section) |
| Methodological Rigor | 0.20 | Positive | SM-004 (blind rubric calibration rationale) directly strengthens methodological rigor of the pre-launch validation mechanism; SM-003 (quality provenance) demonstrates methodology produced real corrections |
| Evidence Quality | 0.15 | Positive | SM-003 (specific tournament corrections), SM-004 (failure-mode rationale), SM-001 (median-case framing accuracy) all add evidence quality |
| Actionability | 0.15 | Positive | SM-002 (time-to-first-value), SM-005 (BLOCK state resolution path), SM-008 (compound workflow adoption reframe) are directly actionable improvements |
| Traceability | 0.10 | Positive | SM-007 (Service Blueprinting P1 justification), SM-003 (tournament corrections trail), SM-004 (rubric criteria derivation) improve traceability from claims to evidence |

**Net assessment:** All 6 scoring dimensions positively impacted. The two Critical findings (SM-001-I4, SM-002-I4) affect Completeness, Actionability, and Evidence Quality -- the highest-weight dimensions. SM-004-I4 (blind rubric calibration) is a new finding from R3's additions that directly strengthens Methodological Rigor, which at 0.20 weight is the highest-value dimension gap remaining.

---

## Iteration Comparison Note

**Iter 3 vs. Iter 4 findings:**

- SM-001 and SM-002 are persistent Criticals from Iter 3, not yet incorporated in the deliverable. Their persistence confirms they represent genuine argument completeness gaps rather than items already addressed.
- SM-003 (quality provenance) is a persistent Major from Iter 3, not yet incorporated. Its continuing absence suggests it should be the highest-priority incorporation target after the two Criticals.
- SM-004-I4 (blind rubric calibration) is **new to Iter 4** -- it was created by R3's addition of the blind evaluation rubric. R3 added the mechanism but not its justification. This is the most important new finding this iteration.
- SM-005-I4 (BLOCK state UX) is **new to Iter 4** -- created by R3's WAVE-N-SIGNOFF 3-state definition. The mechanism is defined; the user experience of the BLOCK state is not.
- SM-006/SM-007/SM-008 carry forward from Iter 3 (SM-007/SM-008 from prior Minor items; SM-006 is the McConkey close). These remain Minor and should be incorporated in a single revision pass.

**Trend:** From Iter 3 (2 Critical, 3 Major, 3 Minor) to Iter 4 (2 Critical, 2 Major, 4 Minor). Reduction in Major findings reflects that R3's structural fixes were substantial; new Minors reflect R3 adding new content that itself has argument completeness opportunities. The Critical count remaining at 2 reflects that the most important persuasion-layer arguments have not yet been incorporated.

---

## Execution Statistics

- **Total Findings:** 8 (2 Critical, 2 Major, 4 Minor)
- **Critical:** 2 (SM-001-I4 Part-time UX as median case; SM-002-I4 Time-to-first-value)
- **Major:** 2 (SM-003-I4 Tournament quality provenance; SM-004-I4 Blind rubric calibration rationale)
- **Minor:** 4 (SM-005-I4 BLOCK state UX; SM-006-I4 McConkey close; SM-007-I4 Service Blueprinting P1; SM-008-I4 Compound workflow)
- **Protocol Steps Completed:** 6 of 6
- **New findings this iteration:** SM-004-I4, SM-005-I4 (both created by R3 additions that introduced new arguments without full justification)
- **Persistent findings:** SM-001-I4, SM-002-I4, SM-003-I4 (carried from Iter 3; not yet incorporated in R3)

---

*Strategy Execution Report*
*Strategy: S-003 (Steelman Technique)*
*Template: `.context/templates/adversarial/s-003-steelman.md`*
*Deliverable: `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`*
*Executed: 2026-03-03T00:00:00Z*
*Iteration: 4*
