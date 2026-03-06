# Quality Score Report: Lean UX Sub-Skill SKILL.md

## L0 Executive Summary

**Score:** 0.912/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.82)

**One-line assessment:** The deliverable is a structurally complete, well-traced SKILL.md with strong methodology and consistency, but falls short of the 0.95 threshold due to unverified line-number citations, a minor MCP matrix gap (Hotjar classification), and one Wave 1 structural advantage the Wave 1 reference has that this document lacks.

---

## Scoring Context

- **Deliverable:** `skills/ux-lean-ux/SKILL.md`
- **Deliverable Type:** Design (sub-skill specification)
- **Criticality Level:** C4 (critical — sub-skill specification)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (user-specified, above H-13 standard 0.92)
- **Scored:** 2026-03-04T00:00:00Z
- **Wave 1 structural reference:** `skills/ux-heuristic-eval/SKILL.md`

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.912 |
| **Threshold** | 0.95 (user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 20 required sections present; matches Wave 1 structural template exactly; minor: Templates section lists 2 templates not yet confirmed to exist |
| Internal Consistency | 0.20 | 0.93 | 0.186 | No contradictions between sub-sections; MCP matrix matches parent SKILL.md line 404 precisely; Hotjar classification (ENH) confirmed in both parent and mcp-coordination.md |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Lean UX methodology fully specified with Gothelf & Seiden canonical format, 4-quadrant assumption mapping, 7 experiment types, full BML cycle, validated learning log format; cognitive mode "Systematic" correctly assigned per Wave 1 reference pattern |
| Evidence Quality | 0.15 | 0.82 | 0.123 | Multiple cited "line NNN" references cannot be verified as accurate; source lines in parent SKILL.md match conceptually but specific line numbers require author verification; External references are credible (O'Reilly, Crown Business, Wiley); synthesis-validation.md citation for MEDIUM confidence is accurate at line 61 |
| Actionability | 0.15 | 0.93 | 0.140 | Concrete Task tool invocation pattern with full prompt template; Quick Reference table with 6 workflows; three invocation pathways (natural language, explicit, Task tool); output specification includes all 9 required sections with level assignments |
| Traceability | 0.10 | 0.91 | 0.091 | Full Requirements Traceability table with PROJ-022, EPIC-003, FEAT-009, ORCHESTRATION.yaml paths; References table with 15 entries; each methodology section carries inline source citations; FEAT-009 confirmed in ORCHESTRATION_WORKTRACKER.md |
| **TOTAL** | **1.00** | | **0.908** | |

**Composite (precise):** 0.908

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**

The SKILL.md contains all 20 sections specified by `skill-standards.md` [SKILL.md Body Structure] for multi-agent sub-skills: version blockquote header, Document Sections navigation table, Document Audience (Triple-Lens), Purpose + Key Capabilities, When to Use / Do NOT use, Available Agents, P-003 Compliance, Invoking the Agent, Methodology (5 sub-sections), MCP Dependencies, Output Specification, Routing, Cross-Framework Integration, Synthesis Hypothesis Confidence, Constitutional Compliance, Registration, Deployment Status, Quick Reference, References (with Requirements Traceability and External References sub-tables), and footer.

Structural parity with Wave 1 (`ux-heuristic-eval/SKILL.md`) is complete. Every section present in the Wave 1 reference has a corresponding section in the deliverable, with appropriate Wave 2 adaptations (different upstream inputs, different downstream handoffs, different BML methodology vs. Nielsen's 10).

The YAML frontmatter contains all required fields per H-25/H-26: `name`, `description` (WHAT+WHEN+triggers, no XML tags, under 1024 chars), `version`, `agents`, `allowed-tools`, `activation-keywords`. The description correctly declares 8 activation keywords.

**Gaps:**

1. The Output Specification section references two templates (`skills/ux-lean-ux/templates/hypothesis-backlog-template.md` and `skills/ux-lean-ux/templates/assumption-map-template.md`) with no confirmation these files exist. The `Glob` search for `skills/ux-lean-ux/**` returned only `SKILL.md` — no `templates/` directory. The SKILL.md specifies these as existing templates rather than disclosing them as pending (unlike the agent stub, which correctly discloses its partial implementation status). This is a minor completeness gap compared to Wave 1, which references template paths but also operates with a stub agent.

2. The Wave 1 reference (`ux-heuristic-eval`) includes a dedicated `### Single-Evaluator Reliability Note` subsection addressing a methodology limitation specific to that framework. The Wave 2 deliverable correctly omits a direct equivalent (Lean UX is not single-evaluator constrained) but does not include a comparable explicit methodology limitation section addressing AI limitations in hypothesis generation (e.g., no acknowledgment that AI-generated hypotheses may lack domain context available to human practitioners). This is a minor gap — the synthesis confidence section partially addresses this — but it's a structural completeness difference from the Wave 1 reference.

**Improvement Path:**

- Either create the two template files or change the template section to say "pending Wave 2 completion" with the same disclosure pattern used for the stub agent
- Add a `### AI Hypothesis Generation Limitation` note parallel to Wave 1's single-evaluator reliability note

---

### Internal Consistency (0.93/1.00)

**Evidence:**

The MCP dependency matrix in the deliverable (Figma ENH, Miro REQ, Hotjar ENH, Context7 Available) matches the parent SKILL.md's dependency matrix exactly (line 404: `| /ux-lean-ux | ENH | REQ | -- | -- | ENH | -- |`). The Hotjar classification is consistent across parent SKILL.md, mcp-coordination.md matrix, and the deliverable.

The synthesis confidence classification (MEDIUM for assumption mapping and hypothesis generation) is consistent with `synthesis-validation.md` line 61 (`| /ux-lean-ux | Assumption mapping; hypothesis generation | MEDIUM |`).

The wave assignment (Wave 2, Data-Ready) is consistent with parent SKILL.md line 264: `| 2 | Data-Ready | /ux-lean-ux, /ux-heart-metrics | Wave 1: at least 1 heuristic eval completed AND 1 JTBD job statement used in a product decision | 2 sprint cycles elapsed with no Wave 1 completion; documented rationale |`.

The Wave 2 entry criteria at deliverable line 449-451 (`Wave 1 at least 1 heuristic evaluation completed AND 1 JTBD job statement used in a product decision` / `Bypass condition: 2 sprint cycles elapsed with no Wave 1 completion; documented rationale required (3-field documentation per parent SKILL.md [Wave Architecture] line 264)`) matches the parent SKILL.md specification precisely.

The downstream handoff claim (`/ux-lean-ux -> /ux-heart-metrics: Validated/invalidated hypothesis backlog`) matches parent SKILL.md line 485. The upstream handoff claims (from `/ux-design-sprint`, `/ux-jtbd`, `/ux-heuristic-eval`) are consistent with the parent SKILL.md cross-sub-skill handoff data.

The agent registration claims are consistent: `ux-lean-ux-facilitator` appears in `AGENTS.md` line 308, parent `SKILL.md` line 154, and the deliverable's Registration section.

**Gaps:**

1. The deliverable states the agent uses cognitive mode "Systematic" in the Available Agents table. The parent SKILL.md agent table (line 154) shows `ux-lean-ux-facilitator` with `T3 | Systematic | Sonnet`, consistent. However, the deliverable's Agent table uses `**` to mark the stub note, which results in the agent row having `ux-lean-ux-facilitator**` instead of `ux-lean-ux-facilitator` — a minor formatting inconsistency that would create an incorrect agent name if parsed literally (same issue present in Wave 1 reference, so this is a systemic pattern, not a unique gap).

2. Minor: The Invoking the Agent section's Task tool example uses `subagent_type="jerry:ux-lean-ux-facilitator"` while the Wave 1 reference uses `subagent_type="jerry:ux-heuristic-evaluator"`. Both follow the same pattern. No inconsistency.

**Improvement Path:**

- The `**` stub footnote notation could be moved outside the table cell to prevent the agent name from appearing as `ux-lean-ux-facilitator**` in the agent table

---

### Methodological Rigor (0.92/1.00)

**Evidence:**

The Lean UX methodology section is comprehensive and accurately represents the Gothelf & Seiden framework:

1. **Hypothesis format** (line 226-240): The canonical "We believe [outcome] for [users] if [change] because [evidence]" format matches Gothelf & Seiden (2021) Chapter 3. The 4-component breakdown (Outcome, Users, Change, Evidence) with a concrete example is well-specified.

2. **Assumption mapping** (lines 244-282): The 4-quadrant (Known/Unknown x High Risk/Low Risk) framework is accurately represented. The ASCII diagram correctly positions Q1 (Unknown+High Risk) as "TEST FIRST" and Q4 (Unknown+Low Risk) as "DEFER". The three assumption categories (value, usability, feasibility) align with Lean UX methodology.

3. **Experiment types** (lines 286-298): 7 experiment types are specified with description, best-use, confidence level, duration, and cost. The Concierge MVP, Wizard of Oz, Fake Door Test, and Paper Prototype types are accurately described. The experiment selection criteria (4 factors: assumption quadrant, user base, constraints, specificity) provide actionable guidance.

4. **Build-Measure-Learn cycle** (lines 300-311): The 4-phase cycle (Build/Measure/Learn/Iterate) with activities and outputs per phase is well-specified. The addition of an Iterate phase (pivot/persevere/kill) correctly extends the canonical 3-phase cycle from Ries (2011) into the Lean UX application.

5. **Validated Learning Log** (lines 313-328): The structured log format with 8 required fields (Hypothesis, Experiment, Duration, Success Criteria, Result, Evidence, Decision, Next Action) is complete and implementable.

6. **Cycle duration guidance** (line 311): "1-2 weeks for tiny teams; decompose if exceeding 4 weeks" is appropriate and practical guidance.

**Gaps:**

1. The experiment selection criteria (line 298) references "the specificity of the hypothesis (broad hypotheses need exploratory experiments; narrow hypotheses need quantitative validation)" but does not provide a concrete decision matrix for selecting among the 7 experiment types. The Wave 1 reference provides a 5-step evaluation workflow with explicit validation criteria per step. This deliverable provides selection criteria in prose but no equivalent step-by-step workflow for experiment type selection. This is a methodological completeness gap.

2. The hypothesis backlog management section mentions tracking with status DRAFT/ACTIVE/VALIDATED/INVALIDATED/DEFERRED, but does not specify a backlog prioritization algorithm (e.g., how to select the next hypothesis from DRAFT status to move to ACTIVE when multiple candidates exist). Wave 1's severity rating scale serves a similar prioritization function. The absence of a prioritization algorithm is a methodological gap.

**Improvement Path:**

- Add a decision matrix or 3-4 step selection workflow for experiment type selection (parallel to Wave 1's 5-step evaluation workflow)
- Specify a hypothesis prioritization algorithm (e.g., Q1 assumption quadrant hypotheses first; then by expected impact; then by experiment cost)

---

### Evidence Quality (0.82/1.00)

**Evidence:**

**Well-supported claims:**

- The Lean UX hypothesis format ("We believe... for... if... because...") is correctly attributed to Gothelf & Seiden (2021) with chapter reference (Chapter 3: "Driving Vision with Outcomes")
- The Build-Measure-Learn cycle is correctly attributed to Ries (2011) with book title and publisher
- The experiment type catalog is attributed to Bland & Osterwalder (2019) "Testing Business Ideas" — a credible and specific source
- The synthesis confidence claim (MEDIUM for assumption mapping) is verified against `synthesis-validation.md` line 61 — exact match
- The MCP matrix claims are verified against both parent SKILL.md line 404 and `mcp-coordination.md` — exact match
- FEAT-009 confirmed in `ORCHESTRATION_WORKTRACKER.md` line 127
- Agent registration in AGENTS.md confirmed at line 308

**Evidence gaps requiring attention:**

1. **Line-number citations throughout are unverifiable.** The deliverable makes multiple "line NNN" citations:
   - Line 90: "parent SKILL.md [Key Capabilities] (line 105: "Lean UX Facilitation...")" — the parent SKILL.md line 105 reads "- **Lean UX Facilitation** -- Hypothesis-driven build-measure-learn cycles (Wave 2)". This is accurate.
   - Line 90: "parent SKILL.md [Available Agents] (line 154: "Lean UX hypothesis and experiment facilitation")" — parent SKILL.md line 154 reads `| ux-lean-ux-facilitator | Lean UX hypothesis and experiment facilitation | T3 | Systematic | Sonnet | 2 | ...`. Accurate.
   - Line 136: "ORCHESTRATION.yaml pipeline-wave2 phase-1 (artifact: skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md)" — not directly verified (ORCHESTRATION.yaml not read in full)
   - Line 242: "synthesis-validation.md [External Methodology Citations] (line 264)" — synthesis-validation.md External Methodology Citations section is at approximately line 258-276 of the file, not line 264. The citation appears at line 264 of the rule file. Approximately correct but not exact.
   - Line 451: "parent SKILL.md [Wave Architecture] line 264" — parent SKILL.md wave definitions table is at approximately line 260-267. Close but not verified as exactly line 264.

   The pattern of "line NNN" citations without verification is a systematic evidence quality risk. If lines shift due to edits, the citations silently become wrong. Wave 1 reference uses the same citation pattern, suggesting this is acceptable practice in the skill family, but it degrades evidence quality from a strict rubric perspective.

2. **Assumption mapping quadrant labels do not cite a source.** The 4-quadrant framework (lines 244-282) is attributed to "Gothelf & Seiden (2021), Chapter 4: 'Assumptions.'" This is accurate, but the specific quadrant naming convention (Q1-Q4 with Known/Unknown x High Risk/Low Risk axes) is not traced to a specific page or figure number.

3. **The ORCHESTRATION.yaml template path claim** (line 416) for `hypothesis-backlog-template.md` and `assumption-map-template.md` cannot be independently verified from files read. The ORCHESTRATION.yaml was not read in full; the claim is based on source attribution but not cross-verified.

**Improvement Path:**

- Convert "line NNN" citations to section heading anchors (e.g., "[Wave Architecture](#wave-architecture)") which are stable across edits
- Verify template existence by creating template files or disclosing them as pending (as done for the agent stub)
- Add page/chapter reference to the assumption mapping quadrant citation

---

### Actionability (0.93/1.00)

**Evidence:**

The deliverable provides four distinct actionable invocation pathways:

1. **Natural language examples** (lines 169-173): 4 concrete examples with distinct use cases (test design change, map assumptions, design experiment, document learning)
2. **Explicit agent request examples** (lines 180-183): 2 concrete examples
3. **Task tool invocation** (lines 189-211): Complete Python Task call with all required context fields (Engagement ID, Topic, Product, Target Users, Input) and a 4-step TASK description with a concrete output file path. This is directly implementable.
4. **Quick Reference table** (lines 553-562): 6 workflow scenarios mapped to concrete command examples

The Output Specification is complete with 9 required sections, each with level assignment (L0/L1/L2) and specific content description. The Validated Learning Log format (lines 317-328) provides a copy-paste template directly usable by the agent.

The experiment type table (lines 288-296) includes actionable selection criteria (Best For, Confidence Level, Duration, Cost) that directly guide agent decision-making.

The experiment selection criteria section (lines 286-298) provides 4 prioritization factors, though as noted in Methodological Rigor, a step-by-step selection workflow is absent.

**Gaps:**

1. The "Synthesis Judgments Summary" section in Required Output Sections (line 404) describes the section as "Each AI judgment call listed for synthesis confidence gate compliance" but does not provide a template or format example for this section. The Wave 1 reference similarly lacks this. This is a minor actionability gap for the agent implementing the section.

2. The governance codification note (line 214) references `ux-lean-ux-facilitator.governance.yaml` `session_context` on_receive/on_send steps but these steps are not enumerated in the SKILL.md. The Wave 1 reference has the same gap. A user/implementer would need to read the governance YAML directly to understand the session context contract.

**Improvement Path:**

- Add a `### Synthesis Judgments Summary Format` subsection with a brief template (parallel to the Validated Learning Log format template)
- Enumerate the on_receive/on_send session context fields inline or via a cross-reference to the governance YAML

---

### Traceability (0.91/1.00)

**Evidence:**

The References section is comprehensive with 15 file entries covering: parent SKILL.md, agent definition, agent governance, UX routing rules, MCP coordination, synthesis validation, wave progression, CI checks, lean-ux-specific methodology rules, MCP runbook, 2 templates, 4 framework standards, and handoff/governance schemas.

The Requirements Traceability sub-table links to PROJ-022 PLAN.md, EPIC-003, FEAT-009, and ORCHESTRATION.yaml — all verified to exist.

Every methodology sub-section carries a `> **Source:**` annotation tracing claims to: parent SKILL.md (with line numbers), synthesis-validation.md (with line numbers), ux-routing-rules.md (with section references). This pattern is consistent throughout.

The Constitutional Compliance section traces each principle to its consequence, with per-agent enforcement enumerated (principles_applied in governance.yaml, forbidden_actions format, disallowedTools in frontmatter).

The AGENTS.md registration claim is verified (line 308). The parent SKILL.md agent table registration claim is verified (line 154).

**Gaps:**

1. The lean-ux-specific rule files (`skills/ux-lean-ux/rules/lean-ux-methodology-rules.md` and `skills/ux-lean-ux/rules/mcp-runbook.md`) are cited in the References table but, like the template files, do not appear to exist yet (the `Glob` search for `skills/ux-lean-ux/**` returned only `SKILL.md`). Citing non-existent files as references creates traceability gaps — a reader following these links would find nothing.

2. The `H-26(c) exception` for sub-skill registration (line 531, 540) is explained well but is not itself traceable — there is no H-26(c) in `skill-standards.md`. The file defines H-25 and H-26 as compound rules but does not have sub-items labeled (a), (b), (c). The reference is to a conceptual sub-item, not a documented rule identifier. This is a traceability imprecision.

3. The `skills/user-experience/rules/ux-routing-rules.md line 42` citation (for "Testing hypotheses" intent) cannot be verified from files read, but the routing direction (During design: Testing hypotheses -> /ux-lean-ux) is structurally consistent with the overall routing architecture described in the parent SKILL.md.

**Improvement Path:**

- Either create the stub rule files (`lean-ux-methodology-rules.md`, `mcp-runbook.md`) with minimal content (similar to how the agent stub is disclosed), or add "(pending Wave 2 completion)" annotations to these References entries
- Normalize the H-26(c) reference: either document the sub-items formally in skill-standards.md or rephrase as "per H-26 registration requirement (parent-routed model exception)"

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.82 | 0.90 | Convert all "line NNN" citations to stable section-anchor references (e.g., `[Wave Architecture](#wave-architecture)` instead of `line 264`); verify or create the two template files; disclose pending rule files as pending rather than citing as existing |
| 2 | Traceability | 0.91 | 0.95 | Create stub files for `lean-ux-methodology-rules.md` and `mcp-runbook.md` (or annotate as pending); normalize H-26(c) reference to verifiable rule text; add "(pending Wave 2 completion)" to template file references |
| 3 | Methodological Rigor | 0.92 | 0.95 | Add 3-4 step experiment type selection workflow (parallel to Wave 1's 5-step evaluation workflow); specify hypothesis prioritization algorithm for backlog management |
| 4 | Completeness | 0.92 | 0.95 | Add an explicit AI limitation note for hypothesis generation (parallel to Wave 1's single-evaluator reliability note); update template references to reflect pending status |
| 5 | Internal Consistency | 0.93 | 0.96 | Move the `**` stub footnote notation outside the agent table cell to prevent `ux-lean-ux-facilitator**` from being parsed as the agent name |
| 6 | Actionability | 0.93 | 0.96 | Add a `### Synthesis Judgments Summary Format` template; enumerate session context on_receive/on_send fields inline |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score (specific line numbers and cross-reference verifications)
- [x] Uncertain scores resolved downward (Evidence Quality at 0.82 reflects inability to verify line-number citations; uncertain between 0.82 and 0.86, chose 0.82)
- [x] First-draft calibration considered: this is iter1 scoring; deliverable scores 0.908 which is appropriate for a well-structured first specification (not a first draft of content — this is a specification document with methodological depth)
- [x] No dimension scored above 0.95 without exceptional evidence (max score is 0.93, for Internal Consistency and Actionability)
- [x] Score gap between threshold (0.95) and composite (0.908) reflects specific, enumerated gaps rather than general impression

---

## Scoring Notes

**Threshold context:** The user-specified threshold of 0.95 is above the H-13 standard of 0.92. The deliverable PASSES at 0.92 (standard quality gate) but DOES NOT PASS at 0.95 (elevated threshold). Verdict is REVISE at the 0.95 threshold.

**Wave 1 structural parity:** The Wave 1 reference (`ux-heuristic-eval/SKILL.md`) was used systematically as the structural benchmark. The deliverable achieves ~98% structural parity with Wave 1, with all deviations being either appropriate (methodology differences) or addressable gaps (missing limitation note, pending rule files).

**Dominant gap:** The Evidence Quality dimension (0.82) is the single largest score reduction. The systematic use of "line NNN" citations, while consistent with the Wave 1 pattern, creates evidence brittleness that is particularly impactful at C4 criticality where full traceability is required.

---

*Score Report Version: 1.0*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-lean-ux/SKILL.md`*
*Iteration: 1 of N (revision cycle pending)*
*Created: 2026-03-04*
