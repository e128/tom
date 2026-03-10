# Quality Score Report: GitHub Issue Drafts — Documentation & Agentic Workflows

## L0 Executive Summary
**Score:** 0.76/1.00 | **Verdict:** REVISE | **Weakest Dimension:** Traceability (0.55)
**One-line assessment:** The six ticket drafts are well-structured with clear scopes and strong security thinking, but fall short due to broken cross-referencing between tickets, an unverifiable issue number claim (#153 for EN-001 is accurate but #130/#135 lack PROJ-015/PROJ-016 grounding in the local repo), missing enforcement-mode detail in the agentic workflow design, no priority/sizing information, and a mkdocs.yml nav gap that is silently assumed rather than called out.

## Scoring Context
- **Deliverable:** `projects/PROJ-030-bugs/work/gh-ticket-drafts.md`
- **Deliverable Type:** Analysis / Design (GitHub Issue specification drafts)
- **Criticality Level:** C2 (standard; multiple files and downstream implementation work affected)
- **Scoring Strategy:** S-014 (LLM-as-Judge)
- **SSOT Reference:** `.context/rules/quality-enforcement.md`
- **Scored:** 2026-03-09T00:00:00Z

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.76 |
| **Threshold** | 0.92 (H-13) |
| **Verdict** | REVISE |
| **Strategy Findings Incorporated** | No |

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.78 | 0.156 | ACs present on all tickets; missing priority, sizing, and mkdocs nav change spec |
| Internal Consistency | 0.20 | 0.72 | 0.144 | TICKET-5 references parent only by prose description, not ticket number; TICKET-6 same; agentic tickets do not reference TICKET-5 from TICKET-4 explicitly |
| Methodological Rigor | 0.20 | 0.82 | 0.164 | CI design pattern is sound (advisory first, escalation path, no LLM in CI); escalation counter mechanism lacks implementation detail |
| Evidence Quality | 0.15 | 0.80 | 0.120 | Referenced files confirmed to exist (ci-cd-pipeline-security.md, ci-cd-supply-chain-security.md, workflows); #153 confirmed as EN-001; "Guides" section exists in mkdocs.yml but no howto/ entries yet |
| Actionability | 0.15 | 0.73 | 0.110 | Docs tickets are actionable; agentic workflow TICKET-4 leaves PR-comment format, escalation counter storage, and CI job naming unspecified |
| Traceability | 0.10 | 0.55 | 0.055 | #130 (PROJ-015) and #135 (PROJ-016) not verifiable in local repo; ticket-to-ticket links use prose not numbers |
| **TOTAL** | **1.00** | | **0.749** | |

> **Composite (rounded):** 0.75

## Detailed Dimension Analysis

### Completeness (0.78/1.00)

**Evidence:**
All six tickets include a Body, Scope or Problem statement, Acceptance Criteria checklist, and References section. The three documentation tickets (TICKET-1 through TICKET-3) specify output paths, tool invocation (`/diataxis skill, diataxis-howto agent`), and mkdocs integration. TICKET-4 includes a Security Considerations section and three-layer review requirement (/eng-team, /red-team, /adversary). TICKET-5 includes a YAML schema and initial mapping entries. TICKET-6 includes advisory-only framing and hook API reference.

**Gaps:**
1. No ticket specifies priority (P0/P1/P2) or effort estimate. GitHub Issues without priority context leave triage ambiguous for a maintainer picking up work.
2. The mkdocs.yml `Guides:` section currently lists only `playbooks/` files. None of the three documentation tickets explicitly call out the required nav entry format (e.g., `- Update SHA-pinned Action: howto/update-sha-pinned-action.md`) or note that the `docs/howto/` directory does not yet exist and must be created.
3. TICKET-4 does not specify what tool/script runs the "CI job" — is it a Python script, a shell script, a jerry CLI command, or a separate GitHub Actions composite action? The implementation choice has significant design implications and is left fully open.
4. TICKET-5's AC "Expand mappings for skill docs, architecture docs, etc." is aspirational scope stated as a required deliverable — this creates ambiguity about what constitutes done.

**Improvement Path:**
Add a priority label and rough effort estimate to each ticket. Add an explicit note that `docs/howto/` must be created and provide the exact mkdocs.yml nav entry to add. Scope TICKET-4's implementation mechanism (script vs. CLI subcommand) or explicitly mark it as a design decision to be made during implementation.

---

### Internal Consistency (0.72/1.00)

**Evidence:**
The three documentation tickets consistently reference the same related issues (#130, #135, #153) and the same two reference files. TICKET-4, TICKET-5, and TICKET-6 form a coherent three-ticket design where TICKET-5 produces the artifact TICKET-4 and TICKET-6 consume.

**Gaps:**
1. TICKET-5 references its parent as "Documentation freshness auditing workflow ticket" (prose) rather than as a ticket number or title. When these become GitHub Issues, there will be no anchor link — a reader must search by title. The same problem affects TICKET-6.
2. TICKET-4 does not mention TICKET-5 or TICKET-6 as child tickets. The decomposition relationship is implied but not stated.
3. TICKET-6 references "the source-to-doc mapping from the mapping configuration" and `.github/doc-source-map.yml` without stating that this file is created by a sibling ticket. A maintainer reading TICKET-6 in isolation sees a dependency on a file that does not exist yet with no pointer to where it comes from.
4. TICKET-2's scope says "Wire the new job into the `ci-success` gate (including skipped-state handling)" but the Acceptance Criteria does not have a corresponding check for skipped-state handling — it only has "Covers ci-success gate wiring pattern (including skipped handling)" as a single AC item that conflates the two. Minor but inconsistent with the level of granularity elsewhere.

**Improvement Path:**
Add explicit forward/backward references: TICKET-4 should list TICKET-5 and TICKET-6 as child tickets. TICKET-5 and TICKET-6 should reference the parent by ticket number, not by prose. TICKET-6 should state "Depends on: TICKET-5 (mapping file must exist)".

---

### Methodological Rigor (0.82/1.00)

**Evidence:**
The documentation tickets correctly follow Diataxis how-to methodology: each specifies a goal-oriented, procedural guide with concrete output paths and tool invocation. TICKET-4's CI design is sound: it applies advisory-before-blocking, uses deterministic file mapping (no LLM in CI loop), and defines an escalation path (3+ consecutive PRs -> error). The security considerations in TICKET-4 and TICKET-6 demonstrate awareness of supply chain risks (mapping file in-repo, no arbitrary command execution from mapping content). The three-layer review requirement (eng-team, red-team, adversary) in TICKET-4 is appropriate for an agentic CI workflow.

**Gaps:**
1. The escalation counter mechanism (TICKET-4 AC: "Escalation counter mechanism (advisory -> blocking)") is mentioned but the implementation approach is undefined. Where is the counter stored? A git-tracked YAML file? A GitHub Actions cache? A comment on the PR? This is the most technically complex part of the design and receives the least specification. Without it, an implementer will make an arbitrary choice that may have security implications.
2. TICKET-6's proposed hook type is given as `pre_tool_use` or `post_tool_use` — this is an either/or that affects when the advisory fires relative to the edit. The design rationale for choosing one over the other is missing. A how-to guide author cannot implement this without resolving the ambiguity.
3. TICKET-3's trustworthiness evaluation checklist is listed as an AC item but no criteria for "trustworthy" are given in the ticket body. The guide author must invent the checklist with no starting criteria.

**Improvement Path:**
Specify the escalation counter storage mechanism in TICKET-4 (recommend: a git-tracked counter file or a GitHub Actions environment variable passed between runs via artifact). Resolve the hook type in TICKET-6 with a brief rationale. Add a seed list of trustworthiness criteria to TICKET-3's scope (e.g., verified publisher, recent commit activity, pinned SHA available, no known CVEs).

---

### Evidence Quality (0.80/1.00)

**Evidence:**
Referenced files confirmed to exist in the repository:
- `docs/reference/ci-cd-pipeline-security.md` — exists, contains SHA Pinning section as referenced
- `docs/explanation/ci-cd-supply-chain-security.md` — exists
- `.github/workflows/ci.yml`, `version-bump.yml`, `release.yml`, `dependabot.yml` — all exist
- `mkdocs.yml` — exists, contains `Guides:` nav section

Issue number #153 is confirmed as EN-001 in `EN-001-ci-pipeline-hardening.md` Related Items.

The claim that `docs/reference/ci-cd-pipeline-security.md` contains a "SHA Pinning section" is accurate — the file contains a `## SHA Pinning` section.

**Gaps:**
1. Issue numbers #130 (PROJ-015: Doc Audit) and #135 (PROJ-016: Doc Writing) cannot be verified in the local repository. There are no work item files for PROJ-015 or PROJ-016 in the local projects directory. These may be accurate GitHub Issue numbers, but the parenthetical labels "(PROJ-015: Doc Audit)" and "(PROJ-016: Doc Writing)" are not grounded in any locally verifiable entity. If the labels are wrong, every ticket that cites them carries incorrect metadata.
2. TICKET-1 references `docs/explanation/ci-cd-supply-chain-security.md` as "(Why SHA pinning matters)" — this is a reasonable description but the file content was not verified to contain that framing. Minor.
3. TICKET-4 references "/diataxis skill (diataxis-auditor agent)" — the `/diataxis` skill exists but whether a `diataxis-auditor` agent specifically handles automated CI-based staleness detection (vs. interactive audit sessions) is not verified.

**Improvement Path:**
Add a note in the References sections of tickets that cite #130 and #135: "Verify these issue numbers before publishing — PROJ-015 and PROJ-016 are not tracked in local worktracker." Alternatively, link to the actual GitHub Issue URLs rather than bare numbers.

---

### Actionability (0.73/1.00)

**Evidence:**
TICKET-1, TICKET-2, and TICKET-3 are highly actionable. Each specifies: exact output file path, nav section to add the guide to, required tool invocation, cross-link targets, and the MkDocs build test as a final validation step. A developer could pick up TICKET-1 immediately and have a clear definition of done.

TICKET-5 is moderately actionable: the output path (`.github/doc-source-map.yml`), schema requirement, and initial mappings are specified. An implementer knows what to build.

**Gaps:**
1. TICKET-4 is not independently actionable without design decisions that the ticket defers. The CI job is described at the level of a concept ("a CI job that runs the mapping check on PR events") but the implementer must decide: Python script or shell script? Standalone job or composite action? What GitHub Actions runner and permissions does it need? What is the job name in ci.yml? Without these, an implementer must design, not just implement.
2. TICKET-6 cannot be picked up until TICKET-5 is complete (the mapping file does not exist). This dependency is unstated. A maintainer might assign TICKET-6 in parallel with TICKET-5, leading to a blocked implementation.
3. No ticket specifies who is responsible for the three-layer review (TICKET-4 AC: "/eng-team security review, /red-team threat assessment, /adversary quality review") — is this the ticket author's responsibility before closing, or a pre-merge requirement? This is ambiguous for a solo maintainer vs. a team.

**Improvement Path:**
Add an "Implementation Notes" section to TICKET-4 specifying the CI job mechanism (at minimum: "recommend a Python script invoked via a new job in ci.yml"). Add an explicit "Depends on: TICKET-5 (must be complete before starting)" to TICKET-6. Clarify the review requirement as a pre-merge AC, not post-merge.

---

### Traceability (0.55/1.00)

**Evidence:**
TICKET-1 provides the strongest traceability: it names the source requirement (#153 for EN-001, which is verified), the documentation files it builds on, and the Diataxis methodology that governs the output type. TICKET-4 links to the originating problems (#130, #135) and existing infrastructure (ci-cd-pipeline-security.md).

**Gaps:**
1. The parent-child relationship between TICKET-4 → TICKET-5 → TICKET-6 is not stated with ticket identifiers. "See parent ticket for design" (TICKET-5) and "from the mapping configuration" (TICKET-6) are informal prose references. In GitHub Issues, these would need to be hyperlinks or "Implements #N" references to be traceable.
2. No ticket states which PROJ-030-bugs work item originated the requirement for these tickets. The WORKTRACKER.md shows EN-001 has tasks TASK-001 and TASK-002 (both completed), but these six tickets appear to be follow-on work. There is no explicit "This ticket is created in response to [work item]" statement.
3. For TICKET-4, the requirement for an agentic workflow is stated as a problem to solve, but there is no reference to a prior decision or discovery that established this as the right approach. An ADR reference or an investigation note would provide traceability to why this design was chosen over alternatives (e.g., why CI-based over a git hook approach for the freshness check).
4. The Diataxis how-to methodology is named as the required approach for tickets 1-3 but there is no link to the `/diataxis` skill documentation or SKILL.md reference path for the agent that will produce the output. A future developer wondering why diataxis-howto specifically cannot trace the requirement.

**Improvement Path:**
Add ticket number references in TICKET-5 and TICKET-6 parent links once numbers are assigned (note: this is a chicken-and-egg issue with draft tickets, but can be addressed with placeholder TICKET-N notation). Add a "Originated from:" field to each ticket linking to the EN-001 worktracker entity or a specific finding that motivated the ticket. Add a brief rationale note to TICKET-4 for why CI-based (rather than git-hook-based) staleness detection was chosen.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Dimension | Current | Target | Recommendation |
|----------|-----------|---------|--------|----------------|
| 1 | Traceability | 0.55 | 0.80 | Add ticket number cross-references between TICKET-4/5/6 using TICKET-N placeholder notation. Add "Originated from: EN-001" to all six tickets. Add explicit dependency declaration in TICKET-6 ("Depends on: TICKET-5"). |
| 2 | Internal Consistency | 0.72 | 0.85 | TICKET-4 must list TICKET-5 and TICKET-6 as child/related tickets. TICKET-5 and TICKET-6 must reference parent by number not prose. TICKET-6 must name TICKET-5 as a prerequisite. |
| 3 | Actionability | 0.73 | 0.85 | Add "Implementation Notes" to TICKET-4 specifying CI job mechanism. Mark TICKET-6 blocked until TICKET-5 is complete. Clarify three-layer review as a pre-merge gate not a post-merge activity. |
| 4 | Completeness | 0.78 | 0.88 | Note that `docs/howto/` directory must be created. Add the exact mkdocs.yml nav entry format to each documentation ticket. Narrow TICKET-5's "expand mappings" AC to either required or explicitly out-of-scope for v1. Specify escalation counter storage in TICKET-4. |
| 5 | Methodological Rigor | 0.82 | 0.90 | Resolve TICKET-6 hook type (pre vs. post tool use) with rationale. Add seed trustworthiness criteria to TICKET-3. Specify escalation counter mechanism in TICKET-4. |
| 6 | Evidence Quality | 0.80 | 0.90 | Add verification note for #130 and #135 issue labels (PROJ-015, PROJ-016). Consider using full GitHub Issue URLs rather than bare numbers for external references. |

## Leniency Bias Check
- [x] Each dimension scored independently
- [x] Evidence documented for each score
- [x] Uncertain scores resolved downward (Traceability: uncertain between 0.55 and 0.65 — chose 0.55; Internal Consistency: uncertain between 0.72 and 0.78 — chose 0.72; Actionability: uncertain between 0.73 and 0.80 — chose 0.73)
- [x] First-draft calibration considered (this is a first draft; composite of 0.75 is within expected 0.65-0.80 range)
- [x] No dimension scored above 0.95 without exceptional evidence

---

## Session Context Handoff

```yaml
verdict: REVISE
composite_score: 0.75
threshold: 0.92
weakest_dimension: Traceability
weakest_score: 0.55
critical_findings_count: 0
iteration: 1
improvement_recommendations:
  - "Add TICKET-N placeholder cross-references between TICKET-4, TICKET-5, TICKET-6 and 'Originated from: EN-001' to all tickets"
  - "TICKET-5 and TICKET-6 must reference parent by ticket number, not prose; TICKET-6 must declare dependency on TICKET-5"
  - "TICKET-4 must specify CI job implementation mechanism; TICKET-6 must resolve hook type (pre vs post tool use)"
  - "Note that docs/howto/ directory does not exist and must be created; provide exact mkdocs.yml nav entry for each guide"
  - "Resolve TICKET-4 escalation counter storage (git-tracked file vs artifact)"
  - "Add verification note or full URLs for #130 (PROJ-015) and #135 (PROJ-016) references"
```
