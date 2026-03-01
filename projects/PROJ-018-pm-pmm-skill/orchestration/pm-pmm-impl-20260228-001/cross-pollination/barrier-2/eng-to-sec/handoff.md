# Cross-Pollination Handoff: Engineering → Security

> **Barrier:** 2
> **From:** Engineering Pipeline (Phase 2 — Tier 1 Agent Definitions)
> **To:** Security Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | What engineering produced that security needs |
| [Artifacts](#artifacts) | File paths for security review |
| [Security-Relevant Decisions](#security-relevant-decisions) | Design choices with security implications |
| [Open Items](#open-items) | Unresolved issues requiring security input |

---

## Key Findings

1. **All 3 Tier 1 agents are T3 (External)** — WebSearch/WebFetch access creates injection surface for all agents, not just pm-customer-insight as initially modeled in Phase 1 threat model.
2. **Cross-reference depth limit (max 2) added** to pm-product-strategist per security review SEC-005. Other agents do not yet have explicit depth limits.
3. **Sensitivity-aware read policy** added to pm-market-strategist. Inherits highest sensitivity from consumed artifacts. Non-downgrade rule enforced via post-completion check.
4. **PII-first processing order** enforced in pm-customer-insight — redaction occurs BEFORE content analysis.
5. **System prompt non-disclosure** added to all 3 agent guardrails sections as defense-in-depth.

## Artifacts

- `eng/phase-2-tier1-agents/pm-product-strategist.md` (revised)
- `eng/phase-2-tier1-agents/pm-customer-insight.md` (revised)
- `eng/phase-2-tier1-agents/pm-market-strategist.md` (revised)
- `eng/phase-2-tier1-agents/pm-product-strategist.governance.yaml` (revised)
- `eng/phase-2-tier1-agents/pm-customer-insight.governance.yaml` (revised)
- `eng/phase-2-tier1-agents/pm-market-strategist.governance.yaml` (revised)
- `eng/phase-2-tier1-agents/SKILL.md` (revised)

## Security-Relevant Decisions

| Decision | Rationale | Security Implication |
|----------|-----------|---------------------|
| All agents at T3 | Require WebSearch/WebFetch for framework research | Expands attack surface beyond customer data injection |
| Opus model for all Tier 1 | Complex reasoning needed for framework operationalization | Higher-capability model may be more resistant to injection but also more capable of creative misuse |
| Discovery/delivery dual mode | Agents behave differently based on mode | Mode-switching could be exploited to bypass delivery-mode guardrails |
| JTBD shared between 2 agents | pm-customer-insight owns primary, pm-product-strategist consumes | Data flow creates trust boundary crossing |

## Open Items

1. **Cross-reference depth limits for pm-customer-insight and pm-market-strategist** — only pm-product-strategist has explicit limit. Phase 3 agents will need this too.
2. **Delivery-mode prerequisite verification** — currently LLM-checked only. No deterministic enforcement mechanism exists for promotion gates.
3. **Web content injection mitigations** — narrative guardrails added but no L3/L5 deterministic enforcement. Acknowledged as Tier B enforcement gap.
