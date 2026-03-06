# Quality Score Report: HEART Metrics Sub-Skill SKILL.md

## L0 Executive Summary

**Score:** 0.887/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.80)

**One-line assessment:** A structurally complete, internally consistent Wave 2 sub-skill specification that closely mirrors the Wave 1 reference pattern, with minor gaps in frontmatter fields, one unverifiable claim, and evidence that could be strengthened with additional practitioner citations -- targeted revisions to frontmatter completeness, the AGENTS.md line-number claim, and secondary framework citations would move this to PASS.

---

## Scoring Context

- **Deliverable:** `skills/ux-heart-metrics/SKILL.md`
- **Deliverable Type:** Design (Sub-skill specification)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.887 |
| **Threshold** | 0.95 (C4 per scoring instructions; H-13 baseline is 0.92) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.88 | 0.176 | All 13 required sections present; frontmatter lacks `version`, `activation-keywords`, `allowed-tools`; agent table includes Tier/Mode columns; methodology stub clearly labeled |
| Internal Consistency | 0.20 | 0.94 | 0.188 | T2/Systematic/Sonnet consistent across SKILL.md and parent SKILL.md; confidence levels align with synthesis-validation.md; one minor AGENTS.md line-number claim unverifiable |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | 5-phase GSM workflow fully specified with inputs, outputs, and activities; HEART dimensions and selection guidelines grounded in Rodden 2010; planned-behavior labeling is methodologically honest |
| Evidence Quality | 0.15 | 0.80 | 0.120 | Primary CHI '10 citation present and correctly attributed; GSM secondary citation (Rodden 2015 Google Research Blog) present; no Koenig-Lewis or other NPS calibration source cited for Happiness dimension industry benchmarks; cross-framework integration sources cite routing rules file but the file is not cross-checked in this scoring pass |
| Actionability | 0.15 | 0.90 | 0.135 | Full output template with worked example (checkout UX-0055); three invocation options with Task code block; concrete metric specification fields (formula, data source, frequency, target, alert condition, baseline) |
| Traceability | 0.10 | 0.88 | 0.088 | References section covers agent files, parent skill, standards, methodology rules, project items, and HEART framework citations; AGENTS.md line-number claim ("line 309") is a point-in-time assertion that may drift; handoff schema acknowledged as not yet committed |
| **TOTAL** | **1.00** | | **0.887** | |

---

## Detailed Dimension Analysis

### Completeness (0.88/1.00)

**Evidence:**

The document contains all 13 sections required by `skill-standards.md` Body Structure table (rows 1-14, noting that rows 6-8 apply as "multi-agent" but the sub-skill is single-agent and the guidance says to include them for orchestrator-invoked agents with a registration note). All expected content categories are present:

- Navigation table (H-23/NAV-001): Present (lines 34-51), all 13 sections listed with anchor links.
- Triple-Lens audience table (H-26 via skill-standards.md): Present (lines 53-61).
- Purpose + Key Capabilities: Present (lines 64-88), including the AI-augmented caveat and deployment status note.
- When to Use / Do NOT Use: Present with routing table and trigger keyword table and negative conditions (lines 93-139).
- Available Agents table: Present with Tier, Mode, Model, Output Location columns (lines 143-151), matching parent SKILL.md row for `ux-heart-analyst` (T2, Systematic, Sonnet).
- Invoking an Agent (3 options): Present including Task code block with `jerry:ux-heart-analyst` subagent type (lines 154-218).
- P-003 Compliance with ASCII diagram: Present (lines 221-238).
- Methodology (5-phase): Present with theoretical foundations table and GSM process detail (lines 242-408).
- MCP Integration: Present with dependency matrix claim and Context7 usage (lines 411-439).
- Output Specification: Present with template and worked example (lines 441-571).
- Cross-Framework Integration: Present with upstream handoff contracts (lines 573-631).
- Synthesis Hypothesis Validation: Present with confidence gate table and validation source examples (lines 633-666).
- Constitutional Compliance table: Present (lines 669-678).
- Quick Reference: Present (lines 680-699).
- References: Present and comprehensive (lines 701-763).
- Footer version block: Present (lines 756-763).

**Gaps:**

1. **Frontmatter incompleteness (MEDIUM impact):** The YAML frontmatter contains only `name`, `description`, `model`, and `tools`. It is missing three Jerry-required fields from `skill-standards.md` [YAML Frontmatter]: `version` (semantic versioning), `allowed-tools` (comma-separated format per Jerry convention), and `activation-keywords`. The Wave 1 reference (ux-jtbd/SKILL.md) also lacks these fields, so this gap may be a systematic Wave 1-2 pattern rather than a deliberate omission. The parent SKILL.md includes all three (`version: "1.0.0"`, `allowed-tools`, `activation-keywords`). Sub-skill SKILL.md files should conform to the same standards.

2. **`heart-methodology-rules.md` referenced but not cross-checked:** The References section cites `skills/ux-heart-metrics/rules/heart-methodology-rules.md` (line 736). This file is not listed in the Glob output of skill files, suggesting it does not yet exist. This is unacknowledged in the SKILL.md body (unlike the agent stub, which is explicitly labeled as "currently a stub"). If the file does not exist, the reference is broken.

3. **Wave 2 entry criteria in SKILL.md body:** The When to Use section describes routing without noting that this sub-skill is only available after Wave 2 entry criteria are met. The parent SKILL.md and wave-progression.md govern this, but a user reading only this sub-skill SKILL.md may not realize the sub-skill requires wave gate passage. A brief note similar to "Available after Wave 2 criteria are met (see `skills/user-experience/SKILL.md` [Wave Architecture])" would complete this section.

**Improvement Path:**

Add `version`, `activation-keywords`, and `allowed-tools` to frontmatter (matching ux-jtbd pattern if that is the sub-skill standard). Acknowledge `heart-methodology-rules.md` as "planned -- not yet committed" in the References section or create a stub file. Add a wave availability note to When to Use.

---

### Internal Consistency (0.94/1.00)

**Evidence:**

Cross-referencing against parent SKILL.md and sibling files, all major claims are consistent:

- **Agent table (T2, Systematic, Sonnet):** Matches parent SKILL.md line 155 exactly: `ux-heart-analyst | HEART metrics framework specialist | T2 | Systematic | Sonnet | 2`.
- **P-003 ASCII diagram:** Correctly places `ux-heart-analyst` as `(T2, Systematic, Sonnet)` -- consistent with parent.
- **MCP dependency claim (no REQ MCPs, ENH Hotjar):** Consistent with `mcp-coordination.md` matrix row for `/ux-heart-metrics`: `-- | -- | -- | -- | ENH | --`. The claim "No REQ MCP dependencies" is verifiably accurate.
- **Context7 classification (Available):** Consistent with `mcp-coordination.md` [Context7 Usage] table which lists `ux-heart-analyst` as not in the explicit agent list but aligns with ENH-tier usage.
- **Synthesis confidence levels (MEDIUM for goal-metric, LOW for threshold):** Exactly match `synthesis-validation.md` [Sub-Skill Synthesis Output Map] rows for `/ux-heart-metrics` (lines 69-70).
- **Cross-framework integration sources:** Cross-Framework Integration section correctly cites `skills/user-experience/rules/ux-routing-rules.md` [Handoff Data Contracts] and `skills/user-experience/SKILL.md` [Cross-Sub-Skill Handoff Data].
- **CRISIS routing sequence:** "Heuristic Eval -> Behavior Design -> HEART" matches parent SKILL.md Lifecycle-Stage Routing CRISIS path.
- **Free cost tier claim:** Correctly states `ux-heart-metrics` is in the Free ($0) tier per `mcp-coordination.md` [Cost Tiers] which lists "HEART" under Free tier.
- **AGENTS.md line 309 claim:** The document states "The `ux-heart-analyst` agent IS registered in `AGENTS.md` under the User-Experience Skill Agents section (line 309), ensuring agent-level discoverability. Verified 2026-03-04." This is an internal consistency claim that cannot be fully verified without reading AGENTS.md. The sibling JTBD SKILL.md makes the same type of claim for line 307. These line numbers are fragile claims that can become incorrect as AGENTS.md evolves. The Wave 1 reference (ux-jtbd/SKILL.md) uses the same pattern, so this is a consistent sub-skill convention rather than a unique inconsistency.

**Gaps:**

1. The `subagent_type` in the Task code block uses `"jerry:ux-heart-analyst"` while the sibling ux-jtbd SKILL.md uses `"jerry:ux-jtbd-analyst"`. The jerry prefix is consistent, but it is unclear whether the runtime registry uses this prefix format or just the agent name. This is a minor consistency question rather than a documented contradiction.

2. The document says Context7 can be used for "Google HEART Framework" documentation (line 429). However, `mcp-coordination.md` [Context7 Usage] does not list `ux-heart-analyst` in the agent list for Context7 (lines 136-138 of mcp-coordination.md), only `ux-heuristic-evaluator`, `ux-atomic-architect`, `ux-inclusive-evaluator`, and `ux-ai-design-guide`. This is a minor internal inconsistency between the sub-skill's claimed Context7 usage and the parent's Context7 agent matrix.

**Improvement Path:**

Remove the AGENTS.md line number claim or replace it with a section name reference (e.g., "registered in AGENTS.md under the User-Experience Skill Agents section"). Add `ux-heart-analyst` to `mcp-coordination.md` Context7 agent table or clarify that Context7 usage for `ux-heart-analyst` is informal (via the general Context7 protocol, not the explicit agent matrix).

---

### Methodological Rigor (0.90/1.00)

**Evidence:**

The methodology section is the most substantive part of the document and demonstrates strong methodological rigor:

1. **Theoretical foundation table:** Both the HEART framework and GSM process are correctly attributed to Rodden, Hutchinson & Fu (2010) CHI '10, with distinct rows explaining their contribution to this sub-skill.

2. **HEART dimensions table:** Definitions and example signals are accurate and operationally useful. The "not all five apply to every context" caveat is methodologically important and present.

3. **Dimension selection guidelines:** Well-structured table with five independent selection considerations (product maturity, product type, feature vs. product, team capacity, available data). These are consistent with established HEART framework practitioner guidance.

4. **GSM process:** Three-step process (Goal -> Signal -> Metric) is correctly specified. Constraints on goals (user-centered, solution-agnostic) match Rodden's original intent. Leading vs. lagging signal distinction is present. Eight metric specification fields (name, dimension, formula, data source, frequency, target, alert condition, baseline) are complete and operationally grounded.

5. **5-phase workflow:** Phases are clearly sequenced with inputs, outputs, and activities. The "(planned -- target behavior)" label throughout is methodologically honest about the stub state. Phase 5 (Dashboard Specification) correctly includes the Synthesis Judgments Summary as a phase output.

6. **Worked example:** The checkout flow example (UX-0055) concretely demonstrates the metric specification format with realistic field values (Checkout Completion Rate formula, data source event names, daily frequency, 85% target, < 75% alert condition, 78% baseline).

**Gaps:**

1. **Signal identification depth:** Phase 3 (GSM Execution) specifies "Identify 2-4 signals per dimension" but the Methodology section's GSM process says "Select 2-4 signals per dimension." There is no guidance on the minimum/maximum ratio of metrics to signals (e.g., "one metric per signal" is stated but not explained -- what if a signal is not directly measurable?). The JTBD reference sub-skill has comparable methodology depth; this is not a gap relative to the Wave 1 reference but is a methodological completeness gap at the absolute rubric level.

2. **Threshold recommendation methodology:** Phase 4 describes how thresholds are set but relies on "industry benchmarks (when available -- cite source)" without specifying what to do when no benchmark exists and no baseline has been established. The LOW confidence labeling partially addresses this but a fallback methodology (e.g., "set target at 10% improvement over first 30-day measurement period") would complete the specification.

3. **Validation of goal uniqueness:** The specification states "Each HEART dimension has exactly one goal statement" but provides no methodology for what to do if two plausible goals exist for the same dimension. Adjudication guidance (e.g., "select the goal more directly tied to the feature scope") would strengthen rigor.

**Improvement Path:**

Add a brief decision rule for signal-to-metric ratio edge cases. Add a fallback threshold methodology for greenfield metrics. Add a goal adjudication tie-break rule for multiple plausible goals per dimension.

---

### Evidence Quality (0.80/1.00)

**Evidence:**

1. **Primary citation (HEART framework):** Correctly cited as Rodden, K., Hutchinson, H., & Fu, X. (2010). "Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications." Proceedings of CHI '10, ACM. This is the definitive source and the citation is accurate.

2. **Secondary GSM citation (Rodden 2015):** "Rodden, K. (2015). 'How to Choose the Right UX Metrics for Your Product.' Google Research Blog" is present. The Google Ventures Library version is also cited. These are valid practitioner-level sources.

3. **Synthesis confidence claims align with synthesis-validation.md:** The confidence classifications (MEDIUM for goal-metric mapping, LOW for threshold recommendations) cite `skills/user-experience/rules/synthesis-validation.md` [Sub-Skill Synthesis Output Map] and are verifiably correct against that source.

4. **Industry benchmark claim (checkout 85%):** The worked example uses "85% (industry benchmark for e-commerce)" as a threshold target without citing a specific study. The accompanying text notes "LOW confidence -- requires domain-specific calibration" which is appropriate, but the example presents the 85% figure in a way that readers may treat as authoritative. No Baymard Institute report or comparable source is cited.

**Gaps:**

1. **No calibration source for Happiness dimension NPS/satisfaction benchmarks:** The Happiness dimension description mentions "NPS score, satisfaction survey rating, sentiment in feedback" as signals, but the threshold recommendation methodology (Phase 4) does not provide any benchmark sources for these metrics. This is consistent with the LOW confidence labeling, but a reference to Reichheld (2003) for NPS or other established satisfaction benchmarking frameworks would strengthen evidence quality.

2. **Cross-framework integration handoff contracts cite ux-routing-rules.md but no content is verified:** The upstream handoff contracts (lines 580-586) cite "Source: `skills/user-experience/rules/ux-routing-rules.md` [Handoff Data Contracts]." This file was not in the provided cross-reference set, so the handoff contract fields (Finding ID, heuristic violated, severity 0-4, affected screen/flow, candidate HEART metric category) cannot be verified against their claimed source in this scoring pass.

3. **`heart-methodology-rules.md` referenced but not confirmed to exist:** The Methodology Rules reference (line 736-737) cites a file that is not present in the directory listing.

4. **No citation for dashboard specification best practices:** Phase 5 (Dashboard Specification) specifies visualization types (counter, time series, funnel) and drill-down patterns without citing any dashboarding standards or analytics platform guidance.

**Improvement Path:**

Add a benchmark citation to the worked example's 85% threshold (e.g., Baymard Institute cart abandonment data). Add a NPS calibration reference to the Happiness dimension. Confirm `heart-methodology-rules.md` exists or mark as planned. Add a brief citation to a dashboard design reference for Phase 5.

---

### Actionability (0.90/1.00)

**Evidence:**

The document is highly actionable in its primary function as a sub-skill specification:

1. **Three invocation options:** Natural language examples (6 example phrases), explicit agent request examples (3 examples), and a complete Task code block with all required fields populated.

2. **Output template:** Complete markdown template covering all required output sections (UX Context header, L0/L1/L2 structure, dimension selection table, GSM tables, metric specification table, dashboard specification, Synthesis Judgments Summary, Validation Required). The template uses clear placeholder syntax.

3. **Worked example:** Concrete checkout flow example (UX-0055) with populated rows across all template sections. The metric specification row shows a complete, realistic entry with actual event names (`checkout_completed`, `checkout_initiated`), realistic targets (>= 85%), and a realistic baseline with date range.

4. **Do NOT Use table:** Six rows with clear alternative routing and reasoning -- directly actionable for routing decisions.

5. **Common Workflows table:** Six common user needs mapped to concrete invocation phrases.

**Gaps:**

1. **No troubleshooting or failure mode guidance:** Unlike the parent SKILL.md which has a CRISIS routing path and the mcp-coordination.md which has degraded mode behavior, this SKILL.md does not address what happens when the analyst receives a product with no analytics infrastructure at all (the most common failure mode for tiny teams). Phase 1 identifies measurement maturity, but there is no guidance on minimum viable instrumentation or what to do if the team cannot instrument analytics.

2. **Threshold recommendation section is "planned" but the template includes it:** The worked example shows a threshold recommendation (85%) but Phase 4 is labeled "(planned -- target behavior)." A user reading only the template would not know that threshold recommendations are LOW confidence until they reach the Synthesis Hypothesis Validation section. A brief note in the Output Format Template's Target field placeholder would close this.

**Improvement Path:**

Add a "No analytics infrastructure" failure mode with a minimum viable measurement path. Add a `[LOW confidence -- see Synthesis Hypothesis Validation]` annotation to the Target Threshold field in the output template.

---

### Traceability (0.88/1.00)

**Evidence:**

The References section is comprehensive and correctly structured:

1. **Agent definition files:** Both `ux-heart-analyst.md` and `ux-heart-analyst.governance.yaml` with correct paths under `skills/ux-heart-metrics/agents/`.

2. **Parent skill references:** Six parent skill files listed with correct repo-relative paths -- all use `skills/user-experience/rules/` prefix as expected.

3. **Standards references:** All six referenced standards include the correct path, standard ID, and section anchor.

4. **Methodology rules:** `skills/ux-heart-metrics/rules/heart-methodology-rules.md` listed -- but the file does not exist in the directory listing (see Completeness gap 2).

5. **Project traceability:** PROJ-022 PLAN.md, EPIC-003, and ORCHESTRATION.yaml paths present.

6. **HEART framework citations:** Three citations covering primary (CHI '10), GSM practitioner (2015 blog), and practitioner guide (2015 Google Ventures). The CHI '10 citation is exact including proceedings title and publisher (ACM).

7. **H-26(c) exception rationale:** Explicitly documented with five sub-bullets explaining why independent registration is not required, satisfying the "full traceability for design decisions" expectation for a C4 deliverable.

**Gaps:**

1. **AGENTS.md line number is a point-in-time claim:** Line 309 is stated as "Verified 2026-03-04." This is a fragile traceability claim. As AGENTS.md evolves, this line number will drift. Best practice is to reference the section name rather than a line number.

2. **`docs/schemas/handoff-v2.schema.json` noted as "planned -- not yet committed":** This is acceptable given the explicit acknowledgment, but the Cross-Framework Integration section uses this schema for handoff contracts without noting the planned status at the point of use (the note appears only in the References section).

3. **ux-routing-rules.md handoff contract fields not independently verified:** The upstream handoff contracts for `/ux-lean-ux`, `/ux-heuristic-eval`, and `/ux-behavior-design` cite specific field names. These cannot be traced to the ux-routing-rules.md file in this scoring pass because that file was not included in the cross-reference set.

**Improvement Path:**

Replace AGENTS.md line number with section name reference. Move the `handoff-v2.schema.json` "planned" note to the point of use in Cross-Framework Integration. Reference ux-routing-rules.md in a cross-reference table at the point of handoff contract specification.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.80 | 0.88 | Add a benchmark citation for the 85% checkout completion threshold in the worked example (e.g., Baymard Institute). Add NPS calibration source to Happiness dimension. Confirm `heart-methodology-rules.md` exists or annotate as "planned -- not yet committed to repository." |
| 2 | Completeness | 0.88 | 0.93 | Add `version`, `activation-keywords`, and `allowed-tools` to YAML frontmatter. Add wave availability note to When to Use section. Acknowledge `heart-methodology-rules.md` as planned in the References table. |
| 3 | Traceability | 0.88 | 0.93 | Replace "line 309" AGENTS.md reference with section name ("User-Experience Skill Agents section"). Move the handoff schema "planned" note to the Cross-Framework Integration section at point of use. |
| 4 | Internal Consistency | 0.94 | 0.96 | Add `ux-heart-analyst` to `mcp-coordination.md` Context7 agent table to align with the Context7 usage claim in MCP Integration. Remove or generalize the AGENTS.md line-number claim. |
| 5 | Actionability | 0.90 | 0.93 | Add a "No analytics infrastructure" failure mode with minimum viable instrumentation guidance. Add LOW confidence annotation to the Target Threshold placeholder in the output template. |
| 6 | Methodological Rigor | 0.90 | 0.93 | Add a fallback threshold methodology for greenfield metrics where no baseline exists and no benchmark applies. Add goal adjudication guidance for multiple plausible goals per HEART dimension. |

---

## Leniency Bias Check

- [x] Each dimension scored independently
- [x] Evidence documented for each score: specific lines, cross-referenced file locations, and specific claims cited for each score
- [x] Uncertain scores resolved downward: Evidence Quality at 0.80 (not 0.85) because the worked-example benchmark is uncited; Completeness at 0.88 (not 0.90) because of the frontmatter gap and unconfirmed file reference
- [x] First-draft calibration considered: This is v1.0.0; the document closely mirrors a Wave 1 reference pattern and exhibits strong structural quality, placing it in the 0.85-0.92 band appropriate for a well-executed first draft at C4
- [x] No dimension scored above 0.95 without exceptional evidence: Internal Consistency at 0.94 is the highest dimension; the marginal inconsistency between Context7 usage claim and mcp-coordination.md agent matrix prevents 0.95+

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.887
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.80
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add benchmark citation for 85% checkout threshold (Baymard Institute or equivalent). Add NPS calibration source for Happiness dimension. Confirm heart-methodology-rules.md existence or annotate as planned."
  - "Add version, activation-keywords, and allowed-tools to YAML frontmatter. Add wave availability note to When to Use section."
  - "Replace AGENTS.md line-309 reference with section name. Move handoff schema planned note to point of use in Cross-Framework Integration."
  - "Add ux-heart-analyst to mcp-coordination.md Context7 agent table to align with sub-skill MCP Integration claim."
  - "Add no-analytics-infrastructure failure mode guidance. Add LOW confidence annotation to Target Threshold placeholder in output template."
  - "Add fallback threshold methodology for greenfield metrics. Add goal adjudication guidance for multiple plausible goals per HEART dimension."
```

---

*Quality Score Report*
*Deliverable: `skills/ux-heart-metrics/SKILL.md`*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Iteration: 1*
*Created: 2026-03-04*
