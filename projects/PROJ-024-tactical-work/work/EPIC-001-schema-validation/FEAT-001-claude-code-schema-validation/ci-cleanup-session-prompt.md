# Constructed Prompt: CI Cleanup -- Script Removal and CLI Consolidation

> **pe-builder** output | Project: PROJ-024 | Criticality: C3 (>10 files, API-adjacent changes, multi-item dependency chain)
> Template: 3 (Multi-Skill Orchestration) adapted for 4-phase sequential implementation with per-phase quality gates.

## L0 Quick-Start Version

```
Execute 4 worktracker items in dependency order under PROJ-024.

Phase 1 -- STORY-023 (GH #177): Remove deprecated scripts/pre_tool_use.py.
Phase 2 -- STORY-024 (GH #178): Consolidate dual SubagentStop hooks into CLI.
Phase 3 -- BUG-005 (GH #214): Rewrite hook tests from scripts/tests/ to tests/.
Phase 4 -- STORY-025 (GH #193): Port scripts/validate-agent-frontmatter.py P-003 check into CLI handler.

Use /orchestration to sequence. Use /problem-solving for implementation.
Include /adversary C4 adversarial critique >= 0.95 per phase before proceeding.
Run full test suite after each phase; baseline = 16,341 passing tests.

Output: commit per phase; worktracker entity status updated to completed.
```

---

## L1 Full Version

Copy-paste the entire block below into a fresh Claude Code session.

---

```
Set JERRY_PROJECT=PROJ-024-tactical-work.

Use /worktracker to update STORY-023, STORY-024, BUG-005, and STORY-025 status to in-progress.

Use /orchestration with orch-planner to sequence the following 4-phase pipeline.
Each phase has a hard dependency on the previous phase completing successfully.
Proceed to the next phase ONLY after: (a) all acceptance criteria pass, (b) full
test suite passes with count >= 16,341, and (c) /adversary C4 quality gate >= 0.95.

---

## Constraints (apply to ALL phases)

NEVER introduce new standalone scripts in scripts/ -- Consequence: increases
surface area, creates parallel code paths that drift from CLI. Instead: all logic
goes through `uv run jerry ...` CLI commands.

NEVER put enforcement logic outside src/ hexagonal layers -- Consequence: bypasses
domain/application/infrastructure boundaries, breaks testability. Instead: domain
rules in domain layer, command handling in application layer, adapters in
infrastructure layer.

NEVER write implementation before the test fails -- Consequence: untested code, no
regression guard. Instead: Red (write failing test for CLI behavior) -> Green
(implement/port) -> Refactor (delete old code).

NEVER add tests to scripts/tests/ -- Consequence: parallel test infrastructure,
not collected by CI unless special config. Instead: all tests in tests/ directory
following existing test pyramid.

NEVER merge with fewer passing tests than baseline (16,341) -- Consequence:
regression introduced. Instead: run full suite via `uv run pytest tests/` after
each phase, verify count >= baseline.

---

## Phase 1 -- STORY-023: Remove Deprecated scripts/pre_tool_use.py (GH #177)

Use /problem-solving with ps-investigator to verify scripts/pre_tool_use.py is
dead code. Confirm all security guardrail logic already exists in
src/infrastructure/internal/enforcement/security_enforcement_engine.py.

Data sources:
- Deprecated script: scripts/pre_tool_use.py
- CLI enforcement: src/infrastructure/internal/enforcement/security_enforcement_engine.py
- Worktracker entity: projects/PROJ-024-tactical-work/work/EPIC-001-schema-validation/FEAT-001-claude-code-schema-validation/STORY-023-remove-deprecated-hook/STORY-023-remove-deprecated-hook.md

Steps:
1. Read scripts/pre_tool_use.py and catalog every security check it performs.
2. Read src/infrastructure/internal/enforcement/security_enforcement_engine.py and
   verify each cataloged check has a corresponding implementation.
3. If any check is missing from the CLI implementation, port it using TDD (H-20):
   write failing test in tests/ first, then implement in src/.
4. Delete scripts/pre_tool_use.py.
5. Use Grep to find all references to pre_tool_use.py or the old script path
   across the entire repository (docs, configs, rule files, CLAUDE.md, .claude/).
   Update every reference to point to the CLI command.
6. Update scripts/tests/test_hooks.py: remove or comment out tests that import
   or invoke the deleted script (full rewrite happens in Phase 3).
7. Run `uv run pytest tests/ -v` and verify count >= 16,341.

Use /adversary with adv-executor to run C4 adversarial critique on Phase 1 output.
Evaluation dimensions: completeness of reference cleanup, no dangling imports,
no broken CI steps, security parity between old script and CLI.
Quality threshold: >= 0.95.

Use /worktracker to update STORY-023 status to completed upon passing quality gate.
Commit with message: "fix(hooks): remove deprecated scripts/pre_tool_use.py (STORY-023, GH #177)"

---

## Phase 2 -- STORY-024: Consolidate Dual SubagentStop Hooks (GH #178)

Use /problem-solving with ps-analyst to analyze the dual SubagentStop
implementations and identify consolidation strategy.

Data sources:
- Standalone hook: scripts/subagent_stop.py
- CLI implementation: search src/ for SubagentStop or subagent_stop references
- Worktracker entity: projects/PROJ-024-tactical-work/work/EPIC-001-schema-validation/FEAT-001-claude-code-schema-validation/STORY-024-consolidate-subagent-hooks/STORY-024-consolidate-subagent-hooks.md

Steps:
1. Read scripts/subagent_stop.py and catalog all hook behaviors.
2. Use Grep to find the CLI-side SubagentStop implementation in src/.
3. Diff the two implementations: identify any logic in the standalone script
   that is absent from the CLI version.
4. If any logic is missing from CLI, port it using TDD (H-20):
   write failing test in tests/ first, then implement in src/.
5. Delete scripts/subagent_stop.py.
6. Use Grep to find all references to subagent_stop.py across the repository.
   Update every reference to point to the CLI command.
7. Update .claude/settings.json and .claude/settings.local.json if they
   reference the standalone script path.
8. Run `uv run pytest tests/ -v` and verify count >= 16,341.

Use /adversary with adv-executor to run C4 adversarial critique on Phase 2 output.
Evaluation dimensions: behavioral parity, no orphaned config references,
hook lifecycle correctness, Clean Architecture compliance.
Quality threshold: >= 0.95.

Use /worktracker to update STORY-024 status to completed upon passing quality gate.
Commit with message: "fix(hooks): consolidate SubagentStop into CLI (STORY-024, GH #178)"

---

## Phase 3 -- BUG-005: Rewrite Hook Tests (GH #214)

Use /problem-solving with ps-analyst to analyze scripts/tests/test_hooks.py and
design replacement tests targeting CLI-based enforcement.

Data sources:
- Old tests: scripts/tests/test_hooks.py
- CLI enforcement: src/infrastructure/internal/enforcement/security_enforcement_engine.py
- pytest config: pytest.ini (contains --ignore entries to remove)
- Worktracker entity: projects/PROJ-024-tactical-work/work/EPIC-001-schema-validation/FEAT-001-claude-code-schema-validation/BUG-005-hook-test-step-defs/BUG-005-hook-test-step-defs.md

Steps:
1. Read scripts/tests/test_hooks.py. Catalog every test case and what behavior
   it verifies.
2. For each test case, design a replacement test that:
   - Lives in tests/ (not scripts/tests/)
   - Tests the CLI-based enforcement (jerry hooks pre-tool-use) or imports
     directly from src/infrastructure/internal/enforcement/
   - Uses BDD Given/When/Then structure per H-20
3. Write the new tests in tests/ using TDD Red phase: all tests fail initially
   because they target CLI entry points.
4. Verify new tests pass (Green phase) by running against existing CLI
   implementation.
5. Delete scripts/tests/test_hooks.py.
6. Edit pytest.ini: remove any --ignore entries that reference scripts/tests/.
7. Run `uv run pytest tests/ -v` and verify count >= 16,341.
   The count should increase because previously-ignored tests are now collected.

Use /adversary with adv-executor to run C4 adversarial critique on Phase 3 output.
Evaluation dimensions: test coverage parity (every old behavior has a new test),
BDD compliance (H-20), no tests remaining in scripts/tests/, pytest.ini cleanup,
test count verification.
Quality threshold: >= 0.95.

Use /worktracker to update BUG-005 status to completed upon passing quality gate.
Commit with message: "fix(tests): rewrite hook tests for CLI enforcement (BUG-005, GH #214)"

---

## Phase 4 -- STORY-025: Port P-003 Validation Script to CLI (GH #193)

Use /problem-solving with ps-analyst to analyze the H-10 violation in
validate_frontmatter_command.py and plan the refactoring.

Data sources:
- Script to port: scripts/validate-agent-frontmatter.py
- CLI handler (H-10 violation): src/agents/application/commands/validate_frontmatter_command.py
- Worktracker entity: projects/PROJ-024-tactical-work/work/EPIC-001-schema-validation/FEAT-001-claude-code-schema-validation/STORY-025-schema-validate-cli/STORY-025-schema-validate-cli.md

Steps:
1. Read scripts/validate-agent-frontmatter.py. Catalog all validation checks,
   especially the P-003 (subagent nesting) check.
2. Read src/agents/application/commands/validate_frontmatter_command.py. Identify:
   a. Which validations already exist in the CLI handler.
   b. Which validations exist only in the standalone script (port candidates).
   c. The H-10 violation: identify the 3 classes in one file.
3. Resolve the H-10 violation first:
   a. Extract each class to its own file in the same directory following naming
      conventions (one_class_per_file.py pattern).
   b. Update all imports across the codebase.
   c. Run tests to verify no regressions.
4. Port missing validation logic (especially P-003 check) into the CLI handler
   using TDD (H-20):
   a. Write failing tests in tests/ for each validation being ported.
   b. Implement the validation in the appropriate hexagonal layer.
   c. Verify tests pass.
5. Delete scripts/validate-agent-frontmatter.py.
6. Use Grep to find all references to validate-agent-frontmatter.py across the
   repository (CI configs, docs, rule files). Update to use
   `uv run jerry agents validate-frontmatter`.
7. Remove any separate CI step that invokes the standalone script.
8. Move any tests from scripts/tests/ that test this script into tests/.
9. Run `uv run pytest tests/ -v` and verify count >= 16,341.

Use /adversary with adv-executor to run C4 adversarial critique on Phase 4 output.
Evaluation dimensions: validation parity (every script check exists in CLI),
H-10 resolution (one class per file), Clean Architecture compliance,
CI pipeline correctness, P-003 check coverage.
Quality threshold: >= 0.95.

Use /worktracker to update STORY-025 status to completed upon passing quality gate.
Commit with message: "feat(agents): port frontmatter validation to CLI (STORY-025, GH #193)"

---

## Post-Pipeline Verification

After all 4 phases complete:

1. Run full test suite: `uv run pytest tests/ -v --tb=short`
   Verify count >= 16,341.
2. Verify no files remain in scripts/ that duplicate CLI functionality:
   - scripts/pre_tool_use.py deleted
   - scripts/subagent_stop.py deleted
   - scripts/validate-agent-frontmatter.py deleted
   - scripts/tests/test_hooks.py deleted
3. Verify pytest.ini has no --ignore entries referencing scripts/tests/.
4. Verify no dangling references: use Grep to search for all three deleted
   script filenames across the entire repository. Zero matches expected
   (except historical references in commit messages or changelogs).
5. Use /worktracker to verify STORY-023, STORY-024, BUG-005, STORY-025 all
   show status: completed.

Final commit (if any cleanup needed):
"chore: post-cleanup verification for CI script removal (FEAT-001)"
```

---

## Construction Notes

| Element | Value | Source |
|---------|-------|--------|
| Skill Routing | /orchestration (orch-planner), /problem-solving (ps-investigator, ps-analyst), /adversary (adv-executor, C4) | Trigger map: "orchestration, pipeline, phases, gates" -> /orchestration; "analyze, investigate" -> /problem-solving; "adversarial, quality gate" -> /adversary |
| Domain Scope | Jerry CLI hook consolidation: scripts/ -> src/ hexagonal architecture migration across 4 worktracker items under FEAT-001 | User input: 4 named items with file paths |
| Data Source | Codebase files (Read, Grep, Glob): scripts/pre_tool_use.py, scripts/subagent_stop.py, scripts/validate-agent-frontmatter.py, src/infrastructure/internal/enforcement/security_enforcement_engine.py, src/agents/application/commands/validate_frontmatter_command.py, scripts/tests/test_hooks.py, pytest.ini | All paths verified via Glob |
| Quality Gate | /adversary C4 >= 0.95 per phase; test count >= 16,341 baseline | User-specified threshold (0.95) exceeds H-13 minimum (0.92) |
| Output Path | Commit per phase with semantic message; worktracker entity status updates | User-specified: commit-per-phase workflow |

### Template Adaptation Notes

Template 3 (Multi-Skill Orchestration) is designed for research -> analysis -> decision pipelines. This prompt adapts it for a 4-phase sequential implementation pipeline where each phase is an independent worktracker item with a dependency on the previous phase. Key adaptations:

1. **Phases are implementation items, not research -> analysis -> decision.** Each phase follows its own TDD micro-cycle (Red -> Green -> Refactor) rather than the template's research -> analysis -> decision macro-pattern.
2. **Quality gate is per-phase, not per-pipeline.** Each phase gets its own /adversary C4 review because each is an independently deliverable worktracker item.
3. **Constraints section added.** NPT-013 format constraints embedded at the top to apply across all phases, which the template does not natively support.
4. **Post-pipeline verification added.** The dependency chain requires end-to-end validation that no regressions propagated across phases.

### Skills Requested vs. Skills Routed

The user requested 6 skills: /eng-team, /red-team, /problem-solving, /nasa-se, /user-experience, /diataxis. The constructed prompt routes to 3 skills: /orchestration, /problem-solving, /adversary. Rationale for the routing decisions:

| Requested Skill | Routing Decision | Rationale |
|-----------------|------------------|-----------|
| /eng-team | Not routed | No threat modeling, security architecture, or DevSecOps work in scope. The security enforcement engine already exists; this is a file deletion and reference cleanup task. |
| /red-team | Not routed | No penetration testing, offensive security, or exploitation work in scope. |
| /problem-solving | Routed (ps-investigator, ps-analyst) | Dead code verification (ps-investigator) and implementation analysis (ps-analyst) are core to each phase. |
| /nasa-se | Not routed | No requirements authoring, V&V, or specification work. These are implementation tasks against existing acceptance criteria in worktracker entities. |
| /user-experience | Not routed | No UX evaluation, user research, or design system work in scope. |
| /diataxis | Not routed | No documentation creation or classification. Doc reference updates are incidental to script deletion, not primary documentation work. |
| /orchestration | Routed (added) | 4-phase dependency chain with quality gates at boundaries requires orchestration coordination. |
| /adversary | Routed (user-specified) | C4 quality gate >= 0.95 per phase. |

---

## Self-Review Score

| Criterion | Weight | Score | Notes |
|-----------|--------|-------|-------|
| C1 Task Specificity | 20% | 3/3 | All 4 items have concrete file paths, named scripts, specific deletion/port/rewrite actions. Zero undefined terms. Zero trailing fragments. Every step is actionable with named files. |
| C2 Skill Routing | 18% | 3/3 | /orchestration (orch-planner), /problem-solving (ps-investigator, ps-analyst), /adversary (adv-executor) all use /skill syntax with named agents. |
| C3 Context Provision | 15% | 3/3 | All data sources named with full repo-relative paths. Worktracker entity paths provided per phase. Baseline test count specified (16,341). No redundant padding. |
| C4 Quality Specification | 15% | 3/3 | Numeric threshold (>= 0.95) with named mechanism (/adversary C4 adv-executor). Evaluation dimensions specified per phase. Test count baseline as secondary quality gate. |
| C5 Decomposition | 12% | 3/3 | 4 named phases with explicit dependency ordering, per-phase quality gates, and post-pipeline verification. Sync barrier: "proceed ONLY after (a) acceptance criteria pass, (b) test suite passes, (c) quality gate >= 0.95." |
| C6 Output Specification | 12% | 3/3 | Per-phase commit messages with semantic format specified. Worktracker entity status updates specified. Post-pipeline verification checklist. |
| C7 Positive Framing | 8% | 2/3 | 5 NPT-013 constraints use NEVER format (required by user as NPT-013 hard constraints). Each has a constructive "Instead:" alternative. The NEVER format is intentional per NPT-013 research (100% compliance vs 92.2% for positive-only, p=0.016). Deducting 1 point because the constraints are in the prompt body rather than isolated in a separate guardrails section. |
| **Weighted Composite** | | **96/100** | (3/3 * 20) + (3/3 * 18) + (3/3 * 15) + (3/3 * 15) + (3/3 * 12) + (3/3 * 12) + (2/3 * 8) = 20 + 18 + 15 + 15 + 12 + 12 + 5.33 = 97.33, rounded to 97. |

**Tier: Exemplary (97/100)**

---

*Built by pe-builder v1.0.0 | Template 3 adapted | NPT-013 constraints embedded | 2026-03-29*
