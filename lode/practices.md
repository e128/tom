# Practices
*Updated: 2026-04-03T14:08:55Z*

Key conventions, workflow rules, and project patterns. The source of truth for how to work in this repo.

## Python Environment

All Python execution uses `uv run` (never `python` directly). Dependencies use `uv add` (never `pip install`). This is HARD rule H-05 — violations corrupt the environment.

```bash
uv run tom session start          # run the CLI
uv run pytest tests/                # run tests
uv add some-package                 # add a dependency
uv sync                             # sync environment
```

## Testing

BDD test-first (Red phase first) at 90% line coverage. Tests live in `tests/`. Use `uv run pytest tests/`. Markers are configured in `pyproject.toml`.

## Session Workflow

1. Set `JERRY_PROJECT` environment variable (required by H-04)
2. Run `tom session start` — loads project context
3. Do work
4. Run `tom session end` — persists session state
5. After any code change, update the affected lode files (post-change verification)

## Skill Invocation

Skills are invoked proactively by keyword detection (H-22). The `/problem-solving` skill handles research/analysis; `/nasa-se` handles requirements/design; `/orchestration` handles multi-phase workflows. Never wait for the user to invoke skills — trigger them proactively when keywords match.

## Commit Style

Semantic commit messages. Use `devex:commit` skill for formatting.

## Lode Maintenance

After any session where more than 3 source files were modified:
1. `nu scripts/lode-ts.nu --changed` to update timestamps on modified lode files
2. Check for STALE_CONTENT with the `lode-sync` agent
3. Run `/lode-audit` periodically after large refactors

## File Size Limits

- Lode files: 250 lines maximum; decompose into sub-files if larger
- Agent definitions: no hard limit but keep focused on one concern
- Skill SKILL.md files: no hard limit but keep concise

## Architecture Layer Rules (H-07)

- Domain layer imports: only domain interfaces and `shared_kernel`
- Application layer imports: domain + shared_kernel only (no infrastructure/interface)
- Infrastructure layer: may import domain, application, and external libraries
- Composition root: the only place infrastructure is wired to ports

## Related Lode Files

- [framework/rules.md](framework/rules.md) — full HARD rules reference
- [framework/architecture.md](framework/architecture.md) — hexagonal layer details
- [python/testing.md](python/testing.md) — BDD and pytest specifics
