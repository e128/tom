# UX Routing Rules

<!-- PARTIAL: Created during PROJ-022 Foundation phase. Routing table populated; full dispatch logic in EPIC-001. -->

> Lifecycle-stage routing logic for the ux-orchestrator agent. Maps product lifecycle stages to sub-skill sequences and manages CRISIS routing.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Lifecycle Stage Router](#lifecycle-stage-router) | Product stage to sub-skill mapping |
| [CRISIS Routing](#crisis-routing) | Emergency 3-skill fixed sequence |
| [Wave-Aware Routing](#wave-aware-routing) | Routing behavior when sub-skills are not yet deployed |
| [Bypass Routing](#bypass-routing) | Wave bypass prompt presentation rules |

---

## Lifecycle Stage Router

<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — 4-step sequential triage. -->
<!-- PARTIAL IMPLEMENTATION: Routing table populated. Full dispatch logic in EPIC-001. -->

The orchestrator implements lifecycle-stage routing as a 4-step sequential triage:

1. **ONBOARD:** Display HIGH RISK user research warning (first invocation per session via session state flag)
2. **CAPACITY CHECK:** Ask team UX time allocation. If < 20% of one person's time: recommend Wave 1 sub-skills only (P-020: user decides)
3. **MCP CHECK:** Detect MCP availability via lightweight Context7 resolve call. If unavailable: route to non-MCP fallback paths
4. **STAGE TRIAGE:** Route by product lifecycle stage using the table below

### Stage Routing Table

| Stage Category | User Intent | Routes To | Wave | Qualification Question |
|---------------|-------------|-----------|------|----------------------|
| Before design | Don't know what to build | `/ux-jtbd` | 1 | — |
| Before design | Need to prioritize features | `/ux-kano-model` | 4 | — |
| Before design | Need validated prototype | `/ux-design-sprint` | 5 | — (bypass prompt if Wave 5 not deployed) |
| During design | Iterating on existing design | `/ux-lean-ux` OR `/ux-heuristic-eval` | 2 / 1 | "Are you testing hypotheses or evaluating an existing interface?" |
| During design | Building component system | `/ux-atomic-design` | 3 | — |
| During design | Building AI product | `/ux-ai-first-design` (if Enabler DONE) OR `/ux-heuristic-eval` + PAIR | 5 / 1 | — |
| After launch | Measure UX health | `/ux-heart-metrics` | 2 | — |
| After launch | Users not completing action | `/ux-behavior-design` | 4 | — |
| Any stage | Check accessibility | `/ux-inclusive-design` | 3 | — |
| CRISIS | Urgent UX problems | Fixed 3-skill sequence (see [CRISIS Routing](#crisis-routing)) | 1,4,2 | — (user confirms CRISIS entry) |

### Ambiguity Resolution

When STAGE TRIAGE produces multiple matches (e.g., "iterate on our accessible checkout"), the orchestrator applies the ordering protocol from `agent-routing-standards.md` [Multi-Skill Combination]:
- Content before quality
- Work before presentation
- If ambiguity remains after ordering: ask the user per H-31

### Common Intent Resolution

| User Says | Routes To | Qualification |
|-----------|----------|---------------|
| "Improve my UX" / "Make this more usable" | Heuristic Eval (existing) or Design Sprint (no design) | "Do you have an existing design?" |
| "Fix a specific UX problem" | Behavior Design (behavioral) or Heuristic Eval (design-level) | "Is the problem about user behavior or design quality?" |
| "Decide what to build" | JTBD (strategic) or Kano (prioritize known features) | "Are you defining the problem or prioritizing features?" |
| "Measure whether UX is working" | HEART Metrics | No qualification needed |
| "Make this accessible" | Inclusive Design | No qualification needed |

---

## CRISIS Routing

<!-- TODO (EPIC-001): Define the fixed 3-skill CRISIS sequence with P-020 compliance. -->

Pending implementation. CRISIS mode executes a fixed sequence: Heuristic Evaluation → Behavior Design → HEART Metrics. User confirms entry into CRISIS mode (P-020 compliance). Rationale: evaluate (identify UX issues) → diagnose (behavioral root cause via Fogg B=MAP) → measure (quantify impact). See SKILL.md Section "CRISIS Mode" for authoritative sequence.

---

## Wave-Aware Routing

<!-- TODO (EPIC-001): Define behavior when a routed sub-skill is not yet deployed (wave not yet signed off). -->

Pending implementation. Router must check wave signoff state before routing to gated sub-skills.

---

## Bypass Routing

<!-- TODO (EPIC-001): Define 3-field bypass prompt presentation and documentation rules. -->

Pending implementation. Bypass requires: unmet criterion, impact assessment, remediation plan.

---

*Rule file: ux-routing-rules.md*
*Parent skill: /user-experience*
*Created: 2026-03-03*
*Status: PARTIAL — Routing table populated; full dispatch logic tracked in EPIC-001*
