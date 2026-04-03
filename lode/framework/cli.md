# Tom CLI
*Updated: 2026-04-03T14:08:50Z*

The `tom` CLI is the primary interface. Run via `uv run tom <command>`.

## Command Reference

```bash
# Session management
tom session start           # start a work session, load project context
tom session end             # end session, persist state
tom session status          # show current session state
tom session abandon         # abandon session without persisting

# Work items
tom items list              # list work items for active project
tom items show <id>         # show detail for a work item

# Projects
tom projects list           # list all projects
tom projects context        # show context for active project
tom projects validate       # validate project structure
```

## Session Requirements (H-04)

`JERRY_PROJECT` must be set before running session commands. Sessions without an active project are blocked.

## Interface Layer

CLI code lives in `src/interface/cli/`. Each command group is a separate module registered in `parser.py`. Commands use `argparse` (stdlib — no Click or Typer dependency).

## Related Lode Files

- [work-tracking.md](work-tracking.md) — what `items` commands operate on
- [../summary.md](../summary.md) — project overview including CLI version
