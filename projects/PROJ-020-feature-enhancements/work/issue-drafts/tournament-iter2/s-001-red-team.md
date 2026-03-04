# Strategy Execution Report: Red Team Analysis

## Execution Context

- **Strategy:** S-001 (Red Team Analysis)
- **Template:** `.context/templates/adversarial/s-001-red-team.md`
- **Deliverable:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Executed:** 2026-03-03T00:00:00Z
- **Iteration:** 2 (R1 revision applied 28 fixes; prior score 0.704 REVISE)
- **H-16 Compliance:** S-003 Steelman applied in prior tournament execution (confirmed via R1 fixes SM-001 through SM-009 annotated throughout deliverable)
- **Finding Prefix:** RT-NNN-iter2

---

# Red Team Report: `/user-experience` Skill Enhancement Issue

**Strategy:** S-001 Red Team Analysis
**Deliverable:** GitHub Enhancement Issue -- feat: Add `/user-experience` skill
**Criticality:** C4 (governance-touching skill definition, architecture, constitutional compliance requirements)
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-001 Red Team Analysis)
**H-16 Compliance:** S-003 Steelman applied in prior tournament round (SM-001 through SM-009 annotations confirmed in deliverable)
**Threat Actor:** Framework Developer Insider -- Goal: ship `/user-experience` skill with minimum governance friction. Capability: full source access, deep Jerry constitutional knowledge, can create agent definitions. Motivation: avoid rework overhead, minimize blocking prerequisites, reduce implementation scope.

---

## Summary

The threat actor is a framework developer who understands Jerry's governance architecture and is motivated to exploit vagueness in acceptance criteria to declare compliance without substantive verification. Despite R1's 28 fixes, the deliverable contains 2 Critical and 6 Major attack vectors concentrated in three areas: (1) acceptance criteria that are structurally unverifiable -- an implementer can mark ACs complete without any external validation mechanism; (2) the AI-First Design conditional path has a circular verification gap where the Enabler's WSM threshold matches the framework's own projected score, enabling self-referential approval; and (3) MCP dependency claims for "bridge" integrations (Hotjar via Zapier) are framed as production-ready but lack the verification gates that would catch MEDIUM-stability integrations failing silently. Recommendation: **REVISE** -- targeted countermeasures required for RT-001 (Critical) and RT-005 (Critical) before acceptance; Major findings addressable in implementation.

---

## Findings Summary

| ID | Severity | Finding | Section |
|----|----------|---------|---------|
| RT-001-iter2 | Critical | Quality benchmark ACs are self-assessed -- no independent calibration artifact or scoring rubric exists to verify the stated pass thresholds | Acceptance Criteria (Wave 1, Wave 2-5) |
| RT-002-iter2 | Major | Wave progression entry criteria are unenforceable -- no mechanism prevents a motivated implementer from falsely asserting criteria are met | Key Design Decisions (Wave Deployment) |
| RT-003-iter2 | Major | P-003 compliance verification is declarative only -- the AC requires the prohibition be stated in frontmatter but does not require runtime or CI enforcement | Acceptance Criteria (Quality Standards) |
| RT-004-iter2 | Major | Synthesis hypothesis confidence gate "override with justification" field creates an auditable bypass path that is structurally indistinguishable from legitimate use | Key Design Decisions (Synthesis Hypothesis Validation) |
| RT-005-iter2 | Critical | AI-First Design Enabler WSM gate is circular -- the Enabler's minimum WSM score (>= 7.80) equals the framework's own projected score (7.80), making the gate trivially self-satisfying | Key Design Decisions / Known Limitations |
| RT-006-iter2 | Major | Hotjar bridge integration is classified as MEDIUM stability and "not plug-and-play" but its failure mode is misclassified as "Enhancement MCP" (cosmetic limitation), while behavioral data it provides is structurally required for B=MAP bottleneck diagnosis accuracy | MCP Integration |
| RT-007-iter2 | Major | The 20% UX capacity threshold for Wave 1 restriction is undefined in measurable terms -- an implementer routes around it by self-reporting any capacity estimate | Key Design Decisions (Routing) |
| RT-008-iter2 | Minor | WSM criteria weights sum check is not cited -- weight reproducibility relies on the reader trusting the table without arithmetic verification access | Research Backing (Framework Selection Scores) |

---

## Detailed Findings

### RT-001-iter2: Quality Benchmark ACs Are Self-Assessed Without Independent Calibration Artifacts [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Acceptance Criteria -- Wave 1 Sub-Skills, Wave 2-5 Sub-Skills |
| **Strategy Step** | Step 2: Ambiguity Exploitation + Step 3: Defense Gap Assessment |
| **Attack Category** | Ambiguity exploitation |
| **Exploitability** | High |
| **Priority** | P0 |
| **Existing Defense** | Missing |

**Evidence:**

Wave 1 AC states:
> "Quality benchmark: agent correctly identifies >= 7 of 10 known heuristic violations in a reference test design (calibration artifact provided with sub-skill)"

Wave 1 JTBD AC states:
> "Quality benchmark: agent produces job statements that a UX practitioner rates as actionable (structured rubric: grammatically correct job format, contains functional + emotional + social dimensions, distinguishes job from solution)"

Wave 2-5 similarly reference benchmarks with numeric thresholds (>= 3 risk categories, >= 80% classification accuracy, >= 90% Kano classification accuracy, >= 5 of 7 violations).

**Attack Vector:**

The calibration artifacts referenced ("reference test design", "reference Storybook", "reference survey dataset", "reference behavioral scenarios") are not defined, do not exist as committed artifacts, and are described as "provided with sub-skill" -- meaning they will be created by the same implementer who is subject to the benchmark. An adversarial implementer creates a trivially easy calibration artifact where the agent is virtually guaranteed to pass, then marks the AC complete.

The JTBD benchmark requires "a UX practitioner rates as actionable" -- but no UX practitioner review is defined as an AC. Who is the practitioner? How are they identified? What does "actionable" mean operationally? The structured rubric (grammatically correct, functional+emotional+social, distinguishes job from solution) is listed as criteria but the scoring mechanism for "rates as actionable" is undefined. An implementer can self-certify by generating a job statement that satisfies the three stated structural criteria and calling themselves the UX practitioner.

The Wave 3 Storybook benchmark (correctly classifies >= 80% of components) is only testable against the "reference Storybook" the implementer creates. If the reference Storybook is simple (e.g., 5 obvious Atoms, 3 obvious Molecules), 80% accuracy is trivial. If it includes edge cases, the threshold is meaningful. The deliverable provides no specification for reference artifact difficulty level or composition.

**Analysis:**

This is a fundamental completeness gap in the quality enforcement architecture. R1 added numeric thresholds (DA-001, IN-001 fixes), which addressed the absence of measurement criteria. However, adding a threshold without specifying the measurement instrument and the artifact against which measurement occurs creates an illusion of verifiability. The calibration artifact definition IS the quality gate -- without it, the numeric threshold is meaningless. A motivated adversary exploits this by treating all calibration artifact creation as implementation work where they are the sole arbiter.

**Recommendation:**

1. For each benchmark AC, explicitly specify: (a) who creates the reference artifact -- must be separate from the implementer; (b) minimum difficulty profile -- e.g., "heuristic-eval reference design must contain >= 3 H1, >= 2 H4, >= 2 H7 violations with no false positives"; (c) artifact must be committed to the repository before benchmark testing begins so it cannot be modified retroactively.
2. Replace "a UX practitioner rates as actionable" with "rated >= 3 of 4 criteria on the structured rubric by two independent reviewers (both non-implementer)."
3. For Wave 2-5, add: "reference artifacts for each benchmark are committed in a dedicated `calibration/` directory alongside the sub-skill before implementation begins."

**Acceptance Criteria for Resolution:** Each benchmark AC references a committed calibration artifact path; artifacts are created before implementation work begins; independent reviewer requirement is named.

---

### RT-002-iter2: Wave Progression Entry Criteria Are Declarative and Unenforceable [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions -- Wave Deployment (Section 5) |
| **Strategy Step** | Step 2: Rule Circumvention + Step 3: Defense Gap Assessment |
| **Attack Category** | Rule circumvention |
| **Exploitability** | High |
| **Priority** | P1 |
| **Existing Defense** | Partial (wave entry criteria are listed; bypass documentation required) |

**Evidence:**

Wave 2 entry criteria:
> "Completed at least 1 heuristic evaluation report AND 1 JTBD job statement that was used in a product decision"

Wave 3 entry criteria:
> "Launched product with an analytics data source (for HEART) OR completed 1 Lean UX build-measure-learn hypothesis cycle"

Wave 4 entry criteria:
> "Storybook instance with 5+ classified Atom-level stories AND completed 1 Persona Spectrum accessibility review"

Wave bypass condition:
> "If a wave stalls for 2+ sprint cycles (approximately 4-6 weeks), documented bypass conditions allow teams to proceed with partial capability: the team documents which entry criteria remain unmet..."

**Attack Vector:**

Entry criteria for Waves 2-5 require real-world artifacts (JTBD job statement "used in a product decision", "launched product", Kano survey with "30+ active users") but are verified via self-attestation. There is no mechanism for the `ux-orchestrator` to verify whether a JTBD job statement was actually "used in a product decision" -- this requires the team to tell the orchestrator it was. An adversary invokes Wave 2 by asserting Wave 1 criteria are met without having completed them.

The bypass mechanism makes this structurally worse: any team that "stalls" for "2+ sprint cycles (approximately 4-6 weeks)" can activate bypass by documenting which criteria remain unmet. But the bypass itself requires only documentation -- not the underlying artifact. Combined with vague timing ("approximately 4-6 weeks"), a motivated team invokes bypass at Week 1 by claiming subjective stall.

The `ux-orchestrator` is defined as reading routing rules from `ux-routing-rules.md`, but the wave enforcement mechanism (how the orchestrator verifies entry criteria) is undefined in the deliverable. The AC states only: "Wave 1 entry criteria documented and enforced (KICKOFF-SIGNOFF.md completion)" -- for Wave 1, the KICKOFF-SIGNOFF.md is a concrete artifact. For Waves 2-5, no equivalent artifact is defined.

**Analysis:**

Wave progression is the deliverable's primary deployment safety mechanism -- it prevents teams from using advanced frameworks before they have built the prerequisite product maturity. Declarative-only enforcement degrades this mechanism to a suggestion. R1's PM-005 fix added bypass documentation requirements but did not add enforcement teeth to the primary entry path.

**Recommendation:**

1. For Waves 2-5, define a concrete gate artifact parallel to KICKOFF-SIGNOFF.md -- e.g., a "WAVE-N-SIGNOFF.md" that the orchestrator requires before unlocking Wave N sub-skills. Each WAVE-N-SIGNOFF.md lists the required artifacts by file path (e.g., "Path to heuristic evaluation report: ___; Path to JTBD job statement: ___; Product decision record referencing this job statement: ___").
2. The bypass mechanism should require the WAVE-N-SIGNOFF.md to be completed with "N/A -- bypassed" and a rationale field, not just "documentation."
3. Add an AC: "Wave 2-5 entry is gated by WAVE-N-SIGNOFF.md completion, checked by ux-orchestrator before routing to Wave N sub-skills."

**Acceptance Criteria for Resolution:** WAVE-N-SIGNOFF.md templates defined for Waves 2-5; ux-orchestrator checks SIGNOFF.md existence before routing to Wave N sub-skills.

---

### RT-003-iter2: P-003 Compliance Verification Is Declarative -- No Runtime or CI Enforcement [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Acceptance Criteria -- Quality Standards |
| **Strategy Step** | Step 2: Rule Circumvention + Boundary Violations |
| **Attack Category** | Rule circumvention |
| **Exploitability** | Medium |
| **Priority** | P1 |
| **Existing Defense** | Partial (AC requires explicit YAML frontmatter exclusion) |

**Evidence:**

The Quality Standards AC states:
> "No sub-skill agent has Task tool access (P-003 enforcement)"
> "Each sub-skill agent definition's `.md` YAML frontmatter explicitly excludes `Task` from `tools` (or uses `disallowedTools: ['Task']`), AND each `.governance.yaml` includes `Task` in `capabilities.forbidden_actions` with P-003 consequence statement"

The R1 fix annotation reads: `[R1-fix: RT-001] Added explicit P-003 worker Task exclusion verification AC per H-34/H-35`

**Attack Vector:**

The AC requires that P-003 exclusion be declared in two places (YAML frontmatter AND governance YAML), but declaration is not enforcement. An implementer creates 10 sub-skill agents across Waves 1-5. Each agent definition has a `tools:` section in YAML frontmatter. Three scenarios allow P-003 violation to slip through:

Scenario A: Frontmatter uses `tools:` omission pattern (most common in Jerry codebase). When `tools:` is omitted from an agent's YAML frontmatter, the agent inherits ALL tools including Task (per agent-development-standards.md: "Inherits ALL if omitted"). An implementer creating 10 agent definitions under time pressure is likely to omit `tools:` rather than explicitly enumerate it -- this is the path of least resistance and it is a P-003 violation by omission, not commission.

Scenario B: The `disallowedTools: ["Task"]` path in the AC is listed as an alternative to explicit `tools:` enumeration. `disallowedTools` requires the implementer to know Task is the specific tool to block. If Task is ever renamed or if a different delegation tool is introduced, `disallowedTools: ["Task"]` becomes stale and the block disappears.

Scenario C: The governance YAML `forbidden_actions` entry is text-based and not machine-verified. An implementer adds "Do not use Task tool" to `forbidden_actions` without the structured consequence format required by H-34/AD-M-009, and the CI schema validation passes because the schema requires 3 entries of any format.

The deliverable provides no AC requiring a CI gate that explicitly checks sub-skill agent YAML frontmatter for Task exclusion across all 10 agent definitions.

**Analysis:**

H-34 and H-35's enforcement relies on CI schema validation (L5). But the CI check validates schema structure, not semantic content -- it verifies that `tools:` exists and matches recognized values, not that Task is absent when it should be. The L5 gate referenced in `agent-development-standards.md` is a "Grep for P-003/P-020/P-022 presence" -- it greps for the string, not for the absence of Task in the tools field.

**Recommendation:**

1. Add AC: "A CI check (script or GitHub Action step) verifies that no sub-skill agent `.md` file's YAML frontmatter includes `Task` in `tools` and that each explicitly enumerates `tools:` rather than omitting it." This converts P-003 from a declared constraint to an enforced one.
2. Explicitly prohibit the `disallowedTools:` path for P-003 compliance in sub-skill agents -- require explicit `tools:` enumeration so the positive list is auditable.
3. Add to the deliverable's Quality Standards AC: "The KICKOFF-SIGNOFF.md for the skill includes a P-003 verification checklist step confirming tools enumeration for all sub-skill agents."

**Acceptance Criteria for Resolution:** CI step defined that asserts no sub-skill agent YAML frontmatter grants Task access; `tools:` enumeration required (not omission) for all sub-skill agents.

---

### RT-004-iter2: Synthesis Hypothesis Confidence Gate Override Creates Auditable-But-Unverifiable Bypass [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions -- Synthesis Hypothesis Validation |
| **Strategy Step** | Step 2: Ambiguity Exploitation + Degradation |
| **Attack Category** | Degradation path |
| **Exploitability** | High |
| **Priority** | P1 |
| **Existing Defense** | Partial (Human Override Justification field exists; paper trail created) |

**Evidence:**

The deliverable states:
> "Each synthesis output therefore includes a `Human Override Justification` field -- if a user chooses to act on a LOW-confidence output, they must document their rationale and the evidence supporting their decision. This creates an auditable paper trail rather than a hard block."

The LOW confidence gate behavior states:
> "Output permanently labeled reference-only; design recommendation section structurally omitted... Users requesting design recommendations from LOW-confidence outputs receive a warning explaining why the section is absent and are directed to gather validation data to upgrade confidence level"

**Attack Vector:**

The design creates a structural omission (no recommendation section at LOW confidence) combined with an override field. But the override field itself is a free-text justification -- any text satisfies the field requirement. An adversary populates the field with "We have sufficient internal knowledge of our user population" or "Our product manager has 5 years of domain expertise" -- neither of which provides actual user validation data. The paper trail exists but the audit has no arbiter.

More critically: the override field is embedded in the output template. A user who wants to bypass LOW-confidence restrictions can simply edit the output file after generation and add a recommendation section manually -- the structural omission only prevents the agent from generating it, not the user from adding it. Nothing in the deliverable addresses this post-generation modification path.

The MEDIUM confidence gate has the same issue: "requires expert review OR validation against 2-3 real user data points." "Expert review" is undefined -- who qualifies? The user themselves? Their co-founder? The gate is a social contract, not a technical constraint.

**Analysis:**

R1's DA-002 and PM-002 fixes replaced "cannot be overridden" language with "P-020-compliant user guidance." This was correct -- hard blocks violate user authority (P-020). However, the residual attack surface is that the override mechanism creates a documented circumvention pathway. The paper trail creates the appearance of governance without the substance. A team building a consumer product with 500K users makes a major feature decision on a LOW-confidence behavioral diagnosis because the override field is "just one more field to fill in."

**Recommendation:**

1. Add a usage warning to the MEDIUM and LOW confidence gate description: "The Human Override Justification field creates an audit record, not a quality gate. Teams invoking LOW-confidence outputs for design decisions assume full responsibility for resulting product risk. The orchestrator logs each override invocation with timestamp and session ID."
2. Define "expert review" for MEDIUM confidence: must be a named external reviewer (not a member of the product team) OR must reference >= 2 user data points with named sources.
3. Add to the synthesis-validation.md AC: "Override invocations are logged to a session audit file (`skills/user-experience/logs/override-audit.md`) with override type (LOW/MEDIUM), justification text, and session timestamp. The orchestrator reads this log at session start to surface override history to the user."

**Acceptance Criteria for Resolution:** Override audit logging implemented; "expert review" defined with named qualifier for MEDIUM confidence gate.

---

### RT-005-iter2: AI-First Design Enabler WSM Gate Is Self-Referentially Circular [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Key Design Decisions (AI-First Design conditional), Known Limitations (AI-First Design conditional status) |
| **Strategy Step** | Step 2: Ambiguity Exploitation + Rule Circumvention |
| **Attack Category** | Ambiguity exploitation + rule circumvention |
| **Exploitability** | High |
| **Priority** | P0 |
| **Existing Defense** | Partial (90-day expiry added per R1 RT-005 fix) |

**Evidence:**

The deliverable states the blocking prerequisite:
> "A synthesis Enabler must reach DONE status with a verified WSM score >= 7.80"

And the framework's projected score:
> "AI-First Design (SYNTHESIZED) | /ux-ai-first-design | 7.80 (P) | 5 (COND)"

The Known Limitations section states:
> "Blocking prerequisite: A synthesis Enabler must reach DONE status with a verified WSM score >= 7.80"

**Attack Vector:**

The Enabler's purpose is to create an AI-First Design framework and demonstrate it meets selection quality standards. The quality standard (>= 7.80 WSM) is set to exactly the same value as the framework's own projected score from the selection analysis. This is a tautological gate: the selection analysis projected 7.80 as the score, the Enabler must achieve >= 7.80, so the Enabler passes by achieving exactly what it was projected to achieve. A motivated implementer creating the Enabler calibrates their WSM scoring to reach exactly 7.80, knowing that is both the target and the baseline expectation.

Additionally, "verified WSM score" is not defined: who verifies it? What is the WSM methodology for evaluating an AI-First Design framework (a meta-evaluation, applying the selection WSM to the framework being created for inclusion in the selection)? The 6-criterion WSM with specific weights is documented for evaluating external frameworks -- but the Enabler is creating a novel framework that does not exist yet and will be evaluated by the same team creating it against criteria they defined.

The 90-day expiry (R1 RT-005 fix) addresses the temporal risk (Enabler stalls indefinitely) but does not address the circular verification logic. An Enabler that reaches DONE with self-assessed WSM 7.80 still passes the gate.

**Analysis:**

The AI-First Design sub-skill is the only framework in the portfolio that must be synthesized before implementation -- all others adopt established external frameworks. The Enabler gate is the mechanism that prevents a low-quality synthesized framework from entering the portfolio. But the gate as defined is trivially passable by an implementer who controls the Enabler's completion criteria and the WSM scoring.

The deeper adversarial risk: if the AI-First Design sub-skill is implemented with a poorly synthesized framework (low confidence interaction patterns, insufficient empirical basis) and enters the portfolio as Wave 5 CONDITIONAL, it will generate LOW-confidence outputs labeled as coming from a "verified" framework. The confidence gate architecture partially mitigates this (LOW confidence gates fire for AI-First Design outputs), but teams who activate Wave 5 may have elevated expectations from the "verified WSM" label.

**Recommendation:**

1. The Enabler gate must require an independent quality reviewer (not the implementer) to validate the WSM score. Add to the AI-First Design Enabler AC: "WSM scoring reviewed and confirmed by a reviewer outside the implementing team; reviewer sign-off is a blocking prerequisite for DONE status."
2. Raise the WSM threshold above the projected score: if the projected score is 7.80, the Enabler gate should be >= 8.00 to require the synthesized framework to demonstrably exceed the projection. This makes the gate non-trivially passable.
3. Define the WSM verification methodology for novel framework synthesis: which of the 6 WSM criteria are applicable to evaluating the synthesized framework (vs. evaluating external established frameworks), and what evidence satisfies each criterion for a novel framework.

**Acceptance Criteria for Resolution:** Enabler WSM gate threshold raised above projected score (>= 8.00 minimum); independent reviewer sign-off required for DONE status; WSM criteria applicability defined for novel framework synthesis.

---

### RT-006-iter2: Hotjar Bridge Misclassified as Enhancement MCP -- Behavioral Diagnosis Degrades to Reference-Only Without It [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | MCP Integration (Section 4), Known Limitations |
| **Strategy Step** | Step 2: Dependency Attacks + Boundary Violations |
| **Attack Category** | Dependency attack |
| **Exploitability** | Medium |
| **Priority** | P1 |
| **Existing Defense** | Partial (fallback paths documented; Hotjar classified as "MEDIUM stability") |

**Evidence:**

MCP classification table:
> "Hotjar | Bridge (Zapier/Pipedream) | MEDIUM -- requires paid middleware | Variable ($0-$99+ depending on Zapier plan) | NOT plug-and-play; requires custom workflow config"

The MCP integration graph shows Hotjar as Enhancement MCP (dashed arrows) for `/ux-heart-metrics`, `/ux-lean-ux`, and `/ux-behavior-design`.

The AC states:
> "Enhancement MCP unavailability produces a cosmetic limitation warning, not a hard failure"

But for `/ux-behavior-design`, the What AI Does section states:
> "Diagnoses which component of B=MAP is the bottleneck (motivation too low? ability too hard? prompt missing or mistimed?)"

And `/ux-behavior-design` LOW-confidence warning states:
> "Design intervention recommendations are LOW confidence. They are reference-only outputs without design recommendation sections."

**Attack Vector:**

The B=MAP diagnosis depends on behavioral recording data to diagnose whether motivation, ability, or prompt is the bottleneck. Without Hotjar (or equivalent behavioral session data), the agent cannot observe real user behavior -- it can only reason from user-provided descriptions. The deliverable labels Hotjar as "Enhancement MCP" implying cosmetic-only impact. But behavioral session recordings are the primary evidence base for B=MAP diagnosis: without them, the bottleneck diagnosis is inferred from qualitative input rather than observed behavior, which is precisely the gap the LOW-confidence warning already flags.

The consequence of Hotjar unavailability in `/ux-behavior-design` is not cosmetic -- it degrades the bottleneck diagnosis from "data-driven inference from session recordings" to "pure synthesis hypothesis from user description." This is the same qualitative difference that the confidence gate architecture addresses: the output should either receive a different confidence tier label or be explicitly flagged as "degraded mode: behavioral data absent."

Similarly, `/ux-lean-ux`'s experiment validation depends on Hotjar for "experiment analytics via bridge" -- without it, hypothesis validation tracks intent (what teams planned to measure) rather than behavior (what users actually did).

**Analysis:**

The MCP classification schema (Required vs. Enhancement) creates a binary that does not capture the actual degradation spectrum. Hotjar sits in a middle category: not required for the skill to produce output, but required for the output's quality tier to be accurately labeled. The cosmetic limitation classification misleads implementers and users about the actual impact of Hotjar unavailability on behavioral sub-skills.

**Recommendation:**

1. Add a third MCP classification tier: "Behavioral-Data Enhancement" -- MCP tools that, when absent, change the confidence tier of outputs (not just cosmetic display). Hotjar falls in this tier for `/ux-behavior-design` and `/ux-lean-ux`.
2. Add an AC: "When Hotjar is unavailable for `/ux-behavior-design`, the B=MAP diagnosis output is automatically downgraded to MEDIUM confidence (from the current degraded-HIGH/MEDIUM state) with an explicit 'Behavioral Data Absent' warning added to the output header."
3. Update the `/ux-behavior-design` degraded-mode documentation to specify: "Without Hotjar, output is hypothesis-from-description, not observation-from-data. Confidence tier adjusts to LOW for bottleneck diagnosis."

**Acceptance Criteria for Resolution:** Hotjar unavailability in `/ux-behavior-design` triggers explicit confidence tier downgrade; AC added requiring confidence tier adjustment in degraded mode.

---

### RT-007-iter2: 20% UX Capacity Threshold Is Self-Reported With No Measurement Guidance [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Key Design Decisions -- Parent Orchestrator Routing (Section 2) |
| **Strategy Step** | Step 2: Ambiguity Exploitation |
| **Attack Category** | Ambiguity exploitation |
| **Exploitability** | High |
| **Priority** | P1 |
| **Existing Defense** | Missing |

**Evidence:**

The routing logic states:
> "Checks team UX capacity -- if < 20% of one person's time, restricts recommendations to Wave 1 sub-skills"

The capacity check is listed in the parent orchestrator AC:
> "Capacity check restricts to Wave 1 when UX time < 20% of one person's time"

The "Part-time UX" segment in The Problem section:
> "UX is a part-time responsibility; depth is limited; frameworks must be low-ceremony | MEDIUM -- Kano and HEART may exceed part-time capacity; prioritize Wave 1-2 only"

**Attack Vector:**

"20% of one person's time" is self-reported by the team invoking the skill. The orchestrator asks (presumably in the onboarding flow) about UX capacity, the team answers. A team that wants access to Wave 2+ frameworks tells the orchestrator they allocate 25% of UX time and proceeds. No definition of what counts as "UX time" (design tool usage? user testing hours? framework application time?), no measurement methodology, no verification mechanism.

The adversary's motivation here is not the implementer but the end user: a part-time UX practitioner who self-reports 20%+ to unlock Wave 2 sub-skills (Lean UX, HEART) before they have the capacity to effectively use them. The resulting outputs will be of lower quality (hypotheses generated without capacity to validate, metrics tracked without capacity to act on) and the confidence gate architecture does not catch this because it addresses AI synthesis quality, not human execution capacity.

Additionally, the threshold itself (20%) is not derived from any stated framework or research -- it is an arbitrary round number. The "Part-time UX" population segment recommendation ("prioritize Wave 1-2 only") contradicts the capacity threshold (Wave 1 only restriction at < 20%) without resolving the gap between Wave 1 and Wave 2 at the boundary.

**Analysis:**

This is a user experience design failure in the orchestrator itself: the capacity gate is the primary mechanism for protecting low-capacity teams from being routed to frameworks they cannot effectively execute. But the gate relies entirely on self-report with no guidance on how to estimate UX time allocation, no consequence for incorrect self-report, and no feedback loop that would surface overcapacity routing (e.g., teams abandoning Wave 2+ sub-skills mid-process).

**Recommendation:**

1. Define "UX capacity" operationally: "Hours per week available for structured UX methodology application (interviews, analysis, template completion, design review). Exclude ad hoc design tool usage." Provide a 5-question capacity estimation prompts in the onboarding flow.
2. Add escalating warnings rather than a hard threshold: at < 10% capacity, restrict to Wave 1 only; at 10-20%, Wave 1-2 with explicit "MEDIUM capacity" warning for each Wave 2 invocation; at > 20%, all waves accessible with onboarding confirmation.
3. Add a capacity re-assessment trigger: if a team completes fewer than 1 sub-skill output per sprint cycle for 2+ cycles, the orchestrator prompts a capacity re-assessment.

**Acceptance Criteria for Resolution:** "UX time" operationally defined with estimation guidance; escalating capacity warning tiers (not binary threshold) documented in ux-routing-rules.md.

---

### RT-008-iter2: WSM Criteria Weight Arithmetic Not Independently Verifiable From Deliverable [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Research Backing -- Framework Selection Scores |
| **Strategy Step** | Step 2: Dependency Attacks (external trust chain) |
| **Attack Category** | Dependency attack |
| **Exploitability** | Low |
| **Priority** | P2 |
| **Existing Defense** | Partial (WSM criteria and weights listed per R1 SM-008 fix; individual scores referenced as in separate artifact) |

**Evidence:**

The Research Backing section states:
> "Arithmetic verification: All 40 framework totals independently verified; 5 error correction rounds"

WSM criteria table lists weights (C1=0.25, C2=0.22, C3=0.18, C4=0.15, C5=0.12, C6=0.08):
> "Graduated-priority weighting assigns higher weights to criteria most aligned with the skill's core value proposition. See the full selection analysis artifact for per-framework scoring breakdowns."

**Attack Vector:**

The weights sum to 1.00 (0.25+0.22+0.18+0.15+0.12+0.08 = 1.00 -- verifiable). But the per-framework raw scores are in a separate artifact (`projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md`), not in the issue body. The issue body presents only final WSM scores (e.g., Nielsen's = 9.25, Design Sprint = 8.65) without intermediate scoring data. A skeptic reading the issue cannot verify whether the scores are accurate from within the issue itself.

The adversarial scenario: an implementer who wants to promote a lower-ranked framework to Wave 1 (for implementation convenience) can adjust raw scores in the selection analysis artifact after the issue is approved. The issue body shows final scores as authoritative but does not commit to them -- they reference the artifact which is mutable.

**Analysis:**

This is a Minor finding because the separate artifact exists and is referenced. The R1 SM-008 fix added WSM criteria names and weights inline, which substantially improves reproducibility. The residual risk is the mutable external artifact without a checksum or commit-hash reference in the issue. For a GitHub Enhancement issue, this is acceptable practice -- the separate artifact is committed to the repository and is version-controlled.

**Recommendation:**

1. Add a checksum or commit reference to the framework selection analysis artifact in the References section: "Framework Selection Analysis | `projects/.../ux-framework-selection.md` | Git commit: {hash at time of issue creation}"
2. Or, add a condensed reproducibility table to the issue body showing top-10 raw scores per criterion (as a sanity check, not a full audit trail).

**Acceptance Criteria for Resolution:** Framework selection analysis referenced with version-lock mechanism (git hash or explicit "frozen at version N" label).

---

## Recommendations

### P0 (Critical -- MUST Mitigate Before Acceptance)

**RT-001-iter2: Quality Benchmark Calibration Artifact Independence**

Action: For each of the 10 sub-skills, define the calibration artifact's composition and difficulty profile before implementation begins. Specify that calibration artifacts are created by someone other than the implementer. Add to Wave 1 AC: "calibration artifacts committed to `skills/{sub-skill}/calibration/` directory before implementation work begins; artifact creator documented."

Acceptance Criteria: Each wave's benchmark AC names a calibration artifact path; artifacts are committed and version-controlled before benchmark testing; independent reviewer requirement is explicit.

**RT-005-iter2: AI-First Design Enabler WSM Gate Independence**

Action: Raise Enabler gate threshold to >= 8.00 (above projected 7.80). Require independent reviewer sign-off on WSM scoring (not implementer self-assessment). Define WSM criteria applicability for novel framework synthesis (which of 6 criteria apply; what constitutes evidence for each in a synthesized framework context).

Acceptance Criteria: Enabler AC updated with >= 8.00 threshold; independent reviewer role named; WSM methodology for novel framework documented in a separate Enabler requirements artifact.

---

### P1 (Important -- SHOULD Mitigate)

**RT-002-iter2: Wave Progression Enforcement Mechanism**

Action: Define WAVE-N-SIGNOFF.md templates for Waves 2-5, parallel to KICKOFF-SIGNOFF.md for Wave 1. Each signoff template lists required artifact paths. ux-orchestrator checks SIGNOFF.md existence before routing.

**RT-003-iter2: P-003 CI Enforcement**

Action: Add CI check asserting no sub-skill agent YAML frontmatter omits `tools:` or includes Task. Require explicit `tools:` enumeration (not omission) for all sub-skill agent definitions.

**RT-004-iter2: Confidence Gate Override Audit Logging**

Action: Implement override audit logging to a session file. Define "expert review" for MEDIUM confidence with named qualifier.

**RT-006-iter2: Hotjar Classification Correction**

Action: Introduce "Behavioral-Data Enhancement" MCP tier for Hotjar. Add AC requiring confidence tier downgrade when Hotjar absent in `/ux-behavior-design`.

**RT-007-iter2: UX Capacity Threshold Operationalization**

Action: Define "UX time" operationally. Replace binary 20% threshold with escalating warning tiers. Add capacity re-assessment trigger to orchestrator.

---

### P2 (Monitor -- MAY Mitigate)

**RT-008-iter2: WSM Artifact Version-Lock**

Action: Add git hash or version reference to framework selection analysis artifact in References section.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Negative | RT-001 (calibration artifacts missing), RT-002 (no WAVE-N-SIGNOFF.md mechanism), RT-006 (Hotjar misclassification creates gap in behavioral confidence tier system) -- three distinct completeness gaps in the quality architecture |
| Internal Consistency | 0.20 | Negative | RT-005 (Enabler gate equal to projected score -- internal inconsistency between the gate's purpose and its calibration), RT-006 (Enhancement MCP label inconsistent with actual behavioral impact), RT-007 (20% threshold and "Part-time UX: Wave 1-2 only" recommendation are contradictory) |
| Methodological Rigor | 0.20 | Negative | RT-003 (P-003 enforcement is declarative, not verified -- weakens constitutional compliance methodology), RT-001 (quality benchmarks without independent calibration artifacts violate measurement rigor) |
| Evidence Quality | 0.15 | Negative | RT-007 (20% capacity threshold is arbitrary, unresearched), RT-008 (WSM reproducibility incomplete without artifact version-lock) |
| Actionability | 0.15 | Neutral | Most countermeasures are concrete and implementable. The deliverable's overall implementation pathway is clear; the RT findings address quality gates, not core architecture. |
| Traceability | 0.10 | Negative | RT-005 (Enabler verification methodology undefined -- cannot trace from Enabler DONE status to WSM score confidence), RT-001 (calibration artifact paths not defined -- cannot trace benchmark results to their evidence base) |

---

## Execution Statistics

- **Total Findings:** 8
- **Critical:** 2 (RT-001, RT-005)
- **Major:** 5 (RT-002, RT-003, RT-004, RT-006, RT-007)
- **Minor:** 1 (RT-008)
- **Protocol Steps Completed:** 5 of 5
- **Attack Vector Categories Covered:** All 5 (Ambiguity: RT-001, RT-005, RT-007; Boundary: RT-003, RT-006; Circumvention: RT-002, RT-003, RT-004, RT-005; Dependency: RT-006, RT-008; Degradation: RT-004, RT-006)
- **H-16 Compliance:** Confirmed -- S-003 Steelman applied prior to this execution (SM-001 through SM-009 annotations visible in deliverable)
