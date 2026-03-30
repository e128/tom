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

scripts/tests/test_hooks.py expects a "decision" field in hook output that doesn't exist. 15 tests broken. Currently excluded via --ignore in pytest.ini. Fix the test assertions to match current hook output format.

---

## Acceptance Criteria

- [ ] test_hooks.py tests pass (all 15)
- [ ] --ignore=scripts/tests/test_hooks.py removed from pytest.ini
- [ ] test_patterns.py tests pass (if applicable, remove --ignore)
- [ ] Full test suite passes with hook tests included

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
