<!-- VERSION: 1.0.1 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "Wave Architecture", "Wave Transition Quality Gates", "Wave Signoff Enforcement" | PARENT: /user-experience skill -->

# Wave Signoff Template

> Template for WAVE-N-SIGNOFF.md files that gate progression from Wave N to Wave N+1. Completed by the ux-orchestrator after wave sub-skills pass quality gates. See also: `skills/user-experience/rules/wave-progression.md` [Signoff Requirements] (authoritative validation criteria), `skills/user-experience/rules/wave-progression.md` [Wave Transition Gates] (0.85 operational threshold per ADR-PROJ022-002 PROVISIONAL), `skills/user-experience/rules/ci-checks.md` [UX-CI-007, UX-CI-008] (CI gates that validate signoff files and ordering), `skills/user-experience/rules/synthesis-validation.md` [Cross-Framework Synthesis Protocol] (synthesis test section of this template). Output location: `skills/user-experience/output/WAVE-{N}-SIGNOFF.md`.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Template](#template) | Copy-paste template for WAVE-N-SIGNOFF.md |
| [Field Descriptions](#field-descriptions) | What each field means and how to populate it |
| [Per-Wave Customization](#per-wave-customization) | Wave-specific evidence requirements |
| [Validation Rules](#validation-rules) | CI gate requirements for signoff acceptance |

---

## Template

<!-- Source: SKILL.md Section "Wave Signoff Enforcement" — wave signoff field structure. Quality gate threshold (0.85) from SKILL.md Section "Wave Transition Quality Gates" per ADR-PROJ022-002 (`docs/design/ADR-PROJ022-002-wave-criteria-gates.md`, PROVISIONAL). Scoring dimensions from `.context/rules/quality-enforcement.md` [Quality Gate] S-014 6-dimension rubric. Note: Wave signoff applies to Waves 1-5 only; Wave 0 (Foundation) uses `KICKOFF-SIGNOFF.md` per `skills/user-experience/templates/kickoff-signoff-template.md`. -->

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

- **Threshold:** >= 0.85 deployment readiness (`docs/design/ADR-PROJ022-002-wave-criteria-gates.md`, PROVISIONAL)
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

| Test | Status | Notes |
|------|--------|-------|
| Synthesis with Wave [N] sub-skills produces valid output | PASS / FAIL / N/A | [test engagement ID or notes] |
| Confidence classifications present in synthesis output | PASS / FAIL / N/A | [verification method] |
| Handoff data contracts validated between Wave [N] sub-skills | PASS / FAIL / N/A | [which handoffs tested] |

## Acceptance Criteria Met

- [ ] All sub-skill artifacts pass C4 >= 0.95 quality gate
- [ ] P-003 enforcement verified (no sub-skill has Task tool)
- [ ] Schema validation passes for all governance YAML files
- [ ] Cross-framework synthesis tested with Wave [N] sub-skills
- [ ] Degraded-mode behavior verified for OPT MCP dependencies
- [ ] Usage evidence documented per wave requirements
- [ ] AGENTS.md updated with Wave [N] agent entries

## Wave Bypass Usage (if any)

| Bypass ID | Sub-Skill | Unmet Criterion | Impact Assessment | Remediation Plan | Status |
|-----------|-----------|----------------|-------------------|------------------|--------|
| (none or list bypasses) | | | | | ACTIVE / RESOLVED |

## Authorization

Wave [N+1] deployment is authorized: YES / NO

**Notes:** [any conditions, observations, or prerequisites for next wave]
```

---

## Field Descriptions

<!-- Source: SKILL.md Section "Wave Signoff Enforcement" — required signoff fields. Quality score column requires S-014 composite >= 0.85 for wave transition per `skills/user-experience/rules/wave-progression.md` [Wave Transition Gates]. This threshold is distinct from C4 artifact quality (>= 0.95) and H-13 governance quality (>= 0.92). -->

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
| Wave Bypass Usage | List of active or resolved bypasses | Yes (even if empty) |
| Authorization | Explicit YES/NO for next wave deployment | Yes |
| Notes | Conditions, observations, or prerequisites | Optional |

---

## Per-Wave Customization

<!-- Source: SKILL.md Section "Wave Architecture" — wave definitions with entry criteria and bypass conditions. Evidence requirements map to wave-progression.md [Wave Transition Gates] per-transition additional evidence column. Each wave subsection below traces to the corresponding wave row in SKILL.md and wave-progression.md. -->

Each wave has specific evidence requirements in the "Usage Evidence" section:

### Wave 1 (Zero-Dependency)

| Evidence Type | Description |
|--------------|-------------|
| Heuristic evaluation completed | At least 1 heuristic eval report exists at expected output path |
| JTBD job statement used | At least 1 JTBD job statement referenced in a product decision document |

### Wave 2 (Data-Ready)

| Evidence Type | Description |
|--------------|-------------|
| Product launched with analytics | Documented product launch with analytics instrumentation reference |
| OR Lean UX hypothesis cycle | At least 1 completed hypothesis cycle (hypothesis → experiment → result) |

### Wave 3 (Design System)

| Evidence Type | Description |
|--------------|-------------|
| Storybook Atom stories | Storybook with 5+ Atom-level stories documented |
| Persona Spectrum review | At least 1 Persona Spectrum review completed |

### Wave 4 (Advanced Analytics)

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
| OR existing user research | Team has existing user research sufficient to bypass Kano prerequisite |
| AI-First Design engagement (if applicable) | At least 1 AI interaction pattern analysis completed; Enabler status DONE + WSM >= 7.80 |

---

## Validation Rules

<!-- Source: `skills/user-experience/rules/ci-checks.md` [UX-CI-007 Signoff File Structure, UX-CI-008 Signoff Ordering] — CI gate pass criteria for WAVE-N-SIGNOFF.md files. Quality gate threshold (0.85) from `skills/user-experience/rules/wave-progression.md` [Wave Transition Gates] per ADR-PROJ022-002 (`docs/design/ADR-PROJ022-002-wave-criteria-gates.md`, PROVISIONAL). S-014 scoring dimensions and weights defined in `.context/rules/quality-enforcement.md` [Quality Gate]. -->

The CI gate (UX-CI-007 in `ci-checks.md`) validates this signoff file:

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

*Template file: wave-signoff-template.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling templates: `skills/user-experience/templates/kickoff-signoff-template.md`*
*Consumed by: `skills/user-experience/rules/ci-checks.md` [UX-CI-007, UX-CI-008], `skills/user-experience/rules/wave-progression.md` [Signoff Requirements]*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
