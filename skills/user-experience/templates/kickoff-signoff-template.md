<!-- VERSION: 1.0.1 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Section "Wave Signoff Enforcement" | PARENT: /user-experience skill -->

# Kickoff Signoff Template

> Template for the KICKOFF-SIGNOFF.md file that gates Wave 1 deployment. Completed by the ux-orchestrator after Foundation phase artifacts pass quality gates. See also: `skills/user-experience/rules/wave-progression.md` [Signoff Requirements] (validation criteria consumed by CI), `skills/user-experience/rules/ci-checks.md` [UX-CI-007] (CI gate that validates signoff files), `skills/user-experience/rules/mcp-coordination.md` [MCP Availability Detection] (MCP ownership assignments in this template). Output location: `skills/user-experience/output/KICKOFF-SIGNOFF.md`.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Template](#template) | Copy-paste template for KICKOFF-SIGNOFF.md |
| [Field Descriptions](#field-descriptions) | What each field means and how to populate it |
| [Validation Rules](#validation-rules) | CI gate requirements for signoff acceptance |

---

## Template

<!-- Source: SKILL.md Section "Wave Signoff Enforcement" — Foundation signoff gates Wave 1. Field structure derives from wave-progression.md [Signoff Requirements]. MCP table from mcp-coordination.md [MCP Availability Detection]. Acceptance criteria map to ci-checks.md [UX-CI-001 through UX-CI-007] and quality-enforcement.md [H-34, H-35 (retired into H-34)]. -->

```markdown
# /user-experience Skill Kickoff Signoff

**Date:** YYYY-MM-DD
**Signed off by:** [user name or session ID]
**Engagement ID:** UX-{NNNN}
**Foundation phase status:** COMPLETE

## Foundation Artifacts Verified

| Artifact | Path | Quality Score | Status |
|----------|------|---------------|--------|
| Parent SKILL.md | `skills/user-experience/SKILL.md` | [score] | PASS / FAIL |
| Orchestrator agent | `skills/user-experience/agents/ux-orchestrator.md` | [score] | PASS / FAIL |
| Orchestrator governance | `skills/user-experience/agents/ux-orchestrator.governance.yaml` | [score] | PASS / FAIL |
| Routing rules | `skills/user-experience/rules/ux-routing-rules.md` | [score] | PASS / FAIL |
| Synthesis validation | `skills/user-experience/rules/synthesis-validation.md` | [score] | PASS / FAIL |
| Wave progression | `skills/user-experience/rules/wave-progression.md` | [score] | PASS / FAIL |
| MCP coordination | `skills/user-experience/rules/mcp-coordination.md` | [score] | PASS / FAIL |
| CI checks | `skills/user-experience/rules/ci-checks.md` | [score] | PASS / FAIL |
| Kickoff signoff template | `skills/user-experience/templates/kickoff-signoff-template.md` | [score] | PASS / FAIL |
| Wave signoff template | `skills/user-experience/templates/wave-signoff-template.md` | [score] | PASS / FAIL |

## MCP Ownership Assignments

| MCP Tool | Owner | Status | Notes |
|----------|-------|--------|-------|
| Context7 | [owner or "Framework-provided"] | Available / Unavailable | [configuration notes] |
| Figma MCP | [owner or "Not yet available"] | Available / Unavailable / Planned | [target date if planned] |
| Miro MCP | [owner or "Not yet available"] | Available / Unavailable / Planned | [target date if planned] |
| Storybook | [owner or "Not applicable"] | Available / Unavailable | [setup notes] |

## Acceptance Criteria Met

- [ ] All Foundation artifacts pass C4 >= 0.95 quality gate
- [ ] P-003 enforcement verified (no sub-skill has Task tool)
- [ ] Schema validation passes for all governance YAML files
- [ ] CLAUDE.md updated with /user-experience skill entry
- [ ] AGENTS.md updated with all deployed agent entries
- [ ] mandatory-skill-usage.md updated with /user-experience trigger keywords
- [ ] MCP ownership assignments documented (all REQ MCPs have owner or fallback plan)
- [ ] Wave 1 sub-skill directories created (skills/ux-heuristic-eval/, skills/ux-jtbd/)

## Authorization

Wave 1 deployment is authorized: YES / NO

**Notes:** [any conditions, observations, or prerequisites for Wave 1 work]
```

---

## Field Descriptions

<!-- Source: SKILL.md Section "Wave Signoff Enforcement" — required signoff fields. Quality score column requires C4 >= 0.95 per user-specified threshold (quality-enforcement.md H-13 default is 0.92; PROJ-022 overrides to 0.95). -->

| Field | Description | Required |
|-------|------------|----------|
| Date | ISO 8601 date of signoff | Yes |
| Signed off by | User name or session identifier who authorized the signoff | Yes |
| Engagement ID | First engagement ID for this /user-experience deployment (format: UX-{NNNN}) | Yes |
| Foundation phase status | Must be "COMPLETE" for signoff to be valid | Yes |
| Foundation Artifacts Verified | All 10 Foundation artifacts with C4 quality scores | Yes |
| MCP Ownership Assignments | Who owns each MCP integration and its current status (source: `skills/user-experience/rules/mcp-coordination.md` [MCP Availability Detection]) | Yes |
| Acceptance Criteria Met | All checkboxes must be checked for signoff to be valid | Yes |
| Authorization | Explicit YES/NO for Wave 1 deployment | Yes |
| Notes | Conditions, observations, or prerequisites | Optional |

---

## Validation Rules

The CI gate (UX-CI-007 in `ci-checks.md`) validates this signoff file:

| Check | Pass Criteria |
|-------|--------------|
| Date field populated | Non-empty, valid ISO 8601 date |
| Signed off by populated | Non-empty string |
| Engagement ID format | Matches `UX-{NNNN}` pattern |
| All artifacts listed | 10 rows in Foundation Artifacts Verified table |
| All artifacts PASS | No "FAIL" status in any row |
| All quality scores present | No empty score fields |
| All quality scores >= 0.95 | Every Foundation artifact score meets C4 threshold (PROJ-022 override of H-13 default 0.92) |
| MCP table populated | All 4 MCP rows have owner and status |
| All acceptance criteria checked | All checkboxes marked `[x]` |
| Authorization is YES | Field contains "YES" |

---

*Template file: kickoff-signoff-template.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling templates: `skills/user-experience/templates/wave-signoff-template.md`*
*Consumed by: `skills/user-experience/rules/ci-checks.md` [UX-CI-007], `skills/user-experience/rules/wave-progression.md` [Signoff Requirements], `skills/user-experience/rules/mcp-coordination.md` [MCP Ownership Assignments]*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
