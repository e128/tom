# TASK-004: Fix M-004 -- nse-requirements Tier Resolution

> **Type:** story
> **Status:** pending
> **Priority:** high
> **Created:** 2026-03-28T00:00:00Z
> **Parent:** STORY-013

---

## Description

`nse-requirements` declares `tool_tier: T4` but has WebSearch + WebFetch (T3) + Memory-Keeper (T4) = effectively T5 capability without the Agent tool.

**User Feedback:** "I think we are missing a Tier or Two. Why wouldn't we want other agents to leverage Memory-Keeper?"

**BLOCKED:** This task is deferred until STORY-015 (Tier Model Renumbering ADR) completes. The fix depends on the new tier definitions.

## Acceptance Criteria

- [ ] STORY-015 completed with new tier model
- [ ] `nse-requirements` governance `tool_tier` updated to match new model
- [ ] `jerry agents validate-frontmatter --agent nse-requirements` passes

## Dependencies

| Type | Item | Description |
|------|------|-------------|
| Blocked By | STORY-015 | Tier renumbering must land first |

## Files to Change

- `skills/nasa-se/agents/nse-requirements.governance.yaml`
- Possibly `docs/schemas/agent-governance-v1.schema.json` (tool_tier enum update per STORY-015)
