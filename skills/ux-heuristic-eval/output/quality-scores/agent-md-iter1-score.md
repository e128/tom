# Quality Score: ux-heuristic-evaluator.md (iter1)
Date: 2026-03-04
Artifact: skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.md
Companion: skills/ux-heuristic-eval/agents/ux-heuristic-evaluator.governance.yaml
Scorer: adv-scorer (S-014 LLM-as-Judge)
Criticality: C4
Quality Gate Threshold: 0.95 (C4)

---

## Dimension Scores

| Dimension | Weight | Score | Weighted | Evidence Summary |
|-----------|--------|-------|----------|-----------------|
| Completeness | 0.20 | 0.83 | 0.166 | All 7 XML sections present; H-34 required governance fields present; stub governance note + missing AD-M-010 allowed_tools + missing ET-M-001 reasoning_effort deduct |
| Internal Consistency | 0.20 | 0.78 | 0.156 | Tool tier T3 matches frontmatter; cognitive mode consistent across files; hexagonal dependency rule violated in `<guardrails>` (tool name "Task tool" used 4x in domain-layer section); Bash tool in frontmatter not described in `<capabilities>` prose |
| Methodological Rigor | 0.20 | 0.85 | 0.170 | Nielsen's 10 heuristics accurately named and numbered; severity 0-4 scale correct; AI supplement heuristics (AI-1/AI-2/AI-3) positioned as quasi-canonical Nielsen additions when they are internal framework constructs; single-evaluator limitation correctly disclosed |
| Evidence Quality | 0.15 | 0.80 | 0.120 | Nielsen (1994, rev. 2020) reference accurate; constitutional principle citations accurate; synthesis-validation.md referenced without existence verification; AI-interaction heuristic supplements presented without external citation; stub governance an honest disclosure but signals unclosed standards gaps |
| Actionability | 0.15 | 0.90 | 0.135 | 5-step workflow with clear per-step instructions; finding format fully templated; escalation conditions specific and measurable; on-send YAML schema complete; self-review checklist (6 items) explicit; degraded mode protocol explicit |
| Traceability | 0.10 | 0.75 | 0.075 | PROJ-022 and SSOT references present in footer; constitutional triplet traceable; no explicit AD-M-xxx traceability citations; hexagonal dependency violation not acknowledged; EPIC-002 deferral signals incomplete standard coverage |

## Weighted Composite: 0.822

## Verdict: REVISE

Score 0.822 is below the C4 threshold of 0.95 and below the general pass threshold of 0.92.
Three dimensions score below 0.85, indicating substantive revision is required before this
agent definition can be considered production-quality for C4 deployment.

---

## Findings (ranked by impact)

### Finding 1 — Hexagonal Dependency Rule Violated in `<guardrails>` Section [Internal Consistency, HIGH]

**Standard:** agent-development-standards.md hexagonal dependency rule: "Domain-layer sections (`<identity>`, `<purpose>`, `<methodology>`, `<guardrails>`) MUST NOT reference specific tool names."

**Evidence:** The `<guardrails>` section references the specific tool name "Task tool" in four locations:
- Line 315: "P-003 VIOLATION: NEVER spawn sub-agents or use the Task tool"
- Line 344: "1. No Task tool invocations -- this agent does NOT use the Task tool"
- Line 346: "2. No agent delegation -- this agent does NOT instruct the orchestrator to invoke other agents on its behalf"
- Line 352: "'P-003 VIOLATION: ux-heuristic-evaluator attempted to spawn a subagent. This agent is a worker and MUST NOT invoke other agents.'"

**Impact:** Violates the hexagonal dependency rule which exists to prevent domain-layer coupling to specific infrastructure tool names. The `<capabilities>` section (port layer) is the correct location for tool name references. The domain layer should describe behavior intent: "Does NOT delegate to other agents" rather than "Does NOT use the Task tool".

**Fix:** In `<guardrails>`, replace tool-name references with behavioral descriptions. E.g., "NEVER delegate work to other agents or spawn sub-processes" instead of "NEVER ... use the Task tool". Move P-003 runtime self-check language to `<capabilities>` section or rephrase without tool names.

---

### Finding 2 — Governance Stub Note Signals Deferred Standard Compliance [Completeness + Traceability, HIGH]

**Standard:** H-34 requires governance files to be validated against `docs/schemas/agent-governance-v1.schema.json`. AD-M-010 requires `capabilities.allowed_tools` declaration. ET-M-001 requires `reasoning_effort` declaration.

**Evidence:** governance.yaml line 4: "# STUB: Minimal governance for PROJ-022 Wave 1. Full implementation in EPIC-002." Three specific gaps from this stub approach:
1. `capabilities.allowed_tools` field is absent — only `output_formats` is declared. Per AD-M-010, research/documentation agents using Context7 SHOULD declare MCP tool usage in `capabilities.allowed_tools`.
2. `reasoning_effort` field is absent — ET-M-001 states agents SHOULD declare reasoning_effort aligned to criticality. A haiku-model systematic agent producing C2+ deliverables should at minimum declare `default` or `medium`.
3. The stub comment itself introduces technical debt that signals the governance file is not at full production quality.

**Fix:** Remove the stub comment and implement the deferred fields. Add `capabilities.allowed_tools` listing the 9 declared tools plus MCP tools. Add `reasoning_effort: default` (appropriate for systematic/haiku validation agent). Confirm schema validation passes against `docs/schemas/agent-governance-v1.schema.json`.

---

### Finding 3 — AI-Interaction Heuristic Supplements Lack External Citation [Evidence Quality + Methodological Rigor, MEDIUM]

**Standard:** P-022 (no deception) + P-011 (evidence-based claims). Every claim about methodology should be traceable to a source.

**Evidence:** The agent's `<identity>` section (line 40-41) claims "AI-interaction heuristic supplements (Transparency, Controllability, Error Recovery)" as if they are canonical extensions to Nielsen's framework. The `<methodology>` section (lines 141-148) presents these as `[AI-SUPPLEMENT]` heuristics labeled AI-1, AI-2, AI-3. However:
- Nielsen's 2020 revision of the 10 heuristics updated language and examples but did not add "AI-interaction supplement" heuristics with these exact names.
- The source for these three AI heuristics is not cited — they appear to be internal framework constructs presented as if externally validated methodology.
- A user or downstream agent consuming this evaluation output would have no way to verify AI-1/AI-2/AI-3 against a published standard.

**Fix:** Add an explicit source attribution for the AI-interaction heuristics. Options: (a) cite a specific published framework (e.g., Ben Shneiderman's 8 Golden Rules, Google PAIR Guidebook, IBM AI Fairness 360 heuristics) if one matches; (b) explicitly label these as "internal Jerry /user-experience skill AI supplement heuristics" so P-022 is satisfied; (c) remove them and route AI-specific evaluation to a dedicated AI heuristics agent. The current framing implies external validation that doesn't exist.

---

### Finding 4 — Missing `capabilities.allowed_tools` in Governance vs. Frontmatter Tool Declarations [Completeness, MEDIUM]

**Standard:** AD-M-010: "New agents SHOULD declare MCP tool usage in `capabilities.allowed_tools`." T3 constraint: "T3+ agents MUST declare citation guardrails."

**Evidence:** The frontmatter declares 8 tools (Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch) plus 2 MCP tools via `mcpServers`. The governance.yaml `capabilities` block contains only `forbidden_actions`, `forbidden_action_format`, and `output_formats` — no `allowed_tools` list. This creates a completeness gap between the runtime tool declaration (frontmatter) and the governance-layer tool declaration (governance.yaml). Additionally, as a T3 agent, the T3 constraint requires citation guardrails; `output_filtering` includes `all_claims_must_have_evidence` but not an explicit citation guardrail requiring source attribution for external content fetched via WebSearch/WebFetch.

**Fix:** Add `capabilities.allowed_tools` to governance.yaml listing all 8 frontmatter tools plus the 2 MCP tool operations. Add an explicit citation guardrail to `guardrails.output_filtering`: `"external_content_must_cite_source"` or similar.

---

### Finding 5 — Bash Tool in Frontmatter Not Described in `<capabilities>` Section [Internal Consistency, LOW-MEDIUM]

**Standard:** The `<capabilities>` section should accurately reflect all tools the agent uses and how they are used.

**Evidence:** The frontmatter declares `Bash` as an available tool (line 18). The `<capabilities>` section describes five capability categories: Read, Write/Edit, Glob/Grep (search codebase), WebSearch/WebFetch, and Context7. There is no mention of Bash or any use case that would require shell command execution. Given this is a systematic evaluation agent producing markdown reports, Bash appears unnecessary.

**Two possible resolutions:**
- If Bash is not needed: Remove it from frontmatter tools. This would reduce the tool tier from T3 (T2 + external) to T2-adjacent (or remain T3 for WebSearch/WebFetch), and the governance.yaml comment about "STUB" would also become a blocker for accurate tool tier declaration.
- If Bash has a legitimate use case: Document it in `<capabilities>` with the specific shell operations used (e.g., "Execute Bash to check file existence before writing output").

**Fix:** Either remove Bash from frontmatter tools (if unused) or document its use case in `<capabilities>`. The current state is an unexplained tool declaration.

---

## Leniency Bias Check
- [x] Each dimension scored independently before computing composite
- [x] Evidence documented for each score — specific line numbers cited
- [x] Uncertain scores resolved downward (Completeness considered 0.87, resolved to 0.83; Internal Consistency considered 0.82, resolved to 0.78; Traceability considered 0.80, resolved to 0.75)
- [x] First-draft / Wave 1 calibration considered — stub governance and deferred fields are characteristic of first-draft work
- [x] No dimension scored above 0.95 — highest is Actionability at 0.90, justified by explicit 5-step workflow with templated outputs

## Score Summary

| Metric | Value |
|--------|-------|
| **Weighted Composite** | 0.822 |
| **C4 Threshold** | 0.95 |
| **General Threshold (H-13)** | 0.92 |
| **Verdict** | REVISE |
| **Gap to C4 Threshold** | 0.128 |
| **Gap to H-13 Threshold** | 0.098 |
| **Weakest Dimension** | Traceability (0.75) |
| **Strongest Dimension** | Actionability (0.90) |
| **Strategy Findings Incorporated** | No (standalone scoring) |

## Priority Revision Roadmap

| Priority | Finding | Dimension Impact | Estimated Score Gain |
|----------|---------|-----------------|---------------------|
| 1 | Fix hexagonal dependency rule violation in `<guardrails>` (Finding 1) | Internal Consistency +0.08-0.10 | ~+0.016-0.020 composite |
| 2 | Complete governance.yaml stub (Finding 2) — add allowed_tools, reasoning_effort, remove stub comment | Completeness +0.05, Traceability +0.07 | ~+0.017 composite |
| 3 | Add external citation or honest internal labeling for AI-interaction heuristics (Finding 3) | Evidence Quality +0.06, Methodological Rigor +0.04 | ~+0.015 composite |
| 4 | Add T3 citation guardrail to governance output_filtering (Finding 4) | Completeness +0.02, Traceability +0.03 | ~+0.007 composite |
| 5 | Resolve Bash tool declaration (Finding 5) | Internal Consistency +0.03 | ~+0.006 composite |

**Projected composite after all revisions:** ~0.822 + 0.061 = ~0.883 (still below 0.95; additional depth work needed to reach C4 threshold)

**To reach 0.95:** Beyond these 5 findings, the agent definition would benefit from:
- Explicit AD-M-xxx traceability citations in the methodology section (Traceability +0.10)
- Addition of `enforcement` quality tier details in governance (Completeness +0.03)
- Verification that `synthesis-validation.md` exists and is correctly referenced (Evidence Quality +0.03)
- `reasoning_effort` documentation with justification for haiku model choice in systematic evaluation context (Internal Consistency, Methodological Rigor +0.02)
