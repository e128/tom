---
name: yeet
description: >
  Ship it — lints, tests, commits, and pushes. Adapted for the Tom Python/uv repo.
  Accepts --skip-tests flag to skip build+test when caller already verified them.
  Triggers on: ship it, yeet, push it, commit and push, deploy this, we're done,
  preflight, preflight check, quality check, pre-commit check, ready to commit.
argument-hint: "[--skip-tests] [--dry-run]"
---

# Yeet Skill

Ship it. Quality gate + commit + push in one autonomous pass.

## Modes

| Invocation            | Behavior                                              |
| --------------------- | ----------------------------------------------------- |
| `/yeet`               | Full: PII scan + lint/format + test + commit + push   |
| `/yeet --skip-tests`  | Fast path: PII scan + lint/format only; skips tests   |
| `/yeet --dry-run`     | Quality gate only — no commit or push                 |

`--dry-run` replaces the retired `/preflight` skill.

## Steps

### 0. Gather context (parallel batch)

Run in parallel:

```
A) git status --short                                    (working-tree status)
B) git rev-list --count HEAD ^main 2>/dev/null || echo 0 (ahead count)
C) git branch --show-current                             (current branch)
```

**Early exits:**
- If no changes in working tree → "Nothing to yeet — working tree is clean." **Stop.**

**Derive from status output:**
- Classification: all `.md`/`.json`/`.yml`/`.yaml`/`.txt`/`.toml` = `docs-only`; any `.py` = `code`; else `mixed`
- If `docs-only` AND `--skip-tests` not explicit → auto-enable `--skip-tests`, log: "Docs/config-only change — skipping tests"
- Cache: `py_changed` (count of .py files), `ahead` (commits ahead of main), `branch`

### 1. Lint/format + test

**A) Lint and format (conditional):**
Only if `py_changed > 0`:
```bash
uv run ruff check --fix src/ tests/
uv run ruff format src/ tests/
```
Skip with "Lint/format skipped — no .py files changed" if zero.

**B) Test (conditional):**
Skip if `--skip-tests` (explicit or auto-detected docs-only).
```bash
uv run pytest tests/ -x -q
```
If exit code is non-zero → **stop and report failures.**

**If `--dry-run`**: report quality gate results and **stop here.** Do not continue to step 2.

### 2. Stage + commit + push

- **Stage** — `git add` all modified/deleted tracked files plus new untracked files.
  Exclude: `.env`, `*.key`, `*.pem`, credentials files, `__pycache__/`, `.pyc`.
  Use explicit file names from `git status`, not `git add -A`.

- **PII scan** — grep staged files for home directory paths (`/Users/`, `/home/`, `C:\\Users\\`).
  If found → **stop and report.** Replace with relative paths or env-var substitution before retrying.

- **Lode summary** — if any `lode/` files are staged, show a brief table: `(path, one-line change description)`.

- **Squash** — use `ahead` from step 0:
    - `ahead > 1`: `git reset --soft $(git merge-base main HEAD)` then re-stage and commit as one
    - 1 or 0: proceed normally

- **Craft commit message** — always generate fresh from the actual diff:
    - Run `git diff --cached --stat` to inspect staged changes
    - Synthesize a **conventional commit** summary: `type(scope): imperative summary`
    - Subject line <=72 chars; use a body for detail when >1 major concern
    - Never truncate — if it ends in `...`, rewrite it

- **Commit** — `git commit -m "message"` (pre-commit hooks will run automatically via `.pre-commit-config.yaml`)
  If pre-commit hooks fail: fix the issue, re-stage, create a NEW commit (never --amend).

- **Push** — `git push` (with `-u origin <branch>` if no upstream set)

- **Create PR** — if the current branch is not `main`:
  ```bash
  gh pr create --title "<commit subject line>" --body "<body>"
  ```
    - Title: reuse the commit subject line
    - Body: `## Summary` with 1-3 bullets, `## Test plan` with checklist, Claude Code footer
    - If a PR already exists for this branch, skip silently
    - Report the PR URL at the end

## Rules

- **All pending changes ship together** — never unstage, cherry-pick, or exclude files. Everything goes into one commit. Do not ask whether to include specific files.
- **Fully autonomous** — no user prompts during execution
- **Stop on failure** — PII fail, lint fail, or test fail halts the pipeline
- **Single commit per push** — squash local commits when `ahead > 1`
- **Do NOT auto-commit or push again** after completing these steps — one-time action
- **`--dry-run` stops after step 1** — quality check only, no side effects
- **UV only** — all Python execution via `uv run` per H-05. Never `python` or `pytest` directly.

## Troubleshooting

- **PII scan finds home directory paths** — replace with relative paths or env-var substitution
- **Pre-commit hook fails** — fix the issue, re-stage, create NEW commit (never --amend)
- **ruff format changes files** — expected; changes are included in the commit
- **Tests pass locally but pre-commit pytest fails** — pre-commit runs pytest too; check for test isolation issues

## User Input

$ARGUMENTS
