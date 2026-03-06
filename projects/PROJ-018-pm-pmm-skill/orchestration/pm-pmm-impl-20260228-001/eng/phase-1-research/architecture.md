# PM/PMM Skill Architecture Document

<!-- VERSION: 1.0.0 | DATE: 2026-03-01 | SOURCE: PROJ-018, GitHub Issue #123 | AGENT: eng-phase-1-research -->

> Canonical architecture for the `/pm-pmm` skill within the Jerry Framework. Defines agent boundaries, framework operationalization, artifact ownership, data flows, and integration points. All implementation work MUST reference this file.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Skill Directory Layout](#skill-directory-layout) | File organization per H-34 dual-file architecture |
| [5-Agent Model Rationale](#5-agent-model-rationale) | Why 5 agents, alternatives considered |
| [Agent Boundary Definitions](#agent-boundary-definitions) | Ownership, exclusions, and routing for each agent |
| [Discovery vs Delivery Mode Architecture](#discovery-vs-delivery-mode-architecture) | Dual-mode operation design |
| [Cagan Four Big Risks Mapping](#cagan-four-big-risks-mapping) | Value Risk and Business Viability Risk scope |
| [18 Framework Operationalization Plan](#18-framework-operationalization-plan) | Which agent uses which frameworks and how |
| [Artifact Ownership Matrix](#artifact-ownership-matrix) | Primary owner and contributors for all 15 artifact types |
| [Cross-Agent Data Flow Design](#cross-agent-data-flow-design) | How agents share data via the orchestrator |
| [Integration Points with Existing Skills](#integration-points-with-existing-skills) | Connections to /worktracker, /adversary, /problem-solving, /architecture, /nasa-se |
| [File Organization per H-34](#file-organization-per-h-34) | Dual-file architecture compliance |
| [References](#references) | Source traceability |

---

## Skill Directory Layout

The `/pm-pmm` skill follows Jerry's standard skill structure per H-25 and H-34.

```
skills/
  pm-pmm/
    SKILL.md                                    # Skill definition (< 500 lines, H-25)
    agents/
      pm-product-strategist.md                  # Agent definition (.md frontmatter + body)
      pm-product-strategist.governance.yaml     # Governance metadata (schema-validated)
      pm-customer-insight.md
      pm-customer-insight.governance.yaml
      pm-business-analyst.md
      pm-business-analyst.governance.yaml
      pm-competitive-analyst.md
      pm-competitive-analyst.governance.yaml
      pm-market-strategist.md
      pm-market-strategist.governance.yaml
    templates/                                  # 15 artifact templates (design-time)
      01-prd.template.md
      02-product-vision.template.md
      03-roadmap.template.md
      04-use-cases.template.md
      05-personas.template.md
      06-journey-maps.template.md
      07-voc-analysis.template.md
      08-business-case.template.md
      09-market-sizing.template.md
      10-competitive-analysis.template.md
      11-battle-cards.template.md
      12-win-loss-analysis.template.md
      13-gtm-plan.template.md
      14-mrd.template.md
      15-buyer-personas.template.md

docs/pm-pmm/                                   # User-generated artifacts (runtime)
  prd/
  product-vision/
  roadmap/
  use-cases/
  personas/
  journey-maps/
  voc/
  business-case/
  market-sizing/
  competitive-analysis/
  battle-cards/
  win-loss/
  gtm-plan/
  mrd/
  buyer-personas/
```

**Key conventions:**
- Agent filenames follow `{skill-prefix}-{function}` kebab-case per AD-M-001
- Every `.md` agent definition has a companion `.governance.yaml` per H-34
- Templates use `{NN}-{artifact-slug}.template.md` naming
- Runtime artifacts are written to `docs/pm-pmm/{artifact-type}/{slug}.md`

---

## 5-Agent Model Rationale

### Selected Architecture: Option B (5 Agents)

The design synthesis (PS-001-E-004 v2.1) evaluated four architecture alternatives. The 5-agent model was selected based on three decisive criteria:

| Criterion | 5-Agent Model Score | Rationale |
|-----------|-------------------|-----------|
| Decision-domain separation | Excellent | Each agent maps to exactly one decision domain |
| Artifact ownership clarity | Excellent | 15 artifacts, 5 agents, zero primary-ownership overlap |
| Routing determinism | Excellent | No ambiguous routing for any primary artifact type |

### Option Scoring Matrix (Weighted Composite)

Four options were evaluated against 6 weighted dimensions. The weights reflect the relative importance of each criterion for the PM/PMM skill architecture, with P-003 compliance receiving the highest weight as a constitutional HARD constraint.

**Dimension Weights:**

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| P-003 Compliance (single-level topology) | 25% | Constitutional HARD constraint -- non-negotiable |
| Zero Artifact Ownership Overlap | 20% | Routing determinism depends on unambiguous ownership |
| Cagan Risk Domain Alignment | 20% | Framework alignment drives framework-to-agent mapping |
| Context Budget Efficiency | 15% | Per-agent framework load affects tool selection accuracy |
| Routing Disambiguation Clarity | 10% | Natural language routing must resolve without H-31 clarification |
| Dual Mode Support | 10% | Discovery/delivery mode must work cleanly per agent boundary |

**Per-Option Dimension Scores:**

| Dimension (Weight) | Option A: 4-Agent | Option B: 5-Agent | Option C: 6-Agent | Option D: 7-Agent |
|---|---|---|---|---|
| P-003 Compliance (0.25) | 0.30 (conflated roles need cross-invocation) | 1.00 (clean single-level) | 1.00 (clean single-level) | 1.00 (clean single-level) |
| Zero Overlap (0.20) | 0.40 (competitive/financial overlap) | 1.00 (zero overlap verified) | 0.90 (journey-map overlap risk) | 1.00 (zero overlap) |
| Risk Domain Alignment (0.20) | 0.60 (3 domains forced into 4 agents) | 1.00 (2+3 split matches Cagan) | 0.80 (over-split on value risk) | 0.70 (fragments viability risk) |
| Context Budget (0.15) | 0.90 (fewer agents = lower overhead) | 0.85 (3-5 frameworks/agent) | 0.70 (2-3 frameworks/agent, thin) | 0.60 (avg 2.1 artifacts/agent, AP-05 risk) |
| Routing Disambiguation (0.10) | 0.50 ("competitive pricing" ambiguous) | 0.90 (clear keyword separation) | 0.60 ("journey" vs "persona" collision) | 0.80 (more agents = more disambiguation) |
| Dual Mode Support (0.10) | 0.80 (works but broad agents blur mode) | 0.95 (mode per agent is clean) | 0.90 (works well) | 0.90 (works well) |

**Weighted Composite Calculation:**

| Option | Calculation | Composite |
|--------|-----------|-----------|
| A: 4-Agent | (0.30 x 0.25) + (0.40 x 0.20) + (0.60 x 0.20) + (0.90 x 0.15) + (0.50 x 0.10) + (0.80 x 0.10) = 0.075 + 0.080 + 0.120 + 0.135 + 0.050 + 0.080 | **0.54** |
| B: 5-Agent | (1.00 x 0.25) + (1.00 x 0.20) + (1.00 x 0.20) + (0.85 x 0.15) + (0.90 x 0.10) + (0.95 x 0.10) = 0.250 + 0.200 + 0.200 + 0.128 + 0.090 + 0.095 | **0.96** |
| C: 6-Agent | (1.00 x 0.25) + (0.90 x 0.20) + (0.80 x 0.20) + (0.70 x 0.15) + (0.60 x 0.10) + (0.90 x 0.10) = 0.250 + 0.180 + 0.160 + 0.105 + 0.060 + 0.090 | **0.85** |
| D: 7-Agent | (1.00 x 0.25) + (1.00 x 0.20) + (0.70 x 0.20) + (0.60 x 0.15) + (0.80 x 0.10) + (0.90 x 0.10) = 0.250 + 0.200 + 0.140 + 0.090 + 0.080 + 0.090 | **0.85** |

**Verdict:** Option B (5-Agent) scores 0.96, clearly ahead of Options C and D (0.85 each) and Option A (0.54). The gap is driven primarily by Option A's P-003 compliance risk and overlap issues, while Options C and D are penalized for over-fragmentation and context efficiency concerns.

### Alternatives Rejected

| Option | Agents | Rejection Reason |
|--------|--------|-----------------|
| A: 4-Agent | Product Strategist, Customer Insight, Business Analyst (+ competitive), Market Strategist | Business Analyst conflates offensive (competitive) and defensive (financial) analysis. "Competitive pricing" routes ambiguously. Scores 0.54 composite -- P-003 risk is disqualifying. |
| C: 6-Agent | 5 agents + pm-journey-mapper | Journey mapping is too thin as standalone. Produces only journey maps and touchpoint analysis. Consolidation into pm-customer-insight eliminates routing confusion. Scores 0.85 composite. |
| D: 7-Agent | 6 agents + Product Ops | Product Ops is an emerging discipline. Premature to add without validated demand. Reserved for v2.0. Scores 0.85 composite -- tied with Option C. |

### The 5 Agents

| Agent | Decision Question | Risk Domain | Primary Owner |
|-------|------------------|-------------|---------------|
| `pm-product-strategist` | "What should we build, and why?" | Value + Viability (strategy) | Product Manager |
| `pm-customer-insight` | "Who are our customers, and what do they need?" | Value Risk | Product Manager + UX Research |
| `pm-business-analyst` | "Is this worth investing in?" | Viability Risk (financial) | Product Manager + Finance |
| `pm-competitive-analyst` | "Who are we up against?" | Viability Risk (market context) | Product Marketing Manager |
| `pm-market-strategist` | "How do we bring this to market?" | Viability Risk (go-to-market) | Product Marketing Manager |

---

## Agent Boundary Definitions

### pm-product-strategist

**Owns:**
- Product Requirements Documents (PRDs) -- full lifecycle from problem statement through acceptance criteria
- Product Vision and Strategy Documents -- strategic direction, north star metric, winning aspiration
- Product Roadmap prioritization inputs -- RICE/ICE/MoSCoW/WSJF scoring, opportunity assessment
- Use Case Specifications -- business-perspective use cases with actors, preconditions, flows

**Does NOT own:**
- User personas (pm-customer-insight owns)
- Financial modeling or pricing (pm-business-analyst owns)
- Competitive intelligence (pm-competitive-analyst owns)
- Go-to-market planning (pm-market-strategist owns)
- Technical architecture decisions (belongs to `/architecture` skill)
- UX/design specifications (out of scope -- Usability Risk)

**Consumes from other agents:**
- Personas and VOC themes from pm-customer-insight to ground PRDs in customer evidence
- Market sizing from pm-business-analyst to validate opportunity scale
- Competitive landscape from pm-competitive-analyst to inform differentiation strategy

**Routing keywords:** PRD, product requirements, backlog, prioritize, RICE, roadmap, "what to build", product vision, strategy, opportunity, feature prioritization, north star

### pm-customer-insight

**Owns:**
- User Persona Documents -- JTBD-oriented personas with functional, emotional, and social jobs
- Customer Journey Maps -- 9-stage maps with Moments of Truth (ZMOT, FMOT, SMOT, UMOT)
- Voice of Customer (VOC) Research Reports -- interview synthesis, theme extraction, opportunity scoring

**Does NOT own:**
- Buyer personas (pm-market-strategist owns -- buyer vs. user distinction)
- Competitive analysis (pm-competitive-analyst owns)
- PRDs or roadmaps (pm-product-strategist owns)
- Pricing research (pm-business-analyst owns Van Westendorp/conjoint)
- UX wireframes or prototypes (out of scope -- Usability Risk)

**Consumes from other agents:**
- Product strategy context from pm-product-strategist to scope persona research
- Competitive positioning from pm-competitive-analyst to understand switching context

**Routing keywords:** persona, customer interview, journey map, VOC, "voice of customer", churn analysis, NPS, CSAT, CES, customer research, user needs, pain points, customer discovery

### pm-business-analyst

**Owns:**
- Business Case / Financial Plan -- NPV, IRR, break-even, sensitivity analysis
- Market Sizing Analysis (TAM/SAM/SOM) -- sole owner of market quantification
- Revenue model analysis, pricing strategy recommendations, unit economics (CAC, LTV, NRR, payback)

**Does NOT own:**
- Competitive intelligence (pm-competitive-analyst owns)
- GTM planning (pm-market-strategist owns)
- Product strategy (pm-product-strategist owns)
- Customer research (pm-customer-insight owns)

**Consumes from other agents:**
- Competitive pricing data from pm-competitive-analyst
- Customer willingness-to-pay signals from pm-customer-insight
- Product scope from pm-product-strategist to estimate investment requirements
- Market positioning from pm-market-strategist for packaging context

**Routing keywords:** business case, financial model, market sizing, TAM, SAM, SOM, pricing model, unit economics, LTV, CAC, NRR, revenue model, break-even, NPV, investment, feasibility

### pm-competitive-analyst

**Owns:**
- Competitive Analysis Documents -- Porter's Five Forces, SWOT, competitive positioning maps
- Battle Cards -- per-competitor comparison with talk tracks and objection handling
- Win/Loss Analysis Reports -- sole owner of win/loss pattern analysis

**Does NOT own:**
- Market sizing (pm-business-analyst owns)
- GTM planning (pm-market-strategist owns)
- User personas (pm-customer-insight owns)
- Product roadmap (pm-product-strategist owns)

**Consumes from other agents:**
- Product differentiation points from pm-product-strategist
- Customer pain points from pm-customer-insight for competitive framing
- Pricing intelligence feeds into pm-business-analyst

**Routing keywords:** competitive analysis, battle card, win/loss, competitor, Porter's, SWOT, "who competes", competitive landscape, market intelligence, differentiation, competitive threat

### pm-market-strategist

**Owns:**
- Go-to-Market (GTM) Plan -- positioning, messaging, launch strategy (T1/T2/T3), channel plan
- Market Requirements Document (MRD) -- market-driven requirements with segment analysis
- Buyer Persona Documents -- buying-committee-focused personas (distinct from user personas)

**Does NOT own:**
- User personas (pm-customer-insight owns -- user vs. buyer distinction)
- Financial modeling (pm-business-analyst owns)
- Competitive analysis (pm-competitive-analyst owns primary analysis)
- Product roadmap (pm-product-strategist owns)

**Consumes from other agents:**
- Competitive positioning from pm-competitive-analyst for messaging
- Market sizing from pm-business-analyst for segment prioritization
- User personas from pm-customer-insight for buyer-user alignment
- Product strategy from pm-product-strategist for launch content

**Routing keywords:** GTM, go-to-market, positioning, messaging, MRD, launch plan, sales enablement, buyer persona, product marketing, category, PLG, product-led growth

---

## Discovery vs Delivery Mode Architecture

Every agent operates in two modes. Discovery is the default -- enforced in the agent system prompt.

### Mode Characteristics

| Dimension | Discovery Mode | Delivery Mode |
|-----------|---------------|---------------|
| **Purpose** | Explore, hypothesize, validate assumptions | Produce stakeholder-ready artifacts |
| **Output length** | 1-2 pages | Full framework depth (5-20 pages) |
| **Framework depth** | Lightweight application, key dimensions only | Complete framework execution with all sections |
| **Evidence standard** | Hypotheses with stated confidence | Data-validated claims with citations |
| **Audience** | PM/PMM internal working document | Cross-functional stakeholders, executives |
| **Artifact status** | `discovery` | `delivery` or `final` |
| **Default?** | Yes -- always start here | Explicit user request or prior discovery exists |

### Mode Selection Logic

```
IF user explicitly requests "delivery" or "full" or "stakeholder-ready":
    mode = delivery
ELIF prior discovery artifact exists for this topic (cross_refs match):
    mode = delivery (suggest upgrade to user, confirm per P-020)
ELSE:
    mode = discovery (default)
```

### Mode Impact on Template Usage

Each artifact template contains both discovery and delivery sections. The agent selects the appropriate sections based on mode:

- **Discovery sections:** Problem hypothesis, quick assessment, key metrics, confidence level, next steps
- **Delivery sections:** Full framework application, detailed analysis, evidence citations, executive summary, appendices

### Design Principle

Discovery before delivery prevents the most expensive PM failure mode: building a polished artifact for a product nobody wants. Discovery validates assumptions cheaply. Delivery commits resources to documentation.

### Discovery-to-Delivery Promotion Requirements

An artifact MUST satisfy the following criteria before transitioning from discovery to delivery mode. This addresses FM-002 (mode switching corruption) from the FMEA analysis.

**Minimum completeness criteria per artifact type:**

| Artifact Type | Discovery Sections Required Complete | Promotion Gate |
|--------------|--------------------------------------|----------------|
| PRD | Problem Statement, Strategic Context, User Stories (JTBD), RICE Scoring, Kano Classification | All 5 discovery sections non-empty; at least 3 JTBD statements defined |
| Product Vision | Vision Statement, Strategic Choices, North Star Metric | Vision statement present; north star metric defined |
| Roadmap | Strategic Context, Priority Framework, Horizon Mapping | At least 3 prioritized items with RICE/WSJF scores |
| Use Cases | Actor Definition, Primary Flow, Preconditions | At least 1 fully specified use case with actors and flow |
| User Personas | Persona Profile, JTBD Statements, Pain Points | At least 1 JTBD statement per persona; pain points enumerated |
| Journey Maps | Stage Definition, Moments of Truth | At least 3 journey stages with touchpoints defined |
| VOC Report | Interview Summary, Theme Extraction | At least 3 themes extracted with supporting evidence |
| Business Case | Executive Summary, Lean Canvas, Market Opportunity, Financial Estimates | All 9 Lean Canvas boxes populated; order-of-magnitude financials present |
| Market Sizing | TAM/SAM/SOM Estimates, Methodology Statement | All 3 levels estimated with stated methodology |
| Competitive Analysis | Landscape Overview, SWOT, Competitor Profiles | At least 3 competitors profiled; SWOT complete |
| Battle Cards | Competitor Overview, Differentiators, Talk Tracks | At least 1 competitor with talk track |
| Win/Loss Analysis | Pattern Summary, Win/Loss Ratio | At least 5 data points analyzed |
| GTM Plan | Positioning Hypothesis, Target Segments, Channel Strategy | Positioning statement present; at least 2 channels identified |
| MRD | Market Problem, Segment Analysis, Requirements Summary | Market problem defined; at least 1 segment analyzed |
| Buyer Personas | Buyer Profile, Buying Process, Decision Criteria | At least 1 buyer persona with decision criteria |

**Validation mechanism (frontmatter status gate):**

1. **Pre-transition check (L3 enforcement):** Before writing `mode: delivery` to an artifact, the producing agent MUST verify that all discovery-mode sections contain substantive content (not just placeholder text). The agent system prompt includes a section-completeness checklist.
2. **Frontmatter gate:** The `status` field transitions from `discovery` to `delivery` only when the agent confirms section completeness. The transition is one-way: once promoted to delivery, an artifact cannot revert to discovery mode. If new discovery is needed, a new artifact ID is created and the old artifact is archived.
3. **Post-transition verification:** After mode promotion, the `/adversary` quality gate verifies that delivery-only sections are being populated. An artifact at `status: delivery` with empty delivery sections triggers a REVISE verdict.
4. **`delivery_sections_complete` field:** Agents set this boolean field in frontmatter to `true` only after all delivery-mode sections are populated. The `delivery -> final` gate requires `delivery_sections_complete: true`.

---

## Cagan Four Big Risks Mapping

### Scope: Value Risk + Business Viability Risk

The `/pm-pmm` skill addresses the two Cagan Big Risks that fall within PM/PMM ownership:

```
                    THE FOUR BIG RISKS
                    ==================

    IN SCOPE (PM/PMM):

      VALUE RISK                   BUSINESS VIABILITY RISK
      Will they buy/use it?        Does it work for the business?

      pm-customer-insight          pm-business-analyst
      pm-product-strategist        pm-competitive-analyst
                                   pm-market-strategist

    OUT OF SCOPE:

      USABILITY RISK               FEASIBILITY RISK
      UX/Design domain             Engineering domain
```

### Agent-to-Risk Mapping

| Agent | Primary Risk | Secondary Risk | Risk Facet |
|-------|-------------|---------------|------------|
| pm-product-strategist | Value Risk | Viability Risk | Strategy synthesis -- connects "what customers need" to "what the business can deliver" |
| pm-customer-insight | Value Risk | -- | Customer understanding -- personas, journeys, voice of customer |
| pm-business-analyst | Viability Risk | -- | Financial viability -- business case, pricing, market sizing |
| pm-competitive-analyst | Viability Risk | -- | Market viability -- competitive landscape, differentiation, win/loss |
| pm-market-strategist | Viability Risk | -- | Go-to-market viability -- positioning, messaging, launch, buyer alignment |

### Cross-Risk Agent: pm-product-strategist

The pm-product-strategist uniquely spans both risks because product strategy requires synthesizing customer value (Value Risk) with business viability (Viability Risk). The PRD, for example, must answer both "is this valuable to customers?" and "is this viable for the business?" This dual-risk position makes it the natural lead agent for orchestrated workflows.

---

## 18 Framework Operationalization Plan

### Framework Count Reconciliation

The Issue #123 specification references **18 validated primary frameworks**. The frontmatter-schema.md framework coverage matrix contains **25 entries** (18 primary + 7 supporting). This section reconciles the count:

| Category | Count | Description |
|----------|-------|-------------|
| **Primary frameworks** (rows 1-18) | 18 | Standalone methodologies from Issue #123 specification. Each produces a distinct canonical output structure. Each is a routing target assigned to a specific agent. |
| **Supporting methods** (rows 19-25 in schema) | 7 | Sub-methodologies or specialized applications of the 18 primaries. Applied as sub-techniques within primary framework execution. Not standalone routing targets. |
| **Total entries in schema matrix** | 25 | 18 primary + 7 supporting |

**Framework Hierarchy:**

| Supporting Method | Parent Primary Framework | Relationship |
|-------------------|------------------------|--------------|
| ICE/MoSCoW/WSJF | RICE Prioritization (#3) | Alternative scoring methods within the same prioritization domain |
| North Star Metric | Playing to Win (#16) | Anchoring metric derived from strategy cascade's "Winning Aspiration" |
| Story Mapping (Patton) | Opportunity Solution Trees (#1) | Collaborative discovery technique feeding into OST structure |
| SWOT Analysis | Porter's Five Forces (#7) | Quick-scan complement to structural competitive analysis |
| NPV/IRR/break-even | SaaS Financial Metrics (#15) | Financial modeling tools used within business case quantification |
| NPS/CSAT/CES | Customer Development (#14) | Customer satisfaction measurement within development phases |
| Opportunity Scoring (ODI) | JTBD (#2) | Outcome scoring methodology from the JTBD/ODI tradition (Ulwick) |

**Per-agent framework count (primary only):**

| Agent | Primary Frameworks | Count |
|-------|-------------------|-------|
| pm-product-strategist | OST, JTBD (secondary), RICE, Kano, Product Kata, Playing to Win | 6 |
| pm-customer-insight | JTBD, Customer Development, Moments of Truth, Service Blueprint | 4 |
| pm-business-analyst | Van Westendorp, Lean Canvas/BMC, SaaS Metrics | 3 |
| pm-competitive-analyst | Porter's Five Forces, Blue Ocean, Crossing the Chasm | 3 |
| pm-market-strategist | Positioning (Dunford), PMF Survey (Ellis), Lauchengco PMM | 3 |
| **Total** (accounting for JTBD shared) | | **18 unique** |

Each of the 18 validated frameworks is assigned to specific agents with defined operationalization -- meaning the agent produces the framework's canonical output structure, not merely mentioning it by name.

### Framework-to-Agent Assignment

| # | Framework | Primary Agent | Secondary Agent(s) | Operationalization |
|---|-----------|--------------|--------------------|--------------------|
| 1 | Opportunity Solution Trees (Torres) | pm-product-strategist | -- | Agent produces a tree structure: outcome at root, opportunities as branches, solutions as leaves. Each node includes evidence link and confidence level. |
| 2 | JTBD (Christensen/Ulwick) | pm-customer-insight | pm-product-strategist | Agent decomposes user needs into functional, emotional, and social jobs. Each job includes "When I..., I want to..., so I can..." statement with importance/satisfaction scores. |
| 3 | RICE Prioritization (Intercom) | pm-product-strategist | -- | Agent scores features on four dimensions: Reach (numeric), Impact (1-3 scale), Confidence (percentage), Effort (person-weeks). Produces ranked score table. |
| 4 | Kano Model | pm-product-strategist | -- | Agent classifies features into must-have, performance, and delight categories. Produces Kano questionnaire structure and classification matrix. |
| 5 | Product Kata (Perri) | pm-product-strategist | -- | Agent walks through the cycle: Direction (vision) -> Current State (metrics) -> Next Target Condition (measurable goal) -> First Step (experiment). |
| 6 | Positioning Framework (Dunford) | pm-market-strategist | -- | Agent executes Dunford's 5 steps: competitive alternatives, unique attributes, value for segment, target segment, market category. Produces positioning statement. |
| 7 | Porter's Five Forces | pm-competitive-analyst | -- | Agent assesses all five forces: (1) competitive rivalry, (2) threat of new entrants, (3) threat of substitutes, (4) bargaining power of suppliers, (5) bargaining power of buyers. Each force rated high/medium/low with evidence. |
| 8 | Van Westendorp PSM | pm-business-analyst | -- | Agent structures four price-point questions: too cheap, cheap/bargain, expensive/getting-expensive, too expensive. Produces price sensitivity curves and optimal price range. |
| 9 | Product-Market Fit Survey (Ellis) | pm-market-strategist | -- | Agent structures the "very disappointed" test. Produces survey design with the canonical question and threshold analysis (40% benchmark). |
| 10 | Blue Ocean / Value Curve (Kim & Mauborgne) | pm-competitive-analyst | -- | Agent produces value curve diagram: X-axis lists competing factors, Y-axis plots our offering vs. competitors. Identifies eliminate-reduce-raise-create actions. |
| 11 | Lean Canvas / BMC (Osterwalder/Maurya) | pm-business-analyst | -- | Agent populates all 9 blocks: Problem, Solution, Key Metrics, Unique Value Prop, Unfair Advantage, Channels, Customer Segments, Cost Structure, Revenue Streams. |
| 12 | Crossing the Chasm (Moore) | pm-competitive-analyst | pm-market-strategist | Agent identifies Technology Adoption Lifecycle position (innovators, early adopters, early majority, late majority, laggards). Produces bowling alley segment targeting strategy. |
| 13 | Lauchengco's PMM Model | pm-market-strategist | -- | Agent maps activities to four PMM roles: Ambassador (voice of market), Strategist (market strategy), Storyteller (messaging), Evangelist (go-to-market). |
| 14 | Customer Development (Blank) | pm-customer-insight | -- | Agent guides through four phases: Customer Discovery -> Customer Validation -> Customer Creation -> Company Building. Produces phase assessment with evidence. |
| 15 | SaaS Financial Metrics (Bessemer/T2D3) | pm-business-analyst | -- | Agent calculates and benchmarks: Rule of 40, Magic Number, LTV:CAC, NRR, Gross Margin, Net Dollar Retention. Compares against BVP Cloud Index benchmarks. |
| 16 | Playing to Win (Lafley & Martin) | pm-product-strategist | -- | Agent walks through strategy cascade: Winning Aspiration -> Where to Play -> How to Win -> Capabilities Required -> Management Systems. |
| 17 | Moments of Truth (P&G/Google) | pm-customer-insight | -- | Agent maps four moments: ZMOT (Zero Moment -- research), FMOT (First Moment -- shelf/site), SMOT (Second Moment -- experience), UMOT (Ultimate Moment -- advocacy). |
| 18 | Service Blueprint (Shostack) | pm-customer-insight | -- | Agent produces service blueprint with five lanes: Physical Evidence, Customer Actions, Frontstage Contact, Backstage Contact, Support Processes. Identifies line of visibility and line of interaction. |

### Additional Supporting Methods (Not Part of Core 18)

These methods are applied by agents as sub-techniques within the core frameworks. They are not standalone routing targets:

| Method | Used By | Context |
|--------|---------|---------|
| ICE/MoSCoW/WSJF prioritization | pm-product-strategist | Alternative scoring when RICE is not optimal |
| North Star Metric | pm-product-strategist | Vision document anchoring |
| Story Mapping (Patton) | pm-product-strategist | Use case organization |
| SWOT Analysis | pm-competitive-analyst | Quick competitive assessment |
| Gartner MQ / Forrester Wave | pm-competitive-analyst | Market positioning reference |
| Category Design (Play Bigger) | pm-competitive-analyst | Category creation strategy |
| StoryBrand (Miller) | pm-market-strategist | Messaging narrative structure |
| Good-Better-Best pricing | pm-business-analyst | Tiered pricing design |
| Conjoint analysis | pm-business-analyst | Feature-price tradeoff analysis |
| NPV/IRR/break-even | pm-business-analyst | Financial modeling |
| NPS/CSAT/CES measurement | pm-customer-insight | CX measurement |
| Opportunity Scoring (Ulwick/ODI) | pm-customer-insight | JTBD outcome scoring |

---

## Artifact Ownership Matrix

Every primary artifact has exactly one owner. Contributing agents provide data inputs but do not produce the artifact. The primary agent is responsible for the artifact's quality, completeness, and lifecycle.

| # | Artifact | Primary Agent | Contributing Agents | Criticality | Mode |
|---|----------|--------------|--------------------|----|------|
| 1 | PRD (Product Requirements Document) | pm-product-strategist | pm-customer-insight | C2 | Both |
| 2 | Product Vision and Strategy | pm-product-strategist | pm-business-analyst | C3 | Both |
| 3 | Product Roadmap | pm-product-strategist | pm-business-analyst, pm-customer-insight | C2 | Both |
| 4 | Use Case Specifications | pm-product-strategist | pm-customer-insight | C1 | Both |
| 5 | User Personas | pm-customer-insight | (standalone) | C1 | Both |
| 6 | Customer Journey Maps | pm-customer-insight | (standalone) | C2 | Both |
| 7 | VOC Research Report | pm-customer-insight | (standalone) | C2 | Both |
| 8 | Business Case | pm-business-analyst | pm-product-strategist, pm-competitive-analyst | C3 | Both |
| 9 | Market Sizing (TAM/SAM/SOM) | pm-business-analyst | pm-competitive-analyst | C2 | Both |
| 10 | Competitive Analysis | pm-competitive-analyst | pm-market-strategist | C2 | Both |
| 11 | Battle Cards | pm-competitive-analyst | pm-market-strategist | C2 | Both |
| 12 | Win/Loss Analysis | pm-competitive-analyst | pm-market-strategist | C2 | Both |
| 13 | GTM Plan | pm-market-strategist | pm-competitive-analyst, pm-customer-insight | C3 | Both |
| 14 | MRD (Market Requirements Document) | pm-market-strategist | pm-competitive-analyst, pm-product-strategist | C2 | Both |
| 15 | Buyer Personas | pm-market-strategist | pm-competitive-analyst | C1 | Both |

### Artifact Count per Agent

| Agent | Primary Artifacts | Count |
|-------|-------------------|-------|
| pm-product-strategist | PRD, Product Vision, Roadmap, Use Cases | 4 |
| pm-customer-insight | Personas, Journey Maps, VOC | 3 |
| pm-business-analyst | Business Case, Market Sizing | 2 |
| pm-competitive-analyst | Competitive Analysis, Battle Cards, Win/Loss | 3 |
| pm-market-strategist | GTM Plan, MRD, Buyer Personas | 3 |
| **Total** | | **15** |

---

## Cross-Agent Data Flow Design

### P-003 Compliant Orchestration

All agent interactions are mediated by the Jerry main context (orchestrator). No agent invokes another agent directly.

```
                    JERRY MAIN CONTEXT
                      (Orchestrator)
                     Routes by intent
                     Manages handoffs
                     Resolves conflicts
                            |
        +-------------------+-------------------+
        |                   |                    |
  pm-product-       pm-customer-        pm-competitive-
  strategist         insight              analyst
        |                                       |
  pm-business-                          pm-market-
  analyst                                strategist

  All data flows through the orchestrator via file artifacts.
  Agents read each other's outputs via file paths in handoffs.
```

### Data Flow Patterns

| From Agent | To Agent | Data Passed | Mechanism |
|------------|----------|-------------|-----------|
| pm-customer-insight | pm-product-strategist | Persona file paths, VOC themes, JTBD statements | Orchestrator passes file paths in handoff `artifacts` array |
| pm-customer-insight | pm-market-strategist | User persona references for buyer-user alignment | File path references via `cross_refs` frontmatter |
| pm-competitive-analyst | pm-business-analyst | Competitive pricing data, market share estimates | Orchestrator passes file paths in handoff |
| pm-competitive-analyst | pm-market-strategist | Competitive positioning, battle card references | Orchestrator passes file paths in handoff |
| pm-business-analyst | pm-product-strategist | Market sizing, feasibility verdict, investment requirements | File path references via `cross_refs` frontmatter |
| pm-business-analyst | pm-market-strategist | Pricing model, packaging recommendations | Orchestrator passes file paths in handoff |
| pm-product-strategist | pm-market-strategist | Product strategy, feature differentiation points | File path references via `cross_refs` frontmatter |
| pm-product-strategist | pm-business-analyst | Product scope, investment estimation inputs | Orchestrator passes file paths in handoff |

### Handoff Structure

Cross-agent data exchange follows the handoff-v2 schema:

```yaml
handoff:
  from_agent: "pm-customer-insight"
  to_agent: "pm-product-strategist"
  task: "Incorporate validated personas into PRD customer context"
  success_criteria:
    - "PRD references persona IDs from pm-customer-insight output"
    - "JTBD statements from personas appear in PRD problem statement"
  artifacts:
    - "docs/pm-pmm/personas/devops-dave.md"
    - "docs/pm-pmm/voc/q1-2026-themes.md"
  key_findings:
    - "Primary persona: DevOps Dave -- platform engineering lead, 200-1000 emp"
    - "Top JTBD: reduce incident MTTR from 45 min to under 5 min"
    - "3 validated pain points from 12 interviews"
  blockers: []
  confidence: 0.8
  criticality: "C2"
```

### Conflict Resolution

When agents produce conflicting recommendations (e.g., pm-business-analyst says "don't invest" while pm-product-strategist says "critical to roadmap"), the orchestrator:

1. Surfaces both outputs to the user with explicit conflict statement
2. Presents the evidence from each agent
3. Asks the user to decide (P-020: User Decides)
4. Does NOT silently pick a winner

---

## Integration Points with Existing Skills

| # | Skill | Integration Type | Data Flow | Details |
|---|-------|-----------------|-----------|---------|
| 1 | `/worktracker` | Bidirectional | PM/PMM artifacts link to work items via `cross_refs` frontmatter. Roadmap items map to Epics/Features/Stories in work hierarchy. | Artifact IDs (PM-PS-001) appear in worktracker entity `Related Items`. Worktracker entity IDs (FEAT-042) appear in artifact `cross_refs`. |
| 2 | `/adversary` | Unidirectional (artifacts -> critique) | PM/PMM artifacts at C2+ are submitted to `/adversary` for quality review using the 6-dimension weighted composite. | Criticality mapping per artifact type defined in artifact ownership matrix. Minimum 3-iteration creator-critic-revision cycle per H-14. |
| 3 | `/problem-solving` | Unidirectional (research -> agents) | ps-researcher feeds pm-product-strategist and pm-competitive-analyst with external research. ps-analyst supports pm-business-analyst with root cause analysis. | Research artifacts from `/problem-solving` are passed as input context to pm-pmm agents via handoff `artifacts` array. |
| 4 | `/architecture` | Bidirectional | ADR decisions inform technical feasibility inputs to PRDs. pm-product-strategist feeds technical requirements to architecture decisions. | ADR file paths referenced in PRD "Technical Constraints" section. Product requirements referenced in ADR "Context" section. |
| 5 | `/nasa-se` | Unidirectional (PRD -> SE verification) | Requirements traceability flows from pm-product-strategist to SE verification pipelines. PRD requirements map to V&V test cases. | PRD requirements IDs appear in SE requirements traceability matrix. |
| 6 | `/use-case` | Unidirectional (use cases -> slicing) | pm-product-strategist produces use case specifications that feed to `/use-case` for slicing and implementation planning. | Use case file paths passed to `/use-case` skill for decomposition into implementation slices. |

### Integration Trigger Map Entry

The `/pm-pmm` skill will be registered in `mandatory-skill-usage.md` with:

| Detected Keywords | Negative Keywords | Priority | Compound Triggers | Skill |
|---|---|---|---|---|
| product strategy, PRD, product requirements, roadmap, prioritize, RICE, customer insight, persona, journey map, VOC, voice of customer, business case, market sizing, TAM, pricing, unit economics, competitive analysis, battle card, win/loss, GTM, go-to-market, positioning, messaging, MRD, launch plan, product marketing, buyer persona | code review, architecture, engineering, implementation, deployment, testing, CI/CD, infrastructure pricing, cloud pricing, adversarial, transcript | TBD | "product requirements" OR "market sizing" OR "go-to-market" (phrase match) | `/pm-pmm` |

---

## File Organization per H-34

### Dual-File Architecture

Each agent uses the H-34 separation-of-concerns architecture:

**`.md` file (Claude Code runtime)**
- YAML frontmatter: Only official Claude Code fields (`name`, `description`, `model`, `tools`)
- Markdown body: System prompt content with XML-tagged sections (`<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`)

**`.governance.yaml` file (machine-readable governance)**
- Validated against `docs/schemas/agent-governance-v1.schema.json`
- Contains: `version`, `tool_tier`, `identity` (role, expertise, cognitive_mode), `persona`, `capabilities` (forbidden_actions, allowed_tools), `guardrails`, `output`, `constitution`, `validation`

### Constitutional Compliance (H-34/H-35)

Every agent MUST declare:

```yaml
# In .governance.yaml
constitution:
  principles_applied:
    - "P-003"  # No recursive subagents
    - "P-020"  # User authority
    - "P-022"  # No deception

capabilities:
  forbidden_actions:
    - "Spawn recursive subagents (P-003)"
    - "Override user decisions (P-020)"
    - "Misrepresent capabilities or confidence (P-022)"
```

### Worker Agent Constraint

All 5 pm-pmm agents are workers, not orchestrators. Per H-34/H-35:
- No agent includes `Task` in `tools` frontmatter
- No agent is T5 tier
- The Jerry main context orchestrates all multi-agent workflows

---

## References

| Source | Content | Location |
|--------|---------|----------|
| GitHub Issue #123 | Full PM/PMM skill specification | `geekatron/jerry` Issue #123 |
| PS-001-E-001 | Cagan/SVPG Product Operating Model | Research corpus |
| PS-001-E-002 | PM/PMM role practices and competencies | Research corpus |
| PS-001-E-003 | 15 primary artifact specifications | Research corpus |
| PS-001-E-004 | Design synthesis, 5-agent model selection | Research corpus |
| PS-001-E-005 | 18 industry frameworks validated | Research corpus |
| agent-development-standards.md | H-34 dual-file architecture, tool tiers | `.context/rules/agent-development-standards.md` |
| quality-enforcement.md | Quality gate thresholds, criticality levels | `.context/rules/quality-enforcement.md` |
| adversary SKILL.md | Reference skill structure | `skills/adversary/SKILL.md` |

---

*Architecture Version: 1.0.0*
*Source: PROJ-018 PM/PMM Skill, GitHub Issue #123*
*Created: 2026-03-01*
*Phase: Phase 1 Research*
