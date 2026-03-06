# Quality Score Report: Behavior Design Sub-Skill SKILL.md

## L0 Executive Summary

**Score:** 0.897/1.00 | **Verdict:** REVISE | **Weakest Dimensions:** Completeness (0.87) and Evidence Quality (0.87)
**One-line assessment:** The SKILL.md is a well-structured, methodologically sound sub-skill specification that falls short of the C4 0.95 threshold — and even the standard H-13 0.92 threshold — due to two absent operational artifacts (template, agent file), missing DOIs on the primary academic citation, and forward references to partially-implemented rule file sections; targeted additions in these three areas will close the gap.

---

## Scoring Context

- **Deliverable:** `skills/ux-behavior-design/SKILL.md`
- **Deliverable Type:** Skill Definition (sub-skill specification)
- **Criticality Level:** C4 (PROJ-022 UX skill build, Wave 4)
- **Quality Threshold:** 0.95 (C4 strict, user-specified)
- **Standard H-13 Threshold:** 0.92 (C2+)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Comparison Baseline:** `skills/user-experience/SKILL.md` (parent skill sub-skill pattern)
- **Scored:** 2026-03-04T00:00:00Z
- **Strategy Findings Incorporated:** No

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.897 |
| **H-13 Threshold** | 0.92 |
| **C4 Strict Threshold** | 0.95 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.87 | 0.174 | All 20 sections present and substantive; two absent operational artifacts (template PLANNED, agent PLANNED) reduce score |
| Internal Consistency | 0.20 | 0.92 | 0.184 | Agent tier, model, wave, output path, synthesis confidence classifications consistent across sub-skill and parent SKILL.md; no contradictions found |
| Methodological Rigor | 0.20 | 0.91 | 0.182 | Six simplicity factors, three motivator pairs, three prompt types, bottleneck algorithm all match Fogg (2009/2020); B=MAP formula notation slightly imprecise |
| Evidence Quality | 0.15 | 0.87 | 0.131 | Full bibliographic detail in References table; DOIs absent from Fogg (2009) conference paper; behaviormodel.org URL present but no access date |
| Actionability | 0.15 | 0.92 | 0.138 | 5-phase execution procedure with numbered activities; bottleneck algorithm with decision criteria; Task tool invocation example with complete prompt; on_receive/on_send field tables |
| Traceability | 0.10 | 0.88 | 0.088 | Explicit paths to all rule files, project governance, handoff schema; forward references to partially-implemented ux-routing-rules.md sections reduce score |
| **TOTAL** | **1.00** | | **0.897** | |

---

## Detailed Dimension Analysis

### Completeness (0.87/1.00)

**Evidence for sections present:**
All required sub-skill SKILL.md sections are present and substantively populated. Compared against the parent `skills/user-experience/SKILL.md` sub-skill pattern:

| Required Element | Present | Evidence |
|-----------------|---------|---------|
| Available Agents table | YES | Lines 131-143: agent name, role, tier, mode, model, output location |
| Wave Architecture section | YES | Lines 630-641: Wave 4 entry criteria, bypass condition, Wave 5 transition criteria |
| Synthesis Hypothesis Confidence | YES | Lines 554-567: MEDIUM for bottleneck diagnosis, LOW for interventions, with rationale |
| CI gates | PARTIAL | Lines 161-163: "CI gate validates no sub-skill agent has Task access (documented in `skills/user-experience/rules/ci-checks.md`)" — referenced but not enumerated in-document |
| Degraded Mode Behavior | YES | Lines 595-627: three degraded scenarios (no data, no heuristic eval, no screenshots) with impact and mitigation tables |
| P-003 Compliance | YES | Lines 146-164: worker-only hierarchy diagram with enforcement details |
| Cross-Framework Integration | YES | Lines 501-551: upstream inputs (heuristic eval) and downstream handoff (HEART metrics) with YAML block |
| Quality Gate Integration | YES | Lines 571-591: S-014 thresholds and dimension interpretation table |
| Registration | YES | Lines 673-682: parent-routed model with all four registration points checked |
| Deployment Status | YES | Lines 686-689: explicit stub disclosure with implementation timeline |

**Gaps:**

1. **B=MAP Diagnosis Template is PLANNED, not present.** Line 456-457: "B=MAP Diagnosis Template | `skills/ux-behavior-design/templates/bmap-diagnosis-template.md` [PLANNED: Wave 4 Phase 2]". The template is a required operational artifact for consistent agent output. Its absence means an agent implementing this SKILL.md cannot produce structured output without inventing their own format. This is a functional gap, not just a documentation gap.

2. **Agent definition file is PLANNED, not present.** Lines 135: "The agent definition file (`skills/ux-behavior-design/agents/ux-behavior-diagnostician.md`) is pending Wave 4 Phase 2 implementation." The SKILL.md specifies the agent's full methodology but the agent itself does not exist. For a C4 deliverable, the SKILL.md specifying an unimplemented agent creates a completeness gap — the specification cannot be executed.

3. **CI gate criteria not enumerated in-document.** The SKILL.md references `ci-checks.md` for CI enforcement but does not state the specific gate criteria that apply to this sub-skill. A reader cannot verify gate compliance without opening a separate STUB file.

**Improvement Path:**
- Create `skills/ux-behavior-design/templates/bmap-diagnosis-template.md` (even a minimal version) before iter 2 scoring, OR clarify that template creation is a separate tracked deliverable with a completion dependency noted here.
- Either implement the agent stub (`ux-behavior-diagnostician.md`) or explicitly state in the Deployment Status section that this SKILL.md is itself a Wave 4 Phase 1 artifact (the specification), and Wave 4 Phase 2 delivers the agent. This reframing would change the evaluation criterion.
- Add a "CI Gate Summary" subsection in Quality Gate Integration listing the 2-3 gate criteria specific to this sub-skill (no Task tool, P-003 compliance, output schema validation).

---

### Internal Consistency (0.92/1.00)

**Evidence:**
Cross-reference verification across all field values:

| Field | Sub-Skill SKILL.md | Parent SKILL.md | Consistent? |
|-------|-------------------|-----------------|-------------|
| Agent name | `ux-behavior-diagnostician` | `ux-behavior-diagnostician` | YES |
| Tool tier | T2 (lines 21, 137) | T2 (line 158) | YES |
| Cognitive mode | Convergent (line 133) | Convergent (line 158) | YES |
| Model | Sonnet (line 133) | Sonnet (line 158) | YES |
| Wave | 4 (lines 45, 133, 630) | 4 (line 158) | YES |
| Output path | `skills/ux-behavior-design/output/{engagement-id}/...` | `skills/ux-behavior-design/output/{engagement-id}/...` | YES |
| Wave 4 entry criteria | Storybook 5+ Atom stories AND 1 Persona Spectrum review (lines 495-496, 636) | Same (line 266) | YES |
| Synthesis: bottleneck diagnosis | MEDIUM (line 560) | MEDIUM (line 361) | YES |
| Synthesis: intervention | LOW (line 561) | LOW (line 362) | YES |
| Bypass condition | Existing user base with analytics (line 638) | Same (line 266) | YES |
| Handoff target | ux-heart-analyst / /ux-heart-metrics | /ux-heart-metrics in Crisis sequence (line 318) | YES |

No contradictions found across 12 verified field pairs. The sub-skill SKILL.md is a faithful, internally consistent specialization of the parent skill pattern.

**Gaps:**
Minor: None critical. One observation — the "Do NOT use for" section at lines 116-124 uses sub-skill names like `/ux-heuristic-eval`, `/ux-atomic-design`, `/ux-inclusive-design`. These are consistent with the parent skill routing intent but the exact URL paths used in the parent skill's Lifecycle-Stage Routing table (lines 306-318) use the unabbreviated `/ux-heuristic-eval`, `/ux-atomic-design`, `/ux-inclusive-design`. No inconsistency; consistent referencing pattern throughout.

**Improvement Path:**
No changes needed for this dimension. Score may improve slightly if template and agent are implemented (reduces "stub" ambiguity in cross-references).

---

### Methodological Rigor (0.91/1.00)

**Evidence:**
All Fogg B=MAP model components are correctly represented:

| Model Element | SKILL.md Representation | Fogg (2009/2020) Ground Truth | Accurate? |
|---------------|------------------------|------------------------------|-----------|
| Three factors | Motivation, Ability, Prompt (line 252) | Motivation, Ability, Prompt (Fogg, 2020: P replaces T) | YES |
| Motivator pairs | Sensation/Pain, Anticipation/Fear, Belonging/Rejection (lines 260-264) | Identical three pairs in Fogg (2009) | YES |
| Six simplicity factors | Time, Money, Physical Effort, Brain Cycles, Social Deviance, Non-Routine (lines 283-288) | Identical six factors in Fogg (2009) | YES |
| Three prompt types | Spark, Facilitator, Signal (lines 301-305) | Identical three types in Fogg (2009) | YES |
| Intervention order | Prompt -> Ability -> Motivation (line 319-334) | Matches Fogg's (2020) "cheapest fix first" principle | YES |
| Action line | Motivation (Y) vs Ability (X) with curved threshold (lines 253-254) | Matches Fogg (2009) graphical model | YES |
| Behavior statement format | "After [CONTEXT], I will [SPECIFIC BEHAVIOR]" (line 364) | Directly quoted from Fogg (2020) Chapter 3 | YES |

**Gaps:**

1. **B=MAP formula imprecision at line 252.** The SKILL.md writes "B = M x A x P (Behavior = Motivation x Ability x Prompt)". Fogg (2009, 2020) presents B=MAP as convergence at a moment — not literal multiplication. The mathematical multiplication operator implies that doubling Motivation doubles Behavior, which the model does not claim. The correct framing is: behavior occurs when all three factors are simultaneously above the action threshold. The text corrects this on line 254 with the action line description, but the formula as stated is imprecise. An advanced UX practitioner might question this.

2. **"Limiting simplicity factor" principle.** Line 295 states "ability is governed by the scarcest resource at the moment of the prompt." This is accurately attributed to Fogg (2009) and the concept is correctly applied. However, Fogg uses "simplicity" as the inverse of difficulty, not "scarcest resource" language — this is a reasonable paraphrase but not a direct quotation. Not a material error.

3. **5-phase execution procedure is internally invented.** Lines 354-423 describe a "5-phase sequential workflow" that the SKILL.md notes "mirrors the Phase 1-5 structure established by the HEART metrics, Lean UX, and Atomic Design sub-skills." This is a reasonable framework extension, but the 5-phase structure is not from Fogg (2009/2020). This is disclosed at line 355 ("describes target behavior for the fully-implemented agent") and is a valid design choice, but a methodological purist would note that the 5-phase structure is framework-internal, not from the primary source.

**Improvement Path:**
- Line 252: Replace "B = M x A x P" with "B=MAP: behavior occurs when Motivation, Ability, and Prompt converge above the action threshold" (matches Fogg's actual model framing), removing the multiplication notation.
- Optionally add a footnote clarifying that the 5-phase execution structure is a Jerry framework implementation pattern, not a Fogg methodology element.

---

### Evidence Quality (0.87/1.00)

**Evidence:**
The External References section (lines 744-752) provides substantive bibliographic detail:

| Citation | Detail Level | Accuracy |
|----------|-------------|---------|
| Fogg (2009) | Conference name, article number, year | Correct — confirmed as "Persuasive '09" |
| Fogg (2020) | Publisher (Houghton Mifflin Harcourt), title | Correct |
| Eyal (2014) | Publisher (Portfolio/Penguin) | Correct |
| Wendel (2020) | Edition (2nd), publisher (O'Reilly) | Correct |

Inline citations appear consistently throughout the methodology sections: lines 92-97 cite (Fogg, 2020) for Key Capabilities, lines 258-270 cite Fogg (2009) for motivator pairs, lines 279-295 cite Fogg (2009) for simplicity factors, lines 298-305 cite Fogg (2009) for prompt types, lines 319-335 cite Fogg (2020) for algorithm ordering, line 364 cites (Fogg, 2020, Chapter 3) for behavior statement format (chapter-level specificity — strong).

Governance IDs indexed with full paths:
- PROJ-022 PLAN.md: `projects/PROJ-022-user-experience-skill/PLAN.md`
- EPIC-004: PROJ-022 EPIC-004 in WORKTRACKER.md
- ORCHESTRATION.yaml: `projects/PROJ-022-user-experience-skill/orchestration/ux-skill-build-20260303-001/ORCHESTRATION.yaml`

**Gaps:**

1. **Missing DOI for Fogg (2009).** The conference paper "A Behavior Model for Persuasive Design" (Persuasive '09, Article No. 40) has a public DOI: 10.1145/1541948.1541999. Omitting the DOI reduces citation completeness. For a C4 deliverable, all primary academic citations should include DOI for stable resolution.

2. **No access date on behaviormodel.org URL.** The parent skill's References section includes a URL to `https://behaviormodel.org/` (parent SKILL.md line 639) but the sub-skill's References section does not repeat this URL. The sub-skill cites the conference paper and book but not the living website. The website may have content updates (Fogg actively updates it). An access date citation on the URL would clarify the version consulted.

3. **Wendel (2020) citation lacks chapter-level specificity.** The SKILL.md notes "Referenced for intervention design patterns" but does not cite which chapters or sections of Wendel (2020) inform the intervention design recommendations. Fogg (2020) is cited with chapter-level specificity (Chapter 3) in one location; Wendel is cited only at the book level.

**Improvement Path:**
- Line 748: Add DOI 10.1145/1541948.1541999 to the Fogg (2009) citation.
- Line 748 or References table: Add URL `https://behaviormodel.org/` with access date 2026-03-04 for the living reference.
- Line 751: Add chapter reference for Wendel (2020) if the intervention table is directly derived from specific chapters.

---

### Actionability (0.92/1.00)

**Evidence:**
The SKILL.md provides multiple complementary layers of actionability:

1. **5-phase execution procedure** (lines 353-422): Each phase has Purpose, numbered Activities, and Output. An implementer can build the agent using this specification. Example: Phase 3 Bottleneck Diagnosis lists 5 activities, each with decision criteria including specific score thresholds and output fields.

2. **Bottleneck identification algorithm** (lines 316-335): 4-step algorithm with explicit pass/fail criteria at each step. "Prompt absent, mistimed, or mismatched -> prompt is the primary bottleneck" is directly executable.

3. **Intervention design table** (lines 341-351): 9 rows mapping bottleneck type to intervention category, example interventions, and effort level. An agent can select the right row based on diagnosed bottleneck.

4. **Task tool invocation example** (lines 192-219): Complete Python Task() call with prompt template containing all required UX CONTEXT fields. An orchestrator can use this verbatim.

5. **on_receive / on_send field tables** (lines 226-244): Type, required flag, and description for all handoff fields. Handoff YAML block (lines 520-541) shows a complete example with UX extension fields.

6. **Degraded mode mitigation table** (lines 602-608): 4 rows with limitation, impact, and specific mitigation action.

**Gaps:**

1. **Degraded mode question scripts are partially specified.** Lines 602-608 list mitigations like "Ask for qualitative assessment: 'How often does this fail?' Map: 'never' = critical, 'rarely' = major, 'sometimes' = moderate." This is specific and actionable. However, the "No session recordings" row says "Ask: 'What do users do instead of the target action?'" — only one question is specified. A fuller question script for each degraded mode scenario would increase executability.

2. **No explicit format for the Scope Brief output** of Phase 1. Phase 1's output is described as "Scope brief: product domain, target behavior statement, observation scope, upstream findings, evidence inventory with quality classification, wave entry status." But there is no template or example format for this intermediate artifact. Phases 4 and 5 output feeds into the Required Output Sections table (which is well-specified), but Phase 1-3 intermediate outputs are described in text only.

**Improvement Path:**
- Expand degraded mode question scripts to 3-5 questions per scenario (or reference the [PLANNED] template).
- Add a "Scope Brief" format example or subsection under Phase 1 Output, or note that the template will contain this format.

---

### Traceability (0.88/1.00)

**Evidence:**
Full traceability chain present for major cross-references:

| Reference Type | Example | Traceable? |
|---------------|---------|-----------|
| Parent SKILL.md | `skills/user-experience/SKILL.md` (line 722) | YES — file exists and contains the referenced content |
| Rule files | 5 files cited with exact paths and status (lines 725-729) | YES — paths are correct; status annotations honest |
| Project governance | PROJ-022 PLAN.md, WORKTRACKER.md, ORCHESTRATION.yaml (lines 740-742) | YES — paths correct |
| Quality enforcement SSOT | `.context/rules/quality-enforcement.md` (line 732) | YES — file exists |
| GitHub Issue | #138 with link (line 46, line 680) | YES — traceable |
| AGENTS.md | "ux-behavior-diagnostician listed under User-Experience Skill Agents" (line 681) | YES — verifiable |
| Agent governance schema | `docs/schemas/agent-governance-v1.schema.json` (line 734) | YES — path cited |
| Handoff schema | `docs/schemas/handoff-v2.schema.json` (line 733) | PARTIAL — cited but noted "pending file creation" in parent |

**Gaps:**

1. **Forward references to STUB sections of `ux-routing-rules.md`.** Lines 486, 488, 489 cite specific sections of `ux-routing-rules.md` by name: "[ux-routing-rules.md Section 'Stage Routing Table']", "[ux-routing-rules.md Section 'CRISIS Routing']", "[ux-routing-rules.md Section 'Common Intent Resolution']". The parent SKILL.md notes this file is "[PARTIAL: EPIC-001]" (parent SKILL.md line 585). These section references cannot be verified because the sections may not exist in the partial file. A reader following the trace will find the file but not the cited sections.

2. **Synthesis Judgments Summary format reference incomplete.** Line 451: "Follows the pattern in `skills/user-experience/rules/synthesis-validation.md`." This file is "[STUB: EPIC-001]" per parent SKILL.md line 586. The pattern cannot be verified by a reader following the trace.

3. **Agent definition and governance YAML files are [PLANNED].** Lines 723-724 cite both `ux-behavior-diagnostician.md` and `ux-behavior-diagnostician.governance.yaml` as `[PLANNED]`. The constitutional compliance claims (P-003 enforcement via forbidden_actions, disallowedTools in frontmatter) are stated as facts about files that do not yet exist. The text appropriately notes these are planned, but the traceability chain terminates at the planning assertion rather than an existing artifact.

**Improvement Path:**
- Lines 486-489: Replace named section references with file-level references: "source: `skills/user-experience/rules/ux-routing-rules.md` (Section pending EPIC-001 implementation)" — this is honest about the current state without creating false forward reference precision.
- Or: Create the `ux-routing-rules.md` sections (even stub headings) so the forward reference resolves to something.
- Line 451: Add "(stub)" annotation: "Follows the pattern in `skills/user-experience/rules/synthesis-validation.md` [STUB: EPIC-001]" to signal the reference is not yet fully resolvable.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.87 | 0.92 | Create `skills/ux-behavior-design/templates/bmap-diagnosis-template.md` with at minimum a stub containing section headings for B=MAP factor assessment, bottleneck algorithm trace, and intervention format. This resolves the PLANNED template gap and makes the SKILL.md operationally complete. Effort: Low (1-2 hours). |
| 2 | Methodological Rigor | 0.91 | 0.94 | Line 252: Replace "B = M x A x P" multiplication notation with convergence framing: "B=MAP: behavior occurs when Motivation, Ability, and Prompt converge simultaneously above the action threshold." This is both more accurate and matches Fogg's (2009, 2020) own language. Effort: Minimal (single line edit). |
| 3 | Evidence Quality | 0.87 | 0.92 | Line 748 (References table, Fogg 2009 row): Add DOI "10.1145/1541948.1541999" to the citation. Add URL "https://behaviormodel.org/ (accessed 2026-03-04)" as an additional reference for the living Fogg Behavior Model resource. Effort: Minimal (two-line edit). |
| 4 | Traceability | 0.88 | 0.92 | Lines 486-489: Qualify the ux-routing-rules.md section references with "(Section pending EPIC-001 implementation)" so readers understand these are forward references to an incomplete file. Alternatively, create stub section headings in ux-routing-rules.md for "Stage Routing Table", "CRISIS Routing", and "Common Intent Resolution". Effort: Low. |
| 5 | Completeness | 0.87 | 0.93 | Add a "CI Gate Summary" subsection under Quality Gate Integration (line 571) listing the 2-3 gate criteria specific to this sub-skill: (1) no Task tool in agent frontmatter, (2) P-003 in governance forbidden_actions, (3) output schema validation. This avoids requiring readers to open ci-checks.md (a STUB) to understand the gates. Effort: Low. |
| 6 | Completeness | 0.87 | 0.93 | Deployment Status section (lines 686-690): Add explicit phrasing that this SKILL.md is the Wave 4 Phase 1 deliverable, and the agent definition files are Wave 4 Phase 2 deliverables. This reframes the "missing" agent as a sequenced deliverable, reducing the perceived completeness gap. Effort: Minimal. |

---

## Gap-to-Threshold Analysis

The deliverable scores 0.897 against the standard H-13 threshold of 0.92 (gap: 0.023) and the C4 strict threshold of 0.95 (gap: 0.053).

**To reach H-13 threshold (0.92):**
Implementing Recommendations 1, 2, 3, and 4 closes the gap:
- Template creation (Rec 1): +0.02 to Completeness (0.87 -> 0.89), weighted impact +0.004
- Formula fix (Rec 2): +0.02 to Methodological Rigor (0.91 -> 0.93), weighted impact +0.004
- DOI + URL (Rec 3): +0.03 to Evidence Quality (0.87 -> 0.90), weighted impact +0.0045
- Traceability qualifications (Rec 4): +0.02 to Traceability (0.88 -> 0.90), weighted impact +0.002
- Estimated revised composite: 0.897 + 0.014 = **~0.911** (borderline PASS at H-13)

**To reach C4 threshold (0.95):**
All 6 recommendations plus agent stub implementation required:
- Agent stub creation would add +0.04 to Completeness (0.87 -> 0.91), weighted impact +0.008
- CI gate summary (Rec 5): +0.02 to Completeness, weighted impact +0.004
- With all changes: estimated composite **~0.923-0.930** — still below 0.95
- The remaining gap to 0.95 requires improvements in Actionability and Internal Consistency, achieved through: (a) expanded degraded mode question scripts, (b) Phase 1-3 intermediate output format specifications, and (c) agent implementation that resolves all forward references.

**Assessment:** The SKILL.md is a strong first draft. The C4 threshold of 0.95 sets a very high bar — at this level, operational artifacts (template, agent file) must exist, not merely be planned. The quickest path to 0.92 (H-13) is Recommendations 1-4. Reaching 0.95 requires Wave 4 Phase 2 agent implementation.

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite was computed
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Completeness held at 0.87 despite strong section coverage due to two absent artifacts; Evidence Quality held at 0.87 despite strong inline citations due to missing DOIs)
- [x] First-draft calibration considered — v1.0.0 initial creation; calibration anchors applied (0.87 = "acceptable but with significant gaps" in two dimensions)
- [x] No dimension scored above 0.95 (Internal Consistency 0.92 and Actionability 0.92 are justified by specific cross-verified field evidence)
- [x] Composite mathematically verified: 0.174 + 0.184 + 0.182 + 0.131 + 0.138 + 0.088 = 0.897

---

## Session Context (Handoff)

```yaml
verdict: REVISE
composite_score: 0.897
threshold: 0.95
h13_threshold: 0.92
weakest_dimension: completeness
weakest_score: 0.87
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Create skills/ux-behavior-design/templates/bmap-diagnosis-template.md (stub with section headings)"
  - "Line 252: Replace B=M x A x P multiplication notation with convergence framing"
  - "Lines 748-749: Add DOI 10.1145/1541948.1541999 and behaviormodel.org URL with access date"
  - "Lines 486-489: Qualify ux-routing-rules.md section references as pending EPIC-001"
  - "Add CI Gate Summary subsection under Quality Gate Integration with 2-3 specific gate criteria"
  - "Deployment Status: add explicit Wave 4 Phase 1 / Phase 2 sequencing language"
```
