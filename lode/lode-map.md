# Lode Map
*Updated: 2026-04-03T15:51:45Z*

Hierarchical index of all lode files. Read this first to orient — don't explore the codebase until you've checked here.

## Top-Level Files

| File | Description |
|------|-------------|
| [summary.md](summary.md) | One-paragraph living snapshot of the project |
| [terminology.md](terminology.md) | Domain language: Tom-specific terms and their meanings |
| [practices.md](practices.md) | Key conventions, workflow rules, and project patterns |

## framework/

Tom framework internals — architecture, rules, skills, agents, CLI, work tracking.

| File | Description |
|------|-------------|
| [framework/architecture.md](framework/architecture.md) | Hexagonal architecture, layer isolation, domain model |
| [framework/rules.md](framework/rules.md) | HARD rules, quality gate, enforcement layers |
| [framework/skills.md](framework/skills.md) | Skills system: SKILL.md format, routing, trigger map |
| [framework/agents.md](framework/agents.md) | Agent definition format, effort/color fields, cognitive modes |
| [framework/cli.md](framework/cli.md) | tom CLI commands: session, items, projects |
| [framework/work-tracking.md](framework/work-tracking.md) | Worktracker entities, hierarchy, WTI rules |

## python/

Python patterns and conventions used in this codebase.

| File | Description |
|------|-------------|
| [python/patterns.md](python/patterns.md) | Python idioms, type hints, async patterns |
| [python/testing.md](python/testing.md) | BDD test-first, pytest, coverage requirements |

## tmp/

Git-ignored session scraps. Nothing here survives across sessions.
