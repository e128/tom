# Quality Score Report: UX Routing Rules (Iteration 2)

## L0 Executive Summary

**Score:** 0.863/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.78)

**One-line assessment:** The routing rules file is functionally complete and well-structured, but two real internal inconsistencies — a missing WAVE-5-SIGNOFF.md entry in the Wave State Detection table, and a mismatch between the "< 20% capacity -> Wave 1 only" recommendation and the Free cost tier that actually spans Waves 1-4 — must be resolved before the file can pass the C4 threshold of 0.95.

---

## Scoring Context

- **Deliverable:** `skills/user-experience/rules/ux-routing-rules.md`
- **Deliverable Type:** Rule File (Routing Logic)
- **Criticality Level:** C4 (architecture/governance artifact for the /user-experience skill)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Authoritative Source:** `skills/user-experience/SKILL.md` (Lifecycle-Stage Routing, Wave Architecture, Cross-Sub-Skill Handoff Data)
- **Sibling Rules Cross-Referenced:** `wave-progression.md`, `synthesis-validation.md`, `mcp-coordination.md`
- **Scored:** 2026-03-04T00:00:00Z
- **Iteration:** 2

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.863 |
| **C4 Threshold** | 0.95 |
| **Standard Threshold (H-13)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (standalone scoring) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.87 | 0.174 | All 10 sub-skills routable; CRISIS, bypass, handoff, no-match all present; minor gap: multi-sub-skill audit path implicit only |
| Internal Consistency | 0.20 | 0.78 | 0.156 | Two real inconsistencies: WAVE-5-SIGNOFF.md absent from Wave State Detection table; capacity check "Wave 1 only" conflicts with Free tier that includes Wave 4 sub-skills |
| Methodological Rigor | 0.20 | 0.88 | 0.176 | 4-step triage is systematic; agent-routing-standards.md protocol applied; P-020/P-022 compliance points correct; minor gap: session state flag mechanism undefined |
| Evidence Quality | 0.15 | 0.90 | 0.135 | VERSION header with source section list; per-section HTML source comments; specific SKILL.md section citations throughout |
| Actionability | 0.15 | 0.88 | 0.132 | Verbatim ONBOARD warning, specific capacity threshold, verbatim bypass prompt, step-by-step CRISIS entry; minor gap: session state flag implementation not specified |
| Traceability | 0.10 | 0.90 | 0.090 | VERSION header, per-section source comments, sibling rule footer; Bypass Documentation sub-section lacks its own source comment (parent section comment covers it) |
| **TOTAL** | **1.00** | | **0.863** | |

---

## Detailed Dimension Analysis

### Completeness (0.87/1.00)

**Evidence:**

All 10 sub-skills appear in the routing table or as explicit routes. The Stage Routing Table covers:
- Wave 1: `/ux-jtbd` (Before design: Don't know what to build), `/ux-heuristic-eval` (During design: Iterating)
- Wave 2: `/ux-lean-ux` (During design: Iterating — hypothesis path), `/ux-heart-metrics` (After launch: Measure UX health)
- Wave 3: `/ux-atomic-design` (During design: Building component system), `/ux-inclusive-design` (Any stage: Check accessibility)
- Wave 4: `/ux-kano-model` (Before design: Need to prioritize features), `/ux-behavior-design` (After launch: Users not completing action)
- Wave 5: `/ux-design-sprint` (Before design: Need validated prototype), `/ux-ai-first-design` (During design: Building AI product) — CONDITIONAL criteria (Enabler DONE + WSM >= 7.80) present

CRISIS routing covers a fixed 3-skill sequence (Heuristic Eval → Behavior Design → HEART) with entry keywords, confirmation prompt, execution table, rationale, and synthesis output specification.

Wave-aware routing provides Wave State Detection table and Routing Behavior for Unavailable Sub-Skills with a 3-step fallback.

Bypass Routing provides verbatim bypass prompt, full documentation structure table, and bypass constraints including cumulative ceiling.

Cross-Sub-Skill Handoff defines 6 data contracts matching the 6 entries in SKILL.md [Cross-Sub-Skill Handoff Data], with handoff validation steps.

Common Intent Resolution maps 7 natural-language patterns. No-match fallback provides a 3-step escalation. Ambiguity Resolution Protocol cites and applies agent-routing-standards.md Multi-Skill Combination ordering.

**Gaps:**

1. The "Comprehensive UX audit" multi-sub-skill workflow (Heuristic Eval + HEART Metrics) is mentioned in Common Intent Resolution as a route but the orchestrator execution path for non-CRISIS multi-sub-skill routing is handled implicitly by the Ambiguity Resolution ordering protocol rather than by an explicit multi-sub-skill routing section. This is technically covered but requires inference; an explicit "Multi-Sub-Skill Routing" section analogous to CRISIS would raise completeness.

2. The ONBOARD warning is specified for "first invocation per session" but what constitutes a session boundary is not defined in this file. This is a minor gap — it may be defined in the ux-orchestrator agent definition, but the routing rules file does not cross-reference it.

**Improvement Path:**

Add an explicit "Multi-Sub-Skill Routing" section for non-CRISIS scenarios (e.g., "Comprehensive UX audit") with the same structure as CRISIS: entry trigger, execution sequence, handoff artifacts. Define "session" and the session state flag mechanism, or add a cross-reference to where it is defined.

---

### Internal Consistency (0.78/1.00)

**Evidence:**

The CRISIS stage is labeled "W1→W4→W2" in the Stage Routing Table, which correctly corresponds to the CRISIS Execution Sequence: Heuristic Eval (Wave 1), Behavior Design (Wave 4), HEART Metrics (Wave 2). Consistent.

The Bypass Prompt and Bypass Documentation sections are internally consistent with each other and with wave-progression.md [Bypass Mechanism].

The Cross-Sub-Skill Handoff data contracts (6 pairs) match the 6 entries in SKILL.md [Cross-Sub-Skill Handoff Data] exactly. Consistent.

**Gaps (real inconsistencies):**

**Inconsistency 1 — Missing WAVE-5-SIGNOFF.md in Wave State Detection table:**

`ux-routing-rules.md` [Wave State Detection] lists 5 signoff files (KICKOFF-SIGNOFF.md through WAVE-4-SIGNOFF.md). `wave-progression.md` [Signoff File Locations] lists 6 signoff files (KICKOFF-SIGNOFF.md through WAVE-5-SIGNOFF.md). The routing rules file is missing the WAVE-5-SIGNOFF.md row, which would indicate "All waves complete" state. This is a functional gap: an orchestrator using only the routing rules file would have no detection logic for full Wave 5 completion.

Specific location: `ux-routing-rules.md` line 134 — table ends at `WAVE-4-SIGNOFF.md` with "Wave 4 complete; Wave 5 authorized". No row for WAVE-5-SIGNOFF.md.

**Inconsistency 2 — Capacity check "Wave 1 only" vs. Free cost tier spanning Waves 1-4:**

`ux-routing-rules.md` [Lifecycle Stage Router] Step 2 (CAPACITY CHECK) states: "If < 20% of one person's time: recommend Wave 1 sub-skills only and display cost tier 'Free ($0)'."

However, `mcp-coordination.md` [Cost Tiers] defines the Free tier as: "HEART, JTBD, Kano, Behavior Design (+ Storybook for Atomic Design)." This includes Wave 4 sub-skills (Kano, Behavior Design) and Wave 2 (HEART Metrics) — not just Wave 1 (JTBD, Heuristic Eval).

The routing rules file links "< 20% capacity" to both "Wave 1 only" and "Free ($0)" as if these are equivalent. They are not: the Free tier covers more sub-skills than Wave 1. The orchestrator should recommend either "Wave 1 sub-skills only" (a wave-gate restriction) OR "Free-tier sub-skills" (a cost-tier restriction), but these are not the same set and the file conflates them.

**Improvement Path:**

Fix 1: Add WAVE-5-SIGNOFF.md row to Wave State Detection table: "WAVE-5-SIGNOFF.md | Wave 5 complete; all waves deployed."

Fix 2: Resolve the capacity check / cost tier conflict. Either (a) change the recommendation to "recommend Free-tier sub-skills (JTBD, HEART, Kano, Behavior Design, Atomic Design with Storybook)" if the intent is cost-based guidance, or (b) keep "Wave 1 sub-skills only" but change the cost tier reference to "Free tier covers these and more — teams can access Free-tier Wave 2-4 sub-skills if wave gates are met", or (c) define a capacity-based sub-skill recommendation that is distinct from the cost tier. Verify the intended business logic with SKILL.md author and document the resolution.

---

### Methodological Rigor (0.88/1.00)

**Evidence:**

The 4-step lifecycle triage (ONBOARD → CAPACITY CHECK → MCP CHECK → STAGE TRIAGE) is a well-defined sequential protocol that matches SKILL.md [Lifecycle-Stage Routing] exactly. Each step has a clear trigger condition, decision branch, and outcome.

The Ambiguity Resolution Protocol explicitly applies agent-routing-standards.md [Multi-Skill Combination] ordering protocol (content before quality, work before presentation), which is the appropriate cross-reference for this type of routing decision.

H-31 is properly cited as the fallback when ordering does not resolve ambiguity: "ask the user per H-31 with a structured question presenting the matched sub-skills and their purposes." This is correct application.

P-020 compliance points are correctly identified at CAPACITY CHECK (user decides whether to accept recommendation), CRISIS entry (user confirms entry), and Bypass Prompt (user approves each bypass). These match the constitutional requirement that the user decides at each decision point.

P-022 compliance points are correctly identified at MCP CHECK (disclose status to user) and Wave-Aware Routing (inform user when sub-skill is unavailable). P-022 is also applied in No-match Fallback: "acknowledge the gap transparently per P-022."

CRISIS execution sequence follows the evaluate-diagnose-measure pattern with documented rationale, which represents sound UX research methodology.

Handoff Validation provides 3 explicit checks (artifact existence, key fields, confidence propagation) that are operationalizable.

Wave State Caching defines 3 cache invalidation conditions, which prevents stale state routing errors.

**Gaps:**

The session state flag for ONBOARD is mentioned ("first invocation per session via session state flag") but the flag storage mechanism, reset condition, and state representation are not defined. An implementer of the ux-orchestrator agent cannot determine from this file alone how to implement the session state flag. This reduces methodological completeness for the ONBOARD step specifically.

**Improvement Path:**

Add a subsection "Session State Management" to the Lifecycle Stage Router section defining: (a) the session state flag name and type (e.g., `onboard_displayed: boolean`), (b) storage location (in-memory during engagement, reset at new engagement ID), and (c) the reset condition. Alternatively, add a cross-reference to where this is defined in the ux-orchestrator agent definition.

---

### Evidence Quality (0.90/1.00)

**Evidence:**

VERSION header is present and complete: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "Lifecycle-Stage Routing", "Wave Architecture", "Cross-Sub-Skill Handoff Data" | PARENT: /user-experience skill -->`. This provides version, date, specific source sections, and parent skill — all required for governance artifact traceability.

Per-section HTML source comments are present for all major sections:
- `<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — 4-step sequential triage. -->` (Lifecycle Stage Router)
- `<!-- Source: agent-routing-standards.md ... Section "Multi-Skill Combination" — ordering protocol applied to UX sub-skill routing. -->` (Ambiguity Resolution Protocol)
- `<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Section "Lifecycle-Stage Routing" — common intent patterns derived from Stage Routing Table. -->` (Common Intent Resolution)
- `<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — CRISIS mode. -->` (CRISIS Routing)
- `<!-- Source: SKILL.md Section "Wave Architecture" — wave-gated deployment. -->` (Wave-Aware Routing)
- `<!-- Source: SKILL.md Section "Wave Architecture" — bypass mechanism. -->` (Bypass Routing)
- `<!-- Source: SKILL.md Section "Cross-Sub-Skill Handoff Data". -->` (Cross-Sub-Skill Handoff)

Wave State Detection also has a detailed source comment citing both the Wave Architecture section and two cross-references to wave-progression.md sub-sections.

Cost tier reference in CAPACITY CHECK correctly cites `skills/user-experience/rules/mcp-coordination.md [Cost Tiers]` with anchor link format.

Constitutional principle citations (P-020, P-022) are specific to behavioral application, not generic.

**Gaps:**

The source annotations are consistent but the Wave State Caching source comment cites SKILL.md and wave-progression.md, while the caching rules in wave-progression.md [State Caching] are identical to those in ux-routing-rules.md [Wave State Caching] — this is intentional duplication but the source comment could note it is authoritative at this location or defer to wave-progression.md as the authoritative source.

**Improvement Path:**

Minor: clarify in the Wave State Caching source comment whether this section is the authoritative source or whether wave-progression.md [State Caching] is, to avoid future maintenance drift. No score-blocking gap.

---

### Actionability (0.88/1.00)

**Evidence:**

Each of the 4 triage steps is described with sufficient detail for direct implementation:

ONBOARD: Verbatim warning text is provided ("AI-generated UX analysis reflects training data patterns, not your specific users..."). The condition for display is defined (first invocation per session).

CAPACITY CHECK: Specific quantitative threshold (< 20% of one person's time) with binary branching. User decision point explicitly called out per P-020.

MCP CHECK: Specific probe mechanism (lightweight Context7 resolve call). Two outcomes with specific actions (route to fallback or proceed). Disclosure requirement per P-022 is actionable ("Disclose MCP status to user").

STAGE TRIAGE: The Stage Routing Table provides complete routing information: intent, destination sub-skill, wave, and qualification question for each ambiguous case. The AI-First Design conditional criteria (Enabler DONE + WSM >= 7.80) are specific and checkable.

CRISIS: Entry keywords are listed verbatim. Confirmation prompt is verbatim. Execution sequence table has Step, Sub-Skill, Purpose, and Handoff to Next — fully implementable.

Bypass Prompt: The full prompt text is provided, ready to paste verbatim into the orchestrator methodology. Bypass Documentation structure is a complete field list.

No-match Fallback: 3 escalation steps with specific actions at each level.

Handoff Validation: 3 explicit checks that the orchestrator performs at each transition, each with a concrete verification action.

**Gaps:**

The ONBOARD session state flag mechanism is not specified (same gap as Methodological Rigor). An implementer reading only this file cannot determine how to implement "first invocation per session" — there is no definition of what a "session" is in this context (engagement ID, new Task call, session restart?).

**Improvement Path:**

Specify the session state flag: what variable/field tracks whether ONBOARD has been displayed, what its scope is (engagement session vs. orchestrator invocation), and where it is stored. If this is defined in the ux-orchestrator agent definition, add a cross-reference with the file path and section name.

---

### Traceability (0.90/1.00)

**Evidence:**

VERSION header: `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "Lifecycle-Stage Routing", "Wave Architecture", "Cross-Sub-Skill Handoff Data" | PARENT: /user-experience skill -->`. All required traceability fields present.

Footer is complete with parent skill, parent SKILL.md path, sibling rules (all 4: wave-progression.md, synthesis-validation.md, mcp-coordination.md, ci-checks.md), creation date, update date, and status.

Per-section HTML comments trace each section to a specific SKILL.md section or agent-routing-standards.md section. The CRISIS section is traced to SKILL.md [Lifecycle-Stage Routing]. The Cross-Sub-Skill Handoff is traced to SKILL.md [Cross-Sub-Skill Handoff Data]. The Wave State Detection subsection cross-references wave-progression.md [Wave State Tracking] and [Signoff Requirements] by name. The Wave State Caching subsection cross-references wave-progression.md [State Caching].

CRISIS Synthesis traces to synthesis-validation.md "Cross-Framework Synthesis Protocol" by section name.

**Gaps:**

The "Bypass Documentation" subsection (under Bypass Routing) does not have its own source comment. The parent section's comment (`<!-- Source: SKILL.md Section "Wave Architecture" — bypass mechanism. -->`) covers it by scope, but the bypass documentation structure specifically is also traceable to wave-progression.md [Bypass Mechanism]. A source comment on the Bypass Documentation subsection would complete the traceability chain.

**Improvement Path:**

Add a source comment to the Bypass Documentation subsection: `<!-- Source: SKILL.md Section "Wave Architecture" — bypass documentation structure. Cross-reference: skills/user-experience/rules/wave-progression.md [Bypass Mechanism] for authoritative bypass field definitions. -->`. This is a minor improvement only.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.78 | 0.90+ | **Add WAVE-5-SIGNOFF.md to Wave State Detection table.** Row: `skills/user-experience/output/WAVE-5-SIGNOFF.md | Wave 5 complete; all waves deployed`. This is a one-line fix that closes the most concrete inconsistency. |
| 2 | Internal Consistency | 0.78 | 0.90+ | **Resolve capacity check / cost tier conflict.** The Capacity Check recommendation "Wave 1 sub-skills only + Free ($0)" is inconsistent because Free tier includes Wave 4 sub-skills. Determine the intended logic (wave-gate based or cost-tier based) and rewrite Step 2 to reflect the actual recommendation. If cost-based: recommend Free-tier sub-skills (JTBD, HEART, Kano, Behavior Design). If wave-gate based: remove the "Free ($0)" cost tier reference or clarify the distinction. |
| 3 | Completeness | 0.87 | 0.93+ | **Add explicit "Multi-Sub-Skill Routing" section** for non-CRISIS scenarios where multiple sub-skills run in sequence (e.g., Comprehensive UX audit: Heuristic Eval + HEART Metrics). Define entry trigger, execution sequence, and handoff artifacts, analogous to the CRISIS section structure. This closes the implicit-only coverage gap for the "Comprehensive UX audit" pattern. |
| 4 | Methodological Rigor / Actionability | 0.88 | 0.92+ | **Specify session state flag mechanism.** Add to Lifecycle Stage Router or a new "Session State Management" subsection: the flag name (e.g., `onboard_displayed`), scope (per engagement ID), storage (in-memory, reset at new engagement), and reset condition. If defined in the ux-orchestrator agent definition, add a cross-reference with file path and section anchor. |
| 5 | Traceability | 0.90 | 0.93+ | **Add source comment to Bypass Documentation subsection** citing wave-progression.md [Bypass Mechanism] as the authoritative cross-reference for bypass field definitions. Minor, but completes the per-subsection traceability chain. |

---

## Leniency Bias Check

- [x] Each dimension scored independently (Completeness, Internal Consistency, Methodological Rigor, Evidence Quality, Actionability, Traceability evaluated in sequence without cross-contamination)
- [x] Evidence documented for each score (specific line references and section names cited above)
- [x] Uncertain scores resolved downward (Internal Consistency: initial impression ~0.83 revised to 0.78 after identifying the capacity/Free-tier mismatch; confirmed as a real inconsistency, not merely a phrasing ambiguity)
- [x] First-draft calibration considered (this is iteration 2; a 0.863 composite for a rule file with two real inconsistencies is appropriate — not inflated)
- [x] No dimension scored above 0.95 without exceptional evidence (highest dimension score is Evidence Quality and Traceability at 0.90)

**Score calibration check:** 0.863 falls in the REVISE band (0.85-0.91). This is consistent with a deliverable that is functionally sound and well-structured, with two specific, fixable errors (one missing table row, one concept conflation) holding it below the governance threshold. The gap to the C4 threshold (0.95) is 0.087, which is meaningful and reflects real work remaining, not cosmetic polish.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.863
threshold: 0.95  # C4 deliverable
standard_threshold: 0.92  # H-13
weakest_dimension: Internal Consistency
weakest_score: 0.78
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add WAVE-5-SIGNOFF.md row to Wave State Detection table (one-line fix)"
  - "Resolve capacity check 'Wave 1 only' vs. Free cost tier spanning Waves 1-4 inconsistency"
  - "Add explicit Multi-Sub-Skill Routing section for non-CRISIS multi-agent scenarios"
  - "Specify ONBOARD session state flag mechanism or add cross-reference to ux-orchestrator agent definition"
  - "Add source comment to Bypass Documentation subsection citing wave-progression.md"
```

---

*Score report: ux-routing-rules-iter2-score.md*
*Scoring agent: adv-scorer*
*Deliverable: skills/user-experience/rules/ux-routing-rules.md*
*Parent SKILL.md: skills/user-experience/SKILL.md*
*Sibling cross-referenced: wave-progression.md, synthesis-validation.md, mcp-coordination.md*
*Scoring standard: S-014 LLM-as-Judge (quality-enforcement.md)*
*Created: 2026-03-04*
