## Acceptance Criteria (continued from issue body)

## Acceptance Criteria


**Issue Closure Condition:** This issue is CLOSED when all Wave 1 (Minimum Viable Launch) acceptance criteria are satisfied -- that means the Parent Orchestrator section and the Wave 1 Sub-Skills section below. Wave 2-5 criteria are tracked in child issues and are NOT required for closure of this issue. You do not need to ski the whole mountain to call it a good day -- you need to ski the first line clean.

### Parent Orchestrator

- [ ] `/user-experience` skill registered in `mandatory-skill-usage.md` with trigger map entry: positive keywords (`UX, user experience, usability, heuristic evaluation, design sprint, lean ux, heart metrics, atomic design, inclusive design, behavior design, kano model, jobs to be done, jtbd, user interface, accessibility audit, design system`), priority 12 (next available after current max priority 11 shared by `/prompt-engineering` and `/diataxis`), negative keywords preventing collision with `/adversary`, `/red-team`, `/nasa-se`, `/transcript`, `/problem-solving`
- [ ] `/user-experience` skill registered in `CLAUDE.md` skill table and `AGENTS.md` agent registry
- [ ] `ux-orchestrator` agent definition created with T5 tool tier, primary cognitive mode: systematic (wave-gated routing logic with sequential prerequisite checks, PASS/WARN/BLOCK enforcement, and checklist execution), secondary function: integrative (synthesis across sub-skill outputs into unified insight reports when 2+ sub-skills produce findings on the same product), Opus model, L0/L1/L2 output levels declared in `.governance.yaml` `output.levels` per AD-M-004
- [ ] `ux-orchestrator.governance.yaml` validates against `docs/schemas/agent-governance-v1.schema.json`
- [ ] Lifecycle-stage triage routing implemented in `skills/user-experience/rules/ux-routing-rules.md`
- [ ] Onboarding warning (HIGH RISK user research gap) displays on first invocation per session
- [ ] Capacity check gates routing to Wave 1 when UX time < 20% of one person's time (P-020 compliant: user authority -- system recommends Wave 1 only but never hard-blocks user decisions to access higher waves)
- [ ] Crisis mode 3-skill sequence (Heuristic Eval -> Behavior Design -> HEART) operational
- [ ] Orchestrator Failure Modes documented and tested: (a) MCP connection failure -- graceful degradation to non-MCP workflow, log warning, continue with reduced capability; (b) BLOCK state encountered -- present user with signoff requirements, offer to generate signoff template, halt sub-skill routing until resolved; (c) Cross-framework partial failure -- complete available sub-skill analysis, mark failed sub-skill as 'incomplete' in synthesis, present partial results with explicit gap disclosure
- [ ] Cross-framework integration handoffs tested for at least 2 canonical sequences (JTBD -> Design Sprint, Lean UX -> HEART) -- tested = validated by running both sub-skills on the same product context and confirming the synthesis report correctly identifies convergent and divergent recommendations
- [ ] Cross-framework synthesis AC: The `/user-experience` parent skill produces a unified insight report combining findings from 2+ sub-skill analyses on the same product, identifying convergent and divergent recommendations across frameworks
- [ ] Parent-to-sub-skill handoff includes: product context (name, domain, target users), selected sub-skill, prior sub-skill outputs (if any), and quality gate threshold
- [ ] Sub-skill-to-sub-skill handoff contract: When the orchestrator chains sub-skills (e.g., Nielsen heuristic evaluation then HEART metrics), the handoff includes: originating sub-skill ID, key findings (3-5 bullets), artifact file paths, downstream_input_field_mapping (specifying which output fields from the upstream sub-skill map to which input fields for the downstream sub-skill -- e.g., JTBD job statement output maps to Design Sprint challenge statement input), and recommended next-step framing for the receiving sub-skill. Cross-sub-skill handoff schema documented in `ux-routing-rules.md`.

### Wave 1 Sub-Skills (Minimum Viable Launch)

- [ ] `/ux-heuristic-eval` sub-skill created with:
  - Systematic cognitive mode, T3 tool tier
  - Figma required MCP, Storybook enhancement MCP
  - `ux-heuristic-evaluator` agent with all 10 Nielsen heuristics enumerated in methodology
  - Structured findings report template with severity ratings (0-4 scale)
  - Non-MCP fallback: screenshot-input mode documented
  - Quality benchmark: agent correctly identifies >= 7 of 10 known heuristic violations in a reference test design (calibration artifact provided with sub-skill)
  - [ ] Heuristic Evaluation Haiku/Figma pre-launch benchmark: >= 90% reliability on Figma MCP OAuth + frame extraction across 3 reference design files (escalate to Sonnet with revised cost estimate if fail)
- [ ] `/ux-jtbd` sub-skill created with:
  - Divergent cognitive mode, T3 tool tier
  - No required MCP; Miro enhancement MCP
  - `ux-jtbd-analyst` agent with job statement synthesis methodology
  - Switch interview guide template
  - Competitive job analysis output format
  - Non-MCP fallback: text-based analysis mode documented
  - Quality benchmark: agent produces job statements that pass a 3-criterion deterministic rubric: (a) follows canonical "When [situation], I want to [motivation], so I can [outcome]" format; (b) contains at least 1 functional AND 1 emotional or social dimension; (c) references an outcome, not a product feature or technology. 3/3 criteria = actionable. No UX practitioner consultation required.
- [ ] Both sub-skills produce outputs that conform to the synthesis hypothesis validation protocol
- [ ] Both sub-skills have per-sub-skill SKILL.md, agent definition, governance YAML, rules, and templates

### Wave 2-5 Sub-Skills (Incremental Deployment)

- [ ] Each subsequent wave's sub-skills meet the same structural requirements as Wave 1, including a per-sub-skill quality benchmark AC (Tracked in child issue)
- [ ] Wave 2: `/ux-lean-ux` assumption map and hypothesis backlog templates operational (benchmark: generates assumption map with >= 3 risk categories from a product brief); `/ux-heart-metrics` GSM template operational (benchmark: populates all 5 HEART dimensions with measurable signals from a product description) (Tracked in child issue)
- [ ] Wave 3: `/ux-atomic-design` Storybook integration tested (benchmark: correctly classifies >= 80% of components in a reference Storybook into Atom/Molecule/Organism hierarchy); `/ux-inclusive-design` WCAG 2.2 checklist complete (benchmark: identifies >= 5 of 7 planted accessibility violations in a reference design) (Tracked in child issue)
- [ ] Wave 4: `/ux-behavior-design` B=MAP diagnosis template operational (benchmark: diagnosis accuracy -- correctly identifies the bottleneck component for >= 3 of 4 reference behavioral scenarios with documented reasoning chain); `/ux-kano-model` survey processing functional (benchmark: classification accuracy -- correct Kano classification for >= 90% of feature pairs in a reference survey dataset) (Tracked in child issue)
- [ ] Wave 5: `/ux-design-sprint` 4-day process templates (per-day) (benchmark: produces a testable prototype spec from a reference challenge statement); `/ux-ai-first-design` conditional Enabler tracked (benchmark: deferred until Enabler DONE -- defined in Enabler acceptance criteria) (Tracked in child issue)

### Synthesis Hypothesis Validation

- [ ] 3-tier confidence gate protocol (HIGH / MEDIUM / LOW) implemented in `skills/user-experience/rules/synthesis-validation.md`
- [ ] LOW-confidence outputs structurally omit design recommendation sections
- [ ] MEDIUM-confidence outputs require named validation source before advancing
- [ ] HIGH-confidence outputs require enumerated acknowledgment of AI judgment calls

### MCP Integration Quality


- [ ] Parent orchestrator performs MCP connectivity pre-check before routing to MCP-dependent sub-skills; on failure, routes to non-MCP fallback path with user notification
- [ ] Each MCP-dependent sub-skill documents degraded-mode behavior when its Required MCP is unavailable (screenshot-input, text-based analysis, or Miro-only mode)
- [ ] Enhancement MCP unavailability produces a cosmetic limitation warning, not a hard failure
- [ ] Hotjar bridge integration includes explicit setup verification step (not plug-and-play; requires Zapier/Pipedream configuration)
- [ ] MCP Integration Runbook: Each MCP-dependent sub-skill includes an operational runbook (`skills/{sub-skill}/rules/mcp-runbook.md`) with: connection setup steps, authentication method and credential management, fallback behavior when MCP server is unavailable, and rate limit handling with backoff strategy
- [ ] Parent Orchestrator MCP Coordination: The `ux-orchestrator` agent maintains a unified MCP connection registry tracking active/inactive status for each sub-skill's MCP dependencies. On sub-skill invocation, the orchestrator pre-checks MCP availability and routes to fallback behavior (graceful degradation to non-MCP workflow) if unavailable
- [ ] Named MCP maintenance owner documented in `mcp-coordination.md` with owner name, coverage scope, and escalation contact

### Pre-Launch Validation

- [ ] Before Wave 1 sub-skill merge, each sub-skill's quality benchmark is validated against an external ground-truth artifact (not self-created by the implementing team). Benchmark achievement is demonstrated via test output comparison, not merely defined. For `/ux-heuristic-eval`: published heuristic evaluation case study with known findings (e.g., Nielsen Norman Group published evaluations). For `/ux-jtbd`: published JTBD case study with known job statements (e.g., Intercom JTBD Playbook examples). Comparison uses a blind evaluation rubric: 3 independent evaluators score both the AI-augmented output and a manually-produced reference output on completeness and actionability without knowing which is AI-augmented. Evaluators must be Jerry Framework users who (a) did not author or contribute to the sub-skill under review, (b) have completed at least one prior sub-skill evaluation, and (c) are drawn from the Jerry community contributor pool. For Wave 1 adoption by a community with no prior sub-skill evaluations, qualification criterion (b) is satisfied by: (i) peer-reviewed UX evaluation experience in any context (publication, course, or professional practice), OR (ii) completion of the built-in UX skill tutorial walkthrough with self-assessment. For teams < 3 people, external Jerry community members fulfill the evaluator requirement. For Wave 5 solo practitioners who cannot source 3 independent evaluators, a solo bypass path is available: the practitioner runs the benchmark evaluation themselves and submits results for asynchronous community peer review within 30 days of merge; if no peer review is received within 30 days, the solo evaluation stands with a "SOLO-VALIDATED" annotation on the benchmark result. Pass threshold: AI-augmented output scores within 15% of the reference output on both dimensions. BOOTSTRAP-VALIDATED: Wave 1 evaluations using the fallback qualification path (criteria b-i or b-ii above) are tagged `BOOTSTRAP-VALIDATED` and are NOT equivalent to fully-verified quality benchmarks. Post-launch cross-validation REQUIRED: if no criterion-(a) evaluator completes cross-validation within 180 days of Wave 1 launch, BOOTSTRAP-VALIDATED benchmarks transition to UNVERIFIED-BENCHMARK status with a visible output flag prepended to the sub-skill's L0 output header (e.g., "[UNVERIFIED-BENCHMARK] Heuristic Eval L0 Summary"). Named owner: the designated Wave Lead (assigned during KICKOFF) is responsible for sourcing cross-validation before the deadline. If the deadline passes without cross-validation, the benchmark status downgrades but does not block continued use -- it signals reduced confidence in the quality baseline via the L0 flag. Re-evaluation failures (cross-validation attempted but benchmark does not pass) trigger Wave 1 WARN state. The solo bypass 30-day auto-stand provision is replaced by a peer review submission requirement -- the solo evaluation must be submitted for peer review, and `SOLO-VALIDATED` status persists until peer review is completed (it does not auto-pass on timeout). This is us keeping it honest -- the mountain does not grade your run just because nobody was watching.

### Benchmark Classification

Sub-skill quality benchmarks fall into two categories requiring different ground-truth approaches:

| Sub-Skill | Benchmark Type | Ground-Truth Source | Adjudication Method |
|-----------|---------------|--------------------|--------------------|
| `/ux-heuristic-eval` | Evaluation | Nielsen Norman Group published evaluations (external case studies with known findings) | Direct comparison: AI output vs. published finding set |
| `/ux-jtbd` | Evaluation | Intercom JTBD Playbook examples (published job statements with known structure) | 3-criterion deterministic rubric (format, dimensions, outcome-framing) |
| `/ux-lean-ux` | Synthesis | No external ground-truth for assumption map quality | Expert panel review: 2+ qualified reviewers assess risk categorization completeness |
| `/ux-heart-metrics` | Evaluation | Google HEART paper GSM examples (published templates with known dimension mappings) | Direct comparison: AI GSM population vs. published reference |
| `/ux-atomic-design` | Evaluation | Brad Frost reference component libraries (published classification examples) | Direct comparison: AI classification vs. published hierarchy |
| `/ux-inclusive-design` | Evaluation | WCAG 2.2 test suites (published accessibility violation sets) | Direct comparison: AI finding set vs. planted violation inventory |
| `/ux-behavior-design` | Synthesis | Fogg Behavior Model published case studies (e.g., Fogg & Hreha 2019 behavioral examples) provide directional ground-truth but not definitive bottleneck diagnosis for novel contexts | Expert panel review: 2+ qualified reviewers assess B=MAP bottleneck identification against reference behavioral scenarios drawn from published case studies |
| `/ux-kano-model` | Evaluation | Matzler & Hinterhuber (1998) reference survey dataset with known classifications | Direct comparison: AI classification vs. published classification accuracy |
| `/ux-design-sprint` | Synthesis | No external ground-truth for prototype spec quality from a challenge statement | Cross-sub-skill convergence check: Design Sprint output evaluated by Heuristic Eval sub-skill for internal consistency |
| `/ux-ai-first-design` | Synthesis | No established ground-truth (emerging domain) | Expert panel review deferred until Enabler DONE |

**Evaluation-type** sub-skills have external ground-truth structurally available -- benchmarks compare AI output against published reference material. **Synthesis-type** sub-skills produce novel outputs where ground-truth requires expert definition -- benchmarks use expert panel review (minimum 2 qualified reviewers per IN-004-I5 expert qualification) or cross-sub-skill convergence checks. **Reviewer qualification cross-reference:** Expert panels for synthesis-type benchmark reviews follow the synthesis validation qualification standard (2 years UX practice, non-team-member). Pre-launch blind evaluators use the separate criterion a/b-i/b-ii standard. The two pools serve distinct functions; qualification standards are intentionally different.

### Quality Standards

- [ ] All agent definitions validate against JSON Schema (H-34)
- [ ] All agents include P-003, P-020, P-022 constitutional compliance in `.governance.yaml` `constitution.principles_applied` (H-34)
- [ ] All agents have >= 3 `forbidden_actions` entries in governance YAML
- [ ] No sub-skill agent has Task tool access (P-003 enforcement)
- [ ] Each sub-skill agent definition's `.md` YAML frontmatter explicitly excludes `Task` from `tools` (or uses `disallowedTools: ["Task"]`), AND each `.governance.yaml` includes `Task` in `capabilities.forbidden_actions` with P-003 consequence statement. P-003 enforcement: Sub-skill agents are declared with `disallowedTools: [Task]` in their `.md` frontmatter, preventing recursive delegation. CI test gate: `grep -rl 'tools:.*Task' skills/user-experience/agents/*.md skills/ux-*/agents/*.md` must return EMPTY (no matches = all workers comply). If non-empty, CI fails listing the non-compliant agent files. Additionally, `grep -rL 'tools:' skills/user-experience/agents/*.md skills/ux-*/agents/*.md` detects files with no `tools:` field at all (which inherit all tools including Task) -- any matches also fail the gate. CI gate documented in `ci-checks.md` with test script reference.
- [ ] Parent orchestrator quality gate uses S-014 scoring at wave transitions
- [ ] Sub-skill deliverables meet >= 0.92 weighted composite for C2+ outputs (H-13)

### Wave Progression

- [ ] Wave 1 entry criteria documented and enforced (KICKOFF-SIGNOFF.md completion)
- [ ] Wave 2-5 entry criteria documented with bypass conditions for stall recovery
- [ ] Wave entry enforcement: orchestrator checks `WAVE-{N}-SIGNOFF.md` existence before routing to Wave N+1 sub-skills
- [ ] Each wave's `WAVE-N-SIGNOFF.md` is a closure deliverable -- wave completion is not recognized until the signoff file passes schema validation (all required fields non-empty) and is committed to the repository
- [ ] Wave bypass requires 3-field documentation (unmet criterion, impact assessment, remediation plan with target date); bypass state produces warning banner on all sub-skill outputs
- [ ] Wave transitions tracked via `/worktracker` entities

### Post-Launch Success Metrics


**Post-launch metrics measurement plan:** Each metric below requires: (a) named owner, (b) measurement frequency (monthly minimum), (c) tooling/storage specification, and (d) 90-day post-launch review trigger. Owner assignment, tooling selection, and storage specification are defined during Wave 1 implementation and documented in `skills/user-experience/rules/metrics-plan.md`. The 90-day post-launch review evaluates whether targets are being met and whether metric definitions need revision.

- [ ] Track: number of unique teams that complete Wave 1 within 30 days of first invocation (target: baseline establishment, no threshold for V1)
- [ ] Track: average S-014 quality score of sub-skill outputs across all invocations (target: >= 0.85 mean composite)
- [ ] Track: wave progression rate -- percentage of teams that advance beyond Wave 1 within 90 days (target: baseline establishment)
- [ ] Track: MCP fallback activation rate per sub-skill (target: < 20% of invocations requiring fallback for Required MCPs)
- [ ] Track: synthesis hypothesis confidence gate override rate -- how often users invoke the Human Override Justification field on LOW-confidence outputs (target: monitoring only; high rates indicate the gate is working as designed)
- [ ] Track: time-to-insight per sub-skill invocation. Time-to-insight defined as: elapsed wall-clock time from sub-skill invocation to first actionable finding presented to user. Measurement: instrumented via session timestamp delta (invocation start to first L0 output). Threshold: <= 15 minutes for Wave 1-2 sub-skills; <= 30 minutes for Wave 3-5 sub-skills. Collected per-invocation; aggregated monthly. The Pre-Launch Validation 15% pass threshold applies per-dimension (completeness and actionability individually), not as a composite. Time-to-insight thresholds (<=15 min Wave 1-2, <=30 min Wave 3-5) are enforced as post-launch operational metrics measured by instrumented session timestamps, not as pre-launch evaluation criteria.

---
