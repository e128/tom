# Quality Score Report: Design Sprint Sub-Skill SKILL.md

## L0 Executive Summary

**Score:** 0.905/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.87)
**One-line assessment:** Strong first-iteration SKILL.md with complete sections, rigorous methodology, and excellent actionability — held below the 0.92 C4 threshold by a frontmatter/body T3 tool-tier inconsistency (Context7 MCP described but not declared) and partial traceability to planned-but-absent files.

---

## Scoring Context

- **Deliverable:** `skills/ux-design-sprint/SKILL.md`
- **Deliverable Type:** Design (Sub-Skill Specification)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold (C4):** >= 0.92 (H-13; C4 requires >= 0.95 per scoring prompt; see note below)
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 1

> **Threshold note:** The scoring prompt specifies >= 0.95 for C4. H-13 in `quality-enforcement.md` specifies >= 0.92 for C2+. The 0.95 prompt override is treated as the operative threshold for this engagement per the C4 criticality context. The deliverable falls below both thresholds at 0.905.

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.905 |
| **Threshold (C4 per prompt)** | 0.95 |
| **Threshold (H-13 baseline)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 23 sections present; minor redundancy between Routing/Wave Gating and Wave Architecture sections |
| Internal Consistency | 0.20 | 0.87 | 0.174 | All key agent spec fields match parent; frontmatter allowed-tools omits Context7 MCP despite body claiming T3 includes it |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | Full Day 1-4 structure, 5-phase execution, per-activity timing; Knapp et al. chapter-level citations |
| Evidence Quality | 0.15 | 0.90 | 0.135 | All three external citations with author-year format; internal paths repo-relative; Nielsen (2000) online article (canonical for claim) |
| Actionability | 0.15 | 0.92 | 0.138 | Complete session_context on_receive/on_send; Task tool invocation example; degraded mode per-MCP tables; CI gate enforcement specified |
| Traceability | 0.10 | 0.88 | 0.088 | Requirements Traceability table present; VERSION header present; some referenced files are [PLANNED] stubs |
| **TOTAL** | **1.00** | | **0.905** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**

All 23 sections specified in the scoring rubric are present and populated:

1. YAML frontmatter: `name`, `description` (WHAT+WHEN+triggers per H-26), `version`, `agents`, `allowed-tools`, `activation-keywords` — all present (lines 1-37)
2. Triple-lens (Document Audience): present with L0/L1/L2 row table (lines 74-83)
3. Purpose + Key Capabilities: present (lines 86-100)
4. When to Use (activation + do-not-use): present (lines 102-128)
5. Available Agents: present with role/tier/mode/model/output location table (lines 130-145)
6. P-003 Compliance: present with topology diagram (lines 147-166)
7. Invoking the Agent (3 methods + session_context): present (lines 168-251)
8. Methodology (Day 1-4 + 5 execution phases): present (lines 253-430)
9. Output Specification (location + required sections + template): present (lines 432-466)
10. Routing (keyword table + lifecycle-stage table + wave gating): present (lines 468-507)
11. Cross-Framework Integration (upstream + downstream + handoff YAML + canonical sequences): present (lines 509-567)
12. Synthesis Hypothesis Confidence (per-step table + gate enforcement + signal extraction): present (lines 569-590)
13. Quality Gate Integration (threshold table + scoring dimension interpretation + CI gate summary): present (lines 592-624)
14. Degraded Mode Behavior (Figma unavail, Miro unavail, both unavail, no upstream research): present (lines 626-679)
15. Wave Architecture (entry criteria + bypass condition + terminal wave): present (lines 682-694)
16. Constitutional Compliance (principle table + AI limitations): present (lines 696-726)
17. Registration (per-registration-point table): present (lines 728-738)
18. Deployment Status (Phase 1/2 distinction): present (lines 741-750)
19. Quick Reference (workflows + agent selection hints): present (lines 752-777)
20. References (repo-relative paths + requirements traceability + external citations): present (lines 779-822)

The `description` field satisfies H-26: WHAT (AJ&Smart Design Sprint 2.0 facilitation), WHEN (rapidly validate a product concept, solve a critical design challenge, test ideas with real users), TRIGGERS (design sprint, GV sprint, rapid prototyping, etc.) — all present in lines 3-18.

**Gaps:**

- Minor structural redundancy: Wave 5 entry criteria ("Wave 4: 30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed") appears verbatim in two sections — "Routing/Wave Gating" (lines 501-507) and "Wave Architecture" (lines 688-694). This is not a missing requirement but a duplication that slightly inflates perceived completeness without adding information.
- Navigation table has 19 section entries, correctly covering all major `##` headings per NAV-004.

**Improvement Path:**

- Consolidate the Wave Gating subsection under "Wave Architecture" (where it logically belongs) and remove the redundant entry from "Routing." This would tighten the document without losing any content.
- Score is 0.92 rather than higher because the duplication represents a structural choice that could be clarified — but all content is present.

---

### Internal Consistency (0.87/1.00)

**Evidence:**

Key verification points all PASS:

| Check | Expected | Actual | Status |
|-------|---------|--------|--------|
| Agent name | `ux-sprint-facilitator` | `ux-sprint-facilitator` (line 134) | PASS |
| Tier | T3 | T3 (line 134) | PASS |
| Mode | Systematic | Systematic (line 134) | PASS |
| Model | Opus | Opus (line 134) | PASS |
| Wave | 5 | 5 (line 47) | PASS |
| Output location | `skills/ux-design-sprint/output/{engagement-id}/ux-sprint-facilitator-{topic-slug}.md` | Matches exactly (line 134) | PASS |
| Wave 5 entry criteria | "30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed" | "30+ users for Kano survey OR 1 B=MAP bottleneck diagnosed" (line 503, 688) | PASS |
| Synthesis Day 4 confidence | HIGH | HIGH (line 575) | PASS (matches synthesis-validation.md line 62) |
| Synthesis Day 2 confidence | MEDIUM | MEDIUM (line 576) | PASS (matches synthesis-validation.md line 63) |
| MCP Figma REQ | REQ | REQ (line 628) | PASS (matches parent SKILL.md MCP matrix) |
| MCP Miro REQ | REQ | REQ (line 628) | PASS (matches parent SKILL.md MCP matrix) |
| Bypass condition | "existing user research" | "existing user research" (line 505, 690) | PASS |
| Version | 1.0.0 | 1.0.0 (lines 19, 43, 815) | PASS |

**Gaps:**

**INCONSISTENCY — T3 allowed-tools vs body description:**

Line 138 states: "Tool tier: T3 (External) = Read, Write, Edit, Glob, Grep, Bash + WebSearch, WebFetch, Context7 MCP."

The frontmatter allowed-tools (line 22) declares: `Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch` — Context7 MCP tools (`mcp__context7__resolve-library-id`, `mcp__context7__query-docs`) are absent.

Per agent-development-standards.md H-34, MCP servers should be declared in `mcpServers` frontmatter field, not `allowed-tools`. The frontmatter therefore may be intentionally omitting Context7 because it belongs in `mcpServers`. However:
1. The body text explicitly claims Context7 MCP as a T3 capability (line 138)
2. The MCP Integration Architecture in the parent SKILL.md does NOT list `ux-sprint-facilitator` under the Context7 usage table (lines 434-440 of parent) — only `ux-atomic-architect` and `ux-ai-design-guide` are listed as Context7 users
3. This creates an implicit inconsistency: body claims Context7 access, parent MCP matrix does not assign it

This is a real inconsistency: either (a) Context7 should be in `mcpServers` frontmatter and in the parent MCP matrix, or (b) the line 138 body text incorrectly describes T3 as including Context7 MCP for this particular agent when it does not.

**Improvement Path:**

- Audit whether `ux-sprint-facilitator` actually needs Context7 access. If yes: add `mcpServers` to frontmatter and add the agent to the parent SKILL.md MCP matrix (Context7 Usage section). If no: remove "Context7 MCP" from line 138's T3 description for this agent, clarifying it as "WebSearch/WebFetch-only T3."
- This is the primary factor preventing a higher Internal Consistency score.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**

The AJ&Smart Design Sprint 2.0 methodology is accurately and thoroughly described:

**Day structure accuracy:**
- GV 5-day to AJ&Smart 4-day compression is correctly described: "combining the original Day 1 (Understand) and Day 2 (Diverge) into a single Day 1 (Map), and merging the original Day 3 (Decide) with Day 4 (Prototype) into Day 3 (Decide + Storyboard)" (line 257). Day mapping table (lines 259-264) is accurate per Courtney (2019).

**Day 1 (Map) methodology accuracy:**
- 7 activities listed: Challenge Definition (HMW), Long-Term Goal, Sprint Questions, User Journey Map, Target Selection, Expert Interviews, HMW Clustering — all per Knapp et al. (2016) Chapters 2-6.
- Target selection quote attributed correctly: "Pick the most important customer and the most important moment" (line 280).

**Day 2 (Sketch) methodology accuracy:**
- 4-step sketch process: Notes (20 min), Ideas (20 min), Crazy 8s (8 min), Solution Sketch (30-90 min) — per Knapp et al. (2016) Chapter 8.
- Art Museum and Speed Critiques correctly described.

**Day 3 (Decide) methodology accuracy:**
- Straw poll → supervote sequence correctly described.
- Decider authority correctly attributed: "Knapp et al. (2016): 'The Decider has final say'" (line 316).
- Rumble vs. All-in-One correctly described.
- Assumption classification (must-be-true, nice-to-have, unknown) is a reasonable methodological elaboration.
- Storyboard panel count (10-16) is accurate per methodology.

**Day 4 (Test) methodology accuracy:**
- 5-user interviews correctly attributed to Nielsen (2000).
- 60-minute interview protocol structure is sound.
- Observation grid methodology with +/-/~ notation is accurate.
- Pattern analysis thresholds (>= 3/5 strong, 2/5 moderate, 1/5 weak) are correctly stated and match synthesis-validation.md signal extraction criteria (line 120 of synthesis-validation.md).
- Sprint question verdicts (Pass/Fail/Partial) are appropriate.

**Execution Phases:** 5-phase procedure is methodologically well-structured and internally consistent with Day 1-4 activities.

**Gaps:**

- Minor: Line 298 states Step 2 (Ideas) is "20 min" — the Sprint book specifies ~20 min for Notes and ~20 min for Ideas, which is approximately correct but the exact timings vary by book edition. This is an acceptable range specification.
- The "Prototype Construction" section (Day 4, Activity 1) references "just enough to feel real" and "Goldilocks quality prototype" attributed to Knapp et al. (2016). This is accurate.
- No methodology gaps found for a SKILL.md specification document.

**Improvement Path:**

- Score is 0.93 — essentially no improvement needed for methodology content. Minor timing precision for 4-step sketch (Notes/Ideas are approximate) does not materially affect methodological rigor.
- To reach 0.95+: add methodological rationale for the HMW question format (e.g., cite Ideo's design thinking literature that established HMW as a technique).

---

### Evidence Quality (0.90/1.00)

**Evidence:**

All three external citations properly formatted:

1. **Knapp, Zeratsky & Kowitz (2016):** "Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days." Simon & Schuster. — Full publisher information; chapter-level attribution throughout text (e.g., lines 280, 296, 316, 334, 343). Specific chapter citations in References section (line 809) enumerate Chapters 1-14 with content descriptions. This is exceptional citation depth.

2. **Courtney, J. (2019):** "The Design Sprint 2.0." AJ&Smart. — Cited at lines 88, 257, 810. Publisher included. Used for 4-day compression rationale.

3. **Nielsen, J. (2000):** "Why You Only Need to Test with 5 Users." Nielsen Norman Group. URL and access date provided (line 811). "5 users uncover approximately 85% of usability problems" is supported by this source.

Internal path references are all repo-relative (e.g., `skills/user-experience/SKILL.md`, `skills/user-experience/rules/synthesis-validation.md`, `docs/schemas/handoff-v2.schema.json`).

Specific quotes with attribution:
- "Pick the most important customer and the most important moment" — Knapp et al. (2016) (line 280) ✓
- "The Decider has final say" — Knapp et al. (2016) (line 316) ✓
- "A Goldilocks quality prototype -- just real enough" — Knapp et al. (2016) (line 334) ✓

**Gaps:**

- **Nielsen (2000) is an online article, not a peer-reviewed paper.** However, it is the canonical and widely-cited source for the 5-user finding in UX practice. The claim "approximately 85% of usability problems" is accurately attributed. This is the standard reference used in UX methodology documentation.
- **Missing citation for HMW framing.** The "How Might We" (HMW) technique is introduced at line 272 without a citation. HMW originated from IDEO and Sidney J. Parnes. While HMW is widely attributed to design thinking practice generally, a specific citation (e.g., Kelley & Littman, 2001; IDEO Design Thinking Toolkit) would strengthen evidence quality.
- **60-minute interview structure** (line 337-342) is described without a citation. The 5/5/30/15/5 minute breakdown appears to be a standard UX research interview format, but no specific citation is provided.

**Improvement Path:**

- Add a citation for the HMW technique: e.g., IDEO (2003) or Brown, T. (2009) "Change by Design" (Harper Business).
- Add a citation for the 60-minute interview protocol structure, or attribute it as "standard UX research interview protocol per Nielsen Norman Group best practices."
- These are specific, achievable additions that would raise this score to 0.93+.

---

### Actionability (0.92/1.00)

**Evidence:**

The SKILL.md provides concrete, implementable specifications across all major areas:

**Session context (on_receive/on_send):** Complete field enumeration with types, required flags, and field descriptions. on_receive: 6 fields (engagement_id, product_context, sprint_challenge, sprint_questions, upstream_artifacts, mcp_availability). on_send: 10 fields (sprint_day_completed, challenge_statement, prototype_fidelity, interview_count, theme_strength, usability_findings_count, sprint_questions_answered, winning_sketch_summary, validated_assumptions, invalidated_assumptions, synthesis_judgments). Enum values specified for prototype_fidelity and theme_strength. This is implementation-ready.

**Task tool invocation example:** Complete Python Task() call with all REQUIRED fields (lines 195-219). The engagement ID, topic, product, target users, sprint challenge, sprint questions, existing research, and MCP availability are all shown. This is directly executable.

**Degraded mode tables:** Three separate tables for Figma unavailable (3 rows), Miro unavailable (3 rows), and both unavailable (4 rows). Each row specifies limitation, impact, and mitigation with concrete instructions (e.g., "Use markdown-based sprint boards: journey map as a structured table, HMW notes as a bulleted list"). The degraded mode disclosure format (lines 665-674) is a ready-to-use template.

**CI gate summary:** Three CI gates with specific Check text and Enforcement mechanism (L4/L5). This is directly implementable in a CI pipeline.

**Output required sections table:** 9-row table with Section, Level, and Content descriptions. All sections have specific content requirements, not vague descriptions.

**Quick reference:** 6 workflow examples with command phrases; 7-row routing disambiguation table.

**Gaps:**

- The `ux-sprint-facilitator.governance.yaml` and `ux-sprint-facilitator.md` agent files are [PLANNED] — so the `disallowedTools: [Task]` and `constitution.principles_applied` declarations referenced in lines 162-164 cannot be verified as implemented. These are actionable specifications, but the actions are deferred to Phase 2.
- The design sprint template (`skills/ux-design-sprint/templates/design-sprint-template.md`) is referenced (line 464) but does not yet exist (Glob confirms only SKILL.md exists in the directory). The template path is specified and actionable, but the file is absent.

**Improvement Path:**

- The score of 0.92 reflects that the specification is fully actionable as a design document, but the referenced stub files (agent definition, template) are absent. To reach 0.95: create the template stub file referenced at line 464 as a Phase 1 deliverable alongside the SKILL.md.

---

### Traceability (0.88/1.00)

**Evidence:**

**VERSION header:** Line 39 provides `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/SKILL.md | PARENT: /user-experience skill | REVISION: initial creation -->` ✓

**References section:** 14 internal references and 3 external citations, all with path and content description ✓

**Requirements Traceability table (lines 799-804):** 3 entries:
- PROJ-022 PLAN.md → `projects/PROJ-022-user-experience-skill/PLAN.md`
- EPIC-005 (Wave 5 Deployment) → PROJ-022 EPIC-005 in WORKTRACKER.md
- ORCHESTRATION.yaml → specific path in orchestration directory

**In-line source attribution:**
- Knapp et al. cited 6+ times with chapter references
- Courtney (2019) cited 3 times
- Nielsen (2000) cited twice (lines 97, 343)
- Constitutional principles cited (P-003, P-020, P-022, P-001, P-002, P-004, P-011) with per-principle requirement and consequence
- AD-M-007 cross-reference for session_context governance codification (line 222)
- AD-M-004 cross-reference for L0/L1/L2 output level justification (line 140)

**Navigation table:** 19-entry Document Sections table at lines 52-73, all entries use anchor links per H-24 ✓

**Gaps:**

- **Referenced files that do not exist:** The References section lists `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` [PLANNED] and `skills/ux-design-sprint/agents/ux-sprint-facilitator.governance.yaml` [PLANNED]. While annotated as [PLANNED], these are the primary implementation artifacts that this SKILL.md specifies. Claims about `disallowedTools: [Task]` (line 162) and `constitution.principles_applied` (line 711) cannot be verified against the actual files because they don't exist yet.
- **ux-routing-rules.md references pending content:** Lines 494, 497 reference `skills/user-experience/rules/ux-routing-rules.md` Stage Routing Table as "pending EPIC-001 completion." This is transparently annotated but means traceability chains end at a stub file for the routing specification.
- **design-sprint-template.md** referenced at line 464 but absent from the filesystem (Glob confirms the only file in skills/ux-design-sprint/ is SKILL.md). The template is a required supporting artifact for full traceability of the output specification.

**Improvement Path:**

- Create the design sprint template stub file (`skills/ux-design-sprint/templates/design-sprint-template.md`) to close the missing artifact gap.
- The [PLANNED] agent files are acceptable for a Phase 1 SKILL.md spec, but their absence reduces traceability from 0.90+ to 0.88.
- Creating the template would raise this score to 0.91.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.87 | 0.93 | Resolve the T3/Context7 MCP ambiguity: either (a) add `mcpServers` frontmatter with Context7 server entry AND add `ux-sprint-facilitator` to the parent SKILL.md Context7 usage table, OR (b) remove "Context7 MCP" from line 138 T3 description and clarify T3 here as WebSearch/WebFetch only. Whichever path is chosen must be consistent across frontmatter, body text, and parent SKILL.md MCP matrix. |
| 2 | Traceability | 0.88 | 0.92 | Create the design sprint template stub file at `skills/ux-design-sprint/templates/design-sprint-template.md` with section structure (observation grid, storyboard panels, sprint question verdict format). This closes the referenced-but-absent artifact gap. |
| 3 | Evidence Quality | 0.90 | 0.93 | Add citation for the HMW technique (IDEO 2003 or Brown 2009 "Change by Design"). Add citation for the 60-minute interview protocol structure (Nielsen Norman Group UX research guide or equivalent). Both additions are single-line references. |
| 4 | Completeness | 0.92 | 0.94 | Consolidate the duplicate Wave 5 entry criteria: remove "Wave Gating" subsection from Routing (lines 499-507) and keep it only in "Wave Architecture" section where it belongs structurally. Update the navigation table accordingly. |
| 5 | Actionability | 0.92 | 0.94 | Create a minimal stub of `skills/ux-design-sprint/agents/ux-sprint-facilitator.md` to validate that the `disallowedTools: [Task]` declaration referenced at line 162 is implementable. Even a stub with frontmatter + section headers would allow CI gate UX-CI-001 to function. |

---

## Leniency Bias Check

- [x] Each dimension scored independently (Internal Consistency scored without influence from high Methodological Rigor)
- [x] Evidence documented for each score (specific line numbers cited for all dimension evidence)
- [x] Uncertain scores resolved downward (Internal Consistency: chose 0.87 not 0.89 given the T3/Context7 gap is verifiable not merely speculative)
- [x] First-draft calibration considered (version 1.0.0, iter1; no prior score)
- [x] No dimension scored above 0.95 without exceptional evidence (highest is Methodological Rigor at 0.93, justified by chapter-level citations and complete Day 1-4 coverage)

**Leniency check result:** The composite of 0.905 is appropriate for a strong first-iteration SKILL.md. The deliberate choice to score Internal Consistency at 0.87 (not 0.90) reflects a real, verifiable inconsistency between body text and frontmatter on Context7 MCP tool access. This inconsistency has downstream consequences: CI checks relying on the MCP matrix would not validate Context7 access for this agent. The deduction is justified, not punitive.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.905
threshold: 0.92
weakest_dimension: internal_consistency
weakest_score: 0.87
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Resolve T3/Context7 MCP inconsistency: add to frontmatter mcpServers + parent MCP matrix OR remove from body T3 description"
  - "Create design-sprint-template.md stub at skills/ux-design-sprint/templates/"
  - "Add HMW citation (IDEO 2003 or Brown 2009) and 60-min interview protocol citation"
  - "Consolidate Wave 5 entry criteria into Wave Architecture section only (remove from Routing)"
  - "Create ux-sprint-facilitator.md stub with frontmatter to enable CI gate validation"
```

---

*Score Report Version: 1.0.0*
*Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*Deliverable: skills/ux-design-sprint/SKILL.md v1.0.0*
*Project: PROJ-022 User Experience Skill*
*Created: 2026-03-04*
