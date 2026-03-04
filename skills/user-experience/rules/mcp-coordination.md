<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "MCP Integration Architecture", "Current Jerry MCP Integration", "Figma Dependency Risk Profile", "Cost Tiers" | PARENT: /user-experience skill -->

# MCP Coordination Rules

> MCP tool coordination rules for the /user-experience skill. Defines the sub-skill MCP dependency matrix, degraded mode behavior, Context7 integration, cost tiers, and future MCP adapter architecture. See also: `skills/user-experience/rules/ux-routing-rules.md` (MCP CHECK step in lifecycle triage), `skills/user-experience/rules/wave-progression.md` (wave deployment readiness affected by MCP availability), `skills/user-experience/rules/ci-checks.md` (CI gate UX-CI-007 validates MCP ownership in kickoff signoff). MCP governance: `.context/rules/mcp-tool-standards.md` [Context7 Integration], [Memory-Keeper Integration].

## Document Sections

| Section | Purpose |
|---------|---------|
| [MCP Dependency Matrix](#mcp-dependency-matrix) | Which sub-skills require which MCP servers |
| [Dependency Classifications](#dependency-classifications) | REQ/ENH/COND definitions and enforcement |
| [Degraded Mode Behavior](#degraded-mode-behavior) | Fallback paths when MCP is unavailable |
| [Figma Dependency Risk Profile](#figma-dependency-risk-profile) | Highest-risk MCP dependency with per-sub-skill fallbacks |
| [Context7 Usage](#context7-usage) | When to use Context7 for UX framework docs |
| [Cost Tiers](#cost-tiers) | MCP cost categories for team planning |
| [MCP Availability Detection](#mcp-availability-detection) | How the orchestrator probes MCP status |
| [Future MCP Adapters](#future-mcp-adapters) | Architecture for Figma/Miro/Storybook adapters |

---

## MCP Dependency Matrix

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "MCP Integration Architecture" — sub-skill dependency matrix. Note: `/ux-ai-first-design` has Figma REQ dependency (SKILL.md line 411) despite the sub-skill itself being conditional on Enabler DONE + WSM >= 7.80 (SKILL.md Section "Wave Architecture" line 267). The COND on line 267 refers to sub-skill wave deployment conditionality, NOT MCP dependency classification. Memory-Keeper is excluded from this matrix: no /user-experience sub-skill requires cross-session persistence via Memory-Keeper; all sub-skill state is engagement-scoped per P-002. -->

| Sub-Skill | Figma | Miro | Storybook | Zeroheight | Hotjar (Bridge) | Whimsical |
|-----------|-------|------|-----------|------------|-----------------|-----------|
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

---

## Dependency Classifications

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "MCP Integration Architecture" — dependency classification definitions. REQ/ENH/COND labels used consistently across the dependency matrix and degraded-mode tables. Note: COND classification applies to MCP dependency conditionality (e.g., feature X required only when condition Y is met), NOT to sub-skill wave deployment conditionality (which is tracked in wave-progression.md [Wave Definitions]). -->

| Classification | Label | Meaning | Failure Behavior |
|---------------|-------|---------|-----------------|
| **Required** | REQ | Sub-skill depends on this MCP for core functionality | Degraded mode + explicit error. Sub-skill operates with reduced capability; output carries degraded-mode banner. |
| **Enhancement** | ENH | MCP improves output quality but is not essential | Cosmetic limitation on failure. Sub-skill operates normally; enhanced features silently degrade to text-only equivalents. |
| **Conditional** | COND | MCP required only under specific conditions | Depends on condition. When condition is met and MCP unavailable: treated as REQ. When condition not met: no dependency. |

### Enforcement Rules

1. **REQ dependencies:** When a REQ MCP is unavailable, the orchestrator MUST inform the user per P-022 and route to the degraded-mode fallback path. The sub-skill MUST NOT silently proceed as if the MCP were available.
2. **ENH dependencies:** When an ENH MCP is unavailable, the sub-skill proceeds normally. No user notification required unless the user explicitly requested the enhanced feature.
3. **COND dependencies:** The orchestrator evaluates the condition before checking MCP availability. If the condition is not met, the MCP is not needed.

---

## Degraded Mode Behavior

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "MCP Integration Architecture" — text-only mode. -->

### Text-Only Mode

When MCP tools are unavailable, all agents operate in **text-only mode**: users provide design descriptions, screenshots, or markup instead of live design artifacts. The agent methodology remains identical; only the input modality changes.

### Per-Dependency Degraded Modes

**Currently available MCP tools:**

| MCP Tool | Degraded Mode | Impact |
|----------|--------------|--------|
| Context7 | WebSearch fallback: use web search for UX framework documentation | May return less targeted results; stale training data risk |

**Future MCP adapters (not yet implemented — architecture only in PROJ-022):**

| MCP Tool | Degraded Mode | Impact |
|----------|--------------|--------|
| Figma | Screenshot-input mode: user provides design screenshots as image inputs | Cannot inspect layers, components, or style tokens programmatically |
| Miro | Text-based exercise mode: sprint/workshop exercises described textually | Cannot create or modify collaborative boards |
| Storybook | Manual component inventory: user provides component list and documentation links | Cannot browse or validate live component stories |
| Zeroheight | Text-based design system reference: user provides design token documentation | Cannot query design system programmatically |
| Hotjar (Bridge) | Manual analytics input: user provides behavioral data via text description | Cannot access heatmaps or session recordings directly |
| Whimsical | Text-based flowcharts: user provides flow descriptions or ASCII diagrams | Cannot create visual diagrams |

### Degraded Mode Disclosure

Per P-022, agents MUST note degraded mode in their output:

```
[DEGRADED MODE] This output was produced without {MCP tool name} access.
Input was provided via {fallback method}. Some features are reduced:
- {specific limitation 1}
- {specific limitation 2}
```

---

## Figma Dependency Risk Profile

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Figma Dependency Risk Profile". -->

Figma is the highest-risk MCP dependency: 4 sub-skills require it, 2 are enhanced by it (6 of 10 total connections).

| Sub-Skill | Non-Figma Fallback | Quality Impact |
|-----------|--------------------|---------------|
| `/ux-heuristic-eval` | Screenshot-input mode: user provides design screenshots as image inputs | Moderate: cannot inspect component states or responsive behavior |
| `/ux-design-sprint` | Miro-only mode: sprint exercises in Miro; manual prototype reference | Significant: prototyping and concept evaluation rely on visual artifacts |
| `/ux-inclusive-design` | Screenshot-input mode: manual component screenshots for evaluation | Moderate: cannot inspect color values or contrast ratios programmatically |
| `/ux-ai-first-design` | Manual design description: text-based interaction pattern analysis | Significant: AI interaction patterns benefit from visual prototyping |

### Figma Mitigation Strategy

1. **Wave 1 sub-skills do not require Figma:** `/ux-heuristic-eval` (REQ Figma) is Wave 1, but screenshot-input mode provides viable fallback.
2. **Figma MCP adapter is architecture-only in PROJ-022:** Actual adapter implementation deferred to post-PROJ-022. Architecture + fallback paths defined here.
3. **Cost tier awareness:** Free tier ($0) explicitly excludes Figma-dependent sub-skills at full capability.

---

## Context7 Usage

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Current Jerry MCP Integration" and `.context/rules/mcp-tool-standards.md` MCP-001. -->

### Currently Available MCP Integration

| MCP Tool | Usage | Agents |
|----------|-------|--------|
| Context7 (resolve-library-id) | Resolve UX framework libraries and design system packages | ux-atomic-architect, ux-ai-design-guide |
| Context7 (query-docs) | Query component library documentation, accessibility API docs | ux-atomic-architect, ux-inclusive-evaluator, ux-ai-design-guide |

### Context7 Usage Rules

Per MCP-001 from `.context/rules/mcp-tool-standards.md` [Context7 Integration]:

1. Context7 MUST be used when an agent task references an external UX library, framework, or design system by name (e.g., Material UI, Radix, WCAG specification).
2. Protocol: `resolve-library-id` first, then `query-docs` with resolved ID.
3. Respect the per-question call limit enforced by the tool.
4. If `resolve-library-id` returns no matches: fall back to WebSearch for that library.

### Context7 UX Framework Examples

| Library/Framework | Expected Agent | Usage |
|-------------------|---------------|-------|
| WCAG 2.2 | ux-inclusive-evaluator | Accessibility success criteria lookup |
| Material Design | ux-atomic-architect | Component pattern documentation |
| Radix UI | ux-atomic-architect | Accessible component API docs |
| Nielsen Norman Group | ux-heuristic-evaluator | Heuristic definitions and severity scales |
| Fogg Behavior Model | ux-behavior-diagnostician | B=MAP framework documentation |

---

## Cost Tiers

<!-- Source: SKILL.md Section "Cost Tiers". -->

| Tier | Monthly Cost | Sub-Skills Available |
|------|-------------|---------------------|
| **Free** | $0 | HEART, JTBD, Kano, Behavior Design (+ Storybook for Atomic Design) |
| **Minimal** | ~$46 | + Heuristic Eval, Design Sprint, Lean UX, Inclusive Design, AI-First Design |
| **Full Enhancement** | ~$145-245 | All 10 with full enhancement MCPs |

### Cost Tier Routing

The orchestrator's CAPACITY CHECK step (see `ux-routing-rules.md` [Lifecycle Stage Router]) considers cost tier implications. When team UX capacity is < 20% of one person's time, the orchestrator recommends Wave 1 sub-skills only, which align with the Free cost tier. The user decides whether to accept this recommendation (P-020).

---

## MCP Availability Detection

<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — MCP CHECK step. -->

The orchestrator's 4-step lifecycle triage includes MCP detection at Step 3:

### Detection Protocol

1. **Probe:** Attempt a lightweight Context7 `resolve-library-id` call (e.g., resolve "WCAG"). Timeout: 5 seconds with 1 retry before declaring unavailable.
2. **If success:** MCP available. Cache status for engagement session.
3. **If failure (timeout > 5s after retry, or error response):** MCP unavailable. Route all sub-skills to non-MCP fallback paths.
4. **Disclose:** Inform user of MCP status per P-022. "MCP tools are [available/unavailable] for this session. [Available features / Degraded mode description]."

### Future MCP Probes

When Figma/Miro/Storybook MCP adapters become available, the detection protocol will expand:

| Probe | Target | Fallback |
|-------|--------|----------|
| Context7 resolve | UX library documentation | WebSearch |
| Figma API health | Figma file access | Screenshot-input mode |
| Miro API health | Miro board access | Text-based exercise mode |
| Storybook endpoint | Component story browsing | Manual component inventory |

---

## Future MCP Adapters

<!-- Source: SKILL.md Section "MCP Integration Architecture" — architecture + fallback paths only. -->

This section defines the adapter architecture for future MCP integrations. **Actual adapter implementation is out of scope for PROJ-022.**

### Adapter Architecture Pattern

Each future MCP adapter follows the same pattern:

```
MCP Adapter Pattern:
1. Health probe endpoint → availability detection
2. Authentication flow → OAuth2 or API key
3. Read-only operations → artifact inspection, data retrieval
4. Write operations (optional) → artifact creation/modification
5. Fallback path → text-only mode per Degraded Mode Behavior
```

### Planned Adapters

| Adapter | Priority | Rationale | Authentication |
|---------|----------|-----------|---------------|
| Figma MCP | HIGH | 6/10 sub-skill connections; highest-risk dependency | OAuth2 (Figma API) |
| Miro MCP | MEDIUM | 2 REQ + 2 ENH connections; Design Sprint critical path | OAuth2 (Miro API) |
| Storybook MCP | MEDIUM | 1 REQ + 3 ENH connections; Atomic Design core workflow | Local endpoint (dev server) |
| Hotjar Bridge | LOW | 2 ENH connections; analytics enrichment only | API key |
| Zeroheight MCP | LOW | 1 ENH connection; design system documentation | API key |
| Whimsical MCP | LOW | 1 ENH connection; diagram enhancement only | OAuth2 |

### Security Considerations

Per `/eng-team` integration (see SKILL.md [Cross-Skill Integration]):

- MCP credential handling follows Jerry's MCP tool standards (`mcp-tool-standards.md`).
- OAuth tokens for Figma/Miro MUST NOT be stored in agent context or output files.
- API keys MUST be managed via environment variables or secrets management.
- Adapter health probes MUST NOT expose authentication state in error messages.

---

*Rule file: mcp-coordination.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling rules: `skills/user-experience/rules/ux-routing-rules.md`, `skills/user-experience/rules/synthesis-validation.md`, `skills/user-experience/rules/wave-progression.md`, `skills/user-experience/rules/ci-checks.md`*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
