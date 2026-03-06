# Quality Score Report: Switch Interview Guide Template (Iteration 2)

## L0 Executive Summary

**Score:** 0.931/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Internal Consistency (0.89)

**One-line assessment:** Iteration 2 closes all five iter1 gaps with precision — inline citations added, Participant Screening section complete, sample size guidance integrated — but a new minor consistency gap (canonical name in AI note vs. forces section) and a thin traceability gap (no cross-reference from the template to ORCHESTRATION.yaml or project ADR chain) hold the composite below the C4 threshold of 0.95; three targeted fixes will close the delta.

---

## Scoring Context

- **Deliverable:** `skills/ux-jtbd/templates/switch-interview-guide.md`
- **Deliverable Type:** Template (interview protocol)
- **Criticality Level:** C4
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Iteration:** 2
- **Prior Score:** 0.872 (iter1)
- **Scored:** 2026-03-04T00:00:00Z

### Companion Artifacts Read

| Artifact | Path | Purpose |
|----------|------|---------|
| Rules file | `skills/ux-jtbd/rules/jtbd-methodology-rules.md` | Consistency check against force model, job statement rules, citation discipline |
| Agent definition | `skills/ux-jtbd/agents/ux-jtbd-analyst.md` | Consistency check against agent methodology and canonical names |
| Parent SKILL.md | `skills/ux-jtbd/SKILL.md` | Consistency check against sub-skill spec and output format template |
| Synthesis validation | `skills/user-experience/rules/synthesis-validation.md` | Confidence classification cross-check |
| Iter1 score report | `skills/ux-jtbd/output/quality-scores/interview-guide-iter1-score.md` | Prior findings comparison |

---

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.931 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | Yes — iter1 score (0.872) and its 5 improvement recommendations |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.95 | 0.190 | All 9 content areas present including new Participant Screening section; post-interview timing note at Analysis Mapping Guide; minor gap: no worked example row in mapping tables |
| Internal Consistency | 0.20 | 0.89 | 0.178 | No contradictions with force model or job rules; sample-size guidance consistent; canonical name fixed in forces header but "Moesta/Spiek" (without "four forces") persists in AI note (line 170 header vs. footer text) |
| Methodological Rigor | 0.20 | 0.95 | 0.190 | 5-10 interview minimum now present at timeline header; 18-month recency screener correctly sourced to Moesta; post-interview 24-hour mapping guidance added; all Moesta stage sequence and supplementary-probe framing intact |
| Evidence Quality | 0.15 | 0.93 | 0.140 | Inline `[Tier 2]` citations added at duration row, environment row, timeline header, forces header, job discovery header; footer with two complete bibliographic references; 18-month claim cited; 5-10 interview claim cited |
| Actionability | 0.15 | 0.93 | 0.140 | Verbatim screener questions ready for use; qualification rule clearly stated; sample size guidance actionable; analysis mapping guide SKILL.md cross-reference present; minor gap: no example filled-in mapping row |
| Traceability | 0.10 | 0.91 | 0.091 | Header comment with VERSION/DATE/SKILL/AGENT/SOURCE present; footer with constitutional compliance and bibliographic citations; all section citations inline; SKILL.md output template cross-referenced; gap: no link to project ADR chain or ORCHESTRATION.yaml decision basis |
| **TOTAL** | **1.00** | | **0.931** | |

---

## Detailed Dimension Analysis

### Completeness (0.95/1.00)

**Evidence:**

All 9 content areas that a complete switch interview guide requires at C4 criticality are now present:

1. **Participant Screening** (lines 29-55, new in v1.1.0): Who qualifies, 18-month recency criterion, 4 screener questions, qualification rule, minimum sample size 5-10. This directly closes the iter1 Priority 2 gap.
2. **Interview Protocol logistics** (lines 62-68): Duration, format, recording, note-taking, environment -- unchanged, complete.
3. **Ethical considerations** (lines 70-76): Informed consent, anonymity, right to withdraw, data handling, P-022 compliance -- complete.
4. **Rapport-building opening with verbatim transition** (lines 78-90): 3 warm-up questions, 5-7 minute guidance, transition sentence -- complete.
5. **6-stage switching timeline with 21 labeled questions** (lines 94-165): Minimum interview count note now present at section header (lines 96-98). All 6 stages with 3-4 questions each.
6. **Four forces supplementary questions** (lines 168-229): 20 labeled questions across push/pull/anxiety/habit -- complete.
7. **Job discovery questions** (lines 232-268): 13 labeled questions across functional/social/emotional -- complete.
8. **Follow-up probes** (lines 272-311): 14 probes across 4 categories -- complete.
9. **Analysis Mapping Guide** (lines 313-375): Response-to-force, response-to-job, job statement extraction (5-step procedure), timeline-to-force mapping, force rating from interview data, SKILL.md output artifact cross-reference. Post-interview 24-hour timing guidance now present at section header (lines 317-318). This closes the iter1 post-interview documentation gap.
10. **AI-Augmented Analysis Note** (lines 378-395): P-022 disclosure with 5 specific limitations, synthesis confidence MEDIUM classification -- complete.

**Gaps:**

1. **No worked example row in the mapping tables.** The Response-to-Force Mapping and Response-to-Job Mapping tables (lines 322-335) define the column structure but contain no populated example rows. The rules file does not contain worked mapping examples either. For a C4 practitioner artifact intended for practitioners who may be new to the methodology, a single filled-in row (e.g., one example response pattern mapped to a force) would close the last completeness gap. This is minor because the 5-step job statement extraction procedure does provide a procedural worked example.

**Improvement Path:**

Add one illustrative example row to the Response-to-Force Mapping table showing a sample interview excerpt mapped to a force (e.g., "I kept hitting errors every time I tried to export — it just never worked" -> Push, Switch Force Analysis Push column). This closes the worked-example gap without adding a new section.

---

### Internal Consistency (0.89/1.00)

**Evidence:**

The template is consistent with the companion artifact family on all substantive methodology:

- **Force model alignment:** Push/Pull/Anxiety/Habit defined identically across the template forces header (line 170), the rules file (`jtbd-methodology-rules.md` lines 164-183), and the SKILL.md Phase 3 methodology (SKILL.md lines 183-339).
- **Force rating scale alignment:** The 1-5 integer scale with signal anchors (lines 366-373) exactly matches the rules file Switch Force Analysis Rules rating scale (rules file lines 186-195). The interview signals (brief unemotional reference = 1, volunteered unprompted = 3, dominant narrative = 5) are methodologically precise and consistent.
- **Job statement canonical format:** The 5-step extraction procedure (lines 340-349) cross-references the rules file by section name for both Job Statement Rules and Job Classification Rules, and the three-clause format (situation/motivation/outcome) matches the canonical format across all parent artifacts.
- **Sample size alignment:** The 5-10 minimum interview guidance in the template (line 54 and line 96) matches the rules file's sample size guidance in the Opportunity Scoring section (rules file lines 148-158). The SKILL.md synthesis hypothesis validation table requires "3-5 interviews for MEDIUM->HIGH upgrade" (SKILL.md lines 620-625) -- this is a different threshold for a different purpose (confidence upgrade vs. pattern recognition), and the template's 5-10 figure is the correct one for pattern recognition per Moesta (2020).
- **Confidence classification alignment:** The AI note (line 386) states "MEDIUM confidence per `skills/user-experience/rules/synthesis-validation.md`" -- this correctly matches the synthesis validation rules (synthesis-validation.md line 60).
- **Canonical name fix applied:** The forces section header now reads "the Moesta/Spiek four forces model" (line 170), aligning with the rules file ("Moesta/Spiek four forces model", rules file line 162) and agent definition ("Moesta/Spiek four forces framework", agent line 37). This closes the iter1 Priority 5 gap.

**Gaps:**

1. **Inconsistency between canonical name in the AI note footer vs. inline text.** The footer (line 400) cites "Moesta, B. and Spiek, C. (2014). The Jobs-to-Be-Done Handbook. Re-Wired Group." — the citation is correct and complete. However, within the AI note body (line 384), the text refers to "the ux-jtbd-analyst agent is used to synthesize interview data" without specifying the four-forces context. This is not a hard inconsistency but represents a partial name consistency: the forces header uses the canonical "four forces model" while the body prose and AI note omit the force model name when it appears in narrative context. The inconsistency is minor but is the clearest gap in internal consistency.

2. **SKILL.md output template cross-reference at line 374 mentions the output format is in "SKILL.md [Output Format Template]" but the SKILL.md section heading is "Output Format Template" within the "Output Specification" section (SKILL.md lines 449-528).** The cross-reference is correct in substance but the section link is imprecise — it refers to the heading as "Output Format Template" which matches the SKILL.md heading exactly. This is actually accurate on review; no gap remains here.

**Improvement Path:**

The primary internal consistency fix is minor: in the AI note section, change "the ux-jtbd-analyst agent is used to synthesize interview data, the following limitations apply" to "the ux-jtbd-analyst agent is used to synthesize switch interview data using the Moesta/Spiek four forces model, the following limitations apply" — this propagates the canonical name consistently into the prose body of the AI note, closing the only remaining name inconsistency.

---

### Methodological Rigor (0.95/1.00)

**Evidence:**

The iter1 methodological gaps are fully closed:

- **Minimum interview count guidance added:** Lines 96-98 state explicitly: "A minimum of 5-10 switch interviews with distinct participants is required before patterns can be reliably identified from timeline data. A single interview produces individual insight, not pattern recognition -- this is a fundamental Moesta methodology constraint." This directly addresses the iter1 Priority 3 gap. The source citation `Source: Moesta (2020) [Tier 2]` is present.
- **18-month recency guidance added with citation:** Lines 37-38 cite "Moesta (2020) [Tier 2]" for the 18-month recency criterion in the Participant Screening section. Methodologically this is correct: memory fidelity for episodic switching events degrades substantially beyond 18 months.
- **Post-interview 24-hour mapping guidance added:** Lines 317-318 provide explicit timing guidance: "Apply this mapping guide within 24 hours of the interview while recall is fresh." This bridges the iter1 gap between "notes taken" and "analysis applied."
- **Supplementary-probe framing preserved:** Line 172 still correctly states "The interviewer does not need to ask all of these -- select the ones that fill gaps in the timeline story." The timeline-first methodology constraint is intact.
- **Chronological ordering preserved:** All 6 stages in correct Moesta sequence (First Thought -> Passive Looking -> Active Looking -> Decision -> Consumption -> Satisfaction).
- **One-on-one format with anti-group-dynamics rationale:** Line 68 cites Moesta (2020) for the environment constraint.

**Gaps:**

1. **No distinction between initial engagement sample size and hypothesis validation sample size.** Line 54 states: "For initial JTBD pattern identification, aim for 10+ interviews; for hypothesis validation, 5 interviews may suffice if the target segment is well-defined." This is a sound methodological distinction, but the SKILL.md synthesis hypothesis validation table (SKILL.md lines 620-625) specifies "3-5 interviews for MEDIUM->HIGH confidence upgrade." The template's "5" minimum for hypothesis validation aligns with the low end of the SKILL.md range, but the distinction between pattern-recognition (10+) and hypothesis-validation (5) is slightly different from the SKILL.md framing (confidence upgrade). A practitioner reading both could find this nuance confusing. This is a methodology documentation clarity gap, not a methodological error. The score 0.95 reflects that the rigor is genuinely excellent with only this very minor clarity issue.

**Improvement Path:**

Add a parenthetical clarification at line 54: replace "for hypothesis validation, 5 interviews may suffice if the target segment is well-defined" with "for hypothesis validation against existing job hypotheses (consistent with the MEDIUM->HIGH confidence upgrade threshold in `skills/user-experience/rules/synthesis-validation.md`), 5 interviews may suffice if the target segment is well-defined." This aligns the template's language with the synthesis-validation.md threshold framing.

---

### Evidence Quality (0.93/1.00)

**Evidence:**

The iter1 evidence quality gaps are substantially closed. Inline `[Tier 2]` citations now appear at:

- **Duration row** (line 64): `Source: Moesta (2020) [Tier 2]` — closes iter1 Priority 1 gap point 1.
- **Environment row** (line 68): `Source: Moesta (2020) [Tier 2]` — closes iter1 Priority 1 gap point 3 ("social dynamics" claim now cited).
- **Timeline section header** (line 98): `Source: Moesta (2020) [Tier 2]` — closes iter1 Priority 1 gap point 4 (6-stage structure attributed to Moesta's demand-side sales model).
- **18-month recency criterion** (line 37): `Source: Moesta (2020) [Tier 2]` — new claim, correctly cited.
- **5-10 interview minimum** (line 54): `Source: Moesta (2020) [Tier 2]` — new claim, correctly cited.
- **Forces model header** (line 170): `Source: Moesta (2020) [Tier 2]` — closes iter1 Priority 4 forces header gap.
- **Job discovery header** (line 234): `Source: Christensen (2016) [Tier 2]; Ulwick (2016) [Tier 2]` — closes iter1 Priority 4 job discovery header gap.
- **Rapport-building opening** (line 78 comment): `Source: Moesta (2020) [Tier 2]` — present in HTML comment.

Footer citations are complete with two full bibliographic entries (Moesta 2020, Moesta-Spiek 2014, lines 399-400).

The citation discipline is now meaningfully aligned with the rules file, which uses the same `Source: Author (year) [Tier N]` inline format throughout.

**Gaps:**

1. **The "5-7 minutes" rapport-building duration claim.** Line 78 has a comment `<!-- Source: Moesta (2020) [Tier 2] -->` but this is an HTML comment — it is not visible to a practitioner reading the rendered template. The citation exists but is invisible in the rendered output. The other citations in the body content (logistics table, timeline header) are visible because they are inside table cells or blockquotes. For the rapport-building section, the source comment should be made visible (e.g., moved into the section header text or a parenthetical note on the opening line).

2. **No citation for the "within 24 hours" post-interview mapping guidance (line 317).** This is a methodological claim about memory fidelity and recall quality that should cite a source. Moesta (2020) supports this practice, but the sentence currently has no inline attribution.

**Improvement Path:**

(1) Move the rapport-building source annotation from the HTML comment to visible text, e.g., add a parenthetical `(Source: Moesta (2020) [Tier 2])` to the section header or as a brief note before the questions. (2) Add `Source: Moesta (2020) [Tier 2]` to the 24-hour post-interview timing claim at line 317.

---

### Actionability (0.93/1.00)

**Evidence:**

The template remains highly actionable, with iter2 adding new actionable content:

- **Recruitment screener questions verbatim-ready:** The 4 screener questions (lines 45-48) are complete sentences in quotation marks, ready for use in a screening survey or pre-interview call.
- **Qualification rule is binary and unambiguous:** Lines 50-51 provide a clear qualification rule: "A participant qualifies if they answer YES to questions 1 and 2, indicate full commitment (question 3), and the switch date falls within 18 months (question 4)." The in-progress switcher flag is also specified, eliminating practitioner judgment ambiguity.
- **Sample size guidance specific and tiered:** Line 54 distinguishes pattern recognition (10+ interviews) from hypothesis validation (5), which is a practically actionable distinction.
- **SKILL.md output template cross-reference:** Line 374 directs analysts to SKILL.md [Output Format Template] for artifact population. This bridges the "analysis mapping guide -> output artifact" gap identified in iter1.
- **Post-interview timing guidance actionable:** "Within 24 hours" (line 317) and the note about tagging by timeline stage and force category (line 318) is specific enough to act on.
- **All 57 labeled questions remain verbatim-usable:** Placeholders clearly marked.

**Gaps:**

1. **No filled-in example row in the mapping tables.** The Response-to-Force Mapping (lines 322-327) and Response-to-Job Mapping (lines 329-335) tables define the column structure but have no populated example. A practitioner attempting their first post-interview mapping must infer the application from the column headers alone. This is the same gap as iter1 Priority 5 (minor), now the only remaining actionability gap.

2. **The SKILL.md cross-reference at line 374 does not specify a line range or anchor.** The SKILL.md output format template begins at line 451 in SKILL.md. The template cross-reference says "Output Format Template in `skills/ux-jtbd/SKILL.md` [Output Format Template]" — the section name match is correct and the cross-reference is functional, but practitioners using this in a large document context would benefit from knowing which section to look for.

**Improvement Path:**

Add one example row to the Response-to-Force Mapping table. The cross-reference at line 374 is adequate as-is; the section name match is sufficient for navigation.

---

### Traceability (0.91/1.00)

**Evidence:**

The template's traceability is strong and improved from iter1:

- **Header comment:** Full provenance block with TEMPLATE identifier, VERSION 1.1.0, DATE 2026-03-04, SKILL, AGENT, SOURCE citation — present (lines 1-3).
- **Navigation table:** 8-row navigation table now includes the new Participant Screening section entry (lines 14-26), matching 8 H2 sections. All section headings match the navigation entries exactly.
- **Footer:** Complete bibliographic references, template version, skill path, agent path, constitutional compliance (P-022, P-001, P-020) — present (lines 398-402).
- **Inline section citations:** Forces header (line 170), job discovery header (line 234), timeline header (line 98), rapport building HTML comment (line 78), Participant Screening recency criterion (line 37), interview minimum (line 54) — all present.
- **Analysis Mapping Guide cross-reference:** Line 374 cross-references the SKILL.md output format template. Line 347-349 cross-reference the rules file Job Statement Rules and Job Classification Rules by section name.
- **Synthesis-validation.md cross-reference:** AI note (line 386) cites synthesis-validation.md directly.
- **Constitutional compliance:** Footer (line 402) cites P-022, P-001, P-020 with descriptions.
- **Output path cited:** Line 75 cites `skills/ux-jtbd/output/{{ENGAGEMENT_ID}}/` — traceable to engagement outputs.

**Gaps:**

1. **No link to the project ADR chain or ORCHESTRATION.yaml decision basis.** The rules file (jtbd-methodology-rules.md lines 348-349) includes a "Decision Basis" footer citing "ADR-PROJ022-001, ADR-PROJ022-002, ORCHESTRATION.yaml" as the decision provenance for the methodology choices. The interview guide template does not have a corresponding decision basis citation. For a C4 deliverable, full traceability of design decisions to the project ADR chain is expected. The template's methodology choices (18-month recency, 5-10 interview minimum, 6-stage structure) are supported by Moesta citations but not traced to the project-level decision chain that justified their inclusion in this sub-skill.

2. **VERSION comment at line 1 does not include a REVISION note explaining what changed in v1.1.0.** The rules file header comment (line 1) includes a REVISION field: "iter4 quality fixes -- inline quality-enforcement.md citation...". The template's header comment at line 1 includes VERSION and DATE but no REVISION field explaining what changed from v1.0.0 to v1.1.0. For audit traceability at C4, the REVISION field provides important context for reviewers who encounter the file in a future state.

**Improvement Path:**

(1) Add a REVISION field to the header comment: `<!-- ... | REVISION: iter2 quality fixes — Participant Screening section, inline Moesta citations, sample size guidance, canonical name alignment -->`. (2) Optionally add a "Decision Basis" footer line matching the rules file pattern: `*Decision Basis: ADR-PROJ022-001, ADR-PROJ022-002, ORCHESTRATION.yaml*`. Both are small additions that complete the traceability chain for C4 review.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Internal Consistency | 0.89 | 0.95 | In the AI note section body (near line 384), propagate the canonical name "Moesta/Spiek four forces model" into the prose context so the forces section header and the AI note body use identical terminology. Estimated impact: +0.06 to Internal Consistency, composite lift ~+0.012. |
| 2 | Traceability | 0.91 | 0.97 | Add REVISION field to header comment (line 1): `REVISION: iter2 quality fixes — Participant Screening section, inline citations, sample size guidance`. Add a Decision Basis footer line mirroring the rules file pattern. Estimated impact: +0.06 to Traceability, composite lift ~+0.006. |
| 3 | Evidence Quality | 0.93 | 0.97 | Move the rapport-building source annotation (line 78) from HTML comment to visible text. Add `Source: Moesta (2020) [Tier 2]` inline to the 24-hour post-interview timing claim at line 317. Estimated impact: +0.04 to Evidence Quality, composite lift ~+0.006. |
| 4 | Completeness | 0.95 | 0.97 | Add one filled-in example row to the Response-to-Force Mapping table showing a sample interview excerpt mapped to a Push force. Estimated impact: +0.02 to Completeness, composite lift ~+0.004. |
| 5 | Methodological Rigor | 0.95 | 0.97 | Add parenthetical to line 54 aligning "5 interviews for hypothesis validation" explicitly with the synthesis-validation.md MEDIUM->HIGH confidence upgrade threshold. Estimated impact: +0.02 to Methodological Rigor, composite lift ~+0.004. |

**Projected composite after all 5 fixes:** ~0.963 (exceeds C4 threshold of 0.95)
**Projected composite after top 3 fixes only:** ~0.955 (meets C4 threshold)

---

## Leniency Bias Check

- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score with specific line references to the v1.1.0 artifact
- [x] Uncertain scores resolved downward: Internal Consistency chose 0.89 not 0.92 (the naming inconsistency is small but measurable; at C4 calibration it depresses the score); Traceability chose 0.91 not 0.93 (absent REVISION field and ADR chain link are genuine gaps at C4 level)
- [x] Iter2 re-scoring calibration applied: a score of 0.931 for a strong second draft after targeted revision is consistent with the calibration anchor (0.92 = genuinely excellent; iter2 is near but not at that level on Internal Consistency and Traceability)
- [x] No dimension scored above 0.95 without specific documented evidence (Completeness and Methodological Rigor at 0.95 reflect genuinely complete content with only minor worked-example and terminology-clarification gaps)
- [x] Weighted composite mathematically verified: (0.95 * 0.20) + (0.89 * 0.20) + (0.95 * 0.20) + (0.93 * 0.15) + (0.93 * 0.15) + (0.91 * 0.10) = 0.190 + 0.178 + 0.190 + 0.140 + 0.140 + 0.091 = 0.929... rounded to 0.929; applying anti-leniency rounding DOWN: **0.929**

> **Anti-leniency recalculation note:** The exact weighted sum is 0.929 (not 0.931 as shown in the summary — the summary table used a display-rounding artifact). The correct composite is **0.929**. The verdict and recommendations are unchanged; the gap to 0.95 is 0.021 (three targeted fixes required).

---

## Corrected Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.929 |
| **Threshold** | 0.95 (C4) |
| **Verdict** | REVISE |
| **Delta to Threshold** | -0.021 |

---

## Session Context (Handoff Schema)

```yaml
verdict: REVISE
composite_score: 0.929
threshold: 0.95
weakest_dimension: Internal Consistency
weakest_score: 0.89
critical_findings_count: 0
iteration: 2
improvement_recommendations:
  - "Propagate canonical name 'Moesta/Spiek four forces model' into AI note body prose for full naming consistency"
  - "Add REVISION field to header comment and Decision Basis footer line matching rules file pattern"
  - "Move rapport-building source from HTML comment to visible text; add inline Moesta citation to 24-hour post-interview timing claim"
  - "Add one filled-in example row to Response-to-Force Mapping table"
  - "Align line-54 hypothesis-validation guidance explicitly with synthesis-validation.md confidence upgrade threshold language"
```

---

*Score Report Version: 1.0.0*
*Scoring Strategy: S-014 (LLM-as-Judge)*
*SSOT: `.context/rules/quality-enforcement.md`*
*Agent: adv-scorer*
*Project: PROJ-022 User Experience Skill*
*Created: 2026-03-04*
