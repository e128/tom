# Steelman Report: feat: Add `/user-experience` skill -- AI-augmented UX for Tiny Teams

## Steelman Context

- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Deliverable Type:** Enhancement Issue (GitHub Issue body / design specification)
- **Criticality Level:** C4 (Critical -- architecture addition, irreversible once merged, tournament mode)
- **Strategy:** S-003 (Steelman Technique)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Steelman By:** adv-executor | **Date:** 2026-03-03T00:00:00Z | **Original Author:** Saucer Boy voice / Jerry framework
- **Iteration:** 5 (R4 applied 23 fixes from Iter 4 critique findings; this steelman evaluates the post-R4 revision)

---

## Summary

**Steelman Assessment:** The post-R4 deliverable has incorporated 23 fixes and is now structurally comprehensive -- agent definitions, governance, MCP coordination, confidence gates, cross-skill handoffs, audit logging, and wave progression enforcement are all specified. The document has crossed a threshold: the main risk is no longer "is this specified well enough to implement?" but "will a reviewer reading this for the first time find the strongest argument accessible?" Six of eight Iter4 findings were NOT incorporated (SM-003 through SM-008-I4) and two were only partially incorporated (SM-001, SM-002). This iteration re-examines all unincorporated findings with fresh eyes and identifies three new strengthening opportunities surfaced by R4's additions that create new argument-completeness gaps.

**Improvement Count:** 1 Critical, 3 Major, 4 Minor

**Original Strength:** Post-R4, this is among the most thoroughly specified feature enhancement issues in the Jerry corpus. The architecture is implementation-ready. The remaining gap is the persuasion layer -- six argument-completeness improvements from Iter4 are still unincorporated, and three new R4-specific gaps have emerged.

**Recommendation:** Incorporate improvements. SM-001-I5 (Part-time UX framing completeness -- carries from Iter4) is the single highest-impact unaddressed finding; it affects the most likely reader segment. SM-003-I5, SM-004-I5, and SM-005-I5 (persistent Majors from Iter4) address the quality provenance, rubric calibration, and compound workflow stories that are the most frequently challenged aspects of enhancement proposals of this type.

---

## Steelman Reconstruction

The following reconstruction presents the deliverable in its strongest form at Iteration 5. Changes are annotated with `[SM-NNN-I5]` identifiers. Sections not annotated are preserved as-is from the post-R4 deliverable. Findings that were in Iter4 but not incorporated are re-presented here with updated context; findings that were in Iter4 and incorporated (even partially) are evaluated for completeness.

---

### The Problem > Who This Is For: Tiny Teams Population Segments (persistent Critical -- SM-001-I5)

*[Population segments table preserved as-is.]*

R4 added: "Population segments (Solo Practitioner, Part-time UX, Dedicated UX) define the range of teams this skill serves. Part-time UX (20-50% allocation) is the most common segment based on Gartner's Tiny Teams research. Each wave's entry criteria and time estimates are calibrated for this median case."

[SM-001-I5] This is progress -- the Part-time UX segment is now identified as the most common. However, two gaps remain from the Iter4 Critical finding:

1. The **segment table** still shows "MEDIUM" for Portfolio Fit for the Part-time UX row, with caveats about Kano and HEART exceeding capacity. This creates a contradiction: the paragraph below the table says Part-time UX is the primary design center, but the table implies MEDIUM suitability. A reader scanning the table gets the wrong signal before reading the paragraph.

2. The **strongest conclusion** from this evidence is still not drawn: Wave 1-2 sub-skills are a genuine capability gain for the Part-time UX team, not a consolation. The framing treats Wave 1-2 as "what you settle for" rather than "what you were designed for."

**Strengthened additions:**

1. **Table fix** -- In the Part-time UX row, change Portfolio Fit from:
   > "MEDIUM -- Kano and HEART may exceed part-time capacity; prioritize Wave 1-2 only"

   To:
   > "HIGH for Wave 1-2 (the primary design center for this skill portfolio); MEDIUM for Wave 3-5 (Kano and HEART may exceed part-time capacity -- treat as aspirational)"

2. **Paragraph strengthening** -- After the existing "Part-time UX is the most common segment" paragraph, add:

   > This framing has a practical implication for the Part-time UX reader evaluating whether this skill is for them: the Portfolio Fit rating in the table above reflects Wave 1-5 combined. For the sub-skills a Part-time UX person will actually use -- Heuristic Eval, JTBD, HEART, and Behavior Design -- the fit is HIGH. Wave 1-2 are not "what you settle for without a UX specialist." They are the primary return on investment for the most common tiny team configuration. A Part-time UX person running Wave 1 gains structured heuristic evaluation and job statement synthesis: two capabilities that previously required either a UX contractor or going without.

---

### The Problem > Who This Is For: Tiny Teams Population Segments > Wave 1 time-to-first-value (persistent Critical -- SM-002-I5)

*[R4-added "Wave 1 time-to-first-value" paragraph preserved as-is.]*

R4 added: "A team completing the kickoff-signoff and running their first Nielsen Heuristic Evaluation sub-skill should reach initial findings within a single work session (estimated 2-4 hours including setup). This estimate will be validated during pre-launch testing."

[SM-002-I5] This is progress but is not yet in the strongest position. The Iter4 Critical finding identified two elements needed:

1. **The anchor** -- Teams apprehensive about the 30-50 day total estimate should anchor on Wave 1 specifically (8-13 days), not the total. The paragraph currently does not establish this anchor.
2. **The KICKOFF-SIGNOFF setup cost** -- Making the 20-minute setup cost explicit converts the "2-4 hours" from a vague claim to a specific commitment.

The paragraph also currently lives in "The Problem > Who This Is For" -- before Wave Deployment is discussed. The most persuasive placement is near the Wave Deployment section, adjacent to the 30-50 day estimate, where the apprehension is highest. However, since relocation would be a structural change, the strengthening here adds the anchor and setup specificity:

**Strengthened replacement for the R4-added paragraph:**

> **Wave 1 time-to-first-value:** The KICKOFF-SIGNOFF.md completion is a one-time 20-minute setup exercise. After that, a developer with no UX background can invoke `/ux-heuristic-eval` with a design screenshot and receive a severity-rated findings report against all 10 Nielsen heuristics -- no prior wave, no MCP tools, no UX training required. From kickoff to first heuristic findings report: **estimated 2-4 hours** (pending pre-launch validation). Teams apprehensive about the 30-50 day total estimate should anchor on Wave 1: **8-13 days of implementation effort**, value delivered in the first session after completion. The 3-state wave enforcement (PASS/WARN/BLOCK) governs access to Wave 2+; it does not delay Wave 1 value.

---

### Research Backing > Adversarial Validation (persistent Major -- SM-003-I5)

*[Adversarial Validation section preserved as-is from post-R4 deliverable.]*

The adversarial validation section still reads:

> "The trust argument: not that the analysis is perfect, but that it has been systematically attacked from nine different angles and survived. The selection is not '10 highest-scoring frameworks' -- it is a deliberately non-redundant portfolio where each framework fills a unique lifecycle niche, validated through three independent non-redundancy properties..."

[SM-003-I5] This finding has been present since Iter3 without incorporation. The current text asserts process completeness ("systematically attacked from nine different angles and survived") without demonstrating outcome substance. A skeptical reviewer can accept that the tournament ran while still questioning whether it changed anything material.

**Strengthened addition after the tournament summary table:**

> **What the tournament changed.** The pre-tournament deliverable had three categories of weakness that the adversarial process found and corrected -- these are verifiable in the R1-R4 change annotations throughout this document:
>
> 1. **Arithmetic errors (Chain-of-Verification, R2):** Five arithmetic errors in the WSM scoring were found and corrected. Three framework selection rankings changed. The `/ux-heuristic-eval` score moved from 9.25 to 9.05; `/ux-behavior-design` from 7.45 to 7.60; `/ux-kano-model` from 7.50 to 7.65. The final selection reflects verified calculations.
>
> 2. **Design contradiction resolved (FMEA, R2):** The `/ux-behavior-design` sub-skill had a contradiction between its LOW-confidence structural omission gate and an output labeled "design intervention recommendations." A LOW-confidence sub-skill cannot produce prescriptive recommendations. Resolution required a deliberate design decision: rename to "Reference Intervention Patterns," reclassify as MEDIUM confidence, and restructure the output contract. This changed what the sub-skill promises to deliver.
>
> 3. **Enforcement closure gaps (Pre-Mortem, Red Team, R1-R3):** The original specification had no Issue Closure Condition (any AC could be treated as blocking), no WAVE-N-SIGNOFF.md enforcement (wave gates were aspirational, not checked), no pre-launch external validation requirement, and no Human Override audit log. All four are now closed with specific mechanisms. The specification went from "gates defined" to "gates enforced."
>
> A specification that corrected 5 arithmetic errors, resolved a design contradiction, and closed 4 enforcement gaps is structurally different from one that merely ran a process. The selection is not the result of a first-draft analysis that survived critique -- it is the result of a self-correcting process with documented, specific corrections.

---

### Acceptance Criteria > Pre-Launch Validation (persistent Major -- SM-004-I5)

*[Pre-launch validation AC preserved as-is from post-R4 deliverable, including the R3-added blind evaluation rubric.]*

The current text reads: "Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions."

[SM-004-I5] This finding was present in Iter4 without incorporation. The 15% threshold and the 3-dimension selection (completeness, actionability, time-to-insight) are stated without derivation. A reviewer challenging the benchmark can ask "why 15%?" and "why those three dimensions?" without getting an answer from the document.

The blind evaluation rubric is the most concrete quality enforcement mechanism in the specification. If the rubric appears arbitrary, the entire pre-launch quality gate loses credibility.

**Strengthened replacement for the pass threshold sentence:**

> Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions. **Calibration rationale:** The 3 dimensions are selected because they map to the three most common failure modes of AI-augmented structured-analysis outputs: (a) **completeness** catches systematic omission bias -- AI models trained on summarized content tend to miss edge cases present in original research; (b) **actionability** catches specificity degradation -- AI outputs that are technically correct but insufficiently specific for a team to act on them; (c) **time-to-insight** catches efficiency regression -- a benchmark that takes 2x as long to produce is not an improvement even if output quality is equivalent. The **15% threshold** is conservative by design: an 85% quality floor against a human-produced reference output is the minimum bar for a structured methodology tool that teams will use to make product decisions. A 25% threshold would permit AI-augmented outputs that meaningfully underperform manual analysis; a 5% threshold would be unrealistically demanding for AI tools producing structured synthesis. If empirical data from Wave 1 beta usage indicates the threshold requires recalibration, the threshold is revisited with evidence.

---

### Key Design Decisions > 2. Parent Orchestrator Routes via Lifecycle-Stage Triage > BLOCK State UX (persistent Minor -- SM-005-I5)

*[BLOCK state definition preserved as-is: "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process."]*

[SM-005-I5] The mechanism is correct; the user experience of the block is absent. A BLOCK state that produces an opaque refusal will be experienced as the skill being broken; a BLOCK state with a resolution path will be experienced as a guardrail.

**Strengthened addition after the BLOCK state definition:**

> **BLOCK state orchestrator message:** When `WAVE-{N}-SIGNOFF.md` does not exist, the orchestrator produces:
>
> > "Wave {N+1} sub-skills ({list}) require Wave {N} completion. `WAVE-{N}-SIGNOFF.md` has not been created. To advance: (1) complete the Wave {N} entry criteria (listed in the [Wave Deployment table](#5-wave-deployment-5-criteria-gated-waves)); (2) complete `WAVE-{N}-SIGNOFF.md` using the template at `skills/user-experience/templates/wave-signoff-template.md`; (3) re-invoke `/user-experience`. If your team needs to proceed despite incomplete Wave {N} criteria, the bypass process is available -- invoke `/user-experience bypass` and the orchestrator will walk you through 3-field bypass documentation."
>
> The BLOCK state does not terminate the session. Wave 1 through {N} sub-skills remain available for direct invocation. This preserves user authority (P-020) while enforcing the wave prerequisite gate.

---

### Estimated Scope (persistent Minor -- SM-006-I5)

*[Estimated Scope section preserved as-is, ending with the calibration note.]*

[SM-006-I5] The Estimated Scope section ends with a calibration note ("If Wave 1 completion exceeds 15 days, the per-sub-skill estimates should be revised upward") that is tonally flat relative to the rest of the document. Every major persuasion section closes with a McConkey mountain metaphor callback; the Scope section does not.

**Strengthened addition after the final calibration note:**

> Wave 1 is the first drop-in. Eight to thirteen days -- that is the commitment. Every subsequent wave is a follow-on line off the same peak. You ski them when the first one goes clean.

---

### V2 Roadmap > V2 Candidates (persistent Minor -- SM-007-I5)

*[V2 Candidates table preserved as-is, including the Service Blueprinting P1 row.]*

[SM-007-I5] The Service Blueprinting P1 row reads: "Covers end-to-end service process niche; also the auto-substitute if AI-First Design Enabler expires." The P1 priority is asserted without explaining why a 7.40-score framework ranks P1 while other higher-scoring V2 candidates may be unlisted. The dual-purpose justification explains the apparent inconsistency but is not stated.

**Strengthened replacement for the Service Blueprinting P1 row description:**

> Covers end-to-end service process niche; **dual-purpose P1 priority**: (1) fills the service design lifecycle gap not covered by any V1 framework; (2) is the pre-committed auto-substitute if the AI-First Design Enabler expires at Wave 5 -- this substitution path is declared in the Known Limitations section, making Service Blueprinting the only V2 candidate with a pre-activated adoption trigger. Score 7.40 ranks lower than AI-First Design (7.80P) but Service Blueprinting's P1 V2 status is pre-approved by the V1 conditional design: if the AI-First Design Enabler expires, Service Blueprinting activates without further prioritization debate.

---

### Relationship to Existing Jerry Skills (persistent Minor -- SM-008-I5)

*[Mermaid ecosystem diagram and integration table preserved as-is.]*

[SM-008-I5] The ecosystem integration section maps directional relationships but does not demonstrate compound value -- the case that using Jerry skills in sequence produces more than the sum of individual outputs. The current integration table lists skill relationships but does not show the full discovery-to-measurement loop that is the highest-value use of the ecosystem.

**Strengthened addition after the integration table:**

> **The compound workflow story.** The highest-value use of the Jerry ecosystem is the full discovery-to-measurement loop:
>
> 1. `/problem-solving` (`ps-researcher`) provides competitive context for JTBD job analysis -- the market research that answers "what jobs are users already hiring alternatives to do?"
> 2. `/ux-jtbd` converts that research into specific job statements defining the product challenge -- the "why are we building this?" answered before design begins.
> 3. `/ux-design-sprint` uses the JTBD job statement as its challenge statement input -- Day 1 of the Sprint starts with a validated problem, not a guess.
> 4. `/nasa-se` converts Sprint findings (validated prototype with Day 4 test data) into technical requirements with UX-grounded acceptance criteria -- requirements that trace to observed user behavior.
> 5. `/ux-heart-metrics` measures whether the shipped product achieves the goals defined by the job statements from Step 2 -- the loop closes on the original user need.
> 6. `/adversary` provides quality gates on the UX deliverables at wave transitions -- the same adversarial rigor applied to the `/user-experience` skill specification is available to validate its outputs.
>
> A team running this full loop produces a product where user research (JTBD) directly informs the sprint challenge, the sprint prototype directly informs technical requirements, and UX metrics measure against the original job-to-be-done. Teams already using `/problem-solving` and `/nasa-se` get compounding return from adding `/user-experience`. The incremental adoption question becomes: "what does adding Wave 1 cost against our existing Jerry workflow?" rather than "is a 30-50 day investment justified?"

---

### Sub-Skill Model Selection > Heuristic Evaluation Model (new Minor -- SM-009-I5)

*[Sub-Skill Model Selection table preserved as-is.]*

[SM-009-I5] The model selection rationale for `/ux-heuristic-eval` assigns `haiku` with the rationale "checklist-based systematic evaluation against 10 discrete heuristics; procedural, not reasoning-intensive." This is the only `haiku` assignment in the portfolio. The rationale is directionally sound but potentially underspecifies the risk.

Heuristic evaluation is checklist-based for routine violations (e.g., missing error messages, absent feedback) but the most valuable findings require contextual inference -- identifying H4 (Consistency and Standards) violations requires cross-platform knowledge; H7 (Flexibility and Efficiency) violations require user population judgment. These are judgment calls that may exceed `haiku`'s reasoning capability.

**Strengthened model selection note for Heuristic Evaluation:**

> **`haiku` assignment rationale and risk note:** The 10-heuristic checklist execution is procedural and `haiku`-appropriate for severity-0 through severity-2 violations (clear violations of explicit rules). Severity-3 and severity-4 violations -- which require contextual judgment about platform conventions, user population expectations, and cross-component consistency -- may produce lower-quality findings at `haiku`. The quality benchmark AC (identifies >= 7 of 10 known violations in a reference design) SHOULD include a severity distribution check: if < 50% of correctly identified violations are severity-3/4, upgrade to `sonnet` during Wave 1 implementation. The `haiku` assignment is a cost-optimization hypothesis to be validated, not a fixed choice.

---

### Best Case Scenario (updated for Iter 5)

The `/user-experience` skill proposal is most compelling under the following conditions:

1. **Team size 2-5, with UX as a part-time responsibility.** This is the median scenario, not an edge case. Wave 1-2 deliver HIGH capability-per-hour return for this configuration -- not MEDIUM. The "MEDIUM" portfolio fit in the table refers to Wave 3-5 access, not the primary Wave 1-2 value.

2. **Teams already in the Figma + Miro workflow.** The Minimal tier (~$23/seat/month) unlocks 9 of 10 sub-skills. The incremental tool cost of `/user-experience` is zero for these teams.

3. **Products with iterative design cycles (bi-weekly releases or faster).** The Lean UX hypothesis cycle and Heuristic Eval iteration pattern are optimized for high-cadence iteration.

4. **Jerry framework users already using `/problem-solving` and `/nasa-se`.** These teams get the full compound discovery-to-measurement loop: JTBD informs Sprint challenge, Sprint findings inform NASA-SE requirements, HEART closes the loop on original job-to-be-done.

5. **Teams blocked on methodology knowledge, not on time.** The skill removes the methodology knowledge barrier. Users still need to provide screenshots, conduct interviews, and interpret findings -- time constraint is not eliminated.

**Key assumptions that must hold:**

- MCP server availability for Figma-dependent sub-skills (mitigated by documented non-MCP fallbacks for all 4 Figma-required sub-skills)
- AI LLM capability sufficient to apply 10-heuristic evaluation, B=MAP diagnosis, and Kano classification with acceptable accuracy (mitigated by per-sub-skill quality benchmarks with blind external validation; `haiku` assignment for Heuristic Eval validated against severity distribution in Wave 1 implementation)
- Teams willing to invest 8-13 days for Wave 1 before first return (mitigated: first deliverable estimated in 2-4 hours from kickoff completion, pending pre-launch validation)

**Confidence in the Steelmanned version:** HIGH. SM-001-I5 and SM-002-I5 are persistent Criticals that remain partially incorporated -- the underlying evidence is in the document but the strongest conclusion has not been drawn. SM-003-I5, SM-004-I5, SM-007-I5, SM-008-I5 are Major/Minor persistent gaps with no incorporation across two iterations. SM-009-I5 is a new gap surfaced by R4's model selection table. None are substantive flaws -- all are argument-completeness and presentation-layer improvements on a structurally sound specification.

---

## Improvement Findings Table

| ID | Improvement | Severity | Original (Before) | Strengthened (After) | Dimension |
|----|-------------|----------|-------------------|----------------------|-----------|
| SM-001-I5 | Part-time UX portfolio fit table contradiction and incomplete primary design center framing | Critical | Table shows MEDIUM fit for Part-time UX; paragraph below says it is the most common segment -- contradiction. Strongest conclusion (Wave 1-2 = HIGH fit, genuine capability gain) not present | Table fix: Wave 1-2 = HIGH, Wave 3-5 = MEDIUM. Paragraph addition: Part-time UX is the primary return on investment; Wave 1-2 described as genuine gain, not fallback | Evidence Quality / Actionability |
| SM-002-I5 | Wave 1 time-to-first-value anchor and setup cost specificity | Critical | Added paragraph identifies "2-4 hours including setup" without anchoring to Wave 1 (8-13 days), without specifying KICKOFF-SIGNOFF cost (~20 min), and without countering the 30-50 day apprehension | Replacement paragraph: KICKOFF-SIGNOFF ~20 min explicit; from-kickoff-to-first-findings path named; 8-13 day Wave 1 anchor vs. 30-50 day total; 3-state enforcement does not delay Wave 1 value | Actionability / Completeness |
| SM-003-I5 | Adversarial validation demonstrates specific corrections, not just process completion | Major | "Systematically attacked from nine angles and survived" -- process claim without outcome specifics. Third iteration without incorporation | Added: three categories of specific corrections with verifiable R-annotation evidence trail: 5 arithmetic errors with changed rankings named; design contradiction with resolution described; 4 enforcement gaps closed with mechanism names | Evidence Quality / Traceability |
| SM-004-I5 | Blind evaluation rubric calibration rationale | Major | 15% threshold and 3 dimensions stated without derivation. Second iteration without incorporation | Each dimension maps to a named AI output failure mode; 15% threshold justified as conservative floor with comparison to permissive (25%) and demanding (5%) alternatives; recalibration trigger defined | Methodological Rigor / Evidence Quality |
| SM-005-I5 | BLOCK state orchestrator message template | Minor | BLOCK state behavior described; no message template. Second iteration without incorporation | Concrete message template with: sub-skill list, template location reference, bypass path, direct invocation fallback for Wave 1-N; P-020 preserved | Completeness / Actionability |
| SM-006-I5 | McConkey metaphor close for Estimated Scope | Minor | Scope ends with calibration note; only section without McConkey voice. Second iteration without incorporation | One McConkey sentence: "Wave 1 is the first drop-in. Eight to thirteen days -- that is the commitment. Every subsequent wave is a follow-on line off the same peak." | Internal Consistency |
| SM-007-I5 | Service Blueprinting V2 P1 dual-purpose justification | Minor | P1 status asserted; 7.40 score appears inconsistent with P1 rank; no explanation | Dual-purpose: gap coverage + pre-committed substitution path; explains why score rank does not match priority rank | Traceability |
| SM-008-I5 | Compound workflow value of Jerry ecosystem integration | Minor | Integration table maps directional relationships; compound sequential value not demonstrated | 6-step full discovery-to-measurement loop; incremental adoption framing changes question from "30-50 days justified?" to "what does adding Wave 1 cost against existing workflow?" | Actionability / Completeness |
| SM-009-I5 | Heuristic Evaluation haiku assignment severity distribution risk | Minor | `haiku` assigned with "procedural" rationale; severity-3/4 violations require contextual inference that may exceed haiku capability | Risk note + validation hook: if severity distribution check < 50% of correctly-identified violations are severity-3/4, upgrade to sonnet; haiku assignment as cost-optimization hypothesis to validate | Methodological Rigor |

---

## Improvement Details

### SM-001-I5: Part-time UX Portfolio Fit Table Contradiction

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | The Problem > Who This Is For: Tiny Teams Population Segments |
| **Affected Dimension** | Evidence Quality / Actionability |

**Original Content (line 83-85):**

> Segment table shows "MEDIUM -- Kano and HEART may exceed part-time capacity; prioritize Wave 1-2 only" as Part-time UX Portfolio Fit. Paragraph below table: "Part-time UX (20-50% allocation) is the most common segment... calibrated for this median case."

**Strengthened Content:** See reconstruction. Two changes: (1) table fix -- split Portfolio Fit to "HIGH for Wave 1-2; MEDIUM for Wave 3-5"; (2) paragraph addition -- "Part-time UX reader: portfolio fit in the table is Wave 1-5 combined; for the sub-skills you will actually use, fit is HIGH."

**Rationale:** The table is the first thing a Part-time UX reader processes. If the table says MEDIUM, the paragraph's claim that this is the primary design center is contradicted before it is read. The contradiction is not a logical flaw in the specification -- Wave 1-2 really is HIGH fit and Wave 3-5 is MEDIUM -- but the combined rating obscures this. Splitting the Portfolio Fit by wave tier resolves the contradiction and directs the Part-time UX reader toward the waves designed for them. This finding has been present since Iter3 and partially addressed (paragraph added) but the table contradiction has not been fixed. The table fix is the missing half.

**Best Case Conditions:** Most effective for Part-time UX readers encountering the skill for the first time. The table is the first substantive content they see; it must signal HIGH fit for their configuration before they read further.

---

### SM-002-I5: Wave 1 Time-to-First-Value Anchor

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | The Problem > Who This Is For: Tiny Teams Population Segments (currently); strongest placement is Key Design Decisions > Wave Deployment |
| **Affected Dimension** | Actionability / Completeness |

**Original Content (line 89):**

> "A team completing the kickoff-signoff and running their first Nielsen Heuristic Evaluation sub-skill should reach initial findings within a single work session (estimated 2-4 hours including setup). This estimate will be validated during pre-launch testing."

**Strengthened Content:** See reconstruction. Key additions: KICKOFF-SIGNOFF ~20 min explicit; 8-13 day Wave 1 anchor vs. 30-50 day total; wave enforcement does not delay Wave 1 value.

**Rationale:** The R4 paragraph added the time estimate but not the decision-making context. A team deciding whether to begin Wave 1 is asking: "when do I see something useful, and how does that compare to the total investment?" The answer -- useful output in the first session, Wave 1 effort is 8-13 days not 30-50 days, enforcement governs Wave 2+ not Wave 1 -- requires all three elements. The R4 paragraph provides the first element but not the second and third. The 30-50 day total appears in the Estimated Scope section and is the most prominent scope signal in the document; without explicitly countering it in the time-to-first-value statement, the total dominates the adoption calculus.

**Best Case Conditions:** Most compelling for teams evaluating whether to begin Wave 1 implementation. The "under 2-4 hours to first output" claim combined with "8-13 day Wave 1 effort" reframes the decision as a bounded commitment with immediate returns.

---

### SM-003-I5: Adversarial Validation Quality Provenance

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Research Backing > Adversarial Validation |
| **Affected Dimension** | Evidence Quality / Traceability |

**Original Content (lines 966-978):**

> Tournament summary table. Closing: "not that the analysis is perfect, but that it has been systematically attacked from nine different angles and survived."

**Strengthened Content:** See reconstruction. Three categories of specific corrections with verifiable R-annotation evidence trail.

**Rationale:** "Survived systematic attack" is a process claim. A reviewer can accept that the tournament ran while questioning whether it was rigorous enough to catch real problems. The quality provenance argument is different: it shows the tournament found and corrected specific errors. The corrections are verifiable -- the R1-R4 annotations throughout the document are the evidence trail. The difference between "the process ran" and "the process worked" is the difference between procedural compliance and substantive quality improvement. This finding has been present since Iter3. Its persistent non-incorporation suggests it belongs in the author's highest-priority revision queue: it is the strongest possible evidence of the skill specification's credibility.

**Best Case Conditions:** Strongest when the reviewer has encountered analyses that underwent "review" but emerged unchanged. The specific-corrections framing proves the adversarial process had teeth.

---

### SM-004-I5: Blind Evaluation Rubric Calibration Rationale

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria > Pre-Launch Validation |
| **Affected Dimension** | Methodological Rigor / Evidence Quality |

**Original Content (line 857 -- relevant excerpt):**

> "Pass threshold: AI-augmented output scores within 15% of the reference output on all three dimensions."

**Strengthened Content:** See reconstruction. Each dimension maps to a named AI failure mode; 15% threshold justified as conservative floor; recalibration trigger defined.

**Rationale:** The blind evaluation rubric is the most concrete quality enforcement mechanism in the specification -- it is the pre-launch gate that determines whether the skill ships. If the rubric appears arbitrary (three dimensions picked without derivation, a threshold stated without justification), the entire quality gate loses credibility. Making the derivation explicit transforms the rubric from a stated requirement to a justified methodology. This finding has been present since Iter4 without incorporation.

**Best Case Conditions:** Strongest when the reviewer is a practitioner who has used AI tools to produce structured analysis outputs and encountered omission bias, specificity degradation, or efficiency regression as failure modes.

---

### SM-005-I5: BLOCK State Orchestrator Message

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Design Decisions > 5. Wave Deployment > Wave Enforcement 3-State Behavior |
| **Affected Dimension** | Completeness / Actionability |

**Original Content (line 640):**

> "BLOCK: WAVE-{N}-SIGNOFF.md does not exist. Orchestrator refuses to route to Wave N+1 sub-skills and directs user to complete the current wave's signoff process."

**Strengthened Content:** See reconstruction. Concrete message template showing specific content, resolution path, and preservation of Wave 1-N direct invocation (P-020).

**Rationale:** The mechanism is correct; the user experience is absent. A BLOCK state producing an opaque refusal will be experienced as the skill being broken. A BLOCK state with a clear resolution path, template location, and bypass option will be experienced as a helpful guardrail. The message template is specifiable now -- it does not require implementation knowledge -- and should be part of the AC rather than deferred.

---

### SM-006-I5: McConkey Close for Estimated Scope

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Estimated Scope |
| **Affected Dimension** | Internal Consistency |

**Original Content (last sentence of Estimated Scope, line 1168):**

> "If Wave 1 completion (parent + 2 sub-skills, ~8-13 days) exceeds 15 days, the per-sub-skill estimates for subsequent waves should be revised upward."

**Strengthened Content:** Add: "Wave 1 is the first drop-in. Eight to thirteen days -- that is the commitment. Every subsequent wave is a follow-on line off the same peak. You ski them when the first one goes clean."

**Rationale:** Every major persuasion section (Vision, Problem, Capability Map, Limitations) closes with a McConkey mountain metaphor callback. Estimated Scope is the only exception. The current closing reads like a different document. Adding the McConkey callback ties the scope section to the commitment framing and reinforces the bounded-wave model.

---

### SM-007-I5: Service Blueprinting V2 P1 Dual-Purpose Justification

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | V2 Roadmap > V2 Candidates |
| **Affected Dimension** | Traceability |

**Original Content (line 905):**

> "Covers end-to-end service process niche; also the auto-substitute if AI-First Design Enabler expires"

**Strengthened Content:** See reconstruction. Explicit dual-purpose framing explaining why 7.40-score framework ranks P1; pre-approved substitution path noted.

**Rationale:** A reader scanning the V2 table sees Service Blueprinting ranked P1 with a 7.40 score. Other P1 candidates (user-research, dark-patterns-audit) have clearer P1 justification. Without the dual-purpose explanation, the P1 rank looks arbitrary or mistaken. The substitution path commitment -- already declared in Known Limitations -- is what elevates Service Blueprinting to pre-approved P1 status. Making this explicit resolves the apparent inconsistency.

---

### SM-008-I5: Compound Workflow Value of Jerry Ecosystem Integration

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Relationship to Existing Jerry Skills |
| **Affected Dimension** | Actionability / Completeness |

**Original Content (lines 1006-1014):**

> Integration table mapping directional relationships between Jerry skills. No demonstration of compound sequential value.

**Strengthened Content:** See reconstruction. 6-step discovery-to-measurement loop; incremental adoption framing.

**Rationale:** The integration table shows which skills connect to which. It does not show why those connections multiply value rather than merely adding it. The compound workflow story -- JTBD informs Sprint challenge, Sprint findings inform NASA-SE requirements, HEART closes the loop -- demonstrates that the integration is structural, not cosmetic. Teams already using `/problem-solving` and `/nasa-se` do not face a 30-50 day standalone investment decision; they face an "incremental addition to my existing workflow" decision. This framing is more persuasive to the most likely audience (existing Jerry framework users).

---

### SM-009-I5: Heuristic Evaluation Haiku Severity Distribution Risk

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Sub-Skill Model Selection |
| **Affected Dimension** | Methodological Rigor |

**Original Content (line 1198):**

> "haiku | Heuristic Evaluation | Checklist-based systematic evaluation against 10 discrete heuristics; procedural, not reasoning-intensive"

**Strengthened Content:** See reconstruction. Risk note on severity-3/4 violations requiring contextual inference; validation hook tied to quality benchmark AC.

**Rationale:** The `haiku` assignment is a cost-optimization hypothesis. For severity-0 through severity-2 violations, it is appropriate. For severity-3 and severity-4 violations -- which require cross-platform knowledge and user population judgment -- it may not produce reliable findings. Since `/ux-heuristic-eval` is Wave 1 (the first sub-skill teams use), a quality regression at high-severity violations would undermine the entire wave progression model. The risk note and validation hook convert the assignment from a fixed choice to a testable hypothesis, which is the more honest framing.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Positive | SM-001-I5, SM-002-I5, SM-005-I5, SM-008-I5 fill argument-completeness gaps in audience framing, time-to-value, enforcement UX, and ecosystem integration |
| Internal Consistency | 0.20 | Positive | SM-001-I5 resolves the table/paragraph contradiction; SM-006-I5 restores McConkey voice consistency to the only section missing it |
| Methodological Rigor | 0.20 | Positive | SM-004-I5 derives the blind rubric threshold from named failure modes; SM-009-I5 adds validation hook for `haiku` model assignment |
| Evidence Quality | 0.15 | Positive | SM-003-I5 transforms "process ran" into "specific corrections made and verifiable"; SM-001-I5 resolves the Part-time UX framing contradiction |
| Actionability | 0.15 | Positive | SM-002-I5 provides the Wave 1 anchor and setup cost; SM-005-I5 gives the BLOCK state a concrete resolution path |
| Traceability | 0.10 | Positive | SM-003-I5 ties adversarial quality claims to R-annotation evidence trail; SM-007-I5 explains the Service Blueprinting P1 rationale |

---

## Execution Statistics

- **Total Findings:** 9
- **Critical:** 2 (SM-001-I5, SM-002-I5 -- both persistent from Iter4, partially incorporated)
- **Major:** 2 (SM-003-I5, SM-004-I5 -- both persistent from Iter4, not incorporated)
- **Minor:** 5 (SM-005-I5, SM-006-I5, SM-007-I5, SM-008-I5 -- persistent from Iter4, not incorporated; SM-009-I5 -- new, surfaced by R4 model selection table)
- **New findings (Iter5-specific):** 1 (SM-009-I5)
- **Persistent unincorporated findings:** 8 (SM-001 through SM-008 carry from Iter4 with full or partial non-incorporation)
- **Protocol Steps Completed:** 6 of 6
