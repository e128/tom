# Pre-Mortem Report: UX Framework Selection (Revision 6)

## Execution Context

- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 6)
- **Criticality:** C4
- **Executed:** 2026-03-03T00:00:00Z
- **Tournament Iteration:** 2 (prior score: 0.747)
- **H-16 Compliance:** S-003 Steelman applied across Revision 2 (SM-001 through SM-009) and Revision 6 (SM-004 consolidated V2 roadmap); confirmed across two tournament iterations.
- **Prior S-004 Report:** `projects/PROJ-020-feature-enhancements/work/analysis/tournament-iter1/s-004-pre-mortem.md`
- **Finding Prefix:** PM-NNN-20260303b (suffix "b" distinguishes Iteration 2 from Iteration 1 findings "20260303")

---

## Failure Declaration (Step 2)

**Temporal perspective shift:** It is September 2026. The `/user-experience` skill was implemented based on the Revision 6 UX Framework Selection analysis and deployed three months ago. Post-launch operational review has surfaced multiple failure modes. Key facts established in the retrospective:

- The AI-First Design Enabler entity was created per the Revision 6 specification, but the PROJ-020 project lead (the named default owner) had competing sprint commitments. The synthesis deliverable was never started. The `/ux-ai-first` sub-skill was shipped as a stub that accepted invocations and produced outputs without surfacing that the underlying framework had not been synthesized. Users received AI-generated responses that appeared authoritative but were based on unstructured training-data knowledge, not the codified synthesis the analysis mandated.
- Teams used `/ux-jtbd` and `/ux-lean-ux` extensively. The synthesis hypothesis labeling was added to Section 7.1 in Revision 3 (addressing PM-002), but the labels were inline callouts that users read once at orientation and did not encounter at each invocation. Within 2 weeks of launch, teams were treating JTBD job statements and Lean UX assumptions as validated findings and committing design decisions to them.
- The Design Sprint zero-user fallback produced outputs labeled "untested prototype -- ready for implementation but not validated." Teams parsed "ready for implementation" and missed "not validated." The conditional structure of the label enabled selective reading. Implementation proceeded without post-launch testing in 4 of 7 teams that invoked the zero-user path.
- The MCP maintenance audit (due Q3 2026) was never executed. The Whimsical community MCP server used as the Design Sprint secondary integration had broken 6 weeks post-launch. Teams received no error message -- the sub-skill degraded silently and routed all Whimsical operations to blank outputs.

**Failure scenario label:** "Analysis approved, implementation succeeded technically, but operational failure modes were embedded in the analysis's dependency enforcement mechanisms, output labeling conventions, and MCP failure-path specifications."

---

## Iteration 1 Mitigation Status

Before identifying new findings, tracking which Iteration 1 findings were addressed in Revision 6 (the deliverable under review):

| Iter-1 Finding | Severity | Revision 6 Status | Notes |
|----------------|----------|-------------------|-------|
| PM-001-20260303 (AI-First Design no enforcement mechanism) | Critical | PARTIALLY MITIGATED | Enabler entity spec added (Section 3.8) with owner, milestone, deadline decision mechanism. Residual risk: default owner pattern (PROJ-020 project lead) is not binding enforcement -- it is documentation of a recommended assignment. |
| PM-002-20260303 (Synthesis hypothesis missing from routing) | Critical | PARTIALLY MITIGATED | HIGH RISK header promoted to document header (IN-007/PM-002); Section 7.1 triage was updated in Revision 3. However, the routing triage is a reference document -- it does not enforce labeling at skill invocation time. |
| PM-003-20260303 (MCP maintenance no named owner) | Major | MITIGATED | PM-003/SR-006 added named owner (PROJ-020 implementation lead as default, transferred at kickoff) with 4 enumerated responsibilities. |
| PM-004-20260303 (Score compression no adjustment guidance) | Major | NOT MITIGATED (deferred) | No context-sensitive weight adjustment guide was added in Revision 6. The finding is acknowledged in the compression zone note but no actionable adjustment mechanism was provided. |
| PM-005-20260303 (Zero-user dead end Kano→JTBD→no path) | Major | MITIGATED | Zero-user pre-launch path added to Section 7.1 via Revision 3 (PM-005/PM-008 response). |
| PM-006-20260303 (Design Sprint zero-user fallback label) | Major | PARTIALLY MITIGATED | Zero-user fallback output defined in R5 with "untested prototype" caveat. However, "ready for implementation" language retained in the skill surface message -- conditional label, not leading label. |
| PM-007-20260303 (All evidence through 3 artifacts only) | Major | MITIGATED | E-024, E-025, E-026 added as direct primary source citations (SR-004 -- R6). |
| PM-008-20260303 through PM-013-20260303 (Minor findings) | Minor | PARTIALLY-TO-FULLY MITIGATED | PM-011 (HEART mode transition) addressed in Section 3.4; PM-012 (Figma fallback for 3 frameworks) addressed via AI reliability tiers table for Nielsen's and degraded-mode behavior for HEART; PM-013 (C4 sensitivity) acknowledged as accepted risk. PM-009 (ceiling expansion process) not added as a formal process. |

**Summary:** Of the 2 Critical findings, both are partially mitigated but retain residual failure modes. Of the 5 Major findings, 3 are fully mitigated, 1 is partially mitigated (PM-006), and 1 is not mitigated (PM-004). This informs the prospective hindsight analysis below.

---

## Summary

The Pre-Mortem analysis of the Revision 6 deliverable identified 11 failure causes across all 5 failure categories. The residual failure risks are concentrated in three structural patterns that Revision 6 did not fully close: (1) enforcement-by-documentation rather than enforcement-by-mechanism for the AI-First Design blocking dependency and synthesis hypothesis output labeling; (2) conditional phrasing that permits selective parsing in the Design Sprint zero-user fallback output; and (3) two entirely new failure modes -- the tooling cost barrier at $46/month creating a selection bias toward free-MCP-compatible frameworks, and the absence of a formal process for the 30-day automatic substitution trigger that was referenced but not structurally defined. The deliverable is assessed as **ACCEPT with targeted P0 and P1 mitigations** -- it is analytically stronger than Revision 5 and has addressed the major structural gaps, but carries 2 residual Critical failure modes and 3 new Major failure modes introduced by Revision 6's additions.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-20260303b | AI-First Design Enabler default owner pattern allows plausible-deniability non-enforcement: "PROJ-020 project lead" is named as default but the analysis does not create the Enabler entity, does not verify the owner exists at the time of analysis approval, and does not specify what "kickoff" means in a way that binds the assignment to a datable event | Process | High | Critical | P0 | Actionability |
| PM-002-20260303b | Zero-user Design Sprint fallback retains "ready for implementation" in the skill surface message -- the conditional framing ("ready for implementation but has not been validated with users") can be parsed selectively; teams read the first clause and miss the second; unconditional implementation proceeds | Assumption | High | Critical | P0 | Actionability |
| PM-003-20260303b | Score compression zone has no context-sensitive weight adjustment guide (PM-004-20260303 from Iteration 1 was not mitigated in Revision 6) -- teams prioritizing MCP integration will produce a different top-10 without a sanctioned path for that adjustment, either ignoring the caveat or performing unsanctioned weight changes | Assumption | Medium | Major | P1 | Completeness |
| PM-004-20260303b | The Revision 6 tooling cost table ($46/month required, $145-245/month full enhancement) creates an implicit framework selection bias that the analysis does not address: teams unable or unwilling to pay Figma+Miro may substitute free tools (Penpot, FigJam) that lack the MCP integrations the analysis relies on, and the skill definitions do not identify which MCP integrations are replaceable with non-listed free alternatives | External | Medium | Major | P1 | Completeness |
| PM-005-20260303b | The 30-day automatic substitution trigger for AI-First Design ("if synthesis not in active development within 30 days of implementation phase start, Service Blueprinting replaces it") references a process that does not exist in the worktracker or in any defined enforcement mechanism -- the trigger will pass silently because no one is checking it; the Enabler entity would need to include a due-date field and a blocking relationship to the sprint planning event | Process | High | Major | P1 | Actionability |
| PM-006-20260303b | Synthesis hypothesis labeling in Section 7.1 routing triage addresses the routing decision point, but the actual skill invocation output does not carry the synthesis hypothesis label on each output artifact -- once the skill is built, the Section 7.1 routing warning is a one-time orientation artifact that users bypass after first use; there is no mechanism specified to ensure the sub-skill itself labels its outputs as synthesis hypotheses at the artifact level | Technical | Medium | Major | P1 | Completeness |
| PM-007-20260303b | The C3 sensitivity perturbation added in Revision 6 (DA-002 -- the adversarial upweighting to 25%) shows that Kano (#9) and Fogg (#10) both fall below the selection threshold under MCP-heavy weighting, but the analysis does not provide a formal remediation path if a team applies this weighting: the Section 7 routing guide still routes to `/ux-kano-model` and `/ux-behavior-design` without conditioning on the team's MCP investment level | Assumption | Low | Minor | P2 | Completeness |
| PM-008-20260303b | The ethics gap V2 prioritization table correctly identifies dark patterns (P1, high risk) and algorithmic bias (P1, high risk), but these are V2 candidates with no V1 mitigations at the skill level -- the Fogg Behavior Model ethical guardrail (Section 3.10) covers only one of the five ethics sub-domains, and the analysis does not specify what behavior a team should exhibit today (before V2) when they encounter algorithmic bias in AI-generated UX or detect a potential dark pattern in their product | Process | Medium | Minor | P2 | Completeness |
| PM-009-20260303b | The post-correction RPN verification table shows FM-001 (single-rater bias) retaining RPN 126 as a "structural constraint" -- this is acknowledged but not actionable. The analysis does not specify what the team should do if they encounter a scoring disagreement in the non-selected frameworks zone (ranks 11-40, ±0.25 uncertainty). In practice, a team member who disputes a rank-12 vs. rank-15 classification has no defined escalation path within the analysis itself | Resource | Low | Minor | P2 | Methodological Rigor |
| PM-010-20260303b | The consolidated V2 roadmap (SM-004 -- R6) lists user research tools (Maze/UserZoom) as the highest-priority P1 addition but provides no bridge guidance for V1 teams who need some user research capability before V2 is built -- the gap between "no dedicated user research framework in V1" and "V2 P1 candidate" is 6-12 months; teams building consumer products are at HIGH RISK during that gap and the analysis provides no interim guidance beyond the "minimum viable research" caveat | External | Medium | Minor | P2 | Completeness |
| PM-011-20260303b | The AI-First Design framework review cadence (IN-009 -- R6) specifies "re-validate before Q4 2026; full revision review at Q2 2027" with the synthesis owner as responsible party -- but if the synthesis deliverable is never produced (the PM-001-20260303b failure path), the review cadence has no deliverable to review; the shelf-life expiration is operationally moot in the failure case and there is no fallback review process for the Service Blueprinting substitution path | Technical | Low | Minor | P2 | Actionability |

---

## Detailed Findings

### PM-001-20260303b: AI-First Design Default Owner Pattern Creates Plausible-Deniability Non-Enforcement [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.8 (AI-First Design Prerequisite Management) |
| **Strategy Step** | Step 3 -- Process failures lens |

**Failure Cause:** The Revision 6 Enabler entity specification (FM-001-20260303 response) defines the owner as "ps-researcher + ps-synthesizer orchestration lead (assigned at PROJ-020 implementation kickoff; if no assignment is made at kickoff, the default is the PROJ-020 project lead)." This conditional default pattern creates an enforcement gap: no assignment is pre-committed, the assignment event ("PROJ-020 implementation kickoff") is not a date-specific trigger, and the Enabler entity itself is not created by the analysis -- it is described for creation. The analysis specifies what the Enabler entity should contain but does not create it, verify it, or bind the owner assignment to any datable obligation.

**Evidence:**
Section 3.8 states: "Worktracker entity [FM-001-20260303 -- R6]: An Enabler entity titled 'AI-First Design Framework Synthesis' MUST be created in the PROJ-020 worktracker before implementation begins. Entity specifications: Owner: ps-researcher + ps-synthesizer orchestration lead (assigned at PROJ-020 implementation kickoff; if no assignment is made at kickoff, the default is the PROJ-020 project lead)."

The phrase "if no assignment is made at kickoff, the default is the PROJ-020 project lead" is the failure-permissive clause: it provides a pre-approved escape route (default to project lead) that makes the un-assigned-at-kickoff state normal rather than a blocking condition.

**Analysis:**
In the failure retrospective, this pattern enabled the following sequence: kickoff occurred, no specific orchestration agent was assigned, the PROJ-020 project lead became the default owner as specified, and then had competing priorities. The analysis had correctly specified the mechanism -- but the mechanism specified a default that was equivalent to "no enforcement." The Iteration 1 finding (PM-001-20260303) called for "a time-bounded automatic substitution clause" -- this was added. However, the substitution clause itself (30-day trigger) has the same enforcement problem: it specifies that the project lead "MUST formally choose at kickoff" but does not specify what happens if the choice is not made at kickoff. The failure mode is one level deeper than Iteration 1 identified.

**Recommendation:**
Replace the "default to project lead" pattern with a "no-default -- blocking" pattern: if no orchestration agent is assigned at kickoff, the 30-day clock starts immediately and Service Blueprinting is the automatic substitution with no further decision required. This makes the default action (substitution) safer than the inaction (no assignment). The Enabler entity specification should be restructured: create it as a trackable artifact with a specific due date computed from the kickoff date (kickoff date + 30 calendar days), not a conditional trigger requiring a human decision to activate.

**Acceptance Criteria:** Section 3.8 specifies that the Enabler entity's 30-day deadline is computed automatically from the kickoff date, requires no decision to activate the substitution trigger, and names Service Blueprinting as the automatic substitution (not a choice requiring a new analysis decision). The phrase "if no assignment is made" is removed -- the Enabler entity must have a named owner at the time of creation, not a conditional default.

---

### PM-002-20260303b: Design Sprint Zero-User Fallback Retains "Ready for Implementation" in Leading Position [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 3.2 (Design Sprint Zero-User Fallback) |
| **Strategy Step** | Step 3 -- Assumption failures lens |

**Failure Cause:** The Revision 5/6 zero-user fallback output specification contains the following skill surface message: "This sprint produced an untested prototype. The prototype is ready for implementation but has not been validated with users. Recommend post-launch user testing within the first 5 active users using the attached test plan." The phrase "ready for implementation" appears before "has not been validated with users." Selective reading produces the interpretation: "prototype is ready for implementation" -- and this is the interpretation teams acted on in the failure retrospective (4 of 7 teams).

**Evidence:**
Section 3.2 states: "The skill surfaces the message: 'This sprint produced an untested prototype. The prototype is ready for implementation but has not been validated with users. Recommend post-launch user testing within the first 5 active users using the attached test plan.'"

The PM-006-20260303 Iteration 1 finding called for replacing "ready for implementation" with a conditional label and adding a 14-day testing trigger. Revision 3 addressed this by adding a 14-day trigger and a post-launch validation commitment -- but the "ready for implementation" language was retained in the skill surface message. The acceptance criteria from PM-006-20260303 specified "The zero-user fallback outcome description contains a conditional label (not 'ready for implementation')," but the revision retained "ready for implementation" while adding qualifying clauses after it.

**Analysis:**
The Iteration 1 finding was technically addressed: a conditional label was added and a testing trigger was specified. However, the implementation of the label retained the dangerous phrase as the first clause and made the safety information the second clause. This is a label structure failure, not a content failure -- the content is correct, but the ordering permits selective parsing. The failure is that the Iteration 1 acceptance criteria was satisfied nominally ("conditional label present") while the structural problem (dangerous phrase in leading position) persisted. This is a pattern where addressing a finding's letter without addressing its spirit results in a persistent failure mode.

**Recommendation:**
Rewrite the skill surface message so the validation status leads and the implementation readiness trails: "VALIDATION STATUS: Untested prototype -- not validated with real users. The prototype is structurally complete and implementation-ready, but design assumptions have NOT been confirmed with users. Mandatory: schedule user testing within 14 days of first user activation using the attached test plan. Implementation without completing this step means design decisions are based on untested assumptions." The validation status must be the first statement, not a qualifying clause appended to "ready for implementation."

**Acceptance Criteria:** The skill surface message begins with validation status (NOT VALIDATED or equivalent), not implementation readiness. The phrase "ready for implementation" does not appear before the validation warning. A human-auditable test confirms that a user reading only the first two words of the message receives a warning, not a permission.

---

### PM-003-20260303b: Score Compression Zone Context-Sensitive Adjustment Guide Not Mitigated (Carry-Forward from PM-004-20260303) [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 (Score Compression Zone acknowledgment, DA-005 response, Sensitivity Analysis) |
| **Strategy Step** | Step 3 -- Assumption failures lens |

**Failure Cause:** The Iteration 1 finding PM-004-20260303 called for a "Context-Sensitive Weight Adjustment Guide" with 3-4 pre-defined scenarios showing rank impact under domain-specific weight changes. Revision 6 added a full C3 adversarial perturbation table (DA-002 -- R6) showing the rank impacts of C3=25%, and this substantially addresses the analytical gap. However, no "Context-Sensitive Weight Adjustment Guide" as a decision aid for teams was added. The perturbation table is an analytical artifact demonstrating sensitivity; it is not a guide that tells teams "if your context matches X, use weight configuration Y and your top-10 becomes Z."

**Evidence:**
Section 1 Sensitivity Analysis now contains three perturbation tables (C1, C2, C3). The DA-002 finding from the Revision 6 change log states: "Finding [DA-002 -- R6]: Under C3=25% upweighting, Kano (#9) and Fogg (#10) fall below the selection threshold... Interpretation: Teams prioritizing MCP integration as a primary selection driver... should consider replacing Kano and/or Fogg with Service Blueprinting and reviewing HEART's role." This is directional guidance but not a structured decision framework.

**Analysis:**
The C3 perturbation table is valuable and substantially strengthens the methodological rigor dimension. However, teams need a structured decision guide, not a raw perturbation table. The difference: a perturbation table shows "what happens if you change this weight"; a decision guide specifies "if your situation matches profile A (analytics-heavy, deep Figma investment, no user research), use the C3=25% weighting and select {specified top-10}." The missing artifact is the mapping from team profile to weight configuration to resulting selection -- not the underlying sensitivity computation.

**Recommendation:**
Add a "When to Override the Baseline Weighting" decision table to Section 1 with at minimum 3 team profiles:
- Profile A: MCP-first team (deep Figma/Miro investment, analytics-driven) -- use C3=25% table from DA-002; Service Blueprinting replaces Fogg; HEART moves to rank #9; accept Kano below threshold.
- Profile B: Pre-MCP team (budget constraint, starting from scratch without tooling) -- weight C6 (Accessibility to non-specialists) higher at 20%, reduce C3 to 10%; show resulting re-ranking.
- Profile C: Service/multi-channel product team -- weight C4 (Maturity) at 20%, substitute Service Blueprinting for Fogg as a pre-approved substitution.

**Acceptance Criteria:** Section 1 contains a decision table mapping at least 3 team profiles to their recommended weight configuration and the resulting top-10 changes (explicit framework name substitutions shown), enabling teams to select a pre-analyzed configuration rather than performing unsanctioned ad-hoc re-weighting.

---

### PM-004-20260303b: Tooling Cost Barrier Creates Undisclosed Framework Selection Bias [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.3 (MCP Maintenance Contract, Tooling Cost Note) |
| **Strategy Step** | Step 3 -- External failures lens |

**Failure Cause:** The Revision 6 tooling cost table (DA-009 -- R6) correctly identifies that the required MCP portfolio (Figma + Miro) costs approximately $46/month for a 2-person team. This creates a framework selection bias that the analysis does not address: teams that cannot or will not pay $46/month are operating with a different MCP configuration than the analysis assumes. Figma has free-tier alternatives (Penpot, FigJam, Whimsical -- though Whimsical is community MCP). The analysis rates frameworks using Figma at C3=7-10 (Native MCP); teams using Penpot instead will experience effective C3=1-3 (no production MCP) for those frameworks. The selection may not hold for teams in this cost bracket.

**Evidence:**
Section 7.3 states: "The required MCP portfolio (Figma + Miro) costs approximately $46/month for a 2-person team. This is the minimum viable MCP configuration for the `/user-experience` skill to function at full capability." The analysis does not address what the effective top-10 selection looks like for teams that substitute free design tools for Figma and Miro.

**Analysis:**
The cost disclosure is accurate and appropriate. The gap is the absence of a "free-tier team" framework selection guidance path. A team using Penpot + FigJam + open-source Storybook faces a dramatically different C3 score distribution. Under Penpot (no MCP server), Figma-dependent frameworks (Design Sprint C3=8, Nielsen's C3=7, Atomic Design C3=10, Microsoft Inclusive Design C3=6, AI-First Design C3=8) would have effective C3 scores of 1-3. This would make frameworks with low Figma dependency relatively more attractive: HEART (C3=4, non-Figma), JTBD (C3=5, Miro + WebSearch), Kano (C3=4, Miro), Fogg (C3=3, no required MCP), Lean UX (C3=6, Miro+Figma). The selection is implicitly scoped to paid-tool teams, but this is not stated.

**Recommendation:**
Add a "Free-Tier Team Configuration" section to Section 7.3 that explicitly states: "The selection in this analysis assumes Figma Professional ($15/editor/month) and Miro Team ($8/member/month) are available. Teams using free-tier tools only should note that C3 scores for Figma-dependent frameworks (Design Sprint, Nielsen's, Atomic Design, Microsoft Inclusive Design, AI-First Design) are significantly reduced. Under a free-tool constraint (Storybook + Penpot/FigJam + open-source tooling), frameworks with Required MCPs = None (/ux-heart-metrics, /ux-jtbd, /ux-kano-model, /ux-behavior-design) remain fully functional; Lean UX degrades to Miro-only which is also paid. For a fully free implementation, the effective top-tier frameworks are: JTBD, HEART (goal-setting mode), Lean UX (without Miro), Nielsen's (screenshot input mode), and Kano (survey input mode)."

**Acceptance Criteria:** Section 7.3 contains a free-tier team configuration note that identifies which sub-skills function without paid MCP subscriptions and provides an alternative minimum-cost portfolio for teams that cannot pay the $46/month baseline.

---

### PM-005-20260303b: 30-Day Automatic Substitution Trigger Is Referenced Without a Defined Tracking Mechanism [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.8 (AI-First Design Prerequisite Management, Deadline Decision) |
| **Strategy Step** | Step 3 -- Process failures lens |

**Failure Cause:** The 30-day automatic substitution trigger in Section 3.8 states: "Deadline decision: If the synthesis deliverable is not completed before the PROJ-020 implementation sprint 1 begins, the project lead MUST formally choose at kickoff: (a) delay `/ux-ai-first` implementation until synthesis is complete, OR (b) substitute Service Blueprinting (rank #11, score 7.40) as the permanent replacement. This decision cannot be deferred." The trigger is well-defined in principle, but no tracking mechanism is specified: there is no artifact that records "kickoff date + 30 days = deadline date," no worktracker field that enforces the deadline, and no escalation path if the choice is not made at kickoff (the "cannot be deferred" statement has no enforcement mechanism).

**Evidence:**
Section 3.8's Enabler entity specification includes "Deadline decision" as a field but does not specify the Enabler entity's own due date in a concrete, computable form. The "Blocking relationship: This Enabler blocks Story: Implement `/ux-ai-first`" is correct but does not prevent the story from being added to the backlog if the Enabler is not tracked. The phrase "This decision cannot be deferred" is an instruction without an enforcement mechanism.

**Analysis:**
The Iteration 1 finding PM-001-20260303 called for "a time-bounded automatic substitution clause (30-day or sprint-count trigger) that activates Service Blueprinting as the replacement if the synthesis deliverable is not in active development." Revision 6 added the deadline decision mechanism. However, a deadline decision described in an analysis document is not the same as a deadline tracked in a worktracker system. The failure path: kickoff occurs, the choice is not formally made, no worktracker alert fires, implementation pressure causes the team to proceed with `/ux-ai-first` as a stub (the failure scenario from the retrospective), and the 30-day clock was never started because "kickoff" was never formally recorded as a date.

**Recommendation:**
Add to the Enabler entity specification: "Due date computation: [Enabler: AI-First Design Framework Synthesis] MUST have a worktracker DUE DATE field set to PROJ-020 kickoff date + 30 calendar days at the time the Enabler entity is created. If no kickoff date has been recorded in the worktracker at Enabler creation time, this is itself a blocking condition -- the Enabler cannot be marked 'in-progress' until a kickoff date is recorded. If the Enabler's DUE DATE passes without DONE status, the following action executes automatically: the [Story: Implement `/ux-ai-first`] is marked BLOCKED and replaced with [Story: Implement `/ux-service-blueprinting`] in the backlog."

**Acceptance Criteria:** The Enabler entity specification in Section 3.8 includes a concrete due-date computation formula (kickoff date + N days), requires the kickoff date to be recorded as a prerequisite for creating the Enabler, and specifies the automatic backlog substitution action that executes when the due date passes without DONE status.

---

### PM-006-20260303b: Synthesis Hypothesis Labeling Is a Routing-Time Warning, Not an Output-Time Label [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.1 (Parent Skill Triage Mechanism) and Section 1 (AI Execution Mode Taxonomy) |
| **Strategy Step** | Step 3 -- Technical failures lens |

**Failure Cause:** The Iteration 1 PM-002-20260303 finding called for synthesis hypothesis labels in the Section 7.1 routing triage. Revision 3 added these labels. However, Section 7.1 is a reference document section, not an operational enforcement point. The skill implementation spec does not specify that each synthesis-hypothesis sub-skill output must carry a visible "[SYNTHESIS HYPOTHESIS]" label on the output artifact itself. The analysis specifies where the warning appears (the routing triage) but does not specify that the warning must persist into the output artifact level.

**Evidence:**
Section 7.1 provides the routing triage with routes (a) through (i). Route (a) states: "Before design -- I don't know what to build yet → Route to: /ux-jtbd (strategic framing)." The Iteration 1 finding accepted criteria required "[SYNTHESIS HYPOTHESIS: AI output requires human validation before use as design decisions]" labels in the Section 7.1 routing triage -- which was implemented. However, the analysis describes the skill output in Section 3.6 (JTBD) as: "AI synthesizes job statements from existing user interview transcripts, support tickets, and App Store reviews... The resulting job statement anchors all subsequent design decisions." The Section 3.6 output description does not require the output artifact to carry a synthesis hypothesis label.

**Analysis:**
There are two enforcement points for the synthesis hypothesis warning: (1) routing time (the user sees the warning before invoking the sub-skill, and Section 7.1 addresses this) and (2) output time (the output artifact itself carries the warning, so the user sees it when they use the output). The analysis addresses routing time but not output time. In production, users invoke a sub-skill repeatedly after the first use -- they stop reading the routing triage and go directly to the output. If the output artifact itself does not carry the synthesis hypothesis label, the warning is only visible at first invocation.

**Recommendation:**
Add to Section 3.6 (JTBD), Section 3.5 (Lean UX), Section 3.2 (Design Sprint Day 4 synthesis), and Section 3.7 (Microsoft Inclusive Design -- Persona Spectrum) a specification that all synthesis-hypothesis step outputs MUST include a header label: "[SYNTHESIS HYPOTHESIS -- REQUIRES VALIDATION] This output was generated from [input source type]. It must be validated with at least [minimum validation threshold] before informing design decisions. See data sufficiency requirements in Section [N]." The output-time label is the persistent enforcement mechanism; the routing-time warning is the orientation mechanism.

**Acceptance Criteria:** Section 3.6, 3.5, 3.2, and 3.7 each contain an explicit output specification that requires synthesis hypothesis step outputs to carry a [SYNTHESIS HYPOTHESIS -- REQUIRES VALIDATION] label with minimum validation threshold at the artifact level, not only at the routing-time warning level.

---

## Recommendations

### P0 -- Critical (MUST Mitigate Before Acceptance)

**PM-001-20260303b: Remove Default Owner Escape Clause from AI-First Design Enabler Specification**
- **Action:** Remove the "if no assignment is made at kickoff, the default is the PROJ-020 project lead" clause. Replace with: Enabler entity must have a named owner assigned AT THE TIME OF CREATION (not at kickoff). If no owner is available at creation time, the Enabler is in BLOCKED state and `/ux-ai-first` implementation cannot begin until an owner is assigned. This makes owner-assignment a prerequisite for starting, not a conditional to be resolved later.
- **Acceptance Criteria:** The phrase "if no assignment is made at kickoff" is removed from Section 3.8. The Enabler entity specification requires a named owner at creation time and treats no-owner as a BLOCKED state.

**PM-002-20260303b: Reorder Zero-User Fallback Surface Message to Lead With Validation Status**
- **Action:** Rewrite the Design Sprint zero-user fallback skill surface message so validation status appears first. Proposed replacement: "VALIDATION STATUS: NOT VALIDATED -- This sprint produced an untested prototype. The prototype is structurally complete but design assumptions have not been confirmed with real users. Implementation may proceed as a risk-acknowledged decision ONLY with explicit commitment to complete user testing within 14 days of first user activation per the attached test plan. Do NOT mark this sprint as complete without acknowledging this status."
- **Acceptance Criteria:** The skill surface message begins with validation status (NOT VALIDATED). The phrase "ready for implementation" does not appear before the validation warning. The output message is auditable by reading only the first sentence.

### P1 -- Important (SHOULD Mitigate)

**PM-003-20260303b: Add Context-Sensitive Weight Adjustment Decision Table**
- **Action:** Add a "When to Override the Baseline Weighting" decision table to Section 1 with 3 team profiles (MCP-first, pre-MCP/budget-constrained, service/multi-channel) mapping each to a weight configuration and explicit framework substitutions.
- **Acceptance Criteria:** Section 1 contains a decision table with at least 3 profiles; each profile shows the weight configuration, resulting top-10 changes (explicit framework substitutions), and selection rationale.

**PM-004-20260303b: Add Free-Tier Team Configuration to Section 7.3**
- **Action:** Add a "Free-Tier Team Configuration" note to Section 7.3 identifying which sub-skills function without paid MCPs and providing an alternative minimum-cost portfolio for teams that cannot meet the $46/month baseline.
- **Acceptance Criteria:** Section 7.3 explicitly states the paid-tool assumption and provides an identified free-tier alternative portfolio (at minimum naming which sub-skills have Required MCPs = None).

**PM-005-20260303b: Add Concrete Due-Date Computation to Enabler Specification**
- **Action:** Add to the Enabler entity specification in Section 3.8: due-date computation formula (kickoff date + N calendar days), requirement that kickoff date be recorded as a prerequisite, and automatic backlog substitution action that fires when due date passes without DONE status.
- **Acceptance Criteria:** Section 3.8 specifies a computable due date (not a conditional decision) and a specified automatic action on expiry.

**PM-006-20260303b: Add Output-Time Synthesis Hypothesis Labeling Requirements to Section 3 Sub-Skill Specifications**
- **Action:** Add synthesis hypothesis output label specifications to Sections 3.2 (Design Sprint -- Day 4 synthesis), 3.5 (Lean UX), 3.6 (JTBD), and 3.7 (Microsoft Inclusive Design -- Persona Spectrum). Each specification requires the output artifact to carry a [SYNTHESIS HYPOTHESIS -- REQUIRES VALIDATION] label with minimum validation threshold.
- **Acceptance Criteria:** Four Section 3 sub-skill entries contain explicit output specifications requiring synthesis hypothesis labels at the artifact level, not only in the routing triage.

### P2 -- Monitor (MAY Mitigate; Acknowledge Risk)

**PM-007-20260303b: C3 Sensitivity Routing Gap**
- **Risk:** Teams applying C3=25% weighting will use Kano and Fogg sub-skills that the analysis shows fall below threshold under their preferred weighting.
- **Monitoring:** Add a note to the C3 perturbation table: "Teams using MCP-heavy weighting (C3=25%) should route to Service Blueprinting sub-skill as their service design tool and should treat Kano and Fogg sub-skills as supplementary rather than core."

**PM-008-20260303b: Ethics Sub-Domain V1 Behavioral Guidance**
- **Risk:** Teams encounter algorithmic bias or dark pattern situations in V1 with no framework guidance.
- **Monitoring:** Add an interim ethics note to Section 4 Coverage Analysis: "Before V2 dark patterns and algorithmic bias frameworks are available, teams SHOULD: (a) apply the Fogg ethical screening to any design involving motivation or prompt mechanics; (b) manually audit against the top 12 Brignull dark patterns checklist (available at deceptive.design) before shipping subscription flows or notification opt-out flows; (c) apply PAIR Guidebook AI fairness heuristics manually before deploying AI-generated content recommendations."

**PM-009-20260303b: Single-Rater Bias Escalation Path**
- **Risk:** Teams disagree with non-selected framework scores without a resolution path.
- **Monitoring:** Add to the FM-001 disclosure: "For teams that need to challenge a non-selected framework's score, the resolution path is: (1) identify the specific criterion where the disagreement exists; (2) apply the criterion rubric mechanically (not by general impression); (3) if the revised score changes the rank by more than 2 positions, document the revised score and the rationale and treat the selection as re-opened for that criterion."

**PM-010-20260303b: V1-to-V2 User Research Gap Interim Guidance**
- **Risk:** Teams building consumer products have no user research path for 6-12 months until V2.
- **Monitoring:** Add to the HIGH RISK gap notice in the document header: "Interim V1 guidance: Teams building consumer products should supplement V1 skill usage with direct tool subscriptions to Maze (free tier: 3 unmoderated sessions/month) or Lookback (free tier: 5 sessions/month) for user research, even before the V2 user research framework is built. The V1 portfolio is not complete without some direct user contact mechanism."

**PM-011-20260303b: AI-First Design Review Cadence Without Synthesis Deliverable**
- **Risk:** If synthesis is never produced, the review cadence is operationally moot.
- **Monitoring:** Section 3.8 should add: "If the substitution trigger activates and Service Blueprinting replaces AI-First Design, the 6-month review cadence transfers to: review Service Blueprinting for emerging AI-product UX frameworks that may enable a future AI-First Design return; check the PAIR Guidebook and NN Group for emerging AI UX patterns that should be incorporated."

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-003-20260303b (no context-sensitive adjustment guide despite C3 perturbation table being added), PM-004-20260303b (tooling cost barrier creates undisclosed selection bias for free-tier teams), PM-006-20260303b (synthesis hypothesis labeling present at routing time but not at output-artifact level), PM-010-20260303b (no V1 interim user research guidance). Multiple completeness gaps remain despite significant Revision 6 additions. |
| Internal Consistency | 0.20 | Positive | Revision 6 significantly improved internal consistency: arithmetic corrections across all three perturbation tables are now verified; DA-001/DA-003 minimality qualification resolves the circular minimality claim; DA-006 adversarial correction reframing correctly characterizes error discovery as evidence of non-zero error rate, not a reliability certificate. No internal contradictions found in Revision 6. |
| Methodological Rigor | 0.20 | Positive | The addition of the C3 adversarial perturbation (DA-002 -- R6), the WSM method naming with academic references (SM-002/DA-008), the post-correction RPN verification table (FM-002-20260303 -- R6), and the ethics gap prioritization table (FM-003-20260303 -- R6) substantially strengthen methodological rigor. PM-009-20260303b (no single-rater bias resolution path) is a minor gap. Net positive improvement from Iteration 1. |
| Evidence Quality | 0.15 | Positive | E-024 (NN Group 2024), E-025 (Baymard Institute), E-026 (Keeney & Raiffa 1976; Belton & Stewart 2002) added as direct primary source citations. This addresses the Iteration 1 PM-007-20260303 finding (all evidence through 3 intermediate artifacts). Evidence dimension is materially stronger in Revision 6. |
| Actionability | 0.15 | Negative | PM-001-20260303b (default owner escape clause weakens the Enabler enforcement mechanism), PM-002-20260303b (zero-user fallback "ready for implementation" label retained in leading position), PM-005-20260303b (30-day trigger has no concrete tracking mechanism). The three actionability failures are the primary residual risk cluster; they represent implementation-phase failure modes that survived the Revision 6 corrections. |
| Traceability | 0.10 | Positive | Revision 6 change log is comprehensive and directly traceable to all tournament-iter1 findings. Navigation table updated (CC-002) to include Revision History. The post-correction RPN verification table provides end-to-end traceability for the FMEA correction chain. H-16 compliance documented and confirmed across two steelman iterations. |

**Overall Assessment:** ACCEPT with P0 and P1 mitigations required. Revision 6 has made material improvements to methodological rigor, evidence quality, and traceability -- three of the six dimensions show positive movement from Iteration 1. The actionability and completeness dimensions retain targeted failure modes. The 2 Critical findings (PM-001-20260303b and PM-002-20260303b) are both residual from Iteration 1 -- they represent cases where Iteration 1 findings were addressed at the content level but not at the structural enforcement level. Addressing these two findings brings the deliverable into the high-probability-of-operational-success range. Estimated composite score impact of P0+P1 mitigations: +0.06 to +0.09 on Actionability and Completeness dimensions (these dimensions have the largest remaining gap from the 0.92 threshold).

---

## Execution Statistics

- **Total Findings:** 11
- **Critical:** 2 (PM-001-20260303b, PM-002-20260303b)
- **Major:** 4 (PM-003-20260303b, PM-004-20260303b, PM-005-20260303b, PM-006-20260303b)
- **Minor:** 5 (PM-007-20260303b through PM-011-20260303b)
- **Protocol Steps Completed:** 6 of 6
- **Failure Categories Covered:** Technical (2), Process (3), Assumption (3), External (2), Resource (1)
- **H-16 Compliance:** Confirmed -- S-003 Steelman applied in Revision 2 (SM-001 through SM-009) and Revision 6 (SM-004 consolidated V2 roadmap); confirmed across both tournament iterations
- **Iteration 1 Carry-Forward Findings:** 3 (PM-001 partially mitigated; PM-002 partially mitigated; PM-004 not mitigated -- becomes PM-003-20260303b)
- **New Findings vs. Iteration 1:** 5 new findings (PM-002-20260303b label structure residual, PM-004-20260303b tooling cost bias, PM-005-20260303b tracking mechanism gap, PM-006-20260303b output-time labeling gap, plus 5 Minor findings surfaced by Revision 6 additions)
- **Finding Prefix Used:** PM-NNN-20260303b

---

*Strategy: S-004 Pre-Mortem Analysis | Template: s-004-pre-mortem.md v1.0.0 | Deliverable Revision: 6 | Tournament: Iteration 2 | Prior Score: 0.747 | Executed: 2026-03-03*
