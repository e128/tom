# Pre-Mortem Report: UX Framework Selection Analysis (R10)

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 10)
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004)
**H-16 Compliance:** S-003 Steelman applied (confirmed -- `projects/PROJ-020-feature-enhancements/work/analysis/tournament-iter5/s-003-steelman.md` exists)
**Failure Scenario:** It is September 2026. The `/user-experience` skill was implemented following this analysis. Six months after launch, the PROJ-020 project lead convenes a post-mortem. Teams have made significant product decisions from LOW-confidence synthesis outputs that were never validated. The AI-First Design Enabler expired at Day 30 without any substitution action. The MCP maintenance contract has no verified owner. Two sub-skills returned blank outputs silently when required MCPs failed. The `/user-experience` parent skill is routing to `/ux-design-sprint` before teams have met Wave 4 criteria, producing untested prototypes without the Design Sprint wave-entry qualification check. The analysis is considered to have "failed spectacularly" because the operational safeguards it defined were not enforceable as written.

---

## Summary

The analysis is substantially comprehensive and methodologically strong on paper; its failure mode is concentrated in operational enforceability. R10 introduced owner assignment rules, mandatory verification, and measurable Wave 5 entry criteria — all directionally correct — but the enforcement mechanisms contain five structural gaps that would predictably lead to bypass in real implementation: the owner assignment rules lack a pre-creation enforcement gate making them reactive rather than preventive; the mandatory gate verification relies on a human reviewer following a checklist without a corresponding document artifact to review; the wave transition evaluator role has no named assignment protocol; the LOW gate qualification acknowledges LLM bypass but the defense-in-depth mitigations are advisory rather than operational; and the Wave 5 Design Sprint criterion replaces one subjective test with three alternatives that have no common threshold anchor. Pre-Mortem identifies 2 Critical, 5 Major, and 3 Minor failure causes requiring targeted mitigation before the analysis can drive a safe implementation.

**Recommendation:** REVISE — targeted mitigations for P0 and P1 findings required before implementation begins.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-I6 | Owner assignment rule is reactive, not preventive: Wave 1 launch readiness gate is defined in Section 7.5, but no mechanism blocks creation of the PROJ-020 project without running the kickoff protocol | Process | High | Critical | P0 | Actionability |
| PM-002-I6 | Gate verification "MUST verify" has no verifiable artifact: Section 7.6 mandates the reviewer confirm gate templates exist in the agent's `<guardrails>` section, but no sub-skill agent definition exists yet — the reviewer has nothing to review | Process | High | Critical | P0 | Actionability |
| PM-003-I6 | Wave transition evaluator role has no named assignment path: Section 7.4 adds the evaluator role but provides no mechanism for assigning a specific person — the role is defined without an owner creation trigger | Process | High | Major | P1 | Completeness |
| PM-004-I6 | LOW gate "cannot be overridden" is a behavioral design intent, not a technical guarantee, but the defense-in-depth mitigations are advisory only | Assumption | Medium | Major | P1 | Methodological Rigor |
| PM-005-I6 | Wave 5 Design Sprint entry criterion uses three "at minimum one of" alternatives with no common measurability anchor — teams can satisfy the criterion with arbitrarily informal evidence | Process | Medium | Major | P1 | Actionability |
| PM-006-I6 | Owner assignment rule specifies the assignment moment (end of kickoff meeting) but provides no escalation path if the kickoff meeting itself is not held before Wave 1 begins | Process | Medium | Major | P1 | Completeness |
| PM-007-I6 | AI-First Design Enabler Day-30 Expiry Check task is the sole binding trigger, but the task is filesystem-based with no automated reminder — primary owner departure between task creation and Day 30 creates an unrecoverable gap | Assumption | Medium | Major | P1 | Methodological Rigor |
| PM-008-I6 | Section 7.6 synthesis gate prompt templates specify LLM behavioral constraints but no definition-of-done artifact path is specified for the reviewer to confirm implementation | Process | Low | Minor | P2 | Actionability |
| PM-009-I6 | Wave backward-pass revision protocol requires the wave transition evaluator to review contradiction resolution, but if the evaluator role is unoccupied (PM-003-I6 failure), this protocol has no executor | Assumption | Low | Minor | P2 | Completeness |
| PM-010-I6 | MCP maintenance contract secondary owner succession has identical triggers as AI-First Design Enabler succession, but the two are tracked in separate worktracker entities with no cross-reference — a single owner's departure may trigger both without either being actioned | Process | Low | Minor | P2 | Completeness |

---

## Detailed Findings

### PM-001-I6: Owner Assignment Rule Is Reactive, Not Preventive [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.5 Required Pre-Launch Worktracker Entities |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Section 7.5 states: "Wave 1 is BLOCKED until all four entity rows have owner fields populated with specific names in the PROJ-020 `WORKTRACKER.md` manifest. An implementer starting Wave 1 MUST confirm entities 1-4 exist with named owners before proceeding."

The owner assignment rule further states: "The PROJ-020 project lead is responsible for populating owner fields for entities 1-4 at the kickoff meeting."

**Analysis:**
The launch readiness gate in Section 7.5 defines a pre-condition for Wave 1 but places the responsibility for checking that pre-condition on "an implementer starting Wave 1." This is a self-policing mechanism: the person who would benefit from skipping the gate (a developer eager to start implementation) is also the person charged with confirming the gate condition. No external blocking mechanism prevents Wave 1 from starting without the gate being checked. In practice, an implementer who is unaware of Section 7.5, who reads but does not follow it, or who incorrectly believes the entities were created will proceed to Wave 1 regardless. The analysis provides no mechanism — such as a CI check on the `WORKTRACKER.md` manifest, an orchestrator pre-flight check, or a formal kickoff sign-off artifact — that would prevent Wave 1 from proceeding if the entities are absent. The failure mode is therefore not that the rule is wrong but that nothing enforces it. Six months into implementation, the Day-30 Expiry Check task (entity 2) has never been created because the Enabler entity (entity 1) was never created, because no kickoff meeting was documented, because no blocking mechanism required it.

**Recommendation:**
Add a concrete blocking artifact: a PROJ-020 kickoff sign-off document (e.g., `projects/PROJ-020-feature-enhancements/kickoff-sign-off.md`) that MUST be created with named owners before any Wave 1 work items are added to the sprint backlog. The sign-off document becomes the reviewable artifact the wave transition evaluator confirms exists. Until this document exists with all four entity rows populated, Wave 1 sprint items are not schedulable.

**Acceptance Criteria:** Section 7.5 names a specific artifact path for the kickoff sign-off document and specifies that the sign-off document is a pre-condition for adding Wave 1 work items to the sprint backlog — not a post-hoc confirmation.

---

### PM-002-I6: Gate Verification "MUST Verify" Has No Verifiable Artifact [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.6 Implementation Specification (Named tool/process) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Section 7.6 states: "The `/adversary` skill's executor agent (`adv-executor`) using S-007 Constitutional AI Critique MUST verify gate implementation compliance by checking that each sub-skill's `<guardrails>` section contains the confidence gate prompt templates. Gate verification is a mandatory item in the sub-skill's Definition of Done -- a sub-skill MUST NOT be marked DONE in the worktracker until the reviewer confirms all three confidence gate templates (HIGH/MEDIUM/LOW) are present in the sub-skill agent definition's `<guardrails>` section."

**Analysis:**
This is a sound enforcement design — verifying the agent definition file contains the required templates is a deterministic, reviewable check. However, the mechanism depends on the sub-skill agent definition file existing at the time of review. As of R10, no sub-skill agent definition files exist; they are the output of the implementation work this analysis is designed to guide. The Definition of Done gate therefore cannot be verified at the time the analysis is reviewed as a quality-gate-passing artifact, because there is nothing to verify yet.

More critically, the gate verification instruction gives the reviewer no file path to check. The analysis specifies that gate templates should appear in the sub-skill's `<guardrails>` section but does not specify where sub-skill agent definition files will be stored. Without a concrete path (e.g., `skills/user-experience/agents/{sub-skill-name}.md`), the `/adversary` skill's `adv-executor` cannot locate the files to verify. An S-007 review of an agent definition at an unspecified path will fail silently — either by searching in the wrong location or by finding no files and treating the search as an absence of violations.

**Recommendation:**
Add to Section 7.6 a concrete agent definition path template: `skills/user-experience/agents/{sub-skill-slug}.md`. Specify that the Definition of Done gate fires against the file at this path. Additionally, create a stub agent definition for the first Wave 1 sub-skill (`/ux-heuristic-eval`) as part of the analysis deliverable to demonstrate the format and give the gate check something concrete to verify before implementation begins.

**Acceptance Criteria:** Section 7.6 specifies: (1) the directory path where sub-skill agent definitions will be stored, and (2) a stub agent definition for at least one sub-skill demonstrating the required `<guardrails>` format — OR an explicit statement that the gate fires only after sub-skill implementation, with a cross-reference to the implementation plan that specifies the path.

---

### PM-003-I6: Wave Transition Evaluator Has No Named Assignment Path [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.4 Implementation Sequencing (Wave transition evaluator) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Section 7.4 states: "The PROJ-020 project lead (or delegated `/user-experience` skill lead) is responsible for evaluating wave transition readiness criteria and formally approving wave transitions. The evaluator reviews the verification method column for the current transition, confirms all criteria are met, and records the transition approval in the worktracker as a completed Task. No wave transition may proceed without explicit evaluator sign-off."

**Analysis:**
The wave transition evaluator role is defined but the assignment mechanism is not. The rule says "PROJ-020 project lead (or delegated skill lead)" — the parenthetical creates ambiguity about who holds the role at any given moment. If the project lead delegates to the skill lead, when does that delegation happen? By what mechanism? The analysis requires evaluator sign-off for every wave transition but provides no worktracker entity corresponding to the evaluator assignment. Unlike the AI-First Design Enabler (which has a mandatory Enabler entity, an Ownership Verification recurring task, and a succession protocol), the wave transition evaluator role has none of these. A project where the project lead is unavailable at Wave 1→Wave 2 transition has no documented path: does the transition proceed without sign-off? Does it block indefinitely? Is there a secondary evaluator?

**Recommendation:**
Add the wave transition evaluator role to the Section 7.5 Required Pre-Launch Worktracker Entities table as entity 5 (a recurring Task titled "Wave Transition Evaluator Designation" with the PROJ-020 project lead as owner, created at kickoff). Specify primary and secondary evaluator names in the kickoff sign-off document. Add a succession protocol matching the AI-First Design Enabler pattern (departure, role change, extended absence triggers).

**Acceptance Criteria:** Section 7.5 includes the wave transition evaluator designation as a required pre-launch entity with a named primary and secondary evaluator, matching the succession protocol pattern applied to the AI-First Design Enabler and MCP Maintenance Contract owner.

---

### PM-004-I6: LOW Gate Defense-in-Depth Mitigations Are Advisory Only [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.6 Synthesis Hypothesis Validation Protocol (LOW gate qualification) |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption failures) |

**Evidence:**
Section 7.6 (PM-007-I5 qualification) states: "The 'cannot be overridden' language describes design intent for the LLM sub-skill agent's behavioral constraints, not a technical enforcement guarantee. An LLM agent can be prompted to override behavioral instructions. The mitigation is defense-in-depth: (a) the agent definition's `<guardrails>` section contains the gate as a constitutional constraint, (b) the output labeling is applied before the user sees results, and (c) the gate verification in the Definition of Done (see Named tool/process below) confirms gates are correctly implemented. A determined user can circumvent any LLM-behavioral gate; the protocol's value is in making the default path safe, not in preventing all bypass."

**Analysis:**
The analysis correctly acknowledges the limitation but presents the three mitigations as if they are independently operational. Mitigation (a) depends on sub-skill implementation having correctly placed the constraint in `<guardrails>` — an assumption about future implementation quality. Mitigation (b) "the output labeling is applied before the user sees results" describes LLM behavior, which the previous sentence explicitly admits is not technically guaranteed. Mitigation (c) the Definition of Done verification depends on PM-002-I6's gap being resolved — if there is no file path for the reviewer to check, the verification cannot confirm the gate is correctly implemented. All three mitigations are circular: they depend on either future implementation correctness (unknowable) or on other mechanisms that themselves carry unresolved gaps. The net effect is that the LOW gate, which the protocol states "cannot be overridden," is in practice a soft suggestion that a motivated user or a poorly implemented agent will bypass without detection. A team making design decisions from LOW-confidence AI-First Design pattern recommendations six months post-launch, under time pressure, will discover that the gate did not prevent the outcome.

**Recommendation:**
Add one non-LLM-behavioral enforcement mechanism for the LOW gate: a post-generation scan step in the sub-skill workflow that checks output content for the `[LOW CONFIDENCE -- REFERENCE ONLY, NOT FOR DESIGN DECISIONS]` label. If the label is absent from output that the AI Execution Mode Taxonomy classifies as LOW confidence, the sub-skill logs a gate-violation event to a specified monitoring path (e.g., `work/.skill-gate-violations/`). This provides a deterministic audit trail independent of LLM behavioral compliance.

**Acceptance Criteria:** Section 7.6 specifies at least one enforcement mechanism for the LOW gate that does not depend on LLM behavioral compliance — specifically, a post-generation output check with a documented logging path for gate violations.

---

### PM-005-I6: Wave 5 Design Sprint Entry Criterion Has No Common Measurability Anchor [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.4 Wave Transition Criteria (Wave 5 entry, Design Sprint) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Section 7.4 states: "Wave 5 entry (Design Sprint): Team faces a major product direction decision OR is at initial product direction validation stage. At minimum one of: (a) a product decision affecting 3+ user-facing features has been deferred for > 1 sprint cycle, (b) the team has 2+ competing product direction hypotheses with no data to resolve between them, or (c) a stakeholder has formally requested a structured exploration of a named challenge [RT-003-I5 -- R10]."

The Verification Method column states: "Decision framing: team can articulate the sprint challenge in a single sentence AND point to the specific deferred decision, competing hypotheses, or stakeholder request that triggered the sprint."

**Analysis:**
R10 replaced the prior subjective "team faces major decision" test with three measurable alternatives (RT-003-I5). This is directionally correct. However, the three criteria are connected by "at minimum one of" with no common measurability threshold. Criterion (c) — "a stakeholder has formally requested a structured exploration of a named challenge" — is the most permissive: any stakeholder request for exploration, formal or not, qualifies. A product manager who sends a Slack message saying "we should probably do a design sprint on this" creates a nominally satisfying stakeholder request. The verification method requires only that the team "can articulate the sprint challenge" and "point to" the triggering event — not that the triggering event meets a quality bar. In six months of operation, a team using criterion (c) to justify a Design Sprint every sprint cycle will satisfy the Wave 5 entry criterion for every sprint, defeating the gatekeeping purpose. The transition from Wave 4→Wave 5 is intended to be a one-time readiness gate for a significant undertaking, but criterion (c) makes it a pass-on-demand gate for any team that has a stakeholder.

**Recommendation:**
Add a qualifying threshold to criterion (c): "a stakeholder has formally requested a structured exploration of a named challenge AND the request is documented in a worktracker Story or Feature entity with acceptance criteria." This requires the stakeholder request to be substantive enough to document in the worktracker, filtering out informal mentions. Additionally, clarify that Wave 5 entry criteria gate individual sprint activations (each Design Sprint requires its own criterion-meeting event), not a permanent unlock.

**Acceptance Criteria:** Section 7.4 criterion (c) requires the stakeholder request to be documented in a worktracker entity with acceptance criteria; the section clarifies that Wave 5 entry criteria apply per sprint activation, not as a one-time readiness gate.

---

### PM-006-I6: Owner Assignment Rule Has No Escalation Path If Kickoff Is Not Held [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.5 Required Pre-Launch Worktracker Entities (owner assignment rule) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Section 7.5 states: "Owner fields MUST contain named individuals (not 'TBD') by the end of the kickoff meeting."

And: "Wave 1 is BLOCKED until all four entity rows have owner fields populated with specific names in the PROJ-020 `WORKTRACKER.md` manifest."

**Analysis:**
The rule correctly requires named owners by the end of the kickoff meeting. The gap is what happens if the kickoff meeting is never formally held — a common occurrence on lean teams where implementation begins informally. If an implementer starts Wave 1 work without a formal kickoff, the owner fields will be absent. The analysis states Wave 1 is BLOCKED under this condition, but provides no mechanism to trigger the kickoff. The chain of enforceability breaks at the very first step: before Wave 1 can be blocked, someone must know Wave 1 is attempting to start, and that someone must check Section 7.5. On a team where the implementer is also the project lead (common in tiny teams), there is no external observer to surface the violation.

**Recommendation:**
Add a pre-kickoff gate to Section 7.5: the PROJ-020 project must have a documented kickoff date in the `PLAN.md` before implementation begins. The `PLAN.md` kickoff date is the trigger for creating entities 1-4. If `PLAN.md` has no kickoff date when an implementer begins Wave 1, this is itself a blocking condition (document the blocking condition as entity 0 in the table, to be resolved before entities 1-4 can be created).

**Acceptance Criteria:** Section 7.5 specifies that the existence of a kickoff date in `PLAN.md` is the precondition for creating entities 1-4, and that absence of this date is itself a blocking condition with a documented resolution path (schedule the kickoff meeting, record the date).

---

### PM-007-I6: Day-30 Expiry Check Is the Sole Binding Trigger With No Automated Reminder [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.8 AI-First Design (expiry review protocol) |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption failures) |

**Evidence:**
Section 3.8 states: "The Jerry worktracker is filesystem-based with no automation engine monitoring DUE DATE fields. Therefore, the expiry trigger requires an explicit human review process, not an automatic state transition: (a) **Day-30 milestone task:** A worktracker task titled 'AI-First Design Enabler Day-30 Expiry Check' MUST be created at Enabler creation time with DUE DATE = Enabler DUE DATE (kickoff + 30 days). **Responsible role:** The Enabler's named primary owner is responsible for executing this check."

**Analysis:**
The analysis correctly identifies that the filesystem-based worktracker has no automation engine. It addresses this by placing the expiry trigger responsibility on the named primary owner. However, this creates a single point of failure: if the primary owner is unavailable on Day 30 (travel, illness, role change, departure), the entire expiry mechanism fails. The succession protocol addresses primary owner departure but requires the secondary owner to "assume primary responsibility immediately" — there is no trigger that tells the secondary owner that Day 30 is arriving. If the primary owner leaves the project on Day 25 without a formal handover, the secondary owner inherits the role but has no notification that the Day-30 task is due in five days. The filesystem worktracker has no way to surface this.

Furthermore, the Day-30 task is created as a child of the Enabler entity. If the Enabler is never created (per PM-001-I6's failure mode), the Day-30 task is also never created, and the expiry mechanism has no existence at all — exactly the failure scenario described in the preamble.

**Recommendation:**
Add a calendar or external notification step: at Enabler creation time, the responsible owner MUST create a calendar reminder (or equivalent time-bound external notification) for Day 30 that is shared with both primary and secondary owners. Document this as a required step in the entity creation checklist (entity 2 in Section 7.5). This does not require worktracker automation — it uses the external calendar already available to the team.

**Acceptance Criteria:** Section 7.5 entity 2 (Day-30 Expiry Check task) includes a sub-step: "At task creation time, create a shared calendar event on Day 30 visible to both primary and secondary owners." The kickoff sign-off document includes a field confirming this calendar event was created.

---

### PM-008-I6: Gate Implementation Definition-of-Done Has No Specified Artifact Path [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.6 Implementation Specification (Named tool/process) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Section 7.6 states: "a sub-skill MUST NOT be marked DONE in the worktracker until the reviewer confirms all three confidence gate templates (HIGH/MEDIUM/LOW) are present in the sub-skill agent definition's `<guardrails>` section."

No path for sub-skill agent definitions is specified anywhere in the document.

**Analysis:**
This is a lower-severity instance of PM-002-I6's structural gap. The gate verification is sound in design but lacks a concrete file path. This causes ambiguity at review time (where does the reviewer look?) and makes it impossible to automate the check via Grep or an `/adversary` S-007 run without first knowing the path. An implementer placing sub-skill definitions in a non-standard location creates an invisible bypass.

**Recommendation:**
Specify the canonical path for sub-skill agent definitions in Section 7.4 or 7.6: `skills/user-experience/agents/{sub-skill-slug}.md`.

**Acceptance Criteria:** At least one section of the document specifies the canonical directory path for sub-skill agent definition files.

---

### PM-009-I6: Wave Backward-Pass Protocol Has No Executor If Evaluator Role Is Vacant [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.4 Wave backward-pass revision protocol |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption failures) |

**Evidence:**
Section 7.4 states: "The wave transition evaluator reviews the contradiction resolution before the team resumes the later wave."

**Analysis:**
The wave backward-pass protocol correctly requires evaluator review of contradiction resolution. However, if PM-003-I6 (wave evaluator assignment gap) results in a vacant evaluator role, the backward-pass protocol loses its executor. This is a cascade failure: PM-003-I6 causes PM-009-I6. The severity is Minor because the backward-pass protocol is invoked less frequently than the wave transition approval (it only fires when a later-wave output contradicts an earlier anchor), but the gap is real.

**Recommendation:**
Specify in the backward-pass protocol that if the wave transition evaluator role is vacant, the PROJ-020 project lead assumes backward-pass review responsibility by default (making the evaluator succession transparent). This links the evaluator succession protocol (PM-003-I6 mitigation) to the backward-pass protocol.

**Acceptance Criteria:** Section 7.4 backward-pass protocol specifies the fallback executor if the wave transition evaluator role is vacant.

---

### PM-010-I6: Dual Succession Triggers With No Cross-Reference Between Them [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.3 MCP Maintenance Contract; Section 3.8 AI-First Design (Enabler ownership) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process failures) |

**Evidence:**
Section 7.3 states: "Succession triggers: (1) primary owner departure from the project, (2) primary owner role change removing UX skill responsibility, (3) primary owner extended absence (> 2 sprint cycles)."

Section 3.8 states: "succession triggers are (1) primary owner departure, (2) primary owner role change, (3) primary owner extended absence (> 2 sprint cycles)."

Both patterns are identical but tracked as separate worktracker recurring tasks (entity 3 and entity 4 in Section 7.5) with no cross-reference.

**Analysis:**
If a single individual holds both the AI-First Design Enabler primary owner role and the MCP maintenance contract owner role, their departure triggers two simultaneous succession events in two separate tracking mechanisms. Nothing in the document alerts the secondary owners or the project lead to this double-trigger. In a tiny team context, the same person holding both roles is probable (not edge-case). A project lead managing a single person's departure might action one succession and miss the other.

**Recommendation:**
Add a note to Section 7.5 entities 3 and 4: "If the AI-First Design Enabler primary owner and the MCP maintenance contract owner are the same individual, their departure triggers both succession events simultaneously. The PROJ-020 project lead MUST verify both entity ownership records are updated when any single succession event is triggered."

**Acceptance Criteria:** Section 7.5 contains a cross-reference note alerting the project lead to check both succession chains when any owner departure is identified.

---

## Recommendations

### P0 — Critical: MUST Mitigate Before Acceptance

**PM-001-I6:** Add a kickoff sign-off document (`projects/PROJ-020-feature-enhancements/kickoff-sign-off.md`) as the concrete blocking artifact for Wave 1. Wave 1 sprint items may not be added to the backlog until this document exists with all four entity rows populated with named owners. The sign-off document is the reviewable pre-condition, eliminating the self-policing gap.

*Acceptance Criteria:* Section 7.5 names the sign-off document path and states it is a pre-condition for scheduling Wave 1 sprint items.

**PM-002-I6:** Add the canonical sub-skill agent definition path (`skills/user-experience/agents/{sub-skill-slug}.md`) to Section 7.6. Specify that the Definition of Done gate fires against the file at this path. Create at least one stub agent definition file for `/ux-heuristic-eval` as part of the analysis deliverable to provide the reviewer a concrete artifact to verify.

*Acceptance Criteria:* Section 7.6 includes the canonical path and a cross-reference to an existing stub agent definition file.

### P1 — Important: SHOULD Mitigate

**PM-003-I6:** Add wave transition evaluator designation as entity 5 in Section 7.5 (a recurring Task with kickoff-assigned primary and secondary evaluators). Add succession protocol matching the AI-First Design Enabler pattern.

*Acceptance Criteria:* Section 7.5 lists entity 5 with named primary and secondary evaluator fields.

**PM-004-I6:** Add a post-generation output scan step for the LOW gate: if the `[LOW CONFIDENCE -- REFERENCE ONLY, NOT FOR DESIGN DECISIONS]` label is absent from output classified as LOW confidence in the AI Execution Mode Taxonomy, a gate-violation event is logged to `work/.skill-gate-violations/`. This provides a deterministic audit trail.

*Acceptance Criteria:* Section 7.6 LOW gate specification includes a non-LLM-behavioral enforcement mechanism with a documented logging path.

**PM-005-I6:** Add a qualifying threshold to criterion (c) of the Wave 5 Design Sprint entry criteria: the stakeholder request must be documented in a worktracker Story or Feature with acceptance criteria. Clarify that Wave 5 entry criteria apply per sprint activation, not as a permanent unlock.

*Acceptance Criteria:* Section 7.4 criterion (c) requires a documented worktracker entity; the section explicitly states the criteria apply per-activation.

**PM-006-I6:** Add to Section 7.5 that the existence of a kickoff date in `PLAN.md` is the precondition for creating entities 1-4. Document absence of this date as a blocking condition (entity 0).

*Acceptance Criteria:* Section 7.5 references `PLAN.md` kickoff date as the trigger for entity creation.

**PM-007-I6:** Add to Section 7.5 entity 2 a sub-step: "At task creation time, create a shared calendar event on Day 30 visible to both primary and secondary owners." Include a confirmation field in the kickoff sign-off document.

*Acceptance Criteria:* Entity 2 in Section 7.5 specifies the calendar event creation sub-step; kickoff sign-off document includes a confirmation field.

### P2 — Monitor: MAY Mitigate; Acknowledge Risk

**PM-008-I6:** Specify the canonical sub-skill agent definition path at least once in the document. Low-cost fix that resolves ambiguity for all gate checks.

**PM-009-I6:** Add a sentence to the backward-pass protocol specifying the project lead as the fallback executor when the evaluator role is vacant.

**PM-010-I6:** Add a cross-reference note to Section 7.5 alerting the project lead to check both succession chains when any owner departure occurs.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-003-I6, PM-006-I6, PM-009-I6, PM-010-I6: Wave transition evaluator, kickoff precondition, backward-pass fallback executor, and dual-succession cross-reference are missing from the document. The analysis defines a rich set of operational safeguards but has gaps in the ownership and assignment chains that support them. |
| Internal Consistency | 0.20 | Negative (minor) | PM-002-I6 creates an internal consistency issue: Section 7.6 mandates gate verification by a reviewer checking `<guardrails>` sections of agent definition files, while the document does not specify where those files will reside. The mandate and the verification mechanism are inconsistent because one requires knowledge the other does not provide. |
| Methodological Rigor | 0.20 | Negative (minor) | PM-004-I6, PM-007-I6: The LOW gate "defense-in-depth" mitigations are advisory rather than operational; the Day-30 Expiry Check has a single-owner dependency with no notification mechanism for the secondary owner. Both represent methodological gaps in the enforcement architecture. |
| Evidence Quality | 0.15 | Neutral | The analysis provides strong evidence citations throughout; Pre-Mortem findings are process/enforcement gaps, not evidence-quality deficiencies. No negative impact on this dimension from these findings. |
| Actionability | 0.15 | Negative | PM-001-I6, PM-002-I6, PM-005-I6: The three Critical and one Major finding in this dimension directly reduce the analysis's ability to drive safe, unambiguous implementation. The launch readiness gate is self-policing, the agent definition path is unspecified, and the Wave 5 Design Sprint criterion has a permissive bypass. These are the highest-impact findings for actionability. |
| Traceability | 0.10 | Neutral | All findings trace to specific sections and evidence from the deliverable. R10's changes are accurately described in the revision log. No traceability deficiencies identified. |

---

## Execution Statistics

- **Total Findings:** 10
- **Critical:** 2
- **Major:** 5
- **Minor:** 3
- **Protocol Steps Completed:** 6 of 6
