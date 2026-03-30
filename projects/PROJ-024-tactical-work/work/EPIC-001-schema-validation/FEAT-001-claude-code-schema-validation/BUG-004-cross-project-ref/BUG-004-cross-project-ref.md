# BUG-004: Fix Cross-Project Reference in ADR-STORY015-001 (Pre-Existing Test Failure)

> **Type:** bug
> **Status:** pending
> **Priority:** high
> **Impact:** medium
> **Created:** 2026-03-30T00:00:00Z
> **Due:**
> **Completed:**
> **Parent:** FEAT-001
> **Owner:**
> **Effort:** 1

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

ADR-STORY015-001-tier-model-renumbering.md references `projects/PROJ-018` which violates project isolation. Causes 1 test failure in test_path_conventions.py. Fix: remove or replace the cross-project reference.

---

## Acceptance Criteria

- [ ] test_no_cross_project_references[PROJ-024-tactical-work] passes
- [ ] No cross-project references in PROJ-024 files
- [ ] Full test suite passes with zero failures

---

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Blocks | BUG-005 | Clean test suite baseline needed before hook test fixes |
| Blocks | STORY-025 | Clean test suite needed for CLI integration |

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-30 | adam.nowak | pending | Created. Internal finding from test suite -- no GitHub Issue. |
