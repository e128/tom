# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context

- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 4 (R3 revision applied; Iteration 3 scored 0.761 REVISE)
- **H-16 Compliance:** S-003 Steelman applied in prior tournament chain (confirmed by Research Backing section referencing C4 adversarial tournament; prior strategy outputs include Steelman per tournament chain)
- **Criticality:** C4 (GitHub Enhancement issue for a framework skill addition -- architecture-level change touching mandatory-skill-usage.md, CLAUDE.md, AGENTS.md, ~67 artifacts; irreversible once merged and adopted)

---

# Pre-Mortem Report: `/user-experience` Skill Enhancement Issue

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `ux-skill-issue-body-saucer-boy.md` -- GitHub Enhancement issue, `/user-experience` skill, ~1163 lines
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004, Iteration 4)
**H-16 Compliance:** S-003 Steelman applied in prior tournament chain (confirmed)
**Failure Scenario:** It is September 2027. The `/user-experience` skill was merged in late March 2026. Wave 1 shipped on schedule. WAVE-1-SIGNOFF.md was completed. But adoption fell to a single active team by Month 6. The MCP Integration Runbook was created for individual sub-skills as required by the new AC (line 836) -- but no parent-level `mcp-health-runbook.md` was created because the AC only specified per-sub-skill runbooks, not a parent orchestrator runbook. When Figma restricted access in Q3 2026, 11 separate per-sub-skill runbooks described the degradation procedure but none had authority over the cross-cutting Figma dependency response. The WAVE-{N}-SIGNOFF.md template was delivered (directory structure lists it) but the Wave Progression ACs still do not require it to exist before issue closure. The cross-sub-skill integration AC at line 790 still has no test specification, so the two canonical sequences were "tested" via informal manual runs that did not verify specific output properties. The Wave 1 retrospective was never produced because no AC requires it. We are explaining failure after the fact, not predicting it.

---

## Summary

R3 applied 18 structural fixes that addressed genuine gaps: the MCP runbook was converted from prose to a named AC deliverable (PM-001 partially resolved -- per-sub-skill runbooks now required, but the parent-level runbook and named maintenance owner ACs are still absent from the Acceptance Criteria). The WAVE-{N}-SIGNOFF.md required fields were specified in the Key Design Decisions section (PM-002 partially resolved -- fields are now defined inline and the template is in the Directory Structure, but the Wave Progression ACs still do not require the template to exist as a closure deliverable). Three other structural R3 fixes (SR-002-I3 cross-framework synthesis AC, FM-004-I3 handoff data contract, SR-008-I3 template files in directory structure) added meaningful substance. However, the Pre-Mortem analysis from the retrospective frame of September 2027 surfaces 2 new Critical and 3 persistent Major findings. The MCP runbook AC (PM-001) was addressed at the sub-skill level but the parent-level coordination gap was not closed. The WAVE-{N}-SIGNOFF.md template requirement remains an incomplete fix. The integration test specification gap (PM-003) is persistent for the third iteration. The override monitoring gap (PM-004) was not addressed in R3. The Wave 1 retrospective gate (PM-005) was not added. The risk posture has improved from MEDIUM-HIGH (Iter 3) to MEDIUM -- but targeted revision is still required before this issue should be merged.

---

## Step 2: Temporal Perspective Shift

**Retrospective frame established:** It is September 2027. The issue was merged in March 2026. We are 18 months post-merge. Wave 1 shipped. WAVE-1-SIGNOFF.md was completed. Adoption plateaued. The Figma MCP access restriction in Q3 2026 produced fragmented responses because each sub-skill had its own runbook but no parent-level authority defined who coordinates a cross-skill Figma outage response. Integration tests for canonical sequences passed their informal "tested" criterion but failed to catch an output format incompatibility that only surfaced when a second team tried to run the JTBD -> Design Sprint sequence. Wave 2 stalled because the retrospective-gate AC was never added and no go/no-go decision was ever forced. We are explaining failure after the fact.

---

## R3 Fix Verification

| Prior Finding (Iter 3) | R3 Fix Applied | Verification Status | Residual Risk |
|------------------------|----------------|---------------------|---------------|
| PM-001-20260303I3: MCP maintenance runbook never created | Line 836: converted to named AC requiring per-sub-skill `mcp-runbook.md` with specified content | **PARTIALLY RESOLVED** | HIGH -- per-sub-skill runbooks added but parent-level `mcp-health-runbook.md` and named maintenance owner AC still absent from Acceptance Criteria |
| PM-002-20260303I3: WAVE-{N}-SIGNOFF.md template content unspecified | Lines 621-628: WAVE-{N}-SIGNOFF.md required fields (6 fields) specified inline; template added to Directory Structure (lines 1034-1036) | **PARTIALLY RESOLVED** | MEDIUM -- fields specified and template in directory structure, but Wave Progression ACs still do not require the template to exist before issue closure |
| PM-003-20260303I3: Cross-sub-skill integration AC has no test specification | Line 790: wording unchanged ("tested for at least 2 canonical sequences") | **NOT RESOLVED** | HIGH -- no test specification added; "tested" remains undefined for the third iteration |
| PM-004-20260303I3: Synthesis confidence gate override monitoring has no named reviewer | Lines 862-868: override rate metric unchanged ("monitoring only") | **NOT RESOLVED** | HIGH -- no threshold, no named reviewer, no response protocol added |
| PM-005-20260303I3: Wave 1 retrospective is not a named deliverable | No Wave 1 retrospective AC added to Wave Progression section | **NOT RESOLVED** | MEDIUM -- "revise upward" signal present but no Phase Gate AC exists |
| PM-006-20260303I3: KICKOFF-SIGNOFF.md template not in Directory Structure | Lines 1034-1036: `templates/` directory added to parent skill with both kickoff and wave signoff templates | **RESOLVED** | None |
| PM-007-20260303I3: Crisis mode has no exit criteria (P2) | Not addressed (P2, acceptable) | **NOT ADDRESSED (P2, acceptable)** | Low |
| PM-008-20260303I3: Free-tier Wave 4 entry criteria gap (P2) | Not addressed (P2, acceptable) | **NOT ADDRESSED (P2, acceptable)** | Low |

**Summary:** 1 of 5 P0/P1 findings fully resolved (PM-006). 2 findings partially addressed with structural improvement but incomplete ACs (PM-001, PM-002). 3 P0/P1 findings remain fully open (PM-003, PM-004, PM-005). Proceeding with Iter 4 prospective hindsight to identify remaining and potentially new failure modes.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-I4 | Parent-level MCP coordination authority is absent: per-sub-skill runbooks added (R3 fix) but no parent `mcp-health-runbook.md` and no named maintenance owner AC -- cross-skill MCP failures have no coordinating authority | Process | High | Critical | P0 | Completeness |
| PM-002-I4 | WAVE-{N}-SIGNOFF.md template not required as closure deliverable: fields now specified inline and template in directory structure, but Wave Progression ACs contain no checkbox requiring the template file to exist before issue closure | Technical | High | Critical | P0 | Internal Consistency |
| PM-003-I4 | Cross-sub-skill integration AC still has no test specification: "tested for at least 2 canonical sequences" unaltered for third iteration -- no input format, expected output properties, or verification method defined | Process | High | Major | P1 | Actionability |
| PM-004-I4 | Synthesis confidence gate override monitoring lacks named reviewer and response protocol: override rate tracked as "monitoring only" without threshold, reviewer role, or action trigger for three iterations | Technical | High | Major | P1 | Methodological Rigor |
| PM-005-I4 | Wave 1 retrospective absent as a Phase Gate: scope estimate "revise upward" signal present but no AC forces a go/no-go decision before Wave 2 commitment | Resource | Medium | Major | P1 | Evidence Quality |
| PM-006-I4 | MCP runbook AC scope is sub-skill only: line 836 requires per-sub-skill runbooks but the content specification omits parent-orchestrator coordination: who resolves a cross-skill MCP failure affecting Figma (4 sub-skills), Miro (2 sub-skills), or Storybook (1 sub-skill) simultaneously | Process | Medium | Major | P1 | Completeness |
| PM-007-I4 | Crisis mode exit criteria remain undefined: the flowchart at lines 428-467 has no exit node from the crisis path; no AC specifies when crisis mode concludes or what happens if the 3-skill sequence fails to resolve the UX problem | Technical | Medium | Minor | P2 | Actionability |
| PM-008-I4 | Free-tier Wave 4 entry criteria gap persists: Kano and Behavior Design are listed as Free-tier sub-skills but Wave 4 entry criteria require Storybook and Figma (Wave 3 tools), which are paid-MCP only | Assumption | Low | Minor | P2 | Internal Consistency |

---

## Detailed Findings

### PM-001-I4: Parent-Level MCP Coordination Authority Absent [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria -- MCP Integration Quality; Known Limitations -- Figma Single Point of Failure |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** R3 converted the MCP runbook from prose commitment to a named AC deliverable (line 836: "MCP Integration Runbook: Each MCP-dependent sub-skill includes an operational runbook (`skills/{sub-skill}/rules/mcp-runbook.md`)"). This is a genuine improvement. However, the AC scope is "Each MCP-dependent sub-skill" -- it creates 7 separate sub-skill-level runbooks (for Figma-dependent, Miro-dependent, Storybook-dependent sub-skills) but provides no parent-level coordination. Crucially, the AC also does not add the named maintenance owner requirement from Iter 3's recommendation -- "A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md`" was not added.

**Evidence:** Line 836 (MCP Integration Quality AC): the runbook specification scope is `skills/{sub-skill}/rules/mcp-runbook.md` -- sub-skill scoped. Lines 602-604: "Quarterly MCP audit cadence with named MCP maintenance owner" -- prose commitment, not an AC. Lines 751-754: "Quarterly MCP audit cadence with named maintenance owner" -- identical prose commitment in Known Limitations. Neither prose commitment maps to an AC checkbox requiring: (a) named maintenance owner documented in `skills/user-experience/SKILL.md`, or (b) a parent-level `skills/user-experience/rules/mcp-health-runbook.md` specifying cross-skill Figma/Miro/Storybook outage coordination. The MCP Integration Quality ACs (lines 831-836) now contain 5 checkboxes -- none requires a parent-level runbook or named owner.

**Analysis:** In the retrospective: the 7 sub-skill runbooks each described their own MCP fallback behavior. When Figma restricted access, the `/ux-heuristic-eval` runbook said "use screenshot mode." The `/ux-design-sprint` runbook said "use text-based prototyping." The `/ux-inclusive-design` runbook said "use manual contrast evaluation." No runbook said "Figma failure affects skills HE, DS, ID, AF and possibly AD, LU -- here is how the parent orchestrator coordinates degraded routing across all affected skills." The quarterly audit happened -- but no one had been assigned ownership of triggering it. The "named maintenance owner" remained a design aspiration rather than a documented role.

**Recommendation:** Add two ACs to MCP Integration Quality:
1. `[ ] A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md` under a "Maintenance" section before Wave 1 merge. The owner is responsible for the quarterly audit cadence and cross-skill failure coordination.`
2. `[ ] A `skills/user-experience/rules/mcp-health-runbook.md` (parent-level) is created before Wave 1 merge, containing: (a) cross-skill impact matrix when each Required MCP fails (which sub-skills degrade for Figma, Miro, Storybook failures), (b) parent orchestrator routing behavior during multi-skill degradation, (c) user communication script for multi-skill degraded state, (d) quarterly audit schedule and trigger criteria.`

**Acceptance Criteria:** Both ACs are in the issue body and produce verifiable file artifacts. The parent-level runbook is distinct from the per-sub-skill runbooks and covers cross-skill coordination.

---

### PM-002-I4: WAVE-{N}-SIGNOFF.md Template Not Required as Closure Deliverable [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria -- Wave Progression; Key Design Decisions -- Wave Deployment |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** R3 specified the WAVE-{N}-SIGNOFF.md required fields inline (lines 623: 6 required fields listed) and added `wave-signoff-template.md` to the Directory Structure (line 1036). This is a meaningful improvement over Iter 3. However, the Wave Progression ACs (lines 852-858) still do not include a checkbox requiring the template file to exist before issue closure. An implementation team reading the Wave Progression ACs would not find a requirement to deliver the template -- they would find a requirement to check for the file's existence at runtime, but not to create the template as a closure deliverable.

**Evidence:** Lines 623: WAVE-{N}-SIGNOFF.md required fields now specified (6 fields). Line 1036: `wave-signoff-template.md` listed in Directory Structure under parent skill templates. Lines 852-858 (Wave Progression ACs):
- Line 854: "Wave 1 entry criteria documented and enforced (KICKOFF-SIGNOFF.md completion)"
- Line 855: "Wave 2-5 entry criteria documented with bypass conditions for stall recovery"
- Line 856: "Wave entry enforcement: orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills"
- Line 857: "Wave bypass requires 3-field documentation..."
- Line 858: "Wave transitions tracked via `/worktracker` entities"

None of these ACs states: "The `skills/user-experience/templates/wave-signoff-template.md` file is created and delivered as part of Wave 1 implementation." Compare: the kickoff-signoff-template.md is now in the Directory Structure (line 1035) -- but similarly has no Wave Progression AC requiring it as a closure deliverable.

**Analysis:** The mechanism is now correctly specified (fields defined, template listed in directory structure) but is not enforced as a closure deliverable. The distinction matters: if the issue closes without the template file, the first implementation team must reconstruct the template from the 6-field specification at lines 623 rather than receiving a canonical template. Two teams building from the specification may produce subtly different templates. The orchestrator, which checks field existence not file identity, cannot detect the divergence.

**Recommendation:** Add to Wave Progression ACs:
`[ ] `skills/user-experience/templates/wave-signoff-template.md` is created and delivered as part of Wave 1 implementation, containing the 6 required fields specified in the Wave Deployment section. The template is the canonical file that all WAVE-{N}-SIGNOFF.md files are produced from. The orchestrator's content validation checks this template's field schema.`

**Acceptance Criteria:** The signoff template is an AC checkbox requiring a named file artifact. Issue closure requires the template to exist. A third party can verify the template contains the 6 required fields.

---

### PM-003-I4: Cross-Sub-Skill Integration AC Has No Test Specification [MAJOR] [PERSISTENT — 3rd Iteration]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Parent Orchestrator |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The AC at line 790 remains unchanged through three iterations: "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)." No test specification has been added. The R3 round added a cross-framework synthesis AC (line 791, `[R3-fix: SR-002-I3]`) and a parent-to-sub-skill handoff data contract (line 792, `[R3-fix: FM-004-I3]`). These are improvements to adjacent ACs -- but they do not address the integration test specification gap. The synthesis AC defines what the integration output should be (unified insight report); the handoff data contract defines what the orchestrator sends to sub-skills. Neither defines what properties of a JTBD -> Design Sprint handoff make the test pass.

**Evidence:** Line 790: "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART)" -- verbatim from R1 and R2 revisions. Line 791: new synthesis AC (`[R3-fix: SR-002-I3]`) -- defines that the parent skill produces a unified insight report, but this is a synthesis output, not an inter-sub-skill handoff test. Line 792: new handoff data contract (`[R3-fix: FM-004-I3]`) -- defines parent-to-sub-skill handoff fields (product context, selected sub-skill, prior outputs, quality gate threshold), but does not define the JTBD output format that feeds into Design Sprint Day 1.

The JTBD sub-skill outputs: "job statement synthesis, switch interview guide, competitive job analysis" (line 196). The Design Sprint sub-skill Day 1 input is a "challenge statement" (line 346). The gap between a JTBD job statement and a Design Sprint challenge statement is undefined. There is no template connecting them. The directory structure lists `job-statement-template.md` (line 1051) and no sprint challenge statement intake template.

**Analysis:** In the retrospective: two teams used the canonical JTBD -> Design Sprint sequence. Team A produced a JTBD job statement in the format "When [situation], I want to [motivation], so I can [outcome]." The Design Sprint facilitator accepted it as the Day 1 challenge statement directly. Team B's JTBD analyst produced a competitive job analysis with three job variants. The Design Sprint facilitator could not determine which job to use as the challenge statement. The "tested" AC had been satisfied by Team A's single successful run, but the test had no specification to catch Team B's failure mode. The integration was nominal, not functional.

**Recommendation:** Add a test specification inline or as a referenced artifact. Minimum required:
> Integration handoff test for JTBD -> Design Sprint: Given a JTBD job statement output from `ux-jtbd-analyst`, the `ux-sprint-facilitator` accepts it as the Day 1 challenge statement input. Test PASSES when: (1) challenge statement contains the job's functional dimension verbatim or paraphrased, (2) challenge statement contains the job's emotional or social dimension, (3) sprint facilitator proceeds to Day 2 without requesting additional input. Test is verified by manual review using `design-sprint-rules.md` as the rubric. Apply equivalent specification structure to Lean UX -> HEART.

**Acceptance Criteria:** Each named canonical sequence has a written test specification with at least 3 verifiable pass criteria. A third party who did not implement the sub-skills can execute the integration test from the specification alone.

---

### PM-004-I4: Synthesis Confidence Gate Override Monitoring Lacks Named Reviewer [MAJOR] [PERSISTENT — 3rd Iteration]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Post-Launch Success Metrics |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** The Post-Launch Success Metrics AC at line 867 remains unchanged: "Track: synthesis hypothesis confidence gate override rate -- how often users invoke the Human Override Justification field on LOW-confidence outputs (target: monitoring only; high rates indicate the gate is working as designed)." No named reviewer, no response threshold, no action protocol has been added through three iteration rounds. The comment "high rates indicate the gate is working as designed" conflates gate awareness with gate effectiveness, and this conflation has survived three rounds of adversarial review.

**Evidence:** Line 867: verbatim from Iter 3 and Iter 2 AC text. The synthesis hypothesis validation AC (lines 822-827) specifies the 3-tier gate mechanism but contains no monitoring or feedback loop. The override rate metric at line 867 is the only feedback mechanism -- and it has no action trigger. Compare with the quality standards AC at line 849: "Parent orchestrator quality gate uses S-014 scoring at wave transitions" -- the quality gate has a defined threshold (0.92) and a defined consequence (wave transition blocked). The override monitoring AC has no equivalent threshold or consequence.

**Analysis:** In the retrospective: 78% of LOW-confidence JTBD override decisions contained justifications like "I know my users" or "This is directional only." The monitoring log existed. No one reviewed it. The comment in the AC had been read as a design rationale by maintainers: "high rates indicate the gate is working as designed" was interpreted as "do nothing." The synthesis confidence gate became an auditable record of automation bias rather than a mechanism for detecting when the gate needed adjustment. The corrective action that was never taken: reviewing whether LOW-confidence outputs should be redesigned to better prevent uninformed overrides.

**Recommendation:** Revise the override rate AC to include three elements:
1. A threshold: "Override rate >= 50% for any LOW-confidence output type sustained for 90 days triggers a review."
2. A reviewer role: "Reviewer: named maintainer (person or role to be assigned before merge)."
3. A response protocol: "Review produces one of: (a) revised confidence classification for the output type, (b) revised gate mechanism (e.g., adding a mandatory delay or confirmation step), (c) documented rationale for accepting the override rate as expected behavior with evidence that overrides produce good product decisions."

**Acceptance Criteria:** The AC includes a threshold, a named reviewer role, and a response protocol. The response protocol specifies at least one action option. The "monitoring only" characterization is replaced with a structured response protocol.

---

### PM-005-I4: Wave 1 Retrospective Absent as Phase Gate [MAJOR] [PERSISTENT — 3rd Iteration]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Estimated Scope; Acceptance Criteria -- Wave Progression |
| **Strategy Step** | Step 3 (Resource failures lens) |

**Failure Cause:** The "revise upward" signal in the Estimated Scope section (lines 1143-1149) was retained through R3 and remains prose guidance rather than a Phase Gate AC. No Wave Progression AC requires a Wave 1 retrospective document to be produced before Wave 2 begins. This finding has been raised in Iter 2, Iter 3, and now Iter 4 without an AC being added. The R3 round focused fixes on structural additions (synthesis AC, handoff contract, template directory) but did not address the Wave 1 Phase Gate.

**Evidence:** Lines 1147-1149: "If Wave 1 completion (parent + 2 sub-skills, ~8-13 days) exceeds 15 days, the per-sub-skill estimates for subsequent waves should be revised upward. [Comparable delivery reference]. If Wave 1 completion exceeds 15 days, the per-sub-skill estimates for subsequent waves should be revised upward." Prose guidance with no enforcement. Lines 852-858 (Wave Progression ACs): 5 checkboxes. None requires a Wave 1 retrospective. None gates Wave 2 start on any retrospective or go/no-go decision.

**Analysis:** In the retrospective: Wave 1 took 22 days (vs. 8-13 day estimate). The team noted the overrun informally. No written retrospective was produced. No go/no-go decision was documented. Wave 2 began because WAVE-1-SIGNOFF.md was completed. Wave 2 took 18 days per sub-skill (vs. 2-4 day estimate). By Wave 3, the project was running at 5-8x original scope estimates. No checkpoint had ever forced a formal reconsideration. The issue is not that teams ignore overruns -- it is that no formal gate exists to make the reconsideration mandatory.

**Recommendation:** Add to Wave Progression ACs:
`[ ] A `work/retros/wave-1-retro.md` retrospective document is produced within 5 business days of WAVE-1-SIGNOFF.md completion. Required content: (a) actual vs. estimated delivery time per Wave 1 artifact, (b) MCP integration actual complexity vs. estimated complexity for each Required MCP, (c) updated scope estimate for Waves 2-5 based on actual Wave 1 delivery rates, (d) go/no-go recommendation from the project owner for Wave 2 commitment. Wave 2 development does not begin until this retrospective exists and the go/no-go decision is documented in it.`

**Acceptance Criteria:** The retrospective is an AC checkbox in the issue. Its required content is specified. Wave 2 dependency on the retrospective is explicit as a prerequisite.

---

### PM-006-I4: MCP Runbook AC Scope Is Sub-Skill Only -- Parent Coordination Gap [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- MCP Integration Quality |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The R3 fix at line 836 specifies per-sub-skill MCP runbooks with correct content (connection setup, authentication, fallback behavior, rate limit handling). This is an improvement. However, the scope of the AC is "Each MCP-dependent sub-skill" -- meaning the runbook artifact is `skills/{sub-skill}/rules/mcp-runbook.md`, one per sub-skill. This creates 7 separate runbooks. No AC requires the parent orchestrator to have a runbook that coordinates cross-skill MCP failures. This is a structural gap distinct from PM-001-I4 (which addresses the named maintenance owner and parent-level health runbook). PM-006-I4 addresses the content completeness of the parent coordination: when Figma fails, 4 sub-skills degrade simultaneously; no runbook documents how the orchestrator handles multi-skill degradation routing.

**Evidence:** Line 836: "MCP Integration Runbook: Each MCP-dependent sub-skill includes an operational runbook (`skills/{sub-skill}/rules/mcp-runbook.md`) with: connection setup steps, authentication method and credential management, fallback behavior when MCP server is unavailable, and rate limit handling with backoff strategy." The MCP dependency diagram (lines 529-546) maps: Figma Required -> HE, DS, ID, AF (4 sub-skills); Figma Enhancement -> AD, LU; Miro Required -> DS, LU; Storybook Required -> AD. A Figma outage creates a 4-sub-skill simultaneous degradation scenario. The parent orchestrator's behavior in this scenario is not specified by any AC.

The `mcp-runbook.md` per sub-skill would say "when Figma is unavailable, use screenshot mode." But the orchestrator is routing multiple users across multiple sub-skills. If a user has previously invoked `/ux-heuristic-eval` and is mid-session when Figma degrades, does the orchestrator switch the active session to screenshot mode? Does it warn about other potentially affected sub-skills the user might invoke next? No AC specifies this.

**Analysis:** The per-sub-skill runbooks address the scenario "I am using this sub-skill and its MCP goes down." They do not address "I am the orchestrator and 4 sub-skills' primary MCP just went down simultaneously." This is a genuine operational coordination gap that the sub-skill-scoped AC cannot close.

**Recommendation:** Revise the MCP Integration Runbook AC to include a parent-level component:
`[ ] `skills/user-experience/rules/mcp-health-runbook.md` (parent-level) is created before Wave 1 merge, containing: (a) cross-skill impact matrix -- for each Required MCP server (Figma, Miro, Storybook), which sub-skills degrade and in what mode; (b) parent orchestrator routing behavior when a Required MCP is unavailable -- which fallback sub-skills are available, what user communication is displayed; (c) multi-skill degradation handling when 2+ Required MCPs fail simultaneously; (d) quarterly audit trigger criteria and audit procedure.`

**Acceptance Criteria:** The parent-level runbook is distinct from the 7 sub-skill runbooks and addresses multi-skill degradation scenarios. The content specification covers items (a) through (d).

---

### PM-007-I4: Crisis Mode Has No Exit Criteria or Escalation Path [MINOR] [PERSISTENT]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions -- Parent Orchestrator Routes |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** The crisis mode 3-skill emergency sequence specification (lines 415-417, flowchart lines 428-467) has no exit node and no escalation path if the 3-skill sequence does not resolve the UX problem. This finding has been carried as P2/Minor since Iter 3 and remains unaddressed in R3.

**Evidence:** Lines 415-417: crisis mode activation criteria defined. Flowchart (lines 428-467): Crisis node routes to "3-skill emergency: Heuristic --> Behavior --> HEART" with no exit node. The intent resolution table (lines 469-481) shows `"CRISIS: urgent UX problems"` routes to "Emergency 3-skill sequence" with no qualification question and no stated endpoint.

**Recommendation:** Add post-crisis recommendation to crisis mode specification: "Crisis mode concludes when: (a) user explicitly acknowledges the UX crisis is resolved, OR (b) HEART metrics report shows improvement on the crisis-affected dimension. If neither condition is met after the 3-skill sequence completes, the orchestrator recommends Design Sprint as the structured next step for solution exploration."

---

### PM-008-I4: Free-Tier Teams Cannot Satisfy Wave 4 Entry Criteria [MINOR] [PERSISTENT]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions -- Wave Deployment; Cost Tiers |
| **Strategy Step** | Step 3 (Assumption failures lens) |

**Failure Cause:** The cost tier model (line 573) lists Kano and Behavior Design as Free-tier sub-skills ($0/month). Both are Wave 4. Wave 4 entry criteria require Wave 3 completion: "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review" -- both requiring paid MCP tools (Storybook, Figma). This internal inconsistency persists from Iter 3 without an acknowledgment or bypass path added to the Wave Deployment table.

**Evidence:** Cost tiers (line 573): Free tier includes Kano, Behavior Design. Wave 4 entry criteria (line 616): "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review." Wave 3 sub-skills (Atomic Design = Storybook Required; Inclusive Design = Figma Required) are not in the Free tier.

**Recommendation:** Add a bypass note to the Wave Deployment table for Wave 4: "Free-tier teams can satisfy Wave 4 entry via the wave stall bypass mechanism (document unmet criterion + impact assessment + remediation plan). The orchestrator supports this bypass per the existing 3-field bypass mechanism at line 857."

---

## Recommendations

### P0 -- Critical: MUST Mitigate Before Acceptance

**PM-001-I4: Add parent-level MCP health runbook and named maintenance owner ACs**
- Mitigation: Add two ACs to MCP Integration Quality section: (1) named MCP maintenance owner documented in `skills/user-experience/SKILL.md` before Wave 1 merge; (2) parent-level `skills/user-experience/rules/mcp-health-runbook.md` with cross-skill impact matrix, orchestrator routing behavior during multi-skill degradation, user communication, quarterly audit procedure.
- Acceptance criteria: Both ACs are checkbox items. The parent-level runbook is distinct from per-sub-skill runbooks and covers cross-skill coordination scenarios.

**PM-002-I4: Add WAVE-{N}-SIGNOFF.md template as a named Wave 1 closure deliverable**
- Mitigation: Add to Wave Progression ACs: "`skills/user-experience/templates/wave-signoff-template.md` is created as part of Wave 1 delivery, containing the 6 required fields specified in the Wave Deployment section. The template is canonical and must exist before issue closure."
- Acceptance criteria: The template is an AC checkbox. Issue cannot close without the template file existing with the required fields.

### P1 -- Important: SHOULD Mitigate

**PM-003-I4: Add test specification for canonical integration sequences**
- Mitigation: Add a test specification inline in the cross-framework integration AC. For JTBD -> Design Sprint: specify 3 verifiable pass criteria (functional dimension present, emotional/social dimension present, facilitator proceeds without additional input). Apply equivalent to Lean UX -> HEART.
- Acceptance criteria: Each named sequence has at least 3 verifiable pass criteria. A third party can execute the test without consulting the implementer.

**PM-004-I4: Add threshold, reviewer role, and response protocol to override monitoring AC**
- Mitigation: Revise line 867 to include: (a) 50% override rate threshold for 90+ days triggers review; (b) named reviewer role assigned before merge; (c) response protocol specifying at least one action option.
- Acceptance criteria: AC includes threshold, reviewer role, and response protocol. "Monitoring only" language is replaced.

**PM-005-I4: Add Wave 1 retrospective as named deliverable and Wave 2 gate**
- Mitigation: Add to Wave Progression ACs: `work/retros/wave-1-retro.md` produced within 5 business days of WAVE-1-SIGNOFF.md; required content specified; Wave 2 explicitly gated on retrospective completion.
- Acceptance criteria: Retrospective is an AC checkbox. Wave 2 dependency is explicit.

**PM-006-I4: Extend MCP runbook AC to require parent-level coordination runbook**
- Mitigation: Add parent-level `mcp-health-runbook.md` requirement to the MCP Integration Runbook AC, covering cross-skill impact matrix, orchestrator routing during multi-skill degradation, and quarterly audit procedure.
- Acceptance criteria: Parent-level runbook is a distinct artifact from sub-skill runbooks and addresses multi-skill scenarios.

### P2 -- Monitor

**PM-007-I4:** Add post-crisis recommendation (Design Sprint if 3-skill sequence fails to resolve). No AC change required -- can be addressed in routing rules implementation.

**PM-008-I4:** Add bypass note to Wave 4 entry criteria acknowledging Free-tier teams can use the existing wave stall bypass mechanism. Minimal AC change.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-001-I4 and PM-006-I4: The prose commitment to a named maintenance owner and parent-level coordination runbook survives into Iter 4 without AC enforcement. The per-sub-skill runbooks (R3 fix) are a real improvement but do not close the parent-coordination gap. Two prose commitments from two separate sections ("Quarterly MCP audit cadence with named maintenance owner" at lines 603, 752) remain unlinked to verifiable ACs. |
| Internal Consistency | 0.20 | Negative | PM-002-I4: WAVE-{N}-SIGNOFF.md fields are now specified (positive improvement) but the template is not required as a closure deliverable -- the enforcement mechanism still falls short of the specified fields. PM-008-I4: Free-tier promise vs. Wave 4 entry criteria inconsistency persists. |
| Methodological Rigor | 0.20 | Negative | PM-004-I4: The synthesis confidence gate's override monitoring has no feedback loop through three iterations. PM-003-I4: The integration test AC has no test specification through three iterations. Both failures represent methodology gaps that survived the R3 adversarial review. |
| Evidence Quality | 0.15 | Neutral | R3 added WSM scale disclosure (SR-005-I3), HEART synthesis hypothesis warning (FM-010-I3), and corrected cost tier label inversion (CV-001-I3). These are genuine improvements. PM-005-I4 represents the remaining evidence gap: the scope estimate "revise upward" signal has no enforcement gate. Net neutral given R3 improvements offsetting the persistent gap. |
| Actionability | 0.15 | Negative | PM-003-I4 and PM-005-I4 are both actionability gaps: the integration test AC cannot be acted on without a test specification; the Wave 1 retrospective AC cannot be satisfied because it does not exist. PM-006-I4 adds a new actionability concern: implementation teams reading the MCP runbook AC will create sub-skill runbooks without knowing a parent-level runbook is also needed. |
| Traceability | 0.10 | Positive | R3 maintained the comment annotation pattern (`[R3-fix: ...]-I3` tags). All R3 fixes are traceable to their source findings. The References section is complete. The Directory Structure now includes the template files. Traceability is the strongest dimension and continues to improve. |

**Pre-Mortem Assessment: REVISE.** R3 applied genuine structural improvements -- the MCP runbook conversion to an AC, the WAVE-{N}-SIGNOFF.md field specification, the template additions to the Directory Structure, and the cross-framework synthesis AC represent real progress. The issue has moved from MEDIUM-HIGH to MEDIUM risk. The remaining failure modes are narrower and more targeted than in prior iterations: 2 Critical findings (PM-001-I4, PM-002-I4) represent incomplete fixes that need AC additions, not design rethinks. 4 Major findings (PM-003-I4 through PM-006-I4) have been persistent across 2-3 iterations and are clearly not being addressed by the R3 fix pattern. R4 should apply targeted fixes to these 6 specific AC gaps. If R4 addresses all 6 P0/P1 findings, the deliverable should be positioned to clear the 0.92 S-014 threshold.

---

## Execution Statistics

- **Total Findings:** 8
- **Critical:** 2
- **Major:** 4
- **Minor:** 2
- **Protocol Steps Completed:** 6 of 6
- **Failure Category Coverage:** Technical (3), Process (3), Resource (1), Assumption (1) -- 4 of 5 lenses applied (External failures lens: no new external findings in Iter 4; Figma monetization risk is documented and mitigated in existing text)
- **Findings with P0 Priority:** 2 (PM-001-I4, PM-002-I4)
- **Findings with P1 Priority:** 4 (PM-003-I4 through PM-006-I4)
- **Findings with P2 Priority:** 2 (PM-007-I4, PM-008-I4)
- **Prior Iter 3 P0/P1 findings fully resolved by R3:** 1 (PM-006-20260303I3: KICKOFF-SIGNOFF.md template added to Directory Structure)
- **Prior Iter 3 P0/P1 findings partially addressed by R3:** 2 (PM-001: per-sub-skill runbooks added but parent-level missing; PM-002: fields specified and template in directory structure but no closure AC)
- **Prior Iter 3 P0/P1 findings not addressed by R3:** 3 (PM-003: integration test spec; PM-004: override monitoring; PM-005: Wave 1 retrospective gate)
- **New findings in Iter 4:** 1 (PM-006-I4: parent MCP coordination scope gap introduced by R3's sub-skill-scoped runbook AC)
- **Persistent P2 findings:** 2 (PM-007, PM-008 -- carried from Iter 3, P2 acceptable)

---

*Strategy Execution Report -- S-004 Pre-Mortem Analysis*
*Template Version: 1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Executed: 2026-03-03*
*Agent: adv-executor*
