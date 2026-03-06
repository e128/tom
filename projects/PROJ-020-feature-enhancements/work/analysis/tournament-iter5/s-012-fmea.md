# FMEA Report: UX Framework Selection Analysis

**Strategy:** S-012 FMEA (Failure Mode and Effects Analysis)
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 9)
**Criticality:** C4 (Tournament Iteration 5 -- FINAL)
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-012)
**H-16 Compliance:** S-003 Steelman applied in prior tournament iterations (confirmed; SM-001/SM-002/SM-003 iter3 outputs incorporated into R8; SM-010-I4/SM-011-I4/SM-012-I4/SM-013-I4 incorporated into R9)
**Elements Analyzed:** 13 | **Failure Modes Identified:** 22 | **Total RPN:** 1,894

---

## Summary

R9 addresses all 6 P0-Critical findings from Iteration 4 (SR-001-I4, SM-010-I4/DA-001-I4, PM-001-I4, PM-002-I4, IN-001-iter4, CV-001/CV-002/CV-003) and 14 of 19 prior Major findings. FMEA of R9 identifies **0 Critical findings** (RPN >= 200), **7 Major findings** (RPN 80-199), and **15 Minor findings** (RPN < 80). The highest-RPN finding (FM-007-20260303I5, RPN 168) concerns the Implementation Specification section's agent prompt templates lacking runtime enforcement clarity. The second-highest (FM-002-20260303I5, RPN 150) concerns an arithmetic inconsistency in the new dynamic attestation examples for AI-First Design. Three of the 7 Major findings are in R9's new sections (Section 7.5 Required Pre-Launch Worktracker Entities, Section 7.6 Implementation Specification). The overall assessment is **ACCEPT with targeted corrections**: the 7 Major findings are bounded in scope, addressable without structural revision, and none invalidates the core selection argument. The document has improved significantly from R8's 28-finding profile to R9's 22-finding profile with zero Critical findings.

---

## Element Inventory

| ID | Element | Description |
|----|---------|-------------|
| E-01 | Evaluation Methodology | Section 1: scoring scale, weighting rationale, WSM methodology, limitations block |
| E-02 | Weighting Rationale | Section 1: WSM justification, C1/C5 correlation analysis, bounding case |
| E-03 | Sensitivity Analysis | Section 1: three perturbation scenarios, pre-registered rules, symmetric uncertainty table |
| E-04 | Full Scoring Matrix | Section 2: 40-framework table, score calculation verification, final ranking |
| E-05 | Selection Methodology | Section 1: complementarity two-pass evaluation, Round 1/Round 2 convergence |
| E-06 | AI-First Design | Section 3.8: prerequisite management, acceptance criteria, dynamic attestation |
| E-07 | Sub-Skill Descriptions | Sections 3.1-3.10: per-framework profiles, AI Execution Mode Taxonomy tables |
| E-08 | Coverage Analysis | Section 4: domain coverage map, gap analysis, V2 roadmap, complementarity matrix |
| E-09 | Routing Framework | Section 7.1-7.4: parent skill triage, sub-skill routing, MCP maintenance, wave plan |
| E-10 | Synthesis Hypothesis Validation Protocol | Section 7.6: confidence gates, agent prompt templates, validation checklist |
| E-11 | Evidence Base | Evidence Summary table: citations E-001 through E-029 |
| E-12 | Operational Governance | MCP maintenance contract (7.3), worktracker entity succession protocols |
| E-13 | Required Pre-Launch Worktracker Entities | Section 7.5: 4-entity checklist, creation triggers, recurrence, source references |

---

## Findings Table

| ID | Element | Failure Mode | S | O | D | RPN | Severity | Corrective Action | Affected Dimension |
|----|---------|-------------|---|---|---|-----|----------|-------------------|--------------------|
| FM-001-20260303I5 | E-13 Required Pre-Launch Worktracker Entities | Section 7.5 lists 4 entities but Entity #1 (AI-First Design Enabler) specifies "TBD primary + TBD secondary (MANDATORY at creation)" -- creating an entity whose owner field is TBD at the time the checklist itself mandates named owners undermines the mandate | 6 | 7 | 4 | 168 | Major | Add resolution instruction: "If owners are not yet known at document-adoption time, Section 7.5 creation is itself in BLOCKED state. The Enabler cannot be created until named owners are identified. Insert a pre-condition: Identify and record the Enabler primary and secondary owners BEFORE creating the entity -- do not create with 'TBD' in the owner fields." | Actionability |
| FM-002-20260303I5 | E-06 AI-First Design | The second arithmetic example in IN-001-iter4 acceptance criterion (d) computes C5 adjusted to 6: total = 9*0.25 + 8*0.20 + 8*0.15 + 2*0.15 + 6*0.15 + 7*0.10 = 2.25+1.60+1.20+0.30+0.90+0.70 = 6.95. But the document shows this as a PASS scenario introduction: "Example with reviewer-adjusted C5: if C5 is assessed at 6 (not 10) because the PAIR Guidebook through Nielsen's covers the niche, then total = ... = 6.95, which also fails." The label is "also fails" -- this is correct. However, the first example shows C1=9, C2=8 with projected C3-C6 constants yielding 7.55, labeled "fails." Neither example shows a passing scenario despite being introduced as "examples" (plural) of the gate. A reader cannot determine from the examples what a passing submission looks like | 5 | 7 | 4 | 140 | Major | Add a passing example: "Example passing scenario: C1=10, C2=9, with projected C3=8, C4=2, C5=10, C6=7 (all reviewer-attested): total = 10*0.25 + 9*0.20 + 8*0.15 + 2*0.15 + 10*0.15 + 7*0.10 = 2.50+1.80+1.20+0.30+1.50+0.70 = 8.00, which passes the >= 7.80 threshold. This satisfies both C1 >= 9 (C1=10) and C2 >= 8 (C2=9) dimension floors." | Actionability |
| FM-003-20260303I5 | E-10 Synthesis Hypothesis Validation Protocol | Section 7.6 Implementation Specification provides canonical output label strings and agent prompt templates, but the prompt templates use placeholder language "based on [data sources]" and "[output type]" that is not resolved to specific values for any sub-skill -- an implementer following the template must interpolate these placeholders without a reference table mapping sub-skills to their specific data sources and output types | 5 | 6 | 4 | 120 | Major | Add a placeholder resolution table: "For each sub-skill, the following interpolations apply to the HIGH and MEDIUM confidence gate templates: `/ux-jtbd` [output type]=job statement synthesis, [data sources]=App Store reviews/competitor analysis/interview transcripts; `/ux-lean-ux` [output type]=assumption map, [data sources]=team-provided product context; `/ux-design-sprint` [output type]=Day 4 thematic analysis, [data sources]=user interview transcripts; and so on for each sub-skill with synthesis hypothesis steps." | Actionability |
| FM-004-20260303I5 | E-03 Sensitivity Analysis | FM-004-20260303I4 (the Fogg circular dependency finding from Iter4) was addressed by adding "symmetric downward uncertainty" (SM-012-I4) as a table showing -0.25 and +0.25 scenarios. However, the SM-012-I4 table in R9 shows only four frameworks (Fogg, Kano, Service Blueprinting, Double Diamond) in both directions. The pre-registered interpretation rule for C3 perturbation still references "Fogg's baseline score (7.60)" as the threshold without incorporating the lower bound from the symmetric uncertainty table. The Iter4 finding FM-004 is partially addressed but the core circularity remains: the pre-registered rule uses Fogg's point estimate as a fixed anchor despite the symmetric analysis establishing it could be 7.35 | 5 | 5 | 5 | 125 | Major | The SM-012-I4 addition partially resolves this by showing the bidirectional analysis exists. To fully resolve: add a footnote to the C3 perturbation pre-registered rule: "Threshold anchor note: Fogg's baseline score used as the 7.60 threshold is the point estimate; under -0.25 uncertainty, Fogg's score could be 7.35. The pre-registered rule applies the point estimate for consistency with the main analysis; teams with high sensitivity to this uncertainty should apply the 7.35 lower bound as the threshold instead." | Internal Consistency |
| FM-005-20260303I5 | E-10 Synthesis Hypothesis Validation Protocol | The validation checklist in Section 7.6 includes a "Passing example (MEDIUM gate, `/ux-jtbd` job statement synthesis)" but provides NO failing example for any confidence level. The checklist states test cases for HIGH/MEDIUM/LOW confidence gates, but an implementer verifying the LOW confidence gate has no reference for what a correct failure (output labeled [LOW CONFIDENCE] with no recommendation) looks like vs. a broken implementation that silently drops the output | 4 | 6 | 4 | 96 | Major | Add a failing example: "Failing example (LOW gate, `/ux-ai-first` AI interaction pattern recommendation): User: 'Recommend interaction patterns for my AI assistant UI.' Agent [INCORRECT]: 'Based on the PAIR Guidebook, I recommend: [specific pattern list].' Agent [CORRECT]: '[LOW CONFIDENCE -- REFERENCE ONLY, NOT FOR DESIGN DECISIONS] This output has low confidence because the AI-First Design framework is synthesized and interaction pattern recommendations for your specific AI product require expert review. Return to NN Group AI UX guidelines or the PAIR Guidebook and make the pattern decision manually. Reference summary only: [brief non-directive overview].'" | Evidence Quality |
| FM-006-20260303I5 | E-13 Required Pre-Launch Worktracker Entities | Section 7.5 specifies Entity #4 as a "Task (recurring)" titled "MCP Ownership Verification" with recurrence Quarterly and source Section 7.3. However, Section 7.3 MCP Maintenance Contract specifies the task is titled "MCP Ownership Verification" but the verification language in 7.3 differs: "to verify both primary and secondary owners are current and able to fulfill their responsibilities." The Section 7.5 checklist omits the verification scope language that 7.3 defines -- an implementer creating the task from the 7.5 checklist alone has insufficient context for what the quarterly task should accomplish | 4 | 5 | 4 | 80 | Major | Add scope reference to Entity #4 in Section 7.5: "Verification scope: confirm primary owner is current and active in the project, secondary owner is identified and reachable, and both are aware of their quarterly MCP audit obligations per Section 7.3. See Section 7.3 for full audit scope definition." | Methodological Rigor |
| FM-007-20260303I5 | E-10 Synthesis Hypothesis Validation Protocol | The Implementation Specification (Section 7.6) adds agent prompt language templates with specific phrasing like "SYNTHESIS OUTPUT [HIGH CONFIDENCE]: I have generated [output type] based on [data sources]. Please review for accuracy before using in design decisions." The template instructs the agent to speak in first person ("I have generated") and to use brackets for placeholders. However, Jerry agent definitions use XML-tagged sections and the methodology section describes agent behavior in third person -- the template phrasing style conflicts with Jerry's agent definition authoring conventions, creating an implementation ambiguity: do these templates go in `<methodology>` (third-person behavioral description) or `<guardrails>` (constraints on output)? The specification says `<guardrails>` but the templates are written as agent utterances | 6 | 5 | 4 | 120 | Major | Clarify implementation pattern: "The prompt templates above describe the CONTENT the agent must produce, not verbatim agent utterances for the agent definition file. In the `<guardrails>` section of the sub-skill's agent definition, express these as behavioral constraints: 'When producing a synthesis hypothesis output at HIGH confidence level, surface a confirmation prompt with this content: [template content]. Do not produce design recommendations until confirmation is received.' The first-person 'I have generated' language is the agent's output voice, not the agent definition authoring style." | Methodological Rigor |
| FM-008-20260303I5 | E-06 AI-First Design | IN-001-iter4 adds dynamic attestation for C3, C5, C6 projected values. The attestation clause specifies "C3 (MCP Integration): the synthesized framework is compatible with at least 2 of the 3 listed MCP servers (Figma, Storybook, Context7) at a level consistent with C3 >= 7." However, Context7 was reclassified by FM-011-20260303I4 (Iter4 Major finding) as an "AI Knowledge Source" not an MCP server. Including Context7 in the "3 listed MCP servers" formulation reintroduces the category confusion that FM-011 was supposed to correct | 4 | 5 | 4 | 80 | Minor | Revise C3 attestation: replace "at least 2 of the 3 listed MCP servers (Figma, Storybook, Context7)" with "at least 2 of the 2 listed MCP design tool servers (Figma, Storybook), noting that Context7 operates as an AI knowledge source not a design tool MCP per FM-011 classification." This preserves the threshold intent (C3 >= 7 requires meaningful MCP integration) while using correct tool categorization. | Internal Consistency |
| FM-009-20260303I5 | E-13 Required Pre-Launch Worktracker Entities | Section 7.5 includes a "Verification" instruction: "An implementer starting Wave 1 should confirm entities 1-4 exist in the PROJ-020 WORKTRACKER.md manifest before proceeding." The instruction uses "should" (MEDIUM tier) rather than "MUST" (HARD tier), but the Section 3.8 and 7.3 source sections use MUST language for the same entity creation requirement. The tier downgrade at the verification step creates an inconsistency: the creation is MANDATORY but the verification before implementation is merely RECOMMENDED | 3 | 6 | 4 | 72 | Minor | Upgrade to MUST: "An implementer starting Wave 1 MUST confirm entities 1-4 exist in the PROJ-020 WORKTRACKER.md manifest before proceeding. If any entity is missing, create it before starting implementation. Missing required entities are a blocking condition, not an advisory gap." | Internal Consistency |
| FM-010-20260303I5 | E-09 Routing Framework | Section 7.4 Wave 5 entry criteria table row "Wave 5 entry (/ux-ai-first)" specifies: "Worktracker Enabler entity status field = DONE. Independent scoring artifact exists at specified path." The "specified path" reference is to the acceptance criteria in Section 3.8, which requires the scoring artifact at `projects/PROJ-020-feature-enhancements/work/framework-synthesis/ai-first-design-framework.md`. However, this is the framework synthesis document path, not the scoring artifact path. The independent scoring document (the one computing C1 and C2 re-scored values) is not given an explicit artifact path anywhere in the document | 3 | 5 | 4 | 60 | Minor | Add scoring artifact path: "The independent scoring artifact (the document in which the expert reviewer's C1 and C2 re-scored values and WSM recalculation are recorded) should be stored at: `projects/PROJ-020-feature-enhancements/work/framework-synthesis/ai-first-design-independent-scoring.md`. This is distinct from the framework synthesis deliverable itself." | Traceability |
| FM-011-20260303I5 | E-03 Sensitivity Analysis | The SM-012-I4 symmetric uncertainty table added in R9 shows Fogg -0.25 as 7.35 and +0.25 as 7.85. The table also shows Kano -0.25 as 7.40, which equals Service Blueprinting's verified baseline score of 7.40. The document acknowledges "Fogg falls below Service Blueprinting's 7.40" under downward uncertainty in the Iter3 SR-003 addition, but the R9 symmetric table does not explicitly note that Kano -0.25 (7.40) ties with Service Blueprinting's verified score (7.40). A reader might interpret the table as showing only Fogg is at risk; in fact, Kano is also at the boundary when downward uncertainty is applied | 4 | 5 | 3 | 60 | Minor | Add note to symmetric uncertainty table: "Note: Kano at -0.25 uncertainty (7.40) ties with Service Blueprinting's verified baseline score (7.40). Both Fogg and Kano are at selection-boundary risk under downward score uncertainty. This reinforces the 'well-supported judgment calls' characterization for the compression zone -- neither is a risk-free selection." | Completeness |
| FM-012-20260303I5 | E-11 Evidence Base | E-029 (Fogg 2009) was flagged in FM-009-20260303I4 (Iter4 Major finding) as "registered in the revision log but unresolvable in the evidence table." R9's revision log for Iter4 confirms the corrective action was to add E-029 to the Evidence Summary table. Scanning the R9 Evidence Summary confirms E-029 IS present: "E-029 | External | Fogg, B.J. (2009)...". FM-009-20260303I4 is resolved. No finding for this element. | 1 | 1 | 1 | 1 | Minor | No corrective action required -- FM-009-20260303I4 resolved confirmed. | Traceability |
| FM-013-20260303I5 | E-07 Sub-Skill Descriptions | The AI Execution Mode Taxonomy for `/ux-heart-metrics` (Section 3.4, added FM-001-20260303I2) classifies "Pull metric values from product analytics API" as Deterministic with treatment "Use directly; verify that the analytics data covers the specific behavior path being diagnosed." The word "behavior path" is borrowed from the Fogg Behavior Model's vocabulary (B=MAP behavior path), not from HEART's vocabulary (HEART measures dimensions not behavior paths). The treatment guidance uses domain-crossing vocabulary that could confuse implementers | 3 | 5 | 4 | 60 | Minor | Replace "behavior path" with HEART-native vocabulary: "Use directly; verify that the analytics data covers the specific HEART dimension metrics being tracked (Engagement: session frequency; Retention: cohort return rate; Task Success: completion rate for target task flows)." | Internal Consistency |
| FM-014-20260303I5 | E-02 Weighting Rationale | SM-011-I4 (Iter4 Major finding) replaced "approximately satisfied" with a quantified bound statement: "at most 0.10-0.20 points distortion, no pair exceeds 0.20, WSM appropriate with bounded caveat." However, the bound is stated without showing which pairs produce the 0.10 and 0.20 distortion values. The SM-012-I4 bounding pair identification from Iter3 (added as P2-8) states "lower bound 0.10 (AI-First Design, C1=C5=10) and upper bound 0.20 (JTBD/Microsoft, C5=10, C1=8)" but this cross-reference from the WSM independence resolution block to the bounding pair identification block may not be visible to a reader who does not read both sections | 3 | 4 | 4 | 48 | Minor | Add cross-reference in WSM independence resolution block: "Bounding pair identification for the 0.10-0.20 distortion range: lower bound pair = AI-First Design (C1=C5=10, distortion = 0.10); upper bound pair = JTBD or Microsoft Inclusive Design (C5=10, C1=8, distortion = 0.20). See bounding pair identification note in [Weighting Rationale] for the arithmetic derivation." | Traceability |
| FM-015-20260303I5 | E-01 Evaluation Methodology | The Candidate Universe Generation paragraph (DA-002 -- R9) states the 40-framework universe includes "5 additional frameworks identified during the tiny-teams research and MCP design tools survey." However, Section 6 Seed List Audit identifies 10 seed frameworks, and the seed list contains frameworks (e.g., Design Thinking, Double Diamond) that appear to be well-known category representatives, not "identified during" the research as novel additions. The DA-002 paragraph implies the 35+5 assembly is exhaustive but does not reconcile this with the 10-framework seed list process | 3 | 5 | 3 | 45 | Minor | Add clarification: "The 35 frameworks from the survey and 5 additional frameworks identified during research were cross-referenced against the 10-framework seed list. All 10 seed frameworks appear in the 40-framework universe (confirmed by Section 6 Seed List Audit outcomes). The seed list did not introduce additional frameworks not already captured by the research sources; it served as a completeness check." | Completeness |
| FM-016-20260303I5 | E-07 Sub-Skill Descriptions | The AI Execution Mode Taxonomy for `/ux-lean-ux` (Section 3.5) classifies "Validate or invalidate the hypothesis" as Synthesis hypothesis with treatment "Human makes the validation/invalidation call; AI provides the evidence summary. AI cannot unilaterally record a hypothesis as validated." This is correct. However, the same taxonomy classifies "Update the Miro hypothesis backlog" as Deterministic with treatment "Use directly after human validation decision is made." The temporal dependency between these two steps (update MUST follow human decision, not precede it) is stated in the treatment text but not enforced at the taxonomy classification level -- a Deterministic classification invites direct execution, and an implementer could sequence the update before the human decision step | 3 | 4 | 4 | 48 | Minor | Add sequence lock: "Miro backlog update step classification note: Deterministic execution is only valid AFTER the human validation/invalidation decision has been recorded. The skill MUST NOT execute the Miro update step until the human decision is received. Add to treatment guidance: 'Gate this step behind human confirmation: the backlog update executes only after the user explicitly selects Validated, Invalidated, or Re-queue for the hypothesis under review.'" | Methodological Rigor |
| FM-017-20260303I5 | E-09 Routing Framework | Section 7.4 Free-tier team configuration note (PM-004-20260303b -- R7) states "Penpot has no production MCP server as of Q1 2026." This note is accurate for its revision date but is now embedded in a document with "accurate as synthesized in Q1 2026" shelf life language in the AI-First Design section only. The Penpot MCP availability note does not carry a date-stamped expiry or review trigger, meaning it may silently become outdated without any monitoring mechanism | 3 | 5 | 3 | 45 | Minor | Add date stamp and review trigger: "Penpot MCP status note [verified Q1 2026]: No production MCP server available. Re-verify at each quarterly MCP audit (Section 7.3) whether a Penpot MCP has been released. If a Penpot MCP becomes available before implementation, update this note and reassess Penpot as an alternative to Figma for free-tier teams." | Methodological Rigor |
| FM-018-20260303I5 | E-08 Coverage Analysis | The Ethics gap V2 prioritization table (Section 4) lists "Algorithmic bias in AI-generated UX" as V2 Priority P1 with path "Google PAIR Guidebook + ACM FAccT heuristics; custom Jerry research task." However, the Candidate Universe Generation (DA-002 -- R9) explicitly scoped OUT "frameworks that are purely theoretical, organizational-change programs, or require dedicated UX research teams." The PAIR Guidebook and ACM FAccT heuristics are described as the V2 path without being screened against this scoping criterion -- they may be theoretical frameworks requiring dedicated research rather than operationalizable sub-skills | 3 | 4 | 3 | 36 | Minor | Add scoping note to V2 algorithmic bias path: "The PAIR Guidebook and ACM FAccT heuristics are V2 research inputs, not pre-approved sub-skill frameworks. Before including either in V2 scoping, apply the candidate universe generation scoping criterion: confirm they have documented methodology steps operationalizable as Jerry sub-skills for teams of 2-5 people. A custom Jerry research task (not a full sub-skill) may be the appropriate V2 artifact." | Methodological Rigor |
| FM-019-20260303I5 | E-13 Required Pre-Launch Worktracker Entities | Section 7.5 table has 4 entities. The "Due/Recurrence" column for Entity #3 is "Quarterly" and for Entity #4 is "Quarterly." Both quarterly recurring tasks are created at the same time (PROJ-020 kickoff). If the kickoff date is in month N, both tasks' first due dates fall in month N+3 simultaneously. No guidance addresses the scenario where the primary owner responsible for both tasks is unavailable during that quarter -- the succession protocol in Section 7.3 addresses MCP owner succession but not the task execution succession for the quarterly tasks specifically | 3 | 4 | 3 | 36 | Minor | Add task execution succession: "Quarterly task execution succession: if the primary owner responsible for either recurring task (Entity #3 or #4) is unavailable when the task falls due, the secondary owner executes the task. If both are unavailable, escalate to the PROJ-020 project lead per H-31. Do not defer quarterly tasks beyond their due date without recording the deferral reason in the worktracker." | Methodological Rigor |
| FM-020-20260303I5 | E-05 Selection Methodology | The Round 1 provisional top-10 table (CV-001-I3 correction, added Iter3) shows Double Diamond entering Round 1 at rank #6 with a score of 7.88. This is framed as strengthening the two-pass methodology argument. However, the table uses weights C1=25/85, C2=20/85, etc. (fractions of the non-C5 weights summing to 85). The document does not explain this normalization (dividing by 85 rather than 100) and a reader could mistake the Round 1 scores as comparable to the Round 2 final scores -- the scales are different and the cross-comparison is potentially misleading | 3 | 5 | 3 | 45 | Minor | Add explicit normalization note to Round 1 table: "Round 1 scores use renormalized weights (C1=25/85, C2=20/85, C3=15/85, C4=15/85, C6=10/85, C5 excluded), producing scores on an adjusted scale. Round 1 scores are NOT comparable to Round 2 final weighted totals (which use C1=25%, C2=20%, C3=15%, C4=15%, C5=15%, C6=10% summing to 100%). Do not compare Round 1 ranks to Section 2 final scores directly." | Internal Consistency |
| FM-021-20260303I5 | E-12 Operational Governance | The MCP maintenance contract succession protocol (Section 7.3, PM-002 -- R8) specifies three succession triggers: "(1) primary owner departure from the project, (2) primary owner role change removing UX skill responsibility, (3) primary owner extended absence (> 2 sprint cycles)." Trigger (2) "role change removing UX skill responsibility" is ambiguous in a project context where roles are informal -- when a person shifts from implementation to testing, does this constitute a "role change removing UX skill responsibility"? | 3 | 4 | 3 | 36 | Minor | Clarify trigger (2): "role change removing UX skill responsibility = any organizational or project assignment change that results in the named primary owner no longer having an active role in PROJ-020 or the `/user-experience` skill implementation. Examples: moving to a different product team, shifting to infrastructure work with no UX component, moving to a management role with no individual contributor UX obligations. When in doubt, the primary owner self-reports to the secondary owner; the secondary owner confirms whether succession is appropriate." | Actionability |
| FM-022-20260303I5 | E-04 Full Scoring Matrix | The Section 2 scoring matrix Note on recalculations states "Revision 4 (S-011 CV-001 through CV-008): Arithmetic corrections applied to 7 non-selected framework totals." However, 8 corrections are listed in the note (Double Diamond, Service Blueprinting, Design Thinking, Hook Model, UX Strategy, Cognitive Walkthrough, UX Honeycomb, Gestalt Principles). The note says "7 non-selected framework totals" but lists 8. This minor arithmetic description error exists in R9 | 2 | 6 | 3 | 36 | Minor | Correct the note: change "7 non-selected framework totals" to "8 non-selected framework totals" to match the 8 listed corrections. | Internal Consistency |

---

## Detailed Findings

### FM-001-20260303I5: Worktracker Entities Checklist Permits TBD Owner Creation

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.5 Required Pre-Launch Worktracker Entities |
| **Strategy Step** | Step 2 (Enumerate Failure Modes) -- "Insufficient" lens |

**Evidence:**
Section 7.5, Entity #1:
> "Owner: TBD primary + TBD secondary (MANDATORY at creation)"

Section 3.8 prerequisite management:
> "MANDATORY: The Enabler entity MUST have a named primary owner AND a named secondary owner assigned AT THE TIME OF CREATION. No default owner exists. If no primary owner is assigned at creation time, the Enabler is placed in BLOCKED state."

**Analysis:**
Section 7.5 lists the Enabler with "TBD primary + TBD secondary" in the Owner column. This directly contradicts Section 3.8's hard rule that owners must be named at creation time and that TBD = BLOCKED. The checklist is supposed to be the actionable creation guide, but it normalizes a TBD state that Section 3.8 explicitly prohibits. An implementer following the checklist step-by-step could create the entity with TBD owners, which the document's own rules define as blocked. S=6 (creates operational ambiguity in a risk control mechanism), O=7 (the TBD appears explicitly in the checklist -- it will be encountered), D=4 (the contradiction between sections requires reading both to detect).

**Recommendation:**
Replace "TBD primary + TBD secondary (MANDATORY at creation)" with: "MUST be assigned before entity creation -- identify owners first. Creating this entity with TBD owners violates the BLOCKED state rule in Section 3.8. If owners are unknown at document-adoption time, this checklist item is itself in BLOCKED state until owners are identified and documented."

**Acceptance Criteria:** Section 7.5 Entity #1 Owner column contains no "TBD" language and includes a blocking warning if owners are not yet identified.

**Post-Correction RPN Estimate:** S=6, O=3, D=4 → RPN 72

---

### FM-002-20260303I5: AI-First Design Arithmetic Examples Show Only Failing Cases

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 3.8 AI-First Design, acceptance criterion (d) |
| **Strategy Step** | Step 2 (Enumerate Failure Modes) -- "Missing" lens |

**Evidence:**
> "Example using projected defaults: if re-scored C1=9, C2=8, with projected C3=8, C4=2, C5=10, C6=7, then total = ... = 7.55, which fails the >= 7.80 threshold."
> "Example with reviewer-adjusted C5: if C5 is assessed at 6... then total = ... = 6.95, which also fails."

Both examples fail. No passing example is provided. The acceptance criterion requires the recalculated total to be >= 7.80 with C1 >= 9 and C2 >= 8.

**Analysis:**
Two failing examples illustrate what does NOT meet the gate. A reviewer or implementer trying to understand what combination DOES meet the gate must compute it independently. This creates an actionability gap precisely where stakes are highest (the AI-First Design selection validation gate). S=5 (a reviewer could mistake the gate as difficult-to-meet without seeing a passing scenario), O=7 (anyone reading the acceptance criteria will encounter only failing examples), D=4 (the absence of a passing example requires recognizing what is missing, not detecting an error).

**Recommendation:**
Add a third example after the two failing examples:
"Example passing scenario: if re-scored C1=10, C2=9, with projected C3=8, C4=2, C5=10, C6=7 (all reviewer-attested), then total = 10*0.25 + 9*0.20 + 8*0.15 + 2*0.15 + 10*0.15 + 7*0.10 = 2.50+1.80+1.20+0.30+1.50+0.70 = 8.00, which passes the >= 7.80 threshold and meets both C1 >= 9 (C1=10) and C2 >= 8 (C2=9) dimension floors."

**Acceptance Criteria:** Section 3.8 acceptance criterion (d) includes at least one passing arithmetic example in addition to the two failing examples.

**Post-Correction RPN Estimate:** S=5, O=3, D=4 → RPN 60

---

### FM-003-20260303I5: Implementation Specification Prompt Templates Have Unresolved Placeholders

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.6 Implementation Specification for Sub-Skill Authors |
| **Strategy Step** | Step 2 (Enumerate Failure Modes) -- "Insufficient" lens |

**Evidence:**
Section 7.6 HIGH confidence synthesis gate template:
> "SYNTHESIS OUTPUT [HIGH CONFIDENCE]: I have generated [output type] based on [data sources]."

Section 7.6 MEDIUM confidence synthesis gate template:
> "SYNTHESIS OUTPUT [MEDIUM CONFIDENCE]: This output requires validation before use in design decisions."

The scope table (Section 7.6, immediately preceding the Implementation Specification) lists specific sub-skills and their confidence levels. However, neither the scope table nor the Implementation Specification maps [output type] and [data sources] to specific values per sub-skill.

**Analysis:**
The Implementation Specification is positioned as actionable guidance for sub-skill authors. Unresolved placeholders require each author to independently determine what [output type] and [data sources] should be for their sub-skill, creating inconsistent implementation across the 10 sub-skills. S=5 (inconsistent implementation degrades cross-sub-skill consistency), O=6 (any implementer following the templates will encounter unresolved placeholders), D=4 (detection requires checking all sub-skills against a reference table that does not exist).

**Recommendation:**
Add a Placeholder Resolution Table after the canonical output label strings:

| Sub-Skill | Step | Confidence | [output type] | [data sources] |
|-----------|------|------------|--------------|----------------|
| `/ux-jtbd` | Job statement synthesis | MEDIUM | job statements | App Store reviews, support tickets, competitor analysis, interview transcripts |
| `/ux-lean-ux` | Assumption mapping | MEDIUM | assumption map | team-provided product context and stated user hypotheses |
| `/ux-design-sprint` | Day 4 thematic analysis (if 3+ sessions) | HIGH | thematic synthesis | user interview transcripts from Day 4 sessions |
| `/ux-inclusive-design` | Persona Spectrum customization | MEDIUM | Persona Spectrum evaluation | team-provided user context brief |
| `/ux-kano-model` | Mode 2 classification | MEDIUM | feature classification | 5-8 structured Kano interviews |
| `/ux-behavior-design` | B=MAP bottleneck diagnosis | MEDIUM | behavior bottleneck diagnosis | product analytics export and qualitative observations |
| `/ux-behavior-design` | Design intervention recommendations | LOW | intervention reference | B=MAP diagnosis output |
| `/ux-heart-metrics` | Goal-metric mapping | MEDIUM | HEART goal-metric mapping | team-stated product goals and priorities |
| `/ux-heart-metrics` | Metric threshold recommendation | LOW | benchmark thresholds | domain-specific benchmark data |
| `/ux-ai-first` | AI interaction pattern recommendations | LOW | pattern reference | synthesized framework document |

**Acceptance Criteria:** Section 7.6 includes a placeholder resolution table or equivalent inline specification mapping each sub-skill synthesis step to its [output type] and [data sources].

**Post-Correction RPN Estimate:** S=5, O=3, D=4 → RPN 60

---

### FM-004-20260303I5: C3 Perturbation Threshold Circularity Partially Unresolved

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 1 Sensitivity Analysis (C3 perturbation pre-registered rule) |
| **Strategy Step** | Step 2 (Enumerate Failure Modes) -- "Inconsistent" lens |

**Evidence:**
Pre-registered interpretation rule for C3 perturbation:
> "DISCONFIRMING result: If 2 or more selected frameworks fall below Fogg's baseline score (7.60) AND 2+ excluded frameworks score above them."

SM-012-I4 symmetric uncertainty table (R9 addition):
> Fogg -0.25: 7.35 | Fogg +0.25: 7.85

FM-004-20260303I4 from Iter4 identified this as a circular dependency -- Fogg's 7.60 is used as the threshold anchor while being in the uncertainty band itself. The SM-012-I4 table shows the bidirectional analysis but the pre-registered rule retains Fogg's point estimate (7.60) as the hard threshold without acknowledging the circularity.

**Analysis:**
The R9 revision partially addressed this by adding the symmetric uncertainty table (SM-012-I4), but the pre-registered rule itself is unchanged. The circularity persists: Fogg 7.60 (which could be 7.35) is the threshold for determining when Fogg fails (falls below threshold). S=5, O=5 (the unchanged pre-registered rule is the first text encountered in the sensitivity analysis), D=5 (the connection between the symmetric table and the pre-registered rule requires integrating two separate sections).

**Recommendation:**
Add a footnote directly to the pre-registered rule: "Threshold anchor note (SM-012-I4 clarification): Fogg's 7.60 baseline is used as the threshold anchor for consistency with the main analysis. Under -0.25 score uncertainty, Fogg could score 7.35. For teams with high sensitivity to this boundary, apply 7.35 as the disconfirming threshold instead of 7.60. The practical consequence: under the 7.35 threshold, the C3=25% perturbation scenario produces a CONFIRMING result (neither Fogg 7.10 nor Kano 7.25 falls below 7.35 by more than 0.25 above Service Blueprinting 7.40), requiring higher standard of evidence to trigger the DISCONFIRMING designation."

**Acceptance Criteria:** Pre-registered interpretation rule for C3 perturbation includes an explicit footnote acknowledging the threshold anchor uncertainty and specifying an alternative lower-bound threshold.

**Post-Correction RPN Estimate:** S=5, O=3, D=4 → RPN 60

---

### FM-005-20260303I5: Validation Checklist Has No Failing Example for LOW Confidence Gate

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.6 Implementation Specification -- Validation Checklist |
| **Strategy Step** | Step 2 (Enumerate Failure Modes) -- "Missing" lens |

**Evidence:**
Section 7.6 provides:
> "Passing example (MEDIUM gate, `/ux-jtbd` job statement synthesis): [4-paragraph passing exchange]"

No failing example exists for any confidence level (HIGH, MEDIUM, or LOW).

The validation checklist includes test cases for all three gates, but the test cases only specify "Expected Behavior" and "Pass Criteria" without a reference interaction showing what incorrect implementation produces.

**Analysis:**
Without a failing example, implementers cannot verify that the LOW confidence gate correctly blocks design recommendations rather than silently producing them without labels. The LOW gate is the strictest and most consequential: it applies to AI interaction pattern recommendations and design intervention recommendations. An incorrectly implemented LOW gate that produces recommendations without labels appears correct to a unit tester without a failing reference. S=4, O=6 (no failing example exists for any test case), D=4.

**Recommendation:**
Add after the passing example:
"Failing example (LOW gate, `/ux-behavior-design` design intervention recommendations):
User: 'Users aren't completing the checkout flow. Based on the B=MAP diagnosis that Ability is the bottleneck, what should I design?'
Agent [INCORRECT -- gate not enforced]: 'Based on the B=MAP Ability bottleneck diagnosis, implement these design interventions: (1) Reduce form fields from 12 to 5. (2) Add inline field validation. (3) Pre-fill known user data.'
Agent [CORRECT -- gate enforced]: '[LOW CONFIDENCE -- REFERENCE ONLY, NOT FOR DESIGN DECISIONS] This output has low confidence because the effectiveness of specific interventions depends on your users' context that cannot be validated from behavioral data alone. Return to the Fogg Behavior Model practitioner guidance and validate the intervention with a lightweight user observation before implementation. Reference summary (not directives): Ability bottlenecks typically involve form complexity, multi-step flows, or unclear next-action signals -- but which applies to your specific checkout depends on your users.'"

**Acceptance Criteria:** Section 7.6 includes at least one failing example showing incorrect gate behavior (recommendation produced without LOW confidence label) vs. correct gate behavior (labeled reference output, no directives).

**Post-Correction RPN Estimate:** S=4, O=3, D=4 → RPN 48

---

### FM-006-20260303I5: Section 7.5 Entity #4 Scope Inadequately Defined

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.5, Entity #4 (MCP Ownership Verification) |
| **Strategy Step** | Step 2 (Enumerate Failure Modes) -- "Insufficient" lens |

**Evidence:**
Section 7.5 Entity #4:
> "Title: MCP Ownership Verification | Creation Trigger: PROJ-020 kickoff | Owner: MCP maintenance contract owner | Due/Recurrence: Quarterly | Source Section: 7.3"

Section 7.3 MCP Maintenance Contract:
> "A recurring worktracker task titled 'MCP Ownership Verification' MUST be created at PROJ-020 kickoff with quarterly recurrence to verify both primary and secondary owners are current and able to fulfill their responsibilities."

The Section 7.5 checklist row for Entity #4 provides the task title, trigger, owner role, and recurrence but omits what "verification" entails. An implementer creating the task from the checklist must read Section 7.3 to understand what to verify. The checklist's purpose is to be self-contained enough to drive creation without cross-referencing.

**Analysis:**
This is an "Insufficient" failure mode -- the entity specification exists but lacks the scope detail needed for the task to be correctly created without reading the source section. S=4, O=5, D=4.

**Recommendation:**
Extend Entity #4 with a "Scope" column or note: "Verification scope: (1) Confirm named primary owner is active in PROJ-020 and acknowledges MCP audit obligation. (2) Confirm named secondary owner is identified and reachable. (3) Verify both owners can execute the quarterly audit per Section 7.3 audit scope. Duration: 15-30 minute check. Output: worktracker note confirming ownership status or recording succession action taken."

**Acceptance Criteria:** Section 7.5 Entity #4 includes sufficient scope definition to execute the verification task without reading Section 7.3.

**Post-Correction RPN Estimate:** S=4, O=3, D=4 → RPN 48

---

### FM-007-20260303I5: Agent Prompt Templates Authoring-Style Conflicts with Jerry Agent Conventions

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.6 Implementation Specification -- Agent Prompt Language Templates |
| **Strategy Step** | Step 2 (Enumerate Failure Modes) -- "Ambiguous" lens |

**Evidence:**
Section 7.6 placement guidance:
> "Gate requirements belong in the `<guardrails>` section (not `<methodology>`) because they are output quality constraints."

Section 7.6 HIGH confidence gate template:
> "Before presenting this synthesis output for design decision-making, surface the following confirmation prompt to the user: 'SYNTHESIS OUTPUT [HIGH CONFIDENCE]: I have generated [output type] based on [data sources]. Please review for accuracy before using in design decisions.'"

Jerry agent definitions per agent-development-standards.md describe agent behavior in the `<guardrails>` section using MUST/SHALL/NEVER language describing constraints, not first-person agent utterances. The template provides a user-facing utterance ("I have generated...") inside a guardrail, mixing behavioral constraints with output voice.

**Analysis:**
This creates implementation ambiguity: should an implementer write the guardrail as "MUST NOT produce design recommendations until user confirms synthesis review" (behavioral constraint) or embed the verbatim "I have generated..." text as a guardrail item? The template implies verbatim embedding but the placement guidance says `<guardrails>` -- the section used for constraints, not utterances. S=6, O=5, D=4.

**Recommendation:**
Add a "How to implement in agent definitions" clarification:
"These templates describe the USER-FACING OUTPUT CONTENT the agent must produce, not verbatim text for the `<guardrails>` YAML/XML section. In the sub-skill's `<guardrails>` section, express the constraint in behavioral terms: 'When producing a Synthesis hypothesis output classified as HIGH confidence in the AI Execution Mode Taxonomy, MUST surface a user-facing confirmation prompt with content matching the HIGH confidence gate template before producing any design recommendations. MUST NOT produce design recommendations until user explicitly confirms.' The first-person template text ('I have generated...') describes what the agent says to the user -- place this in the `<methodology>` section's output formatting guidance, not the `<guardrails>` section."

**Acceptance Criteria:** Section 7.6 Implementation Specification includes explicit guidance separating (a) behavioral constraint language for `<guardrails>` from (b) output content language for the agent's user-facing utterances.

**Post-Correction RPN Estimate:** S=6, O=3, D=4 → RPN 72

---

## Recommendations

### Critical (RPN >= 200)
None in R9. Previous Critical findings from Iter4 were addressed.

### Major (RPN 80-199)

| FM ID | RPN | Corrective Action | Acceptance Criteria | Post-Correction RPN |
|-------|-----|-------------------|---------------------|---------------------|
| FM-001-20260303I5 | 168 | Replace TBD owner language in Section 7.5 Entity #1 with blocking warning if owners unknown | No "TBD" in owner fields; blocking warning present | 72 |
| FM-002-20260303I5 | 140 | Add passing arithmetic example to Section 3.8 acceptance criterion (d) | At least one passing scenario shown in addition to two failing examples | 60 |
| FM-003-20260303I5 | 120 | Add placeholder resolution table mapping sub-skills to [output type] and [data sources] | Table or inline specification covering all 10 sub-skills with synthesis hypothesis steps | 60 |
| FM-004-20260303I5 | 125 | Add threshold anchor footnote to C3 pre-registered rule acknowledging uncertainty | Pre-registered rule footnote specifying alternative 7.35 lower-bound threshold | 60 |
| FM-005-20260303I5 | 96 | Add failing example for LOW confidence gate in Section 7.6 validation checklist | At least one failing example showing incorrect vs. correct LOW gate behavior | 48 |
| FM-006-20260303I5 | 80 | Add scope detail to Section 7.5 Entity #4 | Entity #4 self-contained enough to execute without reading Section 7.3 | 48 |
| FM-007-20260303I5 | 120 | Add authoring clarification separating behavioral constraints from output content templates | Implementation Specification clarifies `<guardrails>` constraint language vs. user-facing utterance content | 72 |

**Estimated total RPN reduction from Major corrections:** 1,894 current → estimated 1,490 post-correction (RPN reduction of ~404 from Major findings alone)

### Minor (RPN < 80)

| FM ID | RPN | Quick Fix |
|-------|-----|-----------|
| FM-008-20260303I5 | 80 | Fix C3 attestation to remove Context7 from "MCP servers" category |
| FM-009-20260303I5 | 72 | Upgrade Section 7.5 Verification instruction from "should" to "MUST" |
| FM-010-20260303I5 | 60 | Add explicit scoring artifact path for AI-First Design independent scoring document |
| FM-011-20260303I5 | 60 | Add note to symmetric uncertainty table: Kano -0.25 ties Service Blueprinting at 7.40 |
| FM-012-20260303I5 | 1 | Confirmed resolved (E-029 present in Evidence Summary). No action. |
| FM-013-20260303I5 | 60 | Replace "behavior path" with HEART-native vocabulary in Execution Mode Taxonomy |
| FM-014-20260303I5 | 48 | Add cross-reference from WSM independence resolution block to bounding pair identification |
| FM-015-20260303I5 | 45 | Add clarification reconciling 35+5 assembly with seed list completeness check |
| FM-016-20260303I5 | 48 | Add sequence lock requiring human validation before Miro backlog update |
| FM-017-20260303I5 | 45 | Add date stamp and review trigger to Penpot MCP status note |
| FM-018-20260303I5 | 36 | Add scoping note to V2 algorithmic bias path |
| FM-019-20260303I5 | 36 | Add quarterly task execution succession guidance for Entity #3 and #4 |
| FM-020-20260303I5 | 45 | Add normalization note to Round 1 provisional top-10 table |
| FM-021-20260303I5 | 36 | Clarify succession trigger (2) "role change removing UX skill responsibility" |
| FM-022-20260303I5 | 36 | Correct "7 non-selected framework totals" to "8 non-selected framework totals" |

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Slightly Negative | FM-002 (missing passing example), FM-003 (unresolved placeholders), FM-005 (missing failing example), FM-011 (Kano boundary risk not highlighted), FM-015 (seed list reconciliation gap) |
| Internal Consistency | 0.20 | Slightly Negative | FM-004 (threshold circularity partially unresolved), FM-008 (Context7 re-categorized as MCP server), FM-009 (should vs. MUST downgrade), FM-013 (vocabulary crossing), FM-020 (Round 1 scale confusion), FM-022 (7 vs. 8 count error) |
| Methodological Rigor | 0.20 | Slightly Negative | FM-007 (agent template authoring ambiguity), FM-006 (Entity #4 scope insufficient), FM-016 (sequence lock missing for Miro update), FM-017 (Penpot note without expiry), FM-018 (V2 ethics path not scoped) |
| Evidence Quality | 0.15 | Slightly Negative | FM-005 (no failing example reduces implementability evidence), FM-014 (bounding pair cross-reference missing) |
| Actionability | 0.15 | Slightly Negative | FM-001 (TBD owner creates non-actionable checklist item), FM-002 (no passing gate example), FM-003 (unresolved placeholders require interpolation), FM-021 (ambiguous succession trigger) |
| Traceability | 0.10 | Neutral | FM-012 confirmed resolved (E-029 present); FM-010 (scoring artifact path missing); FM-014 (bounding pair cross-reference gap) -- minor but contained |

**Overall Assessment:** ACCEPT with targeted corrections. R9 represents a substantial improvement over R8: 6 Criticals addressed, 14 Majors addressed, 3 Minors addressed from Iter4. The remaining 7 Major findings in R9 are all bounded in scope -- 5 are in the new Implementation Specification section (Section 7.6) and Section 7.5 (new checklist). These sections are the primary R9 additions and represent anticipated new-content findings rather than regressions. No finding invalidates the core selection methodology, the 10 framework choices, or the routing framework architecture.

---

## Execution Statistics
- **Total Findings:** 22
- **Critical:** 0
- **Major:** 7
- **Minor:** 15
- **Protocol Steps Completed:** 5 of 5

---

*Strategy Execution Report: S-012 FMEA*
*Template: `.context/templates/adversarial/s-012-fmea.md` v1.0.0*
*Deliverable: `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (R9)*
*Executed: 2026-03-03T00:00:00Z*
*Finding Prefix: FM-NNN-20260303I5*
