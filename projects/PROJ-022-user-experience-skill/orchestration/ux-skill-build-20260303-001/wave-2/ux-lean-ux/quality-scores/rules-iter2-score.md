# Quality Score: lean-ux-methodology-rules.md (Iteration 2)

## Composite Score: 0.942 — REVISE

**Score:** 0.942/1.00 | **Threshold:** 0.95 (C4) | **Verdict:** REVISE | **Delta:** -0.008
**Weakest Dimension:** Actionability (0.92)
**One-line assessment:** Iteration 2 resolved 13 of 14 iter1 gaps with high precision — traceability, consistency, evidence, rigor, and completeness all improved substantially — but ASM-008 (upstream data without severity fallback) remains unaddressed and the ICE evidence anchor citation is still below C4 scrutiny, together holding the composite 0.008 below the 0.95 threshold.

---

## Scoring Context

- **Deliverable:** `skills/ux-lean-ux/rules/lean-ux-methodology-rules.md`
- **Deliverable Type:** Methodology Rules File (sub-skill operational constraints)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold:** 0.95 (C4, user-specified)
- **Prior Score (iter1):** 0.862
- **Cross-references verified:** `skills/ux-lean-ux/SKILL.md` (v1.2.0), `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.md` (v1.1.0), `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.governance.yaml`, `skills/ux-heuristic-eval/rules/heuristic-evaluation-rules.md` (v1.2.0)
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.942 |
| **Threshold** | 0.95 (C4, user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (standalone scoring) |
| **Delta to Threshold** | -0.008 |
| **Delta from iter1** | +0.080 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.94 | 0.188 | All 8 rule families present; BML-003 error behavior added; Related Files added; VLD-008 formalized; ASM-008 fallback still missing |
| Internal Consistency | 0.20 | 0.95 | 0.190 | VLD-008 resolves checklist item 14 gap; QG-001 now acknowledges C4 threshold; lifecycle table minor format issue remains |
| Methodological Rigor | 0.20 | 0.96 | 0.192 | EXP-007 residual case added; EXP-003 escalated to HARD; decision path now exhaustive; no methodology errors found |
| Evidence Quality | 0.15 | 0.93 | 0.1395 | ICE attribution note added; Croll & Yoskovitz Ch.10 added; BML-004 Ch.6 added; ICE anchor still "circa 2015" without formal publication title |
| Actionability | 0.15 | 0.92 | 0.138 | ICE-005 calibration example added; QG-002 denominator mechanics added; ASM-008 upstream data fallback still absent |
| Traceability | 0.10 | 0.94 | 0.094 | Related Files section added; SKILL.md version pinned; VLD-008 traceability chain complete; wave-progression.md referenced; secondary files still have "--" version |
| **TOTAL** | **1.00** | | **0.942** | |

---

## Gaps (per dimension below 0.95)

### Completeness — 0.94

- **Gap:** ASM-008 rule for upstream data without severity ratings is absent. ASM-007 references "heuristic evaluation findings with severity >= 2" but provides no fallback when upstream data arrives without severity classification. The agent has no rule governing this case. | **Evidence:** `lean-ux-methodology-rules.md:165-173` (ASM-007 is the terminal assumption mapping rule; no ASM-008 exists) | **Fix:** Add `ASM-008 | When upstream heuristic evaluation findings are provided without severity ratings, the facilitator SHOULD request severity clarification. If clarification is unavailable, treat the finding as severity 2 (minor usability problem) for assumption categorization purposes and document the assumption as MEDIUM confidence. | MEDIUM`

### Evidence Quality — 0.93

- **Gap:** The ICE framework attribution reads "Sean Ellis, GrowthHackers, circa 2015" — an honest disclosure of the community origin, but "circa 2015" is not a citable reference (no specific blog post URL, article title, or publication). At C4 evidence quality scrutiny, community-origin attribution requires either a specific URL to the GrowthHackers article where ICE scoring was first formalized, or explicit acknowledgment that no canonical primary source exists. The attribution note at line 231 correctly acknowledges the thresholds are practitioner adaptations, which is an improvement, but does not resolve the underlying citation gap for the framework origin itself. | **Evidence:** `lean-ux-methodology-rules.md:225` ("ICE (Impact, Confidence, Ease) scoring prioritizes hypotheses in the backlog. The framework originates from the growth hacking community (Sean Ellis, GrowthHackers, circa 2015)") and line 231 (attribution note) | **Fix:** Add a specific URL to the GrowthHackers community resource (e.g., `https://growthhackers.com/articles/ice-scoring`) or explicitly state: "No canonical primary source exists; the framework is attributed to Sean Ellis via GrowthHackers community practice (2015). See `https://growthhackers.com/articles/ice-scoring` for community reference." If the URL is unavailable or not verifiable, add language: "No peer-reviewed citation available; community-attributed framework."

### Actionability — 0.92

- **Gap:** ASM-008 is absent, creating real operational ambiguity. When a heuristic evaluation report arrives without severity classifications, the agent has no rule specifying whether to treat findings as usability assumptions, request clarification, or skip integration. ASM-007 only fires "when upstream heuristic evaluation findings with severity >= 2 are available" — it is silent on the case where findings exist but severity is absent. | **Evidence:** `lean-ux-methodology-rules.md:173` (ASM-007 ends without fallback; no ASM-008 follows) | **Fix:** Add ASM-008 as described in the Completeness gap above. The rule directly enables the agent to take a specific, implementable action rather than exercising undefined judgment.

### Traceability — 0.94

- **Gap:** Secondary file versions in the Related Files table are "--" (unversioned): `skills/user-experience/rules/wave-progression.md`, `skills/user-experience/rules/mcp-coordination.md`, and `skills/ux-lean-ux/templates/` and `skills/ux-lean-ux/agents/ux-lean-ux-facilitator.governance.yaml`. If these files are updated, there is no way to determine whether this rules file was written against a prior version. The SKILL.md and synthesis-validation.md versions are correctly pinned (v1.2.0 and v1.1.0 respectively). | **Evidence:** `lean-ux-methodology-rules.md:447-451` (governance YAML, wave-progression.md, mcp-coordination.md, templates all show "--" in Version column) | **Fix:** Add version metadata to files that have it (governance YAML: 1.1.0 matching its frontmatter; synthesis-validation.md is already at v1.1.0 and correctly pinned). For files without formal version fields (wave-progression.md, mcp-coordination.md, templates), add the date accessed or the git SHA if available, or explicitly note "version not tracked."

---

## Iteration History

| Iter | Score | Delta | Key Changes |
|------|-------|-------|-------------|
| 1 | 0.862 | — | Initial |
| 2 | 0.942 | +0.080 | BML-003 invalid scope error behavior; Related Files section with full dependency matrix; VLD-008 formalized; QG-001 C4 threshold; BML-004 Ch.6 citation; Croll Ch.10 citation; ICE attribution note; EXP-007 residual case; EXP-003 HARD escalation; ICE-005 calibration example; QG-002 denominator mechanics; wave-progression.md referenced; SKILL.md version pinned |

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Actionability / Completeness | 0.92 / 0.94 | 0.95 | Add `ASM-008`: when upstream heuristic data lacks severity ratings, default to treating findings as severity 2 for assumption categorization; document as MEDIUM confidence; SHOULD request clarification. This single rule closes both the Completeness and Actionability gaps simultaneously. |
| 2 | Evidence Quality | 0.93 | 0.95 | Add a specific URL or explicit "no canonical primary source" statement for the Sean Ellis ICE framework attribution. Recommended: `GrowthHackers community (2015), https://growthhackers.com/articles/ice-scoring — no peer-reviewed citation available.` |
| 3 | Traceability | 0.94 | 0.96 | Pin the governance YAML to version 1.1.0 in the Related Files table (the version is present in the YAML's own `version:` field). Add explicit note for unversioned files (wave-progression.md, mcp-coordination.md) acknowledging lack of version tracking. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing the weighted composite
- [x] Evidence documented for each score with specific line references from the deliverable
- [x] Uncertain scores resolved downward: Evidence Quality uncertain between 0.93-0.94 (chose 0.93 due to "circa 2015" citation remaining unresolved at C4 scrutiny); Actionability uncertain between 0.92-0.93 (chose 0.92 due to ASM-008 still absent, creating genuine operational ambiguity)
- [x] Calibration check: 0.94 composite is correctly mapped as REVISE; near-threshold but still below 0.95
- [x] No dimension scored above 0.96 without specific documented justification
- [x] Methodological Rigor at 0.96 justified: all three prior rigor gaps resolved (EXP-007 residual case, EXP-003 escalation, decision path completeness); no remaining methodology errors found

**Calibration note:** The +0.080 delta from iter1 to iter2 reflects genuine, substantial improvement — 13 of 14 identified gaps closed. The remaining 0.008 gap to threshold is attributable to two narrow, fixable issues: ASM-008 (one new rule, ~3 lines) and the ICE citation URL (one sentence). Estimated revision effort: 15-30 minutes. The file is at the threshold boundary; a targeted iter3 addressing Priority 1 and Priority 2 recommendations should reach PASS.

---

## Session Context Schema

```yaml
verdict: REVISE
composite_score: 0.942
threshold: 0.95
weakest_dimension: Actionability
weakest_score: 0.92
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Add ASM-008: upstream heuristic data without severity fallback rule (closes Actionability and Completeness gaps simultaneously)"
  - "Add specific URL or 'no canonical primary source' statement for Sean Ellis ICE framework attribution"
  - "Pin governance YAML version to 1.1.0 in Related Files; add version-tracking note for unversioned files"
```

---

*Score Report: rules-iter2-score.md*
*Deliverable: skills/ux-lean-ux/rules/lean-ux-methodology-rules.md*
*Scoring Agent: adv-scorer*
*Strategy: S-014 LLM-as-Judge*
*SSOT: .context/rules/quality-enforcement.md*
*Created: 2026-03-04*
