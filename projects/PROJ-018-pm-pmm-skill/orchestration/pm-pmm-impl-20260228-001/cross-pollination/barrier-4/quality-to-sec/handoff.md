# Cross-Pollination Handoff: Quality → Security

> **Barrier:** 4
> **From:** Quality Pipeline (Phase 4 — Final Adversarial Quality Gate)
> **To:** Security Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | Quality findings with security implications |
| [FMEA Security-Relevant Failure Modes](#fmea-security-relevant-failure-modes) | Top RPN items from Group C |
| [Recommendations](#recommendations) | Items for post-deployment security monitoring |

---

## Key Findings

1. **Group C FMEA identified 15 failure modes** — 1 CRITICAL (RPN 336), 9 HIGH (RPN 200-300), 5 MEDIUM.
2. **FM-07 CRITICAL: SKILL.md context budget (RPN 336)** — 532-line SKILL.md loads entirely into context with no selective loading mechanism. Not a direct security risk but increases context rot probability which degrades guardrail adherence.
3. **FM-08: Security DC-MUST conditions now enforced** — revision-1 Fix 1 added cross-reference to deployment manifest (this was the highest-severity finding across all 3 groups).
4. **FM-11: "strategy (standalone)" notation fixed** — revision-1 Fix 2 replaced with simple parseable negative keyword.
5. **Rollback now includes complete registration removal** — revision-1 Fix 3 prevents ghost skill routing.

## FMEA Security-Relevant Failure Modes

| Rank | FM-ID | Failure Mode | RPN | Status Post-Revision |
|------|-------|-------------|-----|---------------------|
| 1 | FM-07 | SKILL.md context budget at 532 lines | 336 | Unmitigated (architectural) |
| 2 | FM-11 | "strategy (standalone)" unparseable notation | 294 | FIXED (revision-1 Fix 2) |
| 3 | FM-04 | Workflow patterns hit H-36 circuit breaker | 280 | Partially mitigated (error handling added, H-36 clarification needed) |
| 4 | FM-01 | Trigger map captures unintended requests | 280 | Partially mitigated (negative keywords improved) |
| 5 | FM-08 | DC-MUST conditions not enforced at deployment | 270 | FIXED (revision-1 Fix 1) |

## Recommendations

1. **Post-deployment injection test monitoring** (MON-01 in security assessment) — quarterly execution of 37 injection scenarios with >= 95% pass rate threshold.
2. **Routing false-positive monitoring** — track whether /pm-pmm activates on non-PM/PMM requests during first 30 days.
3. **Context budget monitoring** — observe whether SKILL.md loading measurably degrades agent quality in production sessions.
