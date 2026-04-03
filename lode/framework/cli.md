# Jerry CLI
*Updated: 2026-04-03T00:00:00Z*

The `jerry` CLI is the primary interface. Run via `uv run jerry <command>`.

## Command Reference

```bash
# Session management
jerry session start           # start a work session, load project context
jerry session end             # end session, persist state
jerry session status          # show current session state
jerry session abandon         # abandon session without persisting

# Work items
jerry items list              # list work items for active project
jerry items show <id>         # show detail for a work item

# Projects
jerry projects list           # list all projects
jerry projects context        # show context for active project
jerry projects validate       # validate project structure
```

## Session Requirements (H-04)

`JERRY_PROJECT` must be set before running session commands. Sessions without an active project are blocked.

## Interface Layer

CLI code lives in `src/jerry/interface/`. Each command group is a separate module. Commands use Click or Typer (see `pyproject.toml` for the current dependency).

## Related Lode Files

- [work-tracking.md](work-tracking.md) — what `items` commands operate on
- [../summary.md](../summary.md) — project overview including CLI version
