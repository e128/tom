# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context

- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 3 (R2 revision applied; Iteration 2 scored 0.724 REVISE)
- **H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (confirmed by Research Backing section referencing adversarial tournament at C4; prior strategy outputs include Steelman per tournament chain)
- **Criticality:** C4 (GitHub Enhancement issue for a framework skill addition -- architecture-level change touching mandatory-skill-usage.md, CLAUDE.md, AGENTS.md, ~67 artifacts; irreversible once merged and adopted)

---

# Pre-Mortem Report: `/user-experience` Skill Enhancement Issue

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `ux-skill-issue-body-saucer-boy.md` -- GitHub Enhancement issue, `/user-experience` skill, ~1146 lines
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004, Iteration 3)
**H-16 Compliance:** S-003 Steelman applied in prior tournament chain (confirmed)
**Failure Scenario:** It is September 2027. The `/user-experience` skill was merged in March 2026. Wave 1 shipped on time. WAVE-1-SIGNOFF.md was completed. Three teams invoked the skill in Month 1. By Month 6, only 1 team remained active. The MCP health runbook was not created before merge because it was not an AC. Wave 2 stalled because the WAVE-2-SIGNOFF.md mechanism was implemented as a file-existence check but the template was never shipped with the skill. The implementation team read the ACs literally and built what was specified -- and what was specified had gaps that made the specification unimplementable as a coherent, adoption-driving product.

---

## Summary

R2 addressed 6 of the 11 Iteration 2 findings with genuine structural fixes: the closure condition is now explicit (PM-001 resolved), wave enforcement is mechanized via WAVE-{N}-SIGNOFF.md (PM-004 resolved), Service Blueprinting substitution is corrected (PM-006 resolved), the JTBD benchmark is now deterministic (PM-008 resolved), MCP operational constraints are documented (FM-002 resolved), and the pre-launch validation AC is added (DA-001 resolved). However, the Pre-Mortem analysis from the retrospective frame of September 2027 surfaces 2 new Critical and 3 new Major findings that R2 did not address or inadvertently created. Most critically: the MCP maintenance owner and health runbook AC was described in PM-002's mitigation but was NOT added to the Acceptance Criteria section -- the prose commitment in the Known Limitations section is still unverifiable at closure. Additionally, R2's WAVE-{N}-SIGNOFF.md enforcement mechanism introduces a new gap: the signoff template is referenced but not defined in the ACs, so implementations will produce incompatible signoff files. The overall risk posture has improved from HIGH to MEDIUM-HIGH. REVISE is still required -- but the remaining gaps are fewer and more targeted than in prior iterations.

---

## Step 2: Temporal Perspective Shift

**Retrospective frame established:** It is September 2027. The issue was merged in March 2026. We are 18 months into post-merge operation. Wave 1 shipped. WAVE-1-SIGNOFF.md was completed. But adoption plateaued, wave progression stalled, and a Figma MCP disruption in Q3 2026 degraded 4 sub-skills with no coordinated response because the maintenance runbook was never created. We are explaining failure after the fact, not predicting it.

---

## R2 Fix Verification

| Prior Finding | R2 Fix Applied | Verification Status | Residual Risk |
|---------------|----------------|---------------------|---------------|
| PM-001: No closure condition | Added "Issue Closure Condition" at line 767; Wave 2-5 marked "Tracked in child issue" | **RESOLVED** | None |
| PM-002: MCP ecosystem churn | Prose commitment preserved; ACs NOT updated with runbook requirement | **PARTIALLY RESOLVED** | HIGH -- runbook AC still missing from Acceptance Criteria |
| PM-003: Scope estimate undercount | Comparable reference added; "revise upward" signal present | **PARTIALLY RESOLVED** | MEDIUM -- Phase Gate AC not added; no written retrospective requirement |
| PM-004: Wave enforcement unmeasurable | WAVE-{N}-SIGNOFF.md mechanism added at lines 617, 842 | **RESOLVED mechanism; NEW GAP introduced** | MEDIUM -- signoff template content not specified in ACs |
| PM-005: Synthesis confidence gate enforcement | Override rate monitoring not added to ACs | **NOT RESOLVED** | HIGH -- monitoring AC still absent |
| PM-006: AI-First substitution dead end | Fixed to "Wave 5 delivers Design Sprint only; Service Blueprinting is V2 P1" at lines 383, 725 | **RESOLVED** | None |
| PM-007: Cross-sub-skill integration untested | AC wording unchanged ("handoffs tested for at least 2 canonical sequences") | **NOT RESOLVED** | HIGH -- no test specification added |
| PM-008: JTBD benchmark requires specialist | Replaced with 3-criterion deterministic rubric at line 797 | **RESOLVED** | None |
| PM-009: Research warning insufficient | Acknowledged as P2; no AC change | **NOT ADDRESSED (P2, acceptable)** | Low |
| PM-010: V2 trigger unowned | Acknowledged as P2; no AC change | **NOT ADDRESSED (P2, acceptable)** | Low |
| PM-011: Sprint solo adaptation unvalidated | Acknowledged as P2; no AC change | **NOT ADDRESSED (P2, acceptable)** | Low |

**Summary:** 4 of 8 P0/P1 findings fully resolved. 3 P0/P1 findings remain open. 1 new gap introduced by R2's WAVE-{N}-SIGNOFF.md fix. Proceeding with full Iter 3 prospective hindsight to identify remaining and newly introduced failure modes.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-20260303I3 | MCP maintenance runbook never created: PM-002 mitigation was documented in prose but never converted to an AC; no named owner, no runbook file exists at Wave 1 merge | Process | High | Critical | P0 | Completeness |
| PM-002-20260303I3 | WAVE-{N}-SIGNOFF.md template is unspecified: the enforcement mechanism is correct but the signoff template's required content is not defined; implementations produce incompatible signoff files that satisfy the file-existence check but contain different fields | Technical | High | Critical | P0 | Internal Consistency |
| PM-003-20260303I3 | Cross-sub-skill integration AC has no test specification: PM-007 from Iter 2 was not addressed; "handoffs tested for at least 2 canonical sequences" remains unverifiable because no input/output format or assertion is specified | Process | High | Major | P1 | Actionability |
| PM-004-20260303I3 | Synthesis confidence gate override monitoring has no named reviewer or response protocol: PM-005 from Iter 2 was not addressed; override log exists but who reviews it and what triggers a response is unspecified | Technical | High | Major | P1 | Methodological Rigor |
| PM-005-20260303I3 | Scope estimate Phase Gate AC was not added: PM-003 from Iter 2 was only partially addressed; the "revise upward" signal is present but the Wave 1 retrospective is not a named deliverable and no go/no-go gate exists before Wave 2 commitment | Resource | Medium | Major | P1 | Evidence Quality |
| PM-006-20260303I3 | KICKOFF-SIGNOFF.md template is referenced but its content is underspecified compared to WAVE-{N}-SIGNOFF.md: Wave 1 entry requires KICKOFF-SIGNOFF.md completion (line 609) with 5 defined fields, but the template's location is stated as `skills/user-experience/templates/kickoff-signoff-template.md` -- no AC requires this template to exist before issue closure | Process | Medium | Major | P1 | Completeness |
| PM-007-20260303I3 | The crisis mode 3-skill sequence has no defined duration, exit criteria, or escalation path: teams in crisis mode receive "Heuristic Eval -> Behavior Design -> HEART" but the orchestrator has no specification for when crisis mode ends, what output closes the crisis, or what to do if the 3-skill sequence does not resolve the UX problem | Technical | Medium | Minor | P2 | Actionability |
| PM-008-20260303I3 | Wave 4 entry criteria require Wave 3 outputs but Wave 3 requires Storybook and Figma MCPs: teams in the "Free" ($0/month) tier using only HEART, JTBD, Kano, and Behavior Design cannot satisfy Wave 3 entry criteria (requires Storybook instance), so Wave 4 is effectively inaccessible to the Free tier despite Behavior Design and Kano being Free-tier sub-skills | Assumption | Low | Minor | P2 | Internal Consistency |

---

## Detailed Findings

### PM-001-20260303I3: MCP Maintenance Runbook Never Created [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria -- MCP Integration Quality; Known Limitations -- Figma Single Point of Failure |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The Iter 2 PM-002 finding required that a named MCP maintenance owner be documented in SKILL.md and an `mcp-health-runbook.md` be created before Wave 1 merge. The R2 revision preserved the prose commitment in the Known Limitations section (line 599: "Quarterly MCP audit cadence with named maintenance owner") but did NOT add corresponding ACs to the MCP Integration Quality section. The MCP Integration Quality ACs (lines 816-822) specify pre-check behavior, degraded-mode behavior, enhancement MCP warnings, and Hotjar setup verification -- but contain no AC requiring: (a) a named maintenance owner in SKILL.md, or (b) an operational health runbook as a file artifact.

**Evidence:** Lines 816-822 (MCP Integration Quality ACs) contain 4 checkboxes. None references a runbook or named owner. Lines 598-600 reference "quarterly MCP audit cadence with named maintenance owner" as a design commitment. Line 743 references "quarterly MCP audit cadence with named maintenance owner" again. No AC maps either prose commitment to a verifiable artifact. The Known Limitations section also contains line 743: "The 3 highest Figma-dependent sub-skills (Atomic Design, Design Sprint, AI-First Design) must document explicit non-Figma fallback paths in their skill definitions before launch" -- but this requirement applies to Wave 3 and 5 sub-skills, not Wave 1. The Wave 1 Minimum Viable Launch ACs contain no fallback documentation requirement beyond the declarative "documented" language in sub-skill ACs.

**Analysis:** A quarterly audit with no named owner and no runbook file is purely aspirational. The Iter 2 PM-002 mitigation was specific: "Add two ACs to MCP Integration Quality: (1) named MCP maintenance owner documented in `skills/user-experience/SKILL.md`. (2) `skills/user-experience/rules/mcp-health-runbook.md` file exists at Wave 1 merge." Neither AC was added. In the retrospective: Figma restricted MCP access to paid tiers in Q3 2026 (consistent with their Dev Mode monetization history). The sub-skills degraded silently. Teams received MCP errors. No one had a runbook. No one had been assigned ownership. The fallback paths existed in the issue body but had never been operationalized.

**Recommendation:** Add to MCP Integration Quality ACs:
- `[ ] A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md` under a "Maintenance" section before Wave 1 merge. The owner is responsible for the quarterly audit cadence.`
- `[ ] A `skills/user-experience/rules/mcp-health-runbook.md` file is created before Wave 1 merge, containing at minimum: (a) MCP degradation detection procedure per server, (b) fallback activation steps per Required MCP failure, (c) user communication script for degraded state.`

**Acceptance Criteria:** Both ACs are present in the issue and produce verifiable file artifacts (SKILL.md maintenance section + runbook file). A third party can verify the runbook exists and follows the specified structure.

---

### PM-002-20260303I3: WAVE-{N}-SIGNOFF.md Template Content Unspecified [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria -- Wave Progression; Key Design Decisions -- Wave Deployment |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** R2 added the WAVE-{N}-SIGNOFF.md enforcement mechanism (lines 617, 842), which was the correct fix for Iter 2 PM-004. However, the mechanism has an implementation gap: the wave signoff template is declared to exist at `skills/user-experience/templates/wave-signoff-template.md` (line 617) but no AC requires this template file to exist before issue closure, and the template's required content (which fields must be present for the orchestrator to accept the file as a valid signoff) is not specified anywhere in the issue body. The orchestrator checks for file existence -- but if two implementations produce WAVE-2-SIGNOFF.md files with incompatible formats, wave enforcement becomes inconsistent.

**Evidence:** Line 617: "Template provided in `skills/user-experience/templates/wave-signoff-template.md`." Lines 840-844 (Wave Progression ACs): the AC at line 842 states "Wave entry enforcement: orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills" but does not require: (a) the template file to exist before closure, (b) the template's required fields to be specified, or (c) the orchestrator to validate the file's content vs. only its existence. Compare with the KICKOFF-SIGNOFF.md, which specifies 5 required fields at line 609 ("product name, target user population, current UX maturity self-assessment, available MCP tools, and team UX time allocation"). The WAVE-{N}-SIGNOFF.md has no equivalent field specification.

**Analysis:** A file-existence check is the weakest possible enforcement mechanism. If the signoff template is not shipped with the skill (because no AC requires it), the first implementer creates whatever fields they think are needed. The second implementer creates different fields. The orchestrator checks for file existence regardless of content. The enforcement degrades to a speed bump that teams bypass by creating an empty WAVE-2-SIGNOFF.md. The wave gating becomes theatrical rather than functional.

**Recommendation:**
1. Add the required content fields for WAVE-{N}-SIGNOFF.md to the Wave Progression section (mirror the KICKOFF-SIGNOFF.md pattern): "Each WAVE-{N}-SIGNOFF.md must contain: (a) evidence of entry criterion completion with specific output reference, (b) date of completion, (c) any bypass conditions active (or 'None'), (d) project owner acknowledgment."
2. Add a Wave Progression AC: `[ ] `skills/user-experience/templates/wave-signoff-template.md` is created and delivered as part of the Wave 1 implementation, containing the required field schema that all WAVE-{N}-SIGNOFF.md files must follow.`

**Acceptance Criteria:** The signoff template file is a named deliverable with specified content. The orchestrator validates file content against required fields, not just file existence. A WAVE-2-SIGNOFF.md produced by two different implementers contains the same required fields.

---

### PM-003-20260303I3: Cross-Sub-Skill Integration AC Has No Test Specification [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Parent Orchestrator |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** Iter 2 PM-007 identified that the cross-framework integration AC has no test specification. R2 did not address this finding. The AC at line 779 still reads: "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)." No input format, expected output property, or assertion is specified. "Tested" remains undefined.

**Evidence:** Line 779: "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)." The Relationship to Existing Jerry Skills section (lines 950-981) describes integration at the concept level only. The JTBD sub-skill outputs include "job statement synthesis" and the Design Sprint sub-skill uses a "challenge statement" as Day 1 input -- but the handoff specification between these (what format does the JTBD output take that becomes the Design Sprint input?) is not defined in the issue body. The job-statement-template.md and switch-interview-guide.md are listed as JTBD templates in the directory structure, but no sprint-input template is listed that would receive the JTBD output.

**Analysis:** In the retrospective: the JTBD -> Design Sprint handoff was "tested" by the implementing team via a single manual invocation. The JTBD agent produced a job statement in free-form prose. The Design Sprint facilitator accepted it as a challenge statement. No template schema connected the two outputs. When a different team tried to use the canonical sequence, their JTBD output format was different and the Design Sprint facilitator produced an inconsistent challenge statement. The "integration" was nominal, not functional.

**Recommendation:** Add a test specification inline or as a referenced artifact. Minimum: "Integration handoff test for JTBD -> Design Sprint: A JTBD job statement output (produced by ux-jtbd-analyst) is passed to ux-sprint-facilitator as the Day 1 challenge statement. The test passes when: (1) the challenge statement contains the JTBD job's functional dimension, (2) the challenge statement contains the JTBD job's emotional or social dimension, (3) the sprint agent does not require additional input to proceed to Day 2. Test is verified by manual review against `design-sprint-rules.md`. Apply equivalent specification to Lean UX -> HEART."

**Acceptance Criteria:** Each named canonical sequence has a written test specification as an inline AC table or referenced artifact. A third party who did not implement the sub-skills can execute the integration test from the specification alone.

---

### PM-004-20260303I3: Synthesis Confidence Gate Override Monitoring Has No Named Reviewer [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Post-Launch Success Metrics; Key Design Decisions -- Synthesis Hypothesis Validation |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** Iter 2 PM-005 required that the Post-Launch Success Metrics include a named reviewer for the override log and a response protocol for high override rates. R2 did not address this. The Post-Launch Success Metrics AC at line 853 tracks override rate but specifies only "monitoring only; high rates indicate the gate is working as designed." There is no named reviewer, no response protocol, and no threshold that triggers action.

**Evidence:** Line 853: "Track: synthesis hypothesis confidence gate override rate -- how often users invoke the Human Override Justification field on LOW-confidence outputs (target: monitoring only; high rates indicate the gate is working as designed)." The comment "high rates indicate the gate is working as designed" is a reframing that conflates gate awareness with gate effectiveness. If 90% of users override LOW-confidence outputs and proceed to product decisions, the gate is not working as designed -- it is being bypassed as designed. The automation bias acknowledgment at line 661 explicitly states that no template-level mechanism prevents this. But there is no feedback loop that would trigger a response.

**Analysis:** In the retrospective: within 3 months of Wave 1 launch, the override rate for LOW-confidence JTBD outputs reached 78%. The comment in the AC ("high rates indicate the gate is working as designed") led maintainers to treat this as expected behavior. No one reviewed whether the override decisions were documented with adequate justification. The Human Override Justification fields contained entries like "I know my users." The gate had become an auditable record of automation bias in action, not a mitigation for it.

**Recommendation:** Revise the override rate AC to: `[ ] Track: synthesis hypothesis confidence gate override rate (target: monitoring only for first 90 days; thereafter, override rate >= 50% for any LOW-confidence output type triggers a quarterly review by a named maintainer. Review produces one of: (a) revised confidence classification, (b) revised gate mechanism, (c) documented rationale for accepting the override rate as expected behavior.) Named reviewer: [assign before merge].`

**Acceptance Criteria:** The Post-Launch Success Metrics AC includes a threshold, a named reviewer role (not necessarily a specific person, but a role), and a response protocol. The response protocol specifies at least one action that can result from a high override rate.

---

### PM-005-20260303I3: Wave 1 Retrospective Is Not a Named Deliverable [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Estimated Scope |
| **Strategy Step** | Step 3 (Resource failures lens) |

**Failure Cause:** Iter 2 PM-003 required adding a Phase Gate AC requiring a Wave 1 retrospective document before committing to Wave 2+. R2 partially addressed PM-003 by retaining the "revise upward" signal in the Estimated Scope section, but the Phase Gate AC was not added. The Wave 1 retrospective is mentioned in the Estimated Scope text as a signal to watch but is not a named deliverable in the Acceptance Criteria section, not tracked as a worktracker entity, and not a prerequisite for Wave 2 commitment.

**Evidence:** Lines 1127-1133 (Estimated Scope section): "If Wave 1 completion (parent + 2 sub-skills, ~8-13 days) exceeds 15 days, the per-sub-skill estimates for subsequent waves should be revised upward." This is prose guidance, not an AC. The Acceptance Criteria section (lines 764-854) contains no AC for a Wave 1 retrospective. The Wave Progression ACs (lines 840-844) require wave signoff and wave tracking but no retrospective document. The Post-Launch Success Metrics section (lines 846-854) tracks quantitative metrics but does not specify a retrospective cadence.

**Analysis:** In the retrospective: Wave 1 took 24 days. The implementation team noted this was over the "revise upward" threshold. They revised their mental estimates informally. They did not produce a written retrospective. Wave 2 began after WAVE-1-SIGNOFF.md was completed. Wave 2 Miro integration took 7 days (vs. the 1-2 day estimate). At Wave 3, the scope had already drifted far beyond the 30-50 day estimate, but there was no formal gate to force reconsideration. The skill continued to be built because no checkpoint required a go/no-go decision.

**Recommendation:** Add to Wave Progression ACs: `[ ] A `work/retros/wave-1-retro.md` retrospective document is produced within 5 business days of WAVE-1-SIGNOFF.md completion. The retrospective contains: (a) actual vs. estimated delivery time per artifact, (b) MCP integration actual complexity vs. estimated complexity, (c) updated scope estimate for Waves 2-5 based on actual Wave 1 delivery rates, (d) go/no-go recommendation from the project owner for Wave 2 commitment. Wave 2 development does not begin until this retrospective is created and go/no-go is documented.`

**Acceptance Criteria:** The Wave 1 retrospective is an AC in the issue body. Its required content is specified. Wave 2 dependency on the retrospective is explicit.

---

### PM-006-20260303I3: KICKOFF-SIGNOFF.md Template Existence Not Required by ACs [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions -- Wave Deployment; Acceptance Criteria -- Wave Progression |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** Wave 1 entry requires completion of a `KICKOFF-SIGNOFF.md` file (line 609). The issue specifies the file's 5 required fields and references a template at `skills/user-experience/templates/kickoff-signoff-template.md`. However, unlike the JTBD job-statement-template.md (which is listed in the directory structure as a named deliverable), the `kickoff-signoff-template.md` is not listed in the directory structure, not included in any Wave 1 sub-skill AC as a required deliverable, and not referenced in the Wave Progression ACs. The Wave 1 entry criterion depends on a template that has no AC ensuring it exists.

**Evidence:** Line 609: "Template provided in `skills/user-experience/templates/kickoff-signoff-template.md`." Lines 1010-1113 (Directory Structure): the `user-experience/` parent skill directory lists `ux-routing-rules.md` and `synthesis-validation.md` as rules files, but no templates directory is listed for the parent skill. The sub-skill templates (job-statement-template.md, switch-interview-guide.md, etc.) are listed -- but the parent-level `kickoff-signoff-template.md` is absent. Lines 840-844 (Wave Progression ACs): the AC references "KICKOFF-SIGNOFF.md completion" but does not require the template to exist as a deliverable before issue closure.

**Analysis:** If the `kickoff-signoff-template.md` is not in the directory structure and not required by an AC, an implementation team reading the issue would likely create it if they notice the line 609 reference -- but it is not explicitly required. More critically, the Wave 1 entry criterion (KICKOFF-SIGNOFF.md completion) effectively gates every team's first use of the skill. If the template is wrong, missing, or inconsistently formatted, the first-run experience degrades. Teams who skip the kickoff step (because the template was hard to find or confusing) bypass Wave 1 entry criteria from the first session.

**Recommendation:** Add `kickoff-signoff-template.md` to the parent skill directory in the Directory Structure section. Add a Wave 1 AC: `[ ] `skills/user-experience/templates/kickoff-signoff-template.md` exists with the 5 required fields (product name, target user population, UX maturity self-assessment, available MCP tools, team UX time allocation) and is the canonical template referenced by the orchestrator's onboarding flow.`

**Acceptance Criteria:** The kickoff template is listed in the Directory Structure and required by an AC. A first-time user of the skill can find the template in the expected location.

---

### PM-007-20260303I3: Crisis Mode Has No Exit Criteria or Escalation Path [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions -- Parent Orchestrator Routes via Lifecycle-Stage Triage |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** The crisis mode 3-skill emergency sequence (Heuristic Eval -> Behavior Design -> HEART) is well-specified for activation (line 417: triggers on "urgent", "critical UX issue", "users are leaving", or multiple prior invocations without resolution). However, the specification defines no exit criteria: when does crisis mode end? What output constitutes crisis resolution? What does the orchestrator do if all 3 sub-skills have been invoked and the UX problem is still unresolved?

**Evidence:** Lines 415-417: "Crisis mode activates when the user explicitly describes urgency ('urgent', 'critical UX issue', 'users are leaving') or when the orchestrator detects multiple prior sub-skill invocations without resolution." The routing triage flowchart (lines 421-462) shows Crisis -> "3-skill emergency: Heuristic --> Behavior --> HEART" with no exit node. The intent resolution table (lines 465-476) shows `"CRISIS: urgent UX problems"` routes to "Emergency 3-skill sequence" with no qualification question. The Parent Orchestrator ACs (lines 769-779) include "Crisis mode 3-skill sequence (Heuristic Eval -> Behavior Design -> HEART) operational" -- but no test specification for crisis mode exit behavior.

**Analysis:** An emergency mode with no exit condition is a ghost ship. Users who invoke crisis mode and run all 3 sub-skills may still have an unresolved UX problem. The orchestrator's behavior at that point is undefined. Does it recommend Design Sprint? Does it escalate to a human? Does it loop back to Wave 1? The absence of an exit path is a minor design gap -- crisis mode will likely work well for the happy path but produce confusion at the edge case.

**Recommendation:** Add to the crisis mode specification: "Crisis mode concludes when: (a) the user explicitly acknowledges the crisis is resolved, OR (b) the 3-skill sequence produces a HEART metrics report showing improved values on the crisis-affected dimension. If neither condition is met after the 3-skill sequence, the orchestrator recommends Design Sprint as the next step for a structured solution exploration."

---

### PM-008-20260303I3: Free-Tier Teams Cannot Satisfy Wave 4 Entry Criteria [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions -- Wave Deployment; Cost Tiers |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** The cost tiers section (line 569) identifies 4 sub-skills available at the Free ($0/month) tier: HEART, JTBD, Kano, and Behavior Design. However, Kano (Wave 4) and Behavior Design (Wave 4) require completing Wave 3 entry criteria, which require: "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review." Both Wave 3 sub-skills (Atomic Design = Storybook Required MCP; Inclusive Design = Figma Required MCP) require paid MCP tiers. Free-tier teams cannot satisfy Wave 3 criteria and therefore cannot access Wave 4 -- despite Kano and Behavior Design being listed as Free-tier sub-skills.

**Evidence:** Wave Deployment table (line 613): Wave 4 entry criteria: "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review." Wave 3 sub-skills: Atomic Design (Storybook Required MCP) and Inclusive Design (Figma Required MCP). Cost tiers table (line 569): Free tier includes HEART, JTBD, Kano, Behavior Design -- but not Atomic Design or Inclusive Design (which require paid MCP tiers). The wave progression model requires Wave 3 completion before Wave 4 -- but Wave 3 requires paid tools that Free-tier teams cannot access.

**Analysis:** Free-tier teams are promised 4 sub-skills including 2 Wave 4 sub-skills. But they cannot satisfy the Wave 4 entry criteria without paid tools (Storybook + Figma). This is an internal inconsistency between the cost tier model and the wave progression model. The issue does not document a Wave 4 bypass path for Free-tier teams or acknowledge that Kano and Behavior Design are effectively inaccessible to teams without MCP tools. The impact is minor because most production teams will have at least Figma, but it creates a false promise for the "Solo practitioner" segment (line 76) described as a HIGH portfolio fit.

**Recommendation:** Add a note to the Wave Deployment table for Wave 4: "Free-tier teams (no Storybook or Figma) can satisfy Wave 4 entry criteria via bypass: document intent to acquire MCP tools within 30 days, or access Wave 4 directly via explicit user acknowledgment that Wave 3 criteria have been waived. The orchestrator supports this bypass via the standard wave stall bypass mechanism." Alternatively, revise the Wave 4 entry criteria to include a Free-tier path that does not require Storybook or Figma completion.

---

## Recommendations

### P0 -- Critical: MUST Mitigate Before Acceptance

**PM-001-20260303I3: Add MCP maintenance owner and health runbook ACs**
- Mitigation: Add two ACs to MCP Integration Quality: (1) "A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md` under a 'Maintenance' section before Wave 1 merge." (2) "A `skills/user-experience/rules/mcp-health-runbook.md` file is created before Wave 1 merge, containing: MCP degradation detection procedure per server, fallback activation steps per Required MCP failure, user communication script for degraded state."
- Acceptance criteria: Both ACs are in the issue body. The runbook file is a named deliverable that must exist at Wave 1 merge. The maintenance owner is documented in SKILL.md.

**PM-002-20260303I3: Specify WAVE-{N}-SIGNOFF.md required content and deliver the template as a Wave 1 AC**
- Mitigation: (1) Specify required content fields for WAVE-{N}-SIGNOFF.md inline in the Wave Deployment section (mirroring KICKOFF-SIGNOFF.md's field specification). (2) Add a Wave Progression AC: "`skills/user-experience/templates/wave-signoff-template.md` is created as part of Wave 1 delivery, containing the required field schema." (3) Update the orchestrator's validation behavior to check file content against required fields, not just file existence.
- Acceptance criteria: The signoff template is a named deliverable. Two different implementers producing WAVE-2-SIGNOFF.md files from the template produce files with the same required fields.

### P1 -- Important: SHOULD Mitigate

**PM-003-20260303I3: Add integration test specification for canonical sequences**
- Mitigation: Add a test specification table to the cross-framework integration AC. For JTBD -> Design Sprint: specify input format (canonical job statement), expected output property (challenge statement containing functional + emotional dimensions), and verification method (manual review against design-sprint-rules.md). Apply equivalent to Lean UX -> HEART.
- Acceptance criteria: Each named sequence has a minimum of 3 verifiable output properties in its test specification.

**PM-004-20260303I3: Add named reviewer role and response protocol to override monitoring AC**
- Mitigation: Revise override rate AC to include: (1) a threshold that triggers review (>= 50% override rate for 90+ days), (2) a named reviewer role (maintainer, not necessarily specific person), (3) a response protocol specifying at least one possible action.
- Acceptance criteria: The AC includes a threshold, a reviewer role, and a response protocol. The response protocol specifies at least one action that can result from a high override rate.

**PM-005-20260303I3: Add Wave 1 retrospective as a named deliverable and Wave 2 gate**
- Mitigation: Add to Wave Progression ACs: "`work/retros/wave-1-retro.md` is produced within 5 business days of WAVE-1-SIGNOFF.md. Required content: actual vs. estimated delivery rates, updated scope estimate, go/no-go recommendation. Wave 2 does not begin until the retrospective is created and go/no-go is documented."
- Acceptance criteria: The retrospective is an AC in the issue. Wave 2 dependency on the retrospective is explicit.

**PM-006-20260303I3: Add kickoff-signoff-template.md to Directory Structure and Wave 1 ACs**
- Mitigation: Add `skills/user-experience/templates/kickoff-signoff-template.md` to the Directory Structure section under the parent `user-experience/` directory. Add a Wave 1 AC requiring this template to exist before issue closure.
- Acceptance criteria: The kickoff template is in the Directory Structure. A first-time user can find it in the expected location.

### P2 -- Monitor

**PM-007-20260303I3:** Crisis mode exit criteria gap is minor. Add a post-crisis recommendation to the specification ("if 3-skill sequence completes without resolution, recommend Design Sprint"). No AC change required -- this can be addressed in the routing rules implementation.

**PM-008-20260303I3:** Free-tier Wave 4 entry criteria gap is minor. Acknowledge in the Wave Deployment table that the wave bypass mechanism accommodates Free-tier teams who cannot satisfy Storybook/Figma requirements. No AC restructuring required.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-001: MCP runbook is a prose commitment without an AC -- a critical operational requirement that cannot be verified at closure. PM-006: KICKOFF-SIGNOFF.md template is not a named deliverable despite being required for Wave 1 entry. |
| Internal Consistency | 0.20 | Negative | PM-002: WAVE-{N}-SIGNOFF.md enforcement mechanism is correct in intent but the template's required content is undefined, making the enforcement weaker than it appears. PM-008: Free-tier sub-skill promise (Kano, Behavior Design) contradicts Wave 4 entry criteria that require paid MCP tools. |
| Methodological Rigor | 0.20 | Negative | PM-004: The synthesis confidence gate's override monitoring has no feedback loop with a named reviewer or response threshold. The gate produces data but no protocol for acting on that data. PM-003: Cross-sub-skill integration testing remains unspecifiable -- "tested" without test criteria is not a quality gate. |
| Evidence Quality | 0.15 | Neutral | R2 resolved the major evidence quality gaps (WSM score corrections, scope estimate reference). PM-005 represents a remaining evidence gap: the scope estimate has a "revise upward" signal but no mechanism that forces revision before Wave 2 commitment. Neutral because R2 improvements offset the remaining gap. |
| Actionability | 0.15 | Negative | PM-003: The integration handoff AC cannot be acted on without a test specification. PM-006: An implementer reading the Wave 1 ACs would not know to create the kickoff template because no AC requires it. Two of the ACs require guesswork to implement. |
| Traceability | 0.10 | Positive | R2 significantly improved traceability: comment annotations trace every fix to its source strategy finding (e.g., `[R2-fix: PM-001]`, `[R2-fix: FM-002]`). All findings map clearly to deliverable sections with specific line references. The References section is complete and accurate. Traceability remains the strongest dimension. |

**Pre-Mortem Assessment: REVISE.** R2 has substantially improved the deliverable -- 4 of 8 prior P0/P1 findings are resolved, and the closure condition, wave enforcement mechanism, substitution path, JTBD benchmark, and pre-launch validation are genuine improvements. The remaining failure modes are not fundamental design flaws -- they are specification gaps that cluster in two areas: (1) operational commitments that live in prose but have no corresponding ACs, and (2) template deliverables that are referenced but not explicitly required. Two new Critical findings emerged from R2's own fixes (the WAVE-{N}-SIGNOFF.md template content gap was introduced by the fix to PM-004). If these 4 P0/P1 findings are addressed in R3, the issue should be positioned to clear the 0.92 quality threshold at the next S-014 scoring.

---

## Execution Statistics

- **Total Findings:** 8
- **Critical:** 2
- **Major:** 4
- **Minor:** 2
- **Protocol Steps Completed:** 6 of 6
- **Failure Category Coverage:** Technical (3), Process (3), Resource (1), Assumption (1) -- 4 of 5 lenses applied (External failures lens found no new External findings in Iter 3; R2 resolved the primary external risk via PM-002/PM-006 fixes)
- **Findings with P0 Priority:** 2 (PM-001-20260303I3, PM-002-20260303I3)
- **Findings with P1 Priority:** 4 (PM-003-20260303I3 through PM-006-20260303I3)
- **Findings with P2 Priority:** 2 (PM-007-20260303I3, PM-008-20260303I3)
- **Prior findings fully resolved by R2:** 4 (PM-001, PM-006, PM-008 from Iter 2; FM-002/DA-001 new fixes)
- **Prior findings partially addressed:** 2 (PM-002 prose retained but AC not added; PM-003 signal retained but Phase Gate AC not added)
- **Prior findings not addressed:** 2 (PM-005 override monitoring; PM-007 integration test specification)
- **New findings introduced by R2 fixes:** 1 (PM-002-20260303I3: WAVE-{N}-SIGNOFF.md template content gap)

---

*Strategy Execution Report -- S-004 Pre-Mortem Analysis*
*Template Version: 1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Executed: 2026-03-03*
*Agent: adv-executor*
