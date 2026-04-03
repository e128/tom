# Agent Self-Critique Protocol

> Reference documentation for transcript skill agent self-critique. Loaded on demand from SKILL.md.
> Covers: Universal Self-Critique Checklist, Agent-Specific Self-Critique (F-004 Quantitative Thresholds), Self-Critique Failure Response.

---

## Agent Self-Critique Protocol

> **PURPOSE:** Pre-finalization quality checks per Tom Constitution P-001 (Truth and Accuracy)
> Each agent MUST perform self-critique before reporting completion.

### Universal Self-Critique Checklist (All Agents)

**Before reporting SUCCESS, EVERY agent must verify:**

```yaml
Constitutional Compliance:
  - [ ] P-001: Is my output accurate and truthful?
  - [ ] P-002: Have I persisted ALL required artifacts to files?
  - [ ] P-003: Did I avoid spawning recursive subagents?
  - [ ] P-004: Do all my extractions have citations to sources?
  - [ ] P-010: Is my state output consistent with actual results?
  - [ ] P-020: Did I respect user decisions (flags, paths)?
  - [ ] P-022: Have I been honest about limitations and errors?

Quality Gates:
  - [ ] Are my output files readable and valid (JSON/Markdown)?
  - [ ] Did I include all required metadata/frontmatter?
  - [ ] Are my reported counts/stats mathematically correct?
  - [ ] Did I document any warnings or errors in state?
```

### Agent-Specific Self-Critique

**ts-parser v2.0 (F-004 Quantitative Thresholds):**
```yaml
Pre-Completion Checks:
  - [ ] Format detection is accurate (VTT vs SRT vs plain)
  - [ ] If VTT: Did I successfully delegate to Python parser?
  - [ ] If Python failed: Did I fall back to LLM parsing?
  - [ ] Schema validation passed (validation_passed = true)
  - [ ] Chunk files created (chunk_count matches actual files)
  - [ ] All segments have sequential IDs (seg-001, seg-002, ...)
  - [ ] parse_metadata includes warnings/errors (if any)
  - [ ] No fabricated timestamps for plain text files (P-001)

Critical Validations (Quantitative):
  - [ ] canonical-transcript.json exists and is valid JSON (file size > 0 bytes)
  - [ ] index.json exists and matches chunk file count (schema_version == "1.0")
  - [ ] chunks/ directory contains all chunk-NNN.json files (count >= 1)
  - [ ] segment_count == sum of segments across all chunks (exact match, tolerance: 0)
  - [ ] Each chunk token count ≤ 35,000 tokens (hard limit per ADR-004)
  - [ ] Chunk token count target: 18,000 ± 2,000 tokens (target_tokens parameter)
  - [ ] Speaker count ≥ 1 (at least one speaker identified)
  - [ ] Total duration > 0 ms (for VTT/SRT formats; null acceptable for plain text)
  - [ ] Warning count ≤ 5 (excessive warnings indicate quality issues)
  - [ ] Error count == 0 for status "success" (no errors if claiming success)
```

**ts-extractor (F-004 Quantitative Thresholds):**
```yaml
Pre-Completion Checks:
  - [ ] INV-EXT-001: extraction_stats counts MATCH array lengths (exact, tolerance: 0)
        assert action_count == len(action_items)
        assert decision_count == len(decisions)
        assert question_count == len(questions)
        assert topic_count == len(topics)
        assert speaker_count == len(speakers)
  - [ ] INV-EXT-002: Questions are semantic, not syntactic (no rhetorical)
  - [ ] ALL extractions have citations (100% coverage, 0 missing citations)
  - [ ] ALL citations reference existing segments in input (100% validity)
  - [ ] Confidence scores are calibrated honestly (P-022)
  - [ ] No hallucinated entities (all sourced from transcript)

Critical Validations (Quantitative):
  - [ ] extraction-report.json exists and is valid JSON (file size > 1KB)
  - [ ] input_format = "chunked" (v2.0 requirement)
  - [ ] chunk_metadata.chunks_processed == expected count (exact match)
  - [ ] All entity arrays are non-null (may be empty, but not null)
  - [ ] High-confidence ratio ≥ 0.70 (70% of extractions with confidence ≥ 0.80)
  - [ ] Average confidence ≥ 0.75 (mean across all entities)
  - [ ] Citation coverage == 100% (every entity has at least one citation)
  - [ ] Tier 1 (rule-based) count ≥ 30% (at least 30% high-confidence extractions)
  - [ ] Tier 3 (LLM) confidence ≥ 0.60 (LLM extractions meet minimum threshold)
  - [ ] Extraction count bounds: 0 ≤ entity_count ≤ 1000 (sanity check)
  - [ ] Speaker count ≥ 1 (at least one speaker in transcript)
  - [ ] Topic count ≥ 1 (at least one topic identified)
```

**ts-formatter (F-004 Quantitative Thresholds):**
```yaml
Pre-Completion Checks:
  - [ ] ALL 8 core files created (00-index.md through 07-topics.md)
  - [ ] _anchors.json created with complete anchor registry
  - [ ] NO file exceeds 35K tokens (hard limit per ADR-004)
  - [ ] Split files have proper navigation (prev/next links)
  - [ ] All internal links resolve (no broken anchors, 100% resolution)
  - [ ] All entity files link to source segments (bidirectional, 100% coverage)
  - [ ] Schema version metadata in all frontmatter (PAT-005)
  - [ ] files_created list matches actual directory contents

Critical Validations (Quantitative):
  - [ ] packet_path directory exists (verified via os.path.exists)
  - [ ] total_tokens == sum of tokens across all files (exact match, tolerance: ±10)
  - [ ] all_files_under_limit == true (ALL files ≤ 35,000 tokens)
  - [ ] File token limits:
        - Soft limit: 31,500 tokens (split at this boundary if possible)
        - Hard limit: 35,000 tokens (MUST NOT exceed)
  - [ ] anchor_count > 0 (at least segment anchors exist)
  - [ ] backlink_count > 0 (at least one backlink per entity type)
  - [ ] File count: 8 ≤ files_created.length ≤ 20 (8 core + up to 12 split files)
  - [ ] Split file ratio ≤ 0.50 (no more than 50% of files are splits)
  - [ ] 00-index.md token count ≤ 5,000 (navigation hub must be concise)
  - [ ] 01-summary.md token count ≤ 8,000 (executive summary constraint)
  - [ ] _anchors.json size < 50KB (anchor registry should be compact)
  - [ ] Internal link resolution rate == 100% (no broken links tolerated)
  - [ ] Entity backlink coverage ≥ 95% (at least 95% of entities have source links)
```

**ts-mindmap-mermaid (F-004 Quantitative Thresholds):**
```yaml
Pre-Completion Checks:
  - [ ] Mermaid syntax is valid (mindmap keyword at start, line 1)
  - [ ] Root node uses ((double parentheses)) (line 2)
  - [ ] ALL nodes use plain text ONLY (no markdown links, 0 violations)
  - [ ] Deep link reference block appended as %% comments (present at end)
  - [ ] Indentation is consistent (2 spaces per level, 100% compliance)
  - [ ] Entity symbols are correct (no confusion between →, ?, !, ✓)
  - [ ] Topic overflow handled if > 50 topics (truncation with note)

Critical Validations (Quantitative):
  - [ ] 08-mindmap/mindmap.mmd exists (file size > 500 bytes)
  - [ ] status = "complete" in ts_mindmap_output
  - [ ] topic_count matches extraction report (exact match, tolerance: 0)
  - [ ] Topic count bounds: 1 ≤ topic_count ≤ 50 (overflow if > 50)
  - [ ] Deep link count > 0 (at least one deep link in reference block)
  - [ ] Deep link count ≤ topic_count * 3 (max 3 links per topic)
  - [ ] Syntax validation passed (no Mermaid parser errors)
  - [ ] File line count ≥ 10 (minimum viable mindmap structure)
  - [ ] Indentation depth ≤ 4 levels (hierarchy constraint per ADR-003)
  - [ ] Node text length ≤ 100 characters (readability constraint)
  - [ ] P-022: Documented syntax limitation (no markdown links in nodes)
```

**ts-mindmap-ascii (F-004 Quantitative Thresholds):**
```yaml
Pre-Completion Checks:
  - [ ] ALL lines are <= 80 characters (terminal compatibility, 100% compliance)
  - [ ] Box-drawing characters are valid UTF-8 (U+2500 block, no ASCII fallback)
  - [ ] Legend is present at bottom explaining symbols (minimum 4 lines)
  - [ ] Tree structure is visually balanced (no excessive left-skew)
  - [ ] Entity symbols match specification ([→], [?], [!], etc.)
  - [ ] No truncation artifacts (ellipsis applied correctly at 77 chars)

Critical Validations (Quantitative):
  - [ ] 08-mindmap/mindmap.ascii.txt exists (file size > 300 bytes)
  - [ ] status = "complete" in ts_mindmap_output
  - [ ] max_line_width <= 80 (hard constraint)
  - [ ] Typical line width: 60-75 characters (readability range)
  - [ ] box_drawing_valid == true (UTF-8 validation passed)
  - [ ] Topic count bounds: 1 ≤ topic_count ≤ 50 (same as Mermaid)
  - [ ] File line count ≥ 15 (minimum viable ASCII mindmap)
  - [ ] Legend line count == 4-6 lines (standard legend format)
  - [ ] Indentation step == 2 spaces (consistent with Mermaid)
  - [ ] Tree depth ≤ 4 levels (same hierarchy constraint as Mermaid)
  - [ ] Entity symbol count ≥ topic_count (at least one entity per topic)
```

**ps-critic (F-004 Quantitative Thresholds):**
```yaml
Pre-Completion Checks:
  - [ ] Quality score calculated correctly (0.0-1.0 range)
  - [ ] ALL validation criteria evaluated (minimum 15 criteria for full packet)
  - [ ] Mindmap criteria (MM-*, AM-*) applied if mindmaps present (8 additional criteria)
  - [ ] Issues list is actionable (specific, not vague; no generic "improve quality")
  - [ ] Recommendations are constructive (actionable, with commands/steps)
  - [ ] criteria_scores includes all evaluated criteria (no missing scores)
  - [ ] Passed/failed determination is honest (>= 0.90 threshold)

Critical Validations (Quantitative):
  - [ ] quality-review.md exists in packet directory (file size > 2KB)
  - [ ] artifacts_validated lists all checked files (count ≥ 8 for core packet)
  - [ ] quality_output.passed reflects actual score (passed ↔ score ≥ 0.90)
  - [ ] Quality score bounds: 0.0 ≤ quality_score ≤ 1.0
  - [ ] Passing threshold: quality_score ≥ 0.90 (hard requirement)
  - [ ] Criteria evaluation coverage: 100% (all applicable criteria scored)
  - [ ] Issue count ≤ 10 (excessive issues indicate systemic failure)
  - [ ] Recommendation count: 1-5 per issue (actionable, not overwhelming)
  - [ ] Per-criterion score range: 0.0 ≤ criterion_score ≤ 1.0
  - [ ] Aggregate score calculation: weighted average of criteria (verified)
  - [ ] Mindmap criteria count: +8 if Mermaid present, +8 if ASCII present
  - [ ] Total criteria evaluated: 15 (core) + 0-16 (mindmaps)
  - [ ] P-022: No inflated scores to avoid user feedback (honesty ≥ 0.95)
```

### Self-Critique Failure Response

**If ANY checklist item fails:**

1. **DO NOT report success**
2. **Document the failure** in agent output state
3. **Add to warnings[] or errors[]** as appropriate
4. **Set status to "failed" or "partial"** (not "complete")
5. **Include recovery instructions** if possible

---
