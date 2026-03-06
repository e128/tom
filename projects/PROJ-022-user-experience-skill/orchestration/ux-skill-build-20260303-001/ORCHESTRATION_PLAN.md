# PROJ-022 /user-experience Skill: Orchestration Plan

> **Document ID:** PROJ-022-ORCH-PLAN
> **Workflow ID:** ux-skill-build-20260303-001
> **Date:** 2026-03-03
> **Status:** ACTIVE
> **GitHub Issue:** [#138](https://github.com/geekatron/jerry/issues/138)

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0: Workflow Overview](#l0-workflow-overview) | Stakeholder summary |
| [L1: Technical Plan](#l1-technical-plan) | Workflow diagram, pipeline definitions, barriers |
| [L2: Implementation Details](#l2-implementation-details) | State schema, path configuration, recovery strategies |
| [Disclaimer](#disclaimer) | Agent-generated plan notice |

---

## L0: Workflow Overview

The `/user-experience` skill adds a comprehensive UX methodology suite to the Jerry Framework. It consists of a parent orchestrator (`/user-experience`) that routes across 10 pluggable sub-skills, each targeting a specific UX discipline. These sub-skills are built incrementally across 5 criteria-gated waves, ensuring each layer of the skill stack is validated before the next is built.

Every artifact in this project passes a C4 adversary quality gate (>= 0.95 composite score using all 10 adversarial strategies) before being committed. This level of rigor is warranted because the skill registers public-facing slash commands, modifies framework routing rules, and establishes governance patterns that future skills will inherit.

The project spans 8 pipelines, ~72 artifacts, and 5 wave-transition sync barriers. Cross-session continuity is maintained via ORCHESTRATION.yaml which acts as the machine-readable SSOT for all state, progress, and next actions across sessions.

---

## L1: Technical Plan

### Workflow Diagram (ASCII)

```
PROJ-022: /user-experience Skill Build
Workflow: ux-skill-build-20260303-001
Criticality: C4 | Quality Threshold: >= 0.95

PIPELINE 1: Foundation (EPIC-001)
─────────────────────────────────────────────────────────────────────────
│ P1: Parent SKILL.md
│    ↓
│ P2: ux-orchestrator.md (T5, Opus, Integrative)
│    ↓
│ P3: ux-orchestrator.governance.yaml
│    ↓
│ P4: Rule Files ×5 [PARALLEL]
│    │  ux-routing-rules.md
│    │  synthesis-validation.md
│    │  wave-progression.md
│    │  mcp-coordination.md
│    │  ci-checks.md
│    ↓
│ P5: Templates ×2 [PARALLEL]
│    │  kickoff-signoff-template.md
│    │  wave-signoff-template.md
│    ↓
│ P6: KICKOFF-SIGNOFF.md
│
│ Each artifact: Creator → C4 Tournament (10 strategies) → Commit
─────────────────────────────────────────────────────────────────────────
                         │
             ╔═══════════════════════╗
             ║  BARRIER: Wave 0→1    ║
             ║  KICKOFF-SIGNOFF.md   ║
             ║  Quality Gate >= 0.95 ║
             ╚═══════════════════════╝
                    │               │
                    ↓               ↓
PIPELINE 2: Wave 1        PIPELINE 8: Registration
(EPIC-002)                (EPIC-008) [can start after Foundation]
                 │
┌────────────────┴─────────────────┐
│ [PARALLEL]                       │
│ Sub-skill A: /ux-heuristic-eval  │  Sub-skill B: /ux-jtbd
│ Agent: ux-heuristic-evaluator    │  Agent: ux-jtbd-analyst
│ Tier T3 | Systematic | Haiku*    │  Tier T3 | Divergent | Sonnet
│ (*benchmark-gated, ↑Sonnet<0.90) │
│ 6 artifacts                      │  6 artifacts
└────────────────┬─────────────────┘
                 │ [both complete]
                 ↓
         Wave 1 Cross-Framework Tests
                 ↓
         WAVE-1-SIGNOFF.md
                 │
     ╔═══════════════════════╗
     ║  BARRIER: Wave 1→2    ║
     ║  WAVE-1-SIGNOFF.md    ║
     ║  Quality Gate >= 0.95 ║
     ╚═══════════════════════╝
          │            │
          ↓            ↓
PIPELINE 3: Wave 2    PIPELINE 7: Integration
(EPIC-003)            (EPIC-007) [starts here]
          │
┌─────────┴──────────┐
│ /ux-lean-ux        │  /ux-heart-metrics
│ T3|Systematic|Snnt │  T2|Systematic|Sonnet
│ 7 artifacts        │  4 artifacts
└─────────┬──────────┘
          ↓
   Wave 2 Tests + WAVE-2-SIGNOFF.md
          │
  ╔═══════════════════╗
  ║  BARRIER: W2→W3  ║
  ║  >= 0.95         ║
  ╚═══════════════════╝
          ↓
PIPELINE 4: Wave 3 (EPIC-004)
┌───────────────────────────────────┐
│ /ux-atomic-design    │  /ux-inclusive-design
│ T3|Systematic|Sonnet │  T3|Systematic|Sonnet
│ 6 artifacts          │  7 artifacts
└─────────────────┬─────────────────┘
                  ↓
     Wave 3 Tests + WAVE-3-SIGNOFF.md
                  │
         ╔════════════════╗
         ║  BARRIER: W3→4 ║
         ╚════════════════╝
                  ↓
PIPELINE 5: Wave 4 (EPIC-005) [PARALLEL sub-skills only]
┌────────────────────────────────────┐
│ /ux-behavior-design │  /ux-kano-model
│ T2|Convergent|Sonnet│  T2|Convergent|Sonnet
│ 5 artifacts         │  6 artifacts
└──────────────┬──────────────────────┘
               │ [both complete; signoff in Pipeline 6]
               ↓
PIPELINE 6: Wave 5 (EPIC-006)
┌────────────────────────────────────────────────┐
│ /ux-design-sprint        │  /ux-ai-first-design
│ T3|Systematic|Opus       │  T3|Divergent|Opus
│ 6 artifacts              │  [CONDITIONAL:
│                          │   Enabler DONE
│                          │   + WSM >= 7.80]
│                          │  6 artifacts
└────────────────┬─────────────────────────────┘
                 ↓
     WAVE-4-SIGNOFF.md (retrospective for EPIC-005)
                 ↓
     WAVE-5-SIGNOFF.md
                 │
       ╔═════════════════╗
       ║  BARRIER: W4→W5 ║
       ╚═════════════════╝

PIPELINE 7: Integration (EPIC-007) [runs after Wave 1]
  → Cross-framework handoff tests (JTBD→Sprint, LeanUX→HEART)
  → Failure mode documentation
  → Purple Team security tests (MCP OAuth, P-003, creds, synthesis, wave bypass)

PIPELINE 8: Registration (EPIC-008) [runs after Foundation]
  → CLAUDE.md skill table update
  → AGENTS.md 11-agent registry update
  → .context/rules/mandatory-skill-usage.md trigger map update [auto-C3 AE-002]
  → skills/user-experience/rules/metrics-plan.md
```

### Pipeline Definitions

| Pipeline | Epic | Name | Entry Gate | Phases | Execution | Sub-skill Count |
|----------|------|------|-----------|--------|-----------|----------------|
| Pipeline 1 | EPIC-001 | Foundation | None | 6 | Sequential | 0 (orchestrator) |
| Pipeline 2 | EPIC-002 | Wave 1 | KICKOFF-SIGNOFF.md | 4 | Parallel then sequential | 2 |
| Pipeline 3 | EPIC-003 | Wave 2 | WAVE-1-SIGNOFF.md | 4 | Parallel then sequential | 2 |
| Pipeline 4 | EPIC-004 | Wave 3 | WAVE-2-SIGNOFF.md | 4 | Parallel then sequential | 2 |
| Pipeline 5 | EPIC-005 | Wave 4 | WAVE-3-SIGNOFF.md | 2 | Parallel | 2 |
| Pipeline 6 | EPIC-006 | Wave 5 | Wave 4 sub-skills done | 4 | Parallel then sequential | 2 (1 conditional) |
| Pipeline 7 | EPIC-007 | Integration | WAVE-1-SIGNOFF.md | 2 | Sequential | 0 (testing) |
| Pipeline 8 | EPIC-008 | Registration | KICKOFF-SIGNOFF.md | 2 | Sequential | 0 (registration) |

### Agent Assignments

| Sub-skill | Agent | Tier | Cognitive Mode | Model | Notes |
|-----------|-------|------|---------------|-------|-------|
| `/user-experience` (parent) | `ux-orchestrator` | T5 | Integrative | Opus | Routes across all 10 sub-skills |
| `/ux-heuristic-eval` | `ux-heuristic-evaluator` | T3 | Systematic | Haiku | Benchmark-gated; escalate to Sonnet if score < 0.90 |
| `/ux-jtbd` | `ux-jtbd-analyst` | T3 | Divergent | Sonnet | Jobs-to-be-Done methodology |
| `/ux-lean-ux` | `ux-lean-ux-facilitator` | T3 | Systematic | Sonnet | Lean UX hypothesis-driven |
| `/ux-heart-metrics` | `ux-heart-analyst` | T2 | Systematic | Sonnet | Google HEART framework |
| `/ux-atomic-design` | `ux-atomic-architect` | T3 | Systematic | Sonnet | Atomic design system patterns |
| `/ux-inclusive-design` | `ux-inclusive-evaluator` | T3 | Systematic | Sonnet | WCAG + inclusive design |
| `/ux-behavior-design` | `ux-behavior-diagnostician` | T2 | Convergent | Sonnet | Fogg B=MAP framework |
| `/ux-kano-model` | `ux-kano-analyst` | T2 | Convergent | Sonnet | Kano feature classification |
| `/ux-design-sprint` | `ux-sprint-facilitator` | T3 | Systematic | Opus | GV Design Sprint 5-day |
| `/ux-ai-first-design` | `ux-ai-design-guide` | T3 | Divergent | Opus | CONDITIONAL: Enabler + WSM >= 7.80 |

**P-003 Enforcement:** All sub-skill agents (T2/T3) MUST NOT declare `Task` in `tools`. Only `ux-orchestrator` (T5) has Task access. Enforced by schema validation and CI check (FEAT-002: ci-checks.md).

### Wave Gate Summary

| Wave | Entry | Exit | Unlocks |
|------|-------|------|---------|
| Wave 0 (Foundation) | None | KICKOFF-SIGNOFF.md | Wave 1, Registration |
| Wave 1 | KICKOFF-SIGNOFF.md | WAVE-1-SIGNOFF.md | Wave 2, Integration |
| Wave 2 | WAVE-1-SIGNOFF.md | WAVE-2-SIGNOFF.md | Wave 3 |
| Wave 3 | WAVE-2-SIGNOFF.md | WAVE-3-SIGNOFF.md | Wave 4 |
| Wave 4 | WAVE-3-SIGNOFF.md | WAVE-4-SIGNOFF.md (in Pipeline 6) | Wave 5 |
| Wave 5 | WAVE-4-SIGNOFF.md | WAVE-5-SIGNOFF.md | Project complete |

### Sync Barriers

| Barrier ID | Trigger Condition | Quality Gate | Unblocks |
|-----------|-----------------|-------------|---------|
| barrier-wave0-to-wave1 | pipeline_foundation.phase.6 complete | C4 >= 0.95, all 10 strategies | Pipeline 2, Pipeline 8 |
| barrier-wave1-to-wave2 | pipeline_wave1.phase.4 complete | C4 >= 0.95, all 10 strategies | Pipeline 3, Pipeline 7 |
| barrier-wave2-to-wave3 | pipeline_wave2.phase.4 complete | C4 >= 0.95, all 10 strategies | Pipeline 4 |
| barrier-wave3-to-wave4 | pipeline_wave3.phase.4 complete | C4 >= 0.95, all 10 strategies | Pipeline 5 |
| barrier-wave4-to-wave5 | pipeline_wave4 phases 1+2 complete | C4 >= 0.95, all 10 strategies | Pipeline 6 |

---

## L2: Implementation Details

### State Schema Reference

Machine-readable state is maintained in:
```
projects/PROJ-022-user-experience-skill/orchestration/ux-skill-build-20260303-001/ORCHESTRATION.yaml
```

Key YAML sections:
- `workflow` — Metadata, patterns, constraints
- `paths` — Dynamic path scheme (no hardcoded pipeline names)
- `pipelines` — 8 pipeline definitions with phases and artifact paths
- `wave_gates` — Entry/exit criteria for each wave
- `barriers` — 5 sync barriers with quality gate configuration
- `adversarial` — C4 strategy set, thresholds, scoring dimensions
- `execution_queue` — 14 execution groups with dependency ordering
- `quality` — Live quality scores (populated during execution)
- `checkpoints` — Per-artifact commit checkpoint log
- `resumption` — Cross-session recovery state and file-read order

### Dynamic Path Configuration

All artifact paths resolve dynamically — no hardcoded pipeline names:

```yaml
# Base pattern
base: "orchestration/ux-skill-build-20260303-001/"
pipeline: "{base}{pipeline_alias}/{phase_id}/"
barrier: "{base}cross-pollination/{barrier_id}/{direction}/"

# Skill artifacts use canonical skills/ tree
skills_root: "skills/"

# Examples:
# Orchestration artifact: orchestration/ux-skill-build-20260303-001/foundation/phase-1/
# Skill artifact:         skills/user-experience/SKILL.md
# Skill artifact:         skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md
```

### Per-Artifact Commit Strategy

Every artifact that passes the C4 quality gate receives its own git commit:
```
feat(PROJ-022): add {artifact-name} [C4: {score}] [skip-bump]
```

ORCHESTRATION.yaml is updated and committed alongside each artifact. This provides maximum revert granularity — any single artifact can be reverted without affecting others.

### Adversarial Quality Configuration

- **Criticality:** C4 (irreversible — registers public skill surface, modifies governance files)
- **Threshold:** 0.95 (user requirement override; framework default is 0.92)
- **Max iterations:** 6 (user requirement; framework default H-14 is 3 minimum)
- **Strategy set:** All 10 (S-001 through S-014, excluding excluded strategies)
- **H-16 enforced:** S-003 (Steelman) MUST precede S-002 (Devil's Advocate) in every review

**Auto-escalation triggers active:**
- AE-001: Does not apply (not touching JERRY_CONSTITUTION.md)
- AE-002: APPLIES to Pipeline 8 `.context/rules/mandatory-skill-usage.md` — auto-C3 minimum (already C4 per workflow)
- AE-003: Does not apply (no ADRs in scope)

**Schema validation:** Every `.governance.yaml` file validates against `docs/schemas/agent-governance-v1.schema.json` before LLM-based quality scoring (H-34).

### Artifact Count by Pipeline

| Pipeline | Features | Artifact Count |
|----------|----------|---------------|
| Pipeline 1 (Foundation) | FEAT-001 to FEAT-004 | 11 |
| Pipeline 2 (Wave 1) | FEAT-005 to FEAT-008 | 14 |
| Pipeline 3 (Wave 2) | FEAT-009 to FEAT-012 | 13 |
| Pipeline 4 (Wave 3) | FEAT-013 to FEAT-016 | 14 |
| Pipeline 5 (Wave 4) | FEAT-017 to FEAT-018 | 10 |
| Pipeline 6 (Wave 5) | FEAT-019 to FEAT-022 | 12 + 2 signoffs |
| Pipeline 7 (Integration) | FEAT-023 to FEAT-024 | 3 |
| Pipeline 8 (Registration) | FEAT-025 to FEAT-026 | 4 |
| **Total** | 26 features | **~72 artifacts** |

### Recovery Strategies

**Cross-session resumption:**
1. Read `ORCHESTRATION.yaml` — section `resumption.recovery_state` identifies the current state
2. Read `ORCHESTRATION_WORKTRACKER.md` — per-artifact execution log with quality scores
3. Check `resumption.next_actions` for the immediate next task
4. Resume from the last committed artifact (per-artifact commits provide fine-grained recovery)

**Quality gate failure recovery:**
- If an artifact fails C4 after 6 iterations: document the delta, capture residual findings, mark `quality_verdict: MAX_ITERATIONS`, and proceed with documented rationale
- If a wave signoff fails: re-examine the sub-skill artifacts that fed it; the cross-framework tests may surface specific defects to address

**Conditional sub-skill (FEAT-020):**
- If activation criteria not met at Wave 5 entry: formally defer FEAT-020, document the WSM score and blocker in ORCHESTRATION.yaml, proceed to WAVE-5-SIGNOFF.md with documented justification

---

## Disclaimer

This orchestration plan was generated by the orch-planner agent (v2.2.0) on 2026-03-03 for project PROJ-022-user-experience-skill. The plan is based on the authoritative specification in GitHub Issue [#138](https://github.com/geekatron/jerry/issues/138) and the WORKTRACKER.md decomposition. Human review is recommended before execution begins, particularly the agent specifications (issue comments 2-3) and the 27 acceptance criteria (issue comment 1). This plan does not constitute official documentation of any implementation; it is a planning artifact subject to revision as execution progresses.
