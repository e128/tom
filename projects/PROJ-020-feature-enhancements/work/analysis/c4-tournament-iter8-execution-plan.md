# C4 Tournament Iteration 8 - Strategy Execution Plan

**Deliverable:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`

**Analysis:** UX Framework Selection - Weighted Multi-Criteria Analysis for Jerry `/user-experience` skill

**Tournament Context:** Final iteration (8 of 8) of C4 adversarial tournament; prior iteration score: 0.851 (REVISE band); target: >= 0.95

---

## Strategy Selection Plan

### Criticality Assessment

- **Requested Level:** C4 (Critical)
- **Auto-Escalation Applied:** No (deliverable is intrinsically C4 — architecture/governance scope for Jerry framework skill)
- **Final Level:** C4

**Justification:** This deliverable defines the framework portfolio for a new Jerry skill (`/user-experience`), making it architecture-critical and irreversible once implemented. The analysis includes synthesis recommendations (AI-First Design) requiring project commitment and multi-skill coordination. This qualifies as C4 under the "architecture/governance" criterion in quality-enforcement.md.

---

### Selected Strategies (Ordered per H-16)

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Rationale |
|-------|-------------|---------------|---------------|-------------------|-----------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Self-review pass before external critique; catch obvious defects early |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | Strengthen the analysis before challenging it; identify the strongest version of each argument |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | H-16 ordering satisfied: S-003 (position 2) before S-002 (position 3). Challenge core assumptions and framework selections |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Identify failure modes in implementation; what could go wrong when teams adopt this portfolio |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Adversarial attack on the analysis methodology; probe for systemic blind spots |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Verify governance compliance; ensure analysis respects Jerry framework principles |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Trace verification chain; validate that supporting evidence is complete and consistent |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Structured failure mode analysis across portfolio adoption scenarios |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Identify what would make the analysis *fail*; work backward from failure states |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | Apply strict quality gate rubric; score against 6 weighted dimensions (Completeness, Internal Consistency, Methodological Rigor, Evidence Quality, Actionability, Traceability) |

---

## H-16 Compliance

**Constraint:** S-003 (Steelman Technique) MUST be ordered BEFORE S-002 (Devil's Advocate)

- S-003 position: **2**
- S-002 position: **3**
- **Constraint satisfied:** YES — S-003 (position 2) executes before S-002 (position 3)

**Rationale:** Steelman identifies the strongest form of each framework selection argument before Devil's Advocate attacks it. This ordering prevents premature rejection of sound approaches and ensures critique is directed at the best version of the analysis, not strawman versions.

---

## Tournament Iteration Context

| Metric | Value |
|--------|-------|
| Current Iteration | 8 (FINAL) |
| Prior 7 Iteration Scores | 0.747, 0.822, 0.848, 0.803, 0.843, 0.862, 0.851 |
| Current Score Band | REVISE (0.85-0.91) |
| Quality Gate Threshold | >= 0.92 |
| Target Score (Iteration 8) | >= 0.95 (closing the gap from prior 0.851) |
| Minimum Iterations (H-14) | 3 (satisfied; currently at 8) |
| Iteration Ceiling per Criticality (RT-M-010) | C4 = 10 iterations max |
| Plateau Detection | Score delta < 0.01 for 3 consecutive iterations → early halt |

**Status:** With 7 prior iterations and final iteration 8 in progress, this represents a mature refinement cycle. The strategy execution order (S-010 → S-003 → S-002 → S-004 → S-001 → S-007 → S-011 → S-012 → S-013 → S-014) is designed to progressively strengthen, challenge, and validate the analysis in a structured sequence.

---

## Execution Notes

### Strategy Execution Order Rationale

The ordering follows the recommended execution sequence from quality-enforcement.md with C4-specific emphasis:

1. **S-010 (Self-Refine)** — Self-review identifies obvious defects before external critique consumes reviewer cycles
2. **S-003 (Steelman)** — Identify strongest arguments and implicit assumptions before attacking them
3. **S-002 (Devil's Advocate)** — Challenge assumptions with full force (now attacking the strongest version)
4. **S-004 (Pre-Mortem)** — Operationalize the critique: what fails in real-world adoption
5. **S-001 (Red Team)** — Systemic attack on methodology and underlying reasoning
6. **S-007 (Constitutional AI)** — Verify governance alignment; check for principle violations
7. **S-011 (Chain-of-Verification)** — Trace evidence chains; validate support completeness
8. **S-012 (FMEA)** — Structured risk analysis across failure modes and severity levels
9. **S-013 (Inversion)** — Identify what would make the analysis completely fail
10. **S-014 (LLM-as-Judge)** — Apply quality gate rubric; generate final score and dimensional breakdown

### Quality Gate Integration

S-014 (LLM-as-Judge) executes LAST, as required by H-17. The scoring uses the 6-dimension rubric:

| Dimension | Weight | Evaluation Focus |
|-----------|--------|------------------|
| Completeness | 0.20 | All 40 frameworks scored; all selection gaps documented; scope boundaries clear |
| Internal Consistency | 0.20 | Framework selections non-redundant per portfolio composition test; minimality argument sound |
| Methodological Rigor | 0.20 | Weighted Sum Method applied consistently; uncertainty bounds defined; correction rounds transparent |
| Evidence Quality | 0.15 | Supporting research artifacts (survey, Tiny Teams research, MCP tool inventory) cited and current |
| Actionability | 0.15 | Sub-skill routing framework clear; implementation prerequisites enumerated; adoption path defined |
| Traceability | 0.10 | Revision history complete; all findings attributed; decision reversibility documented |

**Target scoring:** >= 0.95 weighted composite (closing from prior 0.851 via 7 iterations of refinement)

---

## Strategic Context for Iteration 8

### Key Improvements from Prior Iterations

The prior 7 iterations (scores 0.747→0.822→0.848→0.803→0.843→0.862→0.851) have progressively:

1. **Eliminated arithmetic errors** — CV-001-I7 through CV-015-I7: all 40 frameworks re-verified
2. **Clarified uncertainty bounds** — DA-001-I7: asymmetric -0.35/+0.15 band (downward bias from 100% correction rate)
3. **Resolved critical findings** — 13 P0 findings in R12 (AI execution taxonomy, synthesis hypothesis validation protocol, gate enforcement)
4. **Enforced high-risk warnings** — User research gap prominently documented with onboarding template
5. **Defined implementation gates** — Section 7.6 synthesis hypothesis validation protocol; mandatory quality gates for AI-First Design outputs

### Remaining Challenges for Iteration 8

The transition from 0.851 (REVISE) to >= 0.95 (PASS) requires the final iteration strategies to:

1. **Validate methodology robustness** — S-013 (Inversion) and S-012 (FMEA) probing failure modes
2. **Close methodological gaps** — S-001 (Red Team) attacking systemic blindness; S-011 (Chain-of-Verification) tracing evidence completeness
3. **Verify governance alignment** — S-007 (Constitutional AI) ensuring framework selections respect Jerry principles
4. **Ensure real-world applicability** — S-004 (Pre-Mortem) identifying deployment risks; S-002 (Devil's Advocate) attacking false assumptions

### No Strategy Overrides Applied

User has not specified any strategy removals or additions beyond the C4 required set. All 10 selected strategies execute as defined in quality-enforcement.md.

---

## Compliance Verification (H-15 Self-Review)

Before persistence, verify:

1. ✓ All strategy IDs are valid (S-001 through S-014, selected set only)
2. ✓ H-16 ordering is satisfied (S-003 position 2 < S-002 position 3)
3. ✓ Auto-escalation rules checked (none triggered; C4 is intrinsic)
4. ✓ User overrides reflected (none specified)
5. ✓ Template paths correspond to selected strategies (all verified via Glob output)

---

## File Persistence

**Plan Status:** READY FOR PERSISTENCE

This execution plan has been self-reviewed per H-15 and is ready for handoff to the adversary skill (`/adversary`, adv-executor agent) for tournament iteration 8 execution.

**Next Step:** Invoke `/adversary` skill with this plan as input to execute strategies S-010 through S-014 in order, culminating in final quality gate score (S-014).

---

*Plan generated: 2026-03-03*

*Strategy Selection SSOT: `.context/rules/quality-enforcement.md`*

*Execution Template SSOT: `.context/templates/adversarial/`*

*Agent Responsibility: adv-selector (this plan) → adv-executor (strategy execution) → adv-scorer (final S-014 quality gate)*
