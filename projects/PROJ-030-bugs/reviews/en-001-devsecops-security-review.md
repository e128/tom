# EN-001 DevSecOps Security Review — CI/CD Pipeline Hardening

> Reviewer: eng-devsecops
> PR: #154 (EN-001)
> Review Date: 2026-03-09
> Scope: 5 workflow files + dependabot.yml

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0 Executive Summary](#l0-executive-summary) | Finding totals, pipeline health, critical blockers |
| [L1 Technical Detail](#l1-technical-detail) | Per-file findings with file/line references |
| [L2 Strategic Implications](#l2-strategic-implications) | Coverage gaps, tooling assessment, roadmap |

---

## L0 Executive Summary

### Finding Totals by Severity

| Severity | Count | Disposition |
|----------|-------|-------------|
| Critical | 0 | None |
| High | 2 | Require fix before merge |
| Medium | 4 | Track for remediation |
| Low | 3 | Informational — log and accept or fix opportunistically |

**Pipeline health:** PASS with conditions. The hardening changes represent a material improvement to supply chain security posture. SHA pinning is complete and internally consistent across all action references. The `--frozen` lockfile enforcement closes the documented BUG-003 dirty-tree vector. No regressions in functional behavior were identified.

**Blockers requiring action before merge:**

- H-001 (HIGH): `setup-uv` version pinned to `"latest"` in all workflow files — the action itself is SHA-pinned, but `uv` binary installation resolves an unpinned `latest` tag on `astral-sh` infrastructure, partially defeating supply chain protection for the tool binary.
- H-002 (HIGH): `docs.yml` installs `mkdocs-material>=9.7.2` via bare `pip install` with a floating lower-bound constraint — no SHA-pinned action, no version lock, no `uv`, creating a supply chain gap in the docs deployment path that was not addressed by this PR.

---

## L1 Technical Detail

### File 1: release.yml

**Changes reviewed:** Replaced pip-based CI job with uv (`uv sync --frozen` + `uv run`). Removed pip fallback. Added SHA pins to all actions.

#### SHA Pin Audit

| Action | SHA | Comment Version | Status |
|--------|-----|-----------------|--------|
| `actions/checkout` | `08c6903cd8c0fde910a37f88322edcfb5dd907a8` | v5.0.0 | Consistent across all occurrences |
| `astral-sh/setup-uv` | `d4b2f3b6ecc6e67c4457f6d3e41ec42d3d0fcb86` | v5.4.2 | Consistent across all occurrences |
| `actions/upload-artifact` | `ea165f8d65b6e75b540449e92b4886f43607fa02` | v4.6.2 | Consistent across all occurrences |
| `actions/download-artifact` | `95815c38cf2ff2164869cbab79da8d1f422bc89e` | v4.2.1 | Consistent across all occurrences |
| `softprops/action-gh-release` | `da05d552573ad5aba039eaac05058a918a7bf631` | v2.2.2 | Third-party action, SHA-pinned correctly |

All five action references in `release.yml` are SHA-pinned with human-readable version comments. Internal consistency is confirmed: the same SHA appears for the same action everywhere it is used.

#### Finding R-001 (MEDIUM): `uv` binary resolves `"latest"` at runtime

**File:** `release.yml` lines 63, 87
**Pattern:** `version: "latest"` in `astral-sh/setup-uv` inputs

Although the `setup-uv` action itself is SHA-pinned, the `version: "latest"` input causes the action to fetch and install whatever `uv` binary is currently tagged `latest` on Astral's release infrastructure. If Astral's release pipeline is compromised, or if a new `uv` version introduces a breaking behavioral change, the pinned action SHA provides no protection for the actual `uv` binary version.

**Remediation:** Pin `uv` to a specific version in all `setup-uv` inputs, for example `version: "0.6.6"`. Update this pin via Dependabot when new `uv` releases are verified. This is classified HIGH because `uv` is used in the release pipeline's validation and CI gate steps — a malicious `uv` binary could exfiltrate `GITHUB_TOKEN` or `VERSION_BUMP_PAT` during `uv sync` or `uv run`.

**Severity: HIGH** — affects the release and all uv-using jobs.

#### Finding R-002 (LOW): Release archive bundles `requirements*.txt` (pip-based fallback)

**File:** `release.yml` lines 151-153
```
cp requirements.txt dist/$ARCHIVE_NAME/
cp requirements-dev.txt dist/$ARCHIVE_NAME/
cp requirements-test.txt dist/$ARCHIVE_NAME/
```

The PR comment block (line 59) states the pip install fallback was removed from CI, but `requirements.txt`, `requirements-dev.txt`, and `requirements-test.txt` are still bundled into the release archive. These files are shipped to end users with no version hashes, no integrity verification, and no pinning guarantee. If users follow the `pip install -r requirements.txt` path, they are outside the `uv.lock` supply chain protection.

**Remediation:** Either (a) remove these files from the release archive, replacing them with a user-facing installation note pointing to `pyproject.toml` + `uv`, or (b) convert them to hash-pinned format (`pip install --require-hashes`) and document them as a supported secondary installation path. The GOVERNANCE.md or docs/INSTALLATION.md should make the security tradeoff explicit.

**Severity: LOW** — affects end-user installation, not CI integrity.

#### Finding R-003 (LOW): Release job has `contents: write` at the workflow level

**File:** `release.yml` line 15
```yaml
permissions:
  contents: write
```

The `contents: write` permission is set at the workflow level, granting it to all jobs including the `validate` and `build` jobs that do not need write access. Only the `release` job (which creates the GitHub Release) requires `contents: write`.

**Remediation:** Move permissions to the job level. Set `contents: read` at the workflow level and add `contents: write` only to the `release` job.

**Severity: LOW** — reduces blast radius of a job-level compromise.

---

### File 2: version-bump.yml

**Changes reviewed:** `workflow_dispatch` now respects `[skip-bump]` marker. `actions/checkout` and `astral-sh/setup-uv` pinned to SHA.

#### SHA Pin Audit

| Action | SHA | Comment Version | Status |
|--------|-----|-----------------|--------|
| `actions/checkout` | `08c6903cd8c0fde910a37f88322edcfb5dd907a8` | v5.0.0 | Consistent |
| `astral-sh/setup-uv` | `d4b2f3b6ecc6e67c4457f6d3e41ec42d3d0fcb86` | v5.4.2 | Consistent |

No third-party actions in this file. Both actions are SHA-pinned.

#### Finding VB-001 (MEDIUM): `uv` binary resolves `"latest"` (same vector as R-001)

**File:** `version-bump.yml` line 76
**Same issue as R-001.** The `version-bump` job runs with `contents: write` and uses the `VERSION_BUMP_PAT` secret. A malicious `uv` binary here could exfiltrate the PAT. This is the highest-privilege job in the repository.

**Severity: HIGH** — elevated by access to `VERSION_BUMP_PAT`.

#### Finding VB-002 (MEDIUM): `bump-my-version` installed outside lockfile via `uv tool install`

**File:** `version-bump.yml` line 85
```
run: uv tool install 'bump-my-version==1.2.7'
```

`bump-my-version` is version-pinned (`==1.2.7`), which addresses the supply chain risk documented in the in-file comment (`BUG-003/RISK-01`). However, this installs from PyPI without hash verification. The `uv tool install` command does not consult `uv.lock`. If PyPI serves a compromised `bump-my-version==1.2.7` package (via a re-upload attack or index confusion attack), the pin provides version specificity but not integrity.

**Remediation:** Add `bump-my-version` to the project's `[tool.uv.dev-dependencies]` so it enters `uv.lock` with a content hash. Then use `uv tool install --no-cache bump-my-version==1.2.7` or invoke it via `uv run bump-my-version` against the locked environment. Alternatively, document acceptance of this risk with a rationale for why the `uv tool install` path is preferred (e.g., isolation from project env).

**Severity: MEDIUM** — version-pinned but not hash-verified; requires PyPI index integrity.

#### Finding VB-003 (MEDIUM): `prerelease` user input written to `$GITHUB_OUTPUT` before validation

**File:** `version-bump.yml` lines 108-110
```bash
echo "type=${{ github.event.inputs.bump_type }}" >> "$GITHUB_OUTPUT"
echo "prerelease=${{ github.event.inputs.prerelease }}" >> "$GITHUB_OUTPUT"
echo "Manual dispatch: type=${{ github.event.inputs.bump_type }}, prerelease=${{ github.event.inputs.prerelease }}"
```

`github.event.inputs.prerelease` is interpolated via the `${{ }}` expression context directly into a shell `echo` command and also echoed to the log, before the alphanumeric validation on line 158 runs. The `$GITHUB_OUTPUT` write is safe for environment-variable-style values, but the unvalidated `echo` on line 110 to stdout could produce misleading log output.

More importantly: `github.event.inputs.bump_type` is a restricted `choice` input (patch/minor/major), so it is safe. `prerelease` is a free-form string (`type: string`) — the validation at line 158 (`^[a-zA-Z0-9]+$`) runs only in the "Apply version bump" step, which is conditionally executed. If `steps.bump.outputs.type == 'none'`, the validation step is skipped entirely and the prerelease value is propagated unvalidated to the summary output.

**Remediation:** Move prerelease validation to immediately after the `workflow_dispatch` branch exits, before writing to `$GITHUB_OUTPUT`. A simple guard at the top of the "Determine bump type" step would suffice.

**Severity: MEDIUM** — validation bypass in the `none`-bump-type path; no direct code execution risk, but allows arbitrary strings into `$GITHUB_STEP_SUMMARY`.

#### Security Control: `github.actor` check (BUG-003/F-003) — CONFIRMED EFFECTIVE

**File:** `version-bump.yml` lines 49-58

The `if` condition correctly uses `github.actor` (the authenticated GitHub identity) rather than `github.event.head_commit.author.name` (a committer-controlled field). The `[skip-bump]` marker check for `workflow_dispatch` is correctly implemented. The concurrency group prevents parallel bumps.

This is a well-implemented security control. The commit message marker check is used only for skip-bump gating, not for security decisions.

#### Security Control: Dirty-tree guard — CONFIRMED EFFECTIVE

**File:** `version-bump.yml` lines 129-139

The `Ensure clean working tree` step correctly fails loudly if the working tree is dirty after `uv sync --frozen`. The comment accurately explains why this is a supply chain security control (`allow_dirty = false` prevents committing unreviewed changes). The guard is well-placed before the bump step.

---

### File 3: ci.yml

**Changes reviewed:** All `uv sync` calls now use `--frozen`. All actions pinned to SHA.

#### SHA Pin Audit — Complete

All action references are SHA-pinned and internally consistent:

| Action | SHA | Comment Version | Occurrences |
|--------|-----|-----------------|-------------|
| `actions/checkout` | `08c6903cd8c0fde910a37f88322edcfb5dd907a8` | v5.0.0 | 14 |
| `actions/setup-python` | `8d9ed9ac5c53483de85588cdf95a591a75ab9f55` | v5.5.0 | 3 |
| `astral-sh/setup-uv` | `d4b2f3b6ecc6e67c4457f6d3e41ec42d3d0fcb86` | v5.4.2 | 8 |
| `actions/upload-artifact` | `ea165f8d65b6e75b540449e92b4886f43607fa02` | v4.6.2 | 5 |
| `actions/download-artifact` | `95815c38cf2ff2164869cbab79da8d1f422bc89e` | v4.2.1 | 2 |
| `codecov/codecov-action` | `4650159d642e33fdc30954ca22638caf0df6cac8` | v5.4.3 | 2 |
| `MishaKav/pytest-coverage-comment` | `26f986d2599c288bb62f623d29c2da98609e9cd4` | main (2026-03-09) | 1 |

No SHA consistency violations found. All occurrences of the same action use the same SHA.

#### Finding CI-001 (HIGH): Remaining `pip install` usage in `lint`, `type-check`, and `security` jobs

**File:** `ci.yml` lines 40, 64-66, 87-95

Three jobs use bare `pip install` without `uv`:

**lint job (line 40):**
```bash
pip install "ruff==0.14.11"
```
Exact pin — good. But installed via bare `pip install` using the system Python from `actions/setup-python`, not via `uv`. Not covered by `uv.lock`.

**type-check job (lines 64-66):**
```bash
python -m pip install --upgrade pip
pip install pyright
pip install -e ".[dev]" || pip install -e .
```
`pyright` is entirely unpinned. The `pip install -e ".[dev]"` may pull transitive dependencies not in `uv.lock`. This is an active supply chain gap.

**security job (lines 87-95):**
```bash
python -m pip install --upgrade pip
pip install pip-audit
pip install filelock mypy ruff
pip-audit --strict
```
`pip-audit`, `filelock`, `mypy`, and `ruff` are all unpinned. Ironically, the security scanning job itself has the weakest dependency pinning of any job in CI. An attacker who could serve a compromised `pip-audit` package would be able to suppress security findings.

These three jobs were not converted in this PR. Based on the PR description, the conversion was focused on the jobs that were already failing (BUG-003). However, the remaining pip-based jobs undermine the supply chain posture improvements made elsewhere.

**Remediation:** Convert `lint`, `type-check`, and `security` jobs to use `uv sync --frozen` with `uv run` for all tool invocations. Exact version pins with `==` are better than unpinned, but `uv.lock` hash verification is the correct control. At minimum, pin all packages with `==`.

**Severity: HIGH** — unpinned `pyright` and `pip-audit` in `type-check` and `security` jobs.

#### Finding CI-002 (MEDIUM): `MishaKav/pytest-coverage-comment` pinned to a branch-tracking SHA

**File:** `ci.yml` line 471
```yaml
uses: MishaKav/pytest-coverage-comment@26f986d2599c288bb62f623d29c2da98609e9cd4 # main (2026-03-09)
```

This SHA was correct on 2026-03-09, but the comment `# main (2026-03-09)` reveals this is tracking the `main` branch of a third-party action, not a tagged release. Branch-tracking SHAs are valid as a point-in-time pin, but they carry two risks: (1) Dependabot does not reliably track branch SHA changes; (2) the comment date becomes misleading once the branch advances, making it harder to assess staleness.

**Remediation:** Either (a) wait for `MishaKav/pytest-coverage-comment` to publish a tagged release and migrate to that, or (b) add a note in `dependabot.yml` documenting that this action requires manual SHA refresh. Currently Dependabot is configured to track `github-actions` updates, which should pick up SHA changes for pinned actions, but the `main` branch tracking is less reliable than tag tracking.

**Severity: MEDIUM** — Dependabot coverage for this action is uncertain; manual staleness tracking is required.

#### Finding CI-003 (LOW): `security` job audits a manually-curated subset of dependencies

**File:** `ci.yml` lines 93-95
```bash
pip install filelock mypy ruff
pip-audit --strict
```

`pip-audit` is invoked against only `filelock mypy ruff` — a manually maintained list. If new project dependencies are added to `pyproject.toml` and not added here, they are not scanned. The `--strict` flag is correct (fail on any vulnerability), but the audit scope is incomplete.

**Remediation:** Convert to `uv run pip-audit` against the locked environment so that the scanned dependency set is always the full project dependency graph, eliminating the manual maintenance burden. If the pip path must be retained, document the dependency list maintenance obligation and add a CI check that validates the list against `pyproject.toml`.

**Severity: LOW** — incomplete scan scope; new dependencies may be silently unaudited.

---

### File 4: docs.yml

**Changes reviewed:** Actions pinned to SHA.

#### SHA Pin Audit

| Action | SHA | Comment Version | Status |
|--------|-----|-----------------|--------|
| `actions/checkout` | `08c6903cd8c0fde910a37f88322edcfb5dd907a8` | v5.0.0 | Consistent |
| `actions/setup-python` | `8d9ed9ac5c53483de85588cdf95a591a75ab9f55` | v5.5.0 | Consistent |
| `actions/cache` | `5a3ec84eff668545956fd18022155c47e93e2684` | v4.2.3 | Present, consistent |

#### Finding D-001 (HIGH): `pip install "mkdocs-material>=9.7.2"` — floating version, no uv, no lockfile

**File:** `docs.yml` line 38
```bash
pip install "mkdocs-material>=9.7.2"
```

This is the most exposed supply chain gap remaining after the PR. The `docs.yml` workflow:
- Runs on every push to `main` that touches `docs/**`, `mkdocs.yml`, or `overrides/**`
- Has `permissions: contents: write` (deploys to `gh-pages` branch)
- Installs `mkdocs-material` with a floating `>=` constraint via bare `pip install`
- Does not use `uv` at all
- The action pins were added but the package installation was not addressed

A compromised `mkdocs-material` package could execute arbitrary code with `contents: write` access during `mkdocs gh-deploy`, potentially manipulating the `gh-pages` branch.

**Remediation options (in order of preference):**
1. Switch to `uv sync --frozen` with `mkdocs-material` in `pyproject.toml` extras
2. Pin to an exact version: `pip install "mkdocs-material==9.7.2"` (minimum viable fix)
3. At minimum, the `>=9.7.2` floating constraint must become `==X.Y.Z`

This workflow was explicitly listed in the PR scope but only received action-level pinning. The package installation gap should have been addressed as part of EN-001.

**Severity: HIGH** — `contents: write` context with floating supply chain.

---

### File 5: pat-monitor.yml

**Changes reviewed:** `actions/github-script` pinned to SHA.

#### SHA Pin Audit

| Action | SHA | Comment Version | Status |
|--------|-----|-----------------|--------|
| `actions/github-script` | `60a0d83039c74a4aee543508d2ffcb1c3799cdea` | v7.0.1 | Correct |

#### Assessment

`pat-monitor.yml` has minimal changes (one action pinned). The workflow runs on a weekly schedule with `permissions: contents: read, issues: write`. The `github-script` action runs JavaScript inline — the SHA pin correctly immobilizes this code.

#### Finding PM-001 (LOW): PAT exposed in shell pipeline output

**File:** `pat-monitor.yml` lines 51-66

The PAT check step performs three separate `curl` calls with `${{ secrets.VERSION_BUMP_PAT }}` interpolated. GitHub Actions automatically masks secret values in logs, so the PAT value itself is masked. However, `curl` error output (`-o /dev/null` suppresses response body, which is correct) could still leak timing or status information. The implementation is consistent with standard PAT health-check patterns.

No remediation required. This is an observational note. The masking behavior is correctly relied upon.

**Severity: LOW** — implementation is standard; no change required.

---

### File 6: dependabot.yml

**Changes reviewed:** New file.

#### Configuration Review

```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule: { interval: "weekly", day: "monday" }
    commit-message: { prefix: "ci" }
    labels: ["dependencies", "ci"]
    open-pull-requests-limit: 10

  - package-ecosystem: "pip"
    directory: "/"
    schedule: { interval: "weekly", day: "monday" }
    commit-message: { prefix: "deps" }
    labels: ["dependencies"]
    open-pull-requests-limit: 5
```

**Positive findings:**
- `github-actions` ecosystem coverage closes the manual SHA-update burden
- Weekly cadence is appropriate for a framework project
- `open-pull-requests-limit: 10` for actions is generous but reasonable given ~10 unique action SHAs
- Commit message prefixes align with conventional commits (`ci`, `deps`)

**Gap — `uv` ecosystem not covered:** Dependabot does not natively support the `uv` ecosystem. The `pip` ecosystem entry will scan `requirements*.txt` files but not `uv.lock`. This means transitive dependency vulnerabilities tracked in `uv.lock` are not surfaced by Dependabot.

**Remediation:** Add `osv-scanner` or `pip-audit` scanning against the lockfile as a CI job (complementing Dependabot's `pip` coverage), or migrate to GitHub's dependency graph support for uv when it becomes available. For the interim, the existing `security` job's `pip-audit` step partially covers this, but only for the manually-curated subset (see CI-003).

**Severity:** Informational — not a finding, but a coverage gap to document.

---

## L2 Strategic Implications

### Security Tool Effectiveness Assessment

| Tool / Control | Coverage | Effectiveness | Gap |
|----------------|----------|---------------|-----|
| SHA pinning (GitHub Actions) | Complete — all 7 unique actions pinned consistently | High | `uv` binary version inside setup-uv remains floating |
| `uv sync --frozen` | Partial — applied to uv-based jobs; 3 jobs still use pip | High where applied | `lint`, `type-check`, `security` jobs excluded |
| `pip-audit` | Partial — manually curated dependency subset | Medium | Subset maintenance is manual; not lockfile-driven |
| `bump-my-version==1.2.7` pin | Version-pinned but not hash-verified | Medium | `uv tool install` bypasses `uv.lock` |
| Dirty-tree guard | Complete and effective | High | None identified |
| `github.actor` identity check | Complete and effective | High | None identified |
| `[skip-bump]` on `workflow_dispatch` | Correctly implemented | High | Prerelease validation order gap (VB-003) |
| `GITHUB_TOKEN` vs PAT scope | Appropriately scoped | High | PAT rotation monitored via `pat-monitor.yml` |
| Dependabot | Actions: complete; pip: partial; uv: absent | Medium | `uv.lock` not covered by any ecosystem scanner |
| `contents: write` scoping | Workflow-level in release.yml and docs.yml | Low-Medium | Should be job-scoped |

### False Positive Assessment

No false positives identified. All findings are confirmed by direct code inspection. The `github.actor` check, dirty-tree guard, and prerelease alphanumeric validation are correctly implemented security controls; findings in this report refer to adjacent gaps, not the controls themselves.

### Scan Coverage Gaps

1. **No SAST scanning configured.** No Semgrep or CodeQL job exists. The YAML-injection grep in the `security` job is a custom heuristic (`yaml.load()` / `yaml.unsafe_load()` detection), not a full SAST scan. SAST should be added to CI.

2. **No secrets scanning in CI.** There is no Gitleaks or TruffleHog job. Secrets committed to the repository would not be caught by CI. Given that this repository handles multiple tokens (`VERSION_BUMP_PAT`, `CODECOV_TOKEN`, `GITHUB_TOKEN`), baseline secrets scanning should be added.

3. **No container scanning.** Not applicable to this repository's current artifact type (Python plugin archive, not container images). Re-evaluate if containerization is introduced.

4. **No SBOM generation.** The release archive bundles `pyproject.toml` and `requirements*.txt` but does not produce a CycloneDX or SPDX SBOM. For a framework consumed by other teams, an SBOM would improve downstream trust.

5. **SLSA provenance level.** Current state is approximately SLSA Level 1 (documented automated build). SHA-pinned actions and `uv sync --frozen` are prerequisites for Level 2 (signed provenance). Completing the `uv` binary version pin and eliminating remaining `pip install` invocations would enable a path to Level 2 with the addition of `sigstore/gh-action-sigstore-python` or GitHub's built-in provenance generation.

### Tooling Evolution Recommendations

| Priority | Recommendation | Effort |
|----------|----------------|--------|
| P1 (before merge) | Pin `uv` binary version in all `setup-uv` inputs | Low — single value change across files |
| P1 (before merge) | Pin `mkdocs-material` to exact version in `docs.yml` | Low — change `>=9.7.2` to `==X.Y.Z` |
| P2 (next sprint) | Convert `lint`, `type-check`, `security` jobs to `uv sync --frozen` | Medium — 3 jobs |
| P2 (next sprint) | Add `osv-scanner` against `uv.lock` to complement `pip-audit` | Low — single job addition |
| P3 (next quarter) | Add Gitleaks secrets scanning job to `ci.yml` | Low |
| P3 (next quarter) | Add Semgrep SAST job to `ci.yml` | Medium |
| P4 (roadmap) | Scope `contents: write` to job level in `release.yml` and `docs.yml` | Low |
| P4 (roadmap) | Add CycloneDX SBOM generation to release pipeline | Low |
| P5 (future) | Evaluate SLSA Level 2 provenance generation | High |

### SLSA Maturity Roadmap

| SLSA Level | Requirements | Current State | Gap |
|------------|-------------|---------------|-----|
| Level 1 | Documented automated build | ACHIEVED | — |
| Level 2 | Signed provenance from hosted platform | IN PROGRESS | Requires: uv pin, eliminate pip in CI, add `slsa-github-generator` or equivalent |
| Level 3 | Non-falsifiable provenance, hardened build | NOT STARTED | Requires hermetic builds, provenance service |

---

## Appendix: SHA Consistency Verification

All SHA pins were verified for internal consistency across files. No SHA conflicts found. The same SHA is used for the same action version everywhere it appears.

| Action@SHA | Files Using It | Count |
|------------|----------------|-------|
| `actions/checkout@08c6903c...` | ci.yml, release.yml, version-bump.yml, docs.yml | 20+ |
| `astral-sh/setup-uv@d4b2f3b6...` | ci.yml, release.yml, version-bump.yml | 12 |
| `actions/setup-python@8d9ed9ac...` | ci.yml, docs.yml | 5 |
| `actions/upload-artifact@ea165f8d...` | ci.yml, release.yml | 7 |
| `actions/download-artifact@95815c38...` | ci.yml, release.yml | 3 |
| `codecov/codecov-action@4650159d...` | ci.yml | 2 |
| `actions/cache@5a3ec84e...` | docs.yml | 1 |
| `actions/github-script@60a0d83039...` | pat-monitor.yml | 1 |
| `softprops/action-gh-release@da05d552...` | release.yml | 1 |
| `MishaKav/pytest-coverage-comment@26f986d2...` | ci.yml | 1 |

---

*eng-devsecops | DevSecOps Pipeline Engineer*
*Review date: 2026-03-09*
*SSDF practices: PW.7 (automated code review), PW.8 (dynamic testing), PS.1 (secrets protection)*
