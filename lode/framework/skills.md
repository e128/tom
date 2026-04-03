# Skills System
*Updated: 2026-04-03*

Skills are `/slash-command` capabilities. Each lives in `skills/{name}/SKILL.md`. Agents live in `skills/{name}/agents/`. Skills are invoked proactively by keyword detection (H-22).

## Skill Structure

```
skills/{name}/
    SKILL.md              # skill definition: name, description, agents, methodology
    agents/
        {agent}.md        # agent definition (official Claude Code YAML frontmatter + system prompt)
```

## Key Skills Reference

See `CLAUDE.md` Quick Reference table for the full current list. Key skills:

| Skill | Trigger Keywords | Purpose |
|-------|-----------------|---------|
| `/problem-solving` | research, analyze, investigate, debug | Research and root cause analysis |
| `/nasa-se` | requirements, specification, architecture, design | Requirements and design |
| `/orchestration` | pipeline, workflow, multi-agent, phases | Multi-phase workflow coordination |
| `/worktracker` | task, issue, work item, entity | Work item management |
| `/adversary` | adversarial, tournament, quality gate | Quality reviews and scoring |
| `/diataxis` | documentation, tutorial, how-to | Documentation creation |

## Routing (H-22, H-36)

Routing uses keyword-first detection (Layer 1). The trigger map lives in `.context/rules/mandatory-skill-usage.md`. Circuit breaker: max 3 hops before halting (H-36).

Negative keywords suppress false-positive matches. Priority ordering resolves conflicts when multiple skills match.

## Skill Standards (H-25, H-26)

- Folder name: kebab-case (e.g., `problem-solving`)
- SKILL.md: case-sensitive filename (SKILL.md, not skill.md)
- No README.md inside skill folder
- Description: WHAT + WHEN + triggers, under 1024 chars, no XML
- Must register in CLAUDE.md Quick Reference table

## Agent Standards (H-34)

Agent definitions use a single `.md` file with official Claude Code YAML frontmatter (name, description, tools, model, etc.) and the system prompt as the markdown body.

Constitutional triplet (required in every agent): P-003 (no recursive subagents), P-020 (user authority), P-022 (no deception).

## Tool Security Tiers

| Tier | Tools | Use Case |
|------|-------|----------|
| T1 | Read, Glob, Grep | Evaluation, auditing |
| T2 | T1 + Write, Edit, Bash | Document production |
| T3 | T2 (file-based persistence only) | Analysis with output artifacts |
| T4 | T3 + WebSearch, WebFetch, Context7 | Research, external docs |
| T5 | T4 + Agent | Orchestration |

## Related Lode Files

- [agents.md](agents.md) — agent definition format details
- [rules.md](rules.md) — H-22, H-25, H-26, H-34, H-36
