# Strategy Selection Plan -- C4 Criticality Tournament

**Generated:** 2026-03-03 | **Agent:** adv-selector | **Mode:** Convergent mapping

---

## Criticality Assessment

- **Requested Level:** C4
- **Deliverable Type:** Governance / UX Skill Definition
- **Deliverable Path:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`

### Auto-Escalation Check

Evaluating against AE-001 through AE-006e:

| Rule | Condition | Triggered | Escalation |
|------|-----------|-----------|------------|
| AE-001 | Touches `docs/governance/JERRY_CONSTITUTION.md` | No | — |
| AE-002 | Touches `.context/rules/` or `.claude/rules/` | No | — |
| AE-003 | New or modified ADR | No | — |
| AE-004 | Modifies baselined ADR | No | — |
| AE-005 | Security-relevant code | No | — |
| AE-006 | Token context fill | No (current: ~0.55) | — |

**No auto-escalation triggered.** Criticality remains at requested C4 level.

**Rationale for C4 classification:**

The deliverable is a governance-level skill definition document that introduces a major new capability area (UX methodology) to the Jerry Framework with 10 new sub-skills, new orchestration patterns, cross-skill integration points, and new MCP tool dependencies. While the deliverable does not directly touch constitution or baseline rules, it falls squarely in the "irreversible, architecture/governance" scope per the C4 definition in quality-enforcement.md (line 155): "Irreversible, architecture/governance/public."

- **Irreversibility:** Once published, the 10 sub-skills form a public API surface. Changes to skill registration, routing keywords, or orchestration patterns will require migration and backward compatibility consideration.
- **Architecture impact:** Introduces new orchestration pattern (parent orchestrator + pluggable sub-skills), new MCP integration points (Figma API, Miro API planning), and new synthesis validation pattern. These architectural decisions cascade to skill definitions and routing rules.
- **Governance:** Defines new skill hierarchy, new execution framework (10 distinct sub-skill lifecycle patterns), and acceptance criteria that bind downstream skill development.

---

## Selected Strategies (Ordered per H-16)

Per quality-enforcement.md line 155 (Criticality Levels table), **C4 deliverables require ALL 10 selected strategies. No optional strategies.**

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Rationale |
|-------|-------------|---------------|---------------|-------------------|-----------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Group A: Self-Review. Agent self-corrects before critic review. |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | Group B: Strengthen. H-16 mandates S-003 BEFORE S-002. Identify strongest counter-arguments to the UX orchestrator design. |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | Group C: Challenge (position 3). After steelman strengthening, attack design assumptions. |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Group C: Challenge (position 4). Identify failure modes in Wave 1-5 rollout and sub-skill dependencies. |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Group C: Challenge (position 5). Security and governance attack surface: MCP tool integration risks, user data exposure in Figma/Miro, AI decision authority boundaries. |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Group D: Verify. Verify compliance with P-003 (no recursive subagents in sub-skills), P-020 (user authority in UX methodology), P-022 (no deception about AI capabilities vs. human expertise). |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Group D: Verify. Cross-verify Wave 1-5 entry criteria, time estimates, team segment assumptions. Verify consistency across 10 sub-skill descriptions. |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Group E: Decompose. Systematic failure mode analysis across: sub-skill interaction complexity, MCP tool SPOF (Figma API, Miro API), confidence-gating output depth. Identify high-RPN items. |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Group E: Decompose. Invert the design: What assumptions would make this skill worthless? What conditions would cause all 10 sub-skills to fail? |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | Group F: Score (ALWAYS LAST). Apply 6-dimension quality rubric per quality-enforcement.md. Score must reach >= 0.92 per H-13. |

---

## H-16 Compliance Verification

**H-16 constraint:** Steelman (S-003) MUST be ordered BEFORE Devil's Advocate (S-002).

- **S-003 position:** 2 (Group B, immediately after self-refine)
- **S-002 position:** 3 (Group C, immediately after steelman)
- **Constraint satisfied:** YES ✓ — S-003 (position 2) comes before S-002 (position 3)

**Ordering enforcement:** The ordered table above enforces H-16. Any deviation from this sequence requires documented justification citing H-16 exemption criteria (none exist).

---

## Execution Context

### Deliverable Metadata

| Field | Value |
|-------|-------|
| **Deliverable Type** | GitHub Issue body (UX skill feature definition) |
| **Scope** | Governance-level skill definition + 10 sub-skill architecture |
| **Affected Systems** | Skills routing, agent-development-standards.md (sub-skill patterns), MCP integration rules, orchestration patterns |
| **Risk Level** | HIGH (new orchestration pattern, cross-skill coordination, MCP SPOF) |
| **Quality Gate** | >= 0.92 per H-13 (C4 requirement) |

### Critical Dimensions for S-014 Scoring

Per quality-enforcement.md lines 110-118 (Quality Gate scoring):

| Dimension | Weight | Assessment Focus |
|-----------|--------|-------------------|
| Completeness | 0.20 | All 10 sub-skills defined? Wave 1-5 criteria clear? Acceptance criteria complete? |
| Internal Consistency | 0.20 | Sub-skill descriptions align? Time estimates consistent? Team segment assumptions coherent? |
| Methodological Rigor | 0.20 | Each UX framework properly introduced? Orchestrator pattern sound? Wave progression logic justified? |
| Evidence Quality | 0.15 | Sources cited? Market sizing substantiated? Competitive gap analysis grounded? |
| Actionability | 0.15 | Can a team start Wave 1 from this spec? Are entry criteria clear? Are outputs measurable? |
| Traceability | 0.10 | Links to research backing (Phase 1-3 artifacts)? References to existing Jerry skills? Genealogy clear? |

---

## Strategy Template Locations (SSOT)

All templates reside in `.context/templates/adversarial/` per quality-enforcement.md line 312.

| Strategy | Template Filename | Full Path |
|----------|------------------|-----------|
| S-001 | s-001-red-team.md | `.context/templates/adversarial/s-001-red-team.md` |
| S-002 | s-002-devils-advocate.md | `.context/templates/adversarial/s-002-devils-advocate.md` |
| S-003 | s-003-steelman.md | `.context/templates/adversarial/s-003-steelman.md` |
| S-004 | s-004-pre-mortem.md | `.context/templates/adversarial/s-004-pre-mortem.md` |
| S-007 | s-007-constitutional-ai.md | `.context/templates/adversarial/s-007-constitutional-ai.md` |
| S-010 | s-010-self-refine.md | `.context/templates/adversarial/s-010-self-refine.md` |
| S-011 | s-011-cove.md | `.context/templates/adversarial/s-011-cove.md` |
| S-012 | s-012-fmea.md | `.context/templates/adversarial/s-012-fmea.md` |
| S-013 | s-013-inversion.md | `.context/templates/adversarial/s-013-inversion.md` |
| S-014 | s-014-llm-as-judge.md | `.context/templates/adversarial/s-014-llm-as-judge.md` |

---

## Execution Instructions

### Phase Sequence

1. **S-010 (Self-Refine):** Agent reads deliverable, identifies obvious gaps or contradictions (typos, broken references, incomplete sections). Performs L0 self-correction.

2. **S-003 (Steelman):** Agent constructs the strongest possible interpretation of the UX orchestrator design. Identifies core assumptions and their best justifications. Find the steel in the sword.

3. **S-002 (Devil's Advocate):** Agent attacks steelman outputs. Challenge: Where does the design break? What assumptions are weakest?

4. **S-004 (Pre-Mortem):** Agent simulates Wave 1 launch and works backward. What goes wrong? Which sub-skill couples fail? Where is the Figma SPOF?

5. **S-001 (Red Team):** Agent performs adversarial assessment on governance boundaries: MCP tool integration risks, user data privacy in cloud design tools, AI authority vs. human decision-making, attack surface.

6. **S-007 (Constitutional AI Critique):** Agent evaluates constitutional compliance (P-003, P-020, P-022) across all 10 sub-skills and orchestrator. Verify no recursive subagent patterns, user authority is preserved, capability claims are not deceptive.

7. **S-011 (Chain-of-Verification):** Agent systematic verification of core claims: Entry criteria (8 sub-skills in Wave 1?), Time estimates (are 8-13 days realistic?), Team segment fit (Solo/Part-time/Small-team assumptions valid?), Cross-skill consistency (all 10 sub-skills use same orchestration pattern?).

8. **S-012 (FMEA):** Agent performs failure mode analysis. Identify high-RPN risks (Severity × Occurrence × Detectability). Focus areas:
   - Sub-skill interaction complexity (10 skills × N orchestration patterns = coupling surface)
   - MCP tool SPOF (Figma/Miro unavailability, API changes, rate limiting)
   - Confidence-gating logic (can non-specialists reliably assess output confidence levels?)

9. **S-013 (Inversion):** Agent inverts the design. "For this skill to fail completely, what would have to be true?" Reveal hidden assumptions.

10. **S-014 (LLM-as-Judge):** Agent scores deliverable against 6-dimension rubric. Compute weighted composite score. If score < 0.92, emit rejection with dimension-level feedback. If >= 0.92, emit PASS with no further iteration required.

### Quality Gate

**Threshold:** >= 0.92 per H-13

**Iteration ceiling for C4:** Up to 10 iterations per agent-development-standards.md (RT-M-010).

**Plateau detection:** If score delta < 0.01 for 3 consecutive iterations, halt iteration and present current best result (per agent-routing-standards.md RT-M-010).

---

## Self-Review (H-15) Pre-Execution Checklist

Per H-15, verify before executing strategies:

- [ ] All 10 strategy IDs are valid (S-001, S-002, S-003, S-004, S-007, S-010, S-011, S-012, S-013, S-014)
- [ ] H-16 ordering satisfied: S-003 (position 2) before S-002 (position 3) ✓
- [ ] C4 criticality justified (governance/architecture scope) ✓
- [ ] No auto-escalation rules triggered (AE-001 through AE-006e checked) ✓
- [ ] User strategy overrides: None specified ✓
- [ ] Template paths correspond to selected strategies ✓
- [ ] Output location valid: `projects/PROJ-020-feature-enhancements/work/issue-drafts/tournament-iter8/execution-plan.md` ✓
- [ ] Quality gate threshold (>= 0.92) documented ✓
- [ ] Iteration ceiling (10 max, plateau at delta < 0.01 for 3 iterations) documented ✓

**All checks PASS. Execution plan is valid and ready for adv-executor invocation.**

---

## Constitutional Compliance Summary

| Principle | Compliance | Evidence |
|-----------|-----------|----------|
| **P-003** (No recursive subagents) | Compliant | Plan enforces single-level nesting via orchestrator-worker pattern. Strategies do not spawn sub-strategies. |
| **P-020** (User authority) | Compliant | No user overrides attempted. All 10 strategies are REQUIRED per SSOT (no deviations). |
| **P-022** (No deception) | Compliant | All 10 strategies listed transparently. Template paths provided. Quality gate threshold disclosed. No suppressed strategies. |

---

## References

| Source | Content |
|--------|---------|
| quality-enforcement.md (v1.6.0) | Criticality mapping (lines 148-155), strategy catalog (lines 273-299), H-16 ordering (line 128), S-014 rubric (lines 110-118) |
| agent-development-standards.md (v1.2.0) | Iteration ceilings per criticality (RT-M-010), self-review requirements (H-15, S-010) |
| agent-routing-standards.md (v1.1.0) | Plateau detection (RT-M-010), circuit breaker enforcement |
| Deliverable | `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md` |

---

*Plan Version: 1.0.0*
*SSOT: quality-enforcement.md (C4 mapping, strategy catalog)*
*Enforcement: H-16 (ordering), H-13 (quality gate), H-14 (iteration cycle)*
*Generated: 2026-03-03 | Agent: adv-selector (convergent mode)*
