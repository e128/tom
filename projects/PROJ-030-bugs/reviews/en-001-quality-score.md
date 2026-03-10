# Quality Score Report: EN-001 CI Pipeline Security Hardening

## L0 Executive Summary

**Score:** 0.845/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness (0.82) / Evidence Quality (0.82)

**One-line assessment:** Tasks 1-5 are cleanly executed with strong SHA-pin uniformity and well-cited traceability, but residual pip invocations in `ci.yml` (lint, type-check, security jobs) and an unaddressed `docs.yml` pip install leave the H-05 compliance goal partially incomplete, holding the score below the 0.92 threshold.

---

## Scoring Context

- **Deliverable:** `projects/PROJ-030-bugs/work/EN-001-ci-pipeline-hardening.md` + 5 workflow files + `dependabot.yml`
- **Deliverable Type:** Infrastructure / CI configuration
- **Criticality Level:** C2 (Standard — reversible changes to CI workflows, AE-002 triggers C3 minimum for `.context/rules/` but these are `.github/workflows/`)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-09T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.845 |
| **Threshold** | 0.92 (H-13) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No — scored from deliverable files directly |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.82 | 0.164 | 4/5 ACs complete; task 6 explicitly deferred; `docs.yml` pip install unaddressed |
| Internal Consistency | 0.20 | 0.87 | 0.174 | SHA pins uniformly applied; `lint`/`type-check` jobs use pip without explanatory label |
| Methodological Rigor | 0.20 | 0.85 | 0.170 | Sound finding-to-fix linkage; Dependabot adds sustainability; no verification step documented |
| Evidence Quality | 0.15 | 0.82 | 0.123 | All SHAs present with version comments; one SHA references `main` branch not a release tag |
| Actionability | 0.15 | 0.84 | 0.126 | Changes work as intended for scoped findings; residual pip calls in CI jobs are unresolved supply chain risk |
| Traceability | 0.10 | 0.88 | 0.088 | Strong cross-references (F-IDs, GitHub issues, security review); `docs.yml` lacks finding-ID comment |
| **TOTAL** | **1.00** | | **0.845** | |

---

## Detailed Dimension Analysis

### Completeness (0.82/1.00)

**Evidence:**

The four completed acceptance criteria are verifiably addressed:

- AC1 (`uv sync --frozen` everywhere): All uv-using steps in `release.yml` (lines 70, 93, 183), `version-bump.yml` (lines 98, 183), and `ci.yml` (plugin-validation line 134, template-validation line 178, license-headers line 203, cli-integration line 227, version-sync line 500, hard-rule-ceiling line 525, test-uv line 390) use `--frozen`. Zero bare `uv sync` calls remain in uv-using steps.

- AC2 (SHA pins): Every `uses:` line across all 5 workflow files carries a commit SHA with a version comment. Actions covered: `actions/checkout`, `actions/setup-python`, `astral-sh/setup-uv`, `actions/upload-artifact`, `actions/download-artifact`, `codecov/codecov-action`, `softprops/action-gh-release`, `MishaKav/pytest-coverage-comment`, `actions/github-script`, `actions/cache`.

- AC3 (no pip fallback in `release.yml`): The `validate` and `ci` jobs both use `astral-sh/setup-uv` with inline comment "EN-001/F-001: Use uv directly (H-05 compliance). No pip fallback." No `pip install` calls exist in `release.yml`.

- AC4 (`workflow_dispatch` respects `[skip-bump]`): `version-bump.yml` lines 49-58 implement a compound conditional: `workflow_dispatch` events check `!contains(github.event.head_commit.message, '[skip-bump]')`; non-dispatch events additionally check `github.actor != 'github-actions[bot]'`.

- AC5 (script consolidation, issue #150): Explicitly unchecked in the work item. Task 6 status is PENDING. This is an intentional deferral, clearly documented.

**Gaps:**

1. `docs.yml` line 38: `run: pip install "mkdocs-material>=9.7.2"` — this is a floating version pip install. While RISK-03 targeted `actions/*` floating tags rather than `run:` pip installs, the `docs.yml` pip install was within scope of the H-05 compliance goal (no pip usage in workflows). The finding was "apply `uv sync --frozen` consistently" and `docs.yml` was not converted to use uv at all.

2. `ci.yml` `lint` job (lines 39-40): `run: pip install "ruff==0.14.11"` — uses pip directly. Version-pinned (good), but pip not uv. Not addressed by any EN-001 task explicitly, but the stated goal of H-05 compliance includes this job.

3. `ci.yml` `type-check` job (lines 63-66): `python -m pip install --upgrade pip`, `pip install pyright`, `pip install -e ".[dev]" || pip install -e .` — multiple unpinned pip calls. The fallback `|| pip install -e .` is a floating install.

4. `ci.yml` `security` job (lines 86-89): `python -m pip install --upgrade pip`, `pip install pip-audit`, `pip install filelock mypy ruff` — unpinned pip installs.

**Improvement Path:**

Either explicitly scope out `ci.yml` pip-only jobs (lint, type-check, security) and `docs.yml` from EN-001 with documented rationale (these are intentionally pip-based compatibility checks), or add task entries to address them. The current state implicitly leaves them in scope by stating "all CI workflows" in AC1 without exclusion language. Updating AC1 to read "all uv-using CI workflows" would accurately reflect what was done and close the completeness gap without additional code changes.

---

### Internal Consistency (0.87/1.00)

**Evidence:**

SHA pin format is perfectly uniform: every `uses:` line follows `action@{40-char-SHA} # {version-tag}` with no deviation across all 5 files. The `astral-sh/setup-uv` SHA `d4b2f3b6ecc6e67c4457f6d3e41ec42d3d0fcb86` and `actions/checkout` SHA `08c6903cd8c0fde910a37f88322edcfb5dd907a8` appear identically in every workflow that uses them — no divergent pins.

The `uv sync --frozen` pattern is consistently applied in every uv-using step with no bare `uv sync` calls remaining.

**Gaps:**

1. `ci.yml` `lint` and `type-check` jobs use `pip install` without the explanatory label present in `test-pip` (which has `# Uses standard pip/venv for maximum portability`). Reading `ci.yml` in isolation, it is not clear whether these pip calls are intentional design or oversight from EN-001. The `test-pip` job is clearly labeled; `lint` and `type-check` are not.

2. `docs.yml` specifies `python-version: 3.x` (floating) at line 30 while all other workflows using `actions/setup-python` specify `3.14` explicitly. This is a stylistic inconsistency, not a security risk, but breaks the pattern.

3. `release.yml` `build` job (lines 150-153) includes a comment "Requirements files for pip fallback" while copying `requirements.txt` and `requirements-dev.txt` to the archive. This comment is inconsistent with the EN-001 goal of eliminating pip fallbacks — the comment makes it appear pip fallback is intentional and supported, when EN-001 specifically removed pip fallback from the CI workflows themselves. (The archive may legitimately include requirements files for end-user installation, but the comment framing conflicts with the EN-001 narrative.)

**Improvement Path:**

Add comment labels to `lint` and `type-check` jobs explaining they are intentionally pip-based compatibility checks. Update `docs.yml` to pin Python version. Update the `release.yml` build archive comment to clarify requirements files are for end-user installation, not CI fallback.

---

### Methodological Rigor (0.85/1.00)

**Evidence:**

The approach is methodologically sound. Each task maps directly to a numbered finding (F-001, F-004, F-006, RISK-03) with inline YAML comments citing the originating finding ID. The `version-bump.yml` contains the most rigorous documentation: the `--frozen` rationale comment (lines 89-96) explains *why* the flag prevents dirty lockfiles in mechanistic detail, linking CI Python version differences to dependency re-resolution. This is high-quality inline documentation.

Task scoping is correct: task 6 (script consolidation) is correctly deferred as a separate concern — it touches `scripts/` directory and issue #150, a distinct scope from workflow YAML hardening. The Dependabot configuration addresses the sustainability concern: SHA pins without Dependabot would require manual updates and drift; the config solves the maintenance burden.

**Gaps:**

1. No documented verification step for the `[skip-bump]` fix. The conditional logic change in `version-bump.yml` lines 49-58 is significant — a bug in the conditional could cause version bumps to never run or always run. There is no evidence of a test run, dry-run, or scenario walkthrough verifying the logic is correct.

2. `docs.yml` is addressed (SHA pins applied) but the approach to `docs.yml` is incomplete: `pip install "mkdocs-material>=9.7.2"` at line 38 was not converted to uv or version-pinned more tightly. The methodology did not uniformly apply the same rigor to `docs.yml` that it applied to the other four files.

3. The prerelease input validation in `version-bump.yml` lines 157-161 (`^[a-zA-Z0-9]+$`) is not linked to a specific finding — it appears to be a BUG-003/RISK-02 holdover that is valuable but not referenced in the EN-001 task list.

**Improvement Path:**

Document a verification scenario for the `[skip-bump]` logic (e.g., "Verified: commit with `[skip-bump]` message in `workflow_dispatch` correctly skips bump"). Address `docs.yml` pip install consistency. These are low-effort additions that would raise this score to 0.90+.

---

### Evidence Quality (0.82/1.00)

**Evidence:**

All 10+ GitHub Actions across 5 workflow files are pinned to specific commit SHAs. Each SHA is paired with a human-readable version comment enabling manual verification against the GitHub Actions Marketplace. The version comments are accurate-format (vX.Y.Z semantic versions) for all but one entry. The work item cross-references two security review documents (`bug-003-devsecops-security-review.md`, `bug-003-red-recon-attack-surface.md`) and three GitHub issues (#150, #151, #153). Inline YAML comments directly cite originating finding IDs.

**Gaps:**

1. `ci.yml` line 471: `uses: MishaKav/pytest-coverage-comment@26f986d2599c288bb62f623d29c2da98609e9cd4 # main (2026-03-09)` — the version comment says `main` with a date rather than a semantic version tag. This means the SHA references a commit on the default branch, not a tagged release. This weakens evidence quality for this specific entry: if the maintainer force-pushes or rewrites history on `main`, the version comment becomes misleading. It also means there is no versioned release to cross-reference against.

2. The score report cannot independently verify SHA authenticity within the deliverable — this is a structural limitation, not a deliverable defect. However, the lack of a verification artifact (e.g., a comment in the PR or work item confirming SHAs were cross-checked against official releases) means claims are asserted rather than evidenced.

3. `bump-my-version==1.2.7` in `version-bump.yml` line 85 is pinned to an exact PyPI version — this is correct methodology but is a `uv tool install` call (not a GitHub Action), so it is not covered by the Dependabot `github-actions` config. The `pip` Dependabot ecosystem entry would catch this only if `bump-my-version` appears in a requirements file, which it does not. This is a maintenance gap.

**Improvement Path:**

Replace `# main (2026-03-09)` with a proper versioned release SHA (e.g., `# v0.7.0` or similar) for the `MishaKav/pytest-coverage-comment` action, or document why a tagged release is not available. Add `bump-my-version` to a tracked requirements file or add a note about manual rotation cadence.

---

### Actionability (0.84/1.00)

**Evidence:**

The implemented changes are directly actionable and complete for their stated scope:

- `release.yml`: Pip removed, uv installed via SHA-pinned action, `--frozen` applied. The job structure is correct and will execute as intended.
- `version-bump.yml`: SHA pins applied, `--frozen` applied in both `uv sync` calls, `[skip-bump]` guard added to `workflow_dispatch` conditional.
- `ci.yml`: All uv-using jobs have `--frozen`, all actions SHA-pinned.
- `pat-monitor.yml`: SHA-pinned `actions/github-script`.
- `docs.yml`: SHA-pinned `actions/checkout`, `actions/setup-python`, `actions/cache`.
- `dependabot.yml`: Configured with weekly schedule, correct `package-ecosystem` entries, appropriate labels.

The Dependabot configuration ensures the SHA pins remain maintainable over time — without it, the pins would drift silently.

**Gaps:**

1. `ci.yml` `type-check` job (lines 63-66) contains `pip install -e ".[dev]" || pip install -e .`. The `|| pip install -e .` fallback installs a floating version. If `pip install -e ".[dev]"` fails in a future Python version, the fallback silently installs an unpinned package. This is a residual supply chain risk that EN-001 was motivated to address.

2. `ci.yml` `security` job (lines 86-89) runs `pip install filelock mypy ruff` with floating versions. These are the same tools being scanned for security — a supply chain compromise of an unpinned version of `ruff` or `mypy` here would not be caught by the `pip-audit` scan that follows.

3. `docs.yml` `pip install "mkdocs-material>=9.7.2"` uses a lower-bound-only version pin. This will install the latest compatible version on each run, making `docs.yml` non-reproducible. A Dependabot PR for a `requirements-docs.txt` file would be the clean fix.

**Improvement Path:**

Pin the `pip install` calls in `lint`, `type-check`, and `security` jobs to exact versions (e.g., `ruff==X.Y.Z`) or convert them to use uv. For `docs.yml`, create a `requirements-docs.txt` file with `mkdocs-material==X.Y.Z` and reference it. These changes would raise the Actionability score to 0.92+ by eliminating residual supply chain risk in the same CI pipeline EN-001 was hardening.

---

### Traceability (0.88/1.00)

**Evidence:**

The traceability chain is strong throughout:

- Work item task table maps each task to an originating finding ID (F-001, F-004, F-006, RISK-03)
- Related Items section links to: originating bug BUG-003, GitHub issues #150/#151/#153, security review file, attack surface file
- Inline YAML comments in every changed file cite finding IDs: `# EN-001/F-001`, `# EN-001/F-004`, `# BUG-003/RISK-01`, `# BUG-003/RISK-02`, `# BUG-003/F-003`
- Work item history entry explicitly enumerates which tasks were completed
- `dependabot.yml` header comment: `# EN-001: All GitHub Actions are pinned to commit SHAs.`

**Gaps:**

1. `docs.yml` has no finding-ID comment in its header or inline. The other four workflow files each have structured comments linking to ADRs or finding IDs. `docs.yml` begins with `name: docs` and the first step is `actions/checkout` — there is no indication why the SHA pins were added or which EN-001 finding motivated the change.

2. `ci.yml` `coverage-report` job line 471 uses `MishaKav/pytest-coverage-comment@26f986d2599c288bb62f623d29c2da98609e9cd4 # main (2026-03-09)`. The version comment is a date string rather than a release version, which means future maintainers cannot quickly verify which release this SHA corresponds to in the action's changelog.

3. The pre-existing `# BUG-003/RISK-02` comment in `version-bump.yml` line 156 references a BUG-003 finding rather than an EN-001 finding, which could create confusion about which work item governs updates to that block. A cross-reference `# EN-001 (see also BUG-003/RISK-02)` would clarify the lineage.

**Improvement Path:**

Add a structured comment block to `docs.yml` referencing RISK-03 and EN-001. Update the `MishaKav` action SHA comment to reference the actual release version. These are documentation-only changes.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.82 | 0.90 | Explicitly scope EN-001 to exclude intentionally pip-based jobs (`lint`, `type-check`, `security` in `ci.yml`) by adding a comment label to each job, or add task entries to convert them. Update AC1 wording from "all CI workflows" to "all uv-using CI workflows" to close the gap between stated criteria and implemented scope. |
| 2 | Actionability | 0.84 | 0.92 | Pin the floating `pip install` calls in `ci.yml` `security` job (`filelock mypy ruff`) to exact versions, and pin `docs.yml` `pip install "mkdocs-material>=9.7.2"` to an exact version. These are the highest-residual-risk remaining supply chain gaps in the same pipeline EN-001 hardened. |
| 3 | Evidence Quality | 0.82 | 0.90 | Replace `# main (2026-03-09)` with a proper release version tag for `MishaKav/pytest-coverage-comment`. Confirm whether a tagged release is available; if not, document the rationale for using a branch SHA. |
| 4 | Internal Consistency | 0.87 | 0.93 | Add explanatory comment labels to `ci.yml` `lint` and `type-check` jobs matching the style of the `test-pip` job header comment. Update `release.yml` build archive comment from "Requirements files for pip fallback" to "Requirements files for end-user pip installation" to avoid narrative conflict with EN-001 goals. |
| 5 | Traceability | 0.88 | 0.94 | Add a structured header comment to `docs.yml` referencing RISK-03 / EN-001. Update the `MishaKav` action version comment. |
| 6 | Methodological Rigor | 0.85 | 0.92 | Document a verification scenario for the `[skip-bump]` conditional logic change in the work item history. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score — specific file names, line numbers, and exact content cited
- [x] Uncertain scores resolved downward (Evidence Quality and Completeness both held at 0.82 despite strong SHA-pin work, due to specific gaps that could not be argued away)
- [x] First-draft calibration considered — this is implementation work (not a first draft), but the 0.845 composite reflects genuine gaps in scope completeness and consistency
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Strong SHA-pin uniformity acknowledged in Internal Consistency (0.87) without pulling up weaker dimensions

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.845
threshold: 0.92
weakest_dimension: Completeness
weakest_score: 0.82
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Scope EN-001 acceptance criteria to explicitly exclude intentionally pip-based jobs (lint, type-check, security) by adding comment labels or updating AC1 wording"
  - "Pin floating pip installs in ci.yml security job and docs.yml to exact versions — these are the highest-residual supply chain risk"
  - "Replace MishaKav/pytest-coverage-comment version comment 'main (2026-03-09)' with a release tag version"
  - "Add explanatory labels to ci.yml lint and type-check jobs; update release.yml archive comment about requirements files"
  - "Add docs.yml header comment referencing RISK-03/EN-001"
  - "Document verification scenario for workflow_dispatch skip-bump conditional in work item history"
```
