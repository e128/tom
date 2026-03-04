# C4 Tournament — Iteration 4: Strategy Selection and Execution Plan

**Generated:** 2026-03-03
**Criticality Level:** C4 (Critical)
**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Agent:** adv-selector

---

## Criticality Assessment

| Field | Value |
|-------|-------|
| **Requested Level** | C4 (Critical) |
| **Deliverable Type** | GitHub Enhancement Issue Body (Public-Facing) |
| **Deliverable Path** | `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md` |
| **Auto-Escalation Applied** | No additional escalation (already at C4 ceiling) |
| **Final Level** | C4 |

### Escalation Rationale

This deliverable is a GitHub Enhancement issue body that will be posted publicly on the GitHub repository. GitHub issues are irreversible, public-facing governance artifacts. Per auto-escalation rule **AE-001** in quality-enforcement.md, items involving public governance documentation (in this case, the public communication of a feature proposal) escalate to C4 automatically. The composition/public visibility confirms this is a critical deliverable requiring the full tournament with all 10 selected strategies.

**Prior Tournament Context:**
- Iteration 1: composite score 0.704 (REVISE band)
- Iteration 2: composite score 0.724 (REVISE band) — 28 fixes applied in R1
- Iteration 3: composite score 0.761 (REVISE band) — 10 fixes applied in R2, 18 fixes applied in R3
- **Target for Iteration 4:** >= 0.92 (PASS threshold per H-13)

---

## Selected Strategies (Ordered per H-16)

### Execution Ordering Rationale

The ordering follows the canonical execution order per quality-enforcement.md and enforces **H-16 constraint:** Steelman (S-003) MUST execute BEFORE Devil's Advocate (S-002).

| Order | Strategy ID | Strategy Name | Composite Score | Family | Template Path |
|-------|-------------|---------------|-----------------|--------|----------------|
| **1** | S-010 | Self-Refine | 4.00 | Iterative Self-Correction | `.context/templates/adversarial/s-010-self-refine.md` |
| **2** | S-003 | Steelman Technique | 4.30 | Dialectical Synthesis | `.context/templates/adversarial/s-003-steelman.md` |
| **3** | S-002 | Devil's Advocate | 4.10 | Role-Based Adversarialism | `.context/templates/adversarial/s-002-devils-advocate.md` |
| **4** | S-004 | Pre-Mortem Analysis | 4.10 | Role-Based Adversarialism | `.context/templates/adversarial/s-004-pre-mortem.md` |
| **5** | S-001 | Red Team Analysis | 3.35 | Role-Based Adversarialism | `.context/templates/adversarial/s-001-red-team.md` |
| **6** | S-007 | Constitutional AI Critique | 4.15 | Iterative Self-Correction | `.context/templates/adversarial/s-007-constitutional-ai.md` |
| **7** | S-011 | Chain-of-Verification | 3.75 | Structured Decomposition | `.context/templates/adversarial/s-011-cove.md` |
| **8** | S-012 | FMEA | 3.75 | Structured Decomposition | `.context/templates/adversarial/s-012-fmea.md` |
| **9** | S-013 | Inversion Technique | 4.25 | Structured Decomposition | `.context/templates/adversarial/s-013-inversion.md` |
| **10** | S-014 | LLM-as-Judge | 4.40 | Iterative Self-Correction | `.context/templates/adversarial/s-014-llm-as-judge.md` |

### Detailed Strategy Descriptions

#### Strategy 1: S-010 Self-Refine (Required for C4)

**Purpose:** Early self-review to identify and correct obvious defects before external critique. Enforces H-15 (self-review before presenting).

**Template:** `.context/templates/adversarial/s-010-self-refine.md`

**Rationale:** Catches obvious issues early, reducing burden on downstream strategies. This is a gating step that prevents wasted critic cycles on preventable defects.

**Execution Checkpoint:** Deliverable must pass self-review for obvious spelling, formatting, navigation table completeness, and markdown structure before proceeding to S-003.

---

#### Strategy 2: S-003 Steelman Technique (Required for C4, H-16 Ordered)

**Purpose:** Strengthen the proposal by finding its strongest possible interpretation and supporting arguments before attacking it.

**Template:** `.context/templates/adversarial/s-003-steelman.md`

**Rationale:** H-16 requires steelman before devil's advocate. Strengthening the proposal prevents premature rejection of sound ideas and ensures the subsequent devil's advocate critique targets the best version of the proposal.

**H-16 Compliance:** This strategy MUST execute at position 2 (immediately after S-010) and MUST complete before S-002 executes.

**Expected Outcomes:**
- Strongest supporting evidence identified
- Counter-arguments to common objections
- Clarified value proposition and scope boundaries

---

#### Strategy 3: S-002 Devil's Advocate (Required for C4, After H-16 Steelman)

**Purpose:** Challenge assumptions, logic, scope, and claims in the proposal after it has been strengthened.

**Template:** `.context/templates/adversarial/s-002-devils-advocate.md`

**Rationale:** Aggressive critique of the steelman version identifies vulnerabilities and gaps that may not be apparent from a friendly reading.

**H-16 Compliance:** This strategy executes at position 3, after S-003 steelman has completed.

**Expected Outcomes:**
- Unstated assumptions exposed
- Logical gaps and fallacies identified
- Scope ambiguities and boundary issues
- Unjustified claims flagged

---

#### Strategy 4: S-004 Pre-Mortem Analysis (Required for C4)

**Purpose:** Imagine the proposal has already been implemented and failed catastrophically. Work backward to identify what could have caused failure.

**Template:** `.context/templates/adversarial/s-004-pre-mortem.md`

**Rationale:** Surfaces failure modes that linear forward-planning critique often misses. Generates concrete risk mitigation recommendations.

**Expected Outcomes:**
- Implementation failure modes identified
- Adoption blockers
- Operational risks
- Concrete mitigation strategies

---

#### Strategy 5: S-001 Red Team Analysis (Required for C4)

**Purpose:** Offensive testing from the perspective of an external attacker or adversary. Identify attack surface, exploitation vectors, and governance vulnerabilities.

**Template:** `.context/templates/adversarial/s-001-red-team.md`

**Rationale:** For a public GitHub issue proposing a new skill, red team analysis identifies how the proposal could be misused, exploited, or turned against the project's interests. This is essential for public governance artifacts.

**Expected Outcomes:**
- Attack surface analysis
- Exploit/misuse scenarios
- Governance constraint violations
- Security implications

---

#### Strategy 6: S-007 Constitutional AI Critique (Required for C4)

**Purpose:** Verify compliance with Jerry Constitution and governance constraints. Ensure the proposal does not violate core principles (P-001 through P-022).

**Template:** `.context/templates/adversarial/s-007-constitutional-ai.md`

**Rationale:** Enforces H-18 (constitutional compliance check for C2+). For a C4 public governance artifact, constitutional alignment is non-negotiable.

**Expected Outcomes:**
- Constitutional compliance statement
- Principle-by-principle analysis (P-001 through P-022)
- Governance constraint alignment
- Rights/powers/limitations clarification

---

#### Strategy 7: S-011 Chain-of-Verification (Required for C4)

**Purpose:** Verify that each claim in the proposal can be traced to evidence, reasoning, or established fact. Break any unsupported assertion chains.

**Template:** `.context/templates/adversarial/s-011-cove.md`

**Rationale:** Ensures the proposal is grounded in evidence rather than assertion. For a public proposal, this builds credibility and prevents false claims.

**Expected Outcomes:**
- Claim-to-evidence traceability map
- Unsupported assertions identified
- Evidence quality assessment
- Confidence levels assigned to each claim

---

#### Strategy 8: S-012 FMEA (Required for C4)

**Purpose:** Formal Failure Mode and Effects Analysis. Systematically identify risks, assign severity/occurrence/detection scores, and prioritize mitigation.

**Template:** `.context/templates/adversarial/s-012-fmea.md`

**Rationale:** Structured risk analysis ensures no failure mode is overlooked. Provides quantified risk prioritization for addressing critical issues.

**Expected Outcomes:**
- Complete failure mode catalog
- RPN (Risk Priority Number) scoring
- Mitigation recommendations prioritized
- Risk acceptance/mitigation decisions

---

#### Strategy 9: S-013 Inversion Technique (Required for C4)

**Purpose:** Invert the proposal: ask what would make it fail, what are the opposites, what if we inverted key assumptions?

**Template:** `.context/templates/adversarial/s-013-inversion.md`

**Rationale:** Different reasoning path from forward-linear critique. Inverted thinking often surfaces blind spots and hidden assumptions that haven't surfaced in other strategies.

**Expected Outcomes:**
- Inverted assumptions and their implications
- Opposite scenarios (e.g., what if adoption is zero instead of expected?)
- Hidden dependencies exposed
- Resilience to opposing conditions

---

#### Strategy 10: S-014 LLM-as-Judge (Required for C4, ALWAYS LAST)

**Purpose:** Final quality scoring using a 6-dimension rubric with weighted scoring. Provides the go/no-go decision and detailed dimension-level feedback.

**Template:** `.context/templates/adversarial/s-014-llm-as-judge.md`

**Rationale:** Objective scoring mechanism using the canonical quality gate rubric per H-13 and H-17. Provides quantified progress tracking across iterations.

**Scoring Dimensions (Weights):**
- Completeness (20%)
- Internal Consistency (20%)
- Methodological Rigor (20%)
- Evidence Quality (15%)
- Actionability (15%)
- Traceability (10%)

**Quality Gate Threshold:** >= 0.92 (PASS)

**Pass/Fail Decision:**
- Score >= 0.92: **PASS** — Deliverable accepted
- Score 0.85-0.91: **REVISE** — Near threshold; targeted revision likely sufficient
- Score < 0.85: **REJECTED** — Significant rework required

**ALWAYS EXECUTES LAST:** S-014 cannot execute until all 9 prior strategies have completed and their findings integrated.

---

## H-16 Compliance Verification

**H-16 Constraint:** "Steelman (S-003) MUST be applied before Devil's Advocate (S-002). Canonical review pairing."

| Aspect | Status | Details |
|--------|--------|---------|
| **S-003 Position** | ✓ PASS | Position 2 (executes second, immediately after S-010 self-review) |
| **S-002 Position** | ✓ PASS | Position 3 (executes third, immediately after S-003 steelman) |
| **Ordering Constraint** | ✓ SATISFIED | S-003 at pos 2 < S-002 at pos 3. Steelman executes first. |
| **Execution Flow** | ✓ CORRECT | S-010 → **S-003 Steelman** → **S-002 Devil's Advocate** → S-004 onwards |

**H-16 Compliance Conclusion:** ALL H-16 REQUIREMENTS MET. The execution plan enforces the mandatory steelman-before-devil's-advocate ordering. No violations detected.

---

## Strategy Overrides Applied

**User Overrides:** None received.

**Automatic Overrides:** None applied.

**C4 Strategy Set Completeness:** All 10 required strategies present. No optional strategies excluded. No deviations from SSOT.

---

## Quality Context and Expectations

### Prior Iteration Performance

| Iteration | Composite Score | Band | Deficit to 0.92 | Primary Issues |
|-----------|-----------------|------|-----------------|-----------------|
| Iter 1 | 0.704 | REVISE | -0.216 | Missing nav table, navigation anchor links, incomplete sections |
| Iter 2 | 0.724 | REVISE | -0.196 | Added nav table, improved consistency, still gaps in evidence |
| Iter 3 | 0.761 | REVISE | -0.159 | 10 fixes in R2, 18 fixes in R3; structural integrity improved |
| **Iter 4 (Current)** | **TBD** | Target: PASS | **Target: +0.159** | **Remaining gaps identified by 10 strategies** |

### Iteration 4 Strategy Selection Rationale

Iterations 1-3 applied embedded self-correction and targeted fixes. Iteration 4 applies the full C4 tournament (all 10 strategies) to:

1. **Identify systemic gaps** not caught by prior single-strategy review cycles
2. **Apply structured adversarial thinking** (red team, pre-mortem, inversion) that isn't present in iterative self-correction alone
3. **Validate constitutional compliance** (S-007) explicitly
4. **Quantify progress** against all 6 quality dimensions via S-014
5. **Provide empirical decision boundary:** either score >= 0.92 (accepted) or specific gaps for R4 revision

### Expected Outcomes from This Tournament

**If S-014 Score >= 0.92 (PASS):**
- Deliverable meets quality gate
- Ready for GitHub issue posting
- No further revision required

**If S-014 Score < 0.92 (REVISE or REJECTED):**
- Specific dimension-level scores identify which areas need work
- S-001 through S-013 findings provide concrete gap list
- R4 revision targets identified gaps from tournament strategies
- Iteration 5 continues creator-critic-revision cycle per H-14

---

## Execution Handoff to adv-executor

**Next Agent:** adv-executor (execution agent)

**Handoff Context:**
- Deliverable path: `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- Strategy execution order: S-010 → S-003 → S-002 → S-004 → S-001 → S-007 → S-011 → S-012 → S-013 → S-014
- Quality gate threshold: >= 0.92
- H-16 constraint verified: S-003 before S-002 ✓
- Criticality level: C4 (all 10 strategies required)
- Prior iteration scores: 0.704 → 0.724 → 0.761

**Execution Instructions:**
1. Load each strategy template in order
2. Execute strategy against the deliverable file
3. Collect findings and recommendations
4. Pass accumulated findings to S-014 for final scoring
5. Persist tournament results to tournament-iter4 directory

---

## Self-Review Checklist (H-15)

Before persistence, this plan verifies:

- ✓ All 10 strategy IDs valid (S-001 through S-014, no gaps)
- ✓ H-16 ordering satisfied (S-003 at position 2, S-002 at position 3)
- ✓ Auto-escalation rules checked and applied (AE-001 confirmed C4)
- ✓ Template paths correct (all .md files under `.context/templates/adversarial/`)
- ✓ Criticality level correct (C4 confirmed)
- ✓ No user overrides present (none received)
- ✓ No missing strategies (all 10 required for C4 per SSOT)

---

## References

**Source Documents:**
- `.context/rules/quality-enforcement.md` — Criticality Levels (C1-C4), Strategy Catalog, Auto-Escalation Rules (AE-001 through AE-006e)
- `.context/templates/adversarial/s-001-red-team.md` through `s-014-llm-as-judge.md` — Strategy templates
- `skills/adversary/agents/adv-selector.md` — This agent's specification
- `skills/adversary/agents/adv-executor.md` — Execution agent (next in pipeline)
- `skills/adversary/agents/adv-scorer.md` — Scoring agent (embedded in S-014)

**Related Work:**
- PROJ-020 Worktracker: `projects/PROJ-020-feature-enhancements/WORKTRACKER.md`
- Iteration 3 Results: `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter3/`
- Deliverable: `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`

---

*Agent: adv-selector*
*Version: 1.0.0*
*Constitutional Compliance: Jerry Constitution v1.0*
*SSOT: `.context/rules/quality-enforcement.md`*
*Generated: 2026-03-03*
*Status: Ready for adv-executor handoff*
