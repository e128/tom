# TASK-001: Create CHANGELOG.md and establish changelog process

> **Type:** task
> **Status:** completed
> **Priority:** high
> **Classification:** BUSINESS
> **Activity:** DOCUMENTATION
> **Created:** 2026-03-09T00:00:00Z
> **Parent:** EN-001

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Description](#description) | What this task covers |
| [Acceptance Criteria](#acceptance-criteria) | Definition of done |
| [Related Items](#related-items) | Linked items |
| [History](#history) | Status changes |

---

## Summary

Create CHANGELOG.md at repo root and establish changelog update convention enforced by CI.

---

## Description

Create the initial `CHANGELOG.md` file at the repository root using [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format. Document all changes from PR #152 (BUG-003 fix) and PR #154 (EN-001 CI hardening). Establish the convention that changelog updates are part of every PR going forward.

---

## Acceptance Criteria

- [ ] `CHANGELOG.md` exists at repo root in Keep a Changelog format
- [ ] All changes from PR #152 (BUG-003) are documented under appropriate categories
- [ ] All changes from PR #154 (EN-001) are documented under appropriate categories
- [ ] Unreleased section present for tracking in-progress changes

---

## Related Items

- **Parent:** [EN-001](EN-001-ci-pipeline-hardening.md)
- **GitHub PR:** [#152](https://github.com/geekatron/jerry/pull/152) — BUG-003 fix
- **GitHub PR:** [#154](https://github.com/geekatron/jerry/pull/154) — EN-001 CI hardening

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-09 | Claude | in_progress | Created. Starting CHANGELOG.md creation. |
| 2026-03-09 | Claude | done | CHANGELOG.md created at repo root in Keep a Changelog format. Covers PR #152 (BUG-003) and PR #154 (EN-001). Convention documented. |
