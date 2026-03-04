# Red Team Report: UX Framework Selection -- Weighted Multi-Criteria Analysis

**Strategy:** S-001 Red Team Analysis
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
**Criticality:** C3 (Significant -- framework selection governs a production skill implementation)
**Date:** 2026-03-02
**Reviewer:** adv-executor (S-001 Red Team)
**H-16 Compliance:** S-003 Steelman not formally applied as a separate prior artifact; a steelman note appears inline in the deliverable (Section 2, AI-First Design entry). Per mission parameters, this execution proceeds with acknowledgment that the full H-16 protocol was not completed prior to this red team; the inline steelman is treated as a good-faith partial compliance.
**Threat Actor Profile:**
- **Primary:** A 2-person Tiny Team (developer + PM, no UX specialist) who adopts the selected 10 frameworks and discovers, 6 months later, that critical UX problems in their product were not caught by any of the 10 frameworks they were given.
- **Secondary:** An experienced UX lead reviewing the selection methodology and finding the scoring criteria structurally biased toward lightweight frameworks, producing a selection that looks coherent but fails for complex product contexts.
- **Goal:** Expose attack vectors where the framework selection fails its own stated purpose: enabling AI-augmented Tiny Teams to produce high-quality UX.
- **Capability:** Full read access to the deliverable, awareness of industry-standard UX practice, and domain knowledge of where small teams fail in UX execution.
- **Motivation:** Avoid the failure mode of recommending a framework set that covers paper domains but not real operational UX problems.

---

## Summary

The UX Framework Selection is a technically rigorous, well-structured analysis that evaluated 40 frameworks across 6 criteria and produced a coherent selection rationale. The scoring methodology is internally consistent and the complementarity analysis is genuinely strong. However, a red team assessment reveals four critical or major attack vectors: (1) the methodology lacks validation against real Tiny Team UX failure modes, producing a selection optimized for scoring rather than real-world effectiveness; (2) the MCP integration scores conflate aspirational integration with operational reality for two frameworks whose MCP paths are dependent on third-party bridges rather than production servers; (3) the "AI-First Design" selection is built on a framework that does not yet exist in codified form, representing an unjustifiable risk for a production Jerry skill; (4) the selection has a structural gap in user research and testing methodology that the analysis acknowledges but does not adequately resolve. Recommendation: **REVISE** -- address three critical/major findings before finalizing the skill architecture.

---

## Findings Table

| ID | Attack Vector | Category | Exploitability | Severity | Priority | Defense | Affected Dimension |
|----|---------------|----------|----------------|----------|----------|---------|-------------------|
| RT-001 | Selection criteria not validated against actual Tiny Team UX failure modes -- frameworks scored on structural properties rather than outcome evidence | Ambiguity | High | Critical | P0 | Missing | Methodological Rigor |
| RT-002 | MCP integration scores for Hotjar and Kano inflate C3 scores using indirect/third-party bridges as equivalent to direct MCP servers | Ambiguity | High | Critical | P0 | Missing | Evidence Quality |
| RT-003 | AI-First Design selected as #7 despite having no authoritative codified framework -- the "emerging synthesis" source is the analysis itself, creating a circular reference | Dependency | High | Critical | P0 | Partial | Evidence Quality |
| RT-004 | User research and testing methodology gap: the deliberate exclusion of any user research framework is rationalized but creates a functional gap a Tiny Team cannot overcome with AI substitution alone | Boundary | Medium | Major | P1 | Partial | Completeness |
| RT-005 | Tiny Teams applicability criterion (25% weight) operationally favors lightweight frameworks even when more rigorous frameworks would produce better outcomes at the cost of slightly more effort | Circumvention | High | Major | P1 | Missing | Methodological Rigor |
| RT-006 | Kano Model requires user survey distribution and response collection -- a non-trivial operational dependency that the deliverable does not adequately surface as a Tiny Teams barrier | Boundary | Medium | Major | P1 | Partial | Actionability |
| RT-007 | Complementarity matrix lifecycle coverage has a structural gap: no framework covers the "failed launch" or "triage existing product" scenario, only the "new product" path | Boundary | Medium | Major | P1 | Missing | Completeness |
| RT-008 | Scoring inconsistency: Design Sprint receives C4 Maturity score of 8 but Lean UX receives 8, while Double Diamond (score 9) was rejected partly on other grounds -- the maturity dimension does not differentiate meaningfully within the selected set | Circumvention | Low | Minor | P2 | Partial | Internal Consistency |
| RT-009 | HEART Framework's Hotjar MCP integration is described as "third-party MCP via Zapier/Pipedream" but this is a workflow automation bridge, not a native MCP server -- the distinction is masked by the uniform C3 scoring scale | Ambiguity | Low | Minor | P2 | Missing | Traceability |
| RT-010 | The analysis treats AI-augmentation of frameworks as uniform ("AI handles execution") without framework-specific evidence that AI can execute the specific steps claimed (e.g., AI synthesizing JTBD job statements from app reviews) | Dependency | Medium | Minor | P2 | Partial | Evidence Quality |

---

## Detailed Findings

### RT-001: Criteria Not Validated Against Actual UX Failure Modes [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 1: Evaluation Methodology (Weighting Rationale) |
| **Strategy Step** | Step 2: Enumerate Attack Vectors -- Ambiguity exploitation |

**Attack Vector:** The adversary (a Tiny Team that adopted these frameworks and failed) discovers that none of the 10 selected frameworks helped them catch the most common UX problems that actually sink early-stage products: inadequate onboarding clarity, confusing navigation taxonomy, misaligned mental models, and undefined error states. The selection was optimized for framework structural properties (composability, AI-automatable steps, MCP hooks) rather than for covering the most common UX failure modes that Tiny Teams actually encounter.

**Category:** Ambiguity exploitation -- vague "fitness for purpose" definition permits a selection that scores well on criteria without being validated against actual purpose.

**Exploitability:** High -- the deliverable's own stated purpose is "enabling AI-augmented Tiny Teams to produce high-quality UX," but no section validates that the 10 selected frameworks collectively address the most common sources of poor UX in small-team products.

**Severity:** Critical -- the selection could be systematically correct on all 6 criteria but still fail its core mission if the criteria themselves do not measure mission-critical outcomes.

**Existing Defense:** None. The analysis presents no evidence or research linking framework selection to UX outcome improvement for small teams. The "Tiny Teams research" is cited for team size and AI augmentation patterns, not for which frameworks actually improve UX quality in practice.

**Evidence from deliverable:**
> "The primary purpose of the /user-experience skill is to serve 2-3 person AI-augmented teams. This is the highest-weight criterion because it determines fitness for purpose." (Section 1, Weighting Rationale, C1)

The weighting rationale defines "fitness for purpose" as "applicability to Tiny Teams" -- which is operationalized as team-size compatibility and AI automation potential. This conflates "works for a small team" with "produces good UX outcomes." A framework can be perfectly executable by a small team with AI and still not address the UX problems that actually matter for their product.

**Affected Dimension:** Methodological Rigor (the criteria selection methodology lacks outcome validation)

**Countermeasure:** Add a Section 1 sub-section: "Criteria Validation Against UX Failure Modes." List the 5-7 most common UX failures in early-stage software products (e.g., poor onboarding, confusing navigation, unclear error states, missing empty states, misaligned mental models, inaccessible core flows). Map each failure mode to which of the 10 selected frameworks is positioned to catch it. Any failure mode not caught by any framework is a genuine gap. This validation changes the analysis from "frameworks that work for small teams" to "frameworks that catch the problems that small teams need to catch."

**Acceptance Criteria:** A coverage table showing: (1) 5+ common UX failure modes, (2) which selected framework addresses each, (3) explicit acknowledgment of failure modes not addressed, (4) judgment that uncovered failure modes are either out of scope or handled via AI capability rather than a specific framework.

---

### RT-002: MCP Integration Scores Conflate Production Servers with Third-Party Bridges [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 1: Criterion 3 (MCP Tool Integration); Sections 3.4 and 3.9 |
| **Strategy Step** | Step 2: Enumerate Attack Vectors -- Dependency attack |

**Attack Vector:** A developer on the Tiny Team attempts to implement the HEART metrics workflow using Hotjar MCP. They discover that "third-party MCP via Zapier/Pipedream" is not a native MCP server -- it is a workflow automation bridge requiring: (a) a Zapier account and paid plan, (b) custom Zap configuration, (c) an intermediary webhook or API connector, and (d) ongoing maintenance when Hotjar or Zapier change their APIs. The promised "AI agents can execute framework steps through these MCP integrations" is aspirational rather than operational. The same team finds that the Fogg Behavior Model's Hotjar integration has the same dependency. Two of the 10 selected frameworks have their MCP integration claims dependent on this unverified third-party bridge.

**Category:** Dependency attack -- the MCP integration scores assume external dependencies (Zapier, Pipedream) that are neither verified nor consistently categorized with direct MCP servers.

**Exploitability:** High -- the C3 criterion's own description (Section 1) explicitly states "existing production-ready MCP servers" as the definition for scores of 9-10, and "some manual bridging required" for 7-8. A third-party automation bridge is significantly more than "manual bridging" and should score 3-4, not 6.

**Severity:** Critical -- the MCP integration criterion is weighted 15% and is a primary differentiator used to justify inclusions. If HEART's C3 score is 4 rather than 6, and Fogg's C3 score is 3 rather than 4, neither framework's overall score changes enough to displace them from the top 10 -- but the rationale for their MCP claims is materially false, and the Tiny Team who relies on these integrations will face significant implementation friction that was not disclosed.

**Existing Defense:** Partial. The deliverable does qualify Hotjar as "third-party MCP via Zapier/Pipedream" rather than claiming it is an official MCP server. However, the scoring does not reflect this qualification -- a 6/10 MCP score (HEART) and 4/10 (Fogg) on C3 do not differentiate between "tangential MCP use" and "third-party bridge requiring paid automation platform."

**Evidence from deliverable:**
> "Hotjar (third-party MCP via Zapier/Pipedream) -- Happiness signals from surveys and session recordings; Task Success from funnel analysis" (Section 3.4 HEART, Required MCP Integrations)

> Section 1 C3 criterion: "9-10: Framework's workflow directly and naturally connects to 2+ tools with existing production-ready MCP servers... AI agents can execute most framework steps through these MCP integrations without manual workarounds"

Hotjar via Zapier/Pipedream is definitionally not "without manual workarounds" -- it requires a multi-service configuration.

**Affected Dimension:** Evidence Quality (scoring criteria not applied consistently to the evidence)

**Countermeasure:** (1) Add a "MCP Integration Reality Check" column to the scoring matrix distinguishing: Native MCP (official or well-maintained community server), Bridge MCP (requires Zapier/Pipedream or equivalent intermediary), API-only (direct API integration without MCP wrapper). (2) Reconsider whether "Bridge MCP" qualifies for a score of 6 or should be scored 3-4 per the criterion definition. (3) Add a risk note to each framework that relies on bridge MCP: "Integration requires Zapier/Pipedream subscription and custom configuration; not a plug-and-play MCP."

**Acceptance Criteria:** Each framework's MCP integration type is explicitly categorized. Frameworks using third-party bridges are transparently labeled. Scoring criteria for C3 explicitly defines how bridge integrations are scored relative to native integrations.

---

### RT-003: AI-First Design Framework Is a Circular Reference -- The Analysis Cites Itself [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.7: AI-First Design (Emerging) |
| **Strategy Step** | Step 2: Enumerate Attack Vectors -- Dependency attack |

**Attack Vector:** A skilled UX professional reviewing the selection asks: "Show me the authoritative AI-First Design framework document." The analysis cites "Nudelman 'UX for AI' 2025" and "Adam Fard AI UX frameworks 2025-2026." Nudelman's work is a practitioner book about designing AI products, not a codified framework with defined phases, inputs, outputs, and completion criteria. Adam Fard is a UX designer who publishes articles on AI UX, not an established framework author. The "AI-First Design emerging framework synthesis" described in Section 3.7 is synthesized by the analysis itself -- the framework that a Jerry skill would implement is being invented by this deliverable, not cited from it. When a developer tries to build the `/ux-ai-first` skill, they have no authoritative framework to implement.

**Category:** Dependency attack -- the selection depends on an external framework that does not exist in implementable form; the analysis fills the gap by creating the framework, creating a circular reference.

**Exploitability:** High -- the deliverable explicitly acknowledges this: "The strongest argument against including AI-First Design is that its lack of codification means agents cannot follow authoritative guidance -- the skill risks being inconsistent or incomplete." The analysis then dismisses this concern by noting the framework fills a critical gap. The concern is not dismissed, it is deferred.

**Severity:** Critical -- a Jerry sub-skill (`/ux-ai-first`) cannot be built without a framework to implement. If the framework must be invented by the skill author, then the analysis has selected a vacancy rather than a framework. The skill will be inconsistent, poorly validated, and potentially contradictory to whatever authoritative AI UX frameworks are published in 2026-2027.

**Existing Defense:** Partial. The deliverable includes an explicit steelman of this concern and proposes that "the Jerry skill can synthesize the best-available guidance." This is a defense, but it reframes the problem (selecting a framework) as a different task (framework creation), without acknowledging that the skill-building effort just became significantly larger and riskier.

**Evidence from deliverable:**
> "Despite its low maturity score (3 -- the framework is still being codified), the urgent need and very high tiny team applicability score (10) justify its inclusion over more mature but less relevant alternatives." (Section 3.7)

> "The Jerry skill can synthesize the best-available guidance from Nudelman, Fard, and emerging NN Group content on AI UX, and document that synthesis as the authoritative reference for the skill -- making the framework's lack of external codification less of a barrier." (Section 3.7, Steelman)

This sentence reveals the actual plan: the Jerry skill will create the authoritative reference, not follow one.

**Affected Dimension:** Evidence Quality (the framework cited as a selection basis does not exist as a discrete, citable artifact)

**Countermeasure:** Two options: (A) Replace AI-First Design with Service Blueprinting (score 7.35, #11) or Hook Model (score 7.00, #13) -- both have codified frameworks, established literature, and clear implementation paths. Service Blueprinting in particular is the strongest displaced candidate. The gap in AI product UX is real but can be addressed differently. (B) Retain AI-First Design but reframe it explicitly as "Framework to be created by Jerry project" with a distinct status label ("Synthesized," not "Emerging"), add a prerequisite that `/ux-ai-first` cannot be built until a synthesis document is produced as a separate deliverable, and score its maturity as 1-2 (not 3) to reflect that it requires framework creation, not merely framework adoption.

**Acceptance Criteria:** Either (A) AI-First Design is replaced with a framework that has an authoritative, citable specification, OR (B) AI-First Design is explicitly labeled as a framework-creation exercise with a separate prerequisite deliverable, and its maturity score is corrected to 1-2.

---

### RT-004: User Research Gap Is Understated -- AI Cannot Substitute for Real User Contact [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 4: Gap Analysis ("Intentional gap that was NOT corrected") |
| **Strategy Step** | Step 2: Enumerate Attack Vectors -- Boundary violation |

**Attack Vector:** A Tiny Team building a consumer product with the 10 selected frameworks discovers, after launch, that their product fails because they never spoke to a real user. The analysis explicitly excludes "a dedicated remote user research framework" and justifies this with "AI-synthetic research (personas, simulated usability testing) can substitute for many traditional user research activities." This claim is unsubstantiated. The UX industry's current consensus (NN Group, Baymard Institute, Jobs to Be Done practitioners) is explicitly contrary: AI-generated personas are dangerous substitutes for real user research because they reflect training data biases, not the team's specific user population.

**Category:** Boundary violation -- the gap between "Design Sprint Friday testing" (5 users for 1 day) and adequate user validation for a launched product is substantial. The analysis's coverage of this gap is the minimum viable claim, not a thorough assessment.

**Exploitability:** Medium -- the analysis does acknowledge the gap. The attack vector is the insufficiency of the mitigation, not the absence of acknowledgment.

**Severity:** Major -- user research is not optional for UX quality; it is the empirical foundation of the entire discipline. A framework selection that treats user research as an AI-substitutable activity is systematically underestimating the most common and most costly source of UX failure: building the wrong thing for the wrong user.

**Existing Defense:** Partial. The analysis cites "Design Sprint's Friday testing protocol and Lean UX's validation loops" as coverage. This is a defense, but Friday testing is 5 users for 5 hours -- a minimal bar for complex products.

**Evidence from deliverable:**
> "Intentional gap that was NOT corrected: The selected 10 does not include a dedicated remote user research framework. This is intentional: the Tiny Teams research confirms that AI-synthetic research (personas, simulated usability testing) can substitute for many traditional user research activities." (Section 4)

The claim "AI-synthetic research can substitute for many traditional user research activities" is not cited to a source. The "Tiny Teams research" cited (tiny-teams-research.md) is a survey artifact produced by this same project -- it is not an independent peer-reviewed source for the claim that AI can substitute for user research.

**Affected Dimension:** Completeness (the declared gap is larger than the analysis acknowledges)

**Countermeasure:** (1) Add a specific warning label to the gap: "HIGH RISK: Products with untested user assumptions SHOULD NOT rely on AI-synthetic research as a substitute for real user contact. The Design Sprint Friday protocol and Lean UX validation loops are minimum viable research -- not comprehensive UX research programs." (2) Add a V2 priority recommendation: Service Blueprinting or a dedicated user testing framework (Maze, UserZoom) should be the first addition to the selected set when a V2 is scoped. (3) Remove the unsubstantiated claim that "AI-synthetic research can substitute for many traditional user research activities" or cite an authoritative source that supports it.

**Acceptance Criteria:** The user research gap is labeled HIGH RISK rather than "intentional gap." The claim about AI substitution is either cited or removed. A V2 recommendation for a user research framework is explicitly added to the roadmap.

---

### RT-005: 25% Tiny Teams Weight Structurally Disadvantages Rigorous Frameworks [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1: Weighting Rationale (C1 = 25%); Section 2: Full Scoring Matrix |
| **Strategy Step** | Step 2: Enumerate Attack Vectors -- Rule circumvention |

**Attack Vector:** The adversary (a UX lead) examines the scoring matrix and finds that frameworks with high Tiny Teams scores (9-10) have a 2.25-2.50 point head start on the 10-point scale versus frameworks scoring 5-6 (1.25-1.50 points). This creates a structural ceiling for methodologically rigorous frameworks. Contextual Design (3.40), GOMS (3.05), and Usability Engineering Lifecycle (2.60) all score very low -- but they score low partly because they are genuinely expert-team methodologies, and partly because the 25% weight ensures any framework that requires more than one day of learning is mathematically disadvantaged by 1.0+ points before the other criteria are scored. The result: the selection is biased toward "easy to start" over "effective at solving hard UX problems."

**Category:** Rule circumvention -- the weighting scheme, while internally consistent, produces a structural result that may not align with the stated goal of "producing high-quality UX." A 2-3 person team with AI can potentially execute more rigorous frameworks than the scoring assumes if AI handles the expert overhead.

**Exploitability:** High -- the scoring matrix is transparent enough that any reviewer can observe the weighting effect. The criterion definition for C1 explicitly penalizes frameworks with "multi-week workshops or organizational change requirements" -- which is correct for some frameworks, but also catches frameworks that are rigorous rather than complex.

**Severity:** Major -- the 25% weight is a design choice with significant consequences for which frameworks were selected. If the weight had been 20%, some of the rejected frameworks (Service Blueprinting at 7.35, Hook Model at 7.00) would have scored within 0.3-0.5 points of the selected #10 (Kano at 7.65). The selection outcome is sensitive to this weight in a way the deliverable does not surface.

**Existing Defense:** Missing. The deliverable justifies the 25% weight but does not include a sensitivity analysis showing how the top 10 would change if the weight were 20% or 30%.

**Evidence from deliverable:**
> "Tiny Teams Applicability: 25% -- The primary purpose of the /user-experience skill is to serve 2-3 person AI-augmented teams. This is the highest-weight criterion because it determines fitness for purpose." (Section 1, Weighting Rationale)

This is a reasonable criterion. The attack vector is not that the criterion is wrong, but that its weight is not validated against alternative weights and that the deliverable does not disclose the selection's sensitivity to this choice.

**Affected Dimension:** Methodological Rigor (sensitivity analysis missing from a decision-weighted methodology)

**Countermeasure:** Add a sensitivity analysis sub-section to Section 1: "What if Tiny Teams Applicability were weighted at 20% instead of 25%?" Show the top 10 at alternative weights and confirm the selection is robust (or document which frameworks would swap in). If the selection changes significantly at 20%, the 25% weight needs stronger justification. If the selection is stable, the sensitivity analysis strengthens the methodology's credibility.

**Acceptance Criteria:** A 2-row sensitivity table showing top-10 selection at 25% (current) and at 20% weight. If selection is stable: note confirmed. If selection changes: update weighting rationale with stronger justification for 25% or revise the weight.

---

### RT-006: Kano Model Requires User Survey Distribution -- An Operational Barrier Not Surfaced [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.10: Kano Model |
| **Strategy Step** | Step 2: Enumerate Attack Vectors -- Boundary violation |

**Attack Vector:** A Tiny Team runs `/ux-kano-model` and discovers they need to distribute a structured questionnaire to their user base. For a pre-launch product, they have no user base to survey. For a post-launch product with a small user base (50-200 users), getting statistically meaningful Kano responses typically requires 30+ respondents per feature evaluation to classify features with confidence. The deliverable presents Kano as "AI can design the survey, distribute it, collect responses, and run the classification algorithm" -- but AI cannot manufacture willing survey respondents. This is a fundamental operational constraint that the Tiny Teams pattern elides.

**Category:** Boundary violation -- the framework's effectiveness depends on user survey access that Tiny Teams may not have, especially at early stages when Kano would be most useful for roadmap prioritization.

**Exploitability:** Medium -- the deliverable does describe the survey requirement accurately. The attack is that the Tiny Teams enablement pattern presents the user survey step as "AI distributes it" without acknowledging that having an accessible user population is a prerequisite.

**Severity:** Major -- if Kano cannot be executed pre-launch (no user base) or early post-launch (insufficient respondents), then the framework is useful only for products with established user populations. This narrows the applicability significantly and conflicts with the "feature prioritization before roadmap" use case.

**Existing Defense:** Partial. The deliverable acknowledges the survey mechanism but presents it optimistically.

**Evidence from deliverable:**
> "AI generates a Kano questionnaire for the top 10 proposed features in both 'functional' and 'dysfunctional' formats. The questionnaire is distributed to a targeted user segment." (Section 3.10, Tiny Teams enablement pattern)

The phrase "distributed to a targeted user segment" presupposes the existence of an accessible, willing user segment -- which is not guaranteed for Tiny Teams, especially pre-launch.

**Affected Dimension:** Actionability (the enablement pattern describes steps that cannot be executed without a prerequisite -- user population -- that is not addressed)

**Countermeasure:** Add a "Prerequisites" note to the Kano Model entry: "Kano Model requires at minimum 30 users willing to complete a structured questionnaire. Pre-launch teams without a user population should use JTBD (job statement synthesis from secondary research) instead of Kano, and reserve Kano for post-launch feature prioritization when a user base is accessible." Also add a fallback: for pre-launch teams, document how to conduct a Kano-like analysis using synthetic personas or qualitative interviews rather than quantitative surveys.

**Acceptance Criteria:** Kano Model section includes an explicit prerequisite: "Requires accessible user population for quantitative survey distribution." A pre-launch alternative path is documented (e.g., qualitative Kano approximation or JTBD substitution).

---

### RT-007: Lifecycle Gap -- No Framework for Triage or Rescue of Failing Products [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 4: Complementarity Matrix |
| **Strategy Step** | Step 2: Enumerate Attack Vectors -- Boundary violation |

**Attack Vector:** A Tiny Team is not building a new product -- they are trying to fix a product with poor UX that is losing users. The complementarity matrix (Section 4) shows three lifecycle stages: Before Design, During Design, After Design. All 10 selected frameworks map cleanly onto this forward-looking lifecycle. None are explicitly designed for the "diagnose and triage a launched product with UX problems" scenario. Nielsen's Heuristics is the closest (expert inspection), but it catches design-level problems, not systemic UX failures resulting from misaligned information architecture, broken user mental models, or accumulated technical debt in the interaction layer. A "fix it" team needs a different toolkit than a "build it" team, and the selection does not differentiate.

**Category:** Boundary violation -- the lifecycle coverage boundary ends at "After Design" but real Tiny Teams frequently inherit existing products with accumulated UX debt, not greenfield products.

**Exploitability:** Medium -- the deliverable does not explicitly claim to cover all lifecycle scenarios. The attack is that the "target context" (Tiny Teams building AI-augmented products) includes teams working on existing products, not just new ones.

**Severity:** Major -- UX debt triage is a common Tiny Team scenario. Teams join existing products, acquire products through pivots, or inherit legacy codebases. The selected 10 frameworks are optimized for forward-looking design and do not provide a strong triage methodology.

**Existing Defense:** Missing. The complementarity matrix does not acknowledge the triage or rescue scenario.

**Evidence from deliverable:**
> "BEFORE DESIGN / DURING DESIGN / AFTER DESIGN" (Section 4, Complementarity Matrix)

The three lifecycle phases assume a product that is being designed from scratch or iterated on in a clean state. There is no "TRIAGE EXISTING PRODUCT" phase.

**Affected Dimension:** Completeness (a significant use case scenario is not covered by the selected framework set)

**Countermeasure:** Add a fourth lifecycle scenario to the complementarity matrix: "TRIAGE EXISTING PRODUCT -- diagnose accumulated UX debt in a launched product." Map which of the 10 selected frameworks apply in this scenario (Nielsen's Heuristics is strongest; HEART can identify which dimensions are failing; Fogg can diagnose why specific behaviors are broken). If the triage scenario reveals a gap that none of the 10 frameworks adequately addresses (e.g., Information Architecture audit, cognitive walkthrough for complex navigation), acknowledge it explicitly and recommend it as a V2 addition (Cognitive Walkthrough, at rank 16, is the natural candidate).

**Acceptance Criteria:** Complementarity matrix includes a "Triage Existing Product" lifecycle row showing which frameworks apply and noting any coverage gap.

---

### RT-008: Maturity Scores Show Insufficient Differentiation Within Selected Set [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 2: Full Scoring Matrix (C4 scores) |
| **Strategy Step** | Step 3: Defense gap assessment -- Circumvention |

**Attack Vector:** An analyst reviewing the C4 (Maturity) scores within the selected top 10 notices that 8 of the 10 frameworks score 8/10, creating a narrow scoring range that makes the maturity criterion effectively non-differentiating for the selection. Design Sprint, Nielsen's Heuristics, HEART, Lean UX, JTBD, Fogg Behavior, Microsoft Inclusive Design, and Kano all score 8/10. Only Atomic Design (8) and AI-First Design (3) deviate. If 8 out of 10 frameworks receive the same maturity score, the criterion contributes almost no discriminating information to the selection.

**Category:** Rule circumvention -- the maturity criterion appears as a differentiator in the weighting rationale but functions as an undifferentiated baseline for most frameworks, allowing the 15% weight to be gamed by ensuring most candidates meet a "high enough" threshold.

**Exploitability:** Low -- this is a structural observation about the criterion's discriminating power, not a manipulation by the analysis author.

**Severity:** Minor -- the selection outcome is unlikely to change due to this issue, but the analytical rigor of the methodology is overstated if one of six criteria effectively scores all selected frameworks identically.

**Evidence from deliverable:**

| Framework | C4 Score |
|-----------|----------|
| Design Sprint | 8 |
| Nielsen's Heuristics | 10 |
| Atomic Design | 8 |
| HEART | 8 |
| Lean UX | 8 |
| JTBD | 8 |
| AI-First Design | 3 |
| Microsoft Inclusive | 8 |
| Fogg Behavior | 8 |
| Kano Model | 8 |

8 of 10 selected frameworks score exactly 8/10 on maturity.

**Affected Dimension:** Internal Consistency (criterion appears differentiating but is not within the selected set)

**Countermeasure:** Add a note in Section 1 (Criterion 4) acknowledging: "Within the selected top 10, maturity serves primarily as a floor criterion (eliminating immature frameworks) rather than a discriminator within the qualified set. This is expected behavior -- frameworks passing the top-10 threshold have already cleared a maturity floor." This is an honest acknowledgment rather than a methodological fix.

---

### RT-009: Hotjar Integration Categorization Misleading [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 1: MCP Tool Inventory; Sections 3.4 and 3.9 |
| **Strategy Step** | Step 2: Attack vector -- Ambiguity exploitation |

**Attack Vector:** The "MCP tool inventory from survey" in Section 1 lists "Hotjar (third-party)" but the MCP integration scores for HEART (6/10) and Fogg Behavior Model (4/10) include Hotjar as a meaningful integration factor without clarifying that "third-party MCP via Zapier/Pipedream" means the user must: pay for Zapier, configure automation workflows, and maintain the integration. This is qualitatively different from the officially supported MCP servers (Figma, Miro, Storybook, Zeroheight). The deliverable lists Hotjar in the same MCP inventory alongside official servers, creating a false equivalence. *(Note: this finding overlaps with RT-002 but focuses on the categorization problem rather than the scoring impact.)*

**Affected Dimension:** Traceability (MCP integration types not consistently categorized throughout the document)

**Countermeasure:** In Section 1's MCP tool inventory, separate tools into "Official/Community MCP" vs. "Bridge MCP (requires third-party automation)." Apply this categorization consistently throughout all framework MCP sections.

---

### RT-010: AI Automation Claims Are Framework-Agnostic, Not Evidence-Based [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 3: Individual framework Tiny Teams enablement patterns |
| **Strategy Step** | Step 2: Dependency attack |

**Attack Vector:** Each framework's "Tiny Teams enablement pattern" describes specific AI automation capabilities (e.g., "AI synthesizes job statements from user interview transcripts, support tickets, and App Store reviews" for JTBD; "AI pre-generates 20+ sketch variants" for Design Sprint). These AI capability claims are presented as enabled by the frameworks themselves, but they are general AI capabilities that work with or without the specific framework. A practitioner following these patterns discovers that the AI behaviors described depend on LLM capability at the time of execution, prompt quality, and the availability of the described input artifacts -- not on the framework methodology.

**Category:** Dependency attack -- the AI automation claims depend on LLM capabilities that are environment-specific and not guaranteed by the frameworks.

**Exploitability:** Medium -- the claims are plausible and directionally correct, but they overstate the degree to which the frameworks enable the AI behaviors versus the AI capabilities existing independently.

**Severity:** Minor -- this is an over-claim issue that reduces analytical precision without invalidating the selection.

**Evidence from deliverable:**
> "AI can generate sketch variants on Tuesday, build interactive prototypes on Thursday, and synthesize user interview notes on Friday." (Section 3.1, Design Sprint)

These are LLM capabilities, not Design Sprint capabilities. The framework enables the process structure; AI capability determines whether the automation succeeds.

**Affected Dimension:** Evidence Quality (AI automation claims are overstated as framework-specific benefits)

**Countermeasure:** Add a "Prerequisites for AI augmentation" note to each framework: "AI augmentation of this framework requires: [list specific LLM capabilities, MCP connections, or input artifacts needed]. Without these, the Tiny Teams enablement pattern falls back to [manual alternative]."

---

## Recommendations

### P0 -- Critical (MUST mitigate before acceptance)

**RT-001 -- Validate criteria against UX failure modes**
Add a failure mode coverage table to Section 1 mapping 5+ common UX failures (poor onboarding, confusing navigation, unclear error states, missing empty states, misaligned mental models) to which selected frameworks address each. Document unaddressed failure modes explicitly.
*Acceptance criteria:* Table present with all major failure modes mapped or acknowledged as intentional gaps.

**RT-002 -- Fix MCP integration categorization and scoring**
Distinguish Native MCP from Bridge MCP (Zapier/Pipedream) in the scoring rubric and throughout the document. Add risk labels to frameworks dependent on bridge integrations. Confirm whether C3 scores for HEART and Fogg Behavior accurately reflect bridge integration limitations per the criterion definition.
*Acceptance criteria:* All MCP integrations categorized as Native, Community, or Bridge. C3 scores verified against revised categorization.

**RT-003 -- Resolve AI-First Design circular reference**
Either (A) replace AI-First Design with Service Blueprinting (score 7.35, next candidate, codified framework) or Hook Model (score 7.00), or (B) explicitly label AI-First Design as a framework-to-be-created, add a prerequisite deliverable, and correct the maturity score to 1-2.
*Acceptance criteria:* AI-First Design either replaced with a citable framework OR explicitly reframed as a framework creation exercise with separate prerequisites documented.

### P1 -- Important (SHOULD mitigate)

**RT-004 -- Strengthen user research gap acknowledgment**
Replace "intentional gap" framing with "HIGH RISK gap" framing for user research. Remove or cite the unsubstantiated claim about AI substitution for user research. Add explicit V2 recommendation for a user testing framework.
*Acceptance criteria:* User research gap labeled HIGH RISK. AI substitution claim cited or removed. V2 roadmap updated.

**RT-005 -- Add sensitivity analysis for 25% weight**
Add a 2-row sensitivity table: top-10 selection at 25% vs. 20% Tiny Teams weight. If selection is stable, document it. If selection changes, update justification.
*Acceptance criteria:* Sensitivity table present showing top-10 at alternative weight.

**RT-006 -- Add Kano Model prerequisite: user population**
Add explicit prerequisite: "Requires 30+ accessible survey respondents." Document pre-launch alternative (qualitative Kano approximation or JTBD substitution).
*Acceptance criteria:* Kano prerequisites section present with user population requirement and pre-launch fallback.

**RT-007 -- Add triage lifecycle scenario to complementarity matrix**
Extend the complementarity matrix with a "Triage Existing Product" scenario. Map which of the 10 frameworks apply. Note any gaps (Cognitive Walkthrough as natural V2 candidate).
*Acceptance criteria:* Complementarity matrix includes triage scenario row.

### P2 -- Monitor (MAY mitigate)

**RT-008** -- Add a note in Section 1 that C4 (Maturity) functions primarily as a floor criterion within the top 10, not a differentiator.

**RT-009** -- Separate MCP tool inventory into "Official/Community" vs. "Bridge" categories in Section 1.

**RT-010** -- Add "AI augmentation prerequisites" note to each framework's Tiny Teams enablement pattern.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| **Completeness** | 0.20 | Negative | RT-004 (user research gap understated), RT-007 (triage lifecycle missing), RT-001 (failure mode coverage not validated) -- three significant coverage gaps |
| **Internal Consistency** | 0.20 | Negative | RT-002 (MCP scoring inconsistent with criterion definition), RT-009 (MCP categorization inconsistent), RT-008 (maturity criterion non-differentiating within selected set) |
| **Methodological Rigor** | 0.20 | Negative | RT-001 (criteria not validated against outcome evidence), RT-005 (no sensitivity analysis for dominant weight) -- methodology claims rigor it cannot fully substantiate |
| **Evidence Quality** | 0.15 | Negative | RT-003 (AI-First Design cited framework does not exist; circular reference), RT-002 (MCP claims not operationally verified), RT-010 (AI automation claims overstated as framework-specific) |
| **Actionability** | 0.15 | Mixed | Positive: framework-specific Tiny Teams patterns are detailed and concrete. Negative: RT-006 (Kano user population requirement not disclosed) creates a hidden execution barrier |
| **Traceability** | 0.10 | Positive | Evidence citations (E-001 through E-023) are well-structured; scoring matrix calculation verification is present; steelman/inversion notes are cited inline. The traceability infrastructure is strong. |

**Pre-mitigation estimated composite impact:** The three Critical findings (RT-001, RT-002, RT-003) collectively create substantial evidence quality and methodological rigor deficits. Without mitigation, an S-014 LLM-as-Judge scoring would likely place this deliverable in the 0.82-0.87 range -- below the 0.92 threshold. After addressing the three P0 findings and the four P1 findings, the deliverable should reach or exceed the 0.92 threshold.

---

## Execution Statistics

- **Total Findings:** 10
- **Critical:** 3 (RT-001, RT-002, RT-003)
- **Major:** 4 (RT-004, RT-005, RT-006, RT-007)
- **Minor:** 3 (RT-008, RT-009, RT-010)
- **Protocol Steps Completed:** 5 of 5 (Define Threat Actor, Enumerate Attack Vectors, Assess Defense Gaps, Develop Countermeasures, Synthesize and Score Impact)

---

## What Is Working Well

**Strengths to preserve in the revision:**

1. **Scoring matrix transparency:** The verification table with explicit weighted calculations and the note acknowledging rounding discrepancies is genuinely rigorous. The willingness to correct rank order based on recalculation is methodologically honest.

2. **Complementarity analysis quality:** The "before/during/after" lifecycle matrix and the integration paths table (10 integration paths documented) are the strongest part of the deliverable. This is exactly the kind of portfolio thinking that distinguishes a good framework selection from a list.

3. **Rejected frameworks analysis:** The five rejected frameworks (Sections 5.1-5.5) are analyzed honestly. The Double Diamond and Design Thinking rejections are particularly well-argued -- the analysis correctly identifies that their high brand recognition creates selection pressure that the scoring correctly resists.

4. **Seed list audit:** The transparent audit of seeds (2 selected, 8 cut) with specific rationale for each is a model of analytical honesty. The admission that the two non-seed frameworks (Design Sprint #1, AI-First Design #7) earned their places on merit, not because they were pre-seeded, is credible.

5. **Evidence citation system:** The 23-entry evidence table (E-001 through E-023) provides genuine traceability. The fact that evidence is mapped to specific sections and specific claims is the correct approach.

6. **Criterion 6 (Non-Specialist Accessibility) as a differentiator:** Including accessibility-for-non-specialists as a criterion is a genuinely innovative addition that directly serves the stated Tiny Teams goal. Most framework selection methodologies do not include this dimension.

7. **Inversion and Steelman inline notes:** The application of S-013 and S-003 thinking within the scoring matrix notes (particularly for Fogg vs. Hook Model) demonstrates analytical depth that goes beyond mechanical scoring.

---

*Red Team Report Version: 1.0 | Strategy: S-001 | Deliverable: ux-framework-selection.md | Date: 2026-03-02*
*Finding Prefix: RT | Execution ID: 20260302-RT-001*
*Template: s-001-red-team.md v1.0.0 | adv-executor agent*
