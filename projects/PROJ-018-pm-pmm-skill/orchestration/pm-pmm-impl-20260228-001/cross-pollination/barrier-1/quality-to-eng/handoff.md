# Cross-Pollination Handoff: Quality to Engineering

**Barrier:** 1
**Date:** 2026-03-01
**Schema:** handoff-v2

---

```yaml
from_agent: adv-scorer
to_agent: eng-architect
task: "Apply QA strategy scoring dimensions, anti-leniency calibration, and per-artifact-type rubrics to Phase 2 Tier 1 agent definition engineering"
success_criteria:
  - "Phase 2 agent .md files satisfy the Agent Definition rubric (qa-strategy.md Section 2.3) -- all 7 body sections present, frameworks operationalized with methodology steps, both discovery and delivery mode examples included"
  - "Phase 2 .governance.yaml files satisfy the Governance YAML rubric (qa-strategy.md Section 2.4) -- zero schema validation errors, >= 5 forbidden_actions, >= 2 input_validation rules"
  - "SKILL.md satisfies the SKILL.md rubric (qa-strategy.md Section 2.6) -- L0/L1/L2 progressive disclosure, >= 5 routing triggers per agent, negative keywords for collision-prone agents"
  - "All Phase 2 artifacts designed to survive the 6-dimension weighted composite scoring at >= 0.95 threshold"
artifacts:
  - "quality/phase-1-setup/qa-strategy.md"
key_findings:
  - "Quality threshold is elevated to >= 0.95 weighted composite (above the standard H-13 threshold of 0.92) for this C3 workflow. The accept-with-caveats floor is >= 0.90. Hard reject below 0.90. This means Phase 2 agent definitions must be production-deployment-ready, not merely 'good enough.' The 6 scoring dimensions are: Completeness (0.20), Internal Consistency (0.20), Methodological Rigor (0.20), Evidence Quality (0.15), Actionability (0.15), Traceability (0.10)."
  - "Framework operationalization is the critical quality differentiator for agent .md files. Per the anti-leniency guidance (qa-strategy.md Section 5.1): 'Framework operationalization is binary at the per-framework level. If a framework is listed but has no corresponding methodology steps, that framework counts as ABSENT, not PARTIAL.' A framework that is merely named without methodology steps scores 0.40 on Methodological Rigor. Each of the 18 PM/PMM frameworks assigned to an agent MUST have named methodology steps in the <methodology> section."
  - "Constitutional compliance scoring has a specific rubric (qa-strategy.md Section 2.3): P-003, P-020, P-022 must ALL be explicitly cited in .governance.yaml constitution.principles_applied; >= 3 forbidden_actions must each reference a constitutional principle; worker agents must NOT have Task in allowed_tools. Partial compliance (e.g., only P-003 present) scores 0.40 -- this is below the hard reject threshold for the Traceability dimension alone."
  - "Agent definitions MUST include example outputs for BOTH discovery and delivery modes. Per the anti-leniency calibration: absent examples cap the Actionability dimension at 0.70 maximum, which would pull the weighted composite below the 0.90 floor. Examples must be concrete enough that a user could distinguish one agent's output from another agent's output."
  - "Adversary review at Phase 2 barrier uses 4 executor groups running 6 required C3 strategies (S-007, S-002, S-014, S-004, S-012, S-013) with a minimum of 3 distinct Task invocations for isolation. Group D (S-014 LLM-as-Judge) uses a two-pass scoring protocol to mitigate anchoring bias: Pass 1 scores independently, Pass 2 incorporates findings from Groups A/B/C. Engineering agents should anticipate this adversarial structure and design artifacts to withstand constitutional critique (S-007), devil's advocate challenge (S-002), FMEA failure mode analysis (S-012), and inversion (S-013)."
blockers: []
confidence: 0.94
criticality: C3
```

---

## Quality Criteria for Phase 2 Agent Definitions

### Agent .md File Checklist (from qa-strategy.md Section 2.3)

Reference: `quality/phase-1-setup/qa-strategy.md` Section 2.3

Engineering agents producing Phase 2 agent .md files should verify:

1. **All 7 body sections present:** `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`
2. **Framework operationalization depth:** Each assigned framework has named methodology steps in `<methodology>`, not generic references. Score exemplar: 0.95 = "All frameworks assigned to this agent have named methodology steps." Score exemplar: 0.75 = "Methodology section is a paragraph of general PM philosophy rather than framework-specific steps."
3. **Discovery and delivery mode examples:** Both modes produce distinct, concrete example outputs. Absent examples cap Actionability at 0.70.
4. **Constitutional triplet:** P-003, P-020, P-022 cited in agent body and companion .governance.yaml
5. **Cross-references resolve:** All artifact paths and cross-references point to real or planned files
6. **Routing triggers distinct:** Triggers do not fire for adjacent agents' domains

### Governance YAML Checklist (from qa-strategy.md Section 2.4)

Reference: `quality/phase-1-setup/qa-strategy.md` Section 2.4

1. **Zero schema validation errors** against `docs/schemas/agent-governance-v1.schema.json`
2. **Required fields:** version (semver), tool_tier (T3 for all PM/PMM agents), identity.role, identity.expertise (>= 2), identity.cognitive_mode
3. **forbidden_actions:** >= 5 entries (>= 3 with explicit constitutional principle cross-references)
4. **input_validation:** >= 2 rules, at least one that rejects a specific malformed input pattern (not generic)
5. **session_context:** on_receive and on_send populated for multi-agent workflow participation
6. **Tool tier:** Justified as the minimum viable tier (T3 for all PM/PMM agents due to WebSearch/WebFetch requirement)

### Anti-Leniency Traps to Avoid

Reference: `quality/phase-1-setup/qa-strategy.md` Section 5.1

| Dimension | Common Leniency Trap | Correct Scoring Behavior |
|-----------|---------------------|--------------------------|
| Completeness | "The section exists so it's complete" | A section header without substantive content scores 0.20-0.40, not 1.0 |
| Internal Consistency | "It's mostly consistent" | Any contradiction between two stated facts drops ICON by at least 0.15 per contradiction |
| Methodological Rigor | "They mentioned the framework" | Mentioning a framework with no methodology steps = 0.40 on MRIG |
| Evidence Quality | "The claims sound reasonable" | Unsubstantiated claims score 0.50 on EVID regardless of plausibility |
| Actionability | "An expert would know what to do" | Score against a competent practitioner new to this skill, not an expert |
| Traceability | "The intent is clear even without citations" | No citation = no traceability credit for that claim |

### Template Quality Criteria (from qa-strategy.md Section 2.5)

Reference: `quality/phase-1-setup/qa-strategy.md` Section 2.5

Although templates are formally gated at Barrier 1 (schema) and Barrier 4 (final), the quality dimensions apply:

- Template structure must reflect the framework methodology of the producing agent
- Both discovery and delivery mode variants must be present (absent variants cap Completeness at 0.60)
- A template usable for any domain (not PM/PMM-specific, not framework-specific) caps Methodological Rigor at 0.50

---

*Handoff version: handoff-v2*
*Source: Phase 1 Quality QA Strategy artifact*
*Destination: Phase 2 Engineering Tier 1 Agent Implementation pipeline*
