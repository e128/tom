# Steelman Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

## Steelman Context

- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Deliverable Type:** Design (GitHub issue body defining a new Jerry skill)
- **Criticality Level:** C4
- **Strategy:** S-003 (Steelman Technique)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Steelman By:** adv-executor (I8) | **Date:** 2026-03-03 | **Original Author:** Tournament I1-I8

---

## Summary

**Steelman Assessment:** The I8 deliverable is substantially mature -- it has absorbed 7 prior adversarial iterations and 10 targeted R7 fixes, and presents a coherent, well-evidenced vision for AI-augmented UX capability on tiny teams. The core architecture is sound, the wave deployment model is operationally specified, and the confidence gating system is a genuine differentiating strength. The remaining strengthening opportunities are framing-level: several of the R7 additions (ABANDON re-entry guard, BOOTSTRAP-VALIDATED active deadline, Haiku benchmark) are structurally correct but presented in a way that undersells their significance as risk management innovations. One structural gap remains in the cross-framework synthesis story, and the non-redundancy case -- while partially addressed -- benefits from an explicit framing statement that makes the portfolio logic immediately legible to reviewers.

**Improvement Count:** 0 Critical, 4 Major, 6 Minor

**Original Strength:** High. The deliverable demonstrates methodological rigor throughout: cited statistics, qualified AI capability claims, layered confidence gates, P-020-compliant override mechanisms, explicit fallback paths for all MCPs, criteria-gated wave progression with 3-state enforcement, and a comprehensive adversarial validation history. R7 fixes closed the key I7 findings. The remaining improvements are incremental quality lifts, not structural defects.

**Recommendation:** Incorporate Major improvements before downstream S-002/S-004 critique strategies. Minor improvements enhance precision but do not materially change quality gate passage.

---

## Steelman Reconstruction

The steelman reconstruction preserves all original content. Changes are marked `[SM-NNN-I8]` inline. Full section-by-section pass:

### Vision (Steelmanned)

Two people, one product, zero UX specialists -- and the product is going to feel like a team of eight built it.

The `/user-experience` skill is a parent orchestrator backed by 10 independently evolvable sub-skills covering the full product lifecycle from discovery through post-launch measurement. Each sub-skill implements a single proven UX framework as its own Jerry skill -- registered independently, versioned independently, loaded on-demand. The orchestrator reads the product stage and the team's need, then drops the developer into the right framework.

This is the UX department a 2-person team never thought they could have. Built on frameworks battle-tested across thousands of products over the past three decades. Not watered down. Not a chatbot that gives generic advice. The full methodology, AI-augmented so non-specialists can execute it (with confidence-gated output depth -- HIGH-confidence sub-skills produce full recommendations; MEDIUM produce guided analysis requiring validation; LOW produce reference summaries requiring specialist interpretation), with guardrails that draw a hard line between what AI handles and what humans decide.

**[SM-001-I8]** Add portfolio non-redundancy declaration in Vision: The 10 sub-skills are not the 10 highest-scoring frameworks -- they are a deliberately non-redundant portfolio where each framework fills a unique lifecycle niche. Three independent non-redundancy properties hold across all 10: cadence orthogonality (no two sub-skills share the same execution cadence), output differentiability (each sub-skill produces a structurally distinct artifact type), and C5 portfolio-composition test (each framework's Complementarity score was evaluated assuming the other 9 are included). This distinguishes the portfolio from a ranking exercise and strengthens the argument for including lower-ranked frameworks like Kano (7.65) alongside higher-ranked ones like Design Sprint (8.65).

The boldest line on the mountain is the one nobody thought was skiable. This is that line for tiny teams and UX.

---

### The Problem (Steelmanned)

*[No changes needed. The problem framing is well-evidenced with specific citations for Gartner, Midjourney, Bolt.new, WHO, and Grand View Research. The qualification of the AI speed-up claim as "estimated" and the precision around the WHO disability statistic range are both honest and appropriate.]*

---

### The Solution (Steelmanned)

**[SM-002-I8]** Strengthen the framework ordering note with explicit rationale for why Wave deployment order differs from WSM rank order:

*Current text (lines 166-167):* "Sub-skill descriptions below are ordered by Wave deployment sequence (Wave 1 first), not by WSM selection rank. Wave deployment order differs from WSM rank because it optimizes for dependency satisfaction and learning curve -- high-WSM frameworks that depend on Wave 1 outputs deploy in later waves."

*Steelmanned addition:* "This is not a compromise on quality -- it is deliberate sequencing architecture. The highest-WSM frameworks (Design Sprint at 8.65, Atomic Design at 8.55) deploy in later waves precisely because they produce their full value only when Wave 1 frameworks have established the foundational capability. A team that has never run a heuristic evaluation cannot optimally run a Design Sprint challenge statement session; a team with no existing components cannot optimally apply Atomic Design. Wave 1 is not the 'easy' entry -- it is the dependency-free, immediately actionable entry that maximizes time-to-first-value for the median Part-time UX team."

---

### Key Design Decisions (Steelmanned)

#### Decision 3: P-003 Compliant Single-Level Nesting (Steelmanned)

**[SM-003-I8]** The P-003 compliance section (lines 492-510) correctly describes the architecture but undersells why this matters for the UX skill specifically. Strengthen with consequence framing:

*Add after the architecture diagram:* "The single-level nesting constraint is especially important for a 10-sub-skill portfolio. Without strict T5/T3 separation, a sub-skill agent could theoretically spawn its own sub-agents (e.g., `/ux-design-sprint` Day 2 ideation spawning `/ux-lean-ux` for hypothesis validation). This would create unbounded recursive delegation with no orchestrator-side coordination of cross-framework context. The P-003 enforcement here is not bureaucratic compliance -- it is the architectural control that ensures the parent orchestrator retains authority to synthesize findings across frameworks, which is precisely the cross-framework integration value that makes the portfolio more than the sum of its parts."

#### Decision 6: Synthesis Hypothesis Validation (Steelmanned)

*[The confidence gate architecture is one of the strongest parts of the deliverable. The 3-tier structure, the structural omission of recommendation sections at LOW confidence, and the automation bias acknowledgment are all well-specified. The R5 addition of the 3-field structured evidence template adds concrete auditability. No changes.]*

---

### Acceptance Criteria (Steelmanned)

#### Pre-Launch Validation (Steelmanned)

**[SM-004-I8]** The BOOTSTRAP-VALIDATED mechanism (R6/R7 additions at lines 860-863) is architecturally significant -- it creates a two-tier quality validation system that degrades gracefully when ideal evaluator pools are not available. The framing, however, presents this primarily as a "bootstrap problem workaround" rather than what it actually is: a risk-managed launch path with transparent confidence tracking and automatic status degradation.

*Steelmanned framing:* Insert an explicit "Pre-Launch Validation Architecture" summary at the start of the Pre-Launch Validation section:

"The pre-launch validation system operates on two parallel tracks: (1) Full validation: 3 independent evaluators with criterion-(a) qualification compare AI-augmented output against external ground-truth. This is the gold standard. (2) Bootstrap validation: For Wave 1 adoption by communities without prior sub-skill evaluation experience, criterion-(b) qualification paths provide a structured fallback with explicit confidence tracking. BOOTSTRAP-VALIDATED benchmarks carry a 180-day deadline for full cross-validation. If the deadline passes without cross-validation, benchmarks downgrade to UNVERIFIED-BENCHMARK with visible L0 output flags -- the system signals reduced confidence rather than hiding it. This architecture enables adoption in real-world conditions (where 3 fully qualified evaluators may not be immediately available) without compromising the long-term integrity of the quality baseline."

This framing positions the BOOTSTRAP-VALIDATED mechanism as a risk management innovation rather than a compromise, which is its strongest interpretation.

---

### Research Backing (Steelmanned)

#### Adversarial Validation (Steelmanned)

**[SM-005-I8]** The adversarial validation paragraph (lines 994-1008) currently contains a disambiguation note added in R7 that is accurate but reads as defensive. Strengthen by foregrounding the validation completeness as a positive claim:

*Current (post-R7):* References to "Note: the '8 iterations, 13 revisions' figures refer to the Phase 1-3 research tournament..."

*Steelmanned:* "This issue body has itself undergone a separate C4 adversarial tournament (I1-I8) applying all 9 quality strategies across 8 iterations. The research tournament (8 iterations, 13 revisions, documented in `ux-framework-selection.md`) validated the framework selection. The issue body tournament (I1-I8, documented in `tournament-iter1/` through `tournament-iter8/`) validated the specification completeness. Two independent tournaments -- one for the decision, one for the document -- provide orthogonal validation coverage. The selection is trusted because it was attacked. The specification is trusted because it was attacked separately."

---

### Minor Strengthening Opportunities

**[SM-006-I8]** The ABANDON re-entry guard description (lines 642-643) is correctly specified but the consequence is understated. Add a brief framing sentence: "The re-entry guard is not a punishment mechanism -- it is a quality gate that ensures a team returning to an abandoned wave demonstrates concrete improvement rather than re-invoking the same failing pattern."

**[SM-007-I8]** The crisis mode 3-skill sequence rationale (line 431: "Heuristic Eval identifies *what* is wrong, Behavior Design diagnoses *why* users are not completing desired actions, HEART measures the *impact*") is sound. Strengthen by explicitly naming the complementarity property: "This sequence covers the full diagnostic trifecta: design-level defects (Heuristic), behavioral bottlenecks (Behavior Design), and quantified impact (HEART). Each sub-skill answers a question the others cannot."

**[SM-008-I8]** The Part-time UX Portfolio Fit upgrade from MEDIUM to HIGH (line 83) includes a well-formed justification note. Strengthen the traceability by adding a forward reference: "See the [Wave Deployment](#wave-deployment-5-criteria-gated-waves) section for the specific Wave 1-2 calibration details that justify the HIGH fit rating."

**[SM-009-I8]** The Haiku/T3 model selection for Heuristic Evaluation (lines 1235-1236) is appropriately qualified with the pre-launch benchmark requirement. Add a brief cost framing: "Haiku is selected for Wave 1 systematic checklist execution (10 discrete heuristics, structured finding template) because checklist evaluation is procedural, not reasoning-intensive. The cost reduction vs. Sonnet is significant at scale -- at >= 90% reliability (pre-launch benchmark), Haiku provides equivalent output quality at lower operational cost per evaluation. If the benchmark fails, Sonnet escalation is the defined path."

**[SM-010-I8]** The Sub-Skill Output Levels section (lines 1239-1248) is complete but L2 Strategic Implications is underspecified relative to L0 and L1. Add: "L2 output is the primary input for the parent orchestrator's cross-framework synthesis report. When 2+ sub-skills produce L2 output on the same product, the orchestrator identifies convergent strategic themes (e.g., both JTBD and Heuristic Eval pointing to the same user segment's unmet need) and divergent signals requiring human resolution."

---

## Improvement Findings Table

| ID | Improvement | Severity | Original | Strengthened | Dimension |
|----|-------------|----------|----------|--------------|-----------|
| SM-001-I8 | Portfolio non-redundancy declaration in Vision | Major | Non-redundancy stated implicitly in Research Backing and Framework Selection sections only | Explicit non-redundancy framing in Vision with three named properties (cadence orthogonality, output differentiability, C5 test) | Methodological Rigor |
| SM-002-I8 | Wave ordering rationale made explicit and positive | Major | "Wave deployment order differs from WSM rank because it optimizes for dependency satisfaction" -- descriptive, not evaluative | Explicit argument that later waves for high-WSM frameworks is not a compromise but deliberate sequencing architecture maximizing time-to-first-value | Internal Consistency |
| SM-003-I8 | P-003 consequence framing for UX-specific context | Major | P-003 compliance described as structural fact without UX-specific consequence articulation | Explicit consequence: without P-003, `/ux-design-sprint` could spawn `/ux-lean-ux` sub-agents, bypassing orchestrator cross-framework coordination authority | Evidence Quality |
| SM-004-I8 | BOOTSTRAP-VALIDATED framing as risk management innovation | Major | Presented primarily as "bootstrap problem workaround"; BOOTSTRAP-VALIDATED conditions buried in a long paragraph | Pre-Launch Validation Architecture summary framing both tracks (full + bootstrap) as risk-managed launch path with transparent confidence tracking | Actionability |
| SM-005-I8 | Dual-tournament orthogonal validation framing | Minor | Disambiguation note reads defensively -- "Note: the '8 iterations' figures refer to..." | Positive framing: two independent tournaments provide orthogonal validation coverage (one for the decision, one for the document) | Evidence Quality |
| SM-006-I8 | ABANDON re-entry guard purpose framing | Minor | Mechanism specified correctly but stated as restriction | Quality gate framing: ensures teams demonstrate concrete improvement rather than re-invoking the same failing pattern | Actionability |
| SM-007-I8 | Crisis mode complementarity property named | Minor | "Heuristic identifies what, Behavior diagnoses why, HEART measures impact" -- implicit complementarity | Explicit complementarity claim: "full diagnostic trifecta -- design-level defects, behavioral bottlenecks, quantified impact" | Methodological Rigor |
| SM-008-I8 | Part-time UX HIGH fit forward reference | Minor | Portfolio Fit rationale self-contained in population segments table note | Forward reference to Wave Deployment section where Wave 1-2 calibration detail lives | Traceability |
| SM-009-I8 | Haiku cost framing for model selection | Minor | Model selection stated with benchmark requirement; cost benefit not articulated | Cost framing: Haiku at >= 90% reliability provides equivalent quality at lower operational cost per evaluation vs. Sonnet | Completeness |
| SM-010-I8 | L2 output role in cross-framework synthesis | Minor | L2 "Strategic implications" purpose stated generically | Explicit: L2 is the primary input for parent orchestrator cross-framework synthesis; identifies convergent themes and divergent signals | Completeness |

---

## Improvement Details

### SM-001-I8: Portfolio Non-Redundancy Declaration in Vision

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Vision (line 34-38) |
| **Strategy Step** | Step 3 (Reconstruct), Step 2 (Structural weakness) |

**Evidence (before):**
The Vision section states the portfolio covers "the full product lifecycle from discovery through post-launch measurement" but does not explain the selection logic. The non-redundancy argument appears 1,000+ lines later in Research Backing (line 1006): "The selection is not '10 highest-scoring frameworks' -- it is a deliberately non-redundant portfolio where each framework fills a unique lifecycle niche."

**Strengthened:**
Add to Vision after the sub-skills architecture paragraph: "The 10 sub-skills are selected, not ranked: a deliberately non-redundant portfolio where each framework fills a unique lifecycle niche -- not the 10 highest-scoring frameworks, but the 10 that together cover the full lifecycle without redundant coverage. Three independent non-redundancy properties validated: cadence orthogonality, output differentiability, and C5 portfolio-composition test. Full selection rationale in [Research Backing](#research-backing)."

**Rationale:** Downstream critique strategies (S-002, S-004) will attack the framework selection logic. Establishing the non-redundancy argument in Vision ensures the deliverable's strongest case is visible at the point where a reviewer forms their first impression.

**Best Case Conditions:** This framing is strongest when the reviewer is evaluating the portfolio as a product design decision (which frameworks to include) rather than as a scoring exercise. Given the issue's audience (Jerry framework contributors and users), this is the dominant interpretation.

---

### SM-002-I8: Wave Ordering Rationale as Positive Architecture

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Detailed Sub-Skill Descriptions ordering note (line 166-167) |
| **Strategy Step** | Step 3 (Reconstruct), Step 2 (Presentation weakness) |

**Evidence (before):**
"Sub-skill descriptions below are ordered by Wave deployment sequence (Wave 1 first), not by WSM selection rank. Wave deployment order differs from WSM rank because it optimizes for dependency satisfaction and learning curve -- high-WSM frameworks that depend on Wave 1 outputs deploy in later waves."

**Strengthened:**
Add: "This is not a compromise on quality -- it is deliberate sequencing architecture. The highest-WSM frameworks (Design Sprint: 8.65, Atomic Design: 8.55) deploy in later waves because they produce their full value only when Wave 1 frameworks have established foundational capability. Wave 1 is the dependency-free, immediately actionable entry that maximizes time-to-first-value for the median Part-time UX team."

**Rationale:** A reviewer seeing Design Sprint at Wave 5 might infer it is deprioritized. This framing preempts that misreading and strengthens the internal consistency argument (high scores don't imply early deployment; early deployment is dependency-free, not low-value).

**Best Case Conditions:** Strongest when the reviewer understands the Part-time UX context (20-50% time allocation, Wave 1 calibrated for immediate value). The wave ordering note is immediately adjacent to the sub-skill descriptions where the reviewer will first encounter Wave 5 high-scorers.

---

### SM-003-I8: P-003 UX-Specific Consequence

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions -- P-003 Compliant Single-Level Nesting (lines 492-510) |
| **Strategy Step** | Step 3 (Add missing evidence), Step 2 (Evidence weakness) |

**Evidence (before):**
"The parent orchestrator (`ux-orchestrator`) is the only T5 agent with Task tool access. All sub-skill agents are T2-T3 and cannot spawn further sub-agents. Workers return results to the orchestrator, which coordinates cross-framework integration."

The consequence of violating P-003 is described generically (from Jerry constitution) but not in terms specific to the UX skill portfolio.

**Strengthened:**
Add: "For the UX portfolio specifically, this matters because sub-skills have natural cross-invocation temptation: `/ux-design-sprint` Day 2 ideation could theoretically benefit from `/ux-lean-ux` hypothesis generation; `/ux-behavior-design` B=MAP diagnosis could benefit from `/ux-heart-metrics` data. Without strict P-003 enforcement, sub-skills could spawn each other, bypassing the orchestrator's cross-framework coordination authority. The parent orchestrator is the only entity that can synthesize findings across frameworks -- that synthesis is the primary value over running sub-skills individually."

**Rationale:** The P-003 section currently reads as compliance rather than design reasoning. For a 10-sub-skill portfolio with natural cross-invocation temptations, the UX-specific consequence articulation transforms this from "rule we follow" into "architectural principle we chose."

**Best Case Conditions:** This framing is strongest when the reviewer is evaluating architectural coherence, not just P-003 rule compliance.

---

### SM-004-I8: BOOTSTRAP-VALIDATED as Risk Management Innovation

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Pre-Launch Validation (lines 860-863) |
| **Strategy Step** | Step 3 (Strengthen framing), Step 2 (Presentation weakness) |

**Evidence (before):**
The BOOTSTRAP-VALIDATED mechanism is introduced mid-paragraph within the pre-launch validation AC, in a paragraph that has grown to ~250 words with R6/R7 additions. The mechanism is correct and complete but is framed as an exception path ("For Wave 1 adoption by a community with no prior sub-skill evaluations...") rather than as a designed system feature.

**Strengthened:**
Add a "Pre-Launch Validation Architecture" preamble before the detailed AC checkbox:

"The pre-launch validation system operates on two parallel tracks with explicit confidence tracking:
- **Full Validation Track:** 3 independent criterion-(a) evaluators compare AI output against external ground-truth. Gold standard. No confidence qualifier required.
- **Bootstrap Validation Track:** For communities without prior sub-skill evaluation history, criterion-(b-i/b-ii) qualification paths provide a structured fallback. BOOTSTRAP-VALIDATED status persists with 180-day active deadline for cross-validation. If the deadline passes, benchmarks auto-degrade to UNVERIFIED-BENCHMARK with visible L0 output flags.

This is not a workaround -- it is a risk-managed launch path that enables adoption in real-world conditions while maintaining long-term quality baseline integrity through transparent status tracking and automatic degradation."

**Rationale:** The BOOTSTRAP-VALIDATED mechanism is one of the most sophisticated quality management innovations in the deliverable. Framing it as a risk management design rather than an exception path gives downstream critique strategies (S-002: "this is a compromise") an accurate, stronger counter-argument.

**Best Case Conditions:** Strongest when the reviewer evaluates the deliverable in the context of real-world adoption constraints. The BOOTSTRAP-VALIDATED mechanism only makes sense as a design choice, not a workaround, when its degradation mechanism is surfaced prominently.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Positive | SM-009-I8 (Haiku cost framing), SM-010-I8 (L2 synthesis role) fill minor specification gaps. SM-004-I8 surfaces implicit architecture. |
| Internal Consistency | 0.20 | Positive | SM-002-I8 resolves latent tension between Wave ordering and WSM ranking. SM-001-I8 makes non-redundancy argument consistent across Vision and Research Backing. |
| Methodological Rigor | 0.20 | Positive | SM-001-I8 (non-redundancy framing), SM-003-I8 (P-003 consequence), SM-007-I8 (crisis mode complementarity) all strengthen the reasoning chain from design decisions to architecture properties. |
| Evidence Quality | 0.15 | Positive | SM-003-I8 adds UX-specific consequence evidence. SM-005-I8 reframes dual-tournament coverage as an active argument rather than a defensive note. |
| Actionability | 0.15 | Positive | SM-004-I8 makes BOOTSTRAP-VALIDATED mechanism more actionable by surfacing the two-track architecture. SM-006-I8 clarifies ABANDON re-entry guard purpose. |
| Traceability | 0.10 | Positive | SM-008-I8 adds forward reference from Part-time UX fit claim to Wave Deployment calibration evidence. |

---

## Execution Statistics

- **Total Findings:** 10
- **Critical:** 0
- **Major:** 4
- **Minor:** 6
- **Protocol Steps Completed:** 6 of 6

---

## Best Case Scenario (Step 4)

The steelmanned deliverable is most compelling under these conditions:

1. **Reviewer understands Tiny Teams context.** The portfolio makes maximum sense to someone who has experienced the UX capability gap directly -- a developer who has shipped products without UX expertise and faced the consequences. The problem framing (lines 50-64) is strongest for this audience.

2. **Non-redundancy is accepted as the selection logic.** The 10 frameworks are stronger as a portfolio than as the 10 highest-scoring individual frameworks. If the reviewer accepts that Kano (7.65) and Behavior Design (7.60) fill lifecycle niches that higher-scoring but more redundant frameworks would not cover, the selection rationale holds.

3. **The confidence gate architecture is evaluated as a whole.** The 3-tier confidence gating, the structural omission of LOW-confidence recommendation sections, the automation bias acknowledgment, and the 3-field structured evidence template for overrides work together as a coherent system. Evaluating any one component in isolation misses the cumulative protection.

4. **Wave progression is understood as a learning sequence, not a delay mechanism.** The wave gates are strongest when understood as readiness criteria that prevent teams from applying advanced frameworks before establishing the foundational skills. The KICKOFF-SIGNOFF -> Wave 1 -> Wave 2... sequence is a structured onboarding path, not a gatekeeping mechanism.

**Key assumptions that must hold:**
- Tiny Teams (1-5 people) represents a real and growing population with unmet UX capability needs (supported by Gartner 2026 data)
- AI-augmented workflows can meaningfully accelerate structured UX activities for non-specialists (projected, not fully validated -- honestly disclosed)
- The 10 frameworks are executable by non-UX-specialists with AI assistance (design target for Wave 1-2 sub-skills; requires pre-launch benchmark validation to confirm)
- Jerry's MCP integration ecosystem is stable enough to support 6 MCP server dependencies (mitigated by non-MCP fallback paths for all 10 sub-skills)

**Confidence assessment:** HIGH for the core proposition (tiny teams have a UX gap; structured AI-augmented frameworks can reduce it). MEDIUM for the specific execution claims (AI produces outputs at X% quality; Haiku achieves >= 90% on Figma evaluation). MEDIUM ratings are appropriately flagged throughout.

---

*Steelman Report: S-003-I8 | adv-executor | 2026-03-03*
*Template: s-003-steelman.md v1.0.0*
*SSOT: .context/rules/quality-enforcement.md*
*H-16 Status: Compliant -- S-003 executes first; S-002 may proceed*
