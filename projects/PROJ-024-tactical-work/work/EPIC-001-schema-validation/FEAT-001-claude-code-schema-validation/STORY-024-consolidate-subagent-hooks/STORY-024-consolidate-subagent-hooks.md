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

SubagentStop hook logic exists in both scripts/ and CLI. Consolidate to single implementation to prevent drift and reduce maintenance burden.

---

## Acceptance Criteria

- [ ] Single SubagentStop hook implementation (no duplication)
- [ ] Hook behavior unchanged (same blocking/warning behavior)
- [ ] All existing tests pass
- [ ] No references to the removed duplicate

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
