# Agent System
*Updated: 2026-04-03T15:00:00Z*

Agents are specialized subagents invoked via the Agent tool by orchestrators. Single-file architecture (H-34): `.md` file contains both official Claude Code YAML frontmatter and the system prompt as the markdown body.

## Single-File Architecture

**`.md` YAML frontmatter** — Official Claude Code fields only:
```yaml
---
name: ps-researcher
description: >
  Research agent for surveys and landscape analysis...
model: opus
tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch
---
```

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

## Effort Field

All haiku agents declare `effort: low` — prevents extended thinking inheritance from parent context and signals mechanical/low-complexity execution. Opus agents do not declare effort (default is appropriate for complex tasks). Sonnet agents omit effort unless they have unusual complexity needs.

```yaml
model: haiku
effort: low   # required for haiku agents
```

## MCP Servers

Agents may declare `mcpServers` in frontmatter. Only `context7: true` is valid — `memory-keeper` was retired (never implemented; removed 2026-04-03). Agents without external research needs should omit `mcpServers` entirely.

## Related Lode Files

- [skills.md](skills.md) — skills that contain agents
- [rules.md](rules.md) — H-34, H-01 details
