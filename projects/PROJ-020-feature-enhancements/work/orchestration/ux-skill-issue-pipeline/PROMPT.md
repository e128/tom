# UX Skill GitHub Enhancement Issue — Structured Prompt

> **Project:** PROJ-020-feature-enhancements
> **Created:** 2026-03-02
> **Quality Score:** 100/100 (Exemplary Tier, 7-criterion rubric)
> **Agent:** pe-builder methodology applied by main context

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Overview](#overview) | What this prompt produces |
| [Decisions](#decisions) | Architectural choices locked before execution |
| [Prompt](#prompt) | The full executable structured prompt |

---

## Overview

This prompt orchestrates a 6-phase pipeline to produce a GitHub Enhancement issue for creating a `/user-experience` skill in the Jerry Framework. The issue proposes a hybrid parent + pluggable sub-skills architecture with 10 best-in-class UX frameworks selected from 30+ candidates.

**Final output:** `gh issue create` + `gh issue comment` against `geekatron/jerry`.

---

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Skill architecture | Hybrid: parent orchestrator + pluggable sub-skills | Maximum evolvability; sub-skills register independently but route through parent |
| Issue scope | Vision + AC + follow-up comment with tech spec approach | Keeps issue compelling; implementation details deferred to project work |
| Framework selection | 10 seed + >20 discovered; ps-analyst selects best 10 | Seed list competes on equal footing; no auto-inclusion |
| Quality gate | /adversary C4 >= 0.95, each iteration as background agent | Creator-adversary feedback loop with 5 strategy-specific iterations |
| Voice | /saucer-boy McConkey hype persona | High energy, joy and excellence as multipliers, technical precision preserved |

---

## Prompt

```
Use /worktracker to create an Enhancement titled "Create /user-experience Skill —
Best-in-Class UX Framework with Pluggable Sub-Skills" under PROJ-020.

Use /orchestration with orch-planner to sequence the following 6-phase pipeline.
Output orchestration plan: projects/PROJ-020-feature-enhancements/work/orchestration/
ux-skill-issue-pipeline/ORCHESTRATION_PLAN.md

────────────────────────────────────────────────────────────────────

Phase 1 — UX Framework Research (3 PARALLEL BACKGROUND AGENTS):

Agent 1a (background): Use /problem-solving with ps-researcher to survey user
experience design frameworks and methodologies.
Data source: WebSearch.
Research scope: Discover >20 UX frameworks beyond this seed list of 10:
  1. User-Centered Design (UCD)
  2. Design Thinking (IDEO/Stanford d.school)
  3. Lean UX
  4. Agile UX
  5. BASIC UX Framework
  6. Double Diamond (UK Design Council)
  7. Atomic Design (Brad Frost)
  8. Hook Model (Nir Eyal)
  9. UX Honeycomb (Peter Morville)
  10. Five Elements of UX (Jesse James Garrett)
For each framework (seed + discovered), capture: name, origin/author, core principles,
strengths, weaknesses, applicability to AI-augmented Tiny Teams, maturity level,
community adoption, composability as an independent Jerry sub-skill.
Target: 30+ total frameworks cataloged.
Output: projects/PROJ-020-feature-enhancements/work/research/ux-frameworks-survey.md
with L0/L1/L2 sections.

Agent 1b (background): Use /problem-solving with ps-researcher to survey Gartner's
2026 "Tiny Teams" strategic technology trend.
Data source: WebSearch.
Research scope: Definition and characteristics of Tiny Teams (2-3 people + AI);
how they deliver department-scale software output; AI augmentation patterns for
design workflows; implications for UX tooling; published case studies; how UX
skills must adapt for Tiny Team adoption; Gartner's specific recommendations.
Output: projects/PROJ-020-feature-enhancements/work/research/tiny-teams-research.md
with L0/L1/L2 sections.

Agent 1c (background): Use /problem-solving with ps-researcher to survey the MCP
server ecosystem for design and UX tools.
Data source: WebSearch.
Research scope: Existing MCP servers for Figma, Miro, Sketch, Adobe XD, InVision,
Maze, Hotjar, Storybook, Zeroheight, Framer, Penpot, and other design/prototyping
tools. For tools without MCP servers, assess API capabilities and feasibility of
creating MCP adapter layers. Identify which tools are most critical for UX workflows
in a Tiny Team context.
Output: projects/PROJ-020-feature-enhancements/work/research/mcp-design-tools-survey.md
with L0/L1/L2 sections.

Sync barrier: All 3 research agents must complete before Phase 2.

Include ps-critic adversarial critique after each research output.
Quality threshold: >= 0.90 per research artifact.

────────────────────────────────────────────────────────────────────

Phase 2 — Framework Selection with C4 Adversarial Quality (ps-analyst):

Use /problem-solving with ps-analyst to evaluate all 30+ UX frameworks from Phase 1.
Apply weighted multi-criteria analysis:
  1. Applicability to AI-augmented Tiny Teams (25%)
  2. Composability as an independent pluggable Jerry sub-skill (20%)
  3. MCP tool integration potential (15%)
  4. Framework maturity and community adoption (15%)
  5. Complementarity — no redundancy across selected set (15%)
  6. Accessibility for non-UX-specialists (10%)

Select the 10 best frameworks. Seed list frameworks compete on equal footing — they
are NOT auto-included. For each selected framework, produce:
- Framework name and version/edition
- 2-sentence justification for selection
- Proposed Jerry sub-skill name (e.g., /ux-design-thinking, /ux-lean-ux)
- Required MCP integrations
- Tiny Teams enablement pattern (how this framework helps 2-3 people + AI)

Output: projects/PROJ-020-feature-enhancements/work/analysis/ux-framework-selection.md

Creator-Adversary quality loop with /adversary at C4 >= 0.95, up to 5 iterations:
  Iteration 1 (background agent): adv-executor S-001 Red Team — attack framework
    selection for gaps, missing domains, and selection bias. Feed findings to creator.
  Iteration 2 (background agent): adv-executor S-002 Devil's Advocate — challenge
    weighted criteria and Tiny Teams applicability scores. Feed findings to creator.
  Iteration 3 (background agent): adv-executor S-004 Pre-Mortem — what makes this
    selection fail in practice? Feed findings to creator.
  Iteration 4 (background agent): adv-executor S-013 Inversion — what framework
    combination would be worst? Ensure we're far from it. Feed findings to creator.
  Iteration 5 (background agent): adv-scorer S-014 LLM-as-Judge — final 6-dimension
    scoring. Feed score + dimension breakdown to creator.
Circuit breaker: Stop when score >= 0.95 OR 5 iterations reached.
Plateau detection: delta < 0.01 for 2 consecutive iterations triggers early halt.
Creator revises after each adversary round before the next fires.

────────────────────────────────────────────────────────────────────

Phase 3 — Skill Architecture Vision (ps-architect):

Use /problem-solving with ps-architect to design the /user-experience skill vision.
Input artifacts: Phase 1 research + Phase 2 framework selection (post-adversarial).

Architecture requirements:
- Hybrid model: /user-experience parent orchestrator skill with ux-lead agent
- 10 pluggable sub-skills, one per selected framework, each independently registerable
- Sub-skills route through parent but can be invoked directly
- MCP integration layer for Figma, Miro, and tools identified in Phase 1c
- Alignment with Jerry agent-development-standards.md (H-34, tool tiers, cognitive modes)
- Alignment with Gartner Tiny Teams: enable 2-3 people + AI to produce enterprise-scale
  UX deliverables
- Modular: new framework sub-skills can be added or retired without affecting others
- Address routing implications: doubling skill count pushes toward Phase 2/3 routing
  per agent-routing-standards.md — propose mitigation

Output: projects/PROJ-020-feature-enhancements/work/architecture/ux-skill-architecture-vision.md
Vision-level only: skill hierarchy, agent purposes, MCP map, Tiny Teams workflow.
NOT full technical spec (that comes from the follow-up comment guidance).

Same C4 adversarial quality loop as Phase 2 (5 background agent iterations, >= 0.95).

────────────────────────────────────────────────────────────────────

Phase 4 — GitHub Issue Content Creation with Saucer Boy Voice:

Synthesize Phase 1-3 outputs into a GitHub Enhancement issue.

Issue structure:
  Title: Compelling, concise (<70 chars), saucer-boy energy
  Body sections:
    - Vision (why this matters, what it enables)
    - Tiny Teams Alignment (Gartner 2026 connection)
    - Selected Frameworks (the 10, with 1-line descriptions)
    - Skill Architecture (hybrid parent + pluggable sub-skills)
    - MCP Integrations (tools and integration approach)
    - Acceptance Criteria (verifiable, numbered)
    - Implementation Phases (high-level roadmap)

Use /saucer-boy (background agent) to transform the entire issue into McConkey-style
hype persona voice:
  - High energy, authentic stoke for building something epic
  - Joy and excellence as multipliers
  - Technical precision preserved under the personality
  - Makes the reader WANT to build this immediately

ALSO create a follow-up comment that:
  - Explains how to use Jerry's existing skills (/problem-solving, /nasa-se,
    /orchestration, /adversary, /eng-team, /architecture, /diataxis) to design
    the full technical specification
  - Provides a structured prompt template (Template 3 pattern) the implementer
    can copy-paste to kick off the technical design
  - Written in saucer-boy voice

Output: projects/PROJ-020-feature-enhancements/work/gh-issue-draft.md
        projects/PROJ-020-feature-enhancements/work/gh-issue-followup-comment.md

────────────────────────────────────────────────────────────────────

Phase 5 — Final C4 Adversarial Quality Gate on Issue Content:

Use /adversary with C4 criticality on the complete issue + follow-up comment.
Quality threshold: >= 0.95.

Same 5-iteration background agent pattern:
  Iteration 1 (background): S-001 Red Team — attack issue completeness and gaps
  Iteration 2 (background): S-002 Devil's Advocate — challenge vision claims
  Iteration 3 (background): S-003 Steelman + S-004 Pre-Mortem — strengthen then stress-test
  Iteration 4 (background): S-007 Constitutional + S-012 FMEA — governance + failure modes
  Iteration 5 (background): S-014 LLM-as-Judge — final 6-dimension scoring

Each adversary feeds structured findings back to creator for revision.
Circuit breaker: Score >= 0.95 OR 5 iterations.
Saucer-boy voice MUST be preserved through all revisions.

────────────────────────────────────────────────────────────────────

Phase 6 — GitHub Issue Filing:

Execute `gh issue create` against geekatron/jerry with:
  - Title from Phase 4 (post-adversarial revision)
  - Body from Phase 4 (post-adversarial revision)
  - Labels: enhancement

Then execute `gh issue comment` with the follow-up comment from Phase 4.
Return the issue URL.
```
