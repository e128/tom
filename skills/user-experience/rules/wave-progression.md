# Wave Progression Rules

<!-- STUB: Created during PROJ-022 Foundation phase. Full implementation in EPIC-001. -->

> Criteria-gated wave deployment rules for the /user-experience skill. Defines wave transition quality gates, bypass mechanism, and signoff requirements.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Wave Transition Gates](#wave-transition-gates) | Quality thresholds per wave |
| [Signoff Requirements](#signoff-requirements) | What must exist before next wave begins |
| [Bypass Mechanism](#bypass-mechanism) | 3-field bypass documentation process |
| [Wave State Tracking](#wave-state-tracking) | How wave deployment state is persisted |

---

## Wave Transition Gates

<!-- TODO (EPIC-001): Define per-wave quality gate criteria. -->
<!-- Source: SKILL.md Section "Wave Transition Quality Gates" defines the 0.85 threshold. -->
<!-- Formal derivation: ADR-PROJ022-002-wave-criteria-gates.md (pending). -->

Pending implementation. Wave transition threshold: >= 0.85 deployment readiness score.

| Wave | Prerequisite | Threshold |
|------|-------------|-----------|
| 1 → 2 | WAVE-1-SIGNOFF.md exists | >= 0.85 |
| 2 → 3 | WAVE-2-SIGNOFF.md exists | >= 0.85 |
| 3 → 4 | WAVE-3-SIGNOFF.md exists | >= 0.85 |
| 4 → 5 | WAVE-4-SIGNOFF.md exists | >= 0.85 |

---

## Signoff Requirements

<!-- TODO (EPIC-001): Define signoff file contents and validation. -->

Pending implementation. Each WAVE-N-SIGNOFF.md must contain: sub-skill quality scores, acceptance criteria verification, user approval.

---

## Bypass Mechanism

<!-- TODO (EPIC-001): Define 3-field bypass documentation requirements. -->

Pending implementation. Bypass fields:
1. **Unmet criterion**: Which wave criterion is not met
2. **Impact assessment**: Risk of proceeding without the criterion
3. **Remediation plan**: How the criterion will be satisfied post-bypass

User approval required per P-020.

---

## Wave State Tracking

<!-- TODO (EPIC-001): Define how wave deployment state is persisted and queried. -->

Pending implementation. Signoff files at `skills/user-experience/output/WAVE-N-SIGNOFF.md`.

---

*Rule file: wave-progression.md*
*Parent skill: /user-experience*
*Created: 2026-03-03*
*Status: STUB — Full implementation tracked in EPIC-001*
