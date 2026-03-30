# STORY-023: Remove Deprecated scripts/pre_tool_use.py (GH #177)

> **Type:** story
> **Status:** pending
> **Priority:** medium
> **Impact:** medium
> **Created:** 2026-03-30T00:00:00Z
> **Due:**
> **Completed:**
> **Parent:** FEAT-001
> **Owner:**
> **Effort:** 1
> **GitHub Issue:** [#177](https://github.com/geekatron/jerry/issues/177)

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

scripts/pre_tool_use.py is deprecated since #150 migration to plugin hooks. Dead code in CI path. Remove the file and update any references.

---

## Acceptance Criteria

- [ ] scripts/pre_tool_use.py deleted
- [ ] No remaining imports or references to the old hook
- [ ] Pre-commit hooks still pass
- [ ] CI pipeline still passes

---

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Blocks | STORY-024 | Consolidate hooks after deprecated one is removed |
| Blocks | BUG-005 | Hook infrastructure must be clean before fixing hook tests |

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-30 | adam.nowak | pending | Created from PROJ-024 session. Linked to GH #177. |
