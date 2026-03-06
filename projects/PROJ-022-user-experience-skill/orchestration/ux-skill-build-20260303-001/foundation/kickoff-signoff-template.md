<!-- VERSION: 1.0.2 | DATE: 2026-03-04 | SOURCE: SKILL.md v1.0.0 (skills/user-experience/SKILL.md) Section "Wave Signoff Enforcement" | PARENT: /user-experience skill | STATUS-RESOLUTION: SKILL.md Asset Inventory records this file as [STUB: EPIC-001]; that designation reflects the pre-completion planning state and does not apply to this version (v1.0.2). This file is COMPLETE and authoritative for Wave 0-to-1 transition. -->

# Kickoff Signoff Template

> Template for the KICKOFF-SIGNOFF.md file that gates Wave 1 deployment. Completed by the ux-orchestrator after Foundation phase artifacts pass quality gates. See also: `skills/user-experience/rules/wave-progression.md` [Signoff Requirements] (validation criteria consumed by CI), `skills/user-experience/rules/ci-checks.md` [UX-CI-007] (CI gate that validates signoff files), `skills/user-experience/rules/mcp-coordination.md` [MCP Availability Detection] (MCP ownership assignments in this template). Output location: `skills/user-experience/output/KICKOFF-SIGNOFF.md`. Status resolution: SKILL.md Asset Inventory records this file as [STUB: EPIC-001]; that designation reflects the pre-completion planning state. This version (v1.0.2) is COMPLETE and authoritative for the Wave 0-to-1 transition.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Template](#template) | Copy-paste template for KICKOFF-SIGNOFF.md |
| [Field Descriptions](#field-descriptions) | What each field means and how to populate it |
| [Validation Rules](#validation-rules) | CI gate requirements for signoff acceptance |

---

## Template

<!-- Source: SKILL.md v1.0.0 Section "Wave Signoff Enforcement" — Foundation signoff gates Wave 1. Field structure derives from wave-progression.md [Signoff Requirements]. MCP table from mcp-coordination.md [MCP Availability Detection]. Acceptance criteria map to ci-checks.md [UX-CI-001 through UX-CI-007] and quality-enforcement.md [H-13, H-34]. Quality threshold 0.95 is a PROJ-022 override of H-13 default 0.92 (PROVISIONAL — ADR-PROJ022-002-wave-criteria-gates.md pending baselined during Wave 1 deployment). Engagement ID format UX-{NNNN}: 4-digit zero-padded (range 0001-9999); template-authoritative pending formal definition in ux-routing-rules.md. -->

<!-- PRECONDITIONS: Before populating this template, the ux-orchestrator MUST: (1) Run adv-scorer (S-014) on each Foundation artifact and record the actual composite scores — do NOT use estimated or placeholder scores. (2) Verify all governance YAML files pass schema validation against docs/schemas/agent-governance-v1.schema.json. (3) Confirm CLAUDE.md, AGENTS.md, and mandatory-skill-usage.md have been updated with /user-experience entries. Source: quality-enforcement.md [H-13, H-14, H-17]. -->

```markdown
# /user-experience Skill Kickoff Signoff

**Date:** YYYY-MM-DD
**Signed off by:** [user name or session ID]
**Engagement ID:** UX-{NNNN}
**Foundation phase status:** COMPLETE

## Foundation Artifacts Verified

<!-- Quality Score: express as decimal 0.00-1.00 (e.g., 0.97). C4 >= 0.95 required per PROJ-022 override of H-13 default 0.92 (PROVISIONAL — ADR-PROJ022-002 pending baselined). Source: quality-enforcement.md [H-13, H-17]. -->

| Artifact | Path | Quality Score (C4 >= 0.95) | Status |
|----------|------|----------------------------|--------|
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

**If any artifact is FAIL:** Do not complete this signoff. Re-run adv-scorer (S-014) on the failing artifact, revise, and re-score per the creator-critic-revision cycle (quality-enforcement.md [H-14]). If the score cannot reach 0.95 after the criticality-proportional iteration ceiling (C4=10 iterations per agent-routing-standards.md [RT-M-010]), escalate to user per H-31.

## MCP Ownership Assignments

<!-- Source: mcp-coordination.md [MCP Availability Detection] — 4 Wave 0-1 MCPs requiring ownership documentation. Table covers Wave 0-1 MCPs only. See mcp-coordination.md [MCP Dependency Matrix] for the full matrix including Wave 2-5 MCPs (Zeroheight, Hotjar Bridge, Whimsical). For REQ MCPs: "Available" or "Planned" with non-empty target date are acceptable at kickoff; "Unavailable" without a documented fallback plan is not acceptable (source: mcp-coordination.md [Degraded Mode Behavior]). -->

| MCP Tool | Owner | Status | Notes |
|----------|-------|--------|-------|
| Context7 | [owner or "Framework-provided"] | Available / Unavailable | [configuration notes] |
| Figma MCP | [owner or "Not yet available"] | Available / Unavailable / Planned | [target date if planned] |
| Miro MCP | [owner or "Not yet available"] | Available / Unavailable / Planned | [target date if planned] |
| Storybook | [owner or "Not applicable"] | Available / Unavailable | [setup notes] |

## Acceptance Criteria Met

- [ ] All Foundation artifacts pass C4 >= 0.95 quality gate (quality-enforcement.md [H-13]; PROVISIONAL — ADR-PROJ022-002)
- [ ] P-003 enforcement verified: no sub-skill agent has Task tool in frontmatter (ci-checks.md [UX-CI-001, UX-CI-002])
- [ ] Schema validation passes for all governance YAML files (ci-checks.md [UX-CI-004, UX-CI-005]; agent-development-standards.md [H-34])
- [ ] CLAUDE.md updated with /user-experience skill entry (skill-standards.md [H-26])
- [ ] AGENTS.md updated with all deployed agent entries (skill-standards.md [H-26])
- [ ] mandatory-skill-usage.md updated with /user-experience trigger keywords (mandatory-skill-usage.md [H-22])
- [ ] MCP ownership assignments documented: all REQ MCPs have owner or fallback plan (mcp-coordination.md [MCP Availability Detection])
- [ ] Wave 1 sub-skill directories created with required subdirectory structure (agents/, rules/) per SKILL.md [Wave Architecture]: skills/ux-heuristic-eval/, skills/ux-jtbd/

## Authorization

Wave 1 deployment is authorized: YES / NO

**Notes:** [any conditions, observations, or prerequisites for Wave 1 work. Required when any acceptance criterion has a qualifier or condition; optional otherwise.]
```

---

## Field Descriptions

<!-- Source: SKILL.md v1.0.0 Section "Wave Signoff Enforcement" — required signoff fields. Quality score column requires C4 >= 0.95 per PROJ-022 override of H-13 default 0.92 (PROVISIONAL — ADR-PROJ022-002-wave-criteria-gates.md pending baselined during Wave 1 deployment; see SKILL.md [Standards References]). -->

| Field | Description | Required |
|-------|------------|----------|
| Date | ISO 8601 date of signoff (e.g., 2026-03-04) | Yes |
| Signed off by | User name or session identifier who authorized the signoff | Yes |
| Engagement ID | First engagement ID for this /user-experience deployment. Format: `UX-{NNNN}` (4-digit zero-padded, range 0001-9999). Template-authoritative format pending formal definition in `ux-routing-rules.md`. | Yes |
| Foundation phase status | Must be "COMPLETE" for signoff to be valid (source: SKILL.md v1.0.0 [Wave Signoff Enforcement]) | Yes |
| Foundation Artifacts Verified | All 10 Foundation artifacts with S-014 quality scores expressed as decimal 0.00-1.00 (e.g., 0.97, not 97% or PASS). C4 >= 0.95 threshold required (source: quality-enforcement.md [H-13, H-17]; PROVISIONAL -- ADR-PROJ022-002). | Yes |
| MCP Ownership Assignments | Who owns each Wave 0-1 MCP integration and its current status. Only 4 Wave 0-1 MCPs listed; see `mcp-coordination.md` [MCP Dependency Matrix] for full matrix (source: `skills/user-experience/rules/mcp-coordination.md` [MCP Availability Detection]). | Yes |
| Acceptance Criteria Met | All checkboxes must be checked for signoff to be valid. Each criterion cites its governing CI gate or rule source. | Yes |
| Authorization | Explicit YES/NO for Wave 1 deployment | Yes |
| Notes | Conditions, observations, or prerequisites. Required when any acceptance criterion has a qualifier or condition (e.g., conditional PASS, planned MCP target date). Optional otherwise. | Conditional |

---

## Validation Rules

The CI gate (UX-CI-007 in `ci-checks.md`) automates 5 structural field checks. The remaining 5 checks are manual pre-submission validations performed by the ux-orchestrator before committing the signoff file. Source: `ci-checks.md` [UX-CI-007 implementation scope]; `quality-enforcement.md` [H-13, H-17].

| Check | Pass Criteria | Enforcement |
|-------|--------------|-------------|
| Date field populated | Non-empty, valid ISO 8601 date | CI: UX-CI-007 |
| Signed off by populated | Non-empty string | CI: UX-CI-007 |
| Engagement ID format | Matches `UX-{NNNN}` pattern (4-digit zero-padded; source: template-authoritative, see Field Descriptions) | Manual |
| All artifacts listed | 10 rows in Foundation Artifacts Verified table | CI: UX-CI-007 |
| All artifacts PASS | No "FAIL" status in any row | CI: UX-CI-007 |
| All quality scores present | No empty score fields (express as decimal 0.00-1.00) | Manual |
| All quality scores >= 0.95 | Every Foundation artifact score meets C4 threshold (PROVISIONAL -- ADR-PROJ022-002; PROJ-022 override of quality-enforcement.md H-13 default 0.92) | Manual |
| MCP table populated | All 4 Wave 0-1 MCP rows have owner and status. For REQ MCPs: "Available" or "Planned" with target date acceptable; "Unavailable" without fallback plan not acceptable (source: mcp-coordination.md [Degraded Mode Behavior]). | Manual |
| All acceptance criteria checked | All checkboxes marked `[x]` | CI: UX-CI-007 |
| Authorization is YES | Field contains "YES" | Manual |

---

*Template file: kickoff-signoff-template.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md` v1.0.0*
*Sibling templates: `skills/user-experience/templates/wave-signoff-template.md`*
*Consumed by: `skills/user-experience/rules/ci-checks.md` [UX-CI-007], `skills/user-experience/rules/wave-progression.md` [Signoff Requirements], `skills/user-experience/rules/mcp-coordination.md` [MCP Availability Detection, MCP Ownership Assignments]*
*Quality threshold source: quality-enforcement.md [H-13] (0.92 default), PROJ-022 override to 0.95 (PROVISIONAL -- ADR-PROJ022-002-wave-criteria-gates.md pending baselined)*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Version: 1.0.2*
*Status: COMPLETE (status resolution: SKILL.md Asset Inventory [STUB: EPIC-001] designation reflects pre-completion planning state; does not apply to this version)*
