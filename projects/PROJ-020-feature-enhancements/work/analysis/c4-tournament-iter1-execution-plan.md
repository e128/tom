# C4 Tournament Strategy Execution Plan

## Criticality Assessment

- **Requested Level:** C4
- **Auto-Escalation Applied:** No (no AE rules triggered)
  - Deliverable path does not touch constitution or governance files
  - Deliverable is analysis type, not ADR modification
  - No security-relevant code present
- **Final Level:** C4

**Delivered:** 2026-03-03 | **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` | **Type:** Analysis (Weighted Multi-Criteria Decision Matrix) | **Quality Threshold:** 0.95

---

## Selected Strategies (Ordered for C4)

All 10 strategies are **required** for C4 criticality per SSOT (`quality-enforcement.md` Criticality Levels table). No strategies are optional.

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Cognitive Mode |
|-------|-------------|---------------|---------------|-------------------|----------------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Iterative Improvement |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required (H-16) | Dialectical Synthesis |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required (H-16) | Role-Based Adversarialism |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Risk Anticipation |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Offensive Review |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Governance Compliance |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Structured Verification |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Risk Decomposition |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Constraint Reversal |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required (ALWAYS LAST) | Quality Scoring |

---

## H-16 Compliance Check

**Steelman before Devil's Advocate (H-16 HARD Rule):**

- **S-003 position:** Order 2 (Steelman Technique)
- **S-002 position:** Order 3 (Devil's Advocate)
- **Constraint satisfied:** ✓ YES — S-003 (pos 2) executes **before** S-002 (pos 3)

---

## Execution Groups & Parallelization

Strategies are organized into logical groups. Strategies within a group may execute in parallel; subsequent groups await group completion before starting.

### Group A — Self-Review (Sequential)
**Purpose:** Initial self-correction before external critique
- **Order 1:** S-010 (Self-Refine)
- **Dependencies:** None (runs on raw deliverable)
- **Output:** Refined deliverable with self-identified issues flagged

### Group B — Strengthen & Challenge (Sequence: Steelman → Devil's Advocate)
**Purpose:** Dialectical synthesis per H-16 ordering constraint
- **Order 2:** S-003 (Steelman Technique) — Strengthen core arguments, find strongest interpretation
- **Order 3:** S-002 (Devil's Advocate) — Attack assumptions, identify counter-evidence
- **Dependencies:** S-010 (Group A must complete first)
- **H-16 Constraint:** S-003 **must precede** S-002 (HARD rule, non-negotiable)
- **Output:** Balanced perspective on framework selection robustness

### Group C — Risk & Impact Analysis (Parallel)
**Purpose:** Identify failure modes, preconditions, and boundary conditions
- **Order 4:** S-004 (Pre-Mortem Analysis) — Project failure from future perspective
- **Order 5:** S-001 (Red Team Analysis) — Offensive attack on selection quality and coverage
- **Dependencies:** Group B complete
- **Parallelizable:** Yes — both attack from different angles (prospective vs. offensive)
- **Output:** Risk inventory + attack surface map

### Group D — Governance & Verification (Parallel)
**Purpose:** Compliance gates and evidence chain verification
- **Order 6:** S-007 (Constitutional AI Critique) — Governance compliance, principle alignment
- **Order 7:** S-011 (Chain-of-Verification) — Trace evidence, verify all claims
- **Dependencies:** Group C complete
- **Parallelizable:** Yes — independent verification axes
- **Output:** Compliance checklist + evidence traceability matrix

### Group E — Structural Decomposition (Parallel)
**Purpose:** Systematic risk breakdown and constraint-based reasoning
- **Order 8:** S-012 (FMEA) — Failure modes, effects, criticality ranking
- **Order 9:** S-013 (Inversion Technique) — Reverse the framework logic, find contradictions
- **Dependencies:** Group D complete
- **Parallelizable:** Yes — independent decomposition methods
- **Output:** FMEA table + inversion findings document

### Group F — Quality Scoring (Terminal)
**Purpose:** Aggregate all findings into final quality assessment
- **Order 10:** S-014 (LLM-as-Judge) — **ALWAYS LAST**
  - Consumes all prior strategy outputs (S-001 through S-013)
  - Applies 6-dimension rubric: Completeness, Internal Consistency, Methodological Rigor, Evidence Quality, Actionability, Traceability
  - Weights: [0.20, 0.20, 0.20, 0.15, 0.15, 0.10]
  - **Threshold:** >= 0.95 (per user specification for C4 analysis)
  - Produces final score and revision recommendations
- **Dependencies:** All groups A-E must complete
- **Output:** Quality score >= 0.95 required for acceptance

---

## Execution Sequencing Diagram

```
                            START
                              |
                              v
                         ┌─────────┐
                    [1]  │ S-010   │  Self-Refine
                         └────┬────┘  (Group A)
                              |
                              v
              ┌──────────────────────────────────┐
              │        S-003 → S-002             │ H-16 Sequential
         [2] │ S-003: Steelman ────────────┐    │ (Group B)
              │        ↓                   │    │
         [3] │   S-002: Devil's Advocate ──┘    │
              └──────────────────────────────────┘
                              |
              ┌───────────────┴───────────────┐
              |       (PARALLEL OK)          |
         [4] │    ┌─────────┐                │
              │    │ S-004   │ Pre-Mortem    │ Group C
              │    └─────────┘                │
              │         OR (parallel)         │
         [5] │    ┌─────────┐                │
              │    │ S-001   │ Red Team      │
              │    └─────────┘                │
              └───────────────┬───────────────┘
                              |
              ┌───────────────┴───────────────┐
              │       (PARALLEL OK)          │
         [6] │    ┌─────────┐                │
              │    │ S-007   │ Const. AI     │ Group D
              │    └─────────┘                │
              │         OR (parallel)         │
         [7] │    ┌──────────┐               │
              │    │ S-011    │ CoVE          │
              │    └──────────┘               │
              └───────────────┬───────────────┘
                              |
              ┌───────────────┴───────────────┐
              │       (PARALLEL OK)          │
         [8] │    ┌─────────┐                │
              │    │ S-012   │ FMEA           │ Group E
              │    └─────────┘                │
              │         OR (parallel)         │
         [9] │    ┌──────────┐               │
              │    │ S-013    │ Inversion    │
              │    └──────────┘               │
              └───────────────┬───────────────┘
                              |
                              v
                         ┌─────────┐
                    [10] │ S-014   │  LLM-as-Judge
                         │ SCORING │  (TERMINAL, LAST)
                         └────┬────┘  Threshold >= 0.95
                              |
                              v
                         SCORE >= 0.95?
                            YES / NO
                              |
                              v
                           ACCEPT / REJECT
                              |
                              v
                            END
```

---

## User Overrides Applied

None. All 10 strategies are required per C4 criticality level. No user overrides specified.

---

## Constitutional Compliance (P-003, P-020, P-022)

**P-003 (No Recursive Subagents):** This agent (adv-selector) does NOT spawn subagents. It produces a deterministic execution plan that will be handed to adv-executor or the orchestrator for invocation. Compliance: ✓

**P-020 (User Authority):** No user overrides were received. All 10 required strategies are included per SSOT. If user overrides are provided later, they will be documented and applied per P-020. Compliance: ✓

**P-022 (No Deception):** This plan transparently lists all 10 selected strategies with their rationale, template paths, and ordering constraints. No strategies are hidden or deferred. Compliance: ✓

---

## Self-Review Checklist (H-15 & P-003 Verification)

Before persisting this plan:

- [x] **Strategy ID validation:** All strategy IDs are valid (S-001 through S-014, selected 10 only)
- [x] **H-16 ordering satisfied:** S-003 position (2) < S-002 position (3) ✓
- [x] **Auto-escalation rules checked:** No AE rules triggered → Final level = Requested level ✓
- [x] **Required vs. Optional:** C4 criticality requires all 10; none are optional ✓
- [x] **Template paths verified:** All paths follow `.context/templates/adversarial/s-{NNN}-{slug}.md` pattern ✓
- [x] **No P-003 violation:** This agent produces a plan, does not spawn subagents ✓
- [x] **Completeness:** All required fields in output (strategy IDs, names, template paths, ordering, compliance) ✓
- [x] **User overrides:** None received; transparency documented ✓
- [x] **File persistence:** Plan persisted to specified location ✓

---

## Next Steps (Operational Handoff)

This execution plan is ready for tournament execution by `/adversary` skill agents:

1. **adv-executor** reads this plan and loads strategy templates in order
2. **adv-executor** applies each strategy against the deliverable artifact
3. Strategies generate intermediate critique documents (one per strategy)
4. **adv-scorer** (S-014) consumes all 9 prior strategy outputs + original deliverable
5. **adv-scorer** produces final quality score with dimension-level breakdown
6. **Quality Gate:** If score >= 0.95 → Accept. If < 0.95 → Reject, send to revision cycle
7. **Revision Cycle:** Per H-14, maximum 10 iterations at C4 (provisional ceiling per `agent-routing-standards.md` RT-M-010)

**Criticality:** This is a C4 Critical analysis. All tournament strategies are required. Quality threshold is strict: 0.95. Revision cycles will continue until threshold is met or iteration ceiling (10) is reached.

---

**Plan Version:** 1.0.0
**Generated by:** adv-selector agent
**Date:** 2026-03-03
**Compliance:** H-15 ✓, H-16 ✓, P-003 ✓, P-020 ✓, P-022 ✓
