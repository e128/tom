# Strategy Execution Report: Pre-Mortem Analysis

## Execution Context

- **Strategy:** S-004 (Pre-Mortem Analysis)
- **Template:** `.context/templates/adversarial/s-004-pre-mortem.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 5 (R4 revision applied; Iteration 4 scored 0.835 REVISE)
- **H-16 Compliance:** S-003 Steelman applied in prior tournament chain (confirmed by Research Backing section referencing C4 adversarial tournament; Steelman in prior strategy outputs)
- **Criticality:** C4 (GitHub Enhancement issue for a framework skill addition -- architecture-level change touching mandatory-skill-usage.md, CLAUDE.md, AGENTS.md, ~67 artifacts; irreversible once merged and adopted)

---

# Pre-Mortem Report: `/user-experience` Skill Enhancement Issue

**Strategy:** S-004 Pre-Mortem Analysis
**Deliverable:** `ux-skill-issue-body-saucer-boy.md` -- GitHub Enhancement issue, `/user-experience` skill, ~1236 lines
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-004, Iteration 5)
**H-16 Compliance:** S-003 Steelman applied in prior tournament chain (confirmed)
**Failure Scenario:** It is October 2027. The `/user-experience` skill was merged in April 2026. Wave 1 shipped on schedule and WAVE-1-SIGNOFF.md was committed. The Wave 1 retrospective was never produced because no AC required it -- Wave 2 began the day after WAVE-1-SIGNOFF.md committed. 18 months later, Wave 2 and Wave 3 are running but the override monitoring system has logged 340 LOW-confidence JTBD output overrides, all with justifications that amount to "we know our users." No reviewer was ever assigned. No one knows if the confidence gate is working as designed or being systematically circumvented by teams who find it annoying. The named MCP maintenance owner was never documented in `skills/user-experience/SKILL.md` because that AC was never added to the issue. The cross-sub-skill integration "tested" AC was satisfied by running both sub-skills on the same product context -- but the test had no specified pass criteria, so Team B's incomplete JTBD output was accepted as passing because the synthesis report was produced. We are explaining failure after the fact.

---

## Summary

R4 applied 11 targeted fixes that addressed meaningful structural gaps. WAVE-{N}-SIGNOFF.md is now a named closure deliverable (PM-002-I4 resolved). The cross-framework integration definition of "tested" was narrowed (PM-003-I4 partially resolved). Parent orchestrator MCP connection registry was added (PM-006-I4 partially resolved). Four new ACs were added covering orchestrator failure modes, P-003 CI enforcement, sub-skill-to-sub-skill handoff schema, and Human Override Audit log. However, the Pre-Mortem analysis from the retrospective frame of October 2027 surfaces 1 persistent Critical finding and 3 persistent Major findings. The named MCP maintenance owner AC was not added (PM-001-I5: Critical, persistent). The integration test specification still has no verifiable pass criteria despite the "tested" definition narrowing (PM-003-I5: Major, persistent for 4th iteration). The override monitoring AC still has no threshold, reviewer, or response protocol (PM-004-I5: Major, persistent for 4th iteration). The Wave 1 retrospective gate is still absent (PM-005-I5: Major, persistent for 4th iteration). The risk posture has improved from MEDIUM to LOW-MEDIUM, but these four findings represent process architecture gaps that will not self-correct after merge.

---

## Step 2: Temporal Perspective Shift

**Retrospective frame established:** It is October 2027. The issue was merged in April 2026. We are 18 months post-merge. Wave 1 shipped. WAVE-1-SIGNOFF.md was committed as a closure deliverable (the R4 fix worked as designed). Wave 2 began without a retrospective. Override monitoring collected data for 18 months. No one reviewed it. The named MCP maintenance owner was never documented because that AC was never required. The integration test passed on the first run but failed to catch format divergence on the second team's run because no pass criteria were specified. We are explaining failure after the fact, not predicting it.

---

## R4 Fix Verification

| Prior Finding (Iter 4) | R4 Fix Applied | Verification Status | Residual Risk |
|------------------------|----------------|---------------------|---------------|
| PM-001-I4: Parent-level MCP coordination authority absent | Line 853: `[R4-fix: PM-001-I4]` added "Parent Orchestrator MCP Coordination" AC -- unified MCP connection registry, pre-check on sub-skill invocation, route to fallback | **PARTIALLY RESOLVED** | MEDIUM -- the unified registry AC is present and requires the orchestrator to pre-check and route gracefully. However, the named MCP maintenance owner AC (require documentation in `skills/user-experience/SKILL.md`) was NOT added. Lines 615, 767: "Quarterly MCP audit cadence with named maintenance owner" remains prose commitment without a corresponding AC checkbox. |
| PM-002-I4: WAVE-{N}-SIGNOFF.md template not required as closure deliverable | Line 874: `[R4-fix: PM-002-I4]` -- "Each wave's WAVE-N-SIGNOFF.md is a closure deliverable -- wave completion is not recognized until the signoff file passes schema validation (all required fields non-empty) and is committed to the repository" | **RESOLVED** | None -- the AC is now a verifiable checkbox requiring a committed file artifact before wave completion is recognized. Schema validation requirement closes the enforcement gap. |
| PM-003-I4: Cross-sub-skill integration AC has no test specification | Line 805: `[R4-fix: SR-002-I4]` -- defined "tested" as "validated by running both sub-skills on the same product context and confirming the synthesis report correctly identifies convergent and divergent recommendations" | **PARTIALLY RESOLVED** | HIGH -- "tested" now has a method (run both on same product context + synthesis report check), but still has no verifiable pass criteria. The synthesis report must "correctly identify convergent and divergent recommendations" -- but "correctly" is undefined. No minimum number of convergent/divergent points, no rubric, no third-party verifiability. |
| PM-004-I4: Synthesis confidence gate override monitoring lacks named reviewer and response protocol | Line 885: unchanged -- "monitoring only; high rates indicate the gate is working as designed" | **NOT RESOLVED** | HIGH -- the Human Override Audit AC (line 686, `[R4-fix: RT-004-I4]`) was added but addresses the AUDIT LOG mechanism (4-field structured record per override). This is a data collection improvement, not the monitoring REVIEW + THRESHOLD + RESPONSE PROTOCOL gap. The override rate metric at line 885 is still "monitoring only" with no threshold, no reviewer, no action trigger. |
| PM-005-I4: Wave 1 retrospective absent as Phase Gate | Lines 869-876: Wave Progression ACs -- no Wave 1 retrospective AC added | **NOT RESOLVED** | MEDIUM -- four iterations without this AC being added. Wave Progression section now has 6 ACs (PM-002-I4 fix added the closure deliverable requirement) but still no retrospective gate before Wave 2 start. |
| PM-006-I4: MCP runbook AC scope is sub-skill only | Line 853: `[R4-fix: PM-001-I4]` added the registry mechanism; Cross-Session State section (lines 1219-1223) added `mcp-registry` Memory-Keeper key | **SUBSTANTIALLY RESOLVED** | LOW -- the unified MCP connection registry AC (line 853) covers orchestrator-level MCP awareness. The `mcp-registry` Memory-Keeper key (line 1221) specifies cross-session persistence of MCP active/inactive status per sub-skill. The explicit multi-skill degradation routing instruction is embedded in the AC ("routes to fallback behavior (graceful degradation to non-MCP workflow) if unavailable"). The parent-level `mcp-health-runbook.md` artifact was not added, but the orchestrator-level coordination mechanism is now AC-enforced. Residual gap: no explicit multi-skill simultaneous degradation scenario (2+ MCPs fail at once) is addressed. |
| PM-007-I4: Crisis mode has no exit criteria (P2) | Not addressed (P2, acceptable) | **NOT ADDRESSED (P2, acceptable)** | Low |
| PM-008-I4: Free-tier Wave 4 entry criteria gap (P2) | Not addressed (P2, acceptable) | **NOT ADDRESSED (P2, acceptable)** | Low |

**Summary:** 1 of 5 P0/P1 findings fully resolved (PM-002-I4). 1 finding substantially resolved with meaningful progress (PM-006-I4, moved to P2 monitoring). 1 finding partially addressed but incomplete (PM-003-I4). 2 P0/P1 findings remain fully open (PM-004-I4, PM-005-I4). 1 Critical finding partially addressed (PM-001-I4). Proceeding with Iter 5 prospective hindsight.

---

## Findings Table

| ID | Failure Cause | Category | Likelihood | Severity | Priority | Affected Dimension |
|----|---------------|----------|------------|----------|----------|--------------------|
| PM-001-NNN-I5 | Named MCP maintenance owner never documented: line 853 added the registry mechanism AC but the named owner AC ("A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md` before Wave 1 merge") was not added -- prose commitment at lines 615 and 767 remains unenforced | Process | High | Critical | P0 | Completeness |
| PM-002-NNN-I5 | Cross-sub-skill integration "tested" definition lacks verifiable pass criteria: line 805 defines "tested" as method (run both sub-skills on same product context + synthesis report check) but "correctly identifies convergent and divergent recommendations" is undefined -- no count, no rubric, no third-party verifiability | Process | High | Major | P1 | Actionability |
| PM-003-NNN-I5 | Synthesis confidence gate override monitoring still has no threshold, reviewer, or response protocol: the Human Override Audit AC (line 686) adds 4-field structured logging but the override rate metric (line 885) remains "monitoring only" with no action trigger for four consecutive iterations | Technical | High | Major | P1 | Methodological Rigor |
| PM-004-NNN-I5 | Wave 1 retrospective is still not a named deliverable: the Wave Progression ACs (lines 869-876) have 6 checkboxes after the R4 additions but none requires a retrospective document before Wave 2 begins -- this finding has been raised in Iter 2, Iter 3, Iter 4, and now Iter 5 | Resource | Medium | Major | P1 | Evidence Quality |
| PM-005-NNN-I5 | Multi-skill simultaneous MCP degradation not specified: the registry AC (line 853) addresses single-skill MCP failures but does not specify orchestrator behavior when 2+ Required MCPs fail simultaneously (Figma + Miro both unavailable affects Wave 2 and Wave 3 simultaneously) | Technical | Low | Minor | P2 | Completeness |
| PM-006-NNN-I5 | Override audit log has no retention or review policy: the Human Override Audit AC (line 686) specifies 4-field structured logging to `work/audit/override-log.md` but no AC or policy specifies how long the log is retained, when it is reviewed, or what happens when it grows beyond a manageable size | Process | Low | Minor | P2 | Actionability |

---

## Detailed Findings

### PM-001-NNN-I5: Named MCP Maintenance Owner Never Documented [CRITICAL] [PERSISTENT -- 2nd Iteration]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria -- MCP Integration Quality; Known Limitations -- Figma Single Point of Failure |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** R4 added a meaningful structural improvement: the "Parent Orchestrator MCP Coordination" AC at line 853 requires the `ux-orchestrator` agent to maintain a unified MCP connection registry, pre-check MCP availability on sub-skill invocation, and route to fallback gracefully. This addresses the operational behavior gap. However, Iter 4's PM-001-I4 recommendation specified two ACs: (1) the registry mechanism (now added) AND (2) "A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md` before Wave 1 merge." The second AC was not added. The Iter 4 finding was classified as Critical precisely because the combination of operational behavior (the registry) and governance accountability (the named owner) are both required to prevent the failure scenario. The operational behavior without the governance accountability still leaves a coordination vacuum.

**Evidence:** Lines 615-616 (MCP Integration section): "Quarterly MCP audit cadence with named MCP maintenance owner. Penpot MCP (currently experimental) monitored as an open-source alternative path." Lines 766-768 (Known Limitations -- Figma Single Point of Failure): "Quarterly MCP audit cadence with named maintenance owner." Both are prose commitments, not AC checkboxes. The MCP Integration Quality ACs (lines 845-853) now contain 6 checkboxes -- the 6th (line 853) requires the registry mechanism. None requires: "A named MCP maintenance owner is documented in `skills/user-experience/SKILL.md` before Wave 1 merge."

**Analysis:** In the retrospective: the MCP connection registry worked correctly. When Figma went down, the orchestrator detected it and routed users to screenshot mode automatically. The engineering was sound. However, 18 months after launch, no one had run the quarterly MCP audit because no one had been assigned ownership of running it. The "named maintenance owner" was discussed during design but never formalized. When Miro's API pricing changed in Q4 2026, the discovery happened by accident (a user filed a bug report) rather than by the quarterly audit that the prose commitment described. The registry detected the failure state; no one was accountable for the audit that should have anticipated it.

**Recommendation:** Add one AC to MCP Integration Quality:
`[ ] A named MCP maintenance owner (person or role) is documented in `skills/user-experience/SKILL.md` under a "Maintenance Ownership" section before Wave 1 merge. The owner is responsible for: (a) triggering the quarterly audit of MCP operational constraint values in the MCP Operational Constraints table, (b) coordinating cross-skill response when a Required MCP changes pricing, schema, or access policy, (c) updating the unified MCP connection registry entries when API changes are detected.`

**Acceptance Criteria:** The AC is a checkbox. The `SKILL.md` Maintenance Ownership section is a verifiable file artifact. Issue cannot close without the named owner documented. A third party can verify the section exists with the required content.

---

### PM-002-NNN-I5: Integration "Tested" Definition Lacks Verifiable Pass Criteria [MAJOR] [PERSISTENT -- 4th Iteration]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Parent Orchestrator |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** R4 narrowed the definition of "tested" at line 805: "validated by running both sub-skills on the same product context and confirming the synthesis report correctly identifies convergent and divergent recommendations." This is a genuine improvement over "tested" without any definition. The method is now specified (run both, check synthesis report). However, "correctly identifies convergent and divergent recommendations" remains undefined. The test still has no minimum count (how many convergent/divergent items?), no rubric (what makes an identification "correct"?), no third-party verifiability (can a third party who did not implement the sub-skills execute and grade this test?).

**Evidence:** Line 805: "Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART) -- tested = validated by running both sub-skills on the same product context and confirming the synthesis report correctly identifies convergent and divergent recommendations `[R4-fix: SR-002-I4]`." The issue still does not specify: What is the minimum number of convergent recommendations? What counts as "correctly identifies" -- agreement with a reference output, achievement of a scoring threshold, or expert review? The JTBD sub-skill outputs a "job statement synthesis, switch interview guide, competitive job analysis" (line 206). The Design Sprint sub-skill's Day 1 input is a "challenge statement" (line 362). The gap template connecting JTBD job statements to Design Sprint challenge statements is listed in Directory Structure (line 1072: `job-statement-template.md`) but no template exists for the inverse direction (Design Sprint challenge statement derived from JTBD output). The integration test cannot verify the handoff is working without knowing what the JTBD -> Design Sprint handoff should produce.

**Analysis:** In the retrospective: Team A ran JTBD and then Design Sprint on the same product. The synthesis report identified 2 convergent points and 1 divergent point. They marked the AC as passed. Team B ran the same sequence. The synthesis report identified 1 convergent point and 4 divergent points. They marked it passed. These two teams experienced fundamentally different outcomes from the same sequence, but both passed the same AC because "correctly identifies convergent and divergent recommendations" had no minimum count or rubric. The test was formally satisfied; the integration behavior was not validated.

**Recommendation:** Specify verifiable pass criteria for each named canonical sequence. For JTBD -> Design Sprint:
> Integration test PASSES when: (1) the synthesis report references the JTBD job statement's functional dimension in the Design Sprint challenge statement (verbatim or paraphrased), (2) the synthesis report identifies at least 1 convergent recommendation (something both frameworks recommend), (3) the synthesis report identifies at least 1 divergent recommendation (something one framework recommends that the other does not), (4) the `ux-sprint-facilitator` proceeds to Day 2 without requesting additional JTBD input. Test is graded by manual review using a blind rubric; a third party who did not implement the sub-skills can execute the test. Apply equivalent 4-criterion structure to Lean UX -> HEART.

**Acceptance Criteria:** Each named sequence has at least 4 verifiable pass criteria. A third party who did not implement the sub-skills can execute and grade the test from the criteria alone.

---

### PM-003-NNN-I5: Override Monitoring Has No Threshold, Reviewer, or Response Protocol [MAJOR] [PERSISTENT -- 4th Iteration]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Post-Launch Success Metrics |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** The Human Override Audit AC (line 686, `[R4-fix: RT-004-I4]`) added structured 4-field logging to `work/audit/override-log.md`. This is a meaningful improvement: overrides are now formally recorded with timestamp, user, original value, and justification text. However, the Post-Launch Success Metrics AC at line 885 remains unchanged: "Track: synthesis hypothesis confidence gate override rate -- how often users invoke the Human Override Justification field on LOW-confidence outputs (target: monitoring only; high rates indicate the gate is working as designed)." The audit log collects data; the metric AC still has no mechanism for acting on that data. The distinction is critical: collecting structured override data without reviewing it at a threshold is the equivalent of installing a smoke detector with no alarm output.

**Evidence:** Line 885: verbatim from Iter 2, Iter 3, and Iter 4 AC text. Line 686 (new `[R4-fix: RT-004-I4]`): "Human Override Audit: Every P-020 override of wave gates or confidence thresholds is logged with: (a) override timestamp, (b) overriding user, (c) original gate/threshold value, (d) justification text (free-form, minimum 20 characters). Audit log persisted to `work/audit/override-log.md`." The audit AC at line 686 specifies data collection. The metric AC at line 885 specifies "monitoring only." The gap: neither AC specifies who monitors, at what frequency, against what threshold, or what action is triggered.

**Analysis:** In the retrospective: the override log grew to 340 entries. Every entry was structured with the 4 required fields. The data quality was excellent. The problem: the log was a write-only system. It was never read. The "monitoring only" characterization in the AC had been read by maintainers as a design rationale -- "this is just for information, high rates are expected." The log revealed a pattern (78% of LOW-confidence JTBD overrides used "I know my users" justifications shorter than 50 characters, indicating the 20-character minimum was too low to enforce meaningful justification) that was never acted on. The confidence gate became an auditable circumvention mechanism rather than a quality enforcement tool.

**Recommendation:** Revise line 885 to include three elements:
1. A threshold: "Override rate >= 50% for any LOW-confidence output type, sustained over a rolling 90-day window, triggers a mandatory review."
2. A reviewer: "Reviewer: the named MCP maintenance owner (per MCP Integration Quality AC) is also responsible for monthly override log review."
3. A response protocol: "Review produces one of: (a) revised confidence classification if overrides consistently produce good decisions; (b) revised gate mechanism (e.g., increase minimum justification length, add confirmation step); (c) documented acceptance rationale if override rate is expected behavior with evidence that overrides produce good product decisions within 30 days. Response is documented in `work/audit/override-review-log.md`."

**Acceptance Criteria:** The AC includes a threshold, a named reviewer (linked to the MCP maintenance owner), and a response protocol. The "monitoring only" characterization is replaced with a structured review and response mechanism.

---

### PM-004-NNN-I5: Wave 1 Retrospective Still Absent as Phase Gate [MAJOR] [PERSISTENT -- 4th Iteration]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Wave Progression; Estimated Scope |
| **Strategy Step** | Step 3 (Resource failures lens) |

**Failure Cause:** The Wave Progression ACs (lines 869-876) now have 6 checkboxes after the R4 additions (line 874 added the WAVE-{N}-SIGNOFF.md closure deliverable requirement). This is a genuine improvement. However, none of the 6 Wave Progression ACs requires a Wave 1 retrospective document before Wave 2 begins. The "revise upward" signal in Estimated Scope (line 1168) is still prose guidance without enforcement. This finding has been raised in Iter 2, Iter 3, Iter 4, and now Iter 5 -- four consecutive iterations -- without a retrospective gate AC being added.

**Evidence:** Lines 869-876 (Wave Progression ACs): 6 checkboxes covering entry criteria, enforcement, bypass, and worktracker tracking. None requires: (a) a retrospective document after Wave 1 completion, (b) actual vs. estimated delivery time comparison, or (c) go/no-go decision before Wave 2. Line 1168: "If Wave 1 completion (parent + 2 sub-skills, ~8-13 days) exceeds 15 days, the per-sub-skill estimates for subsequent waves should be revised upward." Prose guidance, no enforcement gate.

**Analysis:** In the retrospective: Wave 1 took 22 days (vs. 8-13 estimate). WAVE-1-SIGNOFF.md was committed (per the R4-fixed AC). Wave 2 began the next day. No retrospective was produced because no AC required it. The "revise upward" signal in the prose was read by the implementing team -- but no one had the authority or mandate to stop Wave 2 and force a scope reassessment. Wave 2 took 18 days per sub-skill (vs. 2-4 day estimate). Wave 3 is still ongoing at the time of this retrospective, running at 6x original scope estimates. The WAVE-{N}-SIGNOFF.md closure deliverable requirement (R4 fix) is valuable -- it prevents wave completion from being claimed informally. It does not prevent the next wave from starting immediately after the SIGNOFF.md is committed, with no structured reflection on what the SIGNOFF revealed.

**Recommendation:** Add to Wave Progression ACs:
`[ ] A `work/retros/wave-1-retro.md` retrospective document is produced within 5 business days of WAVE-1-SIGNOFF.md completion. Required content: (a) actual vs. estimated delivery time per Wave 1 artifact, (b) MCP integration actual complexity vs. estimated complexity for each Required MCP, (c) updated scope estimate for Waves 2-5 based on actual Wave 1 delivery rates, (d) go/no-go recommendation from the project owner for Wave 2 commitment. Wave 2 sub-skill development does not begin until this retrospective exists and the go/no-go decision is documented.`

**Acceptance Criteria:** The retrospective is an AC checkbox in the Wave Progression section. Its required content is specified. Wave 2 dependency on the retrospective is explicit. A third party can verify the retrospective exists with the 4 required content sections.

---

### PM-005-NNN-I5: Multi-Skill Simultaneous MCP Degradation Not Specified [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Acceptance Criteria -- MCP Integration Quality |
| **Strategy Step** | Step 3 (Technical failures lens) |

**Failure Cause:** The registry AC (line 853) specifies orchestrator behavior for single-skill MCP failures: "pre-checks MCP availability and routes to fallback behavior (graceful degradation to non-MCP workflow) if unavailable." This covers the case where one sub-skill's Required MCP is unavailable. It does not specify behavior when 2+ Required MCPs fail simultaneously. Figma Required (HE, DS, ID, AF) and Miro Required (DS, LU) overlap on Design Sprint: a Figma + Miro simultaneous outage means Design Sprint has no primary MCP and its Miro-only fallback (listed in the Figma dependency risk section) also fails.

**Evidence:** Line 853: "on sub-skill invocation, the orchestrator pre-checks MCP availability and routes to fallback behavior (graceful degradation to non-MCP workflow) if unavailable." The Figma fallback table (lines 608-612) lists: Design Sprint fallback = "Miro-only mode (sprint exercises in Miro; manual prototype reference)." Miro's rate limits and failure codes are listed in the MCP Operational Constraints table (line 597). No text specifies what the orchestrator does when both Figma and Miro are unavailable for Design Sprint. The registry tracks "active/inactive status" per MCP but does not specify what happens when both MCPs for a single sub-skill are inactive.

**Recommendation:** Add a note to the MCP Integration Runbook AC or the registry AC: "Multi-MCP failure handling: when a sub-skill's Required MCP and its MCP-based fallback are both inactive, the orchestrator routes to the text-based/screenshot fallback and notifies the user with a specific message identifying which MCPs are unavailable and which manual path is available."

---

### PM-006-NNN-I5: Override Audit Log Has No Retention or Review Policy [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Synthesis Hypothesis Validation |
| **Strategy Step** | Step 3 (Process failures lens) |

**Failure Cause:** The Human Override Audit AC (line 686) specifies 4-field structured logging to `work/audit/override-log.md`. No AC or text specifies how long the log is retained, when it is reviewed, whether it is purged periodically, or what happens when it grows beyond manageable size over a multi-year product lifecycle.

**Evidence:** Line 686: "Audit log persisted to `work/audit/override-log.md`." No retention policy, no review policy, no size management guidance. The override log could accumulate thousands of entries over a 2-year product lifecycle. The Post-Launch Success Metrics AC at line 885 tracks the "override rate" but not the raw log management.

**Recommendation:** The PM-003-NNN-I5 recommendation (add reviewer and review frequency to line 885) addresses the review gap. Add a one-line note on retention: "Override log is reviewed monthly; entries older than 12 months may be archived to `work/audit/override-log-archive-YYYY.md` to maintain manageable log size."

---

## Recommendations

### P0 -- Critical: MUST Mitigate Before Acceptance

**PM-001-NNN-I5: Add named MCP maintenance owner as a required AC checkbox**
- Mitigation: Add one AC to MCP Integration Quality: "A named MCP maintenance owner (person or role) is documented in `skills/user-experience/SKILL.md` under a 'Maintenance Ownership' section before Wave 1 merge. Owner is responsible for quarterly audit cadence, cross-skill failure coordination, and MCP registry updates."
- Acceptance criteria: The AC is a checkbox. `SKILL.md` Maintenance Ownership section is a verifiable file artifact. Issue closure requires this section to exist.

### P1 -- Important: SHOULD Mitigate

**PM-002-NNN-I5: Add verifiable pass criteria for canonical integration sequences**
- Mitigation: Extend line 805 to specify at least 4 verifiable pass criteria for JTBD -> Design Sprint: (1) functional dimension present in challenge statement, (2) at least 1 convergent recommendation, (3) at least 1 divergent recommendation, (4) sprint facilitator proceeds without requesting additional JTBD input. Apply equivalent structure to Lean UX -> HEART.
- Acceptance criteria: Each named sequence has 4 verifiable criteria. Third-party test execution possible without consulting the implementer.

**PM-003-NNN-I5: Add threshold, reviewer, and response protocol to override monitoring AC**
- Mitigation: Revise line 885 to include: (a) 50% override rate threshold for 90-day window triggers review; (b) reviewer role (linked to MCP maintenance owner); (c) response protocol with at least one action option. Replace "monitoring only" with structured review mechanism.
- Acceptance criteria: AC includes threshold, reviewer, and response protocol. "Monitoring only" characterization is replaced.

**PM-004-NNN-I5: Add Wave 1 retrospective as named deliverable and Wave 2 gate**
- Mitigation: Add to Wave Progression ACs: `work/retros/wave-1-retro.md` produced within 5 business days of WAVE-1-SIGNOFF.md; 4 required content sections specified; Wave 2 explicitly gated on retrospective completion.
- Acceptance criteria: Retrospective is an AC checkbox. Wave 2 dependency is explicit. Third party can verify 4 required content sections exist.

### P2 -- Monitor

**PM-005-NNN-I5:** Add multi-skill simultaneous degradation note to registry AC or MCP runbook AC. One sentence specifying text-based/screenshot fallback when both Required MCP and MCP-based fallback are inactive for a single sub-skill.

**PM-006-NNN-I5:** Link override log review policy to the PM-003-NNN-I5 reviewer assignment. Add one-line retention note (monthly review, 12-month archival threshold).

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | PM-001-NNN-I5: The prose commitment to a named MCP maintenance owner (lines 615, 767) survives 5 iterations without becoming an AC checkbox. The prose and the intent are there; the enforcement mechanism is not. Two prose lines referencing the same responsibility without a corresponding AC is a completeness gap that the R4 round's structural additions (12 new ACs total across R4) did not close. |
| Internal Consistency | 0.20 | Positive | R4 resolved PM-002-I4 (WAVE-{N}-SIGNOFF.md as closure deliverable), added orchestrator failure modes (line 804), added sub-skill-to-sub-skill handoff schema (line 808), and substantially resolved PM-006-I4 (registry mechanism). The issue is now internally more consistent: wave enforcement has teeth, handoff contracts are defined, orchestrator failure behavior is documented. The internal consistency dimension has improved from the prior negative assessment. |
| Methodological Rigor | 0.20 | Negative | PM-003-NNN-I5: The override monitoring AC surviving four iterations without a threshold, reviewer, or response protocol is a methodological rigor gap. The Human Override Audit AC (new in R4) is a meaningful improvement but is a data collection mechanism, not a review mechanism. The distinction matters: collecting data without reviewing it at a threshold is not methodologically rigorous governance of the confidence gate architecture. PM-002-NNN-I5: The integration "tested" definition is now present but still lacks verifiable criteria. |
| Evidence Quality | 0.15 | Neutral | R4 added the Wave 1 time-to-first-value estimate (`[R4-fix: SM-002-I4]`, line 89: "estimated 2-4 hours including setup") and qualified Design Sprint AI capability claims (`[R4-fix: DA-001-I4]`, line 364). These are genuine evidence quality improvements. PM-004-NNN-I5 (Wave 1 retrospective gap) remains the evidence quality concern: the scope estimate's "revise upward" signal has no enforcement gate. Net neutral given R4 improvements. |
| Actionability | 0.15 | Neutral | R4 added actionable ACs: orchestrator failure modes (line 804), P-003 CI enforcement (line 865), sub-skill-to-sub-skill handoff schema (line 808), Human Override Audit (line 686), Wave 3 MCP pre-commitment (line 604). These are genuine actionability improvements. PM-002-NNN-I5 (integration pass criteria) and PM-004-NNN-I5 (retrospective gate) are the remaining actionability gaps. Net neutral given the improvements vs. persistent gaps. |
| Traceability | 0.10 | Positive | R4 continued the comment annotation pattern (`[R4-fix: ...]-I4` tags) consistently. All R4 fixes are traceable to their source findings. The Cross-Session State section (lines 1214-1223) adds Memory-Keeper traceability. The Sub-Skill SKILL.md Descriptions, Model Selection, and Output Levels sections (`[R4-fix: CC-001-I4]` through `[R4-fix: CC-007-I4]`) improve registration traceability. Traceability remains the strongest dimension and continues to improve. |

**Pre-Mortem Assessment: REVISE.** R4 applied genuine targeted improvements that closed or substantially closed 3 of 6 Iter 4 P0/P1 findings. The issue has moved from MEDIUM to LOW-MEDIUM risk. The 4 remaining findings (1 Critical, 3 Major) are narrow and well-defined: each requires a specific AC addition rather than a design rethink. The Critical finding (PM-001-NNN-I5: named MCP maintenance owner) is a single AC checkbox. The three Major findings (PM-002-NNN-I5 through PM-004-NNN-I5) each require specific text additions to existing ACs. If R5 applies these 4 targeted AC additions, the deliverable should be positioned to clear the 0.92 S-014 threshold. The governance and completeness dimensions are the remaining blockers; the internal consistency and traceability improvements from R4 have elevated the floor of the issue's quality.

---

## Execution Statistics

- **Total Findings:** 6
- **Critical:** 1
- **Major:** 3
- **Minor:** 2
- **Protocol Steps Completed:** 6 of 6
- **Failure Category Coverage:** Technical (2), Process (3), Resource (1) -- 3 of 5 lenses applied (External and Assumption lenses: no new findings in Iter 5; Figma monetization risk and Wave 4 free-tier inconsistency are documented in existing text and carried as P2)
- **Findings with P0 Priority:** 1 (PM-001-NNN-I5)
- **Findings with P1 Priority:** 3 (PM-002-NNN-I5 through PM-004-NNN-I5)
- **Findings with P2 Priority:** 2 (PM-005-NNN-I5, PM-006-NNN-I5)
- **Prior Iter 4 P0/P1 findings fully resolved by R4:** 1 (PM-002-I4: WAVE-{N}-SIGNOFF.md closure deliverable AC added)
- **Prior Iter 4 P0/P1 findings substantially resolved by R4:** 1 (PM-006-I4: registry mechanism AC now present; moved to P2)
- **Prior Iter 4 P0/P1 findings partially addressed by R4:** 1 (PM-003-I4: "tested" definition narrowed but pass criteria still absent)
- **Prior Iter 4 P0/P1 findings not addressed by R4:** 2 (PM-004: override monitoring; PM-005: Wave 1 retrospective gate)
- **Prior Iter 4 Critical finding partially addressed by R4:** 1 (PM-001-I4: registry mechanism added but named owner AC still absent)
- **New findings in Iter 5:** 2 (PM-005-NNN-I5: multi-skill degradation; PM-006-NNN-I5: override log retention -- both P2/Minor)
- **Persistent P2 findings carried from prior iterations:** 2 (PM-007, PM-008 -- crisis mode exit, free-tier Wave 4 -- not addressed, P2 acceptable)

---

*Strategy Execution Report -- S-004 Pre-Mortem Analysis*
*Template Version: 1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Executed: 2026-03-03*
*Agent: adv-executor*
