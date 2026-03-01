# Cross-Pollination Handoff: Quality to Security

**Barrier:** 1
**Date:** 2026-03-01
**Schema:** handoff-v2

---

```yaml
from_agent: adv-scorer
to_agent: red-vuln
task: "Apply QA strategy scoring dimensions and anti-leniency calibration to Phase 2 security review artifacts (agent-sec-review.md, prompt-injection.md)"
success_criteria:
  - "Phase 2 security artifacts satisfy the Security Artifacts rubric (qa-strategy.md Section 2.7) -- all 5 agents covered in threat analysis, all 15 template types in attack surface enumeration, mitigations name specific guardrail fields"
  - "Security artifact scores meet the >= 0.95 quality threshold on the 6-dimension weighted composite"
  - "Anti-leniency guidance applied: risk ratings calibrated to actual deployment context (Jerry Framework, single-user CLI), not copied from enterprise threat models"
  - "Mitigation specificity: every identified threat has a specific mitigation action naming the guardrail field and expected value, not generic recommendations"
artifacts:
  - "quality/phase-1-setup/qa-strategy.md"
key_findings:
  - "Security artifacts are scored using the same 6-dimension weighted composite as all C3 deliverables: Completeness (0.20), Internal Consistency (0.20), Methodological Rigor (0.20), Evidence Quality (0.15), Actionability (0.15), Traceability (0.10). The quality threshold is >= 0.95 (elevated from standard 0.92). Security artifacts that score below 0.90 are hard-rejected."
  - "Completeness for security artifacts requires: all 5 agents individually covered, all 15 template types enumerated in attack surface, cross-agent data flow threats enumerated, competitive intelligence and customer data handling threats explicitly addressed. If any of the 5 agents is absent from the threat model, Completeness caps at 0.65 -- below the hard reject floor."
  - "Actionability is the critical dimension for security artifacts. Per the anti-leniency rubric: 'Add input validation' is insufficient; 'Add input validation that rejects prompts containing injection patterns in guardrails.input_validation with field_format regex' is acceptable. The mitigation specificity rubric scores 1.0 only when every mitigation is implementable in a specific agent guardrail field with the field name and expected value stated. Score of 0.50 for generic security recommendations not tailored to the agent definition format."
  - "Evidence Quality for security artifacts requires risk ratings calibrated to the actual deployment context. The Jerry Framework is a single-user CLI with local filesystem persistence -- risk ratings copied from enterprise multi-tenant threat models without adjustment score 0.60 on Evidence Quality. Probability estimates must be grounded in the actual deployment context: no network-based attacks, no multi-user access control, but prompt injection and data leakage are high-probability in an LLM agent context."
  - "Anti-leniency posture is mandatory for all scoring in this workflow. Key rules: (1) a score of 0.95 means ready for production deployment without modification, (2) dimension scores must not contradict findings -- if a completeness gap exists, Completeness cannot score 1.0, (3) the default for unverified claims is to score as unsubstantiated, (4) do not average a 0.60 with a 1.0 to produce a 0.80 -- report the 0.60 and document why."
blockers: []
confidence: 0.94
criticality: C3
```

---

## Quality Criteria for Phase 2 Security Artifacts

### Security Artifact Scoring Rubric (from qa-strategy.md Section 2.7)

Reference: `quality/phase-1-setup/qa-strategy.md` Section 2.7

| Dimension | Weight | What Constitutes PASS for Security Artifacts |
|-----------|--------|----------------------------------------------|
| Completeness (0.20) | All 5 agents appear individually in threat analysis. All 15 template types in attack surface. Prompt injection surface covers: system prompt extraction, framework injection, mode-switching abuse, cross-agent data leakage, competitive intelligence handling. |
| Internal Consistency (0.20) | Risk ratings consistent across agents with similar characteristics. A vulnerability present in pm-customer-insight that also exists structurally in pm-market-strategist is flagged in both. Mitigations do not contradict each other. |
| Methodological Rigor (0.20) | Named methodology applied (STRIDE, DREAD, or equivalent). Attack surface follows systematic approach, not ad hoc list. Prompt injection testing documents the actual injection vector, not just the conclusion. |
| Evidence Quality (0.15) | Vulnerability claims include reproduction steps or evidence. Risk ratings are calibrated -- not everything is HIGH. Probability estimates grounded in the Jerry Framework single-user CLI context. |
| Actionability (0.15) | Every identified threat has a specific mitigation naming the guardrail field and expected value. Generic "add input validation" is insufficient. |
| Traceability (0.10) | Each vulnerability traces to specific artifact (agent .md section or template section). Mitigations trace to specific guardrail fields in .governance.yaml. |

### Threat Coverage Rubric

| Score | Description |
|-------|-------------|
| 1.0 | All 5 agents individually covered; all 15 template types enumerated; cross-agent data flow threats enumerated; competitive intelligence and customer data handling threats explicitly addressed |
| 0.85 | All 5 agents covered; template coverage has 3-4 gaps; cross-agent threats present |
| 0.70 | Agents covered; template coverage cursory (by category not individual type); cross-agent threats mentioned but not enumerated |
| 0.50 | Agent coverage present; template coverage absent |
| < 0.50 | Generic PM/PMM threat coverage without reference to specific artifacts |

### Mitigation Specificity Rubric

| Score | Description |
|-------|-------------|
| 1.0 | Every mitigation is implementable in a specific agent guardrail field, with the field name and expected value stated |
| 0.85 | Most mitigations specific; 1-2 are general without implementation path |
| 0.70 | Mitigations are specific in type but not in implementation field |
| 0.50 | Mitigations are generic security recommendations not tailored to agent definition format |
| < 0.50 | No actionable mitigations; threat list only |

### Anti-Leniency Notes Specific to Security Scoring

Reference: `quality/phase-1-setup/qa-strategy.md` Section 5.1

1. **Do not inflate risk ratings.** The deployment context is a single-user CLI tool with local filesystem persistence. Network-based attacks, multi-user privilege escalation, and enterprise access control threats do not apply. Prompt injection and data leakage through the LLM agent pipeline are the genuine high-probability threats.

2. **Mitigation specificity is not optional.** A threat without an implementable mitigation does not score credit on Actionability. "Consider adding validation" earns 0 on that threat's Actionability contribution.

3. **Consistency across agents is required.** If pm-customer-insight has a prompt injection threat from customer quotes and pm-market-strategist has a structurally identical threat from CRM export data, both must be enumerated. Missing the structural parallel drops Internal Consistency.

4. **Calibrate to the actual architecture.** The 5-agent model, the T3 tool tier for all agents, the filesystem-mediated cross-agent data flow, and the keyword-based routing are the specific architectural facts. Threats and mitigations must reference these specifics, not generic LLM agent patterns.

### Scoring Process for Phase 2 Security Artifacts

The adversary review at Phase 2 barrier applies 6 strategies in 4 executor groups:

- **Group A (S-007):** Constitutional AI Critique -- particular focus on pm-competitive-analyst handling P-022 (deception about data provenance)
- **Group B (S-002):** Devil's Advocate -- challenges whether threat model coverage is genuinely comprehensive
- **Group C (S-012 + S-013):** FMEA on cross-agent data flow failure modes; Inversion on maximizing security gaps
- **Group D (S-014):** Two-pass LLM-as-Judge scoring (independent first, then finding-adjusted)

---

*Handoff version: handoff-v2*
*Source: Phase 1 Quality QA Strategy artifact*
*Destination: Phase 2 Security Agent Review pipeline*
