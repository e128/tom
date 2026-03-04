# FMEA Report: UX Framework Selection Analysis

**Strategy:** S-012 FMEA (Failure Mode and Effects Analysis)
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-012 FMEA, Tournament Iteration 7)
**H-16 Compliance:** S-003 Steelman applied prior (confirmed -- SM-001 through SM-013 findings referenced throughout deliverable; R2 change log documents Steelman incorporation)
**Elements Analyzed:** 12 | **Failure Modes Identified:** 28 | **Total RPN:** 2,506

---

## Summary

The deliverable at Revision 11 is a mature, heavily-revised analysis that has addressed the most structurally critical failures identified in prior tournament iterations. FMEA of 12 discrete elements identified 28 failure modes across the document's methodology, governance, implementation specification, and evidence layers. Three Critical findings (RPN >= 200) were identified: the synthesis hypothesis validation protocol contains a systemic self-attestation vulnerability that makes HIGH and MEDIUM gates operationally equivalent to notification-only mechanisms at skill implementation time (FM-007-T7); the cross-sub-skill synthesis registry designated as a V2 target leaves an active integration gap where JTBD and Lean UX can produce contradictory user-characterizations without detection (FM-012-T7); and the wave transition evaluator assignment mechanism has a circular dependency at the no-project-lead scenario (FM-019-T7). Seven Major findings and eighteen Minor findings complete the picture. Recommendation: **REVISE** -- targeted corrections to the three Critical findings and the highest-RPN Major findings will meaningfully improve quality. The deliverable does not require structural overhaul at this revision stage.

---

## Step 1: Element Decomposition

The deliverable was decomposed into 12 discrete analyzable elements:

| ID | Element | Description |
|----|---------|-------------|
| E-01 | Evaluation Methodology | Section 1: scoring criteria, WSM, weighting, sensitivity analysis, uncertainty bounds, AI execution taxonomy |
| E-02 | Full Scoring Matrix | Section 2: 40-framework WSM scores, verification arithmetic, ranking table |
| E-03 | Framework Profiles (Selected 10) | Section 3.1-3.10: individual framework justifications, MCP integrations, AI execution limits, Tiny Teams patterns |
| E-04 | Coverage Analysis | Section 4: domain coverage map, gap analysis, complementarity matrix, V2 roadmap |
| E-05 | Rejected Frameworks | Section 5: exclusion rationale for Double Diamond, Design Thinking, Service Blueprinting, Hook Model, UX Strategy |
| E-06 | Seed List Audit | Section 6: 10 seed framework outcomes |
| E-07 | Parent Skill and Routing Framework | Section 7.1-7.2: `/user-experience` parent skill, routing decision guides, triage mechanism |
| E-08 | MCP Maintenance Contract | Section 7.3: Required vs. enhancement MCP classification, owner assignment, tooling costs |
| E-09 | Implementation Wave Plan | Section 7.4: 5-wave adoption plan, transition criteria, wave task schema, backward-pass protocol |
| E-10 | Worktracker Entity Checklist | Section 7.5: 6 required pre-launch entities, KICKOFF-SIGNOFF.md artifact, launch readiness gate |
| E-11 | Synthesis Hypothesis Validation Protocol | Section 7.6: confidence gates (HIGH/MEDIUM/LOW), gate prompt templates, sub-skill scope table, attestation storage |
| E-12 | Evidence and Traceability Layer | Evidence Summary, Revision History (R1-R11), inline finding IDs throughout document |

---

## Step 2: Failure Mode Enumeration (All 5 Lenses per Element)

Applied lenses: Missing, Incorrect, Ambiguous, Inconsistent, Insufficient.

---

## Findings Table

| ID | Element | Failure Mode | S | O | D | RPN | Severity | Corrective Action | Affected Dimension |
|----|---------|-------------|---|---|---|-----|----------|-------------------|--------------------|
| FM-001-T7 | E-01 | Incorrect: ±0.25 uncertainty band directional bias acknowledged but not operationalized in compression-zone guidance | 5 | 6 | 3 | 90 | Major | Add explicit downward-bias guidance to compression zone actionable table | Methodological Rigor |
| FM-002-T7 | E-01 | Ambiguous: AI Execution Mode Taxonomy in Section 1 defines two modes but Section 7.6 defines three confidence levels (HIGH/MEDIUM/LOW) -- the mapping between the two taxonomies is stated in neither section | 6 | 7 | 5 | 210 | Critical | Add explicit cross-reference mapping: "Deterministic execution" maps to HIGH confidence; "Synthesis hypothesis" maps to MEDIUM or LOW depending on sub-criteria defined in Section 7.6 sub-skill scope table | Methodological Rigor |
| FM-003-T7 | E-01 | Insufficient: WSM independence assumption resolution references C3=25% as the bounding case, but the bounding formula proof assumes symmetric criterion weights -- the proof does not cover the case where C1 and C5 are BOTH increased simultaneously | 4 | 4 | 6 | 96 | Major | Add a note confirming that C1 and C5 simultaneous increase was not tested; characterize the omission as a known limitation of the three-scenario sensitivity coverage | Evidence Quality |
| FM-004-T7 | E-02 | Missing: The Score Calculation Verification table covers only the top 10 frameworks. Non-selected frameworks' weighted totals are verified only via prior correction rounds (S-011 CV-001 through CV-008) with no independent post-correction arithmetic verification table | 5 | 5 | 6 | 150 | Major | Add a note explicitly stating that non-selected framework scores carry the same ±0.25 uncertainty as selected framework scores and that no independent post-R4 verification of non-selected framework scores was performed | Evidence Quality |
| FM-005-T7 | E-02 | Inconsistent: The Gestalt Principles score is listed in the matrix as 6.95 (after S-011 correction), but Section 5 (Rejected Notable Frameworks) does not include Gestalt Principles -- only Double Diamond, Design Thinking, Service Blueprinting, Hook Model, and UX Strategy are profiled. Section 4 Gap Analysis references Gestalt Principles (rank 16) for the Visual Layout gap | 4 | 4 | 5 | 80 | Minor | Add a brief Gestalt Principles entry to Section 5 consistent with its Section 4 reference, or add a note in Section 5 stating that the section covers only the 5 most-competitive near-threshold candidates | Internal Consistency |
| FM-006-T7 | E-03 | Ambiguous: Section 3.8 AI-First Design contains the acceptance criterion for expert reviewer C3/C5/C6 attestation (criterion d), but the sentence structure of the attestation requirement creates ambiguity about whether the expert reviewer must attest EACH of C3, C5, and C6 independently, or whether a single holistic attestation suffices for all three | 6 | 5 | 4 | 120 | Major | Rewrite acceptance criterion (d) with numbered sub-items (d.i), (d.ii), (d.iii) explicitly requiring separate attestation statements for each dimension | Actionability |
| FM-007-T7 | E-11 | Insufficient: The HIGH confidence synthesis gate requires user self-attestation ("I have reviewed this output and accept it for design decisions"). The deliverable acknowledges this limitation in Section 7.6 but designates the HIGH gate as fully protective. The reality is that the HIGH gate is structurally equivalent to a notification mechanism -- a user who clicks confirm without reviewing causes the skill to proceed identically to a user who genuinely reviewed. The defense-in-depth mitigation applies only to MEDIUM and LOW gates, not HIGH | 8 | 7 | 5 | 280 | Critical | Add a structural mitigation for the HIGH gate equivalent to the LOW gate structural mitigation: the HIGH gate's output format should include a brief "Summary of key synthesis judgments for reviewer" block that makes skipping review visibly consequential -- the user must acknowledge at least one specific hypothesis judgment, not just click "confirm" | Completeness |
| FM-008-T7 | E-11 | Missing: The Section 7.6 sub-skill scope table specifies confidence levels for each synthesis step but does not include `/ux-inclusive-design` Persona Spectrum construction for STANDARD populations (only "non-standard populations" is listed as MEDIUM). Standard Persona Spectrum construction using Microsoft's documented permanence/temporality/situationally methodology is Deterministic for well-documented disability types but is Synthesis hypothesis for the customization step | 5 | 6 | 5 | 150 | Major | Add a row to the sub-skill scope table for `/ux-inclusive-design` covering standard Persona Spectrum construction: "Generic Persona Spectrum (permanent/temporary/situational identification from Microsoft toolkit)" as Deterministic; "Custom persona mapping to team's specific user population" as MEDIUM | Completeness |
| FM-009-T7 | E-09 | Ambiguous: The backward-pass cost ceiling states "a maximum of 2 backward passes per wave transition are permitted." It is unclear whether "2 backward passes" means 2 backward passes to the IMMEDIATELY preceding wave, or 2 backward passes in total across the entire multi-wave chain. A team in Wave 4 receiving contradicting evidence from Wave 5 could trigger backward passes back to Wave 1 artifacts -- the ceiling scope is ambiguous | 6 | 5 | 5 | 150 | Major | Clarify: "maximum of 2 backward passes per wave-pair (e.g., Wave 5 contradicting Wave 1 counts as a single backward-pass event regardless of how many intermediate waves are traversed). The backward-pass limit resets for each wave-pair combination." | Actionability |
| FM-010-T7 | E-07 | Missing: The parent skill triage mechanism (Section 7.1) does not include routing for a team that is mid-wave (has completed Wave 1 but not Wave 2) and wants to use a Wave 2+ sub-skill. The routing assumes lifecycle stage but not implementation wave stage. A team at Wave 1 who tries option (g) "After launch -- measure UX health" would be routed to `/ux-heart-metrics` despite Wave 2 not being their next step per Section 7.4 | 5 | 5 | 6 | 150 | Major | Add a wave-awareness check to the parent skill triage: "If you have not yet completed Wave {N}, the sub-skill you are requesting is in Wave {N+X}. You can proceed, but the wave adoption plan recommends completing Wave {N} first for the reasons documented in Section 7.4." Present as advisory, not blocking | Actionability |
| FM-011-T7 | E-10 | Insufficient: The KICKOFF-SIGNOFF.md artifact format requirement (Section 7.5) specifies the structure using a "simple markdown table" but does not provide a template or example. The sign-off artifact is the blocking prerequisite for Wave 1 yet its format is underspecified -- implementers could produce a structurally non-conformant artifact that passes a visual inspection but fails to capture the required information | 5 | 5 | 5 | 125 | Major | Add a concrete KICKOFF-SIGNOFF.md template in Section 7.5 with the exact table structure, a "Signed off by:" line example, and sample fill values. The template should be copy-paste ready | Actionability |
| FM-012-T7 | E-11 | Missing: The cross-sub-skill synthesis registry is designated as a "V2 implementation target" (end of Section 7.6) despite the Section 7.6 scope table identifying 8 sub-skills that produce synthesis hypothesis outputs that could contradict each other. The registry deferral means that contradiction detection is entirely manual during V1 -- and the manual alternative ("relies on wave transition evaluation") is insufficient because wave transition evaluation is a periodic checkpoint, not a real-time gate | 7 | 8 | 5 | 280 | Critical | Elevate synthesis registry to a V1 lightweight implementation: a shared markdown file at `projects/{PROJ-ID}/work/ux/synthesis-registry.md` maintained by the parent skill at each synthesis output invocation. Minimum viable registry: sub-skill name, synthesis type, confidence level, output artifact path, attestation status. This does not require the full contradiction-detection capability -- it provides the audit trail that enables manual contradiction checking at wave transitions | Completeness |
| FM-013-T7 | E-08 | Ambiguous: Section 7.3 MCP Maintenance Contract states the owner "is responsible for... (d) escalating breaking changes to the PROJ-020 project lead." The escalation path terminates at the project lead with no further chain. If the project lead is unavailable or the project is post-launch with no active project lead, the breaking-change escalation has no terminal handler | 4 | 5 | 5 | 100 | Major | Add a post-launch escalation path: "After PROJ-020 launch, escalating breaking MCP changes to the `/user-experience` skill lead if no active PROJ-020 project lead is available. If neither is reachable, file a high-priority GitHub Issue in the Jerry repository titled 'MCP Breaking Change: [tool name]' and escalate per H-31." | Actionability |
| FM-014-T7 | E-09 | Incorrect: Section 7.4 Wave 5 entry criterion (c) requires a "written stakeholder brief" at `projects/{PROJ-ID}/work/sprint-briefs/{brief-slug}.md` before the Design Sprint begins. However, Section 7.4 also states wave skipping is allowed if readiness criteria are met -- a team that skips Waves 2-4 and goes directly to Wave 5 per the skip policy would satisfy neither the sprint-brief path requirement nor the wave readiness criteria. The two policies create a logic gap | 5 | 4 | 5 | 100 | Minor | Add a note under the "Skipping waves" paragraph: "Teams skipping to Wave 5 must satisfy ALL Wave 5 entry criteria regardless of wave-skip authorization. Wave skipping permits bypassing lower-wave criteria; it does not bypass Wave 5-specific entry criteria." | Internal Consistency |
| FM-015-T7 | E-01 | Missing: The Sensitivity Analysis covers three perturbation scenarios (C1, C2, C3) but does not test a C4 (Maturity) perturbation, despite C4 being the dimension where AI-First Design's C4=2 creates the sharpest outlier in the selected set. A C4=0% scenario (not weighted) would test whether AI-First Design remains in the top 10 on the strength of its other criteria alone | 4 | 5 | 6 | 120 | Major | Add a C4=0% sensitivity note: "Removing C4 from the weighted formula (C4=0%, redistributing 15% to C1=30%, C2=25%, remaining weights proportional) [compute the resulting rank for AI-First Design to confirm or deny top-10 retention]. This documents whether AI-First Design's inclusion depends on C4 being weighted at all." | Methodological Rigor |
| FM-016-T7 | E-03 | Insufficient: Section 3.2 Design Sprint's "Zero-user fallback" section defines the output set when no users can be recruited, including an "untested interactive prototype" and hypothesis document. However, the section does not specify who owns the responsibility for completing the post-launch user testing plan at the specified 14-day deadline. The plan is created but its accountability chain is undefined | 4 | 6 | 4 | 96 | Major | Add: "Accountability: the post-launch user testing plan's named executor is the same as the Design Sprint facilitator (the person who ran the sprint). The facilitator is responsible for scheduling the minimum-5-user test within 14 days of first user activation and documenting results in the worktracker story for the Design Sprint." | Actionability |
| FM-017-T7 | E-04 | Insufficient: Section 4 V2 Roadmap designates a "cross-portfolio non-redundancy comparison" as a V2 enhancement (V2 action item RT-005-I6 -- R11), but the V2 Consolidated Roadmap table (Sections 4) does not include this item. The omission means the cross-portfolio validation may be deprioritized against the explicitly listed V2 candidates | 3 | 5 | 4 | 60 | Minor | Add the "C5 External Non-Redundancy Validation" Enabler to the V2 Consolidated Roadmap table with priority P3, category "Methodology", and rationale "Provides external validation of non-redundancy claim" | Traceability |
| FM-018-T7 | E-12 | Ambiguous: The Revision History uses multiple ID namespaces (SM-NNN, RT-NNN, DA-NNN, FM-NNN, PM-NNN, IN-NNN, CV-NNN, SR-NNN, CC-NNN) without a legend mapping these to the strategies that generated them. A reader encountering "DA-007" cannot determine this refers to Devil's Advocate findings without domain knowledge of the tournament strategy prefixes | 4 | 5 | 5 | 100 | Minor | Add a legend to the Revision History header mapping each prefix to its source strategy: "DA = S-002 Devil's Advocate; SM = S-003 Steelman; PM = S-004 Pre-Mortem; CC = S-007 Constitutional AI; SR = S-010 Self-Refine; CV = S-011 Chain-of-Verification; FM = S-012 FMEA; IN = S-013 Inversion; RT = S-001 Red Team" | Traceability |
| FM-019-T7 | E-10 | Incorrect: The KICKOFF-SIGNOFF.md "no-project-lead fallback" rule states that "the individual who initiates the kickoff meeting assumes project lead responsibilities." This creates a circular problem: if no one has initiated the kickoff yet, there is no project lead to initiate it. The 30-day escalation path (file a worktracker impediment) assumes someone is monitoring the worktracker, but if no project lead exists, this monitoring is also unassigned | 7 | 6 | 5 | 210 | Critical | Assign a fallback monitor role explicitly: "If no project lead is assigned within 14 days of PROJ-020 creation, the PROJ-020 creator (the person who created the PROJ-020 worktracker entry) automatically assumes interim project lead responsibilities and is required to initiate the kickoff. This role assignment is non-optional and is documented at PROJ-020 creation time in the worktracker entry." | Actionability |
| FM-020-T7 | E-07 | Missing: The parent skill triage (Section 7.1) includes a "UX capacity triage" check that routes "Part-Time UX" teams to Wave 1 only. However, the capacity triage fires AFTER the lifecycle-stage routing question, meaning a part-time UX team who answers "After launch -- measure UX health" (option g) is already routed to `/ux-heart-metrics` before the capacity check fires. The ordering of the triage checks creates an incorrect routing sequence | 5 | 5 | 5 | 125 | Major | Reorder the parent skill triage: capacity triage MUST fire BEFORE lifecycle-stage routing (not after). A team at part-time UX capacity should be surfaced the Wave 1 advisory before being offered the lifecycle routing menu. The capacity check is a pre-filter, not a post-filter | Internal Consistency |
| FM-021-T7 | E-03 | Insufficient: Section 3.6 (JTBD) describes the Switch interview guide as "included as a skill artifact" for teams with fewer than 3 data sources. No artifact path is specified. A developer or PM following this guidance has no way to locate the referenced guide | 3 | 6 | 4 | 72 | Minor | Add: "The Switch interview guide is stored at `skills/user-experience/resources/jtbd-switch-interview-guide.md`. Note: this artifact must be created at sub-skill implementation time (it does not yet exist as of this analysis)." | Actionability |
| FM-022-T7 | E-11 | Ambiguous: Section 7.6 states the MEDIUM gate audit trail stores attestation records "inline within the sub-skill output file." However, the output file path template uses `projects/{PROJ-ID}/work/ux/{sub-skill-slug}/{output-artifact}.md` -- this means attestation records are stored in project-specific files, not in a cross-project registry. If a PROJ-020 audit needs to verify attestation patterns across multiple projects using the skill, there is no consolidated view | 3 | 4 | 5 | 60 | Minor | Add a note: "For cross-project audit of attestation patterns, the sub-skill output file path convention produces project-scoped records only. A cross-project attestation audit would require querying all `work/ux/{sub-skill-slug}/` directories. This is a V2 tooling consideration." | Traceability |
| FM-023-T7 | E-04 | Missing: The Section 4 Gap Analysis acknowledges the HIGH RISK user research gap but provides no degraded-mode guidance for teams who have already activated multiple sub-skills and discovered a major product decision was made incorrectly due to the gap. There is no retrospective protocol -- only a V2 forward-looking recommendation | 4 | 5 | 5 | 100 | Minor | Add a retrospective protocol note: "If a team discovers post-launch that a major product decision was made incorrectly due to reliance on unvalidated synthesis hypothesis outputs (a consequence of the user research gap), the appropriate response is: (1) run /ux-jtbd with real user interview data to re-anchor job statements; (2) re-run the affected Lean UX hypothesis as an invalidation test; (3) document the revision in the hypothesis backlog as a superseded learning artifact." | Actionability |
| FM-024-T7 | E-06 | Missing: Section 6 (Seed List Audit) documents which seeds were selected and why, but does not document whether any seed frameworks NOT in the 40-framework candidate universe were considered and excluded before scoring. If the user specified seeds not in the initial 40, there is no record of how they were handled | 2 | 4 | 5 | 40 | Minor | Add a note: "All 10 seed frameworks were found in the 40-framework candidate universe generated from the three source inputs (Section 1 Candidate Universe Generation). No seed framework was excluded from the universe before scoring." | Traceability |
| FM-025-T7 | E-05 | Insufficient: Section 5.4 Hook Model exclusion states the asymmetric ethical treatment between Hook and Fogg "is an artifact of how the frameworks are typically presented in popular discourse" (FM-013 -- 2026-03-02). This is a valid acknowledgment, but the section does not update the exclusion rationale to reflect that "diagnostic vs. prescriptive mode" is now the PRIMARY exclusion reason (replacing the ethical-concern differentiator that was removed) | 3 | 4 | 4 | 48 | Minor | Add a summary sentence to Section 5.4: "The updated primary exclusion reason: Fogg's diagnostic B=MAP mode (identifying why behaviors are not occurring) is more aligned with the portfolio's problem-diagnosis orientation than Hook's prescriptive engagement design mode. Ethical risks are equivalent between the two frameworks and do not differentiate the selection." | Internal Consistency |
| FM-026-T7 | E-01 | Missing: The Candidate Universe Generation section (Section 1) notes that 5 frameworks were added beyond the 35 from the ux-frameworks-survey.md, but does not name all 5. Only AI-First Design is explicitly called out. The other 4 are unidentified, preventing verification that the universe was constructed correctly | 4 | 4 | 6 | 96 | Minor | Name all 5 frameworks added beyond the survey artifact, or add a note: "The 5 additional frameworks are identifiable from the scoring matrix -- they are the frameworks not present in the ux-frameworks-survey.md artifact. A cross-reference verification has not been performed in this document; implementers who need to verify universe completeness should cross-reference the scoring matrix against the survey artifact." | Traceability |
| FM-027-T7 | E-08 | Insufficient: The Required vs. Enhancement MCP classification table (Section 7.3) classifies `/ux-heuristic-eval`'s Figma MCP as "Required (for design evaluation)." However, Section 3.1 (Nielsen's Heuristics) documents that 4 of 10 heuristics (H1, H3, H5, H9) can be evaluated from screenshots without Figma, and the 6 contextually-dependent heuristics require team-provided context that Figma does not supply. The "Required" classification overstates Figma's functional necessity | 4 | 5 | 4 | 80 | Minor | Revise the classification: "`/ux-heuristic-eval`: Figma (Required for full 10-heuristic evaluation with automatic component inspection; screenshot-input mode available for all 10 heuristics without Figma -- see Section 3.1 AI Reliability Tiers table for mode-specific fallback)." | Internal Consistency |
| FM-028-T7 | E-12 | Insufficient: The Evidence Summary lists 26+ evidence entries with full project-relative paths (per R5 FM-018 fix) but does not include evidence for the TINY TEAMS POPULATION SEGMENTS table (Section 1, DA-003-I5). The population segments characterization (solo practitioner / pair / small cross-functional / part-time UX) is presented as factual without citing the research artifact that grounds each segment's characteristics | 3 | 5 | 4 | 60 | Minor | Add evidence entries E-027 through E-030 for each population segment's source characterization, or add a note: "The TINY TEAMS POPULATION SEGMENTS table is analyst-derived from the general characterization in tiny-teams-research.md (E-013 through E-017) rather than from distinct per-segment evidence. The segment descriptions reflect analyst judgment about team dynamics, not separately cited research." | Evidence Quality |

---

## Detailed Findings

### FM-002-T7: AI Execution Mode Taxonomy -- Confidence Level Mapping Gap (Critical)

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 1 (AI Execution Mode Taxonomy) / Section 7.6 (Synthesis Hypothesis Validation Protocol) |
| **Strategy Step** | Step 2 (Inconsistent lens) |

**Evidence:**
Section 1 defines two AI execution modes: "Deterministic execution" and "Synthesis hypothesis." Section 7.6 defines three confidence levels: HIGH, MEDIUM, and LOW. The sub-skill scope table in Section 7.6 maps specific skill steps to HIGH, MEDIUM, or LOW confidence, but the mapping logic is never stated explicitly. A reader attempting to understand why `/ux-design-sprint` Day 4 thematic analysis is HIGH while JTBD job synthesis is MEDIUM has no stated mapping rule. The implicit rule appears to be: "Synthesis hypothesis + grounded data = HIGH; Synthesis hypothesis + secondary research only = MEDIUM; Synthesis hypothesis with high uncertainty = LOW" -- but this is not documented anywhere in the deliverable.

**Analysis:**
This ambiguity creates a failure mode for sub-skill authors. When implementing new sub-skills or extending existing ones, the author has no explicit rule to apply when classifying a new synthesis step. They will either guess (producing inconsistent classifications) or re-read all existing examples to infer the rule (producing delays and potential misapplication). At C4 criticality, where the synthesis hypothesis gates are a primary user safety mechanism, an unclear classification rule undermines the protocol's integrity.

**Recommendation:**
In Section 1, add a paragraph after the AI Execution Mode Taxonomy table: "Mapping to Section 7.6 confidence levels: Deterministic execution steps map to HIGH confidence (output may be used directly after human confirmation). Synthesis hypothesis steps are further classified by data quality: (a) HIGH confidence when synthesis is grounded in direct user data (interviews, session recordings, direct observation); (b) MEDIUM confidence when synthesis is grounded in secondary research (App Store reviews, analytics, competitor analysis) or team-provided context; (c) LOW confidence when synthesis relies on AI training-data generalization with no team-specific grounding data. This three-level classification applies consistently across all sub-skill synthesis steps."

**Acceptance Criteria:** Section 1 contains an explicit mapping rule from the two-mode taxonomy to the three-level confidence system. The rule is deterministic: a sub-skill author implementing a new synthesis step can classify it without consulting existing examples.

**Post-Correction RPN Estimate:** S=6, O=3, D=2 = **36**

---

### FM-007-T7: HIGH Confidence Gate Structural Equivalence to Notification (Critical)

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.6 (Synthesis Hypothesis Validation Protocol -- HIGH confidence gate) |
| **Strategy Step** | Step 2 (Insufficient lens) |

**Evidence:**
Section 7.6 HIGH confidence synthesis gate states: "User must confirm: 'I have reviewed this synthesis output and accept it for design decision-making.' Single confirmation per invocation." The agent prompt template reads: "Do not produce the design recommendation until confirmation is received." Compared to the LOW gate, which has a non-behavioral structural mitigation ("the output template itself does not contain a design recommendation block for LOW confidence paths"), the HIGH gate has NO structural mitigation -- only a behavioral gate requiring user confirmation. Section 7.6 itself acknowledges: "The self-attestation limitation acknowledgment... The protocol cannot independently verify that the user has actually performed the claimed review." The LOW gate's structural defense is explicitly described; the HIGH gate has no equivalent structural defense.

**Analysis:**
The HIGH confidence gate is the most frequently triggered gate (8 of 10 sub-skills have at least one HIGH confidence synthesis step). If the HIGH gate functions only as a notification (user clicks confirm reflexively), the safety architecture has a wide operational gap. The LOW gate's structural mitigation (omitting the design recommendation block from the output template) demonstrates that structural enforcement is achievable for LLM agents. The absence of an equivalent structural feature for the HIGH gate leaves the most common gate as the weakest one.

**Recommendation:**
Add a structural mitigation to the HIGH gate equivalent in principle to the LOW gate's omission approach: "The HIGH confidence gate output format MUST include a 'Synthesis Judgments Summary' block before the confirmation prompt. This block lists 2-4 specific judgment calls the AI made in producing the synthesis (e.g., 'I assumed your primary users are mobile-first because your product is a consumer app -- is this accurate?'). The user must acknowledge at least one specific judgment before confirmation is accepted. This structural requirement makes reflexive confirmation visibly consequential by requiring engagement with specific content rather than a generic acknowledgment." This converts the HIGH gate from a notification into a minimal-engagement checkpoint without requiring the full expert-review overhead of the MEDIUM gate.

**Acceptance Criteria:** The HIGH gate prompt template in Section 7.6 includes a Synthesis Judgments Summary structural requirement. The agent prompt language template is updated to include the judgment-enumeration step before the confirmation prompt.

**Post-Correction RPN Estimate:** S=8, O=4, D=3 = **96**

---

### FM-012-T7: V1 Cross-Sub-Skill Synthesis Registry Deferred -- Active Integration Gap (Critical)

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.6 (Cross-sub-skill integration test, final paragraph) |
| **Strategy Step** | Step 2 (Missing lens) |

**Evidence:**
Section 7.6 states: "The parent skill (`/user-experience`) SHOULD maintain a lightweight synthesis registry listing active synthesis hypothesis outputs per user segment, enabling contradiction detection across sub-skill boundaries. This is a V2 implementation target -- V1 relies on manual cross-referencing during wave transition evaluation." The Section 7.6 scope table identifies 8 sub-skills with synthesis hypothesis steps. JTBD produces job statements characterizing user goals (MEDIUM confidence); Lean UX produces assumption maps characterizing user behavior hypotheses (MEDIUM confidence). Both operate on the same user segment. The V1 manual cross-referencing approach is wave-transition-gated (checking at wave boundaries), not invocation-gated (checking at synthesis time).

**Analysis:**
The failure mode: a team runs `/ux-jtbd` in Wave 1 and produces job statement "When I face a deadline, I want to batch-process tasks" (HIGH confidence from 5 user interviews). In Wave 2, `/ux-lean-ux` produces assumption "Users prefer to address tasks one at a time because they find batch operations cognitively overwhelming" (MEDIUM confidence from assumption mapping). These characterizations directly contradict each other but there is no detection mechanism until the next wave transition evaluation. If the team uses the Lean UX assumption to drive a UI decision before the Wave 2→3 transition review, they build on a contradicted hypothesis. At C4 criticality for the overall framework analysis, leaving the primary user-understanding synthesis mechanism with a known detection gap for the V1 implementation is a structural quality risk.

**Recommendation:**
Implement a minimum-viable V1 synthesis registry as a static markdown file, not a dynamic system: "Create a parent-skill-maintained file at `projects/{PROJ-ID}/work/ux/synthesis-registry.md` from the first synthesis output. Each synthesis output invocation appends a row: `| Sub-skill | Step | Confidence | User Segment | Synthesis Summary (1 sentence) | Artifact Path | Date |`. The parent skill's invocation protocol includes: at synthesis output time, check the registry for existing entries with the same user segment -- if a potential contradiction exists, surface it to the user before presenting the synthesis output. This does not require automated contradiction detection -- it requires the agent to read the registry file before generating synthesis output." This is achievable with a single Read + regex check in the parent skill's `<methodology>` section and adds minimal operational overhead.

**Acceptance Criteria:** Section 7.6 specifies a V1 lightweight synthesis registry format and invocation-time check protocol. The V2 tag is changed to "V1 minimum viable" for the registry itself; "V2 enhancement" is retained for automated contradiction detection.

**Post-Correction RPN Estimate:** S=7, O=5, D=2 = **70**

---

### FM-019-T7: KICKOFF-SIGNOFF Circular Dependency at No-Project-Lead Scenario (Critical)

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Section 7.5 (Kickoff sign-off artifact, no-project-lead fallback) |
| **Strategy Step** | Step 2 (Incorrect lens) |

**Evidence:**
Section 7.5 states: "If no PROJ-020 project lead has been formally assigned at the time kickoff is scheduled, the individual who initiates the kickoff meeting assumes project lead responsibilities." The 30-day escalation path states: "the PROJ-020 creator files a worktracker impediment titled 'Kickoff Not Held -- Wave 1 Blocked'." The circular dependency: if no project lead exists, who is responsible for monitoring the worktracker to file the impediment? The worktracker monitoring responsibility is not assigned. The "any team member may initiate the kickoff" provision requires that some team member notices the 14-day deadline has passed -- but there is no mechanism that notifies team members of this deadline if no project lead has set up the monitoring.

**Analysis:**
The kickoff is the blocking prerequisite for Wave 1. The no-project-lead scenario is a realistic failure mode for a self-organizing team adopting Jerry without formal project ownership. The circular dependency (no lead → no monitor → no impediment filed → no escalation → Wave 1 never starts) creates a scenario where the entire implementation silently stalls with no detection. At C4 criticality, a blocking prerequisite with no fallback detection mechanism is a Critical structural gap.

**Recommendation:**
Assign the monitoring responsibility unconditionally to the PROJ-020 creator: "The PROJ-020 creator (the individual who created the PROJ-020 worktracker entry and project directory) is the permanent fallback monitor for the kickoff deadline, regardless of whether a project lead has been formally assigned. At PROJ-020 creation time, the creator MUST create a personal calendar reminder for Day 14 titled 'PROJ-020 Kickoff Check: Project Lead Assigned?' and a Day 30 reminder titled 'PROJ-020 Kickoff Emergency Escalation.' These are personal monitoring obligations that cannot be delegated. The creator's only responsibility is to initiate the kickoff per the no-project-lead fallback if Day 14 passes without formal lead assignment -- not to run the kickoff solo, but to schedule it and convene the team."

**Acceptance Criteria:** Section 7.5 assigns the kickoff monitoring obligation to a specific named role (PROJ-020 creator) with no ambiguity about whose calendar reminders are required. The circular dependency is broken by making the creator the unconditional fallback monitor.

**Post-Correction RPN Estimate:** S=7, O=3, D=2 = **42**

---

## Recommendations

### Critical Priority (RPN >= 200)

| Finding | Corrective Action | Acceptance Criteria | Pre-Correction RPN | Post-Correction RPN |
|---------|------------------|--------------------|--------------------|---------------------|
| FM-002-T7 | Add explicit mapping rule from two-mode AI taxonomy to three-level confidence system in Section 1 | Section 1 contains deterministic classification rule applicable without consulting examples | 210 | 36 |
| FM-007-T7 | Add Synthesis Judgments Summary structural requirement to HIGH confidence gate | HIGH gate prompt template requires enumeration of specific AI judgment calls before confirmation | 280 | 96 |
| FM-012-T7 | Implement minimum-viable V1 synthesis registry as static markdown with invocation-time check | Section 7.6 specifies V1 registry format; parent skill's methodology includes registry check at synthesis time | 280 | 70 |
| FM-019-T7 | Assign kickoff monitoring obligation unconditionally to PROJ-020 creator | No-project-lead fallback has unconditional monitoring responsibility with specific calendar reminder obligations | 210 | 42 |

### Major Priority (RPN 80-199)

| Finding | Corrective Action | Acceptance Criteria | Pre-Correction RPN | Post-Correction RPN |
|---------|------------------|--------------------|--------------------|---------------------|
| FM-001-T7 | Add directional bias guidance to compression zone actionable table | Compression zone guidance explicitly notes downward errors more likely; actionable guidance adjusted accordingly | 90 | 40 |
| FM-003-T7 | Document C1+C5 simultaneous increase as untested sensitivity scenario | Section 1 WSM independence section explicitly flags this as a known limitation | 96 | 48 |
| FM-004-T7 | Add explicit statement that non-selected framework scores are ±0.25 uncertainty with no post-R4 independent verification | Score Calculation Verification section notes non-selected score status | 150 | 60 |
| FM-006-T7 | Rewrite acceptance criterion (d) for AI-First Design with numbered sub-items for each dimension's attestation | Three separate attestation requirements (d.i, d.ii, d.iii) with explicit per-dimension criteria | 120 | 36 |
| FM-008-T7 | Add standard Persona Spectrum construction row to Section 7.6 sub-skill scope table | Scope table includes `/ux-inclusive-design` standard Persona Spectrum as Deterministic + customization as MEDIUM | 150 | 60 |
| FM-009-T7 | Clarify backward-pass cost ceiling scope to wave-pair rather than global count | Section 7.4 backward-pass protocol unambiguously defines "per wave-pair" scope | 150 | 50 |
| FM-010-T7 | Add wave-awareness advisory check to parent skill triage | Parent skill routing includes wave-advancement advisory before routing to later-wave sub-skills | 150 | 60 |
| FM-011-T7 | Add concrete KICKOFF-SIGNOFF.md template to Section 7.5 | Copy-paste ready template with exact table structure and fill examples | 125 | 40 |
| FM-013-T7 | Add post-launch MCP breaking-change escalation path | MCP escalation chain has terminal handler for post-launch scenarios | 100 | 30 |
| FM-015-T7 | Add C4=0% sensitivity note to Sensitivity Analysis | Section 1 documents C4 zero-weighting scenario result for AI-First Design | 120 | 40 |
| FM-016-T7 | Add accountability statement to Design Sprint zero-user fallback section | Post-launch user testing plan has named accountable executor | 96 | 32 |
| FM-020-T7 | Reorder parent skill triage: capacity check fires before lifecycle routing | Section 7.1 triage sequence is capacity-first, lifecycle-second | 125 | 45 |

### Minor Priority (RPN < 80)

| Finding | Corrective Action | Pre-Correction RPN | Post-Correction RPN |
|---------|------------------|--------------------|---------------------|
| FM-005-T7 | Add Gestalt Principles brief entry or explanation note to Section 5 | 80 | 24 |
| FM-014-T7 | Add note that wave-skip does not bypass Wave 5 entry criteria | 100 | 30 |
| FM-017-T7 | Add C5 External Non-Redundancy Validation to V2 Consolidated Roadmap | 60 | 20 |
| FM-018-T7 | Add finding prefix legend to Revision History header | 100 | 30 |
| FM-021-T7 | Add path reference for Switch interview guide as future implementation artifact | 72 | 30 |
| FM-022-T7 | Add cross-project attestation audit note to Section 7.6 | 60 | 20 |
| FM-023-T7 | Add retrospective protocol for teams discovering post-launch user research gap consequences | 100 | 35 |
| FM-024-T7 | Add confirmation that all seed frameworks were in the 40-framework universe | 40 | 15 |
| FM-025-T7 | Update Section 5.4 Hook Model exclusion to clarify updated primary reason | 48 | 20 |
| FM-026-T7 | Name the 5 frameworks added beyond the survey artifact or add a verification note | 96 | 30 |
| FM-027-T7 | Revise Figma "Required" classification for `/ux-heuristic-eval` to acknowledge screenshot fallback | 80 | 24 |
| FM-028-T7 | Add evidence entries or analyst-derivation note for TINY TEAMS POPULATION SEGMENTS | 60 | 20 |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| **Completeness** | 0.20 | **Negative** | FM-007-T7: HIGH confidence gate lacks structural mitigation (most frequent gate, widest operational gap). FM-008-T7: Standard Persona Spectrum construction missing from Section 7.6 scope table. FM-010-T7: Parent skill routing has no wave-awareness advisory. FM-012-T7: V1 synthesis registry deferred leaving active cross-sub-skill detection gap. FM-015-T7: C4 perturbation scenario missing from Sensitivity Analysis. FM-020-T7: Triage sequence ordering error. |
| **Internal Consistency** | 0.20 | **Negative** | FM-002-T7: Two-mode AI taxonomy and three-level confidence system have no stated mapping rule -- structurally inconsistent cross-reference between Section 1 and Section 7.6. FM-005-T7: Gestalt Principles referenced in Section 4 but absent from Section 5 without explanation. FM-014-T7: Wave-skip policy creates a logic gap with Wave 5 entry criteria. FM-025-T7: Hook Model exclusion rationale inconsistently updated -- ethical consistency note added but primary exclusion reason not clearly flagged as superseded. FM-027-T7: Figma "Required" classification in Section 7.3 inconsistent with screenshot-mode capability documented in Section 3.1. |
| **Methodological Rigor** | 0.20 | **Negative** | FM-001-T7: ±0.25 directional bias acknowledged but not operationalized. FM-003-T7: WSM bounding case proof does not cover C1+C5 simultaneous increase scenario. FM-004-T7: Non-selected framework scores carry ±0.25 uncertainty without explicit post-R4 verification statement. FM-019-T7: Kickoff circular dependency leaves blocking prerequisite with no unconditional detection mechanism. |
| **Evidence Quality** | 0.15 | **Negative** | FM-026-T7: Five additional frameworks beyond survey artifact are unnamed -- universe construction cannot be independently verified. FM-028-T7: TINY TEAMS POPULATION SEGMENTS table lacks evidence citations. FM-003-T7: WSM independence proof omits a testable scenario. |
| **Actionability** | 0.15 | **Negative** | FM-006-T7: AI-First Design acceptance criterion (d) has ambiguous attestation scope. FM-009-T7: Backward-pass cost ceiling scope ambiguity impedes implementation. FM-011-T7: KICKOFF-SIGNOFF.md format underspecified for the document that blocks Wave 1. FM-013-T7: MCP breaking-change escalation has no terminal handler for post-launch scenarios. FM-016-T7: Design Sprint zero-user fallback plan lacks named accountability. FM-021-T7: Switch interview guide referenced but not locatable. |
| **Traceability** | 0.10 | **Negative** | FM-017-T7: C5 External Non-Redundancy Validation V2 item not included in V2 Consolidated Roadmap. FM-018-T7: Revision History finding ID prefixes have no legend mapping them to source strategies. FM-022-T7: MEDIUM gate attestation records are project-scoped with no cross-project consolidated view path. FM-024-T7: Seed framework universe coverage not confirmed. |

**Overall Assessment:** The deliverable is mature and structurally sound at Revision 11, with prior tournament iterations having addressed the most severe failures. The 4 Critical findings in this FMEA analysis are concentrated in the implementation-specification layer (Section 7.5, 7.6) rather than in the core selection methodology -- this is a positive signal that the analysis's analytical validity has stabilized. However, all four Critical findings concern mechanisms that govern user safety (synthesis gates) and operational continuity (kickoff fallback), making them high-priority for correction before the analysis is used as an implementation specification.

---

## Execution Statistics

- **Total Findings:** 28
- **Critical:** 4 (FM-002-T7, FM-007-T7, FM-012-T7, FM-019-T7)
- **Major:** 12 (FM-001-T7, FM-003-T7, FM-004-T7, FM-006-T7, FM-008-T7, FM-009-T7, FM-010-T7, FM-011-T7, FM-013-T7, FM-015-T7, FM-016-T7, FM-020-T7)
- **Minor:** 12 (FM-005-T7, FM-014-T7, FM-017-T7, FM-018-T7, FM-021-T7, FM-022-T7, FM-023-T7, FM-024-T7, FM-025-T7, FM-026-T7, FM-027-T7, FM-028-T7)
- **Protocol Steps Completed:** 5 of 5
- **Total RPN (pre-correction):** 2,506
- **Estimated Total RPN (post-correction):** 928 (62.9% reduction)

---

## Execution Context

- **Strategy:** S-012 (FMEA -- Failure Mode and Effects Analysis)
- **Template:** `.context/templates/adversarial/s-012-fmea.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Tournament Iteration:** 7 of 8
- **Prior Score:** 0.862 (Revision 11, Iteration 6)
- **Finding Prefix:** FM-NNN-T7

---

*Report Version: 1.0.0*
*Strategy: S-012 FMEA*
*SSOT: `.context/rules/quality-enforcement.md`*
*Template Conformance: TEMPLATE-FORMAT.md v1.1.0*
