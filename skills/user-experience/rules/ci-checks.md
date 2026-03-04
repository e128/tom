# CI Checks Rules

<!-- STUB: Created during PROJ-022 Foundation phase. Full implementation in EPIC-001. -->

> CI/CD verification rules for the /user-experience skill. Defines automated checks for P-003 enforcement, schema validation, and wave gate compliance.

## Document Sections

| Section | Purpose |
|---------|---------|
| [P-003 Enforcement](#p-003-enforcement) | No sub-skill agent has Task tool |
| [Schema Validation](#schema-validation) | Governance YAML validation against JSON Schema |
| [Wave Gate Compliance](#wave-gate-compliance) | Signoff file existence verification |
| [Trigger Map Validation](#trigger-map-validation) | Keyword collision detection for new sub-skills |

---

## P-003 Enforcement

<!-- TODO (EPIC-001): Define CI grep pattern for Task tool detection in sub-skill agents. -->
<!-- Source: H-35 (constitutional compliance), H-01 (P-003). -->

Pending implementation. CI gate: `grep -r "Task" skills/ux-*/agents/*.md` must return zero matches in `tools:` frontmatter.

---

## Schema Validation

<!-- TODO (EPIC-001): Define CI schema validation for all governance YAML files. -->
<!-- Source: H-34 (agent definition standards). -->

Pending implementation. All `skills/ux-*/agents/*.governance.yaml` files must validate against `docs/schemas/agent-governance-v1.schema.json`.

---

## Wave Gate Compliance

<!-- TODO (EPIC-001): Define CI checks for wave signoff file validation. -->

Pending implementation. Verify signoff file structure and required fields.

---

## Trigger Map Validation

<!-- TODO (EPIC-001): Define keyword collision detection when new sub-skills are added. -->

Pending implementation. New sub-skill keywords must be cross-referenced against `mandatory-skill-usage.md` trigger map per RT-M-004.

---

*Rule file: ci-checks.md*
*Parent skill: /user-experience*
*Created: 2026-03-03*
*Status: STUB — Full implementation tracked in EPIC-001*
