# C4 Tournament Strategy Execution Plan — Iteration 6

**Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Deliverable Type:** GitHub Enhancement Issue (C4 Tournament)
**Criticality Level:** C4 (Critical)
**Iteration:** 6 (post-R5 revision)
**Prior Scores:** I1: 0.704 | I2: 0.724 | I3: 0.761 | I4: 0.835 | I5: 0.867

---

## Criticality Assessment

- **Requested Level:** C4
- **Auto-Escalation Applied:** No
- **Final Level:** C4 (Critical — Irreversible public GitHub deliverable, architecture-defining)

**Escalation Check Results:**
- AE-001 (Constitution touch): Not triggered
- AE-002 (Rules touch): Not triggered
- AE-003 (New/modified ADR): Not triggered
- AE-004 (Baselined ADR modification): Not triggered
- AE-005 (Security-relevant code): Not triggered

**Justification:** This is a public GitHub Enhancement Issue introducing a major new skill (`/user-experience` with 10 sub-skills, parent orchestrator architecture, governance-relevant structure, MCP integration patterns). The deliverable is irreversible once published and architecture-defining for the Jerry framework.

---

## Selected Strategies (Ordered)

Per quality-enforcement.md Criticality Levels table, **C4 criticality requires ALL 10 selected strategies** with no optional exclusions and no removals.

Execution order enforces:
- **H-16 constraint:** Steelman (S-003) MUST be ordered BEFORE Devil's Advocate (S-002)
- **Recommended group ordering:** Self-Review → Strengthen → Challenge → Verify → Decompose → Score

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Notes |
|-------|-------------|---------------|---------------|-------------------|-------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | Group A: Self-Review. Initial polish. |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required (H-16) | Group B: Strengthen. Build strongest version before critique. |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required (H-16) | Group C: Challenge. After Steelman (H-16). |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | Group C: Challenge. Failure modes and mitigation. |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | Group C: Challenge. Offensive assessment and competitive threats. |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | Group D: Verify. Governance and constitutional compliance. |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | Group D: Verify. Claims validation and evidence tracing. |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | Group E: Decompose. Failure mode and effects analysis. |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | Group E: Decompose. Inverse thinking for gap detection. |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | Group F: Score. Quality gate scoring — ALWAYS LAST (H-17). |

---

## H-16 Compliance Check

**Steelman-Before-Critique Constraint:**
- S-003 (Steelman Technique) position: **2**
- S-002 (Devil's Advocate) position: **3**
- **Status:** ✓ SATISFIED — S-003 (pos 2) ordered before S-002 (pos 3)

Per H-16: "Steelman (S-003) MUST be applied before Devil's Advocate (S-002). Canonical review pairing."

---

## Strategy Overrides Applied

**User Overrides:** None received
**System Overrides:** None applied
**All 10 strategies included:** Yes — C4 criticality requires all selected strategies per quality-enforcement.md

---

## Execution Notes

### Prior Iteration Performance
- **I5 score (prior iteration):** 0.867
- **Score trajectory:** Converging upward (0.704 → 0.724 → 0.761 → 0.835 → 0.867)
- **Target threshold:** >= 0.92 (H-13)
- **Expected I6 outcome:** Tournament application of all 10 strategies should bridge the 0.053-point gap to threshold

### Strategy Grouping Rationale

**Group A — Self-Review (S-010):**
- Initial author self-correction before external critique
- Catches obvious defects that consume critic cycles
- Per H-15: "Self-review REQUIRED before presenting"

**Group B — Strengthen (S-003):**
- Build the strongest possible version of the argument
- Preempts premature rejection of sound approaches
- Must execute before Group C per H-16

**Group C — Challenge (S-002, S-004, S-001):**
- Three complementary adversarial lenses:
  - S-002: Dialectical opposition (Devil's Advocate)
  - S-004: Prospective failure modes (Pre-Mortem)
  - S-001: Offensive security/competitive threats (Red Team)

**Group D — Verify (S-007, S-011):**
- S-007: Constitutional AI Critique — governance/policy compliance
- S-011: Chain-of-Verification — evidence and claims tracing

**Group E — Decompose (S-012, S-013):**
- S-012: FMEA — systematic failure analysis
- S-013: Inversion — gap detection via inverse thinking

**Group F — Score (S-014):**
- LLM-as-Judge with 6-dimension quality rubric
- Always last per H-17
- Produces quantitative score for quality gate enforcement (H-13)

---

## Quality Gate Criteria

**Threshold:** >= 0.92 (H-13)
**Failure outcome:** Deliverable rejected; revision required
**Dimensions (per S-014 rubric):**
1. Completeness (weight: 0.20)
2. Internal Consistency (weight: 0.20)
3. Methodological Rigor (weight: 0.20)
4. Evidence Quality (weight: 0.15)
5. Actionability (weight: 0.15)
6. Traceability (weight: 0.10)

---

## Self-Review Before Persistence (H-15)

**Plan verification:**

✓ All strategy IDs valid (S-001, S-002, S-003, S-004, S-007, S-010, S-011, S-012, S-013, S-014)
✓ H-16 ordering satisfied (S-003 pos 2 before S-002 pos 3)
✓ Auto-escalation rules checked (none triggered)
✓ User overrides documented (none received)
✓ All template paths resolved and verified to exist
✓ Criticality level confirmed as C4 per quality-enforcement.md definition
✓ Constitutional compliance verified (P-002, P-003, P-020, P-022)

---

## References

**Source Documents:**
- `.context/rules/quality-enforcement.md` — Criticality levels, strategy catalog, H-16, H-13, H-17
- `agent-development-standards.md` — Ordering rules and group definitions
- `.context/templates/adversarial/` — All 10 strategy execution templates

**Related Artifacts:**
- Deliverable: `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- Prior iteration scores: I1: 0.704, I2: 0.724, I3: 0.761, I4: 0.835, I5: 0.867

---

*Plan Version: 1.0*
*Generated by: adv-selector agent*
*Plan Status: Ready for adv-executor invocation*
*Constitutional Compliance: P-002 (persistence), P-003 (no recursion), P-020 (user authority), P-022 (no deception)*
