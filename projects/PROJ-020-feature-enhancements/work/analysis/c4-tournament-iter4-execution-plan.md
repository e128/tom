# Strategy Selection Plan — C4 Tournament Iteration 4

**Analysis Artifact:** UX Framework Selection (Phase 2 Framework Selection deliverable)
**Deliverable Path:** projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md
**Revision:** 8 (Tournament Iteration 4)
**Target Quality Threshold:** >= 0.95
**Prior Iteration Scores:** 0.747 (Iter1) → 0.822 (Iter2) → 0.848 (Iter3)
**Plan Generated:** 2026-03-03

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Criticality Assessment](#criticality-assessment) | Requested vs. final criticality with escalation check |
| [Selected Strategies (Ordered)](#selected-strategies-ordered) | All 10 required strategies in H-16 compliant sequence |
| [H-16 Compliance Verification](#h-16-compliance-verification) | S-003 position < S-002 position check |
| [Parallelization Groups](#parallelization-groups) | Strategies grouped for parallel execution with dependencies |
| [Strategy Overrides Applied](#strategy-overrides-applied) | User-specified modifications (none) |
| [Self-Review Summary (H-15)](#self-review-summary-h-15) | Pre-persistence validation checklist |

---

## Criticality Assessment

| Aspect | Value | Notes |
|--------|-------|-------|
| **Requested Level** | C4 | Explicitly specified: "C4 criticality tournament" |
| **Auto-Escalation Check** | None triggered | AE-001 through AE-005 checked; deliverable does not touch constitution, rules, ADRs, or security code |
| **Final Level** | **C4** | No escalation applied; remains as requested |
| **Enforcement Scope** | All tiers + tournament | Per quality-enforcement.md criticality table |

**Escalation Assessment Detail:**
- **AE-001** (constitution touch): Deliverable path is analysis/ux-framework-selection.md — does not touch docs/governance/TOM_CONSTITUTION.md. Not triggered.
- **AE-002** (rules/ touch): Deliverable path does not match .context/rules/ or .claude/rules/. Not triggered.
- **AE-003** (new/modified ADR): Deliverable type is Analysis, not ADR. Not triggered.
- **AE-004** (baselined ADR modification): Not an ADR. Not triggered.
- **AE-005** (security-relevant code): Deliverable is analysis, not code. No security keywords (auth, credential, secret, permission, encryption) detected. Not triggered.

**Result:** No auto-escalation. **Final criticality = C4 (Critical).**

---

## Selected Strategies (Ordered)

Per quality-enforcement.md Criticality Levels section: C4 Critical deliverables require **ALL 10 selected strategies** as REQUIRED. No optional strategies apply.

**H-16 Constraint Compliance:** S-003 (Steelman) MUST be ordered BEFORE S-002 (Devil's Advocate). This plan enforces that constraint in the execution sequence below.

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Group |
|-------|-------------|---------------|---------------|-------------------|-------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Group A (Self-Review) |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | Group B (Strengthen) |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | Group C (Challenge) |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Group C (Challenge) |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Group C (Challenge) |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Group D (Verify) |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Group D (Verify) |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Group E (Decompose) |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Group E (Decompose) |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | Group F (Score) |

**Ordering Rationale by Group:**

- **Group A (S-010):** Self-Refine first — agent reviews its own output before external critic engagement per H-15.
- **Group B (S-003):** Steelman Technique applied before devil's advocate per H-16 constraint. Strengthens ideas before attacking them.
- **Group C (S-002, S-004, S-001):** Challenge strategies after strengthening. Order: Devil's Advocate (role-based), Pre-Mortem (forward-looking), Red Team (systematic attack). Executable in parallel.
- **Group D (S-007, S-011):** Verification strategies: Constitutional AI (governance alignment), Chain-of-Verification (evidence coherence).
- **Group E (S-012, S-013):** Decomposition strategies: FMEA (failure modes), Inversion (logic reversal). Executable in parallel.
- **Group F (S-014):** LLM-as-Judge ALWAYS LAST per ordering rules. Scores the complete deliverable after all improvements.

---

## H-16 Compliance Verification

| Constraint | Requirement | This Plan |
|-----------|-------------|-----------|
| S-003 Position | Must precede S-002 | Position 2 < Position 3 ✓ |
| S-002 Position | Must follow S-003 | Position 3 > Position 2 ✓ |
| **Constraint Satisfied** | **Yes** | S-003 (Steelman) executed at step 2, S-002 (Devil's Advocate) executed at step 3 |

**Self-Review Check (H-15):** S-010 (Self-Refine) is positioned at order position 1, ensuring self-review precedes all external critic strategies per H-15 requirement.

**Quality Gate Position (H-17):** S-014 (LLM-as-Judge) is positioned last (order 10) to score the complete revised deliverable after all adversarial strategies have been applied.

---

## Parallelization Groups

Strategies can be executed in parallel within groups, with mandatory sequential dependencies between groups:

```
┌─────────────────────────────────────────┐
│ Group A: S-010 (Self-Refine)            │
│ - Initial self-review                   │
│ - Baseline revisions                    │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│ Group B: S-003 (Steelman)               │
│ - Strengthen core arguments             │
│ - Identify strongest valid interpretations
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│ Group C: Challenge (Parallel)           │
│ - S-002 (Devil's Advocate)              │
│ - S-004 (Pre-Mortem)                    │
│ - S-001 (Red Team)                      │
│ (All 3 executable in parallel)          │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│ Group D: Verification (Parallel)        │
│ - S-007 (Constitutional AI)             │
│ - S-011 (Chain-of-Verification)         │
│ (Both executable in parallel)           │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│ Group E: Decomposition (Parallel)       │
│ - S-012 (FMEA)                          │
│ - S-013 (Inversion)                     │
│ (Both executable in parallel)           │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│ Group F: S-014 (LLM-as-Judge)           │
│ - Final quality scoring                 │
│ - Aggregates all prior feedback         │
│ - MUST RUN LAST                         │
└─────────────────────────────────────────┘
```

**Parallel Execution Notes:**
- **Group C:** All three challenge strategies can run concurrently against the steelman-reinforced deliverable. Each brings distinct perspectives (role play, forward-looking, systematic attack).
- **Group D:** Constitutional and verification strategies can run together; both assume prior challenge strategies have completed.
- **Group E:** FMEA and inversion decomposition strategies can run in parallel; both apply structural analysis independently.
- **Group F:** Must wait for all Groups A-E to complete. LLM-as-Judge scores the final delivery state incorporating all prior strategy feedback.

**Sequential Dependency Enforcement:**
- Group A → B → C → D → E → F (strict ordering)
- Within Group C: No ordering required (all 3 parallel)
- Within Group D: No ordering required (both parallel)
- Within Group E: No ordering required (both parallel)

---

## Strategy Overrides Applied

**User-Specified Modifications:** None.

**Default Behavior:** All 10 required strategies for C4 criticality are included as-is from the SSOT. No user overrides requested or applied.

**Strategy Removals Check:** Not applicable. All 10 required strategies are mandatory for C4 criticality per quality-enforcement.md. Removal of any required strategy would violate quality gate constraints (H-13, H-17).

---

## Self-Review Summary (H-15)

Per H-15 (Self-review before presenting), this plan is self-reviewed against the following criteria:

| Check | Verification | Result |
|-------|--------------|--------|
| **Valid Strategy IDs** | All IDs are S-001, S-002, S-003, S-004, S-007, S-010, S-011, S-012, S-013, S-014 (SSOT selected set) | ✓ PASS |
| **Count Completeness** | Plan includes all 10 selected strategies (0 optional, 10 required for C4) | ✓ PASS |
| **H-16 Constraint** | S-003 position (2) < S-002 position (3): Steelman before Devil's Advocate | ✓ PASS |
| **H-15 Compliance** | S-010 positioned first (position 1) before all external critic strategies | ✓ PASS |
| **H-17 Compliance** | S-014 positioned last (position 10) to score final deliverable state | ✓ PASS |
| **Template Paths** | All 10 template paths verified to exist in `.context/templates/adversarial/s-*.md` | ✓ PASS |
| **Criticality Match** | C4 requested → all 10 required strategies selected (no optional strategies) | ✓ PASS |
| **Ordering Rules** | Recommended execution order (Groups A-F) followed with documented dependencies | ✓ PASS |
| **No Deception** | All constraints, selections, and dependencies transparently listed; nothing omitted | ✓ PASS (P-022 compliance) |

**Pre-Persistence Validation:** All 9 criteria PASS. This selection plan is valid and ready for persistence.

---

## Tournament Context & Iteration Tracking

**Iteration Progression:**
- **Iteration 1 (Prior):** Score 0.747 (REJECTED — below 0.92 threshold)
- **Iteration 2 (Prior):** Score 0.822 (REVISE — within 0.85-0.91 band; targeted revision likely sufficient)
- **Iteration 3 (Prior):** Score 0.848 (REVISE — approaching threshold; consolidated improvements)
- **Iteration 4 (Current):** Target >= 0.95 (Goal: PASS and close gap to 1.0)

**Revision 8 Improvements Summary (from deliverable context):**
- Synthesis Hypothesis Validation Protocol (PM-001) — NEW framework for validity gating
- MCP maintenance owner succession protocol (PM-002) — Governance improvement
- 12 Major improvements and 8 Minor improvements across all sections
- 5 Steelman incorporations from prior iteration critique
- Round 1 fractional weight corrections
- Framework substitution path formalization (AI-First Design vs. Service Blueprinting decision)
- User research gap escalation to V2 scope

**Quality Trajectory:** Steady convergence (0.747 → 0.822 → 0.848) indicates the iterative revision process is working. Iteration 4 should complete the tournament with >= 0.95 score if the feedback from Iteration 3 critics has been effectively incorporated.

---

## Execution Handoff Information

**For adv-executor Agent:**

This plan is ready for handoff to the adv-executor agent to begin tournament strategy execution.

- **Deliverable Input:** projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md
- **Template Directory:** `.context/templates/adversarial/`
- **Strategy Sequence:** Groups A through F in order (parallel execution within groups)
- **Quality Gate:** Target >= 0.95 (provisional; final threshold per S-014 rubric)
- **Prior Context:** Iteration 3 score 0.848 with feedback summary available in prior tournament documentation

**Success Criteria for This Iteration:**
1. All 10 strategies execute without errors
2. S-014 final score >= 0.95 (PASS threshold)
3. Dimension-level breakdown provides actionable refinement signals
4. All prior iteration feedback has been addressed or documented as design decisions

---

## Related Documentation

- **SSOT Source:** `.context/rules/quality-enforcement.md` (Criticality Levels, Strategy Catalog, Implementation)
- **Agent Definition:** `skills/adversary/agents/adv-selector.md` (this agent's role)
- **Executor Reference:** `skills/adversary/agents/adv-executor.md` (execution logic)
- **Scorer Reference:** `skills/adversary/agents/adv-scorer.md` (S-014 rubric application)
- **Prior Tournament Results:** Available in PROJ-020 work/analysis/ directory (iteration 1-3 plans and scores)

---

*Plan Version: 1.0*
*Constitutional Compliance: P-003 (no subagent recursion), P-020 (user authority), P-022 (no deception)*
*SSOT: `.context/rules/quality-enforcement.md` v1.6.0*
*Agent: adv-selector (Strategy Selector)*
*Enforcement: H-13 (quality threshold), H-14 (creator-critic cycle), H-15 (self-review), H-16 (steelman before critique), H-17 (quality scoring), H-18 (constitutional compliance)*
