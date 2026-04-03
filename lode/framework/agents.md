# Agent System
*Updated: 2026-04-03T00:00:00Z*

Agents are specialized subagents invoked via the Agent tool by orchestrators. Dual-file architecture (H-34): `.md` for Claude Code, `.governance.yaml` for governance metadata.

## Dual-File Architecture

**`.md` YAML frontmatter** — Official Claude Code fields only:
```yaml
---
name: ps-researcher
description: >
  Research agent for surveys and landscape analysis...
model: opus
tools: Read, Glob, Grep, Write, Bash, WebSearch, WebFetch
---
```

**`.governance.yaml`** — Validated against `docs/schemas/agent-governance-v1.schema.json`:
```yaml
version: "1.0.0"
tool_tier: T4
identity:
  role: "Research Specialist"
  expertise: ["landscape surveys", "external documentation research"]
  cognitive_mode: divergent
capabilities:
  forbidden_actions:
    - "P-003 VIOLATION: NEVER spawn recursive subagents — Consequence: ..."
    - "P-020 VIOLATION: NEVER override user decisions — Consequence: ..."
    - "P-022 VIOLATION: NEVER misrepresent capabilities — Consequence: ..."
constitution:
  principles_applied: [P-003, P-020, P-022]
```

## Cognitive Modes

| Mode | Use Case | Example Agents |
|------|----------|---------------|
| divergent | Research, exploration | ps-researcher |
| convergent | Analysis, evaluation, scoring | ps-analyst, ps-critic |
| integrative | Cross-source synthesis | ps-synthesizer |
| systematic | Validation, compliance checking | ps-validator |
| forensic | Root cause analysis, debugging | ps-investigator |

## Constitutional Triplet (H-35)

Every agent MUST declare P-003, P-020, P-022 in both `constitution.principles_applied` and `capabilities.forbidden_actions` (min 3 entries). Worker agents MUST NOT have `Agent` in their tools list.

## Orchestrator-Worker Topology (H-01)

One nesting level only: orchestrator (T5) → workers (T1–T4). Workers cannot spawn sub-workers.

## Related Lode Files

- [skills.md](skills.md) — skills that contain agents
- [rules.md](rules.md) — H-34, H-35, H-01 details
