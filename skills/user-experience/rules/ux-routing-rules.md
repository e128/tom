<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "Lifecycle-Stage Routing", "Wave Architecture", "Cross-Sub-Skill Handoff Data" | PARENT: /user-experience skill -->

# UX Routing Rules

> Lifecycle-stage routing logic for the ux-orchestrator agent. Maps product lifecycle stages to sub-skill sequences and manages CRISIS routing. See also: `skills/user-experience/rules/wave-progression.md` (wave gate criteria), `skills/user-experience/rules/synthesis-validation.md` (synthesis confidence gates), `skills/user-experience/rules/mcp-coordination.md` (MCP availability routing).

## Document Sections

| Section | Purpose |
|---------|---------|
| [Lifecycle Stage Router](#lifecycle-stage-router) | Product stage to sub-skill mapping |
| [Common Intent Resolution](#common-intent-resolution) | Ambiguous user intent to specific route |
| [Multi-Sub-Skill Routing](#multi-sub-skill-routing) | Sequential multi-sub-skill execution outside CRISIS mode |
| [CRISIS Routing](#crisis-routing) | Emergency 3-skill fixed sequence |
| [Wave-Aware Routing](#wave-aware-routing) | Routing behavior when sub-skills are not yet deployed |
| [Bypass Routing](#bypass-routing) | Wave bypass prompt presentation rules |
| [Cross-Sub-Skill Handoff](#cross-sub-skill-handoff) | Data contracts between sub-skills |

---

## Lifecycle Stage Router

<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — 4-step sequential triage. -->

The orchestrator implements lifecycle-stage routing as a 4-step sequential triage:

1. **ONBOARD:** Display HIGH RISK user research warning (first invocation per session via session state flag). Warning content: "AI-generated UX analysis reflects training data patterns, not your specific users. All synthesis hypotheses carry confidence classifications (HIGH/MEDIUM/LOW). Validate MEDIUM and LOW findings against real user data before making design decisions."
2. **CAPACITY CHECK:** Ask team UX time allocation. If < 20% of one person's time: recommend Wave 1 sub-skills only (P-020: user decides whether to accept the recommendation or override). Note: the Wave 1 recommendation is based on team capacity constraints, not cost — the Free ($0) cost tier in `skills/user-experience/rules/mcp-coordination.md` [Cost Tiers] covers sub-skills across multiple waves (HEART W2, JTBD W1, Kano W4, Behavior Design W4). Capacity and cost tiers are independent dimensions. If >= 20%: proceed to full stage triage with all deployed waves available.
3. **MCP CHECK:** Detect MCP availability via lightweight Context7 resolve call. If unavailable: route to non-MCP fallback paths (text-only mode). Disclose MCP status to user per P-022.
4. **STAGE TRIAGE:** Route by product lifecycle stage using the table below.

### Stage Routing Table

| Stage Category | User Intent | Routes To | Wave | Qualification Question |
|---------------|-------------|-----------|------|----------------------|
| Before design | Don't know what to build | `/ux-jtbd` | 1 | -- |
| Before design | Need to prioritize features | `/ux-kano-model` | 4 | -- |
| Before design | Need validated prototype | `/ux-design-sprint` | 5 | -- (bypass prompt if Wave 5 not deployed) |
| During design | Iterating on existing design | `/ux-lean-ux` OR `/ux-heuristic-eval` | 2 / 1 | "Are you testing hypotheses or evaluating an existing interface?" (hypotheses → Lean UX; evaluating → Heuristic Eval) |
| During design | Building component system | `/ux-atomic-design` | 3 | -- |
| During design | Building AI product | `/ux-ai-first-design` (if Enabler DONE + WSM >= 7.80) OR `/ux-heuristic-eval` with AI-interaction heuristic supplement | 5 / 1 | "Is the AI-First Design enabler completed?" (if no: route to Heuristic Eval with AI-specific heuristic supplement per SKILL.md CONDITIONAL criteria) |
| After launch | Measure UX health | `/ux-heart-metrics` | 2 | -- |
| After launch | Users not completing action | `/ux-behavior-design` | 4 | -- |
| Any stage | Check accessibility | `/ux-inclusive-design` | 3 | -- |
| CRISIS | Urgent UX problems | Fixed 3-skill sequence (see [CRISIS Routing](#crisis-routing)) | W1→W4→W2 | -- (user confirms CRISIS entry) |

### Ambiguity Resolution Protocol

<!-- Source: agent-routing-standards.md (.context/rules/agent-routing-standards.md) Section "Multi-Skill Combination" — ordering protocol applied to UX sub-skill routing. -->

When STAGE TRIAGE produces multiple matches (e.g., "iterate on our accessible checkout"), the orchestrator applies the ordering protocol from `agent-routing-standards.md` [Multi-Skill Combination]:

1. **Content before quality:** Execute the content-producing sub-skill first, then the evaluation sub-skill.
2. **Work before presentation:** Execute the analytical sub-skill first, then the presentational one.
3. **If ambiguity remains after ordering:** Ask the user per H-31 with a structured question presenting the matched sub-skills and their purposes.

### No-Match Fallback

When the user's intent does not match any pattern in the Stage Routing Table:

1. Present the lifecycle stage categories (Before design / During design / After launch) and ask the user which best describes their situation per H-31.
2. If the user's response still does not match a known pattern: display the Stage Routing Table and ask which sub-skill best fits their need.
3. If the user's need falls outside all deployed sub-skills: acknowledge the gap transparently per P-022 and suggest alternative Jerry skills (e.g., `/problem-solving` for general UX research).

---

## Common Intent Resolution

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Lifecycle-Stage Routing" — common intent patterns derived from Stage Routing Table. These map natural-language user expressions to the appropriate sub-skill route and qualification question. -->

| User Says | Routes To | Qualification |
|-----------|----------|---------------|
| "Improve my UX" / "Make this more usable" | Heuristic Eval (existing) or Design Sprint (no design) | "Do you have an existing design?" |
| "Fix a specific UX problem" | Behavior Design (behavioral) or Heuristic Eval (design-level) | "Is the problem about user behavior or design quality?" |
| "Decide what to build" | JTBD (strategic) or Kano (prioritize known features) | "Are you defining the problem or prioritizing features?" |
| "Measure whether UX is working" | HEART Metrics | No qualification needed |
| "Make this accessible" | Inclusive Design | No qualification needed |
| "Comprehensive UX audit" | Heuristic Eval + HEART Metrics (multi-sub-skill; see [Multi-Sub-Skill Routing](#multi-sub-skill-routing) below) | No qualification needed |
| "CRISIS: urgent UX problems" | Emergency 3-skill sequence | No qualification needed (user confirms CRISIS entry) |

---

## Multi-Sub-Skill Routing

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Lifecycle-Stage Routing" — multi-sub-skill invocation. Ordering protocol from `.context/rules/agent-routing-standards.md` [Multi-Skill Combination] applied to UX sub-skill routing. -->

When a user's intent maps to multiple sub-skills outside of CRISIS mode (e.g., "Comprehensive UX audit"), the orchestrator executes the sub-skills sequentially following the ordering protocol from `agent-routing-standards.md` [Multi-Skill Combination].

### Ordering Rules

| Priority | Rule | UX Application |
|----------|------|---------------|
| 1 | Content before quality | Execute the content-producing sub-skill first, then the evaluation sub-skill (e.g., `/ux-heuristic-eval` produces findings before `/ux-heart-metrics` quantifies them) |
| 2 | Work before presentation | Execute the analytical sub-skill first, then the measurement sub-skill |
| 3 | If ambiguity remains | Ask user per H-31 with a structured question presenting the matched sub-skills and their purposes |

### Multi-Sub-Skill Execution Protocol

| Step | Action | Validation |
|------|--------|----|
| 1 | Identify all matched sub-skills from [Stage Routing Table](#stage-routing-table) | Each sub-skill's wave must be deployed (see [Wave-Aware Routing](#wave-aware-routing)) |
| 2 | Apply ordering rules to determine execution sequence | Sequence follows content-before-quality ordering |
| 3 | Execute first sub-skill and collect output | Output validates per sub-skill's methodology |
| 4 | Pass handoff data to next sub-skill per [Cross-Sub-Skill Handoff](#cross-sub-skill-handoff) | Handoff artifact existence and key fields validated |
| 5 | Execute remaining sub-skills in sequence | Each receives prior sub-skill outputs |
| 6 | Produce cross-framework synthesis per `synthesis-validation.md` [Cross-Framework Synthesis Protocol] | Synthesis triggered when 2+ sub-skill outputs exist for the same engagement |

### Common Multi-Sub-Skill Combinations

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Lifecycle-Stage Routing" — multi-sub-skill patterns derived from Stage Routing Table and Common Intent Resolution table. -->

| User Intent | Sub-Skills | Execution Order | Rationale |
|------------|-----------|----------------|-----------|
| Comprehensive UX audit | `/ux-heuristic-eval` → `/ux-heart-metrics` | Eval first (content), then Metrics (measurement) | Heuristic findings inform which HEART metrics to prioritize |
| Accessible design system | `/ux-atomic-design` → `/ux-inclusive-design` | Atomic first (content), then Inclusive (quality) | Component inventory informs accessibility evaluation scope |
| Research-driven prototype | `/ux-jtbd` → `/ux-design-sprint` | JTBD first (research), then Sprint (design) | Job statements feed sprint understanding phase |

### Constraints

- **Maximum 2 sub-skills** per non-CRISIS multi-sub-skill routing. Combinations exceeding 2 sub-skills escalate to user confirmation per RT-M-007.
- **CRISIS mode takes precedence.** If the user's intent matches CRISIS keywords (see [CRISIS Routing](#crisis-routing)), the fixed 3-skill CRISIS sequence executes instead of multi-sub-skill routing.
- **Wave gating applies.** If any sub-skill in the combination is not yet deployed, the orchestrator informs the user and offers alternatives per [Wave-Aware Routing](#wave-aware-routing).

---

## CRISIS Routing

<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — CRISIS mode. -->

CRISIS mode executes a fixed 3-skill sequence for urgent UX problems. The sequence is not configurable — the orchestrator selects the fixed route.

### CRISIS Entry

1. User indicates urgent UX problem (keywords: "CRISIS", "urgent UX", "users abandoning", "critical usability issue").
2. Orchestrator presents CRISIS confirmation: "CRISIS mode will execute a fixed 3-step sequence: (1) Heuristic Evaluation to identify design issues, (2) Behavior Design to diagnose behavioral root causes via Fogg B=MAP, (3) HEART Metrics to quantify impact. Proceed?"
3. User confirms entry (P-020 compliance: user authorizes the emergency sequence).

### CRISIS Execution Sequence

| Step | Sub-Skill | Purpose | Handoff to Next |
|------|-----------|---------|-----------------|
| 1 | `/ux-heuristic-eval` | Identify UX issues via Nielsen's 10 heuristics | Severity-rated findings (severity >= 2) |
| 2 | `/ux-behavior-design` | Diagnose behavioral root causes via Fogg B=MAP | Bottleneck diagnosis with motivation/ability/prompt breakdown |
| 3 | `/ux-heart-metrics` | Quantify impact using HEART Goals-Signals-Metrics | Metric baselines and target thresholds |

### CRISIS Rationale

The sequence follows the evaluate-diagnose-measure pattern:
- **Evaluate:** Heuristic Eval produces an objective severity-rated inventory of UX problems.
- **Diagnose:** Behavior Design takes the highest-severity findings and traces them to behavioral bottlenecks (is the user unable, unmotivated, or unprompted?).
- **Measure:** HEART Metrics establishes quantitative baselines so the team can track whether fixes actually improve the UX.

### CRISIS Synthesis

After the 3-skill CRISIS sequence completes, the orchestrator automatically produces a CRISIS synthesis report at `skills/user-experience/output/{engagement-id}/ux-orchestrator-crisis.md`. This synthesis follows the Cross-Framework Synthesis Protocol defined in `skills/user-experience/rules/synthesis-validation.md`, but with CRISIS-specific additions:
- **Priority ranking:** Findings are ranked by combined heuristic severity + behavioral bottleneck impact.
- **Quick-win identification:** Findings where the behavioral bottleneck is "prompt" (easiest to fix per Fogg model) are flagged as quick wins.
- **Metric coverage:** Each finding is mapped to a HEART metric so progress can be tracked.

---

## Wave-Aware Routing

<!-- Source: SKILL.md Section "Wave Architecture" — wave-gated deployment. -->

The router checks wave signoff state before routing to gated sub-skills. Wave state is determined by the existence and validity of signoff files.

### Wave State Detection

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Wave Architecture" — signoff file gating. See also: skills/user-experience/rules/wave-progression.md [Wave State Tracking] for authoritative state detection rules, and skills/user-experience/rules/wave-progression.md [Signoff Requirements] for validation criteria. -->

| File | Existence Indicates |
|------|-------------------|
| `skills/user-experience/output/KICKOFF-SIGNOFF.md` | Foundation complete; Wave 1 authorized |
| `skills/user-experience/output/WAVE-1-SIGNOFF.md` | Wave 1 complete; Wave 2 authorized |
| `skills/user-experience/output/WAVE-2-SIGNOFF.md` | Wave 2 complete; Wave 3 authorized |
| `skills/user-experience/output/WAVE-3-SIGNOFF.md` | Wave 3 complete; Wave 4 authorized |
| `skills/user-experience/output/WAVE-4-SIGNOFF.md` | Wave 4 complete; Wave 5 authorized |
| `skills/user-experience/output/WAVE-5-SIGNOFF.md` | Wave 5 complete; all waves deployed (full operational mode) |

### Routing Behavior for Unavailable Sub-Skills

When a user's intent routes to a sub-skill whose wave is not yet deployed:

1. **Inform:** "The sub-skill `/ux-{name}` is part of Wave {N}, which is not yet deployed." (P-022 compliance)
2. **Offer alternatives:**
   - If a Wave 1 sub-skill can partially address the need: suggest it with a disclaimer about scope limitations.
   - If no alternative exists: present the wave bypass mechanism.
3. **Bypass prompt:** If the user wants to proceed anyway, present the 3-field bypass documentation prompt (see [Bypass Routing](#bypass-routing)).

### Wave State Caching

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Wave Architecture" — wave state caching rules. Authoritative caching specification in skills/user-experience/rules/wave-progression.md [State Caching]. -->

The orchestrator checks signoff files once per engagement session and caches the wave state. Cache invalidation occurs:
- On the next routing decision after a signoff file is committed during the session.
- At the start of each new engagement session.
- When a bypass is granted or resolved.

---

## Bypass Routing

<!-- Source: SKILL.md Section "Wave Architecture" — bypass mechanism. -->

Wave bypass allows routing to a sub-skill whose wave has not been formally signed off. Bypass requires user-approved 3-field documentation per P-020.

### Bypass Prompt

When a bypass is requested, the orchestrator presents:

```
Wave bypass requested for /ux-{name} (Wave {N}).

Please provide the following three fields:

1. UNMET CRITERION: Which wave {N} entry criterion is not met?
   Example: "No completed heuristic evaluation from Wave 1"

2. IMPACT ASSESSMENT: What is the risk of proceeding without this criterion?
   Example: "Sprint proceeds without prior framework calibration; findings may lack comparative baseline"

3. REMEDIATION PLAN: How will the unmet criterion be satisfied, and by when?
   Example: "Backfill Wave 1 heuristic evaluation within 2 sprints of Design Sprint completion"
```

### Bypass Documentation

Bypass documentation is persisted at `skills/user-experience/output/{engagement-id}/wave-bypass-{wave-N}.md` with the following structure:

| Field | Content |
|-------|---------|
| Engagement ID | `UX-{NNNN}` |
| Sub-skill bypassed to | `/ux-{name}` |
| Wave bypassed | `{N}` |
| Unmet criterion | User-provided text |
| Impact assessment | User-provided text |
| Remediation plan | User-provided text with target date |
| Bypass approved by | User name or session ID |
| Bypass date | ISO 8601 date |

### Bypass Constraints

- **Cumulative ceiling:** Maximum 2 concurrent bypasses per team. If a team has 2 active bypasses, the orchestrator requires remediation of at least one before granting additional bypasses (source: SKILL.md Section "Wave Transition Quality Gates").
- **Warning banner:** All sub-skill outputs produced under bypass carry a warning banner: "[WAVE BYPASS] This output was produced before Wave {N} entry criteria were met. See wave-bypass-{wave-N}.md for bypass documentation."
- **Bypass tracking:** Active bypasses are listed in the engagement directory and checked at each wave signoff. A wave signoff cannot complete if it has unresolved bypasses for that wave.

---

## Cross-Sub-Skill Handoff

<!-- Source: SKILL.md Section "Cross-Sub-Skill Handoff Data". -->

Sub-skills exchange data via the Jerry handoff protocol (`docs/schemas/handoff-v2.schema.json`) with UX-specific artifact types.

### Handoff Data Contracts

| From | To | Handoff Artifact | Key Fields |
|------|-----|-----------------|-----------|
| `/ux-jtbd` | `/ux-design-sprint` | Job statement + switch forces | Job statement text, push/pull forces, hiring criteria |
| `/ux-jtbd` | `/ux-kano-model` | Job-derived feature list | Feature names mapped to job steps |
| `/ux-design-sprint` | `/ux-lean-ux` | Validated prototype + Day 4 findings | Prototype description, interview findings, validated/invalidated hypotheses |
| `/ux-heuristic-eval` | `/ux-behavior-design` | Severity-rated findings | Finding ID, heuristic violated, severity (0-4), affected screen/flow |
| `/ux-atomic-design` | `/ux-inclusive-design` | Component inventory | Component names, atomic level (atom/molecule/organism), Storybook references |
| `/ux-lean-ux` | `/ux-heart-metrics` | Hypothesis backlog | Hypothesis ID, validated/invalidated status, metric implications |

### Handoff Validation

The orchestrator validates handoff data at each transition:

1. **Artifact existence:** All `artifacts` paths in the handoff resolve to existing files.
2. **Key fields present:** Required handoff fields for the specific sub-skill pair are non-empty.
3. **Confidence propagation:** The receiving sub-skill inherits the synthesis confidence level from the sending sub-skill's output (MEDIUM propagates as MEDIUM; LOW propagates as LOW; HIGH may be downgraded by the receiving sub-skill based on its own assessment).

---

---

*Rule file: ux-routing-rules.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling rules: `skills/user-experience/rules/wave-progression.md`, `skills/user-experience/rules/synthesis-validation.md`, `skills/user-experience/rules/mcp-coordination.md`, `skills/user-experience/rules/ci-checks.md`*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
