# QA Strategy — PM/PMM Skill Quality Assurance Framework

> **Document ID:** QA-STRATEGY-001
> **Workflow ID:** `pm-pmm-impl-20260228-001`
> **Project:** PROJ-018-pm-pmm-skill
> **Criticality:** C3 (Significant — >1 day to reverse, >10 files, skill-level API change)
> **Quality Threshold:** >= 0.95 weighted composite (all phases)
> **Accept-with-Caveats Floor:** >= 0.90 (document caveats, proceed with warning)
> **Hard Reject:** < 0.90
> **Version:** 1.0
> **Created:** 2026-03-01
> **Agents:** adv-selector, adv-scorer
> **Source Constraints:** ORCH-C03 through ORCH-C10, quality-enforcement.md H-13/H-14/H-18

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Quality Framework Overview](#quality-framework-overview) | Criticality classification, thresholds, circuit breaker, scoring mechanism |
| [1. Strategy Selection per Phase](#1-strategy-selection-per-phase) | C3 strategy assignment to each orchestration phase and its specific artifacts |
| [2. Per-Artifact-Type Quality Dimensions](#2-per-artifact-type-quality-dimensions) | Scoring rubrics and dimension weights tailored to each artifact category |
| [3. Adversary Execution Configuration](#3-adversary-execution-configuration) | Multi-executor groupings, isolation rules, and per-group mandates (ORCH-C05) |
| [4. Quality Gate Protocol](#4-quality-gate-protocol) | Pre-barrier checklist, score recording, decision tree, accept/reject/caveat rules, plateau detection |
| [5. Scoring Calibration Notes](#5-scoring-calibration-notes) | Anti-leniency guidance, per-dimension calibration, 0.95 vs 0.85 vs 0.75 exemplars |
| [6. Constraint Compliance Mapping](#6-constraint-compliance-mapping) | How this strategy satisfies each ORCH-C constraint |
| [7. Artifact Inventory and Phase Assignment](#7-artifact-inventory-and-phase-assignment) | Complete list of deliverables tracked through quality gates |
| [8. Overnight Execution Adaptations](#8-overnight-execution-adaptations) | Autonomous execution mode adjustments, logging, post-run review |

---

## Quality Framework Overview

### Criticality Classification

The `/pm-pmm` skill is classified **C3 (Significant)** per `quality-enforcement.md` criticality levels:

| Criterion | Assessment | C3 Threshold |
|-----------|------------|--------------|
| Reversibility | >1 day to reverse -- 5 agents, 15 templates, governance files, SKILL.md, trigger map registration | >1 day |
| File count | >30 files (5 agent `.md` + 5 `.governance.yaml` + 15 templates + SKILL.md + architecture docs + workflows) | >10 files |
| API changes | New skill registration in CLAUDE.md, AGENTS.md, and `mandatory-skill-usage.md` (H-22 trigger map) | API changes |
| Scope | New skill with 5 agents, 15 artifact types, 18 framework integrations, 5 workflow patterns, 3 org configs | New capability |

### Quality Thresholds

| Parameter | Value | Source |
|-----------|-------|--------|
| Criticality level | C3 (Significant) | `quality-enforcement.md` criticality levels |
| Quality threshold (PASS) | >= 0.95 | ORCH-C03, CONSTRAINTS.yaml `quality_threshold_override` (elevated from standard 0.92) |
| Accept-with-caveats threshold | >= 0.90 | CONSTRAINTS.yaml `accept_with_caveats_threshold` |
| Standard C2+ threshold (reference) | >= 0.92 | `quality-enforcement.md` H-13 |
| Maximum iterations per artifact | 5 | ORCH-C04 circuit breaker |
| Plateau detection | Score delta < 0.01 for 3 consecutive iterations | ORCH-C04, `agent-routing-standards.md` RT-M-010 |
| Minimum iterations | 3 | H-14 creator-critic-revision cycle |
| Scoring mechanism | S-014 LLM-as-Judge, 6-dimension weighted composite | `quality-enforcement.md` |
| Leniency bias counteraction | Score strictly against rubric; when uncertain between adjacent scores, choose the lower one | `/adversary` SKILL.md |

### Threshold Elevation Rationale

The threshold is elevated from the standard 0.92 (H-13) to 0.95 for this workflow because:

1. **New skill with broad scope** -- 5 agents, 15 artifact types, and 18 framework integrations create a large defect surface area.
2. **Cross-agent dependency** -- Agent boundary decisions cascade to routing, artifact ownership, templates, and workflows.
3. **Overnight autonomous execution** -- No human review at barrier transitions; elevated threshold compensates.
4. **OSS release preparation** -- Per Issue #123, external-facing artifacts demand higher quality.

### Scoring Dimensions (Baseline Weights)

Per `quality-enforcement.md` SSOT, all C3 deliverables use the 6-dimension weighted composite:

| Dimension | Weight | PM/PMM Focus |
|-----------|--------|--------------|
| Completeness | 0.20 | Framework coverage, AC coverage, all required sections present |
| Internal Consistency | 0.20 | Agent boundaries non-overlapping, artifact ownership unambiguous, mode behaviors consistent |
| Methodological Rigor | 0.20 | Frameworks applied correctly (not just named), methodology sections actionable |
| Evidence Quality | 0.15 | Citations to Issue #123 spec, references to validated frameworks, traceability |
| Actionability | 0.15 | Agent definitions produce usable outputs, templates generate useful artifacts |
| Traceability | 0.10 | AC mapping complete, design decisions linked to requirements |

**Composite score calculation:**

```
composite = (completeness * 0.20) + (internal_consistency * 0.20) + (methodological_rigor * 0.20)
          + (evidence_quality * 0.15) + (actionability * 0.15) + (traceability * 0.10)
```

---

## 1. Strategy Selection per Phase

### 1.1 Overview: C3 Strategy Set

The `/pm-pmm` skill is classified **C3 (Significant)** per quality-enforcement.md:

- Greater than one day to reverse (5 agent definitions, 15 templates, SKILL.md, governance YAMLs, trigger map registrations)
- More than 10 files affected
- Introduces new skill-level routing surface in the Jerry framework

**C3 required strategies:** S-007, S-002, S-014, S-004, S-012, S-013

**C3 optional (not required until Phase 4 tournament):** S-001, S-003, S-010, S-011

**Phase 4 tournament:** All 10 selected strategies (S-001 through S-014, excluding excluded strategies)

---

### 1.2 Phase 1 — Research and Foundation

**Phase 1 artifacts under quality review:**

| Artifact | Pipeline | Path |
|----------|----------|------|
| `architecture.md` | Engineering | `eng/phase-1-research/architecture.md` |
| Template schemas (15 types) | Engineering | `eng/phase-1-research/template-schemas/` |
| `frontmatter.md` (schema) | Engineering | `eng/phase-1-research/frontmatter.md` |
| `threat-model.md` | Security | `sec/phase-1-threat-model/threat-model.md` |
| `attack-surf.md` | Security | `sec/phase-1-threat-model/attack-surf.md` |
| `qa-strategy.md` (this document) | Quality | `quality/phase-1-setup/qa-strategy.md` |

**Strategies applied at Phase 1 Barrier:**

| Strategy | ID | Applies To | Rationale |
|----------|----|------------|-----------|
| Constitutional AI Critique | S-007 | architecture.md, frontmatter schema | Architecture decisions that deviate from Jerry governance (H-34, H-35, P-003) cannot be caught by linting alone. S-007 checks alignment with constitutional triplet before implementation begins. |
| Devil's Advocate | S-002 | architecture.md, template schemas | The 5-agent decomposition, 15-template design, and discovery/delivery mode split are foundational decisions. S-002 challenges whether simpler alternatives were genuinely ruled out. |
| LLM-as-Judge | S-014 | All Phase 1 artifacts | Provides quantitative composite score across all 6 dimensions. Required for barrier gate verdict. |
| Pre-Mortem Analysis | S-004 | architecture.md | Asks: "It is 6 months from now, the skill has failed. What went wrong from architecture decisions made in Phase 1?" Surfaces integration risks before they propagate. |
| FMEA | S-012 | Template schemas, frontmatter schema | Systematically enumerates failure modes for each of the 15 template types. Produces severity × occurrence × detectability scores per failure mode. |
| Inversion Technique | S-013 | architecture.md | Inverts the question: "How would we design a PM/PMM skill that is maximally confusing, inconsistent, and misused?" Surfaces design traps that normal forward analysis misses. |

**Strategies NOT applied at Phase 1 (deferred to tournament):**

| Strategy | ID | Reason |
|----------|----|--------|
| Red Team Analysis | S-001 | Security pipeline handles threat modeling independently; S-001 without security context risks redundancy at Phase 1. |
| Steelman Technique | S-003 | Steelman is most valuable when alternatives have already been articulated (Phase 4 context). |
| Self-Refine | S-010 | Creator-side quality gate; applied by creating agents before submission, not by quality pipeline. |
| Chain-of-Verification | S-011 | Applied in Phase 4 to verify final integrated deliverable against ACs. |

---

### 1.3 Phase 2 — Tier 1 Core Agent Implementation

**Phase 2 artifacts under quality review:**

| Artifact | Pipeline | Path |
|----------|----------|------|
| `pm-product-strategist.md` | Engineering | `eng/phase-2-tier1-agents/` |
| `pm-product-strategist.governance.yaml` | Engineering | `eng/phase-2-tier1-agents/` |
| `pm-customer-insight.md` | Engineering | `eng/phase-2-tier1-agents/` |
| `pm-customer-insight.governance.yaml` | Engineering | `eng/phase-2-tier1-agents/` |
| `pm-market-strategist.md` | Engineering | `eng/phase-2-tier1-agents/` |
| `pm-market-strategist.governance.yaml` | Engineering | `eng/phase-2-tier1-agents/` |
| `SKILL.md` | Engineering | `eng/phase-2-tier1-agents/SKILL.md` |
| `agent-sec-review.md` | Security | `sec/phase-2-agent-review/agent-sec-review.md` |
| `prompt-injection.md` | Security | `sec/phase-2-agent-review/prompt-injection.md` |

**Strategies applied at Phase 2 Barrier:**

| Strategy | ID | Applies To | Rationale |
|----------|----|------------|-----------|
| Constitutional AI Critique | S-007 | All 3 agent .md files, all 3 .governance.yaml | Primary concern: every agent must embed P-003/P-020/P-022 constitutional triplet with >= 3 forbidden actions. S-007 reads the full agent definition against the JERRY_CONSTITUTION. |
| Devil's Advocate | S-002 | SKILL.md routing triggers, agent boundaries | Challenges: Are the routing triggers distinct enough? Could two agents be merged? Are the discovery/delivery mode boundaries genuinely non-overlapping? |
| LLM-as-Judge | S-014 | All Phase 2 artifacts | Quantitative scoring. Each agent .md and .governance.yaml is scored independently, then a cross-agent consistency sub-score is applied. |
| Pre-Mortem Analysis | S-004 | Agent interaction model | Asks: "The customer-insight agent returns sensitive user data to product-strategist. What are the failure scenarios for each information flow?" |
| FMEA | S-012 | Discovery/delivery mode switching | Enumerates failure modes when agents switch modes mid-session: (1) mode state not passed, (2) framework selection diverges between modes, (3) example outputs contradict mode definition. |
| Inversion Technique | S-013 | SKILL.md routing triggers | Inverts: "How could we write triggers that maximize routing mismatches?" Reveals over-broad or under-specified keyword patterns before they ship. |

---

### 1.4 Phase 3 — Tier 2 Specialized Agent Implementation

**Phase 3 artifacts under quality review:**

| Artifact | Pipeline | Path |
|----------|----------|------|
| `pm-business-analyst.md` | Engineering | `eng/phase-3-tier2-agents/` |
| `pm-business-analyst.governance.yaml` | Engineering | `eng/phase-3-tier2-agents/` |
| `pm-competitive-analyst.md` | Engineering | `eng/phase-3-tier2-agents/` |
| `pm-competitive-analyst.governance.yaml` | Engineering | `eng/phase-3-tier2-agents/` |
| `integration-sec.md` | Security | `sec/phase-3-integration-review/integration-sec.md` |
| `cross-agent-risk.md` | Security | `sec/phase-3-integration-review/cross-agent-risk.md` |

**Strategies applied at Phase 3 Barrier:**

| Strategy | ID | Applies To | Rationale |
|----------|----|------------|-----------|
| Constitutional AI Critique | S-007 | Both Tier 2 agent .md and .governance.yaml | Same constitutional check as Phase 2. Particular attention to pm-competitive-analyst: competitive intelligence handling risks touching P-022 (deception about data provenance). |
| Devil's Advocate | S-002 | Cross-agent data flow architecture | Challenges: Is the Tier 1 / Tier 2 distinction justified? Does adding pm-business-analyst and pm-competitive-analyst create routing ambiguity that the current SKILL.md does not resolve? |
| LLM-as-Judge | S-014 | All Phase 3 artifacts + cross-agent consistency | Applies an additional cross-agent consistency dimension: do Tier 2 agents' artifact ownership scopes conflict with Tier 1? |
| Pre-Mortem Analysis | S-004 | Integration model | Asks: "The integration has shipped. Six months later, users report that competitive-analyst and market-strategist produce contradictory outputs on the same input. What integration-level decisions caused this?" |
| FMEA | S-012 | Financial data handling in pm-business-analyst | Financial projections, viability models, and business case artifacts carry high-severity failure modes. FMEA rates each: severity of incorrect financial output, occurrence probability, and current detectability. |

**Additional strategy at Phase 3 (first appearance beyond required set):**

| Strategy | ID | Applies To | Rationale |
|----------|----|------------|-----------|
| Inversion Technique | S-013 | Routing disambiguation rules for Tier 1 vs Tier 2 | When 5 agents are defined, routing collisions between Tier 1 and Tier 2 agents are the most likely operational failure. Inversion asks: "Design the routing table that creates maximum ambiguity." |

---

### 1.5 Phase 4 — Integration, Verification, and Tournament

**Phase 4 artifacts under quality review:**

| Artifact | Pipeline | Path |
|----------|----------|------|
| `org-configs.md` | Engineering | `eng/phase-4-integration/org-configs.md` |
| `workflow-patterns.md` | Engineering | `eng/phase-4-integration/workflow-patterns.md` |
| `trigger-map-update.md` | Engineering | `eng/phase-4-integration/trigger-map-update.md` |
| `e2e-verification.md` | Engineering | `eng/phase-4-integration/e2e-verification.md` |
| `final-sec-report.md` | Security | `sec/phase-4-final/final-sec-report.md` |
| `remediation-plan.md` | Security | `sec/phase-4-final/remediation-plan.md` |

**Tournament configuration — all 10 selected strategies:**

| Execution Order | Strategy | ID | Tournament Role |
|-----------------|----------|----|----------------|
| 1 | Self-Refine | S-010 | Pre-tournament self-assessment by creator agents. Ensures all artifacts are creator-revised before external review. |
| 2 | Constitutional AI Critique | S-007 | Constitutional pass: required first in tournament sequence to catch governance violations before investing critique effort. |
| 3 | Steelman Technique | S-003 | Strengthen the strongest arguments before adversarial attack (H-16 mandate: steelman before devil's advocate). |
| 4 | Devil's Advocate | S-002 | Challenge assumptions established during phases 1-3, now with full artifact context. |
| 5 | Red Team Analysis | S-001 | Treat the complete skill as an adversarial target: attack surface, misuse scenarios, capability abuse. |
| 6 | Pre-Mortem Analysis | S-004 | System-level pre-mortem: entire skill has failed post-deployment. Root cause back to any phase decision. |
| 7 | FMEA | S-012 | Full skill FMEA: all 5 agents, all 15 templates, all 3 org configs, all 5 workflow patterns. |
| 8 | Inversion Technique | S-013 | Full skill inversion: how to maximize user confusion, routing failures, and framework misapplication. |
| 9 | Chain-of-Verification | S-011 | Verify each acceptance criterion (AC-01 through AC-14) against the delivered artifacts. Produces a binary AC-by-AC trace. |
| 10 | LLM-as-Judge | S-014 | Final composite score. Tournament score = weighted average of all 10 strategy findings, using the 6-dimension rubric. |

**Tournament scoring protocol:**

- Each strategy produces findings and a per-strategy quality signal (PASS / CONCERNS / FAIL)
- S-014 (LLM-as-Judge) runs last and incorporates all strategy findings into the composite score
- Final tournament composite must reach >= 0.95 for the skill to proceed to deployment
- Accept-with-caveats applies at >= 0.90: deployment held with documented finding list
- Hard reject below 0.90: halt, log, escalate to human

---

## 2. Per-Artifact-Type Quality Dimensions

### 2.1 Dimension Weights — Baseline (All Artifacts)

Per quality-enforcement.md SSOT, all C3 deliverables use the following 6-dimension weighted composite:

| Dimension | Weight | Abbrev |
|-----------|--------|--------|
| Completeness | 0.20 | COMP |
| Internal Consistency | 0.20 | ICON |
| Methodological Rigor | 0.20 | MRIG |
| Evidence Quality | 0.15 | EVID |
| Actionability | 0.15 | ACTN |
| Traceability | 0.10 | TRAC |

The per-artifact rubrics below specify what each dimension means in the context of each artifact type. adv-scorer MUST apply these rubrics and MUST NOT use generic scoring language that could apply to any artifact.

---

### 2.2 Architecture Decisions (`architecture.md`, ADR-format outputs)

**Dimension-specific rubrics:**

| Dimension | Weight | What Constitutes a PASS for Architecture |
|-----------|--------|------------------------------------------|
| Completeness (COMP) | 0.20 | All viable alternatives are enumerated (minimum 3). No "we considered X but did not explore it." Decision context captures: stakeholder constraints, time constraints, reversibility. |
| Internal Consistency (ICON) | 0.20 | Decision rationale does not contradict itself within the document. Consequences section reflects the actual chosen option, not a prior draft option. All cross-references resolve to real artifacts. |
| Methodological Rigor (MRIG) | 0.20 | **Primary focus for architecture.** Alternatives analysis uses named evaluation dimensions (not generic "pros/cons"). Each alternative is assessed against the same dimensions. Decision matrix or equivalent is present. The methodology for comparing alternatives is explicit. |
| Evidence Quality (EVID) | 0.15 | Claims about alternatives are backed by either: (a) reference to research artifacts (PS-001 series), (b) Jerry framework constraints cited by rule ID, or (c) stated axioms with explicit acknowledgment they are axioms. No unsupported assertions. |
| Actionability (ACTN) | 0.15 | Implementation guidance is sufficient for an engineer unfamiliar with the decision to proceed without re-asking the architect. Each consequence is actionable: "agents MUST implement X" not "agents should think about X." |
| Traceability (TRAC) | 0.10 | Decision maps to at least one acceptance criterion or requirement. Rationale cites the source of constraints (issue number, rule ID, research artifact). |

**Rigor of alternatives analysis — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | All alternatives fully enumerated; identical evaluation dimensions; explicit trade-off narrative; quantitative or semi-quantitative comparison |
| 0.85 | Most alternatives present; some evaluation dimensions missing for one alternative |
| 0.70 | Two alternatives compared but third or fourth are mentioned without analysis |
| 0.50 | One alternative compared to the chosen approach with no formal evaluation |
| < 0.50 | No alternatives analysis present |

**Decision traceability — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | Every claim traces to a cited source (rule ID, AC number, research file path) |
| 0.85 | Most claims traced; 1-2 assertions without explicit citation |
| 0.70 | Core decision traced; consequences section lacks citations |
| 0.50 | Decision statement traced but rationale section is narrative without evidence |
| < 0.50 | No traceability; assertions are free-floating |

---

### 2.3 Agent Definitions (`.md` files with YAML frontmatter)

**Dimension-specific rubrics:**

| Dimension | Weight | What Constitutes a PASS for Agent .md |
|-----------|--------|---------------------------------------|
| Completeness (COMP) | 0.20 | All 7 required markdown body sections present: `<identity>`, `<purpose>`, `<input>`, `<capabilities>`, `<methodology>`, `<output>`, `<guardrails>`. All 5 official Claude Code frontmatter fields that are mandatory for this skill are populated. Framework operationalization depth: each assigned framework has a named methodology step in `<methodology>`, not a general reference. |
| Internal Consistency (ICON) | 0.20 | `<identity>` cognitive mode matches `<methodology>` reasoning pattern. `<capabilities>` tool list does not include tools contradicted by `<guardrails>`. `<output>` artifact paths are consistent with the skill file organization plan. Discovery and delivery modes produce non-overlapping artifact types. |
| Methodological Rigor (MRIG) | 0.20 | Framework operationalization depth: each of the agent's assigned frameworks is operationalized into concrete steps, not cited as a label. For example, if pm-customer-insight uses "Jobs-to-be-Done," the methodology section describes JTBD execution steps, not merely "apply JTBD." Mode-switching logic (discovery vs. delivery) is explicit and deterministic. |
| Evidence Quality (EVID) | 0.15 | Framework citations are accurate: no hallucinated framework names, no misattributed frameworks. Framework versions or canonical sources are cited where relevant. Agent boundaries are justified by reference to framework ownership (which frameworks belong to which agent and why). |
| Actionability (ACTN) | 0.15 | Example outputs are present for both discovery mode and delivery mode. Examples are concrete enough that a user could distinguish this agent's output from another agent's output. Routing triggers are specific enough to not fire for adjacent agents. |
| Traceability (TRAC) | 0.10 | Agent maps to at least one acceptance criterion. Framework assignments trace to the framework allocation table in architecture.md. Constitutional triplet (P-003, P-020, P-022) is explicitly cited in the agent definition. |

**Framework operationalization depth — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | Each framework has named methodology steps in the agent's `<methodology>` section. Steps are concrete enough to produce different outputs depending on input. No framework is a label without a process. |
| 0.85 | Most frameworks operationalized; one or two cited by name only with generic "apply X" instructions |
| 0.70 | Frameworks appear in `<identity>` expertise list but methodology section is mode-generic rather than framework-specific |
| 0.50 | Frameworks are listed in frontmatter description only; body section does not reference them |
| < 0.50 | No frameworks operationalized; agent is a generic analyst with a PM label |

**Constitutional compliance — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | P-003, P-020, P-022 all explicitly cited in `.governance.yaml` `constitution.principles_applied`; >= 3 forbidden_actions each reference a constitutional principle; worker agent does NOT have Task in allowed_tools |
| 0.80 | Constitutional triplet present but one forbidden_action does not explicitly reference a principle |
| 0.60 | P-003/P-020/P-022 are in principles_applied but forbidden_actions are generic (no principle cross-reference) |
| 0.40 | Only P-003 present; P-020 and P-022 missing |
| 0.0 | Constitutional triplet absent |

---

### 2.4 Governance YAMLs (`.governance.yaml` files)

**Dimension-specific rubrics:**

| Dimension | Weight | What Constitutes a PASS for .governance.yaml |
|-----------|--------|----------------------------------------------|
| Completeness (COMP) | 0.20 | Schema validation completeness: all required fields per `agent-governance-v1.schema.json` are present and non-empty. Required fields: `version`, `tool_tier`, `identity.role`, `identity.expertise` (>= 2 entries), `identity.cognitive_mode`. Recommended fields with >= 3 entries: `capabilities.forbidden_actions`, `constitution.principles_applied`. |
| Internal Consistency (ICON) | 0.20 | `tool_tier` is consistent with the tools listed in the companion `.md` frontmatter. Cognitive mode in YAML matches the agent's `<methodology>` reasoning pattern in the .md body. Persona tone is consistent with the agent's expected audience (PM/PMM practitioners). |
| Methodological Rigor (MRIG) | 0.20 | Tool tier selection follows the principle of least privilege: the assigned tier is the lowest tier that satisfies the agent's operational requirements. Justification for tier selection is traceable. `guardrails.fallback_behavior` uses a valid enum value (or documented custom value). |
| Evidence Quality (EVID) | 0.15 | `identity.expertise` entries are specific (not generic). `validation.post_completion_checks` assertions are verifiable (not assertions that require human judgment). |
| Actionability (ACTN) | 0.15 | `guardrails.input_validation` contains at least one rule that would catch a malformed or out-of-scope input. `session_context.on_receive` and `on_send` fields define how this agent participates in multi-agent workflows. |
| Traceability (TRAC) | 0.10 | Version field follows semantic versioning. `enforcement.quality_gate_tier` maps to this workflow's C3 designation. The YAML is traceable to the companion .md via the `name` field match. |

**Schema validation completeness — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | 100% of required fields present; all recommended fields present with valid values; schema validation produces zero errors |
| 0.85 | Required fields 100% present; 1-2 recommended fields missing (e.g., `session_context` absent) |
| 0.70 | All truly required fields present; several recommended fields absent; schema validates with warnings |
| 0.50 | One required field missing or has wrong type |
| < 0.50 | Schema validation fails; multiple required fields absent or malformed |

---

### 2.5 Templates (15 artifact templates)

**Dimension-specific rubrics:**

| Dimension | Weight | What Constitutes a PASS for a Template |
|-----------|--------|----------------------------------------|
| Completeness (COMP) | 0.20 | Template covers all sub-sections required by its artifact type. Discovery mode variant and delivery mode variant are both present (or explicitly declared as mode-agnostic with justification). All placeholder fields are documented with guidance on expected content. No template is a generic markdown structure with a PM label. |
| Internal Consistency (ICON) | 0.20 | Template structure is consistent with the agent assigned to produce it. Artifact ownership matrix shows no overlap between this template and templates owned by other agents. Internal cross-references within the template resolve to real sections. |
| Methodological Rigor (MRIG) | 0.20 | **Framework alignment:** Template structure reflects the framework methodology of the producing agent. For example, a JTBD-based template has sections for Job Executor, Job Statement, and Outcome Metrics — not generic "research notes." Template sections map to framework outputs, not to generic analyst sections. |
| Evidence Quality (EVID) | 0.15 | Template provides guidance fields that prompt the agent to cite evidence. No template section is free-form narrative without evidence guidance. Framework references in section headers are accurate. |
| Actionability (ACTN) | 0.15 | A practitioner who has never used this skill could complete the template based on its guidance. Placeholder text is specific enough to distinguish this template from a generic PM template. Example fill-in is present for at least one section. |
| Traceability (TRAC) | 0.10 | Template header declares: producing agent, framework source, artifact type. Template ID traces to frontmatter schema. |

**Discovery/delivery mode coverage — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | Template explicitly defines discovery variant (open-ended exploration sections) and delivery variant (execution-focused sections); mode is declared in template frontmatter |
| 0.85 | Template has mode sections but one mode is significantly thinner than the other (less than 60% of sections present) |
| 0.70 | Template mentions modes in instructions but structure is identical for both |
| 0.50 | Template is mode-agnostic without explicit justification |
| < 0.50 | Template has no mode awareness; it is purely a generic document skeleton |

---

### 2.6 SKILL.md

**Dimension-specific rubrics:**

| Dimension | Weight | What Constitutes a PASS for SKILL.md |
|-----------|--------|---------------------------------------|
| Completeness (COMP) | 0.20 | Progressive disclosure structure is present: L0 (stakeholder), L1 (developer), L2 (strategic). All 5 agents are referenced with their routing triggers. All 15 template artifact types are documented. Both discovery and delivery modes are explained at L0. File is under the 500-line limit per SKILL.md standards. |
| Internal Consistency (ICON) | 0.20 | Routing triggers in SKILL.md are consistent with triggers in `mandatory-skill-usage.md` update. Agent names in SKILL.md match the actual agent file names. Discovery/delivery mode definitions in SKILL.md are consistent with definitions in agent .md files. |
| Methodological Rigor (MRIG) | 0.20 | Routing trigger coverage: every meaningful use case a PM or PMM practitioner would bring to this skill is addressable through the defined routing triggers. No trigger is so broad that it fires for non-PM/PMM requests (e.g., "analyze" as a standalone trigger is insufficient). |
| Evidence Quality (EVID) | 0.15 | Framework references are accurate. Example use cases cite realistic PM/PMM scenarios. Trigger keywords map to documented practitioner terminology. |
| Actionability (ACTN) | 0.15 | A PM or PMM practitioner reading SKILL.md at L0 can determine in under 2 minutes whether this skill serves their current need. The L1 section gives a developer enough context to extend or debug the skill. Quick-start example is present. |
| Traceability (TRAC) | 0.10 | SKILL.md header cross-references GitHub Issue #123. Each trigger keyword maps to at least one agent. The version field is consistent with the skill version declared in agent .governance.yaml files. |

**Routing trigger coverage — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | Every trigger keyword routes to exactly one agent with no documented ambiguity. Negative keyword list prevents false-positive firing from adjacent PM concepts. At least 5 distinct trigger keywords per agent. |
| 0.85 | Trigger coverage good; 1-2 potential routing ambiguities documented but not yet resolved |
| 0.70 | Triggers cover major use cases but 3+ practitioner scenarios are not triggerable without slash command |
| 0.50 | Generic triggers (e.g., "product," "market") that would fire for non-PM/PMM requests |
| < 0.50 | No meaningful routing logic; SKILL.md is a description with no routing configuration |

**Progressive disclosure — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | Distinct L0/L1/L2 sections; L0 is self-contained for stakeholder decision; L1 has technical implementation detail; L2 has strategic implications for skill evolution |
| 0.85 | L0 and L1 present and distinct; L2 absent or merged into L1 |
| 0.70 | L0 and L1 present but L0 is not truly self-contained (requires L1 reading) |
| 0.50 | Single narrative without progressive disclosure structure |
| < 0.50 | SKILL.md is a list of agent names with brief descriptions only |

---

### 2.7 Security Artifacts (`threat-model.md`, `attack-surf.md`, `agent-sec-review.md`, `prompt-injection.md`, security reports)

**Dimension-specific rubrics:**

| Dimension | Weight | What Constitutes a PASS for Security Artifacts |
|-----------|--------|------------------------------------------------|
| Completeness (COMP) | 0.20 | Threat coverage: all five agents appear in the threat model. All 15 template types appear in the attack surface enumeration. Prompt injection surface covers: system prompt extraction, framework injection, mode-switching abuse, cross-agent data leakage, competitive intelligence handling (pm-competitive-analyst). |
| Internal Consistency (ICON) | 0.20 | Risk ratings are consistent across agents with similar characteristics. A vulnerability present in pm-customer-insight that is also structurally present in pm-market-strategist is flagged in both. Mitigations do not contradict each other across agents. |
| Methodological Rigor (MRIG) | 0.20 | Named threat modeling methodology applied (STRIDE, DREAD, or equivalent). Attack surface enumeration follows a systematic approach (not just a list of concerns). Prompt injection testing documents the actual injection vector, not just the conclusion. |
| Evidence Quality (EVID) | 0.15 | Vulnerability claims include reproduction steps or evidence of the condition. Risk ratings are calibrated: not everything is HIGH. Probability estimates are grounded in the actual deployment context (Jerry Framework, Claude Code, single-user CLI). |
| Actionability (ACTN) | 0.15 | **Mitigation specificity:** Every identified threat has a specific mitigation action, not a generic recommendation. "Add input validation" is insufficient; "Add input validation that rejects prompts containing `</identity>` or `<identity>` injection patterns" is acceptable. Mitigations are implementable in the guardrails of the agent definitions. |
| Traceability (TRAC) | 0.10 | Each vulnerability traces to the specific artifact (agent .md section or template section) where it manifests. Mitigations trace to specific guardrail fields in `.governance.yaml`. |

**Threat coverage — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | All 5 agents individually covered; all 15 template types enumerated in attack surface; cross-agent data flow threats enumerated; competitive intelligence and customer data handling threats explicitly addressed |
| 0.85 | All 5 agents covered; template coverage has 3-4 gaps; cross-agent threats present |
| 0.70 | Agents covered; template coverage cursory (by category rather than individual type); cross-agent threats mentioned but not enumerated |
| 0.50 | Agent coverage present; template coverage absent |
| < 0.50 | Generic PM/PMM threat coverage without reference to specific artifacts |

**Mitigation specificity — specific rubric:**

| Score | Description |
|-------|-------------|
| 1.0 | Every mitigation is implementable in a specific agent guardrail field, with the field name and expected value stated |
| 0.85 | Most mitigations are specific; 1-2 are general ("add rate limiting") without implementation path |
| 0.70 | Mitigations are specific in type but not in implementation field |
| 0.50 | Mitigations are generic security recommendations not tailored to the agent definition format |
| < 0.50 | No actionable mitigations; threat list only |

---

## 3. Adversary Execution Configuration

### 3.1 Multi-Executor Mandate (ORCH-C05)

ORCH-C05 prohibits using one agent for all adversary strategies. This is an anchoring bias prevention rule: a single executor who runs S-007 first will color all subsequent strategy outputs with constitutional lens findings.

**Minimum executor isolation requirement:** At least 3 distinct adv-executor Task invocations per phase. No single executor handles more than 3 strategies. Each executor receives only: (a) the artifact under review, (b) its assigned strategy template, (c) the quality dimensions rubric for this artifact type. It does NOT receive prior executor findings until the adv-scorer synthesis phase.

### 3.2 Executor Groups

**Group A — Constitutional (S-007)**

| Field | Value |
|-------|-------|
| Strategy | S-007 Constitutional AI Critique |
| Executor isolation | Dedicated Task invocation. Receives: artifact file path, constitutional triplet checklist, governance YAML schema |
| Context given | JERRY_CONSTITUTION.md reference, H-34/H-35 rule text, constitutional triplet (P-003, P-020, P-022) |
| Context withheld | Other strategy findings, prior iteration scores, creator rationale |
| Output format | Per-principle compliance table: PASS / FAIL / CONDITIONAL per principle, with quoted evidence from the artifact |
| Applies at | Phases 1, 2, 3, 4 |

**Group B — Dialectical (S-002 Devil's Advocate + S-003 Steelman)**

| Field | Value |
|-------|-------|
| Strategies | S-002 Devil's Advocate, S-003 Steelman (S-003 always runs BEFORE S-002 per H-16) |
| Executor isolation | Single Task invocation for the group, but S-003 MUST complete before S-002 begins within the executor. Separate from Group A. |
| Ordering enforcement | H-16: Steelman before Devil's Advocate. The executor is initialized with S-003 template first, then S-002. Both outputs are delivered in sequence, not merged. |
| Context given | Artifact under review, the strongest argument for the design decisions made |
| Context withheld | Group A constitutional findings, Group C analytical findings |
| Output format | S-003 section: steelmanned defense (3-5 strongest arguments). S-002 section: devil's advocate challenges (each challenge must be falsifiable, not stylistic). |
| Applies at | Phase 1: S-002 only (S-003 deferred to Phase 4). Phases 2-3: S-002. Phase 4 tournament: both. |

**Group C — Analytical (S-012 FMEA + S-013 Inversion)**

| Field | Value |
|-------|-------|
| Strategies | S-012 FMEA, S-013 Inversion Technique |
| Executor isolation | Single Task invocation for the group, separate from Groups A and B |
| Context given | Artifact under review, failure mode taxonomy for the artifact type (from Section 2 rubrics), the inversion question specific to this artifact type |
| Context withheld | Group A and B findings |
| Output format | S-012 section: FMEA table with failure mode, effect, severity (1-10), occurrence (1-10), detectability (1-10), RPN, recommended action. S-013 section: inverted design description followed by the mirrored positive requirements. |
| Applies at | Phases 1, 2, 3, 4 |

**Group D — Scoring (S-014 LLM-as-Judge)**

| Field | Value |
|-------|-------|
| Strategy | S-014 LLM-as-Judge |
| Executor isolation | Separate Task invocation. **Two-pass scoring protocol** (see Anchoring Bias Mitigation below). |
| Context given | **Pass 1:** Artifact under review, the 6-dimension weighted rubric, this qa-strategy.md per-artifact-type rubric. NO prior group findings. **Pass 2:** Group A/B/C findings provided for finding-adjusted scoring. |
| Output format | Pass 1: Independent dimension-by-dimension score table, weighted composite. Pass 2: Adjusted score table with delta annotations. Final: PASS/ACCEPT-WITH-CAVEATS/FAIL verdict, top-3 improvement actions. |
| Applies at | Phases 1, 2, 3, 4 |

**Group D Anchoring Bias Mitigation (FM-015, RPN: 294)**

Group D is the only group that receives upstream findings. This creates an anchoring bias risk: severity language from Group A/B/C findings can inflate or deflate the scorer's independent judgment. Two approaches were evaluated:

| Option | Protocol | Anchoring Isolation | Tradeoff |
|--------|----------|---------------------|----------|
| **A (Recommended)** | Group D receives ONLY the artifact and rubric for Pass 1. Scores independently. Then receives prior findings for Pass 2 adjustment. Both scores recorded. | **Strong isolation.** Scorer forms independent judgment before exposure to upstream framing. | Requires two Task invocations for Group D (additional token cost). |
| B | Group D receives prior findings but MUST produce scores BEFORE reading them (honor system within a single invocation). | Weak isolation. LLM may still be influenced by findings present in context even if instructed to score first. | Single invocation, but anchoring risk remains. |

**Selected: Option A (two-pass protocol).** The stronger isolation approach is selected because anchoring bias is the highest-scoring QA failure mode (FM-015, RPN 294) and the additional token cost of a second Task invocation is small relative to the quality risk.

**Two-pass protocol specification:**

1. **Pass 1 (Independent Scoring):** Group D executor receives: (a) the artifact under review, (b) the 6-dimension weighted rubric, (c) the per-artifact-type rubric from this qa-strategy.md. It does NOT receive Group A/B/C findings. It produces an independent composite score (`score_pass_1`).

2. **Pass 2 (Finding-Adjusted Scoring):** A second Group D executor invocation receives: (a) the artifact, (b) the rubric, (c) all Group A/B/C findings, (d) the Pass 1 score. It produces an adjusted composite score (`score_pass_2`).

3. **Delta check:** If `|score_pass_1 - score_pass_2| > 0.10`, the scorer MUST document the specific finding(s) that caused the shift in a `score_delta_justification` field. Deltas exceeding 0.15 trigger a flag for human review.

4. **Final score:** The `score_pass_2` (finding-adjusted) is the authoritative score used for the quality gate verdict. The `score_pass_1` is retained in the report for transparency and anchoring bias analysis.

**Group E — Tournament Additional (Phases 4 Only)**

| Field | Value |
|-------|-------|
| Strategies | S-001 Red Team Analysis, S-004 Pre-Mortem Analysis, S-010 Self-Refine, S-011 Chain-of-Verification |
| Executor isolation | Minimum 2 additional Task invocations for Group E. Recommended split: (S-001 + S-004) in one executor, (S-010 + S-011) in a second executor. |
| Context given | Full integrated skill artifact set (all phases' deliverables), acceptance criteria AC-01 through AC-14, security report final findings |
| Applies at | Phase 4 tournament only |

### 3.3 Executor Invocation Sequence per Phase (Phases 1-3)

```
Phase N Barrier
│
├─ PARALLEL LAUNCH (no dependency between A, B, C)
│   ├─ Task → Group A executor (S-007)
│   ├─ Task → Group B executor (S-003→S-002 sequence)
│   └─ Task → Group C executor (S-012 + S-013)
│
├─ WAIT for A, B, C completion
│
└─ SEQUENTIAL
    └─ Task → Group D executor (S-014)
               └─ Receives: artifact + A findings + B findings + C findings
               └─ Produces: composite score + verdict
```

### 3.4 Executor Invocation Sequence — Phase 4 Tournament

```
Phase 4 Tournament
│
├─ CREATOR PRE-CHECK
│   └─ Task → S-010 Self-Refine (creator agents self-review all artifacts)
│
├─ PARALLEL LAUNCH (after S-010 complete)
│   ├─ Task → Group A executor (S-007)
│   ├─ Task → Group B executor (S-003→S-002)
│   ├─ Task → Group C executor (S-012 + S-013)
│   └─ Task → Group E-1 executor (S-001 Red Team + S-004 Pre-Mortem)
│
├─ WAIT for Group A, B, C, E-1 completion
│
├─ Task → Group E-2 executor (S-011 Chain-of-Verification)
│          └─ Receives: all Group A/B/C/E-1 findings + AC list
│
├─ WAIT for Group E-2 completion
│
└─ Task → Group D executor (S-014 LLM-as-Judge — Tournament Mode)
           └─ Receives: all findings from all groups
           └─ Produces: tournament composite score + final verdict
```

### 3.5 Revision Cycle After Scoring (ORCH-C07 Compliance)

All revision work is delegated to background subagents via Task. The orchestrator tracks only:

- Artifact ID
- Current iteration count (max 5)
- Current composite score
- PASS / REVISE / FAIL verdict

The orchestrator MUST NOT perform revision work in the main context. When revision is needed:

```
adv-scorer verdict: REVISE (score < 0.95, >= 0.90)
│
└─ Task → creator agent (fresh context)
           Input: original artifact, adv-scorer findings
           Output: revised artifact (same file path)
           Max iterations: 5
           Plateau detection: if delta < 0.01 for 3 consecutive iterations → halt
```

---

## 4. Quality Gate Protocol

### 4.1 Pre-Barrier Checklist

Before any sync barrier transition, the orchestrator MUST verify all items on this checklist. A single FAIL blocks the barrier transition (ORCH-C03).

**Universal pre-barrier checks (all 4 barriers):**

| ID | Check | Verification Method | Pass Condition |
|----|-------|---------------------|----------------|
| PB-01 | All phase artifacts exist as files on disk | File existence check per artifact inventory (Section 7) | Every artifact file present |
| PB-02 | adv-scorer report exists for the current phase | File existence: `quality/phase-{N}-*/adv-phase{N}-report.md` | Report file present and non-empty |
| PB-03 | Composite quality score >= 0.95 | Parse `composite_score` field from adv-scorer report | score >= 0.95 OR score >= 0.90 with caveats documented |
| PB-04 | Iteration count <= 5 for all artifacts | Parse `iteration_count` field per artifact | max(iteration_count) <= 5 |
| PB-05 | All adversarial findings are addressed | Compare finding count to addressed/justified count | finding_count == addressed_count |
| PB-06 | At least 3 distinct adv-executor Task invocations occurred | Count unique Task invocations for adv-executor in this phase | count >= 3 |
| PB-07 | No FAIL verdict in any per-artifact score | Check all per-artifact verdicts in adv report | No artifact verdict == "FAIL" |
| PB-08 | CONSTRAINTS.yaml C01-CHK-01 and C01-CHK-02 verified (Barrier 1 only) | Count agent/barrier nodes in diagrams vs registry | Counts match |
| PB-09 | Adversary ran BEFORE barrier transition timestamp | Compare adv report timestamp to current timestamp | adv_report.timestamp < current_time |

**Barrier-specific additional checks:**

| Barrier | Additional Check | Condition |
|---------|-----------------|-----------|
| Barrier 2 | H-34 schema validation result recorded | `quality/phase-2-gate/schema-validation.log` exists with 0 errors |
| Barrier 2 | H-35 constitutional compliance documented | Each of 3 Tier 1 agents has P-003/P-020/P-022 in governance YAML |
| Barrier 3 | Cross-agent consistency score present | adv-phase3-report.md includes `cross_agent_consistency_score` |
| Barrier 4 | All 10 tournament strategies executed | Tournament report shows 10 strategy findings sections |
| Barrier 4 | AC-01 through AC-14 verified by S-011 | Chain-of-Verification table present with binary result per AC |

### 4.2 Score Recording Format

Every adv-scorer report for this workflow MUST use the following format (fields are machine-parseable by the orchestrator):

```yaml
adv_scorer_report:
  workflow_id: "pm-pmm-impl-20260228-001"
  phase: 2                              # 1 | 2 | 3 | 4
  artifact_id: "pm-product-strategist"  # Artifact identifier
  artifact_type: "agent_definition"     # artifact type from taxonomy
  iteration: 3                          # Which iteration (1-5)

  dimension_scores:
    completeness:          0.95          # Raw 0.0-1.0
    internal_consistency:  0.92
    methodological_rigor:  0.97
    evidence_quality:      0.90
    actionability:         0.96
    traceability:          0.88

  weights:
    completeness:          0.20
    internal_consistency:  0.20
    methodological_rigor:  0.20
    evidence_quality:      0.15
    actionability:         0.15
    traceability:          0.10

  composite_score:         0.938        # Weighted sum; calculated, not asserted
  composite_calculation:   "(0.95×0.20)+(0.92×0.20)+(0.97×0.20)+(0.90×0.15)+(0.96×0.15)+(0.88×0.10)"

  verdict: "ACCEPT_WITH_CAVEATS"        # PASS | ACCEPT_WITH_CAVEATS | REVISE | FAIL

  findings:
    - id: "F-001"
      strategy: "S-007"
      dimension: "traceability"
      severity: "MEDIUM"                # HIGH | MEDIUM | LOW | INFORMATIONAL
      finding: "P-020 is listed in constitution.principles_applied but does not appear in forbidden_actions"
      addressed: true
      address_method: "revised"         # revised | justified
      justification: null               # populated if address_method == justified

    - id: "F-002"
      strategy: "S-012"
      dimension: "completeness"
      severity: "LOW"
      finding: "Delivery mode example output is present but only shows one of three framework variants"
      addressed: true
      address_method: "justified"
      justification: "All three framework variants share the same output structure; showing one is representative per template design decision in architecture.md §3.2"

  caveats:
    - "Traceability dimension scored below 0.90 on first iteration; revised to 0.88 after addressing F-001. Remaining gap is the absence of AC cross-reference in the agent identity section."

  prior_iterations:
    - iteration: 1
      composite_score: 0.871
    - iteration: 2
      composite_score: 0.912

  delta_history:
    - delta_1_to_2: 0.041
    - delta_2_to_3: 0.026

  plateau_triggered: false
  plateau_reason: null

  executor_invocations:
    - group: "A"
      strategy: "S-007"
      task_id: "task-20260301-001"
    - group: "B"
      strategy: "S-003"
      task_id: "task-20260301-002"
    - group: "B"
      strategy: "S-002"
      task_id: "task-20260301-002"
    - group: "C"
      strategy: "S-012"
      task_id: "task-20260301-003"
    - group: "C"
      strategy: "S-013"
      task_id: "task-20260301-003"
    - group: "D"
      strategy: "S-014"
      task_id: "task-20260301-004"
```

**Calculation rule for adv-scorer:** The `composite_score` field MUST be computed as the explicit weighted sum shown in `composite_calculation`. The adv-scorer is PROHIBITED from asserting a composite score that is not derivable from the dimension scores and weights. Any mismatch between the stated composite and the calculated composite is a scoring integrity failure.

### 4.3 Accept/Revise/Reject Decision Tree

```
composite_score = weighted_sum(dimension_scores × weights)
│
├─ score >= 0.95
│   └─ PASS → Artifact flows downstream
│              Barrier transition: ALLOWED
│
├─ 0.90 <= score < 0.95
│   ├─ iteration < 5
│   │   └─ REVISE → Launch creator agent Task with findings
│   │               Increment iteration counter
│   │               Re-run adversary Groups A/B/C, then Group D
│   │               Repeat decision tree
│   │
│   └─ iteration == 5 (max reached)
│       └─ ACCEPT_WITH_CAVEATS
│           → Document caveats in barrier handoff
│           → Proceed with WARNING flag set
│           → Barrier transition: ALLOWED (with warning)
│           → Human must review caveats at post-run review
│
└─ score < 0.90
    ├─ iteration < 5
    │   └─ REVISE → Launch creator agent Task with findings
    │               (same as REVISE path above)
    │
    └─ iteration == 5 (max reached) AND score < 0.90
        └─ FAIL
            → Do NOT pass artifact downstream (ORCH-C10)
            → Log current best result + all adversarial findings
            → Log full revision history
            → HALT barrier transition
            → Escalate to human (overnight execution: halt_and_log per ORCH config)
```

### 4.4 Accept-with-Caveats Rules

When an artifact reaches the ACCEPT_WITH_CAVEATS state (score >= 0.90 but < 0.95 at max iterations), the following rules apply:

| Rule | Requirement |
|------|-------------|
| AC-RULE-01 | Caveats are enumerated in the barrier handoff as a numbered list |
| AC-RULE-02 | Each caveat identifies the affected dimension, the finding ID, and the risk if the caveat is not resolved |
| AC-RULE-03 | The barrier handoff verdict field is set to `ACCEPT_WITH_CAVEATS` (not `PASS`) |
| AC-RULE-04 | Downstream phases are notified of the caveats in their cross-pollination handoff artifacts |
| AC-RULE-05 | The Phase 4 tournament MUST explicitly evaluate whether any prior-phase caveats were resolved or whether they persist in the final skill |
| AC-RULE-06 | Human review at post-run is required to clear caveat status before deployment |
| AC-RULE-07 | No artifact may carry more than 3 unresolved caveats into the next phase. If 4+ caveats exist, the artifact is treated as FAIL |

### 4.5 Plateau Detection and Early Halt Procedure

Plateau detection fires when the quality score improvement between consecutive iterations falls below the threshold.

**Trigger condition:** score_delta < 0.01 for 3 consecutive iterations.

**Plateau detection algorithm:**

```
delta_1_to_2 = score_iteration_2 - score_iteration_1
delta_2_to_3 = score_iteration_3 - score_iteration_2
delta_3_to_4 = score_iteration_4 - score_iteration_3

IF delta_2_to_3 < 0.01 AND delta_3_to_4 < 0.01 AND delta_4_to_5 < 0.01:
    plateau_triggered = TRUE
    HALT iteration cycle
    Record current score as final score
    Apply decision tree to final score
```

**When plateau halts before max iterations:**

The artifact is evaluated against the decision tree using the plateau-halted score. Plateau does not confer PASS status — it merely halts further iteration to prevent context exhaustion. If the plateau score is:
- >= 0.95: PASS (normal)
- 0.90-0.94: ACCEPT_WITH_CAVEATS (caveat: quality plateau reached; specific dimension was unresponsive to revision)
- < 0.90: FAIL (standard FAIL procedure)

**Plateau halt documentation requirement:**

The adv-scorer report MUST set `plateau_triggered: true` and record the `delta_history` array. The `plateau_reason` field MUST describe which dimension stopped responding to revisions (e.g., "Evidence Quality dimension did not improve after iteration 2 despite three targeted revisions; underlying issue appears to be lack of primary source citations which requires external research not possible in this context").

---

## 5. Scoring Calibration Notes

### 5.1 Anti-Leniency Guidance for adv-scorer

adv-scorer operates with leniency bias risk (L2-REINJECT rank=4 in quality-enforcement.md: "LLM-as-Judge scoring: Apply strict rubric. Leniency bias must be actively counteracted"). The following anti-leniency guidance is mandatory for every scoring session in this workflow.

**General anti-leniency posture:**

1. A score of 0.95 means the artifact is ready for production deployment without modification. It is NOT a score for "pretty good." If you have ANY findings that are not marked LOW or INFORMATIONAL, the composite cannot be 0.95.

2. Do not award dimension scores that contradict your findings. If you find a completeness gap (a missing section), the Completeness dimension CANNOT score 1.0.

3. The default for any unverified claim is to score it as if the claim is unsubstantiated. The artifact must earn its Evidence Quality score; the scorer does not assume good faith.

4. Framework operationalization is binary at the per-framework level. If a framework is listed but has no corresponding methodology steps, that framework counts as ABSENT, not PARTIAL, for the Completeness dimension.

5. Do not average out a 0.60 with a 1.0 to produce a 0.80 "Completeness" score. Report the 0.60 as the Completeness score and document why — the weighted composite will reflect it proportionally.

**Per-dimension anti-leniency notes:**

| Dimension | Common Leniency Traps | Anti-Leniency Rule |
|-----------|----------------------|---------------------|
| Completeness | "The section exists so it's complete" | A section header without substantive content scores 0.20-0.40, not 1.0 |
| Internal Consistency | "It's mostly consistent" | Any contradiction between two stated facts in the artifact drops ICON by at least 0.15 per contradiction |
| Methodological Rigor | "They mentioned the framework" | Mentioning a framework with no methodology steps = 0.40 on MRIG for that framework |
| Evidence Quality | "The claims sound reasonable" | Unsubstantiated claims score 0.50 on EVID regardless of plausibility |
| Actionability | "An expert would know what to do" | Score against a competent practitioner who is new to this skill, not an expert |
| Traceability | "The intent is clear even without citations" | No citation = no traceability credit for that claim |

### 5.2 Dimension-Specific Calibration Per Artifact Type

**For agent definition .md files:**

| Dimension | Calibration Anchor |
|-----------|-------------------|
| Completeness | The 18 PM/PMM frameworks assigned to this skill must each appear in at least one agent with a methodology step. If any framework is absent from ALL agent definitions, aggregate Completeness for the skill drops to below 0.80. |
| Methodological Rigor | MRIG for an agent .md is primarily about framework operationalization. Generic "use the best PM judgment" is a MRIG score of 0.40-0.50. Explicit framework steps score 0.90+. |
| Actionability | The discovery mode example output and delivery mode example output are the primary Actionability signals. Absent examples: Actionability cannot exceed 0.70. |

**For .governance.yaml files:**

| Dimension | Calibration Anchor |
|-----------|-------------------|
| Completeness | Schema validation is the ground truth. Zero validation errors is required for COMP >= 0.90. One validation error caps COMP at 0.75. Multiple errors cap COMP at 0.50. |
| Traceability | A YAML that cannot be traced to its companion .md (mismatched name) caps TRAC at 0.40. |

**For templates:**

| Dimension | Calibration Anchor |
|-----------|-------------------|
| Completeness | If both discovery and delivery mode variants are absent, COMP cannot exceed 0.60. |
| Methodological Rigor | A template that could be used for any domain (not specific to PM/PMM and not framework-specific) caps MRIG at 0.50. |

**For SKILL.md:**

| Dimension | Calibration Anchor |
|-----------|-------------------|
| Completeness | All 5 agents must appear with routing triggers. Missing any agent caps COMP at 0.70. |
| Actionability | A PM practitioner who has never used Jerry must be able to invoke the skill from SKILL.md alone. Test: could a practitioner generate a PRD using only SKILL.md guidance? If not, ACTN < 0.80. |

**For security artifacts:**

| Dimension | Calibration Anchor |
|-----------|-------------------|
| Completeness | If any of the 5 agents is absent from the threat model, COMP caps at 0.65. |
| Actionability | Generic recommendations ("add authentication") score 0.50 on ACTN. Mitigation must name the specific guardrail field in the agent definition. |
| Evidence Quality | Risk ratings must be calibrated to the actual deployment context (Jerry Framework, single-user CLI). Ratings copied from enterprise threat models without adjustment score 0.60 on EVID. |

### 5.3 Score Exemplars: What Constitutes 0.95 vs. 0.85 vs. 0.75

**Exemplar: Agent Definition .md File**

| Composite | Characteristics |
|-----------|----------------|
| **0.95 (PASS)** | All 7 body sections present and substantive. All frameworks assigned to this agent have named methodology steps. Both discovery and delivery mode examples are present and specific. Constitutional triplet cited with >= 3 forbidden actions referencing principles. All cross-references resolve. Routing triggers are distinct from all other agents. Minor suggestions only from adversarial review (LOW severity). |
| **0.85 (REVISE)** | All 7 body sections present. 2-3 frameworks are cited by name only with no methodology steps. One mode example is present but the other is absent. Constitutional triplet present in YAML but one forbidden_action is generic. One cross-reference to a file path that does not yet exist (acceptable if file is in same phase). 1-2 MEDIUM findings from adversarial review. Scope for targeted revision is clear. |
| **0.75 (REJECTED — significant rework)** | Section structure present but Methodology section is a paragraph of general PM philosophy rather than framework-specific steps. Examples absent for both modes or present but generic (could apply to any domain). Constitutional triplet partially present (e.g., P-003 only). Multiple MEDIUM and at least one HIGH finding. The core problem: the agent is a labeled analyst, not an operationalized framework-driven agent. |

**Exemplar: Architecture Decision (.md)**

| Composite | Characteristics |
|-----------|----------------|
| **0.95 (PASS)** | Minimum 3 alternatives enumerated with identical evaluation dimensions. Decision matrix or equivalent present. Consequences section maps directly to the chosen option with no legacy text from other options. Every claim cites a rule ID, research artifact, or stated axiom. Pre-mortem concerns addressed in the consequences section. |
| **0.85 (REVISE)** | 3 alternatives enumerated but evaluation dimensions differ between alternatives (one has 5 criteria, another has 3). Decision matrix present but one alternative is evaluated more favorably than the evidence supports. One consequence is forward-looking ("we should eventually...") rather than implementation-ready. 2-3 citations missing. |
| **0.75 (REJECTED — significant rework)** | Only 2 alternatives compared. No formal evaluation dimensions — narrative comparison only. Consequences section describes implementation tasks rather than consequence of the decision. No citations. Alternative analysis reads as post-hoc rationalization of a predetermined decision. |

**Exemplar: SKILL.md**

| Composite | Characteristics |
|-----------|----------------|
| **0.95 (PASS)** | L0/L1/L2 sections clearly delineated and each self-contained for its audience. All 5 agents present with >= 5 routing triggers each. Negative keyword list present for at least 3 agents where collision risk exists. Discovery and delivery modes explained at L0 with a 2-sentence description each. Quick-start example leads a practitioner to their first artifact in <= 5 steps. File is under 500 lines. |
| **0.85 (REVISE)** | L0/L1/L2 sections present but L0 requires reading L1 to understand the skill's scope. 5 agents present; 2 agents have < 3 routing triggers. No negative keyword list; routing collision between pm-market-strategist and pm-competitive-analyst is unresolved. Quick-start example present but assumes familiarity with the Jerry skill invocation syntax. |
| **0.75 (REJECTED — significant rework)** | Single narrative without progressive disclosure. Agents listed with one-sentence descriptions; no routing triggers. Discovery vs. delivery modes mentioned once in the introduction but not explained or differentiated in practice. No quick-start. A PM practitioner reading this document could not invoke the skill without consulting external documentation. |

**Exemplar: Governance YAML**

| Composite | Characteristics |
|-----------|----------------|
| **0.95 (PASS)** | Zero schema validation errors. All required fields present with valid values. `capabilities.forbidden_actions` has >= 5 entries (>= 3 with constitutional principle cross-references). `guardrails.input_validation` has >= 2 rules, one of which rejects a specific malformed input pattern. `session_context.on_receive` and `on_send` populated. Tool tier is the minimum viable for the agent's operational requirements. |
| **0.85 (REVISE)** | Zero schema validation errors. All required fields present. `forbidden_actions` has exactly 3 entries (minimum). `guardrails.input_validation` has one generic rule ("validate input format"). `session_context` fields absent. Tool tier is defensible but not optimized (T3 where T2 would suffice). |
| **0.75 (REJECTED — significant rework)** | One schema validation error (missing required field or wrong type). `forbidden_actions` has 2 entries (below minimum). Constitutional triplet not fully cited. `guardrails` section is present but all values are boilerplate from another agent. Tool tier may be T5 (Full) for an agent that never needs to delegate — principle of least privilege violated. |

---

## 6. Constraint Compliance Mapping

| ORCH Constraint | How This Strategy Satisfies It |
|-----------------|-------------------------------|
| ORCH-C03 | Section 4.1 pre-barrier checklist PB-02 and PB-03 enforce that no creator proceeds without adversary score >= 0.95. Section 4.3 decision tree specifies the path for each score range. |
| ORCH-C04 | Section 4.5 plateau detection and Section 4.3 max iteration enforcement (iterator counter capped at 5). Max iteration ceiling stated in all rubrics. |
| ORCH-C05 | Section 3.2 defines four executor groups (A, B, C, D) each as separate Task invocations. Section 3.3 invocation sequence mandates parallel launch. No group handles more than 3 strategies. |
| ORCH-C06 | Section 1 assigns strategies to each of the 4 phases. Section 4.1 PB-09 verifies adversary ran before barrier transition. Adversary is not only at Phase 4. |
| ORCH-C07 | Section 3.5 delegates all revision to background subagents via Task. Orchestrator tracks only the 4 fields. |
| ORCH-C08 | Section 4.2 score recording format field `findings[].addressed` and `addressed_count` enforcement. PB-05 requires finding_count == addressed_count. |
| ORCH-C09 | Section 3.5 and Section 4.3 keep all content creation in Task-delegated workers. Orchestrator tracks metrics only. |
| ORCH-C10 | Section 4.3 decision tree: FAIL verdict results in "Do NOT pass artifact downstream." Section 4.4 AC-RULE-07 caps caveats at 3 before triggering FAIL. |

---

## 7. Artifact Inventory and Phase Assignment

This table is the authoritative inventory of all artifacts subject to quality gating in this workflow. adv-scorer MUST verify completeness of this list against the phase barrier before issuing a barrier report.

| Phase | Artifact ID | File Name | Artifact Type | Quality Gate |
|-------|-------------|-----------|---------------|-------------|
| 1 | ARCH-001 | `eng/phase-1-research/architecture.md` | architecture_decision | Barrier 1 |
| 1 | TSCH-001 | `eng/phase-1-research/template-schemas/` (15 files) | template_schema | Barrier 1 |
| 1 | FMTS-001 | `eng/phase-1-research/frontmatter.md` | frontmatter_schema | Barrier 1 |
| 1 | THRT-001 | `sec/phase-1-threat-model/threat-model.md` | security_threat_model | Barrier 1 |
| 1 | ATKS-001 | `sec/phase-1-threat-model/attack-surf.md` | security_attack_surface | Barrier 1 |
| 1 | QAST-001 | `quality/phase-1-setup/qa-strategy.md` | quality_strategy | Barrier 1 |
| 2 | AGNT-001 | `eng/phase-2-tier1-agents/pm-product-strategist.md` | agent_definition_md | Barrier 2 |
| 2 | AGNT-002 | `eng/phase-2-tier1-agents/pm-product-strategist.governance.yaml` | governance_yaml | Barrier 2 |
| 2 | AGNT-003 | `eng/phase-2-tier1-agents/pm-customer-insight.md` | agent_definition_md | Barrier 2 |
| 2 | AGNT-004 | `eng/phase-2-tier1-agents/pm-customer-insight.governance.yaml` | governance_yaml | Barrier 2 |
| 2 | AGNT-005 | `eng/phase-2-tier1-agents/pm-market-strategist.md` | agent_definition_md | Barrier 2 |
| 2 | AGNT-006 | `eng/phase-2-tier1-agents/pm-market-strategist.governance.yaml` | governance_yaml | Barrier 2 |
| 2 | SKMD-001 | `eng/phase-2-tier1-agents/SKILL.md` | skill_md | Barrier 2 |
| 2 | SECR-001 | `sec/phase-2-agent-review/agent-sec-review.md` | security_agent_review | Barrier 2 |
| 2 | SECR-002 | `sec/phase-2-agent-review/prompt-injection.md` | security_prompt_injection | Barrier 2 |
| 3 | AGNT-007 | `eng/phase-3-tier2-agents/pm-business-analyst.md` | agent_definition_md | Barrier 3 |
| 3 | AGNT-008 | `eng/phase-3-tier2-agents/pm-business-analyst.governance.yaml` | governance_yaml | Barrier 3 |
| 3 | AGNT-009 | `eng/phase-3-tier2-agents/pm-competitive-analyst.md` | agent_definition_md | Barrier 3 |
| 3 | AGNT-010 | `eng/phase-3-tier2-agents/pm-competitive-analyst.governance.yaml` | governance_yaml | Barrier 3 |
| 3 | SECR-003 | `sec/phase-3-integration-review/integration-sec.md` | security_integration | Barrier 3 |
| 3 | SECR-004 | `sec/phase-3-integration-review/cross-agent-risk.md` | security_cross_agent | Barrier 3 |
| 4 | INTG-001 | `eng/phase-4-integration/org-configs.md` | integration_config | Barrier 4 (Tournament) |
| 4 | INTG-002 | `eng/phase-4-integration/workflow-patterns.md` | integration_workflow | Barrier 4 (Tournament) |
| 4 | INTG-003 | `eng/phase-4-integration/trigger-map-update.md` | routing_registration | Barrier 4 (Tournament) |
| 4 | INTG-004 | `eng/phase-4-integration/e2e-verification.md` | verification_report | Barrier 4 (Tournament) |
| 4 | SECF-001 | `sec/phase-4-final/final-sec-report.md` | security_final_report | Barrier 4 (Tournament) |
| 4 | SECF-002 | `sec/phase-4-final/remediation-plan.md` | security_remediation | Barrier 4 (Tournament) |

**Template artifacts (15 types, gated at Barrier 1 as schemas, then individually validated at Phase 4 tournament):**

| Template ID | Artifact Type | Producing Agent | Gate |
|-------------|--------------|-----------------|------|
| TMPL-001 | Product Requirements Document (PRD) | pm-product-strategist | B1 (schema), B4 (final) |
| TMPL-002 | Product Strategy | pm-product-strategist | B1 (schema), B4 (final) |
| TMPL-003 | Product Roadmap | pm-product-strategist | B1 (schema), B4 (final) |
| TMPL-004 | User Research Plan | pm-customer-insight | B1 (schema), B4 (final) |
| TMPL-005 | Jobs-to-be-Done Canvas | pm-customer-insight | B1 (schema), B4 (final) |
| TMPL-006 | Customer Journey Map | pm-customer-insight | B1 (schema), B4 (final) |
| TMPL-007 | Market Opportunity Assessment | pm-market-strategist | B1 (schema), B4 (final) |
| TMPL-008 | Competitive Analysis | pm-competitive-analyst | B1 (schema), B4 (final) |
| TMPL-009 | Positioning Statement | pm-market-strategist | B1 (schema), B4 (final) |
| TMPL-010 | Go-to-Market Plan | pm-market-strategist | B1 (schema), B4 (final) |
| TMPL-011 | Business Case | pm-business-analyst | B1 (schema), B4 (final) |
| TMPL-012 | Financial Model | pm-business-analyst | B1 (schema), B4 (final) |
| TMPL-013 | Business Viability Risk Assessment | pm-business-analyst | B1 (schema), B4 (final) |
| TMPL-014 | Competitive Intelligence Report | pm-competitive-analyst | B1 (schema), B4 (final) |
| TMPL-015 | Win/Loss Analysis | pm-competitive-analyst | B1 (schema), B4 (final) |

---

## 8. Overnight Execution Adaptations

This workflow executes in overnight autonomous mode per CONSTRAINTS.yaml `overnight_execution` configuration. The following adaptations ensure unattended operation preserves quality while preventing indefinite hangs.

### 8.1 Mode Adjustments

| Parameter | Standard Mode | Overnight Mode | Rationale |
|-----------|---------------|----------------|-----------|
| Human gates | Enabled (user approves barrier transitions) | **Disabled** (`human_gates: disabled`) | No human available during overnight execution |
| Quality gates | Automated with standard threshold (0.92) | **Automated with elevated threshold (0.95)** | Elevated threshold compensates for absent human judgment |
| Accept-with-caveats | Requires human approval | **Automated at >= 0.90** (logged, not blocked) | Prevents overnight execution from halting on near-threshold results |
| Barrier commits | Optional | **Required per barrier** (`commit_per_barrier: true`) | Enables post-run human review of incremental progress |
| Deployment | Immediate upon pass | **Held for post-run human review** regardless of scores | All artifacts held in project directory; no registration in CLAUDE.md/AGENTS.md/mandatory-skill-usage.md until human review |
| Token limit behavior | User decides | **Pause and resume** (`pause_duration_minutes: 5`, `max_retries_on_token_limit: 3`) | Automated recovery from transient token limits |
| Critical failure | User escalation | **Halt and log** (`escalation_on_critical_failure: halt_and_log`) | Overnight execution cannot escalate to human; halt preserves state for review |

### 8.2 Logging Requirements

All quality gate decisions MUST be logged to quality phase directories for post-run review:

| Event | Log Location | Content |
|-------|-------------|---------|
| Strategy execution findings | `quality/phase-{N}-*/adv-executor-{group}-findings.md` | Per-strategy findings with severity classification |
| Composite scores | `quality/phase-{N}-*/adv-phase{N}-report.md` | 6-dimension scores, composite, verdict, iteration history |
| Accept-with-caveats decisions | `quality/phase-{N}-*/caveats-log.md` | Score, dimension breakdown, specific caveats, risk assessment |
| Plateau detections | `quality/phase-{N}-*/adv-phase{N}-report.md` (iteration history) | Iteration scores, deltas, plateau detection trigger point |
| Halt decisions | `quality/phase-{N}-*/halt-report.md` | Reason for halt, best score, unresolvable findings, recommended human actions |
| Barrier commits | Git log | Per-barrier commit with artifact list, score summary, workflow ID |

### 8.3 Failure Recovery Behavior

| Failure Type | Recovery Action |
|-------------|----------------|
| Token limit hit | Pause 5 minutes, retry (max 3 retries). On 4th failure: checkpoint and halt. |
| Quality score < 0.90 at max iterations | Halt barrier. Log all findings and revision history. Do NOT proceed past barrier. |
| Schema validation failure | Attempt one auto-fix via creator Task. If still failing: halt and log. |
| MCP tool failure | Fallback to file-based persistence per `mcp-tool-standards.md` error handling. Continue execution. |
| Context fill >= 0.88 (EMERGENCY tier) | Mandatory checkpoint per AE-006d. Prepare handoff artifact. Halt if compaction would lose orchestration state. |

### 8.4 Post-Run Human Review Checklist

After overnight execution completes, the following items require human review before any artifacts are deployed to the skill directory:

1. **Caveats review** -- Read all `caveats-log.md` files for accept-with-caveats decisions. Evaluate whether caveats are acceptable or require additional revision.
2. **Halt review** -- Read all `halt-report.md` files for any halted phases. Determine whether halted artifacts should be reworked or the entire phase restarted.
3. **Barrier commit audit** -- Verify barrier commits are sequential and complete (barrier-1, barrier-2, barrier-3, barrier-4).
4. **Score trajectory** -- Review composite score progression across iterations for each phase. Look for unexpected score drops or plateaus.
5. **Constitutional compliance** -- Verify P-003, P-020, P-022 compliance across all 5 agent definitions and governance YAMLs.
6. **Agent boundary validation** -- Confirm artifact ownership matrix has zero overlap. Test routing heuristics for documented edge cases ("competitive pricing", "customer pricing", "losing deals").
7. **Framework operationalization** -- Spot-check at least 3 agent definitions to verify frameworks are operationalized with methodology steps, not just named.
8. **Template completeness** -- Verify all 15 templates exist with both discovery and delivery mode support.
9. **Trigger map registration** -- Approve or reject trigger map update in `mandatory-skill-usage.md` before deployment. Verify negative keywords prevent false-positive routing.
10. **Integration verification** -- Review e2e-verification.md results for Workflow 1 ("New Product Launch") pipeline execution.

**Deployment hold:** All artifacts remain in `projects/PROJ-018-pm-pmm-skill/` until human review is complete. Registration in CLAUDE.md, AGENTS.md, and `mandatory-skill-usage.md` is deferred to post-review deployment. This holds regardless of whether all phases scored PASS.

---

*Document version: 1.0*
*Workflow: pm-pmm-impl-20260228-001*
*Quality threshold: >= 0.95 (accept-with-caveats floor: >= 0.90)*
*Created: 2026-03-01*
*Agents: adv-selector, adv-scorer*
*SSOT references: quality-enforcement.md, CONSTRAINTS.yaml, ORCHESTRATION_PLAN.md §6*
