# Agent System
*Updated: 2026-04-08T00:00:28Z*

Agents are specialized subagents invoked via the Agent tool by orchestrators. Single-file architecture (H-34): `.md` file contains both official Claude Code YAML frontmatter and the system prompt as the markdown body.

## Single-File Architecture

**`.md` YAML frontmatter** — 15 official Claude Code fields (as of April 2026, v2.1.91):

```yaml
---
name: ps-researcher
description: >
  Research agent for surveys and landscape analysis...
model: opus
effort: high              # low | medium | high | max (max=Opus 4.6 only) — v2.1.80
tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch
disallowedTools: Agent    # worker agents always disallow Agent (P-003)
permissionMode: default   # default | acceptEdits | auto | dontAsk | bypassPermissions | plan
mcpServers:
  context7: true
memory: project           # user | project | local
background: false
isolation: worktree       # runs in isolated git worktree
color: blue               # red | blue | green | yellow | purple | orange | pink | cyan (UI only)
---
```

`initialPrompt` is a 16th field supported only for main-session agents (`--agent` flag) — not for subagents.

**`.md` markdown body** — System prompt with XML-tagged sections:
```markdown
<identity>
Role: Research Specialist
Cognitive mode: divergent
Expertise: landscape surveys, external documentation research
</identity>

<guardrails>
- P-003 VIOLATION: NEVER spawn recursive subagents — Consequence: ...
- P-020 VIOLATION: NEVER override user decisions — Consequence: ...
- P-022 VIOLATION: NEVER misrepresent capabilities — Consequence: ...
</guardrails>
```

## Deprecations (April 2026)

- **`Task` tool** → renamed to `Agent` in v2.1.63. All skill docs and agent invocation examples have been updated. `Task` remains a backward-compatible alias but is no longer used in this repo.
- **`TaskOutput` tool** → deprecated in v2.1.89. Use `Read` on the task output file path instead. No active usage in this repo.

## Cognitive Modes

| Mode | Use Case | Example Agents |
|------|----------|---------------|
| divergent | Research, exploration | ps-researcher |
| convergent | Analysis, evaluation, scoring | ps-analyst, ps-critic |
| integrative | Cross-source synthesis | ps-synthesizer |
| systematic | Validation, compliance checking | ps-validator |
| forensic | Root cause analysis, debugging | ps-investigator |

## Constitutional Triplet (H-34)

Every agent MUST declare P-003, P-020, P-022 in the `<guardrails>` section with at least 3 `forbidden_actions` entries. Worker agents MUST NOT have `Agent` in their `tools` list.

## Orchestrator-Worker Topology (H-01)

One nesting level only: orchestrator (T5) → workers (T1–T4). Workers cannot spawn sub-workers.

## Effort Field (ET-M-001)

`effort` maps to criticality level. All 92 agent files declare `effort` (89 in `skills/*/agents/`, 3 in `.claude/agents/`). Orchestrators and T5 agents use `high`.

**v2.1.94 change:** The session-level default effort changed from `low` to `high`. All agents now inherit `high` if `effort` is omitted. This makes explicit `effort: low` and `effort: medium` declarations critical for haiku/sonnet agents — without them, they run at `high` effort regardless of model.

| Criticality | effort value | Example agents |
|-------------|-------------|----------------|
| C1 (haiku, mechanical) | `low` | ps-validator, ts-formatter, adv-selector, diataxis-classifier |
| C2 (sonnet, standard) | `medium` | ps-analyst, ps-critic, orch-planner, eng-lead |
| C3 (opus, significant) | `high` | ps-researcher, ps-architect, eng-architect, ux-orchestrator |
| C4 (opus, critical/irreversible) | `max` | (Opus 4.6 only — not currently assigned) |

```yaml
model: haiku
effort: low

model: sonnet
effort: medium

model: opus
effort: high
```

## Color Field (v2.1.91)

`color` is a UI-only display hint for the Claude Code agent panel. Color assignments in this repo:

| Color | Agent group |
|-------|-------------|
| `purple` | Orchestrators (ux-orchestrator, orch-planner, orch-synthesizer, orch-tracker, red-lead) |
| `blue` | Opus research/architecture (ps-researcher, ps-architect, eng-architect, nse-architecture, etc.) |
| `red` | Security/adversarial (adv-*, eng-security, eng-devsecops, red-recon through red-social) |
| `yellow` | Haiku validators/reporters (ps-validator, ps-reporter, ts-parser, nse-reporter, etc.) |

## MCP Servers

Agents may declare `mcpServers` in frontmatter. Only `context7: true` is valid — `memory-keeper` was retired (never implemented; removed 2026-04-03). Agents without external research needs should omit `mcpServers` entirely.

## Related Lode Files

- [skills.md](skills.md) — skills that contain agents
- [rules.md](rules.md) — H-34, H-01 details
- `/claude-revision` skill (`skills/claude-revision/SKILL.md`) — periodic health check for agents; has no agents/ subdirectory (runs directly in main context)
