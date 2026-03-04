# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context

- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 2 (R1 revision applied; Iteration 1 scored 0.704 REVISE)
- **H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (confirmed by Research Backing section referencing prior adversarial tournament at C4; prior strategy outputs include Steelman per tournament chain)
- **Criticality:** C4 (GitHub Enhancement issue for a framework skill addition -- architecture-level change touching mandatory-skill-usage.md, CLAUDE.md, AGENTS.md, ~67 artifacts; irreversible once merged and adopted)

---

# Pre-Mortem Report: `/user-experience` Skill Enhancement Issue

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `ux-skill-issue-body-saucer-boy.md` -- GitHub Enhancement issue, `/user-experience` skill, ~1114 lines
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004)
**H-16 Compliance:** S-003 Steelman applied in prior tournament chain (confirmed)
**Failure Scenario:** It is March 2027. The `/user-experience` skill was merged into Jerry 12 months ago. Wave 1 was delivered but usage has flatlined. Fewer than 3 teams have advanced beyond Wave 2. The maintainers are discussing deprecation. The issue body did not prevent this outcome -- it either specified something that could not be built as written, attracted no sustained adopters, or created implementation ambiguity that caused the skill to ship in degraded form.

---

## Summary

The deliverable is a richly detailed enhancement proposal that has been significantly strengthened by R1 revision. The proposal demonstrates genuine architectural rigor across scope, MCP integration design, and wave deployment structure. However, the Pre-Mortem analysis -- imagining this skill has definitively failed 12 months after merge -- surfaces 3 Critical and 6 Major failure causes that the current text does not sufficiently guard against. The most dangerous failure modes cluster around three themes: (1) the gap between the issue's confident framing and the actual implementation complexity of 11 independent Jerry skills requiring sustained maintenance commitment, (2) the absence of a governing success criterion that would tell implementers when Wave 1 is "good enough" to claim the issue resolved, and (3) MCP brittleness that the fallback documentation acknowledges but does not operationally solve. The overall risk posture is HIGH. The recommendation is REVISE before acceptance -- targeted additions to the Acceptance Criteria, scope framing, and operational failure mode documentation would substantially reduce the residual risk.

---

## Step 2: Temporal Perspective Shift

**Retrospective frame established:** It is March 2027. The issue was merged in early March 2026. We are analyzing from the retrospective vantage point of a skill that has failed to achieve adoption and is under consideration for removal. We are not predicting failure -- we are explaining it after the fact.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-20260303 | No single "done" definition: Wave 1 ships but the issue body never specifies what constitutes the issue being CLOSED, so implementation drifts indefinitely | Process | High | Critical | P0 | Completeness |
| PM-002-20260303 | MCP ecosystem churn invalidates the architecture: Figma or Miro breaks their MCP contract within 12 months, rendering 4-6 sub-skills degraded permanently | External | High | Critical | P0 | Internal Consistency |
| PM-003-20260303 | 30-50 day scope estimate collapses under real-world friction: Wave 1 alone takes 20+ days, Wave 2-5 stall indefinitely due to MCP integration unknowns | Resource | High | Critical | P0 | Evidence Quality |
| PM-004-20260303 | Wave entry criteria are unmeasurable in practice: teams cannot self-assess whether they have met Wave 2-5 entry criteria without tooling that does not exist | Process | High | Major | P1 | Actionability |
| PM-005-20260303 | The synthesis hypothesis confidence gate has no enforcement path: a user submits LOW-confidence output into a product decision; the `Human Override Justification` field is ignored by every user | Technical | High | Major | P1 | Methodological Rigor |
| PM-006-20260303 | AI-First Design Enabler blocks Wave 5 indefinitely: the 90-day expiry triggers substitution to Service Blueprinting, but Service Blueprinting is not specified in the issue and cannot be built from the information present | Assumption | Medium | Major | P1 | Completeness |
| PM-007-20260303 | Cross-sub-skill integration is untested in the issue spec: the canonical sequences (JTBD -> Design Sprint -> HEART) have no acceptance criteria for integration handoffs, so they ship as conceptual but not functional | Process | Medium | Major | P1 | Actionability |
| PM-008-20260303 | Quality benchmarks are subjective or circular: several per-sub-skill ACs use rubrics that require a UX practitioner to evaluate outputs -- a resource the tiny teams audience by definition does not have | Assumption | Medium | Major | P1 | Evidence Quality |
| PM-009-20260303 | The user research gap warning is displayed but not architecturally enforced: the onboarding warning fires once per session, but teams building consumer products continue using synthesis outputs without validation after dismissing the warning | Technical | Medium | Minor | P2 | Methodological Rigor |
| PM-010-20260303 | V2 trigger conditions are well-defined but V2 has no delivery commitment: trigger conditions fire with no assigned owner, timeline, or funding, so P1 gaps (user research, dark patterns) remain open indefinitely | Resource | Medium | Minor | P2 | Completeness |
| PM-011-20260303 | The Design Sprint "4-day to 1-2 day collapse" for solo/pair teams has no validated methodology: claiming a 4-day process collapses to 1-2 days with AI filling missing-participant roles is an unvalidated assumption | Assumption | Low | Minor | P2 | Evidence Quality |

---

## Detailed Findings

### PM-001-20260303: No Single "Done" Definition [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The Acceptance Criteria section lists 30+ individual checkboxes across Parent Orchestrator, Wave 1, Wave 2-5, Synthesis Validation, MCP Integration, Quality Standards, Wave Progression, and Post-Launch Metrics subsections. There is no single acceptance criterion that defines when the GitHub issue itself can be closed. Implementers have no canonical signal for "done at the issue level" -- the issue stays open as a permanent tracker rather than being closeable at Wave 1 completion.

**Evidence:** The Acceptance Criteria section (lines 742-823) contains subsections for 8 distinct concern areas. The Wave Progression subsection (lines 809-813) requires wave 2-5 criteria to be documented but those sub-skills are explicitly out of scope for the "Minimum Viable Launch." The issue does not state which subset of ACs closes the issue. The Estimated Scope section (lines 1092-1101) distinguishes Wave 1 from subsequent waves but does not map that distinction to issue closure.

**Analysis:** GitHub issues are closed when their acceptance criteria are satisfied. If the issue can only be closed when all 10 sub-skills are complete (30-50 days), it will never be closed in a timely way and will become a permanent "tracking issue" that loses relevance. If the issue is intended to be closeable at Wave 1 completion (~8-13 days per Estimated Scope), that must be explicit -- otherwise the Wave 2-5 ACs create phantom requirements that block closure.

**Recommendation:** Add a closing condition statement at the top of the Acceptance Criteria section: "**Issue Closure Condition:** This issue is CLOSED when Wave 1 Minimum Viable Launch ACs are satisfied (Parent Orchestrator + `/ux-heuristic-eval` + `/ux-jtbd` + Synthesis Validation + MCP Integration Quality + Quality Standards). Wave 2-5 sub-skills are tracked as child issues created at Wave 1 merge." Mark all Wave 2-5 ACs as "Tracked in child issues, not required for this issue closure."

**Acceptance Criteria:** The issue body explicitly states a single closure condition. Wave 2-5 delivery is tracked in child issues with explicit worktracker entity links.

---

### PM-002-20260303: MCP Ecosystem Churn Invalidates Architecture [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions -- MCP Integration; Known Limitations -- Figma Single Point of Failure |
| **Strategy Step** | Step 3 (External failures lens) |

**Failure Cause:** The skill's architecture makes 4 sub-skills non-functional and 6 sub-skills degraded if the Figma MCP contract changes. Figma has a documented history of monetizing previously free integrations (Dev Mode became paid in 2023, cited at line 715). The issue acknowledges this risk but treats the fallback paths as sufficient mitigation. In the retrospective: Figma restricted its MCP server to paid tiers in Q3 2026. The quarterly MCP audit cadence was never operationalized because no named maintenance owner was formally assigned. The sub-skills degraded silently. Users received cryptic MCP failure errors with no self-healing behavior.

**Evidence:** The MCP Integration section (lines 496-584) documents 4 Required MCP integrations for Figma. The Known Limitations section (lines 713-721) acknowledges Figma SPOF and lists mitigations including "quarterly MCP audit cadence with named maintenance owner" -- but the Acceptance Criteria section does not include an AC requiring a named maintenance owner or a written audit schedule. The MCP Integration Quality ACs (lines 793-797) require MCP pre-checks and fallback paths but do not require an operational audit process to be established before issue closure.

**Analysis:** Fallback paths documented in the issue body are design-time artifacts. They become operational only if the implementation team reads them, implements them correctly, and actively monitors MCP health. The "quarterly audit with named owner" mitigation is entirely unverifiable from the issue -- it is a good-faith commitment with no AC. In a real retrospective, this is the category of commitment that consistently fails to materialize.

**Recommendation:** Add to the MCP Integration Quality ACs: "[ ] A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md` with explicit responsibility for the quarterly audit cadence. [ ] A `skills/user-experience/rules/mcp-health-runbook.md` is created before Wave 1 merge, documenting: (a) how to detect MCP degradation per sub-skill, (b) which fallback path activates for each Required MCP failure, (c) how to communicate degraded state to users." Also: add a MEDIUM-risk acknowledgment that the issue's wave-gating strategy means MCP failures in later waves could permanently stall wave progression.

**Acceptance Criteria:** A named owner is documented in SKILL.md. An MCP health runbook exists as a file artifact (not as prose in the issue body). The quarterly audit cadence is formalized in the worktracker as a recurring task, not as a promise in an issue.

---

### PM-003-20260303: 30-50 Day Scope Estimate Collapses Under Real-World Friction [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Estimated Scope |
| **Strategy Step** | Step 3 (Resource failures lens) |

**Failure Cause:** The scope estimate of 30-50 days for full V1 completion is based on a multiplier of the `/adversary` skill delivery (~5-7 days). However, the `/adversary` skill required zero MCP integration work, zero cross-sub-skill routing, and zero novel framework synthesis. The `/user-experience` skill introduces each of these at scale. The comparable delivery reference (R1 fix PM-001) improved the estimate's transparency but did not address the structural undercount in the estimate's derivation. In the retrospective: Wave 1 took 22 days (exceeding the "revise upward" trigger of 15 days from line 1101). Wave 2 began but the Miro MCP integration for Lean UX required 5 days of configuration work not captured in the estimate. Wave 3 was never started.

**Evidence:** Estimated Scope section (lines 1092-1101): "Wave 1 sub-skills (Heuristic Eval, JTBD): ~3-5 days per sub-skill." The comparable delivery reference notes the `/adversary` skill took "~5-7 days of effective effort across 2 project phases." The `/adversary` skill consists of 3 agents, 10 strategy templates, and rules -- no MCP integration, no novel framework creation, no cross-agent routing rules, no per-day sprint templates. The `/user-experience` skill includes: 11 SKILL.md files, 20 agent definition files, 20 governance YAML files, ~26 template files, 13 rules files, per-sub-skill quality benchmarks, MCP integration testing for 6 servers, and cross-sub-skill routing implementation. The 4-5x multiplier on artifact count is not the dominant cost driver -- MCP integration testing is, and it is underweighted.

**Analysis:** The 30-50 day range is the lower bound of a realistic estimate, not the midpoint. The estimate for subsequent waves (~2-4 days per sub-skill) does not account for MCP integration testing per server (listed at ~1-2 days per server, and there are 6 servers). Adding 6 servers × 1.5 days = 9 days of MCP work alone, not distributed across sub-skills. The "if Wave 1 exceeds 15 days, revise upward" signal is buried in the Estimated Scope prose and is the only recalibration mechanism. If the estimate is wrong for Wave 1, the issue body provides no guidance for what the revised estimate should be or how to decide whether to proceed.

**Recommendation:** Add an explicit risk acknowledgment: "Scope risk: The 30-50 day estimate assumes MCP integrations require ~1-2 days each and are additive. If any Required MCP integration (Figma, Miro, Storybook) requires more than 2 days of configuration and testing, the overall estimate should be treated as LOW confidence and a revised estimate produced after Wave 1 completion." Add a Phase Gate: "Before committing to Wave 2+, the Wave 1 delivery retrospective MUST produce an updated estimate based on actual per-artifact delivery rates. Wave 2+ does not begin until the revised estimate is accepted by the project owner."

**Acceptance Criteria:** The Wave 1 retrospective produces a written scope revision. The issue is not merged with the implication that 30-50 days is a firm commitment -- scope risk must be explicitly acknowledged in the issue's framing.

---

### PM-004-20260303: Wave Entry Criteria Are Unmeasurable in Practice [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions -- Wave Deployment |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The wave entry criteria use natural-language descriptions of prior achievements that teams must self-assess. Wave 2 requires: "Completed at least 1 heuristic evaluation report AND 1 JTBD job statement that was used in a product decision." Wave 3 requires: "Launched product with an analytics data source (for HEART) OR completed 1 Lean UX build-measure-learn hypothesis cycle." These criteria are not verifiable by the Jerry framework or the orchestrator -- they rely entirely on team self-declaration with no audit trail.

**Evidence:** Wave Deployment table (lines 590-596): entry criteria are stated in plain English without specifying how completion is recorded, where the completion evidence is stored, or how the orchestrator knows the criteria have been met. The Wave Progression ACs (lines 809-813) require criteria to be "documented and enforced" but the enforcement mechanism is not specified.

**Analysis:** "Enforced" means different things to different implementers. If enforcement means "the orchestrator displays a warning and asks the user to confirm," that is very different from "the orchestrator reads a worktracker entity to confirm." Without a specified enforcement mechanism, teams will either: (a) bypass the check by ignoring the warning, or (b) experience friction from ambiguous gating that the orchestrator cannot actually verify. In the retrospective: teams found the wave gating confusing and inconsistent. Some invoked Wave 2 sub-skills before meeting criteria; the orchestrator displayed a warning they dismissed. The gating was effectively decorative.

**Recommendation:** Specify the enforcement mechanism for wave entry criteria: "Wave entry criteria are enforced by the orchestrator reading a `wave-completion-log.md` file in the active Jerry project directory. The log is written by the sub-skill after a qualifying output is produced. The orchestrator checks for the log entry before routing to the next wave's sub-skills." Alternatively, if self-declaration is the intended model, state explicitly: "Wave entry criteria rely on team self-declaration. The orchestrator displays a confirmation dialog requiring explicit user acknowledgment (P-020). No automated enforcement is possible without a persistent completion log."

**Acceptance Criteria:** The Acceptance Criteria section specifies the wave enforcement mechanism (automated log check vs. explicit user declaration). The implementation of wave gating matches the specified mechanism.

---

### PM-005-20260303: Synthesis Hypothesis Confidence Gate Has No Enforcement Path [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions -- Synthesis Hypothesis Validation |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** The confidence gate architecture is described with precision (HIGH/MEDIUM/LOW tiers, structural omission of recommendation sections at LOW, mandatory validation source naming at MEDIUM), but the enforcement mechanism is text-based and bypassable. The `Human Override Justification` field introduced in R1 creates an auditable trail but does not prevent action on LOW-confidence outputs -- it just records that action was taken. The architecture acknowledges it "cannot fully prevent a determined user from treating LOW-confidence outputs as actionable" (line 641). In practice, every user treats LOW-confidence outputs as actionable within 2 weeks of adoption.

**Evidence:** Synthesis Hypothesis Validation section (lines 628-652) and the automation bias acknowledgment (line 641): "no template-level mechanism fully prevents a determined user from treating LOW-confidence outputs as actionable." The sub-skills with LOW-confidence outputs include Kano Model feature priority conflict interpretation, Behavior Design intervention recommendations, HEART metric threshold recommendations, and AI-First Design interaction patterns -- collectively covering at least 4 of the 10 sub-skills' most valuable outputs.

**Analysis:** If the most useful outputs (design recommendations) are LOW confidence and the LOW-confidence gate can be bypassed, the confidence gate system protects precisely the outputs users value least. The gate will be bypassed for the outputs that matter most. The auditable trail (Human Override Justification field) has no review process -- who reads the audit log? What happens when the log shows systematic override?

**Recommendation:** The confidence gate specification should include: (1) a monitoring AC in the Post-Launch Success Metrics that includes a human-readable review cadence for override logs ("The synthesis hypothesis override log is reviewed by the skill maintainer on a quarterly basis; if override rate exceeds 30% for any LOW-confidence output type, the confidence classification or the gate mechanism is revised"); (2) a recommendation that LOW-confidence outputs include a "what validation would upgrade this to MEDIUM" actionable next step, making validation the path of least resistance rather than override.

**Acceptance Criteria:** The Post-Launch Success Metrics AC for override rate monitoring includes a named reviewer and a response protocol for high override rates. LOW-confidence output templates include a "validation upgrade path" section.

---

### PM-006-20260303: AI-First Design Enabler Substitution is Underspecified [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | The Solution -- `/ux-ai-first-design`; Known Limitations -- AI-First Design: Conditional Status |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** The 90-day Enabler expiry mechanism substitutes Service Blueprinting (rank #12, score 7.40) as the Wave 5 replacement. However, Service Blueprinting is not specified anywhere in the issue body. It appears in the V2 Candidates table as a P1 gap. The substitution path activates automatically, but there is nothing to route to -- Service Blueprinting has no SKILL.md, no agent, no templates, no implementation. The auto-substitution produces a routing dead end.

**Evidence:** Conditional status section (lines 379-386): "If the Enabler fails or expires, Service Blueprinting (rank #12, score 7.40) auto-substitutes as an established, immediately adoptable framework." The V2 Roadmap section (lines 826-853) lists Service Blueprinting as a V2 P1 candidate with no implementation. The issue body contains no acceptance criteria for Service Blueprinting's implementation as a fallback.

**Analysis:** "Auto-substitutes as an established, immediately adoptable framework" is a claim without implementation. A routing rule that maps `ai-first-design` to `service-blueprinting` at expiry has no target. The 90-day expiry is a realistic timeline -- if the Enabler takes 90+ days (likely given it requires synthesizing a novel framework), the substitution fires immediately and delivers a broken route.

**Recommendation:** Add one of: (a) A Service Blueprinting stub implementation as a Wave 5 prerequisite -- before the AI-First Design Enabler is created, a minimal Service Blueprinting sub-skill (SKILL.md + basic agent) is delivered as the guaranteed fallback; OR (b) Change the substitution language to: "If the Enabler expires, Wave 5 reverts to Design Sprint only (already implemented). Service Blueprinting is a V2 addition tracked separately." The second option is simpler and more honest about V1 scope.

**Acceptance Criteria:** Either a Service Blueprinting stub implementation exists as an AC for Wave 5 delivery, OR the substitution language is corrected to reference only already-implemented Wave 5 sub-skills.

---

### PM-007-20260303: Cross-Sub-Skill Integration Lacks Functional Acceptance Criteria [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Parent Orchestrator |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The canonical cross-framework sequences (JTBD -> Design Sprint, Lean UX -> HEART) are referenced in the Relationship to Existing Jerry Skills section and in the orchestrator AC, but the acceptance criterion for integration ("Cross-framework integration handoffs tested for at least 2 canonical sequences") has no specification of what the test consists of, what a passing handoff looks like, or what artifact demonstrates the handoff worked.

**Evidence:** Acceptance Criteria -- Parent Orchestrator (line 754): "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)." This AC has no test specification. The Relationship to Existing Jerry Skills section (lines 942-949) describes integration at the concept level. No test artifact or handoff schema is specified anywhere in the issue body.

**Analysis:** Integration testing without a test specification is unverifiable. "Tested" could mean: manually invoked once and did not crash, OR systematically validated that JTBD output format is parseable by the Design Sprint input format. These are very different quality levels. Without a test specification, implementation teams will satisfy the AC in the weakest way possible -- one manual invocation with no assertion.

**Recommendation:** Specify the minimum integration test: "Integration handoff test for JTBD -> Design Sprint: A JTBD job statement output (in canonical format from `job-statement-template.md`) is passed to the `ux-sprint-facilitator` as the challenge statement input. The sprint facilitator produces a Day 1 challenge statement that references the job statement's functional, emotional, and social dimensions. This is verified by manual review against the sprint rules in `design-sprint-rules.md`." Apply the same specification pattern to the Lean UX -> HEART canonical sequence.

**Acceptance Criteria:** Each named canonical sequence has a written test specification as a file artifact (or inline AC table). The integration test is reviewable by a third party who did not implement the sub-skills.

---

### PM-008-20260303: Per-Sub-Skill Quality Benchmarks Require Unavailable UX Expertise [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Wave 1 Sub-Skills |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** The JTBD quality benchmark (line 772) requires "a UX practitioner rates as actionable (structured rubric: grammatically correct job format, contains functional + emotional + social dimensions, distinguishes job from solution)." The target audience of this skill is tiny teams without UX specialists. The quality benchmark for a sub-skill designed for non-specialists requires a specialist to evaluate. This contradiction means the AC is either unverifiable by the implementation team or requires outsourcing the verification to a resource the implementation team may not have.

**Evidence:** Wave 1 ACs (lines 764-773): Heuristic Eval benchmark requires "agent correctly identifies >= 7 of 10 known heuristic violations in a reference test design (calibration artifact provided with sub-skill)" -- this is verifiable. JTBD benchmark requires "a UX practitioner rates as actionable" -- this requires external expertise.

**Analysis:** The heuristic eval benchmark is well-specified (calibration artifact, objective threshold). The JTBD benchmark introduces a subjective human expert gate. If the implementation team does not include a UX practitioner, this AC cannot be satisfied. If a UX practitioner is consulted, the AC is satisfied with a sample size of one evaluator. The rubric criteria in the AC (grammatical format, three dimensions, solution distinction) are clear -- the question is who applies them.

**Recommendation:** Replace "a UX practitioner rates as actionable" with an AI-verifiable rubric: "The output is evaluated by running the job statement through a structured rubric checklist: (1) contains a verb that is a functional job (not a solution), (2) contains at least one emotional or social dimension phrase, (3) does not name a specific product or technology. All three criteria must pass." This makes the benchmark verifiable by the implementation team without specialist expertise -- consistent with the skill's stated audience.

**Acceptance Criteria:** All per-sub-skill quality benchmarks are verifiable without external UX practitioner consultation. Benchmarks that currently require expert judgment are respecified with deterministic rubric criteria.

---

## Recommendations

### P0 -- Critical: MUST Mitigate Before Acceptance

**PM-001-20260303: Define the issue closure condition**
- Mitigation: Add a "Issue Closure Condition" statement at the top of the Acceptance Criteria section. State explicitly that Wave 1 (Parent Orchestrator + Wave 1 sub-skills + Synthesis Validation + MCP Quality + Quality Standards) closes this issue. Wave 2-5 are tracked in child issues created at Wave 1 merge. Mark all Wave 2-5 ACs with "tracked in child issue."
- Acceptance criteria: The issue body contains a single, unambiguous closure condition. A reader can determine in < 30 seconds which ACs close this issue.

**PM-002-20260303: Formalize MCP maintenance as a deliverable, not a commitment**
- Mitigation: Add two ACs to MCP Integration Quality: (1) "A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md`." (2) "A `skills/user-experience/rules/mcp-health-runbook.md` file exists at Wave 1 merge, containing: degradation detection procedure, fallback activation steps, user communication script." Change "quarterly audit cadence" from prose commitment to worktracker recurring task requirement.
- Acceptance criteria: The runbook file exists as a verifiable artifact. The maintenance owner is a named person or role in SKILL.md.

**PM-003-20260303: Acknowledge scope risk explicitly and add a Phase Gate**
- Mitigation: Add a "Scope Risk" callout to the Estimated Scope section: "The 30-50 day range is LOW-confidence for MCP integration work. If Wave 1 completion exceeds 15 days, the per-sub-skill estimate for Waves 2-5 must be revised before committing to subsequent waves." Add a Phase Gate AC: "A Wave 1 retrospective document (`work/retros/wave-1-retro.md`) is produced within 5 days of Wave 1 completion, containing: actual vs. estimated per-artifact delivery rates, revised estimate for Waves 2-5, go/no-go recommendation from the project owner."
- Acceptance criteria: The Phase Gate AC exists in the issue body. The Wave 1 retrospective is a named deliverable in the worktracker.

### P1 -- Important: SHOULD Mitigate

**PM-004-20260303: Specify the wave enforcement mechanism**
- Mitigation: Replace "Wave entry criteria documented and enforced" with either: (a) an AC specifying a `wave-completion-log.md` file written by sub-skills after qualifying outputs, or (b) explicit acknowledgment that enforcement is via user declaration with a confirmation dialog. The implementation must match whichever model is chosen.
- Acceptance criteria: The enforcement mechanism is explicit and the implementation team can implement it without ambiguity.

**PM-005-20260303: Add override log review cadence and validation upgrade path**
- Mitigation: Add to Post-Launch Success Metrics: "[ ] Override log review cadence: The synthesis hypothesis override log is reviewed quarterly by a named maintainer. If override rate for any LOW-confidence output type exceeds 30%, the confidence classification or gate mechanism is revised within one sprint." Add to LOW-confidence output templates: a "Validation Upgrade Path" section showing what data would upgrade the output to MEDIUM confidence.
- Acceptance criteria: The Post-Launch Metrics AC includes a named reviewer and a response protocol. LOW-confidence templates include a Validation Upgrade Path section.

**PM-006-20260303: Correct the Service Blueprinting substitution claim**
- Mitigation: Option A -- add a Service Blueprinting stub implementation as a Wave 5 prerequisite AC. Option B (recommended) -- revise the substitution language to: "If the Enabler expires, Wave 5 delivers Design Sprint only. Service Blueprinting is tracked as a V2 P1 addition."
- Acceptance criteria: The substitution path references only implemented sub-skills. No routing dead ends exist in the auto-substitution logic.

**PM-007-20260303: Specify integration test artifacts for canonical sequences**
- Mitigation: Add a test specification table to the cross-framework integration AC. For each named sequence (JTBD -> Design Sprint, Lean UX -> HEART), specify: input format, expected output property, and how the handoff is verified. Reference the templates used.
- Acceptance criteria: The integration test specification is readable by a third party who did not implement the sub-skills. Each named sequence has a minimum of 3 verifiable output properties.

**PM-008-20260303: Replace specialist-dependent benchmarks with deterministic rubrics**
- Mitigation: Replace the JTBD benchmark's "UX practitioner rates as actionable" criterion with a deterministic 3-point rubric (functional verb, emotional/social dimension, no product/technology name). Apply the same treatment to any Wave 2-5 benchmark that requires expert judgment.
- Acceptance criteria: All per-sub-skill quality benchmarks can be verified by the implementation team without external UX expertise.

### P2 -- Monitor

**PM-009-20260303:** The user research warning's one-per-session display is insufficient for teams building consumer products. Consider adding a per-output watermark ("This output is a hypothesis, not validated research. See the Known Limitations for context.") to all synthesis outputs. No AC change required -- monitor adoption patterns.

**PM-010-20260303:** V2 trigger conditions are well-defined but have no owner or delivery commitment. When V2 planning begins, assign a named owner to each P1 gap and create a worktracker entity. No AC change required for this issue.

**PM-011-20260303:** The Design Sprint "1-2 day solo collapse" claim should be validated with a reference or marked as a design assumption. In V2, test the solo sprint adaptation with a real 1-2 person team and document the outcome.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-001: No closure condition; PM-006: Substitution path references unimplemented sub-skill; PM-010: V2 trigger conditions unowned. Three gaps in what the document claims to specify. |
| Internal Consistency | 0.20 | Negative | PM-002: "Quarterly audit with named owner" is committed to in prose but has no AC -- creates an internal inconsistency between the risk acknowledgment and the acceptance criteria. PM-006: "Auto-substitutes as an established, immediately adoptable framework" contradicts Service Blueprinting's V2 status. |
| Methodological Rigor | 0.20 | Negative | PM-004: Wave enforcement is specified in prose but the enforcement mechanism is undefined. PM-005: Confidence gate architecture is methodologically sound but the monitoring feedback loop is incomplete. PM-007: Integration test specification is absent for a key AC. |
| Evidence Quality | 0.15 | Negative | PM-003: Scope estimate derivation underweights MCP integration complexity; the analogical basis (adversary skill) is not comparable. PM-008: JTBD quality benchmark requires external expertise inconsistent with the skill's target audience. PM-011: Design Sprint solo adaptation is an unvalidated claim. |
| Actionability | 0.15 | Negative | PM-004: Wave entry criteria enforcement is stated without the mechanism to implement it. PM-007: Cross-sub-skill integration AC is stated without a test specification. PM-008: JTBD benchmark cannot be acted on by the implementation team without specialist consultation. |
| Traceability | 0.10 | Positive | The issue body traces all major decisions to prior research artifacts (Architecture Vision, Framework Selection Analysis, UX Frameworks Survey). The References section is complete. R1 revision added comment annotations that trace specific fixes to their source strategy findings (e.g., `[R1-fix: PM-001]`). Traceability is the strongest dimension in this deliverable. |

**Pre-Mortem Assessment:** REVISE. The deliverable demonstrates strong architectural thinking and has been meaningfully improved by R1. The failure modes identified are not fundamental flaws in the skill design -- they are specification gaps that will predictably cause implementation drift, adoption failure, or operational brittleness. Three P0 Critical findings and five P1 Major findings require mitigation before the issue is ready for acceptance. Post-mitigation, this deliverable should clear the 0.92 quality threshold.

---

## Execution Statistics

- **Total Findings:** 11
- **Critical:** 3
- **Major:** 5
- **Minor:** 3
- **Protocol Steps Completed:** 6 of 6
- **Failure Category Coverage:** Technical (1), Process (3), Assumption (3), External (1), Resource (2) -- all 5 lenses applied
- **Findings with P0 Priority:** 3 (PM-001, PM-002, PM-003)
- **Findings with P1 Priority:** 5 (PM-004 through PM-008)
- **Findings with P2 Priority:** 3 (PM-009, PM-010, PM-011)

---

*Strategy Execution Report -- S-004 Pre-Mortem Analysis*
*Template Version: 1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Executed: 2026-03-03*
*Agent: adv-executor*
