# Quality Score Report: MCP Coordination Rules

## L0 Executive Summary
**Score:** 0.876/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.72)
**One-line assessment:** The file is substantively complete and internally sound but falls short of the C4 0.95 threshold on three concrete gaps: (1) the COND classification is fully defined but never instantiated in the matrix, creating a definition-without-usage gap; (2) the Degraded Mode section conflates currently-available Context7 with future-only MCP adapters in a single subsection structure that risks misleading readers; (3) cross-references to source rules are paraphrased rather than anchored, weakening the traceability chain.

---

## Scoring Context
- **Deliverable:** `skills/user-experience/rules/mcp-coordination.md`
- **Deliverable Type:** Rule file (Foundation layer, /user-experience skill)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-04T12:00:00Z
- **Threshold for C4:** 0.95 (user-specified override); standard H-13 threshold is 0.92
- **Iteration:** 2 (prior score: 0.876, same verdict REVISE)
- **Strategy Findings Incorporated:** No (no adv-executor reports provided)

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.876 |
| **Threshold** | 0.95 (C4 user-specified) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.90 | 0.180 | All 8 required sections present; COND classification defined but never used in the matrix is the one notable gap |
| Internal Consistency | 0.20 | 0.88 | 0.176 | Matrix perfectly mirrors SKILL.md; degraded-mode section structure conflates available vs. future tools in a way that could be read inconsistently |
| Methodological Rigor | 0.20 | 0.90 | 0.180 | Sound layered structure, detection protocol is concrete and timeout-specified; COND definition is present but unused weakens rigor |
| Evidence Quality | 0.15 | 0.88 | 0.132 | Source comments on every section; SKILL.md line references are traceable; MCP-001 citation is by name only, not anchor |
| Actionability | 0.15 | 0.90 | 0.135 | Enforcement rules, degraded-mode disclosure template, and detection protocol are clear and implementable; planned adapter table gives concrete scope |
| Traceability | 0.10 | 0.72 | 0.072 | Section-level source comments exist; cross-references to sibling rules and SKILL.md are present; however, mcp-tool-standards.md reference is paraphrase-only, UX-CI-007 "MCP ownership" claim has no direct evidence in ci-checks.md text (UX-CI-007 validates signoff file structure, not specifically MCP ownership), and the intro claim that UX-CI-007 validates MCP ownership cannot be independently verified from the cited source |
| **TOTAL** | **1.00** | | **0.876** | |

---

## Detailed Dimension Analysis

### Completeness (0.90/1.00)

**Evidence:**
All 8 sections declared in the navigation table are present and substantively populated:
- MCP Dependency Matrix: complete 10x6 grid matching SKILL.md line 400-411 exactly.
- Dependency Classifications: REQ/ENH/COND all defined with failure behaviors.
- Degraded Mode Behavior: per-tool fallbacks specified with both current and future tools.
- Figma Dependency Risk Profile: 4-entry table with quality impact ratings.
- Context7 Usage: 2-tool breakdown with per-agent assignments and 5-entry framework examples.
- Cost Tiers: 3-tier table matching SKILL.md line 428-432 exactly.
- MCP Availability Detection: concrete 4-step protocol with timeout specification.
- Future MCP Adapters: 6-entry planned adapter table with priority, rationale, and authentication.

**Gaps:**
The COND (Conditional) dependency classification is fully defined in the Dependency Classifications section — including failure behavior and enforcement rule — but it does not appear in the MCP Dependency Matrix. There is no row where any sub-skill has a COND entry. This is a definition-without-instantiation gap: a reader cannot determine from the matrix when COND would apply, reducing the operational value of the definition. The section note says "COND classification applies to MCP dependency conditionality," but no example exists.

**Improvement Path:**
Either add a note explaining why no current sub-skill has COND dependencies (e.g., "No current sub-skill has conditional MCP dependencies; COND is reserved for future adapters where usage is context-dependent"), or identify at least one sub-skill where a COND dependency plausibly applies and update the matrix. This would raise completeness to 0.95+.

---

### Internal Consistency (0.88/1.00)

**Evidence:**
The MCP Dependency Matrix matches SKILL.md line 400-411 cell-for-cell, including `/ux-ai-first-design` having REQ Figma (not COND), which was specifically called out as a risk in the scoring context. The clarifying note in the matrix source comment correctly disambiguates: "the COND on line 267 refers to sub-skill wave deployment conditionality, NOT MCP dependency classification." This is the most important consistency claim and it is correct.

The Figma Dependency Risk Profile lists 4 sub-skills as REQ, matching the matrix exactly. The claim "4 sub-skills require it, 2 are enhanced by it (6 of 10 total connections)" is verified by counting: REQ = heuristic-eval, inclusive-design, design-sprint, ai-first-design (4). ENH = ux-jtbd (no, ux-jtbd has no Figma). Re-counting: ENH appears for ux-lean-ux (ENH) and ux-atomic-design (ENH) = 2 ENH. Total = 4+2 = 6. The claim is accurate.

**Gaps:**
The Degraded Mode Behavior section structure creates a mild consistency risk. It separates tools into "Currently available MCP tools" (Context7 only) and "Future MCP adapters" tables. However, the section header is "Per-Dependency Degraded Modes," and Context7's degraded mode (WebSearch fallback) is operationally different in kind from the future adapters — Context7 is live and its fallback is exercisable now, while the others are architecture-only. A reader who skims may not absorb this distinction clearly. The document does label the future tools as "not yet implemented — architecture only in PROJ-022," but this appears mid-table as a subheader rather than as a structural separation.

Additionally, the intro blurb claims "ci-checks.md (CI gate UX-CI-007 validates MCP ownership in kickoff signoff)" — but UX-CI-007 in ci-checks.md is described as "Signoff File Structure — All required fields non-empty." The MCP ownership validation is mentioned in the ci-checks.md intro description at line 5 ("MCP ownership validation consumed by UX-CI-007 kickoff signoff"), suggesting MCP ownership is one of the "required fields," but this is not explicit in the UX-CI-007 gate definition itself. This is a subtle inconsistency between the intro claim and the gate specification.

**Improvement Path:**
Restructure the Degraded Mode table to clearly separate "Currently exercisable fallbacks" from "Future adapter fallbacks (architecture only)" at the table level, not mid-table. Clarify whether UX-CI-007's "required fields non-empty" explicitly includes an MCP ownership field, and if so, name it.

---

### Methodological Rigor (0.90/1.00)

**Evidence:**
The artifact follows a principled layered structure:
1. Matrix (what) -> Classifications (rules) -> Degraded Mode (fallback behavior) -> Figma Risk Profile (risk concentration) -> Context7 (current tooling) -> Cost Tiers (team planning) -> Detection (implementation) -> Future Adapters (architecture).

This ordering is methodologically sound: it moves from static dependency facts to dynamic runtime behavior to forward-looking architecture. Each section has a clear purpose.

The Detection Protocol at line 176-179 is notably rigorous: it specifies a 5-second timeout, a 1-retry policy, and a caching strategy ("cache status for engagement session"). This level of operational specificity is appropriate for a C4 rule file.

The enforcement rules for REQ/ENH/COND (lines 53-55) are unambiguous and complete the classification definitions with behavioral consequences.

**Gaps:**
The COND classification weakens rigor: the enforcement rule for COND (line 55) says "The orchestrator evaluates the condition before checking MCP availability. If the condition is not met, the MCP is not needed." But without any instantiated example, an implementer cannot verify whether their understanding of "condition" matches the rule author's intent. The COND rule is formally correct but operationally incomplete for a C4 artifact.

**Improvement Path:**
Add one concrete example of a COND dependency in the Dependency Classifications section, even if hypothetical (e.g., "Example: If Storybook MCP were required only when evaluating components with > 50 variants, that would be classified COND").

---

### Evidence Quality (0.88/1.00)

**Evidence:**
Every section carries an HTML comment with a specific source citation:
- `<!-- Source: SKILL.md Section "MCP Integration Architecture" — sub-skill dependency matrix. -->` (line 25)
- `<!-- Source: SKILL.md Section "MCP Integration Architecture" — dependency classification definitions. -->` (line 43)
- `<!-- Source: SKILL.md Section "MCP Integration Architecture" — text-only mode. -->` (line 61)
- `<!-- Source: SKILL.md Section "Figma Dependency Risk Profile". -->` (line 101)
- `<!-- Source: SKILL.md Section "Current Jerry MCP Integration" and .context/rules/mcp-tool-standards.md MCP-001. -->` (line 122)
- `<!-- Source: SKILL.md Section "Cost Tiers". -->` (line 154)
- `<!-- Source: SKILL.md Section "Lifecycle-Stage Routing" — MCP CHECK step. -->` (line 170)
- `<!-- Source: SKILL.md Section "MCP Integration Architecture" — architecture + fallback paths only. -->` (line 196)

Each claim is independently verifiable by reading SKILL.md. The matrix was verified cell-for-cell against SKILL.md lines 400-411. All data matches.

**Gaps:**
The Context7 usage rules cite "Per MCP-001 from `.context/rules/mcp-tool-standards.md` [Context7 Integration]" — but the citation is by section name, not by rule text or anchor. For a C4 artifact, direct rule text quotation or an explicit anchor link would strengthen evidence quality. Additionally, the MCP-001 paraphrase at line 135 ("Context7 MUST be used when an agent task references an external UX library...") omits the MCP-001 qualifier about "respecting the per-question call limit enforced by the tool" and the WebSearch fallback condition, which are both in line 137 and 138 — but the ordering differs from the SSOT. This is a minor accuracy concern rather than a material error.

**Improvement Path:**
Add the MCP-001 rule ID and the full rule text (or a precise paraphrase matching the SSOT verbatim) in the Context7 Usage section. For the highest-risk data — the Figma REQ classification for `/ux-ai-first-design` — add a note referencing the specific SKILL.md line number (411) for direct verification.

---

### Actionability (0.90/1.00)

**Evidence:**
The file is operationally actionable across three implementation surfaces:

1. **Agent implementers:** The enforcement rules (lines 53-55) specify exactly what the orchestrator MUST do for each dependency class. The degraded-mode disclosure template (lines 90-95) provides a copy-paste-ready output format.

2. **Orchestrator implementation:** The Detection Protocol (lines 176-179) is sufficiently concrete to implement: probe Context7 with a specific call type, 5-second timeout, 1 retry, cache result, disclose to user. No ambiguity in the protocol.

3. **Adapter roadmap:** The Future MCP Adapters section provides priority ordering (HIGH/MEDIUM/LOW), authentication type (OAuth2 vs. API key vs. local endpoint), and a standard adapter pattern template. An engineer starting adapter work has a clear starting point.

4. **Cost tier routing:** The Cost Tier Routing paragraph (lines 164-165) explicitly describes how the orchestrator uses cost tier data (< 20% capacity -> Wave 1 only recommendation -> user decides), which is directly implementable.

**Gaps:**
The wave-in-the-cost-tier description "Free tier ($0) explicitly excludes Figma-dependent sub-skills at full capability" at line 116 is actionable but slightly imprecise: the Free tier does include ux-heuristic-eval (which has REQ Figma) — it just runs in degraded mode. The statement could mislead an implementer into blocking the sub-skill entirely rather than routing to degraded mode.

**Improvement Path:**
Revise line 116 to: "Free tier ($0) runs Figma-dependent sub-skills in degraded mode (screenshot-input fallback), not at full capability." This removes ambiguity about whether Free-tier users are blocked entirely or routed to fallback.

---

### Traceability (0.72/1.00)

**Evidence:**
Section-level source provenance is present via HTML comments on every section (see Evidence Quality analysis above). Cross-references to sibling rule files are specified by both filename and anchor (e.g., "`skills/user-experience/rules/ux-routing-rules.md` (MCP CHECK step in lifecycle triage)"). The navigation table covers all 8 sections with anchor links. The intro blurb identifies all four sibling rule files. The footer specifies parent skill, parent SKILL.md, sibling rules, and creation/update dates.

**Gaps:**
Three specific traceability gaps:

1. **UX-CI-007 "MCP ownership" claim is not traceable.** The intro states "ci-checks.md (CI gate UX-CI-007 validates MCP ownership in kickoff signoff)." Verification of ci-checks.md shows UX-CI-007 is "Signoff File Structure — All required fields non-empty." The MCP ownership claim appears only in the ci-checks.md intro description (line 5 of that file), not in the UX-CI-007 gate specification itself. The claim in mcp-coordination.md's intro therefore traces to a description, not to a defined gate criterion. A reader cannot confirm MCP ownership is explicitly part of the signoff structure from the available evidence.

2. **mcp-tool-standards.md reference is section-name-only.** The Context7 Usage section cites "`.context/rules/mcp-tool-standards.md` [Context7 Integration]" but does not quote the specific rule ID (MCP-001) in the section intro — it appears later (line 133) but is not anchored. For a C4 artifact claiming traceability to an SSOT, the first citation should include the full rule ID.

3. **PROJ-022 scope claim is not traceable.** "Future MCP Adapters" and "Figma MCP adapter is architecture-only in PROJ-022" appears three times, but there is no path to a PROJ-022 artifact (e.g., PROJ-022 PLAN.md or a worktracker entity) in the traceability chain. The scoring context confirms PROJ-022 is the parent project, but the rule file itself does not include a reference path to verify the scope deferral claim.

**Improvement Path:**
1. Update the UX-CI-007 reference to: "ci-checks.md (CI gate UX-CI-007 validates kickoff signoff file structure; signoff fields include MCP ownership per ci-checks.md [Wave Gate Compliance] section)" — or add an explicit MCP ownership field to the UX-CI-007 gate definition in ci-checks.md.
2. Add MCP-001 as the opening citation in the Context7 Usage section intro: "Per MCP-001 (`.context/rules/mcp-tool-standards.md` [Context7 Integration]):" before the rule list.
3. Add a PROJ-022 reference path in the Future MCP Adapters section: "Architecture scope: `projects/PROJ-022-user-experience-skill/PLAN.md` (adapter implementation deferred to post-PROJ-022)."

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.72 | 0.85+ | Fix three traceability gaps: (a) add PROJ-022 path reference in Future MCP Adapters section; (b) add MCP-001 rule ID as opening citation in Context7 Usage intro; (c) clarify UX-CI-007 "MCP ownership" by updating ci-checks.md UX-CI-007 gate definition to explicitly list MCP ownership as a required field. |
| 2 | Completeness | 0.90 | 0.95+ | Address the COND definition-without-instantiation gap: add either a note explaining no current sub-skills have COND dependencies, or a hypothetical example showing when COND would apply. |
| 3 | Internal Consistency | 0.88 | 0.93+ | (a) Restructure Degraded Mode table to visually separate "currently exercisable" (Context7) from "future-only" (Figma/Miro/etc.) fallbacks; (b) Revise Free tier statement at line 116 to clarify degraded mode routing vs. outright exclusion. |
| 4 | Evidence Quality | 0.88 | 0.93+ | Strengthen MCP-001 citation to include full paraphrase matching the SSOT verbatim; add SKILL.md line 411 reference to the `/ux-ai-first-design` REQ Figma entry in the matrix note for direct verification. |
| 5 | Methodological Rigor | 0.90 | 0.93+ | Add a COND instantiation example (even hypothetical) in the Dependency Classifications section to complete the methodology definition. |

---

## Leniency Bias Check
- [x] Each dimension scored independently before composite computation
- [x] Evidence documented for each score with specific line references
- [x] Uncertain scores resolved downward (Traceability held at 0.72 despite partial source comments, because the UX-CI-007 claim is unverifiable)
- [x] First-draft calibration considered (this is a rule file, not first draft — but calibration anchors applied: 0.92 = genuinely excellent, 0.95+ = essentially perfect for C4)
- [x] No dimension scored above 0.95 (max is 0.90 for three dimensions)
- [x] C4 threshold (0.95) held to strict standard — 0.876 is correctly below threshold despite the document being substantively sound

---

## Session Context Protocol

```yaml
verdict: REVISE
composite_score: 0.876
threshold: 0.95
weakest_dimension: Traceability
weakest_score: 0.72
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Fix UX-CI-007 traceability: update ci-checks.md gate definition to explicitly list MCP ownership as a required signoff field"
  - "Add PROJ-022 artifact path reference in Future MCP Adapters section"
  - "Promote MCP-001 rule ID to opening citation in Context7 Usage section"
  - "Resolve COND definition-without-instantiation: add note or hypothetical example"
  - "Restructure Degraded Mode table to separate currently-exercisable vs. future-only fallbacks"
  - "Revise Free tier statement (line 116) to clarify degraded-mode routing vs. outright exclusion"
```
