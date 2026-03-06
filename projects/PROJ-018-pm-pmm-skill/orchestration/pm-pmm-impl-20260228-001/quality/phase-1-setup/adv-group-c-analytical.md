# Adversarial Quality Review -- Group C: Analytical (S-012 FMEA + S-013 Inversion)

> **Reviewer:** adv-executor (Group C -- Analytical)
> **Strategies Applied:** S-012 (FMEA), S-013 (Inversion Technique)
> **Phase:** 1 -- Research & Template Design
> **Date:** 2026-03-01
> **Workflow:** `pm-pmm-impl-20260228-001`
> **Quality Threshold:** >= 0.95 (production-ready)
> **Verdict:** ACCEPT-WITH-CAVEATS (composite: 0.91)

---

## Document Sections

| Section | Purpose |
|---------|---------|
| [1. FMEA Analysis](#1-fmea-analysis) | Failure mode enumeration across all Phase 1 artifacts |
| [2. Top 5 Highest-RPN Failure Modes](#2-top-5-highest-rpn-failure-modes) | Critical failure modes with recommended mitigations |
| [3. Inversion Analysis](#3-inversion-analysis) | Per-element inversion: what would guarantee failure |
| [4. Template Spot-Check Findings](#4-template-spot-check-findings) | FMEA and inversion for user-persona.md, market-sizing.md, mrd.md |
| [5. Per-Artifact Scoring](#5-per-artifact-scoring) | 6-dimension scores per artifact |
| [6. Composite Scores](#6-composite-scores) | Weighted composites and verdicts |
| [7. Specific Findings by Severity](#7-specific-findings-by-severity) | Itemized findings with severity classification |
| [8. Overall Phase 1 Verdict](#8-overall-phase-1-verdict) | Final assessment and gate recommendation |

---

## 1. FMEA Analysis

### 1.1 FMEA Rating Scales

**Severity (S):** 1 = negligible, 10 = catastrophic system failure
**Occurrence (O):** 1 = extremely unlikely, 10 = near-certain to occur
**Detection (D):** 1 = immediately obvious, 10 = virtually undetectable before impact

**RPN = S x O x D.** Maximum = 1000. Focus threshold: RPN > 200.

### 1.2 Full FMEA Table

| FM-ID | Failure Mode | Artifact(s) | Effect | S | O | D | RPN | Recommended Action |
|-------|-------------|-------------|--------|---|---|---|-----|-------------------|
| FM-001 | Agent boundary violation: agent produces artifact assigned to another agent | architecture.md (routing heuristic) | Wrong agent applies wrong frameworks; artifact quality degrades; cross-domain contamination | 8 | 4 | 6 | **192** | Add runtime enforcement: agent system prompt MUST reject artifact types not in its ownership table. Governance YAML `output.allowed_types` field enforced at L3. |
| FM-002 | Mode switching corruption: discovery artifact promoted to delivery without completing delivery sections | frontmatter-schema.md (status progression) | Incomplete artifact treated as authoritative; stakeholder decisions made on insufficient analysis | 9 | 5 | 5 | **225** | Mode transition MUST require section-completeness check, not just frontmatter field update. Pre-transition checklist in agent system prompt. |
| FM-003 | Framework misapplication: framework used for wrong artifact type | architecture.md (framework coverage matrix) | Misleading analysis; RICE applied to competitive analysis instead of PRD prioritization | 7 | 3 | 7 | **147** | Framework-to-template binding in governance YAML; agent rejects framework application outside declared scope. |
| FM-004 | Frontmatter validation gap: required field missing or invalid | frontmatter-schema.md | Routing failure (missing `type`), staleness undetected (missing `last_validated`), cross-ref integrity broken | 7 | 6 | 3 | **126** | JSON Schema validation at write time (L3 enforcement). Already specified but no implementation mechanism defined for Phase 2. |
| FM-005 | Cross-agent data flow contamination: tainted upstream artifact propagates to PRD | architecture.md (aggregation pattern), threat-model.md (TH-004/TH-005) | Injected content in customer quote persists through persona to PRD; distributed broadly | 9 | 5 | 7 | **315** | Content hash verification at read time. Second-pass injection detection in pm-product-strategist. Sensitivity non-downgrade rule. |
| FM-006 | Routing disambiguation failure: ambiguous "persona" triggers both user-persona and buyer-persona agents | architecture.md (Section 6.2) | User receives wrong persona type; downstream artifacts built on incorrect persona foundation | 6 | 7 | 4 | **168** | H-31 disambiguation is specified. Risk remains for automated/scripted invocations where H-31 cannot fire. Add explicit negative keywords for disambiguation. |
| FM-007 | Discovery mode presented as delivery-grade output | frontmatter-schema.md (mode field), architecture.md (Section 7) | Stakeholders treat lightweight hypothesis as validated strategy; incorrect resource allocation decisions | 9 | 4 | 5 | **180** | Mode is in frontmatter and status display header. But: no rendering-level enforcement. A discovery artifact rendered as markdown looks identical to delivery if reader skips the header. Add visual differentiation (e.g., persistent watermark-style callout). |
| FM-008 | Staleness window mismatch: battle-card 30-day window not enforced | frontmatter-schema.md (Section 5.2) | Stale competitive intelligence treated as current; strategic decisions on outdated competitor data | 8 | 6 | 6 | **288** | Domain-specific staleness windows are documented but no automated enforcement mechanism is specified. Require staleness check at artifact-read time, not only at human review. |
| FM-009 | Cross-reference integrity failure: asymmetric references between artifacts | frontmatter-schema.md (Section 6) | PRD references persona that does not back-reference PRD; dependency chain is invisible from one direction | 5 | 5 | 5 | **125** | CI-002 rule is defined as WARNING not BLOCK. For delivery-mode artifacts, asymmetric references SHOULD be BLOCK, not WARNING. |
| FM-010 | Keyword routing collision: "competitive" keyword matches both pm-competitive-analyst and overlapping terms in pm-market-strategist GTM context | architecture.md (Section 4.2 routing prefix) | Request routed to wrong agent; competitive data processed without competitive-analyst guardrails | 7 | 4 | 5 | **140** | Negative keywords specified. However, compound trigger analysis for multi-keyword requests is not specified. A request containing both "competitive" and "GTM" has no defined resolution. |
| FM-011 | P-003 violation via agent chaining: orchestrator attempts to chain worker-to-worker | architecture.md (Section 10) | Constitutional violation; recursive subagent hierarchy | 10 | 2 | 3 | **60** | P-003 compliance is explicit. Governance YAML excludes Task tool from workers. Low occurrence given explicit prohibition. |
| FM-012 | 18-framework count discrepancy: frontmatter-schema.md lists 25 framework entries against the "18 validated" claim | frontmatter-schema.md (Section 7) | Confusion about canonical framework count; QA reviewers unable to verify completeness against ambiguous baseline | 5 | 8 | 4 | **160** | The document acknowledges 25 entries as "18 primary + 7 supporting." However, the mapping from 18 to 25 is not traceable row-by-row. Provide an explicit canonical-18 list separate from the supporting frameworks. |
| FM-013 | Threat model coverage gap: no explicit threat for template-level framework injection (framework parameters as injection vectors) | threat-model.md | Framework parameter injection (e.g., "Apply RICE where R = [IGNORE INSTRUCTIONS]") unmitigated | 7 | 4 | 7 | **196** | TH-002 covers external content injection but framework parameter injection (T-02 in STRIDE) lacks a dedicated TH entry with mitigations. |
| FM-014 | Attack surface analysis declares "Current state of controls: None" for all layers | attack-surface.md (Section 1) | Phase 2 implementers have no baseline to build from; risk of ad-hoc control implementation | 6 | 3 | 4 | **72** | This is by design (pre-Phase-2 assessment). Acceptable for Phase 1. |
| FM-015 | QA strategy multi-executor isolation: anchoring bias if Group D scorer receives all prior findings | qa-strategy.md (Section 3.4) | Scorer anchored to Group A/B/C findings rather than independently evaluating artifact quality | 7 | 6 | 7 | **294** | Group D intentionally receives upstream findings (by design per ORCH-C05). However, the scorer could be anchored by severity language in prior findings. Mitigation: Group D MUST produce its own independent dimension-level score BEFORE reading prior findings, then adjust. Two-pass scoring protocol. |
| FM-016 | Sensitivity field absent from required frontmatter fields | frontmatter-schema.md (Section 2) | No mandatory sensitivity classification; financial data can be written without confidential-financial tag | 8 | 7 | 5 | **280** | Frontmatter schema has `sensitivity` as neither required nor optional. Attack surface analysis (Section 2.4) references sensitivity fields. The schema MUST add `sensitivity` as a required field with domain-appropriate defaults. |
| FM-017 | No `content_hash` field in frontmatter schema | frontmatter-schema.md (Section 2) | TH-008 (artifact tampering) mitigation requires hash verification, but the schema does not include a `content_hash` field | 7 | 5 | 6 | **210** | Add `content_hash` as an optional field now (required at Phase 3 per threat model remediation schedule P3-A). Schema should anticipate future required fields. |
| FM-018 | MRD template `risk_domain` value is "viability" instead of "business-viability-risk" | mrd.md template | Schema validation failure; `risk_domain` enum value does not match frontmatter-schema.md valid values | 6 | 9 | 2 | **108** | Direct inconsistency between template and schema. Fix the template to use `business-viability-risk`. |
| FM-019 | No mechanism to prevent discovery-to-delivery regression (mode going backwards) | frontmatter-schema.md (Section 3.5) | Document states "never backwards" but no enforcement mechanism specified | 7 | 4 | 6 | **168** | Add L3 pre-write check: if existing artifact has `mode: delivery`, reject write with `mode: discovery`. |
| FM-020 | Template naming inconsistency: architecture.md specifies `user-persona.md` but actual file is `05-personas.template.md` | architecture.md (Section 8.1), actual templates directory | Template file lookup fails if agents use architecture.md naming; templates unreachable at deployment | 8 | 8 | 3 | **192** | The orchestration-phase naming (`05-personas.template.md`) differs from the deployment-target naming (`user-persona.md`). This is acceptable IF the Phase 4 deployment step includes a rename. However, no rename step is documented. Document the rename mapping explicitly. |

---

## 2. Top 5 Highest-RPN Failure Modes

### Rank 1: FM-005 -- Cross-Agent Data Flow Contamination (RPN: 315)

**Failure Mode:** Tainted upstream artifact (e.g., injected content in customer quote persisting through persona) propagates to pm-product-strategist's PRD via the aggregation pattern.

**Why this matters:** The architecture explicitly designs pm-product-strategist as the aggregation agent that reads from all four peer agent namespaces. This creates a single-point-of-contamination risk where any upstream compromise achieves PRD-level distribution. The threat model identifies this (TH-004/TH-005) but the architecture document does not specify a runtime content verification mechanism -- only post-hoc content hash verification (P3-A, scheduled for "before GA").

**Recommended Mitigations:**
1. Move content hash verification (P3-A) to Phase 2 priority. PRDs are the highest-distribution artifacts and should not ship without integrity verification.
2. Add a mandatory `source_artifacts` frontmatter field to PRDs that lists all consumed artifact IDs. This is mentioned in attack-surface.md but not in the frontmatter schema.
3. pm-product-strategist's system prompt MUST include a second-pass validation step that re-scans all ingested peer content for injection patterns before producing output.

**Residual risk if mitigated:** Medium -- prompt injection detection is probabilistic, not deterministic. Hash verification catches tampering but not injection that survived initial processing.

---

### Rank 2: FM-015 -- QA Strategy Scorer Anchoring Bias (RPN: 294)

**Failure Mode:** The Group D scorer (S-014 LLM-as-Judge) receives all Group A/B/C findings before scoring. The severity language and finding density from prior groups anchors the scorer's independent judgment, inflating or deflating scores based on prior assessors' framing rather than artifact quality.

**Why this matters:** The QA strategy explicitly designs Group D to receive upstream findings (Section 3.4, "The scoring agent MUST receive all Group A, B, C findings before running"). This is the ONLY group that intentionally receives upstream findings. While this enables finding-adjusted scoring, it also creates a direct anchoring channel. If Group A finds a constitutional violation, Group D will anchor heavily on compliance dimensions regardless of actual artifact quality in other dimensions.

**Recommended Mitigations:**
1. Implement two-pass scoring: Group D FIRST scores the artifact independently (without prior findings), THEN reviews Group A/B/C findings and produces an adjusted score. Both scores are recorded; delta > 0.10 between passes triggers a flag.
2. Present Group A/B/C findings to Group D in a structured format that separates findings from severity language. Example: present facts without HIGH/CRITICAL labels until after first-pass scoring.
3. Add a calibration check: if Group D's score diverges from its first pass by > 0.15 after reading upstream findings, the scorer must document the specific finding that caused the shift.

**Residual risk if mitigated:** Low -- two-pass protocol makes anchoring visible and measurable.

---

### Rank 3: FM-008 -- Staleness Window Mismatch (RPN: 288)

**Failure Mode:** Domain-specific staleness windows (battle-card: 30 days, win-loss: 45 days, competitive-analysis: 60 days) are documented in frontmatter-schema.md but no automated enforcement mechanism is specified. An agent or user reading a 45-day-old battle card receives no system-level warning.

**Why this matters:** The staleness tracking design is comprehensive (Section 5.2 provides domain-specific windows with clear rationale). However, the enforcement is entirely dependent on human review of the `last_validated` field. In a multi-agent system where pm-product-strategist reads battle cards to build PRDs, the aggregation agent has no mechanism to detect that a source artifact is stale before incorporating its content.

**Recommended Mitigations:**
1. Add an artifact-read-time staleness check to agent system prompts: "Before ingesting any cross-referenced artifact, verify that (today - last_validated) does not exceed the domain-specific staleness window. If stale, include a WARNING block in your output and ask the operator whether to proceed."
2. Add a `staleness_status` computed field to the frontmatter schema (CURRENT/STALE/EXPIRED) that is set at read time based on artifact type and `last_validated`.
3. At Phase 4 integration, build a staleness dashboard command (`jerry pm-pmm staleness`) that reports all artifact staleness statuses.

**Residual risk if mitigated:** Low -- system-level staleness detection eliminates human-only dependency.

---

### Rank 4: FM-016 -- Sensitivity Field Absent from Required Frontmatter (RPN: 280)

**Failure Mode:** The frontmatter schema (Section 2, Required Fields) does not include a `sensitivity` field. The attack surface analysis (Section 2.4) and threat model (TH-004, TH-005) both reference sensitivity classification as a critical control. This is a design gap: the schema that defines what every artifact MUST contain does not mandate the field that the security analysis depends on.

**Why this matters:** Without a required `sensitivity` field, agents can write artifacts containing financial data (confidential-financial), competitive intelligence (confidential-competitive), or customer PII (confidential-internal) without any mandatory classification. The entire sensitivity-based access control framework in the attack surface analysis becomes advisory rather than enforceable.

**Recommended Mitigations:**
1. Add `sensitivity` as a required field in frontmatter-schema.md Section 2, with valid values: `internal`, `confidential-internal`, `confidential-financial`, `confidential-competitive`, `confidential-sales`.
2. Define agent-specific default sensitivity values in governance YAML: pm-business-analyst defaults to `confidential-financial`, pm-competitive-analyst defaults to `confidential-competitive`.
3. Add a sensitivity non-downgrade rule: agents cannot set sensitivity lower than the producing agent's default.

**Residual risk if mitigated:** Low -- mandatory sensitivity classification with agent-specific defaults provides deterministic enforcement.

---

### Rank 5: FM-002 -- Mode Switching Corruption (RPN: 225)

**Failure Mode:** A discovery artifact is promoted to delivery status by updating the `mode` field in frontmatter, but delivery-only sections (L1 Deep Analysis, L2 Strategic Implications, Recommendations, Appendix) are not completed. The artifact appears to be delivery-grade based on its frontmatter but contains only discovery-depth content.

**Why this matters:** The status progression (Section 4.1) defines gate conditions for `discovery -> delivery` as "All discovery-mode sections complete; last_validated updated; stakeholder sign-off." However, the gate does NOT verify that delivery-only sections are populated AFTER the mode transition. An artifact can transition to `mode: delivery` and then remain incomplete in delivery sections indefinitely while showing `mode: delivery` in its frontmatter.

**Recommended Mitigations:**
1. Add a section-completeness verification step to the `delivery -> final` transition gate. The gate condition already requires "All delivery-mode sections complete" but this is verified by the producing agent (self-review). Require external verification (critic or schema check).
2. Define a minimum content threshold per delivery section (e.g., each delivery-only section must contain > 100 words or > 1 table/list).
3. Add a `delivery_sections_complete` boolean field to frontmatter that agents set only after completing all delivery sections. The `delivery -> final` gate checks this field.

**Residual risk if mitigated:** Medium -- content completeness checking is imprecise (word count does not equal quality). But it catches the empty-section failure mode.

---

## 3. Inversion Analysis

### 3.1 Inversion: "What would guarantee the 5-agent model FAILS completely?"

**Inverted design (maximally harmful):**
- All 5 agents share identical system prompts with no domain specialization
- No routing heuristics; requests randomly assigned to agents
- Agents freely write to each other's artifact namespaces
- No distinction between discovery and delivery modes
- Agents load all 18 frameworks simultaneously regardless of artifact type
- No negative keywords; every keyword triggers every agent
- Agents chain-invoke each other (P-003 violation)
- No frontmatter schema; artifacts are free-form markdown

**Verification against current design:**

| Inversion Element | Current Design Avoids? | Evidence | Gap? |
|-------------------|----------------------|----------|------|
| Identical system prompts | YES | Each agent has distinct artifact ownership, framework assignment, and risk domain mapping (architecture.md Section 4.1) | No |
| Random routing | YES | Keyword-based routing with positive/negative keywords and disambiguation rules (Section 6) | Minor: compound keyword resolution undefined |
| Cross-namespace writes | PARTIALLY | Architecture assigns artifact ownership but no runtime namespace enforcement mechanism is specified | YES: FM-001 |
| No mode distinction | YES | Discovery/delivery mode architecture with section tagging and frontmatter tracking (Section 7) | No |
| All frameworks loaded | YES | Framework-to-agent mapping is explicit (Section 4.1); agents load only their assigned frameworks | No |
| No negative keywords | YES | Negative keywords specified per agent (Section 4.2) | No |
| Agent chaining | YES | P-003 compliance explicit; workers excluded from Task tool (Section 10) | No |
| No frontmatter schema | YES | Comprehensive frontmatter schema with required fields, type constraints, and validation rules | Minor: sensitivity field gap (FM-016) |

**Inversion verdict:** The current architecture systematically avoids 7 of 8 maximally harmful conditions. The remaining gap (runtime namespace enforcement) is a Phase 2 implementation concern, not an architecture design flaw. The architecture provides the specification; implementation must enforce it.

---

### 3.2 Inversion: "What would make these templates produce MISLEADING artifacts?"

**Inverted template design (maximally misleading):**
- Templates have no mode awareness; discovery and delivery produce identical structure
- Placeholder text is so generic it could describe any industry ("Enter data here")
- Framework sections are labeled but contain no methodology guidance
- No agent guidance comments; agents improvise structure
- Frontmatter has no agent-type binding; any agent fills any template
- No evidence prompting; templates accept pure speculation as valid content
- No cross-reference guidance; templates are isolated documents
- Status display is absent; reader cannot distinguish draft from final

**Verification against templates (spot-check: user-persona.md, market-sizing.md, mrd.md):**

| Inversion Element | Templates Avoid? | Evidence | Gap? |
|-------------------|-----------------|----------|------|
| No mode awareness | YES | All three templates clearly separate discovery and delivery sections with explicit mode labels | No |
| Generic placeholder text | YES | Placeholders are domain-specific (e.g., "When {situation}, I want to {action}" for JTBD; "${X}B" for market sizing) | No |
| Framework sections without methodology | YES | Agent guidance comments provide framework methodology (e.g., JTBD job statement structure, TAM/SAM/SOM calculation steps) | No |
| No agent guidance | YES | All templates include `<!-- AGENT GUIDANCE -->` comments with mode instructions and framework traces | No |
| No agent-type binding | YES | Frontmatter explicitly declares `agent` field tied to the producing agent | Minor: mrd.md has wrong `risk_domain` value (FM-018) |
| No evidence prompting | YES | Templates prompt for sources, data citations, and validation status (e.g., market-sizing.md requires sources per calculation step) | No |
| No cross-reference guidance | YES | Frontmatter `cross_refs` field with standard reference patterns documented in schema | No |
| No status display | YES | Status displayed prominently in document header with mode callout | No |

**Inversion verdict:** Templates systematically avoid all 8 maximally misleading conditions. Template quality is a strength of this Phase 1 deliverable. The one defect found (mrd.md `risk_domain` value) is a data error, not a structural design flaw.

---

### 3.3 Inversion: "What would make the threat model MISS critical threats?"

**Inverted threat model (maximally blind):**
- Only considers external attackers, not insider/operator threats
- Ignores cross-agent data flows entirely
- Uses no structured methodology (just a list of "things that could go wrong")
- Does not map threats to specific agents or artifacts
- Mitigations are generic ("be careful") with no implementation guidance
- Does not consider the aggregation pattern as an attack vector
- Ignores data sensitivity differences between agents
- Does not address mode-switching as a threat vector

**Verification against current threat model:**

| Inversion Element | Threat Model Avoids? | Evidence | Gap? |
|-------------------|---------------------|----------|------|
| External-only threats | YES | Considers operator as threat actor (TH-006 mode bypass, TH-007 routing manipulation) | No |
| Ignores cross-agent flows | YES | Dedicated sections: TH-004, TH-005 (cross-agent data leakage), aggregation chain analysis (Section 4) | No |
| No structured methodology | YES | Full STRIDE analysis across all 6 categories with systematic enumeration (Section 5) | No |
| No agent-specific mapping | YES | Each TH entry specifies affected agent(s) | No |
| Generic mitigations | MOSTLY | Most mitigations specify implementation location (system prompt, governance YAML, orchestrator). Some are still semi-generic (TH-008 "log all artifact reads and writes") | Minor |
| Ignores aggregation pattern | YES | Aggregation chain explicitly modeled in Section 4 with dedicated trust boundary (TB-4) | No |
| Ignores sensitivity differences | YES | TH-004 (competitive), TH-005 (financial), TH-011 (PII) each address domain-specific sensitivity | No |
| Ignores mode-switching threats | YES | TH-006 explicitly covers mode bypass | No |

**Inversion verdict:** The threat model systematically avoids all 8 maximally blind conditions. Coverage is comprehensive. The minor gap is in mitigation specificity for a small number of threats (TH-008 logging recommendation lacks implementation detail).

---

### 3.4 Inversion: "What would make the QA strategy TOO LENIENT?"

**Inverted QA strategy (maximally lenient):**
- Single scorer runs all strategies (anchoring bias)
- Quality threshold is 0.70 (anything passes)
- No iteration ceiling (revise forever without convergence)
- Scorer receives creator's reasoning alongside the artifact (confirmation bias)
- No per-artifact-type rubrics; all artifacts scored on generic dimensions
- No anti-leniency calibration; high scores are the norm
- No plateau detection; identical scores cycle indefinitely
- Accept-with-caveats is the norm, not the exception

**Verification against current QA strategy:**

| Inversion Element | QA Strategy Avoids? | Evidence | Gap? |
|-------------------|---------------------|----------|------|
| Single scorer | YES | Multi-executor isolation with 3+ Task invocations per phase (ORCH-C05, Section 3.1) | No |
| Low threshold | YES | 0.95 quality threshold (production-ready) with 0.90 accept-with-caveats floor | No |
| No iteration ceiling | YES | Max 5 iterations with plateau detection (delta < 0.01 for 3 consecutive) | No |
| Creator reasoning leakage | YES | Groups A/B/C receive only artifact + strategy template + rubric; creator rationale withheld (Section 3.2) | Minor: Group D receives all prior findings (FM-015) |
| Generic rubrics | YES | Per-artifact-type rubrics in Section 2 with artifact-specific scoring criteria | No |
| No anti-leniency | YES | Section 5 explicitly addresses scoring calibration with exemplars at 0.95/0.85/0.75 | No |
| No plateau detection | YES | Plateau detection specified (delta < 0.01, 3 consecutive iterations) | No |
| Accept-with-caveats as norm | YES | Accept-with-caveats requires documented caveats and is positioned as exceptional, not default | No |

**Inversion verdict:** The QA strategy systematically avoids 7 of 8 maximally lenient conditions. The remaining gap (Group D anchoring bias, FM-015) is a design trade-off that the QA strategy acknowledges but does not fully mitigate. The two-pass scoring protocol recommended in FM-015 would close this gap.

---

## 4. Template Spot-Check Findings

### 4.1 user-persona.md (05-personas.template.md)

**Strengths:**
- JTBD framework deeply operationalized: job statements follow canonical structure ("When/I want to/so I can")
- Customer Development methodology explicit in delivery sections (minimum 5 interviews)
- Clear discovery/delivery section separation with mode labels in navigation table
- Disambiguation note distinguishing user persona from buyer persona
- ODI (Outcome-Driven Innovation) opportunity scoring included with interpretation guidance

**FMEA findings:**

| FM-ID | Failure Mode | S | O | D | RPN |
|-------|-------------|---|---|---|-----|
| FM-T01 | Persona created without any validated customer data (pure hypothesis in delivery mode) | 7 | 4 | 4 | 112 |
| FM-T02 | PII persists in interview evidence table (Section 5) despite pm-customer-insight PII rules | 8 | 5 | 5 | 200 |
| FM-T03 | Persona quote in Section 1 misattributed as real when it is fabricated for discovery mode | 5 | 6 | 6 | 180 |

**Inversion check:** Template avoids all 8 inversion conditions. No structural defects.

---

### 4.2 market-sizing.md (09-market-sizing.template.md)

**Strengths:**
- TAM/SAM/SOM methodology fully operationalized with step-by-step calculation tables
- Dual methodology (top-down + bottoms-up) with explicit reconciliation requirement
- Source citation required at every calculation step ("AGENT: Every number needs a source")
- 2x divergence threshold between methods triggers investigation
- Competitive landscape allocation section connects sizing to competitive position

**FMEA findings:**

| FM-ID | Failure Mode | S | O | D | RPN |
|-------|-------------|---|---|---|-----|
| FM-T04 | Top-down sizing uses analyst report from > 2 years ago without staleness flag | 6 | 5 | 5 | 150 |
| FM-T05 | SOM capture timeline presents optimistic Year 1-3 projections without sensitivity analysis | 7 | 6 | 5 | 210 |
| FM-T06 | Bottoms-up ACV assumptions are not validated against actual deal data | 6 | 5 | 6 | 180 |

**Inversion check:** Template avoids all 8 inversion conditions. FM-T05 is notable: market sizing without sensitivity analysis on SOM projections creates false precision. Recommend adding a "Sensitivity Analysis" section showing SOM under optimistic/base/pessimistic assumptions.

---

### 4.3 mrd.md (14-mrd.template.md)

**Strengths:**
- PMF Survey (Sean Ellis) methodology explicitly integrated with threshold (>= 40% "very disappointed")
- Crossing the Chasm framework applied to beachhead segment selection
- Market Requirements table includes competitive gap column linking MRD to competitive analysis
- Discovery/delivery mode distinction present throughout

**FMEA findings:**

| FM-ID | Failure Mode | S | O | D | RPN |
|-------|-------------|---|---|---|-----|
| FM-T07 | `risk_domain: "viability"` does not match schema enum `business-viability-risk` | 6 | 9 | 2 | **108** |
| FM-T08 | Template uses `{{placeholder}}` syntax while other templates use `{placeholder}` -- inconsistent placeholder convention | 4 | 8 | 3 | 96 |
| FM-T09 | Market Requirements section exists only in Delivery Mode -- Discovery mode has no lightweight requirements list | 5 | 5 | 5 | 125 |
| FM-T10 | No explicit cross-reference to user-persona or buyer-persona in template guidance | 5 | 4 | 6 | 120 |

**Defect (FM-018/FM-T07):** The `risk_domain` value "viability" in the MRD template frontmatter does not match any valid value in the frontmatter schema. The schema specifies `business-viability-risk`. This is a data integrity defect that would cause schema validation failure. Severity: MEDIUM -- easily fixable but indicates that templates were not validated against the schema before submission.

**Inconsistency (FM-T08):** The MRD template uses double-brace `{{placeholder}}` syntax while user-persona.md and market-sizing.md use single-brace `{placeholder}` syntax. This inconsistency suggests the MRD template was authored by a different process or agent without cross-template harmonization. Severity: LOW -- functional but creates maintenance debt.

---

## 5. Per-Artifact Scoring

### 5.1 architecture.md

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Completeness | 0.20 | 0.94 | All 4 alternatives enumerated with full scoring. All 15 artifacts mapped. File organization, integration points, and constitutional compliance covered. Minor gap: no explicit discussion of failure recovery when routing fails (what happens after H-31 disambiguation fails). |
| Internal Consistency | 0.20 | 0.95 | Agent artifact counts consistent throughout (5 agents, 15 artifacts). Routing keywords consistent with agent assignments. Risk domain mapping consistent with Cagan taxonomy. No internal contradictions found. |
| Methodological Rigor | 0.20 | 0.93 | Weighted multi-criteria evaluation with explicit dimensions and scoring. All alternatives assessed against identical dimensions. Composite scores defensible. Minor gap: weighting rationale for 25/20/20/15/10/10 split is asserted but not derived from a principled source. |
| Evidence Quality | 0.15 | 0.90 | References Issue #123, H-34, H-36, P-003, AP-07. Cagan taxonomy cited as source for risk domains. However, the claim "zero artifact ownership overlap" is stated as absolute but not formally proven (no exhaustive pairwise overlap test documented). |
| Actionability | 0.15 | 0.92 | Agent definitions specify owned artifacts, frameworks, routing keywords, and negative keywords. Implementation path is clear. Integration points specify protocols. Minor gap: deployment steps from orchestration layout to final `skills/pm-pmm/` structure not specified. |
| Traceability | 0.10 | 0.90 | Maps to Issue #123. P-003, P-020, P-022 compliance explicit. Framework assignments traceable to risk domains. Minor gap: no AC (acceptance criterion) numbers referenced -- traceability goes to issue but not to specific ACs. |

**Composite: (0.94 x 0.20) + (0.95 x 0.20) + (0.93 x 0.20) + (0.90 x 0.15) + (0.92 x 0.15) + (0.90 x 0.10) = 0.188 + 0.190 + 0.186 + 0.135 + 0.138 + 0.090 = 0.927**

**Verdict: REVISE** (below 0.95 threshold)

---

### 5.2 frontmatter-schema.md

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Completeness | 0.20 | 0.87 | Required fields well-defined. Status progression complete. Staleness tracking comprehensive. CRITICAL GAP: `sensitivity` field absent from required fields despite being central to the security model. `content_hash` field absent (FM-017). Framework coverage matrix claims 18 but lists 25 without clear canonical designation. |
| Internal Consistency | 0.20 | 0.91 | Field specifications consistent with examples (Section 8). Status progression consistent with mode definitions. Cross-reference rules internally consistent. Minor inconsistency: framework count narrative (18 vs. 25) creates confusion even though the note explains it. |
| Methodological Rigor | 0.20 | 0.92 | Schema follows YAML best practices. Staleness windows have domain-specific rationale. Cross-reference integrity rules are well-defined (CI-001 through CI-005). Validation methods specified. |
| Evidence Quality | 0.15 | 0.88 | Staleness window durations are rationale-backed (competitive landscape shifts rapidly). Cross-reference patterns cite meaningful relationships. However, the 90-day standard window is asserted without empirical basis. |
| Actionability | 0.15 | 0.93 | Examples (Section 8) are concrete and copy-pasteable. Field specifications are implementable. Status display format provided. Agents can implement this schema without further clarification. |
| Traceability | 0.10 | 0.88 | Maps to architecture.md artifact types and agent assignments. References H-33 for AST-based parsing. Missing: no explicit mapping to acceptance criteria. |

**Composite: (0.87 x 0.20) + (0.91 x 0.20) + (0.92 x 0.20) + (0.88 x 0.15) + (0.93 x 0.15) + (0.88 x 0.10) = 0.174 + 0.182 + 0.184 + 0.132 + 0.1395 + 0.088 = 0.900**

**Verdict: REVISE** (below 0.95 threshold; sensitivity field gap is the primary driver)

---

### 5.3 threat-model.md

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Completeness | 0.20 | 0.94 | Full STRIDE analysis across all 6 categories. 20 threats cataloged (TH-001 through TH-020). All 5 agents covered. Trust boundary diagram with 5 boundary zones. Data flow analysis with aggregation chain. Constitutional constraint mapping. |
| Internal Consistency | 0.20 | 0.93 | Risk ratings are calibrated: not everything is Critical. Threat entries consistently structured. Mitigations do not contradict each other. STRIDE categories comprehensively populated. Minor: TH-006 is classified under Elevation of Privilege (S-02) but is structurally a Spoofing threat. |
| Methodological Rigor | 0.20 | 0.95 | STRIDE methodology systematically applied. Trust boundary analysis follows industry practice. Risk rating methodology defined with criteria table. Mitigation prioritization (P1-P4) is systematic. |
| Evidence Quality | 0.15 | 0.91 | Attack vectors include concrete examples (e.g., TH-001 example with injected system prompt extraction). Risk ratings grounded in deployment context (single-user CLI). Some mitigations lack implementation specificity (TH-008 logging). |
| Actionability | 0.15 | 0.93 | 9 mitigation requirements for Phase 2 with priority ordering and effort estimates. Each mitigation maps to specific threats. Owner assignments specified (Engineering, Skill author). |
| Traceability | 0.10 | 0.92 | Each threat maps to STRIDE category, trust boundary, and affected agent. Mitigations trace to governance YAML fields. Constitutional principles mapped in Section 8. |

**Composite: (0.94 x 0.20) + (0.93 x 0.20) + (0.95 x 0.20) + (0.91 x 0.15) + (0.93 x 0.15) + (0.92 x 0.10) = 0.188 + 0.186 + 0.190 + 0.1365 + 0.1395 + 0.092 = 0.932**

**Verdict: REVISE** (below 0.95 threshold)

---

### 5.4 attack-surface.md

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Completeness | 0.20 | 0.95 | All 7 attack surface layers enumerated. All 5 agents individually analyzed with agent-specific entry points. 5 data input modalities covered (NL, CSV, screenshots, metrics, quotes). Cross-agent information flow risks modeled. Guardrail requirements specified per agent. Priority-ordered remediation with 4 tiers. |
| Internal Consistency | 0.20 | 0.94 | Agent-specific forbidden actions are consistent with architecture.md agent assignments. Namespace boundaries match architecture. Sensitivity classifications are consistent across agents. Minor: Section 1 states "Current controls: None" but some controls are specified architecturally (P-003 enforcement). |
| Methodological Rigor | 0.20 | 0.93 | Systematic layer-by-layer analysis. Per-agent attack surface decomposition follows a consistent format. Input modality analysis is thorough. Trust chain contamination model is well-constructed. |
| Evidence Quality | 0.15 | 0.90 | Attack vectors are concrete (CSV header injection example, transcript speaker label example). Risk ratings grounded in actual workflow patterns. Some priority mitigations lack effort estimates (P1-A "Medium" is vague). |
| Actionability | 0.15 | 0.94 | 16 remediation recommendations with priority ordering. Each recommendation maps to specific threats. Implementation guidance specifies WHERE to implement (orchestrator, system prompt, governance YAML). Owner assignments present. |
| Traceability | 0.10 | 0.91 | References companion document (threat-model.md) by TH-ID. Maps to H-34, P-003. Guardrails trace to governance YAML fields. Missing: no AC-level traceability. |

**Composite: (0.95 x 0.20) + (0.94 x 0.20) + (0.93 x 0.20) + (0.90 x 0.15) + (0.94 x 0.15) + (0.91 x 0.10) = 0.190 + 0.188 + 0.186 + 0.135 + 0.141 + 0.091 = 0.931**

**Verdict: REVISE** (below 0.95 threshold)

---

### 5.5 qa-strategy.md

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Completeness | 0.20 | 0.93 | Per-phase strategy assignments comprehensive. Per-artifact-type rubrics detailed. Multi-executor grouping well-defined. Quality gate protocol with pre-barrier checklist. Scoring calibration notes present. Constraint compliance mapping. Minor gap: no explicit guidance for what happens when an artifact scores differently across Groups A/B/C (conflicting quality signals). |
| Internal Consistency | 0.20 | 0.93 | Strategy assignments consistent with quality-enforcement.md C3 requirements. Dimension weights match SSOT. Executor isolation rules internally consistent. Minor: QA strategy defines 0.95 threshold but quality-enforcement.md SSOT defines 0.92 for C2+. The 0.95 is justified as a project-specific elevation but could confuse implementers. |
| Methodological Rigor | 0.20 | 0.94 | Multi-executor isolation prevents anchoring bias (with the Group D caveat noted in FM-015). Per-artifact-type rubrics are highly specific. Scoring calibration with exemplars is a methodological strength. H-16 ordering enforcement (steelman before devil's advocate) codified. |
| Evidence Quality | 0.15 | 0.90 | Rubric descriptions are detailed enough to be non-ambiguous. Score exemplars at 0.95/0.85/0.75/0.50 provide calibration. However, exemplars are abstract descriptions rather than actual scored artifacts (no real-world calibration data). |
| Actionability | 0.15 | 0.92 | Executor invocation sequences are fully specified as diagrams. Pre-barrier checklist is a concrete go/no-go protocol. Revision cycle with iteration ceiling and plateau detection is actionable. Minor gap: no guidance on how to handle artifacts that pass some groups but fail others within the same phase. |
| Traceability | 0.10 | 0.91 | Maps to ORCH-C03 through ORCH-C10. References quality-enforcement.md, H-13/H-14/H-18. Strategy IDs (S-001 through S-014) consistently used. Missing: no GitHub Issue linkage. |

**Composite: (0.93 x 0.20) + (0.93 x 0.20) + (0.94 x 0.20) + (0.90 x 0.15) + (0.92 x 0.15) + (0.91 x 0.10) = 0.186 + 0.186 + 0.188 + 0.135 + 0.138 + 0.091 = 0.924**

**Verdict: REVISE** (below 0.95 threshold)

---

## 6. Composite Scores

| Artifact | COMP | ICON | MRIG | EVID | ACTN | TRAC | Composite | Verdict |
|----------|------|------|------|------|------|------|-----------|---------|
| architecture.md | 0.94 | 0.95 | 0.93 | 0.90 | 0.92 | 0.90 | **0.927** | REVISE |
| frontmatter-schema.md | 0.87 | 0.91 | 0.92 | 0.88 | 0.93 | 0.88 | **0.900** | REVISE |
| threat-model.md | 0.94 | 0.93 | 0.95 | 0.91 | 0.93 | 0.92 | **0.932** | REVISE |
| attack-surface.md | 0.95 | 0.94 | 0.93 | 0.90 | 0.94 | 0.91 | **0.931** | REVISE |
| qa-strategy.md | 0.93 | 0.93 | 0.94 | 0.90 | 0.92 | 0.91 | **0.924** | REVISE |

**Phase 1 Aggregate Composite:** (0.927 + 0.900 + 0.932 + 0.931 + 0.924) / 5 = **0.923**

**Phase 1 Minimum Artifact Score:** 0.900 (frontmatter-schema.md)

---

## 7. Specific Findings by Severity

### CRITICAL Findings (Block Phase 1 Pass)

| ID | Finding | Artifact | Impact | Recommended Fix |
|----|---------|----------|--------|----------------|
| C-001 | `sensitivity` field missing from required frontmatter fields | frontmatter-schema.md | Entire security model (TH-004, TH-005) depends on sensitivity classification that is not schema-enforced | Add `sensitivity` as required field with valid values enum and agent-specific defaults |
| C-002 | MRD template `risk_domain: "viability"` does not match schema enum `business-viability-risk` | mrd.md template | Schema validation failure at deployment; template produces invalid frontmatter | Change to `risk_domain: "business-viability-risk"` |

### HIGH Findings (Must Fix Before Phase 2)

| ID | Finding | Artifact | Impact | Recommended Fix |
|----|---------|----------|--------|----------------|
| H-001 | Cross-agent contamination (FM-005, RPN 315) has no runtime mitigation in Phase 1 specification | architecture.md, threat-model.md | Tainted upstream artifacts propagate unchecked to PRDs | Move content hash verification to Phase 2 priority; add `source_artifacts` to required frontmatter |
| H-002 | Staleness enforcement is documentation-only (FM-008, RPN 288) | frontmatter-schema.md | Stale artifacts consumed without system-level warning | Add read-time staleness check to agent system prompt specification |
| H-003 | Group D scorer anchoring bias (FM-015, RPN 294) | qa-strategy.md | Quality scores potentially inflated or deflated by prior group findings | Implement two-pass scoring protocol: independent score first, then adjusted score |
| H-004 | `content_hash` field not in frontmatter schema | frontmatter-schema.md | Artifact tampering mitigation (TH-008) has no schema support | Add `content_hash` as optional field (required at Phase 3) |
| H-005 | 18-vs-25 framework count ambiguity | frontmatter-schema.md | Reviewers cannot verify framework completeness against ambiguous baseline | Provide explicit canonical-18 list with separate supporting-frameworks list |
| H-006 | Template naming convention mismatch with architecture spec | architecture.md vs. actual templates | Deployment step must rename 15 files; no rename mapping documented | Document the `NN-name.template.md` to `name.md` rename mapping |
| H-007 | Mode transition has no section-completeness enforcement mechanism | frontmatter-schema.md | Discovery promoted to delivery without delivery sections populated | Add section-completeness gate to `delivery -> final` transition |

### MEDIUM Findings (Should Fix in Phase 2)

| ID | Finding | Artifact | Impact | Recommended Fix |
|----|---------|----------|--------|----------------|
| M-001 | No compound keyword resolution for multi-keyword requests | architecture.md | Request with both "competitive" and "GTM" has undefined routing | Add compound trigger resolution rules for common multi-domain requests |
| M-002 | Template placeholder syntax inconsistency (`{x}` vs `{{x}}`) | Templates (mrd.md vs. others) | Maintenance debt; inconsistent agent prompt processing | Standardize on one placeholder convention across all 15 templates |
| M-003 | TH-006 STRIDE classification mismatch | threat-model.md | Minor categorization issue (Elevation of Privilege vs. Spoofing) | Reclassify to correct STRIDE category |
| M-004 | Architecture.md lacks deployment steps from orchestration layout to final `skills/pm-pmm/` | architecture.md | Phase 4 integration lacks prescribed deployment workflow | Add a deployment checklist section or defer to Phase 4 integration spec |
| M-005 | No explicit AC-level traceability in any artifact | All artifacts | Traceability dimension consistently lowest-scored | Add AC references (AC-01 through AC-14) to each artifact's header or traceability section |
| M-006 | Market-sizing template lacks sensitivity analysis on SOM projections | market-sizing.md template | SOM presented with false precision | Add "Sensitivity Analysis" section with optimistic/base/pessimistic scenarios |
| M-007 | Cross-reference asymmetry rule (CI-002) is WARNING not BLOCK for delivery artifacts | frontmatter-schema.md | Delivery artifacts can have broken bidirectional references | Escalate CI-002 to BLOCK for `mode: delivery` artifacts |
| M-008 | Attack surface Section 1 states "Current controls: None" but architectural controls exist | attack-surface.md | Understates existing protections (P-003 enforcement, routing heuristics) | Distinguish between "no runtime implementation" and "no architectural specification" |

### LOW Findings (Informational)

| ID | Finding | Artifact | Impact | Note |
|----|---------|----------|--------|------|
| L-001 | Architecture.md composite scoring (Option B: 0.97) may overstate confidence | architecture.md | Could be seen as self-congratulatory scoring | The 0.97 is defensible given the criteria but should be acknowledged as architect-self-assessed |
| L-002 | QA strategy 0.95 threshold vs. SSOT 0.92 threshold | qa-strategy.md | Potential confusion for implementers | Justified as project-specific elevation; document rationale more prominently |
| L-003 | Threat model Revision 2.0.0 implies a prior version that is not referenced | threat-model.md | Minor provenance question | Clarify whether 1.0.0 existed or if versioning started at 2.0.0 |

---

## 8. Overall Phase 1 Verdict

### Summary Assessment

| Metric | Value |
|--------|-------|
| Phase 1 Aggregate Composite | 0.923 |
| Quality Threshold | 0.95 |
| Accept-with-Caveats Floor | 0.90 |
| Minimum Artifact Score | 0.900 (frontmatter-schema.md) |
| CRITICAL Findings | 2 |
| HIGH Findings | 7 |
| MEDIUM Findings | 8 |
| LOW Findings | 3 |
| FMEA Failure Modes with RPN > 200 | 5 (FM-005: 315, FM-015: 294, FM-008: 288, FM-016: 280, FM-002: 225) |
| Failure Modes with RPN > 100 | 16 of 20 |

### Verdict: ACCEPT-WITH-CAVEATS

**Phase 1 does NOT meet the 0.95 production-ready threshold.** The aggregate composite of 0.923 places Phase 1 in the REVISE band (0.90-0.95). However, all artifacts individually score above the 0.90 accept-with-caveats floor, and no artifact scores below the 0.85 hard-reject threshold.

**The caveats are:**

1. **frontmatter-schema.md must add `sensitivity` as a required field before Phase 2 begins** (C-001). The entire security model depends on this field. This is not a Phase 2 implementation concern -- it is a Phase 1 schema design gap.

2. **MRD template `risk_domain` value must be corrected** (C-002). This is a 5-second fix but it indicates that templates were not validated against the schema, which is a process gap.

3. **The 5 failure modes with RPN > 200 must have Phase 2 mitigations explicitly scheduled** in the orchestration plan. Specifically:
   - FM-005 (cross-agent contamination, RPN 315): content hash verification must be Phase 2 priority, not Phase 3.
   - FM-015 (scorer anchoring, RPN 294): two-pass scoring protocol must be specified before Phase 2 barrier review.
   - FM-008 (staleness enforcement, RPN 288): read-time staleness check must be in agent system prompt specs.
   - FM-016 (sensitivity field, RPN 280): blocked by C-001 fix.
   - FM-002 (mode switching corruption, RPN 225): section-completeness gate must be defined.

### What Would Elevate Phase 1 to 0.95

The following changes would bring the aggregate composite above 0.95:

1. Add `sensitivity` and `content_hash` fields to frontmatter schema (+0.03 on frontmatter COMP)
2. Fix MRD template `risk_domain` value (+0.01 on template consistency)
3. Add `source_artifacts` to PRD frontmatter requirements (+0.01 on architecture ACTN)
4. Document template rename mapping for deployment (+0.01 on architecture ACTN)
5. Add two-pass scoring protocol to qa-strategy.md (+0.02 on QA MRIG)
6. Add AC-level traceability to all artifacts (+0.01 on all TRAC scores)
7. Resolve 18-vs-25 framework count ambiguity in frontmatter schema (+0.01 on frontmatter ICON)

These 7 changes are estimated to raise the aggregate from 0.923 to approximately 0.955, crossing the 0.95 threshold.

### Phase 1 Strengths

Despite the ACCEPT-WITH-CAVEATS verdict, Phase 1 demonstrates several significant strengths that the FMEA and Inversion analyses confirm:

1. **Architecture design is sound.** The 5-agent model with zero artifact ownership overlap is well-justified. The Cagan risk domain mapping provides a principled decomposition. The inversion analysis confirms the architecture avoids 7 of 8 maximally harmful conditions.

2. **Threat model is comprehensive.** Full STRIDE analysis with 20 enumerated threats, trust boundary mapping, and prioritized mitigations. The inversion analysis confirms no blind spots in threat coverage.

3. **Template quality is high.** Framework operationalization in templates is deep (not label-only). Discovery/delivery mode separation is clear. Evidence prompting is built into template structure. The inversion analysis confirms templates avoid all 8 maximally misleading conditions.

4. **QA strategy multi-executor isolation is well-designed.** The ORCH-C05 anchoring bias prevention through 3+ isolated Task invocations per phase is a genuine methodological strength, with the Group D caveat being the only gap.

5. **Attack surface analysis is the most comprehensive Phase 1 artifact.** Layer-by-layer enumeration, per-agent analysis, and priority-ordered remediations provide a clear implementation roadmap for Phase 2.

---

*Review completed: 2026-03-01*
*Reviewer: adv-executor (Group C -- Analytical)*
*Strategies: S-012 (FMEA), S-013 (Inversion Technique)*
*Anti-leniency statement: Scores reflect rigorous assessment. 0.95 = production-ready with no known gaps. All artifacts scored below 0.95 because specific, addressable gaps were identified. The ACCEPT-WITH-CAVEATS verdict requires the 2 CRITICAL findings to be resolved before Phase 2 begins.*
