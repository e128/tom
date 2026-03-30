# BUG-005: Fix BDD Feature Files with Missing Step Definitions (GH #214)

> **Type:** bug
> **Status:** pending
> **Priority:** high
> **Impact:** high
> **Created:** 2026-03-30T00:00:00Z
> **Due:**
> **Completed:**
> **Parent:** FEAT-001
> **Owner:**
> **Effort:** 3
> **GitHub Issue:** [#214](https://github.com/geekatron/jerry/issues/214)

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Summary](#summary) | What's broken |
| [Acceptance Criteria](#acceptance-criteria) | Verification checklist |
| [Dependencies](#dependencies) | Relationship to other work |
| [History](#history) | Change log |

---

## Summary

`scripts/tests/test_hooks.py` tests a deprecated standalone hook (`scripts/pre_tool_use.py`) that is being removed (STORY-023). After STORY-023/024 consolidate hooks into the CLI, these tests must be rewritten to test the CLI-based enforcement -- not the deleted scripts.

---

## Architectural Constraints

| Constraint | Rationale |
|------------|-----------|
| **Tests MUST target Jerry CLI commands, not standalone scripts** | After STORY-023/024, hooks invoke `uv run jerry ...`. Tests should invoke the same CLI entry points. |
| **Tests MUST live in `tests/`, not `scripts/tests/`** | Clean Architecture: test pyramid is in `tests/` (unit/integration/e2e). `scripts/tests/` is an anti-pattern that creates a parallel test infrastructure. |
| **MUST NOT re-create hook tests that invoke scripts directly** | The old tests use `subprocess.run([sys.executable, hook_path])` to invoke scripts. New tests should use CLI commands or import from `src/`. |
| **MUST follow BDD Red/Green/Refactor (H-20)** | Write failing tests for the CLI enforcement behavior first, then verify they pass. |

---

## Acceptance Criteria

- [ ] Hook enforcement tests rewritten in `tests/` (not `scripts/tests/`) targeting CLI commands
- [ ] Tests cover: safe command approval, dangerous command blocking, path blocking, edge cases
- [ ] `scripts/tests/test_hooks.py` deleted (tests the deleted script)
- [ ] `scripts/tests/test_patterns.py` either moved to `tests/` or deleted if redundant
- [ ] `--ignore=scripts/tests/test_hooks.py` removed from pytest.ini
- [ ] `--ignore=scripts/tests/test_patterns.py` removed from pytest.ini
- [ ] Full test suite passes with zero ignored test files
- [ ] No test files remain in `scripts/tests/` except `test_validate_agent_frontmatter.py` (until STORY-025 ports it)

---

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Blocked By | STORY-023 | Deprecated hook removed |
| Blocked By | STORY-024 | Hooks consolidated -- test against final implementation |
| Blocked By | BUG-004 | Clean test baseline |
| Blocks | STORY-025 | All tests must pass before CLI integration |

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-30 | adam.nowak | pending | Created from PROJ-024 session. 15 tests broken, currently excluded. Linked to GH #214. |
