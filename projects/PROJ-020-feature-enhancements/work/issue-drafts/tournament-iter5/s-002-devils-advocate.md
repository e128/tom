# Devil's Advocate Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

**Strategy:** S-002 Devil's Advocate
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Criticality:** C4 (Critical -- architecture addition, irreversible once merged, tournament mode)
**Date:** 2026-03-03T00:00:00Z
**Reviewer:** adv-executor
**H-16 Compliance:** S-003 Steelman applied 2026-03-03 (confirmed -- `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter5/s-003-steelman.md`)

---

## Role Assumption Statement

**Deliverable challenged:** `ux-skill-issue-body-saucer-boy.md` (post-R4 revision, Iteration 5)
**Scope:** Full issue body as GitHub enhancement specification, architecture specification, and design document for the `/user-experience` skill addition to the Jerry framework
**Criticality level:** C4 (Critical -- architecture addition, irreversible once merged, all 10 adversarial strategies required)
**H-16 compliance:** S-003 Steelman (SM-NNN-I5 findings) applied before this critique. The steelman identified 9 improvement opportunities (2 Critical, 2 Major, 5 Minor). This critique proceeds against the post-R4 deliverable with knowledge of what the steelman recommends but did NOT yet incorporate, allowing the Devil's Advocate to attack from a position of maximum credibility.
**Advocate mandate:** Argue the strongest possible case against this deliverable's positions, assumptions, claims, and design choices. Every finding must be credible, evidence-based, and harder to dismiss than the prior iteration's counter-arguments.

---

## Summary

9 counter-arguments identified (2 Critical, 4 Major, 3 Minor). R4 resolved all three Iter4 Critical findings: DA-001-I4 (Design Sprint AI capability over-claims), DA-002-I4 (Wave 5 unreachable for median user), and DA-003-I4 (ux-orchestrator undocumented failure modes) each received specific AC additions and qualification text. This is a genuine improvement. However, R4 introduced a new structural problem while resolving those three: the blind evaluation rubric's evaluator qualification requirements create a dependency on a "Jerry community contributor pool" that has no defined size, recruitment path, or operational existence. This is DA-001-I5 (Critical). Separately, SM-001-I5 and SM-002-I5 from the steelman have been present across multiple iterations without full incorporation; the Part-time UX table contradiction (MEDIUM in the table, "primary design center" in the text) and the absence of a Wave 1 anchor against the 30-50 day total are argument-completeness failures that weaken the document's persuasion case for its most important reader segment. DA-002-I5 (Critical) elevates the cascade consequence: these gaps mean the pre-launch quality gate is unexecutable as written and the primary audience is systematically under-served by the most prominent summary content they encounter.

Recommend REVISE to address Critical findings before merge. Major findings are addressable without structural rework.

---

## Findings Table

| ID | Finding | Severity | Evidence | Affected Dimension |
|----|---------|----------|----------|--------------------|
| DA-001-I5 | Pre-launch blind evaluation requires a "Jerry community contributor pool" that does not exist and has no defined recruitment path | Critical | Pre-Launch Validation AC: "Evaluators must be Jerry Framework users who... are drawn from the Jerry community contributor pool" | Methodological Rigor |
| DA-002-I5 | Part-time UX table contradiction creates a false adoption barrier for the primary audience segment; Wave 1 time-to-value claim lacks the 8-13 day anchor needed to counter 30-50 day apprehension | Critical | Segment table shows "MEDIUM -- Kano and HEART may exceed part-time capacity" for Part-time UX; paragraph says "most common segment... primary design center"; 30-50 day total in Estimated Scope section; time-to-value paragraph lacks explicit anchor | Evidence Quality / Actionability |
| DA-003-I5 | Memory-Keeper cross-session state specification stores MCP registry state but provides no recovery protocol when Memory-Keeper fails at session start | Major | Cross-Session State section: `jerry/{project}/user-experience/mcp-registry` key stores "MCP connection active/inactive status per sub-skill"; no failure mode defined | Completeness |
| DA-004-I5 | Adversarial validation quality provenance claims ("systematically attacked from nine angles and survived") assert process without demonstrating outcome -- three iterations without incorporating SM-003 specific-corrections evidence | Major | Research Backing > Adversarial Validation: "not that the analysis is perfect, but that it has been systematically attacked from nine different angles and survived" -- no correction specifics | Evidence Quality / Traceability |
| DA-005-I5 | Pre-launch blind evaluation rubric's 15% threshold and 3 dimensions are stated without derivation -- second iteration of SM-004 without incorporation | Major | Pre-Launch Validation AC: "Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions" -- no calibration rationale | Methodological Rigor / Evidence Quality |
| DA-006-I5 | Crisis mode conflict with BLOCK state: a team in crisis-mode activation is routed to a 3-skill emergency sequence, but if they are at Wave 2 or 3 with WAVE-2-SIGNOFF.md incomplete, the BLOCK state activates and prevents routing to Wave 3+ sub-skills in the emergency sequence | Major | Key Design Decisions #2: crisis mode routes to "3-skill emergency: Heuristic --> Behavior --> HEART"; Key Design Decisions #5: "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills" -- no crisis mode BLOCK bypass defined | Internal Consistency |
| DA-007-I5 | BLOCK state lacks an orchestrator message template -- the steelman (SM-005-I5) identified this as missing for the second consecutive iteration; a BLOCK state producing an opaque refusal is indistinguishable from a broken skill | Minor | Wave enforcement 3-state behavior: "BLOCK: ...directs user to complete the current wave's signoff process" -- no message template; no resolution path verbatim | Completeness / Actionability |
| DA-008-I5 | Haiku model assignment for heuristic evaluation is an unvalidated cost-optimization hypothesis treated as a fixed design choice; severity-3/4 violations require contextual inference that haiku may not reliably support | Minor | Sub-Skill Model Selection: "haiku | Heuristic Evaluation | Checklist-based systematic evaluation against 10 discrete heuristics; procedural, not reasoning-intensive" -- SM-009-I5 identified this risk; no validation hook in AC | Methodological Rigor |
| DA-009-I5 | Service Blueprinting V2 P1 priority appears inconsistent with its 7.40 score when other V2 candidates have no score listed; dual-purpose justification is absent from the table | Minor | V2 Candidates table: "P1 | No service design coverage | /ux-service-blueprinting (rank #12, score 7.40) | Covers end-to-end service process niche; also the auto-substitute if AI-First Design Enabler expires" -- the "also the auto-substitute" is not explained as the priority driver | Traceability |

---

## Detailed Findings

### DA-001-I5: Pre-Launch Blind Evaluation Requires a Non-Existent Contributor Pool [CRITICAL]

**Claim Challenged:**
> "Evaluators must be Jerry Framework users who (a) did not author or contribute to the sub-skill under review, (b) have completed at least one prior sub-skill evaluation, and (c) are drawn from the Jerry community contributor pool. For teams < 3 people, external Jerry community members fulfill the evaluator requirement."

**Counter-Argument:** The evaluator qualification requirement contains a circular dependency that renders the pre-launch validation AC unexecutable as written. "Drawn from the Jerry community contributor pool" presupposes that (a) a defined "Jerry community contributor pool" exists as a named, enumerated entity, (b) this pool has members who have "completed at least one prior sub-skill evaluation" at the time Wave 1 launches, and (c) there is a recruitment or access mechanism to reach them. None of these preconditions are documented anywhere in the specification. The Jerry framework is a single-maintainer project (the author of this specification is effectively the entire current contributor pool). Wave 1 is the FIRST sub-skill launch; therefore, no Jerry Framework user can have "completed at least one prior sub-skill evaluation" before Wave 1 ships -- the condition is a strict temporal impossibility for the first wave.

The fallback for teams < 3 people -- "external Jerry community members fulfill the evaluator requirement" -- compounds the problem. There is no mechanism to identify, contact, brief, or confirm participation from these "external community members." The entire pre-launch quality gate rests on a human coordination dependency with no defined implementation path.

**Evidence:**
1. The specification references "Jerry community contributor pool" without defining membership, size, or how to access it
2. Wave 1 is the first sub-skill launch; no sub-skill evaluation has occurred before it -- condition (b) is impossible to satisfy for Wave 1 specifically
3. The directory structure contains no `EVALUATOR-REGISTRY.md`, contributor onboarding guide, or any artifact that would operationalize this pool

**Impact:** If this finding stands, the pre-launch validation AC is unverifiable. The specification commits to a quality gate that cannot be executed as written. A reviewer or approver who asks "show me the three evaluators and their prior evaluation records" before merge will find nothing. This is not a documentation gap -- it is an execution gap: the gate is stated but the mechanism to execute it does not exist.

**Dimension:** Methodological Rigor

**Response Required:** Define the evaluator pool operationally with one of:
(a) A concrete bootstrap path: for Wave 1 specifically, evaluators must be identified and onboarded as part of Wave 1 pre-launch, with a named individual responsible for recruitment. The "at least one prior evaluation" requirement must be waived for Wave 1 OR bootstrapped via a calibration exercise before Wave 1 launch.
(b) An explicit acknowledgment that the evaluator requirement is bootstrapped from zero at Wave 1, with the specific mechanism for satisfying it (e.g., "evaluators will be recruited via [named channel] and trained via a calibration artifact included with the pre-launch validation package").
(c) Reduction to a simpler, achievable standard for Wave 1: the author uses the external validation mechanism against published reference artifacts (Nielsen Norman Group, Intercom Playbook), without requiring three community evaluators that do not yet exist.

**Acceptance Criteria:** The AC must either (1) define the evaluator recruitment mechanism and bootstrap path explicitly, naming who is responsible for operationalizing the pool before Wave 1 merge, OR (2) replace the community evaluator requirement with a Wave 1-executable alternative that does not depend on a pool that does not exist.

---

### DA-002-I5: Part-Time UX Table Contradiction and Missing Wave 1 Anchor [CRITICAL]

**Claim Challenged:**

Two related claims:
1. From the segment table: "MEDIUM -- Kano and HEART may exceed part-time capacity; prioritize Wave 1-2 only" (Part-time UX Portfolio Fit column)
2. From paragraph below: "Part-time UX (20-50% allocation) is the most common segment based on Gartner's Tiny Teams research. Each wave's entry criteria and time estimates are calibrated for this median case."
3. From Wave 1 time-to-first-value: "estimated 2-4 hours including setup"
4. From Estimated Scope: "Total estimated effort for full V1 (10 sub-skills): ~30-50 days"

**Counter-Argument:** The most important reader of this specification -- the Part-time UX practitioner -- encounters the segment table before reading the paragraph that redeems it. The table is a scanning artifact: reviewers read tables before paragraphs, especially in long technical specifications. The table tells this reader "MEDIUM fit" before the document has had a chance to argue otherwise. The paragraph's claim that Part-time UX is the "primary design center" directly contradicts the table's MEDIUM rating, but the contradiction is resolved only if the reader reads both in sequence and reconciles them -- a cognitive burden the specification places on the reader rather than on itself.

Simultaneously, the 30-50 day total in Estimated Scope is the most prominent scope signal in the document. It appears in a section called "Estimated Scope" and is the only labeled total figure. The Wave 1 time-to-value paragraph provides a 2-4 hour first-output estimate but does not anchor it to the bounded Wave 1 commitment (8-13 days). A reader who encounters "30-50 days" first will apply that as their adoption calculus; without an explicit counter-anchor, the 2-4 hour figure is read as "2-4 hours before a 30-50 day journey," not "2-4 hours within an 8-13 day bounded commitment." This distinction changes the adoption decision.

The steelman (SM-001-I5, SM-002-I5) has identified both gaps across two full iterations. Both have been partially addressed -- the paragraph was added (R4-fix), the time-to-value sentence was added (R4-fix) -- but the structural fixes are not yet incorporated: the table still shows MEDIUM, and the Wave 1 anchor against the 30-50 day total is still absent from the time-to-value paragraph.

**Evidence:**
1. Line 83 (segment table, Part-time UX row): "MEDIUM -- Kano and HEART may exceed part-time capacity; prioritize Wave 1-2 only"
2. Line 85 (paragraph): "Part-time UX (20-50% allocation) is the most common segment... calibrated for this median case" -- paragraph and table give incompatible signals
3. Line 89 (time-to-value): "estimated 2-4 hours including setup. This estimate will be validated during pre-launch testing" -- no mention of Wave 1 as 8-13 days, no counter to the 30-50 day total
4. Line 1168 (Estimated Scope): "Total estimated effort for full V1 (10 sub-skills): ~30-50 days" -- the only labeled total figure, no contextual anchor pointing to Wave 1's 8-13 day bounded commitment

**Impact:** The Part-time UX reader encounters two contradictory quality signals and no clear resolution path within the scanning-optimized content they process first. If this reader's initial impression is "MEDIUM fit, 30-50 days," the skill is rejected before the persuasion case is made. This is not a stylistic issue -- it is the primary conversion failure mode for the primary audience.

**Dimension:** Evidence Quality / Actionability

**Response Required:**
1. Fix the Part-time UX Portfolio Fit cell to read: "HIGH for Wave 1-2 (designed for this segment); MEDIUM for Wave 3-5 (Kano and HEART may exceed part-time capacity)"
2. Update the Wave 1 time-to-value paragraph to include explicit anchor: "Wave 1 is an 8-13 day bounded commitment. The 30-50 day total is for all 5 waves of the full V1 portfolio; Wave 1 stands alone as a meaningful delivery unit. From KICKOFF-SIGNOFF.md (approximately 20 minutes) to first heuristic findings: estimated 2-4 hours."

**Acceptance Criteria:** (1) The Part-time UX row in the segment table does not use a single combined MEDIUM rating that covers Waves 1-5 together; it distinguishes Wave 1-2 fit (HIGH) from Wave 3-5 fit (MEDIUM). (2) The time-to-value paragraph explicitly references Wave 1's 8-13 day scope as distinct from the 30-50 day total.

---

### DA-003-I5: Memory-Keeper Failure at Session Start Has No Recovery Protocol [MAJOR]

**Claim Challenged:**
> "The `ux-orchestrator` uses Memory-Keeper for wave progress persistence across sessions. Key pattern: `jerry/{project}/user-experience/{wave-N-status}`. Stores: wave signoff status, completed sub-skill outputs, MCP connection registry state."

**Counter-Argument:** The Cross-Session State section specifies Memory-Keeper as the persistence mechanism for wave status, hypothesis backlogs, and MCP registry state. The MCP integration section documents a fallback hierarchy (non-MCP workflow on MCP failure). But there is no documented recovery protocol for Memory-Keeper failure itself. If Memory-Keeper is unavailable at session start, the orchestrator cannot retrieve wave signoff status. The orchestrator's wave enforcement logic depends on this state: if Memory-Keeper returns empty, does the orchestrator treat all waves as PASS, BLOCK, or present an error?

The MCP standards (`mcp-tool-standards.md`) specify a fallback for Memory-Keeper retrieve failure: "proceed without prior context and note gap." But this fallback is designed for general agents, not for a wave-gated orchestrator where wave status is the gate. An orchestrator that "proceeds without prior context" when Memory-Keeper fails will route the user as if no waves have been completed -- equivalent to a BLOCK state on every wave except Wave 1. For a team at Wave 4, a silent Memory-Keeper failure appears identical to the skill being broken.

**Evidence:**
1. Cross-Session State table: `jerry/{project}/user-experience/wave-{N}-status` key -- no failure mode entry
2. MCP integration failover table documents failover for Figma, Miro, Storybook, Zeroheight, Hotjar, Whimsical -- Memory-Keeper is not in the MCP integration failover table because it is classified as an orchestration tool, not a design-tool MCP
3. No `mcp-runbook.md` for Memory-Keeper is included in the Directory Structure (only design-tool MCPs have runbooks)
4. Orchestrator failure modes AC (line 804) covers "(a) MCP connection failure -- graceful degradation", "(b) BLOCK state encountered", "(c) Cross-framework partial failure" -- Memory-Keeper failure is not in this enumeration

**Impact:** If Memory-Keeper fails silently, the orchestrator either (a) treats the team as Wave 1 despite being at Wave 4, blocking all access to sub-skills the team has already earned, or (b) allows free routing as if all waves are PASS, defeating the enforcement mechanism. Either outcome undermines user trust in the skill. The most likely experienced scenario -- "the skill forgot my progress" -- will be interpreted as a bug, not a documented limitation.

**Dimension:** Completeness

**Response Required:** Add a Memory-Keeper failure recovery protocol to the Orchestrator Failure Modes AC: "(d) Memory-Keeper unavailable at session start -- orchestrator falls back to filesystem wave state: reads `WAVE-{N}-SIGNOFF.md` directly from the repository to determine wave status; if no SIGNOFF.md files found, orchestrator presents the team with a state recovery checklist listing all completed waves from user declaration, with a warning that the session is operating without cross-session memory until Memory-Keeper reconnects."

**Acceptance Criteria:** The Orchestrator Failure Modes AC explicitly addresses Memory-Keeper unavailability with a named fallback behavior that does not result in silent state loss or incorrect wave enforcement.

---

### DA-004-I5: Adversarial Validation "Survived" Claim Without Specific Corrections (Third Iteration) [MAJOR]

**Claim Challenged:**
> "The trust argument: not that the analysis is perfect, but that it has been systematically attacked from nine different angles and survived. The selection is not '10 highest-scoring frameworks' -- it is a deliberately non-redundant portfolio where each framework fills a unique lifecycle niche, validated through three independent non-redundancy properties..."

**Counter-Argument:** "Systematically attacked and survived" is a process claim, not a quality evidence claim. A reviewer can accept that the tournament ran nine strategies across four iterations while still asking the harder question: "did any of the attacks change anything material, or did the specification merely absorb critique without substantive correction?" This question is unanswerable from the current text because the adversarial validation section names strategies and iteration counts but provides no specific examples of what was wrong before the tournament and what was corrected as a result.

The steelman (SM-003-I5) identified this gap three iterations ago and documented three categories of specific corrections with verifiable R-annotation evidence: five arithmetic errors with changed framework rankings, a design contradiction in `/ux-behavior-design` resolved by renaming and reclassifying the output, and four enforcement closure gaps. These corrections are verifiable in the document's R1-R4 annotations. Not a single one of them is mentioned in the Adversarial Validation section. The section as written would be unchanged if the tournament had run zero corrections vs. thirteen -- the text is process-complete but outcome-silent.

**Evidence:**
1. Lines 966-978 (Adversarial Validation): The section lists iteration count (8), revision count (13), strategies applied, error correction rounds (5), and key findings resolved (13) in a summary table -- but the findings resolved cell says "13 P0 Critical findings across all iterations" without naming a single one
2. R2-fix annotations in the document body contain: "CV-003 Corrected from 9.25 to source-verified 9.05", "CV-004 Corrected from 7.45 to source-verified 7.60", "FM-011 Renamed 'design intervention recommendations' to 'Reference Intervention Patterns'", "FM-001-I3 Defined wave enforcement 3-state behavior" -- these are exactly the specific corrections SM-003-I5 proposed documenting, but they are in the body, not the validation section
3. Third consecutive iteration without incorporating SM-003 findings: this finding has been present in Iter3 (persistent), Iter4 (persistent), now Iter5

**Impact:** The adversarial validation section is the specification's primary credibility argument. If the credibility argument says "trust us, it was attacked" without saying "here is what was wrong and what we fixed," the argument fails the standard it sets for itself. A peer reviewer encountering this specification for the first time has no way to assess whether the tournament produced substantive corrections or ceremonial iteration.

**Dimension:** Evidence Quality / Traceability

**Response Required:** Add a "What the tournament changed" paragraph to the Adversarial Validation section documenting at minimum three specific corrections with:
- The original state (what was wrong before)
- The correction applied (what was changed)
- The specific evidence source (R-annotation reference or strategy finding ID)

**Acceptance Criteria:** The Adversarial Validation section includes at least three named, specific corrections with before/after states and R-annotation evidence trail, making the "13 P0 Critical findings resolved" cell verifiable rather than asserted.

---

### DA-005-I5: Blind Evaluation Rubric Threshold and Dimensions Stated Without Derivation (Second Iteration) [MAJOR]

**Claim Challenged:**
> "Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions."

**Counter-Argument:** The pre-launch blind evaluation rubric is the most consequential quality enforcement mechanism in the specification. It is the gate that determines whether the skill ships. But the 15% threshold is stated as a bare number with no derivation: why 15% and not 10% (more demanding) or 25% (more permissive)? Why completeness, actionability, and time-to-insight rather than other dimensions? A reviewer challenging the quality gate can accept the threshold while questioning whether it is appropriate -- and the specification gives them no basis to evaluate that question.

The steelman (SM-004-I5) documented this gap in Iter4 and proposed a derivation: each dimension maps to a named AI output failure mode (completeness = omission bias, actionability = specificity degradation, time-to-insight = efficiency regression), and the 15% threshold is justified as a conservative floor with comparison to permissive and demanding alternatives. This derivation is not present in the document. The second iteration without incorporation.

**Evidence:**
1. Pre-Launch Validation AC (line 857): "Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions" -- standalone assertion
2. The three dimensions (completeness, actionability, time-to-insight) are named but their selection rationale is absent
3. No comparison to alternative thresholds (10% vs 15% vs 25%) to justify why the chosen value is appropriate for a structured methodology tool used to make product decisions

**Impact:** If the rubric appears arbitrary, the entire pre-launch quality gate loses credibility. An approver who asks "why 15%?" receives no answer from the document. An implementing team that falls at 84% (outside 15% threshold on one dimension) has no guidance on whether this is a genuine failure or a threshold calibration problem.

**Dimension:** Methodological Rigor / Evidence Quality

**Response Required:** Add a calibration rationale paragraph after the pass threshold sentence explaining:
- Why each of the three dimensions was selected (each maps to a named failure mode)
- Why 15% is the appropriate threshold (comparison to permissive/demanding alternatives)
- What recalibration trigger applies if empirical data challenges the threshold

**Acceptance Criteria:** The three evaluation dimensions each have a named rationale for their inclusion. The 15% threshold includes a comparison to at least one more permissive and one more demanding alternative with explanation of why the chosen value is appropriate for this tool's use case.

---

### DA-006-I5: Crisis Mode Bypasses Wave Enforcement Without a Defined Exception Path [MAJOR]

**Claim Challenged:**
> "Handles crisis mode -- emergency 3-skill sequence (Heuristic Eval -> Behavior Design -> HEART) for products with urgent UX problems."
> "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills..."

**Counter-Argument:** The crisis mode 3-skill sequence routes through three waves (Heuristic Eval = Wave 1, Behavior Design = Wave 4, HEART = Wave 2). A team invoking crisis mode that is at Wave 1 with WAVE-1-SIGNOFF.md incomplete would be blocked from accessing Behavior Design (Wave 4) and potentially HEART (Wave 2) by the wave enforcement BLOCK state. The specification defines both crisis mode and BLOCK state activation but does not define how they interact. The BLOCK state definition is absolute: "Orchestrator refuses to route to Wave N+1 sub-skills." Crisis mode does not appear in the exceptions list.

This is not a theoretical edge case. Crisis mode is explicitly triggered by "urgent UX problems" -- exactly the scenario where a team that has not completed wave progressions is most likely to need help. A team with a product launch in 48 hours and zero wave completions is the platonic crisis mode user. The BLOCK state prevents them from using the tool for its stated crisis-mode purpose.

**Evidence:**
1. Key Design Decisions #2 (line 431): crisis mode activates "when the user explicitly describes urgency ('urgent', 'critical UX issue', 'users are leaving') or when the orchestrator detects multiple prior sub-skill invocations without resolution" -- no wave prerequisites mentioned
2. Key Design Decisions #5 (line 640): "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills" -- absolute refusal with no exceptions
3. The wave stall bypass (line 642) covers planned stalls ("2+ sprint cycles") but not crisis activation
4. Behavior Design (Wave 4) requires Wave 3 completion. HEART (Wave 2) requires Wave 1 completion. A team invoking crisis mode at Wave 0 would be blocked from both.

**Impact:** Crisis mode will fail for its primary use case: teams without wave completion history who have an urgent UX problem. The skill will refuse to provide emergency guidance precisely when the user has the greatest need and the least patience to navigate a BLOCK state resolution path.

**Dimension:** Internal Consistency

**Response Required:** Define a crisis mode exception in the wave enforcement section:
- Either: crisis mode activates a temporary BYPASS that skips BLOCK state enforcement for the 3-skill emergency sequence, with the bypass logged to `work/audit/override-log.md` under the existing Human Override Audit mechanism
- Or: crisis mode is scoped to work within whatever waves the team has completed (e.g., crisis mode at Wave 1 routes to "Heuristic Eval only"; crisis mode at Wave 2+ adds HEART to the sequence)

**Acceptance Criteria:** The wave enforcement section explicitly addresses how crisis mode interacts with BLOCK state. The interaction is not a logical contradiction in the specification.

---

### DA-007-I5: BLOCK State Lacks Orchestrator Message Template [MINOR]

**Claim Challenged:**
> "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process."

**Counter-Argument:** The BLOCK state describes the orchestrator's behavior ("refuses to route... directs user to complete") without providing the actual message the orchestrator produces. A user encountering a BLOCK state sees only that the skill is not routing them where they want to go. Without an explicit message that names the missing file, the template location, and the bypass path, the BLOCK state is indistinguishable from a broken skill. The steelman (SM-005-I5) has identified this gap for the second consecutive iteration.

**Evidence:**
1. Line 640: BLOCK state describes the behavior but provides no message text or resolution path in user-facing terms
2. The PASS and WARN states both have described behaviors but no message templates either; BLOCK is the highest-friction state and the most in need of a concrete message

**Impact:** Users experiencing a BLOCK state will, with high probability, interpret it as a bug rather than a guardrail. They will either open an issue against the skill or abandon it.

**Dimension:** Completeness / Actionability

**Response Required:** Add a concrete BLOCK state message template showing the content the orchestrator produces when blocking wave progression, including the specific resolution path (missing file name, template location, bypass invocation syntax).

**Acceptance Criteria:** The BLOCK state definition includes an example message template that a user would find actionable, not just a description of the behavior.

---

### DA-008-I5: Haiku Model Assignment for Heuristic Evaluation Treated as Fixed Rather Than Testable Hypothesis [MINOR]

**Claim Challenged:**
> "haiku | Heuristic Evaluation | Checklist-based systematic evaluation against 10 discrete heuristics; procedural, not reasoning-intensive"

**Counter-Argument:** The haiku assignment characterizes heuristic evaluation as "procedural, not reasoning-intensive." This is accurate for severity-0 through severity-2 violations, which are mechanical checklist matches (missing error message, absent feedback, navigation not visible). However, severity-3 and severity-4 violations -- which are the most valuable findings for experienced UX practitioners -- require contextual inference. H4 (Consistency and Standards) violations require cross-platform knowledge; H7 (Flexibility and Efficiency) violations require user population judgment. These are non-trivial reasoning tasks.

The steelman (SM-009-I5) identified this risk as a new finding in Iter5. Since heuristic evaluation is the first sub-skill teams use (Wave 1), a quality regression on high-severity violations would undermine confidence in the entire wave progression model. A team whose first experience with the skill is haiku-generated heuristic findings that miss severity-4 violations will not proceed to Wave 2.

**Evidence:**
1. Line 1198: haiku assignment rationale is "procedural, not reasoning-intensive" -- this characterizes the entire heuristic evaluation task without distinguishing violation severity levels
2. The quality benchmark AC (identifies >= 7 of 10 known violations) does not specify whether the reference design's violations are severity-0/1/2 or include severity-3/4 violations -- making the benchmark weaker than it appears

**Impact:** If haiku does not reliably identify severity-3/4 violations, Wave 1's quality benchmark (>= 7 of 10) may be achievable while still missing the most valuable findings. Teams would pass the benchmark while receiving structurally incomplete evaluation reports.

**Dimension:** Methodological Rigor

**Response Required:** Add a validation hook to the model selection rationale: if the quality benchmark calibration test shows < 50% of correctly-identified violations are severity-3 or severity-4, upgrade to sonnet and re-run the calibration. Also add a severity distribution requirement to the quality benchmark AC: "The 7+ violations identified MUST include at least 2 severity-3 or severity-4 violations."

**Acceptance Criteria:** The haiku assignment is treated as a cost-optimization hypothesis to be validated rather than a fixed design choice. The quality benchmark AC includes a severity distribution requirement.

---

### DA-009-I5: Service Blueprinting V2 P1 Priority Lacks Dual-Purpose Justification [MINOR]

**Claim Challenged:**
> "P1 | No service design coverage | `/ux-service-blueprinting` (rank #12, score 7.40) | Covers end-to-end service process niche; also the auto-substitute if AI-First Design Enabler expires"

**Counter-Argument:** A reviewer scanning the V2 table sees Service Blueprinting ranked P1 with a 7.40 score. Other V2 candidates at P1 (user-research, dark-patterns-audit, algorithmic-bias-review) have clearer P1 rationale -- user research is explicitly the "single largest portfolio gap," dark patterns and algorithmic bias close explicitly named ethics gaps. Service Blueprinting's P1 rank against a 7.40 score requires explanation. The "also the auto-substitute" clause does the explanatory work but reads like a parenthetical rather than the primary justification. The substitution path is the reason Service Blueprinting has pre-approved P1 status; without this being the headline justification, the apparent inconsistency remains.

**Evidence:**
1. Line 905: Service Blueprinting P1 description ends with "also the auto-substitute if AI-First Design Enabler expires" -- the word "also" frames the substitution path as secondary when it is the primary P1 driver
2. The Known Limitations section (line 750) confirms the substitution path: "If the AI-First Design Enabler has not achieved its validation gate by Wave 5, Wave 5 delivers Design Sprint only; Service Blueprinting is a V2 P1 candidate" -- the Known Limitations reference is the canonical home for this commitment, but it does not explain why this pre-commitment elevates Service Blueprinting to P1

**Impact:** A reviewer may question the V2 prioritization methodology or interpret Service Blueprinting's P1 rank as an error. Minor but addressable.

**Dimension:** Traceability

**Response Required:** Revise the Service Blueprinting V2 description to lead with the dual-purpose justification: primary P1 because it is the pre-committed substitution path if AI-First Design Enabler expires (no further prioritization debate needed); secondary P1 because it fills the service design lifecycle gap.

**Acceptance Criteria:** The Service Blueprinting P1 row description explains why a 7.40-score framework ranks P1 without requiring the reader to connect it to a footnote in Known Limitations.

---

## Response Requirements

### P0 (Critical -- MUST resolve before acceptance)

**DA-001-I5: Pre-Launch Evaluator Pool Bootstrap Gap**
- **Required:** Define the Wave 1 evaluator recruitment mechanism. Name who is responsible, how evaluators will be identified and onboarded, and whether condition (b) ("completed at least one prior sub-skill evaluation") is waived or bootstrapped for Wave 1.
- **Acceptance Criteria:** The Pre-Launch Validation AC is executable as written by the implementing team without requiring a community pool that does not yet exist.

**DA-002-I5: Part-Time UX Table Contradiction + Wave 1 Anchor**
- **Required:** (1) Fix the Part-time UX segment table Portfolio Fit cell to distinguish Wave 1-2 (HIGH) from Wave 3-5 (MEDIUM). (2) Update the time-to-first-value paragraph to anchor "2-4 hours" against Wave 1's 8-13 day scope rather than the 30-50 day total.
- **Acceptance Criteria:** A Part-time UX reader scanning the table gets a HIGH signal for their primary use case. The time-to-value paragraph explicitly counters the 30-50 day total apprehension.

### P1 (Major -- SHOULD resolve; require justification if not)

**DA-003-I5: Memory-Keeper Failure Recovery**
- **Required:** Add a Memory-Keeper unavailability scenario to the Orchestrator Failure Modes AC with a named fallback (filesystem SIGNOFF.md as recovery path).
- **Acceptance Criteria:** Four failure modes enumerated in the AC, with Memory-Keeper failure explicitly covered.

**DA-004-I5: Adversarial Validation Specific Corrections**
- **Required:** Add a "What the tournament changed" paragraph with three specific named corrections.
- **Acceptance Criteria:** Adversarial validation section is verifiable, not just process-asserted.

**DA-005-I5: Rubric Calibration Rationale**
- **Required:** Add derivation for 15% threshold and 3-dimension selection.
- **Acceptance Criteria:** Each dimension has a named rationale; threshold has comparison to alternatives.

**DA-006-I5: Crisis Mode / BLOCK State Interaction**
- **Required:** Define whether crisis mode activates a bypass of BLOCK state, or is scoped to available waves.
- **Acceptance Criteria:** Crisis mode and BLOCK state do not produce a logical contradiction in the specification.

### P2 (Minor -- MAY resolve; acknowledgment sufficient)

**DA-007-I5:** Add BLOCK state message template. Acknowledgment: if deferred, note that message template will be defined during Wave 1 implementation AC delivery.

**DA-008-I5:** Add haiku validation hook and severity distribution requirement to quality benchmark AC. Acknowledgment: if deferred to implementation, note that haiku assignment is a cost-optimization hypothesis subject to calibration.

**DA-009-I5:** Lead Service Blueprinting description with dual-purpose justification. Acknowledgment sufficient.

---

## Tracking: RESOLVED vs PERSISTENT from Iter4

### Resolved in R4 (confirmed by R4-fix annotations)

| Iter4 ID | Finding | R4 Resolution | Status |
|----------|---------|---------------|--------|
| DA-001-I4 | Design Sprint AI capability over-claims | R4-fix: "qualified as design targets, not verified capabilities" added to Design Sprint What AI Does section; "20+" claim removed from Capability Map | RESOLVED |
| DA-002-I4 | Wave 5 unreachable for part-time median user | R4-fix: "Part-time time commitment" qualification added; Wave 5 made optional | RESOLVED |
| DA-003-I4 | ux-orchestrator undocumented failure modes | R4-fix: Orchestrator Failure Modes AC added with (a) MCP failure, (b) BLOCK state, (c) cross-framework partial failure | RESOLVED (but Memory-Keeper gap = DA-003-I5 new finding) |
| DA-004-I4 (evaluator infeasibility -- prior iteration) | 3-independent-evaluators requirement | R4-fix: Added community contributor pool and < 3-person team path | PARTIALLY RESOLVED -- bootstrap gap persists = DA-001-I5 |
| RT-005-I4 (solo practitioner) | Solo practitioner fit not distinguished by wave | R4-fix: Solo practitioner row qualified with Wave 1-3 HIGH, Wave 4-5 caveat | RESOLVED |
| CV-001-I4, CV-002-I4 | Cost tier arithmetic errors | R4-fix: Figma plan name corrected; Full Enhancement cost tier recalculated with component breakdown | RESOLVED |
| FM-009-I4 | Zeroheight/Whimsical MCP pre-commitment absent | R4-fix: Wave 3 MCP Pre-Commitment section added as binding entry criterion | RESOLVED |
| RT-003-I4 | P-003 CI enforcement not specified | R4-fix: CI validation specification added to P-003 Task exclusion AC | RESOLVED |
| RT-004-I4, IN-002-I4 | Human override audit log not structured | R4-fix: 4-field audit log format added; persisted to `work/audit/override-log.md` | RESOLVED |

### Persistent (not resolved in R4, escalated as Iter5 findings)

| Iter4 ID | Iter5 ID | Status Change |
|----------|----------|---------------|
| SM-001-I4 (Critical: Part-time UX table contradiction) | DA-002-I5 (Critical) | Partially incorporated -- paragraph added but table not fixed; wave anchor absent |
| SM-002-I4 (Critical: Wave 1 time-to-value anchor) | DA-002-I5 (Critical) | Partially incorporated -- 2-4 hour sentence added but Wave 1 anchor missing |
| SM-003-I4 (Major: adversarial validation process vs. outcome) | DA-004-I5 (Major) | Third iteration without incorporation |
| SM-004-I4 (Major: rubric calibration rationale) | DA-005-I5 (Major) | Second iteration without incorporation |
| DA-006-I3/I4 (Major: crisis mode vs. BLOCK conflict) | DA-006-I5 (Major) | Not resolved in R4 |
| SM-005-I4 (Minor: BLOCK state message template) | DA-007-I5 (Minor) | Second iteration without incorporation |

### New Findings (Iter5-specific)

| ID | Source | Note |
|----|--------|------|
| DA-001-I5 | New finding surfaced by R4's evaluator qualification addition | R4's community pool language creates a bootstrap impossibility not present before R4 |
| DA-003-I5 | New finding surfaced by R4's Memory-Keeper addition | R4's Cross-Session State section creates a new failure mode gap |
| DA-008-I5 | Persistent from SM-009-I5 (Steelman Iter5) | Haiku severity distribution risk -- first appearance in DA series |
| DA-009-I5 | Persistent from SM-007-I5 (Steelman Iter5) | Service Blueprinting dual-purpose justification -- first appearance in DA series |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | DA-003-I5: Memory-Keeper failure mode gap in an otherwise comprehensive failure modes section; DA-007-I5: BLOCK state lacks message template. R4 additions expanded scope but created new coverage gaps. |
| Internal Consistency | 0.20 | Negative | DA-002-I5: Part-time UX table vs. paragraph contradiction unresolved for third iteration; DA-006-I5: crisis mode and BLOCK state are logically incompatible without an explicit exception path |
| Methodological Rigor | 0.20 | Negative | DA-001-I5: Pre-launch quality gate unexecutable as written (bootstrapping impossibility); DA-005-I5: rubric threshold without derivation second iteration; DA-008-I5: haiku assignment treated as fixed rather than testable |
| Evidence Quality | 0.15 | Negative | DA-002-I5: primary audience segment receives contradictory evidence from table vs. paragraph; DA-004-I5: adversarial validation provides process evidence, not outcome evidence -- third iteration |
| Actionability | 0.15 | Negative | DA-001-I5: evaluator pool AC is unexecutable without defined bootstrap path; DA-002-I5: Wave 1 anchor absent means adoption calculus defaults to 30-50 day total; DA-006-I5: crisis mode produces undefined behavior at BLOCK boundary |
| Traceability | 0.10 | Negative | DA-004-I5: 13 P0 Critical findings claimed as resolved but none are named/traceable in the validation section; DA-009-I5: Service Blueprinting P1 rationale requires reader to connect disparate sections |

**Overall Assessment:** REVISE. Two Critical findings require resolution before merge: DA-001-I5 (evaluator pool bootstrap impossibility) is a new gap introduced by R4 that makes the pre-launch quality gate unexecutable; DA-002-I5 (Part-time UX table contradiction + Wave 1 anchor gap) is a persistent gap across three iterations that systematically under-serves the primary audience. Four Major findings (DA-003-I5, DA-004-I5, DA-005-I5, DA-006-I5) are addressable without structural rework and represent meaningful quality improvements. The specification's core architecture remains sound; R4 addressed all three prior Critical findings genuinely. The remaining gap is argument-completeness and execution-validity, not fundamental design error.

---

## Execution Statistics

- **Total Findings:** 9
- **Critical:** 2 (DA-001-I5, DA-002-I5)
- **Major:** 4 (DA-003-I5, DA-004-I5, DA-005-I5, DA-006-I5)
- **Minor:** 3 (DA-007-I5, DA-008-I5, DA-009-I5)
- **Protocol Steps Completed:** 5 of 5
- **Iter4 Criticals Resolved:** 3 of 3 (DA-001-I4, DA-002-I4, DA-003-I4)
- **New Iter5 Criticals:** 2 (DA-001-I5 new from R4 addition, DA-002-I5 persistent escalated)
- **Persistent Majors (3+ iterations):** 1 (DA-004-I5 / SM-003)
- **Persistent Majors (2 iterations):** 2 (DA-005-I5 / SM-004, DA-006-I5 / crisis-BLOCK conflict)
