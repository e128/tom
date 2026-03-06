# Devil's Advocate Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4
**Date:** 2026-03-03T00:00:00Z
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied on 2026-03-03 (confirmed — report at `tournament-iter1/s-003-steelman.md`, execution ID S003-PROJ020-20260303-iter1)

---

## Summary

12 counter-arguments identified (2 Critical, 6 Major, 4 Minor). The deliverable's core architecture is sound and the problem framing is credible, but two Critical findings undermine the value proposition at its root: the "non-specialist execution" premise assumes a level of product/user domain knowledge that most tiny teams demonstrably lack, and the confidence gate enforcement mechanism (particularly LOW-confidence "structural omission") is a behavioral claim with no verifiable enforcement path. Six Major findings target the scope claim inflation, wave progression feasibility, MCP dependency cost realism, AI-First Design conditional risk, and behavioral scalability of the synthesis hypothesis regime. **Recommendation: REVISE. The Critical findings require substantive creator response before acceptance; the Major findings are addressable with targeted revision.**

---

## Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-S002-PROJ020-20260303 | Non-specialist execution premise assumes domain knowledge the framework cannot supply | Critical | "The full methodology, AI-augmented so non-specialists can execute it" -- Vision; every sub-skill's "What humans do" section requires product/user domain judgments | Methodological Rigor |
| DA-002-S002-PROJ020-20260303 | LOW-confidence "structural omission" is unenforced against direct AI querying | Critical | "The agent template physically does not contain a design recommendation section. This cannot be overridden by any user action" -- Decision 6; no enforcement mechanism described against out-of-skill AI prompting | Methodological Rigor |
| DA-003-S002-PROJ020-20260303 | "6-8 person UX team" capability scope claim conflates discipline scope with operational throughput in a misleading way | Major | "A 2-3 person team with this portfolio has the capability coverage...of the following specialist roles" -- Tiny Teams Capability Map; hedged only by a single paragraph disclaimer | Internal Consistency |
| DA-004-S002-PROJ020-20260303 | Wave progression criteria are practically irreversible for most tiny teams | Major | Wave 5 entry criterion requires "30+ users for Kano OR 1 B=MAP bottleneck diagnosed" -- Decision 5 Wave table; this is a substantial research burden for bootstrapped teams | Actionability |
| DA-005-S002-PROJ020-20260303 | MCP cost tiers systematically understate real integration costs | Major | "Minimal: ~$46/month" adding 5 sub-skills -- Decision 4 Cost Tiers table; excludes Whimsical verification burden, Miro workflow setup cost, annual plan commitments | Evidence Quality |
| DA-006-S002-PROJ020-20260303 | Screenshot-input "full heuristic coverage" fallback claim is not equivalent capability | Major | "Non-MCP fallback: Screenshot-input mode...Reduced automation but full heuristic coverage retained" -- sub-skill 1; conflates AI's ability to apply heuristics with access to the design's interactive/dynamic states | Evidence Quality |
| DA-007-S002-PROJ020-20260303 | AI-First Design CONDITIONAL status creates a cascading risk that is unmitigated for the Wave 5 architecture | Major | "Blocking prerequisite: A synthesis Enabler must reach DONE status with a verified WSM score >= 7.80" -- Known Limitations; the auto-substitute (Service Blueprinting) is not yet created either | Completeness |
| DA-008-S002-PROJ020-20260303 | The crisis mode sequence rationale assumes users can correctly self-diagnose "crisis UX problems" | Major | "CRISIS: Urgent UX problems" routing path -- Decision 2 flowchart; no triage criteria distinguishing crisis from non-crisis; misdirection risk is high | Methodological Rigor |
| DA-009-S002-PROJ020-20260303 | 10-sub-skill independent versioning creates a long-term maintenance burden that the issue does not account for | Minor | "Independent versioning. When a better metrics framework than HEART emerges, only /ux-heart-metrics is updated" -- Decision 1; this understates cross-skill interface compatibility burden | Completeness |
| DA-010-S002-PROJ020-20260303 | JTBD "requires actual user interviews" creates a hard prerequisite that breaks the zero-dependency Wave 1 claim | Minor | "Conducts actual user interviews (irreducible -- AI cannot observe real behavior)" -- sub-skill 2 What humans do; Wave 1 is presented as requiring no external user data | Internal Consistency |
| DA-011-S002-PROJ020-20260303 | Design Sprint 2-person adaptation claim is underspecified and potentially counterproductive | Minor | "For 2-person teams, the sprint collapses to 1-2 days with the AI filling the 'missing participant' roles" -- sub-skill 9; AI filling decision-maker roles in a sprint is an unsupported behavioral claim | Evidence Quality |
| DA-012-S002-PROJ020-20260303 | V2 trigger conditions are structurally asymmetric: success triggers V2 but failure mode has no defined response | Minor | "V2 planning begins when any 2 of these conditions are met" -- V2 Roadmap; four success/demand conditions listed; no V1 failure condition (e.g., zero adoption after 6 months) triggers any action | Actionability |

---

## Detailed Findings

### DA-001: Non-Specialist Execution Premise Assumes Domain Knowledge the Framework Cannot Supply [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Vision; all 10 sub-skills "What humans do" sections |
| **Strategy Step** | Step 3 (Counter-argument lens: Unstated Assumptions) |

**Claim Challenged:**
> "The full methodology, AI-augmented so non-specialists can execute it, with guardrails that draw a hard line between what AI handles and what humans decide."

**Counter-Argument:**
The deliverable's central value proposition -- non-specialists can execute professional UX methodology -- depends on those non-specialists possessing substantial unstated domain knowledge. Every "What humans do" entry across all 10 sub-skills requires product judgment, user population knowledge, or strategic context that the frameworks themselves cannot supply. Consider the distribution:

- `/ux-jtbd`: "Judges hypothesis validity against their knowledge of the user population" — requires existing UX research exposure to evaluate AI-generated job statements
- `/ux-lean-ux`: "Identifies which assumptions are riskiest (requires product judgment about what matters)" — requires product management expertise, not just methodology familiarity
- `/ux-heart-metrics`: "Identifies confounding factors (seasonality, marketing campaigns, etc.)" — requires analytics literacy beyond the scope of UX
- `/ux-design-sprint`: "Sets design direction and challenge statement (Day 1)" — this is the hardest part of any design sprint; it is not a structured activity AI can guide without deep user context
- `/ux-kano-model`: "Recruits survey respondents (minimum 30 for statistical reliability)" — user recruitment is a specialized research skill

The argument: A developer who has never conducted user research cannot effectively judge whether AI-generated JTBD job statements "resonate with observed user language" because they have no observed user language. The confidence gate framework exacerbates this: LOW-confidence outputs require the user to have domain knowledge to recognize *why* they should not act on them. A developer who lacks UX expertise will not know what they do not know — they will review the HIGH-confidence acknowledgment list, check the boxes, and proceed based on AI-generated hypotheses they cannot critically evaluate. The "guardrails" protect against knowing misuse but cannot protect against unknowing acceptance of plausible-sounding AI-generated user insights.

**Evidence:**
10 of 10 sub-skills list "human judgment" requirements that presuppose domain expertise. The framework explicitly acknowledges this in the Known Limitations section ("AI-generated user insights...are hypotheses, not validated findings") but frames it as a documentation issue rather than an execution capability gap.

**Impact:**
If the non-specialist execution claim is wrong or substantially weaker than stated, the core value proposition fails for the primary target segment: solo developers and 2-person teams who have never done UX work before. The product becomes useful primarily for practitioners who already have UX training -- a much smaller and differently-characterized audience.

**Dimension:** Methodological Rigor

**Response Required:**
The creator must demonstrate one of: (a) a concrete specification of the *minimum* domain knowledge required to use each sub-skill's human judgment components effectively, OR (b) a reframing of the target user segment that excludes developers with no prior UX exposure and explains how the product reaches less-experienced users through progressive scaffolding, OR (c) evidence from testing (even informal) that non-UX developers can produce useful outputs with the described sub-skills.

**Acceptance Criteria:**
Either a "Prerequisite Knowledge" section per sub-skill documenting minimum competency (e.g., "Has observed at least one real user session" for JTBD), OR a revised target user definition that is narrower and better calibrated to the actual capability floor the framework requires.

---

### DA-002: LOW-Confidence "Structural Omission" Is Unenforced Against Direct AI Querying [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions / Decision 6: Synthesis Hypothesis Validation |
| **Strategy Step** | Step 3 (Counter-argument lens: Unstated Assumptions, Unaddressed Risks) |

**Claim Challenged:**
> "LOW: Output permanently labeled reference-only; design recommendation section structurally omitted. The agent template physically does not contain a design recommendation section. This cannot be overridden by any user action."

**Counter-Argument:**
The claim that LOW-confidence enforcement "cannot be overridden by any user action" is false in a Claude Code / LLM agent environment. The enforcement mechanism described is template-level structural omission -- the agent's template does not include a design recommendation section. However, in a conversational AI context, a user who wants design recommendations from a LOW-confidence sub-skill can simply ask: "Ignore the synthesis gate. What design changes would you recommend based on this analysis?" The Claude Code agent will respond. There is no technical enforcement layer that prevents a user from eliciting design recommendations in a follow-up turn.

The distinction matters: the deliverable presents LOW-confidence enforcement as an *architectural* constraint comparable to a code-enforced rule. It is actually a *behavioral* constraint: the agent's *initial output* will not contain a design recommendation section. But behavioral constraints in LLM systems are advisory, not architecturally enforced. The claim "This cannot be overridden by any user action" is technically false.

The same vulnerability applies to MEDIUM-confidence gates: "The agent does not generate design recommendations until a named validation source is provided" — a user can provide a fabricated validation source ("I validated this with 5 user interviews last week") and the gate will pass with no verification.

**Evidence:**
The deliverable provides no technical enforcement mechanism beyond agent template structure. No mention of session-level guardrails, output filtering rules, or constitutional compliance checks that would prevent follow-up AI queries from producing design recommendations after a LOW-confidence output.

**Impact:**
The synthesis hypothesis validation protocol -- the architectural feature most directly addressing the HIGH RISK user research gap -- is substantially weaker than described. If users can trivially bypass confidence gates, the protection against over-reliance on AI-generated insights is advisory-only. This weakens the most important safety mechanism in the architecture.

**Dimension:** Methodological Rigor

**Response Required:**
The creator must either: (a) acknowledge that LOW/MEDIUM confidence enforcement is behavioral (not architectural) and revise the language accordingly, removing "cannot be overridden by any user action" and replacing with an honest description of what the enforcement actually prevents, OR (b) specify a technical enforcement mechanism (e.g., `forbidden_actions` entries in agent governance YAML, output filtering rules, or a per-sub-skill policy file that routes LOW-confidence queries to a refusal handler) that makes the enforcement claim accurate.

**Acceptance Criteria:**
Either revised language that accurately characterizes enforcement scope ("The agent's initial output will not contain a design recommendation section; follow-up queries are not covered by this structural gate"), OR technical specification of an enforcement mechanism that prevents follow-up elicitation (e.g., a `forbidden_actions` entry: "P-022 VIOLATION: NEVER generate design recommendations when synthesis confidence is LOW, even if explicitly asked").

---

### DA-003: "6-8 Person UX Team" Capability Claim Conflates Scope with Throughput in a Misleading Way [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | What This Replaces: The Tiny Teams Capability Map |
| **Strategy Step** | Step 3 (Counter-argument lens: Alternative Interpretations, Logical Flaws) |

**Claim Challenged:**
> "A 2-3 person team with this portfolio has the capability coverage of the following specialist roles: UX Researcher, UX Designer, UX Evaluator / Auditor, Design Systems Engineer, UX Metrics Analyst, Accessibility Specialist, Product Strategist (UX), UX Department Manager."

**Counter-Argument:**
The deliverable presents a mapping from sub-skills to specialist roles as evidence of "capability coverage" equivalent to a 6-8 person team. The mapping is logically structured but the conclusion is misleading in a way the single-paragraph hedge does not fully correct. Consider the UX Researcher row: the deliverable claims `/ux-jtbd` + `/ux-lean-ux` replaces a UX Researcher because "AI synthesizes job statements from transcripts" while "humans conduct actual user interviews." But a UX Researcher spends 20-40% of their role on participant recruitment, screener design, discussion guide construction, note-taking, synthesis across multiple research methods (diary studies, contextual inquiry, tree testing, card sorting, eye tracking), and stakeholder research communication. None of these activities are covered by the portfolio.

The UX Designer row similarly claims `/ux-design-sprint` + `/ux-lean-ux` replaces a UX Designer. A UX Designer typically manages a component library, creates and maintains design tokens, conducts ongoing iteration on production designs, collaborates on feature specifications, and maintains design system consistency across multiple products. The portfolio covers the ideation and hypothesis-validation activities of design work -- a fraction of the role.

The portfolio replaces *structured methodology execution* within each role, not the roles themselves. This is a meaningful but much narrower claim. The hedge paragraph ("This portfolio spans the same UX discipline scope as a 6-8 person UX team -- it does NOT match the throughput or depth") appears after a table that explicitly says "Replaced By," creating a false impression that is only partially corrected by text below the table.

**Evidence:**
The Capability Map table header column is literally titled "Replaced By." The hedge paragraph uses "discipline scope" (the correct term) but this follows the "Replaced By" framing. Readers scanning the table will take the "Replaced By" label at face value.

**Impact:**
The scope claim is the rhetorical anchor of the entire proposal. If the claim is misleading, teams will adopt the portfolio expecting more comprehensive role replacement than is delivered, leading to adoption failure, disappointment, and reputational damage to the Jerry framework.

**Dimension:** Internal Consistency

**Response Required:**
Rename the "Replaced By" column in the Capability Map table to accurately characterize the relationship (e.g., "AI-Augmented By" or "Structured Activities Covered By"). Add a subtitle to the table: "Activities covered within each role's structured methodology execution, not full role replacement."

**Acceptance Criteria:**
Table column renamed or table subtitle added. The hedge paragraph must either move before the table or be incorporated into the table header language to prevent the misleading impression on scanning readers.

---

### DA-004: Wave Progression Criteria Are Practically Unreachable for Most Tiny Teams [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions / Decision 5: Wave Deployment |
| **Strategy Step** | Step 3 (Counter-argument lens: Unaddressed Risks, Unstated Assumptions) |

**Claim Challenged:**
> "Wave 5 entry: Wave 4: 30+ users for Kano OR 1 B=MAP bottleneck diagnosed."
> "If a wave stalls for 2+ sprint cycles, documented bypass conditions allow teams to proceed with partial capability."

**Counter-Argument:**
The Wave 5 entry criterion requires either: (a) 30+ survey respondents for Kano (a substantial user recruitment effort for bootstrapped teams), or (b) a B=MAP bottleneck diagnosis (requiring that the team has a launched product with observable behavioral data). For a solo developer building a pre-launch product -- the primary target segment -- neither criterion is achievable.

More broadly, the wave progression model assumes a product lifecycle trajectory (pre-launch -> launched with data -> established user base with 30+ engaged users willing to complete surveys) that many tiny teams will not complete before abandoning the product or pivoting. The criteria-gating model may inadvertently create a system where 70-80% of the target users are permanently stuck in Wave 1-2, never experiencing the advanced capabilities that justify the portfolio's investment.

The bypass conditions are mentioned ("documented bypass conditions allow teams to proceed with partial capability") but neither the bypass conditions nor what "partial capability" means are defined in the issue. This is an acceptance criteria gap: the bypass mechanism is an architectural promise with no specified behavior.

**Evidence:**
Wave 5 entry criteria require "30+ users for Kano" explicitly. The bypass mechanism is mentioned in one sentence without specification of conditions. The Capability Map's "2-3 person team" framing does not qualify the claim by wave availability.

**Impact:**
If most target users can only reach Wave 1-2, the portfolio's effective capability is Heuristic Eval + JTBD + Lean UX + HEART -- a significantly narrower offering than the 10-sub-skill proposal implies. Design Sprint and Atomic Design (the highest-scoring sub-skills) are behind Wave 5 gates many teams will never clear.

**Dimension:** Actionability

**Response Required:**
Either specify the bypass conditions and what "partial capability" means (what does a team get when they invoke Design Sprint without meeting Wave 4 entry criteria?), OR revise the wave entry criteria to be more accessible to pre-launch teams (e.g., Wave 5 alternative entry: "Completed at least 3 Wave 1-3 sub-skill invocations across different lifecycle stages").

**Acceptance Criteria:**
Bypass conditions are explicitly defined in the wave table or in a separate subsection. At minimum: what triggers a bypass, what capability is available during bypass mode, and whether bypass mode is temporary or permanent.

---

### DA-005: MCP Cost Tiers Systematically Understate Real Integration Costs [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions / Decision 4: MCP Integration / Cost Tiers |
| **Strategy Step** | Step 3 (Counter-argument lens: Contradicting Evidence, Unstated Assumptions) |

**Claim Challenged:**
> "Minimal: ~$46/month: + Heuristic Eval, Design Sprint, Lean UX, Inclusive Design, AI-First Design (9 sub-skills)"

**Counter-Argument:**
The $46/month "Minimal" tier calculation adds Figma Professional ($15/editor) + Miro Team ($8/member) + Storybook (free) = $23/month + Claude API costs (not listed). This is arithmetically correct as a tool cost floor but understates the real integration costs in several ways:

1. **Figma billing unit:** "$15/editor/month" assumes the developer is the only user. If the team has a designer, the cost doubles to $30/month for 2 editors.
2. **Miro billing unit:** "$8/member/month" is the annual plan. The monthly plan is $10/member. The issue does not clarify billing frequency.
3. **Storybook setup overhead:** Storybook requires a configured project. For teams without an existing Storybook implementation, the setup cost is 1-3 developer days -- a real cost not captured in the $0/month figure.
4. **Whimsical stability risk:** The issue rates Whimsical as "MEDIUM-LOW -- third-party maintained" and recommends "Verify GitHub activity before implementation." This is a due diligence activity with ongoing maintenance cost. Using a community MCP for a production skill creates upgrade-maintenance obligations not reflected in "$0 cost."
5. **Bridge integration cost for Hotjar:** "Variable ($0-$99+ depending on Zapier plan)" -- this is unbounded. A team on a Zapier Free plan faces strict monthly task limits; exceeding them requires upgrade to $49+/month. The cost range is not a useful guide for budget planning.

**Evidence:**
Cost tier table lists "$46/month" without line-item arithmetic in the issue body. Figma per-editor pricing applies per-seat. Annual vs. monthly plan distinction is absent.

**Impact:**
Teams budgeting based on the issue's cost table will encounter unexpected costs at first billing cycle, eroding trust in the framework's practical guidance.

**Dimension:** Evidence Quality

**Response Required:**
Add a cost tier table footnote clarifying: per-editor vs. per-member billing; annual vs. monthly pricing; Hotjar bridge cost floor (minimum Zapier plan required for production use); Claude API cost estimate per sub-skill invocation. The issue should acknowledge that the $46/month figure is a floor for individual developer use, not a team cost estimate.

**Acceptance Criteria:**
Cost table footnotes added clarifying billing units and plan assumptions. Hotjar bridge cost listed with a concrete minimum (e.g., "Requires Zapier Starter plan: $49/month or Pipedream equivalent").

---

### DA-006: Screenshot-Input "Full Heuristic Coverage" Fallback Is Not Equivalent Capability [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `/ux-heuristic-eval` sub-skill description; Key Design Decisions / Decision 4: Figma dependency risk mitigation |
| **Strategy Step** | Step 3 (Counter-argument lens: Contradicting Evidence, Alternative Interpretations) |

**Claim Challenged:**
> "Non-MCP fallback: Screenshot-input mode. User provides design screenshots as image inputs. Reduced automation but full heuristic coverage retained."
> "No sub-skill is entirely blocked by MCP unavailability -- all 10 have documented fallbacks."

**Counter-Argument:**
The claim of "full heuristic coverage" in screenshot-input mode is technically incorrect for several of Nielsen's 10 heuristics. Screenshots capture visual states; they do not capture:

- **H4 (Consistency and Standards):** Requires access to design file tokens, component variants, and style guide to evaluate consistency across screens -- a screenshot of one screen cannot evaluate consistency across the design system.
- **H7 (Flexibility and Efficiency of Use):** Requires observation of or access to interactive prototypes to evaluate keyboard shortcuts, expert shortcuts, and accelerators -- these are behavioral properties invisible in static screenshots.
- **H8 (Aesthetic and Minimalist Design):** Can be partially evaluated from screenshots, but comparative analysis against the complete design's information hierarchy requires access to multiple screens in context.
- **H9 (Help Users Recognize, Diagnose, and Recover from Errors):** Error states may not be captured in the screenshots provided -- if the user does not provide screenshots of error flows, this heuristic cannot be evaluated.

The description "full heuristic coverage retained" overstates the fallback capability. "Partial heuristic coverage with limitations for interactive-state and consistency heuristics" would be accurate.

**Evidence:**
Sub-skill description states "full heuristic coverage retained." The 10 Nielsen heuristics include interactive-state-dependent evaluations that screenshots cannot support.

**Impact:**
Teams relying on the screenshot fallback will receive incomplete heuristic evaluations without being warned about the gaps. The design guarantee "no sub-skill is entirely blocked" is technically maintained but practically misleading if the fallback provides significantly degraded coverage.

**Dimension:** Evidence Quality

**Response Required:**
Revise the fallback description to specify which heuristics have limited coverage in screenshot-input mode (H4, H7, H8, H9 specifically). Apply the same analysis to other sub-skills claiming "full" fallback capability (e.g., `/ux-inclusive-design` screenshot-input mode for evaluating keyboard navigation paths).

**Acceptance Criteria:**
Sub-skill fallback descriptions specify what is and is not evaluable in fallback mode, with heuristic-level or capability-level specificity. The phrase "full coverage retained" is removed from any sub-skill where the fallback is actually partial.

---

### DA-007: AI-First Design CONDITIONAL Status Creates Cascading Risk Unmitigated for Wave 5 Architecture [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | `/ux-ai-first-design` sub-skill; Known Limitations: AI-First Design Conditional Status |
| **Strategy Step** | Step 3 (Counter-argument lens: Unaddressed Risks, Historical Precedents of Failure) |

**Claim Challenged:**
> "Substitution path: If the Enabler fails or expires, Service Blueprinting (rank #12, score 7.40) auto-substitutes as an established, immediately adoptable framework."

**Counter-Argument:**
The substitution path claims Service Blueprinting "auto-substitutes as an established, immediately adoptable framework." However, as the V2 Roadmap documents, Service Blueprinting is not yet a Jerry skill -- it is listed as a P1 V2 candidate. "Immediately adoptable" means immediately adoptable *when V2 is implemented*. If the AI-First Design Enabler fails before V2 is delivered, the substitution path does not exist yet.

This creates a cascading risk: AI-First Design is the only Wave 5 option for AI-product UX requests. If the Enabler fails, the interim path is `/ux-heuristic-eval` + PAIR Guidebook heuristics -- a significantly downgraded capability. The "auto-substitute" language implies this happens automatically with a comparable skill; it does not.

Additionally, the Enabler expiry mechanism is unspecified. "If the Enabler fails or expires" -- what is the expiry condition? Is there a time limit? What constitutes Enabler failure (score below 7.80 after N review cycles? Project abandonment?)? Without specified expiry conditions, the substitution trigger is non-deterministic.

**Evidence:**
V2 Roadmap lists Service Blueprinting as "P1 V2 candidate." AI-First Design Known Limitations says "auto-substitutes." These are contradictory: you cannot auto-substitute with something that does not exist yet.

**Impact:**
The Wave 5 architecture has a known single point of failure (AI-First Design Enabler) whose mitigation path depends on a V2 deliverable. For AI product teams (an explicitly named segment in the routing flowchart: "AI product" stage), the portfolio has no durable Wave 5 option.

**Dimension:** Completeness

**Response Required:**
Correct the "immediately adoptable" claim: Service Blueprinting substitutes *if and when* the V2 sub-skill is complete. Specify the Enabler expiry condition (either a time limit, a score threshold failure criterion, or a project abandonment condition). Note that the interim path (Heuristic Eval + PAIR) is the *only* current mitigation for AI-product UX requests if the Enabler fails.

**Acceptance Criteria:**
Substitution language revised to accurate state: "If the Enabler fails or expires, Service Blueprinting will substitute AFTER the V2 `/ux-service-blueprinting` sub-skill is implemented (P1 V2 candidate). Until V2, the interim path is `/ux-heuristic-eval` with supplemental PAIR Guidebook heuristics." Enabler expiry condition specified in the Known Limitations section.

---

### DA-008: Crisis Mode Sequence Assumes Users Can Correctly Self-Diagnose "Crisis" [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions / Decision 2: Parent Orchestrator Routes via Lifecycle-Stage Triage |
| **Strategy Step** | Step 3 (Counter-argument lens: Unstated Assumptions, Unaddressed Risks) |

**Claim Challenged:**
> "Handles crisis mode -- emergency 3-skill sequence (Heuristic Eval -> Behavior Design -> HEART) for products with urgent UX problems."
> From triage flowchart: "CRISIS: Urgent UX problems → 3-skill emergency: Heuristic → Behavior → HEART"

**Counter-Argument:**
The crisis routing path is triggered by user self-identification: "CRISIS: Urgent UX problems." There are no defined criteria for what constitutes a "crisis." A developer who believes they have urgent UX problems will invoke the crisis path; a developer with equally severe UX problems but no self-awareness of the severity will not.

More importantly, the crisis sequence (Heuristic Eval → Behavior Design → HEART) requires Figma (for Heuristic Eval) and potentially analytics data (for HEART). A team in a genuine UX crisis -- post-launch, users churning, revenue dropping -- may not have Figma set up or an analytics dashboard configured. The crisis path has the same MCP prerequisites as the standard path.

The S-003 Steelman added a rationale for the crisis sequence selection (three properties). But the steelman rationale addresses why this *sequence* is correct, not the equally important question of when to invoke the crisis path vs. the standard path. Without entry criteria, crisis mode is a power tool with no safety on it -- it short-circuits the normal triage and capacity check steps, which means it could be misapplied to non-crisis situations.

**Evidence:**
Routing flowchart shows "Crisis" as a direct input to the emergency sequence with no triage criteria or qualification question. The standard triage flow includes a capacity check (`UX capacity < 20%?`) and an MCP check; the crisis path bypasses both.

**Impact:**
Misapplied crisis mode bypasses the capacity check (allowing teams to invoke three heavyweight sub-skills when they have < 20% UX capacity) and bypasses MCP-readiness checks (invoking Figma-dependent Heuristic Eval when Figma is not configured). At best, the sequence fails with confusing errors. At worst, teams invest several hours in a crisis sequence with no infrastructure to complete it.

**Dimension:** Methodological Rigor

**Response Required:**
Add triage criteria to the crisis routing path: at minimum, define what constitutes a UX crisis (e.g., "user-reported usability failures causing measurable abandonment or churn"). Add a crisis-mode qualification question (e.g., "Are users actively failing to complete critical tasks, and is this affecting business metrics?"). Document the prerequisite check for crisis mode (Figma availability, basic analytics source) so teams know what they need before invoking it.

**Acceptance Criteria:**
Crisis routing entry in the triage flowchart includes at least one qualification question or explicit criterion distinguishing crisis from non-crisis. Crisis mode prerequisite requirements documented (or crisis sequence adapted to work in fallback-only mode when MCP prerequisites are unmet).

---

### DA-009: Independent Sub-Skill Versioning Understates Cross-Skill Interface Compatibility Burden [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions / Decision 1: Each Framework = Its Own Skill |
| **Strategy Step** | Step 3 (Counter-argument lens: Unaddressed Risks) |

**Claim Challenged:**
> "Independent versioning. When a better metrics framework than HEART emerges, only /ux-heart-metrics is updated."

**Counter-Argument:**
Independent versioning is only cost-free if sub-skills have no shared interfaces. The deliverable describes canonical cross-skill sequences (JTBD → Design Sprint → Lean UX → HEART), cross-framework integration handoffs tested in acceptance criteria, and a parent orchestrator that coordinates multi-framework workflows. When `/ux-jtbd` is updated to v2.0 with a different job statement output format, every downstream sub-skill that accepts JTBD output (Design Sprint challenge statement input, Lean UX assumption seeding) requires a compatibility check. The maintenance burden is not isolated to the updated sub-skill.

**Dimension:** Completeness

**Response Required:**
Acknowledgment that cross-skill interface compatibility is a versioning constraint. A note that "independent versioning" applies to sub-skills with no upstream/downstream dependencies; sub-skills in canonical sequences require compatibility verification at version bumps.

**Acceptance Criteria:**
Decision 1 text adds a qualifier: "Sub-skills in canonical cross-framework sequences (JTBD → Sprint, Lean UX → HEART) require cross-skill interface compatibility verification at major version bumps."

---

### DA-010: JTBD "Requires Actual User Interviews" Breaks Wave 1 Zero-Dependency Claim [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | `/ux-jtbd` sub-skill description; Decision 5: Wave 1 entry criteria |
| **Strategy Step** | Step 3 (Counter-argument lens: Contradicting Evidence) |

**Claim Challenged:**
> Wave 1 rationale: "No external user data or MCP required for core function."
> `/ux-jtbd` What humans do: "Conducts actual user interviews (irreducible -- AI cannot observe real behavior)."

**Counter-Argument:**
The Wave 1 framing promises "no external user data required." JTBD explicitly states that conducting actual user interviews is irreducible. These claims contradict each other. If you do not conduct user interviews, your JTBD job statements are AI-generated hypotheses at MEDIUM confidence -- which requires "expert review OR validation against 2-3 real user data points" before advancing. Wave 1 either requires user interviews (contradicting the zero-dependency claim) or produces only MEDIUM-confidence outputs that cannot advance to Wave 2 design activities without external validation.

**Dimension:** Internal Consistency

**Response Required:**
Reconcile the Wave 1 "zero external user data" claim with JTBD's user interview requirement. Either: clarify that JTBD *can* run without user interviews but produces MEDIUM-confidence output only, and the "zero-dependency" claim applies to MCP-only (not user-data) dependency; OR revise Wave 1 to "Low external dependency" and specify JTBD's minimum viable input (transcripts already available vs. new interviews required).

**Acceptance Criteria:**
Wave 1 description and JTBD sub-skill description are consistent about user interview dependency. "Zero-dependency" is defined to specify what it excludes (MCP, not user data).

---

### DA-011: Design Sprint 2-Person AI "Missing Participant" Adaptation Is Unsupported [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | `/ux-design-sprint` sub-skill description |
| **Strategy Step** | Step 3 (Counter-argument lens: Unstated Assumptions, Evidence Quality) |

**Claim Challenged:**
> "For 2-person teams, the sprint collapses to 1-2 days with the AI filling the 'missing participant' roles (note-taker, sketch generator, prototype builder). The facilitator and decision-maker roles remain human."

**Counter-Argument:**
Design Sprint 2.0 methodology (AJ&Smart) explicitly requires diverse perspectives in the decision-making phase. The Decider role (who makes the final call on Day 2) is supposed to be distinct from the Facilitator role, and the voting process during sketch review ("art museum" and dot voting) is designed to surface preference distribution across different stakeholders. With a 2-person team, the AI filling "missing participant" roles during voting essentially means the AI's aesthetic/strategic preferences influence the design direction -- which is exactly the kind of AI decision-making the architecture is supposed to prevent in its human-judgment boundary definitions.

**Dimension:** Evidence Quality

**Response Required:**
Clarify what "AI filling missing participant roles" means specifically for Day 2 decision-making. If AI is generating sketch variants but not voting on them, specify this. If the team is using AI to simulate diverse stakeholder perspectives, this should be flagged with a synthesis hypothesis warning equivalent to the ones applied in other sub-skills.

**Acceptance Criteria:**
Design Sprint 2-person adaptation specifies AI's role in Day 2 decision phases: does AI vote, generate variants only, or play a named advisory role? The human decision-making boundary for design direction is explicit.

---

### DA-012: V2 Trigger Conditions Have No Failure Mode Response [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | V2 Roadmap / V2 Candidates |
| **Strategy Step** | Step 3 (Counter-argument lens: Unaddressed Risks) |

**Claim Challenged:**
> "V2 planning begins when any 2 of these conditions are met in a single month: [4 demand/usage conditions]."

**Counter-Argument:**
The V2 trigger conditions are entirely demand-positive: they fire when usage grows, when more users need features, or when problems surface at scale. There is no trigger condition for V1 failure: zero adoption after 90 days, chronic MCP integration failures, or user feedback indicating the sub-skills are not producing actionable outputs for non-UX-specialist teams. Without a failure-mode trigger, there is no defined response if V1 achieves low adoption and the framework team needs to decide whether to invest in V2 or retire the skill.

**Dimension:** Actionability

**Response Required:**
Add at least one V1 failure trigger condition to the V2 Roadmap: e.g., "If V1 adoption is below the success metric floor (< 5 invocations in 90 days), conduct a user research review before V2 investment."

**Acceptance Criteria:**
V2 Roadmap includes at least one failure-mode trigger condition that defines a structured response (review, redesign, or retirement decision) if V1 fails to achieve adoption.

---

## Recommendations

### P0 (Critical -- MUST resolve before acceptance)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-001 | Add minimum domain knowledge specification per sub-skill OR narrow/reframe the target user definition with calibrated capability expectations | Per-sub-skill "Prerequisite Knowledge" entry OR revised target user segment definition with capability floor |
| DA-002 | Revise LOW/MEDIUM confidence enforcement language to accurately characterize behavioral vs. architectural scope OR specify a technical enforcement mechanism (forbidden_actions, output filtering) that prevents follow-up elicitation | Either honest language revision OR technical enforcement specification |

### P1 (Major -- SHOULD resolve; require justification if not)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-003 | Rename "Replaced By" column; add table subtitle clarifying structured methodology coverage vs. role replacement | Column renamed; hedge language incorporated before or into table header |
| DA-004 | Define bypass conditions for stalled waves; revise Wave 5 criteria if the 30+ users threshold is unreachable for core target segments | Bypass conditions explicitly defined; OR Wave 5 alternative entry path for pre-launch/bootstrapped teams |
| DA-005 | Add cost table footnotes: per-user billing, plan frequency, Hotjar bridge minimum cost, Claude API cost estimate | Footnotes added with billing unit and plan assumption clarity |
| DA-006 | Revise fallback descriptions to specify heuristic-level or capability-level gaps in screenshot-input mode | "Full coverage retained" replaced with accurate partial-coverage description per affected heuristic |
| DA-007 | Correct "immediately adoptable" Service Blueprinting claim; specify Enabler expiry conditions | Language revised to reflect V2 dependency; expiry condition specified |
| DA-008 | Add crisis mode triage criteria and qualification question; document MCP prerequisites for crisis path | At least one entry criterion or qualification question for crisis mode routing; MCP prerequisites documented |

### P2 (Minor -- MAY resolve; acknowledgment sufficient)

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| DA-009 | Add cross-skill interface compatibility caveat to Decision 1 independent versioning description | Qualifier sentence added to Decision 1 |
| DA-010 | Reconcile Wave 1 "zero-dependency" claim with JTBD user interview requirement | Consistent dependency description across Wave 1 rationale and JTBD sub-skill |
| DA-011 | Clarify AI's role in Design Sprint Day 2 decision-making for 2-person teams | Decision boundary specified for AI in sprint voting phases |
| DA-012 | Add V1 failure trigger to V2 Roadmap | At least one failure-mode trigger condition added |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | DA-007 (AI-First Design substitution gap), DA-009 (versioning compatibility omitted), DA-012 (failure mode response absent) collectively indicate structural coverage gaps in the proposal |
| Internal Consistency | 0.20 | Negative | DA-003 (Replaced By vs. capability coverage language conflict), DA-010 (Wave 1 zero-dependency vs. JTBD interview requirement) create internal contradictions that undermine the proposal's precision |
| Methodological Rigor | 0.20 | Negative | DA-001 (non-specialist premise), DA-002 (enforcement mechanism), and DA-008 (crisis mode entry criteria) target the architectural integrity of the core methodology -- the most significant dimension impact |
| Evidence Quality | 0.15 | Negative | DA-005 (cost tier understatement), DA-006 (fallback capability overstated) reduce evidentiary accuracy in the proposal's practical guidance sections |
| Actionability | 0.15 | Negative | DA-004 (wave gating practical unreachability), DA-008 (crisis mode ambiguity), DA-012 (failure response absent) reduce the proposal's actionability for the target user |
| Traceability | 0.10 | Neutral | Findings trace clearly to specific deliverable sections; no traceability gaps identified |

**Estimated composite score impact:** 2 Critical findings (Methodological Rigor, -0.15 to -0.20) + 6 Major findings (spread across Completeness, Consistency, Evidence Quality, Actionability, -0.05 to -0.08 per dimension) = estimated pre-revision ceiling of 0.72-0.78 on the 0.92 gate.

**Overall assessment:** REVISE. The deliverable has a sound architecture and thorough research backing, but two Critical findings (DA-001: non-specialist execution premise; DA-002: enforcement mechanism accuracy) undermine the proposal at its value proposition and safety mechanism level. Six Major findings are addressable in targeted revision. The Critical findings require either substantive reframing or credible technical specification before the proposal can be accepted.

---

## Execution Statistics
- **Total Findings:** 12
- **Critical:** 2 (DA-001, DA-002)
- **Major:** 6 (DA-003 through DA-008)
- **Minor:** 4 (DA-009 through DA-012)
- **Protocol Steps Completed:** 5 of 5

---

## H-15 Self-Review

- All findings have specific evidence from the deliverable (section references, direct quotes): Verified
- Severity classifications are justified (Critical = invalidates core claim/mechanism; Major = significant gap requiring revision; Minor = improvement opportunity): Verified
- Finding identifiers follow DA-NNN-{execution_id} format: Verified (DA-001-S002-PROJ020-20260303 through DA-012-S002-PROJ020-20260303)
- Summary table matches detailed findings: Verified (12 findings in both table and detailed sections)
- No findings minimized or omitted: Verified -- DA-011 (Design Sprint 2-person adaptation) was considered for Major elevation but retained as Minor because the core sprint methodology remains intact; the gap is in one edge case sub-scenario. DA-003 ("Replaced By" language) was considered for Critical elevation but retained as Major because the issue does include a hedge paragraph -- the problem is presentation order, not total omission.

---

*Strategy Execution Report generated by adv-executor per S-002 Devil's Advocate template.*
*Template: `.context/templates/adversarial/s-002-devils-advocate.md`*
*Execution ID: S002-PROJ020-20260303-iter1*
