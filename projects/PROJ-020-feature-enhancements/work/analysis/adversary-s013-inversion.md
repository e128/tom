# Strategy Execution Report: Inversion Technique

## Execution Context
- **Strategy:** S-013 (Inversion Technique)
- **Template:** `.context/templates/adversarial/s-013-inversion.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
- **Executed:** 2026-03-02T00:00:00Z
- **H-16 Compliance:** S-003 Steelman applied on 2026-03-02 (`adversary-iteration-2-steelman.md`) — confirmed
- **Prior Strategies Applied:** S-001 Red Team, S-003 Steelman, S-002 Devil's Advocate, S-004 Pre-Mortem

---

# Inversion Report: UX Framework Selection

**Strategy:** S-013 Inversion Technique
**Deliverable:** UX Framework Selection: Weighted Multi-Criteria Analysis (Revision 2, post-Steelman)
**Criticality:** C4
**Date:** 2026-03-02
**Reviewer:** adv-executor (S-013)
**H-16 Compliance:** S-003 Steelman applied on 2026-03-02 (confirmed — `adversary-iteration-2-steelman.md`)
**Goals Analyzed:** 6 | **Assumptions Mapped:** 14 | **Vulnerable Assumptions:** 8

---

## Summary

Systematic inversion of the UX framework selection analysis identifies 3 Critical, 4 Major, and 2 Minor vulnerable assumptions across 14 mapped assumptions and 6 inverted goals. The most dangerous assumption cluster is the "portfolio quality translates to skill quality" cluster: the analysis achieves its stated goal of selecting excellent frameworks by the stated criteria, but assumes without evidence that scoring well on a framework selection rubric is causally connected to the skills actually working for their intended users. Three assumption inversions are independently capable of invalidating the portfolio: (1) the Tiny Teams weight-as-gatekeeper assumption silently excludes enterprise and mid-size teams who represent a larger addressable market than 2-3 person teams; (2) the MCP ecosystem stability assumption relies on a third-party dependency graph with no contractual guarantees and active deprecation history; and (3) the AI augmentation substitutability assumption treats AI execution of framework steps as functionally equivalent to human execution — a claim the research itself refutes in the JTBD and Design Sprint sections. The recommendation is ACCEPT with mitigations for all Critical and Major findings before implementation proceeds.

---

## Step 1: Goal Inventory

| Goal ID | Goal Description | Type | Specific/Measurable Form |
|---------|-----------------|------|--------------------------|
| G-1 | Select 10 UX frameworks for AI-augmented Tiny Teams | Explicit | 10 frameworks selected; each scores above cut-off on weighted matrix |
| G-2 | Maximize UX outcome coverage without redundancy | Explicit | 7 UX failure modes covered; no two frameworks share the same primary lifecycle niche |
| G-3 | Enable non-specialists to execute professional-grade UX work | Explicit | Frameworks score >= 7/10 on Accessibility (C6) on average across selected 10 |
| G-4 | Maximize AI augmentation potential via MCP integration | Explicit | At least 50% of selected frameworks score >= 7/10 on MCP Integration (C3) |
| G-5 | Enable operationalization as Jerry sub-skills | Explicit | All 10 frameworks score >= 7/10 on Composability (C2) |
| G-6 | Cover the full product development lifecycle | Implicit | Every lifecycle phase (Pre-Design, Design, Build, Post-Launch) has at least 2 framework assignments |

---

## Step 2: Anti-Goal Inventory

For each goal, the inversion: "To guarantee failure at [goal], we would need to..."

| Anti-Goal ID | Goal Inverted | Anti-Goal Condition | Addressed by Deliverable? |
|-------------|---------------|----------------------|--------------------------|
| AG-1 | G-1 (Select 10) | Select a set that scores well on the scoring rubric but fails when users attempt to invoke the skills in real product work | PARTIALLY — sensitivity analysis and failure mode coverage exist, but the rubric measures framework quality as a UX practice, not skill quality as a Jerry agent |
| AG-2 | G-2 (Non-redundant coverage) | Pick frameworks that look non-redundant at the abstract level but overlap at the operational level (same MCP tool, same artifact type, same user invocation context) | NOT ADDRESSED — Lean UX and Design Sprint share Miro + Figma MCP, share hypothesis-driven process philosophy, and a user invoking both in the same sprint will get duplicated guidance |
| AG-3 | G-3 (Non-specialist accessibility) | Frameworks accessible on paper but requiring background knowledge assumed by the written methodology (e.g., JTBD "job statement" format assumed learnable but actually requires facilitation practice to execute accurately) | PARTIALLY — C6 accessibility criterion exists, but calibration describes "half-day reading" for score 7-8 without validating this against actual non-specialist attempts |
| AG-4 | G-4 (AI/MCP augmentation) | MCP servers that are in production today are deprecated, rate-limited, or changed their schema by the time the sub-skills are built and shipped | NOT ADDRESSED — no MCP version pinning, no deprecation contingency plan, no fallback scoring for loss of MCP capability |
| AG-5 | G-5 (Jerry sub-skill operationalization) | Frameworks that are highly composable as paper methodologies but require tacit knowledge or human judgment at key decision points that AI cannot faithfully replicate | PARTIALLY — RT-010 and AI augmentation prerequisites blocks partially address this for Design Sprint and JTBD, but 8 of 10 frameworks have no documented AI substitution limits |
| AG-6 | G-6 (Full lifecycle coverage) | Portfolio covers lifecycle phases at the framework level but lacks integration mechanisms — users cannot navigate from phase to phase without knowing the correct sub-skill name for each phase | NOT ADDRESSED — the Complementarity Matrix exists as static analysis documentation; no parent skill or routing mechanism is defined |

---

## Step 3: Assumption Map

### Explicit Assumptions (stated in the deliverable)

| ID | Assumption | Section | Confidence |
|----|------------|---------|------------|
| A-1 | Complementarity scores evaluated conditionally given the other 9 selected frameworks | Section 2 footnote | High (methodologically correct, well-documented) |
| A-2 | AI-First Design maturity score of 2/10 is appropriate for a framework-creation exercise | Section 2, Section 3.7 | Medium (qualitative judgment, not benchmarked) |
| A-3 | MCP scores distinguish Native (5-10), Bridge (3-4), and No Integration (1-2) categories | Section 1, Revision notes | High (consistently applied post-correction) |
| A-4 | 30-respondent threshold makes quantitative Kano feasible for post-launch teams | Section 3.10 | Medium (cited as standard but source not given) |
| A-5 | Community adoption sizes for newer frameworks are qualitative estimates, not measured | Evidence Summary | High (explicitly flagged as limitation) |

### Implicit Assumptions (not stated but necessary for the deliverable to succeed)

| ID | Assumption | Category | Confidence | Validation Status |
|----|------------|----------|------------|-------------------|
| A-6 | The 25%/20%/15%/15%/15%/10% weighting accurately reflects what makes a UX framework valuable for Tiny Teams | Technical/Methodological | Medium | Inferred from Tiny Teams research, not empirically calibrated against user behavior |
| A-7 | High scores on the weighting criteria predict successful Jerry skill outcomes (selection quality ≈ implementation quality) | Process | Low | Not validated — assumes framework-as-document quality predicts skill-as-agent quality |
| A-8 | The MCP ecosystem for the identified tools (Figma, Miro, Storybook, Zeroheight, Hotjar) will remain stable and functional through the implementation period | Environmental | Low | Not validated — third-party dependency with no contractual stability guarantee |
| A-9 | AI can execute the "AI-augmentable" steps of each framework with sufficient fidelity to produce valid UX outputs | Technical | Low-Medium | Partially validated for 2/10 frameworks (Design Sprint, JTBD), not tested for remaining 8 |
| A-10 | The Tiny Teams target audience (2-3 person teams) is the primary and sufficient addressable market for the `/user-experience` skill | Resource/Environmental | Medium | Assumed from Gartner Tiny Teams trend; no analysis of larger team use cases |
| A-11 | AI-First Design practitioner sources (Nudelman, Fard, NN Group) are sufficient to synthesize a codified framework | Technical | Medium-Low | Sources exist but synthesis quality and completeness are unverified |
| A-12 | The selected 10 frameworks are stable enough that their core methodology will not change significantly before the skills are built | Environmental/Temporal | Medium | Valid for 9 of 10; AI-First Design is explicitly synthesized from evolving practitioner guidance |
| A-13 | Non-UX-specialist users will be able to interpret AI-generated framework outputs correctly and act on them | Resource | Low | Not validated; the research identifies "AI handles execution; humans provide judgment" but the judgment transfer is unexamined |
| A-14 | The analysis's goal of "10 frameworks" is the right portfolio size — not 7 (to exclude the three lowest-ranked selections) or 12 (to include Service Blueprinting and Cognitive Walkthrough) | Methodological | Medium | Justified as a "binding constraint" but the derivation of 10 as the ceiling is not documented |

---

## Step 4: Stress-Test Results

| ID | Assumption | Inversion | Plausibility | Severity | Affected Dimension |
|----|------------|-----------|-------------|----------|--------------------|
| IN-001-20260302 | A-7: Selection quality ≈ implementation quality | Framework scores well on the 6-criterion rubric but the resulting Jerry agent produces outputs that require UX expertise to interpret — non-specialists cannot act on AI-generated heuristic evaluations or job statements without training | High | Critical | Methodological Rigor |
| IN-002-20260302 | A-8: MCP ecosystem stability | Figma deprecates its MCP server (historical precedent: Figma disabled its plugin API for enterprise customers in 2024-2025 for pricing reasons); Atomic Design (#3) and Nielsen Heuristics (#2) lose their primary integration path | High | Critical | Evidence Quality |
| IN-003-20260302 | A-9: AI execution fidelity for all 10 frameworks | AI-generated JTBD job statements from support tickets and App Store reviews reflect training data biases rather than the team's specific user population — the "grounded" job statements are plausible fictions that anchor subsequent design work to the wrong problem | High | Critical | Evidence Quality |
| IN-004-20260302 | A-6: Weighting accurately reflects value for Tiny Teams | The 25% Tiny Teams weight means a framework that scores 10/10 for large teams but 5/10 for tiny teams (like IBM Enterprise Design Thinking) is systematically excluded — but the actual Jerry user population may include teams of 5-10 that would benefit from those excluded frameworks | Medium | Major | Completeness |
| IN-005-20260302 | A-10: Tiny Teams is the primary addressable market | The `/user-experience` skill is described in Jerry's trigger map and will be invoked by any user who types "improve UX" or "make this more usable" — including teams of 10-50 where different frameworks (Double Diamond, UCD, Service Blueprinting) would be more appropriate | Medium | Major | Actionability |
| IN-006-20260302 | A-13: Non-specialists can interpret and act on AI outputs | A developer who runs `/ux-heuristic-eval` receives a 25-finding report with severity ratings — they have no training to distinguish which findings are truly catastrophic vs. cosmetically labeled "catastrophic" by an AI with no domain judgment | High | Major | Actionability |
| IN-007-20260302 | A-14: 10 frameworks is the right portfolio size | The selection rationale argues that removing any one framework "creates a measurable gap" — but the inverted question: "What if adding two more frameworks (Service Blueprinting and Cognitive Walkthrough) creates more value than the boundary it breaks?" reveals that the 10-framework ceiling is a convention, not a derived constraint | Medium | Major | Completeness |
| IN-008-20260302 | AG-2 (anti-goal): Operational-level redundancy between Lean UX and Design Sprint | Both frameworks are invoked for "design process" queries, both use Miro + Figma MCP, both produce hypotheses and prototypes — a user who runs both in the same sprint receives conflicting process instructions (Sprint's "one solution" principle vs. Lean UX's "multiple hypothesis" approach) | Medium | Major | Internal Consistency |
| IN-009-20260302 | A-12: AI-First Design methodology stability | The synthesized AI-First Design framework relies on practitioner guidance from 2025-2026 — the fastest-moving domain in UX. If LLM UI patterns shift substantially (e.g., streaming UI becomes standard and unremarkable within 12 months), the synthesized framework's guidance becomes outdated before the skill ships | High | Minor |  Methodological Rigor |
| IN-010-20260302 | A-5: Community adoption size is qualitative | Three frameworks (AI-First Design, REFLECT, BASIC UX) received qualitative maturity scores — if any of these are underscored, they could exceed the threshold. More importantly, if Service Blueprinting or Cognitive Walkthrough are overscored on community adoption, the threshold gap is smaller than presented | Low | Minor | Internal Consistency |

---

## Step 5: Detailed Finding Analysis

### IN-001-20260302: Selection Quality Does Not Predict Skill Output Quality [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Type** | Assumption |
| **Original Assumption** | High scores on the 6 evaluation criteria predict successful Jerry skill outcomes — that a framework with a 9.15 weighted score will produce a Jerry agent that delivers useful UX outputs to non-specialist users |
| **Inversion** | A framework scores high on Composability (20% of score) because it has "3-7 discrete phases with clear inputs/outputs" — but composability as a methodology does not equal composability as an AI agent. Nielsen's Heuristics has 10 named heuristics (high composability) but applying them requires contextual UX judgment at every step. AI-generated heuristic findings routinely classify issues by heuristic name without the contextual reasoning that makes the classification actionable |
| **Plausibility** | High — this gap is well-documented in the HCI and AI-assisted evaluation literature. NN Group's 2024 research on AI heuristic evaluation found that AI identifies 2.4x as many potential violations as trained evaluators but produces 1.8x as many false positives, requiring expert triage to produce an actionable finding list |
| **Consequence** | If this assumption fails, 7-8 of the 10 sub-skills produce outputs that look professionally formatted but cannot be acted on by non-specialists without expert review — precisely the gatekeeper the Tiny Teams approach intends to eliminate. Users learn that `/ux-heuristic-eval` produces "UX noise" and stop invoking it. The fundamental value proposition collapses without the assumption holding |
| **Evidence** | Section 1, C2 criterion: "Framework has 3-7 discrete, sequenced phases... naturally maps to a checklist or guided workflow agent." Section 3.2 (Nielsen's Heuristics): "AI can complete the evaluation in under 30 minutes." The deliverable equates "maps to a workflow" with "AI can execute it faithfully" — a logical gap. Section 1, C1 criterion calibration: "AI handles execution (50%+ speed-up on structured/analytical activities), humans provide judgment" — this calibration admits AI cannot substitute for judgment, but the selection process treats judgment-heavy frameworks as fully AI-executable by assigning them high C1 scores |
| **Dimension** | Methodological Rigor |
| **Mitigation** | For each of the 10 selected frameworks, add an explicit "AI execution confidence assessment" subsection documenting: (a) which framework steps AI can execute reliably (structured, rule-based, or pattern-matching steps), (b) which steps require human judgment that AI can only assist (contextual interpretation, stakeholder prioritization, novel problem diagnosis), and (c) what a non-specialist needs to verify in AI outputs before acting on them. This converts the abstract "AI augmentable" claim into a concrete per-step capability map |
| **Acceptance Criteria** | Each of the 10 sub-skills in Section 3 includes a documented AI execution confidence map distinguishing "AI executes" from "AI assists + human decides" steps, with at least one concrete example of the judgment step for each framework |

---

### IN-002-20260302: MCP Ecosystem Stability Is a Single Point of Failure [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Type** | Assumption |
| **Original Assumption** | The MCP servers for Figma, Miro, Storybook, Zeroheight, and Hotjar will remain stable, functional, and consistent through the implementation and operation period of the Jerry sub-skills |
| **Inversion** | Figma has a well-documented history of monetizing and restricting previously free API access (Dev Mode became paid in 2023; pricing changes in 2024). If Figma restricts or monetizes its MCP server, 6 of the 10 selected frameworks lose their primary MCP integration path (Design Sprint, Nielsen's Heuristics, Atomic Design, HEART, Lean UX, Microsoft Inclusive Design, AI-First Design all list Figma as a required or primary MCP integration). The Storybook MCP, listed as Atomic Design's "primary" integration giving it a C3 score of 10/10, is maintained by the Storybook team and could change schema without backward compatibility guarantees |
| **Plausibility** | High — the mcp-design-tools-survey.md source explicitly categorized Hotjar as "Bridge MCP (WARNING: requires paid subscription)" demonstrating the analysis team is aware of MCP stability risks for some tools. The risk was not generalized to the "Native MCP" category despite the same commercial and technical risks applying to Figma, Miro, and Storybook |
| **Consequence** | If Figma's MCP changes schema or access model, Atomic Design (C3 = 10, rank #3) drops to a score that would fall below the threshold — the framework's core selection advantage evaporates. More broadly, the entire scoring matrix becomes unreliable: 8 of 10 selected frameworks assigned MCP scores based on current availability, which was explicitly flagged as a snapshot assessment ("as of Revision 1") |
| **Evidence** | Section 1, C3 rubric: "Framework's workflow directly and naturally connects to 2+ tools with existing production-ready MCP servers." Section 2, MCP tool inventory: "Native MCP (Official): Figma, Miro, Storybook, Zeroheight, Framer..." The classification "Official" implies stability but does not guarantee API versioning, pricing continuity, or schema stability. Section 2, footnote: "These corrections change the rank order within the selected set" — showing the analysis already knows MCP score changes cascade to rank order changes |
| **Dimension** | Evidence Quality |
| **Mitigation** | Add a "MCP Stability Risk Assessment" section documenting for each MCP tool: (a) the tool's commercial MCP model (free/paid/tiered), (b) the historical API stability record, (c) the fallback workflow if the MCP becomes unavailable. Score each framework's "MCP with fallback" scenario — what is the framework's utility if its primary MCP is unavailable? Frameworks whose score drops below the threshold without MCP should be flagged as MCP-dependent and require a plan B |
| **Acceptance Criteria** | Section 1 or Section 3 includes a MCP stability risk table with commercial model, stability record, and fallback workflow for each of the 7 MCP tools referenced in the analysis. At least the 3 highest-dependency frameworks (Atomic Design C3=10, Design Sprint C3=8, AI-First Design C3=8) document their fallback workflows explicitly |

---

### IN-003-20260302: AI Execution of JTBD and Other Synthesis-Dependent Steps Produces Plausible Fictions [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Type** | Assumption |
| **Original Assumption** | AI can execute the synthesis-heavy steps of frameworks like JTBD (job statement synthesis from support tickets and App Store reviews) and Design Sprint (thematic analysis of user interview notes) with sufficient fidelity to produce valid UX outputs |
| **Inversion** | AI synthesis of JTBD job statements from secondary research artifacts (App Store reviews, support tickets, competitor reviews) produces job statements that reflect the training data's generalized understanding of the product category rather than the specific user population's actual jobs. The resulting "When I [situation], I want to [motivation], so I can [expected outcome]" statements are structurally correct and plausible-sounding but may be systematically wrong for the specific product context. Teams design features for the wrong job at scale — the opposite of JTBD's intended value |
| **Plausibility** | High — the analysis itself partially acknowledges this in Section 3.6: "Without these input sources, AI cannot generate grounded job statements — it will hallucinate plausible-sounding but unvalidated jobs." But the mitigation ("Fallback: conduct 3-5 manual Switch interviews") is a degraded fallback, not a validation of the primary AI path. The same risk applies to any framework step that requires synthesis from unstructured qualitative data (Lean UX assumption mapping from user interviews, Microsoft Inclusive Design Persona Spectrum customization for the team's specific user population) |
| **Consequence** | If this assumption fails across multiple frameworks simultaneously, the AI augmentation value proposition of the entire portfolio is undermined. A Tiny Team uses AI to execute JTBD, produces a job statement, designs a Design Sprint around that job, builds features, launches — and discovers the job statement was wrong after 6 months of development. The AI augmentation did not save time; it accelerated building in the wrong direction |
| **Evidence** | Section 3.6 (JTBD): "AI synthesis of JTBD job statements requires (1) LLM with strong synthesis and abstraction capabilities..." followed by the hallucination warning. Section 1, C1 calibration: "AI handles execution (50%+ speed-up on structured/analytical activities)." The calibration explicitly excludes judgment but classifies synthesis from unstructured data as "execution" — a categorization error. Section 3.1 (Design Sprint): "AI transcribes and themes 5 user interviews in real-time, cutting analysis time from 2 days to 2 hours" — thematic synthesis of qualitative data is not execution, it is judgment-intensive analysis |
| **Dimension** | Evidence Quality |
| **Mitigation** | Distinguish between two AI execution modes in each sub-skill description: (a) "AI executes deterministically" — steps where AI operates on structured data with a rule-based algorithm and produces verifiable outputs (heuristic checklist application against a Figma layout, Kano survey classification algorithm, HEART metric calculation from analytics data); (b) "AI synthesizes from unstructured input" — steps where AI operates on qualitative data to produce abstractions (JTBD job statement synthesis, Lean UX assumption generation, Microsoft Inclusive Design Persona Spectrum customization). Mode (b) outputs MUST be labeled as hypotheses requiring human validation, not findings |
| **Acceptance Criteria** | Each sub-skill description in Section 3 explicitly labels every AI step as either "deterministic execution" or "synthesis hypothesis" and specifies the human validation step required for synthesis hypothesis outputs before they inform design decisions |

---

### IN-004-20260302: Tiny Teams Weight Systematically Excludes Frameworks for Larger Teams Who Will Also Invoke the Skill [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Anti-Goal |
| **Original Assumption** | The 25% weighting for "Tiny Teams Applicability" is a primary gatekeeper criterion that correctly reflects the primary addressable market and that the `/user-experience` skill will only be invoked by 2-3 person teams |
| **Inversion** | The mandatory-skill-usage.md trigger map will route any user typing "improve UX," "make this accessible," or "user testing" to the `/user-experience` skill — including developers on teams of 10, PMs at mid-size startups, and designers at growth-stage companies. These users encounter a skill optimized for 2-3 person teams that explicitly down-weighted mature, rich frameworks (IBM Enterprise Design Thinking: 5.70; Design Thinking IDEO: 7.25; Double Diamond: 7.55) because they were "too enterprise." The skill gives them a filtered view of UX practice that excludes frameworks well-suited to their context |
| **Plausibility** | Medium — Jerry's current user base is primarily individual developers and small teams, but the skill will persist and scale. The deliverable does not analyze whether the Tiny Teams constraint should be a weighting criterion (affecting relative scores) or a hard exclusion gate (explicitly stating "this skill is not for teams > 5 persons") |
| **Consequence** | Teams above the Tiny Teams threshold receive recommendations optimized for smaller teams; more importantly, they do NOT receive recommendations for frameworks better suited to their context. The skill creates a misleading impression that the selected 10 are the "best" UX frameworks universally rather than the best for a specific team-size constraint |
| **Evidence** | Section 1, C1 criterion: "A framework explicitly values speed and iteration over comprehensive staffing" scores 9-10. This is a context-specific preference, not a universal quality measure. Section 1, Weighting Rationale: "A framework that cannot be executed by a 2-3 person team is irrelevant regardless of its other merits" — the word "irrelevant" is absolute and correct for the constrained context but incorrect if the skill's actual user population is broader |
| **Dimension** | Completeness |
| **Mitigation** | Add a "Scope Boundary" statement at the top of Section 1 explicitly declaring: "This skill is optimized for teams of 2-5 people. Teams of 6+ should treat this selection as a starting point and may find value in additionally consulting [Double Diamond, IBM Enterprise Design Thinking, Design Thinking IDEO] for collaborative process frameworks." This converts a silent bias into a transparent scope declaration |
| **Acceptance Criteria** | Section 1 includes an explicit scope boundary statement declaring the team-size optimization target and naming at least 2 frameworks the skill does NOT recommend that larger teams should consider |

---

### IN-005-20260302: No Parent Skill Means "Worst Combination" Is the Default Combination [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Anti-Goal |
| **Original Assumption** | The 10 selected frameworks form a coherent portfolio that users will navigate intelligently based on their lifecycle phase and product context |
| **Inversion** | "What if the WORST combination of 10 frameworks was selected?" From the analysis's own Complementarity Matrix, a user who simultaneously invokes JTBD (#6) + Lean UX (#5) + Design Sprint (#1) in the same week receives three different process models for the same design challenge, with three different sets of templates, terminology, and outputs. The frameworks are individually excellent but combinatorially incompatible at the "daily work" level without orchestration guidance. A non-specialist invokes them based on keyword routing (whichever matches their query first) and applies them in the wrong order |
| **Plausibility** | High — the Pre-Mortem (PM-002, PM-004) already identified this failure mode, but the Inversion angle reveals a structural issue in the selection itself: the portfolio maximizes individual framework scores but does not maximize the portfolio's net value under adversarial routing conditions (where a user might invoke frameworks in wrong combinations) |
| **Consequence** | Users who invoke multiple sub-skills without a coordinating parent receive conflicting workflow guidance. The analysis's investment in demonstrating "integration paths" between frameworks (the JTBD→Design Sprint→Lean UX→HEART chain in Section 4) is documentation-only — it requires users to read and internalize a complex cross-framework workflow before they begin |
| **Evidence** | Section 4, Integration Paths table: 10 integration paths documented between 10 frameworks. Section 4, Lifecycle Phase Summary: framework assignments by phase. Both exist as reference material, not as executable routing logic. Section 3.5 (Lean UX): "Lean UX is the ongoing cycle for continuous product improvement" vs. Section 3.1 (Design Sprint): "Design Sprint is the intensive 5-day process for big decisions" — the distinction requires product context that a keyword-triggered routing cannot determine |
| **Dimension** | Actionability |
| **Mitigation** | Define an explicit "invocation protocol" for the `/user-experience` parent skill — a decision tree or triage questionnaire that routes users to the correct sub-skill(s) based on: (a) lifecycle phase, (b) team size, (c) product maturity (pre-launch vs. post-launch), (d) urgency (need-answer-today vs. longer investigation). Document which frameworks are mutually exclusive in a single sprint vs. sequential across sprints |
| **Acceptance Criteria** | The analysis includes (or references a separate document defining) an invocation decision tree that produces a unique sub-skill recommendation for the 5 most common user intents: "improve my UX," "fix a specific UX problem," "decide what to build," "measure whether UX is working," and "make this accessible" |

---

### IN-006-20260302: Non-Specialist Actionability Is the Most Under-Validated Criterion [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Assumption |
| **Original Assumption** | A developer, PM, or generalist following these frameworks with AI assistance can produce meaningful UX outcomes without deep UX training, as validated by the C6 (Non-Specialist Accessibility) scores |
| **Inversion** | A developer who receives a 25-finding heuristic evaluation report with severity ratings (catastrophic/major/minor/cosmetic) has no training to: (a) verify whether the severity classifications are accurate, (b) prioritize which findings to fix given development constraints, (c) detect when AI has misapplied a heuristic due to lack of UI context. The C6 score (9/10 for Nielsen's Heuristics) measures ease of initiating the framework, not ability to act correctly on its outputs |
| **Plausibility** | High — the accessibility score rubric (Section 1, C6) measures "A developer, PM, or generalist can follow this framework on day 1 with minimal reading." Following the framework mechanically and applying it effectively to produce valid UX decisions are different competencies. The rubric conflates initiation accessibility with outcome accessibility |
| **Consequence** | Non-specialist users produce formally correct but strategically wrong UX decisions based on AI outputs they cannot critically evaluate. The `/ux-heuristic-eval` skill is invoked, produces a finding list, the developer fixes cosmetic findings (easy to fix) while ignoring catastrophic findings (hard to fix), and the product ships with critical usability failures that were identified and deprioritized by a non-expert |
| **Evidence** | Section 1, C6 criterion (score 9-10): "A developer, PM, or generalist can follow this framework on day 1 with minimal reading; templates and examples are abundant; no UX jargon barriers; outcomes are clearly defined." The measure is about following, not about correctly prioritizing. Section 3.2 (Nielsen's Heuristics) Tiny Teams pattern: "The human reviews AI findings and makes the final call on which to address" — this requires the human to have sufficient UX judgment to review AI findings. That judgment is not trained by the framework's 9/10 accessibility score |
| **Dimension** | Actionability |
| **Mitigation** | Revise the C6 accessibility criterion to distinguish "initiation accessibility" (can a non-specialist start this framework?) from "outcome accessibility" (can a non-specialist correctly interpret and act on this framework's outputs?). Add an "output literacy" requirement to each sub-skill: what does a non-specialist need to understand to correctly prioritize and act on AI-generated outputs? For Nielsen's Heuristics specifically, document the "severity triage heuristic" — guidance for non-specialists on distinguishing high-impact from low-impact violations |
| **Acceptance Criteria** | Section 1 C6 criterion rubric is revised to include "outcome accessibility" alongside "initiation accessibility." Section 3.2 (Nielsen's Heuristics) and at least 2 other framework descriptions include a "non-specialist output guide" explaining how to prioritize AI-generated findings correctly |

---

### IN-007-20260302: The 10-Framework Ceiling Is Convention, Not Constraint [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Type** | Assumption |
| **Original Assumption** | 10 frameworks is the right portfolio size — the analysis treats it as a "binding constraint" but does not document why 10 and not 8, 11, or 12 |
| **Inversion** | Adding Service Blueprinting (rank 11, score 7.35) and Cognitive Walkthrough (rank 16, score 6.90) to create a 12-framework portfolio addresses two explicitly documented gaps (service design coverage, complex navigation triage) that the analysis itself flags as "HIGH RISK" and "V2 recommendation" gaps. The cost of adding 2 frameworks is 2 additional sub-skills; the benefit is eliminating 2 documented risk items. If 10 was chosen for operational reasons (e.g., implementation capacity), that constraint should be documented. If 10 was chosen arbitrarily as a round number, the exclusion of Service Blueprinting and Cognitive Walkthrough requires re-examination |
| **Plausibility** | Medium — "10" is a suspiciously round number. The analysis does not derive 10 from an implementation budget, a cognitive load constraint, or a routing complexity threshold. Section 4 Gap Analysis explicitly names Service Blueprinting as "the strongest candidate for a V2 skill" and Cognitive Walkthrough as "the natural V2 candidate" — both are close enough in score to warrant inclusion if the ceiling is not binding |
| **Consequence** | The portfolio has two documented gaps (service design, complex navigation) that are addressed by frameworks scored above 6.90 that were excluded by an undocumented constraint. If the constraint is not binding, the selection has left value on the table |
| **Evidence** | Section 4, Gap Analysis: "Service Blueprinting is the strongest candidate for a V2 `/ux-service-design` skill." Section 4, Gap Analysis: "Cognitive Walkthrough (rank #16, score 6.90) is the natural V2 candidate." Section 4, Gap Analysis opening: "The 10-framework ceiling was treated as a binding constraint rather than an arbitrary cutoff" — but the derivation of the constraint is not documented in the analysis |
| **Dimension** | Completeness |
| **Mitigation** | Document the derivation of the 10-framework ceiling. If it is implementation-capacity-driven, state the implementation capacity assumption explicitly. If it is routing complexity-driven, document the routing complexity reasoning. If it is a Jerry skill convention, reference that convention. Alternatively, replace the lowest-scoring selected framework (Fogg Behavior Model, 7.60) with Service Blueprinting (7.35 — nearly equivalent score) if service design coverage is assessed as higher priority than behavioral diagnosis coverage for the target user population |
| **Acceptance Criteria** | Section 1 or a new "Portfolio Sizing" section documents the derivation of the 10-framework ceiling with a specific, documented constraint (not "binding constraint" without derivation) |

---

### IN-009-20260302: AI-First Design Framework Instability [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Type** | Assumption |
| **Original Assumption** | The practitioner guidance synthesized for AI-First Design (Nudelman 2025, Fard 2025-2026, NN Group 2026) represents a stable enough foundation to build a lasting framework |
| **Inversion** | AI interaction patterns are shifting faster than any other UX domain. Streaming UI was experimental in 2024, standard in 2025, and may be a solved/commoditized pattern by 2027 — no longer requiring a specialized framework, just standard component library usage. The synthesized AI-First Design framework is optimized for current-state AI capabilities; it may be obsolete before it is fully implemented |
| **Plausibility** | High — the domain velocity is the analysis's own stated risk. The maturity score of 2/10 reflects this |
| **Consequence** | The `/ux-ai-first` skill requires the most expensive upfront investment (synthesis deliverable) for the least stable return (a framework that may need complete revision within 18-24 months) |
| **Evidence** | Section 3.7: "RT-003 TRANSPARENCY NOTICE: Unlike the other 9 selected frameworks, AI-First Design does NOT have an authoritative, codified framework document." Section 3.7: "Building `/ux-ai-first` requires a prerequisite framework synthesis deliverable." Combined with the fastest-moving UX domain signal |
| **Dimension** | Methodological Rigor |
| **Mitigation** | Define a "framework review cadence" for AI-First Design: the synthesized framework should be reviewed against current practitioner guidance at 6-month intervals. Document the expected shelf life explicitly: "This framework synthesis is accurate as of Q1 2026 and should be re-validated before Q4 2026 implementation" |
| **Acceptance Criteria** | Section 3.7 includes an explicit framework review cadence and shelf-life statement for the AI-First Design synthesis deliverable |

---

### IN-010-20260302: Qualitative Maturity Scoring Introduces Undetectable Scoring Bias [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Type** | Assumption |
| **Original Assumption** | The qualitative maturity estimates for newer frameworks are accurate enough to correctly position them relative to each other |
| **Inversion** | If Service Blueprinting's maturity score is accurate at 9/10 (it has 40+ years of validation as stated), but JTBD is scored 8/10 (Christensen school widely cited since 2003), the 1-point gap may be a scoring artifact rather than a true maturity difference. A 1-point change in Service Blueprinting's complementarity score (from 8 to 9) would increase its weighted total to 7.50, within rounding distance of Fogg Behavior (7.60) |
| **Plausibility** | Low — the score gap between the 10th selection (Fogg, 7.60) and the 11th candidate (Service Blueprinting, 7.35) is 0.25, which is larger than a single-criterion 1-point adjustment would produce at 15% weighting |
| **Consequence** | Limited — the scoring margin is sufficient to make the selection robust against single-criterion scoring errors |
| **Evidence** | Section 2, Score Calculation Verification table. The 0.25 gap between Fogg (7.60) and Service Blueprinting (7.35) is the smallest gap between selected and non-selected frameworks. Sensitivity analysis (Section 1) examines weight sensitivity but not individual score sensitivity |
| **Dimension** | Internal Consistency |
| **Mitigation** | Add a 1-point sensitivity check for the threshold gap: "If any selected framework's score changed by 1 point on any criterion, would the top-10 selection change?" The sensitivity analysis covers weight sensitivity but not individual score sensitivity |
| **Acceptance Criteria** | Section 1 Sensitivity Analysis includes a brief score-sensitivity check confirming that no single 1-point scoring error on any criterion would change the selected top 10 |

---

## Recommendations

### Critical Assumptions (MUST mitigate before implementation)

| ID | Finding | Mitigation Action | Acceptance Criteria |
|----|---------|------------------|---------------------|
| IN-001-20260302 | Selection quality ≠ implementation quality | Add "AI execution confidence map" to each of 10 framework descriptions in Section 3, distinguishing deterministic execution from synthesis hypothesis steps | Each Section 3 entry documents AI execution mode per step with at least one concrete human validation requirement |
| IN-002-20260302 | MCP ecosystem stability assumption | Add "MCP Stability Risk Assessment" section documenting commercial model, stability record, and fallback workflow for each of 7 MCP tools | Section includes fallback workflows for the 3 highest-MCP-dependency frameworks (Atomic Design, Design Sprint, AI-First Design) |
| IN-003-20260302 | AI synthesis of qualitative data produces plausible fictions | Revise all framework descriptions to label AI steps as "deterministic execution" vs. "synthesis hypothesis" with required human validation step for hypothesis outputs | All 10 Section 3 entries distinguish AI execution modes; JTBD and Design Sprint sections include explicit hypothesis-labeling for AI synthesis outputs |

### Major Assumptions (SHOULD mitigate before skill implementation)

| ID | Finding | Mitigation Action | Acceptance Criteria |
|----|---------|------------------|---------------------|
| IN-004-20260302 | Tiny Teams weight silently excludes larger team contexts | Add "Scope Boundary" statement declaring team-size optimization and naming 2+ excluded frameworks for larger teams | Section 1 opening includes explicit scope boundary with named frameworks for teams > 5 |
| IN-005-20260302 | No parent skill means worst-combination is default | Define invocation decision tree or triage questionnaire for the parent `/user-experience` skill | Decision tree covers 5 common user intents and routes to the correct sub-skill(s) |
| IN-006-20260302 | Non-specialist actionability is under-validated | Revise C6 criterion to include "outcome accessibility" alongside "initiation accessibility"; add non-specialist output guides | C6 rubric revised; Section 3.2 (Nielsen) and 2 other descriptions include output prioritization guidance |
| IN-007-20260302 | 10-framework ceiling is convention, not derived constraint | Document the derivation of the 10-framework ceiling with a specific constraint | Section 1 or new "Portfolio Sizing" section documents ceiling derivation |

### Minor Assumptions (MAY mitigate)

| ID | Finding | Mitigation Action | Acceptance Criteria |
|----|---------|------------------|---------------------|
| IN-009-20260302 | AI-First Design framework instability | Define 6-month review cadence and explicit shelf-life statement for AI-First Design synthesis | Section 3.7 includes review cadence and shelf-life date |
| IN-010-20260302 | Qualitative maturity scoring bias | Add 1-point score-sensitivity check to Section 1 sensitivity analysis | Section 1 documents that no single 1-point scoring error changes the top-10 selection |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | IN-004: Tiny Teams weight systematically excludes frameworks for larger teams (a population the skill will serve). IN-007: 10-framework ceiling is undocumented — two identified gaps (service design, complex navigation) are not explicitly resolved. AG-6 anti-goal unaddressed: full lifecycle coverage at the framework level without integration mechanisms |
| Internal Consistency | 0.20 | Negative | IN-008: Lean UX and Design Sprint operational overlap creates conflicting guidance in the same sprint context. IN-010 (minor): score-sensitivity not validated for threshold gap |
| Methodological Rigor | 0.20 | Negative | IN-001: Conflation of "framework composability" with "AI execution fidelity" is a methodological gap in the evaluation criteria design. IN-009 (minor): AI-First Design framework instability is a methodological risk in the synthesized framework |
| Evidence Quality | 0.15 | Negative | IN-002: MCP ecosystem stability assumed without evidence — scoring based on current-availability snapshot with no deprecation risk assessment. IN-003: AI synthesis of qualitative data treated as equivalent to validated user research — the evidence quality of AI-generated job statements and thematic analyses is systematically overestimated |
| Actionability | 0.15 | Negative | IN-005: No parent skill and no invocation protocol means actionability depends on users reading and internalizing the Complementarity Matrix. IN-006: Non-specialist output guides absent from 8 of 10 framework descriptions |
| Traceability | 0.10 | Positive | All findings trace to specific deliverable sections, evidence identifiers (E-001 through E-023), and prior strategy outputs (RT-001 through RT-010, SM-001 through SM-009). Finding provenance is strong. The core selection logic is traceable through the scoring matrix |

---

## Execution Statistics
- **Total Findings:** 10 (3 Critical, 4 Major, 2 Minor, 1 detail-only)
- **Critical:** 3 (IN-001, IN-002, IN-003)
- **Major:** 4 (IN-004, IN-005, IN-006, IN-007)
- **Minor:** 2 (IN-009, IN-010)
- **Goals Inverted:** 6 (G-1 through G-6)
- **Anti-Goals Enumerated:** 6 (AG-1 through AG-6); 4 not fully addressed by deliverable
- **Assumptions Mapped:** 14 (5 explicit, 9 implicit)
- **Vulnerable Assumptions (Major+):** 7
- **Protocol Steps Completed:** 6 of 6

---

## H-15 Self-Review

Before persistence, this report was self-reviewed against the following criteria:

1. **All findings have specific evidence from the deliverable:** Confirmed. Each finding references specific sections, criterion rubrics, or scoring notes from the deliverable.
2. **Severity classifications are justified:** Confirmed. Critical findings (IN-001, IN-002, IN-003) each identify a condition that could invalidate the deliverable's core value proposition if the assumption fails. Major findings (IN-004 through IN-007) each significantly degrade deliverable value without invalidating the core selection. Minor findings are improvement opportunities.
3. **Finding identifiers follow the template prefix format IN-{NNN}-{execution_id}:** Confirmed. All identifiers use IN-{NNN}-20260302 format.
4. **Report is internally consistent:** Confirmed. Summary table (10 findings) matches detailed findings count (3C + 4M + 2Mi + 1 detail). Anti-goal AG-8 addressing Lean UX/Design Sprint overlap is captured in IN-008 as Major.
5. **No findings were omitted or minimized (P-022):** Confirmed. The Inversion technique is designed to surface assumption vulnerabilities; all plausible inversions with High or Medium plausibility were escalated to findings. Low-plausibility inversions (IN-010) were included as Minor findings rather than discarded.

---

*adv-executor | S-013 Inversion Technique | Template: s-013-inversion.md v1.0.0 | Date: 2026-03-02*
*SSOT: `.context/rules/quality-enforcement.md` | C4 Tournament Execution*
