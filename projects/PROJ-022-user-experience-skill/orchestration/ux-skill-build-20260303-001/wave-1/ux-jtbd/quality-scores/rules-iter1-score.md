# Quality Score Report: JTBD Methodology Rules

## L0 Executive Summary

**Score:** 0.882/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Evidence Quality (0.80)

**One-line assessment:** Strong, actionable rules file with well-specified methodology (Ulwick/Moesta/Christensen correctly represented) but falls short of C4 threshold (0.95) primarily due to absent inline citations within the rules sections, a minor agent-definition team-size inconsistency, and missing bibliographic references within the file itself rather than deferred to SKILL.md.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/rules/jtbd-methodology-rules.md`
- **Deliverable Type:** Methodology Rules (Other)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **C4 Threshold:** 0.95 (elevated from standard 0.92)
- **Scored:** 2026-03-04T00:00:00Z
- **Reference Files Read:**
  - `skills/ux-jtbd/SKILL.md`
  - `skills/ux-jtbd/agents/ux-jtbd-analyst.md`

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.882 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 7 required sections present with appropriate depth; minor gap: no visible VERSION metadata block at document top (comment only) |
| Internal Consistency | 0.20 | 0.86 | 0.172 | ODI formula, thresholds, confidence levels consistent across rules/SKILL/agent; minor inconsistency: agent def states "tiny teams (1-3 people)" vs. SKILL.md "tiny teams (1-5 people)" |
| Methodological Rigor | 0.20 | 0.91 | 0.182 | Ulwick ODI formula and max=19 derivation correct; Moesta four forces correctly attributed; Christensen framing accurate; anti-patterns well-chosen |
| Evidence Quality | 0.15 | 0.80 | 0.120 | No inline citations within rule content sections; methodology attributed by name only; bibliographic sources deferred to SKILL.md References rather than cited in the rules file |
| Actionability | 0.15 | 0.93 | 0.140 | HARD/MEDIUM enforcement levels on every rule; decision procedures numbered; anti-patterns include detection signals and corrections; edge cases covered (midpoint default, Tier 3-only -> LOW confidence) |
| Traceability | 0.10 | 0.88 | 0.088 | H-23 nav table present with anchor links; VERSION comment at top and bottom; full footer metadata; cross-references to P-001 and P-022 in enforcement columns; cross-referenced synthesis-validation.md; missing: no inline `quality-enforcement.md` reference within rule sections |
| **TOTAL** | **1.00** | | **0.882** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**

All 7 sections enumerated in the navigation table are present and substantively populated:

1. **Job Statement Rules** -- Canonical three-part format table, 6 validation rules (HARD/MEDIUM), 6 anti-patterns with detection signals and corrections.
2. **Job Classification Rules** -- Three type definitions with decision tests, language signals, and a three-step decision procedure. Mixed-type handling covers all four combination scenarios (F+E, F+S, all three, and the split protocol).
3. **Opportunity Scoring Rules** -- Formula stated, input scales with anchors, three-tier score thresholds, 5 validation rules, P-022 sample size disclosure guidance with three evidence context scenarios.
4. **Switch Force Analysis Rules** -- Four forces defined with evidence sources, 1-5 rating scale with detailed anchors, net force formula, interpretation table, 5 analysis rules.
5. **Confidence Classification Rules** -- HIGH/MEDIUM/LOW criteria with examples, 4 escalation rules, confidence propagation protocol.
6. **Scope Rules** -- Job count limits (3-7) with rationale, 4-step consolidation procedure for >7 jobs, parent-child hierarchy definitions, 4 hierarchy rules.
7. **Source Authority Rules** -- Three-tier evidence classification, 7 citation rules, citation format with worked examples.

**Gaps:**

- The VERSION metadata appears only as an HTML comment (`<!-- VERSION: 1.0.0 -->`) rather than a visible frontmatter block or clearly delineated metadata section. For a rules file consumed by agents and humans alike, a machine-readable visible metadata block would improve completeness.
- The scope rules do not address the scenario where a main job initially identified at MEDIUM confidence later gets validated and upgraded -- the upgrade path for scope changes is not covered.

**Improvement Path:**

Add a visible metadata block at the top of the document (not just a comment). Add a brief note in Scope Rules about how scope decisions interact with confidence upgrading.

---

### Internal Consistency (0.86/1.00)

**Evidence:**

Strong consistency across the three reference documents on all major quantitative claims:

| Claim | Rules File | SKILL.md | Agent Def | Status |
|-------|-----------|----------|----------|--------|
| ODI formula | `I + max(I-S, 0)` | `I + max(I-S, 0)` | `I + max(I-S, 0)` | Consistent |
| Max ODI score | 19 (I=10, S=1) | 19 (I=10, S=1) | 19 (I=10, S=1) | Consistent |
| Underserved threshold | >= 10 | >= 10 | >= 10 | Consistent |
| Appropriately served | 6-9 | 6-9 | 6-9 | Consistent |
| Overserved threshold | < 6 | < 6 | < 6 | Consistent |
| Switch force scale | 1-5 | 1-5 | 1-5 (condensed) | Consistent |
| Confidence default | MEDIUM | MEDIUM | MEDIUM | Consistent |
| Job count limits | 3-7 | 3-7 | 3-7 | Consistent |
| HIGH confidence threshold | 3+ independent sources | 3+ sources | 3+ (implied) | Consistent |

**Gaps -- specific inconsistency found:**

- **Team size definition inconsistency:** The agent definition (`ux-jtbd-analyst.md`) Phase 2 states: "Tiny teams (1-3 people) lack capacity to address more than 7 jobs effectively." However, the SKILL.md consistently uses "tiny teams (1-5 people)" -- the project's stated target audience. This is an inconsistency originating in the agent definition, not the rules file itself, but the rules file's Scope Rules section refers to "Tiny teams (1-5 people)" correctly. Since the rules file is being scored and it is internally consistent (using 1-5), this is a downstream issue. However, the rules file could strengthen consistency by explicitly flagging the canonical team size definition to prevent future drift.
- **Net force formula placement:** The net force formula `(Push + Pull) - (Anxiety + Habit)` appears in the rules file Switch Force section correctly. The SKILL.md and agent definition use the same formula. However, the rules file presents the net force as a "calculation" in a separate subsection while the agent's Phase 3 only discusses "assess force balance" without referencing the explicit net force formula. The numeric formula in the rules file is more precise than the agent's methodology section.

**Improvement Path:**

Add a note in Scope Rules that the canonical team size definition is "1-5 people" per the parent SKILL.md, with a cross-reference to prevent definition drift. Consider flagging the net force calculation as a HARD requirement (currently labeled MEDIUM) given that the formula is straightforward and its absence would undermine analytical reproducibility.

---

### Methodological Rigor (0.91/1.00)

**Evidence:**

The three JTBD theoretical frameworks are correctly represented:

**Christensen (2016) -- Jobs Theory:**
- Job statement format ("When [situation], I want to [motivation], so I can [expected outcome]") is the canonical JTBD format from Christensen's demand-side innovation framework.
- The three job types (functional, social, emotional) match Christensen et al.'s classification in "Competing Against Luck."
- The distinction between "main jobs" and "related jobs" follows the job theory taxonomy correctly.

**Ulwick (2016) -- Outcome-Driven Innovation:**
- Formula `Opportunity Score = Importance + max(Importance - Satisfaction, 0)` is the exact Ulwick ODI formula.
- Maximum score of 19 (I=10, S=1: 10 + 9 = 19) is mathematically correct.
- Thresholds (>=10 underserved, 6-9 appropriately served, <6 overserved) match Ulwick's documented ODI output classification.
- The 1-10 integer scales for importance and satisfaction match ODI methodology.
- The three outcome statement formats ("Minimize the time it takes to...", "Minimize the likelihood of...", "Minimize the variability of...") from the agent's Phase 4 correctly represent Ulwick's desired outcome format, though these are in SKILL.md/agent def rather than the rules file.

**Moesta/Spiek (2020) -- Switch Interview Framework:**
- Four forces (Push/Pull vs. Anxiety/Habit) correctly attributed.
- Net force formula `(Push + Pull) - (Anxiety + Habit)` is the correct representation of the Moesta model.
- Evidence sources mapped to each force are accurate (e.g., FAQ pages for anxiety, usage depth for habit).
- The 1-5 integer scale with detailed anchors (evidence volume + intensity) is a valid operationalization.

**Anti-pattern quality:**
All 6 job statement anti-patterns are methodologically sound and represent known failure modes in JTBD practice (solution-embedding, vague outcomes, missing context, feature masquerading, compound jobs, provider perspective).

**Gaps:**

- The rules file does not include Ulwick's three canonical outcome formats ("Minimize the time...", "Minimize the likelihood...", "Minimize the variability...") within the Opportunity Scoring section itself -- these appear only in the agent definition's Phase 4. An agent consulting only the rules file would not know the outcome statement format. This is a rigor gap.
- The relationship between "job steps" (the universal 8-step process) and outcome expectations could be explicitly stated in the Scope Rules or a new section, rather than left entirely to the agent definition.

**Improvement Path:**

Add a brief subsection in Opportunity Scoring Rules that references the three canonical Ulwick outcome formats. Add a cross-reference from Scope Rules to the 8-step universal process in the agent definition.

---

### Evidence Quality (0.80/1.00)

**Evidence:**

The rules file correctly names the three primary sources (Ulwick, Moesta/Spiek, Christensen) throughout the content:

- "Ulwick's Outcome-Driven Innovation (ODI) formula" -- named correctly
- "Moesta/Spiek four forces model" -- named correctly
- "Switch Force Analysis follows the Moesta/Spiek four forces model" -- attributed

The footer metadata block references:
- Parent SKILL.md (which contains full bibliographic citations for all three sources)
- Agent definition (which has inline source references in the methodology)

**Gaps -- primary evidence quality weakness:**

1. **No inline citations within rule sections.** Unlike the agent definition (which cites "Ulwick (2016)", "Moesta (2020)") and SKILL.md (which has a dedicated References section with full bibliography), the rules file contains NO formal citations in the format `Author (Year) [Tier N]`. The rules themselves mandate this citation format for all output artifacts ("Source: Ulwick (2016) [Tier 2]"), but the rules file itself does not model this behavior.

2. **Bibliographic completeness deferred.** All bibliographic references are in SKILL.md. A standalone evaluation of the rules file cannot verify citation accuracy without reading SKILL.md. For a C4 methodology rules file, self-contained evidence is a higher bar.

3. **Cross-referenced files may not exist.** The Confidence Classification section references `skills/user-experience/rules/synthesis-validation.md` and `skills/user-experience/rules/ux-routing-rules.md`. These are upstream dependencies from the parent skill. If they do not exist at the time of agent execution, confidence propagation rules are unverifiable. The SKILL.md notes that the handoff schema is "planned -- not yet committed to repository," suggesting some referenced files may be future artifacts.

4. **Sample size guidance references "traditional ODI research recommends N=50-200"** without citing a specific Ulwick source for this recommendation. This is a specific quantitative claim that should have a citation.

**Improvement Path:**

Add an inline citation block at the bottom of each major section (or inline within the formula/threshold tables) using the rules file's own citation format. Add a References subsection to the rules file itself with the 4-5 core Ulwick/Moesta/Christensen sources. Add conditional language or a note to the cross-referenced file paths indicating they are "planned" or "required" dependencies.

---

### Actionability (0.93/1.00)

**Evidence:**

The rules file is highly actionable. Specific evidence:

1. **HARD/MEDIUM enforcement levels on every rule:** Every rule row in every table is tagged with enforcement level. An agent can distinguish what to enforce strictly vs. when judgment applies.

2. **Anti-patterns with detection + correction:** Each of the 6 job statement anti-patterns includes a "Detection Signal" column (observable evidence that the anti-pattern has occurred) and a "Correction" column (specific remediation action). This is a complete decision loop.

3. **Decision procedure for classification:** The three-step ordered procedure (check emotional first, check social second, default to functional) eliminates ambiguity about classification precedence.

4. **Concrete thresholds throughout:**
   - Switch force ratings: 1-5 with evidence volume anchors (e.g., "Fewer than 3 evidence instances" = 1)
   - Confidence upgrade: explicit "3 or more direct, independent data sources" threshold for HIGH
   - Job scope: specific numbers (3 minimum, 7 maximum) rather than vague guidance
   - LOW confidence escalation: "majority (> 50%)" triggers banner -- no ambiguity about what "majority" means

5. **Edge cases handled:**
   - Insufficient evidence for force rating: use midpoint (3) and flag for validation
   - Tier 3-only evidence: mandatorily classified as LOW confidence
   - Mixed job types: explicit split protocol with worked examples for each combination
   - Confidence downgrade: documented rationale required

6. **Citation format is concrete:** The exact format `Source: {author} ({year}) [Tier {N}]` with three worked examples eliminates format ambiguity.

**Gaps:**

- The MEDIUM enforcement on "Net force calculation MUST be shown explicitly" is arguably undersized -- without the explicit calculation, output reproducibility is compromised. This could be HARD.
- The consolidation procedure (when > 7 jobs) does not specify how to handle ties in opportunity scores during the "prioritize top 7" step. The agent definition covers this (tie-breaking rule: higher Importance, then lower Satisfaction, then broader segment applicability) but the rules file doesn't.

**Improvement Path:**

Promote net force calculation display from MEDIUM to HARD. Add a tie-breaking rule to the Scope Rules consolidation procedure (or reference the agent definition's tie-breaking rule explicitly).

---

### Traceability (0.88/1.00)

**Evidence:**

Strong traceability chain throughout:

1. **H-23 navigation table:** Present at top with all 7 sections and anchor links. Compliant.
2. **VERSION comment at both top and bottom:** `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: ... -->` present at both locations.
3. **Full footer metadata block:**
   - Rule file name
   - Version number
   - Parent sub-skill with file path
   - Agent with file path
   - Parent skill with file path
   - Quality enforcement SSOT with file path
   - Created date
   - Status (COMPLETE)
4. **Constitutional principle citations:** P-001 and P-022 are explicitly referenced in the enforcement columns of relevant rules (e.g., "HARD (P-001 compliance)" in Source Authority, "P-022 compliance" in citation rules).
5. **Source cross-references in confidence section:** `skills/user-experience/rules/synthesis-validation.md` and `skills/user-experience/rules/ux-routing-rules.md` cited in Confidence Propagation with section anchors.
6. **Parent-to-child relationship documented:** The VERSION header SOURCE field names both the SKILL.md and agent definition as source authorities.

**Gaps:**

1. **No inline `quality-enforcement.md` citation within rule content sections.** The SSOT is named in the footer but not referenced within any enforcement rule. For a C4 document, citing the quality enforcement SSOT at least once within the content (e.g., in the Confidence Classification section) would close the traceability gap.
2. **Cross-referenced files from parent skill may be future artifacts.** `synthesis-validation.md` is cited as the source for Confidence Propagation but may not be committed. This creates a dangling reference in the traceability chain.
3. **No explicit ADR or decision document reference.** For C4 criticality, a rules file would ideally reference the ADR or architectural decision that motivated its creation (e.g., PROJ-022 Wave 1 decision). The footer references the project but not a specific ADR.

**Improvement Path:**

Add one inline reference to `quality-enforcement.md` within the rules content (appropriate in Confidence Classification or Source Authority sections). Add a note that `synthesis-validation.md` is a required dependency currently in development (per PROJ-022 Wave progression). Add a project decision reference (PROJ-022, Wave 1 criteria gate) to the footer or a new "Decision Basis" metadata field.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Evidence Quality | 0.80 | 0.90 | Add a References subsection to the rules file itself with formal bibliographic citations for Ulwick (2016), Moesta (2020), and Christensen (2016). Add the ODI N=50-200 sample size claim citation. Use the rules file's own citation format `Source: {author} ({year}) [Tier {N}]` inline in key formula/threshold subsections. |
| 2 | Methodological Rigor | 0.91 | 0.95 | Add a brief subsection in Opportunity Scoring Rules that includes the three canonical Ulwick outcome formats ("Minimize the time...", "Minimize the likelihood...", "Minimize the variability..."). Add a cross-reference to the 8-step universal process from Scope Rules. |
| 3 | Internal Consistency | 0.86 | 0.93 | Add a canonical team size definition note in Scope Rules ("1-5 people per SKILL.md") to prevent future drift. Promote net force display from MEDIUM to HARD or add explicit rationale for MEDIUM classification. |
| 4 | Traceability | 0.88 | 0.94 | Add one inline reference to `quality-enforcement.md` within rule content. Add status note for `synthesis-validation.md` ("required dependency; see PROJ-022 Wave 2"). Add PROJ-022 Wave 1 criteria gate reference to footer. |
| 5 | Completeness | 0.90 | 0.95 | Add a visible metadata block at document top (not comment-only). Add tie-breaking rule for consolidation (when multiple jobs tie on opportunity score) in Scope Rules -- or explicitly reference the agent definition's tie-breaking rule. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before composite computed
- [x] Evidence documented for each score with specific quotes and section references
- [x] Uncertain scores resolved downward (Internal Consistency: uncertain whether 0.87 or 0.85; chose 0.86 as midpoint)
- [x] First-draft / iteration-1 calibration considered (C4 threshold is 0.95; score of 0.882 reflects substantial work but meaningful gap to C4 bar)
- [x] No dimension scored above 0.95 (Actionability at 0.93 is the highest -- justified by HARD/MEDIUM tagging on every rule, detection+correction anti-pattern pattern, and comprehensive edge case coverage)
- [x] Composite verified: (0.90*0.20) + (0.86*0.20) + (0.91*0.20) + (0.80*0.15) + (0.93*0.15) + (0.88*0.10) = 0.180 + 0.172 + 0.182 + 0.120 + 0.140 + 0.088 = 0.882

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.882
threshold: 0.95
weakest_dimension: Evidence Quality
weakest_score: 0.80
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add self-contained References subsection to rules file with Ulwick/Moesta/Christensen bibliography and inline citations in formula/threshold tables"
  - "Add three canonical Ulwick outcome formats to Opportunity Scoring Rules section"
  - "Add canonical team size definition (1-5 people) to Scope Rules to prevent drift from agent def inconsistency"
  - "Add inline quality-enforcement.md reference within rule content sections"
  - "Add visible metadata block at document top; add tie-breaking rule for consolidation in Scope Rules"
```

---

*Score Report: rules-iter1-score.md*
*Scoring Agent: adv-scorer*
*SSOT: `.context/rules/quality-enforcement.md`*
*Strategy: S-014 (LLM-as-Judge)*
*Created: 2026-03-04*
