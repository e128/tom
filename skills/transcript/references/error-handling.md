# Error State Structures and Recovery

> Reference documentation for transcript skill error handling. Loaded on demand from SKILL.md.
> Covers: Error State Structures (F-002), State Passing Error Handling, State Recovery Scenarios (F-003).

---

## Error State Structures (F-002)

> **PURPOSE:** Document how agents communicate errors through state keys.
> Enables downstream agents to detect and handle failures gracefully.

### Error State Schema

**When an agent encounters an error, it MUST populate error-specific fields in its output state key:**

```yaml
{agent}_output:
  # === Standard Error Fields (ALL agents MUST include) ===
  status: string                        # "success" | "partial" | "failed"
  errors: string[]                      # Fatal errors that halted execution
  warnings: string[]                    # Non-fatal issues that may affect quality

  # === Error Recovery Metadata ===
  recovery_possible: boolean            # Can this error be recovered from?
  recovery_command: string | null       # CLI command to retry/resume
  recovery_instructions: string | null  # Human-readable recovery steps

  # === Agent-Specific Error Context ===
  error_context: dict | null            # Additional diagnostic information
```

### Error State Examples by Agent

**ts-parser Error (Python Parser Failure):**

```yaml
ts_parser_output:
  status: "partial"                     # Fallback succeeded, but not preferred path
  canonical_json_path: "/path/to/canonical-transcript.json"
  index_json_path: "/path/to/index.json"
  chunks_dir: "/path/to/chunks/"
  chunk_count: 3

  # Error tracking
  errors:
    - "Python VTT parser failed: UnicodeDecodeError at line 42"
  warnings:
    - "Fallback to LLM parsing - increased cost and latency"

  # Recovery info
  fallback_triggered: true
  recovery_possible: false              # Already recovered via fallback
  recovery_instructions: "LLM fallback completed successfully. No action required."

  # Diagnostic context
  error_context:
    python_error_type: "UnicodeDecodeError"
    failed_encoding: "utf-8"
    attempted_fallback_encodings: ["windows-1252", "iso-8859-1"]
    fallback_method: "llm"
    fallback_model: "sonnet"
```

---

**ts-extractor Error (Context Overflow):**

```yaml
ts_extractor_output:
  status: "failed"                      # Cannot proceed
  extraction_report_path: null          # No output generated

  # Fatal error
  errors:
    - "Context window exceeded: chunk-042.json is 45,000 tokens (limit: 35,000)"
    - "Cannot process chunk without splitting"

  warnings: []

  # Recovery info
  recovery_possible: true
  recovery_command: "uv run tom transcript parse <file> --chunk-target-tokens 15000"
  recovery_instructions: >
    Re-run parsing with smaller chunk size to prevent context overflow.
    Use --chunk-target-tokens 15000 (down from default 18000) to reduce chunk size.

  # Diagnostic context
  error_context:
    failed_chunk_id: "chunk-042"
    failed_chunk_tokens: 45000
    chunk_token_limit: 35000
    suggestion: "Lower --chunk-target-tokens parameter"
```

---

**ts-formatter Error (File Write Failure):**

```yaml
ts_formatter_output:
  status: "failed"
  packet_path: "/output/transcript-meeting-001/"  # Directory created but incomplete

  # Partial completion tracking
  files_created:
    - "00-index.md"
    - "01-summary.md"
    - "02-transcript.md"
  files_failed:
    - "03-speakers.md"
    - "04-action-items.md"
    - "05-decisions.md"
    - "06-questions.md"
    - "07-topics.md"

  # Fatal error
  errors:
    - "IOError: Permission denied writing to /output/transcript-meeting-001/03-speakers.md"
  warnings: []

  # Recovery info
  recovery_possible: true
  recovery_command: "chmod 755 /output/transcript-meeting-001/ && /transcript resume --from formatting"
  recovery_instructions: >
    Fix directory permissions and resume formatting phase.
    Existing files (00-02) will be skipped if valid.

  # Diagnostic context
  error_context:
    permission_error_path: "/output/transcript-meeting-001/03-speakers.md"
    directory_permissions: "dr-xr-xr-x"
    required_permissions: "drwxr-xr-x"
```

---

**ts-mindmap-mermaid Error (Syntax Validation Failure):**

```yaml
ts_mindmap_output:
  enabled: true
  format_requested: "both"

  # Mermaid failed
  mermaid:
    path: "/output/08-mindmap/mindmap.mmd"  # File created but invalid
    status: "failed"
    error_message: "Mermaid syntax validation failed: Invalid node syntax at line 12"
    topic_count: 0
    deep_link_count: 0
    syntax_validated: false

  # ASCII succeeded
  ascii:
    path: "/output/08-mindmap/mindmap.ascii.txt"
    status: "complete"
    error_message: null
    topic_count: 47
    max_line_width: 79
    box_drawing_valid: true

  # Overall status
  overall_status: "partial"             # ASCII succeeded, Mermaid failed
  errors:
    - "Mermaid mindmap generation failed: Syntax error (markdown link in node)"
  warnings:
    - "Mermaid mindmap unavailable - ASCII mindmap generated successfully"

  # Recovery info
  recovery_possible: true
  regeneration_command: "uv run tom transcript mindmap --format mermaid --packet-path /output/"
  recovery_instructions: >
    Mermaid syntax error likely caused by markdown links in node text.
    The ts-mindmap-mermaid agent uses plain text ONLY in nodes per ADR-003 Section 5.3.
    ASCII mindmap is valid and can be used. To retry Mermaid generation:
    1. Review deep link reference block format
    2. Ensure no markdown syntax in topic text
    3. Run regeneration command above
```

---

**quality_output Error (Quality Gate Failure):**

```yaml
quality_output:
  quality_score: 0.68                   # Below threshold
  passed: false                         # Failed quality gate

  # Quality failures
  issues:
    - "T-001: Missing timestamps in 23% of segments"
    - "T-004: Low citation coverage (42% of extractions lack source anchors)"
    - "T-006: Token limit exceeded in 02-transcript-part-003.md (37,500 tokens)"
    - "MM-002: Mermaid mindmap missing deep link reference block"
  recommendations:
    - "Re-run parsing to fix timestamp gaps"
    - "Ensure ts-extractor includes segment_id in all citations"
    - "Re-run ts-formatter with stricter token splitting (31.5K soft limit)"
    - "Add deep link reference block to Mermaid mindmap per ADR-003 Section 5.3"

  # Criteria breakdown
  criteria_scores:
    "T-001": 0.77                       # Timestamp completeness
    "T-002": 0.95                       # Speaker attribution
    "T-003": 0.90                       # Segment ordering
    "T-004": 0.42                       # Citation coverage
    "T-005": 0.85                       # Confidence scoring
    "T-006": 0.50                       # Token budget compliance
    "MM-002": 0.00                      # Deep link reference block

  mindmap_criteria_applied: true
  artifacts_validated:
    - "00-index.md"
    - "01-summary.md"
    - "02-transcript-part-001.md"
    - "02-transcript-part-002.md"
    - "02-transcript-part-003.md"       # Failed token limit
    - "08-mindmap/mindmap.mmd"          # Missing reference block
    - "08-mindmap/mindmap.ascii.txt"    # Passed

  validation_timestamp: "2026-01-30T19:15:00Z"

  # Error tracking
  errors: []                            # No fatal errors, just quality failures
  warnings:
    - "Quality score 0.68 below threshold 0.90"
  status: "failed"

  # Recovery info
  recovery_possible: true
  recovery_command: null                # No single command - requires manual fixes
  recovery_instructions: >
    Address the 4 high-priority issues listed above and re-run ps-critic.
    Critical failures:
    1. T-004 (citation coverage) - Re-run ts-extractor with citation enforcement
    2. T-006 (token limits) - Re-run ts-formatter with --split-at-soft-limit flag
    3. MM-002 (deep links) - Re-run ts-mindmap-mermaid with reference block generation
```

---

### Propagated Error State (Multi-Agent Failure)

**When an error in one agent cascades to downstream agents:**

```yaml
# ts-parser fails completely (no fallback)
ts_parser_output:
  status: "failed"
  errors:
    - "Fatal: Input file is corrupted (invalid WebVTT structure)"
  recovery_possible: false
  recovery_instructions: "Provide a valid VTT, SRT, or TXT file"

# ts-extractor cannot proceed (missing input)
ts_extractor_output:
  status: "failed"
  errors:
    - "Missing required input: ts_parser_output.index_json_path"
    - "Cannot extract entities without parsed transcript"
  recovery_possible: false
  recovery_instructions: "Fix ts-parser errors before proceeding to extraction"

# ts-formatter skipped (dependency failure)
ts_formatter_output:
  status: "skipped"
  errors:
    - "Skipped due to upstream failure: ts-extractor.status = 'failed'"
  recovery_possible: false

# Pipeline halts completely
overall_pipeline_status: "failed"
failed_phase: "parsing"
recovery_instructions: "Fix input file and restart pipeline from beginning"
```

---

## State Passing Error Handling

### Error Propagation Rules

| Error Type | Behavior | State Impact |
|------------|----------|--------------|
| **Fatal Error** | Stop pipeline immediately | Set `status: "failed"` in current agent output |
| **Warning** | Continue pipeline | Add to `warnings[]` array, log in state |
| **Validation Failure** | Agent-specific decision | ts-parser: fallback to LLM; ts-extractor: skip low-confidence |
| **Missing Input** | Fatal error | Cannot proceed, report missing dependency |

### State Validation at Agent Boundaries

**Before ts-extractor:**
```yaml
REQUIRED from ts_parser_output:
  - index_json_path (must exist)
  - chunks_dir (must exist)
  - chunk_count > 0
  - validation_passed == true
```

**Before ts-formatter:**
```yaml
REQUIRED from ts_extractor_output:
  - extraction_report_path (must exist)
  - action_count == len(action_items) in report (INV-EXT-001)
  - decision_count == len(decisions) in report (INV-EXT-001)
  - question_count == len(questions) in report (INV-EXT-001)
```

**Before ps-critic:**
```yaml
REQUIRED from ts_formatter_output:
  - packet_path (directory must exist)
  - files_created (all files must exist)
  - all_files_under_limit == true (ADR-004 compliance)
```

### State Recovery Scenarios (F-003)

> **PURPOSE:** Provide comprehensive recovery procedures for all known failure modes.
> Enables self-service recovery without requiring expert intervention.

---

#### Scenario 1: Python Parser Failure (Encoding Issues)

**Symptom:**
```
Error: Python VTT parser failed: UnicodeDecodeError
Fallback: LLM parsing succeeded (increased cost)
```

**Root Cause:** VTT file uses non-UTF-8 encoding (e.g., Windows-1252, UTF-16).

**Recovery:**
```bash
# Option 1: Force LLM parsing from the start (skip Python parser)
uv run tom transcript parse meeting.vtt --force-llm

# Option 2: Convert file to UTF-8 first (preferred)
iconv -f windows-1252 -t utf-8 meeting.vtt > meeting-utf8.vtt
uv run tom transcript parse meeting-utf8.vtt
```

**Prevention:** Ensure VTT files are UTF-8 encoded before processing.

---

#### Scenario 2: Context Window Overflow (Chunk Too Large)

**Symptom:**
```
Error: Context window exceeded: chunk-042.json is 45,000 tokens (limit: 35,000)
Status: ts-extractor failed
```

**Root Cause:** Chunk exceeds Claude Code Read tool limit (25K tokens). Occurs when transcript has very long monologues.

**Recovery:**
```bash
# Re-parse with smaller chunk size (reduce from default 18K to 12K)
uv run tom transcript parse meeting.vtt --chunk-target-tokens 12000 --output-dir ./output-v2/

# Then continue from extraction phase
# (ts-parser will automatically trigger ts-extractor with new chunks)
```

**Prevention:** Use `--chunk-target-tokens 15000` for transcripts with long segments.

---

#### Scenario 3: File Write Permission Denied

**Symptom:**
```
Error: IOError: Permission denied writing to /output/transcript-meeting-001/03-speakers.md
Status: ts-formatter failed (partial completion)
Files created: 00-02
Files failed: 03-07
```

**Root Cause:** Output directory or parent directory has incorrect permissions.

**Recovery:**
```bash
# Fix directory permissions
chmod 755 /output/transcript-meeting-001/

# Resume formatting phase (will skip existing files 00-02)
uv run tom transcript resume --from formatting --packet-path /output/transcript-meeting-001/

# OR start fresh with correct permissions
chmod 755 /output/
uv run tom transcript parse meeting.vtt --output-dir /output/meeting-002/
```

**Prevention:** Ensure write permissions on output directory before invoking skill.

---

#### Scenario 4: Quality Gate Failure (Score < 0.90)

**Symptom:**
```
Quality Score: 0.68 (threshold: 0.90)
Status: quality_output.passed = false
Issues:
  - T-004: Low citation coverage (42%)
  - T-006: Token limit exceeded in 02-transcript-part-003.md
```

**Root Cause:** Extraction quality issues or token budget violations.

**Recovery:**

**Step 1: Review quality-review.md for specific issues**
```bash
cat /output/transcript-meeting-001/quality-review.md
```

**Step 2: Address each issue:**

**For T-004 (citation coverage):**
```bash
# Re-run extraction with stricter citation enforcement
uv run tom transcript resume --from extraction --enforce-citations
```

**For T-006 (token limits):**
```bash
# Re-run formatting with stricter splitting
uv run tom transcript resume --from formatting --split-at-soft-limit
```

**Step 3: Re-run quality review:**
```bash
uv run tom transcript resume --from quality-review
```

**Prevention:** Use `--model-extractor opus` for better extraction quality.

---

#### Scenario 5: Agent Timeout (Long Transcripts)

**Symptom:**
```
Error: Agent timeout after 300 seconds
Status: ts-extractor failed
Progress: Processed 8/15 chunks before timeout
```

**Root Cause:** Very large transcript (> 10,000 segments) exceeds default timeout.

**Recovery:**
```bash
# Increase timeout for extraction phase
uv run tom transcript parse meeting.vtt --extractor-timeout 600

# OR split transcript into smaller files
uv run python scripts/split_vtt.py meeting.vtt --max-duration 60  # 60 min chunks
uv run tom transcript parse meeting-part-001.vtt
uv run tom transcript parse meeting-part-002.vtt
# ... process each part separately
```

**Prevention:** For transcripts > 2 hours, consider splitting into segments.

---

#### Scenario 6: Partial Extraction (Low Confidence)

**Symptom:**
```
Warning: 45% of action items have confidence < 0.70
Status: ts-extractor succeeded (with warnings)
```

**Root Cause:** Ambiguous language, implicit action items, or poor transcript quality.

**Recovery:**
```bash
# Option 1: Use Opus model for better semantic understanding
uv run tom transcript parse meeting.vtt --model-extractor opus

# Option 2: Lower confidence threshold to include more entities
uv run tom transcript parse meeting.vtt --confidence-threshold 0.5

# Option 3: Review uncertain entities manually
cat /output/extraction-report.json | jq '.action_items[] | select(.confidence < 0.70)'
```

**Prevention:** Improve automatic transcription quality (better audio, less background noise).

---

#### Scenario 7: Mindmap Syntax Validation Failure

**Symptom:**
```
Error: Mermaid syntax validation failed: Invalid node syntax at line 12
Status: ts_mindmap_output.mermaid.status = "failed"
Status: ts_mindmap_output.ascii.status = "complete"
```

**Root Cause:** Markdown links used in Mermaid node text (ADR-003 limitation).

**Recovery:**
```bash
# Regenerate Mermaid mindmap with plain text enforcement
uv run tom transcript mindmap --format mermaid --packet-path /output/ --plain-text-only

# OR use ASCII mindmap (already succeeded)
cat /output/08-mindmap/mindmap.ascii.txt
```

**Prevention:** ts-mindmap-mermaid agent should strip markdown syntax before node generation.

---

#### Scenario 8: File Conflict (Output Already Exists)

**Symptom:**
```
Error: Output directory already exists: /output/transcript-meeting-001/
Conflict: 00-index.md, 01-summary.md (8 files total)
```

**Root Cause:** Previous run output not cleared before re-running.

**Recovery:**
```bash
# Option 1: Delete existing output (CAUTION: data loss)
rm -rf /output/transcript-meeting-001/
uv run tom transcript parse meeting.vtt --output-dir /output/transcript-meeting-001/

# Option 2: Use timestamped directory (recommended)
uv run tom transcript parse meeting.vtt --output-dir /output/transcript-meeting-001-$(date +%Y%m%d-%H%M%S)/

# Option 3: Merge mode (preserve existing files, update only changed)
uv run tom transcript parse meeting.vtt --output-dir /output/transcript-meeting-001/ --merge
```

**Prevention:** Use `--output-dir` with unique names or timestamps.

---

#### Scenario 9: Missing Dependencies (Python Modules)

**Symptom:**
```
Error: ModuleNotFoundError: No module named 'tiktoken'
Status: ts-parser failed (cannot perform token counting)
```

**Root Cause:** UV environment missing required Python dependencies.

**Recovery:**
```bash
# Sync UV dependencies
uv sync

# Verify installation
uv pip list | grep tiktoken

# Re-run parsing
uv run tom transcript parse meeting.vtt
```

**Prevention:** Run `uv sync` after pulling changes or switching branches.

---

#### Scenario 10: Orchestration State Corruption

**Symptom:**
```
Error: State key mismatch: ts_extractor_output.action_count (23) != len(action_items) in extraction-report.json (25)
Violation: INV-EXT-001 (entity count consistency)
Status: ts-formatter refused to proceed
```

**Root Cause:** Agent violated state schema invariant (likely a bug).

**Recovery:**
```bash
# Option 1: Regenerate extraction report from chunks
rm /output/extraction-report.json
uv run tom transcript resume --from extraction --packet-path /output/

# Option 2: Skip validation (CAUTION: may propagate errors)
uv run tom transcript resume --from formatting --skip-validation

# Option 3: Report bug with state dump
uv run tom transcript debug --dump-state /output/ > state-dump.json
# Attach state-dump.json to bug report
```

**Prevention:** This is an agent bug - report to maintainers with reproduction steps.

---
