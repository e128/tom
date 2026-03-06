# Cross-Pollination Handoff: Quality → Security

> **Barrier:** 2
> **From:** Quality Pipeline (Phase 2 — Adversarial Quality Gate)
> **To:** Security Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | Quality findings with security implications |
| [Artifacts](#artifacts) | Quality review file paths |
| [FMEA Security-Relevant Failure Modes](#fmea-security-relevant-failure-modes) | Top RPN items from Group C |
| [Recommendations](#recommendations) | Actions for security pipeline in Phase 3 |

---

## Key Findings

1. **Group C FMEA identified 3 CRITICAL failure modes (RPN > 300)** — all security-related: prompt injection via transcripts (360), injection via aggregated artifacts (324), sensitivity field ignored (315).
2. **Guardrails are narrative, not procedural** — Group C CF-03 flags this as systemic risk. Security guardrails exist as LLM behavioral instructions with no deterministic enforcement.
3. **Inversion analysis I-05** — the most dangerous condition is that extensive guardrail documentation creates false sense of security while actual enforcement is LLM-dependent.
4. **Trust chain contamination** — Group C confirmed security review's multi-agent aggregation concern. Data flowing through pm-customer-insight → pm-product-strategist → pm-market-strategist can amplify a single injection.

## Artifacts

- `quality/phase-2-gate/adv-group-c-analytical.md` (FMEA + Inversion analysis)
- `quality/phase-2-gate/adv-group-a-constitutional.md` (constitutional compliance verification)

## FMEA Security-Relevant Failure Modes

| Rank | FM-ID | Failure Mode | RPN | Status |
|------|-------|-------------|-----|--------|
| 1 | FM-11 | Prompt injection via customer transcripts | 360 | Mitigated (PII-first, speaker verification) but RPN still high |
| 2 | FM-12 | Prompt injection via aggregated artifacts | 324 | Partially mitigated (cross-ref depth limit on 1 agent) |
| 3 | FM-04 | Sensitivity field ignored or downgraded | 315 | Mitigated (post-completion checks added) |
| 4 | FM-05 | Cross-agent data flow contamination | 288 | Acknowledged, deferred to Phase 4 integration |
| 5 | FM-15 | Sensitivity non-downgrade rule unenforced | 280 | Post-completion check added (narrative enforcement) |

## Recommendations

1. **Phase 3 security review** should assess pm-business-analyst and pm-competitive-analyst for the same injection vectors identified in FM-11 and FM-12.
2. **Phase 4 integration** should evaluate whether L3 pre-tool checks can provide deterministic enforcement for sensitivity non-downgrade and injection pattern detection.
3. **Injection test scenarios** (25 in prompt-injection.md) should be extended to cover Tier 2 agents and multi-agent aggregation paths.
