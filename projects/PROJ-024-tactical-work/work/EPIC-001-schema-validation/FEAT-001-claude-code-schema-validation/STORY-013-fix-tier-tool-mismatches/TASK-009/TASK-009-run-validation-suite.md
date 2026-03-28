# TASK-009: Run Validation Suite After All Fixes

> **Type:** story
> **Status:** pending
> **Priority:** high
> **Created:** 2026-03-28T00:00:00Z
> **Parent:** STORY-013

---

## Description

After all M-001 through M-008 fixes land, run the full validation suite to confirm nothing is broken.

## Acceptance Criteria

- [ ] `jerry agents validate-frontmatter` -- 119/119 pass, 0 failures
- [ ] `uv run python scripts/check_plugin_agent_sync.py` -- 89/89 in sync
- [ ] `uv run pytest tests/schemas/test_frontmatter_schemas.py` -- 41/41 pass

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Blocked By | TASK-001 through TASK-008 | All fixes must land first |
