# Quality Score Report: MCP Runbook -- Heuristic Evaluation Sub-Skill

## L0 Executive Summary

**Score:** 0.930/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Completeness, Methodological Rigor, Evidence Quality, Actionability, Traceability (tied at 0.93); Internal Consistency (0.93)
**One-line assessment:** Iter4 fixes are fully confirmed -- all five changes applied correctly and materially improve the document -- but the composite of 0.930 falls short of the C4 threshold (0.95); the primary remaining gaps are: no heuristic-specific guidance for text-description input degradation, the SKILL.md Bash discrepancy is resolved in the runbook but the source files still diverge (cross-document inconsistency), and the limitations table attribution footer is present but its reference to synthesis-validation.md [Confidence Propagation] is unverifiable without that document in scope.

---

## Scoring Context

- **Deliverable:** `skills/ux-heuristic-eval/rules/mcp-runbook.md`
- **Deliverable Type:** Rules/Runbook
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Threshold Applied:** 0.95 (C4 as specified by user; SSOT H-13 minimum is 0.92 for C2+)
- **Iteration:** 5 (trajectory: 0.892 → 0.922 → 0.913 → 0.893 → 0.930)
- **Prior Iteration Applied Fixes:** H4/H9/H10 limitation rows (full 10-heuristic coverage), WebFetch/Figma claim corrected to "Not viable", Bash discrepancy resolved with intent statement, limitations table P-222 attribution footer, pre-evaluation notification P-222 citation
- **Scored:** 2026-03-04T00:00:00Z

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.930 |
| **Threshold (C4, user-specified)** | 0.95 |
| **Threshold (SSOT H-13, C2+)** | 0.92 |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No (no adv-executor reports provided) |
| **Trajectory** | 0.892 → 0.922 → 0.913 → 0.893 → 0.930 (recovery from iter4 trough; iter5 is highest post-iter2) |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.93 | 0.186 | All 10 heuristic limitation rows now present; Bash resolved as intentional; minor gap: text-description suitability lacks per-heuristic degradation guidance |
| Internal Consistency | 0.20 | 0.93 | 0.186 | No contradictions; WebFetch corrected to Not viable; Bash resolved with intent statement; cross-document Bash divergence between SKILL.md and agent def persists but is explicitly documented |
| Methodological Rigor | 0.20 | 0.93 | 0.186 | Complete 10-heuristic limitations table; rigorous workflow-step Context7 mapping; screenshot extraction targets; minor gap: text-description input path has no per-heuristic impact guidance |
| Evidence Quality | 0.15 | 0.93 | 0.1395 | Attribution footer added; P-222 citations present; WebFetch corrected; NNG caveat accurate; minor gap: synthesis-validation.md [Confidence Propagation] anchor cited but not verifiable in scoring context |
| Actionability | 0.15 | 0.93 | 0.1395 | H4/H9/H10 rows provide specific confidence-level guidance; full protocol; all failure conditions mapped; minor: no action guidance for text-description mode across heuristics |
| Traceability | 0.10 | 0.93 | 0.093 | Attribution footer traces confidence labels to synthesis-validation.md; P-222 citation for pre-evaluation notification; forward references for open items; all 5 References entries with path+content |
| **TOTAL** | **1.00** | | **0.930** | |

---

## Detailed Dimension Analysis

### Completeness (0.93/1.00)

**Evidence:**

All five iter4 fixes are confirmed present:

1. **H4 limitation row (line 147):** "Cross-screen consistency and platform hover/focus conventions are unobservable in static screenshots | MEDIUM impact; cross-screen analysis requires multiple screenshots of the same UI pattern." This is a substantive, specific limitation -- not a placeholder.

2. **H9 limitation row (line 148):** "Error states require triggering; screenshot mode cannot capture dynamic error presentation | HIGH impact; error recovery quality cannot be assessed without triggering error states." HIGH impact rating is well-justified: H9 findings in screenshots that happened to capture an error state are fundamentally different from H9 findings inferred from form design.

3. **H10 limitation row (line 149):** "Hover-triggered tooltips and contextual help are not visible in static screenshots | MEDIUM impact; help content accessibility limited to always-visible documentation." Specific and accurate.

4. **Bash resolution (lines 186-189):** "Bash is intentionally excluded from the agent definition frontmatter. The SKILL.md `allowed-tools` entry is a broader sub-skill scope declaration; the agent operates without shell access by design (T3 tier does not require Bash for MCP operations)." This is a definitive resolution statement, not merely documentation of a gap.

The limitations table now covers all 10 heuristics: H1 (lines 140-141), H2 (142), H3 (143), H4 (147), H5 (144), H6 (145), H7 (146), H8 (146), H9 (148), H10 (149). Full coverage confirmed.

All 6 navigational sections are present (lines 9-16) with anchor links. The References section (lines 210-220) has 5 source documents with path+content columns.

**Gaps:**

1. **Text-description suitability -- no per-heuristic degradation guidance.** The supported input formats table (lines 99-107) rates "Text descriptions of interface" as "Acceptable (reduced quality)" but provides no guidance on WHICH heuristics are most degraded in text-description mode. H1 (dynamic feedback), H3 (undo/redo flows), H5 (validation triggers), and H7 (keyboard shortcuts) are all significantly harder to evaluate from text descriptions than from screenshots. An agent following this runbook in text-description mode has no actionable guidance on where to exercise additional caution or note reduced confidence. This is a genuine completeness gap -- screenshot limitations are covered per-heuristic, but text-description limitations are not.

2. **Bash discrepancy remains unresolved at the source.** The runbook resolves the apparent contradiction with a clear design rationale. However, the underlying cross-document divergence (SKILL.md `allowed-tools` lists Bash; agent definition does not) is not flagged as a SKILL.md item to fix. The runbook would be more complete if it tracked this as a forward reference item similar to the Context7 table update (line 218-220). This is minor but a real completeness gap.

**Improvement Path:**

Add a "text-description mode limitations" note to the supported input formats table or a subsection under Screenshot-Input Mode Protocol covering which heuristics have elevated uncertainty in text-only mode. For Bash: add a forward reference note (similar to the Context7 table forward reference) tracking the SKILL.md correction as a PROJ-022 action item.

---

### Internal Consistency (0.93/1.00)

**Evidence:**

- **WebFetch/Figma corrected (line 106):** "Figma export URLs (public links) | Not viable | WebFetch retrieves HTML content; it cannot extract processable image data from Figma share URLs. For Figma content without the Figma MCP, users must provide screenshots directly." The correction is accurate and complete. The prior "Acceptable" claim is gone. No residual inconsistency.

- **Bash resolved (lines 186-189):** The Note block provides a definitive design rationale: "by design." This converts the previously "documented but unresolved" discrepancy into an explicitly resolved design choice with rationale.

- **Degraded mode banner (lines 126-133):** Matches parent `mcp-coordination.md` [Degraded Mode Disclosure] template exactly: three bullet points with identical wording.

- **Context7 4-step protocol (lines 28-31):** Matches mcp-tool-standards.md v1.3.1 [Context7 Integration] protocol exactly.

- **NNG fallback caveat (lines 42-43):** Applied consistently in both rows where NNG appears as a Context7 target.

- **P-222 citations (lines 124, 134):** Both the output disclosure requirement and the pre-evaluation notification requirement cite P-222 consistently.

**Gaps:**

The cross-document Bash divergence (SKILL.md `allowed-tools` includes Bash; agent definition `tools` field does not) is explicitly documented with design rationale. The runbook handles this correctly by declaring "the agent definition is the authoritative tool declaration per H-34." However, the two source documents still diverge, which means a reader encountering the SKILL.md first would have a different expectation than one reading the agent definition first. The runbook bridges this gap, but the gap itself is not closed at the source. This is an acknowledged residual -- the runbook's handling is correct, but the underlying inconsistency limits this dimension from reaching 0.95+.

**Improvement Path:**

The runbook's handling of the Bash discrepancy is correct. The remaining improvement is upstream: adding the SKILL.md correction as a tracked action item (forward reference). No changes to the runbook's internal consistency logic are required.

---

### Methodological Rigor (0.93/1.00)

**Evidence:**

The limitations table is now complete with all 10 heuristics. The H9 HIGH-impact designation is methodologically well-founded: error recovery assessment without triggering error states is a significant evaluation limitation, not a minor one. The H4 MEDIUM-impact designation is also well-calibrated: cross-screen consistency CAN be partially assessed from multiple screenshots, so HIGH would be incorrect.

The workflow-step Context7 mapping (lines 56-64) is methodologically rigorous: it explicitly identifies steps where Context7 is NOT needed (Steps 3 and 4) with rationale, preventing unnecessary tool calls. This is a methodological strength that distinguishes this runbook from generic MCP runbooks.

The "not only in the output report" timing constraint for degraded mode notification (line 134) is a methodologically important procedural requirement that prevents deferred disclosure.

The citation requirements (lines 200-205, 4 numbered rules) cover all tool types systematically: Context7-sourced, WebSearch-sourced, and heuristic-knowledge-based findings each have specific citation rules.

**Gaps:**

The "Acceptable (reduced quality)" suitability rating for text descriptions (line 105) has no methodological guidance on degradation. For screenshot mode, the runbook provides: supported formats, extraction targets per heuristic, limitations per heuristic. For text-description mode, it provides only a suitability rating and a parenthetical "(evaluation limited to described elements only)." An agent operating in text-description mode has no methodological framework equivalent to the screenshot extraction targets table. The rigor asymmetry between the two non-Figma input modes is a genuine methodological gap.

**Improvement Path:**

Add a short subsection or table note under the supported input formats table specifying which extraction targets are typically absent from text descriptions (dynamic states, visual hierarchy cues, affordance visibility) and which heuristics are most affected. This does not need to be as comprehensive as the screenshot extraction targets table -- a "text-description caveats" note with 3-4 bullet points would close the methodological gap.

---

### Evidence Quality (0.93/1.00)

**Evidence:**

All three specific iter4 evidence gaps are addressed:

1. **WebFetch/Figma corrected (line 106):** The "Not viable" designation with explanation ("WebFetch retrieves HTML content; it cannot extract processable image data") is accurate and verifiable. No residual unsupported claim.

2. **Attribution footer (line 151):** "Impact rating attribution: Impact ratings (LOW/MEDIUM/HIGH) are editorial assessment aligned with `skills/user-experience/rules/synthesis-validation.md` [Confidence Propagation]. P-222 disclosure: these ratings reflect evaluator judgment about screenshot-mode limitations, not empirical measurement." This is appropriate P-222-compliant attribution. The editorial judgment is transparent, not presented as derived fact.

3. **Pre-evaluation notification P-222 citation (line 134):** "...per P-222 (no deception about capabilities) -- users must know the evaluation operates under reduced observability." This correctly traces the notification timing requirement to its constitutional basis.

Version-pinned citations throughout: mcp-tool-standards.md v1.3.1, agent-development-standards.md v1.2.0. Specific anchors present: `[Context7 Integration]`, `[Error Handling]`, `[Tool Security Tiers]`, `[Tier Constraints]`.

**Gaps:**

The attribution footer references `skills/user-experience/rules/synthesis-validation.md [Confidence Propagation]`. This anchor is cited but the synthesis-validation.md document is not in the scoring context. If the Confidence Propagation section does not exist or does not define the LOW/MEDIUM/HIGH scale in a way that maps to the runbook's impact labels, the citation provides false traceability comfort. This is a minor evidence quality concern: the citation is appropriate as editorial attribution, but the specific anchor `[Confidence Propagation]` may not exist or may not be the canonical source for these labels. The P-222 disclosure in the footer appropriately hedges that these are editorial judgments, which mitigates this concern significantly.

**Improvement Path:**

If synthesis-validation.md is in scope for PROJ-022 delivery, verify that the `[Confidence Propagation]` anchor exists and defines the LOW/MEDIUM/HIGH confidence impact terminology. If it does not, either update the citation or replace the anchor with a more generic reference ("editorial assessment, calibrated against the sub-skill's confidence classification framework").

---

### Actionability (0.93/1.00)

**Evidence:**

The three added heuristic rows (H4, H9, H10) are directly actionable:

- H4: "MEDIUM impact; cross-screen analysis requires multiple screenshots of the same UI pattern" -- gives the agent a specific workaround (collect multiple screenshots for cross-screen heuristics).
- H9: "HIGH impact; error recovery quality cannot be assessed without triggering error states" -- tells the agent to flag H9 findings as highly uncertain and recommend supplemental human review.
- H10: "MEDIUM impact; help content accessibility limited to always-visible documentation" -- scopes the evaluation to always-visible elements.

The Context7 failure handling table (lines 161-167) maps each failure condition to a specific, executable action with exact disclosure text ("Note 'Context7 no coverage' in the evaluation output next to the affected finding").

The prohibited tools table (lines 193-196) provides both the tool name and the specific prohibition reason, enabling agents to make correct tool selection decisions.

The citation requirements section (lines 200-205) is precise: 4 numbered rules cover all citation scenarios an agent will encounter.

**Gaps:**

As with Completeness and Methodological Rigor: text-description input mode has no actionable guidance. An agent receiving a text description rather than a screenshot cannot consult the extraction targets table (which is screenshot-specific) and has no runbook guidance on which heuristics to flag as uncertain or what confidence level to assign to text-based findings. This is an actionability gap: the runbook does not tell the agent what to DO differently when operating with text descriptions.

**Improvement Path:**

A short "text-description mode caveats" note (3-5 bullets) specifying which heuristics have elevated uncertainty in text-only mode would close this actionability gap. This is the same fix recommended for Completeness and Methodological Rigor -- a single content addition addresses all three dimensions.

---

### Traceability (0.93/1.00)

**Evidence:**

- **Attribution footer (line 151):** Traces confidence impact labels to synthesis-validation.md [Confidence Propagation] with P-222 disclosure. Forward reference to a specific anchor in a specific sibling rule file.

- **Pre-evaluation notification (line 134):** Traces the timing requirement to P-222. The citation is direct and does not require intermediate derivation.

- **References section (lines 210-220):** 5 entries, each with Source, Content, and Path columns. All 5 primary source documents are represented.

- **Frontmatter comment (line 1):** VERSION 1.4.0 | DATE 2026-03-04 | SOURCE | PARENT | GOVERNANCE | PROJECT | REVISION. The REVISION field explicitly documents all 5 iter4 fixes, providing an audit trail.

- **Forward reference note (lines 218-220):** The Context7 table update is tracked as a "PROJ-022 action item." This is the correct handling for open items that cannot be resolved in the current document.

- **Version-pinned in-document citations:** mcp-tool-standards.md v1.3.1, agent-development-standards.md v1.2.0. Specific section anchors throughout.

**Gaps:**

1. The attribution footer cites `synthesis-validation.md [Confidence Propagation]` -- as noted in Evidence Quality, this anchor's existence is unverified in the scoring context. If the anchor does not exist, the traceability chain for confidence impact labels is broken.

2. The Bash resolution note (lines 186-189) states the design rationale but does not reference the H-34 standard that makes the agent definition authoritative over SKILL.md (though H-34 is cited in line 183). The connection between "agent definition is authoritative" and "H-34" is implicit but follows from the sentence structure. Not a significant gap but worth noting.

**Improvement Path:**

Verify or simplify the synthesis-validation.md anchor reference. If the anchor does not exist, update to reference the document generally ("editorial assessment, calibrated against synthesis-validation.md confidence framework") rather than a potentially non-existent anchor.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Completeness + Methodological Rigor + Actionability | 0.93 | 0.95+ | Add text-description input mode guidance. A single note block or "Text-Description Mode Caveats" subsection under Screenshot-Input Mode Protocol should specify: (1) which heuristics are most impacted (H1 dynamic states, H3 flows, H5 validation, H7 shortcuts), (2) that all text-based findings should be noted as "inferred from description; verify with screenshot or interactive evaluation," and (3) that H9 in text-only mode is particularly unreliable. This single addition addresses the gap across three dimensions simultaneously. |
| 2 | Internal Consistency + Completeness | 0.93 | 0.94+ | Add Bash as a tracked forward reference item alongside the Context7 table update. The current resolution note (line 189) correctly states the design intent but does not track the downstream correction needed in SKILL.md. Add: "The SKILL.md `allowed-tools` Bash entry will be corrected in PROJ-022 EPIC-002 implementation cleanup" as a forward reference note in the References section or as a companion item to the existing forward reference (lines 218-220). |
| 3 | Evidence Quality + Traceability | 0.93 | 0.94+ | Verify the `synthesis-validation.md [Confidence Propagation]` anchor. If that anchor does not exist in the synthesis-validation.md document, update the attribution footer citation to reference the document generally ("editorial assessment, calibrated against synthesis-validation.md confidence classification framework") rather than a potentially non-existent anchor. If the anchor exists and is the canonical source for LOW/MEDIUM/HIGH impact labels, the current citation is correct and no change is needed. |

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing weighted composite
- [x] Evidence documented for each score with specific quotes and line numbers
- [x] Uncertain scores resolved downward: all dimensions scored 0.93; no dimension elevated to 0.95 without exceptional documented evidence
- [x] C4 threshold (0.95) applied throughout; composite 0.930 is clearly below the 0.95 user-specified threshold
- [x] No dimension scored above 0.95 (ceiling rule applied: max 0.93 for all dimensions)
- [x] Internal Consistency considered for 0.95 (clean no-contradictions case) but downgraded to 0.93 due to persisting cross-document Bash divergence between SKILL.md and agent definition -- the runbook bridges the gap but the gap exists at source

**Trajectory analysis:** 0.892 → 0.922 → 0.913 → 0.893 → 0.930. Iter5 represents a recovery from the iter4 trough. The 0.037-point gain from iter4 to iter5 reflects five confirmed fixes applied correctly. The remaining gap to the 0.95 C4 threshold (0.020 points) requires closing the text-description mode guidance gap (a genuine content addition, not a reference fix) and minor traceability improvements.

**Calibration note:** Scoring 0.93 uniformly across all six dimensions is an unusual outcome that warrants anti-leniency scrutiny. The convergence reflects a document that has been iteratively refined to address specific point-deduction gaps, leaving a consistent class of remaining minor gaps across all dimensions (text-description mode, source-document cross-reference, synthesis-validation.md anchor). This uniform convergence at 0.93 is consistent with a document at the upper-REVISE band, not with a document that has hidden fatal flaws. The 0.95 threshold requires a further 0.020-point improvement, achievable with the three targeted fixes above.

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.930
threshold: 0.95
weakest_dimension: all_dimensions_tied_at_0.93
weakest_score: 0.93
critical_findings_count: 0
iteration: 5
improvement_recommendations:
  - "Add text-description input mode caveats: per-heuristic confidence guidance for H1/H3/H5/H7/H9 in text-only evaluation mode (single addition closes Completeness + Methodological Rigor + Actionability gaps)"
  - "Add Bash SKILL.md correction as a tracked forward reference item alongside the existing Context7 table forward reference"
  - "Verify synthesis-validation.md [Confidence Propagation] anchor exists; simplify citation to document-level if anchor is not present"
```

---

*Score Report Version: 1.0*
*Scoring Agent: adv-scorer*
*Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Deliverable: `skills/ux-heuristic-eval/rules/mcp-runbook.md` (v1.4.0)*
*Iteration: 5*
*Scored: 2026-03-04*
