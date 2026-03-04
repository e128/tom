# Quality Score Report: ux-jtbd-analyst.md (iter1)

## L0 Executive Summary
**Score:** 0.844/1.00 | **Verdict:** REVISE | **Weakest Dimensions:** Completeness (0.78), Traceability (0.78)
**One-line assessment:** Strong JTBD methodology and internal consistency, but three MEDIUM standard gaps (session_context, reasoning_effort, allowed_tools absent from governance.yaml) and a self-acknowledged STUB status in the companion file block acceptance at C4 threshold.

---

## Scoring Context
- **Deliverable:** skills/ux-jtbd/agents/ux-jtbd-analyst.md
- **Companion Governance:** skills/ux-jtbd/agents/ux-jtbd-analyst.governance.yaml
- **Deliverable Type:** Agent Definition (dual-file: .md + .governance.yaml)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** .context/rules/quality-enforcement.md
- **C4 Threshold:** >= 0.95
- **Scored:** 2026-03-04

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.844 |
| **C4 Threshold** | 0.95 |
| **Standard C2+ Threshold** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.78 | 0.156 | 7/7 XML sections present; H-34/H-35 HARD requirements met; but session_context, reasoning_effort, allowed_tools absent from governance; STUB annotation self-acknowledges incompleteness |
| Internal Consistency | 0.20 | 0.90 | 0.180 | No contradictions; tools/tier/mode all aligned; minor truncation: .md has 5 expertise items, governance.yaml has 3 |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | Christensen/Ulwick/Moesta correctly cited; ODI formula accurate; 8-step process correct; opportunity score max stated as 20 (mathematical max on 1-10 scales is 19) |
| Evidence Quality | 0.15 | 0.82 | 0.123 | Theorists accurately named and attributed; synthesis-validation.md reference plausible but unverifiable; no specific publication citations (book titles, paper years) |
| Actionability | 0.15 | 0.87 | 0.1305 | Clear 5-phase workflow with numbered steps; output schema explicit; formulas computable; gap: no worked example, hiring criteria weighting is descriptive not procedural |
| Traceability | 0.10 | 0.78 | 0.078 | HARD rules traceable; session_context in .md output section but absent from governance.yaml (AD-M-007 gap); ET-M-001 (reasoning_effort) untraceable; STUB declaration marks governance as intentionally incomplete |
| **TOTAL** | **1.00** | | **0.844** | |

---

## Detailed Dimension Analysis

### Completeness (0.78/1.00)

**Evidence — what IS present:**
- All 7 required XML-tagged sections: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>` — all populated with substantive content.
- H-34 required .md frontmatter fields: `name`, `description`, `model`, `tools`, `disallowedTools`, `mcpServers` — all present.
- H-34 required governance fields: `version: 1.0.0`, `tool_tier: T3`, `identity.role`, `identity.expertise` (3 items, meets minItems: 2), `identity.cognitive_mode: divergent`.
- H-35 requirements: `constitution.principles_applied` (5 entries including P-003, P-020, P-022); `capabilities.forbidden_actions` (exactly 3 entries with NPT-009-complete format).
- AD-M-004 output levels: L0, L1, L2 declared in governance.yaml.
- AD-M-006 persona: tone, communication_style, audience_level present.
- AD-M-008 post_completion_checks: 4 entries present.
- AD-M-002 semantic versioning: 1.0.0 correct pattern.

**Gaps:**

1. **AD-M-007 (SHOULD): `session_context` absent from governance.yaml.** The `<output>` section of the .md defines a "Session context on send" YAML block, but the companion governance.yaml has no `session_context` object with `on_receive` / `on_send`. AD-M-007 states agents SHOULD declare this in governance. For a C4 agent operating in an orchestrator-worker topology, this is a meaningful gap.

2. **ET-M-001 (SHOULD): `reasoning_effort` absent from governance.yaml.** ET-M-001 maps C4=max for reasoning effort. No `reasoning_effort` field is declared. For a C4 agent, the expected value is `max`. This omission means the agent will use default reasoning depth rather than the criticality-appropriate allocation.

3. **AD-M-010 (SHOULD): `capabilities.allowed_tools` absent from governance.yaml.** The agent uses Context7 MCP (T3 tier, declared in .md mcpServers) but does not declare `capabilities.allowed_tools` in the governance file. AD-M-010 states research/documentation agents SHOULD declare MCP tool usage here.

4. **STUB annotation in governance.yaml (line 4):** `"# STUB: Minimal governance for PROJ-022 Wave 1. Full implementation in EPIC-002."` This is an explicit self-declaration that the governance file is incomplete. While honest (P-022 compliant), it means the governance file does not represent a complete agent definition at the time of scoring.

5. **expertise truncation:** .md `<identity>` lists 5 expertise items; governance.yaml lists only 3. The 4th ("Demand-side innovation strategy and competitive job analysis") and 5th ("Outcome-Driven Innovation (ODI) opportunity scoring") items from the .md are absent from the governance yaml, reducing the machine-readable routing signal quality (AD-M-005).

**Improvement Path:**
- Add `session_context.on_receive` and `session_context.on_send` arrays to governance.yaml per AD-M-007.
- Add `reasoning_effort: max` to governance.yaml per ET-M-001.
- Add `capabilities.allowed_tools` listing Context7 tools per AD-M-010.
- Add all 5 expertise items to governance.yaml `identity.expertise`.
- Remove or update the STUB comment once all gaps are closed.

---

### Internal Consistency (0.90/1.00)

**Evidence — consistent claims:**
- Tool tier: governance.yaml declares `tool_tier: T3`. The .md `tools` list includes WebSearch and WebFetch (External tools), which is exactly what T3 adds over T2. Fully consistent.
- Tool restriction: `disallowedTools: [Task]` in .md frontmatter, and governance `forbidden_actions[0]` explicitly prohibits Task tool use. P-003 runtime self-check in `<guardrails>` reiterates this. Three-way consistency.
- Cognitive mode: `cognitive_mode: divergent` in governance.yaml; `<identity>` declares "Cognitive Mode: Divergent" and correctly explains the wide-search reasoning pattern. Consistent.
- Model selection: `model: sonnet` in .md, consistent with ux-jtbd SKILL.md which also declares `model: sonnet`. Consistent.
- Confidence default: `<purpose>` states "MEDIUM synthesis confidence by default"; `<methodology>` Phase 5 step 4 defines MEDIUM as default; guardrails output_filtering includes `all_job_statements_must_have_confidence_classification`. Three-way consistent.
- P-003 compliance: declared in governance `constitution.principles_applied`, enforced via `forbidden_actions[0]`, operationalized in `<guardrails>` P-003 Runtime Self-Check. Fully consistent.

**Minor inconsistencies:**
- .md `<identity>` lists 5 expertise items; governance.yaml `identity.expertise` lists 3 items. Not a contradiction (the 3 are a subset of 5) but a truncation that could cause inconsistency if the governance is used as the routing authority.
- The methodology is a 5-phase sequential workflow — this is more "systematic" in structure than "divergent." However, the `<identity>` section explicitly addresses this: "On each iteration you expand the search space rather than narrowing it, surfacing more candidate jobs before convergence happens downstream." The divergent mode refers to the internal reasoning pattern within each phase, not the phase structure. This explanation resolves the apparent tension. No true contradiction.

**Gaps:** None that constitute contradictions.

**Improvement Path:**
- Synchronize expertise list between .md and governance.yaml (add all 5 items to governance).

---

### Methodological Rigor (0.88/1.00)

**Evidence — correct methodology:**
- **Christensen JTBD theory:** Correctly represented as demand-side innovation, jobs as the unit of analysis, "hiring" metaphor used appropriately in Phase 5 ("hiring criteria" for "hiring a product"). CHECK.
- **Ulwick ODI methodology:** Phase 4 correctly implements the 8-step Universal Job Process (Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude). The opportunity scoring formula `Importance + max(Importance - Satisfaction, 0)` is Ulwick's canonical ODI formula. Outcome statement formats ("Minimize the time it takes to", "Minimize the likelihood of", "Minimize the variability of") match Ulwick's canonical outcome language. CHECK.
- **Moesta/Spiek Four Forces:** Phase 3 correctly identifies Push (pain/frustration), Pull (attraction to new), Anxiety (uncertainty about new), Habit (comfort with current). The switch condition `PUSH + PULL > ANXIETY + HABIT` is correctly stated. Evidence sources mapped to appropriate forces (negative reviews → push, positive competitor reviews → pull, FAQ pages → anxiety, integration depth → habit). CHECK.
- **Job statement format:** "When I am [situation], I want to [motivation], so I can [expected outcome]" — canonical three-part format (situation, motivation, outcome). Constraints are correctly stated: solution-agnostic, stable, single-dimension. CHECK.
- **Job type taxonomy:** Functional / Social / Emotional jobs correctly distinguished with correct definitional questions ("What is the user trying to get done?", "How does the user want to appear?", "How does the user want to feel?"). CHECK.
- **Job cluster taxonomy:** Main jobs / Related jobs / Consumption chain jobs correctly distinguished. CHECK.
- **5-phase workflow:** Context Gathering → Job Identification → Switch Force Analysis → Job Mapping → Job Statement Synthesis. This is a coherent, theoretically grounded workflow that would produce a genuine JTBD analysis.

**Gaps:**

1. **Opportunity score maximum precision:** Phase 4 states "Scores range from 1 to 20." With Importance and Satisfaction on a 1-10 scale, the mathematical maximum is: Importance=10, Satisfaction=1 → 10 + max(10-1, 0) = 10 + 9 = 19. The stated maximum of 20 is off by 1. This is a minor precision issue — common in JTBD literature which sometimes approximates — but at C4 quality level it should be exact.

2. **Opportunity score minimum precision:** The stated minimum is 1. With Importance=1, Satisfaction=10 → 1 + max(1-10, 0) = 1 + 0 = 1. This is correct.

3. **Hiring criteria weighting in Phase 5:** The agent is instructed to identify "deal-breakers vs. nice-to-haves" but no formal weighting methodology is specified (e.g., pairwise comparison, MoSCoW, weighted scoring). The output section lists "Hiring Criteria" with "criterion table with measurement and weight" but the methodology for determining the weight is left implicit.

**Improvement Path:**
- Correct opportunity score range to "1 to 19" or add a note that 20 is theoretical only with 0-10 scales.
- Add a sub-step to Phase 5 with a concrete weighting methodology for hiring criteria (e.g., relative importance weighting: each criterion assigned a percentage summing to 100%).

---

### Evidence Quality (0.82/1.00)

**Evidence — accurate citations:**
- **Clayton Christensen:** Named as JTBD theory originator. Correct — Christensen developed JTBD theory, formalized in "The Innovator's Solution" (2003) and "Competing Against Luck" (2016).
- **Tony Ulwick:** Named as ODI methodology author. Correct — Ulwick developed Outcome-Driven Innovation and the Universal Job Process, documented in "Jobs to Be Done: Theory to Practice" (2016).
- **Bob Moesta / Chris Spiek:** Named for the four forces (switch interview) framework. Correct — Moesta and Spiek developed the switch interview methodology, documented in "Demand-Side Sales 101" and related work.
- **ODI opportunity formula:** Mathematically verifiable — `Importance + max(Importance - Satisfaction, 0)` is Ulwick's published formula.
- **8-step Universal Job Process:** The eight steps (Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude) match Ulwick's published universal job process.

**Gaps:**

1. **No specific publication citations.** The agent names theorists correctly but does not cite specific books or papers. This is acceptable for a practitioner tool but reduces traceability for claims like "8-step universal process" or "canonical outcome formats." A reviewer cannot verify methodology alignment without knowing the specific source.

2. **`skills/user-experience/rules/synthesis-validation.md` reference unverifiable.** Phase 5 step 4 and fallback behavior both reference this file. The file existence cannot be confirmed from available information. If it does not exist, confidence classification guidance would be missing.

3. **Competitive evidence sources are prescriptive but not cited.** Phase 1 instructs using "app store reviews, social media mentions, industry reports" but these are generic categories, not specific sources or methodologies.

4. **No cross-references to analogous Jerry skill implementations.** The agent definition does not reference how similar evidence quality standards are applied in comparable skills (e.g., /adversary or /problem-solving), which would strengthen its methodological pedigree within the framework.

**Improvement Path:**
- Add at minimum one specific publication reference per theorist in the identity/purpose section (e.g., "Ulwick ODI — documented in 'Jobs to Be Done: Theory to Practice' (2016)").
- Verify existence of `skills/user-experience/rules/synthesis-validation.md` and add a fallback if absent.

---

### Actionability (0.87/1.00)

**Evidence — clear execution path:**
- The 5-phase methodology provides explicit numbered sub-steps within each phase. An LLM executing this agent could follow the workflow without ambiguity for Phases 1-4.
- Input format specification with required/optional fields and format example enables clean intake.
- Output file path template (`skills/ux-jtbd/output/{engagement-id}/ux-jtbd-analyst-{topic-slug}.md`) is concrete and follows the UX-{NNNN} convention.
- Required output sections table (10 sections with content descriptions) gives clear deliverable structure.
- Opportunity score formula is explicitly computable: `Importance + max(Importance - Satisfaction, 0)`.
- Force balance rating scale (1-5 with definitions for 1, 3, 5) is operationalizable.
- Self-review checkpoint (8 items) is verifiable — each item is a binary check.
- Session context on send provides the exact YAML structure for the handoff.
- Fallback behaviors for 4 failure modes cover the main edge cases.

**Gaps:**

1. **No worked example.** The SKILL.md references theoretical foundations and worked examples, but the agent definition itself contains no sample job statement, sample opportunity score calculation, or sample force analysis. A first-time LLM executor would need to load SKILL.md for examples, adding a dependency.

2. **Hiring criteria weighting is descriptive.** Phase 5 step 2 says "Which criteria are deal-breakers vs. nice-to-haves?" but provides no numeric methodology. The output section requires a "Criterion table with measurement and weight" — but Phase 5 does not specify how to derive the `weight` column.

3. **Job ranking in Phase 5 step 3** uses three inputs (opportunity score, force balance, job frequency), but does not specify how to combine them into a ranking. If two jobs tie on opportunity score but differ on force balance, there is no tie-breaking rule.

**Improvement Path:**
- Add inline worked examples for job statement format and opportunity score calculation (even brief ones).
- Add a concrete weighting sub-step to Phase 5 (e.g., assign relative weight 1-10 per criterion, normalize to 100%).
- Add explicit tie-breaking rule to Phase 5 job ranking.

---

### Traceability (0.78/1.00)

**Evidence — traceable elements:**
- Footer explicitly cites: PROJ-022, Wave 1, constitutional compliance, parent skill, sub-skill, creation date. Full project traceability.
- `<guardrails>` Constitutional Compliance table maps each principle (P-003, P-020, P-022, P-001, P-002) to specific agent behavior. CHECK.
- `<guardrails>` Forbidden Actions cite principle references by ID (P-003 VIOLATION, P-020 VIOLATION, P-022 VIOLATION, P-001 VIOLATION). CHECK.
- `constitution.principles_applied` in governance.yaml maps each principle to behavioral description. CHECK.
- Tool tier T3 traceable to agent-development-standards.md Tool Security Tiers section. CHECK.
- Cognitive mode `divergent` traceable to Cognitive Mode Taxonomy. CHECK.
- Output levels L0/L1/L2 traceable to AD-M-004. CHECK.
- Post-completion checks traceable to AD-M-008. CHECK.

**Gaps:**

1. **AD-M-007 compliance untraceable at CI level.** The session context on send block in `<output>` cannot be automatically validated against `docs/schemas/handoff-v2.schema.json` because it is embedded in the .md markdown body, not in the governance.yaml `session_context` field. The governance schema's `session_context` property (`on_receive`, `on_send`) exists for this purpose, but is unpopulated. An L5 CI check cannot validate handoff protocol compliance.

2. **ET-M-001 (reasoning_effort) has no traceability.** The field is absent from governance.yaml. For a C4 agent with `reasoning_effort: max` expected, this is a missing traceability link.

3. **STUB declaration breaks completeness traceability.** The governance.yaml header states "Full implementation in EPIC-002" — which means current governance does not fully represent the intended design. Traceability to the full requirements set is deferred.

4. **`skills/user-experience/rules/synthesis-validation.md` traceability unverifiable.** Referenced in Phase 5 and fallback behavior. If this file does not exist, the confidence classification methodology has a broken traceability chain.

**Improvement Path:**
- Move/add session context to governance.yaml `session_context.on_send` and add `session_context.on_receive` per AD-M-007.
- Add `reasoning_effort: max` to governance.yaml per ET-M-001.
- Verify synthesis-validation.md exists; create it if needed.
- Remove STUB comment once all gaps are resolved.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness | 0.78 | 0.90+ | Add `session_context.on_receive` and `session_context.on_send` to governance.yaml per AD-M-007. Add `reasoning_effort: max` per ET-M-001. Add `capabilities.allowed_tools` listing Context7 tools per AD-M-010. |
| 2 | Completeness | 0.78 | 0.90+ | Add all 5 expertise items to governance.yaml `identity.expertise` (currently only 3 of 5 are present). Remove STUB comment once complete. |
| 3 | Traceability | 0.78 | 0.88+ | Populate governance.yaml `session_context` block to enable L5 CI validation of handoff protocol compliance. |
| 4 | Methodological Rigor | 0.88 | 0.93+ | Correct opportunity score range from "1 to 20" to "1 to 19" (mathematical precision on 1-10 scales). Add concrete weighting methodology for hiring criteria in Phase 5. |
| 5 | Evidence Quality | 0.82 | 0.90+ | Add specific publication citations for Christensen, Ulwick, and Moesta/Spiek. Verify existence of `skills/user-experience/rules/synthesis-validation.md`. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific file line references
- [x] Uncertain scores resolved downward (Completeness: 0.78 not 0.82; Traceability: 0.78 not 0.82)
- [x] STUB annotation in governance.yaml treated as a real completeness gap, not a minor comment
- [x] No dimension scored above 0.95 — highest is Internal Consistency at 0.90, supported by verified evidence
- [x] C4 calibration applied: 0.844 composite correctly placed in REVISE band; C4 threshold of 0.95 was NOT lowered to standard 0.92

---

## Session Context (adv-scorer -> orchestrator)

```yaml
verdict: REVISE
composite_score: 0.844
threshold: 0.95
weakest_dimension: completeness
weakest_score: 0.78
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add session_context.on_receive/on_send to governance.yaml (AD-M-007)"
  - "Add reasoning_effort: max to governance.yaml (ET-M-001)"
  - "Add capabilities.allowed_tools to governance.yaml (AD-M-010)"
  - "Sync expertise list: add items 4 and 5 to governance.yaml identity.expertise"
  - "Correct opportunity score range to 1-19 (methodological precision)"
  - "Add specific publication citations for Christensen/Ulwick/Moesta-Spiek"
  - "Add session_context block to governance.yaml for L5 CI validation"
```

---

*Scored by: adv-scorer (S-014 LLM-as-Judge)*
*Constitutional Compliance: P-003 (no subagents), P-020 (user authority), P-022 (no deception — leniency bias actively counteracted)*
*SSOT: .context/rules/quality-enforcement.md*
*Artifact: skills/ux-jtbd/agents/ux-jtbd-analyst.md + skills/ux-jtbd/agents/ux-jtbd-analyst.governance.yaml*
