# Cross-Pollination Handoff: Security → Engineering

> **Barrier:** 2
> **From:** Security Pipeline (Phase 2 — Agent Security Review)
> **To:** Engineering Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | Security findings for engineering to address |
| [Artifacts](#artifacts) | Security review file paths |
| [Incorporated Items](#incorporated-items) | What was already addressed in revision 1 |
| [Deferred Items](#deferred-items) | Items for Phase 3 resolution |

---

## Key Findings

1. **Agent security review verdict: REVISE** — 27 security requirements (SEC-001..SEC-027), pm-product-strategist rated CRITICAL risk, others HIGH.
2. **Prompt injection test scenarios defined** — 25 integration test scenarios across 7 injection mitigation blocks (INJ-001..INJ-007). These should inform Phase 3 agent development.
3. **12-13 guardrail gaps per agent** identified in initial review. Revision 1 addressed 5 priority items; remaining gaps are defense-in-depth recommendations.
4. **Trust chain contamination scenario** documented — multi-agent data aggregation can amplify single injection through the pipeline.

## Artifacts

- `sec/phase-2-agent-review/agent-sec-review.md` (617 lines, 27 requirements)
- `sec/phase-2-agent-review/prompt-injection.md` (654 lines, 25 test scenarios)

## Incorporated Items

Items from security review addressed in Barrier 2 revision 1:

| SEC Requirement | Resolution |
|----------------|------------|
| Prompt non-disclosure | Added to all 3 agent guardrails |
| Speaker label enumeration | Added to pm-customer-insight |
| PII-first processing order | Added to pm-customer-insight |
| Cross-reference depth limit | Added to pm-product-strategist (max 2) |
| Sensitivity-aware read policy | Added to pm-market-strategist |
| T3 citation guardrail | Added to all 3 governance YAMLs |

## Deferred Items

Items deferred to Phase 3 (Tier 2 agents) or Phase 4 (integration):

| Item | Target Phase | Rationale |
|------|-------------|-----------|
| Composite persona requirement | Phase 3 | pm-business-analyst and pm-competitive-analyst not yet built |
| Competitive data provenance tracking | Phase 3 | pm-competitive-analyst owns this concern |
| Cross-reference depth limits for remaining agents | Phase 3 | Apply to pm-business-analyst and pm-competitive-analyst |
| Deterministic guardrail enforcement (L3/L5) | Phase 4 | Requires integration infrastructure beyond agent definitions |
| Injection test execution | Phase 4 | Tests designed; execution requires deployed agents |
