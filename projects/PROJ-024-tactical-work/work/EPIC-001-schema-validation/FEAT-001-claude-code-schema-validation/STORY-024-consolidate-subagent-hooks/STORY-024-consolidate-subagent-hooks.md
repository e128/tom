# STORY-024: Consolidate Dual SubagentStop Hooks (GH #178)

> **Type:** story
> **Status:** pending
> **Priority:** medium
> **Impact:** medium
> **Created:** 2026-03-30T00:00:00Z
> **Due:**
> **Completed:**
> **Parent:** FEAT-001
> **Owner:**
> **Effort:** 2
> **GitHub Issue:** [#178](https://github.com/geekatron/jerry/issues/178)

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Summary](#summary) | What and why |
| [Acceptance Criteria](#acceptance-criteria) | Verification checklist |
| [Dependencies](#dependencies) | Relationship to other work |
| [History](#history) | Change log |

---

## Summary

SubagentStop hook logic exists in both `scripts/` (standalone) and CLI (`src/`). The standalone script bypasses Clean Architecture and creates a parallel code path that drifts from the CLI. Consolidate to the CLI implementation only.

---

## Architectural Constraints

| Constraint | Rationale |
|------------|-----------|
| **MUST NOT introduce new scripts** | The scripts/ directory is for build tooling only, not runtime hooks. Hook logic belongs in `src/` under Clean Architecture. |
| **Consolidated implementation MUST live in `src/`** | Domain rules in domain layer, hook handling in application/infrastructure layers. The `.claude/hooks/` entry point invokes `uv run jerry ...` CLI commands. |
| **MUST follow Clean Architecture** | SubagentStop enforcement logic follows hexagonal layers: domain (stop rules), application (command handler), infrastructure (hook adapter). |
| **MUST be testable via `tests/`** | Tests go in `tests/` (unit/integration/e2e), not `scripts/tests/`. CLI command is the test boundary. |

---

## Acceptance Criteria

- [ ] Single SubagentStop implementation in `src/` (Clean Architecture)
- [ ] `scripts/subagent_stop.py` deleted (if it exists as standalone)
- [ ] `.claude/hooks/` entry point invokes via `uv run jerry ...` CLI command
- [ ] Hook behavior unchanged (same blocking/warning behavior verified by tests)
- [ ] Tests in `tests/` (not `scripts/tests/`) cover the consolidated implementation
- [ ] All existing tests pass
- [ ] No references to the removed duplicate
- [ ] Zero new files in `scripts/`

---

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Blocked By | STORY-023 | Remove deprecated hook first to avoid conflicts |
| Blocks | BUG-005 | Hook infrastructure clean before fixing hook tests |

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-30 | adam.nowak | pending | Created from PROJ-024 session. Linked to GH #178. |
