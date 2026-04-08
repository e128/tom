# Claude Revision Log
*Updated: 2026-04-07*

Persistent memory for `/claude-revision`. Each run appends one entry.
Read at Phase 0 to recover last-known state and deferred items.

## Runs

### 2026-04-03
- Agents: 92 | Skills: 33 | Memory files: 1
- Web guidance: skipped (first run)
- HIGH: 5 | MEDIUM: 5 | LOW: 3
- Actions taken:
  - A1: Fixed ux-orchestrator broken YAML (tools/color fields merged)
  - A1b: Fixed cd-generator broken YAML (same pattern)
  - A1c: Removed dead memory-keeper MCP refs from ux-orchestrator (+ agent scanning all others)
  - A2: REVISED — only 2 agents had truly empty tools (not 16; false positive from grep)
  - A3: Added model: haiku to lode-sync and lode-capture-agent, model: sonnet to simplification-agent
  - A4: Added maxTurns: to all 89 skill agents (haiku=10, sonnet=15, opus=25)
  - A5: Fixed effort: medium to effort: high on ux-sprint-facilitator and ux-ai-design-guide (opus agents)
  - R1: Updated stale "8 skills" count to "31 skills" in agent-routing-standards.md
  - R2: Added /bootstrap and /claude-revision to CLAUDE.md skill table
  - R3: Removed volatile agent counts from CLAUDE.md skill descriptions
  - R4: Updated stale priority span references in routing standards
  - S1: Decomposed transcript/SKILL.md (3450 lines) into references/ sub-files
  - Fixed stale skill counts in skill-standards.md
- Deferred:
  - S2: 9 UX skills over 250 lines (558-824 lines each) — MEDIUM, bulk decomposition needed
  - S3: 8 other skills over 250 lines (444-708 lines) — LOW
  - A6: Oversized agent definitions (ts-extractor 1005 lines, nse-architecture 965 lines) — LOW

### 2026-04-07
- Agents: 92 | Skills: 33 | Memory files: 1
- Web guidance: Claude Code v2.1.92-v2.1.94 — default effort changed to high, 6 new SKILL.md frontmatter fields, /tag and /vim removed, plugin skill hooks bug fixed, Agent Teams experimental
- HIGH: 2 | MEDIUM: 6 | LOW: 5
- H1 (10 UX workers with Agent tool) reclassified as FALSE POSITIVE — all had Agent in disallowedTools, not tools
- Actions taken:
  - H2: Added effort: medium to simplification-agent (was inheriting new default of high)
  - M1: Reduced simplification-agent maxTurns from 50 to 25
  - M2: Removed WebSearch/WebFetch from orch-tracker (haiku tracker doesn't need T4 tools)
  - M3: Removed WebSearch/WebFetch from nse-reporter (haiku reporter doesn't need T4 tools)
  - R1: Fixed "18 skill entries" to "17" in agent-routing-standards.md
  - W2: Added 9 new SKILL.md frontmatter fields to skill-standards.md (argument-hint, user-invocable, model, effort, context, agent, paths, shell, disable-model-invocation)
  - S1: Extracted 551 lines from transcript/SKILL.md to 3 reference files (invocation-errors.md, model-selection.md, orchestration-flow.md) — reduced from 1765 to 1214 lines
- Deferred:
  - S2: 9 UX skills over 250 lines (558-824 lines each) — MEDIUM, bulk decomposition needed
  - S3: 8 other skills over 250 lines (427-708 lines) — LOW
  - L2: 14+ oversized agent definitions — LOW
  - L1: nse-configuration (haiku) with T4 tools — LOW, may be justified
  - W3: Check for /tag or /vim references — LOW
