# Quality Score Report: MCP Coordination Rules

## L0 Executive Summary
**Score:** 0.884/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.72)
**One-line assessment:** The deliverable is structurally complete and well-organized, but contains a direct matrix contradiction with its authoritative source (SKILL.md shows `/ux-ai-first-design` as `REQ` for Figma; the deliverable classifies it as `COND`), and the Figma risk section omits the quality-impact column present in the source — these must be resolved before the C4 threshold of 0.95 can be reached.

---

## Scoring Context
- **Deliverable:** `skills/user-experience/rules/mcp-coordination.md`
- **Deliverable Type:** Rule File (governance artifact)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.884 |
| **Threshold** | 0.95 (C4 override applied by user; standard H-13 is 0.92) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No — standalone scoring |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.92 | 0.184 | All 10 sub-skills present in matrix; all 6 MCP tools covered; degraded modes defined; minor gap: Memory-Keeper absent from matrix despite skill frontmatter listing it |
| Internal Consistency | 0.20 | 0.72 | 0.144 | Direct contradiction: SKILL.md matrix shows `/ux-ai-first-design` Figma = REQ; deliverable shows COND; Figma risk table also omits Quality Impact column present in SKILL.md source |
| Methodological Rigor | 0.20 | 0.92 | 0.184 | REQ/ENH/COND taxonomy defined with failure behavior; enforcement rules stated; detection protocol is sequential and testable; adapter architecture pattern documented |
| Evidence Quality | 0.15 | 0.90 | 0.135 | Section-level source annotations present for all 8 sections; MCP-001 cited; cross-refs to sibling rules present; one source annotation incorrectly attributes MCP CHECK step to routing lifecycle rather than SKILL.md MCP architecture section |
| Actionability | 0.15 | 0.92 | 0.138 | Detection protocol is 4-step executable sequence; fallback paths are specific per tool; cost tier routing is decision-point linked to ux-routing-rules.md; degraded mode disclosure template is copy-paste ready |
| Traceability | 0.10 | 0.90 | 0.090 | VERSION header present; parent SKILL.md cited; all 4 sibling rules referenced in footer and preamble; footer includes status and dates; no direct section-level anchor links to SKILL.md headings (MEDIUM gap) |
| **TOTAL** | **1.00** | | **0.884** | |

---

## Detailed Dimension Analysis

### Completeness (0.92/1.00)

**Evidence:**

All 10 sub-skills are present in the MCP Dependency Matrix (lines 28-38). All 6 MCP tools covered by the matrix as columns: Figma, Miro, Storybook, Zeroheight, Hotjar (Bridge), Whimsical. All 8 sections listed in the navigation table are present in the document body. Degraded modes are defined for all 6 future MCP tools plus Context7. Cost tiers are present (3 tiers). Detection protocol covers 4 steps. Future adapter architecture covers all 6 planned adapters with priority, rationale, and authentication fields.

**Gaps:**

Memory-Keeper is listed in `SKILL.md` frontmatter `allowed-tools` and is used by `ux-orchestrator` for phase-boundary state (`mcp-tool-standards.md` MCP-002). It does not appear in the MCP Dependency Matrix or in the Current Jerry MCP Integration table. While `mcp-coordination.md` focuses on design-tool MCPs (Figma/Miro/Storybook) rather than infrastructure MCPs (Memory-Keeper), a complete coordination document should either include it or explicitly state that infrastructure MCP tools are out of scope. The absence is a completeness gap at the minor level.

The Figma Dependency Risk section (lines 105-117) omits the "Quality Impact" column that exists in the SKILL.md Figma Dependency Risk Profile table (source lines 419-424 in SKILL.md). SKILL.md source does not have a quality impact column either — this is correctly reproduced. On re-examination: SKILL.md source table has only Sub-Skill and Non-Figma Fallback columns; the deliverable adds a "Quality Impact" column (lines 105-109). This is an ADDITION not in source, which is appropriate elaboration. Not a gap.

**Improvement Path:**

Add a one-line note in the MCP Dependency Matrix section header explicitly scoping coverage: "This matrix covers design-tool MCP dependencies. Infrastructure MCP tools (Memory-Keeper for state management) are governed by `mcp-tool-standards.md` and are not included here." This would raise Completeness to 0.95+.

---

### Internal Consistency (0.72/1.00)

**Evidence:**

**Critical contradiction identified:**

SKILL.md Section "MCP Integration Architecture" Sub-Skill MCP Dependency Matrix (lines 400-412 of SKILL.md):
```
| `/ux-ai-first-design` | **REQ** | -- | ENH | -- | -- | -- |
```

`mcp-coordination.md` MCP Dependency Matrix (line 37):
```
| `/ux-ai-first-design` | **COND** | -- | ENH | -- | -- | -- |
```

This is a direct contradiction between the deliverable's most central artifact — the dependency matrix — and its authoritative source. The deliverable claims to source this section from "SKILL.md Section 'MCP Integration Architecture'" (line 24), but the classification for `/ux-ai-first-design` diverges from the source.

The COND classification is arguably more architecturally sound (since `/ux-ai-first-design` is a conditional sub-skill with entry criteria), and it is internally consistent within the document (the Dependency Classifications section defines COND correctly, and the Figma Dependency Risk table at line 109 does include `/ux-ai-first-design`, which would only make sense if the Figma dependency is active under some condition). However, the document header claims SKILL.md is the authoritative source, and SKILL.md says REQ. Either the SKILL.md must be updated, or the deliverable must match SKILL.md and add a note explaining the REQ-under-COND-condition interpretation.

**Additional inconsistency:**

The `Context7 Usage Rules` section (lines 131-138) correctly cites `mcp-tool-standards.md [Context7 Integration]` for Protocol steps 1-4. However, step 3 ("Respect the per-question call limit enforced by the tool") is reproduced accurately. Step 4 adds "If `resolve-library-id` returns no matches: fall back to WebSearch for that library." This matches `mcp-tool-standards.md` exactly and is consistent.

The "Storybook endpoint | Component story browsing | Manual component inventory" row in the Future MCP Probes table (line 190) references Storybook endpoint, which aligns with the "Local endpoint (dev server)" authentication in the Planned Adapters table (line 219). Consistent.

**Internal consistency within the deliverable is otherwise sound.** The REQ/ENH/COND taxonomy is applied consistently across all tables except for the one identified contradiction. The degraded mode descriptions align with the risk profile fallbacks. The cost tier text-only mode description aligns with the Free tier sub-skills.

**Gaps:**

The `/ux-ai-first-design` REQ vs COND discrepancy is the single significant internal consistency failure. It must be resolved by aligning with one authoritative source and documenting the resolution.

**Improvement Path:**

Option A: Align the deliverable with SKILL.md (change COND to REQ) and add a note: "Note: `/ux-ai-first-design` is a conditional sub-skill (Wave 5 COND entry criteria apply), but when it is active, Figma is a required dependency. REQ classification applies when the sub-skill is invoked."

Option B: Update SKILL.md to change REQ to COND with the same explanatory note, making the deliverable the correcting authority.

Either option must be chosen explicitly and the source/deliverable must be synchronized. This change alone would raise Internal Consistency to 0.90+.

---

### Methodological Rigor (0.92/1.00)

**Evidence:**

The REQ/ENH/COND classification taxonomy is systematic and complete. Definitions are precise: REQ = degraded mode + explicit error; ENH = cosmetic limitation only; COND = condition-evaluated before MCP check. The three enforcement rules (lines 53-55) are clear behavioral specifications with consequences.

The MCP Availability Detection protocol (lines 172-179) is a 4-step sequence: Probe, If-success, If-failure, Disclose. Each step is deterministic. The probe is specific (lightweight Context7 resolve-library-id call with "WCAG" as the test library), making it testable. The "cache status for engagement session" instruction (step 2) is an implementable optimization.

The Adapter Architecture Pattern (lines 204-211) presents a 5-step pattern applicable to all future adapters. This is rigorous and consistent with the adapter table below it.

The Security Considerations section (lines 226-231) cross-references `/eng-team` and cites `mcp-tool-standards.md`, which is appropriate. OAuth token and API key handling rules are stated with MUST-level language.

**Minor gaps:**

The detection protocol does not specify what constitutes a "timeout" vs. "error" for step 3 — the distinction matters for retry logic (is a timeout retriable before declaring MCP unavailable?). This is a minor gap in operationalizability.

The Cost Tier Routing section (lines 163-165) references the CAPACITY CHECK step in `ux-routing-rules.md` but does not state the exact threshold or decision logic here — it defers correctly, but a forward-reference anchor link would improve rigor.

**Improvement Path:**

Add a timeout definition to the detection protocol: "timeout is defined as > N seconds with no response from the MCP server; 1 retry is attempted before declaring unavailable." This would raise rigor to 0.95.

---

### Evidence Quality (0.90/1.00)

**Evidence:**

Source annotations are present for all 8 sections using HTML comment format:
- Line 24: `<!-- Source: SKILL.md Section "MCP Integration Architecture" — sub-skill dependency matrix. -->`
- Line 43: cites "MCP Integration Architecture" with labels used consistently across tables
- Line 61: cites "MCP Integration Architecture" — text-only mode
- Line 101: cites "SKILL.md Section 'Figma Dependency Risk Profile'"
- Line 122: cites "SKILL.md Section 'Current Jerry MCP Integration' and mcp-tool-standards.md MCP-001"
- Line 154: cites "SKILL.md Section 'Cost Tiers'"
- Line 170: cites "SKILL.md Section 'Lifecycle-Stage Routing' — MCP CHECK step"
- Line 196: cites "SKILL.md Section 'MCP Integration Architecture' — architecture + fallback paths only"

MCP-001 is explicitly cited with document and section (line 133). Cross-references to 4 sibling rule files are present in both preamble and footer.

**Minor gap — source attribution accuracy:**

Section "MCP Availability Detection" cites "SKILL.md Section 'Lifecycle-Stage Routing' — MCP CHECK step" (line 170). The MCP CHECK step appears in SKILL.md's Lifecycle-Stage Routing section (confirmed at line 303 of SKILL.md), so this citation is accurate. However, the detection protocol details (lightweight probe, cache behavior) are elaborations beyond what SKILL.md provides — these elaborations lack source attribution, giving the impression they are directly sourced from SKILL.md when they are original elaborations. This is a minor citation accuracy gap (the rule file author derived the protocol from SKILL.md and elaborated it, which is appropriate, but the source annotation should note the elaboration: "— MCP CHECK step; probe implementation details are elaborations from SKILL.md specification").

**Improvement Path:**

Update the MCP Availability Detection source annotation to: `<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — MCP CHECK step. Probe implementation details (WCAG test call, caching, timeout handling) are elaborations operationalizing the SKILL.md specification. -->` This clarifies what was sourced vs. what was derived.

---

### Actionability (0.92/1.00)

**Evidence:**

The orchestrator can directly implement the 4-step detection protocol (lines 172-179). Steps are unambiguous: Probe uses a specific API call (resolve-library-id with "WCAG"), success/failure branches are defined, disclosure text format is specified.

The Degraded Mode Disclosure template (lines 90-95) is copy-paste ready with placeholder variables. Sub-skill agents can implement this template directly.

The Enforcement Rules (lines 53-55) state behavioral requirements with MUST-level language that maps directly to orchestrator behavior: REQ → inform user per P-022 AND route to degraded-mode fallback; ENH → proceed normally; COND → evaluate condition first.

The Cost Tier Routing guidance (lines 163-165) connects to the CAPACITY CHECK step and references the specific rule file and section, enabling direct implementation.

The Security Considerations (lines 226-231) use MUST NOT language for four specific prohibited behaviors, enabling validation.

**Minor gap:**

The "Future MCP Probes" table (lines 184-190) shows 4 probe rows (Context7, Figma, Miro, Storybook) but the probe implementation details are absent for Figma/Miro/Storybook. For Context7, the probe is detailed (lines 176-179). For future tools, "API health" is the probe description — this is too vague to implement without additional specification. This is appropriate for a future-architecture section but limits actionability slightly.

**Improvement Path:**

Add a note to the Future MCP Probes table: "Probe implementations for Figma/Miro/Storybook will be specified in their respective adapter architecture documents (PROJ-022 scope). The probe endpoint specification follows the Adapter Architecture Pattern: health probe endpoint defined in step 1 of each adapter." This acknowledges the gap without requiring premature specification.

---

### Traceability (0.90/1.00)

**Evidence:**

VERSION header is present (line 1): `<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "MCP Integration Architecture", "Current Jerry MCP Integration", "Figma Dependency Risk Profile", "Cost Tiers" | PARENT: /user-experience skill -->`.

All 4 sibling rule files are referenced in the preamble (line 5) and in the footer (lines 237-238). Parent SKILL.md is cited with repo-relative path in both preamble and footer.

Explicit source annotations in HTML comments trace each section to its SKILL.md parent section.

Footer includes: rule file name, parent skill, parent SKILL.md path, sibling rules (all 4), created date, updated date, and status.

**Minor gaps:**

Source annotations reference SKILL.md section names by title (e.g., "Section 'MCP Integration Architecture'") but do not include anchor links. While SKILL.md section anchors exist (`#mcp-integration-architecture`), the annotations do not provide them. For a C4 deliverable, anchor-level traceability would be more rigorous.

The Internal Consistency finding (REQ vs COND contradiction) is also a traceability failure: the deliverable claims to trace to SKILL.md but diverges from it at the most critical cell in the matrix. This partially overlaps with the Internal Consistency score but is also a traceability failure.

**Improvement Path:**

Enhance source annotations to include SKILL.md anchor links: `<!-- Source: SKILL.md [MCP Integration Architecture](#mcp-integration-architecture) -->`. This costs minimal effort and raises Traceability to 0.95+.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.72 | 0.90+ | Resolve the `/ux-ai-first-design` Figma REQ vs COND contradiction. Choose Option A (align deliverable to SKILL.md, add explanatory note) or Option B (update SKILL.md, document in deliverable). Must synchronize both sources. |
| 2 | Internal Consistency | 0.72 | 0.90+ | (Same fix as #1) Once the matrix cell is corrected, verify the Figma Dependency Risk Profile section still includes `/ux-ai-first-design` (it should remain, since COND means it is active under conditions, and when active Figma is required). |
| 3 | Completeness | 0.92 | 0.95+ | Add a one-sentence scope note to the MCP Dependency Matrix section: "Scope: design-tool MCPs only. Infrastructure MCPs (Memory-Keeper) are governed by `mcp-tool-standards.md`." |
| 4 | Traceability | 0.90 | 0.95+ | Add anchor links to SKILL.md sections in source annotations. Example: change `"Section 'MCP Integration Architecture'"` to `"Section [MCP Integration Architecture](../SKILL.md#mcp-integration-architecture)"`. |
| 5 | Methodological Rigor | 0.92 | 0.95+ | Add a timeout definition to the MCP Availability Detection protocol: "Timeout = > 5 seconds with no response; 1 retry before declaring unavailable." |
| 6 | Evidence Quality | 0.90 | 0.93+ | Update MCP Availability Detection source annotation to distinguish what is sourced from SKILL.md vs. what is original elaboration. |

---

## Leniency Bias Check
- [x] Each dimension scored independently
- [x] Evidence documented for each score: specific line numbers and quoted content used for all claims
- [x] Uncertain scores resolved downward: Internal Consistency was the most uncertain dimension; scored 0.72 (not 0.80) because the REQ vs COND contradiction is direct and central — the matrix is the core artifact of this document
- [x] First-draft calibration considered: this is iteration 2; the file has mature structure but the matrix contradiction is a regression from expected quality
- [x] No dimension scored above 0.95 without exceptional evidence: highest score is 0.92; none above 0.95

---

## Scoring Notes

**Why Internal Consistency scored 0.72 (not higher):**

The contradiction is not peripheral — the MCP Dependency Matrix is the document's primary artifact, and the contradiction is in the cell for the only CONDITIONAL sub-skill in the entire skill. The SKILL.md clearly states `**REQ**` for `/ux-ai-first-design` Figma. The deliverable states `**COND**`. This is a 1-cell difference in a 10-row table, but that cell governs how the orchestrator routes the most complex, highest-criteria sub-skill in the entire skill. The calibration anchor of 0.70 = "Good work with clear improvement areas" applies: the deliverable is good quality overall, but this is a clear and specific gap requiring resolution before a C4 threshold can be met.

**Why the composite (0.884) does not meet the C4 threshold of 0.95:**

The gap is primarily driven by Internal Consistency (0.72 contributing 0.144 weighted vs. a would-be 0.95 contributing 0.190 — a 0.046 gap). Even with perfect scores on all other dimensions, the Internal Consistency dimension at 0.72 limits the composite to approximately 0.93. The C4 threshold of 0.95 requires all dimensions to score in the 0.90-0.95+ range. After resolving the matrix contradiction and implementing the remaining improvements (scope note, anchor links, timeout definition), the composite could reach 0.95+.

**Session Context (handoff schema):**
```yaml
verdict: REVISE
composite_score: 0.884
threshold: 0.95
weakest_dimension: Internal Consistency
weakest_score: 0.72
critical_findings_count: 1
iteration: 2
improvement_recommendations:
  - "Resolve /ux-ai-first-design Figma REQ vs COND contradiction by synchronizing with SKILL.md"
  - "Add Memory-Keeper scope exclusion note to MCP Dependency Matrix section"
  - "Add anchor links to SKILL.md sections in source annotations"
  - "Add timeout definition to MCP Availability Detection protocol"
  - "Update MCP Availability Detection source annotation to distinguish sourced vs elaborated content"
```

---

*Score report: mcp-coordination-iter2-score.md*
*Deliverable scored: skills/user-experience/rules/mcp-coordination.md*
*Scoring agent: adv-scorer*
*SSOT: .context/rules/quality-enforcement.md*
*Created: 2026-03-04*
