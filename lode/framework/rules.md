# Rules and Quality Enforcement
*Updated: 2026-04-07T23:59:32Z*

Tom enforces 25 HARD rules (non-overridable) and a quality gate of 0.92 for C2+ deliverables. The authoritative SSOT is `.context/rules/quality-enforcement.md`.

## Key HARD Rules

| ID | Rule | Consequence |
|----|------|-------------|
| H-01 | No recursive subagents (max 1 level) | Architecture violation |
| H-04 | Active project REQUIRED (`JERRY_PROJECT` env var) | Session won't proceed |
| H-05 | UV only: `uv run` for execution, `uv add` for deps | Environment corruption |
| H-07 | Layer isolation: domain must not import from infrastructure/interface | Architecture violation |
| H-10 | One class per file | Code organization violation |
| H-13 | Quality threshold >= 0.92 for C2+ deliverables | Deliverable rejected |
| H-14 | Creator-critic-revision cycle: min 3 iterations for C2+ | Quality gate bypass |
| H-20 | BDD test-first Red phase; 90% line coverage required | Test standards violation |
| H-22 | Proactive skill invocation (see trigger map) | Work quality degradation |
| H-31 | Clarify when ambiguous; MUST NOT ask when clear | Wrong-direction work |
| H-32 | GitHub Issue parity for tom repo work items | Dual-tracking violation |
| H-34 | Agent definitions: YAML frontmatter + constitutional compliance triplet (P-003/P-020/P-022) | Agent structurally invalid |
| H-36 | Agent routing: circuit breaker max 3 hops; keyword-first routing | Routing loop / token exhaustion |

Full index: `.context/rules/quality-enforcement.md` HARD Rule Index table.

## Quality Gate

- Threshold: >= 0.92 weighted composite score for C2+ deliverables
- Dimensions (with weights): Completeness (0.20), Internal Consistency (0.20), Methodological Rigor (0.20), Evidence Quality (0.15), Actionability (0.15), Traceability (0.10)
- Scoring via S-014 LLM-as-Judge strategy

## Criticality Levels

| Level | Scope | Required Strategies |
|-------|-------|---------------------|
| C1 | Reversible in 1 session, <3 files | S-010 (Self-Refine) |
| C2 | Reversible in 1 day, 3-10 files | S-007, S-002, S-014 |
| C3 | >1 day to reverse, >10 files | C2 + S-004, S-012, S-013 |
| C4 | Irreversible, architecture/governance | All 10 strategies |

## Auto-Escalation Rules

| ID | Condition | Escalation |
|----|-----------|------------|
| AE-001 | Touches `docs/governance/TOM_CONSTITUTION.md` | Auto-C4 |
| AE-002 | Touches `.context/rules/` or `.claude/rules/` | Auto-C3 minimum |
| AE-003 | New or modified ADR | Auto-C3 minimum |
| AE-004 | Modifies baselined ADR | Auto-C4 |
| AE-005 | Security-relevant code | Auto-C3 minimum |
| AE-006a | Context fill NOMINAL (< 0.70) | No action |
| AE-006b | Context fill WARNING (>= 0.70) | Log + consider checkpoint |
| AE-006c | Context fill CRITICAL (>= 0.80) | Auto-checkpoint + reduce verbosity |
| AE-006d | Context fill EMERGENCY (>= 0.88) | Mandatory checkpoint + warn user |
| AE-006e | Compaction event detected | Human escalation for C3+, session restart recommended |

## Enforcement Layers

- **L1** (session start): behavioral foundation via auto-loaded rules
- **L2** (every prompt): re-inject critical rules via HTML comment markers
- **L3** (pre-tool): deterministic gating (AST checks)
- **L4** (post-tool): output inspection
- **L5** (CI/commit): post-hoc verification scripts in `scripts/`

## Related Lode Files

- [skills.md](skills.md) — H-22 (mandatory skill invocation) details
- [../practices.md](../practices.md) — key rules summary for daily work
