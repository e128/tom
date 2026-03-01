# Cross-Pollination Handoff: Engineering → Security

> **Barrier:** 3
> **From:** Engineering Pipeline (Phase 3 — Tier 2 Agent Definitions)
> **To:** Security Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | What engineering produced that security needs |
| [Artifacts](#artifacts) | File paths for security review |
| [Security-Relevant Decisions](#security-relevant-decisions) | Design choices with security implications |

---

## Key Findings

1. **Both Tier 2 agents at T3 (External)** — WebSearch/WebFetch access for benchmarking and competitive intelligence creates injection surface.
2. **Sensitivity upgraded to `restricted`** for both agents per SEC-028/SEC-044. Business cases and competitive intelligence are crown-jewel data.
3. **Provenance tracking implemented** in pm-competitive-analyst using SEC-043 4-tier taxonomy (VERIFIED/UNVERIFIED/INFERRED/STALE).
4. **ACTUAL/PROJECTED labeling** added to pm-business-analyst per SEC-029.
5. **Battle card bias/defamation guardrail** added per SEC-045 — legally defensible language required.
6. **System prompt non-disclosure** added to both governance YAMLs (TH-003).
7. **Cross-reference depth limit max 2** enforced on both agents.

## Artifacts

- `eng/phase-3-tier2-agents/pm-business-analyst.md` (revised)
- `eng/phase-3-tier2-agents/pm-business-analyst.governance.yaml` (revised)
- `eng/phase-3-tier2-agents/pm-competitive-analyst.md` (revised)
- `eng/phase-3-tier2-agents/pm-competitive-analyst.governance.yaml` (revised)
- `eng/phase-2-tier1-agents/SKILL.md` (revised — Tier 2 integration)

## Security-Relevant Decisions

| Decision | Rationale | Security Implication |
|----------|-----------|---------------------|
| Sonnet model for Tier 2 | Balanced analysis sufficient for convergent tasks | Lower-capability model may be more susceptible to injection than Opus |
| pm-business-analyst at C3 | Business Case is C3 criticality | Higher quality gate reduces risk of flawed financial analysis |
| Competitive data from web | pm-competitive-analyst fetches competitor content | Adversary-controlled data enters trusted pipeline |
| 4-tier provenance taxonomy | VERIFIED/UNVERIFIED/INFERRED/STALE | Self-reporting system — no independent verification of provenance claims |
