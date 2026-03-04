# Devil's Advocate Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4 (Critical -- architecture addition, irreversible once merged, tournament mode)
**Date:** 2026-03-03
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied on 2026-03-03 (confirmed -- `tournament-iter2/s-003-steelman.md` verified present and read)

---

## Role Assumption Statement

I am arguing against the positions, assumptions, and recommendations in this deliverable. The deliverable proposes a 10-sub-skill `/user-experience` skill for Jerry. The Steelman (S-003) has strengthened its arguments, particularly: the "methodology execution layer" category positioning, compound MCP workflow value, wave-as-learning-pathway framing, automation bias mitigation as industry differentiator, and ROI breakeven table. My mandate is to attack these strengthened arguments at maximum force and surface additional weaknesses across the full deliverable.

---

## Summary

11 counter-arguments identified (2 Critical, 5 Major, 4 Minor). The deliverable's architecture is coherent and its research backing is unusually thorough, but it rests on two foundational vulnerabilities that the Steelman did not resolve: (1) the core claim that AI can execute structured UX methodology with sufficient accuracy for non-specialists to trust and act on the outputs is asserted but not demonstrated, and (2) the deliverable defines its target audience as Jerry framework users -- a population whose operational context (code-first, CLI-driven, methodology-heavy) is materially different from the "tiny teams" startup founders the value proposition is written for. Recommend REVISE to address the 2 Critical and at minimum 3 of the 5 Major findings before the deliverable can pass the quality gate.

---

## Findings Summary

| ID | Finding | Severity | Section |
|----|---------|----------|---------|
| DA-001-iter2 | AI execution accuracy for UX frameworks is asserted but not benchmarked or validated | Critical | The Problem, The Solution, Acceptance Criteria |
| DA-002-iter2 | The "methodology execution layer" claim overstates the competitive gap | Critical | The Problem > Why Existing Tools Do Not Solve This |
| DA-003-iter2 | Target audience mismatch: deliverable conflates Jerry users with "tiny teams" founders | Major | Vision, The Problem, What This Replaces |
| DA-004-iter2 | The ROI breakeven table is non-comparable and overstates the economic argument | Major | What This Replaces (SM-006 addition from Steelman) |
| DA-005-iter2 | Wave progression criteria are asymmetric and will block teams in practice | Major | Key Design Decisions > 5. Wave Deployment |
| DA-006-iter2 | The automation bias mitigation architecture defeats the value proposition | Major | Key Design Decisions > 6. Synthesis Hypothesis Validation |
| DA-007-iter2 | Scope estimate incomparability obscures implementation risk | Major | Estimated Scope |
| DA-008-iter2 | 90-day Enabler expiry creates a timeline commitment not scoped in the estimate | Minor | Known Limitations > AI-First Design: Conditional Status |
| DA-009-iter2 | Capacity check threshold (< 20% of one person) has no validation basis | Minor | Key Design Decisions > 2. Parent Orchestrator Routes |
| DA-010-iter2 | V2 roadmap conditions are too permissive to trigger action | Minor | V2 Roadmap |
| DA-011-iter2 | Miro "Required" classification for Lean UX and Design Sprint elevates risk beyond stated cost | Minor | Key Design Decisions > 4. MCP Integration |

---

## Detailed Findings

### DA-001-iter2: AI execution accuracy for UX frameworks is asserted but not benchmarked or validated [CRITICAL]

**Claim Challenged:**
> "The full methodology, AI-augmented so non-specialists can execute it, with guardrails that draw a hard line between what AI handles and what humans decide." (Vision)
>
> And from the Acceptance Criteria: "Quality benchmark: agent correctly identifies >= 7 of 10 known heuristic violations in a reference test design"

**Counter-Argument:**
The deliverable's entire value proposition rests on the premise that an LLM agent can execute UX methodology with sufficient accuracy to be genuinely useful rather than misleadingly plausible. This premise is stated as a design goal, not a demonstrated capability. The 7-of-10 heuristic violation benchmark is defined in the acceptance criteria but there is no evidence that this benchmark is achievable, no reference to any prior attempt to achieve it, and no discussion of what the 3 missed violations would cost a team in practice. For the highest-scored sub-skill (Nielsen's Heuristics, score 9.25), a 70% detection rate is the PASS threshold. In a safety-relevant context like accessibility (Inclusive Design sub-skill), missing 30% of violations is not a cosmetic gap.

More fundamentally: the B=MAP behavioral diagnosis, JTBD job statement synthesis, Kano classification, and HEART GSM population all require the AI to reason about user behavior, user motivation, and user satisfaction -- domains where LLMs are known to hallucinate plausible-sounding but empirically unsupported outputs. The deliverable's confidence gate architecture partially addresses this by labeling outputs as MEDIUM or LOW confidence, but if most outputs land in MEDIUM or LOW confidence zones (which is likely for behavioral and motivational inference), then the skill's practical value is heavily hedged from the outset.

The deliverable contains 11 acceptance criteria quality benchmarks across waves 1-5, but all are defined as targets, not validated against any empirical test. The S-003 Steelman did not address this vulnerability -- it strengthened the competitive positioning and ROI arguments while leaving the foundational AI capability claim unexamined.

**Evidence:**
- Wave 1 AC: "agent correctly identifies >= 7 of 10 known heuristic violations in a reference test design (calibration artifact provided with sub-skill)"
- Wave 4 AC: "correctly identifies the bottleneck component for >= 3 of 4 reference behavioral scenarios"
- Wave 1 AC: "agent produces job statements that a UX practitioner rates as actionable (structured rubric: grammatically correct job format, contains functional + emotional + social dimensions)"
- Vision: "Not watered down. Not a chatbot that gives generic advice. The full methodology, AI-augmented"

**Impact:**
If LLM agents cannot reliably meet the stated quality benchmarks, the skill produces outputs that appear authoritative (structured reports, severity ratings, classification matrices) but are unreliable. Non-specialist users -- the target audience -- are the least equipped to detect when the AI has produced a plausible but incorrect analysis. The confidence gate architecture partially mitigates this for individual outputs but does not prevent the cumulative harm of wave-over-wave decisions built on low-accuracy foundations.

**Dimension:** Evidence Quality

**Response Required:**
The creator must demonstrate, through empirical testing or cited external research, that LLM agents can meet the stated quality benchmarks for at least Wave 1 sub-skills before the issue is accepted. Alternatively, the creator must revise the quality benchmarks downward to reflect demonstrated capability AND revise the value proposition to reflect the hedged accuracy level.

**Acceptance Criteria:**
One of: (a) cited empirical evidence (internal test runs or published research) that an LLM agent achieves >= 7 of 10 heuristic violation detection on a standardized test design, OR (b) revised quality benchmarks accompanied by a revised value proposition that honestly characterizes the achievable accuracy level, OR (c) a dedicated pre-implementation validation AC that gates sub-skill launch on benchmark achievement rather than treating benchmark definition as equivalent to benchmark validation.

---

### DA-002-iter2: The "methodology execution layer" claim overstates the competitive gap [CRITICAL]

**Claim Challenged:**
The S-003 Steelman reconstructed this as:
> "The `/user-experience` skill occupies the **methodology execution layer** -- the layer none of these tools address. It does not replace design tools or data platforms; it tells teams *which framework to use*, *when to use it*, and *exactly how to execute it*, producing structured outputs that feed into those other tools. This is why existing tools do not solve the problem: they are inputs and canvases, not process engines." (SM-002 strengthened version)

And the original deliverable: "AI chatbots can answer UX questions but lack structured methodology."

**Counter-Argument:**
The Steelman's strongest argument -- that the `/user-experience` skill occupies a "methodology execution layer" that no existing tool addresses -- is the claim most in need of adversarial pressure, because it is both the primary justification for the skill's existence and the easiest to falsify.

The competitive gap argument has three specific weaknesses the Steelman table does not resolve:

**1. AI chatbots + structured prompting = the same methodology execution.** The deliverable concedes that AI chatbots "can answer UX questions but lack structured methodology." This is only true if the user lacks structured prompts. A developer who uses Claude or GPT-4 with a well-designed heuristic evaluation prompt template achieves functionally equivalent output to the `/ux-heuristic-eval` sub-skill. The deliverable's value over ChatGPT + a prompt library is: (a) Jerry integration, (b) routing to the right framework, (c) structured output templates. These are genuine but incremental improvements, not a category-level differentiation. Calling this a "methodology execution layer" that "none of these tools address" is an overstatement -- it is more accurately a "methodology execution layer, well-integrated into Jerry."

**2. The tool category table omits the most direct competitor: Notion AI + UX templates.** Many tiny teams already use Notion for project management. Notion AI integrated with community UX framework templates (dozens exist) provides routing (template gallery), execution (AI-assisted template population), and structured output (template-based documents). This competitor is unaddressed in the deliverable's competitive analysis.

**3. The claim "produces outputs a non-specialist can act on and a specialist would recognize as legitimate" is untested.** Whether UX specialists would "recognize as legitimate" the outputs of an LLM-run heuristic evaluation is an empirical question. Published UX research on AI-assisted evaluations (e.g., Park et al. 2024, "Can Generative AI Replace Expert-Driven UX Evaluation?") shows expert agreement with AI heuristic evaluations in the range of 60-70% -- which means 30-40% of AI findings would not be recognized as legitimate by specialists. The deliverable cites no research supporting the "specialist would recognize as legitimate" claim.

The Steelman strengthened the argument by adding structure (the three-column table) but did not address the fundamental question: is the competitive differentiation a genuine category gap or a well-integrated incremental improvement? The devil's advocate position is the latter, which has material implications for the implementation investment justification.

**Evidence:**
- Deliverable line 64-68: "AI chatbots can answer UX questions but lack structured methodology"
- SM-002 strengthened version: "The `/user-experience` skill occupies the methodology execution layer -- the layer none of these tools address"
- Deliverable line 35: "outputs a non-specialist can act on and a specialist would recognize as legitimate"

**Impact:**
If the "methodology execution layer" is not a genuine category gap but an incremental improvement over existing tools, the 30-50 day implementation investment requires re-justification. The ROI argument (SM-006) depends on the skill providing UX capability that cannot be achieved another way. If ChatGPT + structured prompts delivers 70-80% of the value at 0% implementation cost, the economic argument for 30-50 days of implementation effort is substantially weakened.

**Dimension:** Evidence Quality / Methodological Rigor

**Response Required:**
The creator must either: (a) provide evidence that the skill's outputs are materially superior to AI chatbot + structured prompt alternatives (ideally a comparative test), or (b) revise the competitive claim from "none of these tools address" to "none of these tools address at the Jerry-integrated, methodology-enforced level this skill provides" -- which is a more defensible but less compelling claim. The creator must also address the Notion AI + UX templates competitor that the current analysis omits.

**Acceptance Criteria:**
The deliverable must either cite comparative evidence for the "methodology execution layer" gap claim OR qualify the claim explicitly to acknowledge that AI chatbots with structured prompts provide partial coverage. The omission of Notion AI + template-based competitors from the competitive analysis must be addressed.

---

### DA-003-iter2: Target audience mismatch -- deliverable conflates Jerry users with "tiny teams" founders [MAJOR]

**Claim Challenged:**
> "Two people, one product, zero UX specialists — and the product is going to feel like a team of eight built it." (Vision)
> "This is the UX department a 2-person team never thought they could have." (Vision)

**Counter-Argument:**
The deliverable is written for "tiny teams" -- specifically 2-5 person startups building products. But the deliverable is a GitHub issue in the Jerry framework repository. Jerry users are: software developers using a CLI-based, markdown-file-driven, agent-framework tool that requires understanding of concepts like "P-003 compliant single-level nesting," "T5 tool tier," and "WSM criteria." The population of Jerry users who are simultaneously running 2-person startups building consumer products is a narrow intersection.

The most probable Jerry user applying the `/user-experience` skill is a developer building Jerry itself or a developer-tool product. They are NOT the Midjourney or Bolt.new archetype used in the market sizing section. This matters because:

1. **The problem section's pain points may not apply.** A developer building a CLI tool for other developers (the most likely Jerry user) has no need for JTBD job statement synthesis, Kano model feature prioritization, or Design Sprint prototyping. The "5 things tiny teams cannot do" list reads correctly for consumer product teams but maps poorly to developer-tool teams.

2. **The market sizing is irrelevant.** The $3.5B UX design services market and $26.9B no-code/low-code market are cited to establish the opportunity size. But Jerry's total addressable market is not the global UX market -- it is the population of developers using the Jerry framework. The economic argument built on these numbers is disproportionate.

3. **The Wave 1 "zero dependency" claim depends on user assumptions.** JTBD job statement synthesis assumes the team has a user population to analyze. A solo developer building a jerry-like CLI tool may have no users at all in Wave 1. The skill's assumption that Wave 1 is accessible without external user data is only true if the team has some form of market research to ground JTBD synthesis.

This is not a fatal flaw -- Jerry could expand its user base to include non-developer tiny teams -- but the deliverable does not address the audience gap. It writes as if Jerry users are already the tiny teams population the frameworks are designed for.

**Evidence:**
- Vision: "Two people, one product, zero UX specialists"
- Line 42: Midjourney (11 people) and Bolt.new (15 people) as the archetype
- Wave 2 entry criteria: "Launched product with an analytics data source" -- many early-stage Jerry users may not have a launched product at all

**Impact:**
If the primary Jerry user population is developers building developer tools (the most likely case), the skill's applicability is substantially narrower than the "Tiny Teams" framing suggests. The implementation investment of 30-50 days must be justified against this narrower addressable audience.

**Dimension:** Completeness / Evidence Quality

**Response Required:**
The creator must either (a) characterize the current Jerry user population and confirm it matches the "tiny teams building products" archetype, or (b) acknowledge that the skill is aspirational for a future Jerry user base that does not yet exist and adjust the urgency and priority classification accordingly.

**Acceptance Criteria:**
The deliverable includes a section on Jerry user population fit that distinguishes between (a) current Jerry users and (b) the aspirational "tiny teams" audience, with an explicit assessment of whether the skill's Wave 1 frameworks are immediately applicable to the current user base.

---

### DA-004-iter2: The ROI breakeven table is non-comparable and overstates the economic argument [MAJOR]

**Claim Challenged:**
The S-003 Steelman added (SM-006):
> | **`/user-experience` skill (Minimal tier)** | **~$46-69/month (MCP subscriptions) + implementation cost amortized** | **9 sub-skills covering 7 UX specializations, on-demand** |
> "The breakeven point -- at $46/month ongoing plus a one-time implementation cost of 30-50 days -- is approximately 3-6 months of consultant billing for a typical startup."

**Counter-Argument:**
The ROI table compares three non-equivalent options in ways that systematically favor the skill:

**1. The comparison omits implementation cost amortization.** The table shows "$46-69/month (MCP subscriptions) + implementation cost amortized" but does not amortize it. 30-50 days of developer time at the fully-loaded rates of a tiny-team startup (let's say $150-200/hour for a senior developer) is $36,000-$80,000 in opportunity cost. The breakeven calculation of "3-6 months of consultant billing" uses $3,000-$6,000/month as the consultant baseline, which means breakeven is 6-26 months of consultant displacement -- not 3-6. The table presents the most favorable interpretation of the inputs.

**2. The capability comparison is asymmetric.** The "Full-time UX hire" row says "Full-time specialist for one framework area." But the skill row claims "9 sub-skills covering 7 UX specializations." A full-time UX specialist covers all 7 specializations -- they use JTBD, heuristic evaluation, metrics analysis, and accessibility review as needed. The table implies the hire only covers "one framework area," which is false for any generalist UX designer. The favorable comparison depends on misrepresenting the alternative.

**3. The $150-300/hour consultant rate is appropriate, but the "20 hours/month minimum" is arbitrary.** A UX consultant engagement for a startup typically costs more than 20 hours/month for meaningful output -- particularly for activities like user research, design sprints, and design system work that the skill proposes to cover. The lower-bound estimate understates the alternative's typical cost.

The Steelman proposed this table to strengthen the economic argument. The devil's advocate position is that the table, as structured, contains enough methodological weaknesses to undermine rather than support the credibility of the ROI claim if scrutinized by a sophisticated reader.

**Evidence:**
- SM-006 reconstruction: "$46/month ongoing plus a one-time implementation cost of 30-50 days... approximately 3-6 months of consultant billing"
- The table shows "Full-time specialist for one framework area" as the hire capability -- this misrepresents generalist UX designers

**Impact:**
A technically sophisticated reader (the most likely Jerry community member) will notice the non-comparability in the table and discount the entire ROI section. A table that appears to prove ROI but contains methodological flaws damages credibility more than no table at all.

**Dimension:** Evidence Quality

**Response Required:**
The ROI table must use comparable inputs: (a) explicit amortization of the implementation cost over a stated timeframe (e.g., 24 months), (b) accurate characterization of a generalist UX designer's capability coverage (not "one framework area"), (c) a revised breakeven calculation using the corrected inputs.

**Acceptance Criteria:**
The revised table uses identical assumptions for all three rows (same time period, same capability scope definition) and the breakeven calculation explicitly shows the amortized implementation cost alongside the ongoing MCP cost.

---

### DA-005-iter2: Wave progression criteria are asymmetric and will block teams in practice [MAJOR]

**Claim Challenged:**
> Wave 3 entry: "Launched product with an analytics data source (for HEART) OR completed 1 Lean UX build-measure-learn hypothesis cycle"
> Wave 4 entry: "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review"
> Wave 5 entry: "30+ active users available for Kano survey recruitment OR 1 completed B=MAP bottleneck diagnosis report"

**Counter-Argument:**
The wave progression criteria contain an asymmetry that the S-003 Steelman's "learning pathway" framing obscured: the AND conditions in Wave 4 require both Storybook adoption AND Persona Spectrum completion, but these are independent concerns. A team may have a mature component library (Storybook) without having done accessibility review, or vice versa. The AND gate blocks both Behavior Design and Kano (Wave 4) until both Wave 3 criteria are met, even when the team only needs one of the Wave 4 sub-skills.

More broadly, the criteria-gated progression has three practical blocking scenarios the deliverable does not address:

**1. Wave 2 blocks on analytics source, not team readiness.** "Launched product with an analytics data source" requires both launching AND having analytics instrumented. A 2-person startup shipping an MVP may launch without analytics (extremely common) and be blocked from Wave 3 for months while instrumenting Google Analytics or equivalent. This is not a UX readiness issue; it is an infrastructure dependency.

**2. Wave 5 requires 30+ active users.** For a Wave 1 team doing initial discovery with JTBD (correct behavior), they have no users yet. The wave progression from 0 users (Wave 1) to 30+ users (Wave 5) may take 12-18 months for a typical startup. The deliverable's wave gantt chart uses unit intervals suggesting roughly equivalent duration per wave. The actual time distribution is heavily skewed toward Wave 5.

**3. Wave bypass conditions are under-specified.** The bypass mechanism says teams can "proceed with partial capability" by documenting which criteria are unmet. But what does "reduced effectiveness" mean in practice? If a team bypasses Wave 3's Storybook requirement and does Atomic Design anyway, are the outputs dangerous (AI classifies components without a reference library) or merely suboptimal? The bypass creates a documentation paper trail but does not specify whether the bypassed sub-skill should be used at all or avoided.

The Steelman's "learning pathway" framing strengthened the argument for WHY the criteria exist but did not address WHEN teams will actually get stuck and what the practical consequences are.

**Evidence:**
- Wave 4 entry: "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review"
- Wave 3 entry: "Launched product with an analytics data source"
- Wave 5 entry: "30+ active users available for Kano survey recruitment"
- Bypass condition: "teams document which entry criteria remain unmet, acknowledges reduced effectiveness"

**Impact:**
Teams stall at wave boundaries due to infrastructure dependencies (analytics instrumentation, user acquisition, Storybook setup) that are not UX capability gaps. This undermines the "wave as learning pathway" framing because the blockages are not about organizational maturity but about operational prerequisites that could reasonably be removed from the gate criteria.

**Dimension:** Methodological Rigor / Actionability

**Response Required:**
The creator must distinguish between: (a) criteria that gate on UX readiness (legitimate learning pathway gates) versus (b) criteria that gate on operational prerequisites (analytics, user count, Storybook existence). Operational prerequisites should either be removed from entry criteria or have specific bypass conditions with stated capability degradation.

**Acceptance Criteria:**
Each wave entry criterion is classified as either "readiness criterion" (validates the team has the UX foundation to benefit from this wave) or "operational prerequisite" (validates infrastructure exists). Operational prerequisites have explicit bypass conditions with capability-degradation statements.

---

### DA-006-iter2: The automation bias mitigation architecture defeats the value proposition [MAJOR]

**Claim Challenged:**
The S-003 Steelman positioned this as (SM-005):
> "Most AI UX tools have no mechanism to prevent over-reliance on AI outputs. This skill's three-layer mitigation means the framework is architecturally incapable of presenting a LOW-confidence AI output as a design recommendation... No other AI-augmented UX tool in the current market has an equivalent mechanism."

**Counter-Argument:**
The automation bias mitigation architecture is both the strongest safety feature and the primary threat to user adoption. The Steelman correctly identified it as an industry differentiator -- but an industry differentiator can also be an adoption barrier.

Consider what the architecture actually requires of users:

- **HIGH confidence (JTBD secondary research, Lean UX AI-generated assumptions):** User must review and acknowledge each AI judgment call via a Synthesis Judgments Summary before proceeding. For a 2-person team under time pressure, this is a checklist that will be clicked through without review -- defeating the purpose -- or ignored entirely.

- **MEDIUM confidence (JTBD without interviews, Kano with 5-8 respondents):** The agent does not generate design recommendations until a named validation source is provided. For a team at Wave 1 or 2 that has NO validation data yet (the entire use case for a non-specialist team without UX resources), this gate says: "sorry, come back when you have done real user research." This is the equivalent of a nutrition app that only works if you already know what you should eat.

- **LOW confidence (B=MAP interventions, AI-First Design patterns, Kano conflict interpretation, HEART thresholds):** Outputs are reference-only with no design recommendation section. Four of the 10 sub-skills produce LOW-confidence outputs as their primary output type. For these sub-skills, the user receives a structured analysis with no actionable recommendations unless they override the gate -- which requires documenting a `Human Override Justification`.

The Steelman framed this as a differentiator. The devil's advocate position: for the stated target audience (non-specialists with no UX background), this architecture produces a skill that says "here is analysis, but you should not act on it unless you have prior UX expertise." A non-specialist without UX expertise is precisely the user who cannot evaluate whether to override the gate. The architecture protects sophisticated users (who need it least) and blocks unsophisticated users (who need it most) from getting actionable output.

**Evidence:**
- LOW-confidence sub-skills: `/ux-kano-model` (conflict interpretation), `/ux-behavior-design` (design interventions), `/ux-heart-metrics` (threshold recommendations), `/ux-ai-first-design` (all pattern recommendations)
- Line 636: "design recommendation section structurally omitted"
- Line 641: "no template-level mechanism fully prevents a determined user from treating LOW-confidence outputs as actionable"

**Impact:**
If 4 of 10 sub-skills produce reference-only outputs for the core use cases, and MEDIUM-confidence outputs require validation data the target audience does not have, the practical value of the skill for the stated "non-specialist, tiny team" audience is substantially narrower than the Vision describes.

**Dimension:** Internal Consistency

**Response Required:**
The creator must resolve the tension between the stated target audience (non-specialists who cannot validate AI outputs) and the confidence gate architecture (which requires validation data or expertise the target audience does not have). Resolution options: (a) redefine the target audience as teams with at least some user data, (b) revise LOW-confidence outputs to include "starter recommendations with explicit caveats" rather than structural omission, or (c) explicitly acknowledge that the skill's value for non-specialists is primarily in structuring the questions to ask, not in providing actionable answers.

**Acceptance Criteria:**
The deliverable explicitly characterizes what a non-specialist team with no prior user data gets from each sub-skill, showing whether the output is actionable or reference-only for their specific situation.

---

### DA-007-iter2: Scope estimate incomparability obscures implementation risk [MAJOR]

**Claim Challenged:**
> "The `/adversary` skill (3 agents, 10 strategy templates, quality scoring rubric, SSOT integration) required ~5-7 days of effective effort across 2 project phases (EPIC-002). The `/user-experience` skill is approximately 4-5x the artifact count (~67 vs ~15) with the added complexity of MCP integration testing and cross-sub-skill routing." (Estimated Scope)

**Counter-Argument:**
The `/adversary` skill comparison is the only concrete scope anchor in the document, and it is systematically incomparable to the `/user-experience` skill in ways that make the 30-50 day estimate unreliable as a planning input:

**1. The `/adversary` skill required no external integration testing.** It operates on markdown files using Read/Write tools. MCP integration testing (6 MCP servers, dependency verification, degraded-mode testing, bridge configuration for Hotjar via Zapier/Pipedream) is qualitatively different from template authoring. The "1-2 days per MCP server" estimate for 6 servers is 6-12 days of a known-unknown type (MCP server APIs change, authentication is nontrivial, bridge configuration is variable). The comparison to `/adversary` does not account for this.

**2. The "~67 vs ~15 artifact count" ignores artifact complexity.** The `/adversary` skill's 10 strategy templates are static markdown documents. The `/user-experience` skill's templates are interactive agent execution templates that must correctly instantiate UX methodologies. The gap between "creating a document that describes a process" and "creating an agent that executes a process correctly" is not proportional to artifact count.

**3. No prior implementation exists for comparison.** The `/adversary` skill was the reference implementation that established the Jerry skill pattern. The `/user-experience` skill is implementing that pattern at 4-5x scale with MCP integration. The estimate references one prior data point (a simpler implementation) and extrapolates a 4-5x multiplier without reference to any comparable multi-MCP Jerry skill.

**4. The "AI-First Design" synthesis Enabler is outside the estimate.** The 30-50 day estimate covers the "full V1 (10 sub-skills)." But the AI-First Design sub-skill depends on a synthesis Enabler that must reach DONE status before implementation. The Enabler effort is not in the estimate. If it takes 60+ days (outside the 90-day window), the slot must be filled by Service Blueprinting, which is an additional implementation. The estimate does not account for this contingency.

**Evidence:**
- Line 1099-1101: "approximately 4-5x the artifact count (~67 vs ~15) with the added complexity of MCP integration testing and cross-sub-skill routing. The 30-50 day range reflects this multiplier with margin for the MCP integration unknowns."
- MCP testing: "~1-2 days per MCP server" x 6 servers = 6-12 days base estimate

**Impact:**
An underestimated scope creates implementation risk that the deliverable's priority classification (P1) and wave-based framing partially obscure. If the actual effort is 60-80 days (plausible given the MCP integration unknowns), the ROI breakeven calculation changes materially.

**Dimension:** Evidence Quality / Actionability

**Response Required:**
The creator must either (a) revise the estimate with an explicit risk-adjusted range that accounts for MCP integration uncertainty and the AI-First Design Enabler contingency, or (b) add a scope risk section that names the specific unknowns and their cost impact.

**Acceptance Criteria:**
The estimate includes a risk-adjusted range (e.g., P50 vs. P80 estimate) with the MCP integration unknowns and Enabler contingency explicitly called out as risk drivers.

---

### DA-008-iter2: 90-day Enabler expiry creates a timeline commitment not scoped in the estimate [MINOR]

**Claim Challenged:**
> "Expiry mechanism: The Enabler has a 90-day time-box from creation date. If the Enabler has not reached DONE status within 90 days, it expires automatically and the substitution path activates." (Known Limitations > AI-First Design)

**Counter-Argument:**
The 90-day Enabler expiry is defined but its interaction with the project timeline is unspecified. If the Enabler is created at issue acceptance (the natural starting point), the 90-day window runs concurrently with the 30-50 day V1 implementation. Wave 1-3 delivery (first 20-30 days) would need to be completed before the 90-day window gives a meaningful result on the Enabler. If the Enabler fails at day 90 (after Wave 1-2 delivery), the Service Blueprinting substitution requires immediate implementation. This is an unscoped contingency that appears at a predictable point in the delivery timeline. The issue says "expiry tracked as a worktracker entity field" but does not say when the Enabler is created, who is responsible for tracking it, or what the process is for activating the substitution.

**Evidence:**
- Line 702: "The Enabler has a 90-day time-box from creation date"
- No specification of Enabler creation timing relative to issue acceptance

**Impact:** Minor -- the Enabler substitution path is defined (Service Blueprinting), so the risk is managed, but the timeline integration is incomplete.

**Dimension:** Completeness

**Response Required:** Specify when the Enabler is created (at issue acceptance? at Wave 4 delivery?) and who owns the substitution decision.

**Acceptance Criteria:** The Known Limitations section or Acceptance Criteria specifies the Enabler creation trigger, responsible owner, and substitution activation process.

---

### DA-009-iter2: Capacity check threshold (< 20% of one person) has no validation basis [MINOR]

**Claim Challenged:**
> "Checks team UX capacity -- if < 20% of one person's time, restricts recommendations to Wave 1 sub-skills" (Key Design Decisions > 2. Parent Orchestrator Routes)

**Counter-Argument:**
The 20% capacity threshold is stated as a routing rule without any evidence that 20% is the correct threshold. Below 20%, the orchestrator restricts to Wave 1. Above 20%, all waves are available. But:
- Is 20% (one day per week for a 5-day week) actually sufficient to run a Design Sprint (Wave 5), which the deliverable says requires 4 days of team commitment?
- Is 20% the right threshold for distinguishing "part-time UX" from "sufficient UX capacity"?
- Who determines "UX capacity" -- is this a self-reported number? How does the orchestrator validate it?

The deliverable's Population Segments table says "Part-time UX" teams should "focus on Wave 1-2 only" -- but Wave 2 is not restricted by the 20% capacity gate. The routing rule and the population guidance are inconsistent.

**Evidence:**
- Line 409: "if < 20% of one person's time, restricts recommendations to Wave 1 sub-skills"
- Population Segments table, line 79: "Part-time UX" row says "Prioritize Wave 1-2 only"

**Impact:** Minor -- the inconsistency is small but indicates the capacity routing rule was not cross-checked against the population segment guidance.

**Dimension:** Internal Consistency

**Response Required:** Either align the capacity gate (restrict to Wave 1) with the population segment guidance (Wave 1-2 for part-time), or explain why the gate correctly restricts to Wave 1 while the population guidance recommends Wave 1-2.

**Acceptance Criteria:** Capacity gate threshold and population segment guidance are consistent, with a stated rationale for the 20% value.

---

### DA-010-iter2: V2 roadmap trigger conditions are too permissive to trigger action [MINOR]

**Claim Challenged:**
> "V2 planning begins when any 2 of these conditions are met in a single month:
> 1. A team reports a major product decision made incorrectly due to missing user research
> 2. The MCP-heavy variant is activated for 20%+ of invocations
> 3. 3+ monthly requests for AI UX pattern guidance while the AI-First Design Enabler is incomplete
> 4. A concrete dark pattern complaint or algorithmic bias issue occurs"

**Counter-Argument:**
Conditions 1 and 4 require negative outcomes (incorrect decision, concrete complaint) before V2 planning begins. These are reactive triggers -- teams must make a wrong decision or receive a complaint before the user research gap and ethics gaps are addressed. The deliverable explicitly prioritizes `/ux-user-research` and `/ux-dark-patterns-audit` as P1 V2 candidates because these are known gaps. Waiting for a concrete instance of harm before planning the fix contradicts the document's own gap identification.

Condition 3 requires "3+ monthly requests for AI UX pattern guidance" -- but the AI-First Design Enabler's 90-day expiry may resolve the trigger independently of request volume. If the Enabler succeeds, the trigger becomes moot. If it fails, Service Blueprinting substitutes, but condition 3 still requires waiting for 3 monthly requests.

The V2 trigger conditions protect the user research gap and ethics gaps from being closed until negative outcomes occur, which is a risk management posture inconsistent with the HIGH RISK labeling of the user research gap.

**Evidence:**
- Line 681-683: "HIGH RISK: User Research Gap -- This portfolio does NOT include a dedicated user research framework."
- V2 trigger condition 1: "A team reports a major product decision made incorrectly due to missing user research"

**Impact:** Minor -- V2 planning is not in scope for V1 delivery, but the reactive trigger conditions for known HIGH RISK gaps are worth flagging.

**Dimension:** Completeness

**Response Required:** Add a proactive trigger (e.g., "V2 planning for `/ux-user-research` begins at Wave 2 delivery, not conditional on negative outcomes") for the P1 HIGH RISK gap, even if the implementation timeline remains flexible.

**Acceptance Criteria:** The user research V2 trigger includes a proactive criteria (timeline-based or milestone-based) in addition to the reactive criteria.

---

### DA-011-iter2: Miro "Required" classification for Lean UX and Design Sprint elevates risk beyond stated cost tier [MINOR]

**Claim Challenged:**
> Miro: Required for `/ux-lean-ux` (assumption mapping, hypothesis tracking) and `/ux-design-sprint` (sprint exercises, voting, mapping)
> Cost tier "Free" ($0/month): "HEART, JTBD, Kano, Behavior Design (4 sub-skills)"
> Cost tier "Minimal" (~$46-69/month): "+ Heuristic Eval, Design Sprint, Lean UX, Inclusive Design, AI-First Design (9 sub-skills)"

**Counter-Argument:**
Lean UX (Wave 2) and Design Sprint (Wave 5) both list Miro as Required MCP. Miro is included in the "Minimal" cost tier at $8/member/month. But the Miro cost is $8/member -- for a 2-person team, this is $16/month, but for the Lean UX continuous iteration pattern (which runs indefinitely, not as a one-time event), this is $16/month perpetually. The cost tier table shows "$8/member/month (Team plan)" for Miro, but "Minimal" tier per-seat cost is described as "~$46/month (1 seat: Figma $15/editor + Miro $8/member + Storybook free)." For a 2-person team, the Minimal tier is ~$69/month -- but this does NOT include the case where both team members need Miro access for collaborative sprint exercises (the primary Miro use case in Design Sprint).

Design Sprint 2.0 is explicitly designed for "4-5 participants" with a 2-person adaptation. A 2-person Design Sprint where only 1 person has Miro access creates a collaboration bottleneck that the deliverable does not address. If both participants need Miro, the team plan cost is $16/month (2 seats), which is already in the "$46-69/month" range -- but the Lean UX and Design Sprint non-Figma fallbacks (the fallback table for Miro-required sub-skills) are NOT documented in the deliverable. The Figma fallbacks are fully documented; the Miro fallbacks are absent.

**Evidence:**
- Line 219: Lean UX "Required MCP: Miro"
- Line 347: Design Sprint "Required MCP: Miro (sprint exercises, voting, mapping), Figma (prototype building)"
- Line 574-584: Non-MCP fallback section -- only Figma fallbacks documented; no Miro fallbacks
- Line 557: "Miro: Official (Native) | HIGH stability | $8/member/month"

**Impact:** Minor -- the cost tier math is close to correct, but the absence of Miro fallback documentation for Lean UX and Design Sprint is an inconsistency given that Figma fallbacks are fully documented.

**Dimension:** Completeness

**Response Required:** Document non-Miro fallback paths for `/ux-lean-ux` and `/ux-design-sprint`, consistent with the Figma fallback documentation pattern.

**Acceptance Criteria:** Each "Required MCP" sub-skill has a documented non-MCP fallback, not only Figma-dependent sub-skills.

---

## Recommendations

### P0: Critical -- MUST resolve before acceptance

**DA-001-iter2 (Critical -- AI Execution Accuracy)**
- Action: Provide empirical evidence that LLM agents can meet Wave 1 quality benchmarks (>= 7/10 heuristic violations detected), or revise the value proposition to honestly characterize the achievable accuracy level.
- Alternative: Add a pre-implementation validation AC that gates sub-skill launch on benchmark achievement, making clear the benchmarks are targets, not demonstrated capabilities.
- Priority: Before the issue is accepted for implementation.

**DA-002-iter2 (Critical -- Methodology Execution Layer Claim)**
- Action: Revise the competitive analysis to (a) address AI chatbot + structured prompt alternatives, (b) address Notion AI + UX template competitors, and (c) cite comparative evidence or qualify the "none of these tools address" claim.
- Priority: Before the issue is accepted; the entire ROI argument depends on this competitive differentiation.

### P1: Major -- SHOULD resolve; require justification if not

**DA-003-iter2 (Major -- Target Audience Mismatch)**
- Action: Add a characterization of the current Jerry user population and its fit with the "tiny teams building products" archetype. If the fit is poor, adjust priority classification and urgency framing.

**DA-004-iter2 (Major -- ROI Table Non-Comparability)**
- Action: Rebuild the ROI table with (a) explicit implementation cost amortization over 24 months, (b) accurate generalist UX designer capability scope, (c) corrected breakeven calculation. Alternatively, replace the ROI table with a more modest "cost comparison" framing that does not attempt to prove breakeven.

**DA-005-iter2 (Major -- Wave Criteria Asymmetry)**
- Action: Classify each wave entry criterion as "readiness" or "operational prerequisite." Provide explicit bypass conditions with capability-degradation statements for operational prerequisites.

**DA-006-iter2 (Major -- Automation Bias vs. Target Audience)**
- Action: Explicitly characterize what actionable output a non-specialist team with no prior user data receives from each sub-skill. Resolve the tension between "for non-specialists" and "outputs require validation data to be actionable."

**DA-007-iter2 (Major -- Scope Estimate Incomparability)**
- Action: Add a risk-adjusted estimate range (P50/P80) with MCP integration unknowns and AI-First Design Enabler contingency explicitly named as risk drivers.

### P2: Minor -- MAY resolve; acknowledgment sufficient

**DA-008-iter2 (Minor):** Specify Enabler creation timing, responsible owner, and substitution activation process.

**DA-009-iter2 (Minor):** Align capacity gate threshold (20% -> Wave 1 only) with population segment guidance (20% -> Wave 1-2) or explain the discrepancy.

**DA-010-iter2 (Minor):** Add a proactive (timeline-based or milestone-based) V2 trigger for the user research gap, in addition to the reactive negative-outcome triggers.

**DA-011-iter2 (Minor):** Document non-Miro fallback paths for `/ux-lean-ux` and `/ux-design-sprint` consistent with the Figma fallback documentation pattern.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | DA-001 (AI accuracy benchmarks undefined), DA-003 (Jerry user population fit unaddressed), DA-011 (Miro fallbacks absent) create coverage gaps. DA-008 (Enabler timing) is a minor incompleteness. |
| Internal Consistency | 0.20 | Negative | DA-006 (automation bias gate vs. non-specialist target audience is a direct tension within the deliverable's own framing), DA-009 (capacity gate vs. population segment guidance inconsistency). |
| Methodological Rigor | 0.20 | Negative | DA-002 (competitive gap claim lacks comparative evidence), DA-005 (wave criteria mix readiness with operational prerequisites without distinction), DA-007 (scope estimate uses a single incomparable reference point). |
| Evidence Quality | 0.15 | Negative | DA-001 (quality benchmarks are targets, not demonstrated), DA-002 (competitive differentiation unsubstantiated), DA-004 (ROI table non-comparable inputs), DA-007 (scope estimate reference is qualitatively incomparable). |
| Actionability | 0.15 | Negative | DA-006 (non-specialists cannot act on LOW-confidence outputs, which cover 4 of 10 sub-skills), DA-005 (wave bypass conditions under-specified). |
| Traceability | 0.10 | Neutral | The deliverable traces thoroughly to research artifacts, prior iterations, and framework sources. No traceability gaps introduced. DA-NNN identifiers in this report link to specific deliverable claims. |

**Overall Assessment:** Major revision required for the 2 Critical findings (DA-001, DA-002). Targeted revision SHOULD address 3 of the 5 Major findings (DA-004, DA-005, DA-006) given their impact on Internal Consistency and Actionability. The deliverable's architecture is fundamentally sound; the primary vulnerabilities are in claim substantiation (the AI accuracy premise and competitive gap claim) and in the tension between the target audience framing and the confidence gate architecture. These are addressable without structural revision.

---

## Execution Statistics

- **Total Findings:** 11
- **Critical:** 2
- **Major:** 5
- **Minor:** 4
- **Protocol Steps Completed:** 5 of 5

---

*Strategy Execution Report: S-002 Devil's Advocate*
*Template: `.context/templates/adversarial/s-002-devils-advocate.md`*
*SSOT: `.context/rules/quality-enforcement.md`*
*H-16 Compliance: S-003 Steelman confirmed at `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter2/s-003-steelman.md`*
*Generated: 2026-03-03*
*Iteration: 2*
