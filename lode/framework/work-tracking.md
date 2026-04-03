# Work Tracking
*Updated: 2026-04-03T00:00:00Z*

Jerry tracks work via a worktracker system. Each project has a `WORKTRACKER.md` index and entity files in `work/`. The `/worktracker` skill is the authoritative guide.

## Entity Hierarchy

```
PROJ (Project)
  └── EPIC
        └── FEAT (Feature)
              └── STORY / ENABLER
                    └── TASK / BUG
```

## Directory Structure (Project-Based Pattern)

```
projects/PROJ-{NNN}-{slug}/
    PLAN.md                    # project plan
    WORKTRACKER.md             # work item index
    work/
        EPIC-{NNN}-{slug}/
            FEAT-{NNN}-{slug}/
                STORY-{NNN}-{slug}/
                    {entity-id}-{slug}.md
```

## WTI Rules

WTI-001 through WTI-009 govern worktracker integrity. Authoritative source: `skills/worktracker/rules/worktracker-behavior-rules.md`.

## Frontmatter

Each entity file has YAML frontmatter with: `id`, `type`, `status`, `title`, and type-specific fields. AST-based parsing is required for entity operations (H-33).

## GitHub Issue Parity (H-32)

When working in the `geekatron/jerry` repo, all worktracker bugs/stories/enablers/tasks MUST have a corresponding GitHub Issue.

## Related Lode Files

- [../summary.md](../summary.md) — `JERRY_PROJECT` requirement (H-04)
- [rules.md](rules.md) — H-32, H-33, H-04
