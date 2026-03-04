# PROJ-022: /user-experience Skill Implementation Plan

## Document Sections

| Section | Purpose |
|---------|---------|
| [Context](#context) | Project background and user requirements |
| [Authoritative Spec](#authoritative-spec) | Source documents for implementation decisions |
| [Wave Assignments](#wave-assignments) | Sub-skill allocation per wave |
| [Implementation Steps](#implementation-steps) | Phased execution plan |
| [Artifact Output Paths](#artifact-output-paths) | Explicit file paths per artifact |
| [Artifact Dependency Graph](#artifact-dependency-graph) | Creation ordering |
| [Commit and Revert Strategy](#commit-and-revert-strategy) | Per-artifact commit methodology |
| [Reference Files](#reference-files) | Reusable patterns and templates |
| [Verification](#verification) | Success criteria |

---

## Context

GitHub issue #138 specifies a `/user-experience` skill for the Jerry Framework: a hybrid parent orchestrator + 10 pluggable sub-skills deployed across 5 criteria-gated waves. This plan covers setup, orchestration, and execution across all 5 waves with C4 adversary quality at every creator output.

**User requirements:**
- C4 >= 0.95 adversary review at EVERY creator output (background agents, up to 6 iterations)
- Use /orchestration (orch-planner for ORCHESTRATION.yaml SSOT), /eng-team, /red-team, /adversary, /worktracker
- All 5 waves, not just Wave 1
- Architecture + fallback paths for MCP (not building actual adapters)
- Per-artifact commits after each C4 pass (maximum revert granularity)
- Validate spec gaps during Foundation phase (fix as discovered)
- Cross-session orchestration via ORCHESTRATION.yaml

**Issue closure:** Wave 1 + Parent Orchestrator. Waves 2-5 tracked in child issues.

---

## Authoritative Spec

All implementation decisions trace to GitHub Issue [#138](https://github.com/geekatron/jerry/issues/138) and its comments:

| Source | Content |
|--------|---------|
| Issue body | Main spec: architecture, sub-skills, waves, MCP integration |
| Comment 1 | 27 acceptance criteria across 8 categories |
| Comment 2 | Agent specifications, MCP dependency matrix, cognitive modes |
| Comment 3 | Directory structure, WSM scores, research backing |

**Spec validation approach:** Validate during Foundation phase. Fix gaps as discovered rather than re-running a full C4 tournament on the spec itself (it already passed 8 iterations in PROJ-020).

---

## Wave Assignments

| Wave | Sub-Skills | Agents |
|------|-----------|--------|
| 0 (Foundation) | Parent orchestrator | `ux-orchestrator` (T5, Opus, Integrative) |
| 1 | `/ux-heuristic-eval`, `/ux-jtbd` | `ux-heuristic-evaluator` (T3, Systematic), `ux-jtbd-analyst` (T3, Divergent) |
| 2 | `/ux-lean-ux`, `/ux-heart-metrics` | `ux-lean-ux-facilitator` (T3, Systematic), `ux-heart-analyst` (T2, Systematic) |
| 3 | `/ux-atomic-design`, `/ux-inclusive-design` | `ux-atomic-architect` (T3, Systematic), `ux-inclusive-evaluator` (T3, Systematic) |
| 4 | `/ux-behavior-design`, `/ux-kano-model` | `ux-behavior-diagnostician` (T2, Convergent), `ux-kano-analyst` (T2, Convergent) |
| 5 | `/ux-design-sprint`, `/ux-ai-first-design` (COND) | `ux-sprint-facilitator` (T3, Systematic), `ux-ai-design-guide` (T3, Divergent) |

---

## Implementation Steps

### Step 1: Project Setup

1. Create `projects/PROJ-022-user-experience-skill/` with `PLAN.md`, `WORKTRACKER.md`, `work/`
2. Update `projects/README.md` with PROJ-022 entry
3. Commit: `feat(PROJ-022): initialize project structure [skip-bump]`

### Step 2: WORKTRACKER Entity Decomposition

8 Epics with Feature breakdowns per sub-skill.

### Step 3: ORCHESTRATION.yaml via /orchestration orch-planner

Cross-session SSOT for all pipelines, quality gates, and checkpoints.

### Step 4: Execute Phases (Cross-Session)

Per-artifact creator -> C4 tournament -> commit cycle.

### Step 5: /eng-team Integration

MCP threat model, CI gate spec, quality benchmarks.

### Step 6: /red-team Integration (Purple Team at EPIC-007)

MCP OAuth flow, credential storage, P-003 enforcement testing.

---

## Artifact Output Paths

**Foundation (EPIC-001):**

| Artifact | Output Path |
|----------|------------|
| Parent SKILL.md | `skills/user-experience/SKILL.md` |
| Orchestrator agent | `skills/user-experience/agents/ux-orchestrator.md` |
| Orchestrator governance | `skills/user-experience/agents/ux-orchestrator.governance.yaml` |
| Routing rules | `skills/user-experience/rules/ux-routing-rules.md` |
| Synthesis validation | `skills/user-experience/rules/synthesis-validation.md` |
| Wave progression | `skills/user-experience/rules/wave-progression.md` |
| MCP coordination | `skills/user-experience/rules/mcp-coordination.md` |
| CI checks | `skills/user-experience/rules/ci-checks.md` |
| Kickoff template | `skills/user-experience/templates/kickoff-signoff-template.md` |
| Wave signoff template | `skills/user-experience/templates/wave-signoff-template.md` |

**Per Sub-Skill Pattern:**

| Artifact | Output Path Pattern |
|----------|-------------------|
| SKILL.md | `skills/ux-{name}/SKILL.md` |
| Agent definition | `skills/ux-{name}/agents/ux-{agent-name}.md` |
| Governance YAML | `skills/ux-{name}/agents/ux-{agent-name}.governance.yaml` |
| Methodology rules | `skills/ux-{name}/rules/{methodology}-rules.md` |
| Report template | `skills/ux-{name}/templates/{report}-template.md` |

**Registration (EPIC-008):**

| Artifact | Output Path |
|----------|------------|
| CLAUDE.md update | `CLAUDE.md` |
| AGENTS.md update | `AGENTS.md` |
| Trigger map update | `.context/rules/mandatory-skill-usage.md` |

---

## Artifact Dependency Graph

```
Parent SKILL.md
  -> ux-orchestrator.md + governance.yaml
    -> Rule files (routing, synthesis, wave, mcp, ci)
    -> Templates (kickoff, wave-signoff)
      -> KICKOFF-SIGNOFF.md
        -> Wave 1 sub-skills (parallel):
           Per sub-skill: SKILL.md -> agent.md -> governance.yaml -> rules -> templates
          -> WAVE-1-SIGNOFF.md
            -> Wave 2 ... -> WAVE-5-SIGNOFF.md
```

---

## Commit and Revert Strategy

- **Per-artifact commits** after each C4 >= 0.95 pass
- **Commit message format:** `feat(PROJ-022): add {artifact-name} [C4: {score}] [skip-bump]`
- **Revert granularity:** Any single artifact can be reverted without affecting others
- **ORCHESTRATION.yaml committed** with each artifact (tracks state)

---

## Reference Files

| Purpose | File Path |
|---------|-----------|
| Skill architecture pattern | `skills/eng-team/SKILL.md` |
| Agent dual-file pattern | `skills/adversary/agents/adv-executor.md` + `.governance.yaml` |
| Governance JSON Schema | `docs/schemas/agent-governance-v1.schema.json` |
| Agent development standards | `.context/rules/agent-development-standards.md` |
| Skill standards | `.context/rules/skill-standards.md` |
| Issue spec (authoritative) | GitHub Issue [#138](https://github.com/geekatron/jerry/issues/138) |

---

## Verification

| Check | How |
|-------|-----|
| Schema validation | Every `.governance.yaml` validates against `docs/schemas/agent-governance-v1.schema.json` |
| P-003 enforcement | No sub-skill agent has Task tool |
| C4 quality gate | Every creator artifact passes >= 0.95 S-014 composite |
| Wave signoff | WAVE-N-SIGNOFF.md exists before Wave N+1 begins |
| Acceptance criteria | All 27 AC from issue #138 satisfied |
| Registration | CLAUDE.md, AGENTS.md, mandatory-skill-usage.md updated |
| Commit trail | Per-artifact commits with C4 scores in messages |

---

*Project: PROJ-022-user-experience-skill*
*Created: 2026-03-03*
*Status: ACTIVE*
