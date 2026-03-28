# FEAT-001: Claude Code Schema Validation Research and Refinement

<!--
TEMPLATE: Feature
VERSION: 1.0.0
SOURCE: ONTOLOGY-v1.md Section 3.4.4
PURPOSE: Significant deliverable containing Stories and Enablers for schema validation work
-->

> **Type:** feature
> **Status:** in_progress
> **Priority:** high
> **Impact:** high
> **Created:** 2026-03-26T22:10:00Z
> **Due:**
> **Completed:**
> **Parent:** EPIC-001
> **Owner:** adam.nowak
> **Target Sprint:**

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Summary](#summary) | Feature overview and value proposition |
| [Benefit Hypothesis](#benefit-hypothesis) | Expected benefits |
| [Acceptance Criteria](#acceptance-criteria) | Definition of done |
| [MVP Definition](#mvp-definition) | Minimum viable scope |
| [Children Stories/Enablers](#children-storiesenablers) | Work decomposition |
| [Progress Summary](#progress-summary) | Overall progress |
| [Related Items](#related-items) | Links and dependencies |
| [History](#history) | Status changes |

---

## Summary

Research Anthropic's official Claude Code documentation, GitHub source, and community resources to discover the authoritative set of YAML frontmatter fields for both agent definitions (.md files) and skill definitions (SKILL.md files). Compare findings against existing Jerry schemas, identify gaps and inaccuracies, and produce refined JSON schemas validated through multi-skill review (security, UX, adversarial C4).

**Value Proposition:**
- Prevents agent/skill misconfiguration that causes silent runtime failures
- Enables CI-time validation of all 50+ agent definitions and 15+ skills
- Creates authoritative reference for agent developers (reduces onboarding friction)
- Security review ensures schema validation cannot be bypassed or exploited

---

## Benefit Hypothesis

**We believe that** creating authoritative, research-validated JSON schemas for Claude Code skill and agent definitions

**Will result in** reduced agent misconfiguration, faster developer onboarding, and CI-enforced definition quality

**We will know we have succeeded when** all existing agent and skill definitions validate against the refined schemas with zero false positives, and new definitions are caught by CI before reaching runtime

---

## Acceptance Criteria

### Definition of Done

- [ ] Agent frontmatter schema validated against Anthropic's official documentation
- [ ] Skill frontmatter schema validated against Anthropic's official documentation
- [ ] Gap analysis completed documenting all differences between existing and official schemas
- [ ] Refined schemas pass security review (no injection vectors, no validation bypass)
- [ ] Developer experience reviewed (clear error messages, discoverable field documentation)
- [ ] C4 adversarial review completed with all 10 strategies (tournament mode)
- [ ] All existing agent definitions validate against refined schema
- [ ] All existing SKILL.md files validate against refined schema

### Functional Criteria

| # | Criterion | Verified |
|---|-----------|----------|
| AC-1 | Refined agent schema includes all fields documented by Anthropic as of March 2026 | [ ] |
| AC-2 | Refined skill schema includes all fields documented by Anthropic as of March 2026 | [ ] |
| AC-3 | Schema correctly rejects invalid field values (wrong enum, bad pattern, missing required) | [ ] |
| AC-4 | Schema correctly accepts all valid field combinations used in existing Jerry definitions | [ ] |
| AC-5 | Research artifacts document sources with URLs and access dates | [ ] |

### Non-Functional Criteria

| # | Criterion | Verified |
|---|-----------|----------|
| NFC-1 | Schema validation completes in < 1 second per file | [ ] |
| NFC-2 | Error messages identify the specific field and constraint violated | [ ] |
| NFC-3 | Schema uses JSON Schema Draft 2020-12 for consistency with existing schemas | [ ] |

---

## MVP Definition

### In Scope (MVP)

- Agent frontmatter schema (claude-code-frontmatter-v1.schema.json) refinement
- Skill frontmatter schema (claude-code-skill-frontmatter-v1.schema.json) refinement
- Research artifacts with source citations
- Security review findings
- C4 adversarial review

### Out of Scope (Future)

- Agent governance schema (agent-governance-v1.schema.json) — Jerry-specific, not Anthropic-sourced
- Automated CI validation pipeline (separate enabler)
- VS Code / IDE schema integration (separate feature)
- settings.json schema refinement (separate effort)

---

## Children Stories/Enablers

### Story/Enabler Inventory

| ID | Type | Title | Status | Priority | Effort |
|----|------|-------|--------|----------|--------|
| STORY-001 | Story | Research Anthropic Official Agent Definition Schema | completed | high | 5 |
| STORY-002 | Story | Research Anthropic Official Skill Definition Schema | completed | high | 5 |
| STORY-003 | Story | Gap Analysis and Schema Refinement | completed | high | 8 |
| STORY-004 | Story | Schema Remediation from C4 Review Findings | pending | high | 3 |
| EN-001 | Enabler | Security Review of Schema Validation Pipeline | completed | high | 5 |
| EN-002 | Enabler | Developer Experience Review of Schema Validation | completed | medium | 3 |
| EN-003 | Enabler | Schema Validation Test Suite | pending | high | 5 |

### Work Item Links

- [STORY-001: Research Anthropic Official Agent Definition Schema](./STORY-001-research-agent-schema/STORY-001-research-agent-schema.md)
- [STORY-002: Research Anthropic Official Skill Definition Schema](./STORY-002-research-skill-schema/STORY-002-research-skill-schema.md)
- [STORY-003: Gap Analysis and Schema Refinement](./STORY-003-gap-analysis-refinement/STORY-003-gap-analysis-refinement.md)
- [STORY-004: Schema Remediation from C4 Review Findings](./STORY-004-schema-remediation/STORY-004-schema-remediation.md)
- [EN-001: Security Review of Schema Validation Pipeline](./EN-001-security-review/EN-001-security-review.md)
- [EN-002: Developer Experience Review of Schema Validation](./EN-002-developer-experience-review/EN-002-developer-experience-review.md)
- [EN-003: Schema Validation Test Suite](./EN-003-validation-test-suite/EN-003-validation-test-suite.md)

---

## Progress Summary

```
+------------------------------------------------------------------+
|                   FEATURE PROGRESS TRACKER                        |
+------------------------------------------------------------------+
| Stories:   [####................] 20% (0/3 completed)             |
| Enablers:  [....................] 0% (0/2 completed)              |
+------------------------------------------------------------------+
| Overall:   [###.................] 15%                              |
+------------------------------------------------------------------+
```

### Progress Metrics

| Metric | Value |
|--------|-------|
| **Total Stories** | 3 |
| **Completed Stories** | 0 |
| **Total Enablers** | 2 |
| **Completed Enablers** | 0 |
| **Total Effort (points)** | 26 |
| **Completed Effort** | 0 |
| **Completion %** | 15% |

---

## Related Items

### Hierarchy

- **Parent Epic:** [EPIC-001: Claude Code Schema Validation](../EPIC-001-schema-validation.md)

### Dependencies

| Dependency Type | Item | Description |
|----------------|------|-------------|
| Depends On | Anthropic docs | Official Claude Code documentation must be accessible |
| Blocks | H-34 enforcement | Refined schemas needed for CI validation pipeline |

---

## History

| Date | Author | Status | Notes |
|------|--------|--------|-------|
| 2026-03-26 | adam.nowak | in_progress | Feature created; STORY-001 and STORY-002 research launched in parallel |
