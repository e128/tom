# Pre-Mortem Report: skills/user-experience/SKILL.md

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `skills/user-experience/SKILL.md` (v1.0.0)
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied in iteration 2 of C4 adversarial review cycle; S-002 Devil's Advocate applied in iteration 3. Pre-mortem operates on the strengthened deliverable (iteration 3 score reflects steelmanned + devil's-advocated version).
**Failure Scenario:** It is September 2026. The `/user-experience` skill has been deployed for 6 months. It has failed. Teams are not using it. Teams that tried it abandoned it. The framework has been removed from the active skills list and is pending deprecation. We are investigating why.

---

## Summary

13 failure causes identified (3 Critical, 6 Major, 4 Minor). The pre-mortem reveals a coherent pattern across failure modes: the skill is architecturally sound but operationally stranded. The wave model traps the most high-value tools (Design Sprint, AI-First) behind prerequisites that tiny teams cannot meet; the orchestrator's synthesis mechanism — the primary reason to prefer this skill over direct sub-skill invocation — is deferred to EPIC-001 and therefore absent at deployment; and the 10 declared sub-skill agents (all `[PLANNED: Wave N]`) mean 9 of 11 agents are non-functional at the v1.0.0 launch. The skill fails not because its design is wrong, but because it ships incomplete while presenting itself as complete. Recommendation: **REVISE** to address Critical P0 findings before advancing toward C4 acceptance.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-20260303T004 | Wave architecture gates highest-value tools behind unreachable prerequisites for tiny teams | Assumption | High | Critical | P0 | Methodological Rigor |
| PM-002-20260303T004 | 9 of 11 agents are `[PLANNED]` at v1.0.0 -- skill deploys with orchestrator routing to non-existent workers | Technical | High | Critical | P0 | Completeness |
| PM-003-20260303T004 | Cross-framework synthesis mechanism deferred to EPIC-001: primary orchestrator value proposition unimplemented | Process | High | Critical | P0 | Completeness |
| PM-004-20260303T004 | MCP dependency failures cause silent degradation with no user-visible warning until evaluation is complete | Technical | High | Major | P1 | Actionability |
| PM-005-20260303T004 | Synthesis confidence gate LOW outputs have no actionable path: teams receive reference-only labels and stop | Process | Medium | Major | P1 | Actionability |
| PM-006-20260303T004 | Wave bypass mechanism requires 3-field documentation but no enforcement or tooling exists | Process | High | Major | P1 | Methodological Rigor |
| PM-007-20260303T004 | AI-first design sub-skill requires Enabler DONE + WSM >= 7.80: these gates are opaque and potentially unachievable | Assumption | Medium | Major | P1 | Actionability |
| PM-008-20260303T004 | CRISIS mode sequence conflicts with SKILL.md description: Heuristic Eval → Behavior Design → HEART (document) vs Heuristic Eval → HEART → JTBD (rule stub) | Technical | Medium | Major | P1 | Internal Consistency |
| PM-009-20260303T004 | Teams with no MCP budget cannot access 4 REQ-MCP sub-skills; cost tier framing underrepresents this barrier | External | Medium | Major | P1 | Evidence Quality |
| PM-010-20260303T004 | Wave signoff templates are `[PLANNED]` -- teams cannot complete Wave 0→1 transition without the kickoff template | Technical | High | Minor | P2 | Completeness |
| PM-011-20260303T004 | Routing disambiguation binary questions misroute real UX problems that span multiple dimensions | Assumption | Medium | Minor | P2 | Actionability |
| PM-012-20260303T004 | ADR-PROJ022-002 wave criteria threshold justification is marked `(pending)`: threshold is undocumented | Process | Low | Minor | P2 | Traceability |
| PM-013-20260303T004 | Tiny team attrition: 1 UX person departing mid-wave orphans all in-progress wave state and synthesis context | External | Medium | Minor | P2 | Methodological Rigor |

---

## Detailed Findings

### PM-001: Wave Architecture Gates Highest-Value Tools Behind Unreachable Prerequisites [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Wave Architecture (lines 248-283), Lifecycle-Stage Routing (lines 287-326) |
| **Category** | Assumption |
| **Likelihood** | High |
| **Priority** | P0 |
| **Affected Dimension** | Methodological Rigor |

**Failure Cause:**

It is September 2026. Teams who invoked `/user-experience` for the first time and asked "We need to figure out what to build" were routed to `/ux-jtbd` (Wave 1). Teams who asked "We need a validated prototype quickly" were told Design Sprint is Wave 5, requires 30+ users for Kano (Wave 4), Storybook with 5+ atoms (Wave 3), and a launched product with analytics (Wave 2). None of these tiny teams with UX as 20-50% of one person's time reached Wave 2, let alone Wave 5. The wave architecture, designed to ensure methodological maturity, instead became a permanent barrier to the tools most needed at product inception.

The bypass mechanism existed on paper but required the user to understand wave states, write 3-field bypass documentation, and navigate the orchestrator's wave gate prompts — cognitive overhead that tiny teams refused to absorb. Teams abandoned the skill and returned to ad-hoc Figma reviews.

**Evidence:** SKILL.md lines 259-260: Wave 5 entry requires "Wave 4: 30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed." Lines 305-306: `"During design: Need validated prototype" -> /ux-design-sprint`. The lifecycle router maps the most urgent early-stage need directly to a Wave 5 tool without presenting the bypass path inline. The note on lines 261-262 explains the Design Sprint early-access mechanism, but it is buried in a nested blockquote and not surfaced in the routing table itself.

**Mitigation:** The routing table must present Design Sprint as Wave 1-accessible with explicit inline bypass conditions. The orchestrator should present a "Your wave state is 0 — Design Sprint requires Wave 5. Would you like to proceed with early access? Bypass requires [two-sentence description]" prompt *at routing time*, not require the user to discover the bypass mechanism from documentation. Add a "Minimum Viable Wave" column to the wave table showing the earliest wave at which each sub-skill can be accessed via bypass.

**Acceptance Criteria:** A tiny team at Wave 0 who invokes "We need a validated prototype" receives a Design Sprint bypass prompt within 2 orchestrator turns, with bypass conditions that can be satisfied in under 5 minutes of documentation effort.

---

### PM-002: 9 of 11 Agents Are `[PLANNED]` at v1.0.0 — Skill Deploys with Routing to Non-Existent Workers [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | References — Agent Definition Files (lines 556-569) |
| **Category** | Technical |
| **Likelihood** | High |
| **Priority** | P0 |
| **Affected Dimension** | Completeness |

**Failure Cause:**

It is September 2026. The SKILL.md shipped in v1.0.0 with `agents` frontmatter listing 11 agents. Only `ux-orchestrator` exists as a stub. All 10 sub-skill agents were `[PLANNED: Wave N]`. When the orchestrator received a routing request and invoked `Task(subagent_type="ux-heuristic-evaluator", ...)`, Claude Code could not resolve the agent. The orchestrator failed with an unrecoverable error that was surfaced to the user as an opaque "agent not found" message.

Teams who tried Wave 1 immediately encountered this failure. Because the SKILL.md presented the full 11-agent roster as if all agents existed, users had no warning they were about to hit a resolution failure. The first impression of `/user-experience` was a crash.

**Evidence:** SKILL.md lines 557-569: 10 of 11 agent rows have status `[PLANNED: Wave N]`. The `agents` frontmatter field (line 16-26) lists all 11 agents including `ux-heuristic-evaluator`, `ux-jtbd-analyst`, etc., which do not exist as files. SKILL.md version is `1.0.0` (line 14) with no `status: ALPHA` or `status: IN_PROGRESS` qualifier.

**Mitigation:** Either (1) remove all `[PLANNED]` agents from the `agents` frontmatter field and only add them when their implementation files exist, or (2) add a `status: alpha` field to the SKILL.md frontmatter with a banner at the top of the document: "Wave 1 agents available. Waves 2-5 are planned. Invoking a Wave 2-5 sub-skill before implementation will result in an agent resolution error." Add an `agent-availability` section to Quick Reference listing which agents are available now vs. planned.

**Acceptance Criteria:** A user invoking any sub-skill receives either a working agent response or a clear, specific message: "ux-heuristic-evaluator is planned for Wave 1 implementation (PROJ-022 EPIC-001). Expected availability: [date]. Currently available agents: [list]." No unrecoverable opaque errors.

---

### PM-003: Cross-Framework Synthesis Mechanism Deferred to EPIC-001 — Primary Value Proposition Unimplemented [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Purpose (line 91), Available Agents (line 143), Cross-Skill Integration (line 441), P-003 Compliance (line 168) |
| **Category** | Process |
| **Likelihood** | High |
| **Priority** | P0 |
| **Affected Dimension** | Completeness |

**Failure Cause:**

It is September 2026. Teams who used `/user-experience` for multi-framework workflows asked the orchestrator to synthesize a Heuristic Eval + JTBD finding. The orchestrator, running from a stub `.md` with no `<methodology>` section, had no documented protocol for synthesis. It produced ad-hoc text combining the two reports without applying the convergence/contradiction classification defined in the Synthesis Hypothesis Validation section (lines 329-384). Output quality varied session to session. Teams could not verify whether the synthesis was following any methodology. The cross-framework synthesis — described as the reason to use the orchestrator over direct sub-skill invocation — was unverifiable and inconsistent.

The SKILL.md has a detailed 4-step Cross-Framework Synthesis Protocol (lines 373-384) but the orchestrator agent stub (lines 23-26 of `ux-orchestrator.md`) explicitly defers full implementation to EPIC-001. The two documents are inconsistent: SKILL.md promises a mechanism; the agent definition admits it does not exist.

**Evidence:** SKILL.md lines 91-92: "The User-Experience skill provides AI-augmented UX methodology...produces persistent artifacts...enforces methodological rigor via synthesis hypothesis confidence gates." Lines 373-384: Cross-Framework Synthesis Protocol with 4 named steps. `ux-orchestrator.md` lines 23-26: `<!-- STUB: Full agent definition to be implemented in PROJ-022 EPIC-001. -->`. No `<methodology>` section in `ux-orchestrator.md`.

**Mitigation:** Add a minimal `<methodology>` section to `ux-orchestrator.md` that implements at least the 4-step synthesis protocol described in SKILL.md. The methodology does not need to be complete, but it must be sufficient for the orchestrator to execute the documented synthesis algorithm. Alternatively, add a "Capabilities Limitation" section to SKILL.md v1.0.0 stating explicitly: "Cross-framework synthesis is not yet implemented. The orchestrator routes and gates; synthesis requires direct user assembly of sub-skill outputs in v1.0.0."

**Acceptance Criteria:** Either the orchestrator's `<methodology>` section implements the 4-step synthesis protocol, OR SKILL.md v1.0.0 documents the synthesis capability as deferred with a target wave/version for delivery.

---

### PM-004: MCP Dependency Failures Cause Silent Degradation with No User-Visible Warning Until Evaluation Is Complete [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | MCP Integration Architecture (lines 388-437) |
| **Category** | Technical |
| **Likelihood** | High |
| **Priority** | P1 |
| **Affected Dimension** | Actionability |

**Failure Cause:**

It is September 2026. Teams without Figma MCP configured invoked `/ux-heuristic-eval` to evaluate their design. The orchestrator's MCP CHECK step (Lifecycle-Stage Routing, line 296) detected unavailable MCPs but did not quantify which sub-skills would be degraded. The user received routing to `/ux-heuristic-eval` with no advance warning that the session would operate in "screenshot-input mode" rather than live Figma analysis. After completing a 30-minute evaluation, the output was labeled "text-only mode" in the final artifact — discovered post-investment.

**Evidence:** SKILL.md line 296: "If MCP unavailable: route to non-MCP fallback paths." Lines 413-417: Figma fallbacks defined. Lines 433-435: "When MCP tools are unavailable, all agents operate in text-only mode... Agents MUST note 'text-only mode' in their output." The warning is post-completion, not pre-routing. The MCP CHECK step routes to fallback silently without surfacing the quality implication.

**Mitigation:** The orchestrator's MCP CHECK step must surface a pre-routing notice: "Figma MCP is unavailable. [Sub-skill name] will operate in screenshot-input mode, which [specific quality implication]. Would you like to proceed in text-only mode or pause to configure Figma MCP?" This is a P-020 compliance mechanism: the user decides with full information, not after investment. Add a `mcp_degradation_notice` output field to the routing response.

**Acceptance Criteria:** A user with no Figma MCP configured who invokes a Figma-REQ sub-skill receives an explicit degradation notice and confirmation prompt BEFORE the sub-skill begins execution.

---

### PM-005: Synthesis Confidence Gate LOW Outputs Have No Actionable Path — Teams Receive Reference-Only Labels and Stop [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Synthesis Hypothesis Validation (lines 332-365) |
| **Category** | Process |
| **Likelihood** | Medium |
| **Priority** | P1 |
| **Affected Dimension** | Actionability |

**Failure Cause:**

It is September 2026. Teams ran `/ux-kano-model` Feature Priority Conflict Interpretation (confidence: LOW) and `/ux-behavior-design` Design Intervention Recommendation (confidence: LOW). Both outputs were `[REFERENCE-ONLY]` with the design recommendation section omitted. Teams received analysis artifacts with no guidance on what to do next: how do you elevate a LOW confidence output? How many users must be surveyed? What specific validation action converts a LOW to MEDIUM? The outputs were tombstoned with no path forward. Teams stopped using the sub-skills that mattered most for their product decisions.

**Evidence:** SKILL.md lines 363-365: LOW gate behavior: "Output template structurally omits the design recommendation section. Tagged with `[REFERENCE-ONLY]` in title. Notice: 'This output reflects AI synthesis from training data. It does not contain design recommendations.'" No "Next Steps to Elevate Confidence" section defined for LOW outputs. Sub-skill synthesis output map (lines 344-358) shows 5 of 12 synthesis steps as LOW, including `/ux-kano-model` feature priority conflict (LOW) and `/ux-ai-first-design` AI interaction pattern recommendations (LOW).

**Mitigation:** Every LOW confidence output must include a "Path to MEDIUM Confidence" section: specific validation actions (e.g., "Interview 3 users using [specific script template]"), minimum data requirements, and estimated effort. The reference-only label must be accompanied by a concrete next step, not a dead end. For `/ux-ai-first-design` specifically, if ALL outputs are LOW, document this upfront in the sub-skill description so teams can calibrate expectations before invocation.

**Acceptance Criteria:** Every LOW-confidence synthesis output includes a "Validation Path" section with: (1) specific validation action, (2) minimum data requirement to advance to MEDIUM, and (3) estimated effort in person-hours.

---

### PM-006: Wave Bypass Mechanism Has No Enforcement or Tooling — Teams Bypass Without Documentation [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Wave Architecture (line 277), References — Rule Files (line 578) |
| **Category** | Process |
| **Likelihood** | High |
| **Priority** | P1 |
| **Affected Dimension** | Methodological Rigor |

**Failure Cause:**

It is September 2026. The wave bypass mechanism was used by 80% of teams who advanced past Wave 1. The 3-field documentation requirement existed in the SKILL.md but `rules/wave-progression.md` was a stub with "Pending implementation." No tooling validated bypass documentation. No warning banner appeared on sub-skill outputs from bypassed waves. The orchestrator accepted bypass intent from the user but did not validate documentation completeness before proceeding. Wave progression became theater: teams bypassed freely without tracking technical debt. When teams later encountered quality failures (sub-skill outputs that assumed Wave N prerequisites), they had no audit trail connecting the failure to a specific bypass decision.

**Evidence:** SKILL.md line 277: "Wave bypass: Requires 3-field documentation (unmet criterion, impact assessment, remediation plan with target date)." `skills/user-experience/rules/wave-progression.md` lines 44-47: "Pending implementation. Bypass fields: 1. Unmet criterion... 2. Impact assessment... 3. Remediation plan." No schema defined. No enforcement described. No file path for bypass documentation.

**Mitigation:** The bypass mechanism must be implemented before Wave 1 deployment: (1) define a machine-readable bypass record format (YAML or frontmatter block), (2) specify the file path where bypass records are persisted (`skills/user-experience/output/{engagement-id}/WAVE-BYPASS-LOG.md`), (3) implement orchestrator validation that checks bypass record completeness before proceeding, (4) define the "warning banner" format and the agents that must display it. Stub `wave-progression.md` must be fully implemented before SKILL.md is marked v1.0.0 complete.

**Acceptance Criteria:** A wave bypass attempt without valid 3-field documentation is rejected by the orchestrator with a specific prompt to complete the missing fields. Bypass records persist to a defined file path that is referenced in WAVE-N-SIGNOFF.md.

---

### PM-007: AI-First Design Sub-Skill Requires Enabler DONE + WSM >= 7.80 — Gate is Opaque and Potentially Unachievable [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Wave Architecture (line 259), Available Agents (line 153) |
| **Category** | Assumption |
| **Likelihood** | Medium |
| **Priority** | P1 |
| **Affected Dimension** | Actionability |

**Failure Cause:**

It is September 2026. A team building an AI product invoked `/user-experience` asking for AI interaction design guidance. The orchestrator checked Wave 5 entry criteria: "AI-First: Enabler DONE + WSM >= 7.80." The team had no idea what "WSM" meant. The orchestrator could not explain it (no definition in SKILL.md). "Enabler DONE" referred to an unspecified worktracker Enabler entity that the team had never created. The sub-skill was permanently inaccessible: the prerequisites were neither self-explanatory nor achievable by teams who had not read PROJ-022 WORKTRACKER.md. Teams building AI products — a primary use case for 2026 — could not use the sub-skill that was most relevant to them.

**Evidence:** SKILL.md line 259: "AI-First: Enabler DONE + WSM >= 7.80" — "WSM" is not defined anywhere in SKILL.md. "Enabler DONE" references a worktracker construct not explained in this document. No section defines what WSM measures, how it is calculated, or what constitutes 7.80.

**Mitigation:** Define WSM (Weighted Synthesis Maturity or whatever it abbreviates) inline at first use in SKILL.md. Provide a 2-sentence formula or measurement method. Link to the Enabler entity in PROJ-022 WORKTRACKER.md. If the WSM >= 7.80 threshold is aspirational/provisional, mark it as such and provide a bypass condition for teams actively building AI products before WSM can be calculated.

**Acceptance Criteria:** A reader of SKILL.md can determine whether their team meets the AI-First Design entry criteria without consulting any external document. WSM is defined, its formula is stated, and the measurement method is self-contained.

---

### PM-008: CRISIS Mode Sequence Conflict Between SKILL.md and Rule Stub [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Lifecycle-Stage Routing (line 309-310), `rules/ux-routing-rules.md` |
| **Category** | Technical |
| **Likelihood** | Medium |
| **Priority** | P1 |
| **Affected Dimension** | Internal Consistency |

**Failure Cause:**

It is September 2026. A team in CRISIS mode (users abandoning checkout) invoked the emergency sequence. SKILL.md line 309-310 stated: "CRISIS -> Emergency 3-skill sequence: Heuristic Eval -> Behavior Design -> HEART." The rule stub `ux-routing-rules.md` described a different sequence: "CRISIS mode executes a fixed sequence: Heuristic Evaluation → HEART Metrics → JTBD Analysis." The orchestrator, implementing from the rule stub, executed a different sequence than what the SKILL.md documented. Teams who expected Behavior Design in the CRISIS sequence (appropriate for checkout abandonment — a behavioral problem) received JTBD instead. The emergency sequence was wrong for behavioral failure scenarios.

**Evidence:** SKILL.md line 309-310: "CRISIS: Urgent UX problems -> Emergency 3-skill sequence: Heuristic Eval -> Behavior Design -> HEART." `skills/user-experience/rules/ux-routing-rules.md` line 32: "CRISIS mode executes a fixed sequence: Heuristic Evaluation → HEART Metrics → JTBD Analysis." These sequences are incompatible. The SKILL.md version (Heuristic Eval → Behavior Design → HEART) is appropriate for behavioral failures; the rule stub version (Heuristic Eval → HEART → JTBD) is not.

**Mitigation:** Resolve the CRISIS sequence conflict immediately: (1) decide the authoritative sequence (SKILL.md version is more appropriate for the stated use case of "users not completing action"), (2) update `ux-routing-rules.md` to match SKILL.md exactly, (3) add the CRISIS sequence rationale inline in SKILL.md ("Heuristic Eval surfaces design-level failures; Behavior Design diagnoses motivation/ability bottlenecks; HEART measures net impact — this sequence follows cause → diagnosis → measurement").

**Acceptance Criteria:** SKILL.md and `ux-routing-rules.md` document identical CRISIS sequences with matching rationale. No discrepancy between the two documents.

---

### PM-009: Teams Without MCP Budget Cannot Access 4 REQ-MCP Sub-Skills — Cost Tier Framing Understates This Barrier [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | MCP Integration Architecture — Cost Tiers (lines 419-424) |
| **Category** | External |
| **Likelihood** | Medium |
| **Priority** | P1 |
| **Affected Dimension** | Evidence Quality |

**Failure Cause:**

It is September 2026. The cost tier table presented the "Free" tier as offering HEART, JTBD, Kano, and Behavior Design — four viable sub-skills without MCP costs. Teams read this and expected meaningful access to the skill. What the table did not communicate: 4 of 10 sub-skills (Heuristic Eval, Inclusive Design, AI-First Design, Design Sprint) require Figma or Miro at a minimum $46/month cost. For a tiny team of 1-5 people at a pre-revenue startup, $46/month for design tooling MCPs requires a budget conversation. Teams who could not access the "Minimal" tier ($46/month) were effectively locked out of the four highest-value sub-skills for rapid product development. The cost tier framing emphasized what was available for free but obscured what was inaccessible.

**Evidence:** SKILL.md lines 419-424: Cost Tiers table. "Free" tier lists 4 sub-skills available without MCP costs. The table does not state that the remaining 6 sub-skills require paid MCPs. The phrase "Sub-Skills Available" implies the listed skills are the totality available at that cost, which creates an accurate but misleading impression for teams that read across rows rather than noticing the absence of the remaining 6 skills.

**Mitigation:** Invert the cost tier framing: add a "Sub-Skills Blocked" column alongside "Sub-Skills Available," and add a "Minimum to Unlock" note showing the cheapest MCP configuration that unblocks each REQ-dependency sub-skill. Make the barrier explicit rather than implicit.

**Acceptance Criteria:** The cost tiers table explicitly states which sub-skills are blocked at each tier (not just which are available), so a team can immediately identify what they cannot access at their current MCP budget.

---

### PM-010: Wave Signoff Templates Are `[PLANNED]` — Teams Cannot Complete Wave 0→1 Transition [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | References — Templates (lines 588-592), Wave Architecture (line 265) |
| **Category** | Technical |
| **Likelihood** | High |
| **Priority** | P2 |
| **Affected Dimension** | Completeness |

**Failure Cause:** The Wave 0→1 transition requires KICKOFF-SIGNOFF.md with "All fields populated." The kickoff-signoff template is `[PLANNED: EPIC-001]`. Teams who attempted to formally progress from Wave 0 to Wave 1 had no template to complete. Informal progression without signoff meant wave state was undefined and the orchestrator's signoff check (`WAVE-{N}-SIGNOFF.md` existence test) always returned false.

**Evidence:** SKILL.md line 265: "The orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills." Lines 590-591: Both templates `kickoff-signoff-template.md` and `wave-signoff-template.md` are `[PLANNED: EPIC-001]`.

**Mitigation:** The kickoff-signoff template must be created before v1.0.0 is released, as it is required for the first transition the orchestrator will attempt. The wave-signoff template must be created before Wave 1 sub-skill deployment begins.

**Acceptance Criteria:** Both signoff templates exist and are non-stub files before the skill is marked available for production use.

---

### PM-011: Binary Routing Questions Misroute Mixed-Context UX Problems [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Lifecycle-Stage Routing — Common Intent-to-Route Resolution (lines 317-326) |
| **Category** | Assumption |
| **Likelihood** | Medium |
| **Priority** | P2 |
| **Affected Dimension** | Actionability |

**Failure Cause:** Real UX problems rarely sort cleanly into binary categories. Teams asking "Fix a specific UX problem" were asked "Is the problem about user behavior or design quality?" — a question that assumes the team has already diagnosed the problem they are trying to solve. Teams who answered wrong (or who did not know) were routed to the wrong sub-skill and received an investigation artifact that did not match their actual problem. Repeated misrouting eroded trust in the orchestrator's routing judgment.

**Evidence:** SKILL.md lines 321-322: Qualification question "Is the problem about user behavior or design quality?" is a binary choice that presupposes diagnosis already complete. The SKILL.md does not provide a third option ("I don't know") or a fallback to dual-path routing.

**Mitigation:** Add a third option to each binary qualification question: "I'm not sure." When "I'm not sure" is selected, route to the lower-overhead sub-skill first (Heuristic Eval before Behavior Design; JTBD before Kano) with an explicit note that the second sub-skill is available after the first output is reviewed.

**Acceptance Criteria:** Every binary qualification question includes an explicit "I'm not sure" branch with a defined fallback routing path.

---

### PM-012: ADR-PROJ022-002 Wave Criteria Threshold Justification Is `(pending)` — Threshold Is Undocumented [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Wave Architecture (line 275) |
| **Category** | Process |
| **Likelihood** | Low |
| **Priority** | P2 |
| **Affected Dimension** | Traceability |

**Failure Cause:** The wave gate threshold of 0.85 is justified inline as "deployment readiness" distinct from H-13's 0.92 "deliverable quality." This rationale is reasonable but the formal derivation ADR-PROJ022-002 is marked `(pending)`. If the threshold is challenged or needs adjustment based on real usage data, there is no ADR to reference. The threshold decision is not traceable to evidence.

**Evidence:** SKILL.md lines 274-276: "Threshold justification (0.85 vs H-13 0.92): ...Formal threshold derivation is tracked in `ADR-PROJ022-002-wave-criteria-gates.md` (pending)."

**Mitigation:** Either complete ADR-PROJ022-002 before the SKILL.md is marked final, or document the provisional threshold rationale inline with enough detail to reconstruct the ADR decision. A one-paragraph derivation inline is acceptable as an interim measure.

**Acceptance Criteria:** ADR-PROJ022-002 exists and is non-stub, OR the SKILL.md inline threshold rationale is marked "(provisional — ADR-PROJ022-002 target date: [date])" to communicate when formal derivation will be available.

---

### PM-013: Team Attrition Orphans In-Progress Wave State and Synthesis Context [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Synthesis Hypothesis Validation (lines 329-384), Wave Architecture (lines 246-283) |
| **Category** | External |
| **Likelihood** | Medium |
| **Priority** | P2 |
| **Affected Dimension** | Methodological Rigor |

**Failure Cause:** Tiny teams (1-5 people) have high attrition. The person who completed Wave 1 and holds the context for why specific JTBD job statements were synthesized the way they were leaves the team. No successor can reconstruct the synthesis decisions. The engagement-id based output system (`{engagement-id}/` directories) accumulates files but does not provide any "session handoff" artifact documenting: which waves are complete, which findings are still active, what the current UX health baseline is. The wave knowledge is non-transferable.

**Evidence:** SKILL.md has no "Knowledge Continuity" or "Engagement Handoff" section. The wave signoff files (lines 265-266) check existence but do not describe their contents beyond "All fields populated." No artifact type is defined for "current engagement state summary."

**Mitigation:** Define a lightweight "Engagement State Summary" artifact as a required output from each wave signoff: 1-page YAML or markdown with current hypothesis status, top 3 UX risks, and open action items. This artifact becomes the handoff document when team membership changes.

**Acceptance Criteria:** WAVE-N-SIGNOFF.md template includes an "Engagement State Summary" section sufficient for a new team member to resume without context from the previous member.

---

## Prioritized Recommendations

### P0 — Critical: MUST Mitigate Before Acceptance

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| PM-001-20260303T004 | Surface Design Sprint bypass path inline in the lifecycle routing table. Orchestrator presents bypass prompt at routing time for Wave-gated tools. Add "Minimum Viable Wave" column to wave table. | Wave 0 team invoking Design Sprint receives inline bypass prompt within 2 turns; bypass requires < 5 minutes of documentation. |
| PM-002-20260303T004 | Remove `[PLANNED]` agents from `agents` frontmatter field OR add `status: alpha` with agent availability section showing which agents exist now. Add pre-routing agent-existence check to orchestrator. | No unrecoverable agent resolution errors. User receives clear availability notice before invoking a planned agent. |
| PM-003-20260303T004 | Add minimal `<methodology>` section to `ux-orchestrator.md` implementing 4-step synthesis protocol, OR document synthesis as deferred in SKILL.md v1.0.0 Capabilities Limitation section. | Orchestrator methodology is implemented and matches SKILL.md synthesis protocol description, OR SKILL.md explicitly documents synthesis as v1.x feature. |

### P1 — Important: SHOULD Mitigate

| ID | Action | Acceptance Criteria |
|----|--------|---------------------|
| PM-004-20260303T004 | MCP CHECK step surfaces pre-routing degradation notice with user confirmation before sub-skill begins. | Figma-REQ sub-skill with unavailable Figma MCP shows degradation notice and requires confirmation before execution begins. |
| PM-005-20260303T004 | Every LOW confidence output includes a "Validation Path" section with specific action, data minimum, and effort estimate. | `/ux-kano-model` Feature Priority Conflict output includes concrete validation path even when labeled REFERENCE-ONLY. |
| PM-006-20260303T004 | Implement bypass record format and file path. Orchestrator validates bypass completeness before proceeding. `wave-progression.md` is fully implemented (no stub). | Incomplete bypass documentation is rejected with specific prompt for missing fields. |
| PM-007-20260303T004 | Define WSM inline. Link to Enabler entity. Add bypass condition for teams actively building AI products. | Reader can determine AI-First Design entry criteria from SKILL.md alone without external documents. |
| PM-008-20260303T004 | Resolve CRISIS sequence conflict. Update `ux-routing-rules.md` to match SKILL.md. Add sequence rationale inline. | SKILL.md and `ux-routing-rules.md` document identical CRISIS sequences. |
| PM-009-20260303T004 | Add "Sub-Skills Blocked" column to cost tiers table. Make MCP barriers explicit rather than implicit. | Cost tiers table shows which sub-skills are blocked at each tier, not just which are available. |

### P2 — Monitor: MAY Mitigate; Acknowledge Risk

| ID | Action | Risk Acknowledgment |
|----|--------|---------------------|
| PM-010-20260303T004 | Create both signoff templates before production deployment. | Blocking for Wave 0→1 transition. Must be resolved before first user reaches Wave 1 signoff. |
| PM-011-20260303T004 | Add "I'm not sure" option to binary qualification questions with fallback routing. | Low-effort fix; delays routing for uncertain users but prevents systematic misrouting. |
| PM-012-20260303T004 | Complete ADR-PROJ022-002 or mark threshold as provisional with target date. | Threshold decision is undocumented but inline rationale is sufficient for operating at v1.0.0. |
| PM-013-20260303T004 | Add Engagement State Summary to wave signoff templates. | Low attrition risk for very small teams; becomes critical when team membership changes during active UX work. |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | **Negative** | PM-002, PM-003, PM-010: 9 of 11 agents planned; synthesis mechanism deferred; signoff templates absent. Core deliverable promises capabilities that do not exist at v1.0.0. |
| Internal Consistency | 0.20 | **Negative** | PM-008: CRISIS sequence conflict between SKILL.md and rule stub. The skill's two canonical documents describe incompatible behavior for the same critical path. |
| Methodological Rigor | 0.20 | **Negative** | PM-001, PM-006, PM-013: Wave architecture gates highest-value tools; bypass has no enforcement; no knowledge continuity mechanism. The methodological framework has gaps that would cause systematic failure in real usage. |
| Evidence Quality | 0.15 | **Negative** | PM-007, PM-009, PM-012: WSM gate undefined; cost barrier understated; wave threshold ADR pending. Claims made without sufficient supporting evidence or measurable definitions. |
| Actionability | 0.15 | **Negative** | PM-004, PM-005, PM-007: MCP degradation is post-completion; LOW confidence outputs are dead ends; AI-First Design gate uses undefined terms. Teams cannot take action based on the skill's outputs in multiple high-frequency scenarios. |
| Traceability | 0.10 | **Neutral** | SKILL.md traces extensively to GitHub Issue #138, PROJ-022 artifacts, and standards references. PM-012 (pending ADR) is a minor gap against an otherwise strong traceability posture. |

**Overall Assessment:** Major mitigation required before C4 acceptance. 3 Critical findings (P0) represent structural deficiencies — shipping the skill as v1.0.0 while 9 of 11 agents are unimplemented, the synthesis mechanism is absent, and the wave architecture misroutes tiny teams at inception — would result in immediate adoption failure. 6 Major findings (P1) represent operationally significant gaps that would progressively erode user trust across 2-4 months of usage. The pattern is consistent: the skill's design is sound and coherent, but the gap between what is promised and what is implemented at v1.0.0 is too large to absorb. The estimated composite score improvement from addressing P0+P1 mitigations: +0.08 to +0.12 on Completeness, Methodological Rigor, and Actionability dimensions.

---

## Execution Statistics

- **Total Findings:** 13
- **Critical (P0):** 3
- **Major (P1):** 6
- **Minor (P2):** 4
- **Protocol Steps Completed:** 6 of 6
- **Failure Categories Applied:** Technical (3), Process (4), Assumption (3), External (2), Resource (1)
- **Temporal Perspective Shift:** Applied — analysis conducted from September 2026 retrospective frame

---

*Strategy: S-004 Pre-Mortem Analysis*
*Template: `.context/templates/adversarial/s-004-pre-mortem.md` v1.0.0*
*Deliverable: `skills/user-experience/SKILL.md` v1.0.0*
*Iteration: 4 of C4 adversarial review cycle*
*Agent: adv-executor*
*Date: 2026-03-03*
