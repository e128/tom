# Quality Score Report: JTBD Sub-Skill SKILL.md (Iteration 6)

## L0 Executive Summary

**Score:** 0.940/1.00 | **Verdict:** REVISE (C4 threshold >= 0.95 not met; PASS at H-13 >= 0.92) | **Weakest Dimensions:** Methodological Rigor, Evidence Quality, Actionability, Traceability (all 0.93)

**One-line assessment:** Both iter6 fixes are verified correct (formula 14.0/9.5 and 7-column template/example match), resolving the iter5 regression; the artifact reaches 0.940 — above the H-13 gate (0.92) but short of the C4-specific 0.95 threshold due to four dimensions held at 0.93 by the planned/prospective methodology caveat and one unresolved broken reference.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/SKILL.md`
- **Deliverable Type:** Skill documentation (sub-skill SKILL.md)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Iteration:** 6 (final — score history: iter1=0.851, iter2=0.897, iter3=0.924, iter4=0.946, iter5=0.941, iter6=0.940)
- **Scored:** 2026-03-04T00:00:00Z
- **Prior Score:** 0.941 (iter5)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.940 |
| **H-13 Threshold** | 0.920 (C2+) |
| **C4 Threshold (invocation-specified)** | 0.950 |
| **H-13 Verdict** | PASS (>= 0.92) |
| **C4 Verdict** | REVISE (< 0.95) |
| **Iter6 Fixes Verified** | Yes — both fixes confirmed present and mathematically correct |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.95 | 0.190 | All 13 nav-table sections substantive; triple-lens, P-003, MCP, synthesis validation all present |
| Internal Consistency | 0.20 | 0.96 | 0.192 | Iter6 fixes verified: formula 14.0/9.5 correct; template and example both 7-column; no contradictions found |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | 5-phase methodology with explicit I/O; all three theoretical foundations cited; prospective "(planned)" caveat limits operational rigor |
| Evidence Quality | 0.15 | 0.93 | 0.1395 | Full academic citations for all 5 sources; validation thresholds concrete; secondary-research limitation acknowledged |
| Actionability | 0.15 | 0.93 | 0.1395 | Three invocation options with code; copy-paste template; worked example; 5 quick-reference workflows; decomposition criteria for multi-job engagements vague |
| Traceability | 0.10 | 0.93 | 0.093 | Full repo-relative paths for all cited files; AGENTS.md line/date confirmed; one broken link (handoff-v2.schema.json planned, not committed) |
| **TOTAL** | **1.00** | | **0.940** | |

---

## Detailed Dimension Analysis

### Completeness (0.95/1.00)

**Evidence:**
All 13 sections listed in the navigation table lead to substantive content:
- Purpose with key capabilities (6 capabilities enumerated) and AI-augmented caveat
- When-to-use with activation path, trigger keywords table, and "Do NOT use when" routing table
- Available Agents with tier, mode, model, and output location
- Invoking an Agent with three options and H-26(c) exception rationale
- P-003 Compliance with topology diagram and three enforcement mechanisms
- Methodology with 5-phase sequential workflow (Phase 1-5, each with purpose, inputs/activities, output)
- MCP Integration with dependency summary, Context7 usage table, and degraded mode
- Output Specification with location pattern, L0/L1/L2 structure, required sections table, full template, and worked example
- Cross-Framework Integration with three downstream handoff contracts and three ASCII workflow diagrams
- Synthesis Hypothesis Validation with confidence gate, validation methods table, and minimum thresholds
- Constitutional Compliance mapping 5 principles (P-001, P-002, P-003, P-020, P-022)
- Quick Reference with 5 common workflows and agent selection hints
- References with four sub-sections (agent files, parent skill files, standards, project traceability, JTBD framework references with 5 full citations)

**Gaps:**
- Agent stub caveat (lines 91 and 241) notes the `ux-jtbd-analyst.md` agent body sections are incomplete. This is a system-level incompleteness that the SKILL.md honestly discloses, but the described methodology is prospective. This is the principal reason this dimension does not reach 0.97+.

**Improvement Path:**
Remove or update the stub caveat once the agent definition `<methodology>`, `<input>`, `<capabilities>`, and `<output>` XML body sections are fully implemented in Wave 1.

---

### Internal Consistency (0.96/1.00)

**Evidence:**
Iter6 fixes verified against the stated formulas:

- **Formula stated** (line 365): "Importance + max(Importance - Satisfaction, 0)"
- **Step 1 worked example** (line 547): Importance=9.1, Satisfaction=4.2, Score=14.0
  - Math: 9.1 + max(9.1 - 4.2, 0) = 9.1 + 4.9 = 14.0. CORRECT.
- **Step 2 worked example** (line 548): Importance=7.8, Satisfaction=6.1, Score=9.5
  - Math: 7.8 + max(7.8 - 6.1, 0) = 7.8 + 1.7 = 9.5. CORRECT.
- **Priority alignment**: Step 1 = HIGH (14.0 highest), Step 2 = MEDIUM (9.5 moderate). Consistent with relative score ordering.

Template table column count (lines 497-506): 7 columns (Step, Universal Process, Domain-Specific Action, Importance, Satisfaction, Opportunity Score, Priority). Worked example table (lines 545-548): 7 columns. MATCH confirmed.

T3 tool tier declared in Available Agents section is consistent with the tools listed in YAML frontmatter (WebSearch and WebFetch present at lines 21-22). Confidence classification of MEDIUM in the Output Specification (lines 439-445) is consistent with the Synthesis Hypothesis Validation section (lines 607-626). H-26(c) exception rationale is internally consistent with the routing design described in the When-to-Use section.

**Gaps:**
No contradictions found. A minor stylistic inconsistency exists in the Output Specification table header: the template section header label is "Opportunity Score" while the formula cell uses `{importance + max(importance - satisfaction, 0)}` with lowercase variable names — this is cosmetic and not a logical contradiction.

**Improvement Path:**
Standardize variable case in formula cells (Importance/Satisfaction capitalized to match section headings). This is a polish item that would approach 0.97+.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**
- Three complementary theoretical frameworks are named and grounded with originators and publication years
- Job statement format is canonical with 4 explicit constraints (lines 268-271): goal-not-feature, solution-agnostic, stable-over-time, single-dimension
- Phase 2 job identification distinguishes functional/social/emotional job types with definitions and examples
- Phase 3 switch force analysis uses the formal four-forces model with the inequality expression (Push+Pull vs. Anxiety+Habit) and maps each force to evidence source types
- Phase 4 job mapping applies Ulwick's 8-step universal process with explicit step names
- Phase 4 outcome expectations follow Ulwick's three canonical formats: "Minimize the time it takes to...", "Minimize the likelihood of...", "Minimize the variability of..."
- Opportunity score formula is explicit and algebraically correct
- Synthesis Hypothesis Validation provides graduated confidence protocol with 4 validation methods and concrete thresholds

**Gaps:**
- All 5 methodology phases are marked "(planned -- target behavior)" (lines 276, 293, 313, 344, 369). While this is honest disclosure, it means the rigorous methodology is not yet operational. A reviewer cannot verify the agent actually executes this methodology. This limits the rigor score below 0.95.
- Phase 1 output (context brief) and Phase 2 output (draft job inventory) lack defined format specifications comparable to the Phase 5 output which feeds the final report template.

**Improvement Path:**
(1) Remove "(planned)" labels once the agent body sections are implemented. (2) Add brief format specifications for Phase 1 context brief and Phase 2 job inventory outputs.

---

### Evidence Quality (0.93/1.00)

**Evidence:**
JTBD Framework References section (lines 700-708) contains 5 complete citations:
- Christensen et al. (2016) *Competing Against Luck*, Harper Business — full bibliographic reference
- Christensen (2003) *The Innovator's Solution*, Harvard Business Review Press — foundational precursor
- Ulwick (2016) *Jobs to Be Done: Theory to Practice*, IDEA BITE PRESS with URL (https://jobs-to-be-done.com/)
- Moesta (2020) *Demand-Side Sales 101*, Lioncrest Publishing
- Moesta and Spiek (2014) *The Jobs-to-Be-Done Handbook*, Re-Wired Group; Klement (2016) *When Coffee and Kale Compete*

Theoretical Foundations table (lines 246-250) maps each approach to originator, year, core contribution, and application in this sub-skill.

Validation methods table (lines 621-626) provides concrete minimum thresholds:
- Switch interviews: "3-5 interviews with target segment"
- Support ticket analysis: "10+ tickets referencing the same job"
- Behavioral analytics: "Metric data supporting the job hypothesis" with specific example ("68% of users")

Worked example cites sources: "User interviews (3 participants)", "3 interview transcripts".

**Gaps:**
- The Synthesis Hypothesis Validation section claims expert review requires "Named expert with domain authority" but does not specify a minimum qualification standard. This is vaguer than the quantitative thresholds for the other validation methods.
- All JTBD synthesis outputs are MEDIUM confidence by default (secondary research). While this is the correct and honest classification, it means no evidence output from this sub-skill can be HIGH confidence without external validation — a structural limitation inherent to the AI-augmented approach.

**Improvement Path:**
Specify a minimum qualification criterion for expert reviewers (e.g., "2+ years product management or UX research with JTBD methodology application").

---

### Actionability (0.93/1.00)

**Evidence:**
Three invocation options are provided with fully populated examples:
- Option 1: 5 natural language command examples in code blocks
- Option 2: 3 explicit agent name request examples
- Option 3: Task tool invocation with complete Python code block including populated UX CONTEXT fields and TASK description

Output template (lines 452-528) is copy-paste ready with all 12 sections and explicit placeholder labels.

Worked example (lines 530-549) shows two populated Job Map rows with real numbers, confirming the template is not purely theoretical.

Quick Reference table (lines 643-659) provides 5 common workflows as verbatim command examples mapping need to command.

"Do NOT use when" table (lines 128-135) routes to 5 specific alternative sub-skills with "Why" explanations.

Downstream handoff contracts table (lines 558-564) provides key fields and use cases for 3 destination sub-skills.

Three ASCII workflow diagrams (lines 576-601) show canonical integration sequences.

**Gaps:**
- "Complex multi-job engagements are decomposed into multiple invocations by the `ux-orchestrator`, each targeting a specific job domain" (line 145) — no criteria are given for what makes an engagement "complex" or how to determine decomposition boundaries (e.g., how many jobs per invocation, how to scope a "specific job domain"). Practitioners would need to guess.

**Improvement Path:**
Add a decomposition guideline: "Decompose when more than 3 distinct main jobs are identified, or when job domains span distinct user segments (e.g., enterprise vs. SMB users). Each invocation targets one main job domain."

---

### Traceability (0.93/1.00)

**Evidence:**
Full references section with four sub-sections:
- Agent definition files: `skills/ux-jtbd/agents/ux-jtbd-analyst.md` and `.governance.yaml` with repo-relative paths
- Parent skill files: 6 rule files listed with full repo-relative paths (`ux-routing-rules.md`, `synthesis-validation.md`, `mcp-coordination.md`, `wave-progression.md`, `ci-checks.md`) plus parent `SKILL.md`
- Standards references: 5 standards files with H-rule numbers and repo-relative paths
- Project traceability: links to `PROJ-022/PLAN.md`, `EPIC-002`, and `ORCHESTRATION.yaml` with full repo-relative path

Source annotations throughout the body cite specific rule file sections (e.g., "Source: `skills/user-experience/rules/ux-routing-rules.md` [Stage Routing Table]" at line 109; "Source: `skills/user-experience/rules/ux-routing-rules.md` [Handoff Data Contracts]" at line 564).

AGENTS.md registration confirmed with specific line number and verification date: "line 307, Verified 2026-03-04" (line 212).

Constitutional Compliance table maps 5 principles to specific sub-skill application behaviors.

**Gaps:**
- `docs/schemas/handoff-v2.schema.json` is cited in the Cross-Framework Integration section (line 554) and in the Standards References table (line 690) as "(planned -- not yet committed to repository)". This is an honest disclosure, but the cross-framework integration content depends on a schema that does not yet exist, creating a forward-reference traceability gap.
- The JTBD framework citations do not include ISBNs, which would enable unambiguous verification of specific editions. Minor for a methodology document.

**Improvement Path:**
(1) Remove or update the handoff schema reference once `handoff-v2.schema.json` is committed. (2) Consider adding ISBNs for the JTBD framework book references for precision.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Methodological Rigor | 0.93 | 0.96 | Implement agent body sections (`<methodology>`, `<input>`, `<capabilities>`, `<output>`) in `ux-jtbd-analyst.md` so the methodology is operational, not prospective. Remove "(planned)" labels once implemented. |
| 2 | Completeness | 0.95 | 0.97 | Complete the agent stub (same as Priority 1 action); update deployment status note to reflect full implementation. |
| 3 | Traceability | 0.93 | 0.95 | Commit `docs/schemas/handoff-v2.schema.json` to the repository and update the cross-framework integration section to remove the "(planned)" qualifier. |
| 4 | Actionability | 0.93 | 0.95 | Add decomposition criteria for multi-job engagements (e.g., threshold of 3+ main jobs or distinct user segments triggers decomposition). |
| 5 | Evidence Quality | 0.93 | 0.95 | Add minimum qualification criterion for expert reviewer validation (currently underspecified relative to quantitative validation thresholds). |

---

## Iter6 Fix Verification

| Fix | Description | Expected | Actual | Status |
|-----|-------------|----------|--------|--------|
| Fix 1a | Opportunity Score Step 1 | 14.0 | 14.0 (line 547) | VERIFIED |
| Fix 1b | Opportunity Score Step 2 | 9.5 | 9.5 (line 548) | VERIFIED |
| Fix 1b-math | Step 2 formula: 7.8 + max(7.8-6.1,0) = 7.8 + 1.7 | 9.5 | 9.5 | VERIFIED |
| Fix 1c | Step 2 Priority | MEDIUM | MEDIUM (line 548) | VERIFIED |
| Fix 2a | Template Job Map column count | 7 columns | 7 columns (lines 497-506) | VERIFIED |
| Fix 2b | Worked example Job Map column count | 7 columns | 7 columns (lines 545-548) | VERIFIED |
| Fix 2c | Template-example column header match | Match | Match (both: Step, Universal Process, Domain-Specific Action, Importance, Satisfaction, Opportunity Score, Priority) | VERIFIED |

---

## Score Progression

| Iteration | Score | Delta | Key Change |
|-----------|-------|-------|------------|
| iter1 | 0.851 | baseline | Initial draft |
| iter2 | 0.897 | +0.046 | Major structural improvements |
| iter3 | 0.924 | +0.027 | Evidence quality and traceability improvements |
| iter4 | 0.946 | +0.022 | Completeness and actionability improvements |
| iter5 | 0.941 | -0.005 | Regression: worked example formula errors + column mismatch introduced |
| iter6 | 0.940 | -0.001 | Both iter5 defects fixed; score stabilizes; regression fully repaired |

**Score plateau analysis:** The 0.001 decrease from iter5 to iter6 (despite fixes) reflects that iter5's regression had already penalized internal consistency, and iter6's fixes restore consistency to 0.96 — but the other four dimensions held at 0.93 (same as iter5) represent a structural ceiling from the planned/prospective methodology nature and the handoff schema gap. These are not fixable by document edits to SKILL.md alone; they require external deliverables (agent implementation, schema commit).

---

## Verdict Clarification

**Two thresholds apply to this deliverable:**

| Gate | Threshold | Score | Verdict |
|------|-----------|-------|---------|
| H-13 (SSOT, C2+) | >= 0.920 | 0.940 | **PASS** |
| C4 invocation-specified | >= 0.950 | 0.940 | **REVISE** |

The artifact passes the authoritative H-13 quality gate defined in `.context/rules/quality-enforcement.md`. It does not reach the stricter C4 threshold specified in the scoring invocation. The remaining 0.010 gap to 0.95 is attributable to four dimensions each at 0.93 — all of which require work external to this SKILL.md (agent body implementation and schema commit) to advance.

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with line-number citations
- [x] Uncertain scores resolved downward (borderline cases rounded to 0.93, not 0.94)
- [x] Iter6 fixes verified with explicit arithmetic before scoring Internal Consistency
- [x] No dimension scored above 0.96 — Completeness 0.95 and Internal Consistency 0.96 both have specific evidence and clear remaining gap documented
- [x] Score progression table reviewed to calibrate iter6 against prior iterations
- [x] C4 threshold (0.95) applied strictly; SSOT H-13 threshold (0.92) applied separately for H-13 verdict

---

*Score Report Version: iter6*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-jtbd/SKILL.md`*
*Created: 2026-03-04*
