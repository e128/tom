# Multi-Agent Workflow Patterns

<!-- VERSION: 1.0.0 | DATE: 2026-03-01 | SOURCE: PROJ-018, Phase 4 Integration | AGENT: eng-phase-4 -->

> Documents 7 multi-agent workflow patterns showing how the 5 PM/PMM agents collaborate through orchestrator-mediated data flows. Each pattern includes agent sequence, data flow, expected artifacts, criticality level, and a concrete example user prompt.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Pattern Overview](#pattern-overview) | Summary table of all 7 patterns |
| [Pattern 1: Full Product Strategy](#pattern-1-full-product-strategy) | All 5 agents in sequence |
| [Pattern 2: Competitive Intelligence Brief](#pattern-2-competitive-intelligence-brief) | pm-competitive-analyst + pm-market-strategist |
| [Pattern 3: Business Case Development](#pattern-3-business-case-development) | pm-business-analyst + pm-product-strategist |
| [Pattern 4: Customer-Driven PRD](#pattern-4-customer-driven-prd) | pm-customer-insight then pm-product-strategist |
| [Pattern 5: Go-to-Market Launch](#pattern-5-go-to-market-launch) | pm-market-strategist + pm-competitive-analyst + pm-business-analyst |
| [Pattern 6: Quick Competitive Scan](#pattern-6-quick-competitive-scan) | pm-competitive-analyst in discovery mode |
| [Pattern 7: Pricing Strategy](#pattern-7-pricing-strategy) | pm-business-analyst with Van Westendorp + Good-Better-Best |
| [Pattern Composition Rules](#pattern-composition-rules) | How to combine and extend patterns |
| [Error Handling](#error-handling) | Failure recovery, partial results, user decision authority |
| [P-003 Compliance Note](#p-003-compliance-note) | Orchestration model for all patterns |

---

## Pattern Overview

| # | Pattern | Agents | Artifacts Produced | Criticality | Duration Estimate |
|---|---------|--------|--------------------|-------------|-------------------|
| 1 | Full Product Strategy | All 5 | 5-7 artifacts | C3 | Multi-session |
| 2 | Competitive Intelligence Brief | 2 | 2-3 artifacts | C2 | Single session |
| 3 | Business Case Development | 2 | 2-3 artifacts | C3 | Single session |
| 4 | Customer-Driven PRD | 2 | 2-3 artifacts | C2 | Single session |
| 5 | Go-to-Market Launch | 3 | 3-4 artifacts | C3 | Multi-session |
| 6 | Quick Competitive Scan | 1 | 1 artifact | C1 | Single session |
| 7 | Pricing Strategy | 1 | 1-2 artifacts | C2 | Single session |

---

## Pattern 1: Full Product Strategy

**Purpose:** Comprehensive product strategy development spanning customer research, competitive analysis, business viability, product requirements, and go-to-market planning. This is the "full stack" PM/PMM workflow.

### Agent Sequence and Data Flow

```
Step 1: pm-customer-insight
  Input:  Customer segment description, interview data (if available)
  Output: User personas (PM-CI-*), VOC themes
    |
    v (persona file paths, JTBD statements)
Step 2: pm-competitive-analyst
  Input:  Market/competitor description, product differentiation points
  Output: Competitive analysis (PM-CA-*), battle cards
    |
    v (competitive landscape, pricing ranges)
Step 3: pm-business-analyst
  Input:  Competitive pricing data (from Step 2), customer WTP (from Step 1)
  Output: Market sizing (PM-BA-*), business case
    |
    v (TAM/SAM/SOM, feasibility verdict)
Step 4: pm-product-strategist
  Input:  Personas (Step 1), competitive data (Step 2), market sizing (Step 3)
  Output: PRD (PM-PS-*), product vision, roadmap
    |
    v (product strategy, feature differentiation)
Step 5: pm-market-strategist
  Input:  Product strategy (Step 4), competitive positioning (Step 2),
          pricing model (Step 3), user personas (Step 1)
  Output: GTM plan (PM-MS-*), buyer personas
```

### Expected Artifacts

| Step | Agent | Artifact | Sensitivity |
|------|-------|----------|-------------|
| 1 | pm-customer-insight | User Personas | confidential |
| 1 | pm-customer-insight | VOC Research Report | confidential |
| 2 | pm-competitive-analyst | Competitive Analysis | restricted |
| 3 | pm-business-analyst | Market Sizing (TAM/SAM/SOM) | restricted |
| 3 | pm-business-analyst | Business Case | restricted |
| 4 | pm-product-strategist | PRD | internal |
| 4 | pm-product-strategist | Product Vision | internal |
| 5 | pm-market-strategist | GTM Plan | internal |

### Criticality: C3

Rationale: Product vision and business case artifacts are C3. Multi-agent workflow with 5+ artifacts produces significant business-impact outputs that take more than 1 day to reverse.

### Example User Prompt

```
I'm building a developer platform for mid-market companies (200-1000 employees) that
automates service onboarding. I need the full product strategy: understand our customers,
analyze the competitive landscape (Backstage, Port, Cortex are main competitors), validate
the business case, write the PRD, and plan the go-to-market.

Start with customer personas based on platform engineering leads, then build the competitive
analysis, assess market sizing, create the PRD grounded in persona data, and finally plan
the GTM launch. Use discovery mode for all artifacts initially.
```

---

## Pattern 2: Competitive Intelligence Brief

**Purpose:** Map the competitive landscape and translate competitive positioning into messaging differentiation. Used when entering a new market or preparing for a competitive deal.

### Agent Sequence and Data Flow

```
Step 1: pm-competitive-analyst
  Input:  Market name, specific competitors, product context
  Output: Competitive analysis (Porter's Five Forces, SWOT, Blue Ocean)
          Battle cards with talk tracks
    |
    v (competitive positioning, threat assessment, battle card references)
Step 2: pm-market-strategist
  Input:  Competitive positioning (Step 1), product context
  Output: Positioning framework (Dunford 5-step)
          Messaging hierarchy with competitive differentiation
```

### Expected Artifacts

| Step | Agent | Artifact | Sensitivity |
|------|-------|----------|-------------|
| 1 | pm-competitive-analyst | Competitive Analysis | restricted |
| 1 | pm-competitive-analyst | Battle Cards | restricted |
| 2 | pm-market-strategist | GTM Plan (positioning section) | internal |

### Criticality: C2

Rationale: Competitive intelligence is important but reversible within 1 day. Battle cards have a 30-day refresh cycle by design.

### Example User Prompt

```
We're preparing for a head-to-head deal against Backstage and Port in the internal developer
platform space. Create a competitive analysis using Porter's Five Forces and Blue Ocean value
curves, then build battle cards for both competitors with talk tracks and objection handling.
After that, create Dunford positioning that differentiates us based on the competitive findings.
```

---

## Pattern 3: Business Case Development

**Purpose:** Validate financial viability of a product initiative by combining market sizing with product scope to produce a stakeholder-ready business case. Used before committing significant engineering investment.

### Agent Sequence and Data Flow

```
Step 1: pm-business-analyst
  Input:  Product/market description, financial constraints
  Output: Market sizing (TAM/SAM/SOM)
          Business case (Lean Canvas, unit economics, NPV)
    |
    v (feasibility verdict, investment requirements, market size)
Step 2: pm-product-strategist
  Input:  Feasibility verdict (Step 1), market sizing data
  Output: PRD scoped to validated market opportunity
          Roadmap prioritized by financial viability
```

### Expected Artifacts

| Step | Agent | Artifact | Sensitivity |
|------|-------|----------|-------------|
| 1 | pm-business-analyst | Market Sizing | restricted |
| 1 | pm-business-analyst | Business Case | restricted |
| 2 | pm-product-strategist | PRD | internal |
| 2 | pm-product-strategist | Roadmap | internal |

### Criticality: C3

Rationale: Business case is C3 (high-impact investment decision). PRD scope is directly constrained by financial viability.

### Example User Prompt

```
Our VP of Product wants a business case for expanding our developer platform to the enterprise
segment (1000+ employees). First, calculate TAM/SAM/SOM for the enterprise IDP market using
both top-down and bottom-up approaches. Then build a business case with NPV analysis, SaaS
unit economics (LTV:CAC, NRR, payback period), and a Lean Canvas.

If the business case is favorable, create a PRD for the enterprise expansion scoped to the
validated market opportunity. Our investment ceiling is $5M for year 1, and we need payback
within 24 months.
```

---

## Pattern 4: Customer-Driven PRD

**Purpose:** Ground product requirements in validated customer evidence. Prevents the most common PM failure: building a PRD based on assumptions rather than customer data.

### Agent Sequence and Data Flow

```
Step 1: pm-customer-insight
  Input:  Customer segment, interview transcripts (if available)
  Output: User personas with JTBD statements
          VOC research report with themes and opportunity scores
    |
    v (persona file paths, JTBD statements, top pain points)
Step 2: pm-product-strategist
  Input:  Personas (Step 1), VOC themes, JTBD statements
  Output: PRD with JTBD-grounded problem statement
          RICE prioritization informed by customer importance scores
          Opportunity Solution Tree rooted in customer outcomes
```

### Expected Artifacts

| Step | Agent | Artifact | Sensitivity |
|------|-------|----------|-------------|
| 1 | pm-customer-insight | User Personas | confidential |
| 1 | pm-customer-insight | VOC Research Report | confidential |
| 2 | pm-product-strategist | PRD | internal |

### Criticality: C2

Rationale: PRD is C2. The cross-agent handoff from customer insight to product strategy is the core value of this pattern.

### Example User Prompt

```
I have interview transcripts from 12 platform engineering leads at mid-market companies.
Build JTBD-oriented personas from this data, including functional, emotional, and social jobs
with opportunity scoring. Then create a PRD for our self-service onboarding feature that is
grounded in the persona data -- the problem statement should reference specific JTBD statements,
and the RICE prioritization should use customer importance scores for the Impact dimension.

Interview transcripts are at: docs/research/interviews/
```

---

## Pattern 5: Go-to-Market Launch

**Purpose:** Comprehensive go-to-market planning that combines competitive positioning, pricing strategy, and customer acquisition planning. Used when preparing a product for market launch.

### Agent Sequence and Data Flow

```
Step 1: pm-competitive-analyst
  Input:  Market, competitors, product differentiation
  Output: Competitive positioning and battle cards
    |
    v (competitive pricing, differentiation points)
Step 2: pm-business-analyst
  Input:  Competitive pricing (Step 1), target segment data
  Output: Pricing strategy (Van Westendorp, Good-Better-Best tiers)
    |
    v (pricing model, packaging recommendations)
Step 3: pm-market-strategist
  Input:  Competitive positioning (Step 1), pricing model (Step 2),
          product strategy context
  Output: Full GTM plan (Dunford positioning, Lauchengco PMM model,
          T1/T2/T3 launch tiers, channel plan)
          MRD with market requirements
          Buyer personas for buying committee
```

### Expected Artifacts

| Step | Agent | Artifact | Sensitivity |
|------|-------|----------|-------------|
| 1 | pm-competitive-analyst | Competitive Analysis | restricted |
| 1 | pm-competitive-analyst | Battle Cards | restricted |
| 2 | pm-business-analyst | Business Case (pricing section) | restricted |
| 3 | pm-market-strategist | GTM Plan | internal |
| 3 | pm-market-strategist | MRD | internal |
| 3 | pm-market-strategist | Buyer Personas | internal |

### Criticality: C3

Rationale: GTM plan is C3 (high business impact, competitive exposure risk). Pricing strategy directly affects revenue.

### Example User Prompt

```
We're launching our enterprise developer platform in Q3 2026. I need a complete go-to-market
plan. Start by analyzing the competitive landscape -- Backstage, Port, Cortex, and OpsLevel
are the key competitors. Then develop a pricing strategy using Van Westendorp to find the
optimal price point and design Good-Better-Best tiers.

Finally, create the full GTM plan with Dunford positioning, a Lauchengco 4-role PMM framework,
T1/T2/T3 launch tiers, channel strategy, and PMF survey design. Also create buyer personas
for the enterprise buying committee: economic buyer (VP Eng), technical evaluator (Staff SRE),
and champion (Platform Lead).
```

---

## Pattern 6: Quick Competitive Scan

**Purpose:** Rapid competitive landscape assessment in discovery mode. Used for early-stage market evaluation or preparing for a competitive conversation. Single-agent, lowest overhead.

### Agent Sequence and Data Flow

```
Step 1: pm-competitive-analyst (discovery mode)
  Input:  Market name, known competitors
  Output: Quick Porter's Five Forces assessment
          Preliminary SWOT
          Top 3 competitor profiles with TALC positions
          Key assumptions to validate
```

### Expected Artifacts

| Step | Agent | Artifact | Sensitivity |
|------|-------|----------|-------------|
| 1 | pm-competitive-analyst | Competitive Analysis (discovery) | restricted |

### Criticality: C1

Rationale: Discovery-mode competitive scan is a lightweight, reversible artifact. 1-2 pages of hypothesis-level assessment.

### Example User Prompt

```
Give me a quick competitive scan of the internal developer platform market. I know about
Backstage, Port, and Cortex as competitors. Run a Porter's Five Forces assessment and
a preliminary SWOT. I need this in discovery mode -- just the key competitive dynamics
and top 3 threat profiles. I'll validate the assumptions later.
```

---

## Pattern 7: Pricing Strategy

**Purpose:** Dedicated pricing analysis using Van Westendorp price sensitivity and Good-Better-Best tiered pricing design. Used when defining or revising product pricing.

### Agent Sequence and Data Flow

```
Step 1: pm-business-analyst
  Input:  Product description, target segment, competitive pricing data (if available),
          customer willingness-to-pay signals (if available)
  Output: Van Westendorp PSM analysis
          - Four price-point questions structured for target segment
          - PMC, PME, IDP, OPP intersection points
          - Acceptable price range
          Good-Better-Best pricing tiers
          - Feature-to-tier mapping
          - Tier pricing with 2-2.5x multiplier
          - Expected revenue mix (10/70/20 or 20/60/20)
```

### Expected Artifacts

| Step | Agent | Artifact | Sensitivity |
|------|-------|----------|-------------|
| 1 | pm-business-analyst | Business Case (pricing section) | restricted |

### Criticality: C2

Rationale: Pricing decisions have direct revenue impact but are reversible within 1 day (can be revised before external publication).

### Example User Prompt

```
Help me define pricing for our developer platform. Run a Van Westendorp price sensitivity
analysis for our target segment (mid-market platform engineering teams, 200-1000 employees).
The main competitive alternative is Backstage (free/open-source) with paid support from
Spotify, and Port which charges ~$30-50K ACV.

Then design Good-Better-Best pricing tiers. Map our features to tiers based on value metrics:
Good = basic service catalog, Better = automated onboarding + observability, Best = compliance
automation + enterprise SSO + premium support. Calculate the expected revenue mix and
cross-reference against the Van Westendorp acceptable price range.
```

---

## Pattern Composition Rules

Patterns can be composed for more complex workflows.

### Composition Guidelines

| Rule | Guidance |
|------|---------|
| Start with customer data when available | Patterns 1 and 4 begin with pm-customer-insight because customer evidence improves all downstream artifacts |
| Competitive data feeds both pricing and positioning | pm-competitive-analyst output is consumed by both pm-business-analyst (pricing) and pm-market-strategist (positioning) |
| Business viability before product scope | Pattern 3 validates financial viability before committing to PRD scope |
| Discovery mode first for all initial runs | All patterns default to discovery mode; upgrade to delivery after validation |
| Maximum 2 skills combined before escalation | Per RT-M-007, if a pattern requires 3+ skills in complex coordination, use `/orchestration` |

### Pattern Extension

| Base Pattern | Extension | Resulting Flow |
|-------------|-----------|----------------|
| Pattern 4 (Customer-Driven PRD) | + Pattern 2 (Competitive Brief) | Customer research -> Competitive analysis -> PRD with competitive context |
| Pattern 7 (Pricing Strategy) | + Pattern 5 (GTM Launch) | Pricing analysis -> Full GTM plan with validated pricing |
| Pattern 6 (Quick Scan) | -> Pattern 2 (Full Competitive) | Discovery scan -> Delivery-mode competitive brief after validation |

---

## Error Handling

All multi-agent workflow patterns are subject to the following error handling rules. These ensure graceful degradation when an intermediate agent fails during a workflow sequence.

### Partial Result Presentation (H-31)

If an intermediate agent fails (produces no output, exceeds context budget, or encounters an unrecoverable error), the orchestrator MUST present all partial results accumulated up to the failure point to the user. The user receives what was successfully produced rather than losing all prior work.

### Downstream Agent Suppression

Downstream agents in the workflow chain MUST NOT execute on failed upstream output. If Step N fails, Steps N+1 through the end of the sequence are suspended. The orchestrator does not attempt to continue the chain with missing or corrupted intermediate data, as this would produce unreliable downstream artifacts.

### User Decision Authority (P-020)

When an agent failure occurs, the orchestrator MUST present the user with three options per P-020 (User Authority):

1. **Retry** -- Re-execute the failed step with the same or modified inputs
2. **Skip** -- Skip the failed step and continue the workflow from the next step (the user accepts responsibility for missing intermediate data)
3. **Abort** -- Terminate the workflow and retain all partial results produced before the failure

The orchestrator MUST NOT make this decision autonomously. The user decides the recovery path.

### Error Handling by Pattern

| Pattern | Failure at Step | Partial Results Available | User Options |
|---------|----------------|--------------------------|--------------|
| 1 (Full Product Strategy) | Any step 1-5 | All artifacts from completed prior steps | Retry / Skip / Abort |
| 2 (Competitive Intelligence Brief) | Step 1 | None | Retry / Abort |
| 2 (Competitive Intelligence Brief) | Step 2 | Competitive analysis, battle cards | Retry / Skip / Abort |
| 3 (Business Case Development) | Step 1 | None | Retry / Abort |
| 3 (Business Case Development) | Step 2 | Market sizing, business case | Retry / Skip / Abort |
| 4 (Customer-Driven PRD) | Step 1 | None | Retry / Abort |
| 4 (Customer-Driven PRD) | Step 2 | Personas, VOC report | Retry / Skip / Abort |
| 5 (Go-to-Market Launch) | Any step 1-3 | All artifacts from completed prior steps | Retry / Skip / Abort |
| 6 (Quick Competitive Scan) | Step 1 | None | Retry / Abort |
| 7 (Pricing Strategy) | Step 1 | None | Retry / Abort |

---

## P-003 Compliance Note

All patterns are orchestrated by the **Jerry main context** (Claude session). No agent invokes another agent. The main context:

1. Selects the first agent based on user request and pattern
2. Passes artifact file paths between agents via handoff `artifacts` arrays
3. Manages step transitions -- each agent writes to the filesystem, next agent reads from filesystem
4. Resolves conflicts when agents produce contradictory recommendations (P-020: present both, user decides)

```
MAIN CONTEXT (orchestrator)
    |
    +-- pm-customer-insight (Step 1)
    |     writes: docs/pm-pmm/personas/...
    |
    +-- pm-competitive-analyst (Step 2)
    |     reads: product context
    |     writes: docs/pm-pmm/competitive-analysis/...
    |
    +-- pm-business-analyst (Step 3)
    |     reads: competitive pricing from Step 2
    |     writes: docs/pm-pmm/business-case/...
    |
    +-- pm-product-strategist (Step 4)
    |     reads: personas from Step 1, market sizing from Step 3
    |     writes: docs/pm-pmm/prd/...
    |
    +-- pm-market-strategist (Step 5)
          reads: all prior artifacts
          writes: docs/pm-pmm/gtm-plan/...
```

---

*Workflow Patterns Version: 1.0.0*
*Source: PROJ-018 PM/PMM Skill, Phase 4 Integration*
*Created: 2026-03-01*
