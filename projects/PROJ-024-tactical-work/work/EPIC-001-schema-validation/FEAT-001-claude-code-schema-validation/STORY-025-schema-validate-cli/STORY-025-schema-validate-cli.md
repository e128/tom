# STORY-025: Add jerry schema validate CLI Command (GH #193)

> **Type:** story
> **Status:** pending
> **Priority:** medium
> **Impact:** high
> **Created:** 2026-03-30T00:00:00Z
> **Due:**
> **Completed:**
> **Parent:** FEAT-001
> **Owner:**
> **Effort:** 2
> **GitHub Issue:** [#193](https://github.com/geekatron/jerry/issues/193)

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

validate-agent-frontmatter.py runs as a separate CI step. Port the P-003 check into the CLI command (jerry agents validate-frontmatter) so there's one code path, not two. Remove the separate CI step.

---

## Acceptance Criteria

- [ ] jerry agents validate-frontmatter includes P-003 Agent tool check
- [ ] CI workflow uses single command (remove separate script step)
- [ ] 89/89 agents pass via CLI command
- [ ] P-003 check has same behavior (string normalization, type-hardened T5, fail-closed)

---

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Blocked By | BUG-004 | Clean test baseline |
| Blocked By | BUG-005 | All hook tests passing |

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-30 | adam.nowak | pending | Created from PROJ-024 session. Linked to GH #193. |
