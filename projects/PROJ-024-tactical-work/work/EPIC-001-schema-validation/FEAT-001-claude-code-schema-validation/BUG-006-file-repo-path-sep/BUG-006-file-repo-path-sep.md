# BUG-006: Fix file_repository.py Hardcoded Forward Slash (GH #117)

> **Type:** bug
> **Status:** pending
> **Priority:** medium
> **Impact:** medium
> **Created:** 2026-03-30T00:00:00Z
> **Due:**
> **Completed:**
> **Parent:** FEAT-001
> **Owner:**
> **Effort:** 1
> **GitHub Issue:** [#117](https://github.com/geekatron/jerry/issues/117)

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

file_repository.py uses hardcoded "/" instead of pathlib for path construction. Breaks on Windows. Same portability theme as GH #113 (statusline fix).

---

## Acceptance Criteria

- [ ] All hardcoded "/" path separators in file_repository.py replaced with pathlib
- [ ] Existing tests pass
- [ ] Path construction works on both Unix and Windows

---

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Independent | -- | No blockers |
| Related | GH #113 | Same portability theme, already closed |

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-30 | adam.nowak | pending | Created from PROJ-024 session. Linked to GH #117. |
