# Wave Signoff Template

<!-- STUB: Created during PROJ-022 Foundation phase. Full implementation in EPIC-001. -->

> Template for WAVE-N-SIGNOFF.md files that gate progression from Wave N to Wave N+1. Completed by the ux-orchestrator after wave sub-skills pass quality gates.

---

## Template

```markdown
# Wave [N] Signoff — /user-experience Skill

**Date:** YYYY-MM-DD
**Wave:** [N]
**Signed off by:** [user name or session ID]

## Sub-Skills Deployed

| Sub-Skill | Agent | Quality Score | Deployment Status |
|-----------|-------|---------------|-------------------|
| /ux-[name-1] | ux-[agent-1] | [score] | DEPLOYED / FAILED |
| /ux-[name-2] | ux-[agent-2] | [score] | DEPLOYED / FAILED |

## Wave Quality Gate

- **Threshold:** >= 0.85 deployment readiness
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

## Acceptance Criteria Met

- [ ] All sub-skill artifacts pass C4 >= 0.95 quality gate
- [ ] P-003 enforcement verified (no sub-skill has Task tool)
- [ ] Schema validation passes for all governance YAML files
- [ ] Cross-framework synthesis tested with Wave [N] sub-skills
- [ ] Degraded-mode behavior verified for OPT MCP dependencies

## Wave Bypass Usage (if any)

| Bypass ID | Unmet Criterion | Impact Assessment | Remediation Plan |
|-----------|----------------|-------------------|------------------|
| (none or list bypasses) | | | |

## Authorization

Wave [N+1] deployment is authorized: YES / NO

**Notes:** [any conditions or observations]
```

---

*Template file: wave-signoff-template.md*
*Parent skill: /user-experience*
*Created: 2026-03-03*
*Status: STUB — Full implementation tracked in EPIC-001*
