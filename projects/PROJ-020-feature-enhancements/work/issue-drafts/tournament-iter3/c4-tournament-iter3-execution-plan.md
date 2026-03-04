# C4 Tournament Iteration 3 — Strategy Execution Plan

<!-- [exec-plan-v1, C4-tournament-iter3] -->

**Generated:** 2026-03-03

**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`

**Criticality:** C4 (Critical — public-facing GitHub Enhancement Issue artifact)

**Iteration:** 3 of 8 maximum

**Prior Scores:**
- Iteration 1: 0.704 (REVISE band)
- Iteration 2: 0.724 (REVISE band)

**Current Status:** Approaching substantive closure threshold (~0.791 projected after R2 revisions)

---

## Criticality Assessment

**Requested Level:** C4 (explicitly assigned)

**Auto-Escalation Applied:** No additional escalation rules triggered
- Deliverable does NOT touch `docs/governance/JERRY_CONSTITUTION.md` (AE-001 not triggered)
- Deliverable does NOT touch `.context/rules/` or `.claude/rules/` (AE-002 not triggered)
- Deliverable is NOT an ADR (AE-003 not triggered)
- Deliverable is NOT a baselined ADR modification (AE-004 not triggered)
- Deliverable does NOT contain security-relevant code (AE-005 not triggered)
- Token context at nominal level (AE-006 not triggered)

**Final Level:** C4 (confirmed)

**Required Strategy Set:** All 10 selected strategies per quality-enforcement.md Criticality Levels table

**Optional Strategies:** None (C4 requires all)

---

## Selected Strategies (Ordered)

### Execution Order per H-16 Constraint

> **H-16 Compliance:** S-003 (Steelman Technique) MUST be ordered BEFORE S-002 (Devil's Advocate).
> This plan satisfies H-16: S-003 at order position 2, S-002 at order position 3.

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Composite Score | Strategy Family |
|-------|-------------|---------------|---------------|-------------------|-----------------|-----------------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | 4.00 | Iterative Self-Correction |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required (H-16) | 4.30 | Dialectical Synthesis |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | 4.10 | Role-Based Adversarialism |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | 4.10 | Role-Based Adversarialism |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | 3.35 | Role-Based Adversarialism |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required (H-18) | 4.15 | Iterative Self-Correction |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | 3.75 | Structured Decomposition |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | 3.75 | Structured Decomposition |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | 4.25 | Structured Decomposition |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required (H-17, LAST) | 4.40 | Iterative Self-Correction |

**Total Strategies:** 10/10 selected strategies included (100% coverage for C4 tournament)

---

## H-16 Compliance Verification

| Requirement | Actual | Status |
|-------------|--------|--------|
| S-003 position | 2 | ✓ PASS |
| S-002 position | 3 | ✓ PASS |
| S-003 before S-002? | Yes (2 < 3) | ✓ PASS |
| Constraint satisfied? | Yes | ✓ PASS |

**H-16 Status:** SATISFIED — Steelman (S-003) executes before Devil's Advocate (S-002), preventing premature rejection of sound approaches.

---

## Recommended Execution Strategy

### Serial Execution (Recommended for C4)

Execute all 10 strategies serially in the order above. This ensures:

1. **S-010 (Self-Refine)** identifies obvious defects early
2. **S-003 → S-002 (Steelman → Devil's Advocate)** dialectical pairing strengthens then challenges
3. **S-004 → S-001 (Pre-Mortem → Red Team)** structured and adversarial risk analysis
4. **S-007 (Constitutional AI)** ensures governance compliance per H-18
5. **S-011 → S-012 → S-013 (Chain-of-Verification, FMEA, Inversion)** structured decomposition finds hidden gaps
6. **S-014 (LLM-as-Judge)** final scoring with 6-dimension rubric

**Total Execution Time (Estimated):**
- Per strategy: 3-8 minutes (depending on artifact complexity)
- Full tournament: 30-80 minutes (serial execution)
- Scoring: 2-5 minutes per iteration

### Parallel Grouping (Alternative — Time-Critical Only)

If token budget or wall-clock time requires parallelization:

**Group A (Self-Review):**
- S-010 (Self-Refine)

**Group B (Strengthen):**
- S-003 (Steelman)

**Group C (Challenge):**
- S-002 (Devil's Advocate)
- S-004 (Pre-Mortem)
- S-001 (Red Team)

**Group D (Verify & Constitutional):**
- S-007 (Constitutional AI)
- S-011 (Chain-of-Verification)

**Group E (Decompose):**
- S-012 (FMEA)
- S-013 (Inversion)

**Group F (Score — ALWAYS LAST):**
- S-014 (LLM-as-Judge)

**Constraints:**
- Groups execute in alphabetical order (A → B → C → D → E → F)
- Within each group, strategies may execute in parallel
- S-003 must complete before S-002 (H-16 constraint enforced within Group B/C boundary)
- S-014 MUST execute last (quality gate requirement)

---

## Strategy Descriptions

### S-010: Self-Refine
**Template:** `.context/templates/adversarial/s-010-self-refine.md`

Agent reviews the deliverable against basic quality criteria and corrects obvious defects before external critique. Per H-15 (self-review requirement), this is the mandatory first step.

**Key Focus:** Completeness, typos, broken links, missing sections, incomplete examples.

---

### S-003: Steelman Technique
**Template:** `.context/templates/adversarial/s-003-steelman.md`

Construct the strongest possible version of each argument and design choice in the deliverable. Identify unstated assumptions and ground them. This precedes Devil's Advocate (S-002) per H-16 constraint.

**Key Focus:** Strongest interpretation of design choices, unstated but sound assumptions, complementary evidence.

---

### S-002: Devil's Advocate
**Template:** `.context/templates/adversarial/s-002-devils-advocate.md`

Challenge core assumptions and design choices. Attack the logic, evidence, and feasibility. Identify unstated risks and limitations. Only applied after Steelman (S-003) per H-16.

**Key Focus:** Assumption weaknesses, logical gaps, feasibility questions, missing edge cases, contradictions.

---

### S-004: Pre-Mortem Analysis
**Template:** `.context/templates/adversarial/s-004-pre-mortem.md`

Assume the deliverable or its implementation has failed. Work backward to identify what could have gone wrong. Surfaces risks not captured by Devil's Advocate.

**Key Focus:** Implementation risks, adoption barriers, measurable failure conditions, contingency gaps.

---

### S-001: Red Team Analysis
**Template:** `.context/templates/adversarial/s-001-red-team.md`

Attack the deliverable as an adversary would. Look for misuse vectors, security gaps, scope violations, and systemic risks. Most aggressive challenge strategy.

**Key Focus:** Attack surfaces, unintended consequences, governance violations, scope creep vectors, systemic risks.

---

### S-007: Constitutional AI Critique
**Template:** `.context/templates/adversarial/s-007-constitutional-ai.md`

Verify compliance with Jerry governance principles. Check alignment with P-001 through P-025, the Jerry Constitution, and framework constraints. Per H-18 (constitutional compliance check required for C2+).

**Key Focus:** Governance alignment, principle compliance, framework constraint satisfaction, constitutional guardrail compliance.

---

### S-011: Chain-of-Verification (CoVe)
**Template:** `.context/templates/adversarial/s-011-cove.md`

Decompose the deliverable into verifiable claims. For each claim, identify what evidence would falsify it. Verify that claimed evidence exists and is sound.

**Key Focus:** Claim decomposition, falsifiability, evidence gaps, assumption verification, warrant adequacy.

---

### S-012: Failure Modes and Effects Analysis (FMEA)
**Template:** `.context/templates/adversarial/s-012-fmea.md`

Systematically identify each component of the deliverable, its potential failure modes, consequences of failure, and mitigations. Ranks failures by severity and likelihood.

**Key Focus:** Component-level failures, severity assessment, criticality ranking, mitigation completeness.

---

### S-013: Inversion Technique
**Template:** `.context/templates/adversarial/s-013-inversion.md`

Flip each core claim to its opposite and test it. If the opposite is also plausible, both are under-argued. Identifies assumptions that feel necessary but are actually contingent.

**Key Focus:** Contingent vs. necessary assumptions, false dichotomies, inverted claims, hidden middle grounds.

---

### S-014: LLM-as-Judge (Scoring)
**Template:** `.context/templates/adversarial/s-014-llm-as-judge.md`

Apply the 6-dimension quality rubric (Completeness, Internal Consistency, Methodological Rigor, Evidence Quality, Actionability, Traceability). Score each dimension 0-1, compute weighted composite, determine pass/fail vs. quality gate (>= 0.92).

**Key Focus:**
- **Completeness (0.20):** All required sections, no gaps
- **Internal Consistency (0.20):** No contradictions within or across sections
- **Methodological Rigor (0.20):** Proper use of frameworks, valid inference
- **Evidence Quality (0.15):** Claims backed by credible sources
- **Actionability (0.15):** Next steps clear, implementation feasible
- **Traceability (0.10):** Sources cited, decisions documented

**Quality Gate:** Score >= 0.92 = PASS; score < 0.92 = REJECTED (revision required per H-13)

---

## Iteration Context

**Prior Revision (R2):** 10 priority fixes applied:
1. WSM fabrication — removed inflated scores
2. Score corrections — validated against supporting evidence
3. Behavior-design contradiction — resolved acceptance criteria ambiguity
4. Closure condition — clarified Wave 1 completion criteria
5. JTBD rubric — fixed scoring methodology
6. MCP constraints — aligned with actual MCP tool capabilities
7. Wave enforcement — strengthened wave progression guardrails
8. Section titles — aligned nav table with content sections
9. Enabler WSM gate — added quality gate for sub-skill Enabler definitions
10. Pre-launch validation — clarified testing and validation requirements

**Projected Outcome (Post-R3):**
- Iteration 3 score: ~0.791 (REVISE band, approaching substantive closure)
- Remaining closure path: 2-3 iterations to reach >= 0.92 PASS threshold
- Key focus areas: Evidence quality gaps, actionability specificity, traceability completeness

---

## Strategy Auto-Escalation Alignment

| Auto-Escalation Rule | Condition | Status |
|---------------------|-----------|--------|
| AE-001 | Touches JERRY_CONSTITUTION.md | Not triggered |
| AE-002 | Touches .context/rules/ | Not triggered |
| AE-003 | New/modified ADR | Not triggered |
| AE-004 | Modifies baselined ADR | Not triggered |
| AE-005 | Security-relevant code | Not triggered |
| AE-006 | Context fill critical | Not triggered (NOMINAL level) |

**Overall:** No escalation rules triggered beyond explicit C4 assignment.

---

## Quality Gate Compliance

| Requirement | Status | Notes |
|-------------|--------|-------|
| H-13: Quality threshold >= 0.92 for C2+ | Active | Final score determines PASS/REVISE/REJECTED |
| H-14: Creator-critic-revision cycle (min 3) | Active | Iteration 3 of 8; minimum cycle satisfied |
| H-15: Self-review before presenting (S-010) | Active | S-010 is first strategy in execution order |
| H-16: Steelman before Devil's Advocate | Satisfied | S-003 at position 2, S-002 at position 3 |
| H-17: Quality scoring (S-014) | Required | S-014 executes last (position 10) |
| H-18: Constitutional compliance (S-007) | Required | S-007 executes at position 6 |

**All quality gate constraints:** SATISFIED

---

## Execution Handoff

**Input Artifact Path:**
```
projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md
```

**Execution Plan Path:**
```
projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter3/c4-tournament-iter3-execution-plan.md
```

**Expected Executor:** `/adversary` skill with all three agents (adv-selector, adv-executor, adv-scorer)

**Parallel Coordination:** If using grouped parallel execution, orchestrate via `/orchestration` skill with phase barriers between groups.

---

## References

**SSOT:** `.context/rules/quality-enforcement.md`
- Criticality Levels: section [Criticality Levels](#criticality-levels)
- Strategy Catalog: section [Strategy Catalog](#strategy-catalog)
- Quality Gate: section [Quality Gate](#quality-gate)
- Auto-Escalation Rules: section [Auto-Escalation Rules](#auto-escalation-rules)

**Template Paths:**
- All strategy templates located in `.context/templates/adversarial/s-{NNN}-{slug}.md`

**Implementation Details:**
- `/adversary` skill: `skills/adversary/SKILL.md`
- adv-selector agent: `skills/adversary/agents/adv-selector.md`
- adv-executor agent: `skills/adversary/agents/adv-executor.md`
- adv-scorer agent: `skills/adversary/agents/adv-scorer.md`

**Prior Tournament Iterations:**
- Iteration 1: `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter1/`
- Iteration 2: `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter2/`

---

*Strategy Selection Plan — Convergent Mode (C4 Tournament Iteration 3)*
*Generated by adv-selector agent per H-16 ordering enforcement*
*Date: 2026-03-03*
*SSOT: quality-enforcement.md v1.6.0*
