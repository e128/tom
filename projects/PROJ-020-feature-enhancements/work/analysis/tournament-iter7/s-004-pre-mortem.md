# Pre-Mortem Report: UX Framework Selection Analysis

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004 Pre-Mortem, Tournament Iteration 7)
**H-16 Compliance:** S-003 Steelman applied (tournament-iter6/s-003-steelman.md confirmed)
**Failure Scenario:** It is September 2026. The `/user-experience` skill was launched and adopted by 12 teams. Three months in, the skill is widely regarded as theoretically sophisticated but operationally untrustworthy. The AI-First Design Synthesis Enabler expired without a qualified reviewer completing the scoring artifact. Multiple sub-skills produce synthesis hypothesis outputs that teams have been treating as validated findings, leading to two major product decisions made on unvalidated assumptions. The parent skill's routing triage is producing inconsistent results because the `KICKOFF-SIGNOFF.md` artifact was never created, and no named owner was assigned at kickoff. The implementation team is paralyzed: they cannot determine which wave they are in, who is responsible for MCP maintenance, or whether the AI-First Design substitution was properly executed. The `/user-experience` skill is placed on hold pending governance remediation.

---

## Step 1: Stage Setting

**Deliverable goals (what success looks like):**
1. A 10-framework portfolio that serves as the operational foundation for the Jerry `/user-experience` skill
2. Clear, actionable guidance for a named owner to execute implementation through 5 waves
3. Governance controls (Enabler, KICKOFF-SIGNOFF, MCP maintenance contract) that function in production without a dedicated project manager
4. Sub-skill output quality gates that prevent synthesis hypothesis outputs from being treated as validated findings
5. An implementation sequencing plan that works for teams of 1-5 people with varying UX capacity

**Failure definition:** The skill is built but fails in production because governance controls were not implemented, sub-skill outputs mislead non-specialists, or the AI-First Design prerequisite path was not managed correctly.

---

## Step 2: Temporal Perspective Shift

It is September 2026. The `/user-experience` skill has failed spectacularly. We are now investigating why.

---

## Step 3 and Step 4: Failure Causes Inventory

### Findings Summary

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-I7 | KICKOFF-SIGNOFF.md was never created; Wave 1 proceeded without blocking prerequisite | Process | High | Critical | P0 | Actionability |
| PM-002-I7 | AI-First Design Enabler's Day-30 expiry check was missed; sub-skill proceeded without synthesis deliverable | Process | High | Critical | P0 | Completeness |
| PM-003-I7 | Synthesis hypothesis validation gates (HIGH/MEDIUM/LOW) implemented without the structural output-template-omission for LOW confidence -- teams received design recommendations from LOW-confidence paths | Technical | Medium | Critical | P0 | Internal Consistency |
| PM-004-I7 | Wave transition evaluator role was not formally assigned at kickoff; wave transitions occurred without recorded approval | Process | High | Major | P1 | Actionability |
| PM-005-I7 | Cross-sub-skill synthesis registry (Section 7.6 V2 target) not flagged as a V1 gap to the parent skill; teams received contradictory synthesis outputs from `/ux-jtbd` and `/ux-lean-ux` with no contradiction detection | Assumption | High | Major | P1 | Internal Consistency |
| PM-006-I7 | The KICKOFF-SIGNOFF.md "no-project-lead fallback" path was ambiguous; the "individual who initiates the kickoff meeting" was disputed between two engineers | Process | Medium | Major | P1 | Actionability |
| PM-007-I7 | Backward-pass cost ceiling (max 2 per wave transition) was not tracked; one team accumulated 5 backward passes before project lead escalation, consuming 2 sprint cycles | Process | Medium | Major | P1 | Completeness |
| PM-008-I7 | MCP secondary owner succession was set up but the quarterly verification task was never executed; MCP primary owner changed roles and the Figma MCP schema broke silently for 6 weeks | Resource | Medium | Major | P1 | Actionability |
| PM-009-I7 | AI-First Design scoring artifact path `projects/{PROJ-ID}/work/analysis/ai-first-design-scoring.md` required substitution of `{PROJ-ID}` with an actual project identifier; the Wave 5 evaluator rejected the artifact because the path used the template variable literally | Technical | Medium | Major | P1 | Traceability |
| PM-010-I7 | The "part-time UX" segment guidance to focus on Wave 1-2 only was advisory language; teams with part-time UX proceeded to Wave 3-4 and produced incomplete Storybook audits causing false accessibility compliance claims | Assumption | Medium | Major | P1 | Completeness |
| PM-011-I7 | Section 7.6 MEDIUM gate self-attestation limitation was documented but no concrete mitigation was implemented in V1; teams confirmed MEDIUM outputs without actual validation, producing unvalidated decision anchors | Assumption | High | Major | P1 | Evidence Quality |
| PM-012-I7 | The parent skill's invocation protocol does not surface the HIGH RISK user research gap warning at runtime; teams using `/ux-jtbd` + `/ux-lean-ux` received MEDIUM confidence outputs without encountering the portfolio-level user research warning from the document preamble | Technical | High | Major | P1 | Completeness |
| PM-013-I7 | The V2 scoping trigger criteria (Section 4) require monitoring of invocation patterns; no monitoring infrastructure existed at launch, so the triggers could never fire even when conditions were met | External | Medium | Minor | P2 | Actionability |
| PM-014-I7 | The "free-tier team configuration note" (Section 7.4) correctly identified Wave 4-5 as Figma-dependent but did not provide a timeline estimate for when free-tier teams should expect to need the paid tools | Assumption | Low | Minor | P2 | Actionability |
| PM-015-I7 | The AI Reliability Tiers table for Nielsen's Heuristics (Section 3.1) listed 4 "High AI confidence" heuristics and 6 "Requires team input" heuristics but the parent skill routing did not communicate this split to users before they invoked `/ux-heuristic-eval` | Assumption | Low | Minor | P2 | Actionability |

---

## Step 5: Detailed Findings

### PM-001-I7: KICKOFF-SIGNOFF Artifact Never Created [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.5 Required Pre-Launch Worktracker Entities |
| **Strategy Step** | Step 3: Generate Failure Causes (Process lens) |

**Failure Cause:** The `KICKOFF-SIGNOFF.md` artifact was mandated as the blocking prerequisite for Wave 1 (Section 7.5: "Wave 1 is BLOCKED until (a) the KICKOFF-SIGNOFF.md artifact exists at the specified path..."). However, the enforcement mechanism is self-attestation by the implementer: "An implementer starting Wave 1 MUST confirm both conditions before proceeding." In practice, an implementer under timeline pressure skipped this check, Wave 1 proceeded without the artifact, and the governance controls (owner assignments, succession protocols) that depend on the artifact were never formally established.

**Evidence:** Section 7.5, Launch readiness gate: "Wave 1 is BLOCKED until (a) the KICKOFF-SIGNOFF.md artifact exists at the specified path with all owner fields populated, AND (b) all entity rows in the PROJ-020 WORKTRACKER.md manifest have owner fields populated with specific names matching the sign-off artifact. An implementer starting Wave 1 MUST confirm both conditions before proceeding." The enforcement mechanism is a behavioral constraint ("MUST confirm"), not a deterministic gate.

**Analysis:** A "MUST confirm" behavioral constraint is not equivalent to a hard block. The analysis acknowledges this limitation for the synthesis hypothesis gates (Section 7.6: "protocol-enforceable gates...not a technical enforcement guarantee"), but applies the same behavioral constraint to the highest-stakes governance artifact without acknowledging this gap. The 14-day and 30-day escalation deadlines also rely on the same self-initiation logic (Section 7.5 kickoff escalation path), creating a scenario where the kickoff never happens and no escalation is triggered because the initiator hasn't initiated yet. This is a bootstrapping problem: the very condition that requires the kickoff (PROJ-020 creation) is also the condition that starts the 14-day clock, but if no one is monitoring the clock, the escalation path cannot activate.

**Recommendation:** Add a deterministic gate to the Wave 1 entry criteria: the `/user-experience` skill's parent agent definition MUST include a startup check that queries the worktracker for `KICKOFF-SIGNOFF.md` existence before routing any sub-skill invocation. If the file does not exist, the parent skill MUST refuse to route and instead surface: "IMPLEMENTATION BLOCKED: KICKOFF-SIGNOFF.md not found at `projects/PROJ-020-feature-enhancements/KICKOFF-SIGNOFF.md`. This file must be created and signed before any sub-skill can be invoked." Additionally, add a specific instruction to the analysis document: "The 14-day escalation clock REQUIRES a designated watcher. Identify this person by name at PROJ-020 creation time and record them in WORKTRACKER.md."

**Acceptance Criteria:** Section 7.5 Launch readiness gate is amended to include: (a) name of the designated kickoff clock watcher recorded at PROJ-020 creation time in WORKTRACKER.md, and (b) a note that the parent skill's agent definition implements a startup check for KICKOFF-SIGNOFF.md before routing.

---

### PM-002-I7: AI-First Design Day-30 Expiry Check Missed [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.8 AI-First Design (Prerequisite Management) |
| **Strategy Step** | Step 3: Generate Failure Causes (Process lens) |

**Failure Cause:** The Day-30 expiry check (Entity #2 in the worktracker entity table) requires the "Enabler primary owner" to execute the check on the Day-30 task's due date. If the primary owner does not execute the check (due to competing priorities, absence, or oversight), the Enabler can silently slip past its due date with the substitution never executed. The secondary owner notification via "shared calendar event" is an advisory mechanism only -- the calendar event does not trigger an action.

**Evidence:** Section 3.8 (PM-002-I4): "Day-30 task: A worktracker task titled 'AI-First Design Enabler Day-30 Expiry Check' MUST be created at Enabler creation time with DUE DATE = Enabler DUE DATE (kickoff + 30 days). Responsible role: The Enabler's named primary owner is responsible for executing this check." Section 7.5 Entity #2 shows this as a one-time Task with owner = Enabler primary owner. The failure mode is that the primary owner's calendar event fires but no explicit completion confirmation is required in the worktracker for the check itself.

**Analysis:** The analysis correctly identifies that the Jerry worktracker has no automation engine (Section 3.8: "The Jerry worktracker is filesystem-based with no automation engine monitoring DUE DATE fields"). The mitigation is a human-executed check. However, the check completion itself has no verification mechanism -- a task can be left in IN_PROGRESS status indefinitely without any downstream consequence until someone queries the worktracker. The substitution trigger also requires the primary owner to manually execute three state transitions (mark Enabler as CANCELLED, activate Service Blueprinting story, mark `/ux-ai-first` as BLOCKED). In a scenario where the primary owner is on leave and the secondary owner was not trained on the substitution procedure, these transitions may not be executed correctly.

**Recommendation:** Add an explicit "expiry check completed" verification step to the pre-launch checklist: the Wave 5 transition evaluator MUST verify that Entity #2 (Day-30 expiry check Task) is in DONE status before approving Wave 5 entry for `/ux-ai-first`. This makes the Day-30 task completion a prerequisite for the wave transition, creating a downstream enforcement point that compensates for the absence of an automation engine. Additionally, add a step to the KICKOFF-SIGNOFF.md format: "Secondary owner has been walked through the Day-30 substitution procedure and confirmed understanding: [Yes/No]."

**Acceptance Criteria:** Section 3.8 and Section 7.4 (Wave 5 `/ux-ai-first` entry criteria) are amended to include: "Wave 5 transition evaluator confirms Entity #2 (Day-30 expiry check Task) status = DONE before approving `/ux-ai-first` entry."

---

### PM-003-I7: LOW Confidence Gate Structural Omission Not Implemented [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.6 Synthesis Hypothesis Validation Protocol |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical lens) |

**Failure Cause:** Section 7.6 specifies that the LOW confidence gate must use a structural output-template-omission approach: "the agent's `<methodology>` section terminates the response at the synthesis summary step, making it structurally impossible for the default output path to include design recommendations." This is a non-behavioral enforcement layer. However, the validation checklist in Section 7.6 does not include a test case that specifically verifies the structural omission (i.e., that the agent definition's response template for LOW confidence paths literally does not contain a design recommendation section). The validation checklist tests for label presence, not for structural absence.

**Evidence:** Section 7.6 validation checklist: "| LOW | Any user input | Output always labeled `[LOW CONFIDENCE]`; no design recommendation | Label always present; never produces recommendation |" -- this tests behavioral compliance (never produces recommendation) but not structural compliance (template does not contain recommendation block). The LOW gate enforcement qualification (FM-002-I6) acknowledges: "An LLM agent can be prompted to override behavioral instructions." The structural mitigation should be verifiable separately from behavioral compliance, but the validation checklist does not include this verification.

**Analysis:** A skilled user prompting the agent with "I understand the low confidence but please give me a design recommendation anyway" will receive a recommendation from an agent whose gate is implemented only behaviorally, even if that is against the agent's stated guardrails. The structural template omission is the only non-circumventable mitigation, but verifying it requires an implementation reviewer to inspect the agent definition's `<methodology>` response template structure, not just test the behavioral output. The current validation checklist does not include this structural inspection step.

**Recommendation:** Add a structural inspection step to the LOW gate validation checklist: "Structural: Inspect the sub-skill agent definition `<methodology>` section for LOW confidence response path. Verify the response template terminates at 'synthesis summary' with no design recommendation section visible in the template structure. Pass criteria: the response template for LOW paths contains no design recommendation block (not just a behavioral instruction to omit it)." This distinguishes structural enforcement from behavioral enforcement.

**Acceptance Criteria:** Section 7.6 validation checklist is amended with the structural inspection test case for LOW confidence paths, and sub-skill agent definitions are required to demonstrate this structural separation in their Definition of Done.

---

### PM-004-I7: Wave Transition Evaluator Not Formally Assigned [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.4 Wave Transition Criteria |
| **Strategy Step** | Step 3: Generate Failure Causes (Process lens) |

**Failure Cause:** Section 7.4 specifies that the wave transition evaluator is "named in the `KICKOFF-SIGNOFF.md` artifact." If the KICKOFF-SIGNOFF.md was not created (as in PM-001-I7), there is no named evaluator for any wave transition. Even when the KICKOFF-SIGNOFF.md exists, the delegation path (project lead -> skill lead -> senior-most engineer) relies on organizational continuity that may not exist in a small team where roles shift frequently. The wave transition Task schema (Section 7.4) requires the "Owner" field to contain the evaluator's name in `{First Name} {Last Name}` format, but this field cannot be populated without a named evaluator.

**Evidence:** Section 7.4: "The PROJ-020 project lead (or delegated `/user-experience` skill lead) is responsible for evaluating wave transition readiness criteria and formally approving wave transitions. Assignment mechanism [PM-003-I6 -- R11]: The wave transition evaluator is named in the KICKOFF-SIGNOFF.md artifact." The delegation chain "senior-most engineer with DONE stories" is a fallback that introduces ambiguity in small teams (what does "senior-most" mean in a 2-person team?).

**Analysis:** The wave transition evaluator role is a single point of accountability without a documented selection algorithm for the "senior-most engineer" fallback. In a 2-person team where both engineers have equivalent DONE stories, the fallback produces an ambiguous result. Clarifying the tie-breaking rule would prevent informal resolution that bypasses the transition documentation requirement.

**Recommendation:** Add a tie-breaking rule to the wave transition evaluator delegation chain: "In teams where seniority is equivalent (e.g., 2-person teams with equal standing), the team member who authored the MOST DONE stories in the current wave assumes evaluator responsibility for that transition only." This converts the ambiguous "senior-most" to a measurable criterion. Additionally, add an explicit note: "The wave transition evaluator role MUST be resolved before any wave transition approval task is created. If the evaluator cannot be determined from the delegation chain, escalate per H-31 before proceeding."

**Acceptance Criteria:** Section 7.4 wave transition evaluator assignment mechanism includes a tie-breaking rule for equivalent-seniority teams.

---

### PM-005-I7: Cross-Sub-Skill Synthesis Contradiction Not Surfaced at V1 Launch [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.6 Synthesis Hypothesis Validation Protocol |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption lens) |

**Failure Cause:** Section 7.6 identifies that the cross-sub-skill synthesis registry is a "V2 implementation target -- V1 relies on manual cross-referencing during wave transition evaluation." However, the wave transition evaluation process does not explicitly require a synthesis consistency check between sub-skills in the same wave. The wave transition Task schema (Section 7.4) requires Verification (checklist of readiness criteria) and Artifacts (evidence file paths), but neither includes cross-sub-skill synthesis consistency as a verification item.

**Evidence:** Section 7.6 (RT-004-I6): "When two or more sub-skills produce synthesis hypothesis outputs that reference the same user population or product context, the contradiction MUST be surfaced to the user before either output advances to design decisions. [...] V1 relies on manual cross-referencing during wave transition evaluation." Section 7.4 wave transition Task schema shows Verification field with "Checklist of readiness criteria with pass/fail per criterion" but the sample verification entry "Heuristic eval: PASS. JTBD job statement used: PASS." demonstrates that the verification is focused on artifact existence, not synthesis consistency.

**Analysis:** "Manual cross-referencing during wave transition evaluation" is not operationalized anywhere in the document. There is no instruction telling the wave transition evaluator what to cross-reference, how to identify contradictions, or what to do when a contradiction is found. This gap means the V1 manual process will not happen reliably, making the cross-sub-skill synthesis registry absence a real operational risk rather than an acknowledged V2 deferral.

**Recommendation:** Add a synthesis consistency check as a required step in the wave transition verification procedure: "Wave {N} to {N+1} transition: Evaluator reviews synthesis hypothesis outputs from all sub-skills activated in Wave N. For each pair of sub-skills targeting the same user population (identify from Section 3 sub-skill profiles), compare synthesis outputs for contradiction. Document any contradictions in the transition Task's Verification field. If a contradiction is found and not resolved, mark the transition as CONDITIONAL pending resolution." Add the cross-sub-skill pair list for Wave 1 (JTBD job statements vs. Lean UX assumption maps) as the minimum V1 manual check.

**Acceptance Criteria:** Section 7.4 wave transition Task schema includes a synthesis consistency check step referencing the cross-sub-skill pair list for each wave.

---

### PM-006-I7: No-Project-Lead Fallback Introduces Disputed Authority [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.5 Required Pre-Launch Worktracker Entities |
| **Strategy Step** | Step 3: Generate Failure Causes (Process lens) |

**Failure Cause:** Section 7.5 specifies: "If no PROJ-020 project lead has been formally assigned at the time kickoff is scheduled, the individual who initiates the kickoff meeting assumes project lead responsibilities." In teams where multiple people could legitimately initiate the kickoff (e.g., two senior engineers both send calendar invites, or the kickoff is initiated via async message in a team channel), the "who initiated" criterion is ambiguous and may produce a disputed assignment.

**Evidence:** Section 7.5 (FM-001-I6): "No-project-lead fallback: If no PROJ-020 project lead has been formally assigned at the time kickoff is scheduled, the individual who initiates the kickoff meeting assumes project lead responsibilities for the purposes of this owner assignment rule. This assignment MUST be documented in the KICKOFF-SIGNOFF.md artifact."

**Analysis:** "Individual who initiates the kickoff meeting" has three plausible interpretations: (1) who created the calendar event, (2) who first proposed having a kickoff in written communication, (3) who opens the meeting when it begins. In distributed teams, these may be different people. The dispute resolution path is not specified -- the document says "MUST be documented" but does not say who decides when disputed.

**Recommendation:** Clarify the tie-breaking definition: "The 'individual who initiates the kickoff' is operationally defined as: (a) the person who creates the calendar event if a formal meeting is held, OR (b) the person who sends the first written message explicitly proposing the kickoff if no calendar event is created. If disputed, the person with the earlier timestamp in the team's communication tool wins. If timestamps are equal or cannot be determined, the team MUST explicitly vote and record the result in WORKTRACKER.md before proceeding to the kickoff itself."

**Acceptance Criteria:** Section 7.5 no-project-lead fallback definition includes an operationalized tie-breaking rule.

---

### PM-007-I7: Backward-Pass Count Not Trackable Without a Named Tracking Artifact [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.4 Wave Backward-Pass Revision Protocol |
| **Strategy Step** | Step 3: Generate Failure Causes (Process lens) |

**Failure Cause:** Section 7.4 specifies a maximum of 2 backward passes per wave transition before mandatory escalation. However, backward passes are tracked as "worktracker impediment[s] linking the two affected sub-skill stories." The backward-pass count ceiling (2) is enforced by the backward-pass evaluator, but there is no specification of WHERE the backward-pass count is recorded -- the count is implicit in the impediment list, which requires manual counting by the evaluator. If impediments are closed without cross-referencing, the count may be understated.

**Evidence:** Section 7.4 (DA-004-I6): "A maximum of 2 backward passes per wave transition are permitted before mandatory escalation to the project lead for a scope decision. [...] Backward-pass evaluator: reviewed by the wave transition evaluator for the EARLIER wave." The wave transition Task schema (Section 7.4) does not include a "backward-pass count" field in its required fields list.

**Analysis:** The backward-pass count ceiling is sound governance, but counting backward passes from a list of impediment worktracker items that may be closed, renamed, or split is error-prone. A team could have 3 backward passes (one of which was closed as "resolved") and genuinely believe they have 2 outstanding, not recognizing that the closed impediment counted toward the ceiling.

**Recommendation:** Add a "Backward Pass Count" required field to the wave transition Task schema: "| Backward Pass Count | Number of backward passes recorded for this wave transition | `0` (if none), or the cumulative count of impediment-linked backward passes |". Specify that closed impediments count toward the ceiling. Add a note: "Once the backward-pass count reaches 2, any additional backward-pass request MUST be filed as an escalation to the project lead first, not as a new impediment."

**Acceptance Criteria:** Wave transition Task schema includes a Backward Pass Count field with counting instructions.

---

### PM-008-I7: MCP Maintenance Quarterly Tasks Not Self-Sustaining [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.3 MCP Maintenance Contract |
| **Strategy Step** | Step 3: Generate Failure Causes (Resource lens) |

**Failure Cause:** The quarterly MCP audit (Entity #4, MCP Ownership Verification) relies on the current MCP primary owner to execute the audit, verify both owners are "current and able to fulfill their responsibilities," and test MCP integrations. If the primary owner changes roles (a succession trigger), the secondary owner assumes responsibility -- but the secondary owner's first quarterly audit is the moment they discover the primary's absence. If the secondary owner does not know which MCP integrations to test or where the integration documentation is, the first secondary-ownership audit may be incomplete.

**Evidence:** Section 7.3: "A recurring worktracker task titled 'MCP Ownership Verification' MUST be created at PROJ-020 kickoff with quarterly recurrence to verify both primary and secondary owners are current and able to fulfill their responsibilities." The task does not specify a checklist of what to verify beyond owner currency. Section 7.3 lists the required MCP integration classifications (required vs. enhancement), but there is no procedure document linking the quarterly audit task to this classification table.

**Analysis:** A quarterly audit task without a linked execution procedure is likely to be completed performatively (marking the task DONE after a brief check) rather than substantively (testing each required MCP integration against the sub-skill's fallback path). The Figma MCP, which is a required integration for 6 sub-skills, has a documented history of schema changes (Dev Mode became paid in 2023; additional changes in 2024 per Section 1). A 6-week gap between a breaking change and discovery is plausible if the audit checklist is not specific.

**Recommendation:** Add a linked MCP audit procedure to the quarterly audit task specification: "The MCP Ownership Verification task MUST reference and execute the following MCP audit checklist: (a) Test Figma MCP connection for each sub-skill listed under Required MCPs = Figma in Section 7.3 classification table; (b) Verify Storybook MCP version compatibility for `/ux-atomic-design` and `/ux-inclusive-design`; (c) Check Miro MCP for `/ux-design-sprint` and `/ux-lean-ux`; (d) Document pass/fail for each integration in the task completion notes." Add this checklist as an appendix or linked artifact in Section 7.3.

**Acceptance Criteria:** Section 7.3 MCP audit procedure specifies a linked integration test checklist with pass/fail recording.

---

### PM-009-I7: AI-First Design Scoring Artifact Path Uses Literal Template Variable [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.4 Wave Transition Criteria (Wave 5 `/ux-ai-first` entry) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical lens) |

**Failure Cause:** The Wave 5 entry criteria for `/ux-ai-first` (Section 7.4) specify: "Independent scoring artifact exists at `projects/{PROJ-ID}/work/analysis/ai-first-design-scoring.md`." The `{PROJ-ID}` template variable will be used literally by implementers who copy the path from the document without substituting the actual project identifier. The wave transition evaluator checking for this artifact at the specified path will not find it because the file was created at the correct path (e.g., `projects/PROJ-020-feature-enhancements/work/analysis/ai-first-design-scoring.md`) while the specification path contains the literal `{PROJ-ID}`.

**Evidence:** Section 7.4 Wave 5 `/ux-ai-first` entry: "Worktracker Enabler entity status field = DONE. Independent scoring artifact exists at `projects/{PROJ-ID}/work/analysis/ai-first-design-scoring.md` [RT-001-I6 -- R11]." The document itself uses this template variable pattern in multiple places (e.g., Section 7.6: `projects/{PROJ-ID}/work/ux/{sub-skill-slug}/{output-artifact}.md`), establishing a pattern where `{PROJ-ID}` should be substituted -- but the explicit substitution instruction appears in the KICKOFF-SIGNOFF.md format specification, not at the point of use.

**Analysis:** This is a documentation gap: the template variable is defined implicitly by convention, not explicitly. In a document that will be executed by implementers who may not have read the entire document, a template variable in a critical verification path creates a predictable failure mode.

**Recommendation:** Replace `{PROJ-ID}` in the scoring artifact path with the actual project identifier: "Independent scoring artifact exists at `projects/PROJ-020-feature-enhancements/work/analysis/ai-first-design-scoring.md`." Add a note: "If this analysis is adapted for a different project, substitute the actual PROJ-ID. The path above reflects the canonical location for PROJ-020." Similarly, resolve all `{PROJ-ID}` template variables in Section 7.6 with the specific path `projects/PROJ-020-feature-enhancements/` where the document's context makes it unambiguous.

**Acceptance Criteria:** All `{PROJ-ID}` template variables in the Wave 5 entry criteria and Section 7.6 are replaced with the literal project path or accompanied by a substitution instruction at the point of use.

---

### PM-010-I7: Part-Time UX Segment Guidance Is Advisory Without Enforcement [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.1 The `/user-experience` Parent Skill |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption lens) |

**Failure Cause:** Section 7.1 specifies a UX capacity triage question: "How much time does your team dedicate to UX work per sprint?" and routes part-time UX teams to Wave 1-2 only. However, this triage is described as a parent skill behavior (advisory), not a hard block. A part-time UX team that answers honestly but then proceeds to Wave 3-4 by invoking sub-skills directly (bypassing the parent skill triage) will receive no enforcement. The parent skill triage is a first-invocation check -- it cannot be enforced at subsequent invocations without stateful memory of the previous triage result.

**Evidence:** Section 7.1 (DA-003-I6): "If the answer is less than 20% of a single person's time (the 'Part-Time UX' segment), the parent skill surfaces a warning: 'At part-time UX capacity, focus on Wave 1 sub-skills...' [...] See the wave adoption plan in Section 7.4 for sequencing guidance." This is a warning, not a block. Section 7.4 free-tier team configuration note: "Teams unable to meet the $46/month Figma+Miro baseline should prioritize Wave 1 and Wave 4 sub-skills..." -- also advisory.

**Analysis:** Advisory routing guidance for a high-risk population segment (part-time UX teams are the most likely to misinterpret synthesis hypothesis outputs as findings and the most likely to produce incomplete accessibility audits) creates a false assurance gap. The guidance correctly identifies the risk but the enforcement path is missing.

**Recommendation:** Add a wave transition criteria item specifically for part-time UX teams: "Part-time UX segments (< 20% of one person's sprint time) MUST document in the Wave 1 → Wave 2 transition Task: current UX capacity as a percentage. If capacity is still < 20%, the transition Task MUST include explicit acknowledgment: 'Team capacity remains at part-time UX level. Wave 3-5 adoption is deferred until capacity exceeds 20%.' Wave 3-5 wave transitions are BLOCKED for teams that have documented part-time UX capacity in a prior wave transition Task until capacity increases." This records the capacity status in the worktracker, creating a downstream enforcement point.

**Acceptance Criteria:** Wave 1 → Wave 2 transition criteria include a UX capacity field, and Wave 3-5 entry criteria reference the capacity record from prior transitions.

---

### PM-011-I7: MEDIUM Gate Self-Attestation Limitation Has No V1 Mitigation Beyond Documentation [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.6 Synthesis Hypothesis Validation Protocol |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption lens) |

**Failure Cause:** Section 7.6 acknowledges that HIGH and MEDIUM confidence gates rely on user self-attestation ("I have reviewed..." / "I have obtained expert review from..."), and notes: "A user clicking 'confirm' without reviewing degrades the gate to a notification mechanism rather than a quality control." The analysis lists three mitigations: (a) prompt text explicitly names what must be reviewed, (b) MEDIUM gate requires naming a specific validation source, (c) LOW gate cannot be overridden. Mitigation (b) creates an auditable claim for MEDIUM confidence. However, there is no process that actually audits those claims before decisions are made from the outputs.

**Evidence:** Section 7.6 (DA-006 -- R9): "Self-attestation limitation acknowledgment: The HIGH and MEDIUM confidence gates rely on user self-attestation. [...] Mitigation: (b) the MEDIUM gate requires naming a specific validation source, creating an auditable claim." Section 7.6 (FM-019-I6): "When a user provides validation attestation for a MEDIUM confidence synthesis, the sub-skill agent MUST append the attestation record to the sub-skill's output artifact." The attestation record exists, but who reviews it and when is not specified.

**Analysis:** An "auditable claim" is only useful if someone audits it. The analysis creates the audit trail (attestation records in `## Validation Attestations`) but does not specify a review step. The wave transition evaluator reviews wave transition Tasks and artifact existence, but is not explicitly required to check attestation records in sub-skill output artifacts.

**Recommendation:** Add attestation record review to the wave transition evaluation procedure: "Wave evaluator MUST spot-check at least 2 synthesis hypothesis output artifacts from the wave's sub-skills for attestation record completeness. For MEDIUM confidence outputs, verify: (1) attestation record exists in `## Validation Attestations` section, (2) validation source is named and plausible (not a generic label like 'team review'), (3) date is within the sprint cycle. Document the spot-check result in the wave transition Task Verification field." This converts the auditable claim into an actually-audited claim.

**Acceptance Criteria:** Wave transition Task verification procedure includes a MEDIUM gate attestation spot-check requirement.

---

### PM-012-I7: HIGH RISK User Research Gap Not Surfaced at Sub-Skill Runtime [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Document Preamble (HIGH RISK -- USER RESEARCH GAP notice) |
| **Strategy Step** | Step 3: Generate Failure Causes (Technical lens) |

**Failure Cause:** The HIGH RISK user research gap warning appears in the document preamble and in Section 4, but Section 7.1 explicitly acknowledges: "The sub-skill routing mechanism in Section 7.1 does NOT surface this limitation at invocation time; implementers MUST embed this warning in the parent `/user-experience` skill's onboarding text." The "implementers MUST embed this warning" instruction is a directive to an implementation team that may not read this analysis document carefully during implementation. If the warning is not embedded, users invoking JTBD or Lean UX will not encounter it.

**Evidence:** Section 7.1 HIGH RISK notice: "The sub-skill routing mechanism in Section 7.1 does NOT surface this limitation at invocation time; implementers MUST embed this warning in the parent `/user-experience` skill's onboarding text." This acknowledges the gap but does not close it -- the instruction to implement is not the implementation.

**Analysis:** A directive to implementers without a corresponding Definition of Done item is advisory. The Definition of Done for the parent skill should require verification that the user research gap warning is present in the skill's onboarding text. Without a DoD item, this can be omitted during implementation under time pressure.

**Recommendation:** Add an explicit item to the required pre-launch checklist (Section 7.5) or create a new Implementation Verification section: "Before any sub-skill is deployed: (1) Verify that the parent `/user-experience` skill's onboarding text includes the HIGH RISK user research gap warning verbatim from Section 7.1; (2) Test that invoking the parent skill for the first time surfaces the warning before routing to any sub-skill; (3) Record verification as a completed worktracker Task at `projects/PROJ-020-feature-enhancements/work/implementation/user-research-gap-warning-verification.md`."

**Acceptance Criteria:** Section 7.5 (or equivalent pre-launch checklist) includes a verification item for the user research gap warning's presence in parent skill onboarding text.

---

### PM-013-I7: V2 Scoping Trigger Criteria Cannot Fire Without Monitoring Infrastructure [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 4 Coverage Analysis (Consolidated V2 Roadmap) |
| **Strategy Step** | Step 3: Generate Failure Causes (External lens) |

**Failure Cause:** Section 4 V2 scoping trigger criteria require monitoring of invocation patterns (e.g., "the C3=25% MCP-heavy team variant portfolio is activated for >= 20% of `/user-experience` invocations in a month"). There is no monitoring infrastructure for tracking invocation statistics in the Jerry framework, and no plan to create one as part of PROJ-020.

**Evidence:** Section 4 V2 scoping trigger criteria table: "The C3=25% MCP-heavy team variant portfolio is activated for >= 20% of `/user-experience` invocations in a month." The Jerry framework is a file-based system with no invocation telemetry.

**Analysis:** The trigger criteria are designed around telemetry that does not exist and is not planned. This means V2 scoping will effectively be triggered by the qualitative triggers only (specific team reports of problems), not by the quantitative ones. This is acceptable but should be acknowledged, and the quantitative triggers should either be removed or accompanied by a lightweight manual tracking mechanism.

**Recommendation:** Amend the V2 scoping trigger criteria to distinguish between manual (self-reported) and telemetry-based triggers: "Manual tracking triggers (actionable now): [list the qualitative triggers]. Telemetry triggers (deferred until monitoring infrastructure exists): [list the quantitative triggers with note: 'These triggers require invocation logging not available in V1. Activate V2 scoping from these triggers only after implementing invocation logging, or treat the qualitative triggers as sufficient proxies']."

**Acceptance Criteria:** V2 scoping trigger criteria distinguish between manual and telemetry-based triggers with appropriate caveats.

---

### PM-014-I7: Free-Tier Team Timeline Estimate Missing [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.4 Free-Tier Team Configuration Note |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption lens) |

**Failure Cause:** Section 7.4 identifies which sub-skills work without the $46/month Figma+Miro baseline (Wave 1 and Wave 4 sub-skills). However, it does not provide guidance on when a free-tier team should expect to need paid tools, making it difficult for such teams to plan budgets or make informed tool adoption decisions.

**Evidence:** Section 7.4: "Teams unable to meet the $46/month Figma+Miro baseline should prioritize Wave 1 and Wave 4 sub-skills (zero Required MCP cost)." No timeline guidance follows.

**Recommendation:** Add a timeline estimate: "Free-tier teams can operate Wave 1 and Wave 4 indefinitely. The $46/month Figma+Miro baseline is needed when the team reaches the Wave 2 → Wave 3 transition (Atomic Design requires Storybook + optional Figma; Inclusive Design requires Figma as Required MCP). At typical Wave 1-2 adoption rates for a 2-person team (6-12 weeks to complete one full Lean UX cycle), budget for Figma and Miro approximately 3 months after Wave 1 kickoff."

**Acceptance Criteria:** Section 7.4 free-tier team configuration note includes an approximate timeline for when paid tools become needed.

---

### PM-015-I7: Nielsen's AI Reliability Split Not Communicated in Parent Skill Routing [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 3.1 Nielsen's 10 Usability Heuristics |
| **Strategy Step** | Step 3: Generate Failure Causes (Assumption lens) |

**Failure Cause:** The parent skill routing mechanism routes users to `/ux-heuristic-eval` for "you have an existing design to evaluate" use cases. Users expect a complete 10-heuristic evaluation. However, Section 3.1 documents that 6 of 10 heuristics require team input before AI can produce actionable findings, and the realistic evaluation time is 20-35 minutes, not "under 10 minutes." The routing mechanism does not pre-brief users on this constraint before invoking the sub-skill.

**Evidence:** Section 3.1 Time estimate qualification: "A complete evaluation (all 10 heuristics) requires: (a) AI mechanical evaluation of H1/H3/H5/H9 (~5-10 minutes); (b) team provides platform context for H2/H4/H6/H7/H8/H10 (~10-20 minutes of team time); (c) AI generates contextual findings from team-provided context (~5 minutes). Total realistic time: 20-35 minutes." Section 7.1 invocation protocol: "| 'Improve my UX' | `/ux-heuristic-eval` if design exists | 'Do you have an existing design to evaluate?' |" -- no time expectation is set.

**Recommendation:** Add a pre-briefing step to the parent skill's routing for `/ux-heuristic-eval`: "Before routing to `/ux-heuristic-eval`, the parent skill surfaces: 'For a complete 10-heuristic evaluation, plan for 20-35 minutes. The evaluation produces two categories of findings: 4 heuristics (H1, H3, H5, H9) can be evaluated directly from your design; 6 heuristics (H2, H4, H6, H7, H8, H10) will require you to provide platform context during the evaluation. Ready to proceed?'"

**Acceptance Criteria:** Parent skill routing for `/ux-heuristic-eval` includes a pre-briefing statement covering evaluation time and the 4/6 heuristic reliability split.

---

## Step 5: Prioritized Mitigation Plan

### P0 -- Critical (MUST mitigate before acceptance)

| ID | Finding | Specific Action | Acceptance Criteria |
|----|---------|-----------------|---------------------|
| PM-001-I7 | KICKOFF-SIGNOFF.md never created | (1) Add named kickoff clock watcher to PROJ-020 creation checklist; (2) Add parent skill startup check for KICKOFF-SIGNOFF.md existence | KICKOFF-SIGNOFF.md absence produces an explicit routing block in the parent skill; Section 7.5 includes named clock watcher requirement |
| PM-002-I7 | AI-First Design Day-30 expiry check missed | (1) Add Day-30 Task completion (DONE status) as prerequisite for Wave 5 `/ux-ai-first` entry; (2) Add secondary owner walkthrough confirmation to KICKOFF-SIGNOFF.md format | Wave 5 evaluator confirms Entity #2 DONE status before approving /ux-ai-first; KICKOFF-SIGNOFF.md includes secondary owner walkthrough confirmation |
| PM-003-I7 | LOW confidence gate structural omission not verified | Add structural inspection test case to LOW gate validation checklist that verifies the response template does not contain a design recommendation section | LOW gate validation checklist pass criteria distinguish behavioral compliance from structural compliance; Definition of Done requires structural inspection |

### P1 -- Important (SHOULD mitigate)

| ID | Finding | Specific Action | Acceptance Criteria |
|----|---------|-----------------|---------------------|
| PM-004-I7 | Wave transition evaluator not formally assigned | Add tie-breaking rule for equivalent-seniority teams to wave transition evaluator delegation chain | Section 7.4 delegation chain includes measurable tie-breaking criterion |
| PM-005-I7 | Cross-sub-skill synthesis contradiction not surfaced at V1 | Add synthesis consistency check to wave transition verification procedure with specific cross-sub-skill pair list for Wave 1 | Wave transition Task schema includes synthesis consistency check step |
| PM-006-I7 | No-project-lead fallback disputed authority | Add operationalized tie-breaking definition for "individual who initiates" to Section 7.5 | Section 7.5 no-project-lead fallback includes timestamp-based tie-breaking rule |
| PM-007-I7 | Backward-pass count not trackable | Add Backward Pass Count field to wave transition Task schema with counting instructions for closed impediments | Wave transition Task schema includes Backward Pass Count field; Section 7.4 specifies closed impediments count toward ceiling |
| PM-008-I7 | MCP maintenance quarterly tasks not self-sustaining | Add linked MCP integration test checklist to quarterly audit task specification | Section 7.3 quarterly audit procedure references integration test checklist with pass/fail recording |
| PM-009-I7 | AI-First Design scoring artifact path uses literal template variable | Replace `{PROJ-ID}` with `PROJ-020-feature-enhancements` in all scoring artifact path references in Section 7.4 and 7.6 | No unresolved template variables in verification-critical file paths |
| PM-010-I7 | Part-time UX segment guidance advisory | Add UX capacity field to Wave 1 → Wave 2 transition Task; add Wave 3-5 block for teams with documented part-time capacity | Wave transition Task schema includes UX capacity field; Wave 3-5 criteria reference capacity record |
| PM-011-I7 | MEDIUM gate self-attestation no V1 audit | Add attestation record spot-check to wave transition evaluator procedure | Wave transition Task verification procedure includes MEDIUM gate attestation spot-check requirement |
| PM-012-I7 | HIGH RISK user research gap not surfaced at runtime | Add user research gap warning verification item to Section 7.5 pre-launch checklist | Section 7.5 or equivalent includes verification item for warning presence in parent skill onboarding |

### P2 -- Monitor (MAY mitigate; acknowledge risk)

| ID | Finding | Risk Monitoring Approach |
|----|---------|--------------------------|
| PM-013-I7 | V2 scoping triggers cannot fire without monitoring infrastructure | Distinguish manual vs. telemetry triggers in Section 4; amend quantitative triggers with "requires invocation logging" caveat |
| PM-014-I7 | Free-tier team timeline estimate missing | Add approximate timeline to Section 7.4 free-tier configuration note |
| PM-015-I7 | Nielsen's reliability split not communicated pre-routing | Add pre-briefing statement to parent skill routing for `/ux-heuristic-eval` |

---

## Step 6: Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-002-I7, PM-005-I7, PM-010-I7, PM-012-I7: AI-First Design expiry check gap, cross-sub-skill synthesis check not operationalized, part-time UX guidance unenforced, and user research gap not surfaced at runtime are structural completeness gaps. The document identifies the risks but does not complete the mitigation loop. |
| Internal Consistency | 0.20 | Negative | PM-003-I7, PM-009-I7: LOW confidence gate validation checklist does not match the structural enforcement claim (behavioral test ≠ structural inspection); template variable in scoring artifact path is internally inconsistent with a document that specifies exact file paths elsewhere. PM-011-I7: "auditable claim" without audit procedure is internally inconsistent with the document's thoroughness on other governance mechanisms. |
| Methodological Rigor | 0.20 | Neutral | The 5-wave adoption plan, sensitivity analysis, and FMEA residual RPN tracking demonstrate strong methodological rigor. The Pre-Mortem findings above affect operational implementation quality, not the core selection methodology. |
| Evidence Quality | 0.15 | Slightly Negative | PM-001-I7: "MUST confirm" behavioral constraints for the KICKOFF-SIGNOFF.md creation are not equivalent to the deterministic verification evidence claimed elsewhere. The analysis correctly documents the protocol-enforceability limitation for synthesis gates but does not apply this same acknowledgment to the KICKOFF-SIGNOFF.md gate. |
| Actionability | 0.15 | Negative | PM-001-I7, PM-004-I7, PM-006-I7, PM-007-I7, PM-008-I7, PM-009-I7: Six Major findings cluster around actionability failures: processes are specified without complete execution paths, ownership roles are specified without tie-breaking rules, and file paths contain unresolved template variables. The document's prior score (0.862) reflects prior improvements to Actionability (the weakest dimension per R11 revision header). Remaining findings concentrate precisely on this dimension. |
| Traceability | 0.10 | Neutral | Finding IDs from prior tournament iterations are well-traced. The V2 action item for cross-portfolio non-redundancy validation (RT-005-I6) is correctly registered. PM-009-I7 (template variable in path) is a minor traceability gap. |

---

## Summary

The Pre-Mortem analysis identified 15 failure causes: 3 Critical (P0), 9 Major (P1), and 3 Minor (P2). The deliverable demonstrates strong methodological rigor in its framework selection process and sensitivity analysis. The concentration of findings in governance execution paths (KICKOFF-SIGNOFF.md, AI-First Design expiry check, synthesis gate validation) indicates that the document's weakest area is the operationalization of its own governance controls -- a pattern consistent with the prior score's identification of Actionability as the weakest dimension.

**Recommendation: REVISE.** Three P0 Critical findings must be mitigated before acceptance. The mitigations are targeted (adding structural verification steps, resolving template variables, adding startup checks) and do not require changes to the core framework selection or methodology.

The three critical failure modes cluster around a common root cause: the document defines WHAT should happen in governance processes but leaves HOW to verify it happened as behavioral self-attestation rather than deterministic checks. Addressing PM-001-I7, PM-002-I7, and PM-003-I7 closes this pattern for the three highest-risk governance paths.

---

## Execution Statistics

- **Total Findings:** 15
- **Critical (P0):** 3
- **Major (P1):** 9
- **Minor (P2):** 3
- **Protocol Steps Completed:** 6 of 6
- **Failure Categories Covered:** Technical (3), Process (6), Assumption (4), External (1), Resource (1) -- all 5 lenses applied
- **H-16 Compliance:** Confirmed -- S-003 Steelman output present at `tournament-iter6/s-003-steelman.md`
