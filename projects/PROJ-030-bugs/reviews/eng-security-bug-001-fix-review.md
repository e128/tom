# Security Code Review: BUG-001 Memory-Keeper Tool Name Fix

<!-- Reviewer: eng-security | Date: 2026-03-09 | Scope: BUG-001 fix across 26 active governance files -->

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0 Executive Summary](#l0-executive-summary) | Finding counts, assessment, immediate actions |
| [L1 Technical Findings](#l1-technical-findings) | Individual findings with evidence and remediation |
| [L2 Strategic Implications](#l2-strategic-implications) | Systemic patterns and architectural assessment |
| [ASVS Verification](#asvs-verification) | Relevant ASVS 5.0 chapter checks |
| [Review Scope](#review-scope) | Files examined, methodology |

---

## L0 Executive Summary

| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 0 |
| Medium | 1 |
| Low | 2 |
| Info | 2 |

**Overall Security Assessment:** PASS WITH CONDITIONS. The BUG-001 fix is structurally sound. The new tool names are correctly aligned with the actual MCP server API. No permission surface expansion was introduced. No dangerous operations were exposed to agents that previously lacked them. Two low-severity findings require remediation; one medium finding requires attention before the fix branch is merged.

**Top 3 Risk Areas:**

1. `context_batch_delete` carries a semantically destructive name but is correctly restricted to administrative use only -- no agent is granted this tool in any active governance file. The wildcard in `settings.local.json` theoretically covers it at the runtime level, which is the medium finding.
2. Seventeen files in the `projects/` directory tree retain the old incorrect tool names. These are historical research and review artifacts, not executed governance files. However, they will mislead future readers and any tooling that scans for tool-name correctness.
3. The TOOL_REGISTRY.yaml `metrics.total_tools` counter is stale at 18 (comment says "14 core + 2 Context7 + 5 Memory-Keeper") when the actual count of defined MCP tools is 7 (2 Context7 + 5 Memory-Keeper). This is a documentation accuracy issue, not a security issue.

**Recommended Immediate Actions:**

1. (Medium) Scope the `mcp__memory-keeper__*` wildcard in `.claude/settings.local.json` by removing it or adding it only as a fallback comment. The five explicit named entries already cover all legitimate tool access. The wildcard grants runtime permission for any future Memory-Keeper tool name without a corresponding governance review.
2. (Low) Add a `[HISTORICAL - PRE-BUG-001-FIX]` banner to the 17 project artifact files that still reference old tool names, or exclude the `projects/` directory from any future tool-name linting CI gate.
3. (Low) Correct the `metrics.total_tools` value in TOOL_REGISTRY.yaml from 18 to the accurate count.

---

## L1 Technical Findings

### Finding F-001 (Medium): Wildcard MCP Permission Expands Future Surface Beyond Governance Review

**CWE:** CWE-732 -- Incorrect Permission Assignment for Critical Resource
**CVSS 3.1 Base Score:** 4.3 (AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N)
**Affected File:** `.claude/settings.local.json`, lines 18 and 24

**Data Flow Trace:**
The `permissions.allow` array in `settings.local.json` contains both a wildcard entry (`mcp__memory-keeper__*`) and five explicit named entries for the same namespace. The wildcard entry was present before the BUG-001 fix and was not removed during the fix. At runtime, Claude Code uses this file to evaluate what tool invocations are permitted. Any new tool added to the Memory-Keeper MCP server in the future -- including destructive operations -- will be silently permitted at the runtime layer without requiring a governance update to `settings.local.json`.

**Evidence:**
```json
"mcp__memory-keeper__*",
"mcp__memory-keeper__context_save",
"mcp__memory-keeper__context_get",
"mcp__memory-keeper__context_session_list",
"mcp__memory-keeper__context_batch_delete",
"mcp__memory-keeper__context_search",
```

The wildcard on line 18 makes lines 19-23 redundant and also grants permission to hypothetical future tools (e.g., `mcp__memory-keeper__context_purge_all`) without any agent-level governance file update being required first.

**Threat Model Correlation:** This matches the AP-07 Tool Overload Creep anti-pattern from `agent-routing-standards.md` -- tools accumulate without per-agent allowlist review. The risk is lower here because the individual agent `.md` files and TOOL_REGISTRY.yaml correctly enumerate only the specific tools each agent is permitted. The wildcard operates at the session-level permission layer, one tier above agent-level enforcement.

**Remediation:**
Remove the wildcard line (`"mcp__memory-keeper__*"`) from `settings.local.json`. The five explicit named entries provide complete coverage for all currently defined Memory-Keeper tools assigned to any agent. Future tools should be added explicitly after agent-level governance review.

Alternatively, if the wildcard is intentional as a fallback for tool discovery during development, add a comment making this explicit and file a worktracker item to remove it before production use.

---

### Finding F-002 (Low): 17 Historical Project Artifacts Retain Pre-Fix Tool Names

**CWE:** CWE-1059 -- Incomplete Documentation
**Affected Files:** 17 files under `projects/PROJ-007-agent-patterns/`, `projects/PROJ-022-user-experience-skill/`, `projects/PROJ-008-agentic-security/`, `projects/PROJ-001-oss-release/`, `projects/PROJ-030-bugs/`

**Evidence:** Grep for `mcp__memory-keeper__(store|retrieve|search|list|delete)` returns 17 files, all located under the `projects/` directory tree. None are in `skills/`, `.context/`, `.claude/`, or the root governance files. All occurrences are in research notes, adversarial review artifacts, and audit records generated before BUG-001 was identified.

Key files:
- `projects/PROJ-030-bugs/research/memory-keeper-tool-name-audit.md` -- correctly documents the old-vs-new mapping as part of the bug research; old names are cited intentionally as the bug subject
- `projects/PROJ-022-user-experience-skill/reviews/adv-executor-s007-skill-md-003.md` -- review artifact proposing (incorrectly) to add `mcp__memory-keeper__store/retrieve/search` to ux-orchestrator; proposal was superseded by the BUG-001 fix
- `projects/PROJ-007-agent-patterns/orchestration/.../ps-architect-001-adr-agent-design.md` -- correctly identifies the mismatch as a violation in its schema validation analysis

**Security Implication:** No runtime security impact. These files are not parsed by any agent at execution time. The risk is operational: a future developer reading these artifacts might extract the old tool names and use them in a new agent definition, reintroducing the bug. Additionally, if a CI linting rule is added to scan for correct tool names, these files will produce false positives unless excluded.

**Remediation:**
Option A (preferred): Add a `[HISTORICAL - PRE-BUG-001-FIX]` notice at the top of each affected file, or add a `.toolname-lint-ignore` marker.
Option B: Exclude the `projects/` directory from any future tool-name correctness CI gate via a `.lintignore` configuration.
Option C: Accept as-is given the files are non-executable historical artifacts and the risk is limited to developer confusion.

---

### Finding F-003 (Low): TOOL_REGISTRY.yaml Metrics Counter Is Stale

**CWE:** CWE-1059 -- Incomplete Documentation
**Affected File:** `TOOL_REGISTRY.yaml`, line 797

**Evidence:**
```yaml
metrics:
  total_tools: 18  # 14 core + 2 Context7 + 5 Memory-Keeper (individual tools counted)
```

The comment says "14 core + 2 Context7 + 5 Memory-Keeper" which totals 21, not 18. The actual count of individually named tools in the `tools:` section is: 5 core filesystem tools (Read, Write, Edit, Glob, Grep) + 1 execution (Bash) + 3 orchestration (Task, TodoWrite, AskUserQuestion) + 2 web (WebSearch, WebFetch) + 2 Context7 + 5 Memory-Keeper = 18. The comment arithmetic is wrong but the number 18 is defensible by a different counting scheme. Either way, the comment is misleading and was not updated during the BUG-001 fix even though the Memory-Keeper tool names changed.

**Security Implication:** None directly. Stale metrics in the registry reduce confidence in the registry as a reliable source of truth for auditing purposes.

**Remediation:** Correct the comment to match the actual count, or remove the breakdown comment and retain only the total. Suggested: `total_tools: 18  # 5 filesystem + 1 execution + 3 orchestration + 2 web + 2 Context7 + 5 Memory-Keeper`

---

### Finding F-004 (Info): context_batch_delete Name Implies Batch Scope -- No Agent Assignment Confirmed

**Affected File:** `TOOL_REGISTRY.yaml` line 288, `mcp-tool-standards.md` line 117

**Observation:** The tool `mcp__memory-keeper__context_batch_delete` replaces `mcp__memory-keeper__delete`. The `batch_` prefix implies the operation accepts multiple keys or a key pattern (confirmed by TOOL_REGISTRY.yaml description: "Delete stored context by key" and BUG-001 research noting it uses `keys` array or `keyPattern` glob syntax). This is a more powerful deletion capability than the predecessor's implied single-key delete.

**Verification Result:** No agent in any active governance file (`skills/*/agents/*.md`, TOOL_REGISTRY.yaml `agent_permissions`, `skills/*/SKILL.md`) is granted `context_batch_delete` or `context_session_list`. Both tools are documented in `mcp-tool-standards.md` as "reserved for administrative use." This is correct and consistent.

**Residual Risk:** The wildcard in `settings.local.json` (F-001) technically permits `context_batch_delete` at the session level. If any agent were to reference this tool name in a prompt despite not having it in their declared `allowed_tools`, the session-level permission would not block it. Agent-level enforcement via the `tools` frontmatter field in `.md` files is the primary control; the session-level wildcard is a compensating gap (covered under F-001).

**Action:** No additional action beyond F-001 remediation required.

---

### Finding F-005 (Info): mcp-tool-standards.md L2-REINJECT Tag Uses Correct New Names

**Affected File:** `.context/rules/mcp-tool-standards.md`, line 7

**Observation:** The L2-REINJECT comment block at the top of `mcp-tool-standards.md` was updated correctly:

```
Memory-Keeper REQUIRED at phase boundaries: phase-complete→context_save, phase-start→context_get.
```

This is the per-prompt re-injection payload that reaches every agent context. It was one of the highest-priority targets for the fix and it is correctly updated. The MCP-002 rule body at line 31 is also correctly updated with `context_save`, `context_get`, and `context_search`.

**Action:** None. Confirmed correct.

---

## L2 Strategic Implications

### Security Posture Assessment

The BUG-001 fix is executed correctly across all active governance files. The threat model for this fix is narrow -- incorrect tool names cause agent failures (operational risk) rather than security vulnerabilities (the old names simply would not resolve against the MCP server). The fix correctly prioritized the active governance files over historical project artifacts.

The permission model for Memory-Keeper tools follows a layered architecture: TOOL_REGISTRY.yaml defines which agents may use which tools (machine-readable governance), individual agent `.md` frontmatter enforces tool access at the agent level, and `settings.local.json` provides session-level allow-listing. The fix maintained this layered structure correctly.

### Systemic Pattern: Wildcard-Plus-Explicit Redundancy

The presence of both `mcp__memory-keeper__*` and five explicit tool names in `settings.local.json` is a pattern that suggests the wildcard was added during initial setup (before the explicit names were known) and was never cleaned up. This is a common drift pattern in permission files. The fix correctly added the new explicit names but did not remove the now-redundant wildcard. Going forward, a policy of "explicit names only, no wildcards" for MCP tool permissions in `settings.local.json` would eliminate this class of drift.

### Comparison With Threat Model Predictions

The BUG-001 research (`projects/PROJ-030-bugs/research/memory-keeper-tool-name-audit.md`) correctly identified all affected files. The fix coverage appears complete for active governance files. The historical artifact residue (F-002) was anticipated in the research but not addressed in the fix -- this is acceptable given the non-executable nature of those files.

### Recommendations for Security Architecture Evolution

1. Add a CI gate that validates tool names in `skills/*/agents/*.md` and `TOOL_REGISTRY.yaml` against a canonical list sourced from `mcp-tool-standards.md` [Canonical Tool Names]. This would have caught BUG-001 at the PR boundary rather than requiring a dedicated bug project.
2. Enforce a "no wildcards in MCP tool permissions" policy in `settings.local.json` via documentation in `mcp-tool-standards.md` MEDIUM Standards.
3. Consider adding a schema validation rule that cross-checks `TOOL_REGISTRY.yaml` `agent_permissions` against the `tools` frontmatter declarations in corresponding `.md` files -- this would detect drift between the two representations of the same permission grant.

---

## ASVS Verification

Relevant ASVS 5.0 chapters for this review scope (MCP tool name configuration, permission file governance):

| Chapter | Requirement Area | Status | Notes |
|---------|-----------------|--------|-------|
| V1 (Architecture) | V1.2 -- Authentication architecture; privilege separation | PASS | Tool-tier model (T1-T5) correctly separates privileges |
| V4 (Access Control) | V4.1 -- General access control design | PASS WITH FINDING | Agent-level toolset restrictions are correctly declared. Session-level wildcard (F-001) is an access control gap at the permission boundary layer |
| V4 (Access Control) | V4.2 -- Operation-level access control | PASS | `context_batch_delete` and `context_session_list` correctly excluded from all agent tool grants |
| V7 (Error Handling) | V7.4 -- Error handling | PASS | Fallback behavior for MCP failure documented in `mcp-tool-standards.md` Error Handling section |
| V8 (Data Protection) | V8.1 -- General data protection | INFO | Memory-Keeper stores cross-session context; no credential storage patterns identified in agent governance |

---

## Review Scope

**Files Examined:**
- `/Users/adam.nowak/workspace/GitHub/geekatron/jerry-wt/fix/proj-030-bugs/.context/rules/mcp-tool-standards.md` (SSOT)
- `/Users/adam.nowak/workspace/GitHub/geekatron/jerry-wt/fix/proj-030-bugs/TOOL_REGISTRY.yaml` (full file)
- `/Users/adam.nowak/workspace/GitHub/geekatron/jerry-wt/fix/proj-030-bugs/.claude/settings.local.json`
- `/Users/adam.nowak/workspace/GitHub/geekatron/jerry-wt/fix/proj-030-bugs/skills/user-experience/agents/ux-orchestrator.governance.yaml`
- `/Users/adam.nowak/workspace/GitHub/geekatron/jerry-wt/fix/proj-030-bugs/skills/user-experience/rules/mcp-coordination.md`
- All `skills/*/agents/*.md` and `skills/*/SKILL.md` files via grep (memory-keeper tool name pattern)
- `AGENTS.md` (no memory-keeper references found)

**Methodology:**
1. Scope definition: active governance files vs. historical project artifacts
2. Grep-based data flow tracing for both old tool names (`store|retrieve|search|list|delete`) and new tool names (`context_save|context_get|context_search|context_session_list|context_batch_delete`)
3. Permission surface analysis: wildcard vs. explicit entries in `settings.local.json`
4. Cross-reference of TOOL_REGISTRY.yaml `agent_permissions` against SKILL.md frontmatter declarations
5. ASVS V4 access control verification for `context_batch_delete` assignment

**Confidence Level:** High (0.90). All active governance files examined directly. Historical artifact residue identified but not individually reviewed for context -- classified as low risk based on file path patterns and directory location.

---

*Reviewer: eng-security*
*Review Date: 2026-03-09*
*Branch: fix/proj-030-bugs*
*Standards: CWE Top 25 2025, OWASP ASVS 5.0, CVSS 3.1*
*SSDF Practice: PW.7 (human-readable code review)*
