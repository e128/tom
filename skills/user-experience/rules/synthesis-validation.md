<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "Synthesis Hypothesis Validation", "Cross-Framework Synthesis Protocol" | PARENT: /user-experience skill -->

# Synthesis Validation Rules

> Validation rules for cross-framework synthesis hypotheses produced by the ux-orchestrator agent. Enforces confidence classification gates (HIGH/MEDIUM/LOW) per P-022. See also: `skills/user-experience/rules/ux-routing-rules.md` (routing to sub-skills that produce synthesis inputs), `skills/user-experience/rules/wave-progression.md` (wave gates that determine which sub-skills are available for synthesis), `skills/user-experience/rules/mcp-coordination.md` (MCP availability affecting synthesis quality).

## Document Sections

| Section | Purpose |
|---------|---------|
| [Confidence Classification](#confidence-classification) | HIGH/MEDIUM/LOW gate definitions and enforcement |
| [Sub-Skill Synthesis Output Map](#sub-skill-synthesis-output-map) | Per-sub-skill confidence assignments |
| [Cross-Framework Synthesis Protocol](#cross-framework-synthesis-protocol) | 4-step synthesis mechanism |
| [Convergence Thresholds](#convergence-thresholds) | When findings from multiple frameworks agree |
| [Contradiction Handling](#contradiction-handling) | When frameworks produce conflicting findings |
| [Synthesis Output Structure](#synthesis-output-structure) | Required sections and format |
| [Failure Mode Handling](#failure-mode-handling) | Low-confidence synthesis escalation |

---

## Confidence Classification

<!-- Source: SKILL.md Section "Synthesis Hypothesis Validation" — 3-tier confidence gate. -->

All synthesis hypotheses MUST include confidence classification per P-022 (no deception about confidence). The orchestrator assigns confidence at synthesis time based on evidence convergence.

### Gate Definitions

| Confidence | Definition | Gate Behavior | Advancement Rule |
|------------|-----------|--------------|-----------------|
| **HIGH** | 3+ frameworks converge on the same finding, OR 2 frameworks converge with strong quantitative evidence | User reviews output + acknowledges specific AI judgment calls via Synthesis Judgments Summary | Advances to design decisions after enumerated acknowledgment |
| **MEDIUM** | 2 frameworks converge OR 1 framework with strong evidence (quantitative data, established methodology, large sample) | Requires expert review OR validation against 2-3 real user data points | Cannot advance to design decisions without named validation source |
| **LOW** | Single framework finding with weak evidence, contradiction present, or AI inference without empirical grounding | Output permanently labeled reference-only; design recommendation section structurally omitted | Cannot be overridden by any user action |

### Gate Enforcement Mechanisms

- **HIGH gate:** Output includes a "Synthesis Judgments Summary" section listing each AI judgment call (e.g., "Interpreted slow task completion as navigation confusion rather than content scanning behavior"). Acknowledgment prompt presented before design recommendations are generated. User must confirm they have reviewed each judgment call.
- **MEDIUM gate:** Output includes a "Validation Required" section with placeholder fields for: (a) expert name and credentials, (b) user data reference (study, interview count, analytics source), or (c) literature citation. Design recommendations are withheld until at least one validation source is provided.
- **LOW gate:** Output template structurally omits the design recommendation section. Title tagged with `[REFERENCE-ONLY]`. Banner: "This output reflects AI synthesis from training data. It does not contain design recommendations."

### Classification Immutability

- HIGH may be downgraded to MEDIUM or LOW by the receiving sub-skill based on its own assessment (confidence propagation per `ux-routing-rules.md` [Cross-Sub-Skill Handoff]).
- MEDIUM may be downgraded to LOW but NEVER upgraded to HIGH without additional evidence.
- LOW is permanent. No user action, expert review, or additional data can override a LOW classification within the same engagement. A new engagement with fresh evidence can produce a different classification.

---

## Sub-Skill Synthesis Output Map

<!-- Source: SKILL.md Section "Synthesis Hypothesis Validation" — per-sub-skill confidence table. -->

Each sub-skill synthesis step has a default confidence based on methodology characteristics. The orchestrator uses these defaults as starting points; actual confidence may differ based on evidence quality in each engagement.

| Sub-Skill | Synthesis Step | Default Confidence | Rationale |
|-----------|---------------|-------------------|-----------|
| `/ux-heuristic-eval` | Severity rating calibration across heuristics | MEDIUM | Severity ratings involve subjective judgment; calibration across Nielsen's 10 heuristics requires consistent application context |
| `/ux-heuristic-eval` | Comparative evaluation synthesis (cross-product or cross-version) | HIGH | Based on systematic checklist methodology with observable UI artifacts; high when screenshots/screen recordings available |
| `/ux-jtbd` | Job statement synthesis from secondary research | MEDIUM | Secondary research lacks direct user observation |
| `/ux-lean-ux` | Assumption mapping; hypothesis generation | MEDIUM | Hypotheses are deliberately unvalidated |
| `/ux-design-sprint` | Day 4 interview thematic analysis | HIGH | Based on direct user interviews (5 users per Sprint methodology) |
| `/ux-design-sprint` | Day 2 sketch selection rationale | MEDIUM | Selection rationale involves subjective judgment |
| `/ux-inclusive-design` | Persona Spectrum customization | MEDIUM | Persona Spectrums are heuristic models, not empirical profiles |
| `/ux-kano-model` | Directional classification (5-8 respondents) | MEDIUM | Small sample provides directional signal only |
| `/ux-kano-model` | Feature priority conflict interpretation | LOW | Resolving conflicting priorities requires domain context AI lacks |
| `/ux-behavior-design` | B=MAP bottleneck diagnosis | MEDIUM | Fogg model application to specific context is interpretive |
| `/ux-behavior-design` | Design intervention recommendation | LOW | Intervention effectiveness depends on context-specific factors |
| `/ux-heart-metrics` | Goal-metric mapping interpretation | MEDIUM | Mapping is methodologically grounded but context-dependent |
| `/ux-heart-metrics` | Metric threshold recommendation | LOW | Threshold values require domain-specific benchmarking data |
| `/ux-ai-first-design` | AI interaction pattern recommendations | LOW | AI design patterns are rapidly evolving; training data may be stale |
| `/ux-atomic-design` | Component taxonomy completeness assessment | MEDIUM | Taxonomy assessment depends on Storybook coverage; partial coverage yields partial assessment |
| `/ux-atomic-design` | Design token consistency analysis | LOW | Token consistency across a full system requires inspection of all component variants; AI sampling may miss edge cases |

---

## Cross-Framework Synthesis Protocol

<!-- Source: SKILL.md Section "Cross-Framework Synthesis Protocol" — 4-step sequential mechanism. -->

When the orchestrator invokes multiple sub-skills for the same engagement, it produces a cross-framework synthesis after all sub-skill outputs are available.

### Trigger

Two or more sub-skill outputs exist for the same engagement ID.

### Mechanism (4-Step Sequential)

| Step | Name | Input | Output | Validation Check |
|------|------|-------|--------|-----------------|
| 1 | **Signal Extraction** | Each sub-skill output's findings/recommendations sections | Actionable signals with source reference | Each signal traces to a specific finding number in a specific sub-skill output |
| 2 | **Convergence Detection** | Extracted signals from all sub-skills | Grouped signals: convergent (2+ frameworks) and singleton (1 framework) | Convergent groups cite all contributing sub-skills; no signal appears in multiple groups |
| 3 | **Contradiction Identification** | Signals that recommend opposing actions | Flagged contradictions with both positions preserved | Every contradiction has exactly 2 opposing positions; no resolution is attempted |
| 4 | **Unified Output** | Convergent findings, singletons, contradictions | Synthesis report with 3 sections per confidence level | All signals from Step 1 appear in exactly one output section |

### Signal Extraction Criteria

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Cross-Framework Synthesis Protocol" — signal extraction per sub-skill type. Extraction criteria thresholds align with each sub-skill's methodology-specific severity or priority scales (e.g., severity >= 2 maps to Nielsen's 0-4 scale defined in `/ux-heuristic-eval` methodology; strength >= 3 maps to JTBD switch force scale). -->

Signals are extracted based on sub-skill type:

| Sub-Skill Type | Signal Extraction Criteria |
|---------------|--------------------------|
| Heuristic Eval | Findings rated severity >= 2 (out of 0-4 scale) |
| HEART Metrics | Metrics below target threshold |
| Lean UX | Unvalidated assumptions; invalidated hypotheses |
| Behavior Design | B=MAP bottleneck diagnoses |
| JTBD | Switch forces (push/pull) with strength >= 3 |
| Kano | Features classified as Must-be or Attractive |
| Atomic Design | Components with no Storybook coverage |
| Inclusive Design | WCAG violations at AA or higher |

---

## Convergence Thresholds

<!-- Source: SKILL.md Section "Cross-Framework Synthesis Protocol" — convergence detection. -->

| Convergence Level | Definition | Synthesis Confidence | Example |
|-------------------|-----------|---------------------|---------|
| **Strong convergence** | 3+ frameworks identify the same UX problem | HIGH | Heuristic Eval finds navigation confusion (severity 3) + HEART shows low Task Success for navigation + Behavior Design diagnoses ability bottleneck in navigation |
| **Moderate convergence** | 2 frameworks identify the same UX problem with supporting quantitative or observational evidence | HIGH | Heuristic Eval finds form error visibility issue (severity 3) + Inclusive Design finds form WCAG violation (AA level) — both provide concrete evidence beyond subjective assessment |
| **Weak convergence** | 2 frameworks identify related but not identical problems | MEDIUM | JTBD identifies "quick checkout" job + HEART shows low Happiness for checkout (related but different lens) |
| **No convergence** | Single framework finding with no corroboration | MEDIUM | Only Kano model identifies a feature as Must-be; no other framework addresses that feature |

### Convergence Matching Rules

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Cross-Framework Synthesis Protocol" — convergence detection rules. Rule 2 operationalizes P-022 (no deception about confidence): when the orchestrator is uncertain whether signals describe the same user problem, it defaults to "related but NOT convergent" to prevent confidence inflation. -->

1. **Same screen/flow:** Signals that reference the same screen, flow, or component are candidates for convergence.
2. **Same user problem:** Signals that describe the same user-facing problem (even using different vocabulary) are convergent. Operationally, "same user problem" means: (a) both signals describe the same user action or goal being impeded, AND (b) both signals affect the same user population segment (or one applies to a superset of the other). When the orchestrator is uncertain whether signals describe the same problem, it defaults to "related but NOT convergent" to avoid inflating confidence (P-022).
3. **Same metric impact:** Signals that predict impact on the same HEART metric are candidates for convergence.
4. **Partial overlap:** When signals overlap on one dimension (e.g., same screen but different problems), they are noted as related but NOT convergent.

---

## Contradiction Handling

<!-- Source: SKILL.md Section "Cross-Framework Synthesis Protocol" — contradiction identification. -->

Contradictions occur when two or more frameworks recommend opposing actions for the same UX problem.

### Contradiction Detection

| Contradiction Type | Example | Handling |
|-------------------|---------|---------|
| **Direct opposition** | Heuristic Eval recommends simplifying a form; Kano Model identifies the removed fields as Must-be features | Present both positions with evidence; assign LOW confidence; user decides (P-020) |
| **Priority conflict** | HEART Metrics prioritizes Task Success improvements; Behavior Design prioritizes Motivation interventions (different bottleneck focus) | Present both priority frameworks; assign MEDIUM confidence; user decides sequencing |
| **Methodology conflict** | Lean UX invalidated a hypothesis that JTBD analysis supports as a core job need | Present the conflict; note methodological difference; assign LOW confidence; recommend additional user research |

### Contradiction Presentation Format

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Cross-Framework Synthesis Protocol" — contradiction output format. The 6-field structure (ID, Position A, Position B, Additional Positions, Resolution, Confidence) enforces P-020 (user decides: "Resolution: User decision required") and P-022 (no AI-generated resolution presented as recommendation). N-way contradiction handling (field 4) extends the base 2-position format for 3+ framework conflicts. -->

Each contradiction in the synthesis output MUST include:

1. **Contradiction ID:** `CONTRA-{NNN}` sequential identifier
2. **Position A:** Framework name, finding reference, recommendation, evidence
3. **Position B:** Framework name, finding reference, recommendation, evidence
4. **Additional Positions (if applicable):** For n-way contradictions (3+ frameworks), list each additional framework as Position C, D, etc. with the same fields. When n > 2, the contradiction confidence is always LOW regardless of type.
5. **Resolution:** "User decision required" — no AI-generated resolution (P-020 compliance)
6. **Confidence:** Always LOW for direct opposition or n-way (3+) contradictions; MEDIUM for 2-way priority/methodology conflicts

---

## Synthesis Output Structure

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Cross-Framework Synthesis Protocol" — output structure requirements. Output filename convention: {topic-slug} per SKILL.md, e.g., ux-orchestrator-synthesis.md for standard synthesis, ux-orchestrator-crisis.md for CRISIS mode. See also: skills/user-experience/rules/ci-checks.md [Output Quality Checks] for CI gates UX-CI-011 through UX-CI-013 that validate synthesis output structure. -->

The orchestrator produces synthesis reports at `skills/user-experience/output/{engagement-id}/ux-orchestrator-synthesis.md` with the following required sections:

| Section | Content | Confidence Level |
|---------|---------|-----------------|
| **Convergent Findings** | Findings where 2+ frameworks agree | HIGH |
| **Single-Framework Findings** | Findings from one framework only | MEDIUM |
| **Contradictions** | Findings where frameworks disagree | LOW (direct) or MEDIUM (priority/methodology) |
| **Synthesis Judgments Summary** | Enumerated list of AI judgment calls | N/A (meta-section) |
| **Validation Required** | Placeholder fields for MEDIUM findings | N/A (meta-section) |

### Required Traceability

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Cross-Framework Synthesis Protocol" — output traceability requirements. These 4 required fields (source sub-skill, finding ID, engagement ID, confidence classification) enable CI gate UX-CI-012 (Traceability Check) defined in `skills/user-experience/rules/ci-checks.md` [Output Quality Checks]. -->

Every finding in the synthesis output MUST include:

- Source sub-skill name (e.g., `/ux-heuristic-eval`)
- Source finding ID (e.g., `HE-003`)
- Engagement ID
- Confidence classification with rationale

---

## Failure Mode Handling

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Cross-Framework Synthesis Protocol" — failure modes. See also: skills/user-experience/rules/mcp-coordination.md [Degraded Mode Behavior] for MCP-related failure modes that affect synthesis input quality. -->

### Low-Confidence Majority

If synthesis confidence is LOW across > 50% of findings, the orchestrator adds a banner:

> "Cross-framework synthesis produced mostly low-confidence results. Consider validating individual sub-skill outputs independently before acting on synthesis recommendations."

This is a P-022 compliance mechanism — the orchestrator does not overstate the value of synthesis when evidence is weak.

### Synthesis Scope Limitation (v1.0.0)

Cross-framework synthesis operates on textual output from sub-skills. It does not access MCP design artifacts directly — synthesis inputs are the sub-skill reports, not raw Figma/Miro data. Future versions may add MCP-aware synthesis if usage patterns warrant it.

---

---

*Rule file: synthesis-validation.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling rules: `skills/user-experience/rules/ux-routing-rules.md`, `skills/user-experience/rules/wave-progression.md`, `skills/user-experience/rules/mcp-coordination.md`, `skills/user-experience/rules/ci-checks.md`*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
