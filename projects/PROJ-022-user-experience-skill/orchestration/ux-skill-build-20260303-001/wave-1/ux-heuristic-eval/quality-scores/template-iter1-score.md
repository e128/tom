# Quality Score Report: Heuristic Report Template (Iter 1)

## L0 Executive Summary

**Score:** 0.843/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness (0.72)

**One-line assessment:** The template is well-structured and evidence-aware but has a material structural mismatch with the parent rules file -- 5 of 9 required sections from `heuristic-evaluation-rules.md` are absent or renamed, and 3 template sections have no counterpart in the authoritative rules spec, blocking PASS at C4 threshold.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/templates/heuristic-report-template.md`
- **Deliverable Type:** Design (Fill-in-the-blank report template)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.843 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.72 | 0.144 | 5 of 9 required sections from rules file absent or renamed; 3 template sections have no rules counterpart |
| Internal Consistency | 0.20 | 0.83 | 0.166 | Section names and finding format internally consistent; but "Severity Justification" field in template conflicts with "Remediation" field name in agent def and rules |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | Severity scale, deduplication, HEART mapping, AI supplement conditional blocks all correctly represented |
| Evidence Quality | 0.15 | 0.87 | 0.131 | Evidence placeholders well-guided; citations in footer correct; HEART attribution present |
| Actionability | 0.15 | 0.90 | 0.135 | Fill-in guidance is clear for present sections; repeatable block pattern works; degraded-mode conditional comments are actionable |
| Traceability | 0.10 | 0.91 | 0.091 | Footer cites all three source documents; AI supplement disclosure traces to P-022; coverage note traces to rules |
| **TOTAL** | **1.00** | | **0.843** | |

---

## Detailed Dimension Analysis

### Completeness (0.72/1.00)

**Evidence:**

The template's navigation table declares 9 sections. The authoritative required section list in `heuristic-evaluation-rules.md` [Report Structure] also declares 9 sections, but with substantially different names and coverage:

| Rules File Required Section | Template Section | Status |
|-----------------------------|-----------------|--------|
| 1. Document Sections (nav table) | Document Sections | PRESENT |
| 2. Executive Summary (L0) | Executive Summary | PRESENT (renamed from "Evaluation Context" distinction) |
| 3. Evaluation Context (L1) | ABSENT | MISSING |
| 4. Findings by Heuristic (L1) | Findings by Severity | STRUCTURAL MISMATCH -- rules require findings organized by heuristic (H1-H10), template organizes by severity (0-4) |
| 5. Ranked Findings Summary (L1) | ABSENT | MISSING -- rules require a separate single summary table ranked by severity |
| 6. Remediation Roadmap (L1) | Recommendations | PARTIAL -- template has this section but omits the "Suggested Implementation Order" narrative required by rules |
| 7. Strategic Implications (L2) | ABSENT | MISSING -- rules require cross-product usability patterns, organizational UX maturity; this is an L2 section the template omits entirely |
| 8. Synthesis Judgments Summary | Synthesis Judgments Summary | PRESENT |
| 9. Handoff Data | Handoff Data | PRESENT |

**Template sections with no rules counterpart:**
- "Methodology" -- not in the 9-section required list (rules call it "Evaluation Context")
- "Heuristic Coverage Matrix" -- not in the 9-section required list (novel addition)
- "Limitations and Reliability" -- not in the 9-section required list (novel addition, though the content is required as part of single-evaluator disclosure)

**Summary of gaps:**
- MISSING: Evaluation Context (L1) section
- MISSING: Ranked Findings Summary (separate table)
- MISSING: Strategic Implications (L2) section
- STRUCTURAL MISMATCH: "Findings by Severity" vs. "Findings by Heuristic" (rules mandate H1-H10 organization; template uses severity-level organization)
- PARTIAL: Recommendations section exists but does not replicate the full remediation roadmap structure

**Critical note on Findings organization:** The rules file [Report Structure] section 4 states: "Organized by heuristic (H1 through H10, then AI-1 through AI-3 if applicable)." The template [Findings by Severity] organizes by severity level (4, 3, 2, 1, 0). The agent definition [Output Specification] shows "Findings by Heuristic (L1): Organized by heuristic H1-H10." The template's organization scheme directly contradicts both the rules file and the agent definition. This is the most significant completeness gap.

**Gaps:**
1. Evaluation Context (L1) section -- absent entirely
2. Ranked Findings Summary (L1) -- absent (no standalone summary table)
3. Strategic Implications (L2) -- absent (entire L2 content category missing from template)
4. Findings organized by severity instead of by heuristic (contradicts rules + agent def)
5. Self-review checklist from rules [Self-Review Checklist (S-010)] not templated

**Improvement Path:**
- Add "Evaluation Context" section between Methodology and Findings with the fields specified in rules #3 (product name, domain, target users, screens list, input modality, MCP status, evaluation scope, degraded mode disclosure)
- Rename "Findings by Severity" to "Findings by Heuristic" and reorganize so each heuristic (H1-H10) is a subsection, with findings nested within each
- Add "Ranked Findings Summary" section: single table with columns Finding ID, Heuristic, Severity, Screen/Flow, Brief Description, Effort
- Add "Strategic Implications" section for L2 cross-product patterns and organizational UX maturity
- Optionally retain "Findings by Severity" as a cross-reference table or fold it into "Ranked Findings Summary"

---

### Internal Consistency (0.83/1.00)

**Evidence:**

Most internal claims are consistent. The severity distribution table (0-4), the HEART categories (Happiness/Engagement/Adoption/Retention/Task success), and the AI supplement conditional comment blocks are all internally consistent throughout the template.

The handoff YAML block is consistent with the narrative fields in other sections -- `severity_distribution`, `heuristic_count`, `degraded_mode`, `handoff_findings_count` all match the template's own usage.

**Specific inconsistency found -- Finding field names:**

The template's repeatable finding block (line 110) uses the field name **"Severity Justification"**:
```
- **Severity Justification:** {{why this severity level -- reference to task impact, frequency, or workaround availability}}
```

The `heuristic-evaluation-rules.md` [Finding Documentation Rules] required fields use the field name **"Remediation"** as the fifth field (not "Severity Justification"). The agent definition [Finding Format] also uses "Remediation" as the fifth field. The template introduces "Severity Justification" as an extra field not declared in the canonical finding format AND renames "Remediation" while omitting it from within the heuristic-specific block.

Cross-checking: the template's **Recommendations section** (line 186-202) uses "Recommendation" as a column header, which is consistent with the rules. But the per-finding block uses "Severity Justification" instead of the canonically named "Remediation" field. This inconsistency means an agent following the template would produce findings that differ structurally from the format declared in the rules and agent definition.

**Second inconsistency -- Findings section header depth:**

The template shows each severity level as `### Severity N` (H3 level), but each individual finding also as `### Finding F-{NNN}` (H3 level) within the same section. This makes severity-level subsections and findings at the same heading depth, which prevents clean document navigation and contradicts the nested structure the rules file implies.

**Third inconsistency -- Heuristic Coverage Matrix not cross-referenced:**

The "Coverage note" at line 175 references `heuristic-evaluation-rules.md [Single-Evaluator Reliability]` as the source for the "3+ heuristics with zero findings" flag, which is correct. However, the Coverage Matrix section itself (line 153-175) has no equivalent in the rules file's required section list, and the template presents it as a peer section to required sections -- which could mislead the agent into treating it as required when the rules do not list it.

**Gaps:**
- "Severity Justification" field in finding block not in canonical format (rules + agent def use "Remediation")
- Heading depth collision between severity level headers and finding headers within Findings by Severity
- Heuristic Coverage Matrix implied as required but not in the rules section list

**Improvement Path:**
- Replace "Severity Justification" with "Remediation" in the finding block to match the canonical format
- Add "Severity Justification" as a sub-bullet under "Severity" (or a parenthetical hint) if severity rationale documentation is desired, rather than as a standalone required field
- Adjust heading levels so severity levels are H3 and individual findings are H4 within each severity, OR reorganize by heuristic (see Completeness)

---

### Methodological Rigor (0.88/1.00)

**Evidence:**

The template correctly models:
- Nielsen's 5-step workflow sequence (via the sections it includes: input collection implicit in Methodology scope, evaluation implied by finding blocks, severity rating via the 0-4 scale, deduplication implicit in the `Deduplication` judgment type row in Synthesis Judgments, ranking by severity in Findings by Severity)
- The severity 0-4 taxonomy with correct severity names (Usability catastrophe through Not a usability problem)
- AI supplement conditional inclusion (lines 64-67, 169-172) with correct P-022 disclosure
- Degraded mode conditional block with correct limitations enumeration (lines 78-82)
- Cross-framework handoff threshold (severity >= 2, line 261)
- HEART candidate category mapping in the handoff table (line 267)
- Single-evaluator reliability disclosure with correct 35% statistic citation and Nielsen (1994c) reference (line 229)
- Effort classification (Low/Medium/High) in per-finding block (line 112)

**Gap 1 -- Deduplication step not templated:**

The rules file [Deduplication Rules] defines Step 4 of the evaluation workflow as a distinct step. The template has no structural placeholder for the deduplication step output -- no section or comment that reminds the agent to consolidate duplicate findings before populating the severity-level blocks.

**Gap 2 -- Self-review checklist absent:**

The rules file [Self-Review Checklist (S-010)] defines a 10-item self-review checklist that the evaluator must verify before persisting the report. The template does not include this checklist, even as a commented block. Without it, the agent must load the rules file separately to perform self-review rather than having it embedded in the output template.

**Gap 3 -- Step ordering mismatch:**

The agent definition [Methodology, Step 5] specifies "Generate the evaluation report" as the final step, and the required report structure in the agent definition's `<output>` section shows findings organized by heuristic, then the ranked summary, then the remediation roadmap. The template's section order (Executive Summary → Methodology → Findings by Severity → Matrix → Recommendations → Synthesis Judgments → Limitations → Handoff) differs from the agent-defined order (Executive Summary → Evaluation Context → Findings by Heuristic → Ranked Findings Summary → Remediation Roadmap → Strategic Implications → Synthesis Judgments → Handoff Data).

**Improvement Path:**
- Add a commented deduplication reminder block before the Findings section (e.g., `<!-- DEDUPLICATION CHECK: Before populating findings, consolidate same-root-cause violations per heuristic-evaluation-rules.md [Deduplication Rules] -->`)
- Add the S-010 self-review checklist as a commented block at the end of the template
- Reorder sections to match the agent definition's canonical output structure

---

### Evidence Quality (0.87/1.00)

**Evidence:**

The template does a strong job guiding the agent toward evidence-based findings:

- The Evidence placeholder (line 109) uses `{{specific interface observation demonstrating the violation}}` -- this matches the rules file's [Evidence Quality Standard] requirement for observable interface artifacts
- The Severity Justification placeholder (line 110) asks for `{{why this severity level -- reference to task impact, frequency, or workaround availability}}` -- this correctly operationalizes the rating discipline from the rules
- The Coverage note (line 175) explicitly references the "3+ heuristics with zero findings" flag from the rules file -- correct source attribution
- The Limitations section (lines 225-256) cites Nielsen (1994c) for the 35% single-evaluator coverage statistic -- citation is correct and traceable
- The footer (lines 308) cites all three methodology sources: Nielsen (1994a, 1994b, 1994c, 2020), Amershi et al. (2019), Google PAIR (2019) -- all present and matching the rules file citations

**Gap 1 -- HEART framework citation missing from inline context:**

The template's handoff table (line 265-268) references HEART categories (Happiness, Engagement, Adoption, Retention, Task success) without any inline citation. The rules file cites "Rodden, Hutchinson, and Fu (2010)" for the HEART framework in the heuristic-to-HEART mapping note. The template's footer does not include this citation. An agent using the template would produce output citing HEART without the required attribution.

**Gap 2 -- AI supplement citations inconsistent with rules file:**

The template's Methodology section (line 62) uses a shorthand reference to AI-1, AI-2, AI-3 without inline citation. The AI supplement disclosure comment block (lines 65-67) mentions "Amershi et al. (2019) and Google PAIR (2019)" which matches the rules file. However, the template body does not include the full citation form used in the rules ("pair.withgoogle.com/guidebook (accessed 2026-03-04)"). This is minor but relevant at C4 scoring.

**Gaps:**
- HEART framework citation (Rodden, Hutchinson & Fu, 2010) absent from handoff section or footer
- AI supplement citation lacks the access date form present in the rules file

**Improvement Path:**
- Add HEART citation to the footer or as a note in the Handoff Data section
- Optionally add a citation comment in the AI supplement conditional block

---

### Actionability (0.90/1.00)

**Evidence:**

The template is strongly actionable for an agent filling it in:

- The `<!-- REPEATABLE BLOCK: FINDING START/END -->` pattern (lines 103, 113) is unambiguous and clear
- The `<!-- Add up to 5 top findings by severity -->` comment (line 48) gives a concrete limit
- The conditional inclusion comments (`<!-- Include this block ONLY when AI Product Flag = true -->`, lines 64, 169) clearly scope optional content
- The `<!-- If no severity N findings: -->` comment pattern (lines 100-101) gives explicit handling for empty sections
- Placeholder syntax `{{PLACEHOLDER}}` is consistent throughout (no mixing of `{placeholder}` and `{{placeholder}}` or other patterns)
- The YAML block (lines 272-302) uses consistent `{{PLACEHOLDER}}` syntax with inline type hints (`{{true | false}}`, `{{0.0-1.0}}`, `{{C1 | C2 | C3 | C4}}`) that eliminate ambiguity

**Gap 1 -- No guidance for finding ID sequencing when using the severity-level organization:**

The template organizes findings by severity level, but finding IDs must be assigned in ranked order (F-001 = highest severity) per the rules file [Finding Documentation Rules, Step 4]. An agent filling in the template might assign IDs sequentially within each severity level block rather than globally ranked. The template provides no comment reminding the agent that IDs are assigned after all findings are ranked, not as they are entered.

**Gap 2 -- No placeholder for "Evaluation Context" fields:**

Because the template omits the Evaluation Context section (see Completeness), there is no actionable placeholder for target users, evaluation scope, or MCP status in a dedicated L1 section. The Methodology section captures some of this (scope definition table at lines 71-76), but the handoff YAML omits target users entirely.

**Gap 3 -- "Suggested Implementation Order" placeholder is vague:**

Line 204 provides the prompt: `{{Brief paragraph describing the recommended sequence -- typically severity 4 first regardless of effort, then quick wins for momentum, then medium/high effort items by severity.}}` This is helpful but the hint embedded in the placeholder essentially prescribes the content, which may lead agents to produce boilerplate instead of engagement-specific sequencing reasoning.

**Improvement Path:**
- Add a comment before the first severity block: `<!-- IMPORTANT: Assign F-{NNN} IDs only after all findings are ranked by severity (Step 4 of evaluation workflow). Do not assign IDs as you document findings. -->`
- Either add the Evaluation Context section (fixing Completeness) or add target user and scope fields to the handoff YAML
- Reframe the "Suggested Implementation Order" placeholder to elicit reasoning rather than restating the default sequence

---

### Traceability (0.91/1.00)

**Evidence:**

The template demonstrates strong traceability in several areas:

- Header comments (lines 1-4) cite the source documents: `SKILL.md [Output Specification]`, `agent <output> section`, `heuristic-evaluation-rules.md [Report Structure]`
- Footer (lines 306-308) cites all three source documents with section references
- The Synthesis Judgments section explicitly cites `skills/user-experience/rules/synthesis-validation.md` (line 210) by path -- this is correct and specific
- The Coverage note (line 175) cites `heuristic-evaluation-rules.md [Single-Evaluator Reliability]` by name -- correct
- The AI supplement disclosure comment (lines 65-67) traces to P-022 by principle reference

**Gap 1 -- Engagement ID format not traced to a source:**

The Handoff YAML `engagement_id: {{ENGAGEMENT_ID}}` placeholder provides no hint that the format is `UX-{NNNN}`. The rules file, agent definition, and SKILL.md all state this format. The template comment block at line 8 shows `> **Engagement:** {{ENGAGEMENT_ID}}` without the format hint. This is a minor traceability gap since the format specification lives in the agent definition's input section.

**Gap 2 -- No reference to handoff-v2.schema.json:**

The SKILL.md [Cross-Framework Integration] and agent definition reference `docs/schemas/handoff-v2.schema.json` as the canonical handoff schema. The template's Handoff YAML block does not reference this schema, meaning the agent filling in the template has no reminder to validate against the schema. The handoff YAML fields in the template are substantially consistent with handoff-v2 (from_agent, to_agent, task, success_criteria, artifacts, key_findings, blockers, confidence, criticality are all present), but the template adds non-schema fields (total_findings, severity_distribution, heuristics_evaluated, screens_evaluated, degraded_mode, handoff_findings_count) without noting these are extensions.

**Gap 3 -- No traceability to ORCHESTRATION.yaml:**

The rules file (line 514) includes a traceability comment referencing the ORCHESTRATION.yaml. The template has no equivalent traceability reference to the orchestration plan that governs this sub-skill's build sequence.

**Improvement Path:**
- Add `UX-{NNNN}` format hint to the `{{ENGAGEMENT_ID}}` placeholder
- Add a comment in the Handoff YAML block referencing `docs/schemas/handoff-v2.schema.json` and noting which fields are extensions beyond the base schema
- Optionally add a traceability comment block at the template bottom matching the pattern used in the rules file

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.72 | 0.88 | **Reorganize findings structure:** Rename "Findings by Severity" to "Findings by Heuristic" with H1-H10 subsections (matching rules + agent def). Move severity-level grouping into "Ranked Findings Summary" as the single ranked table. This addresses the most significant structural mismatch. |
| 2 | Completeness | 0.72 | 0.88 | **Add three missing sections:** (a) "Evaluation Context" (L1) between Methodology and Findings -- with fields: product, target users, screens evaluated, input modality, MCP status, evaluation scope, degraded mode disclosure. (b) "Ranked Findings Summary" (L1) -- single table ranked by severity with columns: Finding ID, Heuristic, Severity, Screen/Flow, Brief Description, Effort. (c) "Strategic Implications" (L2) -- cross-product patterns, org UX maturity, design evolution placeholder. |
| 3 | Internal Consistency | 0.83 | 0.93 | **Fix finding field name conflict:** Replace `**Severity Justification:**` with `**Remediation:**` in the repeatable finding block (line 110) to match the canonical format in `heuristic-evaluation-rules.md` [Finding Documentation Rules] and the agent definition [Finding Format]. If severity rationale is desired, add it as a hint within the `**Severity:**` field placeholder rather than as a separate named field. |
| 4 | Completeness | 0.72 | 0.88 | **Add S-010 self-review checklist** as a commented block at the template end, replicating the 10-item checklist from `heuristic-evaluation-rules.md` [Self-Review Checklist]. This converts a required process step into a structural template element. |
| 5 | Evidence Quality | 0.87 | 0.94 | **Add HEART attribution** to the footer or as an inline citation in the Handoff Data section: `Rodden, K., Hutchinson, H., & Fu, X. (2010). "Measuring the User Experience on a Large Scale." CHI '10.` Also add a note in the Handoff YAML block that `from_agent`/`to_agent`/`task`/`success_criteria`/`artifacts`/`key_findings`/`blockers`/`confidence`/`criticality` fields follow `docs/schemas/handoff-v2.schema.json` and the remaining fields are ux-heuristic-eval extensions. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Completeness held at 0.72 despite template being well-structured in other respects)
- [x] First-draft calibration considered: this is iteration 1; composite 0.843 is within the 0.80-0.90 range typical for good first drafts
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] C4 threshold (0.95) applied, not C2 threshold (0.92) -- this explains why the template does not PASS despite being well-crafted

**Calibration note:** The 0.72 Completeness score is the primary drag. The section organization mismatch (by-severity vs. by-heuristic) and the three missing sections (Evaluation Context, Ranked Findings Summary, Strategic Implications) are objectively present gaps against the authoritative rules spec. These are not interpretation differences -- the rules file [Report Structure] explicitly lists all 9 required sections in explicit order, and three are absent from the template. Benefit of the doubt was not extended.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.843
threshold: 0.95
weakest_dimension: Completeness
weakest_score: 0.72
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Reorganize Findings section from by-severity to by-heuristic (H1-H10) to match rules file and agent definition"
  - "Add Evaluation Context (L1) section: product, target users, screens, input modality, MCP status, scope"
  - "Add Ranked Findings Summary (L1): single table all findings ranked by severity descending"
  - "Add Strategic Implications (L2): cross-product patterns, organizational UX maturity, design evolution"
  - "Fix finding field name: replace Severity Justification with Remediation to match canonical format"
  - "Add S-010 self-review checklist as commented block at template end"
  - "Add HEART citation (Rodden et al. 2010) to footer; annotate handoff YAML extensions vs. handoff-v2 schema fields"
```

---

*Score Report Version: 1.0.0*
*Scoring Agent: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-heuristic-eval/templates/heuristic-report-template.md`*
*Parent Artifacts Reviewed: `heuristic-evaluation-rules.md`, `ux-heuristic-evaluator.md`, `SKILL.md` (ux-heuristic-eval), `synthesis-validation.md`*
*Created: 2026-03-04*
