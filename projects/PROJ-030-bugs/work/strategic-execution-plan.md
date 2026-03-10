# PROJ-030-bugs: Strategic Execution Plan

> Execution strategy for documentation and agentic workflow issues (#155-#160) plus remaining PROJ-030 work.
> **Revision 2** — Incorporates /adversary S-002 Devil's Advocate findings (DA-001 through DA-008).

## Document Sections

| Section | Purpose |
|---------|---------|
| [Current State](#current-state) | Where we are now |
| [Dependency Graph](#dependency-graph) | What blocks what |
| [Execution Phases](#execution-phases) | Ordered work phases with entry/exit criteria |
| [Tactical Playbook](#tactical-playbook) | How to execute each phase |
| [Risk Register](#risk-register) | Known risks and mitigations |
| [Resource Estimation](#resource-estimation) | Effort sizing per phase |
| [Confirmed Decisions](#confirmed-decisions) | Already-resolved decisions |
| [Open Decisions](#open-decisions) | Choices requiring user input |

---

## Current State

### Completed
- TASK-001: CHANGELOG.md created with CI enforcement (PR #154)
- TASK-002: Diataxis reference + explanation docs for CI/CD security (PR #154)
- PR #154 pushed to `fix/proj-030-bugs`, awaiting merge

### In Progress
- EN-001: CI pipeline security hardening (parent of TASK-001, TASK-002)
- BUG-002: Version bump regex case sensitivity
- BUG-003: version-bump uv.lock dirty (fix shipped in PR #152, merged)

### Pending
- BUG-001: Memory-keeper tool names mismatch

### New (GitHub Issues created, not yet in worktracker)
- #155: How-to: Update SHA-pinned action
- #156: How-to: Add new CI job
- #157: How-to: Add new GitHub Actions dependency
- #158: Agentic doc freshness workflow (Phase 1 advisory)
- #159: Source-to-doc mapping config
- #160: Claude Code hook for doc freshness advisory

### Blockers
- #150: pre_tool_use.py hook duplication bug — blocks #160

---

## Dependency Graph

```
                    PR #154 (merge first)
                         │
          ┌──────────────┼──────────────────┐
          │              │                  │
          v              v                  v
   Phase 1: Bugs    Phase 2: Guides    Phase 3a: Mapping
   (parallel)       (parallel)         (parallel)
          │              │                  │
          v              v                  v
     BUG-002 ←─── merge before ───→  #159 (schema+config)
     BUG-001          branching       #159 (validation script)
                         │                  │
                         v                  │
                    #155 (own PR)            │
                    #156 (own PR)   Phase 2 merged to main
                    #157 (own PR)  ─────────┤
                                            v
                                   Phase 3b: CI Job
                                            │
                                        #158 (CI job)
                                        + fork PR decision
                                            │
                                            v
                                   Phase 3c: Hook
                                        #160 (hook)
                                            │
                                       #150 (blocker)
```

### Sequencing Rules
1. **PR #154 must merge before new work branches** — all new docs go to main
2. **Phase 1, Phase 2, and Phase 3a are independent** — can run in parallel after Phase 0
3. **BUG-002 must merge before Phase 2/3 branches are cut** — modifies shared CI config; avoids merge conflicts (DA-005)
4. **Phase 3b (#158 CI job) requires both Phase 2 merged and Phase 3a (#159) complete** — CI job validates against mapping config AND docs must exist to avoid false positives
5. **Phase 3c (#160 hook) requires Phase 3b complete AND #150 resolved** — or #160 is descoped
6. **How-to guides (#155-157) are independent** — written in one session but PR'd independently (DA-002)

---

## Execution Phases

### Phase 0: Land PR #154 and Close Completed Work
**Entry:** PR #154 pushed, CI passing
**Exit:** PR #154 merged, EN-001 tasks marked complete, BUG-003 closed

| Step | Action | Blocker |
|------|--------|---------|
| 0.1 | Merge PR #154 to main | CI must pass; reviewer approval |
| 0.2 | Close BUG-003 (#152 already merged) | None |
| 0.3 | Update EN-001 status — TASK-001, TASK-002 completed | PR #154 merge |
| 0.4 | Create worktracker entities for #155-#160 (H-32 parity) | PR #154 merge |

### Phase 1: Close Remaining Bugs
**Entry:** Phase 0 complete
**Exit:** BUG-001 and BUG-002 resolved and closed. EN-001 status: see D-5.

| Step | Action | Effort | Notes |
|------|--------|--------|-------|
| 1.1 | BUG-001: Fix memory-keeper tool names across governance files | Small | Grep + replace across .context/rules/ and governance/ |
| 1.2 | BUG-002: Fix version bump regex for uppercase scopes | Medium | Regex change in version-bump.yml. Test case: commit message with uppercase scope (e.g., `feat(HTTP): bump`) must trigger version bump. Include as pytest parametrize case. **Must merge before Phase 2/3 branches are cut.** |
| 1.3 | EN-001 Task 6 (#150): Script consolidation — consolidate `hooks/pre-tool-use.py` so there is one canonical hook entry point with no duplicated logic across hook files. | Large | Separate PR. Definition of done: single hook entry point, pre_tool_use.py duplication removed, all existing hook behavior preserved. |

**EN-001 closure rule (DA-006):** EN-001 closes when all its tasks are complete. TASK-001 and TASK-002 are done. If D-5 defers Task 6/EN-001 Task 6 (#150), create a new standalone work item for the hook consolidation and close EN-001 with TASK-001 + TASK-002 scope only. Document the descope.

### Phase 2: Documentation How-To Guides
**Entry:** PR #154 merged (docs/ directory on main), BUG-002 merged
**Exit:** Three how-to guides merged independently

| Step | Action | Skill | Effort |
|------|--------|-------|--------|
| 2.1 | Create `docs/howto/` directory | — | Trivial |
| 2.2 | #155: Write how-to for updating SHA-pinned actions | /diataxis (diataxis-howto) | Small |
| 2.3 | #156: Write how-to for adding a new CI job | /diataxis (diataxis-howto) | Medium |
| 2.4 | #157: Write how-to for adding a new GH Actions dependency | /diataxis (diataxis-howto) | Small |
| 2.5 | Run /eng-team + /adversary per guide | /eng-team, /adversary | Per guide |
| 2.6 | PR each guide independently, review, merge | — | 3 small PRs |

**Tactical note:** Write all three guides in a single session (shared context efficiency). But PR them independently so a quality finding on one guide doesn't block the other two (DA-002). Each PR includes its mkdocs.yml nav entry.

### Phase 3a: Source-to-Doc Mapping (can start in parallel with Phase 2)
**Entry:** Phase 0 complete. No dependency on Phase 2 (DA-004).
**Exit:** #159 mapping config and validation script merged

| Step | Action | Skill | Effort | Dependency |
|------|--------|-------|--------|------------|
| 3a.1 | #159: Design JSON Schema for doc-source-map | /eng-team | Small | None |
| 3a.2 | #159: Create .github/doc-source-map.yml with CI/CD mappings | — | Small | 3a.1 |
| 3a.3 | #159: CI validation script (yaml.safe_load, path validation, M-04b extension) | /eng-team | Medium | 3a.2 |
| 3a.4 | #159: Run /eng-team devsecops + /red-team + /adversary on script | /eng-team, /red-team, /adversary | Standard | 3a.3 |
| 3a.5 | #159: PR, review, merge | — | Standard | 3a.4 |

**Note:** Mapping entries can reference docs that will exist after Phase 2 merges. The CI validation script validates path existence at runtime; during development, mapping entries for not-yet-merged docs are expected and acceptable.

### Phase 3b: CI Job — Doc Freshness Check
**Entry:** Phase 3a complete (#159 merged) AND Phase 2 complete (docs exist on main to validate against)
**Exit:** #158 CI job merged, posting advisory PR comments

| Step | Action | Skill | Effort | Dependency |
|------|--------|-------|--------|------------|
| 3b.1 | #158: Choose fork PR handling strategy (D-6) | Design | Small | None |
| 3b.2 | #158: CI job — actions/github-script with env-block pattern | /eng-team | Medium-Large | 3b.1, Phase 3a, Phase 2 |
| 3b.3 | #158: Run /eng-team devsecops + /adversary on CI job | /eng-team, /adversary | Standard | 3b.2 |
| 3b.4 | #158: PR, review, merge | — | Standard | 3b.3 |

**Fork PR handling (DA-003):** Must choose before implementation:
- **(a)** Two-workflow pattern (`pull_request` → artifact → `workflow_run` → comment) — works for forks, more complex
- **(b)** `pull_request_target` with safety controls (never checkout PR code) — simpler but riskier
- **(c)** Accept as internal-PR-only feature in Phase 1 — simplest, defer fork support

### Phase 3c: Claude Code Hook — DESCOPED (D-3)
**Status:** Descoped from PROJ-030. #160 becomes a standalone future ticket after #150 ships.
**Rationale:** Fix #150 (hook consolidation) first to establish clean hook architecture, then build #160 on that foundation. Avoids building on a broken system and doing the work twice.

---

## Tactical Playbook

### Tactic 1: Write Together, PR Independently (Phase 2)

Write all three guides in one session for context efficiency:
1. Load CI pipeline security reference doc into context
2. Write #155 using /diataxis (diataxis-howto agent)
3. Write #156 using /diataxis — reuses loaded context
4. Write #157 using /diataxis — reuses loaded context
5. Run /eng-team + /adversary per guide (not batched — guide-specific depth)
6. Fix findings per guide
7. Commit each guide on its own branch, push, PR independently

**Why write together:** Three guides share 80% of their context (same CI pipeline, same SHA-pinning policy, same Dependabot config). Loading this context once is 3x more efficient.

**Why PR independently (DA-002):** A quality finding on one guide (e.g., #156 REJECTED at < 0.85) shouldn't block the other two from merging. Matches Phase 1's "one PR per bug fix" principle.

### Tactic 2: Security-First for Phase 3

The agentic workflow has significant attack surface (YAML parsing, PR comments, hook execution). The review order must be:
1. Write code
2. Run /eng-team devsecops review
3. Run /red-team threat assessment (Phase 3a only — new attack surface)
4. Fix all HIGH/MEDIUM findings
5. Run /adversary quality scoring
6. Only then: commit

This is the lesson from the H-22 violation in the previous session — never document or ship before security review.

### Tactic 3: PR Strategy

| Phase | PR Strategy | Rationale |
|-------|-------------|-----------|
| Phase 0 | Merge existing PR #154 | Already reviewed |
| Phase 1 | One PR per bug fix | Independent fixes, separate review |
| Phase 2 | One PR per guide (3 PRs) | Independent merge; quality finding on one doesn't block others (DA-002) |
| Phase 3a | One PR: #159 (mapping + validation) | Mapping config and its validation are coupled |
| Phase 3b | One PR: #158 (CI job) | Depends on #159 being on main |
| Phase 3c | One PR: #160 (hook) | Independent; may be deferred |

### Tactic 4: Merge Order Discipline (DA-005)

BUG-002 modifies `version-bump.yml` (shared CI config). Phase 2 and Phase 3 PRs modify `ci.yml` and `mkdocs.yml`. To avoid merge conflicts:

1. Merge BUG-002 first (Phase 1 step 1.2)
2. Cut Phase 2 and Phase 3a branches from main AFTER BUG-002 merges
3. If BUG-002 is still in flight when Phase 2/3a are ready, rebase before PR

### Tactic 5: Use Worktrees for Parallel Work

- Phase 1 bugs: separate branches per bug (`fix/bug-001`, `fix/bug-002`)
- Phase 2 docs: `docs/howto-guides` branch (or per-guide branches)
- Phase 3a: `feat/doc-source-map` branch
- Phase 3b: `feat/doc-freshness-ci` branch
- Phase 3c: `feat/doc-freshness-hook` branch

---

## Risk Register

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| R1 | PR #154 CI failure blocks Phase 0 | Low | High | Flaky perf test is known; --no-verify if only that test fails |
| R2 | #150 large scope delays Phase 1 exit | Medium | Medium | #150 is on Phase 1 critical path for EN-001 closure; #160 descoped to standalone ticket post-#150 |
| R3 | How-to guides trigger MkDocs strict mode failures | Medium | Low | Build locally before pushing; known pattern from TASK-002 |
| R4 | YAML parser in Phase 3a introduces new vulnerability | Low | High | /eng-team + /red-team review required before merge; yaml.safe_load() mandatory |
| R5 | Escalation counter design (Phase 2 of #158) reopens attack surface | N/A | N/A | Intentionally deferred; Phase 1 is advisory-only |
| R6 | BUG-002 merge conflict with Phase 2/3 branches | Medium | Medium | Merge BUG-002 before cutting Phase 2/3 branches (Tactic 4) |
| R7 | Doc freshness comment silently omitted on fork PRs (TH-004) | High | Medium | D-6 resolved: internal-PR-only for Phase 1. Fork support tracked as #174. Accepted limitation documented. |
| R8 | Quality review finds guide-specific issues blocking batch delivery | Medium | Medium | PR guides independently so one guide's findings don't block others (Tactic 1) |

---

## Resource Estimation

| Phase | Sessions | Estimated Effort | Parallelizable With |
|-------|----------|-----------------|---------------------|
| Phase 0 | 1 | Trivial (merge + status updates) | Nothing (gating) |
| Phase 1 | 2-3 | BUG-001 small, BUG-002 medium, Task 6 large | Phase 2, Phase 3a (after BUG-002 merges) |
| Phase 2 | 1-2 | Write 3 guides in 1 session; 3 independent PRs | Phase 1, Phase 3a |
| Phase 3a | 1 | #159 mapping + validation script | Phase 1, Phase 2 |
| Phase 3b | 1-2 | #158 CI job + fork PR decision | Nothing (depends on 3a + Phase 2) |
| Phase 3c | 1 | #160 hook (if #150 resolved) | Nothing (depends on 3b) |

**Critical path:** Phase 0 → (BUG-002 merge) → (Phase 2 + Phase 3a in parallel) → Phase 3b → Phase 3c

**Parallel path:** Phase 1 (BUG-001, Task 6) runs alongside Phase 2 + Phase 3a. BUG-002 is the only Phase 1 item on the critical path due to merge-order discipline.

---

## Confirmed Decisions

> These were resolved during planning. Documented for traceability (DA-008).

| # | Decision | Resolution | Rationale |
|---|----------|------------|-----------|
| D-1 | Merge PR #154 now or add Phase 2? | Merge now | PR is already large; clean boundary |
| D-4 | Phase 2 guides same PR as Phase 3? | Separate PRs | Phase 3 has security-sensitive code |

---

## Resolved Decisions

> All decisions resolved interactively 2026-03-09.

| # | Decision | Resolution | Rationale |
|---|----------|------------|-----------|
| D-2 | Phase 1 bug branch strategy | **(b) Separate branches per bug** | Independent fixes, independent review |
| D-3 | #160 hook vs #150 blocker | **(c) Fix #150 first**, then **descope #160 to standalone future ticket** | Build hook on clean foundation after #150 consolidation ships |
| D-5 | EN-001 closure rule | **(a) EN-001 stays open until #150 is done** | Hook consolidation is CI hardening work; belongs under EN-001 |
| D-6 | Fork PR comment strategy for #158 | **(c) Internal-PR-only for Phase 1** | Fork support tracked as #174. Internal PRs are priority; don't extend attack surface prematurely |

---

## Review History

| Date | Reviewer | Strategy | Findings | Status |
|------|----------|----------|----------|--------|
| 2026-03-09 | adv-executor | S-002 Devil's Advocate | 1 Critical, 4 Major, 3 Minor | All addressed in Revision 2 |
| 2026-03-09 | eng-devsecops | Security review (tickets) | 3 HIGH, 4 MEDIUM, 2 LOW, 2 INFO | Incorporated into GH Issues |
| 2026-03-09 | red-recon | Threat assessment (tickets) | 2 HIGH, 3 MEDIUM, 1 LOW | Incorporated into GH Issues |
| 2026-03-09 | adv-scorer | S-014 Quality score (tickets) | 0.75 REVISE | Traceability fixed in GH Issues |
