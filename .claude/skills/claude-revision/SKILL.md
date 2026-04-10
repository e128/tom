---
name: claude-revision
description: >
  Periodic health check for the entire Claude Code configuration — agents, skills, CLAUDE.md, rules,
  and lode memory. Optionally fetches latest Anthropic guidance (web research is skippable with --no-web),
  reviews all agents for model/tool/memory optimization, reviews all skills for token efficiency,
  audits CLAUDE.md and .context/rules/ files, checks agent memory health and git tracking, and writes
  a dated revision log to lode/ for cross-session continuity. Run monthly or after bulk agent/skill changes.
  Triggers on: claude revision, periodic audit, agent health check, skill optimization, claude config
  review, monthly claude audit, revision audit, config health, claude maintenance, agents audit,
  skills audit, claude audit.
argument-hint: "[--no-web] [--agents-only] [--skills-only] [--self] [--archive]"
---

# Claude Revision

Periodic health check for the Claude Code configuration. Reviews agents, skills, CLAUDE.md, rules,
and lode memory against the latest official guidance. Writes findings to the revision log for
cross-session continuity — the log at `lode/infrastructure/claude-revision-log.md` is this skill's
persistent memory (skills have no `memory:` field; lode is the only cross-session store).

## Scope Flags

- `--no-web` — skip Phase 1 (web research); fast local run
- `--agents-only` — run Phases 0, 2, 5–6 only
- `--skills-only` — run Phases 0, 3, 4, 5–6 only
- `--self` — include `claude-revision` itself in Phase 3 skill review (normally skipped)
- `--archive` — move older entries in the revision log to an archive file before running

## Phase 0: Load Last Run Context

Read `lode/infrastructure/claude-revision-log.md` if it exists. Surface:
- Date of last run and deferred items
- Agent/skill counts (to detect additions or removals since last run)

If the file doesn't exist, this is the first run — proceed without prior context.

**Archive check:** Count entries in the `## Runs` section. If the log exceeds 200 lines, warn the user
and suggest running with `--archive` to move older entries to `claude-revision-log-archive.md`. If
`--archive` flag is present, do the archive before proceeding.

## Phase 1: Web Research _(skip with `--no-web`)_

Spawn a research agent with these targets:
- `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` — **primary source**: version history with all new features, breaking changes, and deprecations. Filter entries since the last revision log date.
- `https://code.claude.com/docs/en/sub-agents` — agent config (model, tools, memory, maxTurns)
- `https://code.claude.com/docs/en/skills` — skill architecture, trigger patterns
- `https://platform.claude.com/docs/en/agent-sdk/overview` — SDK patterns
- `https://github.com/anthropics/skills` — official skill examples: frontmatter conventions, trigger phrasing, file structure, and reference implementations
- `https://github.com/anthropics/skills/commits/main/` — recent commits: detect new skills, structural changes, or pattern shifts since the last run date

Compare against the last revision log entry date (from Phase 0) to determine if guidance has changed
since the last run. Report new or changed fields, features, or best practices. Report "No new guidance
since YYYY-MM-DD" if unchanged.

## Phases 2–4: Run Directly (No Sub-Agents)

Run in sequence. Direct bash/grep — no Explore agents.

### Phase 2: Agent Review

Tom agents live in TWO locations:
- `.claude/agents/*.md` — lightweight Claude Code agents (lode-sync, etc.)
- `skills/*/agents/*.md` — framework skill agents (~85 agents)

Run these commands directly:

1. Count and list all agents:
   `find .claude/agents skills/*/agents -name "*.md" 2>/dev/null | wc -l` → agent count
   `find .claude/agents skills/*/agents -name "*.md" 2>/dev/null` → agent list

2. Extract frontmatter fields in one pass:
   `rg "^(model|memory|maxTurns|isolation|tools|effort|color):" .claude/agents/ skills/*/agents/ --with-filename`

3. Flag agents with `isolation: worktree` but no explicit `model:`:
   `rg -l "isolation: worktree" .claude/agents/ skills/*/agents/ | xargs -I{} sh -c 'grep -L "^model:" {} && echo "  → no model"'`

4. Find iterating agents (have Agent/Bash tool) missing maxTurns:
   `rg -l "Agent|Bash" .claude/agents/ skills/*/agents/ | xargs rg -L "maxTurns:"`

5. Check model-tier alignment:
   Haiku agents with T4 tools (WebSearch, WebFetch, Context7 MCP) should be verified — haiku is for
   read/search/parse, not reasoning about external docs. Cross-check against mcp-tool-standards.md
   Agent Integration Matrix before flagging (some haiku+T4 are justified by design).

Evaluate only what the grep output reveals against these criteria:

| Check | Criteria |
|-------|----------|
| Model | `haiku` = read/search/count/parse; `sonnet` = reasoning/writing/cross-ref; `opus` = rare orchestration only |
| Tools | Allowlist present? Unnecessary tools increase attack surface and context load |
| maxTurns | Iterating agents (build→fix→test loops) need an explicit limit to prevent runaway |
| memory | Agents that learn codebase-specific patterns across sessions should have `memory: project` |
| effort | Per ET-M-001: C1=low, C2=medium, C3=high, C4=max. Validation agents should use `low` |
| Overlap | Does it duplicate another agent? Should it be merged or differentiated? |
| Description | Clear trigger keywords? Unambiguous when to use vs. similar agents? |

Do not read individual agent files unless a specific field is missing from the grep output.

Return: table of `(agent, lines, model, memory, effort, issues)`. Flag issues HIGH/MEDIUM/LOW.

### Phase 3: Skill Review

Tom skills live in TWO locations:
- `.claude/skills/*/` — lightweight Claude Code skills (lode, lode-audit, yeet, claude-revision)
- `skills/*/SKILL.md` — framework skills (~30 skills)

Run these commands directly:

1. Count skills and get line counts:
   `find .claude/skills -name "SKILL.md" -o -name "WORKFLOW.md" 2>/dev/null | xargs wc -l | sort -rn | head -20`
   `find skills -name "SKILL.md" | xargs wc -l | sort -rn | head -30`

2. Flag skills over 250 lines for review — read only those files.

3. Check for stale agent references in skills:
   Get agent names from both locations, then grep for any known-removed agents.

4. Check for duplicate skills across both locations:
   Compare skill names in `.claude/skills/` against `skills/` — flag any that exist in both.

Read individual skill files only for skills flagged as over-size or containing stale references.

Evaluate flagged skills against these criteria:

| Check | Criteria |
|-------|----------|
| Size | Over 250 lines? Identify content suitable for lode/ or a referenced sub-file |
| Triggers | Too broad (always fires)? Too narrow (never fires)? Missing key phrases? |
| Overlap | Duplicates content in another skill or CLAUDE.md? |
| Staleness | References removed files, old APIs, or outdated patterns? |
| Duplicate | Same skill in both `.claude/skills/` and `skills/`? Consolidate to one location |
| Type | Operational (workflow steps) vs Reference (knowledge injection) — both valid; never flag reference skills for lacking workflow steps |

Return: table of `(skill, lines, type, issues)`. Flag issues HIGH/MEDIUM/LOW.
Skip `claude-revision` itself unless `--self` flag is provided.

### Phase 4: CLAUDE.md and Rules Audit

Tom has:
- `CLAUDE.md` at repo root
- `.context/rules/*.md` (symlinked into `.claude/rules/`)

Run these commands directly:

1. Check rules for stale agent or skill references:
   `rg "skills/[a-z-]+/agents/[a-z-]+" .context/rules/ CLAUDE.md`
   Extract agent names from output → verify each exists.

2. Check for volatile counts in rules files:
   `rg "[0-9]+ (agents?|skills?|rules?)" .context/rules/ CLAUDE.md`

3. Check CLAUDE.md skill table matches actual top-level skills:
   Compare skill list in CLAUDE.md against `ls skills/` (excluding UX sub-skills invoked by
   /user-experience orchestrator, and `shared/` template directory).

Only read full files if a specific issue is found by grep.

Evaluate findings against these criteria:

| Type | Flag When |
|------|-----------|
| Redundant | Duplicates a skill, lode entry, or another rule |
| Verbose | Long explanation where a short rule works |
| Stale | References removed agents, skills, or counts that have changed |
| Conflict | Contradicts a skill or rule |

Return: table of `(file, line, type, finding, recommendation)`.

### Phase 5: Local Health Checks

**5a. Agent Memory Health**

1. Glob `.claude/agent-memory/*/MEMORY.md`
2. For each file: check line count — flag any over 200 lines
3. Cross-check agent frontmatter: which agents declare `memory: project`? Do all have a MEMORY.md? Any with MEMORY.md but no `memory:` flag?
4. Git tracking: `git ls-files --others --exclude-standard .claude/agent-memory/`

**5b. Lode Check**

Check last commit dates for key lode files:
```bash
git log --format="%ad %s" --date=short -1 -- lode/summary.md
git log --format="%ad %s" --date=short -1 -- lode/framework/agents.md
git log --format="%ad %s" --date=short -1 -- lode/lode-map.md
git log --format="%ad %s" --date=short -1 -- lode/infrastructure/claude-revision-log.md
```

Flag entries where last commit date is older than 30 days, or where content references
agents/skills that no longer exist.

## Phase 6: Report & Log

```
## Claude Revision — [DATE]

**Agents:** N reviewed | **Skills:** N reviewed | **Last run:** [date or "first run"]

### Web Guidance (Phase 1)
[New guidance / No changes since DATE / Skipped]

### Agent Health — N agents
| Agent | Lines | Model | Memory | Effort | Issues |
|-------|-------|-------|--------|--------|--------|

### Skill Health — N skills
| Skill | Lines | Type | Issues |
|-------|-------|------|--------|

### CLAUDE.md & Rules
| File | Line | Type | Finding | Recommendation |
|------|------|------|---------|----------------|

### Memory Health
| Agent | MEMORY.md | Lines | Git tracked | Issues |
|-------|-----------|-------|-------------|--------|

### Lode
[Stale entries / All current]

---
HIGH: N  |  MEDIUM: N  |  LOW: N
```

Present the report. **Do not apply any changes yet.** Then ask:
> "Which items would you like to address? (IDs, 'all high', 'agents only', or 'skip')"

After the user responds (or skips), append to `lode/infrastructure/claude-revision-log.md`:

```markdown
### [YYYY-MM-DD]
- Agents: N | Skills: N | Memory files: N
- Web guidance: [new items found / no changes since DATE / skipped]
- HIGH: N | MEDIUM: N | LOW: N
- Actions taken: [list or "none"]
- Deferred: [list or "none"]
```

If the file doesn't exist, create it with this header first:

```markdown
# Claude Revision Log
*Updated: [timestamp]*

Persistent memory for `/claude-revision`. Each run appends one entry.
Read at Phase 0 to recover last-known state and deferred items.

## Runs
```

## Guidelines

- **Phases 2–4 use direct bash/grep, not sub-agents** — sub-agents burn context; direct grep returns exactly the fields needed
- **Don't auto-fix** — present findings, wait for user direction
- **Phase 5a git check is mandatory** — untracked MEMORY.md files vanish on clone
- **Reference skills are complete as-is** — do not flag knowledge-only skills for lacking workflow steps

## User Input

$ARGUMENTS

## Self-Improvement (Mandatory)

This skill must get better with every use. The revision log at `lode/infrastructure/claude-revision-log.md` IS this skill's persistent memory — always append to it at Phase 6.

1. **Always write the Phase 6 log entry** — Even if no changes were made, the dated entry creates a timestamp baseline for detecting drift.
2. **Record deferred items explicitly** — When the user declines to fix a finding, log it under "Deferred" with the original severity.
3. **Capture new check criteria** — If a new pattern was found that should be checked in future runs, document it in SKILL.md criteria tables.
4. **Note guidance changes** — When Phase 1 web research finds a new Anthropic best practice, note it in the log entry.

## Troubleshooting

- **Web fetch fails** — use `--no-web` for fast local-only run
- **Sparse grep results** — no matches means the field is absent; note and continue
- **First run** — normal; no prior context; log created at Phase 6
- **Untracked MEMORY.md files** — run `git add .claude/agent-memory/`
- **Reference skills flagged for missing workflow** — reference skills are complete as-is; re-check classification
- **Log too large** — archive older runs to `claude-revision-log-archive.md`
