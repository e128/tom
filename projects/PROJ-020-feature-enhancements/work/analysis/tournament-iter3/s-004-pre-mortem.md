# Pre-Mortem Report: UX Framework Selection (Revision 7)

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 7)
**Criticality:** C4 (Tournament Iteration 3)
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004 strategy)
**H-16 Compliance:** S-003 Steelman applied in tournament-iter1 (`tournament-iter1/s-003-steelman.md`) and tournament-iter2 (`tournament-iter2/s-003-steelman.md`) -- confirmed prior to this execution.
**Failure Scenario:** It is September 2026. The `/user-experience` skill has been live for six months. Usage is near-zero. The AI-First Design sub-skill was never built. Three MCP integrations broke silently, producing partial or blank outputs with no user-visible error. Teams treated AI-generated synthesis hypotheses as validated design findings and suffered downstream product rework. The skill's designated MCP maintenance owner (PROJ-020 implementation lead) left the project; no succession plan existed, and the quarterly audit never ran. The 5-wave adoption plan stalled at Wave 3 because teams could not complete the Storybook bootstrap prerequisite without guidance. The selection analysis is technically sound but operationally inert.

---

## Summary

Pre-Mortem analysis against Revision 7 identifies **2 Critical, 5 Major, and 4 Minor** failure causes across all five category lenses. The deliverable is heavily documented and structurally robust, but harbors two fundamental operational gaps that can cause the selection to produce real-world harm rather than value: (1) the synthesis hypothesis / validated finding boundary is surfaced adequately in the analysis document but has no enforcement mechanism in the skill output layer, meaning non-specialist users will routinely act on unvalidated AI outputs as if they were confirmed findings; (2) the MCP maintenance ownership chain is a single point of failure with no succession path and no escalation trigger, which means MCP breakage after personnel change produces silent skill degradation. The overall risk posture is HIGH -- the selection analysis itself is defensible, but the operational scaffolding described in the document contains structural failure modes that can invalidate the portfolio's value even when the selection is correct. Recommendation: **REVISE** -- targeted mitigations for both Critical findings are required before the analysis can support implementation decisions at C4 confidence.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-20260303T3 | Synthesis hypotheses treated as validated findings by non-specialists at skill invocation time | Process | High | Critical | P0 | Actionability |
| PM-002-20260303T3 | MCP maintenance owner has no succession path; departure causes silent, undetected skill degradation | Resource | High | Critical | P0 | Completeness |
| PM-003-20260303T3 | 5-wave adoption plan has no explicit failure/blocked state handling; stall at Wave 3 blocks later waves with no recovery path | Process | High | Major | P1 | Actionability |
| PM-004-20260303T3 | AI-First Design Enabler due-date computation is contingent on a kickoff date that may not exist; blocking condition itself is underdefined | Assumption | Medium | Major | P1 | Internal Consistency |
| PM-005-20260303T3 | Sub-skill interoperability depends on users traversing multiple routing layers; no single-session "emergency triage" path for a team with a launched product and immediate UX crisis | Process | Medium | Major | P1 | Completeness |
| PM-006-20260303T3 | Figma dependency risk disclosure is in Section 1 (methodology), not repeated at the point of sub-skill definition -- non-specialists implementing sub-skills may miss it | Process | Medium | Major | P1 | Evidence Quality |
| PM-007-20260303T3 | The 30-respondent Kano threshold is presented as a fixed requirement but has no contingency for teams who will never reach 30 users (e.g., B2B enterprise with 10-15 reachable users) | Assumption | Medium | Major | P1 | Completeness |
| PM-008-20260303T3 | Zero-user fallback validation message compliance depends entirely on implementer discipline; the prohibition on "ready for implementation" phrasing has no machine-enforceable constraint | Process | Low | Minor | P2 | Methodological Rigor |
| PM-009-20260303T3 | The pre-registered C3 perturbation interpretation rule declares Service Blueprinting as a "mandatory" substitution for MCP-heavy teams, but does not specify how teams self-classify as MCP-heavy; the boundary is undefined | Assumption | Low | Minor | P2 | Internal Consistency |
| PM-010-20260303T3 | Ethics gap V2 roadmap assigns P1 priority to dark patterns and algorithmic bias but provides no timeline, owner, or trigger for V2 initiation | Process | Medium | Minor | P2 | Actionability |
| PM-011-20260303T3 | Revision history (14 Major + 2 Critical findings in Iteration 2) has grown to a length that makes it harder to locate current design intent vs. historical rationale -- cognitive load risk for implementers | Resource | Low | Minor | P2 | Methodological Rigor |

---

## Detailed Findings

### PM-001-20260303T3: Synthesis Hypotheses Treated as Validated Findings [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 1 (AI Execution Mode Taxonomy), Sections 3.1-3.10 (per-sub-skill tables) |
| **Strategy Step** | Step 3 -- Technical/Process failure lens |

**Failure Cause:** The AI Execution Mode Taxonomy distinguishes "Deterministic execution" from "Synthesis hypothesis" outputs and instructs that synthesis outputs "MUST be labeled as hypotheses" and "Human validation required." This is a design-layer constraint embedded in an analysis document. At skill invocation time -- when a non-specialist developer runs `/ux-jtbd` and receives a JTBD job statement synthesis from App Store reviews -- there is no described enforcement mechanism that prevents the output from being consumed as a validated finding. The analysis correctly identifies the risk (Section 1: "Treating synthesis hypothesis outputs as validated findings is the primary risk of over-reliance on AI augmentation") but the mitigation lives exclusively at the documentation layer, not the skill output layer.

**Evidence:** Section 1, AI Execution Mode Taxonomy: "Outputs MUST be labeled as hypotheses. Human validation required before informing design decisions." Section 3.6 (JTBD), AI Execution Mode Taxonomy: "Generate assumption map from team-provided product context -- Synthesis hypothesis -- AI synthesizes the assumption list from the product description and stated user hypotheses... Label as hypothesis; team reviews and adds assumptions that AI missed." These are behavioral directives in a planning document, not runtime constraints in a skill implementation specification. The deliverable does not specify what happens in the skill output when a non-specialist ignores the label.

**Analysis:** The failure mode is: (1) non-specialist receives an output labeled "[HYPOTHESIS -- requires validation]"; (2) they have no UX expertise and cannot distinguish a plausible synthesis hypothesis from a validated finding; (3) they proceed to use it for design decisions. The label is necessary but not sufficient. The analysis document should specify a minimum validation gate that the skill enforces before any synthesis hypothesis output can be marked "used" -- for example, the skill should require the user to acknowledge the hypothesis status by answering a specific validation question before producing a downstream artifact. Without this, the label is a liability disclaimer, not a protective mechanism.

**Recommendation:** Add a "Synthesis Hypothesis Validation Protocol" section to the deliverable specifying the minimum acknowledgment gate the skill MUST implement before a synthesis hypothesis output can advance to a design decision. The gate should require: (a) the user explicitly answers the skill's validation prompt (not just reads it); (b) for HIGH and MEDIUM confidence hypotheses, the skill logs the validation source; (c) LOW confidence outputs are blocked from advancing without explicit override plus reason-for-override documentation. This is a skill specification requirement, not a documentation addition.

**Acceptance Criteria:** The deliverable includes a machine-enforceable validation protocol specification (not a behavioral recommendation) for synthesis hypothesis outputs, covering all three confidence levels (HIGH/MEDIUM/LOW) with distinct gate behaviors.

---

### PM-002-20260303T3: MCP Maintenance Owner Has No Succession Path [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.3 (MCP Maintenance Contract) |
| **Strategy Step** | Step 3 -- Resource failure lens |

**Failure Cause:** Section 7.3 identifies the MCP maintenance owner as "the PROJ-020 implementation lead (default)" and adds "If a dedicated UX skill maintainer is assigned during PROJ-020 implementation, that person becomes the owner." There is no succession trigger, no documented handover procedure, no escalation path if the owner leaves, and no secondary owner. The quarterly MCP audit cadence requires a human to execute it; if the owner leaves and no succession plan exists, the audit stops and the skill silently degrades as community MCP servers go stale.

**Evidence:** Section 7.3: "The `/user-experience` skill's MCP dependency health owner is: the PROJ-020 implementation lead (default). If a dedicated UX skill maintainer is assigned during PROJ-020 implementation, that person becomes the owner... Owner is responsible for: (a) executing the quarterly audit cadence, (b) updating sub-skill definitions when MCP servers change status, (c) testing MCP integrations before each PROJ-020 release, (d) escalating breaking changes to the PROJ-020 project lead." No mention of what happens if the owner is unavailable, leaves, or is not replaced. Community MCP production readiness caveat (Section 1, FM-002): "Before implementing any sub-skill that relies on a community MCP server, verify: (a) the GitHub repository URL and last commit date (must be within 6 months of implementation)..." This verification is described as a one-time implementation check, not a recurring owner-executed audit.

**Analysis:** The PROJ-020 implementation lead is a role with a natural project lifecycle -- they are most active during implementation and may be unavailable or reassigned post-launch. The failure mode: implementation lead leaves six months after launch; no successor is named; quarterly audit for Q3 2026 is not executed; Whimsical community MCP undergoes a breaking change in July 2026; `/ux-design-sprint` skills silently produce incomplete sprint maps with no error; teams discover the failure only when sprint artifacts are missing key sections. This is a single-owner dependency on a long-running operational responsibility.

**Recommendation:** Add a "Maintenance Owner Succession Protocol" to Section 7.3 specifying: (a) a named secondary owner at implementation kickoff; (b) a succession trigger (owner departure, 30-day unresponsive period, or project lead escalation); (c) a skills ownership transfer procedure that results in a worktracker task being created; (d) the quarterly audit must be tracked as a recurring worktracker task, not a human-remembered responsibility. The MCP maintenance contract should be treated as a live operational contract with a named owner chain, not a one-page spec section.

**Acceptance Criteria:** Section 7.3 specifies: (1) primary and secondary MCP maintenance owner; (2) succession trigger definition; (3) quarterly audit tracked as a recurring worktracker task with owner and deadline; (4) escalation path if audit is not completed within 7 days of the quarterly deadline.

---

### PM-003-20260303T3: 5-Wave Adoption Plan Has No Stall/Recovery Path [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.4 (Implementation Sequencing: 5-Wave Adoption Plan) |
| **Strategy Step** | Step 3 -- Process failure lens |

**Failure Cause:** The 5-wave adoption plan in Section 7.4 sequences sub-skills by dependency, MCP availability, and adoption curve. It does not define what happens when a wave stalls -- for example, when a team cannot complete the Storybook bootstrap prerequisite for Wave 3 (`/ux-atomic-design`). The plan's wave structure implies sequential completion, but offers no explicit recovery path if a team is blocked at an intermediate wave. A stalled Wave 3 blocks Wave 4 and Wave 5 sequentially, leaving teams with only Wave 1 and 2 sub-skills indefinitely.

**Evidence:** Section 7.4: "Wave 3 -- Design System Foundation: `/ux-atomic-design`, `/ux-inclusive-design` -- Prerequisites: Wave 1 complete; Storybook installation for Atomic; Figma subscription for Inclusive Design." No mention of what happens if Storybook installation fails, is blocked by team policy, or proves too complex for the team. "Wave 4 -- Advanced Analytics: Prerequisites: Wave 2 complete; launched product with behavioral data for Fogg; 30+ accessible users for Kano." No fallback if the team reaches Wave 4 timing but does not yet have 30 accessible users. The wording "Wave X complete" implies strict serialization.

**Analysis:** In practice, Tiny Teams have heterogeneous constraints. A team may be ready for Wave 4 analytically (they have behavioral data) but blocked at Wave 3 technically (Storybook is not installed). The current plan provides no lateral movement: a team blocked at Wave 3 technical prerequisites cannot skip to Wave 4 and return to Wave 3 later. This rigidity will produce abandonment of the adoption plan rather than adaptation.

**Recommendation:** Add a "Wave Bypass Protocol" subsection to Section 7.4 specifying: (a) explicit conditions under which a wave can be deferred while advancing to the next wave; (b) which sub-skills are strictly prerequisite-blocked vs. which can be adopted in any order; (c) a "minimum viable start" path for teams blocked at any wave (e.g., "if blocked at Wave 3, proceed to Wave 4 and return to Wave 3 when Storybook is available"). The plan should treat waves as priority guidance, not sequential gates.

**Acceptance Criteria:** Section 7.4 includes explicit bypass conditions and a minimum viable start path for each wave. At least Wave 3 and Wave 4 have documented lateral-movement options.

---

### PM-004-20260303T3: AI-First Design Enabler Due-Date Computation Is Contingent on an Undefined State [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.8 (AI-First Design -- Prerequisite Management) |
| **Strategy Step** | Step 3 -- Assumption failure lens |

**Failure Cause:** The Enabler due-date computation states: "The Enabler MUST have a DUE DATE field set to: PROJ-020 kickoff date + 30 calendar days, computed at Enabler creation time. If no kickoff date has been recorded in the worktracker at Enabler creation time, this is itself a blocking condition -- the Enabler cannot be marked 'in-progress' until a kickoff date is recorded." This creates a circular dependency: the Enabler cannot be marked in-progress until a kickoff date exists, but the kickoff date is presumably set at project start. If the project starts informally (common in Tiny Teams projects) with no formal kickoff record, the blocking condition activates immediately and the Enabler is permanently stuck in pre-in-progress state.

**Evidence:** Section 3.8: "Due date computation [PM-001-20260303b -- R7]: The Enabler MUST have a DUE DATE field set to: PROJ-020 kickoff date + 30 calendar days, computed at Enabler creation time. If no kickoff date has been recorded in the worktracker at Enabler creation time, this is itself a blocking condition -- the Enabler cannot be marked 'in-progress' until a kickoff date is recorded." The deliverable does not define: (a) who is responsible for recording the kickoff date; (b) what constitutes a "kickoff date" for an informal project start; (c) the maximum time the kickoff-blocking condition can persist before an escalation triggers.

**Analysis:** Tiny Teams (the explicit target audience) often start projects without formal kickoff ceremonies. The kickoff date blocking condition assumes a project management discipline that is precisely what Tiny Teams lack. An Enabler permanently stuck in blocked state because no kickoff date was recorded defeats the entire prerequisite management design. The auto-substitution trigger (Enabler expires without DONE -> Service Blueprinting replaces AI-First Design) also depends on the due date computation, which depends on the kickoff date. If no kickoff date exists, the substitution trigger cannot fire, and the state machine is stuck.

**Recommendation:** Add a fallback kickoff date definition: "If no formal kickoff date is recorded in the worktracker, the kickoff date defaults to the date of first commit to PROJ-020, the date the first worktracker entity was created, or the date of this document's creation (2026-03-02), whichever is earliest. The Enabler owner is responsible for recording the kickoff date within 5 business days of being assigned as owner."

**Acceptance Criteria:** Section 3.8 defines a fallback kickoff date rule that eliminates the blocking condition for projects without formal kickoff records, and specifies the owner's responsibility for recording it.

---

### PM-005-20260303T3: No Single-Session Emergency Triage Path for Crisis Teams [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.1 (Parent Skill Triage), Section 7.2 (Sub-Skill Routing Decision Guide) |
| **Strategy Step** | Step 3 -- Process failure lens |

**Failure Cause:** The parent skill triage and sub-skill routing guides are designed for deliberate adoption: teams who know their stage and are selecting a framework. The guides do not address the most common real-world entry point for a team discovering the `/user-experience` skill: "Our product is losing users and we need to diagnose and fix UX issues this week." A team in this position faces a multi-step triage: (a) identify stage, (b) answer MCP-heavy question, (c) navigate to the correct sub-skill, (d) potentially be told their chosen sub-skill requires 30 users they do not have, (e) be redirected again. The cognitive overhead of the routing system is itself a failure mode.

**Evidence:** Section 7.1 triage mechanism lists 9 options plus the MCP-heavy variant branch, producing at minimum a 2-step decision tree for any user. The "Triage existing product (RT-007 addition)" in Section 4 Complementarity Matrix provides the correct framework sequence (Nielsen's -> HEART -> Fogg -> Lean UX) but it is in Section 4, not in Section 7 where the routing guidance lives. Section 7.2 Sub-Skill Routing Decision Guide has 10 rows but no "I have an existing product with poor UX and need to triage it now" entry -- the closest is "Find usability problems in my existing design -> `/ux-heuristic-eval`" which is one piece of the multi-framework triage sequence.

**Analysis:** The "triage an existing product" use case is the highest-urgency entry point and is handled better in the coverage analysis (Section 4) than in the routing framework (Section 7). A team in crisis will look at the routing guide, find no single answer, and either abandon the skill or arbitrarily pick one sub-skill. The Section 4 triage sequence (Nielsen's -> HEART -> Fogg -> Lean UX) is the correct answer but is buried 700+ lines from the routing section.

**Recommendation:** Add a "Crisis Triage Protocol" entry to Section 7.1 and Section 7.2 with the explicit invocation path: "If your product is live and losing users / has a UX crisis: run `/ux-heuristic-eval` (immediate design diagnosis) THEN `/ux-heart-metrics` (identify which dimensions are failing) THEN `/ux-behavior-design` (diagnose specific behavior failures). This is the 3-skill crisis triage sequence." This mirrors the Section 4 triage matrix but makes it first-class in the routing guidance.

**Acceptance Criteria:** Section 7.1 includes a "crisis triage" routing entry. Section 7.2 includes a "My product is live and has poor UX" row with the 3-skill sequence.

---

### PM-006-20260303T3: Figma Dependency Risk Disclosure Is Absent at Implementation Points [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 (C3 criterion, Figma dependency risk [IN-002]), Sections 3.1, 3.2, 3.7, 3.8 |
| **Strategy Step** | Step 3 -- Process failure lens |

**Failure Cause:** The Figma dependency risk analysis in Section 1 (IN-002) documents that 6 of 10 selected frameworks depend on Figma MCP and that "if Figma changes its MCP server schema, restricts access, or monetizes the integration... these 6 frameworks lose their primary MCP integration path." This risk disclosure and the requirement to "document fallback workflows" for the 3 highest-Figma-dependent frameworks is stated once in the methodology section. At the individual sub-skill sections (3.1 Nielsen's, 3.2 Design Sprint, 3.8 AI-First Design), the Figma dependency is listed in "Required MCP integrations" but the risk and fallback requirement are not repeated.

**Evidence:** Section 1, IN-002: "The 3 highest Figma-dependent frameworks (Atomic Design C3=10, Design Sprint C3=8, AI-First Design C3=8) must document explicit non-Figma fallback paths in their skill definitions before launch." Section 3.2 (Design Sprint): "Required MCP integrations: Figma (official MCP)" -- no fallback path documented in this section. Section 3.3 (Atomic Design): "Required MCP integrations: Storybook (official MCP) -- Primary... Figma (official MCP) -- Design token extraction." The Storybook-as-primary statement provides an implicit fallback, but it is not framed as a Figma fallback path and does not address all Figma-dependent operations. Section 3.8 (AI-First Design): "Required MCP integrations: Figma (official MCP)" -- no fallback documented.

**Analysis:** A reader implementing `/ux-design-sprint` will read Section 3.2, see Figma as a required integration, and implement accordingly. They will not cross-reference Section 1's IN-002 analysis unless they have read the entire document in sequence. The IN-002 requirement ("must document explicit non-Figma fallback paths in their skill definitions before launch") is a post-analysis requirement that applies to the skill implementation, not to this document -- but the document is the specification that drives implementation, and it does not yet contain those fallback paths.

**Recommendation:** Add explicit non-Figma fallback paths to Sections 3.2 (Design Sprint), 3.3 (Atomic Design), and 3.8 (AI-First Design) as required by IN-002. For Design Sprint: "If Figma MCP is unavailable, Day 3 prototype generation falls back to Miro MCP wireframing mode." For Atomic Design: already partially addressed via Storybook primary; document explicitly. For AI-First Design: identify a Storybook-based fallback for AI component documentation.

**Acceptance Criteria:** All three IN-002-flagged sub-skill sections include an explicit "Non-Figma Fallback" subsection within Required MCP Integrations.

---

### PM-007-20260303T3: Kano 30-Respondent Threshold Has No B2B Enterprise Contingency [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.9 (Kano Model -- Implementation Tiers) |
| **Strategy Step** | Step 3 -- Assumption failure lens |

**Failure Cause:** The Kano Model implementation tiers (Section 3.9) define Mode 1 (0-4 users: route to JTBD), Mode 2 (5-29 users: qualitative approximation), and Mode 3 (30+ users: full quantitative Kano). The document states: "The 30-respondent threshold is achievable for virtually any post-launch product with modest usage." This assumption fails for B2B enterprise software teams, which are explicitly within scope (the SCOPE BOUNDARY notice targets "teams of 2-5 people" without restricting to consumer products). A B2B enterprise team may have 10-15 reachable internal users or 8-12 enterprise customers, and this population is permanent -- they will never reach 30 respondents for a feature survey.

**Evidence:** Section 3.9: "Mode 3 -- Post-launch, 30+ reachable users: Full quantitative Kano Model. The 30-respondent threshold is achievable for virtually any post-launch product with modest usage." Section 3.9, Mode 2: "Use qualitative Kano approximation -- conduct 5-8 structured interviews using Kano's functional/dysfunctional question pairs to identify Basic vs. Excitement features directionally. Label results as 'qualitative Kano approximation.'" Mode 2 is the correct path for B2B teams, but the deliverable's framing implies Mode 2 is a temporary stopgap ("Post-launch, small population") rather than a permanent operating mode for certain team types. The SCOPE BOUNDARY notice (document preamble) confirms the 2-5 person scope without consumer-vs-B2B restriction.

**Analysis:** B2B enterprise teams building internal tools or enterprise SaaS with small customer counts will permanently operate in Mode 2. The deliverable should acknowledge this as a permanent operating mode rather than a temporary state, and should provide enriched guidance for teams who will never reach 30 respondents (e.g., ways to increase confidence in Mode 2 qualitative approximations, or an expert interview substitute for the survey mechanism).

**Recommendation:** Add a "Mode 2 Permanent Operating Protocol" to Section 3.9 for teams with permanently small user populations (B2B, internal tools, niche products). Include: (a) enriched guidance for qualitative Kano with 5-8 users; (b) cross-validation path using JTBD job dimensions to triangulate Kano classifications; (c) explicit statement that Mode 2 is a valid permanent operating mode, not a temporary stopgap. Remove the claim that "30-respondent threshold is achievable for virtually any post-launch product" or qualify it with "for consumer-facing products."

**Acceptance Criteria:** Section 3.9 explicitly addresses B2B enterprise teams with permanently small user populations and provides a Mode 2 Permanent Protocol with cross-validation guidance.

---

### PM-008-20260303T3: Zero-User Fallback Prohibition Relies on Implementer Discipline [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 3.2 (Design Sprint -- Zero-User Fallback) |
| **Strategy Step** | Step 3 -- Process failure lens |

**Failure Cause:** Section 3.2 states: "The phrase 'ready for implementation' does not appear in this message and MUST NOT be reinstated in any revision." This is a governance constraint on the analysis document itself, not on the skill implementation. When the skill is actually implemented, the implementer will write the skill output template, and the prohibition on "ready for implementation" language is not carried forward as a machine-enforceable constraint -- it requires the implementer to remember and apply this prohibition.

**Evidence:** Section 3.2: "The skill surfaces the following message. Validation status MUST lead; implementation readiness MUST trail. A user reading only the first sentence must receive a warning, not a permission... The phrase 'ready for implementation' does not appear in this message and MUST NOT be reinstated in any revision." This prohibition applies to this document's revision history, but does not specify how to prevent reinstatement in the actual skill output template.

**Recommendation:** Add a specification that the skill output template for the zero-user fallback scenario must be provided as a literal string in the sub-skill definition file, not generated dynamically by the agent. This makes the prohibition on "ready for implementation" language structural: the template is a fixed string that implementers copy, not compose.

**Acceptance Criteria:** Section 3.2 specifies that the zero-user fallback message is a literal template string to be included verbatim in the skill definition, with a note that the string must be tested before launch by displaying it to a non-specialist and confirming the first sentence conveys a warning.

---

### PM-009-20260303T3: MCP-Heavy Team Self-Classification Boundary Is Undefined [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.1 (MCP-Heavy Team Variant Portfolio), Section 1 (C3 Perturbation Interpretation Rule) |
| **Strategy Step** | Step 3 -- Assumption failure lens |

**Failure Cause:** The pre-registered interpretation rule (Section 1) and the routing variant (Section 7.1) both condition on a team being "MCP-heavy." The routing mechanism asks: "Is your team primarily working in Figma and/or Miro as your core design toolchain AND do you consider MCP tool integration a primary driver of framework value for you?" The second condition ("consider MCP tool integration a primary driver") is entirely subjective -- a non-specialist may not know whether MCP integration is a "primary driver" of value for them. The question could produce inconsistent self-classification.

**Evidence:** Section 7.1: "If YES → apply the C3=25% alternative portfolio... Replace `/ux-kano-model` with `/ux-service-blueprinting`." The C3=25% interpretation rule requires "mandatory substitution" for MCP-heavy teams. If a team incorrectly classifies as MCP-heavy (or non-heavy), they receive an incorrect portfolio recommendation with mandatory-substitution language.

**Recommendation:** Replace the subjective "primary driver" question with an objective heuristic: "Do you use Figma and/or Miro for at least 50% of your design work AND do you intend to use MCP-automated workflows for design tasks (not just storing outputs)?" This provides a behavioral test rather than a value judgment. Alternatively, list 3 concrete examples of what "MCP-heavy" means operationally.

**Acceptance Criteria:** Section 7.1 replaces the subjective MCP-heavy classification question with an objective behavioral test or concrete examples.

---

### PM-010-20260303T3: Ethics V2 Roadmap Has No Initiation Trigger [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 4 (Ethics Gap V2 Prioritization) |
| **Strategy Step** | Step 3 -- Process failure lens |

**Failure Cause:** The ethics gap V2 roadmap identifies P1 items (dark patterns audit, algorithmic bias review) as highest priority V2 additions but provides no initiation trigger, timeline, owner, or escalation path. "V2 sequencing guidance" states "Begin with P1 items as a single V2 sprint" without specifying what triggers V2 initiation or who is responsible for initiating it.

**Evidence:** Section 4: "V2 sequencing guidance: Begin with P1 items (user research tool + Service Blueprinting + dark patterns + algorithmic bias) as a single V2 sprint. P2 items... are a second V2 sprint." No owner, no trigger, no timeline. The document was created 2026-03-02; there is no stated V2 start date or condition.

**Recommendation:** Add a V2 initiation trigger to the ethics gap section: "V2 scope is initiated when any of the following conditions is met: (a) V1 has been in production for 90 days; (b) any Tiny Team using V1 sub-skills reports a dark patterns or algorithmic bias incident; (c) the PROJ-020 project lead formally requests V2 scoping." Assign a named owner for V2 scoping.

**Acceptance Criteria:** Section 4 V2 roadmap includes at least one concrete initiation trigger and a named or role-based owner for V2 initiation.

---

### PM-011-20260303T3: Revision History Cognitive Load Risk for Implementers [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Revision History (end of document) |
| **Strategy Step** | Step 3 -- Resource failure lens |

**Failure Cause:** The Revision History section now spans Revision 4 through Revision 7, documenting 7 Critical, 40+ Major, and several Minor findings with per-finding attribution. The total revision history is longer than several of the sub-skill sections it documents changes to. An implementer reading the document to understand the current design intent must parse historical context to determine which portions of the document body represent current design decisions vs. prior-revision responses.

**Evidence:** Revision 7 change log alone documents 16 finding-level changes (DA-011-20260303b, PM-001-20260303b, PM-002-20260303b, IN-002-20260303iter2, RT-002-ITER2, RT-005-ITER2, RT-007-ITER2, IN-001-20260303iter2, SR-001-20260303B through SR-004-20260303B, DA-012b, SM-011/DA-013b, SM-015, FM-001-20260303I2, DA-014, DA-015, CC-001-20260303-I2). Revision 4 change log is similarly dense.

**Analysis:** The revision history is a correct and valuable audit trail. The minor risk is that new implementers may read change descriptions and assume the change log is the design intent, rather than reading the updated body. This is a document ergonomics issue, not a correctness issue.

**Recommendation:** Add a one-line notice at the top of the Revision History section: "Implementation decisions are in Sections 1-7. This section is the change audit trail and should not be used as the primary source of design intent." This is a cosmetic addition with no content change.

**Acceptance Criteria:** Revision History section includes an "implementation vs. audit trail" disambiguation notice.

---

## Recommendations

### P0 -- Critical (MUST Mitigate Before Acceptance)

**PM-001-20260303T3 -- Synthesis Hypothesis Validation Protocol**
- **Action:** Add a "Synthesis Hypothesis Validation Protocol" section specifying machine-enforceable (not behavioral) gate requirements for synthesis hypothesis outputs at skill invocation time. Cover all three confidence levels with distinct gate behaviors.
- **Target section:** Section 1 (AI Execution Mode Taxonomy) or new Section 7.5
- **Acceptance Criteria:** Protocol specification is present, covers HIGH/MEDIUM/LOW confidence levels, specifies a required user acknowledgment action (not just a label), and applies to all sub-skills.

**PM-002-20260303T3 -- MCP Maintenance Owner Succession Protocol**
- **Action:** Revise Section 7.3 to add: (1) named primary and secondary MCP maintenance owner; (2) succession trigger definition (departure, 30-day unresponsive, escalation); (3) quarterly audit tracked as recurring worktracker task with owner and deadline; (4) escalation path for missed audits.
- **Target section:** Section 7.3 (MCP Maintenance Contract)
- **Acceptance Criteria:** Section 7.3 includes succession protocol with two named owners, a formal trigger, and a worktracker task specification for the quarterly audit.

### P1 -- Important (SHOULD Mitigate)

**PM-003-20260303T3 -- Wave Bypass Protocol for Adoption Plan**
- **Action:** Add a Wave Bypass Protocol subsection to Section 7.4 specifying bypass conditions and minimum viable start paths for each wave. Reframe waves as priority guidance, not strict gates.
- **Target section:** Section 7.4, new subsection "Wave Bypass Protocol"
- **Acceptance Criteria:** Explicit bypass conditions for Wave 3 and Wave 4 blockages; minimum viable start path documented.

**PM-004-20260303T3 -- AI-First Design Enabler Kickoff Date Fallback**
- **Action:** Add a fallback kickoff date definition to Section 3.8 eliminating the circular blocking condition for projects without formal kickoff records.
- **Target section:** Section 3.8, Enabler entity specification
- **Acceptance Criteria:** Fallback definition covers the case where no formal kickoff date is recorded; owner responsibility for recording is specified.

**PM-005-20260303T3 -- Crisis Triage Protocol in Routing Sections**
- **Action:** Add a "Crisis Triage Protocol" entry to Section 7.1 and Section 7.2 with the explicit 3-skill sequence (Nielsen's -> HEART -> Fogg) for teams with an existing product and immediate UX problems.
- **Target section:** Section 7.1 (parent skill triage) and Section 7.2 (sub-skill routing)
- **Acceptance Criteria:** Both routing sections include a "crisis / existing product losing users" entry with the named 3-skill sequence.

**PM-006-20260303T3 -- Figma Fallback Paths at Sub-Skill Level**
- **Action:** Add non-Figma fallback subsections to Sections 3.2 (Design Sprint), 3.3 (Atomic Design), and 3.8 (AI-First Design) as required by IN-002.
- **Target section:** Sections 3.2, 3.3, 3.8
- **Acceptance Criteria:** All three sections include explicit Non-Figma Fallback subsections.

**PM-007-20260303T3 -- Kano Mode 2 Permanent Operating Protocol**
- **Action:** Add Mode 2 Permanent Operating Protocol to Section 3.9 for B2B and enterprise teams. Remove or qualify the "achievable for virtually any post-launch product" claim.
- **Target section:** Section 3.9 (Kano Model -- Implementation Tiers)
- **Acceptance Criteria:** B2B permanent-small-population scenario is explicitly addressed with cross-validation guidance.

### P2 -- Monitor (MAY Mitigate)

**PM-008-20260303T3** -- Zero-user fallback: specify literal template string in sub-skill definition. Monitor for implementer deviation at skill build time.

**PM-009-20260303T3** -- MCP-heavy classification: replace subjective "primary driver" question with objective behavioral test. Low urgency but should be resolved before skill SKILL.md authoring.

**PM-010-20260303T3** -- Ethics V2 roadmap: add initiation trigger and named owner. Can be deferred to V2 scoping kickoff but should be specified before V1 launches to prevent indefinite deferral.

**PM-011-20260303T3** -- Revision history: add one-line disambiguation notice. Cosmetic; address in next editorial pass.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale (PM Finding References) |
|-----------|--------|--------|-----------------------------------|
| Completeness | 0.20 | Negative | PM-002 (MCP maintenance succession gap), PM-003 (adoption plan has no stall recovery), PM-005 (crisis triage path absent from routing), PM-007 (Kano B2B scenario underdefined). Four Major findings expose coverage gaps in the operational scaffolding -- the analysis is structurally complete but operationally incomplete. |
| Internal Consistency | 0.20 | Negative | PM-004 (Enabler kickoff date computation creates circular blocking condition inconsistent with Tiny Teams operating reality), PM-009 (MCP-heavy self-classification question produces inconsistent results). Two findings reveal internal contradictions: the enforcement machinery conflicts with the stated target audience's operating patterns. |
| Methodological Rigor | 0.20 | Neutral | The WSM scoring, sensitivity analysis, and pre-registered interpretation rules are methodologically rigorous and well-documented. PM-008 and PM-011 are minor rigor observations that do not materially affect the selection methodology. No Critical or Major findings touch the core WSM methodology. |
| Evidence Quality | 0.15 | Negative | PM-006 (IN-002 Figma risk disclosure is present in methodology but not implemented at sub-skill specification level -- evidence of identified risk without corresponding mitigation artifact). The evidence quality is high for the selection analysis itself; the gap is between evidence of risk and evidence of mitigation. |
| Actionability | 0.15 | Negative | PM-001 (synthesis hypothesis validation protocol is a behavioral recommendation, not an enforceable specification -- non-specialists cannot act on a documentation label), PM-003 (5-wave adoption plan has no recovery path), PM-005 (routing sections do not surface the crisis triage sequence). Three Major/Critical findings directly impair actionability for the primary target audience (non-specialists). |
| Traceability | 0.10 | Positive | Finding IDs, revision history, and cross-references are thorough. All Pre-Mortem findings trace to specific sections and line-level evidence. The deliverable's internal traceability is a genuine strength that survived across all three iterations. |

**Overall Assessment:** REVISE -- targeted mitigation required. The 2 Critical findings (PM-001, PM-002) represent structural gaps in the operational specification layer that can produce real-world harm when non-specialists use the skill or when maintenance ownership lapses. The 5 Major findings (PM-003 through PM-007) represent completeness and consistency gaps that will reduce adoption effectiveness. No findings invalidate the selection methodology or the top-10 framework choices themselves -- the WSM analysis, sensitivity testing, and portfolio composition remain sound. Mitigation of P0 and P1 findings is estimated to produce a +0.08 to +0.12 composite score improvement, bringing the deliverable within range of the 0.95 target.

---

## Execution Statistics

- **Total Findings:** 11
- **Critical:** 2
- **Major:** 5
- **Minor:** 4
- **Protocol Steps Completed:** 6 of 6 (Steps 1-6 fully executed; Step 7 = persistence of this report)
