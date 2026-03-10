# BUG-003 DevSecOps Security Review: version-bump.yml Pipeline

**Scope:** `.github/workflows/version-bump.yml` (BUG-003 fix), `scripts/create-catchup-tags.sh`, `release.yml`
**Reviewer:** eng-devsecops
**Date:** 2026-03-09
**Standard alignment:** NIST SSDF (PS.1, PW.7), Google SLSA, OWASP CI/CD Security

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0 Executive Summary](#l0-executive-summary) | Severity totals and critical blockers |
| [L1 Technical Findings](#l1-technical-findings) | Per-finding detail with evidence and remediation |
| [L2 Strategic Implications](#l2-strategic-implications) | Tooling gaps, posture assessment, SLSA mapping |

---

## L0 Executive Summary

| Severity | Count | Pipeline Status |
|----------|-------|----------------|
| CRITICAL | 0 | -- |
| HIGH | 2 | Deployment BLOCKED pending remediation |
| MEDIUM | 3 | Track for remediation |
| LOW | 1 | Monitor |
| INFO | 2 | Awareness only |

**Critical blockers:** None that prevent the immediate BUG-003 merge. However, two HIGH findings
must be remediated before the pipeline is considered production-secure: the `release.yml` policy
drift from `uv sync` back to bare `pip install`, and the unsigned catch-up tags creating an
unverifiable provenance gap in the tag history.

**Primary finding:** `--frozen` is the correct fix and improves security posture. The `allow_dirty
= false` supply chain control is fully preserved. The "Ensure clean working tree" reset step
introduces a low-severity masking risk that is adequately mitigated by the diagnostic `git diff
--name-only` log preceding the reset.

---

## L1 Technical Findings

---

### F-001 -- HIGH: `release.yml` Reverts to Bare `pip install`, Undoing the BUG-003 Fix

**File:** `.github/workflows/release.yml`, lines 61-63, 80-84
**Severity:** HIGH
**SSDF Practice:** PW.7 (code review), PS.1 (protect code from unauthorized access)

**Evidence:**

```yaml
# release.yml line 61 -- validate job
- name: Validate version sync across all files
  run: |
    pip install uv 2>/dev/null || true
    uv sync 2>/dev/null || pip install -e .     # <-- falls back to pip, no --frozen
    python scripts/sync_versions.py --check

# release.yml lines 80-84 -- ci job
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install "ruff==0.14.11" pyright
    pip install -e ".[dev,test]"                # <-- bare pip, not uv at all
```

**Risk:** The `version-bump.yml` fix correctly uses `uv sync --frozen`. However `release.yml`
bypasses both `uv` and `--frozen` for its CI and validation jobs. This means release artifacts
are built and tested against a dependency set that was not resolved from the committed `uv.lock`.
A supply chain substitution in a transitive dependency would not be detected by the lockfile
consistency check. Additionally, `pip install -e ".[dev,test]"` is a direct violation of H-05
(UV-only Python environment).

**Remediation:** Update `release.yml` to use `uv sync --frozen` throughout, consistent with the
BUG-003 fix pattern. Replace the fallback `pip install -e .` chain with a hard failure if uv
is unavailable, or install uv via `astral-sh/setup-uv@v5` as version-bump.yml does.

```yaml
# Replacement for release.yml validate job
- name: Install uv
  uses: astral-sh/setup-uv@v5
- name: Validate version sync across all files
  run: |
    uv sync --frozen
    uv run python scripts/sync_versions.py --check

# Replacement for release.yml ci job
- name: Install uv
  uses: astral-sh/setup-uv@v5
- name: Install dependencies
  run: uv sync --frozen
- name: Run lint
  run: uv run ruff check . --config=pyproject.toml
```

---

### F-002 -- HIGH: Catch-Up Tags Are Unsigned -- 36-Version Provenance Gap

**File:** `scripts/create-catchup-tags.sh`
**Severity:** HIGH
**SSDF Practice:** PS.1 (protect code integrity); SLSA Level 2 (signed provenance)

**Evidence:**

```bash
# Line 63 -- annotated but not GPG-signed
git tag -a "$tag" "$hash" -m "Release $tag (catch-up tag created by BUG-003)"

# Push -- no signature verification
git push origin --tags
```

**Risk:** Annotated tags confirm object type and message but provide zero cryptographic guarantee
that the tag was created by an authorized actor. Anyone with repository write access (or any
process holding the `VERSION_BUMP_PAT`) could create identically-formatted tags pointing to
arbitrary commits. The 36 catch-up tags spanning v0.2.3 through v0.24.0 cover the entire
meaningful version history of the project. Consumers who verify release integrity via tag
signatures will find none, and consumers who do not verify will silently accept whatever a
malicious actor substituted.

The problem is compounded by `release.yml` triggering on `v*` tag push: pushing all 36 tags
simultaneously will fire 36 concurrent release jobs, each building and publishing a release
artifact. The script's own comment acknowledges this ("Consider disabling the release workflow
first") but does not enforce the precaution.

**Remediation:**

1. Before executing `--push`, disable `release.yml` via branch protection or `gh workflow disable`.
2. After tag creation, GPG-sign retroactively if the project has an established signing key:
   `git tag -s -f "$tag" "$hash" -m "Release $tag"`. This requires the signing key to have been
   established prior to these versions to be meaningful. If no key existed, document the
   provenance gap explicitly in each release's GitHub Release body.
3. Evaluate adopting Sigstore/cosign for future tag signing, which does not require pre-distributing
   a GPG key and integrates with GitHub Actions OIDC.
4. Add explicit enforcement to the script:

```bash
if [[ "$MODE" == "--push" ]]; then
  echo "WARNING: This will trigger release.yml for ${#MISSING_TAGS[@]} tags."
  echo "Disable release.yml before proceeding. Continue? (yes/NO)"
  read -r confirm
  [[ "$confirm" == "yes" ]] || { echo "Aborted."; exit 1; }
fi
```

---

### F-003 -- MEDIUM: Skip-Bump Detection Is Bypassable via Commit Author Spoofing

**File:** `.github/workflows/version-bump.yml`, lines 44-49
**Severity:** MEDIUM

**Evidence:**

```yaml
if: >-
  github.event_name == 'workflow_dispatch' ||
  (
    !contains(github.event.head_commit.message, '[skip-bump]') &&
    github.event.head_commit.author.name != 'github-actions[bot]'
  )
```

**Risk:** The author name check (`github.event.head_commit.author.name != 'github-actions[bot]'`)
is a string comparison against the commit author name field, which is fully controlled by the
committer at `git commit` time. Any human or automated process can set `user.name =
"github-actions[bot]"` in their git config and push a commit that the skip guard will then
silently swallow, preventing a legitimate version bump from running. This is not directly
exploitable for privilege escalation, but it is an availability attack surface: a contributor
(or a compromised PR that gets merged) can permanently suppress version bumping for any commit
with a spoofed author name.

The `[skip-bump]` commit message marker has the same spoofability property, but that is the
intended design and acceptable since it is a functional opt-out, not a security boundary.

**Remediation:** Replace the author name string check with the cryptographically-verified actor
identity provided by GitHub Actions:

```yaml
if: >-
  github.event_name == 'workflow_dispatch' ||
  (
    !contains(github.event.head_commit.message, '[skip-bump]') &&
    github.actor != 'github-actions[bot]'
  )
```

`github.actor` is set by GitHub from the authenticated token, not from git metadata, and cannot
be spoofed by a commit author. This also correctly handles the case where the bot pushes via
the PAT (the actor will still be the bot's identity).

---

### F-004 -- MEDIUM: `workflow_dispatch` Bypasses All Skip Guards, Enabling Manual Bump Loops

**File:** `.github/workflows/version-bump.yml`, lines 44-45
**Severity:** MEDIUM

**Evidence:**

```yaml
if: >-
  github.event_name == 'workflow_dispatch' ||   # short-circuits: no skip check applied
  (
    !contains(github.event.head_commit.message, '[skip-bump]') &&
    ...
  )
```

**Risk:** A `workflow_dispatch` trigger bypasses both the `[skip-bump]` marker check and the
bot-author check entirely. This means any user with repository Actions write permission can
manually trigger a version bump on a commit that was explicitly marked `[skip-bump]` or that
was itself the output of a prior bump job. In a scenario where a bump commit is pushed and
immediately followed by a manual dispatch, the result would be a double-bump on the same HEAD.

**Remediation:** Add a minimum check for `[skip-bump]` in the commit message even on manual
dispatch, or add a confirmation gate that requires the dispatcher to explicitly confirm they
intend to bump an already-bumped commit:

```yaml
if: >-
  (
    github.event_name == 'workflow_dispatch' &&
    !contains(github.event.head_commit.message, '[skip-bump]')
  ) ||
  (
    github.event_name == 'push' &&
    !contains(github.event.head_commit.message, '[skip-bump]') &&
    github.actor != 'github-actions[bot]'
  )
```

---

### F-005 -- MEDIUM: `git checkout -- .` Reset Could Mask a Legitimate Dependency Drift

**File:** `.github/workflows/version-bump.yml`, lines 111-118
**Severity:** MEDIUM

**Evidence:**

```yaml
- name: Ensure clean working tree
  if: steps.bump.outputs.type != 'none'
  run: |
    if [[ -n "$(git status --porcelain)" ]]; then
      echo "::warning::Working tree dirty before bump — resetting tracked changes"
      git diff --name-only       # diagnostic log
      git checkout -- .          # hard reset of all tracked changes
    fi
```

**Risk:** The step is designed as a belt-and-suspenders guard for the BUG-003 scenario where
`uv sync --frozen` leaves residue. With `--frozen` correctly applied, the step should never
trigger in practice. However, if it does trigger, it silently destroys any tracked changes
that arrived in the working tree by a mechanism other than `uv sync`: a failed patch application,
a corrupt cache restore, a misbehaving generator script earlier in the job. The `::warning`
annotation and `git diff --name-only` output provide post-hoc diagnostic visibility in the
Actions log, but the pipeline does not fail -- it continues to create and push a version bump
commit from a potentially corrupt state.

**Assessment:** The diagnostic logging before the reset is adequate for the primary BUG-003
scenario (lock file residue from pre-frozen `uv sync`). The risk is real but bounded by
the fact that `--frozen` should prevent the trigger condition from occurring at all, making
this step dormant under normal operation.

**Remediation (preferred):** Fail fast rather than silently reset, to force human investigation:

```yaml
- name: Ensure clean working tree
  if: steps.bump.outputs.type != 'none'
  run: |
    if [[ -n "$(git status --porcelain)" ]]; then
      echo "::error::Working tree dirty before bump. Unexpected files modified:"
      git diff --name-only
      git status --porcelain
      echo "With --frozen in place this should not occur. Investigate before proceeding."
      exit 1
    fi
```

If the fail-fast approach is considered too disruptive, retain the current reset behavior but
add `::error` alongside `::warning` so that the event is surfaced in the Actions run summary
as a failure annotation rather than a warning, drawing attention even when the job succeeds.

---

### F-006 -- LOW: `astral-sh/setup-uv@v5` Uses Floating Minor Version Pin

**File:** `.github/workflows/version-bump.yml`, line 65
**Severity:** LOW

**Evidence:**

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v5     # major-version floating pin
```

**Risk:** `@v5` resolves to the latest `5.x.y` release of `setup-uv`. A malicious or accidental
breaking change pushed to the `v5` tag by astral-sh (or a compromised release of that action)
would be silently picked up. This is a common industry practice but violates SLSA Level 3
hermetic build requirements and the SSDF PS.1 principle of protecting the integrity of the
build toolchain.

**Remediation:** Pin to a specific commit SHA:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@f0ec1fc3b38f5e7cd731bb6ce7f79f87a50c2bbd  # v5.4.2
```

Use `dependabot` or `renovate` with `automerge: patch` to keep the pin current automatically
while maintaining integrity guarantees.

---

### F-007 -- INFO: `VERSION_BUMP_PAT` Scope Is Correct but Not Validated at Job Start

**File:** `.github/workflows/version-bump.yml`, line 59; `pat-monitor.yml`
**Severity:** INFO

**Evidence:** The `pat-monitor.yml` workflow validates the PAT weekly using an authenticated API
call and creates a GitHub Issue on failure. The PAT is described in the monitor as requiring
only `Contents: Read and write` with repository-scoped access. This is a minimal-privilege
configuration consistent with SSDF PS.1.

**Observation:** The monitor tests liveness (HTTP 200) but not permissions scope. A PAT that
authenticates successfully but lacks `Contents: write` will produce HTTP 200 from the
`/repos/{owner}/{repo}` endpoint but will fail at the `git push origin main --follow-tags`
step, not at the monitor stage. Consider adding a permission-scoped test (e.g., a test tag
creation and immediate deletion via the GitHub API) to the monitor to confirm write access
is intact.

The 90-day rotation schedule is appropriate. No additional action required for this finding.

---

### F-008 -- INFO: Pre-release Bump Path Uses Fragile `grep -oP` Version Extraction

**File:** `.github/workflows/version-bump.yml`, lines 136-138
**Severity:** INFO

**Evidence:**

```bash
if [[ -n "$PRERELEASE" ]]; then
  bump-my-version bump "$BUMP_TYPE" --no-tag
  bump-my-version bump pre_l --no-commit --no-tag \
    --new-version "$(grep -oP 'version = "\K[^"]+' pyproject.toml | head -1)-${PRERELEASE}.1"
fi
```

**Observation:** The pre-release path extracts the intermediate version via `grep -oP` from
`pyproject.toml` rather than from `bump-my-version`'s own output. If `pyproject.toml` has
multiple `version =` lines (it currently has one for the framework, but the bumpversion config
touches four files), the `head -1` guard is fragile. The stable bump path (line 140) uses
`bump-my-version bump "$BUMP_TYPE"` which handles version extraction internally and is
authoritative. The pre-release path should use `bump-my-version show current_version` after
the first bump to retrieve the post-bump version rather than parsing the TOML directly.

---

## L2 Strategic Implications

### Security Posture Assessment

The BUG-003 fix (`uv sync --frozen`) is correct and directionally improves security posture.
`--frozen` enforces that CI installs exactly the dependency graph committed in `uv.lock`,
preventing silent re-resolution that could introduce a different (potentially vulnerable or
tampered) dependency version. The `allow_dirty = false` gate in bump-my-version is fully
preserved -- `--frozen` eliminates the `uv.lock` modification that was causing the dirty-tree
failure, rather than bypassing the check.

The critical gap is that the fix is applied only to `version-bump.yml`. The `release.yml`
workflow -- which produces the actual release artifacts -- uses bare `pip install` and does
not benefit from the lockfile integrity guarantee. This creates an asymmetry where the version
coordination pipeline is locked but the artifact production pipeline is not.

### SLSA Maturity Mapping

| SLSA Requirement | Current State | Gap |
|-----------------|---------------|-----|
| L1: Documented build process | Met (workflow YAML is the definition) | None |
| L1: Artifacts available for inspection | Partial (checksums generated, not signed) | Sigstore/cosign not integrated |
| L2: Hosted build platform | Met (GitHub Actions, immutable runner) | None |
| L2: Signed provenance from platform | Not met | No SLSA provenance action used |
| L2: Dependencies from lockfile | Met in version-bump.yml only | release.yml gap (F-001) |
| L3: Hardened build platform | Not met | Ephemeral runners not self-hosted hardened |
| L3: Non-falsifiable attestations | Not met | No `slsa-github-generator` usage |

**Recommendation:** Add `slsa-github-generator` to `release.yml` to generate SLSA L2 provenance
attestations. This is a GitHub Actions-native addition requiring no external infrastructure.

### False Positive Assessment

The "Ensure clean working tree" step (F-005) will produce zero warnings in normal operation
after the `--frozen` fix. The `::warning` log annotation is therefore informational insurance
rather than a live signal. It should not be treated as noise in practice.

### Scan Coverage Gaps

The following categories have no automated coverage in the current pipeline:

| Category | Gap | Recommended Tool |
|----------|-----|-----------------|
| Secrets scanning | No Gitleaks or TruffleHog in CI | Add Gitleaks to `ci.yml` |
| SAST | No Semgrep or CodeQL | Enable CodeQL via GitHub default setup |
| Container scanning | No container images produced currently | Not applicable |
| IaC scanning | No Terraform/CloudFormation in scope | Not applicable |
| SBOM generation | Not generated at release time | Add Syft to `release.yml` |

The highest-value addition given current pipeline structure is CodeQL (free for public repos,
zero-config default setup covers Python) and Gitleaks (catches accidental PAT commits, directly
relevant given this project uses a PAT for push-through-protection).

### Tooling Evolution Recommendation

Priority order for pipeline security improvements:

1. Fix `release.yml` to use `uv sync --frozen` (F-001, HIGH, <1 hour effort)
2. Add `github.actor` check to replace author name check (F-003, MEDIUM, <30 minutes)
3. Pin `setup-uv` to a commit SHA and add Dependabot for action pins (F-006, LOW, <1 hour)
4. Enable CodeQL default setup in repository settings (zero config, immediate coverage)
5. Add Gitleaks as a CI step in `ci.yml` (secrets scanning gap)
6. Add `slsa-github-generator` to `release.yml` (SLSA L2 provenance)
7. Evaluate Sigstore/cosign for tag signing on future releases (F-002, ongoing)
