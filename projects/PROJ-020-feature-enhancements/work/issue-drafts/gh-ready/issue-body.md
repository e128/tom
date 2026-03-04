# feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams


## Document Sections

| Section | Purpose |
|---------|---------|
| [Vision](#vision) | Skill mission and design philosophy |
| [The Problem](#the-problem) | Tiny teams UX capability gap and population segments |
| [The Solution](#the-solution) | Parent orchestrator, 10 sub-skills, detailed descriptions |
| [Key Design Decisions](#key-design-decisions) | Framework-per-skill, routing, P-003 compliance, MCP integration, wave deployment, synthesis validation |
| [Tiny Teams Capability Map](#tiny-teams-capability-map) | Capability coverage mapping to traditional UX roles |
| [Known Limitations](#known-limitations) | User research gap, AI-First conditional status, ethics gaps, Figma SPOF, context window |
| [Acceptance Criteria](#acceptance-criteria) | Parent orchestrator, wave sub-skills, synthesis validation, quality standards, wave progression |
| [V2 Roadmap](#v2-roadmap) | V2 candidates, architecture evolution path |
| [Research Backing](#research-backing) | Phase 1-3 artifacts, adversarial validation |
| [Relationship to Existing Jerry Skills](#relationship-to-existing-jerry-skills) | Integration with problem-solving, adversary, worktracker, orchestration, nasa-se, diataxis |
| [Framework Selection Scores](#framework-selection-scores) | Validated WSM scores for all 10 frameworks |
| [Directory Structure](#directory-structure) | Implementation file layout (11 skill directories, ~72 artifacts) |
| [Estimated Scope](#estimated-scope) | Effort estimates with comparable delivery reference |
| [Sub-Skill SKILL.md Descriptions (Draft)](#sub-skill-skillmd-descriptions-draft) | Draft SKILL.md description fields per H-26 |
| [Sub-Skill Model Selection](#sub-skill-model-selection) | Model selection rationale per AD-M-009 |
| [Sub-Skill Output Levels](#sub-skill-output-levels) | L0/L1/L2 output level specification per AD-M-004 |
| [Cross-Session State](#cross-session-state) | Memory-Keeper specification per MCP-002 |
| [References](#references) | Source artifact locations |

---

## Vision

Two people, one product, zero UX specialists — and the product is going to feel like a team of eight built it.

The `/user-experience` skill is a parent orchestrator backed by 10 independently evolvable sub-skills covering the full product lifecycle from discovery through post-launch measurement. Each sub-skill implements a single proven UX framework as its own Jerry skill — registered independently, versioned independently, loaded on-demand. The orchestrator reads the product stage and the team's need, then drops the developer into the right framework.

This is the UX department a 2-person team never thought they could have. Built on frameworks battle-tested across thousands of products over the past three decades. Not watered down. Not a chatbot that gives generic advice. The full methodology, AI-augmented so non-specialists can execute it (with confidence-gated output depth -- HIGH-confidence sub-skills produce full recommendations; MEDIUM produce guided analysis requiring validation; LOW produce reference summaries requiring specialist interpretation), with guardrails that draw a hard line between what AI handles and what humans decide.

The boldest line on the mountain is the one nobody thought was skiable. This is that line for tiny teams and UX.

---

## The Problem

### Tiny Teams Cannot Afford UX -- And It Shows

Gartner's 2026 Strategic Technology Trends report identifies "Tiny Teams" -- teams of 2-5 people augmented by AI replacing department-scale staffing across software development -- as a top trend (source: [Gartner Top Strategic Technology Trends 2026](https://www.gartner.com/en/articles/top-technology-trends-2026), published January 2026). Companies like Midjourney (11 people, reported $200M ARR per [The Information, August 2023](https://www.theinformation.com/articles/midjourney-generates-over-200-million-in-revenue)) and Bolt.new (15 people, reported $20M in 60 days per [StackBlitz blog, December 2024](https://blog.stackblitz.com/posts/bolt-new-20m-60-days/)) demonstrate that AI-augmented tiny teams can deliver results previously requiring 50+ people.

There is a glaring gap in this trend: **UX capability**.  While precise market sizing for "tiny teams needing UX capability" does not exist as a tracked segment, the adjacent indicators are substantial: the global UX design services market was valued at $3.5B in 2023 (Grand View Research) and the no-code/low-code market enabling non-specialist development reached $26.9B in 2023 (Gartner). The intersection -- teams who can build products without specialists but cannot design them well -- represents a meaningful and growing population.

A 2-person startup can use AI to write code, generate tests, create documentation, and manage infrastructure. What they cannot do:

- **Discover what to build.** Without structured user research methodology, teams build what they assume users want. Jobs-to-be-Done and Kano Model provide the frameworks for this -- but only if someone on the team knows how to apply them.

- **Evaluate what they have built.** Without heuristic evaluation or usability testing, teams ship designs with preventable usability problems. Nielsen's 10 Heuristics have been the gold standard for 30 years -- but a developer who has never heard of them cannot apply them.

- **Measure whether their UX works.** Without structured metrics (HEART, Fogg Behavior Model), teams rely on gut feel to assess UX quality. They know something is wrong but cannot diagnose what or why.

- **Build accessible products.** Without inclusive design methodology, teams build for themselves and miss the estimated 16% of the global population with disabilities (source: [WHO Global Report on Health Equity for Persons with Disabilities, December 2022](https://www.who.int/publications/i/item/9789240063600); the commonly cited 15-20% range reflects WHO's 2011 World Report on Disability estimate of 15% updated by the 2022 report's 1.3 billion figure), plus the situational impairments that affect everyone.

- **Build consistent products.** Without component architecture (Atomic Design), teams create one-off UI elements that diverge over time, increasing maintenance cost and degrading user experience.

The result: tiny teams ship fast but ship poorly. They iterate on code but not on experience. They optimize for features but not for usability. The products work -- technically -- but they do not work well for the humans who use them.

That is the equivalent of standing at the top of a line you scouted from every angle, strapped in with the best gear on the market, and then skiing it with your eyes closed. The mountain is there. The capability is there. You just need the methodology to see it.

### Why Existing Tools Do Not Solve This

- **Design tools** (Figma, Sketch) provide the canvas but not the methodology. Knowing how to use Figma does not mean knowing when to run a heuristic evaluation or how to structure a design sprint.
- **UX books and courses** provide the knowledge but not the execution. A developer who reads "Don't Make Me Think" understands the principles but still cannot run a structured JTBD analysis.
- **AI chatbots and AI-augmented tools** provide partial coverage. Tools like Notion AI (2M+ users, structured workflows and templates) and general-purpose AI assistants can answer UX questions and offer template-based guidance. Combined with structured prompt templates, they provide a meaningful starting point. However, no existing tool combines structured UX methodology with adversarial quality gates, constitutional compliance enforcement, synthesis hypothesis confidence gating, and MCP design tool integration into a single coordinated workflow. The gap is not "AI cannot help with UX" -- it is that existing AI UX assistance is disconnected from the structured frameworks, quality enforcement, and tool integrations that make methodology outputs trustworthy and actionable.

The missing piece is the **middle layer**: structured, AI-guided workflows that take proven UX frameworks and make them executable by non-specialists, with guardrails about what AI can and cannot do, quality gates that enforce rigor, and design tool integrations that connect methodology to execution.

### Who This Is For: Tiny Teams Population Segments

The 2026 Tiny Teams trend encompasses distinct population segments with different needs:

| Segment | Team Size | Characteristics | Portfolio Fit |
|---------|----------|-----------------|---------------|
| **Solo practitioner** | 1 | No collaboration overhead; all roles in one person; time is the binding constraint | HIGH for Waves 1-3 (all sub-skills usable by one person); Wave 4 data-collection prerequisites (HEART metric data, B=MAP behavioral data) may require external data sources; Wave 5 Design Sprint adapts to 1-2 day solo sprint but is optional for this segment |
| **Dev+Designer pair** | 2 | Minimal coordination; complementary skills; one person typically drives UX | HIGH -- portfolio's "pair review" patterns (Nielsen's, Lean UX hypothesis validation) map directly |
| **Small cross-functional team** | 3-5 | Enough for role separation; can run a full Design Sprint; manageable coordination | HIGH -- primary optimization target; all sub-skills operate at full design intent |
| **Part-time UX** | 2-5 (one part-time) | UX is a part-time responsibility; depth is limited; frameworks must be low-ceremony | HIGH -- primary design target; Waves 1-2 calibrated for 20-50% allocation; Waves 3-5 aspirational. Note: Portfolio Fit upgraded from MEDIUM (analysis SSOT in `ux-framework-selection.md`) to HIGH based on tournament finding SM-001-I5: Part-time UX is the primary design target segment, and Waves 1-2 are explicitly calibrated for 20-50% allocation. The analysis SSOT retains the original MEDIUM as the pre-calibration baseline. |

Population segments (Solo Practitioner, Part-time UX, Dedicated UX) define the range of teams this skill serves. Part-time UX (20-50% allocation) is the most common segment (inferred from Gartner 2026 Tiny Teams trend characterization -- direct UX allocation measurement not available from this source).  Each wave's entry criteria and time estimates are calibrated for this median case.

Teams in the "part-time UX" segment should treat wave progression beyond Wave 2 as aspirational and focus on the zero-MCP-cost sub-skills (HEART, JTBD, Kano, Behavior Design). Wave 1 requires zero MCP tool cost. Wave 2 MCP cost depends on Miro usage -- Lean UX requires Miro (free tier available; paid Starter tier $8/user/month for advanced features), while HEART has no required MCP.

**Wave 1 time-to-first-value:** Wave 1 timeline includes ~1-2 hours KICKOFF setup (team profile, product context, tooling verification). Total time-to-first-value: KICKOFF (~2 hours) + first sub-skill session (2-4 hours) = initial findings within one working day. A team completing the kickoff-signoff and running their first Nielsen Heuristic Evaluation sub-skill should reach initial findings within a single work session (estimated 2-4 hours post-KICKOFF). Wave 1 completion (both Heuristic Eval and JTBD sub-skills operational, first outputs produced) is estimated at 8-13 days including KICKOFF, based on the comparable delivery reference in [Estimated Scope](#estimated-scope). This estimate will be validated during pre-launch testing.

---

## The Solution

### A Parent Orchestrator with 10 Pluggable Sub-Skills

The `/user-experience` skill uses a **hybrid parent orchestrator + pluggable sub-skills** architecture. Each UX framework is a self-contained Jerry skill that can be independently registered, versioned, and evolved.

The orchestrator knows the terrain; the 10 sub-skills are the gear. You carry what the mountain demands.

```mermaid
graph TD
    UE["/user-experience<br/>(Parent Orchestrator)<br/>ux-orchestrator agent (T5)"]

    subgraph "Wave 1 -- Zero-Dependency"
        HE["/ux-heuristic-eval<br/>Nielsen's 10 Heuristics"]
        JT["/ux-jtbd<br/>Jobs-to-be-Done"]
    end

    subgraph "Wave 2 -- Data-Ready"
        LU["/ux-lean-ux<br/>Lean UX"]
        HR["/ux-heart-metrics<br/>HEART Framework"]
    end

    subgraph "Wave 3 -- Design System"
        AD["/ux-atomic-design<br/>Atomic Design"]
        ID["/ux-inclusive-design<br/>Microsoft Inclusive Design"]
    end

    subgraph "Wave 4 -- Advanced Analytics"
        BD["/ux-behavior-design<br/>Fogg Behavior Model"]
        KM["/ux-kano-model<br/>Kano Model"]
    end

    subgraph "Wave 5 -- Process Intensives"
        DS["/ux-design-sprint<br/>Design Sprint 2.0"]
        AF["/ux-ai-first-design<br/>AI-First Design (CONDITIONAL)"]
    end

    UE --> HE
    UE --> JT
    UE --> LU
    UE --> HR
    UE --> AD
    UE --> ID
    UE --> BD
    UE --> KM
    UE --> DS
    UE --> AF

    style UE fill:#4A90D9,color:#fff
    style AF fill:#E8A838,color:#000
```

### The 10 Sub-Skills

Each sub-skill implements a single, proven UX framework. Together they cover the full product lifecycle. Below is a summary table followed by detailed descriptions of each sub-skill.

#### Summary Table

| # | Sub-Skill | Framework | Lifecycle Stage | Cognitive Mode | Tool Tier | Wave | Score |
|---|-----------|-----------|----------------|----------------|-----------|------|-------|
| 1 | `/ux-heuristic-eval` | Nielsen's 10 Heuristics | During Design | Systematic | T3 | 1 | 9.05 |
| 2 | `/ux-jtbd` | Jobs-to-be-Done | Before Design | Divergent | T3 | 1 | 8.05 |
| 3 | `/ux-lean-ux` | Lean UX | During Design | Systematic | T3 | 2 | 8.25 |
| 4 | `/ux-heart-metrics` | HEART Framework | After Launch | Systematic | T2 | 2 | 8.30 |
| 5 | `/ux-atomic-design` | Atomic Design | While Building | Systematic | T3 | 3 | 8.55 |
| 6 | `/ux-inclusive-design` | Microsoft Inclusive Design | While Building | Systematic | T3 | 3 | 8.00 |
| 7 | `/ux-behavior-design` | Fogg Behavior Model | After Launch | Convergent | T2 | 4 | 7.60 |
| 8 | `/ux-kano-model` | Kano Model | Before Design | Convergent | T2 | 4 | 7.65 |
| 9 | `/ux-design-sprint` | Design Sprint 2.0 | During Design | Systematic | T3 | 5 | 8.65 |
| 10 | `/ux-ai-first-design` | AI-First Design | AI Products | Divergent | T3 | 5 (COND) | 7.80 (P) |

#### Detailed Sub-Skill Descriptions

> **Ordering note:** Sub-skill descriptions below are ordered by Wave deployment sequence (Wave 1 first), not by WSM selection rank. Wave deployment order differs from WSM rank because it optimizes for dependency satisfaction and learning curve -- high-WSM frameworks that depend on Wave 1 outputs deploy in later waves. For WSM rank ordering, see the [Framework Selection Scores](#framework-selection-scores) section.

---

#### 1. `/ux-heuristic-eval` -- Nielsen's 10 Usability Heuristics

**Rank #1 | Score: 9.05 | Wave 1**

The most universally applicable UX evaluation framework in existence. Thirty years of validation across thousands of products. The 10-heuristic checklist maps to a systematic agent that evaluates a design artifact (screenshot, wireframe, prototype URL) against each heuristic and produces a structured findings report with severity ratings. This is the steepest, most proven line on the mountain -- and the first one you should ski.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-heuristic-evaluator` |
| Cognitive Mode | Systematic (10 discrete heuristics, scored findings list) |
| Tool Tier | T3 (external access for Figma) |
| Required MCP | Figma (design file reading, frame extraction) |
| Enhancement MCP | Storybook (component-level heuristic checks) |
| Time to Complete | ~30-35 minutes with AI assistance (design target) |

**What AI does:** Evaluates designs against all 10 Nielsen heuristics; assigns severity ratings (0-4 scale) per violation; generates structured findings report with fix recommendations; cross-references findings against platform conventions.

**What humans do:** Provides platform-specific context (mobile vs. web vs. desktop conventions); triages findings by business priority (not all severity-4 violations are worth fixing immediately); makes the final fix-or-accept decision; reviews contextual heuristics (H4: Consistency, H7: Flexibility) that require domain knowledge.

**Non-MCP fallback:** Screenshot-input mode. User provides design screenshots as image inputs. Reduced automation but full heuristic coverage retained.

---

#### 2. `/ux-jtbd` -- Jobs-to-be-Done

**Rank #6 | Score: 8.05 | Wave 1**

Before you build anything, figure out what problem you are actually solving. JTBD discovers the "jobs" users hire products to do. Based on Clayton Christensen's framework with Intercom's JTBD Playbook adaptations for product teams.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-jtbd-analyst` |
| Cognitive Mode | Divergent (explores broadly to discover user jobs) |
| Tool Tier | T3 |
| Required MCP | None |
| Enhancement MCP | Miro (visual job mapping) |
| Key Output | Job statement synthesis, switch interview guide, competitive job analysis |

**What AI does:** Synthesizes job statements from interview transcripts and secondary research; generates competitive job analysis showing how users currently hire alternative solutions; maps job-to-feature relationships; creates switch interview guides for user research validation.

**What humans do:** Conducts actual user interviews (irreducible -- AI cannot observe real behavior); judges hypothesis validity against their knowledge of the user population; decides which job to pursue (strategic product decision); validates that AI-generated job statements resonate with observed user language.

**Synthesis hypothesis warning:** Job statements generated from secondary research are MEDIUM confidence. They require named validation sources before feeding into Design Sprint challenge statements.

---

#### 3. `/ux-lean-ux` -- Lean UX

**Rank #5 | Score: 8.25 | Wave 2**

Build-measure-learn, on repeat. Lean UX iterates on hypotheses continuously through structured cycles. Based on Jeff Gothelf's Lean UX with adaptations for AI-augmented hypothesis generation.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-lean-ux-facilitator` |
| Cognitive Mode | Systematic (hypothesis cycle is a repeatable process) |
| Tool Tier | T3 |
| Required MCP | Miro (assumption mapping, hypothesis tracking) |
| Enhancement MCP | Figma (MVP prototyping), Hotjar (experiment analytics via bridge) |
| Key Output | Assumption map, hypothesis backlog, experiment design, validation report |

**What AI does:** Generates assumption maps categorizing team beliefs by risk and uncertainty; creates hypothesis backlogs in structured format ("We believe [assumption]. We will know we are right when [measurable signal]."); builds MVPs from hypothesis specifications; tracks experiment results against hypothesis predictions.

**What humans do:** Identifies which assumptions are riskiest (requires product judgment about what matters); judges whether hypothesis results validate or invalidate the assumption; decides what to learn next; determines when to pivot vs. persevere.

---

#### 4. `/ux-heart-metrics` -- HEART Framework (Google)

**Rank #4 | Score: 8.30 | Wave 2**

You shipped the product. Now measure whether it actually works for humans. Google's HEART framework -- Happiness, Engagement, Adoption, Retention, Task Success -- translates abstract UX goals into concrete, measurable signals and metrics.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-heart-analyst` |
| Cognitive Mode | Systematic (GSM template population is procedural) |
| Tool Tier | T2 (no external MCP required for core function) |
| Required MCP | None |
| Enhancement MCP | Analytics API (data ingestion), Hotjar (behavioral data via bridge) |
| Key Output | HEART GSM (Goals-Signals-Metrics) populated template, metric dashboard specification, anomaly detection report |

**What AI does:** Populates HEART GSM templates from analytics data; generates metric definitions with measurement methods; creates dashboard specifications; detects metric anomalies and trends; generates comparison reports across time periods.

**What humans do:** Selects which HEART dimensions matter most for their product (not all 5 are equally relevant); interprets metric trends in business context; identifies confounding factors (seasonality, marketing campaigns, etc.); makes product decisions based on metric data.

**Synthesis hypothesis warning:** Metric threshold recommendations (e.g., "Adoption rate should exceed 30%") are LOW confidence. They are reference benchmarks drawn from training data, not targets calibrated to the team's specific product and user base. Threshold selection requires domain-specific judgment.

---

#### 5. `/ux-atomic-design` -- Atomic Design (Brad Frost)

**Rank #3 | Score: 8.55 | Wave 3**

Components that compose. Brad Frost's atoms-molecules-organisms-templates-pages hierarchy structures component libraries for reuse. The most AI-automatable design system framework in the portfolio due to its rule-based classification system.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-atomic-architect` |
| Cognitive Mode | Systematic (classification hierarchy is rule-based) |
| Tool Tier | T3 |
| Required MCP | Storybook (component library evaluation, story management) |
| Enhancement MCP | Zeroheight (design system documentation), Figma (visual component extraction) |
| Key Output | Component inventory, atomic classification, composition recommendations, documentation |

**What AI does:** Discovers existing components from Storybook; classifies components into atomic hierarchy levels; composes new Organisms from existing Atoms and Molecules; generates component documentation; detects inconsistencies (duplicate components, naming violations, unused atoms); recommends consolidation opportunities.

**What humans do:** Defines component boundaries (when an Atom becomes a Molecule is a design judgment); validates classifications against brand standards and design language; decides on component API surface (props, variants, composability rules); reviews documentation for accuracy.

---

#### 6. `/ux-inclusive-design` -- Microsoft Inclusive Design

**Rank #7 | Score: 8.00 | Wave 3**

Build for everyone. Microsoft's Recognize-Learn-Build exclusion methodology and Persona Spectrum approach goes beyond WCAG compliance to address situational and temporary impairments. An estimated 16% of the global population has a disability (WHO, 2022). Situational impairments affect the rest. Inclusive design catches both.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-inclusive-evaluator` |
| Cognitive Mode | Systematic (checklist evaluation against exclusion categories) |
| Tool Tier | T3 |
| Required MCP | Figma (design evaluation, contrast analysis) |
| Enhancement MCP | Storybook (component-level accessibility), Context7 (WCAG reference docs) |
| Key Output | Persona Spectrum analysis, WCAG 2.2 compliance report, exclusion audit, remediation recommendations |

**What AI does:** Evaluates contrast ratios, text sizing, touch targets against WCAG 2.2 criteria; applies Persona Spectrum analysis to identify permanent, temporary, and situational exclusions; generates compliance reports with specific remediation steps; checks color-blind accessibility; evaluates keyboard navigation paths.

**What humans do:** Provides user population context (which disability types are prevalent in their user base); validates accommodations for non-standard populations (cultural, linguistic, cognitive); prioritizes remediation by impact; reviews Persona Spectrum customizations for accuracy.

---

#### 7. `/ux-behavior-design` -- Fogg Behavior Model

**Rank #10 | Score: 7.60 | Wave 4**

Users are not doing the thing. Why? Fogg's B=MAP equation -- Behavior = Motivation x Ability x Prompt -- diagnoses the bottleneck. The only behavioral diagnostic framework in the portfolio.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-behavior-diagnostician` |
| Cognitive Mode | Convergent (narrows from behavioral data to bottleneck diagnosis) |
| Tool Tier | T2 |
| Required MCP | None |
| Enhancement MCP | Miro (behavior mapping), Hotjar (behavioral recording data via bridge) |
| Key Output | B=MAP bottleneck diagnosis, Reference Intervention Patterns (non-prescriptive), motivation-ability profile |


**What AI does:** Diagnoses which component of B=MAP is the bottleneck (motivation too low? ability too hard? prompt missing or mistimed?); generates Reference Intervention Patterns (non-prescriptive) matched to the bottleneck type -- these are cataloged pattern options, not design recommendations; maps motivation-ability profiles for key user actions; tracks intervention effectiveness.

**What humans do:** Provides behavioral context (why users might have low motivation -- often requires product/market knowledge); validates bottleneck diagnosis against their observation of user behavior; selects intervention approach (there are multiple valid interventions for each bottleneck type); decides which user actions to analyze.

**Synthesis hypothesis warning:** Reference Intervention Patterns are MEDIUM confidence. They require expert review (see [Synthesis Hypothesis Validation](#key-design-decisions) for expert qualification: minimum 2 years UX practice, non-team-member) OR validation against 2-3 real user data points before use in design decisions. The agent generates cataloged intervention patterns, not prescriptive design recommendations.

---

#### 8. `/ux-kano-model` -- Kano Model

**Rank #9 | Score: 7.65 | Wave 4**

Not all features are created equal. Noriaki Kano's three-category model classifies them: Must-Be (expected), Performance (proportional satisfaction), and Attractive (delighters). The difference between a feature that prevents churn and a feature that drives word-of-mouth. Requires user survey data.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-kano-analyst` |
| Cognitive Mode | Convergent (narrows from survey data to priority classification) |
| Tool Tier | T2 |
| Required MCP | None |
| Enhancement MCP | Miro (feature mapping visualization) |
| Key Output | Kano classification matrix, feature priority recommendations, satisfaction coefficients |

**What AI does:** Processes Kano survey responses (functional/dysfunctional question pairs); classifies features into Must-Be, Performance, Attractive, Indifferent, Reverse categories; generates feature priority matrices with satisfaction coefficients; detects classification conflicts within the data; produces visual priority maps.

**What humans do:** Designs the survey questions (feature descriptions must be user-facing, not technical); recruits survey respondents (minimum 30 for statistical reliability); interprets classification results in business context (a "Must-Be" feature that is technically expensive still requires strategic judgment); makes build/defer/cut decisions.

**Synthesis hypothesis warning:** Directional classifications from 5-8 respondents are MEDIUM confidence. Feature priority conflict interpretations are LOW confidence (reference-only).

---

#### 9. `/ux-design-sprint` -- Design Sprint 2.0

**Rank #2 | Score: 8.65 | Wave 5**

Four days. Problem statement to validated prototype. AJ&Smart's Design Sprint 2.0, evolved from the original Google Ventures methodology. The highest-ceremony, highest-impact framework in the portfolio — the one that takes commitment and pays back in spades.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-sprint-facilitator` |
| Cognitive Mode | Systematic (4-day structured process with defined daily outputs) |
| Tool Tier | T3 |
| Required MCP | Miro (sprint exercises, voting, mapping), Figma (prototype building) |
| Enhancement MCP | Whimsical (flowchart alternatives) |
| Key Output | Challenge statement, solution sketches, interactive prototype, Day 4 test findings |

**What AI does:** Design Sprint aims to generate multiple sketch variants during Day 2 ideation and facilitate Figma prototype construction during Day 3 (exact output volume depends on LLM capability at implementation time; acceptance criteria will validate against 2-person team workflow benchmarks during Wave 5 implementation); creates interview guides for Day 4 testing; themes Day 4 interview data into patterns; manages sprint exercise templates (Lightning Demos, How Might We notes, Solution Sketches).

**What humans do:** Sets design direction and challenge statement (Day 1); selects from AI-generated sketch variants (Day 2 decision-making); reviews and refines prototype fidelity (Day 3); conducts user interviews (Day 4 -- irreducible human contact); makes strategic pivot/persevere decisions based on test results.

**Team size adaptation:** Design Sprint 2.0 is designed for 4-5 participants. For 2-person teams, the sprint collapses to 1-2 days with the AI filling the "missing participant" roles (note-taker, sketch generator, prototype builder). The facilitator and decision-maker roles remain human.

**Part-time time commitment:** Wave 5 (Design Sprint) requires dedicated UX time commitment beyond the part-time median case. Teams operating at < 20% UX time allocation may choose to defer Wave 5 or adapt the 5-day sprint to a 2-week part-time format. Wave 5 is optional -- Waves 1-4 deliver substantial UX capability without it.

---

#### 10. `/ux-ai-first-design` -- AI-First Design (SYNTHESIZED)

**Rank #8 | Score: 7.80 (Projected) | Wave 5 (CONDITIONAL)**

When AI is the product, the UX rules change. This sub-skill applies AI-specific interaction patterns -- conversational, agentic, augmentative, autonomous -- for products where AI is the core experience. This is a **synthesized framework** -- it must be created by this project before implementation. No established framework exists at the methodology level required.

| Attribute | Value |
|-----------|-------|
| Agent | `ux-ai-design-guide` |
| Cognitive Mode | Divergent (explores emerging AI interaction patterns) |
| Tool Tier | T3 |
| Required MCP | Figma (AI interface evaluation) |
| Enhancement MCP | Storybook (AI component patterns), Context7 (AI UX research) |
| Key Output | AI interaction specification, trust calibration report, explanation pattern map |

**What AI does:** Generates AI interaction pattern recommendations (conversational, agentic, augmentative, autonomous modes); evaluates trust calibration (does the UI accurately convey AI confidence and limitations?); maps explanation patterns (when and how to explain AI decisions to users); reviews error handling UX for AI failures.

**What humans do:** Provides product context (what type of AI interactions does the product have?); validates AI interaction pattern appropriateness for their user population; decides on explanation depth (how much should the AI explain itself?); reviews trust calibration against actual AI capability.

**Conditional status:**

- **Blocking prerequisite:** A synthesis Enabler must reach DONE status with a verified WSM score >= 8.00. Independent reviewer sign-off required on WSM scoring for Enabler validation. Independent reviewer = any Jerry Framework user who did NOT author the sub-skill under review (i.e., the person scoring the Enabler cannot be the person who built it, and must not have contributed to its design or implementation)
- **Expiry:** 90-day time-box from Enabler creation; auto-substitution on expiry
- **Substitution path:** If the AI-First Design Enabler has not achieved its validation gate by Wave 5, Wave 5 delivers Design Sprint only; Service Blueprinting is a V2 P1 candidate
- **Interim path:** The parent orchestrator routes AI product UX requests to `/ux-heuristic-eval` with supplemental PAIR Guidebook heuristics until the Enabler completes

**Synthesis hypothesis warning:** All AI interaction pattern recommendations are LOW confidence. This is an emerging domain without the 10+ years of validation that frameworks like Nielsen's Heuristics or JTBD have.

---

## Key Design Decisions

Every decision here was a deliberate line choice. No shortcuts, no "we'll figure it out later."

### 1. Each Framework = Its Own Skill

Sub-skills can be registered independently in CLAUDE.md and AGENTS.md. A team using only Nielsen's Heuristics and Lean UX does not load the other 8 sub-skills into context, preserving the Jerry progressive disclosure budget (PR-004 three-tier loading model per `agent-development-standards.md`).

This means:
- **Independent versioning.** When a better metrics framework than HEART emerges, only `/ux-heart-metrics` is updated.
- **Independent evolution.** New frameworks (V2 additions like Service Blueprinting) are added as new sub-skills without modifying existing ones.
- **Context budget preservation.** Only the parent skill description is loaded at session start (Tier 1 metadata per `agent-development-standards.md` progressive disclosure, ~500 tokens). Sub-skills are loaded on-demand via Task tool invocation (Tier 2 core).

Only the parent loads at session start — sub-skills load when you actually need them.

### 2. Parent Orchestrator Routes via Lifecycle-Stage Triage

Only `/user-experience` is registered in `mandatory-skill-usage.md`. The parent orchestrator:

1. **Onboards with a HIGH RISK warning** about the user research gap (first invocation per session)
2. **Checks team UX capacity** -- if < 20% of one person's time, gates routing to Wave 1 sub-skills only (advisory; user can override per P-020)
3. **Routes by product stage:**
   - "Before design" requests go to JTBD or Kano
   - "During design" requests go to Design Sprint, Lean UX, or Heuristic Eval
   - "While building" requests go to Atomic Design or Inclusive Design
   - "After launch" requests go to HEART or Behavior Design
   - "AI product" requests go to AI-First Design (if Enabler complete) or interim heuristic path
4. **Handles crisis mode** -- emergency 3-skill sequence (Heuristic Eval -> Behavior Design -> HEART) for products with urgent UX problems. Selection rationale: Heuristic Eval identifies *what* is wrong (design-level violations), Behavior Design diagnoses *why* users are not completing desired actions (B=MAP bottleneck), HEART measures the *impact* (quantified UX health). This sequence covers diagnose-explain-measure in the minimum sub-skill count. Crisis mode activates when the user explicitly describes urgency ("urgent", "critical UX issue", "users are leaving") or when the orchestrator detects multiple prior sub-skill invocations without resolution.

Users who know the specific sub-skill they need can invoke it directly (e.g., `/ux-heuristic-eval`) to bypass the triage. Direct invocation still checks wave prerequisites: when `WAVE-{N-1}-SIGNOFF.md` does not exist, BOTH orchestrator routing AND direct sub-skill invocation return BLOCK (denial + signoff completion instructions). Direct invocation bypass of a BLOCK state requires the same 3-field documented justification as any other P-020 override (named data source, specific supporting data point, validation date). Enforcement is declared co-equal in `ux-routing-rules.md` -- the sub-skill and orchestrator apply identical prerequisite checks with identical outcomes.

**Routing triage flowchart:**

```mermaid
flowchart TD
    Start["User invokes /user-experience"]
    Onboard["Display HIGH RISK<br/>user research warning"]
    Cap{"UX capacity<br/>< 20% of 1 person?"}
    MCP{"MCP-heavy<br/>team?"}
    Stage{"What product stage?"}

    PreA["Before design:<br/>Don't know what to build"]
    PreB["Before design:<br/>Need to prioritize features"]
    DesA["During design:<br/>Need validated prototype"]
    DesB["During design:<br/>Iterating on existing design"]
    DesC["During design:<br/>Building component system"]
    DesD["During design:<br/>Building AI product"]
    PostA["After launch:<br/>Measure UX health"]
    PostB["After launch:<br/>Users not completing action"]
    Acc["Any stage:<br/>Check accessibility"]
    Crisis["CRISIS:<br/>Urgent UX problems"]

    Start --> Onboard --> Cap
    Cap -->|Yes| WaveLimit["Recommend Wave 1 only"]
    Cap -->|No| MCP
    WaveLimit --> MCP
    MCP -->|Yes| MCPVariant["Apply MCP-heavy<br/>variant recommendations"]
    MCP -->|No| Stage
    MCPVariant --> Stage

    Stage --> PreA --> JTBD["/ux-jtbd"]
    Stage --> PreB --> Kano["/ux-kano-model"]
    Stage --> DesA --> Sprint["/ux-design-sprint"]
    Stage --> DesB --> LeanHeur["/ux-lean-ux or<br/>/ux-heuristic-eval"]
    Stage --> DesC --> Atomic["/ux-atomic-design"]
    Stage --> DesD --> AIFirst{"/ux-ai-first-design<br/>Enabler DONE?"}
    Stage --> PostA --> Heart["/ux-heart-metrics"]
    Stage --> PostB --> Behav["/ux-behavior-design"]
    Stage --> Acc --> Incl["/ux-inclusive-design"]
    Stage --> Crisis --> Seq["3-skill emergency:<br/>Heuristic --> Behavior --> HEART"]

    AIFirst -->|Yes| AFSkill["/ux-ai-first-design"]
    AIFirst -->|No| Interim["Interim: /ux-heuristic-eval<br/>+ PAIR Guidebook heuristics"]
```

**Common intent resolution:**

| User Says | Routes To | Qualification Question |
|-----------|----------|----------------------|
| "Improve my UX" / "Make this more usable" | Heuristic Eval (existing design) or Design Sprint (no design yet) | "Do you have an existing design?" |
| "Fix a specific UX problem" | Behavior Design (behavioral) or Heuristic Eval (design-level) | "Is the problem about user behavior or design quality?" |
| "Decide what to build" | JTBD (strategic) or Kano (prioritize known features) | "Are you defining the problem or prioritizing features?" |
| "Measure whether UX is working" | HEART Metrics | No qualification needed |
| "Make this accessible" | Inclusive Design | Provide user context brief |
| "Set up our design system" | Atomic Design | Provide Storybook reference |
| "We have an AI product" | AI-First Design (if Enabler done) or Heuristic Eval + PAIR | Check Enabler status |
| "CRISIS: urgent UX problems" | Emergency 3-skill sequence | No qualification needed |

### 3. P-003 Compliant Single-Level Nesting

The architecture strictly enforces Jerry's single-level nesting constraint:

```
MAIN CONTEXT (orchestrator)
    |
    +-- ux-orchestrator (T5, has Task tool)
           |
           +-- ux-heuristic-evaluator (T3, NO Task tool)
           +-- ux-jtbd-analyst (T3, NO Task tool)
           +-- ux-lean-ux-facilitator (T3, NO Task tool)
           +-- ...etc
```

- The parent orchestrator (`ux-orchestrator`) is the only T5 agent with Task tool access.
- All sub-skill agents are T2-T3 and cannot spawn further sub-agents.
- Workers return results to the orchestrator, which coordinates cross-framework integration.

### 4. MCP Integration (Figma, Miro, Storybook, Zeroheight + Bridge Tools)

This is the most MCP-dependent skill in the Jerry framework. Six MCP servers mapped to 10 sub-skills. Full integration diagram:

```mermaid
graph LR
    subgraph "MCP Servers"
        Figma["Figma MCP<br/>(Official)"]
        Miro["Miro MCP<br/>(Official)"]
        SB["Storybook MCP<br/>(Official Addon)"]
        ZH["Zeroheight MCP<br/>(Official)"]
        HJ["Hotjar<br/>(Bridge via Zapier)"]
        Whim["Whimsical<br/>(Community)"]
    end

    subgraph "Sub-Skills"
        HE["/ux-heuristic-eval"]
        DS["/ux-design-sprint"]
        AD["/ux-atomic-design"]
        LU["/ux-lean-ux"]
        ID["/ux-inclusive-design"]
        AF["/ux-ai-first-design"]
        HR["/ux-heart-metrics"]
        BD["/ux-behavior-design"]
        JT["/ux-jtbd"]
        KM["/ux-kano-model"]
    end

    Figma ==>|Required| HE
    Figma ==>|Required| DS
    Figma ==>|Required| ID
    Figma ==>|Required| AF
    Figma -.->|Enhancement| AD
    Figma -.->|Enhancement| LU

    Miro ==>|Required| DS
    Miro ==>|Required| LU
    Miro -.->|Enhancement| JT
    Miro -.->|Enhancement| BD
    Miro -.->|Enhancement| KM

    SB ==>|Required| AD
    SB -.->|Enhancement| HE
    SB -.->|Enhancement| ID
    SB -.->|Enhancement| AF

    ZH -.->|Enhancement| AD

    HJ -.->|Enhancement| HR
    HJ -.->|Enhancement| LU
    HJ -.->|Enhancement| BD

    Whim -.->|Enhancement| DS
```

**Legend:** Solid arrows (==>) = Required MCP (degraded mode + explicit error on failure). Dashed arrows (-.>) = Enhancement MCP (cosmetic limitation on failure).

**MCP Server Classification:**

| MCP Server | Type | Stability | Cost | Notes |
|-----------|------|-----------|------|-------|
| **Figma** | Official (Native) | HIGH -- official Figma product | $15/editor/month (Professional) | Highest dependency risk due to breadth of integration |
| **Miro** | Official (Native) | HIGH -- official Miro product | $8/member/month (Team plan) | Required for collaborative UX workflows |
| **Storybook** | Official (Addon) | HIGH -- maintained by Storybook team | Free | Component development ecosystem integration |
| **Zeroheight** | Official (Native) | HIGH -- official product | $99/month (Team plan) | Design system documentation platform |
| **Hotjar** | Bridge (Zapier/Pipedream) | MEDIUM -- requires paid middleware | Variable ($0-$99+ depending on Zapier plan) | NOT plug-and-play; requires custom workflow config |
| **Whimsical** | Community | MEDIUM-LOW -- third-party maintained | Free (basic) | Verify GitHub activity before implementation |

**Cost tiers:**

| Tier | Monthly Cost | Sub-Skills Available | Best For |
|------|-------------|---------------------|----------|
| **Free** | $0/month | HEART, JTBD, Kano, Behavior Design (4 sub-skills) | Solo practitioners, bootstrapped teams, exploration |
| **Minimal** | ~$23/month per seat (Figma Professional $15/editor + Miro Free $0 or Miro Starter $8/member + Storybook free; for 2-person team: ~$46/month) | + Heuristic Eval, Design Sprint, Lean UX, Inclusive Design, AI-First Design (9 sub-skills) | 2-person teams with design workflow |
| **Full Enhancement** | ~$122-221/month (1 seat: Figma Professional $15 + Miro $8 + Storybook $0 + Zeroheight $99/team + Hotjar $0-99 via Zapier; for 2-person team: ~$145-244/month: Figma $30 + Miro $16 + Storybook $0 + Zeroheight $99/team + Hotjar $0-99) | All 10 with full enhancement MCPs (Zeroheight + Hotjar) | Teams investing in design systems and analytics |


**MCP Operational Constraints:**

The following operational constraints apply to MCP server integrations. These are the guardrails that keep the gear working when the mountain throws curveballs.

| MCP Server | Rate Limits | Auth Method | API Version | Known Failure Codes | Fallback |
|-----------|-------------|-------------|-------------|---------------------|----------|
| **Figma** | Tier-dependent (Professional: 720 req/min per-user) | OAuth 2.0 (Personal Access Token for dev) | REST API v1 (as of 2026) | 429 (rate limit), 403 (auth), 404 (file not found) | Screenshot-input mode |
| **Miro** | 100 req/min per-user (Team plan) | OAuth 2.0 | REST API v2 (as of 2026) | 429, 401, 403 | Text-based board description input |
| **Storybook** | N/A (local addon, no external API) | N/A (local filesystem) | Addon API v8+ | N/A | Manual component inventory |
| **Zeroheight** | Populated during Wave 3 implementation | API Key | Populated during Wave 3 implementation | Populated during Wave 3 implementation | Manual design system docs |
| **Hotjar (Bridge)** | Zapier-dependent (100 tasks/month Free, 750 Starter) | Zapier OAuth bridge | Zapier webhook (no direct API) | Zapier 5xx, webhook timeout | Manual analytics data entry |
| **Whimsical** | Populated during Wave 5 implementation | Populated during Wave 5 implementation | Populated during Wave 5 implementation | Populated during Wave 5 implementation | Miro as alternative |

> **Note:** Rate limits and API versions are point-in-time values as of March 2026. The quarterly MCP audit cadence (see below) includes verification of these operational constraints. Rows marked "Populated during Wave N implementation" will be completed when the sub-skills requiring that MCP server enter active development.

**Wave 3 MCP Pre-Commitment:** Before Wave 3 implementation begins, the following must be documented: (a) Zeroheight MCP connection feasibility assessment (API availability, authentication method, rate limits), (b) cost authorization for $99/month Zeroheight tier, (c) fallback workflow if Zeroheight MCP is infeasible. Wave 3 sub-skills producing design system documentation REQUIRE Zeroheight MCP server OR equivalent design system documentation tool. Failure to document all three points blocks Wave 3 KICKOFF-SIGNOFF. Wave 3 entry is BLOCKED without this integration assessment.

**Wave 5 MCP Pre-Commitment:** Before Wave 5 implementation begins, the following must be documented: (a) Whimsical community MCP GitHub activity verified (last commit within 6 months), (b) auth method confirmed per available documentation, (c) fallback to Miro-only mode documented if Whimsical MCP is infeasible. This pre-commitment is an entry criterion for Wave 5. Wave 5 entry is BLOCKED without this assessment.

**Figma dependency risk mitigation:**

Each Figma-dependent sub-skill documents a non-Figma fallback:
- `/ux-heuristic-eval`: Screenshot-input mode (user provides design screenshots as image inputs)
- `/ux-design-sprint`: Miro-only mode (sprint exercises in Miro; manual prototype reference)
- `/ux-inclusive-design`: Screenshot-input mode (manual component screenshots for evaluation)
- `/ux-ai-first-design`: Text-based analysis mode (manual design description input)

Additional mitigations:
- Quarterly MCP audit cadence with named MCP maintenance owner
- Penpot MCP (currently experimental) monitored as an open-source alternative path
- No sub-skill is entirely blocked by MCP unavailability -- all 10 have documented fallbacks

### 5. Wave Deployment (5 Criteria-Gated Waves)

Sub-skills deploy in 5 waves. Progression is **criteria-gated, not time-gated** — teams advance when readiness criteria are met, not on a calendar schedule.

| Wave | Sub-Skills | Rationale | Key Entry Criteria |
|------|-----------|-----------|-------------------|
| **1: Zero-Dependency** | Heuristic Eval, JTBD | No external user data or MCP required for core function. Highest return-per-hour entry skills. | `KICKOFF-SIGNOFF.md` completed (a kickoff checklist confirming: product name, target user population, current UX maturity self-assessment, available MCP tools, and team UX time allocation -- template provided in `skills/user-experience/templates/kickoff-signoff-template.md`) |
| **2: Data-Ready** | Lean UX, HEART | Requires Miro (Lean UX) or analytics source (HEART). Builds on Wave 1. | Completed at least 1 heuristic evaluation report AND 1 JTBD job statement that was used in a product decision |
| **3: Design System** | Atomic Design, Inclusive Design | Requires Storybook (Atomic) and Figma (Inclusive). Component infrastructure. | Launched product with an analytics data source (for HEART) OR completed 1 Lean UX build-measure-learn hypothesis cycle |
| **4: Advanced Analytics** | Behavior Design, Kano | Both require user data. Post-launch skills. | Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review |
| **5: Process Intensives** | Design Sprint, AI-First Design (COND) | Sprint requires 4-day team commitment. AI-First conditional on Enabler. | Kano classification matrix completed for at least 1 product (Wave 4 output) OR B=MAP behavioral analysis completed for at least 1 user flow (Wave 4 output) |


**Wave entry enforcement:** Each wave requires a `WAVE-{N}-SIGNOFF.md` file completed before the orchestrator routes to sub-skills in the next wave. The orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills. Template provided in `skills/user-experience/templates/wave-signoff-template.md`.

**WAVE-N-SIGNOFF.md required fields:** (1) Wave number, (2) Sub-skills included in the wave, (3) Entry criteria verified (checklist with pass/fail per criterion), (4) Quality gate score (S-014 composite for each wave deliverable), (5) Sign-off date, (6) Sign-off authority (named person or role).

**Wave enforcement 3-state behavior:** The orchestrator evaluates `WAVE-{N}-SIGNOFF.md` status and enforces one of three states:
- **PASS:** `WAVE-{N}-SIGNOFF.md` exists AND contains all required fields with non-empty values. Orchestrator routes freely to Wave N+1 sub-skills.
- **WARN:** `WAVE-{N}-SIGNOFF.md` exists but one or more required fields are empty or quality gate score is below 0.85. Orchestrator displays missing fields and asks user to confirm proceeding (P-020: user decides). WARN escalation: 3 consecutive WARN states across ANY sub-skills within one wave (not per-sub-skill) triggers crisis mode escalation. Sub-skill switching does not reset the counter. Crisis mode exit: (a) all WARN conditions resolved to PASS (automated check against WAVE-N-SIGNOFF.md criteria), OR (b) blocker acknowledged with documented remediation plan (worktracker entity creation + named owner + target date), OR (c) ABANDON (see below).
- **ABANDON:** If a team cannot resolve crisis mode blockers after documented attempt (minimum 2 resolution attempts with 3-field justification each), the team may formally ABANDON the wave. ABANDON reverts routing to the previous wave's sub-skill set. The abandoned wave's sub-skills are removed from routing until the blocker is resolved. ABANDON requires user confirmation (P-020). ABANDON is logged in `wave-progression.md` with blocker description and reversion target. Re-entry guard: After ABANDON, the orchestrator MUST consult `wave-progression.md` and BLOCK Wave N+1 routing until a documented blocker-resolution entry is logged. The blocker-resolution entry must describe what changed and reference specific evidence. Without this entry, the wave remains ABANDONED and immediate re-invocation of the abandoned wave's sub-skills returns BLOCK -- no exceptions. Sometimes the line is not skiable today -- you drop back, regroup, and come back when conditions change. That is not failure; that is judgment.
- **BLOCK:** `WAVE-{N}-SIGNOFF.md` does not exist. Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process.

**Wave stall bypass:** If a wave stalls for 2+ sprint cycles (approximately 4-6 weeks), documented bypass conditions allow teams to proceed with partial capability. Bypass requires 3-field documentation: (1) unmet criterion with specific description, (2) impact assessment of proceeding without the criterion, (3) remediation plan with target date for closing the gap. Bypass state persists as a warning banner on all sub-skill outputs produced under bypass -- every output from a bypassed wave's sub-skills carries a visible "WAVE BYPASS ACTIVE" header so the team never forgets what they skipped. The orchestrator logs the bypass for post-hoc review. All 10 sub-skills have documented non-MCP fallback paths.

```mermaid
gantt
    title Wave Deployment Timeline (Criteria-Gated)
    dateFormat X
    axisFormat %s

    section Wave 1
    /ux-heuristic-eval     :w1a, 0, 1
    /ux-jtbd               :w1b, 0, 1

    section Wave 2
    /ux-lean-ux            :w2a, 1, 2
    /ux-heart-metrics      :w2b, 1, 2

    section Wave 3
    /ux-atomic-design      :w3a, 2, 3
    /ux-inclusive-design    :w3b, 2, 3

    section Wave 4
    /ux-behavior-design    :w4a, 3, 4
    /ux-kano-model         :w4b, 3, 4

    section Wave 5
    /ux-design-sprint      :w5a, 4, 5
    /ux-ai-first-design    :crit, w5b, 4, 5
```

### 6. Synthesis Hypothesis Validation (3-Tier Confidence Gates)

Multiple sub-skills produce "synthesis hypothesis" outputs -- AI-generated abstractions that may reflect training data biases rather than the team's specific users. This is where we respect the mountain. A 3-tier confidence gate fires at skill invocation time to prevent over-reliance on unvalidated AI outputs.

| Confidence | Gate Behavior | What This Means in Practice |
|------------|--------------|---------------------------|
| **HIGH** | User reviews output and acknowledges specific AI judgment calls via a Synthesis Judgments Summary | The user sees a list of AI judgment calls and must explicitly acknowledge each one before the output advances to design decisions. Synthesis Judgments Summary format: 3 fields per judgment -- (a) AI-generated claim (verbatim from sub-skill output), (b) Evidence basis (source sub-skill, confidence level, data points cited), (c) Confidence qualifier (HIGH/MEDIUM/LOW with rationale). Documented in `skills/user-experience/rules/synthesis-validation.md`. |
| **MEDIUM** | Requires expert review OR validation against 2-3 real user data points. Expert review qualification: minimum 2 years UX practice experience (product design, user research, or UX consulting), non-team-member, non-involvement declaration required. | The output includes a "Validation Required" section. The agent does not generate design recommendations until a named validation source is provided |
| **LOW** | Output permanently labeled reference-only; design recommendation section structurally omitted | The agent template physically does not contain a design recommendation section. Users requesting design recommendations from LOW-confidence outputs receive a warning explaining why the section is absent and are directed to gather validation data to upgrade confidence level |

**Why this matters:** Without these gates, teams would treat AI-generated job statements, behavioral diagnoses, and feature priority matrices as validated research findings. They are not. They are hypotheses generated from AI training data, which may or may not reflect the team's actual user population. The confidence gates make this distinction architecturally visible and structurally enforced through template design, while preserving user authority (P-020) to override with documented justification.


**Automation bias risk:** Research on AI-assisted decision-making consistently shows that users tend to accept AI outputs uncritically (automation bias). The confidence gate architecture addresses this through three mechanisms: (1) forced acknowledgment of AI judgment calls at HIGH confidence, (2) mandatory validation source naming at MEDIUM confidence, and (3) structural omission of recommendation sections at LOW confidence. However, no template-level mechanism fully prevents a determined user from treating LOW-confidence outputs as actionable. Each synthesis output therefore includes a `Human Override Justification` field -- if a user chooses to act on a LOW-confidence output, they must provide a 3-field structured evidence template: (a) Named data source (source type + date -- e.g., "Customer interview, 2026-02-15" or "Analytics dashboard, 2026-03-01"); (b) Specific supporting data point (verbatim reference required -- generic qualifiers such as "typical", "similar", or "probably" trigger a validation warning and require resubmission with concrete evidence); (c) Validation date (ISO 8601, must be within 90 days of the override). This creates an auditable evidence chain rather than a rubber-stamp paper trail.

**Human Override Audit:** Every P-020 override of wave gates or confidence thresholds is logged with: (a) override timestamp, (b) overriding user, (c) original gate/threshold value, (d) 3-field structured evidence justification (named data source, specific supporting data point, validation date). Audit log persisted to `work/audit/override-log.md`.

**Sub-skills with LOW-confidence outputs (reference-only, no design recommendations):**
- `/ux-kano-model`: Feature priority conflict interpretation
- `/ux-heart-metrics`: Metric threshold recommendation
- `/ux-ai-first-design`: AI interaction pattern recommendations

**Sub-skills with MEDIUM-confidence outputs (require validation before design decisions):**
- `/ux-behavior-design`: Reference Intervention Patterns (non-prescriptive)

**Onboarding warning (displayed first invocation per session):**

> "IMPORTANT: This skill portfolio does NOT include a dedicated user research framework. AI-generated user insights (personas, job statements, assumption maps) are hypotheses, not validated findings. For consumer products or specialized populations, supplement with direct user contact (interviews, observations, surveys) before making design decisions based on synthesis outputs."

---

## Tiny Teams Capability Map

A 2-3 person team with this portfolio has the **capability coverage** of the following specialist roles:

| Traditional UX Role | Capability Covered By | What AI Executes | What Humans Retain |
|---------------------|-------------|-----------------|-------------------|
| **UX Researcher** | `/ux-jtbd` + `/ux-lean-ux` | Synthesizes job statements from transcripts; generates assumption maps; themes interview data | Conducts actual user interviews; judges hypothesis validity; decides what to learn next |
| **UX Designer** | `/ux-design-sprint` + `/ux-lean-ux` | Generates sketch variants; facilitates prototype construction; creates wireframes | Sets design direction; selects from AI variants; makes aesthetic/strategic judgments |
| **UX Evaluator / Auditor** | `/ux-heuristic-eval` | Evaluates designs against 10 heuristics; generates severity-rated findings reports | Triages findings; provides platform context; decides which to fix |
| **Design Systems Engineer** | `/ux-atomic-design` | Discovers existing components; composes new organisms; maintains docs | Defines component boundaries; validates against brand/accessibility standards |
| **UX Metrics Analyst** | `/ux-heart-metrics` + `/ux-behavior-design` | Populates HEART GSM templates; diagnoses B=MAP bottlenecks; generates measurement reports | Interprets trends; identifies confounders; makes product decisions from data |
| **Accessibility Specialist** | `/ux-inclusive-design` | Evaluates contrast, sizing, touch targets; checks WCAG 2.2; applies Persona Spectrum | Provides user population context; validates for non-standard populations |
| **Product Strategist (UX)** | `/ux-jtbd` + `/ux-kano-model` | Synthesizes competitive job analysis; processes Kano responses; generates priority matrices | Frames the strategic problem; decides which job to pursue; validates classifications |
| **UX Department Manager** | `/user-experience` (orchestrator) | Routes to correct sub-skill; manages cross-framework integration; tracks hypothesis backlogs | Provides product context; makes final design decisions; provides organizational judgment |

**The honest take on scope:** This portfolio spans the same UX **discipline scope** as a 6-8 person UX team -- it does NOT match the throughput or depth of 6-8 full-time specialists. The gap is in user research depth (the HIGH RISK limitation documented below) and the creative/strategic judgment that only human expertise provides. Each sub-skill covers a specialist's capability area by combining AI execution of structured/analytical steps with human judgment on strategic decisions.

Two people doing what used to take eight. That is the tiny teams promise. The line nobody thought was skiable. This is the gear that makes it possible.

---

## Known Limitations

We scoped this mountain from every angle. Here is what we found.

### HIGH RISK: User Research Gap

This portfolio does **NOT** include a dedicated user research framework.

AI-generated user insights -- personas, job statements, assumption maps -- are **hypotheses, not validated findings**. The Design Sprint Day 4 testing protocol and Lean UX validation loops are minimum viable research mechanisms, NOT substitutes for a systematic user research program.

**Impact:**
- Teams building consumer products, products for specialized populations, or products in competitive markets SHOULD NOT rely solely on these frameworks for user understanding
- Synthesis hypothesis outputs from JTBD, Lean UX, Design Sprint, and Inclusive Design are particularly affected
- The parent orchestrator's onboarding flow warns every user about this gap at first invocation

**Mitigation:**
- A 3-tier synthesis hypothesis validation protocol (HIGH / MEDIUM / LOW confidence gates) is embedded in the architecture. LOW-confidence outputs structurally omit design recommendations. MEDIUM-confidence outputs require named validation sources before advancing to design decisions.
- V2 planning prioritizes a dedicated `/ux-user-research` sub-skill (Maze/UserZoom integration) as a P1 gap closure.

McConkey respected the mountain. This is us respecting it. The research gap is real, the architecture accounts for it, and V2 closes it.

### AI-First Design: Conditional Status

The `/ux-ai-first-design` sub-skill is ranked #8 in the selection analysis (projected score 7.80) but carries the **CONDITIONAL** designation because the framework must be created by this project before implementation. This is a synthesized framework, not an established one.

- **Blocking prerequisite:** A synthesis Enabler must reach DONE status with a verified WSM score >= 8.00. Independent reviewer sign-off required on WSM scoring for Enabler validation. Independent reviewer = any Jerry Framework user who did NOT author the sub-skill under review (i.e., the person scoring the Enabler cannot be the person who built it, and must not have contributed to its design or implementation)
- **Expiry mechanism:** The Enabler has a 90-day time-box from creation date. If the Enabler has not reached DONE status within 90 days, it expires automatically and the substitution path activates. The expiry deadline is tracked as a worktracker entity field.
- **Substitution path:** If the AI-First Design Enabler has not achieved its validation gate by Wave 5, Wave 5 delivers Design Sprint only; Service Blueprinting is a V2 P1 candidate
- **Interim path:** Until the Enabler completes, the parent orchestrator routes AI product UX requests to `/ux-heuristic-eval` with supplemental PAIR Guidebook heuristics

### Ethics Framework Gaps

The V1 portfolio has partial coverage of UX ethics:
- No dedicated dark patterns audit framework (Brignull deceptive.design taxonomy is a V2 candidate)
- No dedicated algorithmic bias review framework (PAIR Guidebook + ACM FAccT is a V2 candidate)
- Microsoft Inclusive Design covers accessibility ethics but not broader algorithmic or persuasion ethics

### Figma Single Point of Failure

Figma MCP is required for 4 sub-skills and enhances 2 more (6 of 10 total connections). If Figma changes its MCP server schema, restricts access, or monetizes the integration (Figma has a history of restricting previously free API access -- Dev Mode became paid in 2023), these sub-skills lose their primary MCP integration path.

**Mitigations:**
- Each Figma-dependent sub-skill documents a non-Figma fallback path (see MCP Integration section above)
- Quarterly MCP audit cadence with named maintenance owner
- Penpot MCP (currently experimental) monitored as an open-source alternative
- The 3 highest Figma-dependent sub-skills (Atomic Design, Design Sprint, AI-First Design) must document explicit non-Figma fallback paths in their skill definitions before launch

### Context Window Pressure

With 10+ sub-skill definitions potentially loaded in a session, context window pressure is a risk. The architecture mitigates this through progressive disclosure:

- **Tier 1 (session start):** Only the parent `/user-experience` skill description is loaded (~500 tokens). Sub-skill definitions are NOT loaded.
- **Tier 2 (on-demand):** Sub-skill agents are loaded via Task tool invocation. Only the specific sub-skill being used consumes context.
- **Tier 3 (supplementary):** Output templates, prior work artifacts, and framework reference materials are loaded selectively during agent execution.

This ensures a single sub-skill invocation consumes ~2,000-8,000 tokens for the agent definition, not ~20,000-80,000 for all 10 sub-skills simultaneously.

### Scope Creep Risk

As V2 additions expand the sub-skill count (potentially to 14-16), the routing architecture must evolve:
- At 15+ sub-skills: evaluate Layer 2 rule-based routing per the Jerry scaling roadmap
- At 20+ sub-skills: evaluate LLM-as-Router (Layer 3)
- Sub-skill groupings (Discovery, Design, Build, Measure, Ethics) are pre-designed to serve as Layer 2 routing categories

---

---

> **Note:** This issue is split across multiple comments due to size. See comments below for:
> - **Comment 1:** Acceptance Criteria
> - **Comment 2:** Technical Specification
> - **Comment 3:** V2 Roadmap, Research Backing, Appendices
