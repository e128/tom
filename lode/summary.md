# Summary
*Updated: 2026-04-03T00:00:00Z*

**Jerry** is a Python CLI framework for behavior/workflow guardrails that accrues knowledge, wisdom, and experience across AI-assisted coding sessions. It solves **Context Rot** — the degradation of LLM performance as context fills — by using the filesystem as infinite memory: state is persisted to files and loaded selectively. The framework enforces 25 HARD rules (non-overridable governance constraints), a quality gate threshold of 0.92 for C2+ deliverables, and a skill/agent routing system that proactively invokes specialized skills based on keyword detection. Jerry is managed via `jerry session start|end|status|abandon`, `jerry items list|show`, and `jerry projects list|context|validate`. All Python execution uses `uv run`; dependencies use `uv add`. The codebase follows hexagonal architecture with strict layer isolation and BDD test-first development at 90% line coverage.

## Key Facts

- **Package**: `jerry` (see `pyproject.toml` for version)
- **Python execution**: `uv run` only — never `python` or `pip` directly
- **Architecture**: Hexagonal (domain / application / infrastructure / interface layers)
- **Skills**: `skills/` directory — each has a `SKILL.md` file
- **Agents**: `skills/*/agents/` — dual-file format (`.md` + `.governance.yaml`)
- **Rules**: `.context/rules/` — auto-loaded at session start via `.claude/rules/` symlink
- **Active projects**: `projects/` directory, managed via `/worktracker` skill

## Related Lode Files

- [terminology.md](terminology.md) — Jerry-specific vocabulary
- [framework/architecture.md](framework/architecture.md) — hexagonal layer details
- [framework/rules.md](framework/rules.md) — quality enforcement and HARD rules
