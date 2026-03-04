# C4 Tournament — Iteration 2 Execution Plan

**Generated:** 2026-03-03
**Agent:** adv-selector
**Criticality Level:** C4 (Critical)

---

## Criticality Assessment

- **Requested Level:** C4
- **Auto-Escalation Applied:** No
- **Final Level:** C4

**Rationale:** Deliverable is a GitHub Enhancement issue body for a new `/user-experience` skill creation (estimated 67 artifacts, major framework expansion). Scope: irreversible, architecture-level impact, public (GitHub), governance-relevant (new skill structure). Qualifies as C4 per quality-enforcement.md definition: "Irreversible, architecture/governance/public."

**Context:** This is Iteration 2 of the C4 tournament. Iteration 1 (adv-executor + adv-scorer run) scored 0.704 REVISE. Creator-conducted Revision R1 addressed 12 Critical and 2 Major findings. Tournament now re-executes all 10 strategies to validate improvements.

---

## Deliverable Details

| Field | Value |
|-------|-------|
| **Path** | `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md` |
| **Type** | GitHub Issue Body (Enhancement) |
| **Size** | ~1,114 lines |
| **Voice** | Saucer Boy (McConkey personality) |
| **Scope** | `/user-experience` skill specification (parent orchestrator + 10 sub-skills) |
| **Iteration** | 2 (post-R1 revision) |
| **Previous Score** | 0.704 REVISE (Iteration 1) |

---

## Selected Strategies (Ordered per H-16)

All 10 required strategies for C4 criticality. Execution grouped by strategic family per recommended-execution-order pattern. **H-16 compliance:** S-003 (position 2) executes BEFORE S-002 (position 4).

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Strategic Family |
|-------|-------------|---------------|---------------|-------------------|------------------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Iterative Self-Correction |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | Dialectical Synthesis |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | Role-Based Adversarialism |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Role-Based Adversarialism |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Role-Based Adversarialism |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Iterative Self-Correction |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Structured Decomposition |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Structured Decomposition |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Structured Decomposition |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | Iterative Self-Correction |

---

## H-16 Compliance

- **S-003 (Steelman) Position:** 2
- **S-002 (Devil's Advocate) Position:** 3
- **Constraint Satisfied:** YES — S-003 (position 2) executes BEFORE S-002 (position 3)

**Rationale:** Per H-16, Steelman (strengthening core arguments) precedes Devil's Advocate (attacking from opposition perspective). This ordering prevents premature rejection of sound approaches and ensures ideas are fully articulated before systematic critique.

---

## Strategic Execution Groups

Strategies are organized into execution groups aligned with the recommended execution order from agent-development-standards.md. Each group builds on prior results.

### Group A: Self-Review
**Purpose:** Early self-correction; reduce reviewer burden

- **S-010** Self-Refine
  - Read deliverable
  - Identify obvious defects (typos, logic errors, incomplete sections)
  - Apply mechanical fixes
  - Output: Annotated revision list + corrected draft

### Group B: Strengthen
**Purpose:** Build the strongest possible argument before attack

- **S-003** Steelman Technique
  - Find the strongest form of each core claim
  - Identify unstated assumptions that are actually valid
  - Articulate the best-case interpretation
  - Output: Steelman memo (claim-level analysis)

### Group C: Challenge (Role-Based)
**Purpose:** Systematic attack from multiple adversarial angles

- **S-002** Devil's Advocate (core opposition)
  - Assume arguments are wrong
  - Find weakest points
  - Construct opposing position
  - Output: Devil's memo (claim-level contradictions)

- **S-004** Pre-Mortem Analysis (failure scenario)
  - Project to launch + 6 months post-launch
  - Assume the skill has failed
  - Work backward to identify causal factors
  - Output: Pre-mortem findings (18-month failure risks)

- **S-001** Red Team Analysis (adversary lens)
  - Attack the proposal as a malicious actor would
  - Find gaps, contradictions, exploitable assumptions
  - Identify scope creep risks
  - Output: Red team attack surface report

### Group D: Verify (Decomposition)
**Purpose:** Systematic structural analysis

- **S-007** Constitutional AI Critique
  - Check compliance with Jerry Constitution, HARD rules, governance constraints
  - Verify P-003 (no recursive subagents), P-020 (user authority), P-022 (no deception)
  - Identify governance violations
  - Output: Compliance memo (governance-level risks)

- **S-011** Chain-of-Verification (COVE)
  - Trace each major claim back to supporting evidence
  - Verify evidence chain completeness
  - Identify unsupported leaps
  - Output: Verification chain (claim → evidence map)

### Group E: Decompose (Structured Analysis)
**Purpose:** Identify failure modes and systemic risks

- **S-012** FMEA (Failure Mode & Effects Analysis)
  - List all possible failure modes in skill delivery, sub-skill execution, orchestrator routing
  - Rate severity, occurrence, detection for each
  - Identify high-RPN failure risks
  - Output: FMEA table (RPN-ranked failures)

- **S-013** Inversion Technique
  - Invert every major assumption
  - For each inversion, assess implications
  - Identify which inversions are actually catastrophic
  - Output: Inversion analysis (assumption-level risks)

### Group F: Score (Final Assessment)
**Purpose:** Apply weighted quality rubric; produce final quality score

- **S-014** LLM-as-Judge
  - Apply 6-dimension rubric with weights: Completeness (0.20), Internal Consistency (0.20), Methodological Rigor (0.20), Evidence Quality (0.15), Actionability (0.15), Traceability (0.10)
  - Score each dimension 0-10
  - Apply weights
  - Output: Quality score (0.0-1.0) + dimension breakdown + pass/fail verdict
  - **Always execute LAST per quality-enforcement.md**

---

## Execution Sequence

### Session 1: Strategies S-010 → S-003 (Self-Review + Steelman)
**Estimated Duration:** 2-3 turns
**Output Artifact:** `iteration-2/group-a-self-review.md`, `iteration-2/group-b-steelman.md`

1. Load deliverable: `ux-skill-issue-body-saucer-boy.md`
2. Execute S-010 (self-refine) against deliverable
3. Execute S-003 (steelman) against deliverable
4. Aggregate findings; produce intermediate output

### Session 2: Strategies S-002 → S-001 (Challenge Phase)
**Estimated Duration:** 3-4 turns
**Output Artifact:** `iteration-2/group-c-challenge.md`

1. Load deliverable + S-010 + S-003 outputs
2. Execute S-002 (devil's advocate)
3. Execute S-004 (pre-mortem)
4. Execute S-001 (red team)
5. Aggregate challenge findings

### Session 3: Strategies S-007 → S-011 (Verification Phase)
**Estimated Duration:** 2-3 turns
**Output Artifact:** `iteration-2/group-d-verify.md`

1. Load deliverable + challenge findings
2. Execute S-007 (constitutional AI)
3. Execute S-011 (chain-of-verification)
4. Aggregate verification findings

### Session 4: Strategies S-012 → S-013 (Decomposition Phase)
**Estimated Duration:** 2-3 turns
**Output Artifact:** `iteration-2/group-e-decompose.md`

1. Load deliverable + verification findings
2. Execute S-012 (FMEA)
3. Execute S-013 (inversion)
4. Aggregate decomposition findings

### Session 5: Strategy S-014 (Scoring + Tournament Verdict)
**Estimated Duration:** 2-3 turns
**Output Artifact:** `iteration-2/group-f-llm-as-judge.md`

1. Load deliverable + all prior strategy outputs
2. Execute S-014 (LLM-as-Judge) with 6-dimension rubric
3. Produce final quality score
4. Determine pass/fail (threshold: >= 0.92)
5. Produce tournament iteration 2 verdict

---

## Quality Gate Criteria

| Criterion | Threshold | Source |
|-----------|-----------|--------|
| **Weighted Composite Score** | >= 0.92 | H-13, quality-enforcement.md |
| **Dimension: Completeness** | Score + evidence | S-014 rubric, ADR-EPIC002-001 |
| **Dimension: Internal Consistency** | Score + evidence | S-014 rubric |
| **Dimension: Methodological Rigor** | Score + evidence | S-014 rubric |
| **Dimension: Evidence Quality** | Score + evidence | S-014 rubric |
| **Dimension: Actionability** | Score + evidence | S-014 rubric |
| **Dimension: Traceability** | Score + evidence | S-014 rubric |

**Below-Threshold Outcomes:**
- **PASS (>= 0.92):** Deliverable accepted; ready for merge
- **REVISE (0.85-0.91):** Rejected; targeted revision required (trigger Iteration 3)
- **REJECTED (< 0.85):** Rejected; significant rework required (trigger Iteration 3 with escalation)

---

## Strategy Overrides Applied

None. User has not specified any additions or removals. All 10 required strategies for C4 are selected per SSOT.

---

## H-16 Self-Review (S-010 Pre-Flight Check)

Before persisting this plan, verification that:

1. ✓ All 10 strategy IDs are valid (S-001 through S-014, selected only)
2. ✓ H-16 ordering satisfied: S-003 (position 2) before S-002 (position 3)
3. ✓ Auto-escalation rules checked: No auto-escalation triggered (deliverable is already C4)
4. ✓ User overrides reflected: None
5. ✓ Template paths correspond to selected strategies (all verified against glob results)
6. ✓ Execution grouping respects strategic families and recommended order
7. ✓ S-014 positioned last (position 10) as required

**Plan Status:** VALIDATED ✓

---

## Next Steps

1. **adv-executor:** Load this plan and execute Strategies S-010 through S-014 against the deliverable
2. **adv-scorer:** Apply S-014 (LLM-as-Judge) to produce final quality score
3. **Output:** Comprehensive tournament iteration 2 report with strategy findings and quality verdict
4. **Handoff:** If PASS, prepare for merge. If REVISE or REJECTED, trigger Iteration 3 with revised execution plan

---

**Plan Version:** C4-tournament-iter2-001
**SSOT:** `.context/rules/quality-enforcement.md` (Criticality Levels section, C4 row)
**Created By:** adv-selector agent
**Date:** 2026-03-03
