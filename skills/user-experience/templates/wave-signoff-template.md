<!-- VERSION: 1.0.3 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "Wave Architecture", "Wave Transition Quality Gates", "Wave Signoff Enforcement" | PARENT: /user-experience skill | REVISION: iter4 — artifact-to-score specification in Wave Quality Gate, Authorization block restructured with Wave 5 primary variant, Authorization source annotation citing wave-progression.md, Cross-Framework Synthesis navigational hint to SKILL.md Available Agents -->

# Wave Signoff Template

> Template for WAVE-N-SIGNOFF.md files that gate progression from Wave N to Wave N+1. Covers Waves 1-5 only; Wave 0 (Foundation) uses the separate `skills/user-experience/templates/kickoff-signoff-template.md` template. Completed by the ux-orchestrator after wave sub-skills pass quality gates. See also: `skills/user-experience/rules/wave-progression.md` [Signoff Requirements] (authoritative validation criteria), `skills/user-experience/rules/wave-progression.md` [Wave Transition Gates] (0.85 operational threshold per `docs/design/ADR-PROJ022-002-wave-criteria-gates.md`, PROVISIONAL — threshold will be updated when ADR-PROJ022-002 is baselined with Wave 1 calibration data), `skills/user-experience/rules/ci-checks.md` [UX-CI-007, UX-CI-008] (CI gates that validate signoff files and ordering), `skills/user-experience/rules/synthesis-validation.md` [Cross-Framework Synthesis Protocol] (synthesis test section of this template), `.context/rules/quality-enforcement.md` [Quality Gate] (S-014 6-dimension rubric weights used for wave gate scoring). Output location: `skills/user-experience/output/WAVE-{N}-SIGNOFF.md`.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Template](#template) | Copy-paste template for WAVE-N-SIGNOFF.md |
| [Field Descriptions](#field-descriptions) | What each field means and how to populate it |
| [Per-Wave Customization](#per-wave-customization) | Wave-specific evidence requirements |
| [Validation Rules](#validation-rules) | CI gate requirements for signoff acceptance |

---

## Template

<!-- Source: SKILL.md Section "Wave Signoff Enforcement" — wave signoff field structure and required sections. `skills/user-experience/rules/wave-progression.md` [Signoff Requirements] — field completeness criteria and signoff file validation rules. Quality gate threshold (0.85) from SKILL.md Section "Wave Transition Quality Gates" per ADR-PROJ022-002 (`docs/design/ADR-PROJ022-002-wave-criteria-gates.md`, PROVISIONAL — to be baselined with Wave 1 calibration data). Scoring dimensions and weights from `.context/rules/quality-enforcement.md` [Quality Gate] S-014 6-dimension rubric (Completeness 0.20, Internal Consistency 0.20, Methodological Rigor 0.20, Evidence Quality 0.15, Actionability 0.15, Traceability 0.10). Note: Wave signoff applies to Waves 1-5 only; Wave 0 (Foundation) uses `KICKOFF-SIGNOFF.md` per `skills/user-experience/templates/kickoff-signoff-template.md`. -->

```markdown
# Wave [N] Signoff — /user-experience Skill

**Date:** YYYY-MM-DD
**Wave:** [N]
**Signed off by:** [user name or session ID]
**Engagement ID:** UX-[NNNN]

## Sub-Skills Deployed

| Sub-Skill | Agent | Quality Score | Deployment Status |
|-----------|-------|---------------|-------------------|
| /ux-[name-1] | ux-[agent-1] | [score] | DEPLOYED / FAILED |
| /ux-[name-2] | ux-[agent-2] | [score] | DEPLOYED / FAILED |

## Wave Quality Gate

- **Threshold:** >= 0.85 deployment readiness (`docs/design/ADR-PROJ022-002-wave-criteria-gates.md`, PROVISIONAL — threshold will be updated when ADR is baselined)
- **Scoring:** S-014 6-dimension rubric (weights: `.context/rules/quality-enforcement.md` [Quality Gate]; computation: `skills/user-experience/rules/wave-progression.md` [Wave Transition Gates]). Score the primary deliverable artifact for each sub-skill (defined in each sub-skill's SKILL.md `output` section, per `wave-progression.md` [Wave Transition Workflow] Step 2).
- **Composite score:** [score]
- **Result:** PASS / FAIL

## Artifacts Verified

| Artifact | Path | Status |
|----------|------|--------|
| Sub-skill SKILL.md | `skills/ux-[name]/SKILL.md` | PASS / FAIL |
| Agent definition | `skills/ux-[name]/agents/ux-[agent].md` | PASS / FAIL |
| Governance YAML | `skills/ux-[name]/agents/ux-[agent].governance.yaml` | PASS / FAIL |
| Methodology rules | `skills/ux-[name]/rules/[methodology]-rules.md` | PASS / FAIL |
| Report template | `skills/ux-[name]/templates/[report]-template.md` | PASS / FAIL |

## Usage Evidence

| Evidence Type | Description | Artifact/Reference |
|--------------|-------------|-------------------|
| [evidence type per wave] | [what was produced or achieved] | [file path or external reference] |

## Cross-Framework Synthesis Test

<!-- Evaluation criteria: `skills/user-experience/rules/synthesis-validation.md` [Cross-Framework Synthesis Protocol] for "valid output" definition, [Synthesis Output Structure] for required sections. CI gates: `skills/user-experience/rules/ci-checks.md` [UX-CI-011] (confidence classification), [UX-CI-012] (traceability), [UX-CI-013] (LOW template compliance). -->

| Test | Status | Notes |
|------|--------|-------|
| Synthesis with Wave [N] sub-skills produces valid output (per `synthesis-validation.md` [Synthesis Output Structure]; for wave-specific sub-skill names, see `skills/user-experience/SKILL.md` [Available Agents] table, Wave column) | PASS / FAIL / N/A | [test engagement ID or notes] |
| Confidence classifications present in synthesis output (CI: UX-CI-011) | PASS / FAIL / N/A | [verification method] |
| Handoff data contracts validated between Wave [N] sub-skills (per `synthesis-validation.md` [Cross-Framework Synthesis Protocol] Steps 1-4) | PASS / FAIL / N/A | [which handoffs tested] |

## Acceptance Criteria Met

<!-- Source: SKILL.md Sections "Wave Signoff Enforcement" (signoff criteria), "P-003 Compliance" (tool enforcement); `skills/user-experience/rules/ci-checks.md` [CI Gate Summary] (UX-CI-001 through UX-CI-013). Items without corresponding CI gate IDs are human-verified rather than automated. -->

- [ ] All sub-skill artifacts pass C4 >= 0.95 quality gate
- [ ] P-003 enforcement verified (no sub-skill has Task tool; CI: UX-CI-001, UX-CI-002)
- [ ] Schema validation passes for all governance YAML files (CI: UX-CI-004, UX-CI-005)
- [ ] Cross-framework synthesis tested with Wave [N] sub-skills (CI: UX-CI-011, UX-CI-012, UX-CI-013)
- [ ] Degraded-mode behavior verified for OPT MCP dependencies (see `skills/user-experience/rules/mcp-coordination.md` [Degraded Mode Behavior]; human-verified)
- [ ] Usage evidence documented per wave requirements
- [ ] AGENTS.md updated with Wave [N] agent entries (verify each sub-skill agent appears in the AGENTS.md registry per H-26; human-verified)

## Wave Bypass Usage (if any)

| Bypass ID | Sub-Skill | Unmet Criterion | Impact Assessment | Remediation Plan | Status |
|-----------|-----------|----------------|-------------------|------------------|--------|
| (none or list bypasses) | | | | | ACTIVE / RESOLVED |

## Authorization

<!-- Source: wave-progression.md [Post-Wave-5 Operational State] — Wave 5 authorization uses "full operational mode" language; Waves 1-4 use "Wave [N+1] deployment" language. wave-progression.md [Wave State Tracking] — signoff authorizes the next wave. -->

<!-- For Waves 1-4, use: -->
Wave [N+1] deployment is authorized: YES / NO
<!-- For Wave 5 (final wave), replace the above line with: -->
<!-- All waves complete — full operational mode authorized: YES / NO -->

**Notes:** [any conditions, observations, or prerequisites for next wave]
```

---

## Field Descriptions

<!-- Source: SKILL.md Section "Wave Signoff Enforcement" — required signoff fields. `skills/user-experience/rules/wave-progression.md` [Signoff File Validation] — field completeness criteria. Quality score column requires S-014 composite >= 0.85 for wave transition per `skills/user-experience/rules/wave-progression.md` [Wave Transition Gates] and `docs/design/ADR-PROJ022-002-wave-criteria-gates.md` (PROVISIONAL). This threshold is distinct from C4 artifact quality (>= 0.95) and H-13 governance quality (>= 0.92, `.context/rules/quality-enforcement.md` [Quality Gate]). -->

| Field | Description | Required |
|-------|------------|----------|
| Date | ISO 8601 date of signoff | Yes |
| Wave | Wave number (1-5) | Yes |
| Signed off by | User name or session identifier who authorized the signoff | Yes |
| Engagement ID | Engagement ID for this wave's work | Yes |
| Sub-Skills Deployed | All sub-skills in this wave with quality scores | Yes |
| Wave Quality Gate | Composite score and PASS/FAIL result | Yes |
| Artifacts Verified | All artifacts for each sub-skill in the wave | Yes |
| Usage Evidence | Wave-specific evidence of sub-skill usage | Yes |
| Cross-Framework Synthesis Test | Results of synthesis testing with this wave's sub-skills | Yes |
| Acceptance Criteria Met | All checkboxes must be checked | Yes |
| Wave Bypass Usage | List of active or resolved bypasses. Each populated row requires 3 fields per `skills/user-experience/rules/wave-progression.md` [Bypass Fields]: Unmet Criterion, Impact Assessment, Remediation Plan. Lifecycle fields (Bypass ID, Status) are added for tracking. | Yes (even if empty) |
| Authorization | Explicit YES/NO for next wave deployment (Waves 1-4) or full operational mode (Wave 5). Source: `wave-progression.md` [Post-Wave-5 Operational State], [Wave State Tracking] | Yes |
| Notes | Conditions, observations, or prerequisites | Optional |

---

## Per-Wave Customization

<!-- Source: SKILL.md Section "Wave Architecture" — wave definitions with entry criteria and bypass conditions. Evidence requirements map to wave-progression.md [Wave Transition Gates] per-transition additional evidence column. Each wave subsection below traces to the corresponding wave row in SKILL.md and wave-progression.md. -->

Each wave has specific evidence requirements in the "Usage Evidence" section:

### Wave 1 (Zero-Dependency)

<!-- Source: SKILL.md Section "Wave Architecture" — Wave 1 entry criteria: KICKOFF-SIGNOFF.md completed with MCP ownership assignments. Sub-skills: `/ux-heuristic-eval`, `/ux-jtbd`. wave-progression.md [Wave Transition Gates] Wave 1 -> 2 additional evidence. -->

| Evidence Type | Description |
|--------------|-------------|
| Heuristic evaluation completed | At least 1 heuristic eval report exists at expected output path (see `/ux-heuristic-eval` SKILL.md for output location) |
| JTBD job statement used | At least 1 JTBD job statement referenced in a product decision document |

### Wave 2 (Data-Ready)

<!-- Source: SKILL.md Section "Wave Architecture" — Wave 2 entry criteria: at least 1 heuristic eval completed AND 1 JTBD job statement used. Sub-skills: `/ux-lean-ux`, `/ux-heart-metrics`. wave-progression.md [Wave Transition Gates] Wave 2 -> 3 additional evidence. -->

| Evidence Type | Description |
|--------------|-------------|
| Product launched with analytics | Documented product launch with analytics instrumentation reference |
| OR Lean UX hypothesis cycle | At least 1 completed hypothesis cycle (hypothesis -> experiment -> result) |

### Wave 3 (Design System)

<!-- Source: SKILL.md Section "Wave Architecture" — Wave 3 entry criteria: launched product with analytics OR 1 completed Lean UX hypothesis cycle. Sub-skills: `/ux-atomic-design`, `/ux-inclusive-design`. wave-progression.md [Wave Transition Gates] Wave 3 -> 4 additional evidence. -->

| Evidence Type | Description |
|--------------|-------------|
| Storybook Atom stories | Storybook with 5+ Atom-level stories documented |
| Persona Spectrum review | At least 1 Persona Spectrum review completed |

### Wave 4 (Advanced Analytics)

<!-- Source: SKILL.md Section "Wave Architecture" — Wave 4 entry criteria: Storybook with 5+ Atom stories AND 1 Persona Spectrum review. Sub-skills: `/ux-behavior-design`, `/ux-kano-model`. wave-progression.md [Wave Transition Gates] Wave 4 -> 5 additional evidence. -->

| Evidence Type | Description |
|--------------|-------------|
| Kano survey users | 30+ users available for Kano survey |
| OR B=MAP bottleneck diagnosed | At least 1 B=MAP bottleneck diagnosis completed |
| AI-First Enabler (if applicable) | Enabler status DONE + WSM >= 7.80 |

### Wave 5 (Process Intensives)

<!-- Source: SKILL.md Section "Wave Architecture" — Wave 5 entry criteria: Wave 4 complete (30+ users for Kano OR 1 B=MAP bottleneck); AI-First conditional on Enabler DONE + WSM >= 7.80. Sub-skills: `/ux-design-sprint`, `/ux-ai-first-design` (COND). -->

| Evidence Type | Description |
|--------------|-------------|
| Design Sprint completed | At least 1 design sprint cycle (Understand → Sketch → Decide → Prototype → Test) documented |
| OR existing user research | Team has existing user research sufficient to bypass Kano prerequisite: at least 1 prior user study with >= 5 participants, OR analytics dataset with >= 100 user sessions providing behavioral signal equivalent to Kano survey data |
| AI-First Design engagement (if applicable) | At least 1 AI interaction pattern analysis completed; Enabler status DONE + WSM >= 7.80 |

---

## Validation Rules

<!-- Source: `skills/user-experience/rules/ci-checks.md` [UX-CI-007 Signoff File Structure, UX-CI-008 Signoff Ordering] — CI gate pass criteria for WAVE-N-SIGNOFF.md files. Quality gate threshold (0.85) from `skills/user-experience/rules/wave-progression.md` [Wave Transition Gates] per ADR-PROJ022-002 (`docs/design/ADR-PROJ022-002-wave-criteria-gates.md`, PROVISIONAL — to be baselined with Wave 1 calibration data). S-014 scoring dimensions and weights defined in `.context/rules/quality-enforcement.md` [Quality Gate] (Completeness 0.20, Internal Consistency 0.20, Methodological Rigor 0.20, Evidence Quality 0.15, Actionability 0.15, Traceability 0.10). -->

The CI gate (UX-CI-007 in `skills/user-experience/rules/ci-checks.md`) validates this signoff file. Acceptance criteria items without corresponding CI gate IDs (e.g., "Degraded-mode behavior verified") are human-verified rather than automated:

| Check | Pass Criteria |
|-------|--------------|
| Date field populated | Non-empty, valid ISO 8601 date |
| Wave number populated | Integer 1-5 |
| Signed off by populated | Non-empty string |
| Engagement ID format | Matches `UX-{NNNN}` pattern |
| All sub-skills listed | Expected sub-skills for this wave present in table |
| All sub-skills DEPLOYED | No "FAILED" status in sub-skills table |
| Quality gate PASS | Composite score >= 0.85 and result is "PASS" |
| All artifacts verified | No "FAIL" status in artifacts table |
| Usage evidence present | At least 1 row in usage evidence table |
| Acceptance criteria checked | All checkboxes marked `[x]` |
| Bypass section present | Bypass table exists (even if empty) |
| No unresolved bypasses | All bypasses in table have status "RESOLVED" (or table is empty) |
| Authorization is YES | Field contains "YES" |

---

*Template file: wave-signoff-template.md (v1.0.3)*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling templates: `skills/user-experience/templates/kickoff-signoff-template.md`*
*Consumed by: `skills/user-experience/rules/ci-checks.md` [UX-CI-007, UX-CI-008], `skills/user-experience/rules/wave-progression.md` [Signoff Requirements]*
*Quality gate sources: `.context/rules/quality-enforcement.md` [Quality Gate, S-014], `docs/design/ADR-PROJ022-002-wave-criteria-gates.md` (PROVISIONAL)*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
