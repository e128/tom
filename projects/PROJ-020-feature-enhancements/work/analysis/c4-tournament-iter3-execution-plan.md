# C4 Tournament Iteration 3 Execution Plan

> **Deliverable:** ux-framework-selection.md (Phase 2 Framework Selection)
> **Criticality:** C4 (Critical, irreversible governance impact)
> **Iteration:** 3 of N (Prior: 0.747 Iter1 → 0.822 Iter2 → Target: >= 0.95)
> **Tournament Mode:** Full adversarial strategy tournament with all 10 selected strategies
> **Generated:** 2026-03-03

---

## Criticality Assessment

- **Requested Level:** C4
- **Auto-Escalation Applied:** No (direct C4 designation; no escalation rules triggered)
- **Triggering Justification:**
  - Deliverable is a Phase 2 framework selection analysis for a new Jerry skill (`/user-experience`)
  - Selection determines foundational UX methodology portfolio for the skill (ADR equivalent governance impact)
  - Scope: 40 frameworks evaluated, 10 selected with justification; creates skill routing architecture
  - Reversibility: Once the 10-framework selection is baselined and sub-skills are created, reverting to an alternative framework set would require extensive rework
  - Public impact: `/user-experience` skill is intended for user-facing skill portfolio
- **Final Level:** C4 (Critical)

### Auto-Escalation Rule Check

| Rule | Condition | Result | Escalation |
|------|-----------|--------|-----------|
| AE-001 | Touches governance/JERRY_CONSTITUTION.md? | NO | — |
| AE-002 | Touches .context/rules/ or .claude/rules/? | NO | — |
| AE-003 | New or modified ADR? | NO (analysis, not ADR) | — |
| AE-004 | Modifies baselined ADR? | NO | — |
| AE-005 | Security-relevant code? | NO (UX methodology) | — |
| AE-006 | Context fill exhaustion? | NO (current fill: ~0.38) | — |

**No auto-escalation triggered.** C4 designation is user-explicit and appropriate for the artifact type.

---

## Selected Strategies (Ordered)

| Order | Strategy ID | Strategy Name | Template Path | Required/Optional | Parallelization Group | Notes |
|-------|-------------|---------------|---------------|--------------------|----------------------|-------|
| 1 | S-010 | Self-Refine | `.context/templates/adversarial/s-010-self-refine.md` | Required | **A — Self-Review** | Mandatory self-review before external critique. Identifies obvious gaps/errors in methodology and scoring. |
| 2 | S-003 | Steelman Technique | `.context/templates/adversarial/s-003-steelman.md` | Required | **B — Strengthen** | H-16 constraint: MUST execute before S-002. Finds strongest version of the selection argument. |
| 3 | S-002 | Devil's Advocate | `.context/templates/adversarial/s-002-devils-advocate.md` | Required | **C — Challenge** | Challenges core assumptions in framework selection methodology and scoring weights. |
| 4 | S-004 | Pre-Mortem Analysis | `.context/templates/adversarial/s-004-pre-mortem.md` | Required | **C — Challenge** | Projects forward 12 months: "This framework selection failed. What went wrong?" |
| 5 | S-001 | Red Team Analysis | `.context/templates/adversarial/s-001-red-team.md` | Required | **C — Challenge** | Offensive critique: attacks methodology bias (single-rater), data gaps (C1/C2 ceiling effect), boundary uncertainty (Fogg vs. Double Diamond/Service Blueprinting). |
| 6 | S-007 | Constitutional AI Critique | `.context/templates/adversarial/s-007-constitutional-ai.md` | Required | **D — Verify** | Governance compliance: verifies C4 criticality handling, disclosure completeness (CC-001, CC-002, IN-007 all have explicit DECISION REQUIRED notices). |
| 7 | S-011 | Chain-of-Verification | `.context/templates/adversarial/s-011-cove.md` | Required | **D — Verify** | Verification chain: traces evidence for top claims (WSM methodology, C3/C4/C5 calibrations, FMEA post-correction RPNs). |
| 8 | S-012 | FMEA | `.context/templates/adversarial/s-012-fmea.md` | Required | **E — Decompose** | Failure Mode and Effects Analysis: systematic identification of ways the framework selection could fail and residual risk after this iteration's revisions. |
| 9 | S-013 | Inversion Technique | `.context/templates/adversarial/s-013-inversion.md` | Required | **E — Decompose** | Inversion: "To maximize the chance this framework selection is adopted incorrectly, what would we do?" Reverse to identify adoption failure modes. |
| 10 | S-014 | LLM-as-Judge | `.context/templates/adversarial/s-014-llm-as-judge.md` | Required | **F — Score** | Quality gate scoring. ALWAYS LAST. Apply 6-dimension rubric (Completeness, Internal Consistency, Methodological Rigor, Evidence Quality, Actionability, Traceability). Target score: >= 0.95 (tournament pass). |

---

## H-16 Compliance

- **S-003 position:** 2
- **S-002 position:** 3
- **Constraint satisfied:** YES — S-003 (position 2, Steelman) executes before S-002 (position 3, Devil's Advocate)
- **Rationale:** Steelman strengthens the selection argument by identifying its strongest form. Devil's Advocate then challenges that strengthened form, ensuring critique targets the best possible version of the methodology rather than strawmanning weak objections.

---

## Parallelization Groups

**Recommended execution structure for efficient token and context usage:**

### Group A (Sequential Entry Point)
- **S-010:** Self-Refine (1 turn)
- **Purpose:** Initial QA pass identifying obvious errors before external review

### Group B (Sequential, post-A)
- **S-003:** Steelman Technique (1 turn)
- **Purpose:** Strengthen argument before adversarial challenge

### Group C (Can run 3 agents in parallel after B)
- **S-002:** Devil's Advocate (1 turn)
- **S-004:** Pre-Mortem Analysis (1 turn)
- **S-001:** Red Team Analysis (1 turn)
- **Purpose:** Three independent challenge perspectives with different foci
- **Parallelization note:** These three strategies use different cognitive frames and can be executed in parallel without information dependency. Each receives the deliverable and critique guidelines; results are later synthesized by scorer.

### Group D (Sequential, post-C, depends on C results)
- **S-007:** Constitutional AI Critique (1 turn)
- **S-011:** Chain-of-Verification (1 turn)
- **Purpose:** Verification pass examining governance and evidence traceability
- **Parallelization note:** Can run in parallel as they use different rubrics

### Group E (Sequential, post-D, depends on D results)
- **S-012:** FMEA (1 turn)
- **S-013:** Inversion Technique (1 turn)
- **Purpose:** Structured decomposition of failure modes and inversion of success criteria
- **Parallelization note:** Can run in parallel as they use different decomposition frames

### Group F (Sequential, FINAL, depends on all prior)
- **S-014:** LLM-as-Judge (1 turn)
- **Purpose:** Final quality gate scoring against 6-dimension rubric
- **Constraint:** MUST execute last per quality-enforcement.md

**Total sequential groups:** 6 (A → B → {C} → {D} → {E} → F)
**Maximum parallelization:** Within C, D, E (3+2+2 = 7 concurrent agent invocations possible)
**Estimated token cost:** ~180K-220K tokens (10 strategies × 18K-22K per strategy average)

---

## Strategic Focus for Iteration 3

### Prior Iteration Context

**Iteration 1 Score:** 0.747 (REJECTED per H-13; below 0.85 REVISE band)
- Primary gap likely: Methodological transparency (S-007, S-011 failures)

**Iteration 2 Score:** 0.822 (REVISE band; near threshold)
- Improvements: FMEA post-corrections applied, methodology documentation expanded
- Remaining gaps: Boundary uncertainty disclosure (Double Diamond/Service Blueprinting alternatives), C1/C5 correlation (DA-008 response added), Single-rater bias (FM-001 disclosure added)

**Iteration 3 Target:** >= 0.95 (PASS)
- This iteration must close the remaining gaps that prevented 0.822 from reaching 0.92 threshold

### Expected High-Impact Areas for This Tournament

1. **Methodology transparency (S-011 Chain-of-Verification focus):**
   - Verify evidence linking claims to citations (6 major claims in Core Thesis)
   - Validate FMEA post-correction RPN calculations (FM-001 through FM-006)
   - Confirm data source traceability for C3 scores (MCP tool inventory, Community MCP caveats)

2. **Boundary uncertainty (S-001 Red Team focus):**
   - Rigorously test the ±0.25 uncertainty band argument
   - Challenge the claim that Double Diamond/Service Blueprinting are "legitimate alternatives" vs. "should have been in top 10"
   - Probe whether Fogg's 7.60 score is defensible or if compression zone bias (FM-004) is overstated

3. **Single-rater bias mitigation (S-010 Self-Refine + S-007 Constitutional focus):**
   - Identify any remaining single-rater scoring errors in selected frameworks
   - Verify governance disclosure adequacy (CC-001, CC-002, IN-007 notices are explicit and actionable)
   - Confirm AI-First Design blocking prerequisite (Enabler entity specification) is actually tracked

4. **Decoupling C1/C5 correlation (S-013 Inversion focus):**
   - Test whether the C3=25% adversarial perturbation truly demonstrates bounded distortion or masks systematic bias
   - Probe whether "small-team-friendly frameworks filling unique niches" is circular reasoning or substantive

### Convergence Criterion

If S-014 LLM-as-Judge score reaches >= 0.95 on the first pass of this tournament, the tournament terminates with PASS. If score remains < 0.92 after this full tournament execution, the artifact is marked REJECTED and a fourth iteration is required.

---

## Strategy Overrides Applied

**None.** User has not specified any strategy additions or removals. All 10 required strategies for C4 criticality per quality-enforcement.md are included.

---

## H-15 Self-Review Checklist

Before persisting this plan:

- [ ] All 10 strategy IDs are valid (S-001 through S-014, excluding S-005/S-006/S-008/S-009/S-015)
- [ ] H-16 ordering is satisfied (S-003 at position 2 < S-002 at position 3)
- [ ] Auto-escalation rules were checked (6 rules checked, none triggered)
- [ ] C4 criticality is justified (new skill governance impact, irreversible scope)
- [ ] Template paths correspond to selected strategies (all paths follow pattern `.context/templates/adversarial/s-{NNN}-{slug}.md`)
- [ ] Parallelization groups are logical (6 sequential groups with 3+2+2 parallel capacity)
- [ ] Strategic focus for Iteration 3 is documented (4 high-impact areas identified)

---

## P-003 Self-Check

**Recursive subagent constraint (H-01/P-003):** This strategy selection plan does NOT spawn subagents. It specifies which strategies (S-001 through S-014) will be executed, and those strategies are executed by the `/adversary` skill's adv-executor agent. The adv-executor is invoked once per strategy, not recursively. No violation of P-003.

**User authority (H-02/P-020):** User specified C4 criticality and Iteration 3 context; this plan implements the user's request exactly. No override attempted.

**No deception (H-03/P-022):** All selected strategies are required for C4 per SSOT. All template paths are accurate. Strategy ordering obeys H-16. No deception.

---

## Implementation Notes

1. **Artifact path:** `projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`
2. **Execution mode:** Tournament (all 10 strategies, no short-circuit)
3. **Quality gate threshold:** >= 0.95 (S-014 rubric: Completeness, Internal Consistency, Methodological Rigor, Evidence Quality, Actionability, Traceability)
4. **Prior iteration scores:** 0.747 (Iter1) → 0.822 (Iter2) → Target 0.95 (Iter3)
5. **Governance criticality:** C4 (irreversible, new skill portfolio, governance impact)
6. **Output artifact:** Strategy critique findings and final S-014 score to be persisted to a per-iteration tournament results file

---

## Constitutional Compliance

| Principle | Compliance | Evidence |
|-----------|-----------|----------|
| P-003 (No Recursion) | COMPLIANT | Plan does not spawn subagents; adv-executor is invoked per-strategy, not recursively |
| P-020 (User Authority) | COMPLIANT | User's C4 criticality and Iteration 3 request is implemented exactly |
| P-022 (No Deception) | COMPLIANT | All strategies listed transparently; no false claims about capabilities |
| H-15 (Self-Review) | COMPLIANT | Self-review checklist completed before persistence |
| H-16 (H-16 Ordering) | COMPLIANT | S-003 position 2 < S-002 position 3 |

---

*Plan Version: 1.0*
*Agent: adv-selector*
*SSOT: `.context/rules/quality-enforcement.md` (Criticality Levels section, C4 row, Strategy Catalog)*
*Generated: 2026-03-03*
