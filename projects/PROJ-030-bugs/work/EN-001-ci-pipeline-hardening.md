# EN-001: CI pipeline security hardening

> **Type:** enabler
> **Status:** pending
> **Priority:** high
> **Impact:** high
> **Enabler Type:** infrastructure
> **Created:** 2026-03-09T00:00:00Z
> **Due:**
> **Completed:**
> **Parent:** PROJ-030-bugs
> **Owner:**
> **Effort:** 5

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Summary](#summary) | What this enabler covers |
| [Problem Statement](#problem-statement) | Why this work is needed |
| [Technical Approach](#technical-approach) | How the work will be done |
| [Tasks](#tasks) | Individual hardening items |
| [Acceptance Criteria](#acceptance-criteria) | Definition of done |
| [Related Items](#related-items) | Linked bugs and issues |
| [History](#history) | Status changes |

---

## Summary

Security and reliability hardening for all CI/CD workflows (version-bump, release, CI) identified during the BUG-003 investigation. These are systemic pipeline improvements that go beyond the immediate dirty-lockfile fix.

---

## Problem Statement

The BUG-003 investigation (eng-devsecops security review, red-team attack surface analysis) identified 5 findings that affect CI pipeline security beyond the immediate `uv.lock` bug. These are not separate bugs — they are infrastructure debt that the BUG-003 fix exposed but did not address because they span multiple workflow files and concern different attack vectors.

---

## Tasks

| # | Finding | File | Severity | Description |
|---|---------|------|----------|-------------|
| 1 | F-001 | `release.yml` | HIGH | `release.yml` uses `pip install` fallback and bare `uv sync` — apply `uv sync --frozen` consistently; remove `pip` fallback (H-05 violation) |
| 2 | F-004 | `version-bump.yml` | MEDIUM | `workflow_dispatch` bypasses `[skip-bump]` check — a manual trigger can double-bump a commit already marked skip |
| 3 | F-006 | `version-bump.yml` | LOW | `astral-sh/setup-uv@v5` uses floating major-version tag — pin to commit SHA, use Dependabot for updates |
| 4 | RISK-03 | `version-bump.yml` | MEDIUM | `actions/checkout@v5` also uses floating tag — pin to commit SHA |
| 5 | — | `ci.yml` | LOW | Multiple `uv sync` calls without `--frozen` — apply `--frozen` for reproducible CI builds |
| 6 | #150 | `scripts/` | HIGH | Consolidate standalone scripts into jerry CLI per issue #150 |

---

## Technical Approach

Apply `uv sync --frozen` and SHA-pinned actions across all workflows. Port standalone script capabilities into the jerry CLI per issue #150. Each task is a targeted edit to an existing workflow file — no new scripts or infrastructure.

---

## Acceptance Criteria

- [ ] All CI workflows use `uv sync --frozen` (no bare `uv sync` in any workflow)
- [ ] All third-party GitHub Actions pinned to commit SHAs with Dependabot config for updates
- [ ] `release.yml` does not fall back to `pip install` (H-05 compliance)
- [ ] `workflow_dispatch` respects `[skip-bump]` marker
- [ ] No standalone scripts in `scripts/` that duplicate CLI capabilities (issue #150 alignment)

---

## Related Items

### Hierarchy

- **Parent:** [PROJ-030-bugs](../WORKTRACKER.md)

### Related Items

- **Originating Bug:** [BUG-003](BUG-003-version-bump-uv-lock-dirty.md) — investigation that surfaced these findings
- **GitHub Issue:** [#150](https://github.com/geekatron/jerry/issues/150) — standalone script consolidation
- **GitHub Issue:** [#151](https://github.com/geekatron/jerry/issues/151) — version-bump uv.lock dirty
- **Security Review:** [bug-003-devsecops-security-review.md](../reviews/bug-003-devsecops-security-review.md)
- **Attack Surface:** [bug-003-red-recon-attack-surface.md](../reviews/bug-003-red-recon-attack-surface.md)

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-09 | Claude | pending | Created from BUG-003 security review findings |
