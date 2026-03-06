<!-- VERSION: 1.1.1 | DATE: 2026-03-04 | SOURCE: synthesis-validation.md, skills/ux-atomic-design/SKILL.md, skills/ux-inclusive-design/SKILL.md, skills/user-experience/SKILL.md, skills/user-experience/rules/ci-checks.md, skills/user-experience/templates/wave-signoff-template.md, skills/ux-atomic-design/agents/ux-atomic-architect.md, skills/ux-inclusive-design/agents/ux-inclusive-evaluator.md, .context/rules/agent-development-standards.md | REVISION: iter3 -- fix wcag_audit_results → wcag_findings in References table (field name mismatch with agent definition on_send) -->

# Wave 3 Cross-Framework Testing -- /user-experience Skill

> Verifies that the two Wave 3 sub-skills (`/ux-atomic-design` and `/ux-inclusive-design`) can participate in cross-framework synthesis as defined by `skills/user-experience/rules/synthesis-validation.md`. Each test traces to specific source document sections and produces concrete evidence of PASS/FAIL.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Test Scope](#test-scope) | Wave 3 sub-skills, synthesis mechanism, and verification targets |
| [Test 1: Synthesis Output Structure Validation](#test-1-synthesis-output-structure-validation) | 4-step protocol trace using both sub-skill output specifications |
| [Test 2: Confidence Classification Coverage](#test-2-confidence-classification-coverage-ci-ux-ci-011) | Sub-Skill Synthesis Output Map entry verification |
| [Test 3: Handoff Data Contract Validation](#test-3-handoff-data-contract-validation) | Field-by-field handoff-v2 and ux-ext compatibility check |
| [Test 4: Degraded Mode Synthesis](#test-4-degraded-mode-synthesis) | Reduced-confidence input handling under MCP unavailability |
| [Test 5: CI Gate Readiness](#test-5-ci-gate-readiness-ux-ci-011-ux-ci-012-ux-ci-013) | Per-gate evaluation against Wave 3 sub-skill outputs |
| [Verdict](#verdict) | Consolidated test results table |
| [Required Actions Before Wave 3 Signoff](#required-actions-before-wave-3-signoff) | Actions needed before wave gate |
| [Wave 3 Signoff Readiness](#wave-3-signoff-readiness) | Test-to-signoff mapping |
| [References](#references) | Source document paths and traceability |

---

## Test Scope

- **Wave 3 sub-skills:** `/ux-atomic-design` (agent: `ux-atomic-architect`), `/ux-inclusive-design` (agent: `ux-inclusive-evaluator`)
- **Synthesis mechanism:** `ux-orchestrator` 4-step sequential protocol per `skills/user-experience/rules/synthesis-validation.md` [Cross-Framework Synthesis Protocol]
- **What we are verifying:**
  1. Handoff data compatibility between sub-skill outputs and the synthesis protocol inputs
  2. Synthesis protocol readiness -- can all 4 steps execute against Wave 3 sub-skill output formats?
  3. Confidence classification coverage -- are both Wave 3 sub-skills represented in the Sub-Skill Synthesis Output Map?
  4. CI gate evaluability -- can UX-CI-011, UX-CI-012, and UX-CI-013 operate on Wave 3 synthesis outputs?
  5. Degraded mode resilience -- does synthesis handle reduced-confidence inputs from MCP-degraded sub-skills?

---

## Test 1: Synthesis Output Structure Validation

**Objective:** Verify that if both sub-skills produce output in their defined formats, the `ux-orchestrator`'s 4-step synthesis protocol (Signal Extraction, Convergence Detection, Contradiction Identification, Unified Output) can produce a valid output per `synthesis-validation.md` [Synthesis Output Structure].

### Pass Criterion

All 4 synthesis protocol steps (Signal Extraction, Convergence Detection, Contradiction Identification, Unified Output) must have at least one executable input from each Wave 3 sub-skill.

**Method:** Trace through each step using the output specifications from both SKILL.md files, their agent definitions, and their methodology sections.

### Step 1: Signal Extraction

**Protocol requirement** (synthesis-validation.md [Cross-Framework Synthesis Protocol]): Each sub-skill output's findings/recommendations sections produce actionable signals with source reference. Each signal must trace to a specific finding number in a specific sub-skill output.

**Signal Extraction Criteria** (synthesis-validation.md [Signal Extraction Criteria]):
- **Atomic Design:** "Components with no Storybook coverage" -- source: Atomic Design methodology (Frost, 2016)
- **Inclusive Design:** "WCAG violations at AA or higher" -- source: WCAG 2.2 AA conformance level (W3C, 2023)

**Evidence from `/ux-atomic-design` output specification:**

The Atomic Design SKILL.md [Output Specification] defines a required output structure with the following synthesis-eligible sections:

1. **Component Inventory** (L1 section): Full 5-level component inventory with component name, classification level (atom/molecule/organism/template/page), variant count, reuse frequency, and Storybook story status (documented/undocumented/partial). Components marked "undocumented" (no Storybook story) satisfy the signal extraction criterion: "Components with no Storybook coverage."

2. **Storybook Coverage Report** (L1 section): Per-level component coverage percentages, state coverage, variant coverage, and a prioritized list of undocumented components with coverage gap severity. Components failing coverage targets produce extraction-eligible signals. Coverage targets are defined in ux-atomic-design SKILL.md [Storybook Coverage Model] (line 349), Section "Methodology", Subsection "Storybook Coverage Model": **"Component coverage: >= 80% for atoms, >= 60% for molecules/organisms"** (verified at SKILL.md line 355). The same section defines state coverage targets (>= 70% atoms, >= 50% molecules) and variant coverage targets (>= 60% atoms, >= 40% molecules).

3. **Design Token Audit** (L1 section): Per-category token inventory with drift ratio (`drift_ratio = hardcoded_values / total_style_values`). Components with drift ratio above the 0.20 heuristic threshold (SKILL.md [Design Token Architecture]) produce extraction-eligible signals tagged as HIGH priority findings.

4. **Consolidation Candidates** (L1 section): Duplicate or near-duplicate component pairs with similarity assessment. Each consolidation candidate is an actionable signal.

The agent's on_send protocol (SKILL.md [Invoking the Agent]) includes `component_inventory`, `design_token_audit`, `storybook_coverage`, and `consolidation_candidates` structured fields, providing the orchestrator with machine-readable data for signal extraction. The **Synthesis Judgments Summary** (L1 section) lists every AI judgment call with confidence classification (HIGH/MEDIUM/LOW) and rationale, enabling the orchestrator to assess signal reliability.

**Evidence from `/ux-inclusive-design` output specification:**

The Inclusive Design SKILL.md [Output Specification] defines a required output structure with the following synthesis-eligible sections:

1. **WCAG 2.2 Compliance Audit** (L1 section): Full success criteria evaluation organized by principle (POUR), with per-criterion status (PASS/FAIL/N/A), evidence, affected elements, severity (0-4 per Nielsen scale), and remediation with WCAG technique references. Findings with status FAIL and severity >= 2 (minor barrier or above) satisfy the signal extraction criterion: "WCAG violations at AA or higher." The handoff threshold (SKILL.md [Cross-Framework Integration]) explicitly states: "Only findings with severity >= 2 are included in cross-framework synthesis handoffs."

2. **Color Contrast Analysis** (L1 section): Per-element contrast ratio measurements with pass/fail per target level. Failed contrast checks produce WCAG-traceable signals (success criteria 1.4.3, 1.4.6, 1.4.11).

3. **Keyboard Navigation Audit** (L1 section): Tab order issues, keyboard traps, missing focus indicators, shortcut conflicts. Each finding maps to specific WCAG criteria (2.1.1, 2.1.2, 2.4.7, 2.4.11, 2.4.12).

4. **Screen Reader Compatibility** (L1 section): Missing ARIA roles, inadequate alt text, live region problems. Each finding maps to WCAG criteria (1.1.1, 1.3.1, 4.1.2, 4.1.3).

5. **Persona Spectrum Analysis** (L1 section): Per-interaction-pattern profiles mapping permanent, temporary, and situational disability scenarios with exclusion points and design opportunities.

The agent's on_send protocol (SKILL.md [Invoking the Agent]) includes `conformance_result`, `wcag_findings`, `persona_spectrum_analysis`, `contrast_ratios`, `keyboard_audit`, `screen_reader_findings`, `remediation_priorities`, and `synthesis_judgments` structured fields. Finding IDs follow the WCAG success criterion format (e.g., SC 1.4.3) with severity ratings enabling extraction threshold application.

**Step 1 Assessment:** Both sub-skills produce outputs with:
- Unique finding identifiers (component names and Storybook coverage status for Atomic Design; WCAG success criterion IDs with severity ratings for Inclusive Design)
- Threshold-eligible signals (undocumented components and drift ratio violations for Atomic Design; WCAG violations at severity >= 2 for Inclusive Design)
- Source references traceable to the sub-skill output file

**Step 1 Result:** PASS -- Both sub-skill output formats provide sufficient signal structure for extraction.

### Step 2: Convergence Detection

**Protocol requirement** (synthesis-validation.md [Cross-Framework Synthesis Protocol]): Extracted signals from all sub-skills are grouped per convergence thresholds. Convergent groups cite all contributing sub-skills. No signal appears in multiple groups.

**Convergence Matching Rules** (synthesis-validation.md [Convergence Thresholds]):
1. Same screen/flow: Signals referencing the same screen, flow, or component
2. Same user problem: Both signals describe the same user-facing problem
3. Same metric impact: Signals predicting impact on the same HEART metric

**Wave 3 convergence scenarios between Atomic Design and Inclusive Design:**

| Convergence Scenario | Atomic Design Signal | Inclusive Design Signal | Matching Rule | Convergence Level |
|---|---|---|---|---|
| **Component-accessibility alignment** | Component inventory identifies Button atom with 4 variants, Storybook status "partial" (missing disabled state story) | WCAG audit finds Button component fails SC 4.1.2 (Name, Role, Value) -- missing accessible name in disabled state | Rule 1 (same component: Button atom) AND Rule 2 (same user problem: incomplete state handling causes both documentation gap and accessibility failure) | Strong convergence (2 frameworks, same component + same problem) -> HIGH per synthesis-validation.md [Convergence Thresholds] |
| **Token-contrast convergence** | Design token audit identifies color token drift (drift ratio 0.25, above 0.20 threshold): 3 form components use hardcoded `#666666` instead of `color-text-secondary` token | Color contrast analysis finds those same 3 form components fail SC 1.4.3 (Minimum Contrast) -- computed ratio 3.8:1 against white background, below 4.5:1 AA threshold | Rule 1 (same components: form input labels) AND Rule 2 (same user problem: inconsistent color usage causes both token drift and insufficient contrast) | Strong convergence (2 frameworks, supporting quantitative evidence from both drift ratio and contrast ratio) -> HIGH |
| **Coverage-compliance alignment** | Storybook coverage report identifies Navigation organism as "undocumented" (no Storybook stories) with high reuse frequency (appears on 8 of 10 pages) | Keyboard navigation audit finds Navigation organism fails SC 2.4.1 (Skip Navigation) and SC 2.4.7 (Focus Visible) -- no skip-to-content mechanism and inconsistent focus indicators | Rule 1 (same component: Navigation organism) AND Rule 2 (same user problem: navigation component is both undocumented and inaccessible) | Moderate convergence (2 frameworks, different evidence types -- documentation gap vs. accessibility failure) -> HIGH |
| **Unrelated signals** | Consolidation candidate: two similar Card molecules ("ProductCard" and "FeatureCard") recommended for merge | Persona Spectrum analysis identifies cognitive load barrier in checkout form for users with learning disabilities | No matching rule applies -- component consolidation is a structural concern; cognitive load in checkout is a behavioral concern on a different screen/flow | No convergence -> MEDIUM per synthesis-validation.md [Convergence Thresholds] |

**Step 2 Assessment:** Convergence detection can operate on Wave 3 sub-skill signals because:
- Atomic Design produces a component-level inventory that maps directly to the evaluation scope of Inclusive Design's WCAG audit -- both sub-skills operate on the same component taxonomy (Rule 1)
- The "Build to Evaluate" canonical sequence is defined in ux-atomic-design SKILL.md [Cross-Framework Integration], Section "Canonical Multi-Skill Workflow Sequences" (line 595): **"`/ux-atomic-design` then `/ux-inclusive-design`"** with this sub-skill's role stated as **"Produces the component inventory; inclusive design evaluates each component for accessibility compliance."** This explicitly connects Atomic Design output to Inclusive Design input, creating a natural convergence pathway where the component inventory produced by Phase 2-3 of `/ux-atomic-design` becomes the evaluation scope for `/ux-inclusive-design`'s WCAG 2.2 audit
- Design token drift findings (hardcoded color values) directly correlate with color contrast WCAG failures, enabling quantitative convergence (Rule 1 + Rule 2)
- Note: Rule 3 (same metric impact) is less directly applicable in Wave 3 because neither sub-skill operates on HEART metrics natively. However, both sub-skills' findings may reference HEART metric implications when converged with Wave 2 outputs in cross-wave synthesis

**Step 2 Result:** PASS -- Convergence detection is feasible between Atomic Design and Inclusive Design signals using Rule 1 (same component) and Rule 2 (same user problem). The "Build to Evaluate" canonical sequence creates a particularly strong convergence pathway because both sub-skills operate on the same component scope.

### Step 3: Contradiction Identification

**Protocol requirement** (synthesis-validation.md [Contradiction Handling]): Signals recommending opposing actions are flagged as contradictions. Every contradiction has exactly 2 opposing positions. No resolution is attempted.

**Wave 3 contradiction scenarios between Atomic Design and Inclusive Design:**

| Contradiction Type | Atomic Design Position | Inclusive Design Position | Classification |
|---|---|---|---|
| **Direct opposition** | Consolidation analysis recommends merging two similar Card molecules ("ProductCard" and "FeatureCard") into a single generic "Card" molecule to reduce design debt and improve reuse frequency | WCAG audit finds the two cards serve different user contexts: ProductCard has product-specific ARIA labels and alt text patterns, while FeatureCard has different semantic structure -- merging them would create a single component that fails SC 1.3.1 (Info and Relationships) because the generic component loses context-specific semantics | Direct opposition per synthesis-validation.md [Contradiction Handling]: reducing design debt conflicts with maintaining accessible semantics -> LOW confidence |
| **Priority conflict** | Storybook coverage report prioritizes documenting undocumented Atom components first (highest reuse frequency, atoms-first hierarchy priority per Storybook Coverage Model) | Remediation priorities rank Organism-level navigation accessibility fixes first (severity 4: critical barrier blocking keyboard-only users) -- organisms, not atoms, need immediate attention | Priority conflict per synthesis-validation.md [Contradiction Handling]: different prioritization frameworks (documentation-first vs. accessibility-first) -> MEDIUM confidence |
| **Methodology conflict** | Design token audit identifies a custom spacing token (`spacing-compact: 4px`) as non-standard and recommends replacing it with the base scale token (`spacing-xs: 8px`) to reduce drift ratio | Cognitive load assessment finds the 4px compact spacing is essential for information-dense tables evaluated under SC 3.1.5 and SC 1.4.12 (Text Spacing) -- increasing to 8px causes content overflow on mobile, creating a new WCAG violation | Methodology conflict per synthesis-validation.md [Contradiction Handling]: token standardization vs. accessibility constraint -> LOW confidence |

**Contradiction Presentation Format check** (synthesis-validation.md [Contradiction Handling]): The format requires 6 fields: Contradiction ID (`CONTRA-{NNN}`), Position A (framework + finding + recommendation + evidence), Position B (same), Additional Positions (N/A for Wave 3 -- only 2 frameworks in a Wave-3-only synthesis), Resolution ("User decision required"), Confidence (LOW for direct opposition, MEDIUM for priority conflicts).

**Step 3 Assessment:** Contradiction identification can operate on Wave 3 sub-skill signals. The Atomic Design consolidation and standardization recommendations can directly conflict with Inclusive Design accessibility constraints. All 3 contradiction types defined in synthesis-validation.md are plausible between Atomic Design and Inclusive Design. The 2-framework constraint for Wave-3-only synthesis means contradictions are binary. Notably, the "Build to Evaluate" sequence creates a structural tension: Atomic Design optimizes for component consistency and reuse, while Inclusive Design optimizes for accessibility compliance -- these goals can genuinely conflict when consolidation removes context-specific accessible patterns.

**Step 3 Result:** PASS -- Contradiction identification is feasible. All contradiction types have plausible Wave 3 scenarios.

### Step 4: Unified Output

**Protocol requirement** (synthesis-validation.md [Synthesis Output Structure]): A synthesis report with 5 required sections: Convergent Findings (HIGH), Single-Framework Findings (MEDIUM), Contradictions (LOW/MEDIUM), Synthesis Judgments Summary, Validation Required. Every finding includes: source sub-skill name, source finding ID, engagement ID, confidence classification with rationale.

**Traceability check** (synthesis-validation.md [Required Traceability]):

| Traceability Field | `/ux-atomic-design` Source | `/ux-inclusive-design` Source |
|---|---|---|
| Source sub-skill name | `/ux-atomic-design` -- present in on_send structured fields (SKILL.md [Invoking the Agent]) | `/ux-inclusive-design` -- present in on_send structured fields (SKILL.md [Invoking the Agent]) |
| Source finding ID | Component names serve as primary identifiers within the inventory; Storybook coverage gaps and drift instances reference component names. The agent does not natively use `{PREFIX}-{NNN}` format -- synthesis-level re-prefixing required (e.g., `AD-001` for Atomic Design finding 1). | WCAG success criterion IDs (e.g., SC 1.4.3) serve as finding identifiers per the evaluation format (SKILL.md [Methodology]). However, the `SC X.Y.Z` format does not match the `{PREFIX}-{NNN}` CI regex -- synthesis-level re-prefixing required (e.g., `ID-001` for Inclusive Design finding 1). |
| Engagement ID | `engagement_id: UX-{NNNN}` format in on_receive fields (SKILL.md [Invoking the Agent]) | `engagement_id: UX-{NNNN}` format in on_receive fields (SKILL.md [Invoking the Agent]) |
| Confidence classification | Provided per synthesis step: MEDIUM for taxonomy completeness, LOW for design token consistency (SKILL.md [Synthesis Hypothesis Confidence]) | Provided per synthesis step: MEDIUM for Persona Spectrum, severity assignment, remediation priority, and cognitive load assessment (SKILL.md [Synthesis Hypothesis Confidence]). WCAG pass/fail is deterministic and excluded from synthesis confidence gate. |

**Output structure accommodation:** The synthesis output structure (5 sections per synthesis-validation.md [Synthesis Output Structure]) can accommodate both sub-skill signal types:
- Convergent Findings: Atomic Design component gaps convergent with Inclusive Design WCAG failures for the same components (HIGH confidence)
- Single-Framework Findings: Atomic Design consolidation candidates with no accessibility corroboration, or Inclusive Design Persona Spectrum profiles with no component taxonomy corroboration (MEDIUM confidence)
- Contradictions: Opposing recommendations between component consolidation and accessibility semantics preservation (LOW or MEDIUM confidence)
- Synthesis Judgments Summary: AI judgment calls from both sub-skills' individual judgment summaries (component classifications, severity assignments, Persona Spectrum customizations)
- Validation Required: MEDIUM-confidence findings from both sub-skills requiring expert review or user data (component taxonomy from Atomic Design; Persona Spectrum, severity, and priority from Inclusive Design)

**Step 4 Result:** PASS -- The unified output structure accommodates both Wave 3 sub-skill signal types with full traceability. Both sub-skills require synthesis-level `{PREFIX}-{NNN}` ID assignment for CI-compliant finding identifiers -- Atomic Design uses component names natively, Inclusive Design uses WCAG criterion IDs natively; neither matches the `[A-Z]{2,}-[0-9]{3}` CI regex without re-prefixing.

### Test 1 Overall Result: PASS

All 4 synthesis protocol steps can execute against Wave 3 sub-skill output formats. Signal extraction has threshold-eligible findings from both sub-skills. Convergence detection is feasible via Rule 1 (same component) and Rule 2 (same user problem), with the "Build to Evaluate" canonical sequence creating a strong convergence pathway. Contradiction identification covers all 3 defined types. Unified output accommodates both signal types with complete traceability (subject to synthesis-level ID re-prefixing for both sub-skills).

---

## Test 2: Confidence Classification Coverage (CI: UX-CI-011)

**Objective:** Verify that the `synthesis-validation.md` Sub-Skill Synthesis Output Map includes entries for both Wave 3 sub-skills with appropriate confidence levels.

### Pass Criterion

Both `/ux-atomic-design` and `/ux-inclusive-design` must have at least one entry in the Sub-Skill Synthesis Output Map with a defined confidence level.

**Method:** Check `synthesis-validation.md` [Sub-Skill Synthesis Output Map] for `/ux-atomic-design` and `/ux-inclusive-design` entries.

### `/ux-atomic-design` entries

**Source:** synthesis-validation.md [Sub-Skill Synthesis Output Map].

| Sub-Skill | Synthesis Step | Typical Confidence | Present? |
|---|---|---|---|
| `/ux-atomic-design` | Component taxonomy completeness assessment | MEDIUM | YES |
| `/ux-atomic-design` | Design token consistency analysis | LOW | YES |

**Rationale from synthesis-validation.md:** "Taxonomy assessment depends on Storybook coverage (Frost, 2016); partial coverage yields partial assessment" (MEDIUM). "Token consistency across a full system requires inspection of all component variants; AI sampling may miss edge cases" (LOW).

**Cross-reference with sub-skill SKILL.md:** The Atomic Design SKILL.md [Synthesis Hypothesis Confidence] declares two synthesis steps with matching confidence levels:
- "Component taxonomy completeness assessment" -- MEDIUM ("Taxonomy assessment depends on Storybook coverage (Frost, 2016); partial coverage yields partial assessment -- the architect may miss components not visible in the provided inventory")
- "Design token consistency analysis" -- LOW ("Token consistency across a full system requires inspection of all component variants; AI sampling may miss edge cases where hardcoded values override token references in specific states or responsive breakpoints")

Both entries map to the corresponding rows in synthesis-validation.md. Consistency confirmed.

### `/ux-inclusive-design` entries

**Source:** synthesis-validation.md [Sub-Skill Synthesis Output Map].

| Sub-Skill | Synthesis Step | Typical Confidence | Present? |
|---|---|---|---|
| `/ux-inclusive-design` | Persona Spectrum customization | MEDIUM | YES |

**Rationale from synthesis-validation.md:** "Persona Spectrums are heuristic models (Microsoft Inclusive Design Toolkit, 2016), not empirical profiles"

**Cross-reference with sub-skill SKILL.md:** The Inclusive Design SKILL.md [Synthesis Hypothesis Confidence] declares four synthesis steps:
- "Persona Spectrum customization" -- MEDIUM ("Persona Spectrums are heuristic models (Microsoft, 2016), not empirical profiles; the mapping of permanent/temporary/situational scenarios involves AI judgment about plausible user contexts rather than observed user data")
- "Severity assignment (0-4 scale)" -- MEDIUM ("Severity ratings involve AI interpretation of user impact against the Nielsen severity scale (Nielsen, 1994b)")
- "Remediation priority ranking" -- MEDIUM ("Prioritization requires AI judgment about relative user impact severity, affected population size, and estimated implementation effort")
- "Cognitive load assessment" -- MEDIUM ("Reading level evaluation and information density assessments are heuristic (Nielsen, 1994b)")

The synthesis-validation.md Sub-Skill Synthesis Output Map currently has 1 entry for `/ux-inclusive-design` ("Persona Spectrum customization" at MEDIUM). The SKILL.md declares 4 synthesis steps, all at MEDIUM confidence. The synthesis-validation.md map covers the primary synthesis step; the remaining 3 steps (severity assignment, remediation priority, cognitive load) are documented in the SKILL.md but not individually enumerated in the synthesis-validation.md map.

**Note on WCAG pass/fail exclusion:** The Inclusive Design SKILL.md [Synthesis Hypothesis Confidence] explicitly states: "WCAG 2.2 success criteria evaluations (pass/fail per criterion) do not go through the synthesis hypothesis confidence gate because they are deterministic compliance checks, not AI-generated abstractions." This means WCAG pass/fail findings are excluded from the synthesis confidence gate by design -- they carry no synthesis-level confidence classification because their correctness is deterministic. This is consistent with synthesis-validation.md's purpose: the confidence gate applies to AI-generated abstractions, not to deterministic evaluations.

### Coverage assessment

Both Wave 3 sub-skills have entries in the Sub-Skill Synthesis Output Map:
- `/ux-atomic-design`: 2 entries (MEDIUM and LOW) covering taxonomy completeness and token consistency
- `/ux-inclusive-design`: 1 entry (MEDIUM) covering Persona Spectrum customization; 3 additional MEDIUM steps documented in SKILL.md

The UX-CI-011 gate (ci-checks.md [UX-CI-011: Confidence Classification Presence]) checks that "every finding row in the output includes a confidence classification (HIGH, MEDIUM, or LOW)." Since both sub-skills have defined confidence levels in the map, the orchestrator has the classification data needed to populate synthesis output finding rows.

### Mixed-Confidence Resolution Rule applicability

The Mixed-Confidence Resolution Rule (synthesis-validation.md [Mixed-Confidence Resolution Rule]) is directly relevant to `/ux-atomic-design`, which produces both MEDIUM (taxonomy completeness) and LOW (design token consistency) confidence outputs. When both synthesis steps contribute signals to the same synthesis finding (e.g., a component that is both missing from the taxonomy inventory and has hardcoded token values), the orchestrator applies the minimum-confidence rule: the final synthesis confidence for that finding is LOW (the lower of MEDIUM and LOW). This is the expected behavior and does not indicate a deficiency.

For `/ux-inclusive-design`, all 4 synthesis steps are MEDIUM, so the minimum-confidence rule does not produce a downgrade within this sub-skill. However, WCAG pass/fail findings are deterministic and excluded from the synthesis gate entirely -- the minimum-confidence rule does not apply to them.

### Test 2 Result: PASS

Both Wave 3 sub-skills have entries in the Sub-Skill Synthesis Output Map with appropriate confidence levels. Cross-references between synthesis-validation.md and each sub-skill SKILL.md are consistent. The Mixed-Confidence Resolution Rule correctly applies to Atomic Design dual-confidence outputs. Inclusive Design's WCAG pass/fail exclusion from the synthesis confidence gate is by design, not a coverage gap.

---

## Test 3: Handoff Data Contract Validation

**Objective:** Verify that handoff data produced by each sub-skill (as defined in their SKILL.md output specifications and agent on_send protocols) is compatible with the synthesis protocol's input requirements and with cross-sub-skill handoff between Atomic Design and Inclusive Design.

### Pass Criterion

Both sub-skill output specifications must declare structured on_send fields that provide the synthesis protocol with signal extraction data. The `/ux-atomic-design` on_send `component_inventory` field must feed into `/ux-inclusive-design` on_receive `component_inventory` field.

**Method:** Read the on_send/on_receive field specifications from each sub-skill's SKILL.md [Invoking the Agent] section, verify synthesis-relevant fields are present, and check the Atomic Design -> Inclusive Design handoff compatibility.

### `/ux-atomic-design` on_send fields (SKILL.md [Invoking the Agent])

| on_send Field | Type | Required | Synthesis Use |
|---|---|---|---|
| `component_inventory` | array | Yes | Component taxonomy with classification levels, variant counts, reuse frequency -- provides synthesis scope and convergence targets |
| `design_token_audit` | object | Yes | Token categories with consistency scores and drift instances -- provides token-level signals for convergence with contrast findings |
| `composition_rules` | array | Yes | Documented composition patterns -- informs structural understanding but not directly synthesis-eligible |
| `storybook_coverage` | object | Yes | Coverage percentage, undocumented components, missing states -- provides coverage gap signals for extraction |
| `consolidation_candidates` | array | Yes | Duplicate/near-duplicate component pairs -- provides actionable consolidation signals |
| `synthesis_judgments` | array | Yes | AI judgment calls with confidence classification -- enables downstream confidence assessment |

**Engagement ID:** Present in on_receive fields as `engagement_id` (format: `UX-{NNNN}`).

### `/ux-inclusive-design` on_send fields (SKILL.md [Invoking the Agent])

| on_send Field | Type | Required | Synthesis Use |
|---|---|---|---|
| `conformance_result` | object | Yes | Overall conformance level (A/AA/AAA/none) with per-principle pass/fail -- provides compliance summary for synthesis |
| `wcag_findings` | array | Yes | Per-criterion findings with ID, principle, level, pass/fail, evidence, severity, remediation -- provides WCAG-traceable signals |
| `persona_spectrum_analysis` | array | Yes | Per-interaction-pattern Persona Spectrum profiles -- provides qualitative accessibility signals |
| `contrast_ratios` | array | Yes | Color contrast measurements with element reference, values, ratio, pass/fail -- provides quantitative evidence for token-contrast convergence |
| `keyboard_audit` | object | Yes | Keyboard navigation findings -- provides keyboard accessibility signals |
| `screen_reader_findings` | array | Yes | Screen reader compatibility issues -- provides assistive technology signals |
| `remediation_priorities` | array | Yes | Prioritized remediation list with WCAG reference, severity, effort, impact -- provides actionable remediation signals |
| `synthesis_judgments` | array | Yes | AI judgment calls with confidence classification -- enables downstream confidence assessment |

**Engagement ID:** Present in on_receive fields as `engagement_id` (format: `UX-{NNNN}`).

### Atomic Design -> Inclusive Design Handoff Compatibility

The Wave 3 "Build to Evaluate" canonical sequence is defined in ux-atomic-design SKILL.md [Cross-Framework Integration], Section "Canonical Multi-Skill Workflow Sequences" (line 595): **"`/ux-atomic-design` then `/ux-inclusive-design`"** -- Atomic Design **"Produces the component inventory; inclusive design evaluates each component for accessibility compliance."** This defines a direct handoff from Atomic Design to Inclusive Design.

**Handoff path:** `/ux-atomic-design` on_send `component_inventory` -> `/ux-inclusive-design` on_receive `component_inventory`

| Field | Atomic Design on_send | Inclusive Design on_receive | Compatible? |
|---|---|---|---|
| `component_inventory` | array: Classified components with level (atom/molecule/organism/template/page), variant count, and reuse frequency | array: File paths to component inventory from `/ux-atomic-design` (Storybook references, component taxonomy) | YES -- Atomic Design produces the component taxonomy; Inclusive Design consumes it as evaluation scope. The on_receive expects file paths (artifact references per CP-01), while on_send produces structured data. The orchestrator bridges this by passing the artifact file path per CB-03 (prefer file-path references in handoffs). |
| `design_token_audit` | object: Token categories with consistency scores and drift instances | Not explicitly in on_receive | PARTIAL -- Inclusive Design does not explicitly receive design token data, but the Color Contrast Analysis methodology can consume token color values when provided as part of the engagement context. Token drift findings with specific hex values can inform contrast ratio computation. |
| `storybook_coverage` | object: Coverage percentage, components without stories, missing states | Not explicitly in on_receive; consumed via `design_artifacts` (optional) or via component inventory that includes Storybook story status | YES -- Storybook references are part of the component inventory handoff; Inclusive Design can use Storybook stories to evaluate interactive state accessibility. |

**Handoff threshold compatibility:** Atomic Design SKILL.md [Cross-Framework Integration]: "Only components with classification level assigned (atom through page) and at least a name and variant count are included in cross-framework handoffs." Inclusive Design SKILL.md [Cross-Framework Integration]: "Only findings with severity >= 2 (minor barrier or above) are included in cross-framework synthesis handoffs." Both thresholds are signal-reduction filters applied at the source sub-skill level -- they are independent and non-conflicting.

### Finding ID Format Compatibility

| Sub-Skill | Native Finding ID Format | CI Regex `[A-Z]{2,}-[0-9]{3}` Match? | Resolution |
|---|---|---|---|
| `/ux-atomic-design` | Component names (e.g., "Button", "SearchForm", "Header") | NO -- component names are not in `{PREFIX}-{NNN}` format | Synthesis-level re-prefixing required (e.g., `AD-001`, `AD-002`) per synthesis-validation.md [Required Traceability] |
| `/ux-inclusive-design` | WCAG success criterion IDs (e.g., `SC 1.4.3`, `SC 2.1.1`) | NO -- `SC X.Y.Z` format does not match `[A-Z]{2,}-[0-9]{3}` | Synthesis-level re-prefixing required (e.g., `ID-001`, `ID-002`) per synthesis-validation.md [Required Traceability] |

Both Wave 3 sub-skills require synthesis-level re-prefixing. This is consistent with Wave 1 behavior (heuristic eval `F-{NNN}` and JTBD `J-{NNN}` required re-prefixing) and Wave 2 behavior (HEART metric names required re-prefixing to `HM-{NNN}`).

### Test 3 Result: PASS

Both sub-skills declare comprehensive on_send field specifications that provide the synthesis protocol with sufficient data for signal extraction. The Atomic Design -> Inclusive Design handoff via `component_inventory` is structurally compatible -- Atomic Design produces the component taxonomy that Inclusive Design evaluates. Both sub-skills require synthesis-level `{PREFIX}-{NNN}` ID assignment, consistent with prior waves. The "Build to Evaluate" canonical sequence provides a well-defined handoff pathway.

---

## Test 4: Degraded Mode Synthesis

**Objective:** Verify that synthesis can still operate if one or both sub-skills operate in degraded mode.

### Pass Criterion

The synthesis protocol must have a documented failure mode handling entry for degraded sub-skill inputs, and the sub-skill output specifications must include degraded mode indicators.

**Method:** Check what MCP dependencies affect each sub-skill, what degraded mode behavior looks like, and whether the synthesis protocol handles reduced-confidence inputs.

### `/ux-atomic-design` degraded mode

**Source:** ux-atomic-design SKILL.md [MCP Dependencies].

When the Storybook MCP adapter is unavailable (current state -- Storybook is a **REQ** dependency per SKILL.md), the architect operates in **Manual Component Inventory Mode** with the following limitations:
- Cannot browse or validate live component stories programmatically
- Cannot inspect component variants, states, or props interactively
- Cannot verify design token usage in component implementations
- Coverage assessment accuracy depends on completeness of user-provided inventory

The output carries a degraded mode disclosure per P-022 (SKILL.md [MCP Dependencies]):
```
[DEGRADED MODE] This output was produced without Storybook MCP access.
```

**Handoff impact in degraded mode:**

| Output Field | Normal Mode | Degraded Mode | Change |
|---|---|---|---|
| `storybook_coverage` | Programmatic coverage from live Storybook instance | User-reported coverage data; lower accuracy | Coverage percentages less reliable; may undercount or overcount |
| `component_inventory` | Component list with verified Storybook story status | Component list with user-reported story status | Story status (documented/undocumented/partial) depends on user accuracy |
| `design_token_audit` | Token drift detection from component implementation inspection | Token drift detection from documentation and descriptions only | Drift ratio may undercount hardcoded values not visible in text descriptions |
| Signal extraction impact | Components without Storybook coverage provide high-quality extraction signals (programmatically verified) | Components reported as undocumented provide lower-quality extraction signals (user-reported, not verified) | Signal quality reduced but signal type unchanged |

**Key finding:** Atomic Design degraded mode (Manual Component Inventory Mode) produces the same output structure and signal types as normal mode. The core methodology (5-level component taxonomy, composition rules, consolidation analysis) is self-contained in the agent's methodology and does not depend on Storybook MCP. The primary impact is on Storybook coverage accuracy -- coverage percentages in degraded mode are less reliable because they depend on user-provided inventory completeness rather than programmatic verification.

### `/ux-inclusive-design` degraded mode

**Source:** ux-inclusive-design SKILL.md [MCP Dependencies].

When the Figma MCP adapter is unavailable (current state -- Figma is a **REQ** dependency per SKILL.md), the evaluator operates in **Screenshot-Input Mode** with the following limitations:
- Cannot inspect design layers or component hierarchy programmatically
- Cannot extract exact color values for automated contrast ratio computation
- Cannot evaluate interactive states (animations, transitions, dynamic content)
- Cannot access design token definitions or systematic color palette information

The output carries a degraded mode disclosure per P-022 (SKILL.md [MCP Dependencies]):
```
[DEGRADED MODE] This output was produced without Figma MCP access.
```

**Handoff impact in degraded mode:**

| Output Field | Normal Mode | Degraded Mode | Change |
|---|---|---|---|
| `contrast_ratios` | Computed from extracted color values | Computed from user-provided hex/RGB values; or flagged as "insufficient data" where values unavailable | Fewer contrast ratios computable; some elements may have no ratio measurement |
| `wcag_findings` | Full WCAG evaluation with programmatic evidence | Evaluation from screenshots; some criteria (especially interactive states) may be assessed as "NOT APPLICABLE -- requires interactive testing" | Reduced criterion coverage; interactive state criteria less thoroughly evaluated |
| `persona_spectrum_analysis` | No change -- Persona Spectrum is methodology-based, not MCP-dependent | No change | No impact |
| `keyboard_audit` | Limited (Figma does not directly provide keyboard data) | Same -- keyboard audit relies on markup descriptions regardless | Minimal change |
| Signal extraction impact | WCAG violations at severity >= 2 provide high-quality extraction signals with precise evidence | WCAG violations still extracted but evidence may be less precise (estimated rather than measured) | Signal quality reduced for visual-dependent criteria; signal type unchanged |

**Key finding:** Inclusive Design degraded mode (Screenshot-Input Mode) primarily impacts color contrast precision and interactive state evaluation. The WCAG methodology framework (POUR principle evaluation, Persona Spectrum analysis, keyboard audit, screen reader review) operates from the agent's methodology regardless of Figma access. Persona Spectrum analysis is entirely methodology-based and unaffected by MCP degradation.

### Synthesis protocol handling of degraded inputs

**Source:** synthesis-validation.md [Failure Mode Handling], specifically the "MCP Degraded Synthesis Inputs" row.

| Failure Mode | Detection | Orchestrator Action | Confidence Impact |
|---|---|---|---|
| MCP Degraded Synthesis Inputs | Sub-skill operated in text-only mode due to MCP unavailability | Accept sub-skill output but note MCP degradation in synthesis report; add note per affected finding: "Source sub-skill operated without MCP design artifact access" | **No automatic downgrade** -- MCP degradation affects input quality, which is reflected in the sub-skill's own confidence assessment |

**Key finding for Wave 3:** The synthesis protocol explicitly handles degraded inputs via the "MCP Degraded Synthesis Inputs" failure mode. For Atomic Design, the Manual Component Inventory Mode reduces Storybook coverage accuracy but does not alter signal types. For Inclusive Design, the Screenshot-Input Mode reduces contrast ratio precision but does not alter WCAG evaluation methodology. Both degraded mode disclosures per P-022 are visible to the orchestrator in the output files.

**Scenario trace -- Wave 3 degraded synthesis:**

1. `ux-atomic-architect` produces component inventory in Manual Component Inventory Mode with `[DEGRADED MODE]` disclosure
2. `ux-inclusive-evaluator` produces WCAG audit in Screenshot-Input Mode with `[DEGRADED MODE]` disclosure
3. Orchestrator runs 4-step synthesis:
   - Step 1 (Signal Extraction): Extracts Atomic Design signals normally (undocumented components, drift ratio violations). Extracts Inclusive Design signals normally (WCAG violations at severity >= 2). Signal types unchanged; signal quality reduced for Storybook coverage accuracy (Atomic Design) and contrast ratio precision (Inclusive Design).
   - Step 2 (Convergence Detection): Convergence operates on signal content. Component-accessibility convergence (Rule 1 + Rule 2) remains feasible because both sub-skills still produce component-level findings. Token-contrast convergence may be weaker if Inclusive Design cannot compute exact contrast ratios, but approximate assessments still enable convergence detection.
   - Step 3 (Contradiction Identification): No change -- contradictions are content-based. Consolidation vs. accessibility preservation conflicts remain detectable from text-based output.
   - Step 4 (Unified Output): Synthesis report includes per-finding annotations for both degraded conditions. Design token consistency sections retain `[REFERENCE-ONLY]` tagging (unchanged from non-degraded mode since design token consistency is always LOW).

### Test 4 Result: PASS

The synthesis protocol handles degraded-mode inputs from both Wave 3 sub-skills. Atomic Design degraded mode (Storybook MCP unavailability) reduces Storybook coverage accuracy but preserves the component taxonomy methodology. Inclusive Design degraded mode (Figma MCP unavailability) reduces color contrast precision but preserves the WCAG evaluation methodology and Persona Spectrum analysis. Both degraded conditions are disclosed per P-022 and visible to the orchestrator. No automatic confidence downgrade occurs -- each sub-skill's own confidence assessment propagates naturally.

---

## Test 5: CI Gate Readiness (UX-CI-011, UX-CI-012, UX-CI-013)

**Objective:** Verify that the CI gates defined for synthesis outputs can be evaluated against Wave 3 sub-skill outputs.

### Pass Criterion

All 3 CI gates (UX-CI-011, UX-CI-012, UX-CI-013) must be evaluable against Wave 3 synthesis output format.

**Method:** For each CI gate, verify that the synthesis output format produced from Wave 3 sub-skill inputs contains the data patterns the gate's implementation script checks for.

### UX-CI-011: Confidence Classification Presence

**Gate definition** (ci-checks.md [UX-CI-011: Confidence Classification Presence]): Every finding row in synthesis output (matching pattern `| {PREFIX}-{NNN}`) must include a confidence classification (HIGH, MEDIUM, or LOW).

**Wave 3 evaluability:**

The synthesis output from Wave 3 sub-skills will contain finding rows with:
- Convergent Findings: Findings where both Atomic Design and Inclusive Design signals converge on the same component -- classified HIGH per synthesis-validation.md [Convergence Thresholds] (moderate or strong convergence, 2 frameworks with supporting evidence)
- Single-Framework Findings: Findings from only one sub-skill -- classified MEDIUM per synthesis-validation.md [Convergence Thresholds]
- Contradictions: Classified LOW (direct opposition or methodology conflicts) or MEDIUM (priority conflicts) per synthesis-validation.md [Contradiction Handling]

Additionally, Atomic Design design token consistency findings will carry LOW confidence (synthesis-validation.md [Sub-Skill Synthesis Output Map]: "Design token consistency analysis: LOW"). When the Mixed-Confidence Resolution Rule applies (an Atomic Design finding combining taxonomy completeness at MEDIUM with token consistency at LOW), the synthesis-level confidence is LOW.

Inclusive Design WCAG pass/fail findings are excluded from the synthesis confidence gate by design (SKILL.md [Synthesis Hypothesis Confidence]). However, when WCAG findings appear in the synthesis output, they will carry synthesis-level confidence based on convergence status, not sub-skill-level confidence. Persona Spectrum findings carry MEDIUM confidence.

The CI gate script (ci-checks.md [UX-CI-011] implementation) uses `grep -cE '^\|.*[A-Z]{2,}-[0-9]{3}'` to count finding rows and then checks each for `(HIGH|MEDIUM|LOW)`. Since all Wave 3 synthesis findings receive a confidence classification from the synthesis protocol (not left unclassified), this gate can execute successfully.

**UX-CI-011 Result:** PASS -- Confidence classifications are deterministically assigned by the synthesis protocol for all possible Wave 3 finding categories (convergent, singleton, contradiction, token-related LOW confidence).

### UX-CI-012: Traceability

**Gate definition** (ci-checks.md [UX-CI-012: Traceability]): Every finding row must include a source sub-skill name (`/ux-*` pattern) and at least 2 distinct `{PREFIX}-{NNN}` patterns (the synthesis-level ID plus at least one source finding ID).

**Wave 3 evaluability:**

The synthesis output from Wave 3 will contain finding rows with:
- Sub-skill references: `/ux-atomic-design` and/or `/ux-inclusive-design` -- both match the `/ux-[a-z-]+` pattern checked by the gate's Pass 1 (ci-checks.md [UX-CI-012] implementation)
- Finding IDs: Each row will have a synthesis-level ID (e.g., `CONV-001`, `SING-001`, `CONTRA-001`) plus at least one source finding ID (e.g., `AD-001`, `ID-001`). The gate's Pass 2 counts distinct `[A-Z]{2,}-[0-9]{3}` patterns per row and requires >= 2.

**Atomic Design source finding IDs:** Component names are not in `{PREFIX}-{NNN}` format natively. At the synthesis level, the orchestrator must assign `{PREFIX}-{NNN}` identifiers (e.g., `AD-001`, `AD-002`) to Atomic Design findings. This is consistent with synthesis-validation.md [Required Traceability] which requires both a synthesis-level finding ID and a source finding ID.

**Inclusive Design source finding IDs:** WCAG success criterion IDs (`SC X.Y.Z`) are not in `{PREFIX}-{NNN}` format natively. At the synthesis level, the orchestrator must assign `{PREFIX}-{NNN}` identifiers (e.g., `ID-001`, `ID-002`) to Inclusive Design findings. Persona Spectrum findings also require `{PREFIX}-{NNN}` assignment (e.g., `PS-001`).

**UX-CI-012 Result:** PASS (conditional) -- The gate can evaluate Wave 3 outputs if the orchestrator assigns `{PREFIX}-{NNN}` identifiers to both Atomic Design component findings and Inclusive Design WCAG/Persona Spectrum findings in the synthesis report. This condition is structurally identical to the Wave 1 and Wave 2 conditions where source finding IDs required re-prefixing.

### UX-CI-013: LOW Confidence Template Compliance

**Gate definition** (ci-checks.md [UX-CI-013: LOW Confidence Template Compliance]): Sections tagged `[REFERENCE-ONLY]` must not contain subsections named "Design Recommendations" or "Recommended Actions" or recommendation-like bullet patterns.

**Wave 3 evaluability:**

LOW-confidence findings in Wave 3 synthesis outputs arise from:
- Direct opposition contradictions (synthesis-validation.md [Contradiction Handling]): e.g., Atomic Design recommends component consolidation while Inclusive Design identifies accessibility semantics that would be lost
- Methodology conflicts (synthesis-validation.md [Contradiction Handling]): e.g., token standardization recommendation vs. accessibility spacing constraint
- Atomic Design design token consistency findings (synthesis-validation.md [Sub-Skill Synthesis Output Map]): "Design token consistency analysis: LOW"
- Mixed-confidence findings where Atomic Design token consistency LOW combines with taxonomy completeness MEDIUM via the minimum-confidence rule

Per the LOW gate enforcement (synthesis-validation.md [Confidence Classification]): "Output template structurally omits the design recommendation section. Title tagged with `[REFERENCE-ONLY]`."

**Wave 3 specific scope:** Wave 3 has a notable LOW-confidence surface area from Atomic Design's design token consistency analysis. Every design token consistency finding carries LOW confidence, meaning the token audit portions of the synthesis output will be tagged `[REFERENCE-ONLY]`. The Atomic Design SKILL.md [Synthesis Hypothesis Confidence] explicitly states: "LOW outputs (token consistency): Output template structurally omits design token remediation recommendations. Title tagged with `[REFERENCE-ONLY]`." This pre-existing LOW gate compliance within the sub-skill output means the CI gate's scope in Wave 3 includes:
1. Contradiction sections (direct opposition and methodology conflict) -- consistent with Wave 1 and Wave 2
2. Design token consistency sections (all token-related findings) -- new in Wave 3

The CI gate script (ci-checks.md [UX-CI-013] implementation) uses `awk` to extract content within `[REFERENCE-ONLY]` sections and checks for forbidden heading patterns (`Design Recommendations`, `Recommended Actions`, `Design Interventions`) and recommendation-like bullet patterns (`Implement`, `Deploy`, `Redesign`, `Add`, `Remove`, `Replace`, `Migrate`). This operates on the synthesis output file structure.

**UX-CI-013 Result:** PASS -- The gate can evaluate Wave 3 outputs. Its scope in Wave 3 includes design token consistency LOW-confidence sections (from Atomic Design's inherent LOW classification) and contradiction sections. The `[REFERENCE-ONLY]` tagging is already part of the Atomic Design agent's output specification per SKILL.md [Synthesis Hypothesis Confidence].

---

## Verdict

| Test | Scope | Result | Key Evidence |
|------|-------|--------|-------------|
| **Test 1: Synthesis Output Structure** | 4-step protocol trace | **PASS** | All 4 steps (Signal Extraction, Convergence Detection, Contradiction Identification, Unified Output) execute against Wave 3 output formats. Rule 1 (same component) and Rule 2 (same user problem) are the primary convergence pathways, strongly enabled by the "Build to Evaluate" canonical sequence. |
| **Test 2: Confidence Classification Coverage** | CI: UX-CI-011 prerequisite | **PASS** | Both sub-skills have entries in synthesis-validation.md [Sub-Skill Synthesis Output Map]: `/ux-atomic-design` (2 entries: MEDIUM, LOW), `/ux-inclusive-design` (1 entry: MEDIUM; 3 additional MEDIUM steps in SKILL.md). Cross-references consistent with sub-skill SKILL.md declarations. Mixed-Confidence Resolution Rule applicable to Atomic Design dual-confidence outputs. WCAG pass/fail excluded from synthesis gate by design. |
| **Test 3: Handoff Data Contract** | on_send/on_receive + cross-sub-skill handoff | **PASS** | `/ux-atomic-design` on_send includes 6 structured fields (component_inventory, design_token_audit, composition_rules, storybook_coverage, consolidation_candidates, synthesis_judgments). `/ux-inclusive-design` on_send includes 8 structured fields (conformance_result, wcag_findings, persona_spectrum_analysis, contrast_ratios, keyboard_audit, screen_reader_findings, remediation_priorities, synthesis_judgments). Cross-sub-skill handoff via component_inventory is structurally compatible. Both sub-skills require synthesis-level ID assignment. |
| **Test 4: Degraded Mode Synthesis** | Storybook unavailability + Figma unavailability | **PASS** | Atomic Design degraded mode (Manual Component Inventory) reduces Storybook coverage accuracy but preserves taxonomy methodology. Inclusive Design degraded mode (Screenshot-Input) reduces contrast precision but preserves WCAG and Persona Spectrum methodology. Both conditions disclosed per P-022. No automatic confidence downgrade. |
| **Test 5a: UX-CI-011 (Confidence)** | CI gate evaluability | **PASS** | All Wave 3 finding categories receive deterministic confidence classification. Design token consistency findings add LOW-confidence surface area (new in Wave 3). |
| **Test 5b: UX-CI-012 (Traceability)** | CI gate evaluability | **PASS** (conditional) | Both sub-skills require orchestrator-assigned `{PREFIX}-{NNN}` IDs: Atomic Design uses component names natively; Inclusive Design uses WCAG criterion IDs natively. Neither matches CI regex without re-prefixing. |
| **Test 5c: UX-CI-013 (LOW Template)** | CI gate evaluability | **PASS** | Gate scope in Wave 3 includes design token consistency LOW-confidence sections (from Atomic Design's inherent LOW classification). `[REFERENCE-ONLY]` tagging is part of Atomic Design agent's output specification. |

**Test 5 Overall Result:** All three CI gates (UX-CI-011, UX-CI-012, UX-CI-013) are evaluable against Wave 3 synthesis outputs. These gates apply to both standard synthesis output filenames (`ux-orchestrator-synthesis.md` in the `output/{engagement-id}/` directory) and crisis-mode output filenames (`ux-orchestrator-crisis.md` in the `output/{engagement-id}/` directory).

**Overall Wave 3 Cross-Framework Synthesis Readiness: PASS**

All tests pass. One conditional note: Test 5b (UX-CI-012) requires the orchestrator to assign `{PREFIX}-{NNN}` identifiers to both Atomic Design and Inclusive Design findings in synthesis report rows. This is consistent with the synthesis-validation.md [Required Traceability] protocol and the re-prefixing pattern established in Wave 1 and Wave 2.

---

## Required Actions Before Wave 3 Signoff

1. **Finding ID assignment confirmation for both sub-skills:** The ux-orchestrator agent must assign `{PREFIX}-{NNN}` identifiers to Wave 3 findings in synthesis report rows. Atomic Design findings need `AD-{NNN}` prefixes (e.g., `AD-001: Button atom -- undocumented`), and Inclusive Design findings need `ID-{NNN}` prefixes (e.g., `ID-001: SC 1.4.3 Minimum Contrast failure`). This mapping SHOULD be encoded in the ux-orchestrator agent's `<methodology>` section at **Phase 5 (Cross-Framework Synthesis), Step 5d (Unified Synthesis Output)** -- specifically within the instruction "Each finding traces back to its source sub-skill output by engagement ID and finding number" (ux-orchestrator.md line 256). Step 5d currently specifies the 3-section output structure (Convergent, Single-Framework, Contradictions) but does not prescribe the `{PREFIX}-{NNN}` re-prefixing format. Add a synthesis formatting sub-step between the current Step 5d output structure definition and the Failure Mode paragraph.

   **Dual-source traceability chain for convergent findings:** When two Wave 3 sub-skills contribute to a convergent finding (Step 5b), the synthesis row must contain both source IDs. Example convergent finding row format:

   > `CONV-001: Form input label color -- token drift causes contrast failure | /ux-atomic-design (AD-003: color token drift ratio 0.25 on form-input-label) | /ux-inclusive-design (ID-007: SC 1.4.3 Minimum Contrast -- computed ratio 3.8:1 < 4.5:1 AA) | HIGH`

   This format satisfies UX-CI-012's Pass 2 requirement (>= 2 distinct `[A-Z]{2,}-[0-9]{3}` patterns per row): `CONV-001`, `AD-003`, and `ID-007` all match the regex, providing 3 distinct patterns. Single-framework finding rows follow the same pattern with one source ID (e.g., `SING-001: ... | /ux-atomic-design (AD-005: ...) | MEDIUM`).

   Consistent with the Wave 1 re-prefixing requirement for heuristic eval (`HE-{NNN}`) and JTBD (`JT-{NNN}`) and the Wave 2 requirement for HEART metrics (`HM-{NNN}`). Verify by checking that UX-CI-012 regex `[A-Z]{2,}-[0-9]{3}` matches all finding ID references in synthesis output.
2. **Synthesis-validation.md Inclusive Design coverage expansion (MEDIUM priority):** The synthesis-validation.md Sub-Skill Synthesis Output Map currently has 1 entry for `/ux-inclusive-design` (Persona Spectrum customization at MEDIUM). The Inclusive Design SKILL.md declares 3 additional MEDIUM synthesis steps (severity assignment, remediation priority ranking, cognitive load assessment) that are not individually enumerated in the map. Consider adding these entries for completeness. This does not block signoff because all 4 steps share the same MEDIUM confidence level and the map entry covers the primary synthesis step.
3. **Wave signoff population:** The WAVE-3-SIGNOFF.md document requires test rows in the "Cross-Framework Synthesis Test" section. Populate from this document's Verdict table, mapping each test's Result to the signoff template's Pass/Fail column.
4. **Conditional PASS resolution:** Test 5b (UX-CI-012) is PASS (conditional). The condition (orchestrator finding ID assignment for both sub-skills) must be verified before the wave gate can be marked PASS unconditionally.
5. **Agent implementation prerequisite:** Both sub-skill agents (`ux-atomic-architect` and `ux-inclusive-evaluator`) are currently STUB/PLANNED status. Full agent implementation (`<input>`, `<capabilities>`, `<methodology>`, `<output>` sections) must be completed before runtime synthesis can be verified. This test validates structural compatibility based on SKILL.md specifications; runtime verification requires implemented agents.

---

## Wave 3 Signoff Readiness

Mapping from test results to `skills/user-experience/templates/wave-signoff-template.md` [Cross-Framework Synthesis Test] rows:

| Signoff Row | Source Test | Result | Evidence Reference |
|-------------|-----------|--------|-------------------|
| Synthesis output structure validated | Test 1 | PASS | [Test 1: Synthesis Output Structure Validation](#test-1-synthesis-output-structure-validation) |
| Confidence classifications present | Test 2 | PASS | [Test 2: Confidence Classification Coverage](#test-2-confidence-classification-coverage-ci-ux-ci-011) |
| Handoff contracts compatible | Test 3 | PASS | [Test 3: Handoff Data Contract Validation](#test-3-handoff-data-contract-validation) |
| Degraded mode synthesis verified | Test 4 | PASS | [Test 4: Degraded Mode Synthesis](#test-4-degraded-mode-synthesis) |
| CI gates evaluable | Test 5 | PASS (conditional) | [Test 5: CI Gate Readiness](#test-5-ci-gate-readiness-ux-ci-011-ux-ci-012-ux-ci-013) |

---

## References

| Source | Content | Path |
|--------|---------|------|
| Synthesis validation rules | 4-step protocol, confidence classification, convergence thresholds, contradiction handling, output structure | `skills/user-experience/rules/synthesis-validation.md` |
| Atomic Design sub-skill spec | Output specification, methodology, 5-level hierarchy, design tokens, Storybook coverage, cross-framework integration, synthesis confidence | `skills/ux-atomic-design/SKILL.md` |
| Inclusive Design sub-skill spec | Output specification, methodology, WCAG 2.2 audit, Persona Spectrum, cross-framework integration, synthesis confidence | `skills/ux-inclusive-design/SKILL.md` |
| Parent skill spec | Available Agents table, Cross-Framework Synthesis Protocol, Wave Architecture | `skills/user-experience/SKILL.md` |
| CI checks | UX-CI-011 (confidence), UX-CI-012 (traceability), UX-CI-013 (LOW template) gate definitions | `skills/user-experience/rules/ci-checks.md` |
| Wave signoff template | Cross-Framework Synthesis Test section, required test rows | `skills/user-experience/templates/wave-signoff-template.md` |
| Atomic Design agent definition | on_send field specification (`component_inventory`, `design_token_audit`, `synthesis_judgments`); Wave 3 stub status | `skills/ux-atomic-design/agents/ux-atomic-architect.md` |
| Inclusive Design agent definition | on_send field specification (`component_inventory`, `wcag_findings`, `persona_spectrum_analysis`, `synthesis_judgments`); Wave 3 stub status | `skills/ux-inclusive-design/agents/ux-inclusive-evaluator.md` |
| Agent development standards | Handoff Protocol v2, required handoff fields (HD-M-001 through HD-M-005), context passing conventions (CP-01 through CP-05) | `.context/rules/agent-development-standards.md` |
| Quality enforcement | Quality gate thresholds, criticality levels, S-014 scoring dimensions | `.context/rules/quality-enforcement.md` |

**External methodology citations:** Bibliographic references cited in the test body (Frost, 2016 for Atomic Design; W3C, 2023 for WCAG 2.2; Microsoft, 2016 for Inclusive Design Toolkit; Nielsen, 1994b for severity rating scale) are documented with full bibliographic entries in `skills/user-experience/rules/synthesis-validation.md` [External Methodology Citations] and the respective sub-skill SKILL.md References sections.

---

*Document Version: 1.1.0*
*Parent Skill: /user-experience*
*Wave: 3 (Design System)*
*Project: PROJ-022 User Experience Skill*
*Created: 2026-03-04*
