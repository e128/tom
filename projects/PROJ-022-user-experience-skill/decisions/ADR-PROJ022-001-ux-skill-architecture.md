# ADR-PROJ022-001: /user-experience Skill Architecture

<!-- STUB: Created during PROJ-022 Foundation phase. Full ADR to be written during EPIC-001. -->

## Document Sections

| Section | Purpose |
|---------|---------|
| [Status](#status) | ADR lifecycle state |
| [Context](#context) | Problem and constraints |
| [Decision](#decision) | Architectural choice |
| [Consequences](#consequences) | Trade-offs and implications |

---

## Status

**PROVISIONAL** — Architecture validated through PROJ-020 C4 tournament (8 iterations). Decision sections formalized from PROJ-022 Foundation phase evidence. Full validation with Wave 1 implementation data pending.

---

## Context

The /user-experience skill requires an architecture that:
- Supports 10 pluggable sub-skills across 5 criteria-gated waves
- Maintains P-003 compliance (single-level nesting: orchestrator → worker)
- Enables cross-framework synthesis from multiple UX methodologies
- Degrades gracefully when optional MCP servers are unavailable
- Serves tiny teams (1-5 people) without dedicated UX roles

Key decisions to formalize:
1. Parent orchestrator + independent sub-skill topology (vs. monolithic skill)
2. Wave deployment model (vs. all-at-once or feature-flag)
3. Lifecycle-stage routing (vs. user-selected methodology)
4. Cross-framework synthesis approach (vs. independent framework reports)

---

## Decision

**Provisional decision (DRAFT — to be validated with EPIC-001 implementation evidence):**

1. **Parent orchestrator + independent sub-skill topology.** The skill uses a single `ux-orchestrator` (T5, Opus, Integrative) that routes to 10 independent sub-skill worker agents via Task. Each sub-skill is a standalone Jerry skill (`skills/ux-{name}/`) with its own agent, governance YAML, methodology rules, and output templates. Rationale: modular deployment via waves; individual sub-skill replacement without affecting others; P-003 single-level nesting compliance.

2. **Wave deployment model (5 criteria-gated waves).** Sub-skills deploy incrementally through 5 waves with quality gates (S-014 >= 0.85 deployment readiness) at each transition. Rationale: reduces upfront investment risk; each wave is independently useful; teams can stop at any wave. Alternative rejected: all-at-once deployment was rejected because it requires completing all 10 sub-skills before any value delivery.

3. **Lifecycle-stage routing.** The orchestrator routes by product lifecycle stage ("Before design", "During design", "After launch", "CRISIS") rather than requiring users to select a specific UX methodology. Rationale: tiny teams lack UX expertise to select frameworks; stage-based routing reduces cognitive load. The router is deterministic (no LLM-based routing) per H-36(b).

4. **Cross-framework synthesis with confidence gates.** When multiple sub-skills run for the same engagement, the orchestrator synthesizes findings using a 3-tier confidence protocol (HIGH/MEDIUM/LOW). Rationale: prevents AI-generated synthesis from being treated as validated user research (P-022 compliance). Alternative rejected: independent framework reports without synthesis — rejected because cross-framework convergence is the primary value proposition for multi-framework evaluation.

---

## Consequences

**Positive (observed during Foundation phase):**
- Wave model enables per-artifact commits with maximum revert granularity
- P-003 compliance is straightforward: one orchestrator, N workers, no nesting ambiguity
- Lifecycle-stage routing produces a clean, deterministic triage flow

**Negative (anticipated, to validate during Wave 1):**
- 10 sub-skills × 5 artifacts each = 50+ files to maintain; governance overhead scales linearly
- Wave gates may block useful sub-skills that are "good enough" but below 0.85 threshold (see ADR-PROJ022-002)
- Cross-framework synthesis quality depends on sub-skill output consistency — format divergence between sub-skills may degrade synthesis

**Neutral:**
- MCP integration is optional with documented fallback paths; this defers MCP-related consequences to actual usage

---

*ADR: ADR-PROJ022-001-ux-skill-architecture.md*
*Project: PROJ-022-user-experience-skill*
*Created: 2026-03-03*
*Status: PROVISIONAL*
