# Cross-Pollination Handoff: Security → Engineering

> **Barrier:** 3
> **From:** Security Pipeline (Phase 3 — Tier 2 Agent Security Review)
> **To:** Engineering Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | Security findings for engineering |
| [Artifacts](#artifacts) | Security review file paths |
| [Incorporated Items](#incorporated-items) | What was addressed in revision 1 |
| [Deferred Items](#deferred-items) | Items for Phase 4 resolution |

---

## Key Findings

1. **44 new security requirements** (SEC-028..SEC-070) — pm-business-analyst CRITICAL risk, pm-competitive-analyst HIGH risk.
2. **12 new injection test scenarios** (PI-T2-01..PI-T2-12) covering CSV injection, Van Westendorp manipulation, competitive data fabrication, financial model attacks.
3. **FMEA top RPN: FM-02 Competitive data injection at 432** — highest across all phases. Adversary-controlled competitor websites are simultaneously "verified sources" and attack vectors.
4. **~39 SEC requirements remain unaddressed** after revision — these are defense-in-depth recommendations beyond the 8 critical/high items fixed.

## Artifacts

- `sec/phase-3-agent-review/agent-sec-review.md` (882 lines, 44 requirements)

## Incorporated Items

| SEC Requirement | Resolution |
|----------------|------------|
| SEC-028 (sensitivity: restricted) | Applied to pm-business-analyst |
| SEC-029 (ACTUAL/PROJECTED labeling) | Added to pm-business-analyst output filtering |
| SEC-043 (provenance taxonomy) | Aligned pm-competitive-analyst to 4-tier taxonomy |
| SEC-044 (competitive sensitivity) | Applied to pm-competitive-analyst |
| SEC-045 (battle card bias) | Added bias disclosure and legal language guardrails |
| TH-003 (system prompt non-disclosure) | Added to both governance YAMLs |

## Deferred Items

| Item | Target Phase | Rationale |
|------|-------------|-----------|
| ~39 defense-in-depth SEC requirements | Phase 4 | Non-blocking recommendations |
| Deterministic guardrail enforcement (L3/L5) | Phase 4 | Requires integration infrastructure |
| Injection test execution | Phase 4 | Tests designed; execution requires deployed agents |
| Cross-agent provenance propagation validation | Phase 4 | Requires multi-agent integration testing |
