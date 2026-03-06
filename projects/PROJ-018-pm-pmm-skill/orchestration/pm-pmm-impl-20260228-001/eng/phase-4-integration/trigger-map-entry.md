# Trigger Map Entry for `/pm-pmm`

<!-- VERSION: 1.0.0 | DATE: 2026-03-01 | SOURCE: PROJ-018, Phase 4 Integration | AGENT: eng-phase-4 -->

> Prepared trigger map entry for registration in `.context/rules/mandatory-skill-usage.md`. Follows the 5-column enhanced format per `agent-routing-standards.md` (RT-M-003). This entry is designed for human review before insertion.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Trigger Map Entry](#trigger-map-entry) | The exact row to add to mandatory-skill-usage.md |
| [Keyword Derivation](#keyword-derivation) | Source agent for each keyword |
| [Negative Keyword Rationale](#negative-keyword-rationale) | Why each negative keyword is included |
| [Compound Trigger Design](#compound-trigger-design) | Phrase-match triggers for high-specificity routing |
| [Priority Rationale](#priority-rationale) | Why priority 8 is assigned |
| [Collision Analysis](#collision-analysis) | Disambiguation against all 8 existing skills |
| [H-22 Rule Text Update](#h-22-rule-text-update) | Exact text to add to the H-22 rule |
| [Integration Instructions](#integration-instructions) | Exact insertion point in mandatory-skill-usage.md |

---

## Trigger Map Entry

The following row is to be inserted into the Trigger Map table in `.context/rules/mandatory-skill-usage.md`:

| Detected Keywords | Negative Keywords | Priority | Compound Triggers | Skill |
|---|---|---|---|---|
| product strategy, PRD, product requirements, roadmap, prioritize, RICE, Kano, product vision, north star metric, opportunity solution tree, product kata, JTBD, customer insight, persona, customer interview, journey map, VOC, voice of customer, customer discovery, pain points, churn analysis, NPS, CSAT, CES, business case, financial model, market sizing, TAM, SAM, SOM, pricing model, unit economics, LTV, CAC, NRR, NPV, IRR, break-even, feasibility, revenue model, Van Westendorp, Lean Canvas, Rule of 40, Magic Number, payback period, competitive analysis, battle card, win/loss, competitor, Porter's, SWOT, competitive landscape, differentiation, market intelligence, competitive threat, Blue Ocean, value curve, Crossing the Chasm, GTM, go-to-market, positioning, messaging, MRD, launch plan, sales enablement, buyer persona, product marketing, PLG, product-led growth | code review, architecture, ADR, engineering, implementation, deployment, CI/CD, testing, test coverage, infrastructure pricing, cloud pricing, adversarial, tournament, transcript, VTT, SRT, penetration test, exploit, strategy | 9 | "product requirements" OR "product strategy" OR "market sizing" OR "go-to-market" OR "competitive analysis" OR "business case" OR "buyer persona" (phrase match) | `/pm-pmm` |

---

## Keyword Derivation

All detected keywords are drawn from the 5 agent definitions and SKILL.md activation-keywords.

### From pm-product-strategist

| Keywords | Agent Role Connection |
|----------|----------------------|
| product strategy, PRD, product requirements, roadmap, prioritize, RICE, Kano, product vision, north star metric, opportunity solution tree, product kata, JTBD | Product strategy, PRDs, vision, roadmap prioritization |

### From pm-customer-insight

| Keywords | Agent Role Connection |
|----------|----------------------|
| customer insight, persona, customer interview, journey map, VOC, voice of customer, customer discovery, pain points, churn analysis, NPS, CSAT, CES | User personas, journey maps, VOC research |

### From pm-business-analyst

| Keywords | Agent Role Connection |
|----------|----------------------|
| business case, financial model, market sizing, TAM, SAM, SOM, pricing model, unit economics, LTV, CAC, NRR, NPV, IRR, break-even, feasibility, revenue model, Van Westendorp, Lean Canvas, Rule of 40, Magic Number, payback period | Business cases, market sizing, pricing analysis |

### From pm-competitive-analyst

| Keywords | Agent Role Connection |
|----------|----------------------|
| competitive analysis, battle card, win/loss, competitor, Porter's, SWOT, competitive landscape, differentiation, market intelligence, competitive threat, Blue Ocean, value curve, Crossing the Chasm | Competitive analysis, battle cards, win/loss |

### From pm-market-strategist

| Keywords | Agent Role Connection |
|----------|----------------------|
| GTM, go-to-market, positioning, messaging, MRD, launch plan, sales enablement, buyer persona, product marketing, PLG, product-led growth | GTM plans, MRDs, buyer personas, positioning |

### Keyword Count Summary

| Source Agent | Keyword Count |
|-------------|---------------|
| pm-product-strategist | 12 |
| pm-customer-insight | 12 |
| pm-business-analyst | 19 |
| pm-competitive-analyst | 13 |
| pm-market-strategist | 11 |
| **Total unique keywords** | **67** |

---

## Negative Keyword Rationale

Each negative keyword prevents collision with a specific existing skill.

| Negative Keyword | Collides With | Rationale |
|-----------------|---------------|-----------|
| code review | `/problem-solving`, `/eng-team` | Code review is engineering, not product management |
| architecture | `/architecture` | Architecture decisions belong to /architecture skill |
| ADR | `/architecture` | Architecture Decision Records are /architecture domain |
| engineering | `/eng-team` | Engineering implementation is /eng-team domain |
| implementation | `/eng-team` | Implementation work is /eng-team domain |
| deployment | `/eng-team` | Deployment is /eng-team domain |
| CI/CD | `/eng-team` | Continuous integration/deployment is /eng-team |
| testing | `/eng-team` | Test coverage and testing strategy is /eng-team |
| test coverage | `/eng-team` | Specific testing metric, not product metrics |
| infrastructure pricing | `/eng-team` | Cloud infrastructure pricing is not product pricing |
| cloud pricing | `/eng-team` | Cloud cost analysis is not product pricing analysis |
| adversarial | `/adversary` | Adversarial quality review is /adversary domain |
| tournament | `/adversary` | Tournament scoring is /adversary domain |
| transcript | `/transcript` | Transcript parsing is /transcript domain |
| VTT | `/transcript` | Video text track format is /transcript domain |
| SRT | `/transcript` | Subtitle file format is /transcript domain |
| penetration test | `/red-team` | Penetration testing is /red-team domain |
| exploit | `/red-team` | Exploitation methodology is /red-team domain |
| strategy | `/problem-solving` | Standalone "strategy" is too broad; "product strategy" is the correct compound trigger |

### Special Disambiguation: "strategy"

The word "strategy" alone appears in many contexts (competitive strategy, testing strategy, deployment strategy). The negative keyword `strategy` suppresses `/pm-pmm` routing when "strategy" appears without a product context modifier. However, the compound trigger "product strategy" takes precedence via the Layer 1 routing algorithm's Step 2 (Compound Trigger Specificity Override), ensuring that "product strategy" still routes correctly to `/pm-pmm` even though "strategy" is a negative keyword.

### Special Disambiguation: "persona"

The word "persona" has a routing split within `/pm-pmm`:
- Standalone "persona" or "user persona" routes to **pm-customer-insight** (user personas)
- "buyer persona" routes to **pm-market-strategist** (buying committee personas)

This split is handled by the SKILL.md agent selection hints, not by the trigger map entry (the trigger map routes to the skill; the skill routes to the agent).

### Special Disambiguation: "pricing"

"Pricing" can mean product pricing (pm-business-analyst domain) or infrastructure/cloud pricing (eng-team domain). The negative keywords "infrastructure pricing" and "cloud pricing" suppress `/pm-pmm` when pricing refers to infrastructure costs.

---

## Compound Trigger Design

Compound triggers provide high-specificity routing for phrases that are strongly indicative of PM/PMM work. When a compound trigger matches, it takes precedence over individual keyword matching per the routing algorithm (Step 2: Compound Trigger Specificity Override).

| Compound Trigger | Type | Rationale |
|-----------------|------|-----------|
| "product requirements" | Phrase match | Unambiguous PRD domain; no collision with any existing skill |
| "product strategy" | Phrase match | Unambiguous product strategy; prevents standalone "strategy" collision |
| "market sizing" | Phrase match | Unambiguous business analysis; no collision |
| "go-to-market" | Phrase match | Unambiguous GTM planning; no collision |
| "competitive analysis" | Phrase match | Unambiguous competitive intelligence; no collision |
| "business case" | Phrase match | Unambiguous financial analysis; no collision |
| "buyer persona" | Phrase match | Unambiguous market strategy; disambiguates from user "persona" |

---

## Priority Rationale

**Assigned Priority: 9**

Priority 9 avoids collision with `/ast` (priority 8 in current map) and provides a clear 2-level gap from `/adversary` (priority 7). `/eng-team` moves to priority 10 and `/red-team` to priority 11.

### Priority Ordering Context

| Priority | Skill | Rationale |
|----------|-------|-----------|
| 1 | `/orchestration` | Coordinates other skills; must route first |
| 2 | `/transcript` | Narrow domain; false positives rare |
| 3 | `/saucer-boy` | Conversational; rarely conflicts |
| 4 | `/saucer-boy-framework-voice` | Narrow voice domain |
| 5 | `/nasa-se` | Broad domain; many overlaps with /problem-solving |
| 6 | `/problem-solving` | Broadest scope; default research/analysis |
| 7 | `/adversary` | Specialized quality assessment |
| 8 | `/ast` | Frontmatter and markdown structural analysis |
| **9** | **`/pm-pmm`** | **Specialized PM/PMM domain; 67 keywords provide sufficient specificity; 2-level gap from /adversary** |
| 10 | `/eng-team` | Engineering methodology; broad but distinct domain |
| 11 | `/red-team` | Offensive security; narrow and distinct |

**Why priority 9 (not lower):** PM/PMM keywords are domain-specific and unlikely to be confused with general research requests. The 67 keywords and 7 compound triggers provide strong specificity. Priority 9 ensures `/pm-pmm` does not capture requests that should go to `/problem-solving` (priority 6) or `/adversary` (priority 7), and provides a 2-level gap from `/adversary` per the routing algorithm's Step 3 disambiguation threshold.

**Why priority 9 (not higher):** PM/PMM work often involves research phases that could trigger `/problem-solving`. The higher priority number (lower routing priority) ensures that when "research" and "product strategy" co-occur, the compound trigger "product strategy" takes precedence via specificity, not priority. Priority 9 also avoids the collision with `/ast` at priority 8.

---

## Collision Analysis

### Existing Skill Collision Assessment

| Existing Skill | Collision Risk | Shared Keywords | Mitigation |
|---------------|---------------|-----------------|------------|
| `/problem-solving` | Medium | "research", "analyze", "investigate", "evaluate", "compare" | Negative keyword "strategy" on /pm-pmm suppresses standalone usage. Compound trigger "product strategy" overrides via specificity. /problem-solving negative keywords already suppress on "persona" and "voice". |
| `/nasa-se` | Low | "requirements" | "product requirements" compound trigger disambiguates. /nasa-se owns technical requirements, V&V, specifications. /pm-pmm owns product requirements (PRDs). |
| `/adversary` | Low | "competitive" (contextual) | "competitive analysis" in /pm-pmm is market competitive intelligence. "adversarial" in /adversary is quality review. Negative keyword "adversarial" on /pm-pmm prevents collision. |
| `/architecture` | Low | "strategy" (contextual) | Negative keywords "architecture", "ADR" on /pm-pmm. Compound trigger "product strategy" disambiguates from architecture strategy. |
| `/eng-team` | Medium | "pricing" (contextual) | Negative keywords "infrastructure pricing", "cloud pricing" on /pm-pmm. Product pricing routes to /pm-pmm; infrastructure pricing routes to /eng-team. |
| `/transcript` | None | None | No keyword overlap. |
| `/saucer-boy` | None | None | No keyword overlap. |
| `/red-team` | None | None | Negative keywords "penetration test", "exploit" on /pm-pmm prevent any theoretical collision. |
| `/orchestration` | Low | "plan" (contextual) | "plan" alone does not trigger /pm-pmm (not in keyword list). "launch plan" and "GTM plan" are specific enough. /orchestration owns multi-phase workflow coordination. |
| `/ast` | None | None | No keyword overlap. `/ast` handles frontmatter extraction and markdown structural analysis. |

### No False Positive Assessment

| Test Request | Expected Routing | Would /pm-pmm False-Trigger? |
|-------------|-----------------|------------------------------|
| "Review this code for bugs" | /problem-solving | No -- "code review" is negative keyword |
| "Create an ADR for this architecture decision" | /architecture | No -- "architecture" and "ADR" are negative keywords |
| "Run adversarial quality review on this deliverable" | /adversary | No -- "adversarial" is negative keyword |
| "Parse this meeting transcript" | /transcript | No -- "transcript" is negative keyword |
| "Estimate cloud pricing for our infrastructure" | /eng-team | No -- "cloud pricing" is negative keyword |
| "Run a penetration test on the API" | /red-team | No -- "penetration test" is negative keyword |
| "Help me research why this deployment failed" | /problem-solving | No -- "deployment" is negative keyword |
| "Break this project into phases with quality gates" | /orchestration | No -- no /pm-pmm keywords match |
| "Write a PRD for the onboarding feature" | /pm-pmm | Yes (correct) -- "PRD" is positive keyword |
| "Create personas for our engineering customers" | /pm-pmm | Yes (correct) -- "personas" is positive keyword |
| "Help me with our pricing strategy" | /pm-pmm | Yes (correct) -- "pricing" is positive keyword (not "infrastructure pricing" or "cloud pricing") |

---

## H-22 Rule Text Update

Add the following to the H-22 rule text in `mandatory-skill-usage.md`:

**Current text (append to):**

```
MUST invoke `/pm-pmm` for product management and product marketing work including product
strategy (PRDs, vision, roadmaps), customer insight (personas, journey maps, VOC), business
analysis (business cases, market sizing, pricing), competitive intelligence (battle cards,
win/loss), and go-to-market planning (GTM plans, positioning, MRDs, buyer personas).
```

---

## Integration Instructions

### Insertion Point

Add the `/pm-pmm` row to the Trigger Map table in `.context/rules/mandatory-skill-usage.md`, after the `/ast` entry (priority 8) and before the `/eng-team` entry (priority 10, adjusted from 9 to accommodate `/pm-pmm` at priority 9).

### Exact Row to Insert

```markdown
| product strategy, PRD, product requirements, roadmap, prioritize, RICE, Kano, product vision, north star metric, opportunity solution tree, product kata, JTBD, customer insight, persona, customer interview, journey map, VOC, voice of customer, customer discovery, pain points, churn analysis, NPS, CSAT, CES, business case, financial model, market sizing, TAM, SAM, SOM, pricing model, unit economics, LTV, CAC, NRR, NPV, IRR, break-even, feasibility, revenue model, Van Westendorp, Lean Canvas, Rule of 40, Magic Number, payback period, competitive analysis, battle card, win/loss, competitor, Porter's, SWOT, competitive landscape, differentiation, market intelligence, competitive threat, Blue Ocean, value curve, Crossing the Chasm, GTM, go-to-market, positioning, messaging, MRD, launch plan, sales enablement, buyer persona, product marketing, PLG, product-led growth | code review, architecture, ADR, engineering, implementation, deployment, CI/CD, testing, test coverage, infrastructure pricing, cloud pricing, adversarial, tournament, transcript, VTT, SRT, penetration test, exploit, strategy | 9 | "product requirements" OR "product strategy" OR "market sizing" OR "go-to-market" OR "competitive analysis" OR "business case" OR "buyer persona" (phrase match) | `/pm-pmm` |
```

### L2-REINJECT Update

Add `/pm-pmm` to the L2-REINJECT comment at the top of `mandatory-skill-usage.md`:

```html
<!-- L2-REINJECT: rank=6, content="Proactive skill invocation REQUIRED (H-22). /problem-solving for research. /nasa-se for design. /orchestration for workflows. /transcript for transcript parsing and meeting notes. /adversary for standalone adversarial reviews, tournament scoring, formal strategy application. /ast for frontmatter extraction and entity validation (H-33). /eng-team for secure engineering, threat modeling, DevSecOps. /red-team for penetration testing, offensive security, engagement methodology. /pm-pmm for product strategy, customer insight, business analysis, competitive intelligence, and GTM planning." -->
```

---

*Trigger Map Entry Version: 1.0.0*
*Source: PROJ-018 PM/PMM Skill, Phase 4 Integration*
*Created: 2026-03-01*
