# ADR-PROJ022-002: Wave Criteria Gate Thresholds

<!-- STUB: Created during PROJ-022 Foundation phase. Full ADR to be written during EPIC-001. -->

## Document Sections

| Section | Purpose |
|---------|---------|
| [Status](#status) | ADR lifecycle state |
| [Context](#context) | Problem: wave gate threshold vs H-13 threshold |
| [Decision](#decision) | Threshold choice and derivation |
| [Consequences](#consequences) | Trade-offs and calibration plan |

---

## Status

**PROVISIONAL** — Threshold derived from quality-enforcement.md REVISE band boundary (0.85). Calibration data from Wave 1 deployment will inform threshold revision. See Decision section for derivation rationale.

---

## Context

The /user-experience skill uses a wave deployment model with quality gates at each wave transition. The question: what threshold should wave transition gates use?

**Constraint tension:**
- H-13 mandates >= 0.92 weighted composite for C2+ deliverables (agent definitions, rule files, governance artifacts)
- Wave transition gates assess sub-skill *deployment readiness* — whether a sub-skill produces useful output for end users
- These are distinct quality domains: governance artifact quality vs. operational output quality

**Options considered:**
1. **0.92** — Same as H-13. Conservative; may block useful sub-skills that aren't yet polished.
2. **0.85** — Lower threshold reflecting deployment readiness (not governance quality). Risk: may deploy sub-skills that produce mediocre output.
3. **0.80** — Aggressive; prioritizes rapid deployment over quality. Risk: user trust erosion.

---

## Decision

**Provisional decision (DRAFT — to be validated with Wave 1 calibration data):**

**0.85** S-014 weighted composite threshold for wave transition quality gates.

**Rationale:**
- **Distinct quality domains:** H-13's 0.92 threshold governs C2+ *governance artifact* quality (agent definitions, rule files, YAML schemas). Wave gates assess *operational output* quality — whether a sub-skill produces useful UX evaluation output for end users. These are different evaluation targets.
- **Quality floor justification:** 0.85 sits at the boundary of the REVISE band (0.85-0.91) in `quality-enforcement.md`. Sub-skills at this threshold produce structurally complete, methodology-compliant output with minor gaps. Below 0.85, output enters the REJECTED band where significant rework is required.
- **Calibration plan:** After Wave 1 deployment, measure whether sub-skills scoring 0.85-0.91 produce acceptably useful output for end users. If user satisfaction data indicates quality gaps, revise threshold upward (maximum to 0.92, aligning with H-13).

**Threshold NOT applied to:**
- Agent definition files (.md, .governance.yaml) — these use H-13 >= 0.92 (governance artifacts)
- Rule files and templates — these use H-13 >= 0.92 (governance artifacts)
- Wave gates only evaluate the sub-skill's *operational output* on a representative test case

---

## Consequences

**Positive:**
- 0.85 allows deployment of sub-skills that produce useful (if not polished) output, enabling early value delivery
- Clear separation between governance quality (0.92) and operational quality (0.85) prevents threshold confusion
- Calibration plan provides a principled path to threshold adjustment

**Negative:**
- Risk of deploying sub-skills that produce mediocre output (0.85-0.87 range)
- Users may encounter quality inconsistency between Wave 1 (potentially 0.85) and later waves (potentially higher after calibration)

**Key observation for calibration:** Do sub-skills scoring 0.85-0.91 produce acceptably useful output for end users? Track via post-Wave-1 user feedback.

---

*ADR: ADR-PROJ022-002-wave-criteria-gates.md*
*Project: PROJ-022-user-experience-skill*
*Created: 2026-03-03*
*Status: PROVISIONAL*
