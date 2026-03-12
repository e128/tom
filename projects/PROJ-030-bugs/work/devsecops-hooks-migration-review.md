# DevSecOps Finding Report: hooks.json #150 Migration Review

**Date:** 2026-03-10
**Reviewer:** eng-devsecops
**Scope:** hooks.json migration (PreToolUse consolidation), pre-tool-use.py wrapper, scripts/pre_tool_use.py deprecation

---

## L0 Executive Summary

| Category | Status | Severity |
|----------|--------|----------|
| hooks.json migration correctness | FINDING | Medium |
| Wrapper fail-open and I/O propagation | PASS | -- |
| Deployment risk window | FINDING | Low |
| Tool matcher coverage (NotebookEdit) | FINDING | Medium |

**Critical blockers:** None. All three findings are correctness gaps rather than blocking security failures, because the pipeline is fail-open throughout. However, the NotebookEdit gap is a real enforcement hole for a tool that writes file content.

---

## L1 Technical Findings

### F-001 -- hooks.json matcher does not cover NotebookEdit (Medium)

**Location:** `hooks/hooks.json` line 40

```
"matcher": "Write|Edit|MultiEdit|Bash"
```

**Finding:** `NotebookEdit` is absent from the hooks.json matcher. Claude Code will not invoke the PreToolUse hook at all for `NotebookEdit` calls, meaning the SecurityEnforcementEngine and PreToolEnforcementEngine are bypassed entirely for notebook writes.

**Evidence from the codebase:**

The handler internals already account for `NotebookEdit`:

- `hooks_pre_tool_use_handler.py` line 52: `_WRITE_TOOLS = frozenset({"Write", "MultiEdit", "NotebookEdit"})`
- `hooks_pre_tool_use_handler.py` line 58: `_FILE_TARGET_TOOLS = frozenset({"Write", "Edit", "Read", "NotebookEdit"})`
- `security_enforcement_engine.py` line 30: `_WRITE_TOOLS = frozenset({"Write", "Edit", "MultiEdit", "NotebookEdit"})`

All three internal sets handle NotebookEdit. The hooks.json matcher is the entry gate -- if it does not match, the hook process is never spawned and the handler code never executes.

**Impact:** An agent could use `NotebookEdit` to write to blocked paths (e.g., `~/.ssh/`, `.env`) without triggering any security check.

**Remediation:** Add `NotebookEdit` to the matcher:

```json
"matcher": "Write|Edit|MultiEdit|NotebookEdit|Bash"
```

---

### F-002 -- SecurityEnforcementEngine initialization failure is fail-open, not fail-closed (Low)

**Location:** `hooks/pre-tool-use.py` lines 37-41 and `src/bootstrap.py` lines 649-662

**Finding:** The wrapper's outer `except Exception: pass` block (line 37-41) catches any failure during `uv run jerry hooks pre-tool-use` including CLI initialization errors. If `PatternLibraryAdapter` or `SecurityEnforcementEngine` construction raises an exception inside the CLI process, the CLI exits non-zero (line 32-36 in the wrapper logs it to stderr), but the wrapper then unconditionally calls `sys.exit(0)` at line 41.

The result: any bootstrap failure silently allows the tool call through. This is the stated design ("fail-open"), but there is an asymmetry worth documenting: bootstrap failures are silent to the user because the wrapper discards the non-zero exit code.

**Relevant flow:**

```
bootstrap.create_hooks_handlers()
  -> PatternLibraryAdapter(patterns_path=project_root / "scripts" / "patterns" / "patterns.yaml")
```

If `patterns.yaml` is missing, `PatternLibraryAdapter.__init__` may raise. The `SecurityEnforcementEngine.evaluate()` has an inner `try/except` that returns `_APPROVE` on exceptions (line 79-82 in `security_enforcement_engine.py`), but that guard only applies after the engine is constructed. A construction-time failure in the bootstrap exits the CLI process before the handler runs.

**The wrapper at line 32-36 does log the non-zero exit code to stderr**, which is good. But stderr from hooks is typically not surfaced to the operator in normal Claude Code sessions.

**Remediation (Low priority):** This is an accepted fail-open design. Document the risk explicitly in ADR-150-001 and add a startup self-test that verifies `patterns.yaml` exists at deploy time. No code change required for correctness.

---

### F-003 -- Deployment risk window is zero, but rollback restores old gap (Info)

**Location:** `hooks/hooks.json` (the commit boundary)

**Finding:** The hooks.json change is atomic in a single commit, so there is no partial-deployment window where both the old standalone script entry and the new CLI path are absent simultaneously. Claude Code reads hooks.json fresh on each session start, so the transition is clean.

However, the deprecated `scripts/pre_tool_use.py` is no longer registered in hooks.json. If the migration is rolled back by reverting only hooks.json (not the code), the rollback reintroduces the old standalone script. If the migration is rolled back by reverting both, the SecurityEnforcementEngine checks are lost (they were not in the old script). There is no dual-running period to detect regressions before the old path is removed.

**Remediation:** The DEPRECATED header in `scripts/pre_tool_use.py` is correct and sufficient. Recommend a one-session parallel run test before merging (run both paths manually against a sample PreToolUse payload and compare outputs) before the cleanup PR deletes the old file.

---

## L2 Strategic Implications

### Wrapper design assessment

The wrapper (`hooks/pre-tool-use.py`) is well-structured. Key properties verified:

| Property | Assessment |
|----------|-----------|
| Fail-open on exception | CONFIRMED -- line 37-41 catch block, sys.exit(0) unconditional |
| stdout propagation | CONFIRMED -- `result.stdout` written to `sys.stdout.buffer` (line 27) |
| stderr propagation | CONFIRMED -- `result.stderr` written to `sys.stderr.buffer` when non-empty (lines 28-29) |
| Non-zero exit code handling | CONFIRMED -- logged to stderr (lines 32-36), but wrapper still exits 0 |
| stdin forwarding | CONFIRMED -- `sys.stdin.buffer.read()` passed as subprocess input (line 23) |
| Timeout budget | CONFIRMED -- subprocess timeout 4s < hooks.json timeout 5s; 1s buffer is appropriate |

The one design note: the wrapper always exits 0 regardless of the CLI's exit code. This is intentional fail-open, but it means a blocking decision from the CLI (exit code that signals block) would only take effect if expressed through stdout JSON (`{"decision": "block", ...}`), which is the correct Claude Code hook protocol. Confirmed that the handler returns exit 0 always (line 196 in `hooks_pre_tool_use_handler.py`), so the wrapper's unconditional exit 0 is consistent with the handler's behavior.

### Tool coverage gap summary

The internal code handles a superset of what the hooks.json matcher activates:

| Tool | hooks.json matcher | SecurityEngine | PreToolEngine | StalenessDetector |
|------|--------------------|---------------|---------------|-------------------|
| Write | YES | YES | YES (evaluate_write) | YES |
| Edit | YES | YES | YES (evaluate_edit) | YES |
| MultiEdit | YES | YES | NO (not in _EDIT_TOOLS, falls through to None) | NO (no file_path key) |
| NotebookEdit | **NO** | YES (coded) | YES (coded, evaluate_write) | YES (coded) |
| Bash | YES | YES (_BASH_TOOLS) | NO (returns None) | NO |

`MultiEdit` note: `_EDIT_TOOLS = frozenset({"Edit"})` in the handler, so `MultiEdit` runs security checks but not architecture enforcement. This may be intentional (MultiEdit uses `edits` list, not a single `old_string`/`new_string`), but it should be confirmed.

### Recommendation priority

| Priority | Action |
|----------|--------|
| P1 | Add `NotebookEdit` to hooks.json matcher (F-001) |
| P2 | Confirm MultiEdit architecture enforcement gap is intentional |
| P3 | Add `patterns.yaml` existence check to deploy/CI validation (F-002) |
| P4 | Run parallel output comparison before deleting scripts/pre_tool_use.py (F-003) |
