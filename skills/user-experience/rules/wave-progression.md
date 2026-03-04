<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "Wave Architecture", "Wave Transition Quality Gates", "Wave Signoff Enforcement" | PARENT: /user-experience skill -->

# Wave Progression Rules

> Criteria-gated wave deployment rules for the /user-experience skill. Defines wave transition quality gates, bypass mechanism, signoff requirements, and wave state tracking. See also: `skills/user-experience/rules/ux-routing-rules.md` (wave-aware routing and bypass routing), `skills/user-experience/rules/synthesis-validation.md` (synthesis quality dependent on wave-deployed sub-skills), `skills/user-experience/rules/mcp-coordination.md` (MCP availability affecting wave deployment readiness), `skills/user-experience/rules/ci-checks.md` (CI gates UX-CI-007 and UX-CI-008 that validate signoff files).

## Document Sections

| Section | Purpose |
|---------|---------|
| [Wave Definitions](#wave-definitions) | 6 waves (0-5) with sub-skills and entry criteria |
| [Wave Transition Gates](#wave-transition-gates) | Quality thresholds and evidence requirements per transition |
| [Signoff Requirements](#signoff-requirements) | What must exist before the next wave begins |
| [Bypass Mechanism](#bypass-mechanism) | 3-field bypass documentation process |
| [Wave State Tracking](#wave-state-tracking) | How wave deployment state is persisted and queried |
| [Wave Transition Workflow](#wave-transition-workflow) | Step-by-step transition process |

---

## Wave Definitions

<!-- Source: SKILL.md Section "Wave Architecture" — wave deployment model. ADR-PROJ022-001 (docs/design/ADR-PROJ022-001-ux-skill-architecture.md) provides architectural rationale for the criteria-gated wave approach. -->

Waves are **deployment phases** for incremental skill build-out, not runtime execution order. At runtime, the orchestrator routes to any deployed sub-skill based on user need.

| Wave | Name | Sub-Skills | Entry Criteria | Bypass Condition |
|------|------|-----------|----------------|-----------------|
| **0** | Foundation | `ux-orchestrator` + rules + templates | PROJ-022 plan approved | N/A |
| **1** | Zero-Dependency | `/ux-heuristic-eval`, `/ux-jtbd` | KICKOFF-SIGNOFF.md completed with MCP ownership assignments | N/A (first wave) |
| **2** | Data-Ready | `/ux-lean-ux`, `/ux-heart-metrics` | Wave 1: at least 1 heuristic eval completed AND 1 JTBD job statement used in a product decision | 2 sprint cycles elapsed with no Wave 1 completion; documented rationale |
| **3** | Design System | `/ux-atomic-design`, `/ux-inclusive-design` | Wave 2: launched product with analytics OR 1 completed Lean UX hypothesis cycle | Storybook already in use (skip Lean UX prerequisite for Atomic Design) |
| **4** | Advanced Analytics | `/ux-behavior-design`, `/ux-kano-model` | Wave 3: Storybook with 5+ Atom stories AND 1 Persona Spectrum review | Existing user base with analytics (skip Persona Spectrum prerequisite) |
| **5** | Process Intensives | `/ux-design-sprint`, `/ux-ai-first-design` (COND) | Wave 4: 30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed; AI-First: Enabler DONE + WSM >= 7.80 | Design Sprint can proceed without Kano prerequisite if team has existing user research |

---

## Wave Transition Gates

<!-- Source: SKILL.md Section "Wave Transition Quality Gates". -->
<!-- Threshold derivation: ADR-PROJ022-002-wave-criteria-gates.md (PROVISIONAL, 0.85). -->

Each wave transition is a quality checkpoint. The orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills.

### Threshold

**0.85** S-014 weighted composite for wave transition quality gates.

This threshold is distinct from H-13's 0.92 for governance artifacts. Wave gates assess sub-skill *operational output quality* (deployment readiness), not governance artifact quality. See `ADR-PROJ022-002-wave-criteria-gates.md` for provisional threshold derivation (ADR is STUB; to be baselined during Wave 1 deployment).

### Per-Transition Requirements

| Transition | Quality Check | Threshold | Additional Evidence |
|-----------|---------------|-----------|-------------------|
| Wave 0 → 1 | KICKOFF-SIGNOFF.md completeness | All fields populated (pass/fail) | MCP ownership assignments present |
| Wave 1 → 2 | Wave 1 deliverables quality scoring | S-014 composite >= 0.85 on heuristic eval report | At least 1 heuristic eval completed AND 1 JTBD job statement used |
| Wave 2 → 3 | Wave 2 deliverables + usage evidence | S-014 composite >= 0.85 | Documented usage artifact (product launch OR hypothesis cycle) |
| Wave 3 → 4 | Wave 3 deliverables + Storybook artifact | S-014 composite >= 0.85 | Storybook story count verification (5+ Atom stories) |
| Wave 4 → 5 | Wave 4 deliverables + user data evidence | S-014 composite >= 0.85 | User count (30+) or behavioral data artifact |

### Scoring Dimensions

Wave gate scoring uses the same S-014 6-dimension rubric as H-13, with weights:

| Dimension | Weight |
|-----------|--------|
| Completeness | 0.20 |
| Internal Consistency | 0.20 |
| Methodological Rigor | 0.20 |
| Evidence Quality | 0.15 |
| Actionability | 0.15 |
| Traceability | 0.10 |

---

## Signoff Requirements

<!-- Source: SKILL.md Section "Wave Signoff Enforcement". Signoff files are validated by CI gates UX-CI-007 (Signoff File Structure) and UX-CI-008 (Signoff Ordering) defined in `skills/user-experience/rules/ci-checks.md`. -->

### Signoff File Locations

| Wave | Signoff File | Location |
|------|-------------|----------|
| Foundation | KICKOFF-SIGNOFF.md | `skills/user-experience/output/KICKOFF-SIGNOFF.md` |
| Wave 1 | WAVE-1-SIGNOFF.md | `skills/user-experience/output/WAVE-1-SIGNOFF.md` |
| Wave 2 | WAVE-2-SIGNOFF.md | `skills/user-experience/output/WAVE-2-SIGNOFF.md` |
| Wave 3 | WAVE-3-SIGNOFF.md | `skills/user-experience/output/WAVE-3-SIGNOFF.md` |
| Wave 4 | WAVE-4-SIGNOFF.md | `skills/user-experience/output/WAVE-4-SIGNOFF.md` |
| Wave 5 | WAVE-5-SIGNOFF.md | `skills/user-experience/output/WAVE-5-SIGNOFF.md` |

### Signoff File Validation

A signoff file is valid when:

1. **Schema completeness:** All required fields are non-empty (date, signed off by, sub-skills deployed table, quality gate result, artifacts verified table, acceptance criteria checklist).
2. **Quality gate pass:** Composite score >= 0.85 for all sub-skills in the wave.
3. **Acceptance criteria met:** All acceptance criteria checkboxes are checked.
4. **Bypass resolution:** No unresolved bypasses for the completing wave (active bypasses block signoff).
5. **Repository committed:** The signoff file is committed to the repository (wave completion is not recognized until committed).

### Templates

- Kickoff signoff: `skills/user-experience/templates/kickoff-signoff-template.md`
- Wave signoff: `skills/user-experience/templates/wave-signoff-template.md`

---

## Bypass Mechanism

<!-- Source: SKILL.md Section "Wave Architecture" — bypass mechanism. -->

Wave bypass allows routing to a sub-skill whose wave has not been formally signed off. Bypass requires user-approved 3-field documentation per P-020.

### Bypass Fields

| Field | Description | Example |
|-------|------------|---------|
| **Unmet Criterion** | Which wave entry criterion is not met | "No completed heuristic evaluation from Wave 1" |
| **Impact Assessment** | Risk of proceeding without this criterion | "Sprint proceeds without prior framework calibration; findings may lack comparative baseline" |
| **Remediation Plan** | How the unmet criterion will be satisfied, and by when | "Backfill Wave 1 heuristic evaluation within 2 sprints of Design Sprint completion" |

### Bypass Documentation

Bypass documentation is persisted at `skills/user-experience/output/{engagement-id}/wave-bypass-{wave-N}.md`. See `ux-routing-rules.md` [Bypass Routing] for full documentation structure.

### Bypass Constraints

| Constraint | Rule | Rationale |
|-----------|------|-----------|
| **Cumulative ceiling** | Maximum 2 concurrent bypasses per team | Prevents accumulation of technical UX debt through unbounded wave skipping |
| **Warning banner** | All outputs produced under bypass carry: "[WAVE BYPASS] This output was produced before Wave {N} entry criteria were met." | P-022 compliance: users know the output lacks wave prerequisites |
| **Signoff blocking** | A wave signoff cannot complete if it has unresolved bypasses for that wave | Forces remediation before wave closure |
| **User approval** | User must explicitly approve each bypass (P-020) | No automatic bypasses; user decides whether to accept the risk |

### Bypass Lifecycle

1. **Request:** User's intent routes to a sub-skill whose wave is not deployed.
2. **Inform:** Orchestrator discloses wave unavailability per P-022.
3. **Prompt:** Orchestrator presents 3-field bypass prompt (see `ux-routing-rules.md` [Bypass Routing]).
4. **Document:** User provides 3 fields; orchestrator persists bypass documentation.
5. **Execute:** Sub-skill runs with bypass warning banner on all outputs.
6. **Remediate:** User completes the unmet criterion per remediation plan.
7. **Close:** Bypass is resolved; warning banner removed from future outputs.

---

## Wave State Tracking

<!-- Source: SKILL.md Section "Wave Architecture" and ux-routing-rules.md [Wave-Aware Routing]. -->

### State Detection

Wave state is determined by the existence and validity of signoff files:

| File Exists | State |
|------------|-------|
| No signoff files | Only Foundation (Wave 0) is authorized |
| `KICKOFF-SIGNOFF.md` valid | Wave 1 authorized |
| `WAVE-1-SIGNOFF.md` valid | Wave 2 authorized |
| `WAVE-2-SIGNOFF.md` valid | Wave 3 authorized |
| `WAVE-3-SIGNOFF.md` valid | Wave 4 authorized |
| `WAVE-4-SIGNOFF.md` valid | Wave 5 authorized |
| `WAVE-5-SIGNOFF.md` valid | All waves complete |

### State Caching

The orchestrator checks signoff files once per engagement session and caches the wave state. Cache invalidation occurs:

- On the next routing decision after a signoff file is committed during the session.
- At the start of each new engagement session.
- When a bypass is granted or resolved.

### Worktracker Integration

Wave transitions are tracked via `/worktracker` entities:

- Each wave is a Feature entity under the `/user-experience` Epic.
- Sub-skill deployment Stories are children of the wave Feature.
- Signoff is an Enabler that gates the next wave Feature.

---

## Wave Transition Workflow

<!-- Source: SKILL.md Section "Wave Transition Quality Gates" — orchestrator-driven transition process. Step sequence derived from Wave Signoff Enforcement flow: verify → score → evidence → bypass check → generate → user approval → commit → cache invalidation. -->

The orchestrator follows this workflow when a wave transition is requested:

| Step | Action | Failure Behavior |
|------|--------|-----------------|
| 1 | Verify all sub-skills in the wave have produced output | Block transition; list sub-skills without output |
| 2 | Score each sub-skill's representative output (the sub-skill's primary deliverable artifact as defined in its SKILL.md `output` section) via S-014 | Block if any score < 0.85 |
| 3 | Verify additional evidence requirements (usage artifacts, story counts, user counts) | Block; list unmet evidence requirements |
| 4 | Check for unresolved bypasses in this wave | Block; list unresolved bypasses |
| 5 | Generate WAVE-N-SIGNOFF.md using template | Present to user for review |
| 6 | User signs off (P-020: user authorizes wave closure) | No automatic signoff; user decides |
| 6a | Update bypass documentation with remediation evidence and target date status (prerequisite: Step 4 identified unresolved bypasses requiring remediation before signoff) | Bypass remains unresolved if remediation incomplete; signoff blocked per Bypass Constraints |
| 7 | Commit signoff file to repository | Wave transition is recognized |
| 8 | Invalidate wave state cache | Next routing decision uses updated state |

### Post-Wave-5 Operational State

When `WAVE-5-SIGNOFF.md` is valid (all waves complete), the orchestrator enters **full operational mode**: all 10 sub-skills are deployed and available for routing. No further wave transitions are needed. The orchestrator continues to enforce synthesis quality gates, MCP availability detection, and bypass constraint checks during normal operation. Wave signoff files are retained as immutable audit artifacts.

---

*Rule file: wave-progression.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling rules: `skills/user-experience/rules/ux-routing-rules.md`, `skills/user-experience/rules/synthesis-validation.md`, `skills/user-experience/rules/mcp-coordination.md`, `skills/user-experience/rules/ci-checks.md`*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
