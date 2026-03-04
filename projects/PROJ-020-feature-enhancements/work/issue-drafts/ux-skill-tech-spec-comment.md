# Technical Specification: `/user-experience` Skill

> Follow-up comment to the `/user-experience` enhancement issue. This document contains the detailed technical specification for implementation.

---

## 1. Sub-Skill Specification Table

Complete specification for all 10 sub-skills and the parent orchestrator.

### 1.1 Parent Orchestrator

| Attribute | Value |
|-----------|-------|
| **Skill Name** | `/user-experience` |
| **Primary Agent** | `ux-orchestrator` |
| **Cognitive Mode** | Integrative |
| **Tool Tier** | T5 (Full -- requires Task tool for sub-skill delegation) |
| **Model** | Opus (complex routing decisions across 10 sub-skills) |
| **Required MCP** | None (routing logic does not require external tool access) |
| **Wave** | N/A (deployed first, before Wave 1) |

### 1.2 Sub-Skill Agent Specifications

| # | Sub-Skill | Primary Agent | Cognitive Mode | Tool Tier | Required MCP | Enhancement MCP | Wave | Verified Score |
|---|-----------|--------------|----------------|-----------|-------------|-----------------|------|----------------|
| 1 | `/ux-heuristic-eval` | `ux-heuristic-evaluator` | Systematic | T3 | Figma | Storybook | 1 | 9.25 |
| 2 | `/ux-jtbd` | `ux-jtbd-analyst` | Divergent | T3 | None | Miro | 1 | 8.05 |
| 3 | `/ux-lean-ux` | `ux-lean-ux-facilitator` | Systematic | T3 | Miro | Figma, Hotjar (Bridge) | 2 | 8.25 |
| 4 | `/ux-heart-metrics` | `ux-heart-analyst` | Systematic | T2 | None | Analytics API, Hotjar (Bridge) | 2 | 8.30 |
| 5 | `/ux-atomic-design` | `ux-atomic-architect` | Systematic | T3 | Storybook | Zeroheight, Figma | 3 | 8.55 |
| 6 | `/ux-inclusive-design` | `ux-inclusive-evaluator` | Systematic | T3 | Figma | Storybook, Context7 | 3 | 8.00 |
| 7 | `/ux-behavior-design` | `ux-behavior-diagnostician` | Convergent | T2 | None | Miro, Hotjar (Bridge) | 4 | 7.45 |
| 8 | `/ux-kano-model` | `ux-kano-analyst` | Convergent | T2 | None | Miro | 4 | 7.50 |
| 9 | `/ux-design-sprint` | `ux-sprint-facilitator` | Systematic | T3 | Miro, Figma | Whimsical | 5 | 8.65 |
| 10 | `/ux-ai-first-design` | `ux-ai-design-guide` | Divergent | T3 | Figma | Storybook, Context7 | 5 (COND) | 7.80 (P) |

### 1.3 Cognitive Mode Rationale

| Mode | Applied To | Why |
|------|-----------|-----|
| Systematic | Heuristic Eval, Lean UX, HEART, Atomic Design, Inclusive Design, Design Sprint | Step-by-step protocol with defined outputs per step; checklist execution pattern |
| Divergent | JTBD, AI-First Design | Explores broadly to discover user jobs or emerging AI interaction patterns |
| Convergent | Behavior Design, Kano Model | Narrows from behavioral data to diagnosis (Fogg); narrows from survey data to priority classification (Kano) |
| Integrative | Parent Orchestrator | Combines user context signals with routing logic to select the right sub-skill |

### 1.4 Agent Naming Convention

All agents follow the `ux-{framework-slug}` prefix pattern per AD-M-001. Each agent name describes the role, not just the framework:

| Agent | Role Description | Why Not Just Framework Name |
|-------|-----------------|---------------------------|
| `ux-heuristic-evaluator` | Evaluates designs against heuristics | "ux-nielsen" would not convey the evaluation action |
| `ux-jtbd-analyst` | Analyzes job-to-be-done structures | "ux-jtbd" alone is ambiguous (researcher vs. analyst) |
| `ux-lean-ux-facilitator` | Facilitates Lean UX hypothesis cycles | Lean UX involves facilitation, not just analysis |
| `ux-heart-analyst` | Analyzes HEART metrics data | HEART involves data analysis, not evaluation |
| `ux-atomic-architect` | Architects component hierarchies | Atomic Design is architecture work, not evaluation |
| `ux-inclusive-evaluator` | Evaluates accessibility compliance | Inclusive Design is primarily evaluative |
| `ux-behavior-diagnostician` | Diagnoses behavioral bottlenecks | Fogg model is diagnostic, not evaluative |
| `ux-kano-analyst` | Analyzes Kano survey classifications | Kano involves data analysis and classification |
| `ux-sprint-facilitator` | Facilitates Design Sprint process | Design Sprint is a facilitated process |
| `ux-ai-design-guide` | Guides AI-specific design decisions | AI-First Design is guidance-oriented |

---

## 2. MCP Integration Map

### 2.1 Required vs Enhancement Dependencies

| MCP Server | Type | Required By | Enhances | Total Connections |
|-----------|------|-------------|----------|-------------------|
| **Figma** | Official | `/ux-heuristic-eval`, `/ux-design-sprint`, `/ux-inclusive-design`, `/ux-ai-first-design` | `/ux-atomic-design`, `/ux-lean-ux` | 6 |
| **Miro** | Official | `/ux-design-sprint`, `/ux-lean-ux` | `/ux-jtbd`, `/ux-behavior-design`, `/ux-kano-model` | 5 |
| **Storybook** | Official Addon | `/ux-atomic-design` | `/ux-heuristic-eval`, `/ux-inclusive-design`, `/ux-ai-first-design` | 4 |
| **Zeroheight** | Official | (none) | `/ux-atomic-design` | 1 |
| **Hotjar** | Bridge (Zapier) | (none) | `/ux-heart-metrics`, `/ux-lean-ux`, `/ux-behavior-design` | 3 |
| **Whimsical** | Community | (none) | `/ux-design-sprint` | 1 |

### 2.2 Sub-Skill MCP Dependency Matrix

| Sub-Skill | Figma | Miro | Storybook | Zeroheight | Hotjar | Whimsical |
|-----------|-------|------|-----------|------------|--------|-----------|
| `/ux-heuristic-eval` | **REQ** | -- | ENH | -- | -- | -- |
| `/ux-jtbd` | -- | ENH | -- | -- | -- | -- |
| `/ux-lean-ux` | ENH | **REQ** | -- | -- | ENH | -- |
| `/ux-heart-metrics` | -- | -- | -- | -- | ENH | -- |
| `/ux-atomic-design` | ENH | -- | **REQ** | ENH | -- | -- |
| `/ux-inclusive-design` | **REQ** | -- | ENH | -- | -- | -- |
| `/ux-behavior-design` | -- | ENH | -- | -- | ENH | -- |
| `/ux-kano-model` | -- | ENH | -- | -- | -- | -- |
| `/ux-design-sprint` | **REQ** | **REQ** | -- | -- | -- | ENH |
| `/ux-ai-first-design` | **REQ** | -- | ENH | -- | -- | -- |

**REQ** = Required (degraded mode + explicit error on failure). **ENH** = Enhancement (cosmetic limitation on failure).

### 2.3 Figma Dependency Risk Profile

Figma is the highest-risk MCP dependency:

| Metric | Value |
|--------|-------|
| Sub-skills requiring Figma | 4 (Heuristic Eval, Design Sprint, Inclusive Design, AI-First Design) |
| Sub-skills enhanced by Figma | 2 (Atomic Design, Lean UX) |
| Total Figma connections | 6 of 10 sub-skills |
| Single-point-of-failure severity | HIGH |

**Documented fallback paths:**

| Sub-Skill | Non-Figma Fallback |
|-----------|-------------------|
| `/ux-heuristic-eval` | Screenshot-input mode: user provides design screenshots as image inputs |
| `/ux-design-sprint` | Miro-only mode: sprint exercises in Miro; manual prototype reference |
| `/ux-inclusive-design` | Screenshot-input mode: manual component screenshots for evaluation |
| `/ux-ai-first-design` | Manual design description: text-based interaction pattern analysis |
| `/ux-atomic-design` | Storybook-primary: Storybook is the required MCP; Figma is enhancement only |
| `/ux-lean-ux` | Miro-primary: Miro is the required MCP; Figma is enhancement only |

### 2.4 Cost Tiers

| Tier | Monthly Cost | Sub-Skills Available | Configuration |
|------|-------------|---------------------|---------------|
| **Free** | $0 | HEART, JTBD, Kano, Behavior Design (+ Storybook for Atomic Design) | No MCP servers required for core function |
| **Minimal** | ~$46 | + Heuristic Eval, Design Sprint, Lean UX, Inclusive Design, AI-First Design | Figma Professional ($15/editor) + Miro Team ($8/member) for 2-person team |
| **Full Enhancement** | ~$145-245 | All 10 with full enhancement MCPs | + Zeroheight ($99/mo) + Hotjar (variable) |

---

## 3. Wave Deployment Plan

### 3.1 Wave Definitions

| Wave | Name | Sub-Skills | Entry Criteria | Bypass Condition |
|------|------|-----------|----------------|-----------------|
| **0** | Foundation | Parent orchestrator only | N/A | N/A |
| **1** | Zero-Dependency | `/ux-heuristic-eval`, `/ux-jtbd` | KICKOFF-SIGNOFF.md completed with all MCP ownership assignments | N/A (first wave) |
| **2** | Data-Ready | `/ux-lean-ux`, `/ux-heart-metrics` | Wave 1: at least 1 heuristic eval completed AND 1 JTBD job statement used in a product decision | Bypass: 2 sprint cycles elapsed with no Wave 1 completion; allow Wave 2 with documented rationale |
| **3** | Design System | `/ux-atomic-design`, `/ux-inclusive-design` | Wave 2: launched product with analytics reporting OR 1 completed Lean UX hypothesis cycle with documented result | Bypass: Storybook already in use (skip Lean UX prerequisite for Atomic Design) |
| **4** | Advanced Analytics | `/ux-behavior-design`, `/ux-kano-model` | Wave 3: Storybook with 5+ Atom stories AND 1 Persona Spectrum review completed | Bypass: existing user base with analytics (skip Persona Spectrum prerequisite) |
| **5** | Process Intensives | `/ux-design-sprint`, `/ux-ai-first-design` (COND) | Wave 4: 30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed; AI-First Design: Enabler DONE + WSM >= 7.80 | Bypass: Design Sprint can proceed without Kano prerequisite if team has existing user research |

### 3.2 Wave Transition Quality Gates

Each wave transition is a quality checkpoint enforced through `/adversary` integration:

| Transition | Quality Check | Threshold |
|-----------|---------------|-----------|
| Wave 0 -> 1 | KICKOFF-SIGNOFF.md completeness review | Completeness pass/fail (all fields populated) |
| Wave 1 -> 2 | Wave 1 deliverables quality scoring | S-014 composite >= 0.85 on heuristic eval report |
| Wave 2 -> 3 | Wave 2 deliverables + usage evidence | S-014 composite >= 0.85 + documented usage artifact |
| Wave 3 -> 4 | Wave 3 deliverables + Storybook artifact | S-014 composite >= 0.85 + Storybook story count verification |
| Wave 4 -> 5 | Wave 4 deliverables + user data evidence | S-014 composite >= 0.85 + user count or behavioral data artifact |

---

## 4. Routing Architecture

### 4.1 Trigger Map Entry

The following entry is added to `mandatory-skill-usage.md`:

| Detected Keywords | Negative Keywords | Priority | Compound Triggers | Skill |
|---|---|---|---|---|
| UX, user experience, usability, design sprint, heuristic evaluation, accessibility, inclusive design, component library, design system, HEART metrics, jobs to be done, JTBD, kano model, lean UX, behavior design, AI UX, product design, wireframe, prototype, user testing, UX audit, UX metrics | adversarial, tournament, quality gate, penetration, exploit, transcript, requirements, specification, V&V, code review | 12 | "UX audit" OR "design sprint" OR "heuristic evaluation" OR "user experience" OR "design system" OR "HEART metrics" (phrase match) | `/user-experience` |

**Priority 12 rationale:** Current maximum priority is 11 (`/diataxis`, `/prompt-engineering`). UX keywords are distinct from all existing skill domains. Negative keywords prevent collision with `/adversary` ("quality gate"), `/red-team` ("penetration"), `/nasa-se` ("requirements"), and `/transcript`.

### 4.2 Lifecycle-Stage Triage Flowchart

The parent orchestrator routes requests through a multi-stage triage:

```
1. ONBOARD: Display HIGH RISK user research warning (first invocation per session)
2. CAPACITY CHECK: Ask team UX time allocation
   -> If < 20% of one person's time: restrict to Wave 1 sub-skills only
3. MCP CHECK: Detect if team is MCP-heavy
   -> If yes: apply C3=25% variant portfolio recommendations
4. STAGE TRIAGE: Route by product stage
   |
   +-- "Before design: Don't know what to build"     -> /ux-jtbd
   +-- "Before design: Need to prioritize features"   -> /ux-kano-model
   +-- "During design: Need validated prototype"       -> /ux-design-sprint
   +-- "During design: Iterating on existing design"   -> /ux-lean-ux OR /ux-heuristic-eval
   +-- "During design: Building component system"      -> /ux-atomic-design
   +-- "During design: Building AI product"            -> /ux-ai-first-design (if Enabler DONE)
   |                                                     OR /ux-heuristic-eval + PAIR (interim)
   +-- "After launch: Measure UX health"               -> /ux-heart-metrics
   +-- "After launch: Users not completing action"     -> /ux-behavior-design
   +-- "Any stage: Check accessibility"                -> /ux-inclusive-design
   +-- "CRISIS: Urgent UX problems"                    -> Emergency 3-skill sequence:
                                                          Heuristic Eval -> Behavior Design -> HEART
```

### 4.3 Sub-Skill Direct Invocation

Users who know the specific sub-skill can invoke directly via slash command (e.g., `/ux-heuristic-eval`). This bypasses the parent's triage mechanism. Each sub-skill has its own `activation-keywords` in its `SKILL.md`, registered at a lower routing priority than the parent.

### 4.4 Common Intent-to-Route Resolution

| User Says | Routes To | Qualification Question |
|-----------|----------|----------------------|
| "Improve my UX" / "Make this more usable" | Heuristic Eval (existing design) or Design Sprint (no design yet) | "Do you have an existing design?" |
| "Fix a specific UX problem" | Behavior Design (behavioral) or Heuristic Eval (design-level) | "Is the problem about user behavior or design quality?" |
| "Decide what to build" | JTBD (strategic) or Kano (prioritize known features) | "Are you defining the problem or prioritizing features?" |
| "Measure whether UX is working" | HEART Metrics | No qualification needed |
| "Make this accessible" | Inclusive Design | Provide user context brief |
| "CRISIS: urgent UX problems" | Emergency 3-skill sequence | No qualification needed |

---

## 5. Synthesis Hypothesis Validation

### 5.1 The 3-Tier Confidence Gate System

Multiple sub-skills produce "synthesis hypothesis" outputs -- AI-generated abstractions that may reflect training data biases rather than the team's specific users. A 3-tier confidence gate fires at skill invocation time.

| Confidence | Gate Behavior | Advancement Rule |
|------------|--------------|-----------------|
| **HIGH** | User reviews output + acknowledges specific AI judgment calls via Synthesis Judgments Summary | Advances to design decisions after enumerated acknowledgment |
| **MEDIUM** | Requires expert review OR validation against 2-3 real user data points | Cannot advance to design decisions without named validation source |
| **LOW** | Output permanently labeled reference-only; design recommendation section structurally omitted from output | Cannot be overridden by any user action |

### 5.2 Sub-Skill Synthesis Output Map

| Sub-Skill | Synthesis Step | Typical Confidence | Gate Implication |
|-----------|---------------|-------------------|-----------------|
| `/ux-jtbd` | Job statement synthesis from secondary research | MEDIUM | Requires named validation source |
| `/ux-lean-ux` | Assumption mapping; hypothesis generation | MEDIUM | Requires named validation source |
| `/ux-design-sprint` | Day 4 interview thematic analysis | HIGH | Enumerated acknowledgment |
| `/ux-design-sprint` | Day 2 sketch selection rationale | MEDIUM | Requires named validation source |
| `/ux-inclusive-design` | Persona Spectrum customization | MEDIUM | Requires named validation source |
| `/ux-kano-model` | Directional classification (5-8 respondents) | MEDIUM | Requires named validation source |
| `/ux-kano-model` | Feature priority conflict interpretation | LOW | Reference-only; no design recommendations |
| `/ux-behavior-design` | B=MAP bottleneck diagnosis | MEDIUM | Requires named validation source |
| `/ux-behavior-design` | Design intervention recommendation | LOW | Reference-only; no design recommendations |
| `/ux-heart-metrics` | Goal-metric mapping interpretation | MEDIUM | Requires named validation source |
| `/ux-heart-metrics` | Metric threshold recommendation | LOW | Reference-only; no design recommendations |
| `/ux-ai-first-design` | AI interaction pattern recommendations | LOW | Reference-only; no design recommendations |

### 5.3 Gate Enforcement Mechanism

- **HIGH gate:** Agent output includes a "Synthesis Judgments Summary" section listing each AI judgment call. The output includes an acknowledgment prompt the user must respond to before the agent proceeds to generate design recommendations.
- **MEDIUM gate:** Agent output includes a "Validation Required" section with placeholder for the user to provide a named validation source (expert name, user data reference, or study citation). The agent does not generate the design recommendation section until the validation source is provided.
- **LOW gate:** The agent's output template structurally omits the design recommendation section. The output is tagged with `[REFERENCE-ONLY]` in the title and includes a notice: "This output reflects AI synthesis from training data. It does not contain design recommendations. Use as reference material for human decision-making only."

---

## 6. Jerry Skill Integration Points

### 6.1 Integration Matrix

| Jerry Skill | Integration Type | Direction | Integration Details |
|-------------|-----------------|-----------|-------------------|
| `/problem-solving` | Research support | Upstream | `ps-researcher` provides market research for JTBD competitive job analysis; `ps-analyst` supports Kano survey data interpretation and trade-off analysis |
| `/adversary` | Quality enforcement | Applied to outputs | S-014 quality scoring on UX deliverables at wave transitions; full adversarial critique for C2+ UX artifacts per H-13/H-14 |
| `/worktracker` | Operational tracking | Infrastructure | Tracks all UX work items: sub-skill stories, wave transition tasks, Enabler status for AI-First Design, MCP ownership verification tasks |
| `/orchestration` | Workflow coordination | Coordinates sub-skills | Manages multi-framework workflows; canonical sequences: JTBD -> Design Sprint -> Lean UX -> HEART; barrier-sync between sub-skills |
| `/nasa-se` | Requirements handoff | Downstream | UX requirements from JTBD job statements and Nielsen's findings feed into technical requirements and V&V criteria |
| `/diataxis` | Documentation method | Complementary | Component documentation (from Atomic Design) and design system guides use Diataxis four-quadrant methodology |
| `/ast` | Entity validation | Infrastructure | Worktracker entities for UX work items validated via AST-based frontmatter extraction (H-33) |

### 6.2 Canonical Multi-Skill Workflow Sequences

| Sequence | Skills Involved | Use Case |
|----------|----------------|----------|
| Discovery -> Sprint | `/ux-jtbd` -> `/ux-design-sprint` | JTBD job statement feeds into Design Sprint challenge statement |
| Sprint -> Iterate -> Measure | `/ux-design-sprint` -> `/ux-lean-ux` -> `/ux-heart-metrics` | Sprint produces prototype; Lean UX iterates on it; HEART measures post-launch |
| Evaluate -> Diagnose -> Measure | `/ux-heuristic-eval` -> `/ux-behavior-design` -> `/ux-heart-metrics` | Crisis mode sequence for urgent UX problems |
| Build -> Evaluate | `/ux-atomic-design` -> `/ux-inclusive-design` | Build components, then evaluate accessibility |
| Discover -> Prioritize | `/ux-jtbd` -> `/ux-kano-model` | Discover jobs, then prioritize features via Kano |

### 6.3 Handoff Data Between Sub-Skills

Cross-sub-skill handoffs use the Jerry handoff protocol (handoff-v2.schema.json) with UX-specific artifact types:

| From Sub-Skill | To Sub-Skill | Handoff Artifact | Format |
|---------------|-------------|-----------------|--------|
| `/ux-jtbd` | `/ux-design-sprint` | Job statement + switch forces | Markdown with structured fields |
| `/ux-jtbd` | `/ux-kano-model` | Job-derived feature list | Markdown table |
| `/ux-design-sprint` | `/ux-lean-ux` | Validated prototype + Day 4 findings | File path reference to Figma prototype + findings markdown |
| `/ux-heuristic-eval` | `/ux-behavior-design` | Severity-rated findings | Markdown with severity enum (CRITICAL/HIGH/MEDIUM/LOW) |
| `/ux-atomic-design` | `/ux-inclusive-design` | Component inventory | Markdown table with Storybook story references |
| `/ux-lean-ux` | `/ux-heart-metrics` | Validated/invalidated hypotheses | Markdown hypothesis backlog |

---

## 7. Risk Register

| # | Risk | Likelihood | Impact | Mitigation | Monitoring |
|---|------|-----------|--------|------------|------------|
| R1 | **Figma MCP breaking change** disrupts 4+ sub-skills simultaneously | Medium | High | Non-Figma fallback documented per sub-skill; quarterly MCP audit; named MCP maintenance owner | Check Figma MCP changelog monthly; MCP ownership task in worktracker |
| R2 | **User research gap** causes teams to make poor product decisions from unvalidated AI synthesis | High | High | Onboarding warning; synthesis hypothesis validation protocol (3-tier confidence gates); V2 P1 priority for user research framework | Track user feedback about synthesis quality; monitor confidence gate override attempts |
| R3 | **AI-First Design Enabler** fails or expires | Medium | Medium | Service Blueprinting auto-substitution path; interim PAIR Guidebook + Lean UX workaround | Track Enabler status in worktracker; quarterly review of synthesis progress |
| R4 | **Context window pressure** from 10+ sub-skill definitions loaded simultaneously | Low | High | Only parent skill loaded at session start (Tier 1); sub-skills loaded on-demand via Task tool (Tier 2); CB-02 budget preserved | Monitor context fill levels during multi-sub-skill sessions |
| R5 | **Scope creep** as V2 additions expand sub-skill count beyond manageable routing | Medium | Medium | Layer 2 routing at 15+ sub-skills per scaling roadmap; sub-skill groupings pre-designed for Phase 3 | Track sub-skill count; trigger Layer 2 evaluation at 15 |
| R6 | **Over-reliance on AI synthesis** despite confidence gates | Medium | High | LOW gate structurally omits design recommendations; MEDIUM gate requires named validation source; audit trail in output artifacts | Review confidence gate distributions across invocations |
| R7 | **Wave adoption stalls** at Wave 1-2 due to team capacity | Medium | Low | Bypass conditions documented; free-tier config supports 5 sub-skills at $0 MCP cost | Track wave progression per team |
| R8 | **Community MCP server abandonment** (Whimsical) | Medium | Low | Community MCPs are Enhancement-only, never Required; verify GitHub activity before implementation | Check GitHub repository activity before each wave that uses community MCP |

---

## 8. Implementation Artifacts Checklist

### 8.1 Foundation (Before Wave 1)

| # | Artifact | Path | Blocking | Status |
|---|----------|------|----------|--------|
| 1 | KICKOFF-SIGNOFF.md | `projects/PROJ-020-feature-enhancements/KICKOFF-SIGNOFF.md` | Blocks Wave 1 | TODO |
| 2 | Parent skill SKILL.md | `skills/user-experience/SKILL.md` | Blocks all routing | TODO |
| 3 | Parent orchestrator agent definition | `skills/user-experience/agents/ux-orchestrator.md` | Blocks all routing | TODO |
| 4 | Parent orchestrator governance YAML | `skills/user-experience/agents/ux-orchestrator.governance.yaml` | Blocks all routing | TODO |
| 5 | Parent routing rules | `skills/user-experience/rules/ux-routing-rules.md` | Blocks lifecycle triage | TODO |
| 6 | Synthesis validation rules | `skills/user-experience/rules/synthesis-validation.md` | Blocks confidence gates | TODO |
| 7 | Trigger map update | `.context/rules/mandatory-skill-usage.md` (add row) | Blocks keyword routing | TODO |
| 8 | CLAUDE.md skill table entry | `CLAUDE.md` (add `/user-experience` row) | Blocks skill discovery | TODO |
| 9 | AGENTS.md agent registry entries | `AGENTS.md` (add orchestrator + sub-skill agents) | Blocks agent discovery | TODO |

### 8.2 Per-Sub-Skill (Repeated 10 Times)

For each sub-skill `ux-{slug}`:

| # | Artifact | Path Pattern | Notes |
|---|----------|-------------|-------|
| 1 | Sub-skill SKILL.md | `skills/ux-{slug}/SKILL.md` | Activation keywords, description, agent reference |
| 2 | Primary agent definition | `skills/ux-{slug}/agents/ux-{agent-name}.md` | YAML frontmatter (official fields only) + markdown body |
| 3 | Agent governance YAML | `skills/ux-{slug}/agents/ux-{agent-name}.governance.yaml` | Validates against `docs/schemas/agent-governance-v1.schema.json` |
| 4 | Framework methodology rules | `skills/ux-{slug}/rules/{framework}-rules.md` | Framework-specific methodology, constraints, quality criteria |
| 5 | Output template(s) | `skills/ux-{slug}/templates/{template-name}.md` | Structured output templates for agent deliverables |

### 8.3 Sub-Skill Artifact Index

| Sub-Skill | SKILL.md | Agent | Governance | Rules | Templates |
|-----------|----------|-------|------------|-------|-----------|
| `/ux-heuristic-eval` | `skills/ux-heuristic-eval/SKILL.md` | `ux-heuristic-evaluator.md` | `ux-heuristic-evaluator.governance.yaml` | `heuristic-evaluation-rules.md` | `heuristic-report-template.md` |
| `/ux-jtbd` | `skills/ux-jtbd/SKILL.md` | `ux-jtbd-analyst.md` | `ux-jtbd-analyst.governance.yaml` | `jtbd-methodology-rules.md` | `job-statement-template.md`, `switch-interview-guide.md` |
| `/ux-lean-ux` | `skills/ux-lean-ux/SKILL.md` | `ux-lean-ux-facilitator.md` | `ux-lean-ux-facilitator.governance.yaml` | `lean-ux-methodology-rules.md` | `hypothesis-backlog-template.md`, `assumption-map-template.md` |
| `/ux-heart-metrics` | `skills/ux-heart-metrics/SKILL.md` | `ux-heart-analyst.md` | `ux-heart-analyst.governance.yaml` | `heart-methodology-rules.md` | `heart-gsm-template.md` |
| `/ux-atomic-design` | `skills/ux-atomic-design/SKILL.md` | `ux-atomic-architect.md` | `ux-atomic-architect.governance.yaml` | `atomic-design-rules.md` | `component-inventory-template.md` |
| `/ux-inclusive-design` | `skills/ux-inclusive-design/SKILL.md` | `ux-inclusive-evaluator.md` | `ux-inclusive-evaluator.governance.yaml` | `inclusive-design-rules.md` | `persona-spectrum-template.md`, `accessibility-report-template.md` |
| `/ux-behavior-design` | `skills/ux-behavior-design/SKILL.md` | `ux-behavior-diagnostician.md` | `ux-behavior-diagnostician.governance.yaml` | `fogg-behavior-rules.md` | `bmap-diagnosis-template.md` |
| `/ux-kano-model` | `skills/ux-kano-model/SKILL.md` | `ux-kano-analyst.md` | `ux-kano-analyst.governance.yaml` | `kano-methodology-rules.md` | `kano-survey-template.md`, `feature-priority-template.md` |
| `/ux-design-sprint` | `skills/ux-design-sprint/SKILL.md` | `ux-sprint-facilitator.md` | `ux-sprint-facilitator.governance.yaml` | `design-sprint-rules.md` | `sprint-day-templates/` (per-day templates) |
| `/ux-ai-first-design` | `skills/ux-ai-first-design/SKILL.md` | `ux-ai-design-guide.md` | `ux-ai-design-guide.governance.yaml` | `ai-first-design-rules.md` | `ai-interaction-spec-template.md` |

### 8.4 Total Artifact Count

| Category | Count |
|----------|-------|
| Foundation artifacts | 9 |
| Per-sub-skill artifacts (10 sub-skills x 5 artifacts) | 50 |
| Additional templates (sub-skills with 2+ templates) | ~8 |
| **Total** | **~67 artifacts** |

### 8.5 Worktracker Decomposition (Post-Approval)

Following user approval of this specification, the implementation decomposes into:

| Entity Type | Count | Examples |
|-------------|-------|---------|
| Epic | 1 | "Implement /user-experience Skill Portfolio" |
| Features | 6 | "Parent Orchestrator", "Wave 1 Sub-Skills", "Wave 2 Sub-Skills", ... |
| Enablers | 2 | "AI-First Design Synthesis", "MCP Ownership Assignment" |
| Stories | ~20 | Per-sub-skill implementation stories |
| Tasks | ~40-60 | Individual artifact creation, testing, integration tasks |

---

## 9. Governance Compliance Summary

### 9.1 HARD Rules Addressed

| Rule | How Addressed |
|------|--------------|
| H-01 (P-003) | Single-level nesting: ux-orchestrator (T5) delegates to sub-skill agents (T2-T3) via Task; no sub-skill has Task access |
| H-02 (P-020) | Architecture vision PROPOSED status; user approval required before implementation |
| H-03 (P-022) | HIGH RISK user research gap documented; AI-First Design conditional status disclosed; synthesis confidence gates enforce transparency |
| H-04 | All work tracked under PROJ-020-feature-enhancements |
| H-13 | Sub-skill deliverables subject to >= 0.92 quality gate for C2+ outputs |
| H-14 | Creator-critic-revision cycle applies to all sub-skill agent definitions |
| H-22 | Parent skill registered in mandatory-skill-usage.md trigger map |
| H-23 | All markdown artifacts include navigation tables |
| H-25 | Sub-skill naming follows kebab-case (`ux-{slug}`); SKILL.md required per sub-skill |
| H-26 | All sub-skills registered in CLAUDE.md and AGENTS.md |
| H-34 | All agent definitions use dual-file architecture (.md + .governance.yaml); governance YAMLs validate against schema |
| H-36 | Parent orchestrator routing respects circuit breaker (max 3 hops); keyword-first routing via trigger map |

### 9.2 Constitutional Compliance (Per Agent)

Every agent (orchestrator + 10 sub-skill agents) will declare in `.governance.yaml`:

```yaml
constitution:
  principles_applied:
    - P-003  # No recursive subagents
    - P-020  # User authority
    - P-022  # No deception

capabilities:
  forbidden_actions:
    - "P-003 VIOLATION: NEVER spawn recursive subagents -- Consequence: agent hierarchy violation breaks orchestrator-worker topology and causes uncontrolled token consumption."
    - "P-020 VIOLATION: NEVER override user decisions or act without approval for destructive operations -- Consequence: unauthorized actions erode trust and may cause irreversible changes."
    - "P-022 VIOLATION: NEVER misrepresent capabilities, confidence levels, or actions taken -- Consequence: deceptive output undermines governance and prevents accurate quality assessment."
```

Sub-skill agents will additionally declare:
- No Task tool in `tools` frontmatter (enforcing H-34b worker constraint)
- Domain-specific forbidden actions (e.g., ux-heuristic-evaluator: "NEVER claim a design passes all heuristics without evaluating each one individually")
