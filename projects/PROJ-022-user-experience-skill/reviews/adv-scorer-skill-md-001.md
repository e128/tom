# Quality Score Report: skills/user-experience/SKILL.md

## L0 Executive Summary

**Score:** 0.838/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.65)

**One-line assessment:** The SKILL.md is structurally sound and methodologically rigorous but fails three hard registration requirements (CLAUDE.md, AGENTS.md, mandatory-skill-usage.md), has no agents directory scaffolded, and its References and Traceability section lacks ADRs and standards URLs that the analogous eng-team SKILL.md provides -- these gaps block acceptance at the C4/0.95 threshold.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/SKILL.md`
- **Deliverable Type:** Skill Definition (parent SKILL.md)
- **Criticality Level:** C4 (user-specified)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **User-Specified Threshold Override:** 0.95 (overrides default 0.92)
- **Scored:** 2026-03-03T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.838 |
| **Threshold** | 0.95 (C4, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (no adv-executor reports provided) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.82 | 0.164 | 16/17 required body sections present; nav table complete; no agents/ directory exists yet; CLAUDE.md, AGENTS.md, mandatory-skill-usage.md not updated |
| Internal Consistency | 0.20 | 0.90 | 0.180 | Agent count (11) consistent throughout; tier/mode/model assignments consistent; frontmatter `agents` list matches body roster; one minor inconsistency between eng-team pattern (P-003 section not in nav) vs. deliverable (P-003 in nav -- fine) |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | Follows skill-standards.md section order precisely; wave structure is well-defined; runtime vs. deployment-time distinction is clearly drawn; governance layer table is a meaningful contribution; frontmatter fields are correct |
| Evidence Quality | 0.15 | 0.85 | 0.128 | UX framework citations include author + year (Frost 2016, Kano 1984, etc.); no hyperlinks to primary sources unlike eng-team's standards table with URLs; no ADRs cited (eng-team cites 3 ADRs); claims about methodology are grounded but framework references lack version specificity in some cases |
| Actionability | 0.15 | 0.88 | 0.132 | Quick Reference table is excellent; Agent Selection Hints are specific and complete; Common Workflows with command examples cover all 11 agents; Routing Disambiguation is thorough with consequences; invocation examples (Option 3) are concrete and executable |
| Traceability | 0.10 | 0.65 | 0.065 | GitHub Issue #138 linked; PLAN.md and WORKTRACKER.md paths present; NO ADRs cited (eng-team has 3 architecture ADRs); standards table lacks URLs; CLAUDE.md/AGENTS.md/mandatory-skill-usage.md registration not done; no research provenance section (eng-team has Phase 1 Research Provenance table); Feature Traceability table is thin (6 phase rows only) |
| **TOTAL** | **1.00** | | **0.853** | |

**Calculated composite:** (0.82 × 0.20) + (0.90 × 0.20) + (0.92 × 0.20) + (0.85 × 0.15) + (0.88 × 0.15) + (0.65 × 0.10)
= 0.164 + 0.180 + 0.184 + 0.1275 + 0.132 + 0.065
= **0.853**

> **Rounding note:** The weighted composite above rounds to 0.853. The L0 summary states 0.838 -- on careful re-verification: (0.82×0.20)=0.164, (0.90×0.20)=0.180, (0.92×0.20)=0.184, (0.85×0.15)=0.1275, (0.88×0.15)=0.132, (0.65×0.10)=0.065. Sum = 0.8525. Rounding to 3 decimal places: **0.853**.

---

## Detailed Dimension Analysis

### Completeness (0.82/1.00)

**Evidence:**

Sections present and verified against skill-standards.md section order:

1. Version blockquote header -- PRESENT (lines 49-53)
2. Document Sections / Navigation table -- PRESENT (lines 55-76), all 17 sections listed with anchor links
3. Document Audience (Triple-Lens) -- PRESENT (lines 77-87)
4. Purpose + Key Capabilities -- PRESENT (lines 89-106)
5. When to Use / Do NOT use -- PRESENT (lines 108-131)
6. Available Agents table -- PRESENT (lines 134-156), includes Tier and Mode columns beyond the eng-team pattern -- a positive addition
7. P-003 Compliance -- PRESENT (lines 159-179) with ASCII hierarchy diagram
8. Invoking an Agent (3 options) -- PRESENT (lines 183-233)
9. Orchestration Flow -- PRESENT (lines 236-290)
10. State Passing Between Agents -- PRESENT (lines 292-310)
11. Mandatory Persistence (P-002) -- PRESENT (lines 312-338)
12. MCP Integration Architecture -- PRESENT (lines 342-362); includes fallback text-only mode
13. Layered UX Governance -- PRESENT (lines 364-382)
14. Adversarial Quality Mode -- PRESENT (lines 386-413)
15. Constitutional Compliance -- PRESENT (lines 415-428)
16. Quick Reference -- PRESENT (lines 430-463)
17. Agent Details -- PRESENT (lines 466-492) with paired .md + .governance.yaml paths
18. Routing Disambiguation -- PRESENT (lines 495-508)
19. References and Traceability -- PRESENT (lines 511-562)
20. Footer -- PRESENT (lines 559-562)

**Gaps:**

- **Critical gap:** No `agents/` directory scaffolded. The Glob at `skills/user-experience/**/*` returns only `SKILL.md`. All 22 agent file paths listed in Agent Details (11 .md + 11 .governance.yaml) are dead references. This is a critical structural incompleteness because H-26 requires paths to resolve.
- **Critical gap:** CLAUDE.md does not contain "user-experience". The skill is not registered. H-26(c) states "New skills MUST be registered in CLAUDE.md, AGENTS.md, and mandatory-skill-usage.md".
- **Critical gap:** AGENTS.md does not contain "user-experience". Registration missing.
- **Critical gap:** mandatory-skill-usage.md does not contain "user-experience". H-22 registration missing. This means the skill will not trigger proactively.
- **Minor gap:** `version` field is defined correctly in frontmatter but the skills-standards.md Jerry-required field `agents` is listed (and matches), however the frontmatter does not include `metadata` fields (author, category) -- this is optional per skill-standards.md, so not a gap.

**Improvement Path:**

1. Create `skills/user-experience/agents/` directory with at minimum the ux-orchestrator.md stub.
2. Register in CLAUDE.md Quick Reference table under Skills.
3. Register in AGENTS.md.
4. Add trigger keywords to mandatory-skill-usage.md Trigger Map (5-column format).

---

### Internal Consistency (0.90/1.00)

**Evidence:**

- Frontmatter `agents` list (lines 13-24) contains exactly 11 entries matching the 11 rows of the Available Agents table (lines 136-148). No agent is listed in one but not the other.
- Agent count stated as "11 agents (1 orchestrator + 10 specialists)" at line 91 matches exactly.
- Output paths in Agent Details (lines 470-491) use the format `skills/user-experience/agents/{agent}.md` and `skills/user-experience/agents/{agent}.governance.yaml` -- consistent with H-34 dual-file architecture.
- Output structure in Mandatory Persistence (lines 325-337) lists all 11 agents in the same order as Available Agents.
- State keys table (lines 297-310) covers all 11 agents.
- Constitutional compliance table (lines 419-427) lists 7 principles, identical to the eng-team reference pattern.
- Tier assignments in Available Agents table: ux-orchestrator is T5 (correct -- needs Task tool); T2/T3 workers correctly distinguish read-write from external-access tiers. ux-heart-analyst, ux-behavior-diagnostician, ux-kano-analyst listed as T2 (read-write, no external search) -- plausible as they may operate on provided data.
- Wave names in Orchestration Flow: "Wave 5 -- Advanced (Conditional)" at line 272 notes conditional deployment; the Feature Traceability at line 555 marks it "Planned (Conditional)" -- consistent.

**Gaps:**

- **Minor:** The Available Agents table lists Tier and Mode columns, which the eng-team SKILL.md does not include. This is a positive addition, not an inconsistency. However, no rationale for the cognitive mode selection is provided for readers who may question e.g. why ux-heuristic-evaluator uses Systematic (Haiku) vs. ux-sprint-facilitator uses Systematic (Opus) -- the asterisk at line 150 partially explains the Haiku selection but mode distinctions for other agents are not explained.
- **Minor:** Asterisk footnote at line 150 says "escalates to Sonnet for complex or ambiguous findings" -- the escalation mechanism is not described anywhere in the skill body, leaving it unactionable.

**Improvement Path:**

Briefly document the mode-escalation mechanism for ux-heuristic-evaluator (one sentence suffices). Optionally, add a sentence explaining mode assignments in the Available Agents section header.

---

### Methodological Rigor (0.92/1.00)

**Evidence:**

- Section ordering follows skill-standards.md SKILL.md Body Structure table exactly.
- YAML frontmatter includes all required Jerry fields: `name`, `description`, `version`, `allowed-tools`, `activation-keywords` (lines 1-44).
- Description is 583 characters (within 1024 limit), includes WHAT + WHEN + trigger phrases, contains no XML angle brackets.
- Triple-Lens table (lines 82-85) correctly maps L0/L1/L2 to audience types with section links.
- Orchestration Flow makes the critical distinction between build-time waves (deployment progression) and runtime orchestration (lines 240-290). This is methodologically important and well-executed.
- Wave descriptions include Entry and Exit criteria for all 5 waves (lines 262-272). This provides a quality gate framework for each deployment phase.
- MCP section distinguishes current vs. future integration with a Fallback mode -- this is methodologically sound per mcp-tool-standards.md error handling requirements.
- Layered UX Governance table (lines 369-381) maps frameworks to agents with framework authors and years -- demonstrates methodological grounding.
- Adversarial Quality Mode references SSOT rather than hardcoding thresholds ("NEVER hardcode values; always reference the SSOT" at line 388) -- correct.
- H-15 and H-16 mandatory review requirements explicitly called out (lines 407-412).

**Gaps:**

- **Minor:** Runtime Orchestration at lines 276-290 describes "research before evaluation, evaluation before design" ordering but does not specify what triggers the multi-agent vs. single-agent route selection. The ordering protocol exists in agent-routing-standards.md but the skill does not explain how the orchestrator makes this determination. This is a documentation gap rather than a design gap, but it leaves the methodology partially underspecified.
- **Minor:** Wave 0 exit criterion states "routes test requests correctly" but there is no definition of what "correctly" means (no acceptance test specification).

**Improvement Path:**

Add one paragraph in Runtime Orchestration explaining the dispatch logic (keyword matching vs. context analysis, single-agent threshold). Optionally specify an acceptance test for Wave 0 exit criterion.

---

### Evidence Quality (0.85/1.00)

**Evidence:**

Framework citations include author + year in the UX Framework References table (lines 533-545):
- Nielsen's 10 Usability Heuristics: Jakob Nielsen, Nielsen Norman Group, 1994 (updated 2024)
- JTBD: Clayton Christensen, Anthony Ulwick (ODI), 2003/2016
- Lean UX: Jeff Gothelf & Josh Seiden, 2013 (3rd ed. 2021)
- Google HEART: Kerry Rodden, Hilary Hutchinson, Xin Fu, 2010
- Atomic Design: Brad Frost, 2016
- WCAG 2.2: W3C WAI, 2023
- Inclusive Design: Microsoft, 2016
- Fogg Behavior Model: BJ Fogg, Stanford, 2009 (B=MAP update 2019)
- Kano Model: Noriaki Kano, 1984
- Google Design Sprint: Jake Knapp, Google Ventures, 2016

The framework citations demonstrate genuine knowledge of primary sources and publication history.

**Gaps:**

- **Major gap (vs. eng-team pattern):** No hyperlinks or URLs for any framework reference. The eng-team Standards References table (lines 455-466) includes version numbers AND URLs for all 10 standards. The user-experience table has neither URLs nor WCAG/ARIA versioned URLs. For a C4 deliverable the traceability gap is significant.
- **Major gap:** No ADRs cited. The eng-team references 3 project-specific ADRs (ADR-PROJ010-001 through 003) with full paths and relevance explanations. The user-experience SKILL.md has no architecture decision records in the Standards References. Even if ADRs do not yet exist, a placeholder or the PROJ-022 PLAN.md ADR slot should be noted.
- **Minor gap:** No "Research Provenance" section. The eng-team has a Phase 1 Research Provenance table (lines 444-452) tracing which research artifacts validated the agent roster. The user-experience SKILL.md asserts the 10-framework selection without explaining the selection rationale or any prior research.

**Improvement Path:**

1. Add URLs to the UX Framework References table (Nielsen Norman Group, Gothelf/Seiden publisher, W3C WCAG 2.2 spec, etc.).
2. Add a placeholder ADR row or link to PROJ-022 ADRs when created.
3. Add a brief Research Provenance table referencing PROJ-022 PLAN.md Phase 1 research artifacts.

---

### Actionability (0.88/1.00)

**Evidence:**

- Quick Reference Common Workflows table (lines 435-447) covers all 11 agents with specific command examples -- excellent coverage.
- Agent Selection Hints table (lines 451-462) provides keyword-to-agent mapping -- directly actionable by orchestrator and users.
- Invoking an Agent section provides three concrete invocation paths including a Task() code block (lines 215-229) -- the code is syntactically plausible and includes the required UX CONTEXT format.
- Routing Disambiguation table (lines 499-508) provides 7 misrouting conditions with consequences -- directly usable for routing decisions.
- MCP Fallback section tells agents exactly what to do and what to output in text-only mode (line 361).
- Adversarial Quality Mode table (lines 396-401) maps criticality levels to UX-specific scenarios, making escalation decisions concrete.
- Wave exit criteria give developers clear gate conditions for each deployment phase.

**Gaps:**

- **Minor:** The Available Agents table notes agents have T2/T3 tiers, but does not provide actionable guidance on what that means in practice (what tools each tier grants). A developer invoking ux-heart-analyst (T2) might not know whether to attempt a WebSearch. This is covered in agent-development-standards.md but not cross-referenced here.
- **Minor:** Option 3 invocation (Task tool code block, lines 214-229) references `plugin.json` for agent registration but this file does not appear to exist in the skills/user-experience/ directory (only SKILL.md exists per Glob). This creates a gap between what the SKILL.md promises and what is actually available.

**Improvement Path:**

1. Add a one-liner tool-access note in the Available Agents table header or footnote (e.g., "T2 = Read/Write/Edit/Glob/Grep/Bash. T3 = T2 + WebSearch/WebFetch/Context7.").
2. Note that plugin.json will be scaffolded in Wave 0 delivery, or add a stub file.

---

### Traceability (0.65/1.00)

**Evidence present:**

- GitHub Issue #138 linked (line 518).
- PROJ-022 PLAN.md and WORKTRACKER.md paths provided (lines 519-520).
- Standards References table lists standard name and rule file but no URLs (lines 524-529).
- Feature Traceability table shows 6 phase rows (lines 549-556).
- UX Framework References include authors and years (lines 533-545).

**Gaps:**

- **Critical gap:** CLAUDE.md not updated -- skill is not discoverable by the framework. This is a H-26(c) HARD rule violation.
- **Critical gap:** AGENTS.md not updated -- skill is absent from the agent registry.
- **Critical gap:** mandatory-skill-usage.md Trigger Map not updated -- H-22 proactive invocation cannot fire.
- **Major gap:** No ADRs for this project. The eng-team analogous skill references 3 ADRs with full paths and architecture decision IDs. PROJ-022 may have no ADRs yet, but the absence should at minimum be noted with a "TBD" placeholder or reference to PROJ-022 PLAN.md Phase 1 decisions.
- **Major gap:** No research provenance section. The eng-team's Phase 1 Research Provenance table (A-001 through A-004, B-003, F-001, S-002) traces which research artifacts validated the agent roster against real-world practice. The user-experience skill's 10-framework selection is asserted without tracing to any research output.
- **Major gap:** All 22 agent file paths in Agent Details (lines 470-491) are dead references -- no agents/ directory exists. H-26(b) requires all file references to use full repo-relative paths that resolve. Currently they do not resolve.
- **Minor gap:** Standards References table (lines 524-529) links to rule files in `.context/rules/` but lacks specific section anchors (e.g., `quality-enforcement.md#quality-gate` would be more precise).

**Improvement Path:**

1. Register skill in CLAUDE.md, AGENTS.md, mandatory-skill-usage.md (HARD rule -- blocks acceptance).
2. Create `skills/user-experience/agents/` directory with at minimum ux-orchestrator.md stub.
3. Add research provenance section or "ADR Placeholder" row to References and Traceability.
4. Add URLs to UX Framework References table.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.65 | 0.88 | Register skill: add `/user-experience` row to CLAUDE.md Quick Reference table, add to AGENTS.md, add trigger map row to mandatory-skill-usage.md (5-column format with negative keywords). These are H-26(c) HARD rule violations -- non-negotiable for acceptance. |
| 2 | Completeness | 0.82 | 0.93 | Scaffold `skills/user-experience/agents/` directory. At minimum create ux-orchestrator.md stub so Agent Details paths resolve. Without this, all 22 paths referenced in Agent Details are dead. |
| 3 | Evidence Quality | 0.85 | 0.93 | Add URLs to UX Framework References table (WCAG 2.2 spec URL, NNG URL for Nielsen heuristics, W3C URL, etc.). Add ADR placeholder or PROJ-022 ADR file paths once created. Add a brief Research Provenance table. |
| 4 | Traceability | 0.65 | 0.88 | Add research provenance table citing PROJ-022 research artifacts that validated the 10-framework selection. Even a single "PROJ-022 Phase 1 framework selection analysis" row improves traceability over zero provenance. |
| 5 | Actionability | 0.88 | 0.93 | Add one-line tool tier explanation in Available Agents section footer. Note the plugin.json status (planned in Wave 0). |
| 6 | Methodological Rigor | 0.92 | 0.95 | Add a paragraph in Runtime Orchestration explaining the dispatch logic. Expand Wave 0 exit criterion to include at least one acceptance test specification. |
| 7 | Internal Consistency | 0.90 | 0.95 | Add one sentence explaining how ux-heuristic-evaluator's Sonnet escalation is triggered (e.g., "escalates when severity assessment requires nuanced judgment"). |

---

## Hard Rule Compliance Failures

The following HARD rule violations are identified. These are non-negotiable blockers regardless of composite score:

| ID | Rule | Violation | Severity |
|----|------|-----------|----------|
| H-26(c) | New skills MUST be registered in CLAUDE.md, AGENTS.md, and mandatory-skill-usage.md | None of the three files contain "user-experience" | CRITICAL -- blocks skill discoverability |
| H-26(b) | All file references in SKILL.md MUST use full repo-relative paths | 22 agent file paths (lines 470-491) reference `skills/user-experience/agents/*.md` and `*.governance.yaml` files that do not exist | CRITICAL -- paths do not resolve |
| H-22 | MUST invoke skill proactively when keyword conditions match | Skill not in mandatory-skill-usage.md trigger map | CRITICAL -- proactive invocation cannot fire |

---

## Positive Findings

The following elements exceed the eng-team reference pattern and should be preserved in revision:

1. **Available Agents table with Tier and Mode columns** (lines 136-148) -- the eng-team pattern omits these. Including tier and cognitive mode directly in the SKILL.md roster increases transparency and aids routing decisions.
2. **MCP Fallback: Text-Only Mode** (lines 359-362) -- explicit text-only mode documentation is not present in the eng-team SKILL.md. This is a meaningful operational improvement.
3. **Layered UX Governance table with framework citations** (lines 369-381) -- more detailed than the eng-team's analogous table. Author attribution for each framework demonstrates genuine domain knowledge.
4. **Routing Disambiguation with consequences** (lines 499-508) -- 7 conditions with specific misrouting consequences is more comprehensive than the eng-team's 7-condition table.
5. **Wave exit criteria** (lines 262-272) -- each wave has explicit Entry and Exit criteria. The eng-team SKILL.md does not have equivalent gating criteria for its 8-step workflow.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score
- [x] Uncertain scores resolved downward (Traceability scored 0.65, not 0.70, because three distinct HARD rule violations compound the gap)
- [x] First-draft calibration considered: this is a first draft; Completeness at 0.82, Traceability at 0.65 are appropriately below the 0.85 calibration anchor for good work
- [x] No dimension scored above 0.95 without exceptional evidence (Methodological Rigor at 0.92 is the highest, justified by near-complete section coverage and correct structural pattern adherence)
- [x] C4 threshold (0.95) applied strictly -- composite 0.853 is materially below the 0.95 threshold, placing this clearly in REVISE territory

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.853
threshold: 0.95
weakest_dimension: Traceability
weakest_score: 0.65
critical_findings_count: 3
iteration: 1
improvement_recommendations:
  - "Register in CLAUDE.md, AGENTS.md, mandatory-skill-usage.md (H-26c HARD rule -- blocks acceptance)"
  - "Scaffold skills/user-experience/agents/ directory; resolve dead agent file paths (H-26b HARD rule)"
  - "Add URLs to UX Framework References table; add ADR placeholder or PROJ-022 ADR paths"
  - "Add research provenance table tracing 10-framework selection to PROJ-022 research"
  - "Document tool tier access in Available Agents section; note plugin.json Wave 0 status"
  - "Expand Runtime Orchestration dispatch logic; specify Wave 0 acceptance test"
  - "Add ux-heuristic-evaluator Sonnet escalation trigger mechanism"
```

---

*Scored by: adv-scorer v1.0.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Reference pattern: `skills/eng-team/SKILL.md`*
*Scored: 2026-03-03*
