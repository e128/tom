# Quality Score Report: Synthesis Validation Rules

## L0 Executive Summary
**Score:** 0.879/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.72)
**One-line assessment:** The artifact is structurally sound and methodologically rigorous, but falls short of the C4 threshold (0.95) due to insufficient external evidence for confidence classification thresholds, a terminology inconsistency between the sub-skill synthesis map and its parent SKILL.md, and one incompletely specified failure mode; address these three targeted gaps to reach PASS.

---

## Scoring Context
- **Deliverable:** `skills/user-experience/rules/synthesis-validation.md`
- **Deliverable Type:** Research/Design (Rule File)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Threshold:** 0.95 (C4 per scoring request)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.879 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 7 sections present with required sub-sections; sub-skill map expands SKILL.md but omits two sub-skills present in SKILL.md agent roster |
| Internal Consistency | 0.20 | 0.85 | 0.170 | Terminology inconsistency: synthesis map uses sub-skill names that differ from SKILL.md agent names (e.g., `/ux-heuristic-eval` vs. `ux-heuristic-evaluator`); one structural protocol contradiction |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | 4-step sequential mechanism is well-defined; convergence rules are precise; contradiction types are enumerated; P-020/P-022 compliance woven throughout |
| Evidence Quality | 0.15 | 0.72 | 0.108 | Source attribution uses HTML comments only; confidence thresholds (e.g., "severity >= 2", "strength >= 3", "5-8 respondents") lack external citation to the originating frameworks (Nielsen, Fogg, Kano); rationale column in sub-skill map is descriptive but not empirically grounded |
| Actionability | 0.15 | 0.90 | 0.135 | Gate enforcement mechanisms are operationally specific (structured sections, placeholder fields, structural omission); CONTRA-{NNN} format precise; failure modes actionable |
| Traceability | 0.10 | 0.92 | 0.092 | HTML comment source markers on all major sections trace to named SKILL.md sections; CI gate references (UX-CI-011/012/013) verified as existing; sibling rule cross-references accurate |
| **TOTAL** | **1.00** | | **0.879** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**
The artifact contains all 7 sections enumerated in its own navigation table: Confidence Classification, Sub-Skill Synthesis Output Map, Cross-Framework Synthesis Protocol, Convergence Thresholds, Contradiction Handling, Synthesis Output Structure, and Failure Mode Handling. Navigation table (H-23) is present with anchor links (H-24). All major protocol elements are present: gate definitions (lines 29-33), enforcement mechanisms (lines 37-39), immutability rules (lines 43-45), 4-step sequential mechanism (lines 88-93), convergence matching rules (lines 129-132), contradiction format (lines 154-161), and required traceability fields (lines 183-189).

**Gaps:**
1. The Sub-Skill Synthesis Output Map (lines 55-72) covers 10 sub-skills across 16 rows, but the parent SKILL.md Sub-Skill Synthesis Output Map (lines 352-365) covers only 12 rows for 9 sub-skills. The rule file expands the map with `/ux-heuristic-eval` (2 rows) and `/ux-atomic-design` (2 rows) not present in SKILL.md. However, the SKILL.md agent roster (line 17-26) lists `ux-sprint-facilitator` (Design Sprint) which IS covered (lines 61-62), and `ux-atomic-architect` (Atomic Design) which is covered (lines 71-72). Cross-checking: the SKILL.md synthesis map has no entries for `/ux-heuristic-eval` comparative synthesis — this is added by the rule file but without explanation of why it was omitted from SKILL.md. This creates an unexplained divergence.
2. The Failure Mode Handling section (lines 192-207) handles only two failure modes: Low-Confidence Majority and Synthesis Scope Limitation. The sibling rule file `mcp-coordination.md` is cited as covering MCP-related failure modes, but the cross-reference does not specify which MCP degraded modes affect synthesis input quality — the reader must look up the sibling file. This is a completeness gap for a standalone rule file.

**Improvement Path:**
- Add a brief explanatory note for the expanded Sub-Skill Synthesis Output Map entries not present in SKILL.md (one sentence per added sub-skill explaining why they were added at rule-file level).
- Add a third failure mode "MCP Degraded Synthesis" with 2-3 bullet points summarizing the relevant `mcp-coordination.md` behavior so the rule file stands alone.

---

### Internal Consistency (0.85/1.00)

**Evidence:**
The confidence classification gate definitions are consistent throughout the document. HIGH/MEDIUM/LOW assignments in the Sub-Skill Synthesis Output Map are consistent with Convergence Thresholds (e.g., SKILL.md and the rule file both assign LOW to "Feature priority conflict interpretation" for `/ux-kano-model`). The CONTRA-{NNN} format is defined once and applied consistently. P-020 and P-022 are referenced with consistent interpretation throughout.

**Gaps:**
1. **Terminology inconsistency — sub-skill identifiers.** The Sub-Skill Synthesis Output Map (lines 55-72) uses slash-command notation: `/ux-heuristic-eval`, `/ux-jtbd`, `/ux-lean-ux`, `/ux-design-sprint`, `/ux-inclusive-design`, `/ux-kano-model`, `/ux-behavior-design`, `/ux-heart-metrics`, `/ux-ai-first-design`, `/ux-atomic-design`. The SKILL.md Available Agents table uses agent name notation: `ux-heuristic-evaluator`, `ux-jtbd-analyst`, `ux-lean-ux-facilitator`, `ux-sprint-facilitator`, `ux-inclusive-evaluator`, `ux-kano-analyst`, `ux-behavior-diagnostician`, `ux-heart-analyst`, `ux-ai-design-guide`, `ux-atomic-architect`. These are two different naming conventions for the same entities. A reader cannot directly cross-reference the Sub-Skill map to the agent roster without mapping manually. Additionally, the sub-skill command names used in the map (e.g., `/ux-heuristic-eval`) do not match the SKILL.md agent names OR the sub-skill directory structure (neither is defined). This creates ambiguity about which identifier is canonical.
2. **Structural protocol tension — Step 2 convergence confidence.** The Cross-Framework Synthesis Protocol Step 2 states "Convergent signals (2+ frameworks) and singleton (1 framework)" (line 91) without assigning confidence at this step. However, the SKILL.md (line 384) says "Convergent signals (2+ frameworks identify the same issue) receive HIGH synthesis confidence. Single-framework signals receive MEDIUM." The rule file Convergence Thresholds table (lines 118-123) introduces a finer-grained classification: Strong Convergence (3+ = HIGH), Moderate Convergence (2 with quantitative evidence = HIGH), Weak Convergence (2 without strong evidence = MEDIUM), No Convergence (single framework = MEDIUM). This is MORE detailed than SKILL.md but the Step 2 table in the Mechanism section (line 91) does not reference this sub-classification — a reader of the mechanism table alone would think all 2+ convergences are HIGH, which conflicts with the Convergence Thresholds section.

**Improvement Path:**
- Choose one canonical sub-skill identifier format (slash-command vs. agent name vs. sub-skill directory) and apply consistently throughout. Add a "Terminology Note" sidebar explaining the two naming conventions if both must be preserved.
- Update the Step 2 row in the Mechanism table (line 91) to say "Convergent signals grouped per Convergence Thresholds section (HIGH or MEDIUM depending on convergence level)" to remove the contradiction with the finer-grained table.

---

### Methodological Rigor (0.92/1.00)

**Evidence:**
The 4-step sequential mechanism is precisely specified with input, output, and validation check columns (lines 88-93). Each step is independently verifiable. Convergence matching rules are operationally precise (lines 129-132) with the P-022 default rule for uncertainty ("defaults to 'related but NOT convergent'"). The contradiction detection taxonomy (3 types: direct opposition, priority conflict, methodology conflict) with distinct confidence assignments is sound UX methodology. Gate enforcement mechanisms (Judgments Summary, Validation Required section, structural omission) provide concrete implementation guidance, not vague intent. The Classification Immutability rules (lines 43-45) are unambiguous — LOW cannot be upgraded, MEDIUM cannot be upgraded to HIGH without evidence.

**Gaps:**
1. The Signal Extraction Criteria table (lines 100-110) provides thresholds for 8 sub-skill types, but `/ux-design-sprint` and `/ux-ai-first-design` are absent from the extraction criteria. Since these sub-skills are in the synthesis map (and thus can produce inputs to synthesis), the absence of extraction criteria creates a methodology gap: the orchestrator has no defined rule for what constitutes an extractable signal from Design Sprint or AI-First Design outputs. This is a genuine methodology gap, not a documentation choice.
2. The convergence matching definition of "same user problem" (lines 130-131) is rigorous but relies on orchestrator judgment for the "same user population segment" sub-criterion without a tiebreak rule when populations partially overlap. The P-022 default ("related but NOT convergent") handles full uncertainty, but partial overlap is a grey area that a real orchestrator would encounter frequently.

**Improvement Path:**
- Add rows for `/ux-design-sprint` and `/ux-ai-first-design` to the Signal Extraction Criteria table with methodology-appropriate criteria (e.g., Design Sprint: "Interview themes identified by 3+ of 5 users"; AI-First Design: "Patterns flagged as HIGH trust-risk or HIGH error-risk").
- Add a tiebreak rule for population overlap: "When user populations partially overlap (e.g., one signal applies to 'mobile users' and another to 'all users'), treat as convergent if the overlapping population segment is >= 50% of the smaller segment."

---

### Evidence Quality (0.72/1.00)

**Evidence:**
Source attribution is present on all major sections via HTML comment markers (lines 23, 52, 78, 97, 115, 127, 138, 152, 167, 181, 194). All citations trace to named SKILL.md sections. CI gate references (UX-CI-011, UX-CI-012, UX-CI-013) are verified as existing entries in `ci-checks.md` (confirmed by independent file read). The rationale column in the Sub-Skill Synthesis Output Map (lines 57-72) provides human-readable justification for each confidence assignment.

**Gaps:**
1. **Signal extraction thresholds lack external citations.** The criteria "severity >= 2 (out of 0-4 scale)" is attributed to Nielsen's heuristic scale in an inline comment (line 97) but Nielsen's Severity Rating for Usability Problems paper/standard is not cited by name. "Strength >= 3" for JTBD switch forces is attributed to "JTBD switch force scale" in the same comment but no source (Jobs-to-be-Done theory literature, Ulwick's Outcome-Driven Innovation, or similar) is cited. "5-8 respondents" for Kano directional classification is asserted without citation to Kano's original paper, Berger et al.'s 1993 quantification, or any accepted Kano sample size guidance. These are not internal framework claims — they are specific quantitative thresholds whose authority derives from external methodologies and must be traceable to those external sources.
2. **Confidence rationale column is descriptive, not evidential.** The rationale column entries (e.g., "Severity ratings involve subjective judgment; calibration across Nielsen's 10 heuristics requires consistent application context") explain WHY the confidence was chosen but do not cite evidence that this confidence level is calibrated against observed outcomes (e.g., "In practice, AI-generated severity ratings diverged from expert ratings by X in study Y"). For a C4 document governing AI judgment quality gates, the confidence assignments themselves are consequential claims that benefit from empirical grounding.
3. **No citation for P-022 interpretation.** P-022 is cited 4 times as the source of the confidence disclosure obligation, but no reference to the Jerry Constitution governing document path is provided. The rule file is consumed outside the SKILL.md context and a standalone reader cannot locate P-022 without the parent CLAUDE.md navigation table.

**Improvement Path:**
- Add inline citations for at least the three main signal extraction thresholds: Nielsen severity scale (cite Nielsen, J. 1994 or NNG source), JTBD switch force scale (cite Ulwick or Moesta), Kano sample size guidance (cite Berger et al. 1993 or accepted practice).
- Add a "Constitutional References" sub-section or a footer note: "P-022 (no deception about confidence): `docs/governance/TOM_CONSTITUTION.md`" for standalone traceability.
- For the confidence rationale column, consider adding "(evidence basis: [source])" to the highest-stakes LOW assignments (particularly AI-First Design and Design Token Consistency) where the rationale has the most impact on practitioner behavior.

---

### Actionability (0.90/1.00)

**Evidence:**
The Gate Enforcement Mechanisms (lines 37-39) are operationally specific: each gate produces a named, structurally defined section ("Synthesis Judgments Summary," "Validation Required," `[REFERENCE-ONLY]` tag). The Contradiction Presentation Format (lines 154-161) provides a 6-field mandatory structure with a sequential ID pattern (CONTRA-{NNN}) that an implementer can directly translate to output generation logic. The Synthesis Output Structure table (lines 170-177) defines required sections, content, and confidence level — fully implementable. The Required Traceability fields (lines 183-189) are atomic and unambiguous (4 fields, each with an example value).

**Gaps:**
1. The MEDIUM gate enforcement (line 38) specifies three validation source options: "(a) expert name and credentials, (b) user data reference, or (c) literature citation." The design recommendations are "withheld until at least one validation source is provided" — but the mechanism for how the orchestrator receives this validation source (user prompt input? structured field in a follow-up invocation? file reference?) is not specified. A practitioner implementing this gate does not know the interaction model for collecting the MEDIUM validation.
2. The output file naming convention references `{engagement-id}/ux-orchestrator-synthesis.md` (line 169) but the engagement ID format is not defined in this file. A cross-reference to the sibling rule that defines engagement IDs would make this immediately actionable without requiring the reader to hunt through sibling files.

**Improvement Path:**
- Add one sentence to the MEDIUM gate enforcement describing the interaction model: "The orchestrator presents a validation prompt to the user requesting one of the three validation sources; upon receipt, the orchestrator includes the validation reference in the output and re-generates the design recommendations section."
- Add a parenthetical reference: "engagement ID format defined in `skills/user-experience/rules/ux-routing-rules.md`" after `{engagement-id}` in the output path.

---

### Traceability (0.92/1.00)

**Evidence:**
All 7 major sections carry HTML comment source markers citing the specific SKILL.md section they derive from. The Cross-Framework Synthesis Protocol section headers cite "SKILL.md Section 'Cross-Framework Synthesis Protocol' — 4-step sequential mechanism" (line 78). The Convergence Matching Rules comment (lines 126-128) explicitly cites P-022 compliance rationale for the default-to-non-convergent rule. CI gate references (UX-CI-011/012/013) were verified against `ci-checks.md`. The footer (lines 212-218) provides complete sibling rule cross-references with exact relative paths. The document version, creation date, update date, and status are all present.

**Gaps:**
1. The Confidence Classification section's gate immutability rules (lines 43-45) cite `ux-routing-rules.md [Cross-Sub-Skill Handoff]` but the specific section name is not verified by the reader — a broken section anchor would not be detected. The citation format should include the section anchor explicitly: `ux-routing-rules.md#cross-sub-skill-handoff`.
2. The Synthesis Output Structure section (line 167) cites `ci-checks.md [Output Quality Checks]` for UX-CI-011 through UX-CI-013, but the section bracket name `[Output Quality Checks]` is a display label, not a verified anchor. If the ci-checks.md section is renamed, the cross-reference silently breaks.

**Improvement Path:**
- Convert all `[Section Name]` cross-references to `#anchor-slug` format for verifiability: `ux-routing-rules.md#cross-sub-skill-handoff`, `ci-checks.md#output-quality-checks`.
- These are minor link hygiene issues; the overall traceability chain is sound.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.72 | 0.85 | Add external citations for signal extraction thresholds (Nielsen severity scale, Kano sample size, JTBD switch force scale) and a constitutional reference footer for P-022. These are the highest-impact gaps: quantitative thresholds governing AI confidence gates are claims that require external grounding. |
| 2 | Internal Consistency | 0.85 | 0.93 | Resolve the sub-skill naming convention inconsistency (slash-command vs. agent name) by choosing one canonical form and adding a terminology note. Update Step 2 of the Mechanism table to reference the Convergence Thresholds sub-classification to prevent the apparent contradiction between SKILL.md's simplified description and the rule file's finer-grained table. |
| 3 | Methodological Rigor | 0.92 | 0.96 | Add signal extraction criteria rows for `/ux-design-sprint` and `/ux-ai-first-design`. These are the two sub-skills covered in the synthesis map that have no extraction criteria, creating a genuine execution gap. |
| 4 | Completeness | 0.90 | 0.95 | Add a brief "MCP Degraded Synthesis" failure mode summarizing the 2-3 key degraded-mode behaviors from `mcp-coordination.md` that affect synthesis quality. Add explanatory notes for the two Sub-Skill Synthesis Output Map entries added beyond SKILL.md scope. |
| 5 | Actionability | 0.90 | 0.95 | Specify the MEDIUM gate validation collection interaction model (how the orchestrator solicits the named validation source). Add engagement ID format reference in the output path definition. |
| 6 | Traceability | 0.92 | 0.96 | Convert `[Section Name]` cross-references to `#anchor-slug` format for verifiable link integrity. Low effort, eliminates silent breakage risk. |

---

## Leniency Bias Check
- [x] Each dimension scored independently before composite calculation
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Internal Consistency downgraded from 0.88 to 0.85 when the naming inconsistency scope was confirmed; Evidence Quality downgraded from 0.78 to 0.72 when the absence of external citations for quantitative thresholds was confirmed as a genuine gap for a C4 document)
- [x] C4 calibration applied: the 0.95 threshold for C4 is significantly higher than the standard 0.92; dimensions that would PASS at 0.92 standard may still be insufficient for C4
- [x] No dimension scored above 0.95 (highest is Methodological Rigor at 0.92, which has documented evidence and documented gaps)

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.879
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.72
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add external citations for signal extraction thresholds (Nielsen severity, Kano sample size, JTBD switch force scale) and P-022 constitutional reference footer"
  - "Resolve sub-skill naming inconsistency (slash-command vs. agent name) and update Step 2 Mechanism table to reference Convergence Thresholds sub-classification"
  - "Add signal extraction criteria rows for /ux-design-sprint and /ux-ai-first-design (currently absent, creating execution gap)"
  - "Add MCP Degraded Synthesis failure mode and explanatory notes for sub-skill map entries beyond SKILL.md scope"
  - "Specify MEDIUM gate validation collection interaction model; add engagement ID format reference"
  - "Convert [Section Name] cross-references to #anchor-slug format"
```
