# C4 Tournament — Iteration 5: Strategy Selection Plan

## Document Sections

| Section | Purpose |
|---------|---------|
| [Criticality Assessment](#criticality-assessment) | Requested vs. final criticality level, auto-escalation analysis |
| [Selected Strategies (Ordered)](#selected-strategies-ordered) | All 10 required strategies with template paths and ordering rationale |
| [H-16 Compliance](#h-16-compliance) | Steelman before Devil's Advocate constraint verification |
| [Execution Context](#execution-context) | Prior iterations, convergence metrics, scheduling notes |

---

## Criticality Assessment

- **Requested Level:** C4
- **Auto-Escalation Applied:** No
  - AE-001 (constitution touch): Not applicable
  - AE-002 (.context/rules/ touch): Not applicable
  - AE-003 (ADR modification): Not applicable (GitHub Issue body)
  - AE-004 (baselined ADR modification): Not applicable
  - AE-005 (security-relevant): Not applicable
  - AE-006 (context fill): Not triggered (token budget available)
- **Final Level:** C4

**Rationale:** Deliverable is a GitHub Enhancement issue body for a major new skill (`/user-experience`). C4 criticality is appropriate due to:
- **Irreversible scope:** High-visibility public issue drives product direction and market perception
- **Architecture impact:** Introduces new skill ecosystem (parent + 10 sub-skills) with governance implications
- **Governance:** Skill registration, MCP integration, routing strategy affect Jerry framework
- **Prior tournament iterations:** 4 prior revisions (I1-I4) demonstrate high-stakes quality bar

---

## Selected Strategies (Ordered)

**All 10 selected strategies are REQUIRED for C4 per SSOT `quality-enforcement.md`.**

Execution order enforces H-16 constraint (Steelman before Devil's Advocate) and follows recommended group structure from ordering-rules section.

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Group |
|-------|-------------|---------------|---------------|-------------------|-------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | A |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | B |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | C |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | C |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | C |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | D |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | D |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | E |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | E |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | F |

### Execution Group Reference

- **Group A — Self-Review:** S-010 (Self-Refine) — Early introspective review per H-15
- **Group B — Strengthen:** S-003 (Steelman Technique) — Build strongest form of argument before critique per H-16
- **Group C — Challenge:** S-002 (Devil's Advocate), S-004 (Pre-Mortem), S-001 (Red Team) — Adversarial attack from multiple angles
- **Group D — Verify:** S-007 (Constitutional AI Critique), S-011 (Chain-of-Verification) — Governance and logical consistency checks
- **Group E — Decompose:** S-012 (FMEA), S-013 (Inversion) — Structured failure analysis and inverse thinking
- **Group F — Score:** S-014 (LLM-as-Judge) — ALWAYS LAST per ordering-rules

---

## H-16 Compliance

**Constraint:** "Steelman (S-003) MUST be ordered BEFORE Devil's Advocate (S-002)"

| Item | Position | Status |
|------|----------|--------|
| S-003 (Steelman) | 2 | ✓ |
| S-002 (Devil's Advocate) | 3 | ✓ |
| **Constraint Satisfied** | Position 2 < Position 3 | **YES** |

**Rationale:** Executing Steelman before Devil's Advocate prevents premature rejection of sound approaches. Strengthening the deliverable's core arguments first provides the Devil's Advocate with a robust target to challenge, improving the quality of adversarial feedback.

---

## Execution Context

### Prior Iterations

| Iteration | Score | Band | Fixes Applied | Persistent Issues |
|-----------|-------|------|----------------|-------------------|
| I1 | 0.704 | REVISE | — | 28 total gaps |
| I2 | 0.724 | REVISE | 28 R1 fixes | 10 unresolved from R1 |
| I3 | 0.761 | REVISE | 10 R2 fixes | Gaps remain |
| I4 | 0.835 | REVISE | 18 R3 fixes | 23 unresolved (10 Criticals + 5 constitutional + 8 persistent) |
| **I5 (this round)** | TBD | — | 23 proposed fixes | — |

### Convergence Analysis

- **Score progression:** 0.704 → 0.724 → 0.761 → 0.835 (trend: +0.020, +0.037, +0.074)
- **Delta acceleration:** Revisions are becoming more effective (larger score improvements per iteration)
- **Threshold gap:** 0.92 - 0.835 = 0.085 remaining (REVISE band; near-threshold status indicates targeted fixes will likely suffice)
- **Iteration forecast:** At current acceleration (δ ≈ 0.074), iteration 5 could plausibly reach 0.90-0.92 range if R4 fixes are well-targeted to the 23 identified persistent issues

### Execution Notes

1. **Strategy order is deterministic:** Follow the group sequence (A → B → C → D → E → F) for reproducible results
2. **S-014 scoring is mandatory:** Template execution ends with S-014 LLM-as-Judge scoring; output includes 6-dimension rubric scores
3. **Constitutional check via S-007:** Iteration 4 identified 5 constitutional compliance gaps; S-007 execution will explicitly validate governance constraints
4. **Persistent issue focus:** R4 fixes address the 23 issues marked persistent from I4; use S-012 (FMEA) and S-013 (Inversion) to surface any remaining systematic gaps
5. **Output path:** All strategy outputs will be aggregated into a single tournament iteration report at `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter5/TOURNAMENT_REPORT.md`

---

## Self-Review Checklist (H-15)

Before persisting this execution plan, verification per H-15:

✓ All 10 strategy IDs are valid (S-001, S-002, S-003, S-004, S-007, S-010, S-011, S-012, S-013, S-014)
✓ H-16 ordering satisfied (S-003 position 2 before S-002 position 3)
✓ Auto-escalation rules checked (none triggered; C4 is final level)
✓ Template paths correspond to selected strategies (all paths verified via Glob)
✓ All required C4 strategies included (no optional strategies in C4; all 10 required strategies present)

---

## Constitutional Compliance (P-003, P-020, P-022)

| Principle | Agent Behavior | Status |
|-----------|----------------|--------|
| P-003 (No Recursion) | adv-selector operates as a worker agent; does not spawn subagents | ✓ |
| P-020 (User Authority) | Strategy set determined by SSOT rules, not user override | ✓ |
| P-022 (No Deception) | All selected and excluded strategies transparently listed | ✓ |

---

*Strategy Selection Plan Version: 1.0*
*Agent: adv-selector*
*Created: 2026-03-03*
*SSOT Reference: quality-enforcement.md (Criticality Levels, Strategy Catalog, Ordering Rules)*
*H-16 Enforcement: ✓ Steelman before Devil's Advocate*
