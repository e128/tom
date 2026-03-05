<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: synthesis-validation.md, skills/ux-design-sprint/SKILL.md, skills/ux-ai-first-design/SKILL.md, skills/user-experience/SKILL.md, skills/user-experience/rules/ci-checks.md, ux-sprint-facilitator.md, ux-ai-design-guide.md | REVISION: initial -->

# Wave 5 Cross-Framework Testing -- /user-experience Skill

> Verifies that the two Wave 5 sub-skills (`/ux-design-sprint` and `/ux-ai-first-design`) can participate in cross-framework synthesis as defined by `skills/user-experience/rules/synthesis-validation.md`. Each test traces to specific source document sections and produces concrete evidence of PASS/FAIL.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Test Scope](#test-scope) | Wave 5 sub-skills, synthesis mechanism, and verification targets |
| [Test 1: Synthesis Output Structure Validation](#test-1-synthesis-output-structure-validation) | 4-step protocol trace using both sub-skill output specifications |
| [Test 2: Confidence Classification Coverage](#test-2-confidence-classification-coverage-ci-ux-ci-011) | Sub-Skill Synthesis Output Map entry verification |
| [Test 3: Handoff Data Contract Validation](#test-3-handoff-data-contract-validation) | Field-by-field handoff-v2 and ux-ext compatibility check |
| [Test 4: Degraded Mode Synthesis](#test-4-degraded-mode-synthesis) | MCP-dependent degraded mode handling (T3 -- Figma/Miro OPT dependencies) |
| [Test 5: CI Gate Readiness](#test-5-ci-gate-readiness-ux-ci-011-ux-ci-012-ux-ci-013) | Per-gate evaluation against Wave 5 sub-skill outputs |
| [Verdict](#verdict) | Consolidated test results table |
| [Required Actions Before Wave 5 Signoff](#required-actions-before-wave-5-signoff) | Actions needed before wave gate |
| [References](#references) | Source document paths and traceability |

---

## Test Scope

- **Wave 5 sub-skills:** `/ux-design-sprint` (agent: `ux-sprint-facilitator`, UNCONDITIONAL), `/ux-ai-first-design` (agent: `ux-ai-design-guide`, CONDITIONAL: WSM >= 7.80 AND FEAT-020 DONE)
- **Synthesis mechanism:** `ux-orchestrator` 4-step sequential protocol per `synthesis-validation.md` [Cross-Framework Synthesis Protocol]
- **Verification targets:** (1) handoff data compatibility, (2) 4-step synthesis protocol readiness, (3) confidence classification coverage in the Sub-Skill Synthesis Output Map, (4) CI gate evaluability (UX-CI-011/012/013), (5) degraded mode resilience
- **Key Wave 5 characteristics:** Both sub-skills are T3 (Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch + Context7). Design Sprint has Figma REQ and Miro REQ MCP dependencies (mcp-coordination.md [MCP Dependency Matrix]); AI-First Design has Figma REQ MCP dependency. These are the most MCP-dependent sub-skills in the `/user-experience` skill. AI-First Design is CONDITIONAL -- synthesis must handle the scenario where only Design Sprint is available.

---

## Test 1: Synthesis Output Structure Validation

**Objective:** Verify both sub-skills can produce signals for all 4 synthesis protocol steps.

**Pass Criterion:** All 4 steps have at least one executable input from each Wave 5 sub-skill. Additionally, at least one scenario where only Design Sprint is available (CONDITIONAL activation of AI-First Design failed) must be covered.

### Step 1: Signal Extraction

**Extraction criteria** (synthesis-validation.md [Signal Extraction Criteria]):
- **Design Sprint:** "Interview themes identified by >= 3 of 5 users in Day 4 testing" -- majority pattern threshold per Sprint methodology (Knapp, Zeratsky & Kowitz, 2016)
- **AI-First Design:** "Patterns flagged as HIGH trust-risk or HIGH error-risk in AI interaction audit" -- trust-risk and error-risk are the two primary failure modes in AI interaction design (Yang et al., 2020)

**`/ux-design-sprint` signals:** The agent produces a Day 4 observation grid (5 users x sprint questions) with pattern analysis using quantitative theme strength thresholds: strong (>= 3 of 5 users) = HIGH confidence, moderate (2 of 5) = MEDIUM confidence, weak (1 of 5) = noted but not actionable. Additional signals: sprint question verdicts (pass/fail/partial), assumption validation results (validated/invalidated/inconclusive), and the Synthesis Judgments Summary listing every AI judgment call. On-send protocol includes `sprint_day_completed`, `prototype_fidelity`, `interview_count`, `theme_strength`, `usability_findings_count`, `sprint_questions_answered`, `validated_assumptions`, `invalidated_assumptions`, `synthesis_judgments`, `degraded_mode`, and `handoff_ready`. Synthesis-level `DS-{NNN}` IDs assigned by orchestrator.

**`/ux-ai-first-design` signals:** The agent produces a trust-risk classification (HIGH/MEDIUM/LOW) with 4-criterion assessment and algorithm trace, an error-risk classification (HIGH/MEDIUM/LOW) with 4-criterion assessment and algorithm trace, an interaction pattern specification from the 3x3 trust-risk x error-risk matrix, a feedback loop design across 4 Amershi interaction phases, and a progressive disclosure plan (5 stages). On-send protocol includes `trust_risk_level`, `error_risk_level`, `interaction_pattern`, `ai_capability_type`, `feedback_loop_design`, `human_oversight_level`, `progressive_disclosure_plan`, `synthesis_judgments_count`, `degraded_mode`, and `handoff_ready`. Synthesis-level `AI-{NNN}` IDs assigned by orchestrator.

**CONDITIONAL-only scenario (AI-First Design unavailable):** When AI-First Design CONDITIONAL activation fails (WSM < 7.80 OR FEAT-020 not DONE), only Design Sprint signals are available for synthesis. The orchestrator routes AI-related requests to `/ux-heuristic-eval` with PAIR protocol as an interim alternative (ux-ai-first-design SKILL.md [Lifecycle-Stage Routing Integration]). In this scenario, synthesis operates with Design Sprint signals only; all findings are "Single-Framework Findings" at MEDIUM confidence per synthesis-validation.md [Convergence Thresholds, No convergence].

**Step 1 Result:** PASS -- Both sub-skills produce structured, threshold-eligible signals with source traceability. CONDITIONAL-only scenario handled via standard single-framework synthesis path.

### Step 2: Convergence Detection

**Convergence Matching Rules** (synthesis-validation.md): (1) Same screen/flow, (2) Same user problem, (3) Same metric impact.

| Scenario | Design Sprint Signal | AI-First Design Signal | Rule | Level |
|---|---|---|---|---|
| User trust failure in AI feature | Day 4 strong theme: >= 3/5 users distrust AI recommendation output, fail to act on suggestions | HIGH trust-risk classification: over-trust consequence = significant, output verifiability = unverifiable | Rule 1+2 | Strong -> HIGH |
| AI error recovery gap | Day 4 moderate theme: 2/5 users confused by AI error state, cannot recover | HIGH error-risk: detection latency = delayed, recovery cost = high | Rule 2 | Moderate -> HIGH |
| Same metric impact (Task Success) | Sprint question verdict: FAIL on "Can users complete the AI-assisted task?" with strong negative theme | Interaction pattern spec identifies automation mismatch reducing task completion | Rule 3 | Moderate -> HIGH |
| Unrelated domains | Strong theme on navigation flow unrelated to AI | Trust-risk assessment for a separate AI capability | None | No conv. -> MEDIUM |
| CONDITIONAL-only: single framework | Day 4 strong theme on checkout friction (>= 3/5 users) | (unavailable -- CONDITIONAL activation failed) | N/A | No convergence possible (single framework) -> MEDIUM per synthesis-validation.md |

Rule 3 (same metric impact) is particularly operational in Wave 5: Design Sprint Day 4 produces direct behavioral observations of users interacting with AI features, while AI-First Design produces trust-risk and error-risk classifications for those same features. The sprint's observation grid data (what users actually do) and the AI-First Design's risk classification (what the framework predicts) provide independent evidence streams that converge on the same HEART metric impact.

**Step 2 Result:** PASS -- Convergence detection feasible via all three matching rules.

### Step 3: Contradiction Identification

| Type | Design Sprint Position | AI-First Design Position | Confidence |
|---|---|---|---|
| Direct opposition | Day 4 verdict PASS: >= 3/5 users successfully use AI feature without guidance (sprint question passes) | HIGH trust-risk: framework classifies the AI capability as requiring full oversight because over-trust consequence is catastrophic | LOW |
| Priority conflict | Sprint finding: users want more AI autonomy (strong theme, interview quotes supporting delegation) | Progressive disclosure plan recommends Stage 2 (Suggestion) as maximum appropriate autonomy; "never lower oversight" rule prevents advancing | MEDIUM |
| Methodology conflict | Day 4 observation: users engage positively with AI feature (strong positive theme on Happiness) | AI-First Design: error-risk HIGH because errors are irreversible, recommending human_in_loop pattern that restricts the fluid interaction users preferred | LOW |
| CONDITIONAL-only: single framework | Day 4 mixed findings on AI feature usability | (unavailable -- CONDITIONAL activation failed) | N/A | No contradictions possible (requires 2+ frameworks); all findings classified as Single-Framework at MEDIUM |

All 3 contradiction types from synthesis-validation.md are plausible. The direct opposition scenario is particularly notable for Wave 5: Design Sprint provides empirical behavioral evidence (what users actually do in testing) while AI-First Design provides framework-based risk assessment (what the trust-risk/error-risk model predicts). These methodologies can produce conflicting conclusions about appropriate autonomy levels.

**Step 3 Result:** PASS -- All contradiction types have plausible Wave 5 scenarios.

### Step 4: Unified Output

**Traceability check:**

| Field | `/ux-design-sprint` | `/ux-ai-first-design` |
|---|---|---|
| Sub-skill name | `from_agent: ux-sprint-facilitator` | `from_agent: ux-ai-design-guide` |
| Finding ID | Orchestrator-assigned `DS-{NNN}` | Orchestrator-assigned `AI-{NNN}` |
| Engagement ID | `UX-{NNNN}` in on-send | `UX-{NNNN}` in on-send |
| Confidence | HIGH (strong themes, Day 4 interviews), MEDIUM (sketch selection, moderate themes) | LOW (AI pattern recommendations), MEDIUM (directional risk classifications) |

All 5 synthesis output sections (Convergent Findings, Single-Framework Findings, Contradictions, Synthesis Judgments Summary, Validation Required) can be populated from Wave 5 signals. The CONDITIONAL-only scenario (only Design Sprint available) populates only Single-Framework Findings.

**Step 4 Result:** PASS

### Test 1 Overall Result: PASS

---

## Test 2: Confidence Classification Coverage (CI: UX-CI-011)

**Objective:** Verify both sub-skills have entries in the Sub-Skill Synthesis Output Map.

**Pass Criterion:** Both must have at least one entry with a defined confidence level.

### Entries found (synthesis-validation.md [Sub-Skill Synthesis Output Map])

| Sub-Skill | Synthesis Step | Typical Confidence | Present? |
|---|---|---|---|
| `/ux-design-sprint` | Day 4 interview thematic analysis | HIGH | YES |
| `/ux-design-sprint` | Day 2 sketch selection rationale | MEDIUM | YES |
| `/ux-ai-first-design` | AI interaction pattern recommendations | LOW | YES |

**Cross-references confirmed:** Design Sprint agent `<methodology>` Phase 4 declares matching confidence levels: strong themes (>= 3/5 users) carry HIGH confidence; moderate themes (2/5) carry MEDIUM confidence (ux-sprint-facilitator.md [Phase 4: Day 4 (Test), Pattern Analysis]). SKILL.md [Required Output Sections, Synthesis Judgments Summary] requires each judgment to include confidence classification (HIGH/MEDIUM/LOW). AI-First Design SKILL.md [Synthesis Hypothesis Validation] and agent `<guardrails>` section enforce: "All interaction pattern recommendations must carry LOW confidence tags" (ux-ai-design-guide.md [Required Report Structure, Feedback Loop Design]).

**Mixed-Confidence Resolution Rule:** Applicable to Design Sprint: HIGH thematic analysis + MEDIUM sketch selection = MEDIUM when combined. AI-First Design has only LOW-confidence entries; the minimum-confidence rule produces LOW for all AI-First Design synthesis findings. Expected behavior per synthesis-validation.md.

**Asymmetry note:** Design Sprint is the only sub-skill in the `/user-experience` skill that produces HIGH confidence synthesis signals. This is because Day 4 user interviews (5 users per Nielsen, 2000) provide direct observational evidence -- the highest-quality evidence source in the UX methodology stack. AI-First Design, by contrast, produces exclusively LOW confidence signals because the AI interaction design field evolves rapidly and training data may be stale (synthesis-validation.md [Sub-Skill Synthesis Output Map], rationale column).

### Test 2 Result: PASS

---

## Test 3: Handoff Data Contract Validation

**Objective:** Verify handoff data compatibility with synthesis protocol inputs.

**Pass Criterion:** Both sub-skills must declare all 9 handoff-v2 required fields and at least 3 ux-ext fields.

### `/ux-design-sprint` handoff (SKILL.md, agent `<output>` Handoff Data)

**handoff-v2:** All 9 fields present in explicit YAML blocks (`from_agent: ux-sprint-facilitator`, `to_agent`, `task`, `success_criteria` [2], `artifacts`, `key_findings` [3], `blockers: []`, `confidence: 0.75`, `criticality: C2`). Two downstream handoff targets are declared: `/ux-lean-ux` and `/ux-heuristic-eval`. Key_findings declares 3 template entries per handoff, meeting the CB-04 3-5 guideline minimum per `agent-development-standards.md` [Context Passing Conventions].

**ux-ext fields (5):** `sprint_day_completed`, `prototype_fidelity`, `interview_count`, `theme_strength`, `usability_findings_count` -- all synthesis-relevant. The on-send protocol adds additional context fields (`sprint_questions_answered`, `validated_assumptions`, `invalidated_assumptions`, `synthesis_judgments`, `degraded_mode`, `handoff_ready`) beyond the ux-ext minimum.

**Handoff confidence calibration:** Explicitly documented in agent definition: 0.65 for degraded prototype fidelity (no Figma, low fidelity); 0.75 default for standard sprint completion; 0.85 when strong themes dominate.

### `/ux-ai-first-design` handoff (SKILL.md, agent `<output>` Handoff Data)

**handoff-v2:** All 9 fields present in explicit YAML blocks (`from_agent: ux-ai-design-guide`, `to_agent`, `task`, `success_criteria` [3], `artifacts`, `key_findings` [3], `blockers: []`, `confidence: 0.5`, `criticality: C2`). Two downstream handoff targets declared: `/ux-inclusive-design` and `/ux-heuristic-eval`. Key_findings declares 3 template entries per handoff.

**ux-ext fields (6):** `trust_risk_level`, `error_risk_level`, `interaction_pattern`, `ai_capability_type`, `feedback_loop_design` (nested object with 4 sub-fields: initially, during_interaction, when_wrong, over_time), `human_oversight_level` -- all synthesis-relevant. The on-send protocol adds `progressive_disclosure_plan`, `synthesis_judgments_count`, `degraded_mode`, and `handoff_ready`.

**Handoff confidence calibration:** Explicitly documented in agent definition: 0.4 for no AI system behavioral data; 0.5 default for mixed evidence; 0.6 when quantitative AI system performance data supports the design.

### Field Compatibility

| Dimension | `/ux-design-sprint` | `/ux-ai-first-design` | Compatible? |
|---|---|---|---|
| Finding ID format | Orchestrator-assigned `DS-{NNN}` | Orchestrator-assigned `AI-{NNN}` | YES -- both satisfy `[A-Z]{2,}-[0-9]{3}` regex |
| Confidence levels | HIGH + MEDIUM | LOW | YES -- same classification system |
| Engagement ID | `UX-{NNNN}` | `UX-{NNNN}` | YES -- identical format |
| Confidence format | Numeric (0.75) | Numeric (0.5) | YES -- both use numeric handoff-v2 values; map to qualitative via calibration scale (agent-development-standards.md [Handoff Protocol]: 0.0-0.3=low, 0.4-0.6=moderate, 0.7-0.8=high) |
| Artifact path | `skills/ux-design-sprint/output/{eid}/` | `skills/ux-ai-first-design/output/{eid}/` | YES -- standard convention |
| Handoff-v2 completeness | 9/9 fields explicit in YAML block | 9/9 fields explicit in YAML block | YES -- full handoff-v2 compliance |

### Test 3 Result: PASS (unconditional)

Both sub-skills provide complete handoff-v2 data with explicit YAML declaration of all 9 required fields. This is the first unconditional PASS for Test 3 in the /user-experience skill — an improvement over Wave 4, where Kano's streamlined on-send protocol provided only 2 of 9 fields directly. Both require orchestrator-assigned `{PREFIX}-{NNN}` IDs per the standard pattern established in Waves 1-4.

---

## Test 4: Degraded Mode Synthesis

**Objective:** Verify synthesis operates if sub-skills run in degraded mode.

**Pass Criterion:** Synthesis protocol has documented handling for reduced-confidence inputs; handoff schemas include degraded mode indicators.

### Wave 5: Significant MCP Dependencies (T3 Architecture with REQ Dependencies)

Wave 5 is the most MCP-dependent wave. Both sub-skills are T3 (Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch + Context7). Beyond Context7, they have design-tool MCP dependencies that are currently architecture-only (future MCP adapters, not yet implemented per mcp-coordination.md [Future MCP Adapters]).

| Sub-Skill | REQ MCP | OPT/ENH MCP | Impact of REQ Unavailability |
|---|---|---|---|
| `/ux-design-sprint` | Figma, Miro | Whimsical (ENH) | Significant: prototype fidelity reduced (no Figma interactive prototype); sprint board format reduced to markdown-based (no Miro collaborative board) |
| `/ux-ai-first-design` | Figma | Storybook (ENH) | Significant: AI interaction pattern analysis limited to text-based descriptions (no visual prototyping) |

### Currently Exercisable Degraded Modes

Since Figma, Miro, and Storybook MCP adapters are not yet implemented (post-PROJ-022 scope per mcp-coordination.md [Future MCP Adapters]), **all Wave 5 engagements currently operate in degraded mode for design-tool MCPs**. Context7 is the only currently exercisable MCP dependency.

**Context7 degraded mode:** WebSearch fallback per MCP-001 (mcp-tool-standards.md [Error Handling]). Design Sprint uses Context7 for researching design patterns and competitor analysis during Day 2 lightning demos; AI-First Design uses it for looking up AI SDK documentation and interaction pattern references. Fallback to WebSearch with "Context7 no coverage" note.

### Design-Tool MCP Degraded Modes (Architecture-Level)

**Design Sprint -- Degraded Prototype Mode:** When Figma MCP is unavailable, prototype fidelity drops from "high" to "medium" or "low"; agent guides manual prototype construction (paper, presentation software, or simplified digital tools). When Miro MCP is unavailable, sprint board format changes from collaborative Miro board to markdown-based sprint artifacts; Art Museum voting conducted via ranked list or numbered voting instead of spatial dot voting. `degraded_mode: true` in on-send; confidence drops from 0.75 to 0.65. Agent `<input>` section specifies the explicit degraded mode disclosure format (ux-sprint-facilitator.md [Input, Degraded mode]).

**Design Sprint -- Both Figma AND Miro unavailable:** Sprint methodology is fully preserved; collaboration and prototype fidelity are reduced. This is the expected operational mode for PROJ-022, since neither adapter exists yet. Handoff `prototype_fidelity: low` and `degraded_mode: true` signal this state.

**AI-First Design -- Text-Only Mode:** When Figma MCP is unavailable, the agent operates on text-based interaction pattern analysis using user-provided descriptions, screenshots, and markup. Trust-risk and error-risk classification methodology remains identical; only input modality changes. The agent explicitly handles this in fallback behavior (ux-ai-design-guide.md [Fallback Behavior]: "If no screenshots or design artifacts are provided: ask structured questions about AI interface state, transparency mechanisms, and error handling flows").

### CONDITIONAL Activation Failure as Degraded Mode

When AI-First Design CONDITIONAL activation fails (WSM < 7.80 OR FEAT-020 not DONE), the sub-skill is entirely unavailable -- not degraded. The orchestrator routes to `/ux-heuristic-eval` with PAIR protocol as the interim alternative. This is structurally distinct from MCP degradation: MCP degradation produces output with reduced confidence (`degraded_mode: true`), while CONDITIONAL activation failure produces no output at all. The orchestrator sends `handoff_ready: false` for the AI-First Design slot when CONDITIONAL activation fails. Synthesis proceeds with Design Sprint only, producing single-framework findings at MEDIUM confidence.

### Synthesis Handling

Reduced-confidence inputs are handled through standard confidence propagation:
- Design Sprint `degraded_mode: true` with `prototype_fidelity: low` -> confidence drops from 0.75 to 0.65 per handoff confidence calibration; orchestrator notes reduced fidelity per P-022
- Design Sprint `degraded_mode: true` affects Day 4 findings quality (prototype fidelity influences user test validity); strong themes (>= 3/5) still produce HIGH confidence findings from direct user observation, but the observation quality is influenced by prototype fidelity
- AI-First Design `degraded_mode: true` -> confidence remains at default 0.5 (already LOW); degraded mode note in synthesis report per P-022
- If only Design Sprint produces output (CONDITIONAL activation failed for AI-First Design) -> "Single-Framework Findings" only (MEDIUM per synthesis-validation.md)
- LOW-confidence majority banner activates if > 50% findings are LOW (synthesis-validation.md [Failure Mode Handling]) -- more likely in Wave 5 than previous waves because AI-First Design contributes exclusively LOW confidence signals

### Test 4 Result: PASS

MCP degraded modes are well-documented for both sub-skills. Design Sprint explicitly declares degraded mode disclosure format and confidence reduction. AI-First Design operates with text-only mode as standard fallback. CONDITIONAL activation failure handled via standard wave-gating mechanism (not MCP degradation). All degraded states signal through on-send fields for synthesis confidence propagation. The LOW-confidence majority banner is more likely to activate in Wave 5 than previous waves, which is appropriate behavior per P-022.

---

## Test 5: CI Gate Readiness (UX-CI-011, UX-CI-012, UX-CI-013)

**Objective:** Verify CI gates can evaluate Wave 5 synthesis outputs.

**Pass Criterion:** All 3 gates evaluable against Wave 5 synthesis output format.

### UX-CI-011: Confidence Classification Presence

Wave 5 findings receive deterministic confidence from the synthesis protocol: HIGH (convergent with Design Sprint strong themes), MEDIUM (singleton or moderate themes or weak convergence), LOW (AI-First Design recommendations, direct opposition contradictions, methodology conflicts). The gate's `grep -cE '^\|.*[A-Z]{2,}-[0-9]{3}'` regex and `(HIGH|MEDIUM|LOW)` check operate on all Wave 5 finding rows.

Wave 5 presents the widest confidence range of any wave: HIGH from Design Sprint Day 4 direct user observation, through MEDIUM from sketch selection and risk classifications, to LOW from all AI-First Design pattern recommendations. The confidence classification presence check must handle all three levels within the same synthesis output.

**Result:** PASS

### UX-CI-012: Traceability

Sub-skill references `/ux-design-sprint` and `/ux-ai-first-design` match the `/ux-[a-z-]+` pattern (Pass 1). Synthesis-level IDs (`CONV-001`, `SING-001`, `CONTRA-001`) plus source IDs (`DS-001`, `AI-003`) provide >= 2 distinct `[A-Z]{2,}-[0-9]{3}` patterns per row (Pass 2). Both `DS` and `AI` are 2-letter prefixes satisfying the regex.

**CONDITIONAL-only scenario:** When only Design Sprint is available, all finding rows reference `/ux-design-sprint` with `DS-{NNN}` source IDs. Pass 1 (sub-skill reference) and Pass 2 (>= 2 distinct IDs) still succeed because the synthesis-level ID (e.g., `SING-001`) is distinct from the source ID (e.g., `DS-001`).

**Result:** PASS (conditional) -- requires orchestrator `DS-{NNN}` and `AI-{NNN}` ID assignment. Structurally identical to the Wave 2 `HM-{NNN}`, Wave 3 `AD-{NNN}`/`ID-{NNN}`, and Wave 4 `BD-{NNN}`/`KA-{NNN}` conditions.

### UX-CI-013: LOW Confidence Template Compliance

LOW-confidence content in Wave 5 synthesis arises from: (1) all AI-First Design interaction pattern recommendations (every recommendation carries LOW confidence per agent guardrails), (2) direct opposition contradictions between Design Sprint empirical findings and AI-First Design risk classifications, (3) methodology contradictions between behavioral observation and framework-based prediction.

**Two-layer enforcement:** LOW confidence tagging operates at two complementary layers:
- **Agent-level (first-pass signal):** The ux-ai-design-guide output template includes `[REFERENCE-ONLY]` headers on the Feedback Loop Design section and Progressive Disclosure Plan section (ux-ai-design-guide.md [Required Report Structure, Feedback Loop Design] and [Progressive Disclosure Plan]). These are agent-authored tags signaling that AI design recommendations carry LOW confidence and should not be treated as implementation directives. Similarly, the ux-sprint-facilitator identifies AI facilitation limitations (ux-sprint-facilitator.md [AI-Facilitated Sprint Limitations]) -- though sprint Day 4 findings carry HIGH confidence, intervention recommendations carry MEDIUM/LOW.
- **Synthesis-level (enforcement mechanism):** The orchestrator independently applies the LOW confidence gate per synthesis-validation.md [Gate Enforcement Mechanisms]: "Output template structurally omits the design recommendation section. Title tagged with `[REFERENCE-ONLY]`." This is the enforcement layer that UX-CI-013 validates.

The gate's `awk`-based check (ci-checks.md [UX-CI-013]) scans `[REFERENCE-ONLY]` sections in synthesis output files for forbidden headings ("Design Recommendations", "Recommended Actions"). The agent-level tag is a first-pass signal; the synthesis-level LOW gate is the enforcement mechanism. Both are complementary but operate at different layers -- UX-CI-013 validates the synthesis layer.

**Wave 5 significance:** AI-First Design is the sub-skill most affected by UX-CI-013 because all its synthesis-contributed findings carry LOW confidence. Every AI-First Design recommendation in the synthesis output must appear under `[REFERENCE-ONLY]` headers with design recommendations structurally omitted.

**Result:** PASS

---

## Verdict

| Test | Scope | Result | Key Evidence |
|------|-------|--------|-------------|
| **Test 1** | 4-step protocol trace | **PASS** | All steps execute. Design Sprint HIGH signals (Day 4 direct observation) converge with AI-First Design risk classifications. All contradiction types plausible. CONDITIONAL-only scenario covered. |
| **Test 2** | CI: UX-CI-011 prereq | **PASS** | Design Sprint: 2 entries (HIGH, MEDIUM). AI-First Design: 1 entry (LOW). Cross-references consistent. Mixed-confidence rule applies. Widest confidence range of any wave. |
| **Test 3** | handoff-v2 + ux-ext | **PASS (unconditional)** | Design Sprint: 9/9 handoff-v2 + 5 ux-ext. AI-First Design: 9/9 handoff-v2 + 6 ux-ext. Full handoff-v2 compliance; first unconditional Test 3 PASS in /user-experience skill (improvement over Wave 4 Kano streamlined pattern). |
| **Test 4** | Degraded mode | **PASS** | Figma/Miro REQ dependencies well-documented with degraded mode disclosure. Currently all operate in design-tool degraded mode (adapters not yet built). CONDITIONAL failure handled via wave-gating. |
| **Test 5a** | UX-CI-011 | **PASS** | Deterministic confidence for all finding categories. Widest HIGH/MEDIUM/LOW range. |
| **Test 5b** | UX-CI-012 | **PASS** (cond.) | `DS-{NNN}` and `AI-{NNN}` satisfy regex. Requires orchestrator assignment. CONDITIONAL-only scenario still passes. |
| **Test 5c** | UX-CI-013 | **PASS** | Two-layer enforcement: agent-level `[REFERENCE-ONLY]` tags (AI-First Design) + synthesis-level LOW gate (ci-checks.md [UX-CI-013]). AI-First Design most affected sub-skill. |

**Overall Wave 5 Cross-Framework Synthesis Readiness: PASS (1 condition)**

One conditional item remains: Test 5b -- orchestrator assigns `DS-{NNN}` (Design Sprint) and `AI-{NNN}` (AI-First Design) identifiers per synthesis-validation.md [Required Traceability] (Required Action #1). This is consistent with the same conditional pattern in Waves 1-4 and does not block signoff. Notably, Wave 5 has no handoff formalization condition (both sub-skills declare full 9/9 handoff-v2 fields) -- an improvement over Wave 4.

---

## Required Actions Before Wave 5 Signoff

Actions ordered by priority (blocking conditions first, then enhancements, then completed):

1. **[P1] Finding ID assignment:** The ux-orchestrator must assign `DS-{NNN}` (Design Sprint) and `AI-{NNN}` (AI-First Design) identifiers in synthesis rows. Traceability chain: synthesis-level ID + source description (e.g., `DS-001: Strong theme -- users unable to complete AI-assisted checkout (3/5 users, Day 4)`, `AI-003: HIGH trust-risk -- recommendation engine over-trust consequence catastrophic`). Encode in ux-orchestrator `<methodology>` Phase 5 as a synthesis formatting step. Verify via UX-CI-012 regex. Resolves Test 5b conditional PASS. **Status:** OPEN -- to be implemented when ux-orchestrator agent definition is created/updated. **Owner:** PROJ-022 orchestration session (ux-orchestrator agent build).
2. **[P2] Wave signoff population:** Populate `skills/user-experience/work/WAVE-5-SIGNOFF.md` cross-framework synthesis test rows from the Verdict table. **Status:** OPEN -- requires wave signoff creation.

### Wave 5 Signoff Readiness

| Signoff Row | Source Test | Result |
|-------------|-----------|--------|
| Synthesis output structure validated | Test 1 | PASS |
| Confidence classifications present | Test 2 | PASS |
| Handoff contracts compatible | Test 3 | PASS |
| Degraded mode synthesis verified | Test 4 | PASS |
| CI gates evaluable | Test 5 | PASS (conditional) |

---

## References

| Source | Content | Path |
|--------|---------|------|
| Synthesis validation rules | 4-step protocol, confidence classification, convergence thresholds, contradiction handling | `skills/user-experience/rules/synthesis-validation.md` |
| Design Sprint sub-skill spec | AJ&Smart Design Sprint 2.0 methodology, output specification, cross-framework integration | `skills/ux-design-sprint/SKILL.md` |
| AI-First Design sub-skill spec | Trust-risk x error-risk framework, interaction patterns, CONDITIONAL activation, cross-framework integration | `skills/ux-ai-first-design/SKILL.md` |
| Parent skill spec | Available Agents, Wave Architecture, Synthesis Protocol | `skills/user-experience/SKILL.md` |
| CI checks | UX-CI-011/012/013 gate definitions and implementation patterns | `skills/user-experience/rules/ci-checks.md` |
| MCP coordination | MCP Dependency Matrix, degraded mode behavior, Figma risk profile, future MCP adapters | `skills/user-experience/rules/mcp-coordination.md` |
| Design Sprint agent | Identity, methodology, on-send protocol, handoff data format, degraded mode disclosure | `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` |
| AI-First Design agent | Identity, methodology, on-send protocol, trust-risk/error-risk classification, CONDITIONAL verification | `skills/ux-ai-first-design/agents/ux-ai-design-guide.md` |
| Agent development standards | Handoff Protocol v2 (HD-M-001 through HD-M-005) | `.context/rules/agent-development-standards.md` |
| Quality enforcement | Quality gate thresholds, criticality levels | `.context/rules/quality-enforcement.md` |
| Wave 4 cross-framework tests | Preceding wave test pattern, conditional PASS precedent | `skills/user-experience/work/wave-4-cross-framework-tests.md` |

**External methodology citations:** Knapp, Zeratsky & Kowitz (2016) for Design Sprint, Courtney (2019) for Sprint 2.0, Yang et al. (2020) for trust-risk/error-risk framework, Amershi et al. (2019) for AI interaction guidelines, Nielsen (2000) for 5-user testing threshold -- full entries in `synthesis-validation.md` [External Methodology Citations].

---

*Document Version: 1.0.0*
*Parent Skill: /user-experience*
*Wave: 5 (Process Intensives)*
*Project: PROJ-022 User Experience Skill*
*Created: 2026-03-04*

<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: synthesis-validation.md, skills/ux-design-sprint/SKILL.md, skills/ux-ai-first-design/SKILL.md, skills/user-experience/SKILL.md, skills/user-experience/rules/ci-checks.md, ux-sprint-facilitator.md, ux-ai-design-guide.md | REVISION: initial -->
