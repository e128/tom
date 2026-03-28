# TASK-005: Fix M-005 -- orchestration Agents Add Web Tools

> **Type:** story
> **Status:** pending
> **Priority:** medium
> **Created:** 2026-03-28T00:00:00Z
> **Parent:** STORY-013

---

## Description

`orchestration/SKILL.md` `allowed-tools` includes `WebSearch, WebFetch` but orch-planner, orch-synthesizer, orch-tracker don't declare them in their frontmatter.

**User Feedback:** Add them to the agent frontmatter.

## Acceptance Criteria

- [ ] `skills/orchestration/agents/orch-planner.md` tools includes `WebSearch, WebFetch`
- [ ] `skills/orchestration/agents/orch-synthesizer.md` tools includes `WebSearch, WebFetch`
- [ ] `skills/orchestration/agents/orch-tracker.md` tools includes `WebSearch, WebFetch`
- [ ] All three governance YAMLs updated if tool_tier needs to change
- [ ] `jerry agents validate-frontmatter` passes for all three

## Files to Change

- `skills/orchestration/agents/orch-planner.md`
- `skills/orchestration/agents/orch-synthesizer.md`
- `skills/orchestration/agents/orch-tracker.md`
- Possibly their `.governance.yaml` files (tier update)
