# How to Add a New CI Job

> Add a job to `.github/workflows/ci.yml` that meets all Tom security controls and wires correctly into the `ci-success` gate.

## Before You Begin

You need:
- Write access to the repository
- The job's purpose, trigger scope (all events or PR-only), and whether it uses the project virtual environment via `uv`
- Current SHA-to-version mapping from [docs/reference/ci-cd-pipeline-security.md](../reference/ci-cd-pipeline-security.md#sha-pinning)

---

## Steps

### 1. Define the job with a descriptive name

Add the job block to `.github/workflows/ci.yml` inside the `jobs:` key. Use a kebab-case job ID and a human-readable `name:`.

```yaml
  my-new-job:
    name: My New Check
    runs-on: ubuntu-latest
```

### 2. Declare job-level permissions (mandatory)

The workflow-level `permissions:` block in `ci.yml` includes `pull-requests: write`. Any job that omits its own `permissions:` block inherits this silently. Always declare a job-level `permissions:` block to override the workflow default.

For jobs that only read the repository and produce no GitHub API side effects:

```yaml
  my-new-job:
    name: My New Check
    runs-on: ubuntu-latest
    permissions:
      contents: read
```

If the job writes PR comments, add `pull-requests: write`. Grant no other permissions.

### 3. SHA-pin every GitHub Action used in the job

For each `uses:` line, replace the floating tag with the commit SHA and add a version comment. Use the SHA-to-version table in [docs/reference/ci-cd-pipeline-security.md](../reference/ci-cd-pipeline-security.md#sha-pinning).

```yaml
    steps:
      - uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
```

Do not use floating tags such as `@v5` or `@main`.

### 4. Pin the uv binary version (uv jobs only)

If the job installs dependencies or runs Python via `uv`, install `uv` with the version pinned to match existing jobs. Check the current value in the [UV Binary Pinning](../reference/ci-cd-pipeline-security.md#uv-binary-pinning) section of the reference doc.

```yaml
      - name: Install uv
        uses: astral-sh/setup-uv@d4b2f3b6ecc6e67c4457f6d3e41ec42d3d0fcb86 # v5.4.2
        with:
          version: "0.10.9"

      - name: Set up Python
        run: uv python install 3.14  # Check pyproject.toml requires-python for current version
```

### 5. Install dependencies with `uv sync --frozen`

Install the project's virtual environment using `--frozen`. Append extras as the job requires.

```yaml
      - name: Install dependencies
        run: uv sync --frozen
```

If the job needs the `dev` or `test` extras:

```yaml
      - name: Install dependencies
        run: uv sync --frozen --extra dev --extra test
```

Never use `uv sync` without `--frozen` in CI.

### 6. Pass `github.event` values via env block (CLCHK-001)

If any `run:` script needs a value from `github.event` (such as PR title, actor, or commit message), declare it in an `env:` block on the step. Never inline `${{ github.event.* }}` directly inside a `run:` script.

```yaml
      - name: Check something PR-specific
        env:
          PR_TITLE: ${{ github.event.pull_request.title }}
          PR_ACTOR: ${{ github.actor }}
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
        run: |
          # Use $PR_TITLE, $PR_ACTOR, $BASE_SHA as shell variables
          if [[ "$PR_ACTOR" == "dependabot[bot]" ]]; then
            echo "Bot — skipping."
            exit 0
          fi
```

This applies to any `github.event.*` expression. GitHub context values that are safe constants (e.g., `github.event_name`, `github.ref`, `github.sha`) may be inlined only when they cannot carry user-controlled content.

### 7. Handle skipped-state if the job is PR-only (CLCHK-003 pattern)

If the job runs only on pull requests (`if: github.event_name == 'pull_request'`), it reports `skipped` on push events. The `ci-success` gate must accept both `success` and `skipped` for this job.

In the job definition, add the event filter:

```yaml
  my-new-job:
    name: My New Check
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
```

In the `ci-success` gate step (step 8 below), use the `success || skipped` check pattern instead of `!= "success"`.

Skip this step entirely if the job runs on all events.

### 8. Wire the job into the `ci-success` gate

Open the `ci-success` job at the bottom of `ci.yml`. Add your job ID to two places.

**In `needs:`:**

```yaml
  ci-success:
    name: CI Success
    runs-on: ubuntu-latest
    needs: [lint, type-check, security, ..., my-new-job]
    if: always()
```

**In the `Check all jobs passed` run block:**

For a job that runs on all events, add a failure branch alongside the existing ones. The `${{ needs.*.result }}` values are GitHub-controlled enums (`success`, `failure`, `cancelled`, `skipped`) and cannot carry user content, so inlining them in `run:` is safe — unlike `github.event.*` values from step 6.

```yaml
          if [[ "${{ needs.lint.result }}" != "success" ]] || \
             ...
             [[ "${{ needs.my-new-job.result }}" != "success" ]]; then
```

And add the job to the success echo at the bottom:

```yaml
          echo "  - My new check: OK"
```

For a PR-only job (CLCHK-003), add a separate block that accepts both `success` and `skipped`:

```yaml
          MY_NEW_JOB_RESULT="${{ needs.my-new-job.result }}"
          if [[ "$MY_NEW_JOB_RESULT" != "success" && "$MY_NEW_JOB_RESULT" != "skipped" ]]; then
            echo "my-new-job failed: $MY_NEW_JOB_RESULT"
            exit 1
          fi
```

And update the echo line to show the dynamic result:

```yaml
          echo "  - My new check: ${MY_NEW_JOB_RESULT}"
```

### 9. Update the security reference tables

Open `docs/reference/ci-cd-pipeline-security.md` and update two tables:

- **SHA Pinning — "Workflows where SHA-pinned actions appear"**: Add a column or row entry for `ci.yml` next to each action your job uses.
- **UV Binary Pinning — "Workflows that apply this pin"**: Add your job name to the `ci.yml` row if the job uses `uv`.

If the job uses `uv sync --frozen`, add it to the **Frozen Lockfile Enforcement** table row for `ci.yml`.

### 10. Run CI to verify

Push the branch and confirm the new job appears in the GitHub Actions run. Verify:

- Your new job runs and passes (or shows `skipped` if PR-only and the run is a push).
- The `ci-success` job passes and its log includes your job's status line.
- No other jobs are broken.

---

## Verification

In the GitHub Actions run for your branch, the `ci-success` job log should contain your job's echo line:

```
  - My new check: OK
```

For a PR-only job on a push event:

```
  - My new check: skipped
```

---

## Troubleshooting

**Problem:** `ci-success` fails with "One or more jobs failed" even though your new job passed.

**Solution:** Your job ID in `needs:` does not match the job key in `jobs:`. Confirm the ID is identical in both places.

**Problem:** `ci-success` fails on push events reporting your new job as `skipped`.

**Solution:** Your job uses `if: github.event_name == 'pull_request'` but you added it to the `!= "success"` branch rather than the CLCHK-003 `success || skipped` pattern. Move the job to the PR-only block in the `ci-success` step.

**Problem:** `uv sync --frozen` exits with an error about the lockfile being inconsistent.

**Solution:** Run `uv sync` locally to update `uv.lock`, then commit the updated lockfile before pushing.

**Problem:** A `run:` script mishandles a PR title with special characters or quotes.

**Solution:** The `github.event.pull_request.title` value is being inlined with `${{ }}`. Move it to an `env:` block per step 6 (CLCHK-001).

---

## Related

- **Reference:** [CI/CD Pipeline Security Controls](../reference/ci-cd-pipeline-security.md) — SHA table, UV pinning, frozen lockfile, and CLCHK pattern definitions
- **Explanation:** [About CI/CD Supply Chain Security](../explanation/ci-cd-supply-chain-security.md) — Background on why these controls exist
