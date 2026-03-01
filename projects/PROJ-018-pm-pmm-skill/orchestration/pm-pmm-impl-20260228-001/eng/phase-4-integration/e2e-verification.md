# End-to-End Verification Checklist

<!-- VERSION: 1.0.0 | DATE: 2026-03-01 | SOURCE: PROJ-018, Phase 4 Integration | AGENT: eng-phase-4 -->

> Comprehensive verification checklist for the `/pm-pmm` skill deployment. Covers file existence, schema validation, constitutional compliance, SKILL.md integrity, template completeness, cross-agent data flow integrity, sensitivity cascade, trigger map collision checking, and integration point verification.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Verification Summary](#verification-summary) | Pass/fail overview across all categories |
| [V1: File Existence Checks](#v1-file-existence-checks) | All 26+ files in correct locations |
| [V2: Schema Validation](#v2-schema-validation) | Governance YAMLs pass JSON Schema |
| [V3: Constitutional Compliance](#v3-constitutional-compliance) | P-003/P-020/P-022 in all agents |
| [V4: SKILL.md Integrity](#v4-skillmd-integrity) | Agent registry, keywords, line count |
| [V5: Template Completeness](#v5-template-completeness) | All 15 templates with correct frontmatter |
| [V6: Cross-Agent Data Flow Integrity](#v6-cross-agent-data-flow-integrity) | All flows have defined source and consumer |
| [V7: Sensitivity Cascade](#v7-sensitivity-cascade) | Restricted stays restricted through handoff chains |
| [V8: Trigger Map Collision Check](#v8-trigger-map-collision-check) | No false positives against existing skills |
| [V9: Integration Point Verification](#v9-integration-point-verification) | All 6 integration points verified |
| [V10: H-23 Navigation Table Compliance](#v10-h-23-navigation-table-compliance) | All files have navigation tables |
| [V11: Caveats and Known Gaps](#v11-caveats-and-known-gaps) | Items that do not block but require tracking |

---

## Verification Summary

| Category | Checks | Expected Result |
|----------|--------|-----------------|
| V1: File Existence | 26 files + 15 runtime dirs | All present |
| V2: Schema Validation | 5 governance YAMLs | 0 errors each |
| V3: Constitutional Compliance | 5 agents x 5 checks | 25/25 pass |
| V4: SKILL.md Integrity | 8 checks | 8/8 pass |
| V5: Template Completeness | 15 templates x 4 checks | 60/60 pass |
| V6: Cross-Agent Data Flow | 8 flows | 8/8 defined |
| V7: Sensitivity Cascade | 4 cascade paths | 4/4 compliant |
| V8: Trigger Map Collision | 10 existing skills | 0 false positives |
| V9: Integration Points | 6 integration points | 6/6 verified |
| V10: H-23 Compliance | 6 primary files | 6/6 have nav tables |
| V11: Caveats | 7 tracked | Non-blocking |

---

## V1: File Existence Checks

### Core Skill Files (11 files)

| # | File Path (Production) | Type | Status |
|---|----------------------|------|--------|
| 1 | `skills/pm-pmm/SKILL.md` | Skill definition | [ ] Verified |
| 2 | `skills/pm-pmm/agents/pm-product-strategist.md` | Agent definition | [ ] Verified |
| 3 | `skills/pm-pmm/agents/pm-product-strategist.governance.yaml` | Governance YAML | [ ] Verified |
| 4 | `skills/pm-pmm/agents/pm-customer-insight.md` | Agent definition | [ ] Verified |
| 5 | `skills/pm-pmm/agents/pm-customer-insight.governance.yaml` | Governance YAML | [ ] Verified |
| 6 | `skills/pm-pmm/agents/pm-market-strategist.md` | Agent definition | [ ] Verified |
| 7 | `skills/pm-pmm/agents/pm-market-strategist.governance.yaml` | Governance YAML | [ ] Verified |
| 8 | `skills/pm-pmm/agents/pm-business-analyst.md` | Agent definition | [ ] Verified |
| 9 | `skills/pm-pmm/agents/pm-business-analyst.governance.yaml` | Governance YAML | [ ] Verified |
| 10 | `skills/pm-pmm/agents/pm-competitive-analyst.md` | Agent definition | [ ] Verified |
| 11 | `skills/pm-pmm/agents/pm-competitive-analyst.governance.yaml` | Governance YAML | [ ] Verified |

### Template Files (15 files)

| # | File Path (Production) | Artifact Type | Owner Agent |
|---|----------------------|---------------|-------------|
| 12 | `skills/pm-pmm/templates/01-prd.template.md` | PRD | pm-product-strategist |
| 13 | `skills/pm-pmm/templates/02-product-vision.template.md` | Product Vision | pm-product-strategist |
| 14 | `skills/pm-pmm/templates/03-roadmap.template.md` | Roadmap | pm-product-strategist |
| 15 | `skills/pm-pmm/templates/04-use-cases.template.md` | Use Cases | pm-product-strategist |
| 16 | `skills/pm-pmm/templates/05-personas.template.md` | User Personas | pm-customer-insight |
| 17 | `skills/pm-pmm/templates/06-journey-maps.template.md` | Journey Maps | pm-customer-insight |
| 18 | `skills/pm-pmm/templates/07-voc-analysis.template.md` | VOC Analysis | pm-customer-insight |
| 19 | `skills/pm-pmm/templates/08-business-case.template.md` | Business Case | pm-business-analyst |
| 20 | `skills/pm-pmm/templates/09-market-sizing.template.md` | Market Sizing | pm-business-analyst |
| 21 | `skills/pm-pmm/templates/10-competitive-analysis.template.md` | Competitive Analysis | pm-competitive-analyst |
| 22 | `skills/pm-pmm/templates/11-battle-cards.template.md` | Battle Cards | pm-competitive-analyst |
| 23 | `skills/pm-pmm/templates/12-win-loss-analysis.template.md` | Win/Loss Analysis | pm-competitive-analyst |
| 24 | `skills/pm-pmm/templates/13-gtm-plan.template.md` | GTM Plan | pm-market-strategist |
| 25 | `skills/pm-pmm/templates/14-mrd.template.md` | MRD | pm-market-strategist |
| 26 | `skills/pm-pmm/templates/15-buyer-personas.template.md` | Buyer Personas | pm-market-strategist |

### Runtime Artifact Directories (15 directories)

| # | Directory Path | For Artifact Type |
|---|---------------|-------------------|
| 27 | `docs/pm-pmm/prd/` | PRD |
| 28 | `docs/pm-pmm/product-vision/` | Product Vision |
| 29 | `docs/pm-pmm/roadmap/` | Roadmap |
| 30 | `docs/pm-pmm/use-cases/` | Use Cases |
| 31 | `docs/pm-pmm/personas/` | User Personas |
| 32 | `docs/pm-pmm/journey-maps/` | Journey Maps |
| 33 | `docs/pm-pmm/voc/` | VOC Reports |
| 34 | `docs/pm-pmm/business-case/` | Business Case |
| 35 | `docs/pm-pmm/market-sizing/` | Market Sizing |
| 36 | `docs/pm-pmm/competitive-analysis/` | Competitive Analysis |
| 37 | `docs/pm-pmm/battle-cards/` | Battle Cards |
| 38 | `docs/pm-pmm/win-loss/` | Win/Loss Analysis |
| 39 | `docs/pm-pmm/gtm-plan/` | GTM Plan |
| 40 | `docs/pm-pmm/mrd/` | MRD |
| 41 | `docs/pm-pmm/buyer-personas/` | Buyer Personas |

### Registration Files (3 files modified)

| # | File Path | Modification | Status |
|---|----------|-------------|--------|
| 42 | `CLAUDE.md` | `/pm-pmm` row in Skills table | [ ] Verified |
| 43 | `AGENTS.md` | 5 agent entries added | [ ] Verified |
| 44 | `.context/rules/mandatory-skill-usage.md` | Trigger map entry + H-22 text + L2-REINJECT | [ ] Verified |

### AGENTS.md Content Verification

All 5 pm-pmm agent entries must exist in `AGENTS.md` with correct model assignments.

| # | Agent Name | Expected Model | Status |
|---|-----------|---------------|--------|
| A1 | pm-product-strategist | opus | [ ] Verified |
| A2 | pm-customer-insight | opus | [ ] Verified |
| A3 | pm-market-strategist | opus | [ ] Verified |
| A4 | pm-business-analyst | sonnet | [ ] Verified |
| A5 | pm-competitive-analyst | sonnet | [ ] Verified |

```bash
# Verify all 5 agent entries exist with correct model assignments
echo "=== AGENTS.md Verification ==="
for agent_model in \
  "pm-product-strategist:opus" \
  "pm-customer-insight:opus" \
  "pm-market-strategist:opus" \
  "pm-business-analyst:sonnet" \
  "pm-competitive-analyst:sonnet"; do
  agent="${agent_model%%:*}"
  model="${agent_model##*:}"
  if grep -q "$agent" AGENTS.md; then
    if grep -A5 "$agent" AGENTS.md | grep -q "$model"; then
      echo "PASS: $agent (model: $model)"
    else
      echo "FAIL: $agent exists but model mismatch (expected: $model)"
    fi
  else
    echo "FAIL: $agent not found in AGENTS.md"
  fi
done
```

### Verification Command

```bash
# Run after deployment to verify all file existence checks
echo "=== Core Files ==="
for f in \
  skills/pm-pmm/SKILL.md \
  skills/pm-pmm/agents/pm-product-strategist.md \
  skills/pm-pmm/agents/pm-product-strategist.governance.yaml \
  skills/pm-pmm/agents/pm-customer-insight.md \
  skills/pm-pmm/agents/pm-customer-insight.governance.yaml \
  skills/pm-pmm/agents/pm-market-strategist.md \
  skills/pm-pmm/agents/pm-market-strategist.governance.yaml \
  skills/pm-pmm/agents/pm-business-analyst.md \
  skills/pm-pmm/agents/pm-business-analyst.governance.yaml \
  skills/pm-pmm/agents/pm-competitive-analyst.md \
  skills/pm-pmm/agents/pm-competitive-analyst.governance.yaml; do
  test -f "$f" && echo "PASS: $f" || echo "FAIL: $f"
done

echo "=== Templates ==="
template_count=$(ls skills/pm-pmm/templates/*.template.md 2>/dev/null | wc -l)
echo "Template count: $template_count (expected: 15)"

echo "=== Runtime Dirs ==="
dir_count=$(ls -d docs/pm-pmm/*/ 2>/dev/null | wc -l)
echo "Runtime dir count: $dir_count (expected: 15)"

echo "=== Registrations ==="
grep -q '/pm-pmm' CLAUDE.md && echo "PASS: CLAUDE.md" || echo "FAIL: CLAUDE.md"
grep -q '/pm-pmm' .context/rules/mandatory-skill-usage.md && echo "PASS: mandatory-skill-usage.md" || echo "FAIL: mandatory-skill-usage.md"
```

---

## V2: Schema Validation

All 5 governance YAML files must validate against `docs/schemas/agent-governance-v1.schema.json`.

### Per-File Validation

| # | File | Required Fields Check | Schema Validation | Status |
|---|------|-----------------------|-------------------|--------|
| 1 | `pm-product-strategist.governance.yaml` | version, tool_tier, identity.role, identity.expertise (>=2), identity.cognitive_mode | [ ] Pass | [ ] Verified |
| 2 | `pm-customer-insight.governance.yaml` | version, tool_tier, identity.role, identity.expertise (>=2), identity.cognitive_mode | [ ] Pass | [ ] Verified |
| 3 | `pm-market-strategist.governance.yaml` | version, tool_tier, identity.role, identity.expertise (>=2), identity.cognitive_mode | [ ] Pass | [ ] Verified |
| 4 | `pm-business-analyst.governance.yaml` | version, tool_tier, identity.role, identity.expertise (>=2), identity.cognitive_mode | [ ] Pass | [ ] Verified |
| 5 | `pm-competitive-analyst.governance.yaml` | version, tool_tier, identity.role, identity.expertise (>=2), identity.cognitive_mode | [ ] Pass | [ ] Verified |

### Field-Level Checks (All Agents)

| Field | Expected Pattern | Check |
|-------|-----------------|-------|
| `version` | `^\d+\.\d+\.\d+$` | "1.0.0" in all 5 files |
| `tool_tier` | `T1\|T2\|T3\|T4\|T5` | "T3" in all 5 files |
| `identity.cognitive_mode` | `divergent\|convergent\|integrative\|systematic\|forensic` | Valid mode in all 5 files |
| `identity.expertise` | Array, minItems 2 | >= 5 entries in all 5 files |
| `capabilities.forbidden_actions` | Array, minItems 3 | >= 5 entries in all 5 files |
| `constitution.principles_applied` | Array, includes P-003, P-020, P-022 | All 3 present in all 5 files |
| `output.required` | boolean | `true` in all 5 files |
| `output.levels` | Array including L0, L1, L2 | All 3 levels in all 5 files |

---

## V3: Constitutional Compliance

### P-003 (No Recursive Subagents) -- 5 Checks

| # | Agent | Governance YAML Check | .md File Check | Status |
|---|-------|----------------------|----------------|--------|
| 1 | pm-product-strategist | P-003 in principles_applied | Task NOT in tools frontmatter | [ ] Verified |
| 2 | pm-customer-insight | P-003 in principles_applied | Task NOT in tools frontmatter | [ ] Verified |
| 3 | pm-market-strategist | P-003 in principles_applied | Task NOT in tools frontmatter | [ ] Verified |
| 4 | pm-business-analyst | P-003 in principles_applied | Task NOT in tools frontmatter | [ ] Verified |
| 5 | pm-competitive-analyst | P-003 in principles_applied | Task NOT in tools frontmatter | [ ] Verified |

### P-020 (User Authority) -- 5 Checks

| # | Agent | Governance YAML Check | .md Guardrails Check | Status |
|---|-------|----------------------|---------------------|--------|
| 1 | pm-product-strategist | P-020 in principles_applied | "Never override user decisions" in guardrails | [ ] Verified |
| 2 | pm-customer-insight | P-020 in principles_applied | "Never override user decisions" in guardrails | [ ] Verified |
| 3 | pm-market-strategist | P-020 in principles_applied | "Never override user decisions" in guardrails | [ ] Verified |
| 4 | pm-business-analyst | P-020 in principles_applied | "Never override user decisions" in guardrails | [ ] Verified |
| 5 | pm-competitive-analyst | P-020 in principles_applied | "Never override user decisions" in guardrails | [ ] Verified |

### P-022 (No Deception) -- 5 Checks

| # | Agent | Governance YAML Check | .md Guardrails Check | Status |
|---|-------|----------------------|---------------------|--------|
| 1 | pm-product-strategist | P-022 in principles_applied | "Never misrepresent confidence" in guardrails | [ ] Verified |
| 2 | pm-customer-insight | P-022 in principles_applied | "Never misrepresent confidence" in guardrails | [ ] Verified |
| 3 | pm-market-strategist | P-022 in principles_applied | "Never misrepresent product-market fit" in guardrails | [ ] Verified |
| 4 | pm-business-analyst | P-022 in principles_applied | "Never misrepresent financial projections" in guardrails | [ ] Verified |
| 5 | pm-competitive-analyst | P-022 in principles_applied | "Never misrepresent competitive position" in guardrails | [ ] Verified |

### Additional Principles (P-001, P-002, P-011)

| Principle | Check | Expected |
|-----------|-------|----------|
| P-001 (Truth/Accuracy) | Present in all 5 governance YAMLs | 5/5 |
| P-002 (File Persistence) | Present in at least 4 governance YAMLs (pm-competitive-analyst has P-001, P-011 but uses P-002 in .md body) | >= 4/5 |
| P-011 (Evidence-Based) | Present in all 5 governance YAMLs | 5/5 |

### Worker Agent Constraint

| Check | Method | Expected |
|-------|--------|----------|
| No agent has `Task` in tools | Grep all .md frontmatter `tools:` sections for "Task" | 0 matches |
| No agent is T5 tier | Grep all .governance.yaml for `tool_tier: "T5"` | 0 matches |
| All agents are T3 tier | Grep all .governance.yaml for `tool_tier: "T3"` | 5 matches |

---

## V4: SKILL.md Integrity

| # | Check | Method | Expected | Status |
|---|-------|--------|----------|--------|
| 1 | Agent registry matches actual files | Compare Available Agents table (5 entries) with files in agents/ (5 .md files) | Exact match: pm-product-strategist, pm-customer-insight, pm-market-strategist, pm-business-analyst, pm-competitive-analyst | [ ] Verified |
| 2 | Agent model assignments correct | Cross-reference SKILL.md model column with .md frontmatter `model:` | Tier 1 = opus (3 agents), Tier 2 = sonnet (2 agents) | [ ] Verified |
| 3 | Activation-keywords count | Count items in SKILL.md frontmatter `activation-keywords` array | >= 60 keywords | [ ] Verified |
| 4 | Line count within budget | `wc -l skills/pm-pmm/SKILL.md` | < 600 lines | [ ] Verified |
| 5 | Navigation table present (H-23) | Check for `\| Section \| Purpose \|` table | Present after frontmatter | [ ] Verified |
| 6 | Triple-lens audience table present | Check for L0/L1/L2 audience table | Present with ELI5/Engineer/Architect levels | [ ] Verified |
| 7 | Framework catalog lists 18 primary frameworks | Count framework rows in Framework Catalog tables | 18 primary (6+4+3+3+3, with JTBD shared) | [ ] Verified |
| 8 | Artifact Ownership Matrix lists 15 artifacts | Count rows in Artifact Ownership Matrix | 15 artifacts with zero ownership overlap | [ ] Verified |

### Agent Registry Cross-Reference

| Agent in SKILL.md | .md File Exists | .governance.yaml Exists | Model Match | Tier Match |
|--------------------|----------------|------------------------|-------------|------------|
| pm-product-strategist | [ ] | [ ] | opus / opus | Tier 1 / Tier 1 |
| pm-customer-insight | [ ] | [ ] | opus / opus | Tier 1 / Tier 1 |
| pm-market-strategist | [ ] | [ ] | opus / opus | Tier 1 / Tier 1 |
| pm-business-analyst | [ ] | [ ] | sonnet / sonnet | Tier 2 / Tier 2 |
| pm-competitive-analyst | [ ] | [ ] | sonnet / sonnet | Tier 2 / Tier 2 |

---

## V5: Template Completeness

### Per-Template Checks

All 15 templates must have valid frontmatter with required fields.

| # | Template | Has `id` | Has `type` | Has `agent` | Has `status` | All 11 Fields | Status |
|---|----------|----------|-----------|-------------|-------------|---------------|--------|
| 1 | 01-prd.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 2 | 02-product-vision.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 3 | 03-roadmap.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 4 | 04-use-cases.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 5 | 05-personas.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 6 | 06-journey-maps.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 7 | 07-voc-analysis.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 8 | 08-business-case.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 9 | 09-market-sizing.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 10 | 10-competitive-analysis.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 11 | 11-battle-cards.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 12 | 12-win-loss-analysis.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 13 | 13-gtm-plan.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 14 | 14-mrd.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |
| 15 | 15-buyer-personas.template.md | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] Verified |

### Full Frontmatter Field Verification Command

All 11 required frontmatter fields must be present in each template. Run the following command to verify:

```bash
# Verify all 11 required frontmatter fields exist in each template
REQUIRED_FIELDS="id type agent status mode risk_domain sensitivity created last_validated frameworks_applied cross_refs"
echo "=== Template Frontmatter Verification (11 fields) ==="
for template in skills/pm-pmm/templates/*.template.md; do
  name=$(basename "$template")
  missing=""
  for field in $REQUIRED_FIELDS; do
    if ! grep -q "^${field}:" "$template" 2>/dev/null && \
       ! grep -q "^  ${field}:" "$template" 2>/dev/null && \
       ! grep -q "\"${field}\":" "$template" 2>/dev/null; then
      missing="$missing $field"
    fi
  done
  if [ -z "$missing" ]; then
    echo "PASS: $name (11/11 fields)"
  else
    echo "FAIL: $name -- missing:$missing"
  fi
done
```

### Template-to-Agent Assignment Verification

| Template | Expected Agent | Expected Artifact Type | Expected Sensitivity Default |
|----------|---------------|----------------------|----------------------------|
| 01-prd | pm-product-strategist | prd | internal |
| 02-product-vision | pm-product-strategist | product-vision | internal |
| 03-roadmap | pm-product-strategist | roadmap | internal |
| 04-use-cases | pm-product-strategist | use-cases | internal |
| 05-personas | pm-customer-insight | personas | confidential |
| 06-journey-maps | pm-customer-insight | journey-maps | confidential |
| 07-voc-analysis | pm-customer-insight | voc | confidential |
| 08-business-case | pm-business-analyst | business-case | restricted |
| 09-market-sizing | pm-business-analyst | market-sizing | restricted |
| 10-competitive-analysis | pm-competitive-analyst | competitive-analysis | restricted |
| 11-battle-cards | pm-competitive-analyst | battle-cards | restricted |
| 12-win-loss-analysis | pm-competitive-analyst | win-loss | restricted |
| 13-gtm-plan | pm-market-strategist | gtm-plan | internal |
| 14-mrd | pm-market-strategist | mrd | internal |
| 15-buyer-personas | pm-market-strategist | buyer-personas | internal |

### Template Frontmatter Required Fields

Each template must include these frontmatter fields as placeholders for runtime population:

| Field | Template Value | Runtime Value |
|-------|---------------|---------------|
| `id` | `PM-{XX}-NNN` | `PM-PS-001`, `PM-CI-002`, etc. |
| `type` | Artifact type slug | `prd`, `personas`, `battle-cards`, etc. |
| `agent` | Agent name | `pm-product-strategist`, etc. |
| `status` | `draft` | `draft` -> `discovery` -> `delivery` -> `final` |
| `mode` | `discovery` | `discovery` or `delivery` |
| `risk_domain` | Agent's risk domain | `value-risk` or `business-viability-risk` |
| `sensitivity` | Agent's default | `internal`, `confidential`, or `restricted` |
| `created` | `YYYY-MM-DD` | Actual creation date |
| `last_validated` | `YYYY-MM-DD` | Date of last review |
| `frameworks_applied` | Empty array | Populated by agent at runtime |
| `cross_refs` | Empty array | Populated with related artifact IDs |

---

## V6: Cross-Agent Data Flow Integrity

All 8 data flows defined in the architecture must have clearly identified source agent, consumer agent, data type, and mechanism.

| # | From Agent | To Agent | Data | Mechanism | Defined in SKILL.md | Defined in Architecture | Status |
|---|-----------|----------|------|-----------|---------------------|-------------------------|--------|
| 1 | pm-customer-insight | pm-product-strategist | Persona file paths, VOC themes, JTBD statements | File paths in handoff artifacts array | [ ] | [ ] | [ ] Verified |
| 2 | pm-customer-insight | pm-market-strategist | User persona references for buyer-user alignment | cross_refs frontmatter | [ ] | [ ] | [ ] Verified |
| 3 | pm-competitive-analyst | pm-market-strategist | Competitive positioning, battle card references | File paths in handoff | [ ] | [ ] | [ ] Verified |
| 4 | pm-competitive-analyst | pm-business-analyst | Competitive pricing data, market share estimates | Orchestrator passes file paths | [ ] | [ ] | [ ] Verified |
| 5 | pm-business-analyst | pm-product-strategist | Market sizing, feasibility verdict | cross_refs frontmatter | [ ] | [ ] | [ ] Verified |
| 6 | pm-business-analyst | pm-market-strategist | Pricing model, packaging recommendations | Orchestrator passes file paths | [ ] | [ ] | [ ] Verified |
| 7 | pm-product-strategist | pm-market-strategist | Product strategy, feature differentiation | cross_refs frontmatter | [ ] | [ ] | [ ] Verified |
| 8 | pm-product-strategist | pm-business-analyst | Product scope, investment estimation inputs | Orchestrator passes file paths | [ ] | [ ] | [ ] Verified |

### Data Flow Validation Rules

| Rule | Check | Expected |
|------|-------|----------|
| DF-01 | Every flow has a producing agent with the data in its output scope | All 8 source agents produce the stated data |
| DF-02 | Every flow has a consuming agent with the data in its input scope | All 8 consumer agents accept the stated data |
| DF-03 | No circular dependencies exist | No agent A -> B -> A cycle without intermediate user intervention |
| DF-04 | Financial data flows use directional indicators, not exact figures | Flows from pm-business-analyst use ranges/directions per TH-005 |
| DF-05 | Confidential data flows use summarization, not verbatim content | Flows from pm-customer-insight summarize rather than reproduce per TH-003 |

---

## V7: Sensitivity Cascade

The sensitivity cascade ensures that data classified at a higher sensitivity level does not leak to lower-sensitivity artifacts through handoff chains.

### Sensitivity Defaults by Agent

| Agent | Default Sensitivity | Artifacts |
|-------|-------------------|-----------|
| pm-product-strategist | `internal` | PRD, Product Vision, Roadmap, Use Cases |
| pm-customer-insight | `confidential` | User Personas, Journey Maps, VOC |
| pm-business-analyst | `restricted` | Business Case, Market Sizing |
| pm-competitive-analyst | `restricted` | Competitive Analysis, Battle Cards, Win/Loss |
| pm-market-strategist | `internal` | GTM Plan, MRD, Buyer Personas |

### Cascade Path Verification

| # | Cascade Path | Source Sensitivity | Consumer Sensitivity | Rule | Status |
|---|-------------|-------------------|---------------------|------|--------|
| 1 | pm-customer-insight -> pm-product-strategist | confidential | internal | Summarize, do not reproduce verbatim (TH-003). PRD references persona IDs but does not include PII or verbatim customer quotes. | [ ] Verified |
| 2 | pm-business-analyst -> pm-product-strategist | restricted | internal | Financial figures presented as ranges/directions, not exact values (TH-005). PRD references market size as "~$X-Y billion" not exact projections. | [ ] Verified |
| 3 | pm-competitive-analyst -> pm-market-strategist | restricted | internal | Competitive data summarized for positioning context. GTM plan references competitive themes, not full battle card content (TH-005). | [ ] Verified |
| 4 | pm-competitive-analyst -> pm-business-analyst | restricted | restricted | Same sensitivity level. Competitive pricing data can flow directly. Sensitivity maintained. | [ ] Verified |

### Non-Downgrade Rules Verification

| Agent | Guardrail | Governance YAML Entry | .md Guardrails Section | Status |
|-------|-----------|----------------------|----------------------|--------|
| pm-product-strategist | Cannot reproduce confidential content verbatim | `sensitivity_non_downgrade_enforcement_for_confidential_sources` | TH-005 in output filtering | [ ] Verified |
| pm-customer-insight | Cannot downgrade below confidential | `sensitivity_default_confidential_no_downgrade_without_user_override` | Sensitivity default enforcement | [ ] Verified |
| pm-business-analyst | Cannot downgrade below restricted | `sensitivity_default_restricted_no_downgrade_without_user_override` | SEC-028 in output filtering | [ ] Verified |
| pm-competitive-analyst | Cannot downgrade below restricted | `sensitivity_default_restricted_no_downgrade_without_user_override` | SEC-044 in output filtering | [ ] Verified |
| pm-market-strategist | Cannot reproduce confidential/restricted content verbatim | `competitive_intelligence_summarized_not_quoted_verbatim` | TH-005 in output filtering | [ ] Verified |

---

## V8: Trigger Map Collision Check

Verify that the `/pm-pmm` trigger map entry does not produce false positives against any of the 10 existing skills plus `/pm-pmm` itself.

### False Positive Test Cases

| # | Test Request | Expected Skill | /pm-pmm Triggers? | Reason |
|---|-------------|---------------|-------------------|--------|
| 1 | "Review this code for security vulnerabilities" | /eng-team | No | "code review" is negative keyword |
| 2 | "Create an ADR for our database migration" | /architecture | No | "architecture" and "ADR" are negative keywords |
| 3 | "Run adversarial quality review on this document" | /adversary | No | "adversarial" is negative keyword |
| 4 | "Parse this VTT meeting recording" | /transcript | No | "transcript" and "VTT" are negative keywords |
| 5 | "Run a penetration test on the production API" | /red-team | No | "penetration test" is negative keyword |
| 6 | "Break this project into 4 phases with quality gates" | /orchestration | No | No /pm-pmm keywords match |
| 7 | "Estimate AWS infrastructure pricing for our cluster" | /eng-team | No | "infrastructure pricing" is negative keyword |
| 8 | "Investigate why our deployment pipeline failed" | /problem-solving | No | "deployment" is negative keyword |
| 9 | "Talk like mcconkey and roast this code" | /saucer-boy | No | No /pm-pmm keywords match |
| 10 | "Check this entity's frontmatter metadata" | /ast | No | No /pm-pmm keywords match |

### True Positive Test Cases

| # | Test Request | Expected Agent | Compound Trigger? | Matching Keywords |
|---|-------------|---------------|-------------------|-------------------|
| 1 | "Write a PRD for the onboarding feature" | pm-product-strategist | No | "PRD" |
| 2 | "Create product requirements for our API" | pm-product-strategist | Yes: "product requirements" | "product requirements" |
| 3 | "Build JTBD personas for platform engineers" | pm-customer-insight | No | "persona", "JTBD" |
| 4 | "Map the customer journey for enterprise onboarding" | pm-customer-insight | No | "journey map" |
| 5 | "Calculate TAM/SAM/SOM for the developer platform market" | pm-business-analyst | Yes: "market sizing" | "TAM", "SAM", "SOM", "market sizing" |
| 6 | "Analyze competitors using Porter's Five Forces" | pm-competitive-analyst | Yes: "competitive analysis" | "competitive analysis", "Porter's" |
| 7 | "Create a go-to-market plan for our launch" | pm-market-strategist | Yes: "go-to-market" | "go-to-market", "launch plan" |
| 8 | "Run Van Westendorp pricing analysis" | pm-business-analyst | No | "Van Westendorp", "pricing" |
| 9 | "Build battle cards for Backstage and Port" | pm-competitive-analyst | No | "battle card" |
| 10 | "Create buyer personas for the enterprise buying committee" | pm-market-strategist | Yes: "buyer persona" | "buyer persona" |

---

## V9: Integration Point Verification

All 6 integration points from the architecture document must be verified.

| # | Skill | Integration Type | Verification Check | Status |
|---|-------|-----------------|-------------------|--------|
| 1 | `/worktracker` | Bidirectional | Artifact IDs (PM-PS-001) can appear in worktracker cross_refs. Worktracker entity IDs (FEAT-042) can appear in artifact cross_refs. No file-level dependency. | [ ] Verified |
| 2 | `/adversary` | Unidirectional | PM/PMM artifacts at C2+ can be submitted for quality review. Criticality mapping defined per artifact ownership matrix (C1-C3). Minimum 3-iteration cycle per H-14. | [ ] Verified |
| 3 | `/problem-solving` | Unidirectional | Research artifacts from ps-researcher can be passed as input context to PM/PMM agents via handoff artifacts array. No reverse dependency. | [ ] Verified |
| 4 | `/architecture` | Bidirectional | ADR file paths can be referenced in PRD Technical Constraints section. Product requirements can be referenced in ADR Context section. Cross_refs enable bidirectional linking. | [ ] Verified |
| 5 | `/nasa-se` | Unidirectional | PRD requirements IDs can flow to SE verification. Requirements traceability established via cross_refs. No reverse dependency from /nasa-se to /pm-pmm. | [ ] Verified |
| 6 | `/use-case` | Unidirectional | pm-product-strategist use case file paths can be passed to /use-case skill for slicing. No reverse dependency. | [ ] Verified |

### Integration Point Validation Rules

| Rule | Check | Expected |
|------|-------|----------|
| IP-01 | No integration point introduces a circular dependency between skills | No skill A -> B -> A cycle |
| IP-02 | All bidirectional integrations use cross_refs (not direct agent invocation) | /worktracker and /architecture use file references only |
| IP-03 | All unidirectional integrations flow outward from /pm-pmm (except /problem-solving which flows in) | Data direction verified |
| IP-04 | No integration point violates P-003 (no agent invokes another skill's agent) | Main context mediates all cross-skill interactions |

---

## V10: H-23 Navigation Table Compliance

All primary files that are Claude-consumed markdown over 30 lines must include a navigation table.

| # | File | Lines | Navigation Table Present | Status |
|---|------|-------|-------------------------|--------|
| 1 | `skills/pm-pmm/SKILL.md` | ~532 | [ ] Present | [ ] Verified |
| 2 | `skills/pm-pmm/agents/pm-product-strategist.md` | ~440 | [ ] Present | [ ] Verified |
| 3 | `skills/pm-pmm/agents/pm-customer-insight.md` | ~413 | [ ] Present | [ ] Verified |
| 4 | `skills/pm-pmm/agents/pm-market-strategist.md` | ~391 | [ ] Present | [ ] Verified |
| 5 | `skills/pm-pmm/agents/pm-business-analyst.md` | ~439 | [ ] Present | [ ] Verified |
| 6 | `skills/pm-pmm/agents/pm-competitive-analyst.md` | ~456 | [ ] Present | [ ] Verified |

Governance YAML files are exempt from H-23 (pure data files, not markdown).

Template files are exempt if under 30 lines.

---

## V11: Caveats and Known Gaps

The following items are acknowledged from the Barrier 3 constraint check and quality handoff. They do NOT block deployment but must be tracked for post-deployment iteration.

| # | Caveat | Source | Severity | Tracking Action |
|---|--------|--------|----------|-----------------|
| 1 | 19 SEC defense-in-depth requirements not fully implemented (51/70 = 73% per final security assessment Section 4) | Barrier 3 constraint-check.md, sec/phase-4-final/final-security-assessment.md Section 4 | Medium | File security enabler for L3/L5 enforcement mechanisms |
| 2 | Narrative guardrail enforcement gap | Barrier 3 quality-to-eng handoff | Medium | Post-deployment: design deterministic guardrail checks |
| 3 | Provenance self-reporting (pm-competitive-analyst) | Barrier 3 constraint-check.md | Low | Post-deployment: design provenance audit workflow |
| 4 | pm-competitive-analyst.governance.yaml at 0.911 | Barrier 3 quality-to-eng handoff | Low | File improvement enabler; non-blocking (aggregate 0.920 passes H-13) |
| 5 | WebSearch query privacy (FM-18) | Barrier 3 constraint-check.md | Low | Accepted risk: documented in threat model |
| 6 | Paraphrase bypass of "no verbatim" restriction | Barrier 3 quality-to-eng handoff | Medium | Post-deployment: evaluate summarization quality |
| 7 | SKILL.md context budget (~532 lines) | Barrier 3 constraint-check.md | Low | Mitigated: triple-lens navigation enables selective section loading |

### Post-Deployment Improvement Backlog

| Priority | Item | Agent |
|----------|------|-------|
| P1 | L3 deterministic sensitivity field validation | All agents |
| P1 | L5 CI governance YAML schema validation on PR | All agents |
| P2 | Provenance audit workflow for competitive claims | pm-competitive-analyst |
| P2 | pm-competitive-analyst.governance.yaml output_filtering improvement | pm-competitive-analyst |
| P3 | SKILL.md progressive disclosure optimization | SKILL.md |
| P3 | WebSearch query sanitization pattern | All T3 agents |

---

*Verification Checklist Version: 1.0.0*
*Source: PROJ-018 PM/PMM Skill, Phase 4 Integration*
*Created: 2026-03-01*
