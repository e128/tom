# C4 Tournament Iteration 7 — Strategy Execution Plan

**UX Framework Selection Analysis**
**Criticality Level:** C4 (Critical)
**Tournament Iteration:** 7 of 8
**Score Trajectory:** 0.747 → 0.822 → 0.848 → 0.803 → 0.843 → 0.862 → pending
**Quality Threshold:** >= 0.95
**Revision Context:** Revision 11, 3 Critical findings resolved in R11

---

## Strategy Selection Plan

## Criticality Assessment
- **Requested Level:** C4
- **Auto-Escalation Applied:** No
- **Final Level:** C4

**Justification:** The UX Framework Selection Analysis is an architecture/governance decision with irreversible consequences. C4 criticality is appropriate for multi-criteria framework decisions that impact product direction and multi-team UX implementation strategies. No auto-escalation rules triggered (deliverable does not touch constitution, governance files, ADRs, or security-critical code).

---

## Selected Strategies (Ordered)

All 10 selected strategies are REQUIRED for C4 criticality per quality-enforcement.md Criticality Levels table. No optional strategies exist at C4. Execution follows the recommended order with H-16 constraint (S-003 Steelman before S-002 Devil's Advocate) satisfied.

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Notes |
|-------|-------------|---------------|---------------|-------------------|-------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Group A: Self-review before presenting |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | Group B: Strengthen ideas before attacking (H-16 prerequisite) |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | Group C: Challenge assumptions (H-16 satisfied: S-003 at position 2 before S-002 at position 3) |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Group C: Identify failure modes |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Group C: Comprehensive attack surface analysis |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Group D: Governance and policy compliance |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Group D: Verify claims and evidence |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Group E: Structured failure analysis |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Group E: Reverse-engineer problem statement |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | Group F: Final quality scoring (ALWAYS LAST) |

---

## H-16 Compliance

**H-16 Constraint:** Steelman (S-003) MUST be ordered before Devil's Advocate (S-002).

- **S-003 position:** 2
- **S-002 position:** 3
- **Constraint satisfied:** YES — S-003 (position 2) precedes S-002 (position 3)

**Rationale:** Strengthening the UX framework selection arguments before attacking them prevents premature rejection of valid approaches. This canonical pairing ensures robust evaluation: first reinforce strengths, then challenge assumptions.

---

## Execution Group Structure

Strategies are organized into functional groups per the recommended execution order:

**Group A — Self-Review:**
- S-010 (Self-Refine) — Agent self-corrects obvious defects before critique

**Group B — Strengthen:**
- S-003 (Steelman Technique) — Build strongest possible case for each framework option

**Group C — Challenge:**
- S-002 (Devil's Advocate) — Attack assumptions and identify weaknesses
- S-004 (Pre-Mortem Analysis) — Anticipate failure scenarios
- S-001 (Red Team Analysis) — Comprehensive adversarial assessment

**Group D — Verify:**
- S-007 (Constitutional AI Critique) — Check governance and policy alignment
- S-011 (Chain-of-Verification) — Verify evidence quality and claim support

**Group E — Decompose:**
- S-012 (FMEA) — Structured failure mode enumeration and risk assessment
- S-013 (Inversion Technique) — Reverse-engineer the problem to verify framing

**Group F — Score:**
- S-014 (LLM-as-Judge) — Apply quality rubric with 6 dimensions (ALWAYS LAST)

---

## Quality Scoring Context

**Quality Rubric Dimensions (S-014):**
- Completeness (20%)
- Internal Consistency (20%)
- Methodological Rigor (20%)
- Evidence Quality (15%)
- Actionability (15%)
- Traceability (10%)

**Tournament Target:** >= 0.95 (elevated threshold for C4 iteration 7 recovery)

**Prior Iteration Performance:**
- Iteration 6 score: 0.862 (within REVISE band, 0.85-0.91)
- 3 Critical findings resolved in Revision 11
- Current trajectory: improving toward tournament closure

---

## Strategy Overrides Applied

**None.** All 10 required C4 strategies are selected per quality-enforcement.md. No user overrides are specified. No strategies are removed or added.

---

## Template File Path Verification

All template files exist and are accessible:

- ✓ `.context/templates/adversarial/s-001-red-team.md`
- ✓ `.context/templates/adversarial/s-002-devils-advocate.md`
- ✓ `.context/templates/adversarial/s-003-steelman.md`
- ✓ `.context/templates/adversarial/s-004-pre-mortem.md`
- ✓ `.context/templates/adversarial/s-007-constitutional-ai.md`
- ✓ `.context/templates/adversarial/s-010-self-refine.md`
- ✓ `.context/templates/adversarial/s-011-cove.md`
- ✓ `.context/templates/adversarial/s-012-fmea.md`
- ✓ `.context/templates/adversarial/s-013-inversion.md`
- ✓ `.context/templates/adversarial/s-014-llm-as-judge.md`

---

## Self-Review (H-15)

Per H-15, before persisting this plan, verification:

1. **All strategy IDs valid:** ✓ S-001, S-002, S-003, S-004, S-007, S-010, S-011, S-012, S-013, S-014 (10 selected from quality-enforcement.md catalog)
2. **H-16 ordering satisfied:** ✓ S-003 (position 2) before S-002 (position 3)
3. **Auto-escalation rules checked:** ✓ No escalation rules triggered; deliverable is analysis, not governance/constitutional/ADR
4. **User overrides reflected:** ✓ No overrides specified; all 10 required C4 strategies selected
5. **Template paths verified:** ✓ All 10 template files exist in `.context/templates/adversarial/`
6. **Criticality level appropriate:** ✓ C4 justified (irreversible architecture decision)
7. **Quality threshold specified:** ✓ 0.95 (C4 tournament threshold)
8. **Completeness:** ✓ All required fields present: strategy IDs, names, paths, ordering, H-16 compliance, template verification

---

## Constitutional Compliance

| Principle | Agent Behavior | Status |
|-----------|----------------|--------|
| P-002 (File Persistence) | Selection plan persisted to output file | ✓ |
| P-003 (No Recursion) | No subagents spawned; deterministic mapping only | ✓ |
| P-020 (User Authority) | User criticality (C4) accepted; no override applied | ✓ |
| P-022 (No Deception) | All strategies transparently listed; no hidden exclusions | ✓ |
| H-15 (Self-Review) | Plan self-reviewed before persistence | ✓ |

---

## Next Steps

**For adv-executor agent:** Load and execute all 10 strategies in the order specified using template files. Apply each strategy to the UX Framework Selection Analysis (Revision 11). Generate strategy-specific critique output. Feed all results to S-014 LLM-as-Judge for final composite scoring.

**For scoring:** Use the quality rubric dimensions listed above. Target threshold: >= 0.95. If score < 0.95, classify findings by criticality and generate targeted revision guidance.

**Iteration tracking:** Log this execution and final score as Tournament Iteration 7. Update worktracker and project PLAN.md with outcome. If threshold met, tournament complete. If threshold not met, escalate for human review per H-31 (iteration ceiling for C4 is 10 per RT-M-010).

---

**Plan Generated:** 2026-03-03
**Criticality:** C4
**Tournament Iteration:** 7 of 8
**Status:** Ready for adv-executor execution
