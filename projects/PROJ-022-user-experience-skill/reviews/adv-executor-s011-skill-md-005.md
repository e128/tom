# Chain-of-Verification Report: User-Experience SKILL.md

**Strategy:** S-011 Chain-of-Verification
**Deliverable:** `skills/user-experience/SKILL.md`
**Criticality:** C4
**Date:** 2026-03-03
**Reviewer:** adv-executor (S-011)
**H-16 Compliance:** S-003 Steelman applied in prior iterations (indirect for CoVe)
**Claims Extracted:** 18 | **Verified:** 13 | **Discrepancies:** 5 (1 Critical, 2 Major, 2 Minor)

---

## Summary

18 testable factual claims were extracted from `skills/user-experience/SKILL.md` and independently verified against source documents. 13 claims verified clean. 5 discrepancies found: 1 Critical (handoff schema file referenced but does not exist), 2 Major (T5 tool tier definition omits Memory-Keeper; ux-orchestrator.md stub missing Memory-Keeper tools per T5 specification), and 2 Minor (Goal-Signal-Metric singular vs. Goals-Signals-Metrics plural; HEART framework claim about tool abbreviation in ux-routing-rules). The Critical finding references a non-existent file in two locations. Correction required before acceptance.

---

## Findings Summary

| ID | Claim | Source | Discrepancy | Severity | Affected Dimension |
|----|-------|--------|-------------|----------|--------------------|
| CV-001-005 | `docs/schemas/handoff-v2.schema.json` referenced as the Jerry handoff protocol schema | Jerry codebase (`docs/schemas/`) | File does not exist; only `agent-governance-v1.schema.json`, `agent-definition-v1.schema.json`, `agent-canonical-v1.schema.json`, `session_context.json` exist | Critical | Traceability |
| CV-002-005 | T5 tier defined as "T3 + Task (orchestration delegation)" in tool tier key | `agent-development-standards.md` Tool Security Tiers table | Source defines T5 as "T3 + T4 + Task" (includes Memory-Keeper from T4); SKILL.md omits T4 layer | Major | Evidence Quality |
| CV-003-005 | ux-orchestrator.md frontmatter tools list does not include Memory-Keeper MCP tools | `agent-development-standards.md` T5 tier definition | T5 agents require T3 + T4 + Task; T4 adds Memory-Keeper; ux-orchestrator.md lists no Memory-Keeper tools despite being classified T5 | Major | Internal Consistency |
| CV-004-005 | "Goal-Signal-Metric framework" (singular) for HEART | `ux-frameworks-survey.md`, Google research | Source consistently says "Goals-Signals-Metrics (GSM)" (plural); SKILL.md uses singular form throughout | Minor | Evidence Quality |
| CV-005-005 | ux-routing-rules.md described as documenting "Handoff schema" | `skills/user-experience/rules/ux-routing-rules.md` | File is a STUB with section structure only; does not yet contain handoff schema documentation per SKILL.md section 481 | Minor | Traceability |

---

## Detailed Findings

### CV-001-005: Non-Existent Handoff Schema File Referenced [CRITICAL]

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Section** | Cross-Skill Integration (line 470); References > Standards References (line 617) |
| **Strategy Step** | Step 3: Independent Verification — source document unavailable |

**Evidence (from deliverable):**

Line 470: `Handoffs use the Jerry handoff protocol (\`docs/schemas/handoff-v2.schema.json\`) with UX-specific artifact types`

Line 617: `| Handoff Schema | \`docs/schemas/handoff-v2.schema.json\` |`

**Independent Verification:**

Glob of `docs/schemas/*` in the worktree returns:
```
docs/schemas/SCHEMA_VERSIONING.md
docs/schemas/SESSION_CONTEXT_GUIDE.md
docs/schemas/agent-canonical-v1.schema.json
docs/schemas/agent-definition-v1.schema.json
docs/schemas/agent-governance-v1.schema.json
docs/schemas/session_context.json
```

`handoff-v2.schema.json` is not present in `docs/schemas/`. The file does not exist.

**Discrepancy:** SKILL.md cites `docs/schemas/handoff-v2.schema.json` as the governing handoff schema and lists it in the Standards References table. The file does not exist. Users following the cross-sub-skill handoff protocol described in the SKILL.md will find a broken reference.

**Severity rationale:** Critical — the handoff schema governs inter-agent data contracts. A reference to a non-existent schema means the stated governance artifact is inaccessible. Any developer attempting to follow the handoff protocol will hit a broken reference. This undermines traceability and could cause incorrect handoff implementations.

**Dimension:** Traceability (0.10) — governance reference chain is broken.

**Correction:** Either (a) create `docs/schemas/handoff-v2.schema.json` (the schema is defined in `agent-development-standards.md` [Handoff Schema] section and requires only codification), or (b) update both references to the actual handoff schema defined inline in `agent-development-standards.md` Handoff Schema section with a note that no standalone file exists yet:

Replace line 470:
```
Handoffs use the Jerry handoff protocol (defined in `agent-development-standards.md` [Handoff Schema] section; `docs/schemas/handoff-v2.schema.json` is planned but not yet created) with UX-specific artifact types:
```

Replace line 617:
```
| Handoff Schema | `agent-development-standards.md` [Handoff Schema] (`docs/schemas/handoff-v2.schema.json` planned) |
```

---

### CV-002-005: T5 Tier Definition Omits T4 (Memory-Keeper) Layer [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | Available Agents — tool tier key (line 157) |
| **Strategy Step** | Step 4: Consistency Check — MATERIAL DISCREPANCY |

**Evidence (from deliverable):**

Line 157: `**Tool tier key:** T2 = Read-Write (Read, Write, Edit, Glob, Grep, Bash); T3 = T2 + External (WebSearch, WebFetch, Context7 MCP); T5 = T3 + Task (orchestration delegation).`

**Independent Verification:**

From `agent-development-standards.md` Tool Security Tiers table:

```
| T2 | Read-Write | T1 + Write, Edit, Bash | ...
| T3 | External   | T2 + WebSearch, WebFetch, Context7 | ...
| T4 | Persistent | T2 + Memory-Keeper | ...
| T5 | Full       | T3 + T4 + Task | Orchestration with delegation, full capability |
```

The authoritative source defines T5 as "T3 + T4 + Task" — which includes Memory-Keeper from T4.

**Discrepancy:** SKILL.md defines T5 as "T3 + Task" omitting the T4 layer. This mischaracterizes what T5 agents have access to, understates the capabilities of ux-orchestrator, and could lead sub-skill developers to omit Memory-Keeper from orchestrator coordination workflows.

**Dimension:** Evidence Quality (0.15) — the cited source defines T5 differently than stated.

**Correction:** Replace the T5 entry in line 157:

From: `T5 = T3 + Task (orchestration delegation)`

To: `T5 = T3 + T4 + Task (orchestration delegation with Memory-Keeper persistence)`

---

### CV-003-005: ux-orchestrator Stub Missing Memory-Keeper Tools [MAJOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Major |
| **Section** | P-003 Compliance / References — Agent Definition Files |
| **Strategy Step** | Step 3: Independent Verification |

**Evidence (from deliverable):**

Line 145: `| \`ux-orchestrator\` | Parent orchestrator: routing, wave gating, cross-framework synthesis | T5 | ...`
Line 157: T5 tier (even as stated in SKILL.md) includes at minimum T3 + Task.
The authoritative T5 definition (from CV-002 source) includes Memory-Keeper.

**Independent Verification:**

`skills/user-experience/agents/ux-orchestrator.md` frontmatter tools list:
```yaml
tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Task
  - WebSearch
  - WebFetch
```

No Memory-Keeper tools (`mcp__memory-keeper__store`, `mcp__memory-keeper__retrieve`, `mcp__memory-keeper__search`) are declared. The SKILL.md frontmatter `allowed-tools` (line 27) also does not include Memory-Keeper.

Per `agent-development-standards.md`: T5 = "T3 + T4 + Task". T4 adds Memory-Keeper. T5 orchestrators therefore should have Memory-Keeper access per the tier definition.

Per `mcp-tool-standards.md` MCP-002: "Memory-Keeper `store` MUST be called at orchestration phase boundaries." The ux-orchestrator manages wave transitions (orchestration phase boundaries) and should use Memory-Keeper for cross-session state.

**Discrepancy:** The ux-orchestrator.md stub is classified as T5 but does not declare Memory-Keeper tools. This is structurally incomplete relative to the T5 specification. The SKILL.md describes the orchestrator as managing wave state and cross-session coordination — use cases that T4 Memory-Keeper tools directly serve.

**Dimension:** Internal Consistency (0.20) — T5 classification is inconsistent with actual declared tool set.

**Correction:** Add Memory-Keeper tools to `skills/user-experience/agents/ux-orchestrator.md` frontmatter:

```yaml
tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Task
  - WebSearch
  - WebFetch
  - mcp__memory-keeper__store
  - mcp__memory-keeper__retrieve
  - mcp__memory-keeper__search
```

Also add Memory-Keeper to the SKILL.md `allowed-tools` list (line 27).

Note: This is a stub file to be fully implemented in EPIC-001. The correction should be tracked as a EPIC-001 implementation requirement.

---

### CV-004-005: HEART Framework Metric Name Singular vs. Plural [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Key Capabilities (line 100); Quick Reference agent selection hints (line 533) |
| **Strategy Step** | Step 4: Consistency Check — MINOR DISCREPANCY |

**Evidence (from deliverable):**

Line 100: `**HEART Metrics** -- Google's Goal-Signal-Metric framework for UX measurement (Wave 2)`
Line 533: `HEART, metrics, happiness, engagement, adoption, retention, task success, GSM, measurement`

**Independent Verification:**

From the upstream UX frameworks survey research (ux-frameworks-survey.md):
`"Core Principles: Uses Goals-Signals-Metrics (GSM) model"`
`"GSM model makes metrics actionable"`

The Google HEART framework uses "Goals-Signals-Metrics" (plural for all three components). SKILL.md uses "Goal-Signal-Metric" (singular). The plural form is the authoritative terminology used in the original framework documentation and the research backing.

**Discrepancy:** The singular form "Goal-Signal-Metric" is a minor paraphrase of the authoritative "Goals-Signals-Metrics." While the abbreviation "GSM" is correct and is included in the keyword hint, the expanded form is imprecise.

**Dimension:** Evidence Quality (0.15) — minor citation imprecision.

**Correction:** On line 100, change:
`Google's Goal-Signal-Metric framework for UX measurement`
to:
`Google's Goals-Signals-Metrics (GSM) framework for UX measurement`

---

### CV-005-005: ux-routing-rules.md Handoff Schema Claim Overstated for Stub [MINOR]

| Attribute | Value |
|-----------|-------|
| **Severity** | Minor |
| **Section** | Cross-Skill Integration (line 481) |
| **Strategy Step** | Step 3: Independent Verification — source is stub |

**Evidence (from deliverable):**

Line 481: `Handoff schema documented in \`skills/user-experience/rules/ux-routing-rules.md\`.`

**Independent Verification:**

`skills/user-experience/rules/ux-routing-rules.md` exists and the Rule Files table (line 579) correctly marks it as `[STUB: EPIC-001]`. The file exists as a stub with section structure and TODO markers.

**Discrepancy:** SKILL.md's Cross-Skill Integration section (line 481) states that the handoff schema is "documented in" ux-routing-rules.md without acknowledging the stub status. In contrast, the References section accurately marks it as `[STUB: EPIC-001]`. The prose claim overstates the current state — the schema is not yet documented there.

**Dimension:** Traceability (0.10) — minor inconsistency between prose claim and reference table annotation.

**Correction:** Update line 481 to be consistent with the References section:

From: `Handoff schema documented in \`skills/user-experience/rules/ux-routing-rules.md\`.`

To: `Handoff schema will be documented in \`skills/user-experience/rules/ux-routing-rules.md\` (currently [STUB: EPIC-001]).`

---

## Claim Inventory

| CL-ID | Claim Text | Source | Result |
|-------|-----------|--------|--------|
| CL-001 | `docs/schemas/handoff-v2.schema.json` as handoff protocol schema | Jerry codebase | MATERIAL DISCREPANCY (CV-001-005) |
| CL-002 | T5 = "T3 + Task" in tool tier key | `agent-development-standards.md` | MATERIAL DISCREPANCY (CV-002-005) |
| CL-003 | ux-orchestrator T5 tools include T3 + Task | `ux-orchestrator.md` frontmatter | MATERIAL DISCREPANCY (CV-003-005) |
| CL-004 | "Goal-Signal-Metric" as HEART framework name | `ux-frameworks-survey.md` | MINOR DISCREPANCY (CV-004-005) |
| CL-005 | Handoff schema documented in ux-routing-rules.md | `skills/user-experience/rules/ux-routing-rules.md` | MINOR DISCREPANCY (CV-005-005) |
| CL-006 | WCAG 2.2 / W3C / 2023 | Industry reference | VERIFIED |
| CL-007 | Nielsen's 10 Heuristics / 1994 (updated 2024) | Industry reference | VERIFIED |
| CL-008 | Fogg B=MAP / 2009 (B=MAP 2019) | Industry reference | VERIFIED |
| CL-009 | AJ&Smart Design Sprint 2.0 attribution | `comment-3-appendices.md` | VERIFIED |
| CL-010 | WSM >= 7.80 for AI-First Design enabler gate | `comment-3-appendices.md` framework scores | VERIFIED (7.80 confirmed) |
| CL-011 | S-014 composite >= 0.85 for wave transitions | `ADR-PROJ022-002-wave-criteria-gates.md` | VERIFIED (preliminary decision = 0.85) |
| CL-012 | ADR-PROJ022-001 status = "(DRAFT)" | `ADR-PROJ022-001-ux-skill-architecture.md` | VERIFIED |
| CL-013 | ADR-PROJ022-002 status = "(DRAFT)" | `ADR-PROJ022-002-wave-criteria-gates.md` | VERIFIED |
| CL-014 | Rule files listed as "[STUB: EPIC-001]" | `skills/user-experience/rules/*.md` | VERIFIED |
| CL-015 | Template files listed as "[STUB: EPIC-001]" | `skills/user-experience/templates/*.md` | VERIFIED |
| CL-016 | metrics-plan.md listed as "[PLANNED: EPIC-008]" | Codebase (file absent) | VERIFIED (absent, correctly marked PLANNED) |
| CL-017 | HEART framework: Kerry Rodden / Google / 2010 | `ux-frameworks-survey.md` | VERIFIED |
| CL-018 | 11 agents (1 orchestrator + 10 sub-skills) | YAML frontmatter agents list, Available Agents table | VERIFIED (11 entries consistent) |

**Verification rate:** 13/18 verified clean = 72.2%. 5 discrepancies (1 Critical, 2 Major, 2 Minor).

---

## Recommendations

### Critical (MUST correct before acceptance)

**CV-001-005 — Missing handoff-v2.schema.json:**
Either create `docs/schemas/handoff-v2.schema.json` based on the schema defined in `agent-development-standards.md` [Handoff Schema] section, OR update SKILL.md lines 470 and 617 to reference the inline schema definition and note the file is planned. Two-location correction required.

### Major (SHOULD correct)

**CV-002-005 — T5 definition incomplete:**
On line 157, change the T5 entry to: `T5 = T3 + T4 + Task (orchestration delegation with Memory-Keeper persistence)`.

**CV-003-005 — ux-orchestrator.md stub missing Memory-Keeper tools:**
Track as EPIC-001 implementation requirement. Add `mcp__memory-keeper__store`, `mcp__memory-keeper__retrieve`, `mcp__memory-keeper__search` to `skills/user-experience/agents/ux-orchestrator.md` frontmatter tools list and to SKILL.md `allowed-tools`.

### Minor (MAY correct)

**CV-004-005 — HEART GSM singular/plural:**
On line 100, change "Goal-Signal-Metric" to "Goals-Signals-Metrics (GSM)".

**CV-005-005 — Handoff schema stub acknowledgment:**
On line 481, add "(currently [STUB: EPIC-001])" qualifier to align with the References section annotation.

---

## Scoring Impact

| Dimension | Weight | Impact | Rationale |
|-----------|--------|--------|-----------|
| Completeness | 0.20 | Neutral | No claims about completeness are incorrect; all planned/stub annotations are accurate |
| Internal Consistency | 0.20 | Negative | CV-003-005: T5 classification of ux-orchestrator is inconsistent with the declared tool set; T5 claims Memory-Keeper but frontmatter omits it |
| Methodological Rigor | 0.20 | Neutral | Wave gate threshold (0.85), bypass criteria, and synthesis confidence gates are correctly described against source documents |
| Evidence Quality | 0.15 | Negative | CV-002-005: T5 definition contradicts authoritative source; CV-004-005: HEART framework terminology imprecise |
| Actionability | 0.15 | Negative | CV-001-005: Broken reference to non-existent schema blocks developers from implementing handoffs per the stated protocol |
| Traceability | 0.10 | Negative | CV-001-005: Two-location broken reference to non-existent governance artifact; CV-005-005: prose-reference inconsistency |

**Overall Assessment:** REVISE required. 1 Critical finding (broken schema reference at two locations) blocks clean acceptance. 2 Major findings (T5 definition error, stub tool gap) require correction. The Critical finding has a straightforward fix — either create the file or update both references to acknowledge the inline definition.

---

## Execution Statistics
- **Total Findings:** 5
- **Critical:** 1
- **Major:** 2
- **Minor:** 2
- **Protocol Steps Completed:** 5 of 5
- **Claims Extracted:** 18
- **Verified Clean:** 13 (72.2%)
- **Material Discrepancies:** 3 (CV-001 Critical, CV-002 Major, CV-003 Major)
- **Minor Discrepancies:** 2 (CV-004, CV-005)
- **Unverifiable:** 0
