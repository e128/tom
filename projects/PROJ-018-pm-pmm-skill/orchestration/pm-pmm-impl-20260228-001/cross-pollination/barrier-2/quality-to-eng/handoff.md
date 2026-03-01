# Cross-Pollination Handoff: Quality → Engineering

> **Barrier:** 2
> **From:** Quality Pipeline (Phase 2 — Adversarial Quality Gate)
> **To:** Engineering Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | Quality gate results for engineering |
| [Artifacts](#artifacts) | Quality review file paths |
| [Score Summary](#score-summary) | Per-group and aggregate scores |
| [Caveats for Phase 3](#caveats-for-phase-3) | Items engineering must address in next phase |

---

## Key Findings

1. **Phase 2 aggregate: 0.939 (ACCEPT_WITH_CAVEATS)** — above 0.90 overnight threshold, below 0.95 production-ready.
2. **Weakest artifact: pm-market-strategist** (0.924 in Group D) — sensitivity containment and C3 justification were gaps; revision helped but didn't fully close.
3. **Strongest artifacts: governance YAMLs** (0.950 in Group D) — schema compliance and constitutional coverage are excellent.
4. **Framework operationalization praised across all groups** — no name-dropping, genuine canonical output structures.
5. **JTBD duplication flagged** — pm-product-strategist should reference pm-customer-insight as primary JTBD owner rather than re-operationalizing.

## Artifacts

- `quality/phase-2-gate/adv-group-a-constitutional.md` (Group A: 0.973)
- `quality/phase-2-gate/adv-group-b-dialectical.md` (Group B: 0.958)
- `quality/phase-2-gate/adv-group-c-analytical.md` (Group C: 0.890)
- `quality/phase-2-gate/adv-group-d-scoring.md` (Group D: 0.939)
- `quality/phase-2-gate/revision-1-summary.md`

## Score Summary

| Group | Strategy | Pre-Revision | Post-Revision |
|-------|----------|-------------|---------------|
| A | S-007 Constitutional | 0.973 | (no re-score) |
| B | S-003+S-002 Dialectical | 0.958 | (no re-score) |
| C | S-012+S-013 Analytical | 0.890 | (no re-score) |
| D | S-014 LLM-as-Judge | — | 0.939 |
| **Aggregate** | | **0.940 (A+B+C avg)** | **0.939 (D final)** |

## Caveats for Phase 3

Engineering must address these 8 caveats when building Tier 2 agents:

1. **CAV-01:** JTBD duplication — reduce pm-product-strategist's JTBD to consumption-only
2. **CAV-02:** Discovery-mode framework subsets — specify which framework sections apply per mode
3. **CAV-03:** Delivery prerequisite dead-end — add intermediate "delivery-draft" behavior
4. **CAV-04:** Competitive data provenance — pm-competitive-analyst must track source reliability
5. **CAV-05:** Guardrail enforcement gap — acknowledge Tier B status for narrative guardrails
6. **CAV-06:** Keyword collision — `/pm-pmm` vs `/problem-solving` negative keywords at registration
7. **CAV-07:** SKILL.md context budget — consider Tier 2 deferral for framework catalog section
8. **CAV-08:** Security review traceability — cross-reference agent-sec-review.md in agent definitions
