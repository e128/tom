# Summary
*Updated: 2026-04-07T23:59:51Z*

**Tom** is a Python CLI framework for behavior/workflow guardrails that accrues knowledge, wisdom, and experience across AI-assisted coding sessions. It solves **Context Rot** — the degradation of LLM performance as context fills — by using the filesystem as infinite memory: state is persisted to files and loaded selectively. The framework enforces 25 HARD rules (non-overridable governance constraints), a quality gate threshold of 0.92 for C2+ deliverables, and a skill/agent routing system that proactively invokes 31 specialized skills (92 agents) based on keyword detection — including `/claude-revision` for periodic framework health checks. Tom is managed via `tom session start|end|status|abandon`, `tom items list|show`, and `tom projects list|context|validate`. All Python execution uses `uv run`; dependencies use `uv add`. The codebase follows hexagonal architecture with strict layer isolation and BDD test-first development at 90% line coverage.

## Key Facts

- **Package**: `tom` (see `pyproject.toml` for version)
- **Python execution**: `uv run` only — never `python` or `pip` directly
- **Architecture**: Hexagonal (domain / application / infrastructure / interface layers)
- **Skills**: `skills/` directory — each has a `SKILL.md` file
- **Agents**: `skills/*/agents/` — single `.md` file (YAML frontmatter + system prompt body)
- **Rules**: `.context/rules/` — auto-loaded at session start via `.claude/rules/` symlink
- **Active projects**: `projects/` directory (currently empty — only README.md), managed via `/worktracker` skill

## Related Lode Files

- [terminology.md](terminology.md) — Tom-specific vocabulary
- [practices.md](practices.md) — development practices and conventions
- [framework/architecture.md](framework/architecture.md) — hexagonal layer details
- [framework/rules.md](framework/rules.md) — quality enforcement and HARD rules
- [framework/agents.md](framework/agents.md) — agent definition standards (single-file .md with YAML frontmatter)
- [framework/cli.md](framework/cli.md) — CLI command reference
- [framework/skills.md](framework/skills.md) — skill structure and invocation
- [framework/work-tracking.md](framework/work-tracking.md) — worktracker entity hierarchy and directory structure
- [python/patterns.md](python/patterns.md) — Python coding patterns
- [python/testing.md](python/testing.md) — BDD test-first and coverage standards
