# BUG-005: Skill(jerry:name) permission pattern undocumented (#181)

> **Type:** bug
> **Status:** completed
> **Priority:** high
> **Impact:** high
> **Severity:** major
> **Created:** 2026-03-11
> **Completed:** 2026-03-14
> **Parent:** PROJ-030-bugs
> **Owner:** saucer-boy
> **Found In:** 0.29.0
> **Fix Version:** 0.29.1

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Summary](#summary) | Brief description and key details |
| [Steps to Reproduce](#steps-to-reproduce) | Steps to reproduce the issue |
| [Root Cause Analysis](#root-cause-analysis) | Investigation and root cause details |
| [A/B Test Results](#ab-test-results) | Empirical permission pattern testing |
| [Fix Description](#fix-description) | Solution approach and changes made |
| [Acceptance Criteria](#acceptance-criteria) | Conditions for bug to be fixed |
| [Related Items](#related-items) | Hierarchy and related work items |
| [History](#history) | Status changes and key events |

---

## Summary

Claude Code settings.local.json contained `Skill(jerry:name)` and `Skill(name)` permission entries without verified understanding of which form the permission system matches against. The Anthropic documentation is ambiguous for plugin-namespaced skills — examples only show short names, and the plugin namespace section doesn't address the permission pattern.

---

## Steps to Reproduce

1. Open `.claude/settings.local.json`
2. Observe entries like `Skill(jerry:adversary)` and `Skill(adversary)`
3. Check Anthropic docs at code.claude.com/docs/en/skills and code.claude.com/docs/en/permissions
4. Note that docs only show non-namespaced examples — no guidance on plugin-namespaced skills
5. Remove all Skill() entries and invoke a skill — observe permission prompt (Test 1)

**Key Details:**
- **Symptom:** Unclear whether skill permission entries were functional or inert
- **Frequency:** Affects every session start (permission evaluation)
- **Workaround:** Both forms included (belt-and-suspenders)

---

## Root Cause Analysis

### Investigation Summary

The S-013 Inversion review raised IN-001: "We've never verified that Skill(name) actually grants permissions at runtime." Initial investigation (skill-permission-runtime-investigation.md) confirmed Skill() is a documented pattern but relied on documentation analysis without empirical testing. The docs are genuinely ambiguous about plugin-namespaced skills.

### Root Cause

Anthropic documentation gap: the `Skill()` permission syntax section uses only non-namespaced examples (`Skill(commit)`, `Skill(deploy *)`). The skills documentation says plugin skills use `plugin-name:skill-name` namespace but doesn't specify whether the permission system matches against the short name, the fully-qualified name, or both.

### Contributing Factors

- Prior work declared the ambiguity resolved based on documentation analysis alone (no A/B test)
- The short form working by coincidence (no name collisions exist) masked the need to verify

---

## A/B Test Results

Empirical testing conducted 2026-03-14 within a live Claude Code session:

| Test | Config | Skill Invoked | Prompted? | Runtime Auto-Added |
|------|--------|--------------|-----------|-------------------|
| 1 | No Skill() entries | `/worktracker` | **YES** | `Skill(worktracker)` (short form) |
| 2 | `Skill(adversary)` only | `/adversary` | **NO** | — |
| 3 | `Skill(jerry:ast)` only | `/jerry:ast` | **NO** | — |
| 4 | `Skill(jerry:*)` wildcard | `/jerry:diataxis` | **NO** | — |

### Key Findings

1. **Skill() entries are required** — without them, Claude Code prompts for permission in `default` mode (Test 1)
2. **Both forms work** — short name and fully-qualified name both suppress prompts (Tests 2, 3)
3. **Claude Code's runtime writes short form** — when auto-adding "don't ask again" entries, the runtime writes `Skill(worktracker)` not `Skill(jerry:worktracker)` (Test 1 observation)
4. **Wildcard works** — `Skill(jerry:*)` matches all jerry plugin skills (Test 4)
5. **Fully-qualified form is the only collision-safe approach** — the plugin namespace exists to disambiguate when multiple plugins share skill names; the short form works only when there are no collisions

### Decision

Use `Skill(jerry:*)` — fully-qualified namespace wildcard. This is collision-safe, covers all current and future jerry skills, and eliminates the need to update settings when new skills are added.

---

## Fix Description

### Solution Approach

Replace 19 individual `Skill(jerry:name)` entries with a single `Skill(jerry:*)` wildcard in settings.local.json.

### Changes Made

- settings.local.json: 56 allow entries → 4 entries (1 skill wildcard + 3 MCP wildcards)
- Removed all deprecated `Bash(:*)` colon syntax entries
- Removed all Bash entries subsumed by settings.json
- Removed hooks block (P-020/P-022 violations per C4 tournament)

### Code References

| File | Change Description |
|------|-------------------|
| `.claude/settings.local.json` | Replaced 19 explicit Skill entries with `Skill(jerry:*)` wildcard |
| `projects/PROJ-030-bugs/research/skill-permission-runtime-investigation.md` | IN-001 investigation artifact |
| `projects/PROJ-030-bugs/work/devsecops/settings-local-json-design.md` | Architecture design document |

---

## Acceptance Criteria

### Fix Verification

- [x] `Skill(jerry:*)` wildcard suppresses prompts for all jerry plugin skills
- [x] A/B test results documented with empirical evidence
- [x] Settings.local.json uses only documented, collision-safe permission patterns
- [x] No regression in skill invocation behavior

---

## Related Items

### Hierarchy

- **Parent:** PROJ-030-bugs

### Related Items

- **GitHub Issue:** [#181](https://github.com/geekatron/jerry/issues/181)
- **Related Bug:** [BUG-004](BUG-004-settings-json-schema.md) — settings.json invalid fields (#180)
- **Related Task:** [TASK-005](TASK-005-bash-syntax-migration.md) — Bash syntax migration (#182)
- **Research:** `projects/PROJ-030-bugs/research/skill-permission-runtime-investigation.md`
- **Research:** `projects/PROJ-030-bugs/research/skill-permission-bash-syntax-research.md`
- **Design:** `projects/PROJ-030-bugs/work/devsecops/settings-local-json-design.md`

---

## History

| Date | Status | Notes |
|------|--------|-------|
| 2026-03-11 | pending | Initial report from S-013 Inversion review (IN-001) |
| 2026-03-14 | in_progress | Documentation analysis + A/B testing |
| 2026-03-14 | completed | Resolved with Skill(jerry:*) wildcard based on empirical tests |
