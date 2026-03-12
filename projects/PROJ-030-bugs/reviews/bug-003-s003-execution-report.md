# Strategy Execution Report: S-003 Steelman Technique

## Execution Context

- **Strategy:** S-003 (Steelman Technique)
- **Template:** `.context/templates/adversarial/s-003-steelman.md`
- **Deliverable:** `.github/workflows/version-bump.yml` + `scripts/create-catchup-tags.sh`
- **Executed:** 2026-03-09T00:00:00Z
- **Finding Prefix:** SM (from Identity section)

---

## Findings Summary

| ID | Severity | Finding | Section |
|----|----------|---------|---------|
| SM-001 | Major | `--frozen` rationale understates mechanism — comment names symptom, not root cause (resolver re-resolution) | Lines 79–83 `Install project dependencies` |
| SM-002 | Major | Second `--frozen` invocation (line 156) insufficiently justified — strongest argument (prevents post-bump re-dirtying) absent | Lines 150–156 `Validate version sync` |
| SM-003 | Major | "Belt-and-suspenders" comment contradicts fail-fast implementation — comment implies recovery, code exits | Lines 108–123 `Ensure clean working tree` |
| SM-004 | Major | MTTR reduction purpose of diagnostic output chain not articulated — `::error::` + `git diff` + guidance each serve a specific role not explained | Lines 116–122 |
| SM-005 | Major | `github.actor` security argument names conclusion but not attack vector — "spoofable" without mechanism is assertion, not evidence | Lines 44–51 job `if:` condition |
| SM-006 | Minor | Cost/benefit asymmetry of `github.actor` change not stated — zero-cost change closing a genuine, if low-severity, manipulation vector | Lines 44–51 |
| SM-007 | Minor | Dry-run-as-default design rationale for catch-up script not explained | `scripts/create-catchup-tags.sh` lines 18, 46–49 |
| SM-008 | Minor | `yes/no` over `y/n` confirmation choice not justified | `scripts/create-catchup-tags.sh` line 82 |
| SM-009 | Minor | Provenance warning framed as caution rather than operator decision-making information | `scripts/create-catchup-tags.sh` lines 78–80 |

---

## Detailed Findings

### SM-001: `--frozen` Rationale Understates Root Mechanism

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Lines 79–83, `Install project dependencies` step |
| **Strategy Step** | Step 2 (Identify Weaknesses in Presentation) + Step 3 (Reconstruct the Argument) |

**Evidence:**

```yaml
# BUG-003: Use --frozen to prevent uv.lock modification in CI.
# CI must install from the committed lockfile, never re-resolve.
- name: Install project dependencies
  run: uv sync --frozen
```

**Analysis:**
The comment correctly identifies the desired outcome ("prevent modification") but does not supply the mechanism that makes `--frozen` the uniquely correct fix: `uv sync` without `--frozen` performs full dependency re-resolution using the installed Python version's metadata, which produces a different `uv.lock` when Python 3.14's resolver produces a different solution than the development environment's resolver. Without this mechanism being named, a reviewer cannot distinguish "correct fix" from "workaround that happens to work today." The evidence chain — resolver behaviour → lockfile mutation → dirty tree → bump failure — is absent from the comments.

**Recommendation:**
Expand the comment to name the mechanism: "Without `--frozen`, `uv sync` re-resolves dependencies using the installed Python version's metadata, which can produce a different `uv.lock` (observed with Python 3.14). `--frozen` installs exactly what was committed, enforcing reproducibility and using the lockfile as an integrity manifest."

---

### SM-002: Second `--frozen` Invocation Understated

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Lines 150–156, `Validate version sync` step |
| **Strategy Step** | Step 2 (Identify Weaknesses in Presentation) — Completeness gap |

**Evidence:**

```yaml
# BUG-003: Use --frozen here too — version field change in
# pyproject.toml does not affect dependency resolution.
- name: Validate version sync
  run: |
    uv sync --frozen
```

**Analysis:**
The comment is technically correct but undersells the risk. The strongest justification for `--frozen` at this invocation is not that the version field change doesn't affect resolution (a negative claim), but that without `--frozen`, a post-bump `uv sync` could re-resolve and re-dirty the tree immediately after `bump-my-version` produced a clean commit — undoing the hygiene guarantee achieved in the previous step. This is a qualitatively different and stronger argument.

**Recommendation:**
Revise to: "Use `--frozen` here too — without it, post-bump `uv sync` could re-resolve and re-dirty the tree, undoing the clean state just established by `bump-my-version`."

---

### SM-003: Comment/Implementation Mismatch in Clean-Tree Step

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Lines 108–123, `Ensure clean working tree` step |
| **Strategy Step** | Step 2 (Structural Weakness) + Step 3 (Reconstruct) |

**Evidence:**

```yaml
# Belt-and-suspenders: even with --frozen, reset any changes that
# could cause bump-my-version to fail (allow_dirty = false).
# Only resets tracked files — does not remove untracked files.
- name: Ensure clean working tree
  if: steps.bump.outputs.type != 'none'
  run: |
    if [[ -n "$(git status --porcelain)" ]]; then
      echo "::error::Working tree unexpectedly dirty before bump..."
      ...
      exit 1
    fi
```

**Analysis:**
The comment says "reset any changes" (implying `git checkout -- .` recovery). The implementation does `exit 1` (hard failure). This mismatch is a structural weakness: the comment is from an earlier draft of the fix that used silent recovery; the implementation was subsequently hardened to fail-fast per the F-005 security review. The mismatch creates cognitive dissonance for reviewers and suggests the comment was not updated when the implementation changed. The fail-fast approach is the stronger design (it surfaces anomalies rather than masking them), but the comment currently argues for the weaker approach.

**Recommendation:**
Replace comment with: "Fail-fast guard: even with `--frozen`, an unexpectedly dirty tree indicates an assumption violation outside this pipeline's control. Silent recovery would mask the root cause. Hard failure surfaces the anomaly with diagnostics — `git diff --name-only` gives the operator the exact files, and the guidance message gives the most likely remediation path."

---

### SM-004: MTTR Purpose of Diagnostic Chain Not Articulated

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Lines 116–122 |
| **Strategy Step** | Step 3 (Supply Missing Evidence) |

**Evidence:**

```bash
echo "::error::Working tree unexpectedly dirty before bump (uv sync --frozen should prevent this)"
git diff --name-only
echo ""
echo "If only uv.lock is dirty, the lockfile needs regeneration."
echo "Run 'uv lock' locally and commit the updated uv.lock."
exit 1
```

**Analysis:**
Each line of the diagnostic output serves a specific purpose that is not documented: `::error::` annotates the GitHub Actions log at the correct severity (surfaced in the PR check); `git diff --name-only` provides the operator's first diagnostic datum; the guidance message provides the most likely remediation path. The implementation is well-constructed; the gap is in the rationale documentation that would make this design defensible against "why not just `git checkout -- .` here?"

**Recommendation:**
Add a comment above this block: "Each diagnostic line reduces MTTR: `::error::` annotates the GA log, `git diff` names the dirty files, and the guidance message provides the most likely fix path. This is deliberately more informative than a silent reset."

---

### SM-005: `github.actor` Attack Vector Not Named

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Lines 44–51, job `if:` condition |
| **Strategy Step** | Step 2 (Evidence Weakness) + Step 3 (Strengthen Evidence) |

**Evidence:**

```yaml
# BUG-003/F-003: Use github.actor (authenticated identity from token)
# instead of author.name (spoofable via git config user.name)
if: >-
  github.event_name == 'workflow_dispatch' ||
  (
    !contains(github.event.head_commit.message, '[skip-bump]') &&
    github.actor != 'github-actions[bot]'
  )
```

**Analysis:**
The comment names the property distinction ("authenticated vs. spoofable") but not the concrete attack vector. Without the attack vector, "spoofable" reads as theoretical. The concrete attack is: any developer can set `git config user.name "github-actions[bot]"` and commit, causing the original check to treat their commit as a bot commit and permanently suppress the version bump for their change. This is a real, trivially-executable attack with a material pipeline consequence.

**Recommendation:**
Expand to: "Use `github.actor` (platform-set from authenticated token) not `author.name` (user-configurable git metadata). Attack vector: any committer can `git config user.name 'github-actions[bot]'` to impersonate the bot and suppress version bumps for their commits. `github.actor` is not user-controllable."

---

### SM-006: Cost/Benefit Asymmetry Not Stated (Minor)

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Lines 44–51 |
| **Strategy Step** | Step 3 (Strengthen Framing) |

**Evidence:** The comment justifies the security improvement but does not note it is a single-field name replacement with zero runtime cost.

**Analysis:** Noting the asymmetry (zero cost, genuine attack surface closed) preempts a "is this worth the churn?" objection from reviewers.

**Recommendation:** Add: "This is a single-field replacement with zero runtime cost and zero behavioural change for legitimate runs."

---

### SM-007: Dry-Run-as-Default Rationale Absent (Minor)

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | `scripts/create-catchup-tags.sh` lines 18, 46–49 |
| **Strategy Step** | Step 3 (Supply Missing Reasoning) |

**Evidence:**

```bash
MODE="${1:-}"
...
if [ -z "$MODE" ]; then
    echo "[DRY RUN] No tags created. Use --apply to create locally, --push to create and push."
    exit 0
fi
```

**Analysis:** The dry-run default is a correct safety design but its rationale (accidental execution of a release-infrastructure script with no arguments should have zero side effects) is not stated.

**Recommendation:** Add comment: "# Default: dry run. Accidental execution without arguments must have zero side effects — this script touches release infrastructure."

---

### SM-008: `yes/no` Confirmation Choice Unjustified (Minor)

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | `scripts/create-catchup-tags.sh` line 82 |
| **Strategy Step** | Step 3 (Supply Missing Evidence) |

**Evidence:** `read -p "Continue pushing ${#MISSING_TAGS[@]} tags? (yes/no): " confirm`

**Analysis:** Requiring `yes` (not `y`) prevents muscle-memory confirmation of a bulk push of 36 release-triggering tags. The design choice is correct; the rationale is absent.

**Recommendation:** Add inline comment: `# Require full "yes" to prevent accidental confirmation via muscle-memory "y" keypress`

---

### SM-009: Provenance Warning Framing (Minor)

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | `scripts/create-catchup-tags.sh` lines 78–80 |
| **Strategy Step** | Step 3 (Strengthen Framing) |

**Evidence:**

```bash
echo "PROVENANCE NOTE: These catch-up tags are annotated but NOT GPG-signed."
echo "They provide version history but not cryptographic provenance."
```

**Analysis:** The note is accurate but passive. Framing it as "operator decision information" rather than a caution would make its purpose clearer: the operator can make an informed choice about whether unsigned tags are acceptable for their release pipeline's trust model.

**Recommendation:** Add: "Consumers verifying tag signatures will not find them. If your release pipeline requires GPG-signed tags, add a signing step before pushing."

---

## Execution Statistics

- **Total Findings:** 9
- **Critical:** 0
- **Major:** 5
- **Minor:** 4
- **Protocol Steps Completed:** 6 of 6
- **H-15 Self-Review:** Completed
- **Steelman Report Path:** `projects/PROJ-030-bugs/research/bug-003-s003-steelman.md`
- **Downstream Readiness:** Ready for S-002 (Devil's Advocate) per H-16
