# Kickoff Signoff Template

<!-- STUB: Created during PROJ-022 Foundation phase. Full implementation in EPIC-001. -->

> Template for the KICKOFF-SIGNOFF.md file that gates Wave 1 deployment. Completed by the ux-orchestrator after Foundation phase artifacts pass quality gates.

---

## Template

```markdown
# /user-experience Skill Kickoff Signoff

**Date:** YYYY-MM-DD
**Signed off by:** [user name or session ID]
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

## Acceptance Criteria Met

- [ ] All Foundation artifacts pass C4 >= 0.95 quality gate
- [ ] P-003 enforcement verified (no sub-skill has Task tool)
- [ ] Schema validation passes for all governance YAML files
- [ ] CLAUDE.md, AGENTS.md, mandatory-skill-usage.md updated

## Authorization

Wave 1 deployment is authorized: YES / NO

**Notes:** [any conditions or observations]
```

---

*Template file: kickoff-signoff-template.md*
*Parent skill: /user-experience*
*Created: 2026-03-03*
*Status: STUB — Full implementation tracked in EPIC-001*
