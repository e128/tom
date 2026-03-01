# Cross-Pollination Handoff: Engineering to Security

**Barrier:** 1
**Date:** 2026-03-01
**Schema:** handoff-v2

---

```yaml
from_agent: eng-architect
to_agent: red-vuln
task: "Validate Tier 1 agent definitions against threat model; incorporate architecture decisions into Phase 2 agent security review and prompt injection testing"
success_criteria:
  - "All 3 Tier 1 agents (pm-product-strategist, pm-customer-insight, pm-market-strategist) reviewed for prompt injection vectors mapped to their specific input types"
  - "Guardrail recommendations from attack-surface.md incorporated into Phase 2 agent .md guardrails sections and .governance.yaml input_validation/output_filtering"
  - "Discovery/delivery mode switching attack surface (MS-01 through MS-04) validated against architecture.md mode selection logic and promotion requirements"
  - "Cross-agent data flow risks (DF-01 through DF-10) mapped to the specific artifact ownership boundaries defined in architecture.md"
  - "Sensitivity classification defaults per agent (frontmatter-schema.md Section 'Sensitivity Field Specification') validated against threat model TH-005 and TH-007"
artifacts:
  - "eng/phase-1-research/architecture.md"
  - "eng/phase-1-research/frontmatter-schema.md"
key_findings:
  - "5-agent model with zero artifact ownership overlap creates clean security boundaries: each agent writes to its own artifact namespace, reducing cross-write attack surface. pm-product-strategist is the primary aggregation agent consuming outputs from all 4 peers, making it the highest-value indirect injection target (aligns with attack-surface.md Section 5.3 trust chain contamination)."
  - "All 5 agents are T3 (External) tier with WebSearch/WebFetch access. No agent is T5 (no Task tool). This means all agents can reach external sources (TB-5 boundary) but cannot spawn sub-agents (P-003 enforced via tools frontmatter). T3 tier assignment expands the attack surface for all agents beyond T2-only read-write."
  - "Discovery/delivery mode architecture includes explicit promotion requirements with per-artifact-type minimum completeness criteria (architecture.md 'Discovery-to-Delivery Promotion Requirements' table). Mode switching is governed by frontmatter status field progression: draft -> discovery -> delivery -> final -> archived. The one-way transition (delivery cannot revert to discovery) is a security-relevant constraint that prevents mode downgrade attacks."
  - "Artifact frontmatter schema introduces security-critical fields: sensitivity (public/internal/confidential/restricted) with agent-specific defaults (pm-customer-insight and pm-business-analyst default to confidential), risk_domain (value-risk/business-viability-risk), and cross_refs (bidirectional artifact links). The sensitivity non-downgrade rule prevents agents from lowering classification below their default without P-020 user override."
  - "Cross-agent data flows are mediated exclusively through filesystem artifacts (P-003 compliant -- no direct agent-to-agent invocation). Data flow paths (architecture.md 'Data Flow Patterns' table) define 8 named flows. The aggregation chain into pm-product-strategist is the critical path for taint propagation: pm-customer-insight (PII), pm-competitive-analyst (competitive intel), pm-business-analyst (financial data), and pm-market-strategist (GTM context) all flow into PRDs and Vision documents."
blockers: []
confidence: 0.93
criticality: C3
```

---

## Context for Phase 2 Security Review

The Phase 2 security pipeline (agent-sec-review.md, prompt-injection.md) should focus on validating the following architecture decisions that carry security implications:

### Agent Boundary Security Implications

Reference: `eng/phase-1-research/architecture.md` Section "Agent Boundary Definitions"

- Each agent has explicitly defined "Does NOT own" exclusions -- these are enforcement boundaries that should be validated in agent guardrails
- Routing keywords per agent create the attack surface for agent impersonation (threat S-01 in threat-model.md)
- The pm-product-strategist spans both Value Risk and Viability Risk (cross-risk agent), giving it the broadest data access and making its guardrails the highest priority for security review

### Frontmatter Fields Requiring Security Validation

Reference: `eng/phase-1-research/frontmatter-schema.md` Section "Artifact Frontmatter Schema"

- `sensitivity` field: Agent-specific defaults (confidential for pm-customer-insight, pm-business-analyst, pm-competitive-analyst; internal for pm-product-strategist, pm-market-strategist) must be enforced in agent guardrails
- `risk_domain` field: Maps to Cagan risk categories; security review should verify agents cannot produce artifacts outside their declared risk domain
- `cross_refs` field: Bidirectional artifact links create the data flow graph; cross-reference chain poisoning (threat T-06) requires validation
- `content_hash` field: Referenced in attack-surface.md guardrails but not yet defined in frontmatter schema -- Phase 2 should resolve this gap
- `mode` field: Regex validation `^(discovery|delivery)$` is specified in governance YAML but needs injection-resistant enforcement

### Discovery/Delivery Mode Attack Surface

Reference: `eng/phase-1-research/architecture.md` Section "Discovery vs Delivery Mode Architecture"

- Mode selection logic uses keyword-based heuristic at the orchestrator level -- trivially exploitable per MS-01
- Promotion requirements table provides minimum completeness criteria per artifact type -- these are the prerequisite checks that MS-02 (discovery artifact spoofing) would target
- The `delivery_sections_complete` boolean field in frontmatter is a gate for delivery-to-final transition -- this field must resist tampering
- Post-transition verification via `/adversary` quality gate is the compensating control for mode switching abuse

---

*Handoff version: handoff-v2*
*Source: Phase 1 Engineering Research artifacts*
*Destination: Phase 2 Security Agent Review pipeline*
