# GitHub Issue Drafts — Documentation & Agentic Workflows

> Draft ticket content for /eng-team, /red-team, /adversary review before creation.

## Category 1: Documentation How-To Guides

### TICKET-1: How-to guide — Update a SHA-pinned GitHub Action

**Title:** docs: How-to guide for updating SHA-pinned GitHub Actions

**Labels:** documentation

**Body:**

Create a Diataxis how-to guide covering the procedure for updating a SHA-pinned GitHub Action when Dependabot opens a PR or a manual update is needed.

**Scope:**
- Verify the new SHA against the action's release page
- Update the SHA and version comment in all workflow files where the action appears
- Cross-reference the SHA-to-version mapping table in `docs/reference/ci-cd-pipeline-security.md`
- Run CI to validate the update
- Update the reference documentation table

**Acceptance Criteria:**
- [ ] How-to guide at `docs/howto/update-sha-pinned-action.md`
- [ ] Added to mkdocs.yml nav under Guides
- [ ] Cross-links to reference doc (`docs/reference/ci-cd-pipeline-security.md`)
- [ ] Passes MkDocs strict mode build
- [ ] Created using /diataxis skill (diataxis-howto agent)

**References:**
- `docs/reference/ci-cd-pipeline-security.md` (SHA Pinning section)
- `docs/explanation/ci-cd-supply-chain-security.md` (Why SHA pinning matters)
- Related: #130 (PROJ-015: Doc Audit), #135 (PROJ-016: Doc Writing), #153 (EN-001)

---

### TICKET-2: How-to guide — Add a new CI job to the Jerry pipeline

**Title:** docs: How-to guide for adding a new CI job

**Labels:** documentation

**Body:**

Create a Diataxis how-to guide for adding a new job to `.github/workflows/ci.yml`.

**Scope:**
- SHA-pin all GitHub Actions used in the new job
- Pin the uv binary version to match existing jobs
- Use `uv sync --frozen` for dependency installation
- Wire the new job into the `ci-success` gate (including skipped-state handling)
- Update `docs/reference/ci-cd-pipeline-security.md` tables

**Acceptance Criteria:**
- [ ] How-to guide at `docs/howto/add-ci-job.md`
- [ ] Added to mkdocs.yml nav under Guides
- [ ] Covers ci-success gate wiring pattern (including skipped handling)
- [ ] Passes MkDocs strict mode build
- [ ] Created using /diataxis skill (diataxis-howto agent)

**References:**
- `docs/reference/ci-cd-pipeline-security.md` (all sections)
- `.github/workflows/ci.yml` (ci-success job pattern)
- Related: #130, #135, #153

---

### TICKET-3: How-to guide — Add a new GitHub Actions dependency

**Title:** docs: How-to guide for adding a new GitHub Actions dependency

**Labels:** documentation

**Body:**

Create a Diataxis how-to guide for introducing a new third-party GitHub Action to the CI pipeline.

**Scope:**
- Evaluate the action's maintenance status and trustworthiness
- Find the correct commit SHA for the desired version
- Add to Dependabot monitoring (if not already covered by `github-actions` ecosystem)
- Update SHA-to-version mapping in reference docs
- Security considerations for new supply chain dependencies

**Acceptance Criteria:**
- [ ] How-to guide at `docs/howto/add-github-actions-dependency.md`
- [ ] Added to mkdocs.yml nav under Guides
- [ ] Includes action trustworthiness evaluation checklist
- [ ] Passes MkDocs strict mode build
- [ ] Created using /diataxis skill (diataxis-howto agent)

**References:**
- `docs/reference/ci-cd-pipeline-security.md` (SHA Pinning, Dependabot sections)
- `docs/explanation/ci-cd-supply-chain-security.md` (threat model)
- Related: #130, #135, #153

---

## Category 2: Agentic Documentation Workflows

### TICKET-4: Design agentic /diataxis documentation freshness auditing workflow

**Title:** feat: Agentic /diataxis documentation freshness auditing workflow

**Labels:** enhancement, documentation

**Body:**

Design and implement an agentic workflow that uses the /diataxis skill (diataxis-auditor agent) to automatically audit documentation freshness and quality when relevant source files change.

**Problem:**
Documentation drifts from implementation over time. CI/CD pipeline docs become stale when workflows are modified. Reference docs cite outdated version numbers. How-to guides reference deprecated procedures. Currently, documentation staleness is only caught by manual review.

**Proposed Design:**

1. **Trigger:** When a PR modifies files in `.github/workflows/`, `pyproject.toml`, `src/`, or `skills/*/`, a CI job runs the diataxis-auditor to check if corresponding docs are affected.

2. **Detection:** The auditor maps source files to documentation files using a configurable mapping (e.g., `.github/workflows/ci.yml` maps to `docs/reference/ci-cd-pipeline-security.md`). When a source file changes and its mapped doc file is NOT also modified in the PR, the auditor flags it.

3. **Output:** The CI job produces a PR comment listing potentially stale docs with a recommendation to review/update them. This is advisory (warning), not blocking (error).

4. **Escalation path:** If a mapped doc is flagged as stale in 3+ consecutive PRs without update, escalate from warning to error.

**Acceptance Criteria:**
- [ ] Source-to-doc mapping configuration file (YAML)
- [ ] CI job that runs mapping check on PR events
- [ ] PR comment output with stale doc warnings
- [ ] Escalation counter mechanism (advisory -> blocking)
- [ ] Documentation of the workflow itself (meta!)
- [ ] Security review via /eng-team (agentic CI security)
- [ ] Threat assessment via /red-team (supply chain and injection risks)
- [ ] Quality review via /adversary

**Security Considerations:**
- No LLM execution in CI for this phase — deterministic file mapping only
- Future phase may add LLM-powered content analysis (requires separate security review)
- Mapping file must be in repo (not external) to prevent supply chain manipulation
- PR comment content is derived from repo-internal mapping only (no untrusted input)

**References:**
- `/diataxis` skill (diataxis-auditor agent)
- #130 (PROJ-015: Doc Audit), #135 (PROJ-016: Doc Writing)
- `docs/reference/ci-cd-pipeline-security.md` (existing CI security controls)

---

### TICKET-5: Implement doc-to-source mapping for automated staleness detection

**Title:** feat: Source-to-documentation mapping configuration for staleness detection

**Labels:** enhancement, documentation

**Body:**

Create the source-to-documentation mapping configuration that powers the documentation freshness auditing workflow (see parent ticket for design).

**Scope:**
- Define YAML schema for source-to-doc mappings
- Create initial mapping covering CI/CD docs:
  - `.github/workflows/ci.yml` -> `docs/reference/ci-cd-pipeline-security.md`
  - `.github/workflows/version-bump.yml` -> `docs/reference/ci-cd-pipeline-security.md`
  - `.github/workflows/release.yml` -> `docs/reference/ci-cd-pipeline-security.md`
  - `.github/dependabot.yml` -> `docs/reference/ci-cd-pipeline-security.md`
  - `.github/workflows/*.yml` -> `docs/explanation/ci-cd-supply-chain-security.md`
- Expand mappings for skill docs, architecture docs, etc.
- Validate mapping at CI time (all referenced files must exist)

**Acceptance Criteria:**
- [ ] Mapping file at `.github/doc-source-map.yml`
- [ ] JSON Schema for mapping validation
- [ ] Initial CI/CD doc mappings populated
- [ ] CI validation that all paths in mapping exist
- [ ] Reference documentation for the mapping format

**References:**
- Parent: Documentation freshness auditing workflow ticket
- `docs/reference/ci-cd-pipeline-security.md`

---

### TICKET-6: Claude Code hook for documentation freshness pre-commit check

**Title:** feat: Pre-commit hook for documentation freshness advisory

**Labels:** enhancement, documentation

**Body:**

Implement a Claude Code `pre_tool_use` or `post_tool_use` hook that advises when source file edits may require corresponding documentation updates, using the source-to-doc mapping from the mapping configuration.

**Problem:**
The CI-based freshness check catches stale docs after PR creation. A pre-commit advisory would catch them earlier — at edit time — reducing the feedback loop.

**Proposed Design:**
1. When files matching source patterns in the doc-source-map are edited, the hook checks if the corresponding doc file was also edited in the same session.
2. If not, emit an advisory message: "You modified X which maps to doc Y. Consider updating Y."
3. Advisory only — never blocks. The CI job is the enforcement gate.

**Acceptance Criteria:**
- [ ] Hook implementation using Claude Code hooks API
- [ ] Reads from `.github/doc-source-map.yml`
- [ ] Advisory-only output (no blocking)
- [ ] Does not fire for doc-only changes
- [ ] Security review: hook must not execute untrusted content from mapping file

**Security Considerations:**
- Hook runs in user's local environment — must not execute arbitrary commands from mapping file
- Mapping file is read-only data (file paths), not executable content
- Hook must validate mapping file structure before processing

**References:**
- Parent: Documentation freshness auditing workflow ticket
- Claude Code hooks documentation
- `.github/doc-source-map.yml` (from mapping ticket)
