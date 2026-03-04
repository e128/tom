# Strategy Execution Report: Red Team Analysis

## Execution Context

- **Strategy:** S-001 (Red Team Analysis)
- **Template:** `.context/templates/adversarial/s-001-red-team.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Criticality:** C4 (Tournament Iteration 4)
- **H-16 Compliance:** S-003 Steelman confirmed at `tournament-iter3/s-003-steelman.md`
- **Revision:** R8 (prior tournament scores: 0.747 → 0.822 → 0.848; target >= 0.95)

---

# Red Team Report: UX Framework Selection

**Strategy:** S-001 Red Team Analysis
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md` (Revision 8)
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-001)
**H-16 Compliance:** S-003 Steelman applied in Tournament Iteration 3 (confirmed: `tournament-iter3/s-003-steelman.md`)
**Threat Actor:** A skeptical implementation team member who inherits the deliverable with no prior context and must decide whether to act on it, looking for gaps that would block or derail real implementation work.

---

## Step 1: Threat Actor Profile

**Goal:** Expose claims, gaps, and prerequisites that would cause an implementation team to make incorrect decisions, invest effort in the wrong direction, or encounter blocking surprises after beginning implementation work.

**Capability:** Full access to the document, awareness of typical framework-selection pitfalls in AI tooling (MCP instability, projected-score frameworks), understanding of operational constraints for tiny software teams, and the ability to cross-check claims against the document's own internal logic.

**Motivation:** The threat actor is not malicious; they are time-pressured and skeptical. They want to know: "Can I actually act on this document today? What will go wrong first? What claims does this document make that I cannot verify independently?"

**Exploitable surfaces:**
1. The document contains at least one framework with entirely projected (not measured) scores
2. The document contains a 10-framework ceiling that is analyst-assumed, not user-specified
3. Multiple protocol enforcement mechanisms are described as "machine-enforceable" but exist only as text in this document
4. The sensitivity analysis disconfirms two selections for a material subset of teams and the substitution path requires a framework (Service Blueprinting) that is explicitly labeled "NOT YET IMPLEMENTED"
5. The document describes wave transition criteria that reference sub-skills that do not yet exist

---

## Step 2: Attack Vector Enumeration

### Vector 1: The "Machine-Enforceable Gate" Gap (Ambiguity / Degradation)

Section 7.5 introduces a "Synthesis Hypothesis Validation Protocol" with "machine-enforceable gate requirements" for skill invocation. However, none of the 10 sub-skills (`/ux-jtbd`, `/ux-lean-ux`, etc.) currently exist. The gates described in Section 7.5 enforce behavior at "skill invocation time" -- but there are no skills to invoke. The protocol is written as if these enforcement mechanisms will be automatically present when the skills are built. The document provides no specification of what code, prompt template, or architecture actually implements the gate logic. The adversary (implementation team) can invoke `/ux-jtbd` in any form without any mechanism firing. **The "machine-enforceable" claim overstates the current state of enforcement.**

Evidence: Section 7.5 states: "Gates fire at skill invocation time (when the sub-skill produces the synthesis output), not at document-generation time." However, CC-004 (Section 3 introduction) explicitly states: "The sub-skills described here have not been built yet." The enforcement mechanism references a non-existent runtime.

**Exploitability:** High -- any implementation team reading Section 7.5 as a current specification will be confused about what to build.

### Vector 2: AI-First Design C4=2 Acceptance Threshold Circular Dependency (Circumvention)

The acceptance threshold for AI-First Design was raised from >= 7.60 to >= 7.80 with dimension floors C1 >= 9 and C2 >= 8 in R8 (IN-002). However, the acceptance criteria state: "C3-C6 carry their projected values from Section 2 (C3=8(P), C4=2, C5=10(P), C6=7(P)); C1 and C2 are independently re-scored." This means C3, C4, C5, and C6 are held fixed at projected values regardless of what the synthesis deliverable actually achieves. C4=2 is locked in because it is not a projected score -- it is the objective score for a non-existent framework. A synthesized framework that achieves C1=10 and C2=9 would pass the gate at 7.85 even if it has terrible MCP integration (C3=2) or poor complementarity. **The gate allows passing by meeting only C1 and C2 floors while treating all other projected values as fixed assumptions.**

Evidence: Section 3.8 states the gate requires "C1 >= 9 and C2 >= 8" and that "C3-C6 carry their projected values." The gate arithmetic example shows: if C1=9, C2=8, total = 7.55 (FAIL). But if C1=10, C2=9, total = 7.85 (PASS) -- with C3=8, C5=10, C6=7 still treated as projections, not independent measurements. The gate validates 33% of the criteria independently (C1, C2) and assumes 67% (C3, C5, C6) will match projections.

**Exploitability:** Medium -- a synthesis deliverable could achieve pass status while falling short on MCP integration and community adoption dimensions that are assumed rather than measured.

### Vector 3: MCP-Heavy Team Substitution Path References Unavailable Framework (Boundary / Dependency)

The C3=25% pre-registered interpretation rule in Section 1 states that for MCP-heavy teams, "Service Blueprinting MUST replace Kano and/or Fogg -- this is not optional guidance but a selection requirement given those teams' weighting." The parent skill triage in Section 7.1 includes `[MCP-heavy variant: /ux-service-blueprinting]` annotations. However, Service Blueprinting is explicitly labeled `[WAVE V2 -- NOT YET IMPLEMENTED; V1 interim: retain /ux-kano-model with non-MCP execution path]` in the same section. **The mandatory substitution for a defined class of teams (MCP-heavy) points to a framework sub-skill that does not yet exist and is not scheduled in the current wave plan.**

Evidence: Section 7.1 triage option (b) states: "`[MCP-heavy variant: /ux-service-blueprinting]` [WAVE V2 -- NOT YET IMPLEMENTED; V1 interim: retain `/ux-kano-model` with non-MCP execution path (CSV survey mode per Section 3.9)...]`". The V2 sequencing guidance in Section 4 does not specify when V2 will be implemented or what triggers V2 initiation beyond two concurrent trigger conditions. An MCP-heavy team following the mandatory substitution guidance arrives at a non-existent sub-skill.

**Exploitability:** High -- any team that uses Figma and Miro as primary tools (a substantial fraction of the target audience) is directed toward a mandatory substitution that has no implementation timeline.

### Vector 4: Wave 5 Entry Criteria Create an Indefinite Hold on Design Sprint (Degradation)

The 5-Wave Adoption Plan (Section 7.4) places `/ux-design-sprint` in Wave 5 with the entry criterion: "Team faces a major product direction decision OR is at initial product direction validation stage." The sub-skill routing guide (Section 7.2) states `[WAVE 5 -- NOT YET IMPLEMENTED until Wave 5 entry criteria are met; interim: /ux-lean-ux]`. Design Sprint ranked #2 in the entire analysis (8.65) and is the second-highest-scored framework. However, the Wave 5 label means it cannot be invoked until after Wave 4 is complete and the specific entry criteria are met. **For a team at the very beginning of product development -- the scenario Design Sprint is specifically designed for -- the framework is unavailable until four other waves are completed, which is the opposite of what the framework's intended use case requires.**

Evidence: Section 7.4 Wave 5 entry criteria: "Wave 5 entry (Design Sprint): Team faces a major product direction decision OR is at initial product direction validation stage." Wave 4 completion requires "30+ accessible users OR diagnosed at least one B=MAP bottleneck." A pre-launch team has zero users, so Wave 4 completion is impossible, making Design Sprint permanently unavailable at the moment it is most valuable (before any users exist).

**Exploitability:** High -- pre-launch teams following the wave plan are blocked from accessing the #2 ranked framework, which is specifically designed for early-stage product direction validation.

### Vector 5: "Analyst-Assumed" 10-Framework Ceiling Limits Portfolio Without User Input (Ambiguity / Circumvention)

Section CC-002 (document header) states: "The 10-framework ceiling is an analyst-assumed constraint based on standard Jerry skill portfolio size conventions, not a user-specified requirement." The entire analysis optimizes around this ceiling. However, the selection methodology, sensitivity analysis, and wave plan all treat 10 as a hard constraint. The two frameworks that would close P1 documented gaps (Service Blueprinting for service design, a User Research framework) are excluded specifically because the ceiling is 10. **A user who was never asked whether 10 is the right ceiling is now receiving a portfolio with acknowledged HIGH RISK gaps that were directly caused by a constraint they did not specify.**

Evidence: Section 4 "HIGH RISK -- USER RESEARCH GAP" states: "This portfolio does NOT include a dedicated user research framework." Section CC-002 states the ceiling is "analyst-assumed." Section 4 V2 Roadmap lists User Research Framework as "P1 (highest)" priority V2 candidate. The document acknowledges the ceiling caused a HIGH RISK gap but does not re-open the ceiling question even with this knowledge.

**Exploitability:** Medium -- the ceiling decision is disclosed but not explicitly re-confirmed with the user after the HIGH RISK gap is identified. The gap is documented but framed as "V2" rather than as a potential ceiling reconsideration.

### Vector 6: Pre-Registered Interpretation Rules Applied Retrospectively Undermine Falsifiability (Ambiguity / Rule Circumvention)

Section 1 contains three "pre-registered interpretation rules" for the C1, C2, and C3 sensitivity perturbations. The C3 perturbation rule is labeled `[DA-011-20260303b/RT-001-ITER2/IN-001-20260303iter2 -- R7]`, indicating it was registered in R7. The C1 and C2 perturbation rules are labeled `[SR-002 -- R8, retrospectively applied]` with the text: "Application (known result, retrospectively applied)." A pre-registered rule applied retrospectively after the result is known is definitionally not pre-registration. The C1 and C2 pre-registration claims add the appearance of methodological rigor to rules that were written knowing the outcome.

Evidence: Section 1 C1 perturbation: "Pre-registered interpretation rule for C1 perturbation [SR-002 -- R8, retrospectively applied]: ... Application (known result, retrospectively applied): No selected framework falls below threshold... This is a CONFIRMING result." The retroactive pre-registration is explicitly labeled, but the label "pre-registered" implies forward-looking registration that does not apply here.

**Exploitability:** Medium -- reduces the evidential weight of the C1 and C2 perturbation analysis. A skeptic could correctly argue that the "confirming" result for C1 and C2 provides no independent validation because the rule was written after the result was known.

### Vector 7: Synthesis Hypothesis Confidence Labels Not Grounded in Calibration Data (Dependency / Degradation)

The AI Execution Mode Taxonomy (Section 1) and per-sub-skill taxonomy tables classify framework steps as "Deterministic execution" or "Synthesis hypothesis" with confidence labels (HIGH/MEDIUM/LOW). These labels claim functional significance in Section 7.5 (the Synthesis Hypothesis Validation Protocol gates behavior based on them). However, the confidence level assignments appear to be analyst judgment calls, not empirically calibrated confidence scores. There is no calibration methodology, no reference to a confidence calibration study, and no stated basis for why, for example, "Day 4 thematic analysis" is HIGH confidence while "B=MAP bottleneck diagnosis" is MEDIUM confidence.

Evidence: Section 7.5 states gates fire based on "HIGH confidence synthesis," "MEDIUM confidence synthesis," and "LOW confidence synthesis" labels. Section 3.2 Design Sprint AI Execution Mode Taxonomy states Day 4 thematic analysis is "HIGH (grounded in interview data)" while Section 3.10 Fogg Behavior Model states B=MAP diagnosis is "MEDIUM (data quality determines confidence)." The HIGH vs. MEDIUM distinction is a qualitative judgment call, not a calibrated probability estimate. There is no stated basis for why "grounded in interview data" elevates the confidence level enough to change the gate behavior from requiring expert review to requiring only user acknowledgment.

**Exploitability:** Medium -- the entire Section 7.5 enforcement protocol depends on confidence labels whose calibration basis is unspecified. The gates may be misfiring (allowing MEDIUM confidence outputs when LOW is warranted, or requiring expert review when user acknowledgment would suffice).

### Vector 8: Crisis Triage Sequence Does Not Address Underlying Cause (Degradation)

The crisis triage entry (PM-005, option j in Section 7.1) prescribes a 3-skill emergency sequence: `/ux-heuristic-eval` (triage) → `/ux-behavior-design` (diagnosis) → `/ux-heart-metrics` (measurement). The rationale states: "Do NOT start with /ux-design-sprint or /ux-lean-ux in crisis mode; those are improvement frameworks, not triage frameworks." However, `/ux-heart-metrics` (Step 3) is placed in Wave 2 of the adoption plan, requiring Wave 1 completion (at least one heuristic eval finding and one JTBD job statement). A team invoking the crisis sequence may not have completed Wave 1 prerequisites for HEART. Additionally, the crisis triage assumes that behavioral data exists (for `/ux-behavior-design`) -- but a team in crisis with churning users may not have properly configured analytics, which is precisely the kind of infrastructure gap that contributes to the crisis.

Evidence: Section 7.4: "Wave 2 -- Data-Ready Skills: `/ux-lean-ux`, `/ux-heart-metrics`; Prerequisites: Wave 1 complete; analytics source for HEART." Section 7.1 option (j): crisis sequence includes `/ux-heart-metrics` in Step 3 without noting the Wave 2 analytics prerequisite. Section 3.10 Fogg: "Explicit degraded-mode behavior: If invoked with no analytics data source..." -- acknowledges data absence but the crisis sequence uses Fogg as Step 2, which requires behavioral data.

**Exploitability:** Low-Medium -- the crisis sequence may fail at Step 2 or Step 3 for teams without configured analytics, which is a common scenario for early-stage products in crisis.

---

## Step 3: Defense Gap Assessment

| RT-ID | Finding | Existing Defense | Defense Classification | Priority |
|-------|---------|-----------------|----------------------|----------|
| RT-001-20260303T4 | "Machine-enforceable gate" overstates enforcement in non-existent runtime | CC-004 forward-looking framing notice in Section 3; Section 7.5 scope table | Partial -- CC-004 warns about sub-skill non-existence but Section 7.5 uses "machine-enforceable" language without qualifying it as future-state | P0 |
| RT-002-20260303T4 | AI-First Design gate validates only C1/C2 while holding C3-C6 as fixed projections | Section 3.8 acceptance criteria; IN-002 threshold revision; "If total < 7.80... Service Blueprinting is designated as permanent replacement" | Partial -- the threshold gate catches total score failures but does not independently validate MCP integration (C3) or complementarity (C5) | P1 |
| RT-003-20260303T4 | Mandatory MCP-heavy team substitution points to non-existent sub-skill | V1 interim guidance (retain Kano with non-MCP path) | Partial -- interim guidance exists but is buried in the same line as the mandatory substitution label; easy to miss | P0 |
| RT-004-20260303T4 | Wave 5 placement blocks Design Sprint for pre-launch teams | Wave bypass/stall recovery protocol (PM-003) in Section 7.4 | Partial -- the bypass protocol addresses wave stalls but does not address the specific case where a pre-launch team needs Design Sprint before any user data exists | P1 |
| RT-005-20260303T4 | Analyst-assumed 10-framework ceiling caused HIGH RISK gap without user confirmation | CC-002 notice discloses the ceiling; HIGH RISK gap is prominently surfaced in document header | Partial -- disclosure is good but the ceiling decision is not re-opened after the HIGH RISK gap is identified, leaving the user without a clear re-confirmation mechanism | P1 |
| RT-006-20260303T4 | C1/C2 pre-registration rules retrospectively applied | Explicit "retrospectively applied" label in SR-002 | Partial -- the label is present but "pre-registered" terminology still implies forward-looking registration to a reader who does not notice the qualifier | P2 |
| RT-007-20260303T4 | Synthesis hypothesis confidence labels are analyst judgment, not calibrated | AI Execution Mode Taxonomy documentation per sub-skill | Missing -- no calibration methodology is referenced; confidence levels have no stated empirical basis | P1 |
| RT-008-20260303T4 | Crisis sequence has unaddressed analytics dependency | Fogg degraded-mode behavior documented | Partial -- Fogg degraded mode is documented but the crisis sequence does not reference it or provide a data-absent crisis path | P2 |

---

## Step 4: Countermeasures

### P0 Countermeasures (MUST address before acceptance)

**RT-001-20260303T4 -- "Machine-Enforceable Gate" Language Correction**

The phrase "machine-enforceable gate requirements" in Section 7.5 must be qualified as a specification for future skill implementations, not a description of current enforcement capability. Revise the Section 7.5 opening sentence to: "The following gate requirements MUST be implemented at skill invocation time when each sub-skill is built." Replace "machine-enforceable" throughout Section 7.5 with "required implementation specification" or "gate requirement (to be enforced at skill implementation time)."

Acceptance criteria: Section 7.5 contains no language that implies gates fire in the current system. A reader unfamiliar with the document's prior revisions can correctly understand that the gates are specifications for future implementation.

**RT-003-20260303T4 -- MCP-Heavy Team Substitution Path Clarified**

The mandatory substitution directive for MCP-heavy teams in Sections 1 and 7.1 must be modified to make the non-existence of Service Blueprinting as a Jerry sub-skill the primary, not secondary, piece of information. Current: "`[MCP-heavy variant: /ux-service-blueprinting]` [WAVE V2 -- NOT YET IMPLEMENTED; V1 interim: retain...]`". Proposed: restructure so that the V1 interim path is prominent and the mandatory substitution is framed as: "Mandatory for post-V2 MCP-heavy teams: replace Kano/Fogg with `/ux-service-blueprinting` when that sub-skill is available (Wave V2). Current V1 action: use Kano Model with non-MCP CSV survey path (Section 3.9) and acknowledge the MCP gap."

Acceptance criteria: A team reading the MCP-heavy variant section understands that no `/ux-service-blueprinting` sub-skill exists and knows exactly what to do instead in V1.

### P1 Countermeasures (SHOULD address)

**RT-002-20260303T4 -- AI-First Design Gate Scope Disclosure**

Add a disclosure to the Section 3.8 acceptance criteria noting that the gate independently validates only C1 and C2, while C3 (MCP integration = 8), C5 (complementarity = 10), and C6 (accessibility = 7) are held as projections from the scoring matrix. State explicitly: "The gate does not independently re-score C3, C5, or C6. If the synthesis deliverable differs substantially from these projected values (e.g., C3 lower than 8 due to limited MCP integration in the synthesized framework's methodology), the reviewer must flag this as a supplementary concern even if the weighted total passes the >= 7.80 threshold."

Acceptance criteria: Section 3.8 acceptance criteria contain a statement that identifies which criteria are independently validated and which are held as projections.

**RT-004-20260303T4 -- Pre-Launch Design Sprint Access Path**

The Wave 5 placement and bypass protocol do not address the specific scenario of a pre-launch team needing Design Sprint before any user base exists. Add a Wave 5 pre-launch bypass condition: "If a team is at the initial product validation stage (0 users, major direction decision needed), Design Sprint may be invoked directly without completing Waves 1-4, provided the team acknowledges the single-prerequisite: the team can articulate the sprint challenge in one sentence. Route directly to Wave 5 Design Sprint in this case."

Acceptance criteria: Section 7.4 Wave 5 entry criteria explicitly address the pre-launch zero-user scenario. A pre-launch team can follow the plan and access Design Sprint without being blocked by Wave 4 (which requires 30+ users).

**RT-005-20260303T4 -- Ceiling Re-Confirmation Request**

After the HIGH RISK user research gap is identified (Section 4 and document header), the document should explicitly ask: "Given this HIGH RISK gap, please confirm whether the 10-framework ceiling is acceptable, or whether expanding to 11 (adding Service Blueprinting) or 12 (adding a User Research tool) is preferred for your implementation scope." This converts the analyst assumption into a confirmed user decision.

Acceptance criteria: Section 4 HIGH RISK gap notice or Section CC-002 contains a user confirmation request for the ceiling, with the framing that the HIGH RISK gap was not known when the ceiling was assumed.

**RT-007-20260303T4 -- Synthesis Hypothesis Confidence Calibration Basis**

Add a brief calibration note to the AI Execution Mode Taxonomy (Section 1) explaining the basis for HIGH/MEDIUM/LOW confidence assignments: "Confidence levels reflect: HIGH = AI operates on structured, verifiable input with human-validated grounding data (interview transcripts, measured analytics); MEDIUM = AI synthesizes from team-provided context that may be incomplete or biased; LOW = AI generates from general training data with minimal grounding in team-specific user evidence." This does not require an empirical calibration study -- it requires stating the classification logic so readers can evaluate whether the labels are appropriately assigned.

Acceptance criteria: Section 1 AI Execution Mode Taxonomy contains a confidence level classification rationale that explains what distinguishes HIGH from MEDIUM from LOW, allowing a reader to evaluate whether a given step is correctly classified.

### P2 Countermeasures (MAY address)

**RT-006-20260303T4 -- Pre-Registration Terminology Correction**

Replace "pre-registered interpretation rule" with "interpretation rule" for the C1 and C2 perturbation rules in Section 1. The C3 perturbation rule (registered in R7 before the result was incorporated in R8) may retain "pre-registered." The C1 and C2 rules are analysis-consistent but not pre-registered in the meaningful methodological sense.

Acceptance criteria: The C1 and C2 perturbation sections do not use the term "pre-registered" for rules that were written with knowledge of the result.

**RT-008-20260303T4 -- Crisis Sequence Analytics Dependency Note**

Add a qualifier to the crisis triage sequence (Section 7.1, option j): "Step 2 (/ux-behavior-design) requires behavioral data. If no analytics are configured, use Fogg's degraded mode (qualitative B=MAP assessment from anecdotal observations). Step 3 (/ux-heart-metrics) can be run in goal-setting mode (establish baseline metrics from this point forward) without pre-existing analytics data."

Acceptance criteria: The crisis sequence handles the no-analytics scenario explicitly rather than assuming analytics infrastructure exists.

---

## Findings Summary

| ID | Severity | Finding | Section |
|----|----------|---------|---------|
| RT-001-20260303T4 | Major | "Machine-enforceable gate" overstates enforcement capability for non-existent sub-skills | Section 7.5 (Synthesis Hypothesis Validation Protocol) |
| RT-002-20260303T4 | Minor | AI-First Design acceptance gate validates only 2 of 6 criteria independently; 4 criteria held as fixed projections | Section 3.8 (AI-First Design acceptance criteria) |
| RT-003-20260303T4 | Major | Mandatory MCP-heavy team substitution points to a non-existent `/ux-service-blueprinting` sub-skill without sufficiently prominent V1 fallback | Sections 1, 7.1 (Sensitivity Analysis C3, MCP-heavy variant) |
| RT-004-20260303T4 | Major | Wave 5 placement of Design Sprint (#2 ranked framework) blocks pre-launch teams who need it most | Section 7.4 (Wave 5 entry criteria) |
| RT-005-20260303T4 | Minor | 10-framework analyst-assumed ceiling caused HIGH RISK user research gap but no user re-confirmation was sought after the gap was identified | Sections CC-002, header HIGH RISK notice, Section 4 gap analysis |
| RT-006-20260303T4 | Minor | C1/C2 "pre-registered" interpretation rules applied retrospectively, undermining falsifiability claim | Section 1 (C1 and C2 perturbation analysis) |
| RT-007-20260303T4 | Minor | Synthesis hypothesis confidence labels (HIGH/MEDIUM/LOW) lack stated calibration basis, weakening Section 7.5 gate enforcement logic | Section 1 AI Execution Mode Taxonomy; Section 7.5 |
| RT-008-20260303T4 | Minor | Crisis triage sequence (PM-005) assumes behavioral analytics infrastructure exists without addressing no-analytics fallback | Section 7.1 option (j) |

---

## Detailed Findings

### RT-001-20260303T4: "Machine-Enforceable Gate" Overstates Current Enforcement Capability [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.5 (Synthesis Hypothesis Validation Protocol) |
| **Strategy Step** | Step 2 (Ambiguity exploitation) / Step 3 (Defense gap assessment) |

**Attack Vector:** An implementation team reads Section 7.5 and believes that when they build `/ux-jtbd`, the enforcement mechanism described therein will "just work" -- i.e., that some existing system layer will fire the gates. They may deprioritize implementing the gate logic themselves, or build skills without it, resulting in synthesis hypothesis outputs flowing into design decisions without the required validation.

**Category:** Ambiguity exploitation + Degradation

**Exploitability:** High -- the CC-004 forward-looking framing notice is placed at the top of Section 3 (the selected 10 section), but Section 7.5 is a separate section added in R8 that does not include an equivalent forward-looking qualifier. A reader who encounters Section 7.5 without having read CC-004 will interpret "machine-enforceable gate requirements" as current operational enforcement.

**Severity:** Major -- this does not invalidate the selection analysis, but it creates a misunderstanding about what exists now vs. what must be built. If an implementation team builds skills without the gate logic, the entire Section 7.5 "machine-enforceable" claim becomes a false promise with real consequences: synthesis hypothesis outputs from JTBD and Lean UX will flow into design decisions without required validation.

**Existing Defense:** CC-004 notice states "The sub-skills described here have not been built yet." But this is in Section 3, not Section 7.5.

**Evidence:**
- Section 7.5 opening: "The following machine-enforceable gate requirements apply at skill invocation time for any sub-skill step classified as 'Synthesis hypothesis' in the AI Execution Mode Taxonomy."
- Section 3 CC-004: "The 'Tiny Teams enablement pattern' sections below describe the intended AI-augmented workflow for each proposed Jerry sub-skill. These patterns represent design targets for implementation, not descriptions of currently operational capabilities. The sub-skills described here have not been built yet."
- Section 7.5 Enforcement Mechanism column: "Skill surfaces confirmation prompt before producing the design recommendation. If user does not confirm, output is labeled '[UNCONFIRMED SYNTHESIS -- NOT FOR DESIGN DECISIONS]' and the sub-skill halts at the synthesis step." -- No such skill exists to surface this prompt.

**Dimension:** Methodological Rigor, Actionability

**Countermeasure:** Revise Section 7.5 to qualify enforcement language as a future implementation specification. Add a notice parallel to CC-004 at the start of Section 7.5: "Note: The gate requirements below are implementation specifications for when each sub-skill is built. They do not describe currently operational enforcement mechanisms." Replace "machine-enforceable" with "implementation-required gates."

**Acceptance Criteria:** Section 7.5 contains no language that implies current operational enforcement of non-existent sub-skills. An implementer reading Section 7.5 in isolation understands they must build the gate logic into each skill.

---

### RT-003-20260303T4: Mandatory MCP-Heavy Team Substitution References Non-Existent Sub-Skill [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Sections 1 (C3 perturbation), 7.1 (parent skill triage, MCP-heavy variant) |
| **Strategy Step** | Step 2 (Boundary violations) / Step 3 (Defense gap assessment) |

**Attack Vector:** A team identifies itself as MCP-heavy (uses Figma and Miro as primary tools, considers MCP integration a primary value driver). They follow the C3=25% mandatory substitution directive and route to `/ux-service-blueprinting`. This sub-skill does not exist. The routing guidance is presented as "not optional" but the destination is non-existent.

**Category:** Boundary violation (gap between specification and implementation) + Dependency attack

**Exploitability:** High -- the MCP-heavy team identification is likely to match a significant fraction of teams using the Jerry `/user-experience` skill (Figma and Miro are the dominant design toolchain). The word "MUST" in the substitution directive conveys mandatory compliance to a non-existent implementation target.

**Severity:** Major -- a material class of teams (MCP-heavy) following the document's own mandatory guidance will arrive at a sub-skill that does not exist and has no current-wave implementation plan. The V1 interim guidance ("retain `/ux-kano-model` with non-MCP execution path") is the buried secondary clause in a long parenthetical, not the prominent instruction.

**Existing Defense:** V1 interim guidance exists in the same paragraph. Section 5.3 (Service Blueprinting rejected frameworks section) provides rationale and recommendation.

**Evidence:**
- Section 1 C3 perturbation: "For such teams, Service Blueprinting MUST replace Kano and/or Fogg -- this is not optional guidance but a selection requirement given those teams' weighting."
- Section 7.1 triage option (b): "`[MCP-heavy variant: /ux-service-blueprinting] [WAVE V2 -- NOT YET IMPLEMENTED; V1 interim: retain /ux-kano-model with non-MCP execution path (CSV survey mode per Section 3.9) and note MCP-heavy teams should prioritize Service Blueprinting when it becomes available]`"
- Section 7.4: Service Blueprinting is not listed in any of the 5 waves (it is a V2 item per Section 4 V2 Roadmap). No implementation timeline exists for it.

**Dimension:** Actionability, Completeness

**Countermeasure:** Restructure the MCP-heavy team guidance in both Section 1 and Section 7.1 so that the V1 action is the primary directive and the V2 substitution is the secondary. Proposed structure: "For MCP-heavy teams in V1: use `/ux-kano-model` in non-MCP CSV survey mode (Section 3.9). When `/ux-service-blueprinting` becomes available (planned for V2; no current implementation timeline), it replaces Kano/Fogg for MCP-heavy contexts. Mandatory substitution applies to post-V2 deployments."

**Acceptance Criteria:** A reader following the MCP-heavy variant guidance in V1 receives a clear, actionable instruction (use Kano in CSV mode) as the primary directive, not as a buried secondary clause.

---

### RT-004-20260303T4: Wave 5 Blocks Design Sprint for Pre-Launch Teams Who Need It Most [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Section 7.4 (Wave 5 implementation sequencing), Section 7.1 (parent skill triage), Section 7.2 (sub-skill routing guide) |
| **Strategy Step** | Step 2 (Degradation paths) / Step 3 (Defense gap assessment) |

**Attack Vector:** A 3-person team with a new product idea but zero users follows the 5-Wave Adoption Plan. They correctly start with Wave 1 (Nielsen's + JTBD). They then attempt to move to Wave 2 (requires analytics/Miro). Wave 4 requires 30+ users (impossible at pre-launch). Wave 5 requires Wave 4 completion. The team cannot access Design Sprint until they have 30+ users AND have diagnosed a B=MAP bottleneck -- conditions that are structurally impossible for a pre-launch product. Design Sprint is the one framework specifically designed for "initial product direction validation" (the Wave 5 entry criterion) and is being held behind a wave that requires post-launch user data.

**Category:** Degradation path (access restriction)

**Exploitability:** High -- the target audience includes teams that are specifically pre-launch. The wave plan's linearization forces post-launch prerequisites before the one framework most useful pre-launch can be accessed.

**Severity:** Major -- this misroutes the target audience away from the highest-value framework for their lifecycle stage. Design Sprint scored 8.65 (2nd overall) specifically because of its tiny-team and early-stage value. Wave 5 placement inverts the framework's intended use case.

**Existing Defense:** Wave 5 entry criteria include "Team faces a major product direction decision OR is at initial product direction validation stage" -- but this criterion cannot be reached without first completing Wave 4 per the wave gating logic.

**Evidence:**
- Section 7.4 Wave 5: "Wave 5 -- Process Intensives: `/ux-design-sprint`, `/ux-ai-first` (CONDITIONAL): Design Sprint requires 4 consecutive days of team commitment -- implement after other skills are established and a major decision warrants the time investment."
- Section 7.4 Wave 4 → Wave 5 transition: "Team has 30+ accessible users (for Kano) OR has diagnosed at least one B=MAP bottleneck with a resulting design change (for Fogg). (2) Analytics source shows at least 30 days of post-launch behavioral data available."
- Section 3.2 Design Sprint: "Framework version: Design Sprint 2.0 (AJ&Smart)" -- designed for early-stage product direction validation.
- Section 7.1 triage option (c): "[WAVE 5 -- NOT YET IMPLEMENTED until Wave 5 entry criteria are met per Section 7.4; interim: use /ux-lean-ux for lightweight hypothesis-driven prototyping]"

**Dimension:** Actionability, Internal Consistency

**Countermeasure:** Add a pre-launch bypass condition to Wave 5 entry criteria: "Exception: A team at the initial product direction validation stage with zero users may invoke `/ux-design-sprint` directly without completing Waves 1-4, provided: (1) the sprint challenge can be articulated in a single sentence, and (2) the team acknowledges that post-sprint validation will require at least 3 real users. This exception recognizes that Design Sprint is designed precisely for the pre-launch zero-user scenario."

**Acceptance Criteria:** Section 7.4 explicitly addresses the pre-launch zero-user case and grants direct Wave 5 access for teams at the initial product direction validation stage.

---

### RT-002-20260303T4: AI-First Design Acceptance Gate Validates Only 2 of 6 Criteria [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 3.8 (AI-First Design acceptance criteria, validation gate) |
| **Strategy Step** | Step 2 (Rule circumvention) |

**Attack Vector:** A synthesis deliverable that achieves C1=10, C2=9 (total 7.85, PASS) but falls short on MCP integration (C3=4, not 8) would pass the gate while delivering a framework that integrates poorly with the MCP toolchain that justifies the `/user-experience` skill's tool cost.

**Evidence:** Section 3.8: "Arithmetic implication: C3-C6 carry their projected values from Section 2 (C3=8(P), C4=2, C5=10(P), C6=7(P)); C1 and C2 are independently re-scored... the full 6-criterion WSM formula applies."

**Countermeasure:** Add a supplementary check: "The reviewer must also assess whether the synthesized framework's MCP integration (C3) materially differs from the projected 8/10. If the synthesis deliverable lacks MCP integration capabilities comparable to the projection (i.e., C3 would score 5 or lower), the reviewer must flag this as a supplementary concern in the synthesis deliverable review, even if the weighted total passes >= 7.80."

**Acceptance Criteria:** Section 3.8 acceptance criteria note that C3 projection assumptions should be verified by the reviewer, not merely accepted as fixed.

---

### RT-005-20260303T4: 10-Framework Ceiling Caused HIGH RISK Gap Without User Re-Confirmation [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Document header (HIGH RISK notice), Section CC-002, Section 4 (gap analysis) |
| **Strategy Step** | Step 2 (Ambiguity exploitation) |

**Attack Vector:** A user reads the document, sees the HIGH RISK user research gap notice, and assumes the analyst considered and confirmed that 10 frameworks is still the right ceiling despite this gap. No such confirmation occurred -- the ceiling was assumed before the gap was identified. The user proceeds without knowing they could have asked for an 11-framework portfolio that closes the HIGH RISK gap.

**Evidence:** Section CC-002: "The 10-framework ceiling is an analyst-assumed constraint... not a user-specified requirement." Section 4 HIGH RISK: "This portfolio does NOT include a dedicated user research framework." Section 4 V2 Roadmap: User Research Framework listed as "P1 (highest)" V2 candidate.

**Countermeasure:** Add a user confirmation prompt to either Section CC-002 or the Section 4 HIGH RISK notice: "Because this gap is HIGH RISK and the ceiling was analyst-assumed (not user-specified), please confirm: is a 10-framework V1 portfolio acceptable given this gap, or would you prefer to expand to 11 by including Service Blueprinting (which partially addresses the service/research gap) and reconsider the ceiling?"

**Acceptance Criteria:** The document explicitly offers the user a ceiling re-confirmation decision after the HIGH RISK gap is surfaced.

---

### RT-006-20260303T4: Retrospective "Pre-Registration" Weakens Perturbation Falsifiability [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 1 (C1 and C2 sensitivity perturbation analysis) |
| **Strategy Step** | Step 2 (Rule circumvention) |

**Attack Vector:** A reader assessing the methodological rigor of the sensitivity analysis notices that "pre-registered interpretation rules" for C1 and C2 were written after the results were known. This is disclosed but labeled "pre-registered," which is terminologically incorrect. A skeptic can correctly argue that the CONFIRMING results for C1 and C2 provide weaker evidential support for the selection than the document implies.

**Evidence:** Section 1 C1 perturbation: "[SR-002 -- R8, retrospectively applied] ... Application (known result, retrospectively applied): No selected framework falls below threshold. This is a CONFIRMING result."

**Countermeasure:** Replace "Pre-registered interpretation rule" with "Interpretation rule (retrospectively formalized)" for C1 and C2 perturbation rules. Reserve "pre-registered" for the C3 rule only, which was genuinely registered before the result was incorporated.

**Acceptance Criteria:** C1 and C2 perturbation sections do not use "pre-registered" for rules formalized with knowledge of the result.

---

### RT-007-20260303T4: Confidence Labels Lack Stated Calibration Basis [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 1 (AI Execution Mode Taxonomy), Section 7.5 (Synthesis Hypothesis Validation Protocol), Sections 3.1-3.10 (per-sub-skill taxonomy tables) |
| **Strategy Step** | Step 2 (Ambiguity exploitation) |

**Attack Vector:** An implementer building the gates described in Section 7.5 finds that the HIGH/MEDIUM/LOW confidence label distinctions in the taxonomy tables do not have explicit classification logic. They cannot determine whether a new synthesis step in a future skill should receive HIGH or MEDIUM confidence without guessing. Over time, confidence labels accumulate inconsistently, weakening the enforcement protocol.

**Evidence:** Section 3.2 Design Sprint: "Day 4 thematic analysis of interview transcripts (if interviews conducted): HIGH (grounded in interview data)." Section 3.10 Fogg: "B=MAP bottleneck diagnosis from behavioral data: MEDIUM (data quality determines confidence)." Both are "grounded in data" -- the distinction between HIGH and MEDIUM is not explained by a classification rule, only by the specific label in each row.

**Countermeasure:** Add a confidence classification rationale to Section 1 AI Execution Mode Taxonomy: "Confidence levels are assigned by the following classification logic: HIGH = AI executes a structured analytical step against team-provided, human-validated grounding data (interview transcripts, measured analytics from real users); MEDIUM = AI synthesizes from team-provided context that is not externally validated or from data whose quality is team-dependent; LOW = AI generates from general training data with no grounding in team-specific user evidence."

**Acceptance Criteria:** Section 1 contains an explicit classification rationale that an implementer can apply to classify new synthesis steps without requiring analyst judgment.

---

### RT-008-20260303T4: Crisis Sequence Assumes Analytics Infrastructure [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Section 7.1 option (j) (crisis triage), Section 3.10 (Fogg degraded mode) |
| **Strategy Step** | Step 2 (Dependency attacks) |

**Attack Vector:** A team in active crisis (high churn) follows the crisis sequence. They attempt Step 2 (`/ux-behavior-design`) and find they have no properly configured behavioral analytics. The sequence stalls. The crisis worsens because the prescribed Step 2 cannot proceed.

**Evidence:** Section 7.1 option (j): "Step 2: /ux-behavior-design (same day: diagnose the specific B=MAP bottleneck causing user drop-off)." Section 3.10: "Explicit degraded-mode behavior: If invoked with no analytics data source, the skill surfaces: 'No behavioral data detected...'" -- degraded mode exists but is not referenced in the crisis sequence.

**Countermeasure:** Add a crisis sequence qualifier: "Step 2 (/ux-behavior-design): If behavioral data exists, use it to diagnose B=MAP bottleneck. If no analytics are configured, use Fogg degraded mode: describe qualitatively where users are dropping off, what they say when they fail, and any available anecdotal observations. Output will be LOW confidence B=MAP hypothesis -- proceed to Step 3 regardless."

**Acceptance Criteria:** The crisis sequence handles the no-analytics scenario explicitly.

---

## Step 5: Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Neutral | The portfolio selection, coverage analysis, complementarity matrix, and V2 roadmap are thorough. The incompleteness finding (RT-001) is about enforcement language, not selection coverage. RT-003 and RT-004 identify gaps in the implementation guidance completeness, not the framework selection completeness. |
| Internal Consistency | 0.20 | Negative (mild) | RT-003 creates an inconsistency between the mandatory substitution directive and the current implementation state. RT-004 creates an inconsistency between Design Sprint's stated use case (initial product direction validation) and its Wave 5 placement (post-launch user data required). RT-006 creates a minor inconsistency between "pre-registered" terminology and retrospective application. |
| Methodological Rigor | 0.20 | Negative (mild) | RT-001 overstates the rigor of enforcement mechanisms. RT-006 undermines the methodological claim of pre-registration for C1/C2 perturbation rules. RT-007 creates a basis gap in the confidence calibration methodology underpinning the entire Section 7.5 enforcement framework. |
| Evidence Quality | 0.15 | Neutral | All findings are about specification gaps, not evidence quality. The scoring evidence (E-001 through E-029) and the research artifact citations are unaffected by these findings. |
| Actionability | 0.15 | Negative (mild) | RT-001 creates actionability confusion about what to build. RT-003 directs MCP-heavy teams toward a non-existent sub-skill. RT-004 blocks the most actionable early-stage framework. These are the highest-impact actionability issues identified. |
| Traceability | 0.10 | Positive | The document's traceability is a strength that has been strengthened across revisions. Every finding in this report traces to specific section references. The revision log is detailed and well-attributed. |

**Overall Assessment:** ACCEPT WITH COUNTERMEASURES

Three Major findings require targeted revisions before the document is used as the definitive implementation guide. None of the findings invalidate the framework selection or the analytical methodology. The findings are concentrated in the implementation guidance sections (7.x) added in R7-R8, not in the core selection analysis (Sections 1-5). The document's fundamental analytical work -- the 40-framework scoring matrix, sensitivity analysis, coverage analysis, and complementarity matrix -- remains sound. The pre-mortem, FMEA, and constitutional compliance work from prior iterations has addressed the most serious analytical risks.

**Estimated composite score impact of countermeasures (if addressed):** The three Major findings (RT-001, RT-003, RT-004) are concentrated in Internal Consistency (0.20) and Actionability (0.15), representing 35% of the total weight. Under prior S-014 scoring the document received 0.848. Addressing these three findings would strengthen Internal Consistency and Actionability by approximately 0.05-0.08 each, for a projected composite score increase of approximately 0.05-0.09. If minor findings are also addressed, the projected increase is approximately 0.08-0.12, placing the deliverable in the range of 0.93-0.97 against the >= 0.95 target.

---

## Execution Statistics

- **Total Findings:** 8
- **Critical:** 0
- **Major:** 3 (RT-001, RT-003, RT-004)
- **Minor:** 5 (RT-002, RT-005, RT-006, RT-007, RT-008)
- **Protocol Steps Completed:** 5 of 5

## Prioritized Countermeasure Plan

**P0 -- MUST address before acceptance:**
- RT-001-20260303T4: Add implementation-specification qualifier to Section 7.5 "machine-enforceable gate" language
- RT-003-20260303T4: Restructure MCP-heavy team substitution directive so V1 interim path is primary instruction

**P1 -- SHOULD address:**
- RT-004-20260303T4: Add pre-launch zero-user bypass condition to Wave 5 Design Sprint entry criteria
- RT-002-20260303T4: Add supplementary C3 projection assumption check to AI-First Design acceptance gate
- RT-005-20260303T4: Add explicit user ceiling re-confirmation prompt after HIGH RISK gap is surfaced
- RT-007-20260303T4: Add confidence level classification rationale to Section 1 AI Execution Mode Taxonomy

**P2 -- MAY address:**
- RT-006-20260303T4: Replace "pre-registered" with "retrospectively formalized" for C1/C2 perturbation rules
- RT-008-20260303T4: Add no-analytics fallback qualifier to crisis triage sequence Step 2

---

*Strategy: S-001 Red Team Analysis | Finding Prefix: RT-NNN-20260303T4 | Template: s-001-red-team.md v1.0.0 | Executed: 2026-03-03*
