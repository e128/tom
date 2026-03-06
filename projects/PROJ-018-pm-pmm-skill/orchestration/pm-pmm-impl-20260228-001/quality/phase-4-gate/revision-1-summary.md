# Phase 4 Gate Revision 1 Summary

<!-- VERSION: 1.0.0 | DATE: 2026-03-01 | SOURCE: Adversarial Groups A, B, C converging findings -->

> Targeted revisions to Phase 4 integration artifacts based on converging adversarial quality findings from Groups A, B, and C.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Revision Overview](#revision-overview) | Scope, inputs, and files modified |
| [Fix Detail Table](#fix-detail-table) | All 8 fixes with file, change, and score impact |
| [Per-Fix Detail](#per-fix-detail) | Detailed description of each fix |
| [Traceability Matrix](#traceability-matrix) | Finding ID to fix mapping |

---

## Revision Overview

**Revision:** 1
**Date:** 2026-03-01
**Inputs:**
- `quality/phase-4-gate/adv-group-a-constitutional.md` -- Group A (S-007 Constitutional) findings
- `quality/phase-4-gate/adv-group-b-dialectical.md` -- Group B (S-003/S-002 Dialectical) findings
- `quality/phase-4-gate/adv-group-c-analytical.md` -- Group C (S-012/S-013 Analytical) findings
- `sec/phase-4-final/final-security-assessment.md` -- Final security assessment (DC-MUST conditions, SEC compliance numbers)

**Files Modified:**
1. `eng/phase-4-integration/deployment-manifest.md`
2. `eng/phase-4-integration/trigger-map-entry.md`
3. `eng/phase-4-integration/e2e-verification.md`
4. `eng/phase-4-integration/workflow-patterns.md`

**Fix Count:** 8

---

## Fix Detail Table

| Fix # | Title | Files Changed | Finding Sources | Type |
|-------|-------|---------------|-----------------|------|
| 1 | Add DC-MUST cross-reference to deployment manifest | deployment-manifest.md | Groups A, B, C (security prerequisite gap) | BLOCKING |
| 2 | Fix "strategy (standalone)" negative keyword notation | trigger-map-entry.md | Groups A, C (routing parsability) | Standard |
| 3 | Add registration rollback details | deployment-manifest.md | Groups B, C (rollback specificity) | Standard |
| 4 | Fix priority collision with /ast | trigger-map-entry.md | Groups A, B (priority collision at 8) | Standard |
| 5 | Add AGENTS.md verification to E2E | e2e-verification.md | Groups A, C (registration verification gap) | Standard |
| 6 | Add error handling to workflow patterns | workflow-patterns.md | Groups B, C (error handling gap) | Standard |
| 7 | Fix stale caveat numbers | deployment-manifest.md, e2e-verification.md | Groups A, B, C (data accuracy) | Standard |
| 8 | Expand template frontmatter validation | e2e-verification.md | Groups A, C (template field coverage gap) | Standard |

---

## Per-Fix Detail

### Fix 1: Add DC-MUST Cross-Reference to Deployment Manifest (BLOCKING)

**File:** `eng/phase-4-integration/deployment-manifest.md`
**Lines affected:** 117-144 (new "Security Prerequisites" subsection inserted before "Content Integrity")

**What changed:**
- Added a new "Security Prerequisites" subsection within the Pre-Deployment Checklist section.
- Lists all 7 DC-MUST conditions from `sec/phase-4-final/final-security-assessment.md` Section 8.1 with their IDs, descriptions, and current pass/fail status.
- Includes a gate statement: deployer MUST NOT proceed to Deployment Execution Steps until all PASS conditions are confirmed and DC-MUST-06/DC-MUST-07 have documented plans.

**Justification:** Without this cross-reference, a deployer could execute deployment without checking security prerequisites. The DC-MUST conditions are the security team's deployment gate and must be visible in the deployment manifest.

### Fix 2: Fix "strategy (standalone)" Negative Keyword

**File:** `eng/phase-4-integration/trigger-map-entry.md`
**Lines affected:** 28 (trigger map row), 103 (negative keyword table), 105-108 (disambiguation text), 173 (collision analysis)

**What changed:**
- Replaced `strategy (standalone without "product")` with `strategy` (simple string) in the trigger map entry row and the negative keyword rationale table.
- Updated the "Special Disambiguation: strategy" text to explain that the compound trigger "product strategy" overrides the negative keyword via the Layer 1 routing algorithm's Step 2 (Compound Trigger Specificity Override).
- Updated the collision analysis entry for `/problem-solving` to reference the simple `strategy` negative keyword.

**Justification:** The parenthetical qualifier `(standalone without "product")` is not parseable by the Layer 1 routing algorithm, which expects simple comma-separated strings. The compound trigger mechanism already handles the "product strategy" vs. standalone "strategy" disambiguation correctly.

### Fix 3: Add Registration Rollback Details

**File:** `eng/phase-4-integration/deployment-manifest.md`
**Lines affected:** 269-306 (Rollback Plan section, expanded from 8 lines to 37 lines)

**What changed:**
- Replaced `# Remove trigger map entry from mandatory-skill-usage.md (manual edit)` with Step R1 containing specific grep patterns and exact text to remove.
- Replaced `# Remove /pm-pmm entry from CLAUDE.md (manual edit)` with Step R2 containing grep pattern and exact line to delete.
- Replaced `# Remove AGENTS.md entries (manual edit)` with Step R3 containing grep pattern and the 5 specific agent names to remove.
- Retained the `rm -rf` commands as Step R4.

**Justification:** "Manual edit" provides no actionable guidance during an emergency rollback. Precise grep patterns and removal targets enable a deployer to execute rollback quickly and completely without guessing which content belongs to `/pm-pmm`.

### Fix 4: Fix Priority Collision with /ast

**File:** `eng/phase-4-integration/trigger-map-entry.md`
**Lines affected:** 28 (trigger map row), 139-165 (Priority Rationale section), 221 (Integration Instructions), 226 (Exact Row to Insert)

**What changed:**
- Changed `/pm-pmm` priority from 8 to 9 in the trigger map entry row and the "Exact Row to Insert" in Integration Instructions.
- Updated the Priority Rationale section: changed header from "Assigned Priority: 8" to "Assigned Priority: 9".
- Updated the priority ordering table: `/pm-pmm` now sits at priority 9, `/eng-team` at 10, `/red-team` at 11. `/ast` remains at 8 with no collision.
- Updated rationale text to explain the 2-level gap from `/adversary` (priority 7) and collision avoidance with `/ast` (priority 8).
- Updated Integration Instructions insertion point description.

**Justification:** Both `/ast` and `/pm-pmm` were assigned priority 8, creating a collision that the routing algorithm's Step 3 (Numeric Priority Ordering) cannot resolve. Moving `/pm-pmm` to priority 9 provides clear separation and a 2-level gap from `/adversary` (priority 7) per the routing algorithm's disambiguation threshold.

### Fix 5: Add AGENTS.md Verification to E2E

**File:** `eng/phase-4-integration/e2e-verification.md`
**Lines affected:** 108-143 (new "AGENTS.md Content Verification" subsection inserted after Registration Files table)

**What changed:**
- Added a verification table listing all 5 pm-pmm agent entries with their expected model assignments: opus for pm-product-strategist, pm-customer-insight, pm-market-strategist; sonnet for pm-business-analyst, pm-competitive-analyst.
- Added a verification command script that checks each agent's presence in AGENTS.md and validates the model assignment.

**Justification:** The E2E verification checked for `/pm-pmm` presence in CLAUDE.md and mandatory-skill-usage.md but did not verify AGENTS.md content. Without this check, a deployment could pass verification with missing or incorrectly configured agent entries in AGENTS.md.

### Fix 6: Add Error Handling to Workflow Patterns

**File:** `eng/phase-4-integration/workflow-patterns.md`
**Lines affected:** 399-449 (new "Error Handling" section inserted before "P-003 Compliance Note")

**What changed:**
- Added a new "Error Handling" section with three subsections:
  1. **Partial Result Presentation (H-31):** If an intermediate agent fails, the orchestrator presents all partial results to the user.
  2. **Downstream Agent Suppression:** Downstream agents in the chain do not execute on failed upstream output.
  3. **User Decision Authority (P-020):** The user decides whether to retry, skip, or abort.
- Added a per-pattern error handling table showing which partial results are available at each failure point.
- Added the section to the navigation table.

**Justification:** The workflow patterns documented the happy path but did not specify behavior when an intermediate agent fails. Without error handling specification, an orchestrator has no guidance on whether to continue, retry, or abort, and may make autonomous decisions that violate P-020 (User Authority).

### Fix 7: Fix Stale Caveat Numbers

**Files:** `eng/phase-4-integration/deployment-manifest.md`, `eng/phase-4-integration/e2e-verification.md`
**Lines affected:** deployment-manifest.md line 288 (Caveats table row 1); e2e-verification.md line 476 (V11 Caveats table row 1)

**What changed:**
- **deployment-manifest.md:** Replaced "~39 unaddressed SEC defense-in-depth requirements" with "19 SEC defense-in-depth requirements not fully implemented (51/70 implemented = 73% per final security assessment Section 4)". Updated the Impact column to specify "16 NOT IMPLEMENTED and 3 PARTIALLY IMPLEMENTED requirements".
- **e2e-verification.md:** Applied the same number correction and added the final security assessment Section 4 as a source reference.

**Justification:** The "~39" figure was a stale estimate from an earlier phase. The final security assessment (Section 4) reports 51/70 implemented (73%), meaning 19 are not fully implemented (16 NOT IMPLEMENTED + 3 PARTIALLY IMPLEMENTED). The deployment manifest and E2E verification must reflect actual security assessment numbers to avoid misleading deployers about the scope of unaddressed requirements.

### Fix 8: Expand Template Frontmatter Validation

**File:** `eng/phase-4-integration/e2e-verification.md`
**Lines affected:** 255-303 (V5 Template Completeness section, expanded per-template table and added verification command)

**What changed:**
- Added an "All 11 Fields" column to the per-template check table, expanding it from 6 columns to 7.
- Added a new "Full Frontmatter Field Verification Command" subsection with a bash script that checks all 11 required fields (`id`, `type`, `agent`, `status`, `mode`, `risk_domain`, `sensitivity`, `created`, `last_validated`, `frameworks_applied`, `cross_refs`) in each template's frontmatter.

**Justification:** The original V5 check only verified 4 fields (`id`, `type`, `agent`, `status`) out of the 11 required fields documented in the "Template Frontmatter Required Fields" table within the same section. This gap meant 7 fields could be missing from templates without detection. The verification command provides a deterministic check for all 11 fields.

---

## Traceability Matrix

| Finding Source | Fix # | Status |
|----------------|-------|--------|
| Groups A, B, C: Security prerequisite gap (deployment can bypass security conditions) | Fix 1 | Resolved |
| Groups A, C: "strategy (standalone without 'product')" not parseable by routing algorithm | Fix 2 | Resolved |
| Groups B, C: Rollback plan says "manual edit" without specifics | Fix 3 | Resolved |
| Groups A, B: Priority collision between /pm-pmm and /ast (both at priority 8) | Fix 4 | Resolved |
| Groups A, C: AGENTS.md content not verified in E2E checklist | Fix 5 | Resolved |
| Groups B, C: No error handling specification for workflow pattern failures | Fix 6 | Resolved |
| Groups A, B, C: Stale "~39" caveat number contradicts final security assessment (19 actual) | Fix 7 | Resolved |
| Groups A, C: Template frontmatter verification covers only 4 of 11 required fields | Fix 8 | Resolved |

---

*Revision 1 Complete*
*Date: 2026-03-01*
*Fixes Applied: 8/8*
*Files Modified: 4*
