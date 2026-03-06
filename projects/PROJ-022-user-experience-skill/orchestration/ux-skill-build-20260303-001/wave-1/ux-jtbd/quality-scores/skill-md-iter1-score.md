# Quality Score Report: JTBD Sub-Skill SKILL.md

## L0 Executive Summary

**Score:** 0.851/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness (0.75)

**One-line assessment:** The SKILL.md is a strong, well-structured document with rigorous JTBD methodology and solid evidence quality, but fails the C4 threshold (0.95) due to a missing "Invoking an Agent" section required by skill-standards.md for multi-agent-capable skills, and an H-26(c) registration gap in CLAUDE.md and mandatory-skill-usage.md.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/SKILL.md`
- **Deliverable Type:** Sub-skill SKILL.md definition file for `/ux-jtbd` (Jobs-to-Be-Done)
- **Criticality Level:** C4
- **Quality Gate Threshold:** 0.95 (C4 requirement specified in prompt; standard H-13 threshold is 0.92)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Skill Standards Reference:** `.context/rules/skill-standards.md`
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.851 |
| **Threshold** | 0.95 (C4, per scoring brief) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.75 | 0.150 | "Invoking an Agent" section missing; CLAUDE.md and mandatory-skill-usage.md registration absent per H-26(c) |
| Internal Consistency | 0.20 | 0.88 | 0.176 | Agent stub STUB caveat creates a factual tension with the SKILL.md's operational tone; cross-references verified accurate |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | ODI formula correct; job types classified properly; Christensen cite uses secondary text not primary JTBD source; Moesta/Spiek citation lacks a specific publication |
| Evidence Quality | 0.15 | 0.87 | 0.131 | Framework citations present with years and publications; Moesta/Spiek primary citation weak; governance/rule cross-references verified |
| Actionability | 0.15 | 0.84 | 0.126 | 5-phase workflow is executable; Quick Reference clear; missing "Invoking an Agent" section creates developer friction for the most common workflow question |
| Traceability | 0.10 | 0.88 | 0.088 | References section comprehensive; all named rule file paths verified to exist; one section cross-reference (ci-checks.md) is accurate |
| **TOTAL** | **1.00** | | **0.851** | |

---

## Detailed Dimension Analysis

### Completeness (0.75/1.00)

**Evidence:**

The skill-standards.md SKILL.md Body Structure table (rows 1-14) defines required sections. For multi-agent-capable skills (which this SKILL.md treats itself as, given it includes "P-003 Compliance" and "Available Agents"), row 8 explicitly requires: "Invoking an Agent — YES (multi-agent only) — Three options: natural language, explicit agent, Task tool code."

The `/ux-jtbd/SKILL.md` includes rows 1-7 and 9-14 but **row 8 ("Invoking an Agent") is entirely absent.** The navigation table (line 35-52) confirms no such section exists and no anchor link for it is declared.

**H-26(c) registration gap:**
- H-26(c) states: "New skills MUST be registered in CLAUDE.md, AGENTS.md, and mandatory-skill-usage.md (if proactive per H-22)."
- AGENTS.md: `/ux-jtbd` appears as `ux-jtbd-analyst` in the agent table — PRESENT.
- CLAUDE.md Skills table: Only `/user-experience` is registered; `/ux-jtbd` is not listed as an independent skill — ABSENT.
- mandatory-skill-usage.md Trigger Map: No row exists for `/ux-jtbd` — ABSENT.

**Note on sub-skill vs. skill:** The SKILL.md does correctly acknowledge that `/ux-jtbd` is a sub-skill routed by `ux-orchestrator`, not invoked directly by users (line 96: "This sub-skill is invoked by the `ux-orchestrator` agent... It is NOT invoked directly by users"). This partially mitigates the CLAUDE.md and mandatory-skill-usage.md gap, since direct user invocation is not the intended activation path. However, H-26(c) does not carve out a sub-skill exception — the rule applies to "new skills." Score credit given for the AGENTS.md entry.

**What is present:** All other required sections (navigation table, triple-lens, purpose, when-to-use, available agents, P-003 compliance, domain sections, integration, constitutional compliance, quick reference, references, footer) are present and substantive.

**Gaps:**
1. "Invoking an Agent" section missing — required per skill-standards.md row 8 for multi-agent skills
2. CLAUDE.md registration absent — H-26(c) partial compliance
3. mandatory-skill-usage.md registration absent — H-26(c) partial compliance
4. `output/` directory does not exist — no prior outputs to indicate operational use

**Improvement Path:**
- Add "Invoking an Agent" section with three invocation methods: natural language ("Use /user-experience to map JTBD for..."), explicit agent name reference, and note that direct Task invocation is done by ux-orchestrator only
- Determine whether sub-skill registration in CLAUDE.md is waived by design (document the exception) or add a sub-skill table entry
- Clarify mandatory-skill-usage.md applicability: if sub-skills are intentionally omitted, add a comment to that file explaining the parent-skill-routes pattern

---

### Internal Consistency (0.88/1.00)

**Evidence:**

Cross-reference verification results:
- Line 106: `skills/user-experience/rules/ux-routing-rules.md [Stage Routing Table]` — verified accurate. The Stage Routing Table in ux-routing-rules.md line 39 shows "Before design | Don't know what to build | `/ux-jtbd`" — CONSISTENT.
- Line 388: `skills/user-experience/SKILL.md [Cross-Sub-Skill Handoff Data]` — parent SKILL.md exists and the cross-sub-skill handoff data is referenced at lines 149-163 of parent — CONSISTENT.
- Line 432: `skills/user-experience/rules/synthesis-validation.md` — file verified to exist — CONSISTENT.
- Line 319: `skills/user-experience/rules/mcp-coordination.md [MCP Dependency Matrix]` — file verified to exist — CONSISTENT.
- Line 163 (Available Agents): References `skills/ux-jtbd/agents/ux-jtbd-analyst.md` and `skills/ux-jtbd/agents/ux-jtbd-analyst.governance.yaml` — both files verified to exist — CONSISTENT.
- Line 165 (P-003 Compliance): `skills/user-experience/rules/ci-checks.md` — file verified to exist — CONSISTENT.

**Tension: Agent stub vs. operational SKILL.md tone:**
The SKILL.md describes the `ux-jtbd-analyst` as a fully operational agent with a detailed 5-phase methodology. The agent definition file (`ux-jtbd-analyst.md`) contains: `<!-- STUB: Full agent definition to be implemented in PROJ-022 EPIC-002 (Wave 1). -->` — the full system prompt body is absent, with only identity, purpose, and guardrails stubs present.

This creates an internal tension: the SKILL.md documents a complete methodology the agent would execute, but the underlying agent cannot execute that methodology without a full system prompt. The SKILL.md does not disclose this stub state to its readers.

The parent SKILL.md (line 114) does disclose: "Currently deployed: `ux-orchestrator` (Wave 0 Foundation). Wave 1-5 sub-skill agents are **not yet deployed**." The `/ux-jtbd/SKILL.md` does not carry a matching disclosure.

**Gaps:**
1. SKILL.md does not disclose the agent stub state — inconsistency with the parent SKILL.md's Wave deployment disclosure (line 114 of parent)
2. Output directory `skills/ux-jtbd/output/` does not exist; the Output Specification section describes it as the output location without acknowledging it must be created — minor but technically inaccurate for an uninitialized skill

**Improvement Path:**
- Add a deployment status note (analogous to parent SKILL.md line 114) indicating this sub-skill's agent is a Wave 1 stub pending EPIC-002 implementation
- Create the `output/` directory with a `.gitkeep` so the referenced path exists

---

### Methodological Rigor (0.90/1.00)

**Evidence:**

The JTBD methodology as documented is substantively correct and well-structured:

1. **Job statement format** (line 73): "When [situation], I want to [motivation], so I can [expected outcome]" — this is the canonical format used in professional JTBD practice. Correctly presented.

2. **Three job type classification** (functional/social/emotional) — accurately reflects Christensen's three-job-type model from "Competing Against Luck" (2016).

3. **Moesta/Spiek four forces model** (lines 244-259): The push/pull/anxiety/habit framework is correctly attributed and accurately described. The equation "Switch happens when PUSH + PULL > ANXIETY + HABIT" is consistent with Moesta's presentations.

4. **Ulwick ODI 8-step universal job process** (lines 277-285): Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude — this is Ulwick's canonical job process from "Jobs to Be Done: Theory to Practice" (2016). Accurately reproduced.

5. **Opportunity score formula** (line 291): "Importance + max(Importance - Satisfaction, 0)" — this is Ulwick's correct ODI opportunity algorithm. Correctly stated.

6. **AI-augmented caveat** (lines 80-88): The MEDIUM confidence classification for AI-synthesized JTBD is methodologically sound and honest — primary research validation is indeed required.

**Gaps and inaccuracies:**

1. **Christensen citation**: The JTBD theory is attributed to Christensen's "The Innovator's Solution" (2003). This is the correct Christensen work for this period, but it is not the primary JTBD-for-product-development source. The canonical academic source for JTBD as a product strategy framework is "Competing Against Luck" (Christensen et al., 2016), which is cited separately in the References section. "The Innovator's Solution" is a secondary source for JTBD. The Theoretical Foundations table should cite "Competing Against Luck" as the primary JTBD Theory source.

2. **Moesta/Spiek primary citation**: The reference "Bob Moesta and Chris Spiek (2014)" in the Theoretical Foundations table lacks a specific publication. The 2014 date likely refers to Moesta/Spiek's early published writings; the most citable work is Moesta's "Demand-Side Sales 101" (2020), which is separately listed in References. The 2014 date is not traceable to a specific publication.

3. **Phase 4 ODI outcome format** (line 289): "Minimize the time it takes to [step action]" — this correctly represents Ulwick's functional outcome format. However, ODI also uses "Minimize the likelihood of [undesired outcome]" and "Minimize the variability of [step action]" — both cited correctly. The format example is accurate but incomplete (shows only 2 of Ulwick's 3 canonical outcome statement types).

**Improvement Path:**
- In Theoretical Foundations table, update JTBD Theory row: cite "Competing Against Luck" (2016) as the primary JTBD source; retain "The Innovator's Solution" as secondary
- Add a specific publication for the Moesta/Spiek 2014 citation or change the date to align with "Demand-Side Sales 101" (2020)
- Add the third Ulwick outcome format ("Minimize the variability of...") to Phase 4 for completeness

---

### Evidence Quality (0.87/1.00)

**Evidence:**

**Traceable to standards:**
- H-34 compliance claim (line 144): "See `skills/ux-jtbd/agents/ux-jtbd-analyst.md` for the full agent definition and `skills/ux-jtbd/agents/ux-jtbd-analyst.governance.yaml` for governance metadata" — both files verified to exist, governance.yaml shows correct schema structure with `version`, `tool_tier`, `identity.role`, `identity.expertise` (3 entries), `identity.cognitive_mode`, `capabilities.forbidden_actions` (3 NPT-009 entries), `constitution.principles_applied` (5 entries including P-003, P-020, P-022).
- P-003 compliance (lines 148-166): Enforcement claims are substantiated — `disallowedTools: [Task]` confirmed in ux-jtbd-analyst.md frontmatter (line 18-20 of agent stub).
- MCP-001 compliance (lines 325-332): Context7 protocol correctly stated per mcp-tool-standards.md.

**Framework citations quality:**
- Christensen (2003) — specific book cited; attributable
- Ulwick (2005, 2016) — specific books cited with publisher URL; attributable
- Moesta/Spiek (2014) — date without specific publication; weak traceability
- Klement (2016) — "When Coffee and Kale Compete" cited — attributable and correct as a Switch Interview reference
- Moesta (2020) — "Demand-Side Sales 101" cited — attributable

**Rule file claims:**
- `skills/user-experience/rules/ux-routing-rules.md [Stage Routing Table]` — verified section header exists in that file
- `skills/user-experience/rules/mcp-coordination.md [MCP Dependency Matrix]` — file exists (content not fully read but file confirmed)
- `skills/user-experience/rules/synthesis-validation.md` — file exists

**Gaps:**
1. Moesta/Spiek 2014 citation lacks specific publication — reduces traceability for one of the three core theoretical foundations
2. The governance.yaml identity.expertise has only 3 entries; the standards require "Min 2 entries" (AD-M-005) — this is met, but the fourth expertise domain (hiring criteria identification) documented in SKILL.md is absent from governance.yaml
3. No independent validation that `ci-checks.md` actually implements the CI enforcement it is cited as providing — it exists but was not read; this is an unverified claim

**Improvement Path:**
- Replace Moesta/Spiek 2014 citation with a specific work (e.g., the Harvard Business School case or the Re-Wired Group published article)
- Add "Hiring criteria identification" and "Job mapping decomposition" to governance.yaml identity.expertise
- Consider reading ci-checks.md to verify its content matches the enforcement claims in SKILL.md

---

### Actionability (0.84/1.00)

**Evidence:**

**What works:**
- 5-phase sequential workflow (lines 205-306) is step-by-step with specific inputs, activities, and outputs per phase — directly executable
- Output location specified with pattern: `skills/ux-jtbd/output/{engagement-id}/ux-jtbd-analyst-{topic-slug}.md` — unambiguous
- Quick Reference Common Workflows table (lines 470-476) gives copy-paste-friendly natural language examples
- Cross-Framework Integration workflows with ASCII diagrams (lines 399-425) show concrete execution sequences
- Confidence gate behavior (lines 435-439) is specific: "Requires expert review OR validation against 2-3 real user data points"
- Validation method thresholds (lines 443-450) are specific: "3-5 switch interviews", "10+ support tickets" — directly actionable

**Gap: Missing "Invoking an Agent" section:**
skill-standards.md row 8 specifies three required invocation options:
1. Natural language invocation
2. Explicit agent name invocation
3. Task tool code example

None of these appear in the SKILL.md. A developer reading this document cannot determine the exact command or syntax to invoke `ux-jtbd-analyst` explicitly (e.g., `Use the ux-jtbd-analyst agent to...` vs. Task tool delegation syntax). The Quick Reference section shows natural language examples but does not distinguish between user-to-orchestrator and orchestrator-to-agent invocation paths.

**Gap: No example output artifact:**
No example or template of the expected output format exists. Given the complexity of the job statement inventory + switch force analysis + job map structure, an example or template in `references/` would substantially improve actionability.

**Improvement Path:**
- Add "Invoking an Agent" section documenting all three invocation methods with examples
- Add a note that direct invocation bypasses the orchestrator's wave gate and lifecycle triage — clarifying when direct invocation is appropriate vs. when to go through ux-orchestrator
- Consider adding an output template to `skills/ux-jtbd/references/` for the job statement report structure

---

### Traceability (0.88/1.00)

**Evidence:**

**References section** (lines 486-524) is comprehensive:
- Agent files: both `.md` and `.governance.yaml` paths listed — verified accurate
- Parent Skill files: 6 entries with repo-relative paths — all 6 files verified to exist (via glob)
- Standards references: 6 entries — all are legitimate SSOT files
- JTBD framework references: 5 academic/book citations with author, year, full title, publisher

**Cross-reference spot-checks (all accurate):**
- Line 106: `ux-routing-rules.md [Stage Routing Table]` → verified to contain Stage Routing Table section header
- Line 164: `disallowedTools: [Task]` enforcement claim → verified in agent frontmatter line 18-20
- Line 319: `mcp-coordination.md [MCP Dependency Matrix]` → file exists (section header not verified)
- Line 432: `synthesis-validation.md` → file exists
- Line 165: `ci-checks.md` → file exists

**Footer traceability:**
Footer (lines 528-536) correctly identifies: version, parent skill, constitutional compliance, SSOT, project, creation date, agent. All traceable.

**Gaps:**
1. `ci-checks.md` reference (line 165) asserts it "documents" CI enforcement for P-003 Task prohibition — file exists but content not verified; risk of inaccurate claim
2. `mcp-coordination.md [MCP Dependency Matrix]` cited with a specific section header name — section header was not verified against file content (file exists but section name unconfirmed)
3. The SKILL.md version comment (line 25: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: skills/user-experience/SKILL.md | PARENT: /user-experience skill -->`) incorrectly lists SOURCE as the parent SKILL.md rather than the creating agent or ADR — minor but imprecise provenance
4. No ADR or decision record traceable to the sub-skill architecture decisions (e.g., why JTBD is in Wave 1, why Sonnet model was chosen over Haiku or Opus)

**Improvement Path:**
- Read ci-checks.md to verify P-003 enforcement content and update the cross-reference claim if needed
- Verify `mcp-coordination.md [MCP Dependency Matrix]` section header name
- Update VERSION comment SOURCE to reference the creating work item (PROJ-022 EPIC-001 or similar) rather than the parent SKILL.md

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.75 | 0.90 | Add "Invoking an Agent" section per skill-standards.md row 8: three invocation methods (natural language user-to-orchestrator, explicit agent reference by ux-orchestrator, note that direct user invocation bypasses wave gate). This is the single largest gap. |
| 2 | Completeness | 0.75 | 0.90 | Resolve H-26(c) registration ambiguity: either (a) add a sub-skill entry in CLAUDE.md with a note that it is routed via `/user-experience` parent skill, or (b) document an explicit exception in the SKILL.md explaining why sub-skills intentionally omit CLAUDE.md and mandatory-skill-usage.md registration. |
| 3 | Internal Consistency | 0.88 | 0.94 | Add deployment status note to SKILL.md matching parent SKILL.md disclosure: "This sub-skill agent is a Wave 1 stub (PROJ-022 EPIC-002). Full implementation pending." This resolves the SKILL.md operational tone vs. stub agent body tension. |
| 4 | Methodological Rigor | 0.90 | 0.95 | Update Theoretical Foundations: (a) change JTBD Theory primary source to "Competing Against Luck" (2016); (b) replace Moesta/Spiek 2014 with a specific publication or traceable reference; (c) add the third Ulwick outcome format ("Minimize the variability of...") to Phase 4. |
| 5 | Actionability | 0.84 | 0.92 | Create `skills/ux-jtbd/references/ux-jtbd-output-template.md` with a concrete output artifact template covering the required sections (Job Statement Inventory, Switch Force Analysis, Job Map, Hiring Criteria, Opportunity Scores, Synthesis Judgments Summary). Add reference in SKILL.md Output Specification. |
| 6 | Evidence Quality | 0.87 | 0.92 | Read `ci-checks.md` and `mcp-coordination.md` to verify the specific section headers cited in SKILL.md match actual content. Update citations if discrepant. |
| 7 | Traceability | 0.88 | 0.93 | Add architecture decision traceability: reference the ADR or PROJ-022 work item that established Wave 1 classification and Sonnet model choice for ux-jtbd-analyst. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific line number or section references
- [x] Uncertain scores resolved downward (Completeness: 0.75 not 0.80 given two H-26(c) registration gaps + missing required section)
- [x] First-draft calibration considered (this is v1.0.0; good first-draft but below the 0.95 C4 ceiling)
- [x] No dimension scored above 0.95 without exceptional evidence
- [x] Weighted composite verified: (0.75×0.20) + (0.88×0.20) + (0.90×0.20) + (0.87×0.15) + (0.84×0.15) + (0.88×0.10) = 0.150 + 0.176 + 0.180 + 0.131 + 0.126 + 0.088 = 0.851
- [x] Score of 0.851 is significantly below the C4 threshold of 0.95; REVISE verdict is unambiguous

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.851
threshold: 0.95
weakest_dimension: Completeness
weakest_score: 0.75
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add 'Invoking an Agent' section per skill-standards.md row 8 (three invocation methods)"
  - "Resolve H-26(c) registration: CLAUDE.md and mandatory-skill-usage.md absent or explicitly excepted"
  - "Add Wave 1 stub deployment status note matching parent SKILL.md disclosure"
  - "Fix Theoretical Foundations citations: Christensen primary source, Moesta/Spiek specific publication"
  - "Create output template in references/ directory"
  - "Verify ci-checks.md and mcp-coordination.md section headers cited in SKILL.md"
  - "Add ADR/work-item traceability for Wave 1 classification and model choice"
```

---

*Score Report Version: 1.0.0*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Skill Standards: `.context/rules/skill-standards.md`*
*Agent: adv-scorer*
*Created: 2026-03-04*
