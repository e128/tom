# Deployment Manifest

<!-- VERSION: 1.0.0 | DATE: 2026-03-01 | SOURCE: PROJ-018, Phase 4 Integration | AGENT: eng-phase-4 -->

> Comprehensive deployment manifest mapping all orchestration staging files to their production locations within `skills/pm-pmm/`. This manifest is the authoritative checklist for human-reviewed deployment.

## Document Sections

| Section | Purpose |
|---------|---------|
| [File Mapping Table](#file-mapping-table) | Source-to-destination mapping for all 21 core files |
| [Template File Mapping](#template-file-mapping) | All 15 artifact templates |
| [Registration Actions](#registration-actions) | CLAUDE.md, AGENTS.md, mandatory-skill-usage.md updates |
| [Runtime Directory Scaffolding](#runtime-directory-scaffolding) | Artifact output directories to create |
| [Pre-Deployment Checklist](#pre-deployment-checklist) | Validation steps before deployment |
| [Deployment Execution Steps](#deployment-execution-steps) | Ordered steps for human reviewer |
| [Post-Deployment Verification](#post-deployment-verification) | Verification steps after deployment |
| [Rollback Plan](#rollback-plan) | How to revert if deployment fails |
| [Caveats Carried from Barrier 3](#caveats-carried-from-barrier-3) | Known issues from prior phases |

---

## File Mapping Table

### SKILL.md (Skill Definition)

| # | Source (Orchestration) | Destination (Production) | Action |
|---|----------------------|--------------------------|--------|
| 1 | `eng/phase-2-tier1-agents/SKILL.md` | `skills/pm-pmm/SKILL.md` | Copy |

### Tier 1 Agent Definitions (3 agents, 6 files)

| # | Source (Orchestration) | Destination (Production) | Action |
|---|----------------------|--------------------------|--------|
| 2 | `eng/phase-2-tier1-agents/pm-product-strategist.md` | `skills/pm-pmm/agents/pm-product-strategist.md` | Copy |
| 3 | `eng/phase-2-tier1-agents/pm-product-strategist.governance.yaml` | `skills/pm-pmm/agents/pm-product-strategist.governance.yaml` | Copy |
| 4 | `eng/phase-2-tier1-agents/pm-customer-insight.md` | `skills/pm-pmm/agents/pm-customer-insight.md` | Copy |
| 5 | `eng/phase-2-tier1-agents/pm-customer-insight.governance.yaml` | `skills/pm-pmm/agents/pm-customer-insight.governance.yaml` | Copy |
| 6 | `eng/phase-2-tier1-agents/pm-market-strategist.md` | `skills/pm-pmm/agents/pm-market-strategist.md` | Copy |
| 7 | `eng/phase-2-tier1-agents/pm-market-strategist.governance.yaml` | `skills/pm-pmm/agents/pm-market-strategist.governance.yaml` | Copy |

### Tier 2 Agent Definitions (2 agents, 4 files)

| # | Source (Orchestration) | Destination (Production) | Action |
|---|----------------------|--------------------------|--------|
| 8 | `eng/phase-3-tier2-agents/pm-business-analyst.md` | `skills/pm-pmm/agents/pm-business-analyst.md` | Copy |
| 9 | `eng/phase-3-tier2-agents/pm-business-analyst.governance.yaml` | `skills/pm-pmm/agents/pm-business-analyst.governance.yaml` | Copy |
| 10 | `eng/phase-3-tier2-agents/pm-competitive-analyst.md` | `skills/pm-pmm/agents/pm-competitive-analyst.md` | Copy |
| 11 | `eng/phase-3-tier2-agents/pm-competitive-analyst.governance.yaml` | `skills/pm-pmm/agents/pm-competitive-analyst.governance.yaml` | Copy |

### Artifact Templates (15 files)

| # | Source (Orchestration) | Destination (Production) | Action |
|---|----------------------|--------------------------|--------|
| 12 | `eng/phase-1-research/templates/01-prd.template.md` | `skills/pm-pmm/templates/01-prd.template.md` | Copy |
| 13 | `eng/phase-1-research/templates/02-product-vision.template.md` | `skills/pm-pmm/templates/02-product-vision.template.md` | Copy |
| 14 | `eng/phase-1-research/templates/03-roadmap.template.md` | `skills/pm-pmm/templates/03-roadmap.template.md` | Copy |
| 15 | `eng/phase-1-research/templates/04-use-cases.template.md` | `skills/pm-pmm/templates/04-use-cases.template.md` | Copy |
| 16 | `eng/phase-1-research/templates/05-personas.template.md` | `skills/pm-pmm/templates/05-personas.template.md` | Copy |
| 17 | `eng/phase-1-research/templates/06-journey-maps.template.md` | `skills/pm-pmm/templates/06-journey-maps.template.md` | Copy |
| 18 | `eng/phase-1-research/templates/07-voc-analysis.template.md` | `skills/pm-pmm/templates/07-voc-analysis.template.md` | Copy |
| 19 | `eng/phase-1-research/templates/08-business-case.template.md` | `skills/pm-pmm/templates/08-business-case.template.md` | Copy |
| 20 | `eng/phase-1-research/templates/09-market-sizing.template.md` | `skills/pm-pmm/templates/09-market-sizing.template.md` | Copy |
| 21 | `eng/phase-1-research/templates/10-competitive-analysis.template.md` | `skills/pm-pmm/templates/10-competitive-analysis.template.md` | Copy |
| 22 | `eng/phase-1-research/templates/11-battle-cards.template.md` | `skills/pm-pmm/templates/11-battle-cards.template.md` | Copy |
| 23 | `eng/phase-1-research/templates/12-win-loss-analysis.template.md` | `skills/pm-pmm/templates/12-win-loss-analysis.template.md` | Copy |
| 24 | `eng/phase-1-research/templates/13-gtm-plan.template.md` | `skills/pm-pmm/templates/13-gtm-plan.template.md` | Copy |
| 25 | `eng/phase-1-research/templates/14-mrd.template.md` | `skills/pm-pmm/templates/14-mrd.template.md` | Copy |
| 26 | `eng/phase-1-research/templates/15-buyer-personas.template.md` | `skills/pm-pmm/templates/15-buyer-personas.template.md` | Copy |

**Total files to deploy: 26** (1 SKILL.md + 10 agent files + 15 templates)

---

## Registration Actions

These are modifications to existing framework files, NOT copy operations.

| # | Target File | Action | Details |
|---|------------|--------|---------|
| R1 | `CLAUDE.md` (root) | Append to Skills table | Add row: `\| /pm-pmm \| Product management and product marketing decision framework \|` |
| R2 | `AGENTS.md` | Append agent registry entries | Add 5 entries: pm-product-strategist (opus), pm-customer-insight (opus), pm-market-strategist (opus), pm-business-analyst (sonnet), pm-competitive-analyst (sonnet) |
| R3 | `.context/rules/mandatory-skill-usage.md` | Append to Trigger Map table | Add `/pm-pmm` trigger map entry per `eng/phase-4-integration/trigger-map-entry.md` |

---

## Runtime Directory Scaffolding

These directories are created at deployment time to receive runtime artifacts. They are empty on deployment.

```bash
mkdir -p docs/pm-pmm/prd
mkdir -p docs/pm-pmm/product-vision
mkdir -p docs/pm-pmm/roadmap
mkdir -p docs/pm-pmm/use-cases
mkdir -p docs/pm-pmm/personas
mkdir -p docs/pm-pmm/journey-maps
mkdir -p docs/pm-pmm/voc
mkdir -p docs/pm-pmm/business-case
mkdir -p docs/pm-pmm/market-sizing
mkdir -p docs/pm-pmm/competitive-analysis
mkdir -p docs/pm-pmm/battle-cards
mkdir -p docs/pm-pmm/win-loss
mkdir -p docs/pm-pmm/gtm-plan
mkdir -p docs/pm-pmm/mrd
mkdir -p docs/pm-pmm/buyer-personas
```

Each directory should contain a `.gitkeep` file to preserve directory structure in version control.

---

## Pre-Deployment Checklist

Complete ALL checks before executing the deployment steps.

### Structural Validation

| # | Check | Command / Method | Expected Result |
|---|-------|-----------------|-----------------|
| P1 | SKILL.md exists and is < 600 lines | `wc -l eng/phase-2-tier1-agents/SKILL.md` | < 600 lines (currently 532) |
| P2 | All 5 agent .md files exist | `ls eng/phase-2-tier1-agents/*.md eng/phase-3-tier2-agents/*.md` | 6 files (5 agents + 1 SKILL.md) |
| P3 | All 5 governance .yaml files exist | `ls eng/phase-2-tier1-agents/*.yaml eng/phase-3-tier2-agents/*.yaml` | 5 files |
| P4 | All 15 template files exist | `ls eng/phase-1-research/templates/*.template.md \| wc -l` | 15 |
| P5 | No production `skills/pm-pmm/` exists yet | `ls skills/pm-pmm/ 2>/dev/null` | Should fail (directory not found) |

### Schema Validation

| # | Check | Command / Method | Expected Result |
|---|-------|-----------------|-----------------|
| S1 | All governance YAMLs validate against schema | Validate each `.governance.yaml` against `docs/schemas/agent-governance-v1.schema.json` | 0 errors per file |
| S2 | All agent .md frontmatter has required fields | Verify `name`, `description`, `model`, `tools` in each .md YAML frontmatter | All 4 fields present in all 5 agents |
| S3 | All template files have valid frontmatter | Check each template for `id`, `type`, `agent`, `status` fields | All templates parseable |

### Constitutional Compliance

| # | Check | Command / Method | Expected Result |
|---|-------|-----------------|-----------------|
| C1 | P-003 in all governance YAMLs | Grep for `P-003` in all `.governance.yaml` | Present in all 5 |
| C2 | P-020 in all governance YAMLs | Grep for `P-020` in all `.governance.yaml` | Present in all 5 |
| C3 | P-022 in all governance YAMLs | Grep for `P-022` in all `.governance.yaml` | Present in all 5 |
| C4 | No agent has Task tool | Grep for `Task` in all agent .md `tools:` sections | 0 matches |
| C5 | All agents have >= 3 forbidden_actions | Count entries in each `.governance.yaml` | >= 3 per agent |

### Security Prerequisites

All 7 DC-MUST conditions from `sec/phase-4-final/final-security-assessment.md` Section 8.1 MUST be satisfied before deployment execution. A deployer MUST NOT proceed to Deployment Execution Steps until all PASS conditions are confirmed and the two non-deterministic conditions (DC-MUST-06, DC-MUST-07) have documented plans.

| # | DC-MUST ID | Condition | Status |
|---|------------|-----------|--------|
| SP1 | DC-MUST-01 | All 5 agent `.md` files exclude `Task` from `tools` frontmatter | PASS |
| SP2 | DC-MUST-02 | All 5 `.governance.yaml` files include P-003, P-020, P-022 in `constitution.principles_applied` | PASS |
| SP3 | DC-MUST-03 | All 5 `.governance.yaml` files have >= 3 entries in `capabilities.forbidden_actions` | PASS |
| SP4 | DC-MUST-04 | All 5 agents include "untrusted external data" treatment in Security Guardrails | PASS |
| SP5 | DC-MUST-05 | Sensitivity defaults correct: pm-customer-insight=confidential, pm-business-analyst=restricted, pm-competitive-analyst=restricted, pm-product-strategist=internal, pm-market-strategist=internal | PASS |
| SP6 | DC-MUST-06 | Operator population limited to authenticated internal PM/PMM practitioners | N/A -- verify at deployment time |
| SP7 | DC-MUST-07 | All 37 injection test scenarios scheduled for execution within 30 days of first production use | NOT MET -- test plan must be documented before deployment |

### Content Integrity

| # | Check | Command / Method | Expected Result |
|---|-------|-----------------|-----------------|
| I1 | SKILL.md agent registry matches actual files | Cross-reference Available Agents table with files | 5 agents listed, 5 files exist |
| I2 | Activation-keywords count >= 50 | Count keywords in SKILL.md frontmatter | >= 50 keywords |
| I3 | All 8 cross-agent data flows documented | Verify Cross-Agent Data Flow table | 8 flows defined |
| I4 | All 6 integration points documented | Verify Integration Points table | 6 integration points |
| I5 | Navigation table present in SKILL.md (H-23) | Check for `\| Section \| Purpose \|` | Present |

---

## Deployment Execution Steps

Execute in this exact order. Each step depends on the previous step's success.

### Step 1: Create Production Directory Structure

```bash
mkdir -p skills/pm-pmm/agents
mkdir -p skills/pm-pmm/templates
```

### Step 2: Deploy SKILL.md

```bash
cp eng/phase-2-tier1-agents/SKILL.md skills/pm-pmm/SKILL.md
```

### Step 3: Deploy Agent Definitions (Tier 1)

```bash
cp eng/phase-2-tier1-agents/pm-product-strategist.md skills/pm-pmm/agents/
cp eng/phase-2-tier1-agents/pm-product-strategist.governance.yaml skills/pm-pmm/agents/
cp eng/phase-2-tier1-agents/pm-customer-insight.md skills/pm-pmm/agents/
cp eng/phase-2-tier1-agents/pm-customer-insight.governance.yaml skills/pm-pmm/agents/
cp eng/phase-2-tier1-agents/pm-market-strategist.md skills/pm-pmm/agents/
cp eng/phase-2-tier1-agents/pm-market-strategist.governance.yaml skills/pm-pmm/agents/
```

### Step 4: Deploy Agent Definitions (Tier 2)

```bash
cp eng/phase-3-tier2-agents/pm-business-analyst.md skills/pm-pmm/agents/
cp eng/phase-3-tier2-agents/pm-business-analyst.governance.yaml skills/pm-pmm/agents/
cp eng/phase-3-tier2-agents/pm-competitive-analyst.md skills/pm-pmm/agents/
cp eng/phase-3-tier2-agents/pm-competitive-analyst.governance.yaml skills/pm-pmm/agents/
```

### Step 5: Deploy Templates

```bash
cp eng/phase-1-research/templates/*.template.md skills/pm-pmm/templates/
```

### Step 6: Create Runtime Artifact Directories

```bash
for dir in prd product-vision roadmap use-cases personas journey-maps voc business-case market-sizing competitive-analysis battle-cards win-loss gtm-plan mrd buyer-personas; do
  mkdir -p docs/pm-pmm/$dir
  touch docs/pm-pmm/$dir/.gitkeep
done
```

### Step 7: Register in CLAUDE.md

Add to the Skills table in `CLAUDE.md`:

```markdown
| `/pm-pmm` | Product management and product marketing decision framework |
```

### Step 8: Register in AGENTS.md

Add 5 agent entries to `AGENTS.md` following the existing format for agents in other skills.

### Step 9: Register in mandatory-skill-usage.md

Add the trigger map entry from `eng/phase-4-integration/trigger-map-entry.md` to the Trigger Map table in `.context/rules/mandatory-skill-usage.md`.

### Step 10: Update H-22 Rule Text

Add `/pm-pmm` to the H-22 rule text in `mandatory-skill-usage.md`:

```
MUST invoke `/pm-pmm` for product strategy, customer insight, business analysis, competitive intelligence, and go-to-market planning.
```

---

## Post-Deployment Verification

### File Existence Checks

| # | Check | Command | Expected |
|---|-------|---------|----------|
| V1 | SKILL.md exists | `test -f skills/pm-pmm/SKILL.md` | Exit 0 |
| V2 | All 10 agent files exist | `ls skills/pm-pmm/agents/ \| wc -l` | 10 files |
| V3 | All 15 templates exist | `ls skills/pm-pmm/templates/ \| wc -l` | 15 files |
| V4 | All 15 runtime dirs exist | `ls docs/pm-pmm/ \| wc -l` | 15 directories |
| V5 | CLAUDE.md contains /pm-pmm | `grep '/pm-pmm' CLAUDE.md` | Match found |
| V6 | mandatory-skill-usage.md contains /pm-pmm | `grep '/pm-pmm' .context/rules/mandatory-skill-usage.md` | Match found |

### Functional Smoke Tests

| # | Test | Method | Expected |
|---|------|--------|----------|
| F1 | Skill triggers on "Write a PRD" | New Claude session, say "Write a PRD for X" | `/pm-pmm` skill activates, pm-product-strategist selected |
| F2 | Skill triggers on "Create personas" | New Claude session, say "Create JTBD personas" | pm-customer-insight selected |
| F3 | Negative keyword suppression works | New Claude session, say "Review this code" | `/pm-pmm` does NOT activate |
| F4 | Discovery mode is default | Request artifact without specifying mode | Agent defaults to discovery mode |
| F5 | Agent produces file artifact | Complete a discovery request | File written to `docs/pm-pmm/{type}/{slug}.md` |

### Schema Post-Check

| # | Test | Method | Expected |
|---|------|--------|----------|
| SC1 | Production governance YAMLs validate | Run schema validation on `skills/pm-pmm/agents/*.governance.yaml` | 0 errors |
| SC2 | Production agent .md frontmatter valid | Check Claude Code fields in production copies | All required fields present |

---

## Rollback Plan

If deployment fails at any step, execute rollback in reverse order:

### Step R1: Remove trigger map entry from mandatory-skill-usage.md

Remove the `/pm-pmm` row from the Trigger Map table and the H-22 rule text addition. Use the following grep pattern to locate:

```bash
grep -n 'pm-pmm' .context/rules/mandatory-skill-usage.md
```

Remove the entire table row containing `| product strategy, PRD, product requirements, ...` and the H-22 text containing `MUST invoke /pm-pmm`. Also revert the L2-REINJECT comment to remove `/pm-pmm` references.

### Step R2: Remove /pm-pmm entry from CLAUDE.md

Remove the row from the Skills table:

```bash
grep -n 'pm-pmm' CLAUDE.md
```

Delete the line: `| /pm-pmm | Product management and product marketing decision framework |`

### Step R3: Remove AGENTS.md entries

Remove all 5 agent entries. Use the following grep pattern to locate:

```bash
grep -n 'pm-product-strategist\|pm-customer-insight\|pm-market-strategist\|pm-business-analyst\|pm-competitive-analyst' AGENTS.md
```

Remove the full agent entry blocks for: `pm-product-strategist`, `pm-customer-insight`, `pm-market-strategist`, `pm-business-analyst`, `pm-competitive-analyst`.

### Step R4: Remove production directories

```bash
rm -rf skills/pm-pmm/
rm -rf docs/pm-pmm/
```

---

## Caveats Carried from Barrier 3

The following caveats from the Barrier 3 constraint check are acknowledged and do NOT block deployment. They are tracked for post-deployment iteration.

| # | Caveat | Impact | Mitigation |
|---|--------|--------|------------|
| 1 | 19 SEC defense-in-depth requirements not fully implemented (51/70 implemented = 73% per final security assessment Section 4) | Security guardrails rely on LLM behavioral compliance for the 16 NOT IMPLEMENTED and 3 PARTIALLY IMPLEMENTED requirements | Post-deployment: file security enablers for L3/L5 enforcement |
| 2 | Narrative guardrail enforcement gap | No deterministic enforcement for security guardrails | Post-deployment: design L3 AST-based validation for sensitivity fields |
| 3 | Provenance self-reporting (pm-competitive-analyst) | No independent verification of provenance claims | Post-deployment: design provenance audit workflow |
| 4 | pm-competitive-analyst.governance.yaml at 0.911 | Below 0.92 individual threshold | Non-blocking: aggregate 0.920 passes H-13; file improvement enabler |
| 5 | WebSearch query privacy (FM-18) | Strategic intent may leak to search providers | Accepted risk: documented in threat model |
| 6 | Paraphrase bypass of "no verbatim" restriction | Confidential content paraphrasing circumvents guardrail | Post-deployment: evaluate summarization quality in practice |
| 7 | SKILL.md context budget (~532 lines) | Exceeds ~500-token Tier 1 budget | Mitigated: triple-lens navigation enables selective loading |

---

*Manifest Version: 1.0.0*
*Source: PROJ-018 PM/PMM Skill, Phase 4 Integration*
*Created: 2026-03-01*
