# PROJ-022 Orchestration Worktracker

> **Workflow ID:** ux-skill-build-20260303-001
> **Project:** PROJ-022-user-experience-skill
> **Criticality:** C4 | **Quality Threshold:** >= 0.95
> **Created:** 2026-03-03
> **Status:** NOT STARTED

## Document Sections

| Section | Purpose |
|---------|---------|
| [Status Summary](#status-summary) | Pipeline and wave progress at a glance |
| [EPIC-001: Foundation](#epic-001-foundation) | Per-artifact execution log, scores, commits |
| [EPIC-002: Wave 1](#epic-002-wave-1) | Per-artifact execution log |
| [EPIC-003: Wave 2](#epic-003-wave-2) | Per-artifact execution log |
| [EPIC-004: Wave 3](#epic-004-wave-3) | Per-artifact execution log |
| [EPIC-005: Wave 4](#epic-005-wave-4) | Per-artifact execution log |
| [EPIC-006: Wave 5](#epic-006-wave-5) | Per-artifact execution log |
| [EPIC-007: Integration](#epic-007-integration) | Per-artifact execution log |
| [EPIC-008: Registration](#epic-008-registration) | Per-artifact execution log |
| [Wave Gate Log](#wave-gate-log) | Barrier passage history |
| [Quality Score History](#quality-score-history) | Per-artifact C4 tournament scores |
| [Decision Log](#decision-log) | Deviations, conditional decisions, deferrals |

---

## Status Summary

| Pipeline | Epic | Status | Artifacts Done | Gate Status |
|----------|------|--------|---------------|------------|
| Foundation | EPIC-001 | NOT STARTED | 0 / 11 | KICKOFF-SIGNOFF: PENDING |
| Wave 1 | EPIC-002 | BLOCKED (Foundation) | 0 / 14 | WAVE-1-SIGNOFF: PENDING |
| Wave 2 | EPIC-003 | BLOCKED (Wave 1) | 0 / 13 | WAVE-2-SIGNOFF: PENDING |
| Wave 3 | EPIC-004 | BLOCKED (Wave 2) | 0 / 14 | WAVE-3-SIGNOFF: PENDING |
| Wave 4 | EPIC-005 | BLOCKED (Wave 3) | 0 / 10 | WAVE-4-SIGNOFF: PENDING |
| Wave 5 | EPIC-006 | BLOCKED (Wave 4) | 0 / 14 | WAVE-5-SIGNOFF: PENDING |
| Integration | EPIC-007 | BLOCKED (Wave 1) | 0 / 3 | N/A |
| Registration | EPIC-008 | BLOCKED (Foundation) | 0 / 4 | N/A |
| **TOTAL** | | **NOT STARTED** | **0 / ~72** | |

---

## EPIC-001: Foundation

### FEAT-001: Parent SKILL.md + Orchestrator Agent

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 1 | Parent SKILL.md | `skills/user-experience/SKILL.md` | NOT STARTED | — | — | — | — |
| 2 | Orchestrator agent def | `skills/user-experience/agents/ux-orchestrator.md` | NOT STARTED | — | — | — | — |
| 3 | Orchestrator governance | `skills/user-experience/agents/ux-orchestrator.governance.yaml` | NOT STARTED | — | — | — | — |

### FEAT-002: Routing and Governance Rules

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 4 | Routing rules | `skills/user-experience/rules/ux-routing-rules.md` | NOT STARTED | — | — | — | — |
| 5 | Synthesis validation | `skills/user-experience/rules/synthesis-validation.md` | NOT STARTED | — | — | — | — |
| 6 | Wave progression | `skills/user-experience/rules/wave-progression.md` | NOT STARTED | — | — | — | — |
| 7 | MCP coordination | `skills/user-experience/rules/mcp-coordination.md` | NOT STARTED | — | — | — | — |
| 8 | CI checks | `skills/user-experience/rules/ci-checks.md` | NOT STARTED | — | — | — | — |

### FEAT-003: Templates

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 9 | Kickoff signoff template | `skills/user-experience/templates/kickoff-signoff-template.md` | NOT STARTED | — | — | — | — |
| 10 | Wave signoff template | `skills/user-experience/templates/wave-signoff-template.md` | NOT STARTED | — | — | — | — |

### FEAT-004: Kickoff Signoff

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 11 | KICKOFF-SIGNOFF.md | `skills/user-experience/work/KICKOFF-SIGNOFF.md` | NOT STARTED | — | — | — | — |

**EPIC-001 Progress:** 0 / 11 artifacts | Gate: PENDING

---

## EPIC-002: Wave 1

> **Blocked by:** `skills/user-experience/work/KICKOFF-SIGNOFF.md`

### FEAT-005: /ux-heuristic-eval Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 12 | SKILL.md | `skills/ux-heuristic-eval/SKILL.md` | NOT STARTED | — | — | — | — |
| 13 | Agent definition | `skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md` | NOT STARTED | — | — | — | — |
| 14 | Governance YAML | `skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.governance.yaml` | NOT STARTED | — | — | — | — |
| 15 | Heuristic eval rules | `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md` | NOT STARTED | — | — | — | — |
| 16 | MCP runbook | `skills/ux-heuristic-eval/rules/mcp-runbook.md` | NOT STARTED | — | — | — | — |
| 17 | Report template | `skills/ux-heuristic-eval/templates/heuristic-report-template.md` | NOT STARTED | — | — | — | — |

### FEAT-006: /ux-jtbd Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 18 | SKILL.md | `skills/ux-jtbd/SKILL.md` | NOT STARTED | — | — | — | — |
| 19 | Agent definition | `skills/ux-jtbd/agents/ux-jtbd-analyst.md` | NOT STARTED | — | — | — | — |
| 20 | Governance YAML | `skills/ux-jtbd/agents/ux-jtbd-analyst.governance.yaml` | NOT STARTED | — | — | — | — |
| 21 | JTBD methodology rules | `skills/ux-jtbd/rules/jtbd-methodology-rules.md` | NOT STARTED | — | — | — | — |
| 22 | Job statement template | `skills/ux-jtbd/templates/job-statement-template.md` | NOT STARTED | — | — | — | — |
| 23 | Switch interview guide | `skills/ux-jtbd/templates/switch-interview-guide.md` | NOT STARTED | — | — | — | — |

### FEAT-007: Wave 1 Cross-Framework Testing

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 24 | Cross-framework test results | `skills/user-experience/work/wave-1-cross-framework-tests.md` | NOT STARTED | — | — | — | — |

### FEAT-008: Wave 1 Signoff

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 25 | WAVE-1-SIGNOFF.md | `skills/user-experience/work/WAVE-1-SIGNOFF.md` | NOT STARTED | — | — | — | — |

**EPIC-002 Progress:** 0 / 14 artifacts | Gate: PENDING

---

## EPIC-003: Wave 2

> **Blocked by:** `skills/user-experience/work/WAVE-1-SIGNOFF.md`

### FEAT-009: /ux-lean-ux Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 26 | SKILL.md | `skills/ux-lean-ux/SKILL.md` | NOT STARTED | — | — | — | — |
| 27 | Agent definition | `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` | NOT STARTED | — | — | — | — |
| 28 | Governance YAML | `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.governance.yaml` | NOT STARTED | — | — | — | — |
| 29 | Lean UX methodology rules | `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md` | NOT STARTED | — | — | — | — |
| 30 | MCP runbook | `skills/ux-lean-ux/rules/mcp-runbook.md` | NOT STARTED | — | — | — | — |
| 31 | Hypothesis backlog template | `skills/ux-lean-ux/templates/hypothesis-backlog-template.md` | NOT STARTED | — | — | — | — |
| 32 | Assumption map template | `skills/ux-lean-ux/templates/assumption-map-template.md` | NOT STARTED | — | — | — | — |

### FEAT-010: /ux-heart-metrics Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 33 | SKILL.md | `skills/ux-heart-metrics/SKILL.md` | NOT STARTED | — | — | — | — |
| 34 | Agent definition | `skills/ux-heart-metrics/agents/ux-heart-analyst.md` | NOT STARTED | — | — | — | — |
| 35 | Governance YAML | `skills/ux-heart-metrics/agents/ux-heart-analyst.governance.yaml` | NOT STARTED | — | — | — | — |
| 36 | HEART methodology rules | `skills/ux-heart-metrics/rules/heart-methodology-rules.md` | NOT STARTED | — | — | — | — |

### FEAT-011: Wave 2 Cross-Framework Testing

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 37 | Cross-framework test results | `skills/user-experience/work/wave-2-cross-framework-tests.md` | NOT STARTED | — | — | — | — |

### FEAT-012: Wave 2 Signoff

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 38 | WAVE-2-SIGNOFF.md | `skills/user-experience/work/WAVE-2-SIGNOFF.md` | NOT STARTED | — | — | — | — |

**EPIC-003 Progress:** 0 / 13 artifacts | Gate: PENDING

---

## EPIC-004: Wave 3

> **Blocked by:** `skills/user-experience/work/WAVE-2-SIGNOFF.md`

### FEAT-013: /ux-atomic-design Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 39 | SKILL.md | `skills/ux-atomic-design/SKILL.md` | NOT STARTED | — | — | — | — |
| 40 | Agent definition | `skills/ux-atomic-design/agents/ux-atomic-architect.md` | NOT STARTED | — | — | — | — |
| 41 | Governance YAML | `skills/ux-atomic-design/agents/ux-atomic-architect.governance.yaml` | NOT STARTED | — | — | — | — |
| 42 | Atomic design rules | `skills/ux-atomic-design/rules/atomic-design-rules.md` | NOT STARTED | — | — | — | — |
| 43 | MCP runbook | `skills/ux-atomic-design/rules/mcp-runbook.md` | NOT STARTED | — | — | — | — |
| 44 | Component inventory template | `skills/ux-atomic-design/templates/component-inventory-template.md` | NOT STARTED | — | — | — | — |

### FEAT-014: /ux-inclusive-design Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 45 | SKILL.md | `skills/ux-inclusive-design/SKILL.md` | NOT STARTED | — | — | — | — |
| 46 | Agent definition | `skills/ux-inclusive-design/agents/ux-inclusive-evaluator.md` | NOT STARTED | — | — | — | — |
| 47 | Governance YAML | `skills/ux-inclusive-design/agents/ux-inclusive-evaluator.governance.yaml` | NOT STARTED | — | — | — | — |
| 48 | Inclusive design rules | `skills/ux-inclusive-design/rules/inclusive-design-rules.md` | NOT STARTED | — | — | — | — |
| 49 | MCP runbook | `skills/ux-inclusive-design/rules/mcp-runbook.md` | NOT STARTED | — | — | — | — |
| 50 | Persona spectrum template | `skills/ux-inclusive-design/templates/persona-spectrum-template.md` | NOT STARTED | — | — | — | — |
| 51 | Accessibility report template | `skills/ux-inclusive-design/templates/accessibility-report-template.md` | NOT STARTED | — | — | — | — |

### FEAT-015: Wave 3 Cross-Framework Testing

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 52 | Cross-framework test results | `skills/user-experience/work/wave-3-cross-framework-tests.md` | NOT STARTED | — | — | — | — |

### FEAT-016: Wave 3 Signoff

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 53 | WAVE-3-SIGNOFF.md | `skills/user-experience/work/WAVE-3-SIGNOFF.md` | NOT STARTED | — | — | — | — |

**EPIC-004 Progress:** 0 / 14 artifacts | Gate: PENDING

---

## EPIC-005: Wave 4

> **Blocked by:** `skills/user-experience/work/WAVE-3-SIGNOFF.md`
> **Note:** Wave 4 signoff (FEAT-021) is produced in EPIC-006 / Pipeline 6

### FEAT-017: /ux-behavior-design Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 54 | SKILL.md | `skills/ux-behavior-design/SKILL.md` | NOT STARTED | — | — | — | — |
| 55 | Agent definition | `skills/ux-behavior-design/agents/ux-behavior-diagnostician.md` | NOT STARTED | — | — | — | — |
| 56 | Governance YAML | `skills/ux-behavior-design/agents/ux-behavior-diagnostician.governance.yaml` | NOT STARTED | — | — | — | — |
| 57 | Fogg behavior rules | `skills/ux-behavior-design/rules/fogg-behavior-rules.md` | NOT STARTED | — | — | — | — |
| 58 | B=MAP diagnosis template | `skills/ux-behavior-design/templates/bmap-diagnosis-template.md` | NOT STARTED | — | — | — | — |

### FEAT-018: /ux-kano-model Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 59 | SKILL.md | `skills/ux-kano-model/SKILL.md` | NOT STARTED | — | — | — | — |
| 60 | Agent definition | `skills/ux-kano-model/agents/ux-kano-analyst.md` | NOT STARTED | — | — | — | — |
| 61 | Governance YAML | `skills/ux-kano-model/agents/ux-kano-analyst.governance.yaml` | NOT STARTED | — | — | — | — |
| 62 | Kano methodology rules | `skills/ux-kano-model/rules/kano-methodology-rules.md` | NOT STARTED | — | — | — | — |
| 63 | Kano survey template | `skills/ux-kano-model/templates/kano-survey-template.md` | NOT STARTED | — | — | — | — |
| 64 | Feature priority template | `skills/ux-kano-model/templates/feature-priority-template.md` | NOT STARTED | — | — | — | — |

**EPIC-005 Progress:** 0 / 10 artifacts | Gate: PENDING (signoff in EPIC-006)

---

## EPIC-006: Wave 5

> **Blocked by:** Wave 4 sub-skills complete (EPIC-005 phases 1+2)
> **FEAT-020 conditional:** Requires Enabler DONE + WSM >= 7.80

### FEAT-019: /ux-design-sprint Sub-Skill

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 65 | SKILL.md | `skills/ux-design-sprint/SKILL.md` | NOT STARTED | — | — | — | — |
| 66 | Agent definition | `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` | NOT STARTED | — | — | — | — |
| 67 | Governance YAML | `skills/ux-design-sprint/agents/ux-sprint-facilitator.governance.yaml` | NOT STARTED | — | — | — | — |
| 68 | Design sprint rules | `skills/ux-design-sprint/rules/design-sprint-rules.md` | NOT STARTED | — | — | — | — |
| 69 | MCP runbook | `skills/ux-design-sprint/rules/mcp-runbook.md` | NOT STARTED | — | — | — | — |
| 70 | Sprint day templates (Day 1-4) | `skills/ux-design-sprint/templates/sprint-day-*.md` | NOT STARTED | — | — | — | — |

### FEAT-020: /ux-ai-first-design Sub-Skill (CONDITIONAL)

> Activation criteria: Enabler DONE AND WSM >= 7.80

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 71 | SKILL.md | `skills/ux-ai-first-design/SKILL.md` | CONDITIONAL | — | — | — | — |
| 72 | Agent definition | `skills/ux-ai-first-design/agents/ux-ai-design-guide.md` | CONDITIONAL | — | — | — | — |
| 73 | Governance YAML | `skills/ux-ai-first-design/agents/ux-ai-design-guide.governance.yaml` | CONDITIONAL | — | — | — | — |
| 74 | AI-first design rules | `skills/ux-ai-first-design/rules/ai-first-design-rules.md` | CONDITIONAL | — | — | — | — |
| 75 | MCP runbook | `skills/ux-ai-first-design/rules/mcp-runbook.md` | CONDITIONAL | — | — | — | — |
| 76 | AI interaction spec template | `skills/ux-ai-first-design/templates/ai-interaction-spec-template.md` | CONDITIONAL | — | — | — | — |

### FEAT-021: Wave 4 Signoff (retrospective for EPIC-005)

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 77 | WAVE-4-SIGNOFF.md | `skills/user-experience/work/WAVE-4-SIGNOFF.md` | NOT STARTED | — | — | — | — |

### FEAT-022: Wave 5 Signoff

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 78 | WAVE-5-SIGNOFF.md | `skills/user-experience/work/WAVE-5-SIGNOFF.md` | NOT STARTED | — | — | — | — |

**EPIC-006 Progress:** 0 / 14 artifacts (8 mandatory + 6 conditional) | Gate: PENDING

---

## EPIC-007: Integration

> **Blocked by:** `skills/user-experience/work/WAVE-1-SIGNOFF.md`

### FEAT-023: Cross-Framework Handoff Testing

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 79 | Cross-framework handoff tests | `skills/user-experience/work/cross-framework-handoff-tests.md` | NOT STARTED | — | — | — | — |
| 80 | Failure mode documentation | `skills/user-experience/work/failure-mode-documentation.md` | NOT STARTED | — | — | — | — |

### FEAT-024: Purple Team Security Testing

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 81 | Purple team results | `skills/user-experience/work/purple-team-results.md` | NOT STARTED | — | — | — | — |

**EPIC-007 Progress:** 0 / 3 artifacts

---

## EPIC-008: Registration

> **Blocked by:** `skills/user-experience/work/KICKOFF-SIGNOFF.md`
> **Note:** `.context/rules/mandatory-skill-usage.md` modification is auto-C3 per AE-002 (already C4)

### FEAT-025: Framework Registration

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 82 | CLAUDE.md update | `CLAUDE.md` | NOT STARTED | — | — | — | — |
| 83 | AGENTS.md update (11 agents) | `AGENTS.md` | NOT STARTED | — | — | — | — |
| 84 | Trigger map update | `.context/rules/mandatory-skill-usage.md` | NOT STARTED | — | — | — | — |

### FEAT-026: Metrics Plan

| # | Artifact | Output Path | Status | Iterations | Score | Verdict | Commit SHA |
|---|----------|------------|--------|-----------|-------|---------|-----------|
| 85 | Metrics plan | `skills/user-experience/rules/metrics-plan.md` | NOT STARTED | — | — | — | — |

**EPIC-008 Progress:** 0 / 4 artifacts

---

## Wave Gate Log

| Gate | Status | Gate Artifact | Score | Verdict | Date | Notes |
|------|--------|--------------|-------|---------|------|-------|
| Wave 0 → Wave 1 | PENDING | `KICKOFF-SIGNOFF.md` | — | — | — | |
| Wave 1 → Wave 2 | PENDING | `WAVE-1-SIGNOFF.md` | — | — | — | |
| Wave 2 → Wave 3 | PENDING | `WAVE-2-SIGNOFF.md` | — | — | — | |
| Wave 3 → Wave 4 | PENDING | `WAVE-3-SIGNOFF.md` | — | — | — | |
| Wave 4 → Wave 5 | PENDING | `WAVE-4-SIGNOFF.md` | — | — | — | Produced inside Pipeline 6 |

---

## Quality Score History

> Populated as artifacts complete C4 quality gate.
> Format: `artifact-id: [iteration_scores...] → VERDICT`

```
# Foundation
SKILL.md (ux-orchestrator):      []
ux-orchestrator.md:              []
ux-orchestrator.governance.yaml: []
ux-routing-rules.md:             []
synthesis-validation.md:         []
wave-progression.md:             []
mcp-coordination.md:             []
ci-checks.md:                    []
kickoff-signoff-template.md:     []
wave-signoff-template.md:        []
KICKOFF-SIGNOFF.md:              []

# Wave 1 (populated when executed)
# Wave 2 (populated when executed)
# ... etc.
```

---

## Decision Log

> Record deviations, conditional trigger decisions, and quality plateau resolutions here.

| Date | Decision | Rationale | Impact |
|------|----------|-----------|--------|
| 2026-03-03 | ORCHESTRATION.yaml initialized | Project setup — orch-planner agent | None |
| — | FEAT-020 conditional status | WSM evaluation deferred to Wave 5 entry | FEAT-020 may be deferred if WSM < 7.80 |

---

*Orchestration Worktracker initialized: 2026-03-03*
*Agent: orch-planner v2.2.0*
*Next action: EPIC-001 Foundation — Phase 1: skills/user-experience/SKILL.md*
