# Strategy Selection Plan — C4 Tournament Iteration 6

## Criticality Assessment

- **Requested Level:** C4
- **Auto-Escalation Applied:** No (C4 is the highest level; no escalation needed)
- **Final Level:** C4

**Justification:** The deliverable `ux-framework-selection.md` is a critical phase-gate artifact for PROJ-020 feature enhancements. It is:
- Irreversible (framework selection locks the operational foundation for the `/user-experience` skill)
- Architecture-defining (establishes the portfolio structure and sub-skill routing for the parent skill)
- Governance-critical (section 7.6 implements implementation-critical synthesis hypothesis validation gates)

C4 criticality is appropriate and no auto-escalation adjustment is required.

---

## Selected Strategies (Ordered per H-16)

The C4 criticality level mandates ALL 10 selected strategies. The execution order below enforces H-16 constraint: S-003 (Steelman) appears at position 2, before S-002 (Devil's Advocate) at position 5.

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional |
|-------|-------------|---------------|---------------|-------------------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required (C4) |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required (C4, H-16 enforcer) |
| 3 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required (C4) |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required (C4) |
| 5 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required (C4, H-16 compliant) |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required (C4) |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required (C4) |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required (C4) |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required (C4) |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required (C4, FINAL) |

---

## H-16 Compliance

**Constraint:** S-003 (Steelman Technique) MUST be ordered BEFORE S-002 (Devil's Advocate).

- **S-003 position:** Order 2
- **S-002 position:** Order 5
- **Constraint satisfied:** YES — S-003 (pos 2) appears before S-002 (pos 5)

**Rationale:** Steelman is applied early to strengthen the deliverable's core arguments before Devil's Advocate attacks them. This sequence prevents premature rejection of sound approaches and ensures the critique phase operates on the strongest possible formulation of the analysis.

---

## Execution Group Mapping

Strategies are grouped by function for operational clarity (not execution order — follow the numbered sequence above):

**Group A — Self-Review:**
- S-010 (Self-Refine) — Execution position 1

**Group B — Strengthen (Dialectical Synthesis):**
- S-003 (Steelman Technique) — Execution position 2

**Group C — Challenge (Role-Based Adversarialism):**
- S-001 (Red Team Analysis) — Execution position 3
- S-004 (Pre-Mortem Analysis) — Execution position 4
- S-002 (Devil's Advocate) — Execution position 5

**Group D — Verify (Structured Decomposition & Constitutional):**
- S-007 (Constitutional AI Critique) — Execution position 6
- S-011 (Chain-of-Verification) — Execution position 7

**Group E — Decompose (Structured Analysis):**
- S-012 (FMEA) — Execution position 8
- S-013 (Inversion Technique) — Execution position 9

**Group F — Score (Final Quality Gate):**
- S-014 (LLM-as-Judge) — Execution position 10 (ALWAYS LAST)

---

## Strategy Overrides Applied

**None.** All 10 required strategies for C4 are included with no removals or additions.

---

## Quality Metrics

**Current iteration state:**
- Iteration: 6 of 8 maximum per `quality-enforcement.md` C4 iteration ceiling
- Previous scores: 0.747 → 0.822 → 0.848 → 0.803 → 0.843
- Current target: >= 0.92 (quality gate threshold per H-13)
- Score band: Current best (0.843) in REVISE band (0.85-0.91); latest revision shifted to REVISE-boundary

**Revision 10 context:**
- 5 Critical findings resolved from Iteration 5
- 16 Major findings resolved
- 3 substantive additions
- Navigation, gate enforcement, and attestation boundary corrected

---

## Self-Review Checklist (H-15)

Per H-15, before persisting this selection plan, verify:

- [x] All strategy IDs are valid (S-001 through S-014, from authorized strategy catalog in quality-enforcement.md)
- [x] H-16 ordering constraint satisfied (S-003 at position 2, S-002 at position 5; 2 < 5)
- [x] All 10 selected strategies included (C4 requirement: "All 10 selected")
- [x] Auto-escalation rules checked (AE-001 through AE-006e; none trigger for this deliverable)
- [x] Template paths correspond to selected strategies (format: `.context/templates/adversarial/s-{NNN}-{slug}.md`)
- [x] No user overrides present (none requested)
- [x] Criticality level assignment justified (C4 appropriate for irreversible, architecture-critical, governance-critical artifact)

---

## Constitutional Compliance (P-003, P-020, P-022)

This strategy selection plan adheres to all constitutional principles:

| Principle | Agent Behavior | Compliance |
|-----------|----------------|-----------|
| P-003 (No recursive subagents) | adv-selector does not spawn subagents; strategy execution is delegated to adv-executor and adv-scorer via Task tool, respecting orchestrator-worker topology | **Compliant** |
| P-020 (User authority) | All strategies are required by C4 criticality per quality-enforcement.md SSOT; no user overrides requested or applied; user has authority to adjust criticality level if C4 is not appropriate | **Compliant** |
| P-022 (No deception) | This selection plan transparently lists all selected and excluded strategies; H-16 constraint is explicitly documented and verified; all template paths are verified as accurate | **Compliant** |

---

## Persistence

This strategy selection plan is persisted to:

**File path:** `projects/PROJ-020-feature-enhancements/work/analysis/c4-tournament-iter6-execution-plan.md`

**Status:** READY FOR EXECUTION

---

## Next Steps (for adv-executor)

1. Load each strategy template in execution order (S-010 → S-003 → S-001 → S-004 → S-002 → S-007 → S-011 → S-012 → S-013 → S-014)
2. Execute each strategy against the deliverable using the template guidance
3. Collect findings from each strategy
4. Route to adv-scorer for S-014 (LLM-as-Judge) quality scoring in final position
5. Persist iteration results to worktracker entity for PROJ-020

---

*Strategy Selection Plan Version: 1.0.0*
*Agent: adv-selector*
*Date: 2026-03-03*
*Constitutional Compliance: Jerry Constitution v1.0*
*SSOT: `.context/rules/quality-enforcement.md` (Criticality Levels section)*
