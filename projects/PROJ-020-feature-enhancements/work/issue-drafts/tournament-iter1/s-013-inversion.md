# Strategy Execution Report: Inversion Technique (S-013)

## Execution Context

- **Strategy:** S-013 (Inversion Technique)
- **Template:** `.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Deliverable Type:** GitHub Enhancement Issue -- `/user-experience` skill proposal (~1020 lines)
- **Criticality:** C4
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 1 of 8 | Target: >= 0.95
- **H-16 Compliance:** C4 tournament sequence; S-003 Steelman confirmed as prior strategy in tournament chain

---

## Inversion Report: `/user-experience` Skill -- GitHub Enhancement Issue

**Strategy:** S-013 Inversion Technique
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-013)
**H-16 Compliance:** S-003 Steelman applied in prior tournament iteration (confirmed)
**Goals Analyzed:** 11 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 9

---

## Summary

Inversion analysis of the `/user-experience` skill proposal reveals one Critical assumption vulnerability (the AI assistance quality assumption underlying every sub-skill), four Major vulnerabilities (MCP ecosystem stability, non-specialist execution capability, wave adoption self-selection, and the synthesis hypothesis validation assumption), and four Minor vulnerabilities. The most dangerous anti-goal condition is that the deliverable guarantees failure of its core promise -- "two people doing what used to take eight" -- if AI assistance quality is insufficient for non-specialists executing structured UX frameworks without real training. The deliverable is rich in structural sophistication but under-specified on how it validates that AI guidance quality is sufficient before users make consequential design decisions on AI-generated outputs. Recommendation: **REVISE** -- address Critical and Major findings before implementation proceeds.

---

## Step 1: Goals Inventory

| # | Goal | Type | Stated / Inferred |
|---|------|------|-------------------|
| G-01 | Enable tiny teams (1-5 people) to execute professional UX methodology without a UX specialist | Primary | Stated |
| G-02 | Cover the full UX lifecycle via 10 sub-skills implementing proven frameworks | Scope | Stated |
| G-03 | Comply with Jerry framework architectural constraints (P-003, H-34, CB-02, progressive disclosure) | Compliance | Stated |
| G-04 | Deploy in 5 criteria-gated waves to reduce adoption risk and progressive complexity | Risk Management | Stated |
| G-05 | Provide synthesis hypothesis validation gates to prevent over-reliance on AI outputs | Safety | Stated |
| G-06 | Achieve S-014 scoring >= 0.92 at wave transitions for C2+ UX deliverables | Quality | Stated |
| G-07 | Each sub-skill is independently maintainable and evolvable without modifying sibling skills | Maintainability | Implicit |
| G-08 | The MCP integration remains stable enough to provide the documented functionality | Infrastructure | Implicit |
| G-09 | Non-specialist developers successfully execute UX frameworks using AI guidance alone | Adoptability | Implicit (core value prop) |
| G-10 | Jerry users adopt `/user-experience` as their primary UX methodology tool | Adoption | Implicit |
| G-11 | The issue specification is complete enough to implement without major clarifying questions | Implementability | Implicit |

---

## Step 2: Anti-Goals (Goal Inversions)

For each goal, "What would guarantee we FAIL to achieve this goal?"

**G-01 Anti-Goal:** To guarantee tiny teams cannot execute UX methodology without a specialist:
- AI guidance quality is too low for non-specialists to follow without expert interpretation
- Sub-skill outputs require UX knowledge to interpret (circular dependency)
- Error mode is invisible: teams believe they applied the framework correctly but did not
- The most dangerous anti-goal: confident incorrect execution is worse than no execution

**G-04 Anti-Goal:** To guarantee wave adoption fails:
- Wave entry criteria are too ambiguous to self-assess without external validation
- Teams cannot determine which wave they are in without a specialist to diagnose it
- Wave stall bypass conditions incentivize skipping rather than meeting criteria

**G-05 Anti-Goal:** To guarantee over-reliance on AI synthesis outputs:
- The confidence gate protocol is documented but not technically enforced in the agent templates
- LOW-confidence outputs that "structurally omit design recommendations" rely on the agent following a rule -- not on any deterministic mechanism
- Users can invoke sub-skills with custom prompts that bypass the confidence gate framing
- The HIGH-confidence gate requires users to "acknowledge AI judgment calls" -- but the specific judgment calls are determined by the AI at runtime, creating a validation loop the AI controls

**G-08 Anti-Goal:** To guarantee MCP integration becomes non-functional:
- Figma changes MCP schema or restricts access (explicitly flagged as "history" of doing so)
- Hotjar bridge requires paid Zapier configuration that many tiny teams will skip
- Community-maintained Whimsical MCP becomes unmaintained
- MCP server dependency creates 6-point single-thread failure path affecting 10 sub-skills

**G-09 Anti-Goal:** To guarantee non-specialists fail when executing UX frameworks:
- AI generates plausible-sounding but incorrect heuristic severity ratings
- Users accept MEDIUM-confidence job statements as validated research for product decisions
- The "Synthesis Judgments Summary" for HIGH-confidence outputs is too long to review meaningfully
- Non-specialists cannot distinguish a well-executed heuristic evaluation from a superficially plausible one

**G-11 Anti-Goal:** To guarantee the issue specification causes implementation confusion:
- Agent cognitive modes are specified but agent methodology sections are not (they will be authored during implementation with no template)
- The conditional `/ux-ai-first-design` blocking prerequisite (WSM score >= 7.80) has no mechanism to track or enforce the block at implementation time
- 67 artifacts across 11 skill directories with no implementation ordering specified beyond "waves"

---

## Step 3: Assumption Map

| ID | Assumption | Type | Category | Confidence | Validation Status |
|----|------------|------|----------|------------|-------------------|
| A-01 | AI assistance quality is sufficient for non-specialists to execute UX frameworks correctly | Core | Technical | Low | Untested -- no validation mechanism described |
| A-02 | MCP servers (Figma, Miro, Storybook) remain available and functionally stable across the implementation timeline | Infrastructure | Environmental | Medium | Partially addressed (fallback paths documented) |
| A-03 | The 3-tier synthesis hypothesis confidence gate is sufficient to prevent consequential over-reliance on unvalidated AI outputs | Safety | Process | Medium | Asserted but not empirically validated |
| A-04 | Wave entry criteria can be self-assessed by tiny teams without external validation | Adoption | Process | Low | Not validated -- criteria require UX judgment to assess |
| A-05 | The conditional `/ux-ai-first-design` blocking prerequisite mechanism will be implemented and enforced during development | Implementation | Process | Medium | Not specified beyond "Enabler must reach DONE" |
| A-06 | Non-specialist users will read and act on synthesis hypothesis warnings rather than treating AI outputs as authoritative | Behavioral | Process | Low | No user behavior validation; counter-evidence exists in LLM over-trust literature |
| A-07 | Each sub-skill can be versioned and updated independently without breaking cross-sub-skill workflows | Technical | Technical | Medium | Asserted but no interface contract specified |
| A-08 | The parent orchestrator routing logic correctly diagnoses user intent from natural language stage descriptions | Technical | Technical | Medium | No routing accuracy target stated or validation described |
| A-09 | Tiny teams will self-qualify for the appropriate wave rather than jumping to the highest-value sub-skills directly | Behavioral | Process | Low | Counter-incentive: JTBD and Design Sprint have the most visible value proposition |
| A-10 | The GitHub issue specification provides sufficient detail for implementation without major clarifying questions | Implementability | Process | Medium | Not reviewed by an implementer prior to tournament |
| A-11 | The WSM scoring methodology used for framework selection is valid for predicting real-world tiny team outcomes | Research | Technical | Medium | Partially validated (adversarial tournament but not user outcome data) |
| A-12 | Non-MCP fallback paths provide meaningfully equivalent UX framework execution, not just partial coverage | Infrastructure | Technical | Medium | Stated but fallback quality not specified |
| A-13 | 30-50 day total effort estimate is realistic for the implementation scope | Resource | Temporal | Low | No basis provided; 67 artifacts across 11 directories is substantial |
| A-14 | The parent orchestrator's triage routing can handle the full diversity of real user UX requests with the 8-category intent map | Technical | Technical | Medium | 8 categories for a complex domain; edge cases not covered |

---

## Step 4: Stress-Test Results

| ID | Assumption | Inversion | Plausibility | Severity | Affected Dimension |
|----|------------|-----------|--------------|----------|--------------------|
| IN-001-20260303 | A-01: AI quality sufficient for non-specialist execution | AI generates plausible-sounding heuristic ratings that are systematically biased toward severity under-rating or over-rating based on training data artifacts | HIGH -- documented LLM calibration failures in structured evaluation tasks | Critical | Methodological Rigor |
| IN-002-20260303 | A-06: Users will act on confidence warnings | Users treat AI synthesis outputs as validated research despite LOW/MEDIUM confidence labels (documented automation bias phenomenon) | HIGH -- extensive HCI literature on automation bias and alert fatigue | Critical | Evidence Quality |
| IN-003-20260303 | A-03: Confidence gate prevents over-reliance | User invokes sub-skill with "ignore confidence warnings" prompt or custom system message; confidence gate is a framing convention, not a deterministic enforcement mechanism | MEDIUM -- requires adversarial or careless user behavior | Major | Methodological Rigor |
| IN-004-20260303 | A-02: MCP stability | Figma restricts MCP access or changes schema (documented precedent: Dev Mode became paid 2023); 4 required + 2 enhancement sub-skills affected simultaneously | HIGH -- explicitly documented in deliverable as a known risk | Major | Completeness |
| IN-005-20260303 | A-04: Wave criteria are self-assessable | Team in Wave 2 reads "launched product with analytics" as entry criterion but interprets "product" as prototype and "analytics" as page views from Google Analytics free tier; proceeds to Wave 3 incorrectly | HIGH -- criteria use domain terms that require UX expertise to interpret correctly | Major | Actionability |
| IN-006-20260303 | A-09: Teams will follow wave progression | Teams directly invoke `/ux-design-sprint` (Wave 5, score 8.65 -- highest-value visible brand) before completing Wave 1-4, encountering the sprint without JTBD groundwork or Lean UX hypothesis framework | HIGH -- Design Sprint is the most recognizable brand in the portfolio; users are incentivized to skip | Major | Completeness |
| IN-007-20260303 | A-10: Specification sufficient for implementation | Implementation team cannot determine the agent methodology section content for any of the 10 sub-skill agents from the issue body; issue specifies agent names, cognitive modes, tool tiers, but not the actual methodology each agent follows | MEDIUM -- issue is a GitHub proposal, not a technical spec, but the gap between issue and implementable spec is large | Minor | Actionability |
| IN-008-20260303 | A-13: 30-50 day effort estimate is realistic | Implementation of 67 artifacts with MCP integration testing, adversarial validation for each sub-skill at wave launch, and S-014 scoring at wave transitions is underestimated by 2-3x | MEDIUM -- comparable Jerry skill implementations (adversary: 3 agents + 10 templates) took longer than analogous estimates | Minor | Traceability |
| IN-009-20260303 | A-12: Non-MCP fallbacks are equivalent | "Screenshot-input mode" for `/ux-heuristic-eval` removes Figma's component-level analysis, annotation extraction, and design token access; the AI evaluates screenshots the same way any human would but without structured data access -- this is not a "fallback" it is a fundamentally different capability tier | HIGH -- screenshot analysis is qualitatively different from programmatic design file access | Minor | Completeness |

---

## Step 5: Detailed Findings

### IN-001-20260303: AI Guidance Quality Is Unvalidated for Non-Specialist Use [CRITICAL]

**Type:** Assumption
**Original Assumption:** AI assistance quality is sufficient for non-specialists to execute UX frameworks correctly and produce outputs of professional quality (A-01).
**Inversion:** The AI generates plausible-sounding heuristic severity ratings, job statements, and B=MAP diagnoses that are calibrated to training data rather than the specific product and user population being evaluated. A non-specialist has no mechanism to detect this error because they lack the domain expertise required to validate the AI's UX judgment.
**Plausibility:** HIGH. Documented in LLM calibration literature for structured evaluation tasks. Nielsen's 10 Heuristics severity ratings require contextual expertise to assign correctly. The AI produces a rating; the user lacks the baseline to verify it. This creates a confident-but-wrong execution failure that is harder to detect than no execution at all.
**Consequence:** The deliverable's core value proposition -- "two people doing what used to take eight" -- rests entirely on this assumption. If AI UX framework guidance quality is insufficient for non-specialists, the skill produces the illusion of UX practice without its substance. Teams make product decisions based on systematically biased AI outputs, with worse outcomes than no UX analysis. This is the foundational assumption of the entire proposal and it has no validation mechanism.
**Evidence:** The deliverable describes AI actions at the capability level ("evaluates designs against all 10 Nielsen heuristics; assigns severity ratings") but provides no quality benchmark or validation mechanism. The synthesis hypothesis confidence gates address the question of *whether* AI outputs are validated against real users, but not the prior question of *whether the AI correctly applies the framework methodology at all*.
**Dimension:** Methodological Rigor
**Mitigation:** Add a "Framework Execution Quality" acceptance criterion: each sub-skill MUST document a benchmark evaluation against a known-good sample (e.g., `/ux-heuristic-eval` evaluated against a published heuristic evaluation study with known findings; the AI's findings compared for recall and precision). This does not require user outcome data -- it requires that the AI's framework application be validated against expert-authored ground truth before production launch.
**Acceptance Criteria:** (1) Each sub-skill has a documented benchmark test with a ground-truth artifact. (2) The benchmark establishes a minimum recall threshold (e.g., AI identifies >= 80% of severity-3+ findings from expert evaluation). (3) The benchmark result is included in the sub-skill's SKILL.md.

---

### IN-002-20260303: Automation Bias Will Defeat Confidence Gate User Behavior Assumption [CRITICAL]

**Type:** Assumption
**Original Assumption:** Non-specialist users will read and act on synthesis hypothesis warnings rather than treating AI outputs as authoritative (A-06).
**Inversion:** Users exhibit automation bias -- the well-documented tendency to over-trust automated systems, especially when the output is presented authoritatively and the user lacks the domain expertise to challenge it. A tiny team receiving a "MEDIUM confidence" job statement labeled with a warning proceeds to treat it as validated research because: (a) the warning appears as fine print relative to the richly formatted job statement, (b) the user cannot identify *which specific aspects* of the AI output to distrust, and (c) the organizational pressure to ship overrides epistemic caution.
**Plausibility:** HIGH. This is not a hypothetical -- automation bias in AI-assisted decision-making is the central finding of a decade of HCI research. The deliverable's architecture acknowledges the research gap limitation but treats the confidence gate as a behavioral solution to a structural problem.
**Consequence:** The synthesis hypothesis validation protocol, which the deliverable presents as a key differentiator, is undermined at the behavioral level. The architectural enforcement (LOW-confidence outputs structurally omit design recommendation sections) addresses the most severe case but leaves MEDIUM and HIGH cases to user discipline. MEDIUM-confidence outputs "require named validation source" -- but the deliverable does not specify what happens when a user provides a named source that does not actually validate the assumption.
**Evidence:** "MEDIUM confidence outputs require named validation source before advancing to design decisions" (Synthesis Hypothesis Validation section). The mechanism for what "named validation source" means, how it is verified, and what happens when it is a cursory reference is unspecified. The confidence gate is behavioral, not technical, for MEDIUM and HIGH tiers.
**Dimension:** Evidence Quality
**Mitigation:** (1) Restructure the HIGH-confidence gate from "user acknowledges AI judgment calls" to "user provides explicit counter-evidence or challenge for at least one AI judgment call" -- shifting from passive acknowledgment to active engagement. (2) Define "named validation source" with specificity: at minimum, it must be (a) a named individual who interacted with real users, (b) a survey with >= N respondents, or (c) a published secondary source with a citation. (3) For MEDIUM-confidence outputs, the agent should generate specific challenge questions directed at the AI's own reasoning, presenting them as "What would falsify this output?" rather than "Here are the caveats."
**Acceptance Criteria:** (1) HIGH-confidence gate requires user to answer at minimum one AI-generated challenge question about the output before proceeding. (2) MEDIUM-confidence "named validation source" has a structured definition with minimum specificity requirements. (3) Behavioral design of confidence gate UX is documented in `synthesis-validation.md` with reference to automation bias literature.

---

### IN-003-20260303: Confidence Gate Is Framing Convention, Not Enforcement Mechanism [MAJOR]

**Type:** Assumption / Anti-Goal
**Original Assumption:** The 3-tier synthesis hypothesis confidence gate is sufficient to prevent consequential over-reliance on unvalidated AI outputs (A-03).
**Inversion:** A user invokes a sub-skill with a custom prompt that asks the AI to "skip the confidence warnings and give me the design recommendations directly." Since the confidence gate is implemented as an instruction to the agent (not as a deterministic code gate), an adversarial or careless invocation bypasses it. Additionally, the LOW-confidence design recommendation omission is described as "the agent template physically does not contain a design recommendation section" -- but agent templates are markdown files that developers can modify.
**Plausibility:** MEDIUM. Requires either adversarial prompting or developer modification of template files. However, the confidence gate architecture relies on LLM compliance with instructions, which is a known weak enforcement mechanism for safety-critical behavior.
**Consequence:** The architectural guarantee "LOW-confidence outputs structurally omit design recommendations" is softer than stated. The deliverable presents this as an enforceable constraint, which influences how implementers and users perceive the safety guarantee.
**Evidence:** "The agent template physically does not contain a design recommendation section. This cannot be overridden by any user action" (Synthesis Hypothesis Validation section). This claim is architecturally inaccurate -- users can override LLM behavior via system prompt modification, and developers can modify template files. The "cannot be overridden" language overstates the enforcement guarantee.
**Dimension:** Methodological Rigor
**Mitigation:** (1) Replace "cannot be overridden by any user action" with an accurate description of the enforcement mechanism and its limits. (2) Add a note that LOW-confidence enforcement is LLM-instruction-based, not deterministic. (3) For the most consequential LOW-confidence case (AI-First Design), add a human-in-the-loop gate (explicit sign-off from a named human reviewer) rather than relying solely on agent instruction compliance.
**Acceptance Criteria:** (1) Confidence gate enforcement description accurately reflects the mechanism. (2) `synthesis-validation.md` documents enforcement limitations and the conditions under which the gate can be circumvented. (3) The acceptance criteria for sub-skill launch include validation that the confidence gate behaves as specified under adversarial prompting.

---

### IN-004-20260303: MCP Ecosystem Brittleness Undermines Core Promise for Target Audience [MAJOR]

**Type:** Assumption
**Original Assumption:** MCP servers (Figma, Miro, Storybook) remain available and functionally stable across the implementation timeline (A-02).
**Inversion:** Figma restricts MCP access (documented precedent: Dev Mode API became paid in 2023). Four sub-skills require Figma; two enhance with it. A Figma schema change simultaneously degrades 6 of 10 sub-skills. The target audience -- tiny teams at the "Free" ($0/month) and "Minimal" ($46/month) tiers -- is precisely the audience least likely to have stable MCP configurations or the technical capacity to maintain custom bridges.
**Plausibility:** HIGH. The deliverable explicitly documents this risk: "Figma has a history of restricting previously free API access." The risk is acknowledged but the mitigation relies on quarterly audits and a named maintenance owner -- both of which are ongoing operational commitments the issue does not establish accountability for.
**Consequence:** The "Free tier (4 sub-skills)" cost model assumes HEART, JTBD, Kano, and Behavior Design require no MCP. But Miro is listed as an "Enhancement MCP" for JTBD, Kano, and Behavior Design -- meaning a tiny team at the Free tier gets degraded versions of 3 of their 4 available sub-skills. The cost tier table creates a false precision about what "free" delivers.
**Evidence:** "Free ($0/month): HEART, JTBD, Kano, Behavior Design (4 sub-skills)" (MCP Integration section). But JTBD has "Enhancement MCP: Miro (visual job mapping)"; Kano has "Enhancement MCP: Miro (feature mapping visualization)"; Behavior Design has "Enhancement MCP: Miro (behavior mapping), Hotjar (behavioral recording data via bridge)." The Free tier delivers 4 sub-skills without their enhancement MCPs, which is true but materially different from the full sub-skill experience.
**Dimension:** Completeness
**Mitigation:** (1) Rename "Free" tier to "Core (No MCP)" and explicitly document which capabilities are absent. (2) Add a "Free tier capability delta" table showing what is lost without enhancement MCPs for each sub-skill. (3) The MCP maintenance owner should be identified as a role (not a person placeholder) in the issue, with a link to the quarterly audit cadence mechanism.
**Acceptance Criteria:** (1) Cost tier table accurately represents the capability available at each tier, including enhancement MCP gaps. (2) Each sub-skill's non-MCP fallback path documents the capability delta explicitly (not just "fallback documented" but "fallback delivers X% of core functionality"). (3) MCP maintenance owner role is established as a named responsibility in project governance.

---

### IN-005-20260303: Wave Entry Criteria Require the Expertise They Are Designed to Replace [MAJOR]

**Type:** Assumption
**Original Assumption:** Wave entry criteria can be self-assessed by tiny teams without external validation (A-04).
**Inversion:** Wave 2 entry criterion: "Wave 1: at least 1 heuristic eval + 1 JTBD job statement used." "Used" is undefined. Did "used" mean incorporated into a product decision? Filed in a document? Reviewed by the team? A team that generates a heuristic evaluation but ignores the findings has technically "used" the sub-skill. Wave 3 criterion: "launched product with analytics OR 1 Lean UX hypothesis cycle." "Launched product" and "hypothesis cycle" both require UX expertise to define correctly.
**Plausibility:** HIGH. Wave criteria ambiguity is a systemic design issue. Criteria-gated wave progression is valuable only if the criteria are unambiguous. The current criteria use terminology that non-specialists interpret differently from UX practitioners.
**Consequence:** Teams advance waves incorrectly, building on a foundation that does not exist. A team that advances to Wave 3 (design system) without genuine Wave 1-2 competency attempts Atomic Design and Inclusive Design without the user insight and hypothesis foundation those frameworks build on.
**Evidence:** Wave 5 entry criterion: "Wave 4: 30+ users for Kano OR 1 B=MAP bottleneck diagnosed." "30+ users for Kano" requires running a Kano survey -- which itself requires UX expertise to design and field. The wave entry criterion for Wave 5 is essentially "successfully completed Wave 4," making the criteria circular rather than independently verifiable.
**Dimension:** Actionability
**Mitigation:** (1) Rewrite wave entry criteria as binary, self-verifiable checklists with no ambiguous terms: "Wave 2: `/ux-heuristic-eval` produced a findings report with >= 3 findings documented in a file in the project repository AND `/ux-jtbd` produced a job statement document in the project repository." Completion artifacts, not expertise judgments. (2) Add a "Wave Self-Assessment Checklist" document that teams complete and commit before advancing, making wave progression traceable via worktracker. (3) Eliminate the "stall bypass" condition or specify it as a specific exception requiring explicit governance sign-off, not a self-service option.
**Acceptance Criteria:** (1) Each wave's entry criteria are expressed as artifact-verifiable binary conditions. (2) A `wave-progression-checklist.md` template exists in the skill directory. (3) Wave stall bypass requires documented exception rather than self-service team decision.

---

### IN-006-20260303: Design Sprint Brand Recognition Incentivizes Wave-Skipping [MAJOR]

**Type:** Anti-Goal
**Original Assumption:** Tiny teams will follow the wave progression rather than jumping directly to the highest-perceived-value sub-skills (A-09).
**Inversion:** Design Sprint 2.0 is the most recognizable framework in the portfolio (Google Ventures brand). JTBD was popularized by the "Jobs to be Done" book and Clay Christensen. These two sub-skills -- ranked #2 (8.65) and #6 (8.05) respectively -- are in Waves 5 and 1. A team reading the issue body will see "Design Sprint" and think "that's exactly what we need" and invoke `/ux-design-sprint` directly, bypassing Waves 1-4 entirely. The wave progression is documented but not enforced.
**Plausibility:** HIGH. The deliverable explicitly allows direct sub-skill invocation: "Users who know the specific sub-skill they need can invoke it directly (e.g., `/ux-heuristic-eval`) to bypass the triage." This is correct behavior for expert users but creates a wave-bypass path for non-experts who misidentify their need.
**Consequence:** The wave progression -- which is the risk-management mechanism for the entire architecture -- is effectively optional. A team that invokes `/ux-design-sprint` without JTBD groundwork runs a sprint without a validated challenge statement, producing a prototype for a problem that has not been validated as the right problem to solve. The 4-day investment is wasted.
**Evidence:** "Users who know the specific sub-skill they need can invoke it directly... to bypass the triage" (Key Design Decision #2). This creates a self-service bypass for the wave progression. No guardrail is mentioned that would warn a user invoking Wave 5 skills without Wave 1-4 completion.
**Dimension:** Completeness
**Mitigation:** (1) The parent orchestrator should check wave progression completion status when routing to Wave 3+ sub-skills and issue a prominent warning (not a block) when wave prerequisites are incomplete. (2) Each sub-skill's SKILL.md should document prerequisite wave skills and display them at invocation time. (3) The "bypass triage" path should be renamed "Expert override" with a confirmation prompt: "You are invoking a Wave N sub-skill directly. Wave N builds on [prior waves]. Are you familiar with [framework dependencies]? (Y to proceed / N to return to orchestrator)."
**Acceptance Criteria:** (1) Parent orchestrator checks wave prerequisites before routing to Wave 3+ sub-skills and issues a documented warning on first invocation of out-of-sequence skills. (2) Each Wave 3-5 sub-skill SKILL.md documents wave prerequisites. (3) Direct invocation of Wave 3-5 sub-skills triggers a confirmation step when wave progression data is not available.

---

### IN-007-20260303: Implementation Specification Gap Between Issue and Buildable Spec [MINOR]

**Type:** Assumption
**Original Assumption:** The GitHub issue specification provides sufficient detail for implementation without major clarifying questions (A-10).
**Inversion:** An implementation team reads the issue and cannot determine: (1) the specific methodology each agent follows (the issue specifies "Systematic cognitive mode, T3 tool tier" but not the step-by-step evaluation protocol), (2) the agent template structure (no template examples for any sub-skill), (3) the agent-to-agent handoff protocol for cross-sub-skill workflows, or (4) how the parent orchestrator maintains wave progression state across sessions.
**Plausibility:** MEDIUM. GitHub issues are proposals, not technical specs. However, this issue presents itself as a complete feature specification (it includes a 67-artifact directory structure, acceptance criteria, and a 5-wave deployment plan), raising the expectation that implementation can begin from the issue alone.
**Evidence:** The directory structure shows `heuristic-evaluation-rules.md`, `jtbd-methodology-rules.md`, etc. -- but the content of these rules files is not specified in the issue. An implementer cannot author these files without either the original research artifacts (referenced but not linked inline) or domain expertise in each framework.
**Dimension:** Actionability
**Mitigation:** Add a "Implementation Entry Points" section listing the documents an implementer should read before authoring each wave's sub-skills, with explicit references to the research artifacts that contain the methodology detail.
**Acceptance Criteria:** An implementer can identify the source of methodology content for each sub-skill's rules files from the issue body.

---

### IN-008-20260303: Effort Estimate May Be Materially Underestimated [MINOR]

**Type:** Assumption
**Original Assumption:** 30-50 day total effort estimate is realistic for the full V1 implementation scope (A-13).
**Inversion:** 67 artifacts across 11 skill directories, with MCP integration testing for 6 MCP servers, adversarial validation at each wave launch, S-014 scoring for C2+ outputs at wave transitions, and the conditional AI-First Design Enabler requirement. The `/adversary` skill -- 3 agents + 10 strategy templates -- is a reference comparable and represents substantial implementation effort. `/user-experience` has 10 sub-skill agents + governance YAMLs + rules files + templates per sub-skill.
**Plausibility:** MEDIUM. Effort estimates for complex skill portfolios are typically underestimated by 2-3x in frameworks without prior comparable implementations.
**Evidence:** "Total estimated effort for full V1 (10 sub-skills): ~30-50 days, phased across waves" (Estimated Scope section). No basis for this estimate is provided. The comparable `/adversary` skill implementation had a substantial research phase before implementation.
**Dimension:** Traceability
**Mitigation:** Add a basis of estimate reference: either a comparable skill implementation or a breakdown by artifact type (N agents * N hours/agent, etc.).
**Acceptance Criteria:** Effort estimate is traceable to a breakdown by artifact type or comparable implementation.

---

### IN-009-20260303: Non-MCP Fallbacks Deliver Qualitatively Different Capability [MINOR]

**Type:** Assumption
**Original Assumption:** Non-MCP fallback paths provide meaningfully equivalent UX framework execution (A-12).
**Inversion:** "Screenshot-input mode" for `/ux-heuristic-eval` is described as providing "full heuristic coverage retained" but removes: programmatic component identification, design token extraction, annotation reading, frame-level navigation, and the structured design file metadata that enables systematic evaluation. A screenshot-based heuristic evaluation is what any UX practitioner does manually -- it is not an AI-augmented evaluation with structured data access.
**Plausibility:** HIGH. The capability delta between programmatic Figma access and screenshot input is well-understood in design tooling contexts.
**Evidence:** "Non-MCP fallback: Screenshot-input mode. User provides design screenshots as image inputs. Reduced automation but full heuristic coverage retained." (Sub-skill #1 description). "Reduced automation but full heuristic coverage retained" conflates automation level with framework coverage. The heuristics can still be evaluated, but the quality of evaluation is qualitatively lower.
**Dimension:** Completeness
**Mitigation:** Each fallback path description should include a "Capability Delta" statement: what specific analytical capabilities are absent in the fallback and what the user should expect to do manually to compensate.
**Acceptance Criteria:** Each non-MCP fallback path documents the specific capabilities absent and the manual compensation required.

---

## Findings Summary

| ID | Assumption / Anti-Goal | Type | Confidence | Severity | Evidence | Affected Dimension |
|----|------------------------|------|------------|----------|----------|--------------------|
| IN-001-20260303 | A-01: AI quality sufficient for non-specialist execution | Assumption | Low | **Critical** | No benchmark validation mechanism for any sub-skill | Methodological Rigor |
| IN-002-20260303 | A-06: Users will act on confidence warnings | Assumption | Low | **Critical** | Automation bias not addressed; "named validation source" undefined | Evidence Quality |
| IN-003-20260303 | A-03: Confidence gate prevents over-reliance | Assumption | Medium | **Major** | "Cannot be overridden" claim overstates LLM enforcement | Methodological Rigor |
| IN-004-20260303 | A-02: MCP stability across implementation timeline | Assumption | Medium | **Major** | Figma restriction precedent documented; cost tier table misleads on Free capability | Completeness |
| IN-005-20260303 | A-04: Wave criteria are self-assessable | Assumption | Low | **Major** | Criteria use UX terminology requiring expertise to interpret | Actionability |
| IN-006-20260303 | A-09: Teams will follow wave progression | Anti-Goal | N/A | **Major** | Direct invocation bypass path has no wave prerequisite check | Completeness |
| IN-007-20260303 | A-10: Specification sufficient for implementation | Assumption | Medium | **Minor** | Methodology content for rules files not sourced in issue | Actionability |
| IN-008-20260303 | A-13: 30-50 day estimate is realistic | Assumption | Low | **Minor** | No basis of estimate provided | Traceability |
| IN-009-20260303 | A-12: Non-MCP fallbacks are equivalent | Assumption | Medium | **Minor** | "Full coverage retained" overstates fallback quality | Completeness |

---

## Step 6: Recommendations

### Critical -- MUST Address Before Implementation Proceeds

**IN-001-20260303:** Add a framework execution quality benchmark requirement to each sub-skill's acceptance criteria. Before launching any sub-skill, validate AI framework application against an expert-authored ground-truth sample. Document recall/precision against the benchmark in the sub-skill's SKILL.md.

**IN-002-20260303:** Redesign the HIGH and MEDIUM confidence gates from passive acknowledgment to active engagement. Require users to answer AI-generated challenge questions about the output (not just acknowledge caveats). Define "named validation source" with minimum specificity requirements. Reference automation bias literature in `synthesis-validation.md`.

### Major -- SHOULD Address Before Wave 1 Launch

**IN-003-20260303:** Remove "cannot be overridden by any user action" language. Accurately document that confidence gate enforcement is LLM-instruction-based with known bypass paths. Add adversarial prompting test cases to sub-skill acceptance criteria.

**IN-004-20260303:** Rename "Free" tier to "Core (No MCP)" and add a capability delta table for each sub-skill at the no-MCP tier. Establish MCP maintenance owner as a named role with documented accountability.

**IN-005-20260303:** Rewrite wave entry criteria as artifact-verifiable binary conditions (file exists in repo, not expertise judgment). Create `wave-progression-checklist.md` template. Require documented exception for wave stall bypass.

**IN-006-20260303:** Add wave prerequisite check to parent orchestrator routing for Wave 3+ sub-skills. Add confirmation prompt for direct Wave 3-5 sub-skill invocation. Document this in `ux-routing-rules.md`.

### Minor -- MAY Address at Implementation Discretion

**IN-007-20260303:** Add "Implementation Entry Points" section with references to research artifacts for each sub-skill's methodology content.

**IN-008-20260303:** Add basis of estimate breakdown by artifact type or comparable skill reference.

**IN-009-20260303:** Each non-MCP fallback path should include an explicit capability delta statement.

---

## Scoring Impact

| Dimension | Weight | Impact | IN-NNN References | Rationale |
|-----------|--------|--------|-------------------|-----------|
| Completeness | 0.20 | Negative | IN-004-20260303, IN-006-20260303, IN-009-20260303 | Free tier capability understated (IN-004); wave bypass path leaves architecture incomplete (IN-006); fallback capability delta unstated (IN-009) |
| Internal Consistency | 0.20 | Neutral | IN-003-20260303 | "Cannot be overridden" claim is internally inconsistent with LLM-based enforcement architecture, but the overall document is logically coherent |
| Methodological Rigor | 0.20 | Negative | IN-001-20260303, IN-003-20260303 | No benchmark validation for AI framework execution quality (IN-001, the most severe gap); confidence gate enforcement overstated (IN-003) |
| Evidence Quality | 0.15 | Negative | IN-002-20260303 | Automation bias phenomenon directly undermines the confidence gate behavioral assumption with high-evidence counter-evidence from HCI literature (IN-002) |
| Actionability | 0.15 | Negative | IN-005-20260303, IN-007-20260303 | Wave criteria not self-assessable by non-specialists (IN-005); methodology content for rules files not sourced (IN-007) |
| Traceability | 0.10 | Negative | IN-008-20260303 | Effort estimate not traceable to basis (IN-008); wave criteria not traceable to completion artifacts |

**Overall Assessment:** 2 Critical, 4 Major, 3 Minor findings. Five of six scoring dimensions show negative impact from inversion findings. The most vulnerable assumption cluster is the "behavioral compliance" cluster (IN-001, IN-002, IN-003, IN-006): the deliverable's safety and adoption architecture assumes users behave in epistemically careful ways that the automation bias and wave-skipping evidence contradicts.

**Recommendation: REVISE** -- The deliverable is architecturally sophisticated and well-researched. The Critical findings do not invalidate the approach; they identify that the confidence gate and AI quality validation mechanisms need to be redesigned from behavioral compliance to structural enforcement. Addressing IN-001 and IN-002 will require meaningful additions to the acceptance criteria and `synthesis-validation.md` specification. Addressing IN-005 and IN-006 requires a rework of wave entry criteria and parent orchestrator routing logic.

---

## Execution Statistics

- **Total Findings:** 9
- **Critical:** 2
- **Major:** 4
- **Minor:** 3
- **Protocol Steps Completed:** 6 of 6
- **Goals Analyzed:** 11 (7 explicit, 4 implicit)
- **Assumptions Mapped:** 14 (across 5 categories: Technical, Environmental, Process, Behavioral, Temporal)
- **Most Vulnerable Cluster:** Behavioral compliance (IN-001, IN-002, IN-003, IN-006) -- architecture assumes user epistemic caution that automation bias evidence contradicts
