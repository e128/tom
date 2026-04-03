# MCP Tool Standards

<!-- VERSION: 2.0.0 | DATE: 2026-04-03 | REVISION: Remove Memory-Keeper (never implemented). Simplify to Context7 only. -->

> Governance rules for proactive MCP tool usage across Tom Framework agents.

<!-- L2-REINJECT: rank=9, content="Context7 REQUIRED for external library/framework docs: resolve-library-id then query-docs; respect tool-enforced call limit. Fall back to WebSearch if Context7 returns no results." -->

## Document Sections

| Section | Purpose |
|---------|---------|
| [HARD Rules](#hard-rules) | Non-overridable MCP usage constraints |
| [MEDIUM Standards](#medium-standards) | Overridable with documented justification |
| [Context7 Integration](#context7-integration) | When and how to use Context7 docs lookup |
| [Canonical Tool Names](#canonical-tool-names) | Authoritative MCP tool identifiers |
| [Agent Integration Matrix](#agent-integration-matrix) | Which agents use Context7 |
| [Error Handling](#error-handling) | Fallback behavior for MCP failures |
| [References](#references) | Source document traceability |

---

## HARD Rules

> These rules CANNOT be overridden. Violations will be blocked.

| ID | Rule | Source | Consequence |
|----|------|--------|-------------|
| MCP-001 | Context7 MUST be used when any agent task references an external library, framework, SDK, or API by name. Respect the per-question call limit enforced by the tool. WebSearch is permitted only for general concepts or when Context7 returns no results. | FEAT-028 AC-1 | Research quality degradation. Stale training-data knowledge used instead of current docs. |

> **Namespace:** MCP-001 uses a file-scoped `MCP-` prefix (not the global `H-` series in `quality-enforcement.md`). Scoped to MCP tool governance only.

---

## MEDIUM Standards

> Override requires documented justification.

| ID | Standard | Guidance |
|----|----------|----------|
| MCP-M-002 | New agents SHOULD declare MCP tool usage in their agent definition file's `tools` YAML frontmatter. Research/documentation agents SHOULD use Context7. | Follow existing agent patterns in `skills/*/agents/*.md`. |

---

## Context7 Integration

**Protocol:**
1. Call `mcp__context7__resolve-library-id` with library name and research question
2. Call `mcp__context7__query-docs` with resolved library ID and specific query
3. Respect the per-question call limit enforced by the tool; each distinct library resets the limit
4. If `resolve-library-id` returns no matches, fall back to WebSearch for that library

**Triggers:** Task mentions any external package, library, SDK, or framework by name.

| Scenario | Use Context7? | Alternative |
|----------|---------------|-------------|
| Library API docs | **YES** | — |
| Framework patterns | **YES** | — |
| SDK usage examples | **YES** | — |
| General concepts | No | WebSearch |
| Codebase-internal questions | No | Read/Grep |
| Context7 returns no results | No | WebSearch |

---

## Canonical Tool Names

> Authoritative tool names for agent definitions.

| Tool | Canonical Name | Purpose |
|------|---------------|---------|
| Context7 Resolve | `mcp__context7__resolve-library-id` | Resolve package to library ID |
| Context7 Query | `mcp__context7__query-docs` | Query library documentation |

---

## Agent Integration Matrix

> Summary of which agents use Context7.

| Agent | Context7 | Rationale |
|-------|----------|-----------|
| ps-researcher | resolve, query | Library/framework research |
| ps-analyst | resolve, query | API documentation lookup |
| ps-architect | resolve, query | Architecture research |
| ps-investigator | resolve, query | Debugging with library docs |
| ps-synthesizer | resolve, query | Cross-source synthesis |
| nse-explorer | resolve, query | Trade study research |
| nse-architecture | resolve, query | Architecture standards research |
| eng-architect | resolve, query | Library/framework security research |
| eng-lead | resolve, query | Standards and dependency research |
| eng-backend | resolve, query | Backend framework security docs |
| eng-frontend | resolve, query | Frontend framework security docs |
| eng-infra | resolve, query | Infrastructure and container docs |
| eng-devsecops | resolve, query | Security tooling documentation |
| eng-qa | resolve, query | Testing framework documentation |
| eng-security | resolve, query | Security standard documentation |
| eng-reviewer | resolve, query | Standards verification research |
| eng-incident | resolve, query | IR framework documentation |
| pm-customer-insight | resolve, query | Customer research documentation |
| pm-market-strategist | resolve, query | Market strategy framework docs |
| pm-competitive-analyst | resolve, query | Competitive analysis methodology |
| red-lead | resolve, query | Methodology framework research |
| red-recon | resolve, query | Reconnaissance tool documentation |
| red-vuln | resolve, query | Vulnerability database research |
| red-exploit | resolve, query | Exploitation framework docs |
| red-privesc | resolve, query | OS and AD documentation |
| red-lateral | resolve, query | Network protocol documentation |
| red-persist | resolve, query | OS internals documentation |
| red-exfil | resolve, query | Protocol and channel documentation |
| red-reporter | resolve, query | Reporting framework docs |
| red-infra | resolve, query | C2 framework documentation |
| red-social | resolve, query | Social engineering methodology |
| adv-executor | resolve, query | Fact verification during adversarial strategy execution |
| ux-orchestrator | resolve, query | UX methodology and framework documentation |
| ux-atomic-architect | resolve, query | Component library documentation |
| ux-heart-analyst | resolve, query | HEART/GSM framework documentation |
| ux-heuristic-evaluator | resolve, query | External UX standards and Nielsen documentation |
| ux-inclusive-evaluator | resolve, query | WCAG specifications, ARIA authoring practices |
| ux-jtbd-analyst | resolve, query | JTBD framework documentation |
| ux-kano-analyst | resolve, query | Kano model methodology |
| ux-lean-ux-facilitator | resolve, query | Lean UX methodology |

**Not Context7 (by design):**
- **adv-scorer, adv-selector** — Scoring/selection is self-contained; no external research
- **wt-*** — Read-only auditing of worktracker files
- **ps-critic, ps-validator, ps-reviewer** — Quality evaluation; no external library research
- **ps-reporter** — Report generation from existing data
- **nse-requirements, orch-\*, ts-\*** — Internal coordination; no external library docs needed
- **ux-ai-design-guide, ux-sprint-facilitator, ux-behavior-diagnostician** — WebSearch/WebFetch only
- **pm-product-strategist, pm-business-analyst** — WebSearch/WebFetch only

> **Classification rule for new agents:** See MCP-M-002 in [MEDIUM Standards](#medium-standards).

---

## Error Handling

| Failure | Fallback |
|---------|----------|
| Context7 `resolve-library-id` returns no matches | Fall back to WebSearch for that library |
| Context7 `query-docs` returns empty or irrelevant | Use WebSearch; note "Context7 no coverage" in output |
| Context7 tool-enforced call limit reached | Fall back to WebSearch for remaining queries |
| MCP server unavailable | Continue work without MCP tools; log gap in session worktracker entry |

---

## Permission Syntax

For Claude Code permission patterns (MCP wildcards, skill permissions, Bash patterns, file access, evaluation order, settings scope), see `docs/reference/claude-code-permissions.md`.

### MCP Server Namespace Note

Context7 registers under two server names depending on installation method:
- **`mcp__context7__*`** — direct MCP server configuration (via `.mcp.json` or CLI)
- **`mcp__plugin_context7_context7__*`** — plugin-registered form (via `enabledPlugins` in `.claude/settings.json`)

Both wildcards are in `settings.local.json` to cover both registration paths.

### Permission Mode

Neither `settings.json` nor `settings.local.json` sets `defaultMode`. Claude Code defaults to `"default"` mode. The `Skill()` entries in `settings.local.json` pre-approve skill invocations so they don't prompt.

---

## References

| Source | Content |
|--------|---------|
| FEAT-028-mcp-tool-integration (AC-1) | Feature entity; AC-1 mandates Context7 governance |
| `quality-enforcement.md` | Quality gate thresholds and enforcement architecture |
| `docs/reference/claude-code-permissions.md` | Claude Code permission syntax reference |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-04-03 | Remove Memory-Keeper (MCP server was never registered or implemented). Retire MCP-002 (Memory-Keeper at phase boundaries). Retire MCP-M-001 (Memory-Keeper for research). Simplify Agent Integration Matrix to Context7 only. Remove Memory-Keeper Canonical Tool Names and Integration section. |
| 1.4.0 | 2026-03-28 | MCP-M-001 updated with T3/T4 tier references. eng-*/red-* exclusion notes expanded. |
| 1.3.1 | 2026-02-20 | Initial MCP tool governance standards. |
