# Tom CLI
*Updated: 2026-04-07T23:59:38Z*

The `tom` CLI is the primary interface. Run via `uv run tom <command>`. All namespaces accept a `--json` global flag for machine-readable output.

## Command Reference

```bash
# Session management
tom session start           # start a work session, load project context
tom session end             # end session, persist state
tom session status          # show current session state
tom session abandon         # abandon session without persisting

# Work items
tom items list              # list work items for active project
tom items list --status <s> # filter by status (pending|in_progress|blocked|done|cancelled)
tom items list --type <t>   # filter by type (task|bug|story|epic|subtask|spike)
tom items show <id>         # show detail for a work item
tom items create <title>    # create a new work item (--type, --parent)
tom items start <id>        # mark item in progress
tom items complete <id>     # mark item done
tom items block <id>        # mark item blocked (--reason required)
tom items cancel <id>       # cancel item

# Projects
tom projects list           # list all projects
tom projects context        # show context for active project
tom projects validate <id>  # validate project structure

# Configuration
tom config show             # display all config values (--source to show origin)
tom config get <key>        # get a specific config value
tom config set <key> <val>  # set a config value (--scope project|root|local)
tom config path             # show config file paths

# Transcripts
tom transcript parse <file> # parse VTT/SRT to canonical JSON (--output-dir, --profile, --model-*)

# Context monitoring
tom context estimate        # compute context fill estimate (reads Claude Code JSON from stdin)

# Markdown AST
tom ast parse <file>        # parse markdown to AST JSON
tom ast render <file>       # roundtrip render via mdformat
tom ast validate <file>     # validate markdown (--schema, --nav)
tom ast query <file> <sel>  # query AST nodes by type
tom ast frontmatter <file>  # extract blockquote frontmatter fields
tom ast modify <file>       # modify a frontmatter field (--key, --value required)
tom ast reinject <file>     # extract L2-REINJECT directives
tom ast detect <file>       # detect document type
tom ast sections <file>     # extract XML-tagged sections
tom ast metadata <file>     # extract HTML comment metadata

# Agent build pipeline
tom agents build            # build vendor-specific agent files (--adapter, --agent, --dry-run)
tom agents extract          # reverse-engineer canonical source from vendor files
tom agents validate         # validate canonical agent definitions against schema
tom agents list             # list agents with metadata (--skill)
tom agents diff             # show drift between canonical and generated files
tom agents validate-frontmatter  # validate YAML frontmatter in agent/skill files

# CI utilities
tom ci detect-bump-type     # detect version bump type from conventional commits

# Hook event handlers
tom hooks prompt-submit     # handle UserPromptSubmit hook event
tom hooks session-start     # handle SessionStart hook event
tom hooks pre-compact       # handle PreCompact hook event
tom hooks pre-tool-use      # handle PreToolUse hook event
tom hooks stop              # handle Stop hook event (context stop gate)
tom hooks subagent-stop     # handle SubagentStop hook event
```

## Session Requirements (H-04)

`JERRY_PROJECT` must be set before running session commands. Sessions without an active project are blocked.

## Interface Layer

CLI code lives in `src/interface/cli/`. Each command group is a separate module registered in `parser.py`. Commands use `argparse` (stdlib — no Click or Typer dependency).

## Related Lode Files

- [work-tracking.md](work-tracking.md) — what `items` commands operate on
- [../summary.md](../summary.md) — project overview including CLI version
