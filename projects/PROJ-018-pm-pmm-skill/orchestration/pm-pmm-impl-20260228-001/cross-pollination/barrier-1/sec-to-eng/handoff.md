# Cross-Pollination Handoff: Security to Engineering

**Barrier:** 1
**Date:** 2026-03-01
**Schema:** handoff-v2

---

```yaml
from_agent: red-vuln
to_agent: eng-architect
task: "Incorporate threat model mitigations and attack surface guardrails into Phase 2 Tier 1 agent definitions (.md system prompts and .governance.yaml guardrails)"
success_criteria:
  - "All Critical-rated threats (TH-001, TH-002, TH-003, TH-005, TH-006) have corresponding guardrail entries in the 3 Tier 1 agent .governance.yaml files"
  - "Per-agent guardrail recommendations from attack-surface.md Section 12 are implemented in agent system prompt <guardrails> sections"
  - "Sensitivity classification enforcement (non-downgrade rule) is implemented in agent output filtering guardrails"
  - "Prompt injection mitigations for each Tier 1 agent's specific input types are encoded in input_validation rules"
  - "Cross-agent data flow guardrails (content hash verification, sensitivity enforcement, aggregation summarization policy) are included in pm-product-strategist's session_context.on_receive"
artifacts:
  - "sec/phase-1-threat-model/threat-model.md"
  - "sec/phase-1-threat-model/attack-surface.md"
key_findings:
  - "20 threats identified via STRIDE analysis (TH-001 through TH-020). Five are rated Critical: TH-001 (prompt injection via customer quotes targeting pm-customer-insight), TH-002 (prompt injection via competitor web content targeting pm-competitive-analyst), TH-003 (cross-agent taint propagation through the aggregation chain into pm-product-strategist), TH-005 (competitive intelligence leakage from battle cards into broadly-distributed PRDs), TH-006 (financial data exposure from business cases into product artifacts). Phase 2 agent definitions MUST include mitigations for all Critical threats affecting their respective agents."
  - "67 attack vectors enumerated across 9 attack surface layers (L1-L9). The highest-severity layers are: L1 (user input -- 15 vectors, Critical), L3 (agent system prompts -- 4 vectors, Critical), L7 (persisted artifacts -- 8 vectors, Critical). All layers currently have zero controls in pre-Phase-2 state. The attack-surface.md Section 12 provides per-agent guardrail recommendations that should be transcribed directly into Phase 2 .governance.yaml guardrails."
  - "Per-agent prompt injection profiles differ significantly by input type: pm-customer-insight faces PI-CI-01 through PI-CI-03 (customer quotes, survey responses, support tickets -- all treated as authoritative content by design), pm-product-strategist faces PI-PS-01 through PI-PS-03 (aggregated artifacts as highest-value indirect injection target), pm-market-strategist faces PI-MS-01 through PI-MS-03 (CRM exports with multi-user-populated fields creating distributed injection surface). Agent guardrails MUST be tailored to each agent's specific input profile, not generic."
  - "Discovery/delivery mode switching has 4 attack vectors (MS-01 through MS-04). The most exploitable is MS-01 (keyword-based mode forcing) which is trivial because mode selection is keyword-based. Recommended mitigations: prerequisite checklist enforcement, explicit user confirmation for mode switching (not keyword inference), mode transparency via mandatory frontmatter field, prerequisite quality check on discovery artifacts before delivery promotion."
  - "Trust boundary analysis identifies 6 boundaries (TB-0 through TB-5). The critical gap is TB-4 (agent-to-agent via filesystem): there is no second trust boundary check between artifact write and artifact read. The recommended data flow guardrails (content hash verification, sensitivity classification enforcement, aggregation summarization policy, provenance chain, namespace isolation) MUST be incorporated into agent session_context.on_receive and output_filtering specifications."
blockers: []
confidence: 0.91
criticality: C3
```

---

## Threat Mitigations Required in Phase 2 Agent Definitions

### Critical Threats Mapped to Tier 1 Agents

Reference: `sec/phase-1-threat-model/threat-model.md` Section 6 "Threat Catalog"

| Threat ID | Agent Affected | Mitigation Required in Agent Definition |
|-----------|---------------|----------------------------------------|
| TH-001 | pm-customer-insight | Wrap customer quotes in `<customer_quote source="unverified" trust="untrusted">` delimiters in system prompt; add input_validation rule forbidding execution of customer-sourced content; strip system-role speaker labels from transcript inputs |
| TH-002 | pm-competitive-analyst (Tier 2) | External source tagging with `<external_source trust="untrusted" origin="competitor">` delimiters; invisible Unicode stripping; provenance tracking in battle card frontmatter -- defer to Phase 3 |
| TH-003 | pm-product-strategist | Content hash verification on ingested artifacts (on_receive); sensitivity classification enforcement (non-downgrade); aggregation summarization policy (summarize rather than reproduce verbatim from confidential sources) |
| TH-005 | pm-product-strategist, pm-market-strategist | Output filtering guardrail: competitive intelligence from confidential sources must be summarized, not quoted verbatim, in artifacts with lower sensitivity classification |
| TH-006 | pm-product-strategist | Output filtering guardrail: financial figures from pm-business-analyst (Tier 2, confidential) must be presented as ranges or rounded values in internal-classified PRDs, not exact figures |

### Per-Agent Guardrail Requirements from Attack Surface Analysis

Reference: `sec/phase-1-threat-model/attack-surface.md` Section 12 "Recommended Guardrails Per Agent"

**pm-product-strategist (Tier 1):**
- input_validation: Artifact path existence check on all cross_refs before ingestion; injection pattern scanning on ingested artifact content; mode prerequisite validation before delivery mode
- output_filtering: Sensitivity non-downgrade enforcement; aggregation summarization for confidential sources; framework application must produce canonical output structure (prevents injection-via-framework-parameter)
- forbidden_actions: P-003 (no subagents), P-020 (no overriding product direction), P-022 (no misrepresenting confidence), no delivery without discovery, no architecture decisions

**pm-customer-insight (Tier 1):**
- input_validation: Customer quote delimiting (untrusted tags); speaker label sanitization; PII detection patterns (email, phone, LinkedIn URL); mode format validation
- output_filtering: Confidence level required on all persona hypotheses; all claims must cite interview or data source; journey maps must include Moments of Truth; no secrets in output
- forbidden_actions: P-003, P-020 (no overriding segment focus), P-022 (no misrepresenting validation status), no buyer personas, no pricing recommendations

**pm-market-strategist (Tier 1):**
- input_validation: CRM export field sanitization; mode format validation; analyst report content delimiting
- output_filtering: Positioning must follow Dunford 5-step structure; GTM plans must include success metrics; buyer personas must distinguish from user personas; no secrets in output
- forbidden_actions: P-003, P-020 (no overriding positioning decisions), P-022 (no misrepresenting PMF status), no user personas, no financial models

### Sensitivity Classification Enforcement Requirements

Reference: `sec/phase-1-threat-model/threat-model.md` Section 6 (TH-005, TH-007); `eng/phase-1-research/frontmatter-schema.md` Section "Sensitivity Field Specification"

- Agent-specific sensitivity defaults MUST be enforced: pm-customer-insight defaults to `confidential`, pm-business-analyst defaults to `confidential`, pm-competitive-analyst defaults to `confidential`
- Non-downgrade rule: agents MUST NOT set sensitivity lower than their default without explicit P-020 user override
- Cross-agent sensitivity propagation: downstream agents consuming a `confidential` source artifact MUST maintain `confidential` or higher in their output

---

*Handoff version: handoff-v2*
*Source: Phase 1 Security Threat Model and Attack Surface artifacts*
*Destination: Phase 2 Engineering Tier 1 Agent Implementation pipeline*
