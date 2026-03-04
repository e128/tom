# C4 Tournament — Iteration 1 Execution Plan

**Deliverable:** UX Skill Enhancement Issue (GitHub Issue Body)
**Path:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Deliverable Type:** GitHub Enhancement Issue (Skill Proposal, ~1020 lines)
**Criticality Level:** C4 (Critical)
**Iteration:** 1 of 8 (maximum per RT-M-010)
**Target Quality Score:** >= 0.95 (C4 standard)

---

## Criticality Assessment

**Requested Level:** C4 (Critical)

**Auto-Escalation Rules Checked:**

| Rule | Condition | Result |
|------|-----------|--------|
| AE-001 | Touches JERRY_CONSTITUTION.md | Not triggered |
| AE-002 | Touches .context/rules/ or .claude/rules/ | Not triggered |
| AE-003 | New or modified ADR | Not triggered (GitHub issue, not ADR) |
| AE-004 | Modifies baselined ADR | Not triggered |
| AE-005 | Security-relevant code | Not triggered |

**Escalation Applied:** No (requested C4 is justified by scope)

**Final Criticality Level:** C4 (Critical)

**Justification:** Deliverable scope is irreversible (published GitHub issue for public feature), architecture-level (introduces new skill with 10 sub-skills and orchestration pattern), and governance-visible (framework enhancement proposal). C4 criticality is independently justified.

---

## C4 Strategy Set

Per `quality-enforcement.md` Criticality Levels section:

**C4 Enforcement:** All tiers + tournament
**Required Strategies:** All 10 selected — {S-001, S-002, S-003, S-004, S-007, S-010, S-011, S-012, S-013, S-014}
**Optional Strategies:** None (all are required for C4)

---

## Selected Strategies (Ordered for Execution)

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Sequence Group |
|-------|-------------|---------------|---------------|-------------------|-----------------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Group A: Self-Review |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | Group B: Strengthen (H-16) |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | Group C: Challenge (after S-003) |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Group C: Challenge |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Group C: Challenge |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Group D: Verify |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Group D: Verify |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Group E: Decompose |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Group E: Decompose |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | Group F: Score (LAST) |

---

## H-16 Compliance Check

| Strategy | Position | Constraint | Status |
|----------|----------|-----------|--------|
| S-003 (Steelman) | 2 | MUST come before S-002 | ✓ Pass |
| S-002 (Devil's Advocate) | 3 | MUST come after S-003 | ✓ Pass |

**H-16 Constraint Satisfied:** Yes — S-003 (position 2) executes before S-002 (position 3). Steelman (strengthen arguments) precedes Devil's Advocate (attack arguments), per H-16 canonical pairing rule.

---

## Strategy Execution Groups

Strategies are logically grouped by purpose and applied in sequence. Each group builds on prior results.

### Group A: Self-Review (Foundation)

**Purpose:** Internal quality check before external critique
**Strategy:** S-010 (Self-Refine)

Apply self-review discipline per H-15. The agent reviews its own output for obvious defects, clarity, completeness, and internal consistency before submission to critics. This phase reduces reviewer burden and prevents trivial revisions from consuming critique cycles.

**Template:** `.context/templates/adversarial/s-010-self-refine.md`

---

### Group B: Strengthen (Dialectical Synthesis)

**Purpose:** Identify and amplify the strongest aspects of the proposal
**Strategy:** S-003 (Steelman Technique)

Before attacking the proposal, identify its strongest points and arguments. The steelman technique constructs the best possible version of the argument, ensuring that subsequent critique attacks a fair representation rather than a strawman. This is the H-16 mandatory precursor to Group C critique.

**Template:** `.context/templates/adversarial/s-003-steelman.md`

**H-16 Dependency:** This group MUST execute before Group C (Challenge).

---

### Group C: Challenge (Dialectical Negation + Risk Analysis)

**Purpose:** Identify weaknesses, counter-arguments, risks, and failure modes
**Strategies:** S-002, S-004, S-001 (in order)

This is the primary adversarial pass. Three complementary challenge strategies attack the proposal from different angles:

1. **S-002 (Devil's Advocate)** — Articulate the strongest counter-arguments to the proposal. What could go wrong? What assumptions are unfounded?

2. **S-004 (Pre-Mortem Analysis)** — Assume the proposal fails after 12 months. Work backward to identify what caused the failure. Identify specific failure scenarios and their leading indicators.

3. **S-001 (Red Team Analysis)** — Conduct an offensive security and architectural attack on the proposal. Identify vulnerabilities in design, governance, scalability, and operational security.

**Templates:**
- `.context/templates/adversarial/s-002-devils-advocate.md`
- `.context/templates/adversarial/s-004-pre-mortem.md`
- `.context/templates/adversarial/s-001-red-team.md`

---

### Group D: Verify (Governance + Evidence)

**Purpose:** Validate against constitutional constraints and cross-verify claims
**Strategies:** S-007, S-011 (in order)

This phase verifies that the proposal meets governance standards and that its evidence and reasoning are sound:

1. **S-007 (Constitutional AI Critique)** — Audit the proposal against Jerry governance (JERRY_CONSTITUTION.md, quality-enforcement.md, H-01 through H-36). Does the proposal violate any governance constraints? Does it inadvertently create new governance violations?

2. **S-011 (Chain-of-Verification)** — Verify claims hierarchically. Trace evidence chains: are the claims supported? Are sources cited? Are logical dependencies valid?

**Templates:**
- `.context/templates/adversarial/s-007-constitutional-ai.md`
- `.context/templates/adversarial/s-011-cove.md`

---

### Group E: Decompose (Systematic Analysis)

**Purpose:** Expose hidden assumptions and systemic failure modes
**Strategies:** S-012, S-013 (in order)

This phase decomposes the proposal systematically:

1. **S-012 (FMEA)** — Failure Mode and Effects Analysis. Identify potential failure modes in the proposal's design, implementation, and operational phases. Prioritize by severity and likelihood. Assess current controls and gaps.

2. **S-013 (Inversion Technique)** — Invert the proposal: assume its goals and constraints are opposite. What would the opposite proposal look like? What does the inversion reveal about hidden assumptions?

**Templates:**
- `.context/templates/adversarial/s-012-fmea.md`
- `.context/templates/adversarial/s-013-inversion.md`

---

### Group F: Score (Quantitative Quality Gate)

**Purpose:** Apply consistent, dimension-based quality scoring
**Strategy:** S-014 (LLM-as-Judge) — ALWAYS LAST

This is the quantitative gate. S-014 applies the 6-dimension quality rubric:

1. **Completeness** (weight 0.20) — All necessary aspects covered
2. **Internal Consistency** (weight 0.20) — No contradictions or gaps
3. **Methodological Rigor** (weight 0.20) — Well-reasoned, evidence-based
4. **Evidence Quality** (weight 0.15) — Claims backed by research or precedent
5. **Actionability** (weight 0.15) — Clear, implementable guidance
6. **Traceability** (weight 0.10) — Links to sources, governance, decisions

**Score Threshold:** >= 0.95 for C4 (Iteration 1)

**Score Interpretation:**
- >= 0.95: Exemplary (PASS)
- 0.90-0.94: High quality (marginal PASS for C4; may trigger targeted revision)
- < 0.90: Below threshold (REJECTED, major revision required)

**Template:** `.context/templates/adversarial/s-014-llm-as-judge.md`

**Constraint:** S-014 MUST execute last. It consumes outputs from all prior strategies and integrates them into a single dimensional breakdown. Executing S-014 before prior strategies would omit critical input data.

---

## Execution Protocol

**Sequential execution:** Execute strategies in the order listed above (1 through 10). Each strategy consumes outputs from prior strategies.

**Input/Output Chaining:**

| Strategy | Reads From | Produces |
|----------|-----------|----------|
| S-010 | Original deliverable | Self-refined version + defect log |
| S-003 | S-010 output | Strengthened arguments + best-case case |
| S-002 | S-003 output | Counter-arguments + assumptions list |
| S-004 | S-002 output | Pre-mortem failure scenarios + risk ranking |
| S-001 | S-004 output | Red team attack surface + vulnerability report |
| S-007 | S-001 output | Governance audit + compliance gaps |
| S-011 | S-007 output | Evidence verification + citation audit |
| S-012 | S-011 output | FMEA matrix + failure mode rankings |
| S-013 | S-012 output | Inversion analysis + hidden assumption map |
| S-014 | All prior | Quality score (0.0-1.0) + dimension breakdown |

---

## Quality Gate Rules

**H-13 (Quality Threshold):** C4 deliverables require >= 0.92 weighted composite score. C4 iterations typically target >= 0.95 for exemplary quality.

**H-14 (Creator-Critic-Revision Cycle):** Minimum 3 iterations required for C4. Maximum 8 iterations (per RT-M-010) before escalation.

**H-15 (Self-Review):** S-010 is mandatory before any external critique (enforced by S-010 placement at position 1).

**H-16 (Steelman Before Critique):** S-003 must execute before S-002 and any challenge strategies (enforced by ordering).

**H-17 (Quality Scoring):** S-014 scoring is mandatory for all C4 deliverables (enforced by S-014 inclusion and final position).

**H-18 (Constitutional Compliance):** S-007 constitutional audit is mandatory (enforced by S-007 inclusion at position 6).

---

## Iteration Ceiling

Per RT-M-010 (MEDIUM standard):

| Criticality | Min Iterations | Max Iterations | Condition |
|-------------|----------------|----------------|-----------|
| C4 | 3 | 8 | Ceiling per criticality |

**Current Iteration:** 1 of 8

**Early Halt Condition (Plateau Detection):** If quality score delta < 0.01 for 3 consecutive iterations, circuit breaker activates and work halts with current best result.

---

## Output Artifacts

After each strategy execution, produce:

1. **Strategy output file:** `c4-tournament-iter{N}-s{NNN}-{strategy-slug}-results.md`
2. **Cumulative scorecard:** `c4-tournament-iter{N}-scorecard.md` (updated after each strategy)
3. **Final iteration summary:** `c4-tournament-iter{N}-final-assessment.md` (after S-014)

**Example paths (Iteration 1):**
- `c4-tournament-iter1-s-010-self-refine-results.md`
- `c4-tournament-iter1-s-003-steelman-results.md`
- `c4-tournament-iter1-scorecard.md` (updated iteratively)
- `c4-tournament-iter1-final-assessment.md` (after S-014)

---

## Self-Review (H-15 Compliance)

This execution plan has been reviewed for:

1. **Strategy Set Completeness:** All 10 required C4 strategies included ✓
2. **H-16 Ordering:** S-003 (pos 2) before S-002 (pos 3) ✓
3. **Template Path Validity:** All 10 paths follow standard pattern `.context/templates/adversarial/s-{NNN}-{slug}.md` ✓
4. **Logical Sequencing:** Groups A-F follow recommended execution order (self-review → strengthen → challenge → verify → decompose → score) ✓
5. **Constraint Satisfaction:** H-13, H-14, H-15, H-16, H-17, H-18 all addressed ✓

**Plan Status:** Ready for execution

---

## Constitutional Compliance (P-003, P-020, P-022)

| Principle | Compliance | Evidence |
|-----------|-----------|----------|
| P-003 (No recursive subagents) | Compliant | This agent (adv-selector) produces a selection plan only; does not invoke other agents |
| P-020 (User authority) | Compliant | User requested C4 tournament; selection respects all required strategies per SSOT |
| P-022 (No deception) | Compliant | All strategies listed transparently; no excluded strategies without documentation |

---

## References

**SSOT:** `.context/rules/quality-enforcement.md`

**Source Sections:**
- Criticality Levels (L-150-156)
- Strategy Catalog (L-273-299)
- Implementation (L-302-327)
- Auto-Escalation Rules (L-240-254)

**Agent Definition:** `skills/adversary/agents/adv-selector.md` (v1.0.0)

**Related:** ADR-EPIC002-001 (strategy scores), ADR-EPIC002-002 (enforcement architecture)

---

**Plan Created:** 2026-03-03
**Agent:** adv-selector (Strategy Selector)
**Status:** Ready for adv-executor invocation
