# Cross-Pollination Handoff: Engineering → Security

> **Barrier:** 4
> **From:** Engineering Pipeline (Phase 4 — Integration and Deployment)
> **To:** Security Pipeline
> **Date:** 2026-03-01

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [Key Findings](#key-findings) | What engineering produced that security needs |
| [Artifacts](#artifacts) | File paths for security review |
| [Security-Relevant Decisions](#security-relevant-decisions) | Design choices with security implications |

---

## Key Findings

1. **Deployment manifest now cross-references all 7 DC-MUST security prerequisites** — deployer cannot proceed without confirming security conditions (Fix 1 from revision-1).
2. **Priority changed from 8 to 9** to avoid /ast collision — no security impact but routing determinism improved.
3. **"strategy (standalone)" replaced with simple negative keyword** — routing algorithm can now parse all keywords deterministically.
4. **Rollback plan includes specific registration removal instructions** — enables complete skill removal including trigger map, CLAUDE.md, and AGENTS.md entries.
5. **Error handling added to workflow patterns** — agent failure mid-chain now escalates to user per P-020/H-31, preventing autonomous continuation on corrupted data.

## Artifacts

- `eng/phase-4-integration/deployment-manifest.md` (revised — Fixes 1, 3, 7)
- `eng/phase-4-integration/workflow-patterns.md` (revised — Fix 6)
- `eng/phase-4-integration/trigger-map-entry.md` (revised — Fixes 2, 4)
- `eng/phase-4-integration/e2e-verification.md` (revised — Fixes 5, 7, 8)

## Security-Relevant Decisions

| Decision | Rationale | Security Implication |
|----------|-----------|---------------------|
| DC-MUST cross-reference in deployment | Ensures security prerequisites checked at deployment time | Closes process integrity gap identified by all 3 adversary groups |
| Stale caveat correction (39→19) | Final security assessment reports 51/70 (73%) implemented | Deployer now has accurate risk picture |
| Registration rollback specifics | Enables complete skill removal | Prevents ghost skill routing to nonexistent files |
| Template frontmatter 11-field validation | Full schema coverage for template verification | Prevents templates with missing sensitivity or risk_domain fields |
